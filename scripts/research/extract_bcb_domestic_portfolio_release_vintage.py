#!/usr/bin/env python3
"""Extract only the domestic-market portfolio investment rows and headers from BCB release XLSX vintages."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
FILES = {
    "202601": ROOT / "data/raw/bcb/release_tables_202601/bcb_external_sector_tables_202601.xlsx",
    "202603": ROOT / "data/raw/bcb/release_tables_202603/bcb_external_sector_tables_202603.xlsx",
}
def main():
    out = {"schema_version": 1, "purpose": "exact_bcb_domestic_portfolio_release_table_extraction", "workbooks": []}
    for vintage, path in FILES.items():
        raw = path.read_bytes()
        wb = load_workbook(path, read_only=True, data_only=True)
        ws = wb["Tabela 10"]
        rows = []
        for idx, row in enumerate(ws.iter_rows(min_row=1, max_row=min(ws.max_row, 48), values_only=True), start=1):
            vals = list(row[:12])
            label = " ".join(str(v) for v in vals[:2] if v is not None)
            if idx <= 12 or "Investimento em carteira negociados no mercado doméstico" in label or idx in (40, 41, 42):
                rows.append({"row": idx, "cells_A_L": vals})
        out["workbooks"].append({
            "publication_vintage": vintage,
            "source_path": str(path.relative_to(ROOT)),
            "source_bytes": len(raw),
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "sheet": ws.title,
            "max_row": ws.max_row,
            "max_column": ws.max_column,
            "selected_rows": rows
        })
        wb.close()
    dest = ROOT / "data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json"
    dest.write_text(json.dumps(out, indent=2, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
if __name__ == "__main__":
    main()
