# StageZero validation kit — run run-20261012-080239-b7eb87

**Idea:** AI agent that chases unpaid invoices for independent consultants

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Fractional CFO firms struggle to recover unpaid invoices from clients in a timely manner because follow-up requires persistent, personalized outreach that pulls senior practitioners away from billable advisory work; the current workaround is manual email and phone follow-up by the CFO or an admin, which costs billable hours, delayed cash flow, and strained client relationships. Hypothesis: an AI agent that autonomously sequences, personalizes, and escalates invoice follow-up communications removes that time and cash-flow cost for fractional CFO firms managing collections across multiple client engagements.

## Customer segments (ranked)

| # | Segment | Companies | Competitors | Pain signals | Priority |
|---|---------|-----------|-------------|--------------|----------|
| 1 | fractional-cfo-firms | 1487124 | 2089 | 1 | 70 |
| 2 | independent-accounting-practices | 169908 | 2089 | 1 | 43 |
| 3 | boutique-creative-agencies | 68916 | 2089 | 1 | 41 |

### fractional-cfo-firms
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Financial Services', 'Management Consulting']}]`
- Sample companies: AADI INDUSTRIES LIMITED, AAGAM CAPITAL LIMITED
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 70/100 — Fractional operators own collections for many clients; leverage per saved hour is highest

### independent-accounting-practices
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Accounting', 'Bookkeeping']}, {'field': 'basic_info.employee_count_range', 'type': 'in', 'value': ['2-10']}]`
- Sample companies: Zenday, Taxo Consultancy Services, VNL Limited
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 43/100 — Invoicing and collections are core recurring pain for billable-hours firms

### boutique-creative-agencies
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Marketing and Advertising', 'Design']}]`
- Sample companies: New Light, Mygubbi, brandis
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 41/100 — Retainer billing disputes are common and visible in hiring signals (billing/invoice roles)

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

- `ev-company-independent-accounting-practices` crustdata /company/search — 169908 results (segment size); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Accounting', 'Bookkeeping']}, {'field': 'basic_info.employee_count_range', 'type': 'in', 'value': ['2-10']}], 'limit': 25}`
- `ev-company-fractional-cfo-firms` crustdata /company/search — 1487124 results (segment size); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Financial Services', 'Management Consulting']}], 'limit': 25}`
- `ev-company-boutique-creative-agencies` crustdata /company/search — 68916 results (segment size); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Marketing and Advertising', 'Design']}], 'limit': 25}`

## Guardrail notes
- guardrail PASS

Estimated model cost for this run: $0.0311
