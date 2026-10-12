# StageZero validation kit — run run-20261012-080405-09d5b8

**Idea:** AI agent that chases unpaid invoices for independent consultants

**Stage diagnosis:** Stage 0 (Improvise) on the ACQ $100M Scaling Roadmap: nothing is happening yet; the goal is to get people to try your stuff for free. Graduation = people find it helpful unprompted.

## Problem statement

Freelance IT and tech consultants struggle to collect payment on unpaid invoices because chasing clients requires persistent, time-consuming follow-up that pulls them away from billable work; the current workaround is manually sending reminder emails and making awkward phone calls themselves, which costs them both hours of non-billable time and the discomfort of damaging client relationships through repeated personal pressure. Hypothesis: an AI agent that autonomously sends escalating, professionally toned payment follow-up sequences on behalf of the consultant removes that time and relationship cost for freelance IT and tech consultants who invoice clients directly and operate without dedicated accounts receivable staff.

## Customer segments (ranked)

| # | Segment | Companies | Competitors | Pain signals | Priority |
|---|---------|-----------|-------------|--------------|----------|
| 1 | freelance-it-and-tech-consultancies | 5219872 | 2089 | 1 | 70 |
| 2 | solo-management-consultants | 2671528 | 2089 | 1 | 55 |
| 3 | independent-marketing-and-creative-agencies | 2259569 | 0 | 1 | 53 |

### freelance-it-and-tech-consultancies
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Computer and Network Security', 'IT Services and IT Consulting', 'Software Development', 'Technology, Information and Internet', 'Technology, Information and Media']}]`
- Sample companies: Acropetal Technologies Limited, Adam Comsof Ltd, ADC INDIA COMMUNICATIONS LTD
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 70/100 — Tech consultants frequently work with slow-paying enterprise procurement departments, have no collections process, and lose billable hours chasing payments instead of delivering work.

### solo-management-consultants
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Business Consulting and Services']}]`
- Sample companies: Business Advisers International, Aditya Ispat Limited - India, AMD Industries, Inc.
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 55/100 — They lack dedicated finance staff, often feel awkward chasing clients personally, and late payments directly threaten their cash flow with no buffer from a larger organization.

### independent-marketing-and-creative-agencies
- ICP filters: `[{'field': 'basic_info.industries', 'type': 'in', 'value': ['Advertising Services', 'Design Services', 'Graphic Design', 'Marketing Services', 'Public Relations and Communications Services']}]`
- Sample companies: Barak Valley Cements Ltd, Creative Merchants, DOT & Company
- Pain signal: no job-title signal for 'invoice' in this segment
- Priority 53/100 — Creative consultants routinely face scope-creep disputes and delayed approvals that stall payments; they need a professional, automated voice to follow up without damaging client relationships they depend on for referrals.

## Mom Test interview scripts

### solo-management-consultants
1. Walk me through the last time a client paid you late — what actually happened from the moment the invoice was due to when the money hit your account?
1. How many invoices did you send out in the last 90 days, and how many of those were paid after the due date?
1. What did you actually do the last time a client went more than two weeks past due — what steps did you take and in what order?
1. How much time did you spend last month on any kind of follow-up related to unpaid or overdue invoices?
1. Tell me about the last time you had an awkward or uncomfortable conversation with a client specifically about money they owed you — what led up to it and how did it go?
1. Have you ever decided not to follow up on a late invoice, or waited longer than you should have — what was going through your head at the time?
1. What tools or systems have you actually used to track which invoices are outstanding — walk me through your current setup?
1. Have you ever written off an invoice or accepted a partial payment just to avoid the chase — what happened there?
1. How has chasing late payments affected your relationship with a client — can you give me a specific example?
1. What did late payments actually cost you in the last year — not just the money owed, but time, stress, or work you couldn't take on because cash was tied up?

### freelance-it-and-tech-consultancies
1. Walk me through the last time a client paid you late — what exactly did you do to follow up?
1. How many invoices did you have to chase more than once in the last three months?
1. What was the longest you waited for an overdue payment in the past year, and how did that situation eventually get resolved?
1. Show me or describe the last follow-up message you sent to a late-paying client — how did you write it and where did you send it from?
1. How much time did you spend last month on any kind of invoice-related admin, including chasing, resending, or reconciling payments?
1. Tell me about a time you felt uncomfortable or hesitant to follow up on an overdue invoice — what did you do instead?
1. What tools or systems did you use the last time you tracked which invoices were still outstanding?
1. Has a late payment ever caused you to delay paying your own bills or dip into savings — what happened?
1. Describe the last time you had to escalate a non-payment beyond a reminder email — what steps did you take and what did it cost you in time or money?
1. Have you ever written off an invoice as uncollectable rather than continuing to chase it — what was the amount and what made you give up?

### independent-marketing-and-creative-agencies
1. Walk me through the last time a client paid you late — what actually happened from the moment the invoice was due to when you finally got paid?
1. How many invoices did you have to follow up on more than once in the last 90 days, and how did you handle each follow-up?
1. What did you do the last time a client went completely silent after you sent an invoice?
1. How much time did you spend last month on chasing payments — emails, calls, messages — and how did you track that effort?
1. Tell me about the most uncomfortable payment chase you've had with a client — what did you do and how did it affect the relationship?
1. What tools or systems did you use the last time you sent a payment reminder — email, accounting software, a spreadsheet, something else?
1. Have you ever written off an invoice as uncollectable — what was the situation and what steps had you already taken before giving up?
1. When a client last disputed or delayed an invoice, what was your process for resolving it and how long did it take?
1. How did you decide when to escalate a late payment to a formal demand letter or a collections service, and did you actually do it?
1. What did late payments cost you in real terms last year — did you ever have to delay paying a supplier, a contractor, or yourself because a client hadn't paid?

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

- `ev-company-solo-management-consultants` crustdata /company/search — 2671528 results (segment size); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Business Consulting and Services']}], 'limit': 25}`
- `ev-company-freelance-it-and-tech-consultancies` crustdata /company/search — 5219872 results (segment size); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Computer and Network Security', 'IT Services and IT Consulting', 'Software Development', 'Technology, Information and Internet', 'Technology, Information and Media']}], 'limit': 25}`
- `ev-company-independent-marketing-and-creative-agencies` crustdata /company/search — 2259569 results (segment size); query `{'filters': [{'field': 'basic_info.industries', 'type': 'in', 'value': ['Advertising Services', 'Design Services', 'Graphic Design', 'Marketing Services', 'Public Relations and Communications Services']}], 'limit': 25}`

## Guardrail notes
- guardrail PASS

Estimated model cost for this run: $0.0000
