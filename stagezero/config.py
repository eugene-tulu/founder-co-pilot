from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    neatlogs_api_key: str | None
    llm_base_url: str | None
    llm_api_key: str | None
    llm_model: str
    crustdata_api_key: str | None
    runs_dir: str
    fail_stage: str | None
    fail_times: int

    @property
    def online(self) -> bool:
        return bool(self.llm_api_key and self.crustdata_api_key)

    @classmethod
    def from_env(cls, runs_dir: str = "runs") -> "Settings":
        return cls(
            neatlogs_api_key=os.environ.get("NEATLOGS_API_KEY") or None,
            llm_base_url=os.environ.get("LLM_BASE_URL") or None,
            llm_api_key=os.environ.get("LLM_API_KEY") or None,
            llm_model=os.environ.get("LLM_MODEL", "gpt-4o-mini"),
            crustdata_api_key=os.environ.get("CRUSTDATA_API_KEY") or None,
            runs_dir=os.environ.get("STAGEZERO_RUNS_DIR", runs_dir),
            fail_stage=os.environ.get("STAGEZERO_FAIL_AT") or None,
            fail_times=int(os.environ.get("STAGEZERO_FAIL_TIMES", "1")),
        )
