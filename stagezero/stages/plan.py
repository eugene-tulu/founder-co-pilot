from __future__ import annotations

import json

from ..crustdata import CrustdataClient
from ..fixtures import DEMO_HYPOTHESES
from ..llm import LLM
from ..models import Hypothesis, Idea

SYSTEM_PROMPT = """You are the planning brain of a customer-discovery agent for startup founders.
Given a one-sentence startup idea, produce exactly 3 customer-segment hypotheses.
Each hypothesis: name (slug), description, why this segment feels the pain,
and crustdata-style company filters (field/type/value triples; prefer industries
and headcount fields, keep them broadly correct).
Return JSON only: {"hypotheses": [{"name":..., "description":..., "why":..., "filters": [{"field": "industries", "type": "in", "value": ["accounting"]}]}]}"""


async def plan_hypotheses(idea: Idea, llm: LLM, crustdata: CrustdataClient) -> list[Hypothesis]:
    """Plan stage: turn the idea into 3 falsifiable ICP hypotheses with search filters."""
    if not llm.online or not crustdata.online:
        return [Hypothesis(**h) for h in DEMO_HYPOTHESES]

    user = f"Idea: {idea.idea_text}\nDomain: {idea.domain}"
    try:
        raw = await llm.chat(SYSTEM_PROMPT, user, json_mode=True)
        data = json.loads(raw)
        hyps = [Hypothesis(**h) for h in data.get("hypotheses", [])][:3]
    except Exception:
        return [Hypothesis(**h) for h in DEMO_HYPOTHESES]
    if len(hyps) < 3:
        return [Hypothesis(**h) for h in DEMO_HYPOTHESES]

    # Resolve industry terms to valid filter values via the free autocomplete endpoint.
    for h in hyps:
        values = [f.get("value") for f in h.filters if f.get("field") == "industries" and f.get("type") == "in"]
        resolved: list[str] = []
        for term in (values[0] if values else [idea.domain]):
            if isinstance(term, str):
                hit = await crustdata.autocomplete("industries", term)
                resolved.extend(hit.get("values", [term]) if isinstance(hit, dict) else [term])
        if resolved:
            h.filters = [{"field": "industries", "type": "in", "value": sorted(set(resolved))[:5]}]
    return hyps
