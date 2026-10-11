# StageZero validation kit — run run-20261012-003954-207445

**Idea:** AI agent that chases unpaid invoices for independent consultants

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Independent Accounting Practices firms struggle to get paid on time because invoice chasing is manual, interrupt-driven work; the current workaround is hiring AR/collections staff or ignoring aging invoices, which costs cash flow and hours. Hypothesis: an agent that chases unpaid invoices removes that cost, starting with 'independent-accounting-practices'.

## Customer segments (ranked)

| # | Segment | Companies | Competitors | Pain signals | Priority |
|---|---------|-----------|-------------|--------------|----------|
| 1 | independent-accounting-practices | 1284 | 41 | 3 | 99 |
| 2 | boutique-creative-agencies | 968 | 23 | 2 | 77 |
| 3 | fractional-cfo-firms | 217 | 12 | 1 | 44 |

### independent-accounting-practices
- ICP filters: `[{'field': 'industries', 'type': 'in', 'value': ['accounting', 'bookkeeping']}]`
- Sample companies: Ledgerline CPA, Northgate Bookkeeping, Books & Bell LLP
- Pain signal: job posting: 'Accounts Receivable Specialist - collections calls' at Northgate Bookkeeping
- Pain signal: job posting: 'Billing Coordinator' at Ledgerline CPA
- Pain signal: 3 of 10 sampled firms list AR aging follow-up in job descriptions
- Priority 99/100 — Invoicing and collections are core recurring pain for billable-hours firms

### boutique-creative-agencies
- ICP filters: `[{'field': 'industries', 'type': 'in', 'value': ['marketing and advertising', 'design']}]`
- Sample companies: Studio Meridian, Fold Creative, North & Yarrow
- Pain signal: job posting: 'Studio Manager - invoicing and client billing' at Studio Meridian
- Pain signal: job posting: 'Finance Manager (agency)' at Fold Creative
- Priority 77/100 — Retainer billing disputes are common and visible in hiring signals (billing/invoice roles)

### fractional-cfo-firms
- ICP filters: `[{'field': 'industries', 'type': 'in', 'value': ['financial services', 'management consulting']}]`
- Sample companies: Trellis CFO Group, Part-Time Controller Co
- Pain signal: job posting: 'Client Accountant - month-end close and collections' at Trellis CFO Group
- Priority 44/100 — Fractional operators own collections for many clients; leverage per saved hour is highest

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

**proceed**

## Evidence

- `ev-company-independent-accounting-practices` offline-fixture (demo mode, not live Crustdata data) — 1284 results (segment size); query `{'filters': [{'field': 'industries', 'type': 'in', 'value': ['accounting', 'bookkeeping']}]}`
- `ev-company-fractional-cfo-firms` offline-fixture (demo mode, not live Crustdata data) — 217 results (segment size); query `{'filters': [{'field': 'industries', 'type': 'in', 'value': ['financial services', 'management consulting']}]}`
- `ev-company-boutique-creative-agencies` offline-fixture (demo mode, not live Crustdata data) — 968 results (segment size); query `{'filters': [{'field': 'industries', 'type': 'in', 'value': ['marketing and advertising', 'design']}]}`

## Guardrail notes
- guardrail PASS

Estimated model cost for this run: $0.0000
