"""neatlogs wiring. Tracing is optional: with no NEATLOGS_API_KEY everything still runs."""
from __future__ import annotations

import time
from contextlib import contextmanager
from typing import Iterator

import neatlogs

from .config import Settings

_enabled = False
_started = False


def init_tracing(settings: Settings) -> bool:
    """Initialise neatlogs once per process. Returns True when tracing is live."""
    global _enabled, _started
    if _started:
        return _enabled
    _started = True
    if not settings.neatlogs_api_key:
        return False
    try:
        neatlogs.init(api_key=settings.neatlogs_api_key, workflow_name="stagezero")
        _enabled = True
    except Exception:
        _enabled = False
    return _enabled


def is_enabled() -> bool:
    return _enabled


@contextmanager
def run_trace(run_id: str, idea: str, demo_mode: bool) -> Iterator[None]:
    """Group the whole pipeline as one WORKFLOW trace."""
    if _enabled:
        with neatlogs.trace(
            name=f"pipeline {run_id}", kind="WORKFLOW", run_id=run_id, idea=idea, demo_mode=demo_mode
        ):
            yield
    else:
        yield


def log_stage(stage: str, status: str, **attrs) -> None:
    if _enabled:
        neatlogs.log(
            "stage_end stage={stage} status={status}",
            level="info" if status == "ok" else "warning",
            stage=stage,
            status=status,
            **attrs,
        )


def log_tool(tool: str, status: str, **attrs) -> None:
    if _enabled:
        neatlogs.log(
            "tool_call tool={tool} status={status}",
            level="info" if status == "ok" else "warning",
            tool=tool,
            status=status,
            **attrs,
        )


def log_guardrail(status: str, **attrs) -> None:
    if _enabled:
        neatlogs.log(
            "provenance_guardrail status={status}",
            level="warning" if status != "PASS" else "info",
            status=status,
            **attrs,
        )


class StageTimer:
    def __init__(self) -> None:
        self.t0 = time.perf_counter()

    def ms(self) -> int:
        return int((time.perf_counter() - self.t0) * 1000)


def finish() -> None:
    if _enabled:
        neatlogs.flush()
        neatlogs.shutdown()
