import json
from pathlib import Path

from stagezero.pipeline import run_pipeline
from stagezero.stages.guardrail import check_claims
from stagezero.models import Evidence


def _settings(tmp_path: Path):
    from stagezero.config import Settings

    return Settings(
        neatlogs_api_key=None,
        llm_base_url=None,
        llm_api_key=None,
        llm_model="gpt-4o-mini",
        crustdata_api_key=None,
        runs_dir=str(tmp_path / "runs"),
        fail_stage=None,
        fail_times=0,
    )


def test_offline_end_to_end(tmp_path: Path):
    kit = __import__("asyncio").run(
        run_pipeline(_settings(tmp_path), "AI agent that chases unpaid invoices for independent consultants")
    )
    assert len(kit.segments) == 3
    assert kit.decision in {"proceed", "pivot", "kill"}
    assert all(len(s.questions) == 10 for s in kit.scripts)
    assert kit.experiment_plan and kit.kill_criteria
    run_dir = tmp_path / "runs" / kit.run_id
    assert (run_dir / "VALIDATION_KIT.md").exists()
    md = (run_dir / "VALIDATION_KIT.md").read_text()
    assert "Mom Test" in md and "evidence" in md.lower()
    state = json.loads((run_dir / "run_state.json").read_text())
    assert set(state["stages"]) == {"ingest", "plan", "discover", "analyze", "scriptkit"}


def test_guardrail_blocks_unsourced_numbers():
    evidence = [Evidence(id="ev-1", source="t", result_count=1284)]
    res = check_claims("We found 1284 companies but only 55 signals.", evidence)
    assert res.blocked == ["55"]
    ok = check_claims("We found 1284 companies.", evidence)
    assert ok.status == "PASS"


def test_failure_injection_recovers(tmp_path: Path):
    settings = _settings(tmp_path)
    settings = settings.__class__(**{**settings.__dict__, "fail_stage": "discover", "fail_times": 1})
    kit = __import__("asyncio").run(
        run_pipeline(settings, "AI agent that chases unpaid invoices for independent consultants")
    )
    assert kit.recovered_from_failure
    state = json.loads((tmp_path / "runs" / kit.run_id / "run_state.json").read_text())
    assert any("discover" in f["stage"] for f in state["failures"])


def test_resume_skips_completed_stages(tmp_path: Path):
    import asyncio

    asyncio.run(run_pipeline(_settings(tmp_path), "AI agent that chases unpaid invoices", run_id="fixed-run"))
    kit = asyncio.run(run_pipeline(_settings(tmp_path), "anything else", resume="fixed-run"))
    state = json.loads((tmp_path / "runs" / "fixed-run" / "run_state.json").read_text())
    assert state["resumed"] is True
    # ingest was re-derived from the original idea, not the new text
    assert kit.idea.idea_text == "AI agent that chases unpaid invoices"
