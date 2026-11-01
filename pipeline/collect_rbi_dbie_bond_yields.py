#!/usr/bin/env python3
"""Capture RBI DBIE raw table evidence and fail closed on opaque source columns."""
import csv, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
import requests

API = "https://data-api.dbie.rbihub.in/api/tables/financial_markets/r217_month_end_yield_of_sgl_transactions_in_government_dated_se"
CSV_URL = API + "/csv"
OUT = Path("artifacts/india_bond_yields")
def main():
    session = requests.Session()
    session.headers.update({"User-Agent": "PRECISION-WIRES-NSE200-COLLECTOR/1.0"})
    metadata_response = session.get(API, timeout=(8, 25))
    metadata_response.raise_for_status()
    metadata_bytes = metadata_response.content
    metadata = metadata_response.json()
    csv_response = session.get(CSV_URL, timeout=(8, 40))
    csv_response.raise_for_status()
    raw_bytes = csv_response.content
    raw_text = raw_bytes.decode("utf-8-sig")
    parsed = list(csv.reader(raw_text.splitlines()))
    if len(parsed) < 2:
        raise RuntimeError("DBIE raw CSV is empty or lacks data rows")
    headers = [h.strip() for h in parsed[0]]
    sample = [[c.strip() for c in row] for row in parsed[1:4]]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "rbi_dbie_raw.csv").write_bytes(raw_bytes)
    (OUT / "rbi_dbie_table_metadata.json").write_bytes(metadata_bytes)
    observed = datetime.now(timezone.utc).isoformat()
    report = {
      "status": "RBI_DBIE_RAW_SCHEMA_DIAGNOSTIC_PASS_MAPPING_BLOCKED",
      "source": "Reserve Bank of India, Database on Indian Economy",
      "source_api": API, "source_csv": CSV_URL,
      "observed_at_utc": observed,
      "raw_csv_sha256": hashlib.sha256(raw_bytes).hexdigest(),
      "metadata_sha256": hashlib.sha256(metadata_bytes).hexdigest(),
      "csv_header": headers, "csv_data_rows": max(0, len(parsed)-1),
      "sample_rows": sample,
      "metadata_top_level_keys": sorted(metadata.keys()) if isinstance(metadata, dict) else [],
      "metadata_excerpt": metadata if isinstance(metadata, dict) else str(metadata),
      "mapping_status": "BLOCKED",
      "mapping_reason": "CSV exports opaque c1..cN fields; no maturity labels are present in CSV headers. No cN-to-tenor mapping is inferred or promoted.",
      "factor_registry_promotion": "NOT_PROMOTED",
      "release_timestamp_status": "UNKNOWN_NOT_SUPPLIED_IN_RETRIEVED_PAYLOAD",
      "frequency": "MONTHLY",
      "instrument_scope": "RBI month-end SGL yield table; do not equate with daily FBIL 10-year benchmark."
    }
    (OUT / "rbi_dbie_source_adapter_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k != "metadata_excerpt"}, indent=2))
    if not headers or not any(h.lower().startswith("c") and h[1:].isdigit() for h in headers):
        raise RuntimeError("Expected opaque cN fields were not present; diagnostic assumptions invalid")
if __name__ == "__main__":
    main()
