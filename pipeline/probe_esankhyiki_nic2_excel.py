#!/usr/bin/env python3
"""Verify one exact public NIC-2 monthly workbook using observed catalogue metadata."""
import hashlib,json,ssl,urllib.parse,urllib.request,urllib.error
from datetime import datetime,timezone
from pathlib import Path
from io import BytesIO
import pandas as pd
BASE="https://api.mospi.gov.in/api/esankhyiki/"
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-research/1.0)"
def get(url,accept="application/json, */*"):
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":accept,"Content-Type":"application/json","Origin":"https://esankhyiki.mospi.gov.in","Referer":"https://esankhyiki.mospi.gov.in/catalogue-main/catalogue"})
 ctx=ssl.create_default_context();ctx.set_ciphers("DEFAULT:@SECLEVEL=1");ctx.options|=0x4
 op=urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
 try:
  with op.open(req,timeout=45) as r:return r.status,r.headers.get("Content-Type",""),r.geturl(),r.read(30000000)
 except urllib.error.HTTPError as e:return e.code,e.headers.get("Content-Type",""),e.geturl(),e.read(2000000)
def main():
 out=Path("artifacts/esankhyiki_iip_workbook_probe");out.mkdir(parents=True,exist_ok=True)
 url=BASE+"cms/golden-sheet/list?"+urllib.parse.urlencode({"unique_id":"IIPMFY26018AUG"})
 s,ct,fu,b=get(url); payload=json.loads(b.decode("utf-8-sig"))
 data=payload.get("data",[])
 if not data: raise RuntimeError("Exact NIC-2 monthly table metadata not returned")
 row=data[0]
 required=["unique_id","table_name","release_date","ref_period","file_path","file_name","data_source"]
 missing=[k for k in required if not row.get(k)]
 if missing:raise RuntimeError("Metadata missing required fields: "+",".join(missing))
 rel=BASE+"file/download/"+urllib.parse.quote(row["file_path"].lstrip("/")+row["file_name"],safe="/")
 ds,dct,dfu,db=get(rel,"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/octet-stream")
 if ds!=200 or not db.startswith(b"PK"):raise RuntimeError(f"Workbook download not verified: status={ds}, type={dct}, bytes={len(db)}")
 xlsx=out/"IIPMFY26018AUG.xlsx";xlsx.write_bytes(db)
 xl=pd.ExcelFile(BytesIO(db));sheets=[]
 for name in xl.sheet_names:
  frame=pd.read_excel(BytesIO(db),sheet_name=name,header=None,dtype=object)
  sheets.append({"sheet":name,"rows":len(frame),"columns":len(frame.columns),"preview":frame.head(8).fillna("").astype(str).values.tolist()})
 report={"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"catalogue_api_url":url,"catalogue_http_status":s,"catalogue_response_sha256":hashlib.sha256(b).hexdigest(),"record":{k:row.get(k) for k in required+["catalogue_code","year","frequency","created_at","updated_at","status"]},"download_url":rel,"download_http_status":ds,"download_content_type":dct,"download_final_url":dfu,"download_bytes":len(db),"download_sha256":hashlib.sha256(db).hexdigest(),"excel_sheets":sheets,"decision":"SINGLE_WORKBOOK_PUBLIC_DOWNLOAD_AND_PARSE_PASS"}
 (out/"workbook_probe.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({k:report[k] for k in ("record","download_http_status","download_content_type","download_bytes","download_sha256","excel_sheets","decision")},ensure_ascii=False,indent=2)[:18000])
if __name__=="__main__":main()
