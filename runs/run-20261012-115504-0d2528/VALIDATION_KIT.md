# StageZero validation kit — run run-20261012-115504-0d2528

**Idea:** AI agent that chases unpaid invoices

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Independent accounting practices struggle to collect on unpaid invoices because chasing overdue balances requires persistent, time-consuming outreach that pulls skilled staff away from billable client work; the current workaround is hiring dedicated AR or billing coordinators to make collections calls and manage aging follow-up, which costs salary overhead for a role that generates no direct revenue and is common enough that 3 in 10 sampled firms bake it into job descriptions. Hypothesis: an AI agent that autonomously identifies overdue invoices, sends escalating follow-up communications, and logs responses removes that staffing cost and reclaims billable hours for the 1,284 independent accounting practices in this segment.

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
1. Have you ever hired or considered hiring someone specifically to handle collections calls — what happened when you looked into that?
1. Describe the last client relationship that got awkward or damaged because of a collections conversation — how did that play out?
1. How did you decide when to stop chasing a late invoice yourself and either write it off or escalate it to a collections agency?
1. What did your outstanding receivables balance look like at the end of last quarter, and how does that compare to what you consider normal or acceptable?
1. Tell me about a time a client gave you a reason or excuse for not paying — how did you handle that conversation and what was the outcome?
1. Have you ever lost a client because of how a collections follow-up was handled — what happened leading up to that?

### fractional-cfo-firms
1. Walk me through the last time you had to chase a client's unpaid invoice — what did that process actually look like from start to finish?
1. In the past 90 days, how many hours did your team spend on collections-related follow-up across your client portfolio?
1. Tell me about the last invoice that went past 60 days overdue — what steps did you take, and how did it ultimately get resolved?
1. When a client's customer goes silent on an overdue invoice, what has your team actually done to escalate it without damaging the client relationship?
1. Have you ever lost a fractional CFO engagement because collections work was consuming too much of your team's capacity — what happened?
1. What tools or systems did you use the last time you ran a collections workflow for a client, and what did that setup cost you?
1. Describe the last time you hired or considered hiring someone specifically to handle client collections — what triggered that decision?
1. When you onboard a new fractional CFO client, how have you handled setting expectations around who owns the collections process?
1. Tell me about a situation where a client's cash flow crisis was directly tied to slow collections — how did your firm respond and what did it cost you in time?
1. Have you ever turned down a client or dropped a client because their collections volume was too burdensome for your team — what was the situation?

### boutique-creative-agencies
1. Walk me through the last time a client paid you late — what actually happened from the moment the invoice was due to when you finally got paid?
1. How did you handle chasing that overdue payment — who did it, what did they do, and how long did it take out of their week?
1. What tools or systems did you use the last time you followed up on an unpaid invoice — email, phone, accounting software, something else?
1. Tell me about the most awkward or difficult collections situation you dealt with in the past year — how did you navigate it with the client relationship in mind?
1. When you last hired or considered hiring someone for a studio manager or finance role, how much of the job description was specifically about chasing payments and managing billing?
1. How much time did your team collectively spend last month on invoice follow-up, and who specifically was doing that work?
1. Describe the last invoice that went more than 60 days overdue — what was the sequence of steps you took, and what was the outcome?
1. Have you ever written off or discounted an invoice just to avoid the discomfort of continuing to chase a client — what happened there?
1. What did your cash flow situation actually look like during a period when several clients were paying late — how did you manage it operationally?
1. When a client pushed back or disputed an invoice, what did you do step by step, and how much of your own time did it consume before it was resolved?

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

Estimated model cost for this run: $0.0205
