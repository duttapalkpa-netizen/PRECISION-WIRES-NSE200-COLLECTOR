#!/usr/bin/env python3
"""Inspect archived BCB historical release XLSX vintages for portfolio-investment rows."""
from __future__ import annotations
import json
import re
import unicodedata
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
FILES = {
    "202601": ROOT / "data/raw/bcb/release_tables_202601/bcb_external_sector_tables_202601.xlsx",
    "202603": ROOT / "data/raw/bcb/release_tables_202603/bcb_external_sector_tables_202603.xlsx",
}
TERMS = (
    "investimentos em carteira",
    "mercado domestico",
    "mercado doméstico",
    "fundos de investimento",
    "titulos de divida",
    "títulos de dívida",
    "acoes",
    "ações",
)

def norm(value):
    s = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s).strip()

def cell_value(v):
    if v is None:
        return None
    if hasattr(v, "isoformat"):
        return v.isoformat()
    return v if isinstance(v, (int, float, bool, str)) else str(v)

def main():
    result = {"schema_version": 1, "purpose": "inspect_same_vintage_official_bcb_release_tables",
              "workbooks": []}
    for vintage, path in FILES.items():
        if not path.exists():
            raise SystemExit(f"Missing archived workbook: {path}")
        wb = load_workbook(path, read_only=True, data_only=True)
        entry = {"publication_vintage": vintage, "path": str(path.relative_to(ROOT)), "sheets": []}
        for ws in wb.worksheets:
            hits = []
            for row_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
                vals = [cell_value(v) for v in row]
                joined = " | ".join(str(v) for v in vals if v is not None)
                n = norm(joined)
                if any(norm(term) in n for term in TERMS):
                    hits.append({"row": row_idx, "values": vals})
            if hits:
                entry["sheets"].append({"sheet": ws.title, "max_row": ws.max_row,
                                        "max_column": ws.max_column, "matching_rows": hits})
        wb.close()
        result["workbooks"].append(entry)
    out = ROOT / "data/qa/BCB_HISTORICAL_RELEASE_TABLES_TARGET_CELLS_20261117.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
if __name__ == "__main__":
    main()
