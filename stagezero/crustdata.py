"""Crustdata REST client (x-api-version 2025-11-01) plus a retry-with-degraded helper.

Field names for live filters are discovered at runtime via the free autocomplete
endpoint; see discover.py. Offline mode serves fixtures so the pipeline is
fully demonstrable without keys.
"""
from __future__ import annotations

import asyncio
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

    async def _post(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
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
                log_tool(path, "ok", attempt=attempt)
                return resp.json()
            except Exception as exc:  # noqa: BLE001 - we retry every transport error
                last = exc
                log_tool(path, "error", attempt=attempt, error=str(exc)[:200])
                await asyncio.sleep(0.5 * (attempt + 1))
        raise CrustdataError(f"{path} failed after {self.MAX_ATTEMPTS} attempts: {last}")

    async def company_search(self, filters: list[dict[str, Any]], limit: int = 25) -> dict[str, Any]:
        payload = {"filters": filters, "limit": limit}
        return await self._post("/company/search", payload)

    async def job_search(self, filters: list[dict[str, Any]], limit: int = 25) -> dict[str, Any]:
        payload = {"filters": filters, "limit": limit}
        return await self._post("/job/search", payload)

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
