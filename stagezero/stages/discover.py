from __future__ import annotations

from ..crustdata import CrustdataClient
from ..fixtures import DEMO_SEGMENTS, FIXTURE_SOURCE
from ..models import Evidence, Hypothesis, Idea, Segment
from ..tracing import log_tool

PAIN_TERMS = ["billing", "invoice", "collections", "accounts receivable", "bookkeeping"]


def _count(data: dict) -> int:
    for key in ("total", "total_count", "count"):
        if isinstance(data.get(key), int):
            return data[key]
    rows = data.get("results") or data.get("companies") or data.get("data") or []
    return len(rows) if isinstance(rows, list) else 0


def _names(data: dict, limit: int = 3) -> list[str]:
    rows = data.get("results") or data.get("companies") or data.get("data") or []
    names: list[str] = []
    for row in rows[:limit]:
        if isinstance(row, dict):
            name = row.get("name") or (row.get("basic_info") or {}).get("name")
            if name:
                names.append(name)
    return names


async def discover_segments(
    idea: Idea,
    hypotheses: list[Hypothesis],
    crustdata: CrustdataClient,
    offline: bool,
) -> dict:
    """Discovery stage: size each segment and pull pain signals from real data."""
    segments: list[Segment] = []
    evidence: list[Evidence] = []
    recovered = False
    pain_term = next((t for t in PAIN_TERMS if t.split()[0] in idea.idea_text.lower()), PAIN_TERMS[0])

    for hyp in hypotheses:
        if offline:
            fx = DEMO_SEGMENTS[hyp.name]
            seg = Segment(
                name=hyp.name,
                icp_filters=hyp.filters,
                company_count=fx["company_count"],
                sample_companies=fx["sample_companies"],
                pain_signals=fx["pain_signals"],
                competitor_count=fx["competitor_count"],
                rationale=hyp.why,
            )
            segments.append(seg)
            evidence.append(
                Evidence(
                    id=f"ev-company-{hyp.name}",
                    source=FIXTURE_SOURCE,
                    query={"filters": hyp.filters},
                    result_count=fx["company_count"],
                    note="segment size",
                )
            )
            continue

        seg = Segment(name=hyp.name, icp_filters=hyp.filters, rationale=hyp.why)
        # Segment size. A real failure here triggers the degraded retry (recovery path).
        try:
            data, degraded = await crustdata.search_with_fallback(hyp.filters, limit=25)
            seg.degraded = degraded
            recovered = recovered or degraded
        except Exception as exc:  # noqa: BLE001 - stage must never crash the pipeline
            log_tool("company_search", "unavailable", hypothesis=hyp.name, error=str(exc)[:200])
            data, seg.degraded = {}, True
            recovered = True
        seg.company_count = _count(data)
        seg.sample_companies = _names(data)
        evidence.append(
            Evidence(
                id=f"ev-company-{hyp.name}",
                source="crustdata /company/search",
                query={"filters": hyp.filters, "limit": 25},
                result_count=seg.company_count,
                note="degraded retry" if seg.degraded else "segment size",
            )
        )

        # Pain signals: job postings that mention the pain term.
        try:
            jobs = await crustdata.job_search(
                [{"field": "job_title", "type": "(.)", "value": pain_term}], limit=25
            )
            job_rows = jobs.get("results") or jobs.get("jobs") or jobs.get("data") or []
            signals = [
                f"job posting: {r.get('title', r.get('job_title', 'role'))} at "
                f"{r.get('company_name', (r.get('company') or {}).get('name', 'a firm')) if isinstance(r.get('company'), dict) else r.get('company_name', 'a firm')}"
                for r in job_rows[:3]
                if isinstance(r, dict)
            ]
            evidence.append(
                Evidence(
                    id=f"ev-jobs-{hyp.name}",
                    source="crustdata /job/search",
                    query={"filters": [{"field": "job_title", "type": "(.)", "value": pain_term}]},
                    result_count=len(job_rows),
                    note="pain signals from hiring",
                )
            )
        except Exception:
            signals = []
        # Competitors: firms whose name betrays the same product.
        try:
            comp_data, _ = await crustdata.search_with_fallback(
                [{"field": "basic_info.name", "type": "(.)", "value": pain_term.split()[0]}], limit=25
            )
            seg.competitor_count = _count(comp_data)
        except Exception:
            seg.competitor_count = 0
        seg.pain_signals = signals or [f"no job-title signal for '{pain_term}' in this segment"]
        segments.append(seg)

    return {"segments": segments, "evidence": evidence, "recovered": recovered}
