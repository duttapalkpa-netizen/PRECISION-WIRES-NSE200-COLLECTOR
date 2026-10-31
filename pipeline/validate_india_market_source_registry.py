#!/usr/bin/env python3
"""Validate source inventory metadata only; does not claim live source availability."""
from pathlib import Path
import csv
from urllib.parse import urlparse

REGISTRY = Path("config/india_market_data_source_registry.csv")
REQUIRED = {"source_id","source_name","owner","official_url","data_domains","factor_groups","access_mode","auth_requirement","priority","validation_status","validation_note"}
ALLOWED = {"DISCOVERED_NOT_LIVE_VALIDATED","LIVE_SMOKE_PASS","DOMAIN_QA_PASS","BLOCKED"}

def validate(rows):
    if not rows:
        raise ValueError("source registry is empty")
    seen = set()
    for n, row in enumerate(rows, 2):
        if REQUIRED - set(row):
            raise ValueError(f"missing columns at row {n}: {sorted(REQUIRED-set(row))}")
        sid = row["source_id"].strip()
        if not sid or sid in seen:
            raise ValueError(f"blank or duplicate source_id at row {n}: {sid}")
        seen.add(sid)
        u = urlparse(row["official_url"].strip())
        if u.scheme != "https" or not u.netloc:
            raise ValueError(f"invalid HTTPS official_url at row {n}")
        if row["validation_status"] not in ALLOWED:
            raise ValueError(f"invalid status at row {n}")
        if row["validation_status"] != "DISCOVERED_NOT_LIVE_VALIDATED":
            raise ValueError(f"status promotion requires separate evidence workflow: {sid}")
        for key in ("owner","access_mode","auth_requirement","validation_note"):
            if not row[key].strip():
                raise ValueError(f"missing {key} at row {n}")
    return {"status":"REGISTRY_SCHEMA_PASS","source_count":len(rows),"live_validated_count":0,"promoted_count":0}

def main():
    with REGISTRY.open(newline="",encoding="utf-8-sig") as f:
        print(validate(list(csv.DictReader(f))))

if __name__ == "__main__":
    main()
