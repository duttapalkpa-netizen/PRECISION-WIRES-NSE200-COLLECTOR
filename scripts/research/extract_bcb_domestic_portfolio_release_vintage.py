#!/usr/bin/env python3
"""Extract and reconcile exact domestic portfolio release vintages against latest archived BCB SGS CSVs."""
from __future__ import annotations
import csv
import hashlib
import json
from decimal import Decimal
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
VINTAGES = {
    "2025-12": {
        "publication": "202601",
        "xlsx": ROOT / "data/raw/bcb/release_tables_202601/bcb_external_sector_tables_202601.xlsx",
        "column": 4,  # Table 10 column D = Dec-2025
    },
    "2026-02": {
        "publication": "202603",
        "xlsx": ROOT / "data/raw/bcb/release_tables_202603/bcb_external_sector_tables_202603.xlsx",
        "column": 5,  # Table 10 column E = Feb-2026
    },
}
SGS_FILES = {
    "22930": ROOT / "bcb_domestic_market_crosscheck_202609/sgs_22930.csv",
    "22936": ROOT / "data/raw/bcb/instrument_net_capture_20261117/sgs_22936.csv",
    "22942": ROOT / "data/raw/bcb/instrument_net_capture_20261117/sgs_22942.csv",
}
def dec(v):
    return Decimal(str(v))
def load_sgs(path):
    out = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            date = row.get("data")
            value = row.get("valor")
            if not date or not value:
                continue
            day, month, year = date.split("/")
            out[f"{year}-{month}"] = Decimal(value.replace(",", "."))
    return out
def main():
    sgs = {code: load_sgs(path) for code, path in SGS_FILES.items()}
    result = {
        "schema_version": 2,
        "purpose": "same_vintage_bcb_domestic_portfolio_component_reconciliation",
        "unit": "USD million",
        "sources": {},
        "periods": [],
        "acceptance": "PASS_EXTRACTION_AND_TABLE_IDENTITIES; VINTAGE_DIFFERENCES_QUANTIFIED_NOT_ATTRIBUTED",
    }
    for code, path in SGS_FILES.items():
        raw = path.read_bytes()
        result["sources"][code] = {
            "path": str(path.relative_to(ROOT)),
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
        }
    for month, meta in VINTAGES.items():
        raw = meta["xlsx"].read_bytes()
        wb = load_workbook(meta["xlsx"], read_only=True, data_only=True)
        ws = wb["Tabela 10"]
        col = meta["column"]
        labels = {
            14: "domestic-market equity liabilities",
            20: "investment-fund liabilities in Brazil (Table 10 footnote 1)",
            24: "domestic-market debt-security liabilities",
            40: "domestic-market portfolio total",
            41: "domestic-market equity and investment-fund total",
            42: "domestic-market debt-security total",
            45: "footnote: nonresident quota holder owns less than 10% of investment fund NAV in Brazil",
        }
        table = {row: ws.cell(row=row, column=1).value for row in labels}
        values = {row: ws.cell(row=row, column=col).value for row in (14,20,24,40,41,42)}
        release = {str(row): str(dec(value)) for row, value in values.items()}
        eq = dec(values[14]); funds = dec(values[20]); debt = dec(values[24])
        eqfunds = dec(values[41]); total = dec(values[40]); debt_total = dec(values[42])
        table_identity = {
            "equity_plus_funds_equals_row41": abs(eq + funds - eqfunds) <= Decimal("0.00001"),
            "debt_row24_equals_row42": abs(debt - debt_total) <= Decimal("0.00001"),
            "equity_funds_plus_debt_equals_total": abs(eqfunds + debt_total - total) <= Decimal("0.00001"),
        }
        current = {code: sgs[code][month] for code in SGS_FILES}
        current_eqfunds = current["22930"] + current["22936"]
        current_total = current_eqfunds + current["22942"]
        deltas = {
            "22930_domestic_equity_latest_minus_release": str(current["22930"] - eq),
            "22936_fund_liabilities_latest_minus_release": str(current["22936"] - funds),
            "22942_domestic_debt_latest_minus_release": str(current["22942"] - debt),
            "equity_funds_composite_latest_minus_release": str(current_eqfunds - eqfunds),
            "domestic_portfolio_total_latest_minus_release": str(current_total - total),
        }
        result["periods"].append({
            "reference_month": month,
            "publication_vintage": meta["publication"],
            "xlsx_path": str(meta["xlsx"].relative_to(ROOT)),
            "xlsx_bytes": len(raw),
            "xlsx_sha256": hashlib.sha256(raw).hexdigest(),
            "table": "Tabela 10 – Investimentos em carteira – passivos",
            "reference_month_column": col,
            "release_table_rows": {str(k): {"label": str(table[k]), "value_usd_mn": release.get(str(k))} for k in labels if k != 45},
            "footnote_1": str(table[45]),
            "release_component_values_usd_mn": {
                "domestic_equity": str(eq), "investment_funds": str(funds),
                "domestic_debt": str(debt), "equity_funds_total": str(eqfunds),
                "domestic_portfolio_total": str(total),
            },
            "latest_archived_sgs_values_usd_mn": {k: str(v) for k,v in current.items()},
            "latest_archived_sgs_composites_usd_mn": {
                "equity_funds": str(current_eqfunds), "domestic_portfolio_total": str(current_total)
            },
            "latest_minus_release_usd_mn": deltas,
            "release_table_internal_identities": table_identity,
        })
        wb.close()
    if not all(all(p["release_table_internal_identities"].values()) for p in result["periods"]):
        result["acceptance"] = "FAIL_RELEASE_TABLE_INTERNAL_IDENTITY"
        raise SystemExit("BCB release Table 10 internal identities failed")
    dest = ROOT / "data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json"
    dest.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
if __name__ == "__main__":
    main()
