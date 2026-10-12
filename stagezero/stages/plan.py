from __future__ import annotations

from ..crustdata import CrustdataClient
from ..fixtures import DEMO_HYPOTHESES
from ..llm import LLM, parse_json_loose
from ..models import Hypothesis, Idea

SYSTEM_PROMPT = """You are the planning brain of a customer-discovery agent for startup founders.
Given a one-sentence startup idea, produce exactly 3 customer-segment hypotheses.
Each hypothesis: name (slug), description, why this segment feels the pain,
and Crustdata company-search conditions using ONLY these valid columns:
basic_info.industries, basic_info.employee_count_range, basic_info.name,
country, city, linkedin_company_category, funding.last_round_type.
Every hypothesis MUST include exactly one basic_info.employee_count_range
condition (one of "1-10", "11-50", "51-200") and 1-3 specific industries;
avoid catch-all industries. Each condition is {"field": ..., "type": ..., "value": ...}
with type one of ["=", "!=", "<", "=<", ">", "=>", "in", "not_in", "(.)", "has_all"]
where "(.)" is a case-insensitive all-words match. Return JSON only:
{"hypotheses": [{"name":..., "description":..., "why":..., "filters": [{"field": "basic_info.industries", "type": "in", "value": ["Accounting"]}]}]}"""


async def plan_hypotheses(idea: Idea, llm: LLM, crustdata: CrustdataClient) -> list[Hypothesis]:
    """Plan stage: turn the idea into 3 falsifiable ICP hypotheses with search filters."""
    if not llm.online or not crustdata.online:
        return [Hypothesis(**h) for h in DEMO_HYPOTHESES]

    user = f"Idea: {idea.idea_text}\nDomain: {idea.domain}"
    try:
        raw = await llm.chat(SYSTEM_PROMPT, user, json_mode=True)
        data = parse_json_loose(raw)
        hyps = [Hypothesis(**h) for h in data.get("hypotheses", [])][:3]
    except Exception:
        return [Hypothesis(**h) for h in DEMO_HYPOTHESES]
    if len(hyps) < 3:
        return [Hypothesis(**h) for h in DEMO_HYPOTHESES]

    # Resolve industry terms to valid filter values via the free autocomplete endpoint.
    for h in hyps:
        values = [
            f.get("value")
            for f in h.filters
            if f.get("field") == "basic_info.industries" and f.get("type") == "in"
        ]
        resolved: list[str] = []
        for term in (values[0] if values else [idea.domain]):
            if isinstance(term, str):
                hit = await crustdata.autocomplete("basic_info.industries", term)
                suggestions = hit.get("suggestions", []) if isinstance(hit, dict) else []
                resolved.extend(
                    s.get("value", term) if isinstance(s, dict) else str(s) for s in suggestions
                ) or [term]
        if resolved:
            h.filters = [{"field": "basic_info.industries", "type": "in", "value": sorted(set(resolved))[:5]}]
    return hyps
