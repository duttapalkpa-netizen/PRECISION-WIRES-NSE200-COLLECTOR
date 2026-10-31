#!/usr/bin/env python3
"""Probe observed public catalogue listing filters and capture HTTP error bodies."""
import hashlib,json,ssl,urllib.parse,urllib.request,urllib.error
from datetime import datetime,timezone
from pathlib import Path
BASE="https://api.mospi.gov.in/api/esankhyiki/cms/golden-sheet/"
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-research/1.0)"
def get(url):
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"application/json, */*","Content-Type":"application/json","Origin":"https://esankhyiki.mospi.gov.in","Referer":"https://esankhyiki.mospi.gov.in/catalogue-main/catalogue"})
 context=ssl.create_default_context();context.set_ciphers("DEFAULT:@SECLEVEL=1");context.options|=0x4
 opener=urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
 try:
  with opener.open(req,timeout=30) as r:return r.status,r.headers.get("Content-Type",""),r.read(8000000)
 except urllib.error.HTTPError as e:return e.code,e.headers.get("Content-Type",""),e.read(2000000)
def main():
 out=Path("artifacts/esankhyiki_iip_catalogue_api");out.mkdir(parents=True,exist_ok=True)
 variants=[
  ("distinct", "distinct-products", {"product":"IIP"}),
  ("list_product", "list", {"product":"IIP"}),
  ("list_product_page", "list", {"product":"IIP","page":1}),
  ("list_product_page_limit", "list", {"product":"IIP","page":1,"limit":10}),
  ("list_ref_period", "list", {"product":"IIP","ref_period":"2026"}),
 ]
 report={"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"source":"official MoSPI e-Sankhyiki public catalogue API","responses":[]}
 for name,endpoint,params in variants:
  url=BASE+endpoint+"?"+urllib.parse.urlencode(params)
  try:
   status,ct,b=get(url);(out/(name+".bin")).write_bytes(b)
   try:payload=json.loads(b.decode("utf-8-sig"))
   except Exception:payload=None
   item={"name":name,"url":url,"status":status,"content_type":ct,"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"json":payload is not None}
   if payload is not None:
    item["keys"]=list(payload)[:30] if isinstance(payload,dict) else []
    item["payload"]=payload
   else:item["body_preview"]=b[:2000].decode("utf-8","replace")
   report["responses"].append(item)
  except Exception as e:report["responses"].append({"name":name,"url":url,"error":str(e)})
 (out/"catalogue_api_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 for x in report["responses"]:
  print(json.dumps({k:x.get(k) for k in ("name","status","content_type","bytes","json","keys","body_preview","error")},ensure_ascii=False)[:4000])
  if x.get("payload") and x["name"]!="distinct":print(json.dumps(x["payload"],ensure_ascii=False)[:10000])
if __name__=="__main__":main()
