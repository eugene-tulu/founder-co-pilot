from __future__ import annotations

import json
import os
import time
import uuid
from pathlib import Path
from typing import Any, Callable

from . import tracing
from .config import Settings
from .crustdata import CrustdataClient
from .llm import LLM
from .models import Evidence, Hypothesis, Idea, InterviewQuestions, Segment, ValidationKit
from .stages import analyze, discover, guardrail, ingest, plan, report, scriptkit

PRICE_IN_PER_MTOK = float(os.environ.get("STAGEZERO_PRICE_IN_PER_MTOK", "3.0"))
PRICE_OUT_PER_MTOK = float(os.environ.get("STAGEZERO_PRICE_OUT_PER_MTOK", "15.0"))


class StageError(RuntimeError):
    pass


def _to_dict(obj: Any) -> Any:
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if isinstance(obj, dict):
        return {k: _to_dict(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_to_dict(v) for v in obj]
    return obj


class Pipeline:
    """Sequential, resumable, traced pipeline. State persists after every stage."""

    def __init__(self, settings: Settings, run_id: str, offline: bool) -> None:
        self.settings = settings
        self.run_id = run_id
        self.offline = offline
        self.run_dir = Path(settings.runs_dir) / run_id
        self.state_path = self.run_dir / "run_state.json"
        self.state: dict[str, Any] = {
            "run_id": run_id,
            "offline": offline,
            "stages": {},
            "stage_ms": {},
            "failures": [],
            "recovered_from_failure": False,
            "resumed": False,
        }
        self.llm = LLM(settings, tracing.is_enabled())
        self.crustdata = CrustdataClient(settings, tracing.is_enabled(), offline=offline)

    # ------------------------------------------------------------------ state
    def load(self) -> None:
        if self.state_path.exists():
            existing = json.loads(self.state_path.read_text())
            self.state = {**self.state, **existing, "resumed": True}

    def save(self) -> None:
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(json.dumps(self.state, indent=2, default=str))

    # ------------------------------------------------------------------ stages
    async def run_stage(self, name: str, fn: Callable, *args, **kwargs) -> Any:
        if name in self.state["stages"]:
            tracing.log_stage(name, "skipped-resume", run_id=self.run_id)
            return _dispatch(self.state["stages"][name])

        tracing.log_stage(name, "start", run_id=self.run_id)
        t0 = time.perf_counter()
        try:
            self._maybe_inject_failure(name)
            result = _to_dict(await fn(*args, **kwargs))
        except StageError as exc:
            tracing.log_stage(name, "failed", run_id=self.run_id, error=str(exc)[:200])
            self.state["failures"].append({"stage": name, "error": str(exc), "injected": True})
            self.state["recovered_from_failure"] = True
            t1 = time.perf_counter()
            result = _to_dict(await fn(*args, **kwargs))
            ms = int((time.perf_counter() - t1) * 1000)
            self.state["stages"][name] = result
            self.state["stage_ms"][name] = ms
            tracing.log_stage(name, "ok-after-recovery", run_id=self.run_id, duration_ms=ms)
            self.save()
            return _dispatch(result)

        ms = int((time.perf_counter() - t0) * 1000)
        self.state["stages"][name] = result
        self.state["stage_ms"][name] = ms
        tracing.log_stage(name, "ok", run_id=self.run_id, duration_ms=ms)
        self.save()
        return _dispatch(result)

    def _maybe_inject_failure(self, stage: str) -> None:
        """Optional chaos switch for demoing recovery: STAGEZERO_FAIL_AT / --fail-at."""
        if self.settings.fail_stage == stage:
            count = sum(1 for f in self.state["failures"] if f["stage"] == stage)
            if count < self.settings.fail_times:
                raise StageError(f"injected failure in '{stage}' (chaos switch on)")

    # ------------------------------------------------------------------ run
    async def run(self, idea_text: str) -> ValidationKit:
        with tracing.run_trace(self.run_id, idea_text, self.offline):
            idea = Idea(**await self.run_stage("ingest", ingest.parse_idea, idea_text, self.llm))

            hyps_raw = await self.run_stage("plan", plan.plan_hypotheses, idea, self.llm, self.crustdata)
            hypotheses = [Hypothesis(**h) for h in hyps_raw]

            disc = await self.run_stage(
                "discover", discover.discover_segments, idea, hypotheses, self.crustdata, self.offline
            )
            segments = [Segment(**s) for s in disc["segments"]]
            evidence = [Evidence(**e) for e in disc["evidence"]]
            # Scores are derived from evidence, so recompute them: a resumed run must
            # produce the same scores as the original run.
            analyze.score_segments(segments)
            if disc.get("recovered"):
                self.state["recovered_from_failure"] = True

            analysis = await self.run_stage(
                "analyze", analyze.analyze, idea, segments, evidence, self.llm
            )
            problem_statement, decision, rationale = (
                analysis["problem_statement"],
                analysis["decision"],
                analysis["rationale"],
            )

            problem_statement, gres, gnotes = await guardrail.enforce(
                problem_statement, evidence, self.llm, segments
            )
            tracing.log_guardrail(gres.status, run_id=self.run_id, blocked=gres.blocked)

            scripts_raw = await self.run_stage(
                "scriptkit", scriptkit.build_scripts, idea, segments, self.llm
            )
            scripts = [InterviewQuestions(**s) for s in scripts_raw]
            exp_plan, gates, kills = scriptkit.acq_stage_plan(idea.founder_stage)

            cost = (
                self.llm.prompt_tokens / 1e6 * PRICE_IN_PER_MTOK
                + self.llm.completion_tokens / 1e6 * PRICE_OUT_PER_MTOK
            )

            kit = ValidationKit(
                run_id=self.run_id,
                idea=idea,
                stage_diagnosis=report.STAGE_DIAGNOSIS,
                problem_statement=problem_statement,
                segments=segments,
                scripts=scripts,
                experiment_plan=exp_plan,
                graduation_gates=gates,
                kill_criteria=kills,
                decision=decision,
                guardrail_notes=gnotes or [f"guardrail {gres.status}"],
                evidence=evidence,
                recovered_from_failure=self.state["recovered_from_failure"],
                cost_usd=round(cost, 6),
            )
            self.state["llm"] = {
                "calls": self.llm.calls,
                "prompt_tokens": self.llm.prompt_tokens,
                "completion_tokens": self.llm.completion_tokens,
                "cost_usd": round(cost, 6),
            }
            self.state["decision"] = decision
            self.save()
            report.write_run_artifacts(kit, self.state, self.run_dir)
            return kit


def _dispatch(value: Any) -> Any:
    """Stored stage results come back as dicts; pass them through unchanged."""
    return value


async def run_pipeline(
    settings: Settings,
    idea_text: str,
    run_id: str | None = None,
    resume: str | None = None,
    demo: bool | None = None,
) -> ValidationKit:
    # demo=True forces offline fixture mode; None means "offline iff no keys".
    offline = (not settings.online) if demo is None else demo
    run_id = resume or run_id or f"run-{time.strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"
    tracing.init_tracing(settings)
    pipeline = Pipeline(settings, run_id, offline)
    if resume:
        pipeline.load()
    try:
        kit = await pipeline.run(idea_text)
    finally:
        tracing.finish()
    return kit
