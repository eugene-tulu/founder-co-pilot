"""Crustdata REST client (x-api-version 2025-11-01) plus a retry-with-degraded helper.

Field names for live filters are discovered at runtime via the free autocomplete
endpoint; see discover.py. Offline mode serves fixtures so the pipeline is
fully demonstrable without keys.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

import httpx

from .config import Settings
from .tracing import log_tool


class CrustdataError(RuntimeError):
    pass


class CrustdataClient:
    BASE = "https://api.crustdata.com"
    API_VERSION = "2025-11-01"
    MAX_ATTEMPTS = 3

    def __init__(self, settings: Settings, tracing_on: bool, offline: bool = False) -> None:
        self.online = bool(settings.crustdata_api_key) and not offline
        self.tracing_on = tracing_on
        self._key = settings.crustdata_api_key
        self._cache_path = Path(settings.runs_dir) / "crustdata_cache.json"
        self._cache: dict[str, Any] = {}
        self.cache_hits = 0
        if self._cache_path.exists():
            try:
                self._cache = json.loads(self._cache_path.read_text())
            except Exception:
                self._cache = {}

    def _cache_key(self, path: str, payload: dict[str, Any]) -> str:
        blob = json.dumps({"path": path, "payload": payload}, sort_keys=True)
        return hashlib.sha1(blob.encode()).hexdigest()[:16]

    def _persist_cache(self) -> None:
        try:
            self._cache_path.parent.mkdir(parents=True, exist_ok=True)
            self._cache_path.write_text(json.dumps(self._cache, indent=1))
        except OSError:
            pass

    async def _post(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        key = self._cache_key(path, payload)
        if key in self._cache:
            self.cache_hits += 1
            log_tool(path, "cache-hit", cached_from=self._cache[key].get("_cached_from", "live"))
            return self._cache[key]
        if not self.online:
            raise CrustdataError("offline")
        headers = {
            "authorization": f"Bearer {self._key}",
            "content-type": "application/json",
            "x-api-version": self.API_VERSION,
        }
        last: Exception | None = None
        for attempt in range(self.MAX_ATTEMPTS):
            try:
                async with httpx.AsyncClient(timeout=30.0) as client:
                    resp = await client.post(f"{self.BASE}{path}", json=payload, headers=headers)
                if resp.status_code == 429:
                    raise CrustdataError("rate limited (429)")
                resp.raise_for_status()
                data = resp.json()
                if isinstance(data, dict) and data.get("error"):
                    if data["error"].get("type") == "insufficient_credits":
                        raise CrustdataError("insufficient credits")
                    raise CrustdataError(str(data["error"].get("message", "api error"))[:200])
                self._cache[key] = data
                self._persist_cache()
                log_tool(path, "ok", attempt=attempt)
                return data
            except CrustdataError:
                raise
            except Exception as exc:  # noqa: BLE001 - we retry every transport error
                last = exc
                log_tool(path, "error", attempt=attempt, error=str(exc)[:200])
                await asyncio.sleep(0.5 * (attempt + 1))
        raise CrustdataError(f"{path} failed after {self.MAX_ATTEMPTS} attempts: {last}")

    async def company_search(self, conditions: list[dict[str, Any]], limit: int = 25) -> dict[str, Any]:
        payload = {"filters": self._tree(conditions), "limit": limit}
        return await self._post("/company/search", payload)

    async def job_search(self, conditions: list[dict[str, Any]], limit: int = 25) -> dict[str, Any]:
        payload = {"filters": self._tree(conditions), "limit": limit}
        return await self._post("/job/search", payload)

    @staticmethod
    def _tree(conditions: list[dict[str, Any]]) -> dict[str, Any]:
        """Crustdata contract: filters is a single condition or an {"op","conditions"} tree."""
        if len(conditions) == 1:
            return conditions[0]
        return {"op": "and", "conditions": conditions}

    async def autocomplete(self, field: str, query: str) -> dict[str, Any]:
        """Free endpoint: resolve a human term to valid filter values."""
        try:
            return await self._post("/company/search/autocomplete", {"field": field, "query": query})
        except CrustdataError:
            return {}

    async def search_with_fallback(
        self, filters: list[dict[str, Any]], limit: int = 25
    ) -> tuple[dict[str, Any], bool]:
        """Try full search; on failure retry degraded (smaller limit). Returns (data, degraded)."""
        try:
            return await self.company_search(filters, limit=limit), False
        except CrustdataError:
            return await self.company_search(filters, limit=min(5, limit)), True
