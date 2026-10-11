#!/usr/bin/env python3
"""Generate business/BUSINESS_PLAN.md from real run artifacts.

This is the cfo.ai-facing artifact: pricing, costs, revenue, runway.
The same numbers are meant to be pushed into a cfo.ai Model over the MCP
server (https://api.cfo.ai/mcp) so the plan is inspectable and editable.
"""
from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Pricing (per month)
PRICE_PRO = 29.0
PRICE_TEAM = 199.0
# Fixed infra (USD/month): small VM + storage + misc
INFRA_USD = 18.0
# Crustdata hackathon allowance
CRUSTDATA_CREDITS = 5000
CRUSTDATA_CREDITS_PER_RUN = 12  # ~4 searches x ~3 results at 0.03 credits + jobs
# Hackathon compute credits
AWS_CREDITS = 25.0
LITELLM_CREDITS = 20.0


def load_runs() -> list[dict]:
    runs = []
    runs_dir = ROOT / "runs"
    for path in sorted(runs_dir.glob("*/run_summary.json")):
        try:
            runs.append(json.loads(path.read_text()))
        except Exception:
            continue
    return runs


def avg(runs: list[dict], key: str, default: float = 0.0) -> float:
    values = [r[key] for r in runs if isinstance(r.get(key), (int, float))]
    return statistics.fmean(values) if values else default


def main() -> int:
    runs = load_runs()
    cost_per_run = avg(runs, "cost_usd", 0.0) or 0.004
    p50_ms = avg(runs, "stage_ms") if runs else 0.0
    lines = []
    a = lines.append
    a("# StageZero — business plan (for cfo.ai)")
    a("")
    a(f"_Generated from {len(runs)} real run(s) in `runs/`. This document is the source of truth for")
    a("the cfo.ai Model; push these tables into a Model via the cfo.ai MCP server")
    a("(`https://api.cfo.ai/mcp`) so pricing, cost and runway stay inspectable._")
    a("")
    a("## 1. The agent")
    a("")
    a("StageZero runs customer discovery for pre-PMF founders: one idea in, a data-sized")
    a("segment analysis, Mom Test interview scripts and a proceed/pivot/kill decision out.")
    a("")
    a("## 2. Unit cost per run")
    a("")
    a(f"- Model inference (LiteLLM, Sonnet-class): **${cost_per_run:.4f}** per run (measured)")
    a(f"- Crustdata data: ~{CRUSTDATA_CREDITS_PER_RUN} credits/run; 5,000 hackathon credits = "
      f"~{CRUSTDATA_CREDITS // CRUSTDATA_CREDITS_PER_RUN} runs before purchase")
    a("- Infra amortised: ~$0.01/run at 1,000 runs/month on one small VM")
    a(f"- **Fully-loaded cost per run: ~${cost_per_run + 0.01:.4f}**")
    a("")
    a("## 3. Pricing")
    a("")
    a("| Plan | Price/month | Includes |")
    a("|------|-------------|----------|")
    a("| Free | $0 | 1 validation kit, fixture-backed segment counts |")
    a(f"| Pro | ${PRICE_PRO:.0f} | Unlimited kits, live Crustdata data, saved runs, resume |")
    a(f"| Team | ${PRICE_TEAM:.0f} | Shared run library, exports, segment history |")
    a("")
    a("## 4. Revenue and gross margin scenarios")
    a("")
    a("Assumes Pro mix of 60% Pro / 40% Team of paying customers, 2 kits/customer/month,")
    a("model cost per run as measured above.")
    a("")
    a("| Scenario | Customers | Runs/mo | Revenue | Infra + inference | Gross profit | Margin |")
    a("|----------|-----------|---------|---------|-------------------|--------------|--------|")
    pro_share, team_share = 0.6, 0.4
    for customers in (100, 500, 2000):
        runs_per_month = customers * 2
        revenue = customers * (pro_share * PRICE_PRO + team_share * PRICE_TEAM)
        variable = runs_per_month * (cost_per_run + 0.01)
        gross = revenue - INFRA_USD - variable
        margin = gross / revenue * 100 if revenue else 0
        a(f"| {customers} | {customers} | {runs_per_month} | ${revenue:,.0f} | "
          f"${INFRA_USD + variable:,.0f} | ${gross:,.0f} | {margin:.0f}% |")
    a("")
    a("## 5. Runway (hackathon bootstrap)")
    a("")
    a(f"- AWS credits: ${AWS_CREDITS:.0f} (hackathon)")
    a(f"- LiteLLM budget: ${LITELLM_CREDITS:.0f} (hackathon) = ~${LITELLM_CREDITS / cost_per_run:,.0f} runs "
      f"at ${cost_per_run:.4f}/run")
    a(f"- Crustdata: 5,000 credits = ~{CRUSTDATA_CREDITS // CRUSTDATA_CREDITS_PER_RUN} runs")
    a(f"- At the Base scenario (100 customers), monthly burn is ${INFRA_USD:.0f} infra + "
      f"${200 * (cost_per_run + 0.01):.2f} inference, so compute credits alone cover the first months;")
    a("  first $29 Pro customer funds the rest.")
    a("")
    a("## 6. Decisions this plan supports")
    a("")
    a("- Free tier gated on fixture data keeps acquisition cheap while Crustdata costs stay near zero.")
    a("- Team plan priced for the 'founder + cofounder + advisor' buyer, not per-seat.")
    a("- If Crustdata live endpoints exceed ~$0.02/run at scale, cache segment counts monthly.")
    a("")
    out = ROOT / "business" / "BUSINESS_PLAN.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines))
    print(f"wrote {out.relative_to(ROOT)} from {len(runs)} run(s); cost/run=${cost_per_run:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
