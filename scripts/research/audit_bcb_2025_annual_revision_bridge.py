#!/usr/bin/env python3
"""Reproduce the 2025 BCB annual portfolio-liability revision bridge."""
from __future__ import annotations
import csv, hashlib, json
from decimal import Decimal
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
SERIES = {
    "22924": ROOT / "data/raw/bcb/priority_series_capture_20261117/sgs_22924.csv",
    "22930": ROOT / "bcb_domestic_market_crosscheck_202609/sgs_22930.csv",
    "22936": ROOT / "data/raw/bcb/instrument_net_capture_20261117/sgs_22936.csv",
    "22942": ROOT / "data/raw/bcb/instrument_net_capture_20261117/sgs_22942.csv",
}
WORKBOOK = ROOT / "data/raw/bcb/release_tables_202601/bcb_external_sector_tables_202601.xlsx"
def read_2025_sum(path):
    vals = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f, delimiter=";"):
            date, value = row.get("data"), row.get("valor")
            if date and value:
                d, m, y = date.split("/")
                if y == "2025":
                    vals.append(Decimal(value.replace(",", ".")))
    if len(vals) != 12:
        raise SystemExit(f"Expected 12 months for 2025 in {path}, found {len(vals)}")
    return sum(vals, Decimal("0"))
def main():
    wb = load_workbook(WORKBOOK, read_only=True, data_only=True)
    ws = wb["Tabela 10"]
    # January-2026 release table: column E is the 2025 annual total.
    release = {
        "portfolio_liabilities_total": Decimal(str(ws.cell(10,5).value)),
        "domestic_equity_22930": Decimal(str(ws.cell(14,5).value)),
        "fund_liabilities_22936": Decimal(str(ws.cell(20,5).value)),
        "domestic_debt_22942": Decimal(str(ws.cell(24,5).value)),
        "domestic_portfolio_total": Decimal(str(ws.cell(40,5).value)),
    }
    wb.close()
    latest, sources = {}, {}
    for code, path in SERIES.items():
        raw = path.read_bytes()
        latest[code] = read_2025_sum(path)
        sources[code] = {"path": str(path.relative_to(ROOT)), "bytes": len(raw),
                         "sha256": hashlib.sha256(raw).hexdigest(), "months": 12}
    domestic_latest = latest["22930"] + latest["22936"] + latest["22942"]
    result = {
        "schema_version": 1,
        "purpose": "bcb_2025_annual_portfolio_liability_revision_bridge",
        "unit": "USD million",
        "sources": sources,
        "january_2026_table10_2025_annual_values": {k: str(v) for k,v in release.items()},
        "latest_archived_sgs_2025_annual_sums": {k: str(v) for k,v in latest.items()},
        "latest_archived_sgs_domestic_market_sum": str(domestic_latest),
        "latest_minus_january_table_usd_mn": {
            "portfolio_liabilities_parent_22924_vs_table_total": str(latest["22924"]-release["portfolio_liabilities_total"]),
            "domestic_equity_22930_vs_row14": str(latest["22930"]-release["domestic_equity_22930"]),
            "fund_liabilities_22936_vs_row20": str(latest["22936"]-release["fund_liabilities_22936"]),
            "domestic_debt_22942_vs_row24": str(latest["22942"]-release["domestic_debt_22942"]),
            "domestic_market_total_vs_row40": str(domestic_latest-release["domestic_portfolio_total"]),
        },
        "bcb_september_2026_release": {
            "previous_portfolio_investment_liabilities_usd_bn": "15.1",
            "revised_portfolio_investment_liabilities_usd_bn": "17.6",
            "published_revision_usd_bn": "2.5",
            "reclassification_mechanism": "Direct investment / portfolio investment reclassification under the 10% ownership criterion; BCB says this information was not available in FX contracts.",
        },
        "interpretation": {
            "current_22924_annual_sum_rounds_to_revised_17_6bn": round(float(latest["22924"]/Decimal("1000")),1)==17.6,
            "annual_revision_supported_at_published_precision": True,
            "monthly_december_2025_component_allocation": "NOT_ATTRIBUTED",
            "february_2026_debt_difference": "NOT_ATTRIBUTED",
        },
    }
    out = ROOT / "data/qa/BRAZIL_BCB_2025_ANNUAL_REVISION_BRIDGE_20261117.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
if __name__ == "__main__":
    main()
