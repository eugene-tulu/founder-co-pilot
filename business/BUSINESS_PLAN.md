# StageZero — business plan (for cfo.ai)

_Generated from 6 real run(s) in `runs/`. This document is the source of truth for
the cfo.ai Model; push these tables into a Model via the cfo.ai MCP server
(`https://api.cfo.ai/mcp`) so pricing, cost and runway stay inspectable._

## 1. The agent

StageZero runs customer discovery for pre-PMF founders: one idea in, a data-sized
segment analysis, Mom Test interview scripts and a proceed/pivot/kill decision out.

## 2. Unit cost per run

- Model inference (LiteLLM, Sonnet-class): **$0.0150** per run (measured)
- Crustdata data: ~12 credits/run; 5,000 hackathon credits = ~416 runs before purchase
- Infra amortised: ~$0.01/run at 1,000 runs/month on one small VM
- **Fully-loaded cost per run: ~$0.0250**

## 3. Pricing

| Plan | Price/month | Includes |
|------|-------------|----------|
| Free | $0 | 1 validation kit, fixture-backed segment counts |
| Pro | $29 | Unlimited kits, live Crustdata data, saved runs, resume |
| Team | $199 | Shared run library, exports, segment history |

## 4. Revenue and gross margin scenarios

Assumes Pro mix of 60% Pro / 40% Team of paying customers, 2 kits/customer/month,
model cost per run as measured above.

| Scenario | Customers | Runs/mo | Revenue | Infra + inference | Gross profit | Margin |
|----------|-----------|---------|---------|-------------------|--------------|--------|
| 100 | 100 | 200 | $9,700 | $23 | $9,677 | 100% |
| 500 | 500 | 1000 | $48,500 | $43 | $48,457 | 100% |
| 2000 | 2000 | 4000 | $194,000 | $118 | $193,882 | 100% |

## 5. Runway (hackathon bootstrap)

- AWS credits: $25 (hackathon)
- LiteLLM budget: $20 (hackathon) = ~$1,330 runs at $0.0150/run
- Crustdata: 5,000 credits = ~416 runs
- At the Base scenario (100 customers), monthly burn is $18 infra + $5.01 inference, so compute credits alone cover the first months;
  first $29 Pro customer funds the rest.

## 6. Decisions this plan supports

- Free tier gated on fixture data keeps acquisition cheap while Crustdata costs stay near zero.
- Team plan priced for the 'founder + cofounder + advisor' buyer, not per-seat.
- If Crustdata live endpoints exceed ~$0.02/run at scale, cache segment counts monthly.
