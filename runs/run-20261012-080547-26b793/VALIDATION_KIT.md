# StageZero validation kit — run run-20261012-080547-26b793

**Idea:** AI agent that chases unpaid invoices for independent consultants

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

The evidence provided is insufficient to support a falsifiable problem statement. The pain signals explicitly flag that there is no job-title signal for invoice-related pain in the solo management consultant segment, there are no competitor signals to confirm an active market, and the company count is zero, meaning no real segment members were identified or validated. Writing a problem statement from this data would require fabricating facts rather than drawing on segment evidence. The hypothesis cannot be responsibly formed until primary research confirms that solo management consultants actually experience delayed invoice payment as a meaningful friction point, quantifies how much time or revenue is lost to chasing payments, and identifies what workaround they currently rely on, whether that is manual follow-up emails, accountants, or tools like FreshBooks or QuickBooks. Collect that evidence first, then resubmit.

## Customer segments (ranked)

| # | Segment | Companies | Competitors | Pain signals | Priority |
|---|---------|-----------|-------------|--------------|----------|
| 1 | solo-management-consultants | 0 | 0 | 1 | 40 |
| 2 | boutique-it-and-tech-consultancies | 0 | 0 | 1 | 40 |
| 3 | independent-financial-and-accounting-advisors | 0 | 0 | 1 | 40 |

### solo-management-consultants
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Business Consulting and Services']}]`
- Sample companies: n/a
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 40/100 — Solo consultants lack a dedicated finance or AR team, so chasing overdue invoices means awkward client conversations that risk the relationship. Late payments directly threaten personal cash flow with no buffer, making automated follow-up extremely valuable.
- Note: sized via degraded retry (live search unavailable)

### boutique-it-and-tech-consultancies
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Computer and Network Security', 'IT Services and IT Consulting', 'Technology, Information and Internet', 'Technology, Information and Media']}]`
- Sample companies: n/a
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 40/100 — With multiple concurrent client engagements and invoices in flight, even a small team gets overwhelmed tracking payment statuses. Founders are focused on delivery, not collections, and a single late enterprise payment can create serious cash-flow gaps.
- Note: sized via degraded retry (live search unavailable)

### independent-financial-and-accounting-advisors
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Accounting', 'Business Intelligence Platforms', 'Financial Services']}]`
- Sample companies: n/a
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 40/100 — Financial consultants bill on hourly or project bases and often serve SMB clients who pay slowly. The irony of an accountant with overdue invoices is real — they know the problem intimately but still lack time and tools to automate persistent, professional follow-up without damaging client trust.
- Note: sized via degraded retry (live search unavailable)

## Mom Test interview scripts

### solo-management-consultants
1. Walk me through the last time a client paid you late — what actually happened from the moment the invoice was due to when the money hit your account?
1. How many invoices did you send out in the last 90 days, and how many of those were paid after the due date?
1. What did you actually do the last time a client went more than two weeks past due — what steps did you take, in what order?
1. Tell me about the most uncomfortable follow-up conversation you had with a client over an unpaid invoice — how did you handle it?
1. How much time did you spend last month on any activity related to chasing, tracking, or following up on unpaid invoices?
1. Have you ever decided not to follow up on a late invoice, or to follow up less aggressively than you wanted to — what drove that decision?
1. What tools or systems did you use the last time you sent a payment reminder — walk me through exactly what you did?
1. Has a late-paying client ever affected your ability to cover your own expenses or take on new work — what happened?
1. Have you ever written off an invoice entirely rather than continue chasing it — what was the situation and how much was involved?
1. What did the last invoice follow-up message you sent actually say, and how long did it take you to write it?

### boutique-it-and-tech-consultancies
1. Walk me through the last time a client paid you late — what actually happened from the moment the invoice was due to when you finally got the money?
1. How many invoices did you have to follow up on more than once in the last three months, and roughly how much time did that take you?
1. What did you actually do the last time a client went silent after you sent an invoice — what steps did you take and in what order?
1. Tell me about the most uncomfortable collections situation you dealt with in the past year — how did you handle it and what was the outcome?
1. What tools or systems did you use the last time you chased a late payment — email, phone, accounting software, something else?
1. How did you decide when to escalate a late invoice to a more serious conversation or a third party — what triggered that decision last time?
1. Describe the last time a late payment actually affected your ability to cover business expenses or pay yourself — what did you do to bridge that gap?
1. When you last had multiple overdue invoices at once, how did you prioritize which ones to chase first and what did that process look like?
1. Have you ever written off an invoice as uncollectable — what happened leading up to that decision and how much was involved?
1. What did the follow-up communication you sent to a late-paying client last time actually say, and how long did it take you to write it?

### independent-financial-and-accounting-advisors
1. Walk me through the last time a client paid you late — what actually happened from the moment the invoice was due to when you finally got paid?
1. How many invoices did you have to follow up on more than once in the last three months, and how did you handle each follow-up?
1. What did you do the last time a client went completely silent after you sent an invoice?
1. How much time did you spend last month on any kind of payment-chasing activity — emails, calls, messages?
1. Tell me about the tools or systems you used the last time you sent a payment reminder — what did that process look like step by step?
1. Have you ever written off an invoice as uncollectable? What led to that decision and how much was it for?
1. Describe the last time chasing a late payment felt awkward or damaged your relationship with a client — what did you do?
1. What did you actually do the last time you had three or more invoices overdue at the same time?
1. Have you ever hired anyone — a bookkeeper, VA, or collections service — specifically to help you recover unpaid invoices? How did that go?
1. Think back to the last invoice that was more than 60 days overdue — walk me through every action you took and roughly how long each step took you.

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

**pivot**

## Evidence

- `ev-company-solo-management-consultants` crustdata /company/search — 0 results (degraded retry); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Business Consulting and Services']}], 'limit': 25}`
- `ev-company-boutique-it-and-tech-consultancies` crustdata /company/search — 0 results (degraded retry); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Computer and Network Security', 'IT Services and IT Consulting', 'Technology, Information and Internet', 'Technology, Information and Media']}], 'limit': 25}`
- `ev-company-independent-financial-and-accounting-advisors` crustdata /company/search — 0 results (degraded retry); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Accounting', 'Business Intelligence Platforms', 'Financial Services']}], 'limit': 25}`

## Guardrail notes
- guardrail PASS

## Recovery

- At least one tool failure occurred during this run and the agent recovered (see run_state.json).

Estimated model cost for this run: $0.0319
