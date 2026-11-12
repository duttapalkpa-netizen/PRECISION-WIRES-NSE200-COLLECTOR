#!/usr/bin/env python3
"""Recover six blocked NSE quarterly filings from official IndAS Details HTML tables.

This is a research-only repair of already-downloaded, SHA-pinned NSE evidence.
It does not fetch new data, infer missing values, alter production ranking, or
promote unverified source rows. Lakhs are converted explicitly to INR.
"""
from __future__ import annotations

import hashlib
import io
import json
import math
import re
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

ROOT = Path(".")
LEDGER = ROOT / "data/raw/quarterly_financial_metrics.csv"
DISCLOSURES = ROOT / "inputs/batch1/data/raw/quarterly_results_disclosures.csv"
EVIDENCE_DIR = ROOT / "data/raw/quarterly_filing_evidence"
OUT_DIR = ROOT / "outputs/quarterly_results"
REPORT = OUT_DIR / "quarterly_nse_indas_html_table_recovery.json"
MANIFEST = OUT_DIR / "quarterly_nse_indas_html_table_recovery_manifest.json"

PINNED_SOURCE_RUN_ID = 41588275108
PINNED_SOURCE_ARTIFACT_ID = 13209151475
PINNED_SOURCE_ARTIFACT_SHA256 = "f0f53e610f8e0ae53f93a9c46f2246e82324538dca252556df0a70f60a230997"
PINNED_DISCLOSURES_SHA256 = "1f95e41758e397191294d4843601588eeb0b73c8ce7b4ef79913817fd0b7a7d7"
PINNED_LEDGER_SHA256 = "8687356bd833ac78d2dd01e7eb356d32043cc4045f75baba8a02d6174a74d561"

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def norm(value) -> str:
    if pd.isna(value):
        return ""
    return re.sub(r"\s+", " ", str(value)).strip().lower()

def parse_number(value) -> float:
    if pd.isna(value):
        raise ValueError("missing numeric table cell")
    text = str(value).strip().replace(",", "").replace("₹", "").replace("INR", "").strip()
    if text in {"", "-", "—", "–", "NA", "N/A"}:
        raise ValueError("blank or non-numeric financial cell")
    negative = text.startswith("(") and text.endswith(")")
    if negative:
        text = text[1:-1].strip()
    number = float(text)
    if not math.isfinite(number):
        raise ValueError("non-finite financial value")
    return -abs(number) if negative else number

def parse_date(value) -> str:
    parsed = pd.to_datetime(str(value).strip(), dayfirst=True, errors="coerce")
    if pd.isna(parsed):
        raise ValueError(f"unparseable source date: {value!r}")
    return parsed.date().isoformat()

def metadata_value(table: pd.DataFrame, label: str) -> str:
    matches = table[table.iloc[:, 0].map(norm).eq(norm(label))]
    if len(matches) != 1:
        raise ValueError(f"metadata label {label!r} matched {len(matches)} rows")
    return str(matches.iloc[0, 1]).strip()

def validate_official_ixbrl_url(url: str) -> str:
    parsed = urlparse(str(url).strip())
    if parsed.scheme != "https" or parsed.hostname != "nsearchives.nseindia.com":
        raise ValueError("iXBRL source is not the exact approved NSE HTTPS origin")
    if not parsed.path.startswith("/corporate/ixbrl/") or not parsed.path.lower().endswith(".html"):
        raise ValueError("source is not an NSE corporate iXBRL details page")
    if parsed.username or parsed.password or parsed.port not in (None, 443):
        raise ValueError("unsafe iXBRL URL authority")
    return url

def extract_indas_html_table_metrics(blob: bytes, expected: dict) -> dict:
    """Extract exact quarterly cells from the official NSE IndAS Details HTML."""
    if not blob or not re.search(br"<\s*(?:!doctype\s+)?html\b", blob[:8192], re.I):
        raise ValueError("evidence is not an HTML document")
    tables = pd.read_html(io.BytesIO(blob))
    if len(tables) < 2:
        raise ValueError("NSE IndAS HTML lacks metadata or financial statement table")

    meta = tables[0]
    symbol = metadata_value(meta, "NSE Symbol").upper()
    isin = metadata_value(meta, "ISIN").upper()
    unit = metadata_value(meta, "Level of rounding used in financial results")
    reporting_type = metadata_value(meta, "Reporting Type")
    reporting_quarter = metadata_value(meta, "Reporting Quarter")
    meta_basis = metadata_value(meta, "Nature of report standalone or consolidated").upper()

    if symbol != str(expected["SYMBOL"]).upper():
        raise ValueError("HTML symbol does not match NSE disclosure")
    if isin != str(expected["ISIN"]).upper():
        raise ValueError("HTML ISIN does not match NSE disclosure")
    if meta_basis != str(expected["BASIS"]).upper():
        raise ValueError("HTML metadata basis does not match NSE disclosure")
    if norm(reporting_type) != "quarterly":
        raise ValueError("source filing is not explicitly quarterly")
    if norm(unit) != "lakhs":
        raise ValueError(f"unapproved or unknown statement unit: {unit!r}")
    if not reporting_quarter:
        raise ValueError("reporting quarter is absent")

    selected = None
    required_labels = {
        norm("Revenue from operations"),
        norm("Total profit (loss) for period"),
        norm("Basic earnings (loss) per share from continuing and discontinued operations"),
    }
    for table_index, table in enumerate(tables[1:], start=1):
        if table.shape[1] < 3:
            continue
        labels = {norm(x) for x in table.iloc[:, 1].tolist()}
        quarter_header = norm(table.columns[2])
        if required_labels.issubset(labels) and "3 months" in quarter_header and "year to date" not in quarter_header:
            selected = (table_index, table)
            break
    if selected is None:
        raise ValueError("no uniquely qualifying 3-month financial statement table")

    table_index, table = selected
    labels = table.iloc[:, 1].map(norm)
    quarter_header = str(table.columns[2]).strip()

    def exact_row(label: str) -> int:
        indices = labels[labels.eq(norm(label))].index.tolist()
        if len(indices) != 1:
            raise ValueError(f"financial label {label!r} matched {len(indices)} rows")
        return int(indices[0])

    start_row = exact_row("Date of start of reporting period")
    end_row = exact_row("Date of end of reporting period")
    basis_row = exact_row("Nature of report standalone or consolidated")
    revenue_row = exact_row("Revenue from operations")
    pat_row = exact_row("Total profit (loss) for period")
    eps_row = exact_row("Basic earnings (loss) per share from continuing and discontinued operations")

    start_date = parse_date(table.loc[start_row].iloc[2])
    period_end = parse_date(table.loc[end_row].iloc[2])
    table_basis = str(table.loc[basis_row].iloc[2]).strip().upper()
    if table_basis != str(expected["BASIS"]).upper():
        raise ValueError("financial statement table basis does not match disclosure")
    if period_end != str(expected["PERIOD_END"]):
        raise ValueError("financial statement period end does not match disclosure")
    if start_date >= period_end:
        raise ValueError("financial statement period start/end ordering invalid")

    # NSE explicitly declares the statement rounding unit as Lakhs.
    # Convert Revenue and PAT to base INR; EPS is already INR per share.
    multiplier = 100_000.0
    revenue = parse_number(table.loc[revenue_row].iloc[2]) * multiplier
    pat = parse_number(table.loc[pat_row].iloc[2]) * multiplier
    eps = parse_number(table.loc[eps_row].iloc[2])

    return {
        "SYMBOL": symbol,
        "ISIN": isin,
        "PERIOD_END": period_end,
        "BASIS": table_basis,
        "REVENUE": revenue,
        "PAT": pat,
        "EPS": eps,
        "REVENUE_FACT": (
            f"Official NSE IndAS Details HTML table {table_index}, row {revenue_row}: "
            f"Revenue from operations; {quarter_header}; INR Lakhs × 100000 = INR"
        ),
        "PAT_FACT": (
            f"Official NSE IndAS Details HTML table {table_index}, row {pat_row}: "
            f"Total profit (loss) for period; {quarter_header}; INR Lakhs × 100000 = INR"
        ),
        "EPS_FACT": (
            f"Official NSE IndAS Details HTML table {table_index}, row {eps_row}: "
            f"Basic earnings (loss) per share from continuing and discontinued operations; "
            f"{quarter_header}; INR/share"
        ),
        "REVENUE_UNIT": "INR",
        "PAT_UNIT": "INR",
        "EPS_UNIT": "INR_PER_SHARE",
        "REVENUE_CONTEXT_START": start_date,
        "PAT_CONTEXT_START": start_date,
        "EPS_CONTEXT_START": start_date,
        "HTML_TABLE_INDEX": table_index,
        "HTML_ROUNDING_UNIT": unit,
        "REPORTING_QUARTER": reporting_quarter,
    }

def main() -> int:
    for path in (LEDGER, DISCLOSURES):
        if not path.is_file():
            raise SystemExit(f"BLOCKED_MISSING_PINNED_INPUT: {path}")
    if sha256_file(DISCLOSURES) != PINNED_DISCLOSURES_SHA256:
        raise SystemExit("BLOCKED_DISCLOSURE_SNAPSHOT_SHA_MISMATCH")
    if sha256_file(LEDGER) != PINNED_LEDGER_SHA256:
        raise SystemExit("BLOCKED_RECONCILED_LEDGER_SHA_MISMATCH")

    ledger = pd.read_csv(LEDGER, dtype=str).fillna("")
    disclosures = pd.read_csv(DISCLOSURES, dtype=str).fillna("")
    blocked = ledger[ledger["EXTRACTION_STATUS"].eq("BLOCKED_NO_VERIFIED_XBRL_METRICS")].copy()
    if len(blocked) != 6:
        raise SystemExit(f"BLOCKED_EXPECTED_SIX_TARGET_ROWS_GOT_{len(blocked)}")

    disclosure_index = disclosures.set_index("SOURCE_URL", drop=False)
    recovered = []
    for _, row in blocked.iterrows():
        source_key = str(row["SOURCE_URL"])
        if source_key not in disclosure_index.index:
            raise SystemExit(f"BLOCKED_RAW_DISCLOSURE_NOT_FOUND: {row['SYMBOL']}")
        raw_row = disclosure_index.loc[source_key]
        if isinstance(raw_row, pd.DataFrame):
            raise SystemExit(f"BLOCKED_NONUNIQUE_RAW_DISCLOSURE: {row['SYMBOL']}")
        raw = json.loads(str(raw_row["RAW_RECORD_JSON"]))
        if str(raw.get("symbol", "")).upper() != str(row["SYMBOL"]).upper():
            raise SystemExit(f"BLOCKED_RAW_SYMBOL_MISMATCH: {row['SYMBOL']}")
        if str(raw.get("consolidated", "")).strip().upper() != "STANDALONE":
            raise SystemExit(f"BLOCKED_RAW_BASIS_MISMATCH: {row['SYMBOL']}")
        disclosed = pd.to_datetime(row["DISCLOSED_AT"], errors="coerce", utc=True)
        raw_disclosed = pd.to_datetime(raw_row["PUBLICATION_TIMESTAMP"], errors="coerce", utc=True)
        if pd.isna(disclosed) or pd.isna(raw_disclosed) or disclosed != raw_disclosed:
            raise SystemExit(f"BLOCKED_DISCLOSURE_TIMESTAMP_MISMATCH: {row['SYMBOL']}")

        ixbrl_url = validate_official_ixbrl_url(raw.get("ixbrl", ""))
        evidence_path = ROOT / str(row["EVIDENCE_PATH"])
        if not evidence_path.is_file():
            raise SystemExit(f"BLOCKED_MISSING_HTML_EVIDENCE: {evidence_path}")
        blob = evidence_path.read_bytes()
        evidence_sha = hashlib.sha256(blob).hexdigest()
        if evidence_sha != str(row["SOURCE_SHA256"]).lower():
            raise SystemExit(f"BLOCKED_HTML_EVIDENCE_SHA_MISMATCH: {row['SYMBOL']}")
        if "html" not in str(row["SOURCE_CONTENT_TYPE"]).lower():
            raise SystemExit(f"BLOCKED_EXPECTED_HTML_CONTENT_TYPE: {row['SYMBOL']}")

        expected = {
            "SYMBOL": row["SYMBOL"],
            "ISIN": row["ISIN"],
            "BASIS": "STANDALONE",
            "PERIOD_END": pd.to_datetime(row["PERIOD_END"], errors="raise").date().isoformat(),
        }
        facts = extract_indas_html_table_metrics(blob, expected)
        repaired = row.to_dict()
        repaired.update(facts)
        repaired["SOURCE_URL"] = ixbrl_url
        repaired["SOURCE_SHA256"] = evidence_sha
        repaired["SOURCE_CONTENT_TYPE"] = "text/html"
        repaired["EXTRACTION_STATUS"] = "SOURCE_LINKED_NSE_HTML_TABLE_FACTS"
        repaired["EVIDENCE_PATH"] = str(row["EVIDENCE_PATH"])
        # Keep the actual original NSE disclosure timestamp and observation time.
        repaired["DISCLOSED_AT"] = row["DISCLOSED_AT"]
        repaired["OBSERVED_AT_UTC"] = row["OBSERVED_AT_UTC"]
        recovered.append(repaired)
        mask = ledger["SOURCE_URL"].eq(source_key)
        if int(mask.sum()) != 1:
            raise SystemExit(f"BLOCKED_LEDGER_TARGET_NOT_UNIQUE: {row['SYMBOL']}")
        for key, value in repaired.items():
            if key in ledger.columns:
                ledger.loc[mask, key] = value

    from pipeline.quarterly_metric_batches_merge import apply_global_revision_policy, validate_evidence
    ledger = apply_global_revision_policy(ledger)
    evidence_verified = validate_evidence(ledger)
    counts = ledger["EXTRACTION_STATUS"].value_counts().to_dict()
    expected_counts = {
        "SOURCE_LINKED_XBRL_FACTS": 1864,
        "SOURCE_LINKED_NSE_HTML_TABLE_FACTS": 4,
        "SUPERSEDED_BY_LATER_DISCLOSURE": 120,
    }
    if counts != expected_counts:
        raise SystemExit("BLOCKED_UNEXPECTED_STATUS_COUNTS: " + json.dumps(counts, sort_keys=True))
    if len(ledger) != 1988 or evidence_verified != 1988:
        raise SystemExit("BLOCKED_FULL_ROW_OR_EVIDENCE_RECONCILIATION")
    if ledger["SOURCE_URL"].nunique() != 1988:
        raise SystemExit("BLOCKED_SOURCE_URL_NOT_UNIQUE_AFTER_HTML_REPAIR")

    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ledger.to_csv(LEDGER, index=False)

    from pipeline.quarterly_results_research import build_financial_features
    features, feature_report = build_financial_features(LEDGER)
    if feature_report.get("status") != "COMPUTED" or len(features) != 1868:
        raise SystemExit("BLOCKED_FEATURE_REBUILD: " + json.dumps(feature_report, sort_keys=True))
    features_path = OUT_DIR / "quarterly_financial_features.csv"
    features.to_csv(features_path, index=False)

    report = {
        "status": "PASS",
        "source_snapshot": {
            "run_id": PINNED_SOURCE_RUN_ID,
            "artifact_id": PINNED_SOURCE_ARTIFACT_ID,
            "artifact_sha256": PINNED_SOURCE_ARTIFACT_SHA256,
            "disclosures_sha256": PINNED_DISCLOSURES_SHA256,
            "pre_repair_ledger_sha256": PINNED_LEDGER_SHA256,
        },
        "target_rows_before_repair": 6,
        "unique_html_evidence_files": int(len({x["SOURCE_SHA256"] for x in recovered})),
        "recovered_rows": [
            {k: x[k] for k in (
                "SYMBOL", "ISIN", "PERIOD_END", "BASIS", "DISCLOSED_AT",
                "REVENUE", "PAT", "EPS", "REVENUE_UNIT", "PAT_UNIT", "EPS_UNIT",
                "SOURCE_URL", "SOURCE_SHA256", "HTML_TABLE_INDEX", "HTML_ROUNDING_UNIT",
            )}
            for x in recovered
        ],
        "status_counts_after_global_revision_policy": counts,
        "merged_ledger_rows": len(ledger),
        "source_evidence_files_sha256_verified": evidence_verified,
        "feature_report": feature_report,
        "feature_rows": len(features),
        "merged_ledger_sha256": sha256_file(LEDGER),
        "features_sha256": sha256_file(features_path),
        "production_invariants": {
            "production_selector_changed": False,
            "ranking_score_changed": False,
            "pressure_fade_changed": False,
            "diagnostics_672_changed": False,
            "hard_gate_relaxed": False,
        },
        "policy": (
            "Only official NSE IndAS Details HTML tables were parsed. Symbol, ISIN, "
            "period end, standalone basis, quarterly reporting type, table row labels, "
            "3-month column, and Lakhs unit were explicitly validated. Revenue and PAT "
            "were converted from INR Lakhs to INR; EPS remained INR/share. Original "
            "DISCLOSED_AT and OBSERVED_AT_UTC values were preserved. Global revision "
            "policy superseded the two older duplicate standalone disclosures."
        ),
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    manifest = {
        "status": "PASS",
        "source_artifact": report["source_snapshot"],
        "source_disclosures_sha256": PINNED_DISCLOSURES_SHA256,
        "repaired_ledger_sha256": report["merged_ledger_sha256"],
        "features_sha256": report["features_sha256"],
        "recovery_report_sha256": sha256_file(REPORT),
        "status_counts": counts,
        "feature_rows": len(features),
        "source_evidence_files_sha256_verified": evidence_verified,
        "production_invariants": report["production_invariants"],
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
