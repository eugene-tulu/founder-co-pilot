from __future__ import annotations

from pathlib import Path

from ..models import ValidationKit

STAGE_DIAGNOSIS = (
    "Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; "
    "the goal is to get people to try your stuff for free. Graduation = people find it "
    "helpful unprompted."
)


def render_markdown(kit: ValidationKit) -> str:
    lines: list[str] = []
    lines.append(f"# StageZero validation kit — run {kit.run_id}")
    lines.append("")
    lines.append(f"**Idea:** {kit.idea.idea_text}")
    lines.append("")
    lines.append(f"**Stage diagnosis:** {kit.stage_diagnosis}")
    lines.append("")
    lines.append("## Problem statement")
    lines.append("")
    lines.append(kit.problem_statement)
    lines.append("")
    lines.append("## Customer segments (ranked)")
    lines.append("")
    lines.append("| # | Segment | Companies | Competitors | Pain signals | Priority |")
    lines.append("|---|---------|-----------|-------------|--------------|----------|")
    for i, seg in enumerate(sorted(kit.segments, key=lambda s: -s.priority_score), 1):
        lines.append(
            f"| {i} | {seg.name} | {seg.company_count} | {seg.competitor_count} "
            f"| {len(seg.pain_signals)} | {seg.priority_score} |"
        )
    lines.append("")
    for seg in sorted(kit.segments, key=lambda s: -s.priority_score):
        lines.append(f"### {seg.name}")
        lines.append(f"- ICP filters: `{seg.icp_filters}`")
        lines.append(f"- Sample companies: {', '.join(seg.sample_companies) or 'n/a'}")
        for sig in seg.pain_signals:
            lines.append(f"- Pain signal: {sig}")
        lines.append(f"- Priority {seg.priority_score}/100 — {seg.rationale}")
        if seg.degraded:
            lines.append("- Note: sized via degraded retry (live search unavailable)")
        lines.append("")
    lines.append("## Mom Test interview scripts")
    lines.append("")
    for script in kit.scripts:
        lines.append(f"### {script.segment}")
        for q in script.questions:
            lines.append(f"1. {q}")
        lines.append("")
    lines.append("## Experiment plan (this week)")
    lines.append("")
    for step in kit.experiment_plan:
        lines.append(f"- {step}")
    lines.append("")
    lines.append("## Graduation gates")
    lines.append("")
    for gate in kit.graduation_gates:
        lines.append(f"- {gate}")
    lines.append("")
    lines.append("## Kill criteria")
    lines.append("")
    for kill in kit.kill_criteria:
        lines.append(f"- {kill}")
    lines.append("")
    lines.append("## Decision")
    lines.append("")
    lines.append(f"**{kit.decision}**")
    lines.append("")
    lines.append("## Evidence")
    lines.append("")
    for ev in kit.evidence:
        lines.append(f"- `{ev.id}` {ev.source} — {ev.result_count} results ({ev.note}); query `{ev.query}`")
    if kit.guardrail_notes:
        lines.append("")
        lines.append("## Guardrail notes")
        for note in kit.guardrail_notes:
            lines.append(f"- {note}")
    if kit.recovered_from_failure:
        lines.append("")
        lines.append("## Recovery")
        lines.append("")
        lines.append("- At least one tool failure occurred during this run and the agent recovered (see run_state.json).")
    lines.append("")
    lines.append(f"Estimated model cost for this run: ${kit.cost_usd:.4f}")
    lines.append("")
    return "\n".join(lines)


def write_run_artifacts(kit: ValidationKit, state: dict, run_dir: Path) -> dict[str, Path]:
    run_dir.mkdir(parents=True, exist_ok=True)
    kit_json = run_dir / "validation_kit.json"
    kit_md = run_dir / "VALIDATION_KIT.md"
    state_json = run_dir / "run_state.json"
    summary_json = run_dir / "run_summary.json"
    kit_json.write_text(kit.model_dump_json(indent=2))
    kit_md.write_text(render_markdown(kit))
    state_json.write_text(__import__("json").dumps(state, indent=2, default=str))
    summary = {
        "run_id": kit.run_id,
        "decision": kit.decision,
        "top_segment": max(kit.segments, key=lambda s: s.priority_score).name if kit.segments else None,
        "segments": len(kit.segments),
        "recovered_from_failure": kit.recovered_from_failure,
        "cost_usd": round(kit.cost_usd, 6),
        "stage_ms": state.get("stage_ms", {}),
    }
    summary_json.write_text(__import__("json").dumps(summary, indent=2))
    return {"kit_json": kit_json, "kit_md": kit_md, "state_json": state_json, "summary_json": summary_json}
