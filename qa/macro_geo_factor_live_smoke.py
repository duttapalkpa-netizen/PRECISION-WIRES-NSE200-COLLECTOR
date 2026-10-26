#!/usr/bin/env python3
"""Bounded live smoke test of official US Treasury daily yield CSV (21-day window)."""
from datetime import datetime, timezone, timedelta
import json
import requests
from pipeline.macro_geo_factor_source_collectors import fetch_treasury_yields

end = datetime.now(timezone.utc).date()
start = end - timedelta(days=21)
session = requests.Session()
session.headers.update({"User-Agent": "PRECISION-WIRES-NSE200-COLLECTOR/1.0 (bounded source smoke)", "Accept": "text/csv,*/*"})
rows = fetch_treasury_yields(session, start, end)
labels = sorted({row["SERIES"] for row in rows})
if len(rows) == 0 or not {"US_TREASURY_2Y", "US_TREASURY_10Y", "US_TREASURY_30Y"}.issubset(labels):
    raise SystemExit(json.dumps({"status": "FAIL", "rows": len(rows), "series": labels}))
if any(not row.get("SOURCE_URL", "").startswith("https://home.treasury.gov/") for row in rows):
    raise SystemExit(json.dumps({"status": "FAIL", "reason": "source provenance URL missing or unexpected"}))
print(json.dumps({"status": "PASS", "window_start": start.isoformat(), "window_end": end.isoformat(),
                  "rows": len(rows), "series": labels, "source": "US Department of the Treasury",
                  "url_examples": sorted({row["SOURCE_URL"] for row in rows})[:3]}, indent=2))
