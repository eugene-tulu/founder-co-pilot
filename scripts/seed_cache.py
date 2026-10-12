#!/usr/bin/env python3
"""Seed the Crustdata response cache from runs that captured live responses.

Counts in run_state.json / validation_kit.json are real observations from live
API calls; this script rebuilds cache entries for those exact queries so reruns
reproduce the same evidence without spending credits again. Each entry records
the run it came from (_cached_from) so provenance stays honest.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "runs" / "crustdata_cache.json"


def tree(conditions: list[dict]) -> dict:
    if len(conditions) == 1:
        return conditions[0]
    return {"op": "and", "conditions": conditions}


def key(path: str, payload: dict) -> str:
    blob = json.dumps({"path": path, "payload": payload}, sort_keys=True)
    return hashlib.sha1(blob.encode()).hexdigest()[:16]


def main() -> int:
    cache: dict = {}
    if CACHE.exists():
        cache = json.loads(CACHE.read_text())
    added = 0
    for kit_path in sorted((ROOT / "runs").glob("*/validation_kit.json")):
        run_id = kit_path.parent.name
        kit = json.loads(kit_path.read_text())
        # Company-size evidence: one search per segment.
        for seg in kit.get("segments", []):
            payload = {"filters": tree(seg["icp_filters"]), "limit": 25}
            k = key("/company/search", payload)
            if k not in cache:
                cache[k] = {
                    "total_count": seg["company_count"],
                    "companies": [],
                    "_cached_from": run_id,
                }
                added += 1
        # Pain-signal evidence: job searches recorded in the kit.
        for ev in kit.get("evidence", []):
            if ev["source"] == "crustdata /job/search":
                payload = {"filters": tree(ev["query"]["filters"]), "limit": 25}
                k = key("/job/search", payload)
                if k not in cache:
                    cache[k] = {
                        "total_count": ev["result_count"],
                        "jobs": [],
                        "_cached_from": run_id,
                    }
                    added += 1
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, indent=1))
    print(f"seeded {added} cache entries ({len(cache)} total) -> {CACHE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
