# StageZero validation kit — run run-20261012-114615-c42fb3

**Idea:** AI agent that chases unpaid invoices for independent consultants

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Independent accounting practices struggle to collect on unpaid invoices because chasing late-paying clients requires dedicated staff time that pulls skilled accountants away from billable work; the current workaround is hiring specialist roles such as Accounts Receivable Specialists and Billing Coordinators to handle collections calls and AR aging follow-up, which costs recurring headcount expense and overhead across a segment of 1,284 firms where 30% already embed this function directly into job descriptions. Hypothesis: an AI agent that autonomously monitors invoice aging, sends escalating follow-up communications, and logs collection activity removes the need for dedicated AR collections headcount for independent accounting practices that lack the scale to justify a full-time specialist but face consistent late-payment friction.

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
1. How did you handle the awkwardness the last time you had to chase a long-term client for an overdue payment — what did you actually say or send?
1. What did your collections process look like six months ago versus today — has anything changed, and what prompted that change?
1. The last time you had more than five invoices overdue at once, how did you prioritize which ones to chase first, and what was the outcome?
1. Have you ever lost a client relationship specifically because of a collections conversation — what happened and how did you handle it afterward?

### fractional-cfo-firms
1. Walk me through the last time one of your clients had a significant overdue receivables problem — what actually happened and how did your team get pulled into it?
1. How did your staff spend their time last month on collections-related work across your client portfolio — what did that look like day to day?
1. Tell me about the last invoice that went past 60 days for one of your clients — what steps did you or your team take to chase it, and in what order?
1. Have you ever lost a client engagement or had scope creep because collections work consumed more of your team's capacity than expected — what happened?
1. When you hired or considered hiring someone specifically to handle client-facing collections and AR follow-up, what broke down that made that role necessary?
1. Describe the tools your team currently uses to track and follow up on overdue invoices across multiple clients — how did you end up with that setup?
1. Has a client ever pushed back or complained about how collections were being handled on their behalf — what was the situation and how did you resolve it?
1. What did your team actually do the last time a client's customer went completely unresponsive to payment reminders — walk me through each step?
1. How have you tried to standardize the collections process across your client base, and where did that break down in practice?
1. Tell me about a time when slow collections directly affected a client's cash flow forecast you were managing — how did you find out and what did you do about it?

### boutique-creative-agencies
1. Walk me through the last time a client payment came in later than the due date — what actually happened from the moment you noticed it was overdue?
1. How did you handle chasing that late payment — who did it, what did they do, and how long did it take?
1. What tools or systems did you use the last time you sent a payment reminder to a client?
1. Tell me about the most uncomfortable collections situation you dealt with in the past year — how did it play out?
1. When you last hired or considered hiring someone for a studio manager or finance role, how much of the job description was specifically about chasing invoices and managing billing?
1. How much time did your team collectively spend last month on anything related to outstanding invoices — following up, reconciling, escalating?
1. Have you ever lost a client relationship or damaged one because of how a payment dispute or overdue invoice was handled — what happened?
1. What did you do the last time a client disputed an invoice or went silent after one was sent?
1. Can you show me or describe the process you currently have documented — if any — for what happens when an invoice hits 30, 60, or 90 days overdue?
1. In the past 12 months, did you write off any invoices as uncollectable — how much, and what led you to give up on chasing them?

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
