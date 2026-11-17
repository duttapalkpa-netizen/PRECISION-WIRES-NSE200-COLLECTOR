#!/usr/bin/env python3
"""Audit 15 archived official BCB SGS portfolio series for monthly accounting identities.

Research-only. Reads immutable raw CSV captures and their capture manifests.
Does not download, overwrite, forward-fill, infer missing values, or authorize production use.
"""
from __future__ import annotations
import csv, hashlib, json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFESTS = [
    ROOT / "data/raw/bcb/priority_series_capture_20261117/manifest.json",
    ROOT / "data/raw/bcb/instrument_net_capture_20261117/manifest.json",
]
SERIES_PATHS = {
    "22905": "data/raw/bcb/priority_series_capture_20261117/sgs_22905.csv",
    "22906": "data/raw/bcb/priority_series_capture_20261117/sgs_22906.csv",
    "22907": "data/raw/bcb/priority_series_capture_20261117/sgs_22907.csv",
    "22908": "data/raw/bcb/priority_series_capture_20261117/sgs_22908.csv",
    "22924": "data/raw/bcb/priority_series_capture_20261117/sgs_22924.csv",
    "22925": "data/raw/bcb/priority_series_capture_20261117/sgs_22925.csv",
    "22926": "data/raw/bcb/priority_series_capture_20261117/sgs_22926.csv",
    "22909": "data/raw/bcb/instrument_net_capture_20261117/sgs_22909.csv",
    "22912": "data/raw/bcb/instrument_net_capture_20261117/sgs_22912.csv",
    "22915": "data/raw/bcb/instrument_net_capture_20261117/sgs_22915.csv",
    "22927": "data/raw/bcb/instrument_net_capture_20261117/sgs_22927.csv",
    "22936": "data/raw/bcb/instrument_net_capture_20261117/sgs_22936.csv",
    "22939": "data/raw/bcb/instrument_net_capture_20261117/sgs_22939.csv",
    "22942": "data/raw/bcb/instrument_net_capture_20261117/sgs_22942.csv",
    "22945": "data/raw/bcb/instrument_net_capture_20261117/sgs_22945.csv",
}
TOLERANCE = Decimal("0.1")  # all source observations are rounded to USD million, 0.1m precision

def load_csv(path: Path):
    raw = path.read_bytes()
    rows = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        if reader.fieldnames != ['"data"', '"valor"'] and reader.fieldnames != ["data", "valor"]:
            raise ValueError(f"unexpected CSV header in {path}: {reader.fieldnames}")
        for row in reader:
            date = (row.get('"data"') or row.get("data") or "").strip('"')
            value = (row.get('"valor"') or row.get("valor") or "").strip('"')
            if not date or not value:
                raise ValueError(f"blank observation in {path}")
            dd, mm, yyyy = date.split("/")
            period = f"{yyyy}-{mm}"
            if period in rows:
                raise ValueError(f"duplicate period {period} in {path}")
            rows[period] = Decimal(value.replace(",", "."))
    if not rows:
        raise ValueError(f"empty CSV: {path}")
    ordered = list(rows)
    if ordered != sorted(ordered):
        raise ValueError(f"non-ascending periods in {path}")
    return raw, rows

def main():
    manifest_index = {}
    manifest_digests = {}
    for path in MANIFESTS:
        manifest_raw = path.read_bytes()
        manifest = json.loads(manifest_raw)
        manifest_digests[str(path.relative_to(ROOT))] = hashlib.sha256(manifest_raw).hexdigest()
        if not str(manifest.get("status", "")).startswith("RAW_CAPTURE_"):
            raise ValueError(f"manifest status is not raw-capture PASS: {path}")
        for code, meta in manifest["series"].items():
            manifest_index[code] = meta

    series, raw_audit = {}, {}
    for code, relpath in SERIES_PATHS.items():
        path = ROOT / relpath
        raw, values = load_csv(path)
        meta = manifest_index[code]
        digest = hashlib.sha256(raw).hexdigest()
        if digest != meta["sha256"] or len(raw) != meta["byte_length"]:
            raise ValueError(f"raw integrity mismatch for SGS {code}")
        if meta.get("http_status") != 200 or meta.get("raw_capture_status", "PASS") != "PASS":
            raise ValueError(f"source capture was not HTTP/raw PASS for SGS {code}")
        series[code] = values
        raw_audit[code] = {"path": relpath, "bytes": len(raw), "sha256": digest,
                           "row_count": len(values), "first_period": next(iter(values)),
                           "last_period": next(reversed(values)), "title": meta.get("title")}

    periods = sorted(set.intersection(*(set(v) for v in series.values())))
    if not periods:
        raise ValueError("no common periods across all 15 series")
    equations = [
        ("portfolio_net_assets_minus_liabilities", "22905", lambda v: v["22905"] - (v["22906"] - v["22924"])),
        ("asset_net_equals_equity_funds_debt_assets", "22906", lambda v: v["22906"] - (v["22909"] + v["22912"] + v["22915"])),
        ("asset_net_equals_outflows_minus_inflows", "22906", lambda v: v["22906"] - (v["22908"] - v["22907"])),
        ("liability_net_equals_inflows_minus_outflows", "22924", lambda v: v["22924"] - (v["22925"] - v["22926"])),
        ("liability_net_equals_equity_funds_debt_liabilities", "22924", lambda v: v["22924"] - (v["22927"] + v["22936"] + v["22939"])),
        ("debt_liabilities_equals_domestic_plus_external", "22939", lambda v: v["22939"] - (v["22942"] + v["22945"])),
    ]
    results = []
    for name, target, fn in equations:
        diffs = []
        for period in periods:
            vals = {code: series[code][period] for code in SERIES_PATHS}
            diffs.append((period, fn(vals)))
        max_abs = max(abs(d) for _, d in diffs)
        failed = [{"period": p, "difference_usd_mn": str(d)} for p, d in diffs if abs(d) > TOLERANCE]
        results.append({"identity": name, "n_periods": len(diffs),
                        "within_tolerance": len(diffs)-len(failed), "failed_periods": failed,
                        "max_abs_difference_usd_mn": str(max_abs),
                        "tolerance_usd_mn": str(TOLERANCE),
                        "status": "PASS" if not failed else "FAIL"})
    payload = {
        "schema_version": 1,
        "purpose": "research_only_monthly_BCB_portfolio_series_internal_accounting_identity_audit",
        "provider": "Banco Central do Brasil / BCData SGS",
        "unit": "USD million",
        "capture_scope": "15 official monthly SGS series; two archived capture manifests",
        "period_count_common": len(periods),
        "first_common_period": periods[0],
        "last_common_period": periods[-1],
        "common_periods": periods,
        "tolerance_policy": "USD 0.1 million, reflecting source values published to one decimal place; no wider tolerance applied",
        "manifest_sha256": manifest_digests,
        "raw_series": raw_audit,
        "identities": results,
        "all_identities_pass": all(x["status"] == "PASS" for x in results),
        "production_integration": "NOT_AUTHORIZED",
        "portfolio_flow_signal": "NOT_AUTHORIZED",
        "limitations": [
            "Internal accounting identities do not prove full BPM6 semantic equivalence or release-vintage stability.",
            "This monthly Brazil series panel is not a direct crosswalk to IMF quarterly BFPA/BFPL.",
            "No capital-flow ranking, country score or trading trigger is calculated."
        ]
    }
    dest = ROOT / "data/qa/BCB_PORTFOLIO_INTERNAL_IDENTITY_AUDIT_20261118.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    if not payload["all_identities_pass"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
