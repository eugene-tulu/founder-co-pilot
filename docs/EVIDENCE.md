# Submission evidence (neatHack #1)

All artifacts below live in this public repository:
https://github.com/eugene-tulu/founder-co-pilot

## neatlogs

Project: "Eugene's project" (`2066e414-44c4-42a4-b74f-d8450f0a90b6`), workflow `stagezero`.
Every stage, tool call and guardrail verdict is a logged event; LLM calls are traced via
the wrapped OpenAI client. Traces (all `status=OK`, `finalizationStatus=finalized`):

| Trace ID | Duration | Run | Demonstrates |
|---|---|---|---|
| `fe7451c8d6acfc5daf1d173068e018c1` | 106s | `run-20261012-075804` | **Before**: v1 request contract — Crustdata calls failed, segments sized 0, decision `pivot` |
| `3100c861c0a05f664657984d35ed342f` | 51s | `run-20261012-080239` | **After** (fix in commit `c5b4cb2`): real data — 1.49M / 169,908 / 68,916 companies, decision `proceed` |
| `eb9dcc1f7258b1501d213baa77c58f82` | 75s | `run-20261012-080405` | LLM-planned hypotheses live: 5.2M / 2.7M / 2.3M companies, decision `proceed` |
| `caf8a8e30434ec118703cb8771749002` | 127s | `run-20261012-080547` | 7 spans, 6 LLM calls; failure surfaced via `insufficient_credits` (degraded path, no silent zeros) |
| `7aac3f78c83ac9bfcda9d9905533e7c6`, `8f612d44cda8250d71788beff0e7839e` | — | resume rebuilds | `--resume` replays completed stages with zero API calls |

**The agent improved**: run `075804` (trace `fe7451c8…`) failed discovery with 0-company
segments; the failing tool calls were read from the trace/API error stream, the request
contract was fixed (`c5b4cb2`), and the same idea then produced real segment sizes
(trace `3100c861…` / `eb9dcc1f…`). **Recovers from failures**: `--fail-at discover`
injects a stage failure; `run_state.json` records it and the kit is still delivered
(degraded retries in `crustdata.search_with_fallback`).

## Entire

- Repository on Entire: **https://entire.io/gh/eugene-tulu/founder-co-pilot** (Public, ready)
- Entire CLI 0.11.4 + entire-graph plugin 0.4.0 active; `entire graph init-agents` output
  committed (`.entire/graph-agent.md`, `AGENTS.md`, `CLAUDE.md`)
- Full code graph snapshot committed: `runs/entire-graph.ndjson` (2,969 NDJSON lines:
  files, symbols, 30-relation edges)
- Checkpoints: hooks installed (`entire enable --agent codex`). A linked checkpoint needs an
  agent session; if none is captured before submission, the accepted alternative is the
  graph output above. Checkpoint URL format (once created):
  `https://entire.io/gh/eugene-tulu/founder-co-pilot/commit/<FULL_SHA>`

## cfo.ai

**Live Model built and verified** (org PULA, scenario `Main Scenario`), tables created over MCP
(`https://api.cfo.ai/mcp`, device/OAuth via `scripts/cfoai_mcp.py`):

- **Monthly model** (verified readback, 2026-10): Base 100 customers → revenue **$9,700/mo**,
  inference+data **$3**, infra $18, gross profit $9,679, margin 99.8%; Growth 500 → $48,500 / $15;
  Scale 2,000 → $194,000 / $60. Runway months = 45 hackathon credits ÷ monthly burn.
  https://app.cfo.ai/s/p_AQKAqAYkNTUwNDUwY2UtY2JkNS00MDRlLTg4MGMtZjhlZDMwNWE4MjJlDWRlZmF1bHRfbGF5ZXI
- **Scenarios** (customer counts): https://app.cfo.ai/s/p_AQKAqAYkNTRiNDgzNjMtMjJjZS00ZTA1LWJhM2MtMzA4YTJmMTAxZmY1DWRlZmF1bHRfbGF5ZXI
- **Pricing** ($0 / $29 / $199): https://app.cfo.ai/s/p_AQKAqAYkYzk1YTNkNzktMGJhMC00MDc0LTk1MDgtMzgxNTIyMmJkNTliDWRlZmF1bHRfbGF5ZXI
- **Cost drivers** (measured $0.015/run model cost, 2 kits/customer/mo, 60/40 Pro/Team mix, $18 infra/mo, $45 credits):
  https://app.cfo.ai/s/p_AQKAqAYkNzJlZjhjZjEtMmE1Yy00ZGY1LTgwNTQtNGUwNjgzZjRkZTdkDWRlZmF1bHRfbGF5ZXI
- Model page: https://app.cfo.ai/s/p_AQGAqAYkMTE1NDg2MmEtOWFkOS00MTM1LTg3YzMtMDMwYjA1M2QyZjFkDWRlZmF1bHRfbGF5ZXI
- The same numbers are generated in-repo from measured run costs:
  [`business/BUSINESS_PLAN.md`](../business/BUSINESS_PLAN.md) via `scripts/make_business_plan.py`

## Crustdata

- Live runs above use real Crustdata data (5,000 hackathon credits, promo NEATLOGS-OCT2026).
  Credits were exhausted mid-hackathon by development debugging; responses are cached in
  `runs/crustdata_cache.json` with `_cached_from` provenance, and `--resume` rebuilds any
  captured run with zero new API spend.

## The agent

- `python -m stagezero run --idea "AI agent that chases unpaid invoices for independent consultants" --demo`
  (offline, no keys) → `runs/<id>/VALIDATION_KIT.md`
- Live kit replay: `--resume run-20261012-080405-09d5b8`
- Tests: `pytest` (4 passing: end-to-end, guardrail, recovery, resume)
