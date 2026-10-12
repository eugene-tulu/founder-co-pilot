# StageZero validation kit — run run-20261012-114715-955e43

**Idea:** AI agent that chases unpaid invoices for independent consultants

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Independent accounting practices struggle to collect on unpaid invoices because chasing late-paying clients requires dedicated staff time that pulls skilled accountants away from billable work; the current workaround is hiring specialist roles such as Accounts Receivable Specialists and Billing Coordinators to handle collections calls and AR aging follow-up, which costs recurring headcount expense and overhead across a segment of 1,284 firms where 30% of sampled practices have embedded this function directly into job descriptions. Hypothesis: an AI agent that autonomously executes invoice follow-up sequences removes that staffing cost and distraction for independent accounting practices that cannot justify a full-time collections hire but are losing revenue to aging receivables.

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
1. Walk me through the last time a client invoice went more than 30 days past due — what exactly did you do, step by step, to follow up on it?
1. In the past six months, how many hours did you or your staff spend on chasing overdue invoices, and how did you track that time?
1. Tell me about the most recent client you wrote off as uncollectable — what happened, and how much was the outstanding balance?
1. What tools or systems did you actually use the last time you sent a payment reminder — email, phone, accounting software, something else?
1. Describe the last time you hired or considered hiring someone specifically to handle collections or billing follow-up — what triggered that decision?
1. When a client last disputed or ignored an invoice, what did you do to resolve it, and how long did the whole process take?
1. How did you handle the awkwardness the last time you had to chase a long-term client for an overdue payment — what did you actually say or send?
1. Think back to the last quarter — which invoices took the longest to collect, and what was different about those clients or situations compared to ones who paid on time?
1. What workarounds have you put in place to reduce late payments — things like deposit requirements, payment terms changes, or late fees — and when did you actually start doing those?
1. The last time you posted or considered posting a job for an accounts receivable or billing role, what specific tasks were you hoping that person would take off your plate?

### fractional-cfo-firms
1. Walk me through the last time one of your clients had a significantly overdue invoice — what actually happened from the moment you noticed it was late to when it got resolved?
1. How did you handle collections follow-up for overdue client invoices in the last quarter — who did it, how often, and what did that process look like?
1. Tell me about the most time-consuming collections situation you dealt with in the past six months — what made it drag on?
1. The last time an invoice went past 60 days, what specific steps did you or your team take, and roughly how many hours did it consume?
1. Have you ever lost a client relationship because of how a collections conversation was handled — what happened?
1. When you've hired or considered hiring staff to handle month-end close and collections together, what was the breaking point that made you decide you needed dedicated headcount for it?
1. What tools or software did you actually use the last time you chased a late payment — email, phone, your accounting system — and how did you decide which to use?
1. Describe the last time a client gave you a reason or excuse for not paying on time — how did you respond and how did that play out?
1. How did you track which invoices were overdue across all your clients last month — can you walk me through exactly what that looked like?
1. Have you ever written off or discounted an invoice rather than continue pursuing it — what led you to that decision and how much was involved?

### boutique-creative-agencies
1. Walk me through the last time a client payment came in later than the due date — what actually happened from the moment you noticed it was overdue?
1. How did you handle chasing that late payment — who did it, what did they do, and how long did it take?
1. What tools or systems did you use the last time you sent a payment reminder to a client?
1. Tell me about the most uncomfortable collections situation you dealt with in the past year — how did it play out?
1. When you last hired or considered hiring someone for a studio manager or finance role, how much of the job description was specifically about chasing invoices and managing client billing?
1. How much time did your team collectively spend last month on anything related to unpaid or overdue invoices — emails, calls, follow-ups?
1. Have you ever written off an invoice as uncollectable rather than continuing to chase it — what led to that decision?
1. What did you do the last time a client disputed or ignored an invoice — walk me through each step you took?
1. How have late payments affected your ability to pay your own team or freelancers on time in the past 12 months?
1. When you last looked at your accounts receivable, what was the oldest unpaid invoice, and what had you already tried to collect it?

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

Estimated model cost for this run: $0.0212
