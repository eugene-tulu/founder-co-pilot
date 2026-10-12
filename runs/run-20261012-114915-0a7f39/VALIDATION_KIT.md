# StageZero validation kit — run run-20261012-114915-0a7f39

**Idea:** AI agent that chases unpaid invoices for independent consultants

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Independent accounting practices struggle to collect on unpaid invoices because chasing overdue accounts requires dedicated staff time that pulls skilled bookkeepers and CPAs away from billable client work; the current workaround is hiring specialist roles such as Accounts Receivable Specialists and Billing Coordinators to handle collections calls and AR aging follow-up, which costs recurring headcount expense and overhead across a segment of 1,284 firms where 30% of sampled practices have already embedded this function into job descriptions. Hypothesis: an AI agent that autonomously monitors invoice aging, sends escalating follow-up communications, and logs collection activity removes the need for dedicated AR staffing for independent accounting practices that lack the scale to justify a full-time collections hire.

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
1. How many hours did you or your staff spend last month on any kind of collections activity — calls, emails, reminders — across all overdue accounts?
1. Tell me about the most recent hire or contractor you brought on specifically to handle billing follow-up or accounts receivable — what triggered that decision?
1. What tools or software did you actually use the last time you sent a payment reminder to an overdue client — walk me through the process?
1. Think back to a client you eventually wrote off as uncollectable in the past year — how long did you chase that invoice before giving up, and what did that process look like?
1. How did you handle the last situation where a client disputed an invoice or went silent after repeated follow-ups?
1. When did you last calculate how much in outstanding receivables you had at any one time, and what number did you find?
1. Describe the last time a collections task fell through the cracks — what happened and what was the outcome?
1. What did you actually do the last time you had to follow up with a long-term client who was late paying — did you treat it differently than a new client, and how?
1. Have you ever lost a client relationship specifically because of how a collections conversation went — what happened?

### fractional-cfo-firms
1. Walk me through the last time one of your clients had a significant overdue receivables problem — what actually happened and how did your team get pulled into it?
1. How did your staff spend their time last month on collections-related work across your client portfolio — what did that look like day to day?
1. Tell me about the last invoice that went past 60 days for one of your clients — what steps did you or your team take to chase it, and in what order?
1. When you last hired or considered hiring someone specifically to handle client collections, what was the breaking point that triggered that decision?
1. Describe the tools or systems your team used most recently to track and follow up on aging receivables across multiple clients — how did that actually work in practice?
1. Think about the last time a client pushed back on a collections follow-up you sent on their behalf — what happened and how did you handle it?
1. How did you last report on collections status to a client — what did you pull together, how long did it take, and what did the client say?
1. Tell me about a time a client relationship got awkward or strained because of overdue invoices — how did your firm navigate that?
1. When you last onboarded a new fractional CFO client, how did you assess and set up their AR and collections process, and what problems did you run into?
1. Describe the last time you lost billable hours or had to write off time because of how much effort collections work consumed across your client accounts.

### boutique-creative-agencies
1. Walk me through the last time a client invoice went past its due date — what exactly did you do, and in what order?
1. How many hours did you or someone on your team spend last month on any kind of follow-up related to outstanding payments?
1. Tell me about the most uncomfortable client conversation you've had around a late payment — how did it start and how did it end?
1. What tools or systems did you actually use the last time you chased an overdue invoice — email, phone, accounting software, something else?
1. Have you ever written off or discounted an invoice just to avoid the awkwardness of continuing to chase it — what happened there?
1. When you hired or considered hiring someone for a studio manager or finance role, how much of the job description was driven by billing and collections headaches specifically?
1. Describe the last time a late payment actually disrupted your ability to pay a freelancer, supplier, or your own salary — what did you do to bridge that gap?
1. How did you decide on your current payment terms, and have you ever changed them after a specific bad experience with a client?
1. Tell me about a client you lost or nearly lost because of how a billing dispute or collections conversation was handled — what went wrong?
1. What did the last 90-days-overdue invoice cost you in total — including any time spent, relationship damage, or cash flow workarounds you had to put in place?

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

Estimated model cost for this run: $0.0215
