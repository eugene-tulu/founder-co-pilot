#!/usr/bin/env python3
"""Build the StageZero business-plan Model in cfo.ai (monthly model + scenarios)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cfoai_mcp as m  # noqa: E402

MONTHS = [f"2026-{m_:02d}" for m_ in range(10, 13)] + [f"2027-{m_:02d}" for m_ in range(1, 10)]
CASES = ["Base", "Growth", "Scale"]
CUSTOMERS = {"Base": 100, "Growth": 500, "Scale": 2000}

def d(name: str) -> str:
    return f'`Value`$[Driver = "{name}"]'


REV = ('`Paying customers` * (' + d("Pro share of paying") + ' * `Price per month`$[Plan = "Pro"] '
       '+ ' + d("Team share of paying") + ' * `Price per month`$[Plan = "Team"])')
COST = '`Paying customers` * ' + d("Kits per customer per month") + ' * ' + d("Model cost per run")
PROFIT = '`Revenue` - `Inference and data cost` - `Infra cost`'

values_rows = [[f"Paying customers[{c}]"] + [CUSTOMERS[c]] + [None] * (len(MONTHS) - 1) for c in CASES]

payload = {
    "create": {
        "name": "Monthly model",
        "columns": [{"time": "MONTH"}],
        "rows": [
            {"variable": "Paying customers", "breakdown": ["Case"], "rollup": "LAST",
             "child_defaults": [{"dimension": "Case",
                                 "actuals": "`Customers`$[Case = this.Case]",
                                 "forecast": "`Paying customers`[-1]"}]},
            {"variable": "Revenue", "breakdown": ["Case"], "rollup": "SUM",
             "child_defaults": [{"dimension": "Case", "actuals": REV, "forecast": REV}]},
            {"variable": "Inference and data cost", "breakdown": ["Case"], "rollup": "SUM",
             "child_defaults": [{"dimension": "Case", "actuals": COST, "forecast": COST}]},
            {"variable": "Infra cost", "formula": d("Infra cost per month")},
            {"variable": "Gross profit", "breakdown": ["Case"],
             "formula": PROFIT},
            {"variable": "Gross margin", "breakdown": ["Case"],
             "formula": "iferror(`Gross profit` / `Revenue`, NULL)"},
            {"variable": "Runway months", "breakdown": ["Case"],
             "formula": d("Hackathon credits") + " / (`Infra cost` + `Inference and data cost`)"},
        ],
    }
}

out = m.mcp_call("edit_table_blocks", payload)
r = out["result"]["result"]
print("isError:", r.get("isError"))
sc = r.get("structuredContent", {})
print(json.dumps({k: sc.get(k) for k in ("status", "changed", "issues", "table", "page")}, indent=1)[:800])
if r.get("isError"):
    print(json.dumps(sc)[:2500])
else:
    Path("/tmp/kilo/monthly.json").write_text(json.dumps(sc))
    print("saved /tmp/kilo/monthly.json")
