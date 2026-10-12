# Demo video script (target: 2:40–2:55)

One rule: show, don't tell. Every claim gets an artifact on screen. The video must
cover, for each of neatlogs, Entire and cfo.ai: architecture, implementation,
runtime, reasoning and result.

## 0:00–0:20 — The problem (hook)

"Foundors skip customer discovery and build the wrong thing. StageZero is a
customer-discovery agent: one idea in, a falsifiable problem statement, data-sized
segments, Mom Test scripts and a proceed/pivot/kill decision out."

Screen: terminal, run the demo:
```
python -m stagezero run --idea "AI agent that chases unpaid invoices for independent consultants" --demo
```

## 0:20–1:10 — The agent (30% of score)

Show the architecture (README diagram) and walk one real run:
- `ingest` → `plan` (LLM plans 3 ICP hypotheses with Crustdata columns)
- `discover` (segment size, job-posting pain signals, competitor counts)
- `analyze` (transparent scoring: pain 45 / size 30 / saturation 25 → decision)
- `guardrail` → `scriptkit` → `report`
Screen: `runs/<id>/VALIDATION_KIT.md` scrolling to segments table, decision line,
kill criteria. Point out state persistence: crash mid-run, `--resume` finishes it.

## 1:10–1:55 — neatlogs (traces, failures, recovery)

- Architecture: span per stage + wrapped LLM client; `neatlogs.init/wrap/flush`.
- Runtime: dashboard Traces tab of the live runs (run-20261012-080405…); show the
  span tree and `stage_end`/`tool_call`/`provenance_guardrail` events.
- Reasoning: the credited live run proved the filter contract (0 companies →
  pivot) until API errors were read from traces; keep the before/after pair
  (080405 pivot-with-zeros vs. later real counts) as "the agent improved".
- Failure + recovery: `--fail-at discover` → `run_state.json` failure log →
  degraded retry → kit still delivered.

## 1:55–2:25 — Entire (checkpoints + graph)

- Implementation: `entire enable`, `entire plugin install graph`, `entire graph
  init-agents`; show `.entire/graph-agent.md` + `AGENTS.md` managed block.
- Runtime + result: `entire graph snapshot --format ndjson > runs/entire-graph.ndjson`
  (committed); `entire graph search --query "..."` answering a real question about
  the repo (e.g. where segment scoring happens → stages/analyze.py).
- If the user completes a Claude Code/Codex session: checkpoint link +
  `entire checkpoint explain HEAD` (Sessions + Changes), and the URL
  `https://entire.io/gh/eugene-tulu/founder-co-pilot/commit/<SHA>`.

## 2:25–2:45 — cfo.ai (business plan)

- Architecture: `scripts/make_business_plan.py` turns measured run costs into
  pricing/cost/revenue/runway; same tables pushed to a cfo.ai Model via
  `https://api.cfo.ai/mcp` (inspect_skills → build-model → edit_table_blocks).
- Screen: `business/BUSINESS_PLAN.md` (cost/run $0.015 measured, scenarios 100/500/2000
  customers, runway on hackathon credits) and the cfo.ai Model page if pushed.

## 2:45–2:55 — Close

"Built in a weekend for neatHack #1. Judgment: founders who validate with evidence
ship fewer products nobody wants." + repo URL.

## Before recording

- [ ] `python -m stagezero run --demo` clean on a fresh terminal (fixtures, no keys)
- [ ] `--resume run-20261012-080405-09d5b8` reproduces the live kit
- [ ] neatlogs traces visible for both live runs; doctor PASS
- [ ] `entire graph snapshot` current in git; search demo rehearsed
- [ ] business/BUSINESS_PLAN.md regenerated
- [ ] terminal font size readable at 1080p; no secrets on screen (.env never shown)
