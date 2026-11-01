#!/usr/bin/env python3
"""Bounded live smoke test for the official MoSPI NAS Q1 FY2026-27 GDP table.

Downloads one exact public catalogue workbook (constant-price GDP), preserves
raw bytes and provenance, and performs conservative workbook/domain QA.
It does not normalize/promote Factor Registry coverage or modify production logic.
"""
from __future__ import annotations
import hashlib, json, ssl, time, urllib.parse, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path
from openpyxl import load_workbook

API = "https://api.mospi.gov.in/api/esankhyiki/"
LIST = API + "cms/golden-sheet/list"
DOWNLOAD = API + "file/download/"
PRODUCT = "NAS"
TABLE_ID = "AEQEAFY2607QTR"  # Q1 FY2026-27 GDP + expenditure, constant prices
OUT = Path("artifacts/mospi_nas_gdp_smoke")
UA = "Mozilla/5.0 (compatible; PRECISION-WIRES-NAS-GDP-Smoke/1.0)"

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def opener():
    # MoSPI's public API endpoint currently requires legacy TLS renegotiation.
    # Keep CA validation and hostname checking enabled; only enable legacy server
    # connect compatibility, matching the already-validated IIP collector.
    ctx = ssl.create_default_context()
    ctx.set_ciphers("DEFAULT:@SECLEVEL=1")
    ctx.options |= 0x4
    return urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))

def get(url: str, accept: str = "application/json, */*"):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": accept,
        "Origin": "https://esankhyiki.mospi.gov.in",
        "Referer": "https://esankhyiki.mospi.gov.in/catalogue-main/catalogue",
    })
    with opener().open(req, timeout=35) as response:
        body = response.read(40_000_000)
        return {
            "status": response.status,
            "content_type": response.headers.get("Content-Type", ""),
            "final_url": response.geturl(),
            "body": body,
        }

def catalogue_record():
    # The exact latest Q1 FY2026-27 table is advertised on the first NAS
    # catalogue page. Read only that bounded page; do not crawl 1,700+ entries.
    first_url = LIST + "?" + urllib.parse.urlencode({
        "product": PRODUCT, "page": 1, "limit": 10
    })
    first = get(first_url)
    if first["status"] != 200:
        raise RuntimeError(f"NAS catalogue HTTP {first['status']}")
    payload = json.loads(first["body"].decode("utf-8-sig"))
    meta = payload.get("meta_data") or {}
    records = list(payload.get("data") or [])
    if not records:
        raise RuntimeError("NAS catalogue first page returned no records")
    matches = [r for r in records if str(r.get("unique_id", "")) == TABLE_ID]
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected exactly one {TABLE_ID} on bounded first page; found {len(matches)}"
        )
    record = matches[0]
    required = ("unique_id", "product", "table_name", "ref_period",
                "release_date", "file_path", "file_name")
    missing = [k for k in required if not record.get(k)]
    if missing:
        raise RuntimeError(f"Catalogue record missing required metadata: {missing}")
    if record["product"] != PRODUCT:
        raise RuntimeError(f"Unexpected product: {record['product']}")
    title = str(record["table_name"]).lower()
    if "quarterly" not in title or "constant" not in title or "gdp" not in title:
        raise RuntimeError(f"Unexpected table title: {record['table_name']}")
    return record, {
        "request_url": first_url,
        "response_sha256": sha256(first["body"]),
        "catalogue_total_records": int(meta.get("totalRecords") or 0),
        "catalogue_total_pages": int(meta.get("totalPages") or 0),
        "page_records_returned": len(records),
        "scope": "single first-page exact-ID lookup; no full catalogue crawl",
    }

def workbook_inventory(path: Path):
    wb = load_workbook(path, read_only=True, data_only=True)
    sheets = []
    numeric_total = 0
    nonempty_total = 0
    quarter_tokens = set()
    for ws in wb.worksheets:
        sample = []
        numeric = 0
        nonempty = 0
        max_row = 0
        max_col = 0
        for row_index, row in enumerate(ws.iter_rows(), start=1):
            values = [cell.value for cell in row]
            if any(v is not None for v in values):
                nonempty += sum(v is not None for v in values)
                max_row = max(max_row, row_index)
                max_col = max(max_col, len(values))
            for value in values:
                if isinstance(value, (int, float)) and not isinstance(value, bool):
                    numeric += 1
                if isinstance(value, str):
                    upper = value.strip().upper()
                    for token in ("Q1", "Q2", "Q3", "Q4", "APRIL-JUNE", "JULY-SEPTEMBER"):
                        if token in upper:
                            quarter_tokens.add(token)
            if len(sample) < 12 and any(v is not None for v in values):
                sample.append([str(v) if v is not None else None for v in values[:12]])
        sheets.append({
            "sheet": ws.title, "max_row_observed": max_row,
            "max_column_observed": max_col, "nonempty_cells": nonempty,
            "numeric_cells": numeric, "sample_rows": sample,
        })
        numeric_total += numeric
        nonempty_total += nonempty
    wb.close()
    if not sheets or nonempty_total == 0 or numeric_total == 0:
        raise RuntimeError("Workbook domain QA failed: no non-empty numeric observations")
    if not quarter_tokens:
        raise RuntimeError("Workbook domain QA failed: no quarterly labels found")
    return {
        "sheet_count": len(sheets), "nonempty_cells": nonempty_total,
        "numeric_cells": numeric_total, "quarter_tokens_found": sorted(quarter_tokens),
        "sheets": sheets,
    }

def extract_gdp_observation(path: Path):
    """Extract the All-India GDP row from the Q1 constant-price statement."""
    wb = load_workbook(path, read_only=True, data_only=True)
    ws = wb[wb.sheetnames[0]]
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    header_index = next((i for i, row in enumerate(rows)
                         if any(isinstance(v, str) and "Quarterly Levels" in v for v in row)), None)
    if header_index is None:
        raise RuntimeError("GDP table header 'Quarterly Levels' not found")
    year_row = next((row for row in rows[header_index + 1:header_index + 4]
                     if sum(str(v).strip() == "2026-27" for v in row if v is not None) >= 2), None)
    if year_row is None:
        raise RuntimeError("GDP table FY 2026-27 columns not found")
    positions = [i for i, value in enumerate(year_row)
                 if str(value).strip() == "2026-27"]
    if len(positions) != 2:
        raise RuntimeError(f"Expected level and growth FY2026-27 columns; found {positions}")
    gdp_row = next((row for row in rows
                    if any(isinstance(v, str) and v.strip().upper() == "GDP" for v in row)), None)
    if gdp_row is None:
        raise RuntimeError("All-India GDP row not found in workbook")
    level = gdp_row[positions[0]]
    growth = gdp_row[positions[1]]
    if not isinstance(level, (int, float)) or not isinstance(growth, (int, float)):
        raise RuntimeError("GDP level/growth observations are not numeric")
    if level <= 0 or not -100.0 < growth < 100.0:
        raise RuntimeError(f"Implausible GDP observation: level={level}, growth={growth}")
    # Independent headline cross-check: MoSPI/PIB reports real GDP ₹81.36 lakh crore
    # and 7.8% growth for this exact quarter; one lakh crore = 100,000 crore.
    if abs(level / 100000.0 - 81.36) > 0.02 or abs(growth - 7.8) > 0.15:
        raise RuntimeError(f"GDP row does not reconcile to official Q1 headline: {level}, {growth}")
    return {
        "series": "REAL_GDP_CONSTANT_2022_23",
        "period": "FY2026-27-Q1",
        "dimension": "ALL_INDIA",
        "value": float(level),
        "unit": "INR_CRORE",
        "yoy_growth_percent": float(growth),
        "base_year": "2022-23",
        "source_table_id": TABLE_ID,
    }

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    retrieved = datetime.now(timezone.utc).isoformat()
    record, catalogue = catalogue_record()
    filename = Path(str(record["file_name"])).name
    if filename != record["file_name"] or not filename.lower().endswith(".xlsx"):
        raise RuntimeError("Unsafe or unexpected catalogue filename")
    raw_path = OUT / filename
    download_url = DOWNLOAD + urllib.parse.quote(
        str(record["file_path"]).lstrip("/") + filename, safe="/"
    )
    downloaded = get(download_url,
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/octet-stream")
    body = downloaded["body"]
    if downloaded["status"] != 200 or not body.startswith(b"PK"):
        raise RuntimeError(
            f"Official workbook download invalid: HTTP {downloaded['status']}, "
            f"type={downloaded['content_type']}, bytes={len(body)}"
        )
    raw_path.write_bytes(body)
    inventory = workbook_inventory(raw_path)
    observation = extract_gdp_observation(raw_path)
    qa = {
        "status": "PASS",
        "source_group": "macro_indicators",
        "series": "GDP quarterly estimates with expenditure components at constant prices",
        "table_id": TABLE_ID,
        "product": PRODUCT,
        "reference_period": record["ref_period"],
        "release_date_precision": "date",
        "release_date": record["release_date"],
        "base_year": "2022-23",
        "frequency": "Quarterly",
        "domain_checks": {
            "exact_catalogue_table_id": True,
            "official_product_NAS": True,
            "quarterly_constant_price_GDP_title": True,
            "xlsx_signature_valid": True,
            "nonempty_numeric_workbook": True,
            "quarterly_labels_found": True,
        },
        "workbook": inventory,
        "observations": [observation],
    }
    manifest = {
        "retrieved_at_utc": retrieved,
        "source_publisher": "MoSPI e-Sankhyiki Data Catalogue",
        "catalogue_record": record,
        "catalogue_pagination": catalogue,
        "download_request_url": download_url,
        "download_final_url": downloaded["final_url"],
        "http_status": downloaded["status"],
        "content_type": downloaded["content_type"],
        "raw_file": filename,
        "bytes": len(body),
        "sha256": sha256(body),
        "qa_status": qa["status"],
        "limitations": [
            "One Q1 FY2026-27 constant-price GDP workbook only; not a complete GDP history.",
            "Current-price GDP is a separate table and was not merged.",
            "Release timestamp is date precision only; no time-of-day is inferred.",
            "No Factor Registry coverage promotion or production logic change."
        ],
    }
    (OUT / "workbook_inventory.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "domain_qa.json").write_text(
        json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS", "table_id": TABLE_ID,
        "reference_period": record["ref_period"],
        "release_date": record["release_date"],
        "bytes": len(body), "sha256": manifest["sha256"],
        "sheets": inventory["sheet_count"],
        "numeric_cells": inventory["numeric_cells"],
        "quarter_tokens": inventory["quarter_tokens_found"],
        "gdp_value_inr_crore": observation["value"],
        "gdp_yoy_growth_percent": observation["yoy_growth_percent"],
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
