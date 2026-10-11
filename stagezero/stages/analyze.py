from __future__ import annotations

from ..llm import LLM, maybe_llm
from ..models import Evidence, Idea, Segment

PROBLEM_SYSTEM = """You write a falsifiable problem statement for a startup, using this template:
"{Customer} struggle(s) to {job-to-be-done} because {root cause}; the current
workaround is {workaround}, which costs {cost}. Hypothesis: {solution sketch} removes
that cost for {focus segment}." Use only facts from the segment evidence. Plain text, no numbering."""

SEGMENT_RATIONALE_SYSTEM = """Explain in one paragraph why this segment scored as it did,
citing only the given numbers. At most 60 words."""


def score_segments(segments: list[Segment]) -> None:
    """Transparent scoring: pain 45%, segment size 30%, low saturation 25%."""
    if not segments:
        return
    max_size = max(s.company_count for s in segments) or 1
    for seg in segments:
        pain = min(len(seg.pain_signals) / 3.0, 1.0)
        size = min(seg.company_count / max_size, 1.0)
        saturation = min(seg.competitor_count / max(seg.company_count, 1), 1.0)
        seg.priority_score = round(100 * (0.45 * pain + 0.30 * size + 0.25 * (1 - saturation)))


def decide(segments: list[Segment]) -> tuple[str, str]:
    if not segments:
        return "kill", "No segment could be sized; the discovery run failed."
    top = max(segments, key=lambda s: s.priority_score)
    if top.priority_score >= 60 and top.company_count > 0:
        return "proceed", (
            f"Proceed: run 10 interviews in '{top.name}' (score {top.priority_score}, "
            f"~{top.company_count} companies show the ICP, {top.competitor_count} competitors)."
        )
    if top.priority_score >= 35:
        return "pivot", (
            f"Pivot: pain signals are thin in '{top.name}' (score {top.priority_score}). "
            "Re-cut segments around the hiring signals that do appear."
        )
    return "kill", (
        f"Kill this cut: no segment shows measurable pain (best {top.priority_score}). "
        "Revisit the problem before writing code."
    )


async def problem_statement(idea: Idea, top: Segment, llm: LLM) -> str:
    fallback = (
        f"{top.name.replace('-', ' ').title()} firms struggle to get paid on time because "
        "invoice chasing is manual, interrupt-driven work; the current workaround is hiring "
        f"AR/collections staff or ignoring aging invoices, which costs cash flow and hours. "
        f"Hypothesis: an agent that chases unpaid invoices removes that cost, starting with "
        f"'{top.name}'."
    )
    user = (
        f"Idea: {idea.idea_text}\nTop segment: {top.name}\nCompany count: {top.company_count}\n"
        f"Pain signals: {top.pain_signals}\nCompetitors in segment: {top.competitor_count}"
    )
    return await maybe_llm(llm, PROBLEM_SYSTEM, user, fallback)


async def analyze(
    idea: Idea, segments: list[Segment], evidence: list[Evidence], llm: LLM
) -> dict:
    """Analyze stage: score segments, decide proceed/pivot/kill, write problem statement."""
    score_segments(segments)
    decision, rationale = decide(segments)
    top = max(segments, key=lambda s: s.priority_score) if segments else None
    statement = await problem_statement(idea, top, llm) if top else "No segment data."
    return {"problem_statement": statement, "decision": decision, "rationale": rationale}
