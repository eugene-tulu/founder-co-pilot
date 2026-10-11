from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..models import Evidence

_NUM = re.compile(r"\$?\d[\d,]*(?:\.\d+)?\s?(?:companies|jobs|postings|firms|k|K|%)?")


@dataclass
class GuardrailResult:
    status: str  # PASS | BLOCKED | REPAIRED
    known_values: set[str] = field(default_factory=set)
    blocked: list[str] = field(default_factory=list)


def known_numbers(evidence: list[Evidence], segments=None) -> set[str]:
    """Every numeric value the agent may claim, taken from tool outputs only."""
    values: set[str] = set()
    for ev in evidence:
        values.add(str(ev.result_count))
    if segments is not None:
        for seg in segments:
            values.add(str(seg.company_count))
            values.add(str(seg.competitor_count))
            values.update(str(len(seg.pain_signals)))
    return values


def check_claims(text: str, evidence: list[Evidence], segments=None) -> GuardrailResult:
    known = known_numbers(evidence, segments)
    blocked: list[str] = []
    for match in _NUM.finditer(text):
        token = match.group(0).strip()
        digits = re.sub(r"[^\d]", "", token)
        if not digits:
            continue
        if digits in known or digits.rstrip("0") in known:
            continue
        blocked.append(token)
    return GuardrailResult(status="BLOCKED" if blocked else "PASS", known_values=known, blocked=blocked)


def _strip_unsourced(text: str, blocked_tokens: list[str]) -> str:
    """Hard fallback: drop sentences that contain blocked tokens."""
    keep: list[str] = []
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        if any(tok in sentence for tok in blocked_tokens):
            continue
        keep.append(sentence)
    return " ".join(keep).strip() or "[unsourced claims removed]"


async def enforce(text: str, evidence: list[Evidence], llm, segments=None) -> tuple[str, GuardrailResult, list[str]]:
    """Block any number that cannot be traced to a tool output; one LLM repair retry."""
    result = check_claims(text, evidence, segments)
    notes: list[str] = []
    if result.status == "PASS":
        return text, result, notes

    notes.append(f"guardrail blocked {len(result.blocked)} unsourced number(s): {result.blocked}")
    system = (
        "You are a provenance guardrail. Remove or replace every number that is not "
        "provided in EVIDENCE below. Keep all numbers that appear in EVIDENCE verbatim. "
        "Reply with the corrected text only."
    )
    allowed = ", ".join(sorted(result.known_values)) or "(none)"
    user = f"EVIDENCE numbers: {allowed}\n\nTEXT:\n{text}"
    repaired = text
    if llm is not None and getattr(llm, "online", False):
        try:
            repaired = await llm.chat(system, user)
        except Exception:
            repaired = _strip_unsourced(text, result.blocked)
    else:
        repaired = _strip_unsourced(text, result.blocked)

    recheck = check_claims(repaired, evidence, segments)
    if recheck.status == "PASS":
        return repaired, GuardrailResult(status="REPAIRED", known_values=result.known_values), notes
    notes.append("guardrail removed residual unsourced claims after repair retry")
    stripped = _strip_unsourced(repaired, recheck.blocked or result.blocked)
    return stripped, GuardrailResult(status="REPAIRED", known_values=result.known_values), notes
