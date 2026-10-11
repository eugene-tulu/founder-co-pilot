from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class Idea(BaseModel):
    idea_text: str
    domain: str = "general"
    founder_stage: str = "stage0-improvise"
    has_free_users: bool = False
    has_first_sale: bool = False


class Hypothesis(BaseModel):
    name: str
    description: str
    filters: list[dict[str, Any]] = Field(default_factory=list)
    why: str = ""


class Segment(BaseModel):
    name: str
    icp_filters: list[dict[str, Any]] = Field(default_factory=list)
    company_count: int = 0
    sample_companies: list[str] = Field(default_factory=list)
    pain_signals: list[str] = Field(default_factory=list)
    competitor_count: int = 0
    priority_score: int = 0
    rationale: str = ""
    degraded: bool = False


class Evidence(BaseModel):
    id: str
    source: str  # crustdata | offline-fixture
    query: dict[str, Any] = Field(default_factory=dict)
    result_count: int = 0
    note: str = ""


class InterviewQuestions(BaseModel):
    segment: str
    questions: list[str] = Field(default_factory=list)


class ValidationKit(BaseModel):
    run_id: str
    idea: Idea
    stage_diagnosis: str
    problem_statement: str
    segments: list[Segment] = Field(default_factory=list)
    scripts: list[InterviewQuestions] = Field(default_factory=list)
    experiment_plan: list[str] = Field(default_factory=list)
    graduation_gates: list[str] = Field(default_factory=list)
    kill_criteria: list[str] = Field(default_factory=list)
    decision: str
    guardrail_notes: list[str] = Field(default_factory=list)
    evidence: list[Evidence] = Field(default_factory=list)
    recovered_from_failure: bool = False
    cost_usd: float = 0.0
