#!/usr/bin/env python3
"""Bounded live MoSPI CPI 2024=100 September-2026 workbook QA."""
from __future__ import annotations
import hashlib,json,ssl,urllib.request
from datetime import datetime,timezone
from pathlib import Path
from openpyxl import load_workbook

SOURCE_URL="https://www.mospi.gov.in/uploads/documents/productChartTable/1792047898150-CPI_Data_For_DIID_Sep26-12.10.2026%20(1).xlsx"
OUT=Path("artifacts/mospi_cpi_2024_smoke")
EXPECTED={"combined_cpi_index":109.49,"combined_cpi_yoy_inflation":5.54}
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-CPI-2024-Smoke/1.0)"

def sha256(b): return hashlib.sha256(b).hexdigest()

def fetch():
    ctx=ssl.create_default_context()
    req=urllib.request.Request(SOURCE_URL,headers={"User-Agent":UA,"Accept":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"})
    with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx)).open(req,timeout=35) as r:
        body=r.read(40_000_000)
        meta={"http_status":r.status,"content_type":r.headers.get("Content-Type",""),
              "final_url":r.geturl(),"bytes":len(body)}
    if meta["http_status"]!=200 or not body.startswith(b"PK"):
        raise RuntimeError(f"Official MoSPI CPI XLSX invalid: {meta}")
    return body,meta

def inspect(path):
    wb=load_workbook(path,read_only=True,data_only=True)
    sheets=[]; numeric=[]; nonempty=0
    for ws in wb.worksheets:
        sample=[]; nn=0; nc=0; mr=mc=0
        for ri,row in enumerate(ws.iter_rows(),1):
            vals=[c.value for c in row]
            if any(v is not None for v in vals):
                nn+=sum(v is not None for v in vals); mr=max(mr,ri); mc=max(mc,len(vals))
                if len(sample)<20: sample.append([str(v) if v is not None else None for v in vals[:20]])
            for v in vals:
                if isinstance(v,(int,float)) and not isinstance(v,bool):
                    numeric.append(float(v)); nc+=1
        nonempty+=nn
        sheets.append({"sheet":ws.title,"nonempty_cells":nn,"numeric_cells":nc,
                       "max_row_observed":mr,"max_column_observed":mc,"sample_rows":sample})
    wb.close()
    checks={k:any(abs(v-target)<0.015 for v in numeric) for k,target in EXPECTED.items()}
    if not sheets or not numeric or not all(checks.values()):
        raise RuntimeError(f"CPI domain QA failed: checks={checks}, numeric_cells={len(numeric)}")
    return {"sheet_count":len(sheets),"nonempty_cells":nonempty,"numeric_cells":len(numeric),
            "domain_checks":checks,"sheets":sheets}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    retrieved=datetime.now(timezone.utc).isoformat()
    body,http=fetch()
    raw=OUT/"CPI_Data_For_DIID_Sep26-12.10.2026.xlsx"; raw.write_bytes(body)
    inv=inspect(raw)
    qa={"status":"PASS","source_group":"macro_indicators",
        "series":"All India Combined General CPI index and inflation",
        "base_year":"2024=100","frequency":"Monthly","reference_period":"September 2026",
        "release_date":"2026-10-12","release_date_precision":"date","provisional":True,
        "expected_published_headline":EXPECTED,"domain_checks":{
          "official_mospi_host":http["final_url"].startswith("https://www.mospi.gov.in/"),
          "xlsx_signature_valid":True,**inv["domain_checks"]},
        "workbook":inv,"limitations":[
          "One September 2026 CPI data workbook only; not a complete monthly historical series.",
          "CPI 2012=100 data are not merged.",
          "September 2026 is provisional.",
          "Release time-of-day is not inferred.",
          "No Factor Registry promotion or production logic change."]}
    manifest={"retrieved_at_utc":retrieved,"source_publisher":"Ministry of Statistics and Programme Implementation (MoSPI)",
      "source_url":SOURCE_URL,"final_url":http["final_url"],**http,
      "raw_file":raw.name,"sha256":sha256(body),"qa_status":"PASS"}
    (OUT/"workbook_inventory.json").write_text(json.dumps(inv,ensure_ascii=False,indent=2)+"\n")
    (OUT/"domain_qa.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n")
    (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"PASS","base_year":"2024=100","period":"September 2026",
      "bytes":len(body),"sha256":manifest["sha256"],"numeric_cells":inv["numeric_cells"],
      "domain_checks":qa["domain_checks"]},indent=2))
if __name__=="__main__": main()
