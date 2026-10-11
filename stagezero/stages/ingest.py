from __future__ import annotations

from ..llm import LLM, maybe_llm
from ..models import Idea

DOMAIN_KEYWORDS = {
    "invoice": "finance-ops",
    "invoic": "finance-ops",
    "billing": "finance-ops",
    "account": "finance-ops",
    "recruit": "hr",
    "hiring": "hr",
    "marketing": "growth",
    "sales": "growth",
    "support": "support",
    "legal": "legal",
    "health": "health",
    "code": "software",
    "develop": "software",
}


async def parse_idea(idea_text: str, llm: LLM) -> Idea:
    """Normalise a one-sentence idea into an Idea, guessing the domain by keywords."""
    text = idea_text.strip()
    lowered = text.lower()
    domain = "general"
    for needle, guess in DOMAIN_KEYWORDS.items():
        if needle in lowered:
            domain = guess
            break

    system = (
        "You normalise a startup idea into a structured brief. "
        "Reply with JSON only: {domain, restated_idea}."
    )
    user = f"Idea: {text}\nGuessed domain: {domain}"
    fallback = text
    out = await maybe_llm(llm, system, user, fallback, json_mode=True)
    return Idea(idea_text=text, domain=domain)
