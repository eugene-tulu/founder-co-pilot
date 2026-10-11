# StageZero — customer discovery for founders who are still building the wrong thing

A single agent (plus tool-calling stages) that takes a one-sentence startup idea and
runs the part founders skip: **customer problem selection and segmentation, validated
against real market data**, ending in a falsifiable proceed / pivot / kill decision.

Built for [neatHack #1](https://neatlogs.com/hackathon) (Oct 10–12, 2026) with
[neatlogs](https://neatlogs.com), [Entire](https://entire.io) and
[cfo.ai](https://cfo.ai/neathacks), using the Acquisition.com *$100M Scaling Roadmap*
Stage 0 (Improvise) as the strategy spine.

## What it does

```
idea ──► ingest ──► plan ──► discover ──► analyze ──► guardrail ──► scriptkit ──► report
         normalise   3 ICP      size        score       every       Mom Test     validation kit
                     hypotheses segments    segments    number      scripts      (markdown+json)
                     (cfo.ai-   w/ real     + decide    traced to
                     style plan) Crustdata   proceed/    tool
                                  data       pivot/kill  output
```

Output (per run, in `runs/<run_id>/`):

- `VALIDATION_KIT.md` — the deliverable: stage diagnosis, falsifiable problem statement,
  ranked ICP segments with evidence, 10-question Mom Test script per segment, this-week
  experiment plan, graduation gates, kill criteria, decision
- `validation_kit.json` — machine-readable kit
- `run_state.json` — per-stage state (enables resume after failure) + failure log
- `run_summary.json` — decision, scores, cost, stage timings

## Quickstart

```bash
pip install -e .            # or: pip install neatlogs openai httpx pydantic

# Demo mode: fully offline, fixture data, no keys needed
python -m stagezero run --idea "AI agent that chases unpaid invoices for independent consultants" --demo

# Real mode: set keys in .env (see .env.example) and drop --demo
export NEATLOGS_API_KEY=...     # neatlogs PROJECT API key (not the nlw_ ingest key)
export LLM_BASE_URL=...         # any OpenAI-compatible endpoint (hackathon LiteLLM key works)
export LLM_API_KEY=...
export CRUSTDATA_API_KEY=...    # 5,000 hackathon credits, promo NEATLOGS-OCT2026
python -m stagezero run --idea "..."

# Recovery demo (chaos switch): inject a failure, watch the agent recover
python -m stagezero run --idea "..." --demo --fail-at discover
```

## Design decisions

- **Every stage is a span.** neatlogs traces the whole run (`WORKFLOW`), each stage
  (`stage_end stage=… status=…`), every tool call, and the guardrail verdict. With a
  `NEATLOGS_API_KEY` the wrapped OpenAI client and stage logs appear in the Traces tab;
  without one, everything still runs and `run_state.json` holds the same structure.
- **Numbers must be earned.** The provenance guardrail blocks any number in the problem
  statement that is not present in a tool output (segment counts, job-signal counts).
  Unsourced claims get one LLM repair retry, then a hard strip. Blocked claims are
  logged and searchable in neatlogs (`provenance_guardrail status=BLOCKED`).
- **Recovery is a feature, not a hope.** Stages persist to `run_state.json` after each
  step, so a crash mid-run resumes (completed stages are skipped). Crustdata searches
  retry degraded (smaller limit) before failing; the chaos switch rehearses it.
- **Data over vibes.** Segment sizes, pain signals (hiring posts) and competitor counts
  come from Crustdata's `/company/search` + `/job/search`; industry filter values are
  resolved through Crustdata's free `/company/search/autocomplete` endpoint. In demo
  mode all of this is fixture data, clearly labelled as such in every artifact.

## Hackathon evidence map

| Criterion | Where to look |
|---|---|
| Agent works start→finish | `runs/*/VALIDATION_KIT.md`, `python -m stagezero run --demo` |
| neatlogs | every stage/tool/guardrail event; trace links from a keyed run; recovery run `runs/*` with `recovered_from_failure: true` |
| Entire | repo built under Entire checkpoints; `entire graph snapshot --format ndjson` output + `.entire/graph-agent.md` committed |
| cfo.ai | [`business/BUSINESS_PLAN.md`](business/BUSINESS_PLAN.md) (pricing, costs, revenue, runway, generated from real run costs) |
| Improved agent | before/after pair: run with a bug, investigate in neatlogs traces, fix, rerun (see `git log`) |
| Built in public | build-log posts tagged #neatHack |

## Layout

```
stagezero/
  config.py     env settings (all keys optional)
  tracing.py    neatlogs init/trace/log + stage timing
  crustdata.py  Crustdata REST client, retries, degraded fallback
  llm.py        OpenAI-compatible client (neatlogs-wrapped), token/cost accounting
  models.py     pydantic schemas for the kit
  pipeline.py   resumable, traced, failure-injectable orchestrator
  stages/       ingest, plan, discover, analyze, guardrail, scriptkit, report
scripts/make_business_plan.py   generates business/BUSINESS_PLAN.md from run costs
tests/          offline end-to-end, guardrail, recovery, resume tests
```

## Honest limits

- Crustdata filter field names are discovered via autocomplete where possible; exact
  schema varies by plan (live endpoints are enterprise-tier). Degraded mode exists so a
  missing/limited key never breaks the run.
- Segment scoring is deliberately transparent (pain 45% / size 30% / low saturation 25%)
  so a founder can argue with it.
- Demo-mode numbers are fixtures, not market truth.
