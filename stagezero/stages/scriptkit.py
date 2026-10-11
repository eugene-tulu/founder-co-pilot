from __future__ import annotations

from ..llm import LLM, maybe_llm
from ..models import Idea, InterviewQuestions, Segment

MOM_TEST_SYSTEM = """Write 10 Mom Test interview questions for the given customer segment.
Rules: ask about past behaviour, never opinions or predictions ("did you" not "would you");
never pitch the idea; dig into current workarounds and their cost. JSON only:
{"questions": ["...", ...]}"""

FALLBACK_QUESTIONS = [
    "Walk me through the last time you had to deal with {pain}. What happened?",
    "How much time did that take you and your team last month?",
    "What do you currently use to handle {pain}?",
    "What did you last pay for to solve this, and what made you decide it was worth it?",
    "Who else on your team touches this problem?",
    "When was the last time this cost you money directly?",
    "What have you already tried that did not work?",
    "How do you know when this problem has gotten worse?",
    "If this were solved overnight, what would you do with the saved time?",
    "What would have to be true for you to pay for a fix this month?",
]


async def build_scripts(idea: Idea, segments: list[Segment], llm: LLM) -> list[InterviewQuestions]:
    """Build a 10-question Mom Test script per top segment."""
    scripts: list[InterviewQuestions] = []
    pain = " ".join(w for w in idea.idea_text.lower().split() if w not in {"a", "an", "the", "for", "that", "of"})
    for seg in segments[:3]:
        user = f"Idea: {idea.idea_text}\nSegment: {seg.name}\nPain signals: {seg.pain_signals[:2]}"
        fallback_json = '{"questions": [' + ", ".join(
            '"' + q.format(pain=pain).replace('"', "'") + '"' for q in FALLBACK_QUESTIONS
        ) + "]}"
        raw = await maybe_llm(llm, MOM_TEST_SYSTEM, user, fallback_json, json_mode=True)
        import json

        try:
            questions = json.loads(raw)["questions"]
        except Exception:
            questions = [q.format(pain=pain) for q in FALLBACK_QUESTIONS]
        scripts.append(InterviewQuestions(segment=seg.name, questions=[str(q) for q in questions][:10]))
    return scripts


def acq_stage_plan(stage: str = "stage0-improvise") -> tuple[list[str], list[str], list[str]]:
    """Experiment plan, graduation gates and kill criteria on the ACQ $100M roadmap spine."""
    if stage.startswith("stage0"):
        plan = [
            "Recruit 10 founders from the top segment for free 20-minute interviews this week (warm channel first: past email contacts, LinkedIn 1st-degree).",
            "Run the Mom Test script; capture past behaviour, never opinions.",
            "Give the top 3 most-pained interviewees the workflow done-for-them by hand (concierge), free, once.",
            "Log every interview against the kill criteria below.",
        ]
        gates = [
            "At least 8 of 10 interviews confirm the pain is recurring and already costs measurable time/money",
            "At least 5 interviewees accept a second, free concierge run unprompted",
            "At least 3 interviewees describe the current, specific workaround in detail",
        ]
        kills = [
            "Fewer than 4 of 10 interviewees recognise the pain unprompted",
            "Interviewees already solved it well enough that a paid tool feels unnecessary",
            "The segment keeps describing it as a nice-to-have, not a recurring cost",
        ]
    else:
        plan = ["Run pricing probes with early free users before building paid plans."]
        gates = ["3 users pay or pre-commit for a V1."]
        kills = ["No user pays after a direct ask."]
    return plan, gates, kills
