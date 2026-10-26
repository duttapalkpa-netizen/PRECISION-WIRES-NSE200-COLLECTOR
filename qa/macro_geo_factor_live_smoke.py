#!/usr/bin/env python3
"""Bounded live smoke test for Treasury yields, DXY and official policy-feed connectivity."""
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys
import json
import xml.etree.ElementTree as ET
import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline.macro_geo_factor_source_collectors import (
    POLICY_FEEDS, fetch_treasury_yields, fetch_dxy_yahoo
)

end = datetime.now(timezone.utc).date()
start = end - timedelta(days=21)
session = requests.Session()
session.headers.update({"User-Agent": "PRECISION-WIRES-NSE200-COLLECTOR/1.0 (bounded source smoke)",
                        "Accept": "text/csv,application/xml,application/rss+xml,application/atom+xml,*/*"})
report = {"window_start": start.isoformat(), "window_end": end.isoformat(), "sources": {}, "failures": []}

try:
    rows = fetch_treasury_yields(session, start, end)
    labels = sorted({row["SERIES"] for row in rows})
    expected = {"US_TREASURY_2Y", "US_TREASURY_10Y", "US_TREASURY_30Y"}
    if not expected.issubset(labels) or not all(row.get("SOURCE_URL", "").startswith("https://home.treasury.gov/") for row in rows):
        raise ValueError("Treasury yield schema or provenance check failed")
    report["sources"]["us_yields"] = {"status": "PASS", "rows": len(rows), "series": labels,
                                      "source": "US Department of the Treasury",
                                      "url_examples": sorted({row["SOURCE_URL"] for row in rows})[:2]}
except Exception as exc:
    report["sources"]["us_yields"] = {"status": "BLOCKED", "error": f"{type(exc).__name__}: {str(exc)[:220]}"}
    report["failures"].append("us_yields")

try:
    rows = fetch_dxy_yahoo(session, start, end)
    report["sources"]["dxy"] = {"status": "PASS", "rows": len(rows),
                                "date_min": min(r["DATE"] for r in rows), "date_max": max(r["DATE"] for r in rows),
                                "source": "Yahoo Finance chart API; DX-Y.NYB",
                                "url": rows[0]["SOURCE_URL"]}
except Exception as exc:
    report["sources"]["dxy"] = {"status": "BLOCKED", "error": f"{type(exc).__name__}: {str(exc)[:220]}"}
    report["failures"].append("dxy")

for feed_url, country, source_name in POLICY_FEEDS:
    try:
        response = session.get(feed_url, timeout=(8, 20))
        response.raise_for_status()
        root = ET.fromstring(response.content)
        local_names = [element.tag.rsplit("}", 1)[-1].lower() for element in root.iter()]
        entry_count = sum(name in ("item", "entry") for name in local_names)
        if not local_names or not (root.tag.rsplit("}", 1)[-1].lower() in ("rss", "feed", "rdf") or entry_count > 0):
            raise ValueError("response is not a recognizable RSS/Atom document")
        report["sources"][f"policy_feed_{source_name.lower()}"] = {
            "status": "PASS", "feed_entries": entry_count, "country": country, "url": response.url
        }
    except Exception as exc:
        report["sources"][f"policy_feed_{source_name.lower()}"] = {
            "status": "BLOCKED", "error": f"{type(exc).__name__}: {str(exc)[:220]}", "url": feed_url
        }
        report["failures"].append(f"policy_feed_{source_name.lower()}")

report["status"] = "PASS" if not report["failures"] else "PARTIAL_BLOCKED"
print(json.dumps(report, indent=2))
if report["failures"]:
    raise SystemExit(1)
