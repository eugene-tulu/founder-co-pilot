# StageZero validation kit — run run-20261012-075804-fec6da

**Idea:** AI agent that chases unpaid invoices for independent consultants

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Independent accounting practices struggle to recover payment on overdue client invoices because following up manually is time-consuming and professionally awkward; the current workaround is sending reminder emails and making phone calls themselves, which costs billable hours diverted away from client work and risks damaging client relationships. Hypothesis: an AI agent that autonomously sends escalating, professionally toned payment chasers on behalf of the practice removes that time and relationship cost for independent accounting practices.

## Customer segments (ranked)

| # | Segment | Companies | Competitors | Pain signals | Priority |
|---|---------|-----------|-------------|--------------|----------|
| 1 | independent-accounting-practices | 0 | 0 | 1 | 40 |
| 2 | fractional-cfo-firms | 0 | 0 | 1 | 40 |
| 3 | boutique-creative-agencies | 0 | 0 | 1 | 40 |

### independent-accounting-practices
- ICP filters: `[{'field': 'industries', 'type': 'in', 'value': ['accounting', 'bookkeeping']}]`
- Sample companies: n/a
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 40/100 — Invoicing and collections are core recurring pain for billable-hours firms
- Note: sized via degraded retry (live search unavailable)

### fractional-cfo-firms
- ICP filters: `[{'field': 'industries', 'type': 'in', 'value': ['financial services', 'management consulting']}]`
- Sample companies: n/a
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 40/100 — Fractional operators own collections for many clients; leverage per saved hour is highest
- Note: sized via degraded retry (live search unavailable)

### boutique-creative-agencies
- ICP filters: `[{'field': 'industries', 'type': 'in', 'value': ['marketing and advertising', 'design']}]`
- Sample companies: n/a
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 40/100 — Retainer billing disputes are common and visible in hiring signals (billing/invoice roles)
- Note: sized via degraded retry (live search unavailable)

## Mom Test interview scripts

### independent-accounting-practices
1. Walk me through the last time you had to deal with ai agent chases unpaid invoices independent consultants. What happened?
1. How much time did that take you and your team last month?
1. What do you currently use to handle ai agent chases unpaid invoices independent consultants?
1. What did you last pay for to solve this, and what made you decide it was worth it?
1. Who else on your team touches this problem?
1. When was the last time this cost you money directly?
1. What have you already tried that did not work?
1. How do you know when this problem has gotten worse?
1. If this were solved overnight, what would you do with the saved time?
1. What would have to be true for you to pay for a fix this month?

### fractional-cfo-firms
1. Walk me through the last time you had to deal with ai agent chases unpaid invoices independent consultants. What happened?
1. How much time did that take you and your team last month?
1. What do you currently use to handle ai agent chases unpaid invoices independent consultants?
1. What did you last pay for to solve this, and what made you decide it was worth it?
1. Who else on your team touches this problem?
1. When was the last time this cost you money directly?
1. What have you already tried that did not work?
1. How do you know when this problem has gotten worse?
1. If this were solved overnight, what would you do with the saved time?
1. What would have to be true for you to pay for a fix this month?

### boutique-creative-agencies
1. Walk me through the last time you had to deal with ai agent chases unpaid invoices independent consultants. What happened?
1. How much time did that take you and your team last month?
1. What do you currently use to handle ai agent chases unpaid invoices independent consultants?
1. What did you last pay for to solve this, and what made you decide it was worth it?
1. Who else on your team touches this problem?
1. When was the last time this cost you money directly?
1. What have you already tried that did not work?
1. How do you know when this problem has gotten worse?
1. If this were solved overnight, what would you do with the saved time?
1. What would have to be true for you to pay for a fix this month?

## Experiment plan (this week)

- Recruit 10 founders from the top segment for free 20-minute interviews this week (warm channel first: past email contacts, LinkedIn 1st-degree).
- Run the Mom Test script; capture past behaviour, never opinions.
- Give the top 3 most-pained interviewees the workflow done-for-them by hand (concierge), free, once.
- Log every interview against the kill criteria below.

## Graduation gates

- At least 8 of 10 interviews confirm the pain is recurring and already costs measurable time/money
- At least 5 interviewees accept a second, free concierge run unprompted
- At least 3 interviewees describe the current, specific workaround in detail

## Kill criteria

- Fewer than 4 of 10 interviewees recognise the pain unprompted
- Interviewees already solved it well enough that a paid tool feels unnecessary
- The segment keeps describing it as a nice-to-have, not a recurring cost

## Decision

**pivot**

## Evidence

- `ev-company-independent-accounting-practices` crustdata /company/search — 0 results (degraded retry); query `{'filters': [{'field': 'industries', 'type': 'in', 'value': ['accounting', 'bookkeeping']}], 'limit': 25}`
- `ev-company-fractional-cfo-firms` crustdata /company/search — 0 results (degraded retry); query `{'filters': [{'field': 'industries', 'type': 'in', 'value': ['financial services', 'management consulting']}], 'limit': 25}`
- `ev-company-boutique-creative-agencies` crustdata /company/search — 0 results (degraded retry); query `{'filters': [{'field': 'industries', 'type': 'in', 'value': ['marketing and advertising', 'design']}], 'limit': 25}`

## Guardrail notes
- guardrail PASS

## Recovery

- At least one tool failure occurred during this run and the agent recovered (see run_state.json).

Estimated model cost for this run: $0.0272
