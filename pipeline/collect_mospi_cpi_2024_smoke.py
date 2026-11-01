#!/usr/bin/env python3
"""Bounded live MoSPI CPI 2024=100 official workbook smoke + domain QA.

Fetches one exact All-India Combined General CPI table, preserves source bytes,
provenance and hashes, and checks the September 2026 published headline.
Does not merge CPI 2012=100, back-series, or promote Factor Registry coverage.
"""
from __future__ import annotations
import hashlib, json, ssl, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path
from openpyxl import load_workbook

API = "https://api.mospi.gov.in/api/esankhyiki/"
LIST = API + "cms/golden-sheet/list"
DOWNLOAD = API + "file/download/"
PRODUCT = "CPI"
TABLE_ID = "CPIMCY26004SEP"
OUT = Path("artifacts/mospi_cpi_2024_smoke")
UA = "Mozilla/5.0 (compatible; PRECISION-WIRES-CPI-2024-Smoke/1.0)"
EXPECTED = {"index": 109.49, "inflation": 5.54}

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def opener():
    ctx = ssl.create_default_context()
    ctx.set_ciphers("DEFAULT:@SECLEVEL=1")
    ctx.options |= 0x4
    return urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))

def get(url: str, accept="application/json, */*"):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":accept,
      "Origin":"https://esankhyiki.mospi.gov.in",
      "Referer":"https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI"})
    with opener().open(req,timeout=35) as response:
        body=response.read(40_000_000)
        return {"status":response.status,"content_type":response.headers.get("Content-Type",""),
                "final_url":response.geturl(),"body":body}

def catalogue_record():
    pages=[]
    for page in range(1,6):  # bounded: at most 50 catalogue records
        url=LIST+"?"+urllib.parse.urlencode({"product":PRODUCT,"page":page,"limit":10})
        res=get(url)
        if res["status"]!=200: raise RuntimeError(f"CPI catalogue HTTP {res['status']}")
        payload=json.loads(res["body"].decode("utf-8-sig"))
        records=list(payload.get("data") or [])
        pages.append({"page":page,"records":len(records),"sha256":sha256(res["body"]),
                      "request_url":url})
        matches=[r for r in records if str(r.get("unique_id",""))==TABLE_ID]
        if matches:
            if len(matches)!=1: raise RuntimeError("Duplicate exact CPI table ID in catalogue")
            r=matches[0]
            required=("unique_id","product","table_name","ref_period","release_date","file_path","file_name")
            missing=[k for k in required if not r.get(k)]
            if missing: raise RuntimeError(f"CPI catalogue metadata missing: {missing}")
            title=str(r["table_name"]).lower()
            if r["product"]!=PRODUCT or "combined" not in title or "general" not in title:
                raise RuntimeError(f"Unexpected CPI catalogue record: {r}")
            if "2024" not in title and "2024" not in str(r):
                raise RuntimeError("Catalogue record does not identify CPI base 2024")
            if "september" not in str(r.get("ref_period","")).lower() and "sep" not in str(r.get("ref_period","")).lower():
                raise RuntimeError(f"Wrong CPI reference period: {r.get('ref_period')}")
            return r,{"pages_checked":pages,"scope":"maximum five catalogue pages / 50 records; exact table ID only"}
        meta=payload.get("meta_data") or {}
        if page>=int(meta.get("totalPages") or 5) or not records: break
    raise RuntimeError(f"Exact CPI 2024 September combined table {TABLE_ID} not found in bounded catalogue scan")

def inspect_workbook(path):
    wb=load_workbook(path,read_only=True,data_only=True)
    sheets=[]; values=[]; nonempty=0; numeric=0
    for ws in wb.worksheets:
        sample=[]; nr=nc=0; maxrow=maxcol=0
        for ri,row in enumerate(ws.iter_rows(),start=1):
            vals=[c.value for c in row]
            if any(v is not None for v in vals):
                nr+=sum(v is not None for v in vals); maxrow=max(maxrow,ri); maxcol=max(maxcol,len(vals))
                if len(sample)<15: sample.append([str(v) if v is not None else None for v in vals[:16]])
            for v in vals:
                if isinstance(v,(int,float)) and not isinstance(v,bool):
                    nc+=1; numeric+=1; values.append(float(v))
        nonempty+=nr
        sheets.append({"sheet":ws.title,"nonempty_cells":nr,"numeric_cells":nc,
                       "max_row_observed":maxrow,"max_column_observed":maxcol,"sample_rows":sample})
    wb.close()
    if not sheets or not numeric: raise RuntimeError("CPI workbook has no numeric data")
    def has(target): return any(abs(v-target)<0.015 for v in values)
    checks={"published_combined_general_index_109_49_present":has(EXPECTED["index"]),
            "published_combined_general_yoy_inflation_5_54_present":has(EXPECTED["inflation"])}
    if not all(checks.values()):
        raise RuntimeError(f"CPI workbook does not reconcile to official Sep-2026 headline: {checks}")
    return {"sheet_count":len(sheets),"nonempty_cells":nonempty,"numeric_cells":numeric,
            "domain_checks":checks,"sheets":sheets}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    retrieved=datetime.now(timezone.utc).isoformat()
    record,catalogue=catalogue_record()
    filename=Path(str(record["file_name"])).name
    if filename!=record["file_name"] or not filename.lower().endswith(".xlsx"):
        raise RuntimeError(f"Unsafe/unexpected CPI filename: {filename}")
    url=DOWNLOAD+urllib.parse.quote(str(record["file_path"]).lstrip("/") + filename,safe="/")
    res=get(url,"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/octet-stream")
    body=res["body"]
    if res["status"]!=200 or not body.startswith(b"PK"):
        raise RuntimeError(f"Invalid CPI workbook download: HTTP {res['status']}, bytes={len(body)}, type={res['content_type']}")
    raw=OUT/filename; raw.write_bytes(body)
    inventory=inspect_workbook(raw)
    qa={"status":"PASS","source_group":"macro_indicators","series":"All India Combined General CPI index and inflation",
        "table_id":TABLE_ID,"product":"CPI","base_year":"2024=100","frequency":"Monthly",
        "reference_period":record["ref_period"],"release_date":record["release_date"],
        "release_date_precision":"date","expected_published_headline":EXPECTED,
        "domain_checks":{"exact_catalogue_table_id":True,"official_CPI_product":True,
          "combined_general_table":True,"base_year_2024":True,"xlsx_signature_valid":True,
          **inventory["domain_checks"]},"workbook":inventory,
        "limitations":["One All-India Combined General September 2026 table only; not a complete CPI time series.",
          "CPI 2012=100 is not merged; CPI 2024=100 only.",
          "September 2026 is provisional as stated in the official release.",
          "Release time-of-day is not inferred from date-only catalogue metadata.",
          "No Factor Registry promotion or production logic change."]}
    manifest={"retrieved_at_utc":retrieved,"source_publisher":"MoSPI e-Sankhyiki Data Catalogue",
      "catalogue_record":record,"catalogue_scan":catalogue,"download_request_url":url,
      "download_final_url":res["final_url"],"http_status":res["status"],"content_type":res["content_type"],
      "raw_file":filename,"bytes":len(body),"sha256":sha256(body),"qa_status":"PASS"}
    (OUT/"workbook_inventory.json").write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+"\n")
    (OUT/"domain_qa.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n")
    (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"PASS","table_id":TABLE_ID,"reference_period":record["ref_period"],
      "release_date":record["release_date"],"bytes":len(body),"sha256":manifest["sha256"],
      "numeric_cells":inventory["numeric_cells"],"domain_checks":inventory["domain_checks"]},indent=2))

if __name__=="__main__": main()
