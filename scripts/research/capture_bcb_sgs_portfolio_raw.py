#!/usr/bin/env python3
"""Capture official BCB SGS portfolio series as immutable raw evidence."""
from __future__ import annotations
import hashlib, json, math, os
from datetime import datetime, timezone
from pathlib import Path
import requests

OUT = Path("artifacts/bcb_sgs_portfolio")
OUT.mkdir(parents=True, exist_ok=True)
SERIES = {
    "22905": {"label": "portfolio_investment_monthly_net", "unit": "million USD", "frequency": "monthly", "semantic_limit": "aggregate portfolio net; do not classify as assets or liabilities"},
    "22906": {"label": "portfolio_net_acquisition_financial_assets", "unit": "million USD", "frequency": "monthly", "semantic_limit": "portfolio financial-asset net acquisition"},
    "22925": {"label": "portfolio_net_incurrence_liabilities_inflows", "unit": "million USD", "frequency": "monthly", "semantic_limit": "portfolio liability net incurrence inflows"},
    "22940": {"label": "portfolio_debt_securities_inflows", "unit": "million USD", "frequency": "monthly", "semantic_limit": "portfolio debt securities inflows"},
}
session = requests.Session()
session.headers.update({"User-Agent": "PRECISION-WIRES-research/1.0 (public official-source archival)", "Accept": "application/json"})
manifest = {"source": "Banco Central do Brasil / SGS public API", "retrieval_started_utc": datetime.now(timezone.utc).isoformat(), "series": {}, "overall_status": "PASS"}
for code, meta in SERIES.items():
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json"
    retrieved = datetime.now(timezone.utc).isoformat()
    entry = {**meta, "source_url": url, "retrieval_timestamp_utc": retrieved}
    try:
        response = session.get(url, timeout=(10, 35))
        raw = response.content
        raw_path = OUT / f"sgs_{code}.json"
        raw_path.write_bytes(raw)
        entry.update({
            "http_status": response.status_code,
            "final_url": response.url,
            "response_headers": {k: response.headers.get(k) for k in ("Content-Type","Date","ETag","Last-Modified","Content-Length")},
            "raw_file": raw_path.name,
            "raw_bytes": len(raw),
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
        })
        if response.status_code != 200:
            raise ValueError(f"HTTP_{response.status_code}")
        payload = response.json()
        if not isinstance(payload, list) or not payload:
            raise ValueError("JSON_NOT_NONEMPTY_ARRAY")
        dates, bad = [], []
        for i, row in enumerate(payload):
            if not isinstance(row, dict) or set(("data","valor")) - set(row):
                bad.append(f"row_{i}_schema"); continue
            try:
                dt = datetime.strptime(row["data"], "%d/%m/%Y").date()
                val = float(str(row["valor"]).replace(",", "."))
                if not math.isfinite(val): raise ValueError("nonfinite")
                dates.append(dt)
            except Exception:
                bad.append(f"row_{i}_value")
        duplicates = len(dates) - len(set(dates))
        ordered = dates == sorted(dates)
        entry.update({"row_count": len(payload), "valid_rows": len(dates), "invalid_rows": bad[:20],
                      "duplicate_date_count": duplicates, "dates_monotonic": ordered,
                      "first_observation": min(dates).isoformat() if dates else None,
                      "last_observation": max(dates).isoformat() if dates else None})
        if bad or duplicates or not ordered or len(dates) != len(payload):
            raise ValueError("SCHEMA_OR_DATE_QA_FAILED")
        entry["status"] = "PASS"
    except Exception as exc:
        entry["status"] = "FAIL"
        entry["error"] = f"{type(exc).__name__}: {exc}"
        manifest["overall_status"] = "FAIL"
    manifest["series"][code] = entry
manifest["retrieval_finished_utc"] = datetime.now(timezone.utc).isoformat()
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({"overall_status": manifest["overall_status"], "series": {k: {x:v.get(x) for x in ("status","row_count","raw_bytes","raw_sha256","last_observation","error")} for k,v in manifest["series"].items()}}, indent=2))
if manifest["overall_status"] != "PASS":
    raise SystemExit(1)
