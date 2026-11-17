#!/usr/bin/env python3
"""Extract and reconcile BCB historical Table 10 values across publication-period workbooks."""
from __future__ import annotations
import csv, hashlib, json, re
from decimal import Decimal
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
WORKBOOKS = {
    "202601": {"path": ROOT / "data/raw/bcb/release_tables_202601/bcb_external_sector_tables_202601.xlsx", "targets": ["2025-12"]},
    "202603": {"path": ROOT / "data/raw/bcb/release_tables_202603/bcb_external_sector_tables_202603.xlsx", "targets": ["2026-02"]},
    "202610": {"path": ROOT / "data/raw/bcb/release_tables_202610/bcb_external_sector_tables_202610.xlsx", "targets": ["2026-09"]},
}
SGS_FILES = {
    "22930": ROOT / "bcb_domestic_market_crosscheck_202609/sgs_22930.csv",
    "22936": ROOT / "data/raw/bcb/instrument_net_capture_20261117/sgs_22936.csv",
    "22942": ROOT / "data/raw/bcb/instrument_net_capture_20261117/sgs_22942.csv",
}
MONTHS = {"jan": "01", "fev": "02", "mar": "03", "abr": "04", "mai": "05", "jun": "06",
          "jul": "07", "ago": "08", "set": "09", "out": "10", "nov": "11", "dez": "12"}
def dec(v): return Decimal(str(v))
def load_sgs(path):
    out = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f, delimiter=";"):
            date, value = row.get("data"), row.get("valor")
            if date and value:
                day, month, year = date.split("/")
                out[f"{year}-{month}"] = Decimal(value.replace(",", "."))
    return out
def month_columns(ws):
    years = {}
    months = {}
    current_year = None
    for col in range(2, ws.max_column + 1):
        year_value = ws.cell(row=5, column=col).value
        if year_value is not None:
            m = re.search(r"20\d{2}", str(year_value))
            if m: current_year = m.group(0)
        month_value = str(ws.cell(row=7, column=col).value or "").strip().lower()
        month_token = re.match(r"[a-zç]+", month_value)
        if current_year and month_token:
            token = month_token.group(0)[:3]
            if token in MONTHS:
                key = f"{current_year}-{MONTHS[token]}"
                months[key] = col
    return months
def main():
    sgs = {code: load_sgs(path) for code, path in SGS_FILES.items()}
    manifest = json.loads((ROOT / "data/raw/bcb/BCB_HISTORICAL_RELEASE_TABLES_VINTAGE_MANIFEST_20261117.json").read_text())
    manifest_by_period = {x["publication_period"]: x for x in manifest["files"]}
    result = {"schema_version": 3, "purpose": "BCB_domestic_portfolio_historical_table_vintage_and_latest_SGS_comparison",
              "unit": "USD million", "source_sgs": {}, "workbooks": [],
              "acceptance": "PASS_TABLE_EXTRACTION_AND_INTERNAL_IDENTITIES; VINTAGE_DIFFERENCES_QUANTIFIED_NOT_ATTRIBUTED"}
    for code, path in SGS_FILES.items():
        raw = path.read_bytes()
        result["source_sgs"][code] = {"path": str(path.relative_to(ROOT)), "bytes": len(raw),
                                      "sha256": hashlib.sha256(raw).hexdigest()}
    for vintage, meta in WORKBOOKS.items():
        path = meta["path"]
        raw = path.read_bytes()
        wb = load_workbook(path, read_only=True, data_only=True)
        ws = wb["Tabela 10"]
        cols = month_columns(ws)
        manifest_entry = manifest_by_period[vintage]
        last_modified = re.search(r"last-modified: ([^\r\n]+)", manifest_entry["http_headers"], re.I)
        entry = {"publication_period_file": vintage, "path": str(path.relative_to(ROOT)),
                 "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
                 "http_last_modified": last_modified.group(1) if last_modified else None,
                 "table": "Tabela 10 – Investimentos em carteira – passivos",
                 "header_year_row_5": [ws.cell(5,c).value for c in range(1,min(ws.max_column,12)+1)],
                 "header_month_row_7": [ws.cell(7,c).value for c in range(1,min(ws.max_column,12)+1)],
                 "periods": []}
        for month in meta["targets"]:
            if month not in cols:
                raise SystemExit(f"Target month {month} not found in {vintage} Table 10 headers: {cols}")
            col = cols[month]
            values = {row: ws.cell(row=row, column=col).value for row in (14,20,24,40,41,42)}
            eq, funds, debt = (dec(values[r]) for r in (14,20,24))
            eqfunds, total, debt_total = (dec(values[r]) for r in (41,40,42))
            identities = {
                "equity_plus_funds_equals_row41": abs(eq + funds - eqfunds) <= Decimal("0.00001"),
                "debt_row24_equals_row42": abs(debt - debt_total) <= Decimal("0.00001"),
                "equity_funds_plus_debt_equals_total": abs(eqfunds + debt_total - total) <= Decimal("0.00001"),
            }
            current = {code: sgs[code][month] for code in SGS_FILES}
            current_eqfunds = current["22930"] + current["22936"]
            current_total = current_eqfunds + current["22942"]
            period_record = {
                "reference_month": month, "column_number": col,
                "release_rows_usd_mn": {
                    "22930_domestic_equity_row14": str(eq),
                    "22936_fund_liabilities_row20": str(funds),
                    "22942_domestic_debt_row24": str(debt),
                    "equity_funds_total_row41": str(eqfunds),
                    "domestic_portfolio_total_row40": str(total),
                    "debt_total_row42": str(debt_total),
                    "fund_footnote_row45": str(ws.cell(row=45, column=1).value),
                },
                "latest_archived_sgs_usd_mn": {k: str(v) for k,v in current.items()},
                "latest_archived_sgs_composites_usd_mn": {"equity_funds": str(current_eqfunds),
                                                            "domestic_portfolio_total": str(current_total)},
                "latest_minus_table_usd_mn": {
                    "22930": str(current["22930"]-eq), "22936": str(current["22936"]-funds),
                    "22942": str(current["22942"]-debt), "equity_funds": str(current_eqfunds-eqfunds),
                    "domestic_total": str(current_total-total)},
                "table_internal_identities": identities,
            }
            if vintage == "202603" and month == "2026-02":
                cumulative_col = 6
                cumulative = {row: dec(ws.cell(row=row, column=cumulative_col).value) for row in (14,20,24,40,41,42)}
                inferred_jan = {row: cumulative[row] - dec(values[row]) for row in cumulative}
                current_jan = {code: sgs[code]["2026-01"] for code in SGS_FILES}
                period_record["jan_feb_cumulative_and_inferred_january"] = {
                    "cumulative_release_rows_usd_mn": {str(k): str(v) for k,v in cumulative.items()},
                    "inferred_january_release_rows_usd_mn": {str(k): str(v) for k,v in inferred_jan.items()},
                    "latest_archived_sgs_january_usd_mn": {k: str(v) for k,v in current_jan.items()},
                    "latest_minus_inferred_january_usd_mn": {
                        "22930": str(current_jan["22930"]-inferred_jan[14]),
                        "22936": str(current_jan["22936"]-inferred_jan[20]),
                        "22942": str(current_jan["22942"]-inferred_jan[24]),
                        "equity_funds": str(current_jan["22930"]+current_jan["22936"]-inferred_jan[41]),
                        "domestic_total": str(current_jan["22930"]+current_jan["22936"]+current_jan["22942"]-inferred_jan[40]),
                    },
                    "inferred_january_table_identities": {
                        "equity_plus_funds_equals_row41": abs(inferred_jan[14]+inferred_jan[20]-inferred_jan[41]) <= Decimal("0.00001"),
                        "debt_row24_equals_row42": abs(inferred_jan[24]-inferred_jan[42]) <= Decimal("0.00001"),
                        "equity_funds_plus_debt_equals_total": abs(inferred_jan[41]+inferred_jan[42]-inferred_jan[40]) <= Decimal("0.00001"),
                    }
                }
            entry["periods"].append(period_record)
        result["workbooks"].append(entry)
        wb.close()
    if not all(all(p["table_internal_identities"].values()) for w in result["workbooks"] for p in w["periods"]):
        result["acceptance"] = "FAIL_TABLE_INTERNAL_IDENTITY"
        raise SystemExit("BCB Table 10 internal identities failed")
    dest = ROOT / "data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json"
    dest.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
if __name__ == "__main__":
    main()
