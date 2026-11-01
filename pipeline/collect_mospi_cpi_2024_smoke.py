#!/usr/bin/env python3
"""Bounded live MoSPI CPI 2024=100 September-2026 workbook QA."""
from __future__ import annotations
import hashlib,json,ssl,urllib.request
from datetime import datetime,timezone
from pathlib import Path
from openpyxl import load_workbook

SOURCE_URL="https://www.mospi.gov.in/uploads/documents/productChartTable/1792047898150-CPI_Data_For_DIID_Sep26-12.10.2026%20(1).xlsx"
OUT=Path("artifacts/mospi_cpi_2024_smoke")
EXPECTED={"index":109.49,"inflation":5.54}
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-CPI-2024-Smoke/1.1)"

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
    sheets=[]; numeric_count=0; nonempty=0
    for ws in wb.worksheets:
        sample=[]; nn=nc=0; mr=mc=0
        for ri,row in enumerate(ws.iter_rows(),1):
            vals=[c.value for c in row]
            if any(v is not None for v in vals):
                nn+=sum(v is not None for v in vals); mr=max(mr,ri); mc=max(mc,len(vals))
                if len(sample)<8: sample.append([str(v) if v is not None else None for v in vals[:12]])
            nc+=sum(isinstance(v,(int,float)) and not isinstance(v,bool) for v in vals)
        nonempty+=nn; numeric_count+=nc
        sheets.append({"sheet":ws.title,"nonempty_cells":nn,"numeric_cells":nc,
                       "max_row_observed":mr,"max_column_observed":mc,"sample_rows":sample})
    if "General" not in wb.sheetnames: wb.close(); raise RuntimeError("General sheet missing")
    ws=wb["General"]
    # Expected columns: Base Year, State Code, State Name, Sector, Year, Month, Index, Inflation, Status.
    matched=[]
    for row in ws.iter_rows(min_row=2,values_only=True):
        if len(row)>=9 and (str(row[0]).strip(),str(row[1]).strip(),str(row[2]).strip(),
            str(row[3]).strip(),str(row[4]).strip(),str(row[5]).strip().lower()) == (
            "2024","00","All India","Combined","2026","september"):
            matched.append(row)
    wb.close()
    if len(matched)!=1: raise RuntimeError(f"Expected one exact All-India Combined Sep-2026 row; found {len(matched)}")
    row=matched[0]
    try: index=float(row[6]); inflation=float(row[7])
    except (TypeError,ValueError): raise RuntimeError("Exact CPI headline row has non-numeric index/inflation")
    status=str(row[8]).strip().upper()
    checks={"exact_all_india_combined_september_2026_row":True,
      "base_year_2024":True,"combined_index_matches_109_49":abs(index-EXPECTED["index"])<0.005,
      "combined_yoy_inflation_matches_5_54":abs(inflation-EXPECTED["inflation"])<0.005,
      "provisional_status_P":status=="P"}
    if not all(checks.values()): raise RuntimeError(f"CPI exact-row domain QA failed: {checks}; row={row}")
    return {"sheet_count":len(sheets),"nonempty_cells":nonempty,"numeric_cells":numeric_count,
      "domain_checks":checks,"headline_observation":{"base_year":2024,"state_code":"00",
      "state_name":"All India","sector":"Combined","year":2026,"month":"September",
      "index":index,"inflation_percent":inflation,"status":status},
      "sheets":sheets}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    retrieved=datetime.now(timezone.utc).isoformat()
    body,http=fetch()
    raw=OUT/"CPI_Data_For_DIID_Sep26-12.10.2026.xlsx"; raw.write_bytes(body)
    inv=inspect(raw)
    qa={"status":"PASS","source_group":"macro_indicators",
      "series":"All India Combined General CPI index and inflation","base_year":"2024=100",
      "frequency":"Monthly","reference_period":"September 2026","release_date":"2026-10-12",
      "release_date_precision":"date","provisional":True,
      "domain_checks":{"official_mospi_host":http["final_url"].startswith("https://www.mospi.gov.in/"),
        "xlsx_signature_valid":True,**inv["domain_checks"]},
      "workbook":inv,"limitations":[
        "Official General sheet September 2026 rows are provisional; item/subclass/class/group/division tabs in this workbook show August 2026 in the inspected release.",
        "This is one official CPI workbook, not a complete monthly historical series.",
        "CPI 2012=100 data are not merged; only base 2024=100 is tested.",
        "Release time-of-day is not inferred from date-only metadata.",
        "No Factor Registry promotion or production logic change."]}
    manifest={"retrieved_at_utc":retrieved,"source_publisher":"Ministry of Statistics and Programme Implementation (MoSPI)",
      "source_url":SOURCE_URL,"final_url":http["final_url"],**http,
      "raw_file":raw.name,"sha256":sha256(body),"qa_status":"PASS"}
    (OUT/"workbook_inventory.json").write_text(json.dumps(inv,ensure_ascii=False,indent=2)+"\n")
    (OUT/"domain_qa.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n")
    (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"PASS","observation":inv["headline_observation"],
      "bytes":len(body),"sha256":manifest["sha256"],"numeric_cells":inv["numeric_cells"],
      "domain_checks":qa["domain_checks"]},indent=2))
if __name__=="__main__": main()
