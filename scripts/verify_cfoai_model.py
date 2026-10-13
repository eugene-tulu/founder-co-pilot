#!/usr/bin/env python3
"""Read back the monthly model and print a compact verification table."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cfoai_mcp as m  # noqa: E402

out = m.mcp_call("inspect_table_blocks", {
    "read": {
        "target": "Monthly model", "depth": 2,
        "periods": "boundaries",
        
    }
})
r = out["result"]["result"]
sc = r.get("structuredContent", {})
if r.get("isError"):
    print(json.dumps(sc)[:1500])
    sys.exit(1)

rows = sc.get("rows", [])
cols = [c.get("display_name") for c in sc.get("columns", [])]
print("columns:", cols[:4], "...")
for row in rows:
    name = row.get("display_name", "")
    vals = row.get("values", [])
    if name.startswith(("Paying", "Revenue", "Inference", "Infra", "Gross", "Runway")):
        shown = [round(v, 2) if isinstance(v, (int, float)) else v for v in vals[:3]]
        print(f"{name:34s} {shown}")
Path("/tmp/kilo/monthly_read.json").write_text(json.dumps(sc))
print("full readback saved")
