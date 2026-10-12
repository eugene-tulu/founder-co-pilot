# StageZero validation kit — run run-20261012-115151-c1dc17

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
1. Walk me through the last time a client went more than 30 days past due on an invoice — what exactly did you do, step by step, to follow up?
1. How much time did you personally spend last month on any kind of invoice follow-up or collections activity across your client base?
1. Tell me about the most recent client you had to write off as uncollectable — what happened and how much was it for?
1. What tools or systems have you actually used to track which invoices are overdue — can you show me what that looks like today?
1. Have you ever hired or considered hiring someone specifically to handle collections or billing follow-up? What happened when you explored that?
1. Describe the last time you felt uncomfortable or avoided reaching out to a late-paying client — what did you do instead and how long did you wait?
1. How did you handle the last situation where a client disputed an invoice or went silent after you sent a reminder?
1. What did your collections process look like two years ago versus today — what changed and what prompted those changes?
1. Tell me about a client relationship that got awkward or damaged because of a conversation around an overdue payment — what did you do?
1. When you last looked at your accounts receivable aging report, what was the total dollar amount sitting beyond 60 days, and what actions had you already taken on those?

### fractional-cfo-firms
1. Walk me through the last time one of your clients had a significant overdue receivables problem — what actually happened and how did your team get pulled into it?
1. How did your staff spend their time last month on collections-related work across your client portfolio — what did that look like day to day?
1. Tell me about the last invoice that went past 60 days for one of your clients — what steps did you or your team take to chase it, and in what order?
1. Have you ever lost a client engagement or had scope creep because collections work consumed more of your team's capacity than expected — what happened?
1. What tools or processes did your team actually use in the last quarter to track and follow up on aging receivables across multiple clients simultaneously?
1. Describe the last time you had to hire or assign dedicated headcount specifically because collections and AR follow-up was overwhelming your existing staff?
1. When a client's customer went silent on an overdue invoice, what did your team actually do — walk me through the specific steps and how long it took?
1. How have you handled the awkward dynamic when your team had to chase a payment from someone who is also a key relationship for your client — what did you do?
1. What did your team charge or absorb in time costs last time a collections situation escalated to the point where it threatened a client's cash flow crisis?
1. Have you ever tried a third-party service, software, or outsourced solution to handle invoice follow-up for clients — what made you try it and what made you stop or continue?

### boutique-creative-agencies
1. Walk me through the last time a client invoice went past its due date — what exactly did you do, and in what order?
1. How many hours did you or someone on your team spend last month on any kind of follow-up related to outstanding payments?
1. Tell me about the most uncomfortable client conversation you've had around a late payment — how did it start and how did it end?
1. What tools or systems did you actually use the last time you chased an overdue invoice — email, phone, accounting software, something else?
1. Have you ever written off or discounted an invoice just to avoid the awkwardness of continuing to chase it — what happened?
1. When you hired or considered hiring someone for a studio manager or finance role, how much of the job description was driven by billing and collections headaches specifically?
1. Describe the last time a late payment actually disrupted your ability to pay a freelancer, supplier, or your own salary — what did you do to bridge that gap?
1. How did you decide on your current payment terms, and have you ever changed them after a specific bad experience with a client?
1. Tell me about a client you lost or nearly lost because of how a billing conversation was handled — what went wrong?
1. What did your collections process look like 12 months ago compared to today — what changed and what triggered that change?

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

Estimated model cost for this run: $0.0211
