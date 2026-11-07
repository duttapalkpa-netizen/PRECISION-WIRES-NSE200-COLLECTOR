#!/usr/bin/env python3
"""Read-only integrity audit for existing IIP certified revision batches 001-005.

This validates ledger arithmetic, batch summaries, source hashes, and cross-batch
transition uniqueness. It does not fetch sources, recertify cells, or promote rows.
"""
import csv
import hashlib
import json
import re
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research/continuity"
BATCHES = [
    ("001", BASE / "IIP_CELL_LEVEL_REVISION_BATCH_001_2023-04.csv",
     BASE / "IIP_CELL_LEVEL_REVISION_BATCH_001_SUMMARY.json"),
    ("002", BASE / "IIP_CELL_LEVEL_REVISION_BATCH_002_2023-04.csv",
     BASE / "IIP_CELL_LEVEL_REVISION_BATCH_002_SUMMARY.json"),
    ("003", BASE / "IIP_CELL_LEVEL_REVISION_BATCH_003_2023-04.csv",
     BASE / "IIP_CELL_LEVEL_REVISION_BATCH_003_SUMMARY.json"),
    ("004", BASE / "IIP_CELL_LEVEL_REVISION_BATCH_004_2023-05.csv",
     BASE / "IIP_CELL_LEVEL_REVISION_BATCH_004_SUMMARY.json"),
    ("005", BASE / "IIP_CELL_LEVEL_REVISION_BATCH_005_2023-06.csv",
     BASE / "IIP_CELL_LEVEL_REVISION_BATCH_005_SUMMARY.json"),
]
HEX64 = re.compile(r"^[0-9a-f]{64}$")

def pick(row, *names):
    for name in names:
        if row.get(name) not in (None, ""):
            return row[name]
    return ""

def audit():
    errors, hash_drift, batches, seen = [], [], [], {}
    total_rows = 0
    for batch, csv_path, summary_path in BATCHES:
        raw = csv_path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        with csv_path.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            fields = set(reader.fieldnames or [])
        if not rows:
            errors.append(f"batch {batch}: empty ledger")
        expected_count = summary.get("certified_cell_level_source_matches",
                        summary.get("certified_exact_source_matches",
                        summary.get("candidate_cells", summary.get("candidate_rows_reviewed"))))
        if expected_count != len(rows):
            errors.append(f"batch {batch}: summary row count {expected_count} != ledger {len(rows)}")
        declared_csv_hash = summary.get("csv_sha256") or summary.get("ledger_csv_sha256")
        if declared_csv_hash and declared_csv_hash != digest:
            alias_path = (ROOT / "data/macro/IIP_CELL_LEVEL_REVISION_BATCH_001_2023-04.csv") if batch == "001" else None
            alias_digest = hashlib.sha256(alias_path.read_bytes()).hexdigest() if alias_path and alias_path.exists() else None
            alias_same_bytes = bool(alias_path and alias_path.exists() and alias_path.read_bytes() == raw)
            if alias_digest == declared_csv_hash:
                hash_drift.append({"batch": batch, "legacy_declared_sha256": declared_csv_hash,
                    "current_committed_sha256": digest, "alternate_copy": str(alias_path.relative_to(ROOT)),
                    "alternate_copy_sha256": alias_digest, "alternate_copy_same_bytes_as_research": alias_same_bytes,
                    "status": "DECLARED_HASH_MATCHES_ALTERNATE_COPY"})
            else:
                hash_drift.append({"batch": batch, "legacy_declared_sha256": declared_csv_hash,
                    "current_committed_sha256": digest, "alternate_copy": str(alias_path.relative_to(ROOT)) if alias_path else None,
                    "alternate_copy_sha256": alias_digest, "alternate_copy_same_bytes_as_research": alias_same_bytes,
                    "status": "QUARANTINED_UNRESOLVED_PROVENANCE"})
        certified = 0
        for line, row in enumerate(rows, 2):
            period = pick(row, "observation_period", "period")
            nic = row.get("nic_code", "").strip()
            prev = pick(row, "previous_vintage_table_id", "previous_table_id")
            curr = pick(row, "current_vintage_table_id", "current_table_id")
            key = (period, nic, prev, curr)
            if not all(key):
                errors.append(f"batch {batch}:{line}: incomplete transition key")
            if key in seen:
                errors.append(f"batch {batch}:{line}: duplicate transition also in {seen[key]}")
            seen[key] = f"batch {batch}:{line}"
            old_hash = row.get("previous_workbook_sha256", "")
            new_hash = row.get("current_workbook_sha256", "")
            if not HEX64.fullmatch(old_hash) or not HEX64.fullmatch(new_hash):
                errors.append(f"batch {batch}:{line}: invalid workbook SHA-256")
            old_value = pick(row, "previous_value")
            new_value = pick(row, "current_value")
            delta = row.get("revision_delta", "")
            if old_value and new_value and delta:
                try:
                    if Decimal(new_value) - Decimal(old_value) != Decimal(delta):
                        errors.append(f"batch {batch}:{line}: revision_delta arithmetic mismatch")
                except Exception:
                    errors.append(f"batch {batch}:{line}: nonnumeric revision values")
            match = pick(row, "source_value_match", "source_match")
            if match not in ("PASS_BOTH_OFFICIAL_PIB_AND_SOURCE_WORKBOOK", "EXACT"):
                errors.append(f"batch {batch}:{line}: unsupported source match label {match!r}")
            if batch == "001":
                status = row.get("certification_status", "")
                if status != "CERTIFIED_CELL_LEVEL_SOURCE_MATCH":
                    errors.append(f"batch 001:{line}: invalid certification status")
            else:
                if not row.get("official_pib_url", row.get("official_current_pib_url", row.get("current_official_pib_url", ""))):
                    errors.append(f"batch {batch}:{line}: missing official PIB URL")
            certified += 1
        total_rows += len(rows)
        batches.append({"batch": batch, "rows": len(rows), "sha256": digest,
                        "summary_count": expected_count, "status": "CHECKED"})
    result = {
        "status": ("BLOCKED_BATCH_LEDGER_INTEGRITY" if errors else ("PASS_WITH_HASH_DRIFT_QUARANTINED" if hash_drift else "PASS_EXISTING_BATCH_LEDGER_INTEGRITY")),
        "batches_checked": len(batches), "certified_rows_in_existing_ledgers": total_rows,
        "unique_transition_keys": len(seen), "batches": batches, "hash_drift_quarantined": hash_drift, "errors": errors,
        "hard_gate": "BLOCKED",
        "scope": "Read-only ledger integrity only. Does not independently recertify original workbooks/PIB, add certified cells, or close unresolved IIP audit gaps."
    }
    return result

if __name__ == "__main__":
    result = audit()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] in ("PASS_EXISTING_BATCH_LEDGER_INTEGRITY", "PASS_WITH_HASH_DRIFT_QUARANTINED") else 1)
