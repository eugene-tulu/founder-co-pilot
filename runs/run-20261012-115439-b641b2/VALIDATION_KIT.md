# StageZero validation kit — run run-20261012-115439-b641b2

**Idea:** AI agent that chases unpaid invoices for independent consultants

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Independent accounting practices struggle to collect on unpaid invoices because chasing late-paying clients requires dedicated staff time that pulls skilled accountants away from billable work; the current workaround is hiring specialist roles such as Accounts Receivable Specialists and Billing Coordinators to handle collections calls and AR aging follow-up, which costs recurring headcount expense and overhead across a segment of 1,284 firms where 30% of sampled practices have embedded this function directly into job descriptions. Hypothesis: an AI agent that autonomously executes invoice follow-up sequences, escalation reminders, and collections outreach removes the need for dedicated AR staffing for independent accounting practices that cannot justify a full-time collections hire but are losing revenue to payment delays.

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
1. Walk me through the last time a client invoice went past 30 days — what exactly did you do, step by step, to follow up on it?
1. In the past 12 months, how many hours did you or your staff spend on chasing overdue invoices, and how did you track that time?
1. Tell me about the most recent client you wrote off as uncollectable — what happened, and how much was the invoice for?
1. What tools or systems did you actually use the last time you sent a payment reminder — email, phone, accounting software, something else?
1. Describe the last time you hired or considered hiring someone specifically to handle collections or billing follow-up — what triggered that decision?
1. When a client last disputed or ignored an invoice, what did you do to resolve it, and how long did that take from start to finish?
1. How did you handle the awkwardness the last time you had to personally call a long-term client about an overdue balance — what did you say and how did it affect the relationship?
1. What did your collections follow-up process look like six months ago versus today — what changed and why did you change it?
1. The last time you reviewed your accounts receivable aging report, what was the total dollar amount sitting beyond 60 days, and what action did you take that same day?
1. Have you ever lost a client because of how you pursued an overdue invoice — what happened and what would you have done differently?

### fractional-cfo-firms
1. Walk me through the last time one of your clients had a significantly overdue invoice — what actually happened from the moment you noticed it was late to when it got resolved?
1. How did you handle collections follow-up for overdue client invoices last month — who did it, and how much time did they spend on it?
1. Tell me about the last client you lost or almost lost because of an awkward conversation around an unpaid invoice — what did that situation look like?
1. What tools or systems did your team actually use the last time they ran a collections cycle — spreadsheets, your accounting software, emails, phone calls?
1. Describe the most recent hire you made whose responsibilities included collections or accounts receivable follow-up — what did that role cost you and what problem were you trying to solve?
1. When a client's invoice hit 60 days overdue in the past year, what was the step-by-step process your team followed, and who owned each step?
1. Think about the last time a consultant on your team had to stop billable work to chase a payment — how long did that take and how did it affect their utilization?
1. Has a client ever pushed back or ended a relationship after receiving a collections follow-up from your firm — what happened and how did you handle it?
1. What did your team actually do the last time they had more than five clients with outstanding invoices simultaneously — how did they prioritize and execute?
1. In the last quarter, did you turn down a new client engagement or delay onboarding because your team's capacity was tied up in administrative work like collections — what was the situation?

### boutique-creative-agencies
1. Walk me through the last time a client invoice went past its due date — what exactly did you do, step by step, to follow up on it?
1. In the past 12 months, how many invoices did you end up writing off or settling for less than the full amount because chasing them felt too costly or awkward?
1. Tell me about the most uncomfortable moment you've had with a client specifically because of a payment conversation — what happened and how did you handle it?
1. What tools or systems did you actually use last month to track which invoices were overdue — can you show me what that looked like?
1. How much time did you or someone on your team spend last month on invoice follow-up activities — emails, calls, reminders — and who specifically was doing that work?
1. Did you ever lose a client or damage a relationship because of how a payment chase was handled — what went wrong?
1. When you last hired or considered hiring someone for a studio manager or finance role, how much of the job description was about chasing payments versus other responsibilities?
1. Describe the last time a client gave you a reason or excuse for not paying on time — what did you say back to them and what was the outcome?
1. Have you ever used a third-party service — a collections agency, a lawyer, a factoring company — to recover an unpaid invoice, and what did that cost you in fees, time, or the client relationship?
1. Walk me through how you decided what payment terms to put in your last three client contracts — did late payment penalties come up, and if so, have you ever actually enforced them?

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

Estimated model cost for this run: $0.0225
