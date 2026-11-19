#!/usr/bin/env python3
"""Capture official IMF registration inventory using exact route exposed by page-owned JS."""
import hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
OUT=Path("artifacts/imf_registration_inventory");OUT.mkdir(parents=True,exist_ok=True)
PAGE="https://sdmxcentral.imf.org/data/registrations.html"
JS="https://sdmxcentral.imf.org/assets/js/pages/data/registrations.js?v=11.24.0"
DATA="https://sdmxcentral.imf.org/registration/id?format=fusion-json&includeMetrics=true"
def fetch(url,accept,name):
 ts=datetime.now(timezone.utc).isoformat();req=Request(url,headers={"User-Agent":"PRECISION-WIRES-registration-inventory/1.0","Accept":accept})
 try:
  with urlopen(req,timeout=60) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read(50*1024*1024+1)
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
 (OUT/name).write_bytes(body)
 return {"url":url,"retrieved_at_utc":ts,"http_status":status,"final_url":final,"content_type":headers.get("Content-Type"),"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest()},body
pm,pb=fetch(PAGE,"text/html","registrations.html")
jm,jb=fetch(JS,"application/javascript","registrations.js")
dm,db=fetch(DATA,"application/json","registration_inventory.json")
js=jb.decode("utf-8","replace")
# Verify route string and root base URL are present in the two captured official page assets.
route_ok="registration/id?format=fusion-json&includeMetrics=true" in js
try:
 obj=json.loads(db); items=obj.get("data",obj) if isinstance(obj,dict) else obj
 if isinstance(items,dict):items=[items]
 matches=[]
 for x in items if isinstance(items,list) else []:
  s=json.dumps(x,ensure_ascii=False).upper()
  if "BOP" in s or "BR1" in s:matches.append(x)
 summary={"parse":"PASS","top_level_type":type(obj).__name__,"item_count":len(items) if isinstance(items,list) else None,"bop_or_br1_matches":matches}
except Exception as e:summary={"parse":"REVIEW","error":str(e),"body_preview":db[:800].decode("utf-8","replace")}
manifest={"page":pm,"page_module":jm,"data_endpoint":dm,"route_confirmed_in_page_module":route_ok,"data_summary":summary,"interpretation":"The exact endpoint path is taken from the official page JS; no credentials or write methods used."}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")
print(json.dumps(manifest,indent=2,ensure_ascii=False))
if pm["http_status"]!=200 or jm["http_status"]!=200 or dm["http_status"]!=200 or not route_ok:raise SystemExit("One or more official public inventory requests failed")
