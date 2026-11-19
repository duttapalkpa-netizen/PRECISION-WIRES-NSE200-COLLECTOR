#!/usr/bin/env python3
"""Acquire official October 2026 WEO workbook and inventory EMDE membership tables.

No hand-entered membership. Preserve the exact workbook, response metadata,
SHA-256, sheet dimensions, headers and all Country Groups rows for inspection.
"""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,zipfile,xml.etree.ElementTree as ET
from openpyxl import load_workbook

URL="https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx"
ROOT=Path("imf_weo_oct2026_evidence"); ROOT.mkdir(exist_ok=True)
raw=ROOT/"WEOOct2026all.xlsx"
retrieved=datetime.now(timezone.utc).isoformat()
req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-IMF-WEO-Research/1.0","Accept":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,*/*"})
try:
 with urlopen(req,timeout=90) as r:
  status=r.status; headers=dict(r.headers.items()); final_url=r.geturl(); body=r.read(200*1024*1024+1)
except HTTPError as e:
 status=e.code; headers=dict(e.headers.items()) if e.headers else {}; final_url=URL; body=e.read()
except (URLError,TimeoutError) as e:
 raise SystemExit(f"Download failed: {e}")
if status!=200: raise SystemExit(f"Workbook HTTP status {status}")
if len(body)>200*1024*1024: raise SystemExit("Workbook exceeds 200 MiB safety cap")
raw.write_bytes(body)
sha=lambda b:hashlib.sha256(b).hexdigest()
safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
meta={"source_url":URL,"final_url":final_url,"retrieved_at_utc":retrieved,"http_status":status,
 "response_headers":safe,"byte_count":len(body),"sha256":sha(body),"file":str(raw)}
try:
 wb=load_workbook(raw,read_only=True,data_only=True)
except Exception as e:
 raise SystemExit(f"XLSX open/parse failed: {e}")
sheets={}
emde_hits=[]
for ws in wb.worksheets:
 maxrow=ws.max_row; maxcol=ws.max_column
 sample=[]
 for row in ws.iter_rows(min_row=1,max_row=min(maxrow or 1,15),values_only=True):
  sample.append([None if x is None else str(x) for x in row[:min(maxcol or 1,30)]])
 entry={"title":ws.title,"max_row":maxrow,"max_column":maxcol,"top_rows":sample}
 if "group" in ws.title.lower():
  all_rows=[]
  for ridx,row in enumerate(ws.iter_rows(values_only=True),start=1):
   vals=[None if x is None else str(x) for x in row]
   if any(v is not None for v in vals):
    all_rows.append({"row_number":ridx,"values":vals})
    if any("emerging market and developing economies" in (v or "").lower() for v in vals):
     emde_hits.append({"sheet":ws.title,"row_number":ridx,"values":vals})
  entry["all_nonempty_rows"]=all_rows
 sheets[ws.title]=entry
wb.close()
result={"status":"PASS_WORKBOOK_ACQUIRED" if status==200 else "FAIL","metadata":meta,
 "sheet_names":list(sheets),"sheets":sheets,"emde_text_hits":emde_hits,
 "guardrails":{"source_only_official_IMF":True,"membership_not_inferred":True,"no_synthetic_members":True}}
(ROOT/"workbook_inventory.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"status":result["status"],"metadata":meta,
 "sheet_names":list(sheets),
 "sheets":{k:{"max_row":v["max_row"],"max_column":v["max_column"],"top_rows":v["top_rows"]} for k,v in sheets.items()},
 "emde_text_hits":emde_hits},indent=2,ensure_ascii=False))
