# StageZero validation kit — run run-20261012-114939-1c03da

**Idea:** AI agent that chases unpaid invoices

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Independent accounting practices struggle to collect on unpaid invoices because chasing overdue balances requires persistent, time-consuming outreach that pulls skilled staff away from billable client work; the current workaround is hiring dedicated AR or billing coordinators to make collections calls and manage aging reports, which costs salary overhead for a role that generates no direct revenue and consumes capacity that could otherwise serve clients. Hypothesis: an AI agent that autonomously monitors invoice aging and executes follow-up communications removes that staffing cost and time drain for independent accounting practices.

## Customer segments (ranked)

| # | Segment | Companies | Competitors | Pain signals | Priority |
|---|---------|-----------|-------------|--------------|----------|
| 1 | independent-accounting-practices | 1284 | 41 | 3 | 99 |
| 2 | boutique-creative-agencies | 968 | 23 | 2 | 77 |
| 3 | fractional-cfo-firms | 217 | 12 | 1 | 44 |

### independent-accounting-practices
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Accounting', 'Bookkeeping']}, {'field': 'basic_info.employee_count_range', 'type': 'in', 'value': ['2-10']}]`
- Sample companies: Ledgerline CPA, Northgate Bookkeeping, Books & Bell LLP
- Pain signal: job posting: 'Accounts Receivable Specialist - collections calls' at Northgate Bookkeeping
- Pain signal: job posting: 'Billing Coordinator' at Ledgerline CPA
- Pain signal: 3 of 10 sampled firms list AR aging follow-up in job descriptions
- Priority 99/100 — Invoicing and collections are core recurring pain for billable-hours firms

### boutique-creative-agencies
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Marketing and Advertising', 'Design']}]`
- Sample companies: Studio Meridian, Fold Creative, North & Yarrow
- Pain signal: job posting: 'Studio Manager - invoicing and client billing' at Studio Meridian
- Pain signal: job posting: 'Finance Manager (agency)' at Fold Creative
- Priority 77/100 — Retainer billing disputes are common and visible in hiring signals (billing/invoice roles)

### fractional-cfo-firms
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Financial Services', 'Management Consulting']}]`
- Sample companies: Trellis CFO Group, Part-Time Controller Co
- Pain signal: job posting: 'Client Accountant - month-end close and collections' at Trellis CFO Group
- Priority 44/100 — Fractional operators own collections for many clients; leverage per saved hour is highest

## Mom Test interview scripts

### independent-accounting-practices
1. Walk me through the last time you had an invoice go more than 30 days past due — what exactly did you do to follow up on it?
1. How much time did you or your staff spend last month on chasing overdue payments, and who specifically was doing that work?
1. Tell me about the most frustrating collections situation you dealt with in the past year — what made it so difficult?
1. What tools or systems did you actually use the last time you sent a payment reminder — email, phone, your accounting software, something else?
1. Have you ever hired or considered hiring someone specifically to handle collections calls — what happened when you explored that?
1. Describe the last client relationship that got awkward or damaged because of a conversation about an unpaid invoice — how did that play out?
1. How did you decide when to stop chasing a late invoice and write it off — can you give me a specific recent example?
1. What did your outstanding receivables balance look like at the end of last quarter, and how did that compare to what you expected?
1. Have you ever lost revenue because you were too uncomfortable or too busy to follow up on a late payment — what was the situation?
1. When you last brought on a new client, what payment terms did you set and what actually happened with their first few invoices?

### fractional-cfo-firms
1. Walk me through the last time you had to chase a client's unpaid invoice — what did that process actually look like from start to finish?
1. In the past 90 days, how many hours did your team spend on collections-related follow-up across your client portfolio?
1. Tell me about the last invoice that went past 60 days overdue — what steps did you take, and who on your team owned each step?
1. What tools or systems did you use the last time you sent a collections follow-up — email, phone, accounting software, something else?
1. Have you ever lost a client relationship because of how collections were handled — what happened?
1. When you last hired or considered hiring someone to help with month-end close and collections, what was the specific breaking point that triggered that decision?
1. Describe the most recent time a client's cash flow was materially hurt by slow receivables — how did you find out, and what did you do about it?
1. What did you actually do the last time a debtor ignored two or more follow-up attempts — did you escalate, write it off, or something else?
1. How did you track which invoices were overdue across all your clients last month — can you show me what that looked like?
1. Think back to the last time you onboarded a new fractional CFO client — how did collections responsibilities get defined, and what broke down in the first 90 days?

### boutique-creative-agencies
1. Walk me through the last time a client paid you late — what actually happened from the moment the invoice was due to when you finally got paid?
1. How did you handle chasing that overdue payment — who did it, what did they do, and how long did it take them?
1. What was the most recent invoice you wrote off as uncollectable — what led to that decision?
1. Last month, roughly how many hours did you or your team spend on invoice follow-up across all clients?
1. Tell me about a time a late payment caused you to delay paying a freelancer or supplier — how did you manage that situation?
1. When you last hired or considered hiring someone for a studio manager or finance role, how much of the job description was about chasing payments specifically?
1. What tools or systems have you actually tried to manage overdue invoices — how did you set them up and why did you stop or keep using them?
1. Describe the last awkward conversation you had with a client about an unpaid invoice — how did you approach it and what was the outcome?
1. Has a late-paying client ever affected your decision to work with them again — what happened and how did you handle it at the time?
1. What did your cash flow situation look like during your worst month for late payments in the past year — what did you have to do differently because of it?

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

- `ev-company-independent-accounting-practices` offline-fixture (demo mode, not live Crustdata data) — 1284 results (segment size); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Accounting', 'Bookkeeping']}, {'field': 'basic_info.employee_count_range', 'type': 'in', 'value': ['2-10']}]}`
- `ev-company-fractional-cfo-firms` offline-fixture (demo mode, not live Crustdata data) — 217 results (segment size); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Financial Services', 'Management Consulting']}]}`
- `ev-company-boutique-creative-agencies` offline-fixture (demo mode, not live Crustdata data) — 968 results (segment size); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Marketing and Advertising', 'Design']}]}`

## Guardrail notes
- guardrail PASS

## Recovery

- At least one tool failure occurred during this run and the agent recovered (see run_state.json).

Estimated model cost for this run: $0.0198
