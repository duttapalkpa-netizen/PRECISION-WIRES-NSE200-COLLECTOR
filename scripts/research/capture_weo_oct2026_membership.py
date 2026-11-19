#!/usr/bin/env python3
"""Capture official IMF October 2026 WEO workbook and inspect Country Groups sheet."""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,zipfile
from openpyxl import load_workbook

URL="https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx"
OUT=Path("weo_oct2026_capture"); OUT.mkdir(exist_ok=True)
ts=datetime.now(timezone.utc).isoformat()
req=Request(URL,headers={"User-Agent":"Mozilla/5.0 PRECISION-WIRES research evidence capture","Accept":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream,*/*"})
try:
 with urlopen(req,timeout=120) as r:
  status=r.status; headers=dict(r.headers.items()); data=r.read()
except HTTPError as e:
 status=e.code; headers=dict(e.headers.items()) if e.headers else {}; data=e.read()
except (URLError,TimeoutError) as e:
 raise SystemExit(f"download failed: {e}")
if status!=200: raise SystemExit(f"IMF workbook HTTP {status}: {data[:500]!r}")
if not data.startswith(b"PK"): raise SystemExit(f"Response not XLSX ZIP: {headers}; bytes={len(data)}")
path=OUT/"WEOOct2026all.xlsx"; path.write_bytes(data)
wb=load_workbook(path,read_only=True,data_only=True)
report={"source_url":URL,"retrieved_at_utc":ts,"http_status":status,
 "headers":{k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization"}},
 "byte_count":len(data),"sha256":hashlib.sha256(data).hexdigest(),
 "sheetnames":wb.sheetnames,"sheets":[]}
for ws in wb.worksheets:
 info={"title":ws.title,"max_row":ws.max_row,"max_column":ws.max_column,"matching_rows":[]}
 for row in ws.iter_rows():
  vals=[c.value for c in row]
  txt=" | ".join(str(v) for v in vals if v is not None)
  if any(term in txt.lower() for term in ("emerging market and developing economies","emerging and developing economies","emerging market & developing economies","emerging market and developing")):
   info["matching_rows"].append({"row":row[0].row,"values":vals[:30]})
 info["sample_rows"]=[]
 for row in ws.iter_rows(min_row=1,max_row=min(ws.max_row,8),values_only=True):
  info["sample_rows"].append(list(row[:20]))
 report["sheets"].append(info)
wb.close()
(OUT/"workbook_inspection.json").write_text(json.dumps(report,indent=2,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2,ensure_ascii=False,default=str))
