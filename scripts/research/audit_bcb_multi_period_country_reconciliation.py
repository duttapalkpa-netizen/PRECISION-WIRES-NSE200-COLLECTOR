#!/usr/bin/env python3
"""Reproduce the bounded BCB domestic portfolio multi-period cross-vintage check.

Reads only committed raw CSVs. Does not download, rewrite, or normalize source files.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCES = {
    "22930": {
        "path": "bcb_domestic_market_crosscheck_202609/sgs_22930.csv",
        "sha256": "c4730c84ee81765a1c5ae41d91c1ea6f153bcb51ac70ee14b45b453b4dcab776",
    },
    "22936": {
        "path": "data/raw/bcb/instrument_net_capture_20261117/sgs_22936.csv",
        "sha256": "0d1b040d5b11af0b1b98704a70f4972f2790bdfe3c6e78bb16948c7a31640e24",
    },
    "22942": {
        "path": "data/raw/bcb/instrument_net_capture_20261117/sgs_22942.csv",
        "sha256": "4c09c850decf3317d27d1c0f4dc4aa68dc4f0b3aa2aafacfece113ff7f9c7169",
    },
}
# BCB release values in USD billion, transcribed from the official cited monthly releases.
# Tuple order: equity+funds, domestic debt, total.
RELEASES = {
    "2025-12": ("-1.4", "5.3", "3.9"),
    "2026-01": ("1.9", "6.9", "8.9"),
    "2026-02": ("2.8", "2.6", "5.4"),
    "2026-03": ("-0.4", "-2.5", "-2.9"),
    "2026-04": ("1.1", "-0.5", "0.6"),
    "2026-06": ("-2.2", "1.6", "-0.6"),
    "2026-07": ("1.9", "-0.7", "1.1"),
    "2026-08": ("-6.5", "1.3", "-5.2"),
    "2026-09": ("-1.7", "-0.4", "-2.1"),
}
Q = Decimal("0.1")


def load_series(code: str) -> dict[str, Decimal]:
    meta = SOURCES[code]
    raw = (ROOT / meta["path"]).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != meta["sha256"]:
        raise ValueError(f"SHA-256 mismatch for SGS {code}: {digest}")
    text = raw.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text), delimiter=";")
    if reader.fieldnames != ['"data"', '"valor"'] and reader.fieldnames != ["data", "valor"]:
        # csv handles quoted field names in standard input; fail closed on unexpected schema.
        raise ValueError(f"Unexpected CSV header for SGS {code}: {reader.fieldnames}")
    out: dict[str, Decimal] = {}
    for row in reader:
        date = row.get("data") or row.get('"data"')
        value = row.get("valor") or row.get('"valor"')
        if not date or not value:
            raise ValueError(f"Missing date/value in SGS {code}")
        day, month, year = date.split("/")
        key = f"{year}-{month}"
        if key in out:
            raise ValueError(f"Duplicate month {key} in SGS {code}")
        out[key] = Decimal(value.replace(",", "."))
    return out


def round_bn(value_mn: Decimal) -> Decimal:
    return (value_mn / Decimal("1000")).quantize(Q, rounding=ROUND_HALF_UP)


def main() -> None:
    series = {code: load_series(code) for code in SOURCES}
    rows = []
    for month, release in RELEASES.items():
        if any(month not in series[code] for code in SOURCES):
            raise ValueError(f"Missing required month {month}")
        eq_funds = series["22930"][month] + series["22936"][month]
        debt = series["22942"][month]
        total = eq_funds + debt
        calculated = (round_bn(eq_funds), round_bn(debt), round_bn(total))
        expected = tuple(Decimal(x).quantize(Q) for x in release)
        rows.append({
            "month": month,
            "sgs_eq_funds_bn": str(calculated[0]),
            "release_eq_funds_bn": str(expected[0]),
            "eq_funds_match": calculated[0] == expected[0],
            "sgs_debt_bn": str(calculated[1]),
            "release_debt_bn": str(expected[1]),
            "debt_match": calculated[1] == expected[1],
            "sgs_total_bn": str(calculated[2]),
            "release_total_bn": str(expected[2]),
            "total_match": calculated[2] == expected[2],
        })
    matches = sum(sum((r["eq_funds_match"], r["debt_match"], r["total_match"])) for r in rows)
    complete_months = sum(all((r["eq_funds_match"], r["debt_match"], r["total_match"])) for r in rows)
    result = {
        "schema_version": 1,
        "purpose": "research_only_bcb_multi_period_domestic_portfolio_release_crosscheck",
        "source_sha256_verified": {code: meta["sha256"] for code, meta in SOURCES.items()},
        "months_checked": len(rows),
        "complete_months": complete_months,
        "comparisons": len(rows) * 3,
        "comparisons_matched": matches,
        "rows": rows,
        "status": "PASS_BOUNDED_REPRODUCIBILITY_WITH_TWO_UNRESOLVED_VINTAGE_MONTHS"
        if complete_months == 7 and matches == 23 else "FAIL",
    }
    out = ROOT / "bcb_multi_period_reconciliation_result.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] == "FAIL":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
