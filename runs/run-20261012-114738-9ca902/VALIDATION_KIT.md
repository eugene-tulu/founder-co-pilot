# StageZero validation kit — run run-20261012-114738-9ca902

**Idea:** AI agent that chases unpaid invoices

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Independent accounting practices struggle to collect on unpaid invoices because chasing overdue accounts requires persistent, time-consuming outreach that pulls skilled staff away from billable work; the current workaround is hiring dedicated AR or billing coordinators to make collections calls and manage aging reports, which costs salary overhead for a non-revenue-generating role and reduces the capacity of qualified accountants to serve clients. Hypothesis: an AI agent that autonomously monitors invoice aging, sends escalating follow-up communications, and logs responses removes that staffing cost and time drain for independent accounting practices.

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
1. Tell me about the most frustrating collections situation you dealt with in the past year — how did it play out from start to finish?
1. What tools or systems did you actually use the last time you sent a payment reminder — email, phone, your accounting software, something else?
1. Have you ever hired or considered hiring someone specifically to handle collections calls — what happened when you explored that?
1. What was the total dollar value of invoices you wrote off as uncollectable in the last 12 months, and how did you decide when to give up?
1. Describe the last time a client relationship got awkward or damaged because of a collections conversation — how did you handle it?
1. When a client went silent on an overdue invoice, what was the sequence of steps you actually took before escalating or giving up?
1. How did you track which overdue invoices had been followed up on and which hadn't — show me what that process looked like in practice?
1. Tell me about a time you lost a client or nearly lost one during the collections process — what did that cost you beyond the unpaid invoice itself?

### fractional-cfo-firms
1. Walk me through the last time you had to chase a client's unpaid invoice — what did that process actually look like from start to finish?
1. In the past 90 days, how many hours did your team spend on collections-related follow-up across your client portfolio?
1. Tell me about the last invoice that went past 60 days overdue — what steps did you take, and who owned each step?
1. What tools or systems did you use the last time you sent a collections follow-up — email, phone, accounting software, something else?
1. Have you ever lost a client relationship because of how collections were handled — what happened?
1. When you last hired or considered hiring someone, how much of that role was expected to cover collections and AR follow-up specifically?
1. Describe the most awkward or difficult collections situation you personally dealt with in the last year — how did you resolve it?
1. How did you track which invoices needed follow-up last month — what did that workflow look like day to day?
1. Have you ever had a client engagement where AR aging got bad enough that it affected your own firm's deliverables or relationship — what did you do?
1. What did you try before settling on your current collections process — what made you abandon those earlier approaches?

### boutique-creative-agencies
1. Walk me through the last time a client paid you late — what actually happened from the moment the invoice was due to when you finally got the money?
1. How did you handle chasing that overdue payment — who did it, what did they do, and how long did it take out of their week?
1. What tools or systems did you use the last time you sent a follow-up on an unpaid invoice — email, phone, accounting software, something else?
1. Tell me about the most awkward or difficult collections situation you've had with a client in the past year — how did you navigate it?
1. When you last hired or considered hiring someone for a studio manager or finance role, how much of the job description was specifically about chasing payments and managing billing?
1. How much time did your team collectively spend last month on invoice follow-ups — can you walk me through where those hours actually went?
1. Have you ever lost a client or damaged a relationship because of how a payment chase was handled — what happened?
1. What did you do the last time a client disputed or ignored an invoice entirely — who got involved and what was the resolution process?
1. Have you ever written off an invoice as uncollectable rather than continuing to chase it — what was the amount and what made you give up?
1. When you last reviewed your accounts receivable, what was the oldest unpaid invoice sitting there, and what steps had already been taken to collect it?

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
