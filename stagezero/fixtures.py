"""Offline fixtures so the agent runs end-to-end with no API keys (demo mode).

Counts are illustrative placeholders, clearly labelled as fixtures in every
artifact the agent emits.
"""
from __future__ import annotations

DEMO_IDEA = "AI agent that chases unpaid invoices for independent consultants"

FIXTURE_SOURCE = "offline-fixture (demo mode, not live Crustdata data)"

DEMO_HYPOTHESES = [
    {
        "name": "independent-accounting-practices",
        "description": "Solo/small accounting and bookkeeping practices (2-10 staff) that invoice clients monthly",
        "filters": [{"field": "industries", "type": "in", "value": ["accounting", "bookkeeping"]}],
        "why": "Invoicing and collections are core recurring pain for billable-hours firms",
    },
    {
        "name": "fractional-cfo-firms",
        "description": "Fractional CFO / virtual controller firms handling many small clients",
        "filters": [{"field": "industries", "type": "in", "value": ["financial services", "management consulting"]}],
        "why": "Fractional operators own collections for many clients; leverage per saved hour is highest",
    },
    {
        "name": "boutique-creative-agencies",
        "description": "Boutique creative/marketing agencies with retainers and milestone invoicing",
        "filters": [{"field": "industries", "type": "in", "value": ["marketing and advertising", "design"]}],
        "why": "Retainer billing disputes are common and visible in hiring signals (billing/invoice roles)",
    },
]

DEMO_SEGMENTS = {
    "independent-accounting-practices": {
        "company_count": 1284,
        "sample_companies": ["Ledgerline CPA", "Northgate Bookkeeping", "Books & Bell LLP"],
        "pain_signals": [
            "job posting: 'Accounts Receivable Specialist - collections calls' at Northgate Bookkeeping",
            "job posting: 'Billing Coordinator' at Ledgerline CPA",
            "3 of 10 sampled firms list AR aging follow-up in job descriptions",
        ],
        "competitor_count": 41,
    },
    "fractional-cfo-firms": {
        "company_count": 217,
        "sample_companies": ["Trellis CFO Group", "Part-Time Controller Co"],
        "pain_signals": [
            "job posting: 'Client Accountant - month-end close and collections' at Trellis CFO Group",
        ],
        "competitor_count": 12,
    },
    "boutique-creative-agencies": {
        "company_count": 968,
        "sample_companies": ["Studio Meridian", "Fold Creative", "North & Yarrow"],
        "pain_signals": [
            "job posting: 'Studio Manager - invoicing and client billing' at Studio Meridian",
            "job posting: 'Finance Manager (agency)' at Fold Creative",
        ],
        "competitor_count": 23,
    },
}
