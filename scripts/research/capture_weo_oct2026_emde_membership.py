#!/usr/bin/env python3
"""Capture official October 2026 WEO workbook and inspect country-group sheet.

This is membership-source acquisition only. It does not infer BOP coverage or
aggregate observations. Raw workbook and provenance are preserved.
"""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,zipfile,io,xml.etree.ElementTree as ET
URL="https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx"
OUT=Path("weo_oct2026_emde_membership");OUT.mkdir(exist_ok=True)
ts=datetime.now(timezone.utc).isoformat()
req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-WEO-membership-audit/1.0","Accept":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"})
try:
 with urlopen(req,timeout=90) as r:
  status=r.status; final=r.geturl(); headers=dict(r.headers.items()); body=r.read()
except HTTPError as e:
 status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
except (URLError,TimeoutError) as e:
 status=0;final=URL;headers={};body=str(e).encode()
safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
fn="WEOOct2026all.xlsx";(OUT/fn).write_bytes(body)
result={"source_url":URL,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,
 "byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":fn}
if status==200:
 try:
  import openpyxl
  wb=openpyxl.load_workbook(io.BytesIO(body),read_only=True,data_only=True)
  result["sheet_names"]=wb.sheetnames
  previews={}
  for name in wb.sheetnames:
   ws=wb[name]; result.setdefault("sheet_dimensions",{})[name]={"max_row":ws.max_row,"max_column":ws.max_column}
   if "group" in name.lower():
    previews[name]=[[c for c in row] for row in ws.iter_rows(min_row=1,max_row=min(ws.max_row,35),values_only=True)]
  result["country_group_sheet_preview"]=previews
  wb.close();result["workbook_parse"]="PASS"
 except Exception as e:result["workbook_parse"]="FAIL";result["parse_error"]=str(e)
else: result["workbook_parse"]="NOT_RUN"
(OUT/"manifest.json").write_text(json.dumps(result,indent=2,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2,ensure_ascii=False,default=str))
if status!=200 or result.get("workbook_parse")!="PASS":raise SystemExit("WEO workbook capture/parse failed")
