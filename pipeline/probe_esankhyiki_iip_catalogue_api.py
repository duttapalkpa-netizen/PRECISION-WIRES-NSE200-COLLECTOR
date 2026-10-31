#!/usr/bin/env python3
"""Call observed public e-Sankhyiki catalogue endpoints and inspect IIP metadata."""
import hashlib,json,urllib.parse,urllib.request,ssl
from datetime import datetime,timezone
from pathlib import Path
BASE="https://api.mospi.gov.in/api/esankhyiki/cms/golden-sheet/"
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-research/1.0)"
def get(url):
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"application/json, */*","Content-Type":"application/json","Origin":"https://esankhyiki.mospi.gov.in","Referer":"https://esankhyiki.mospi.gov.in/catalogue-main/catalogue"})
 # Retain certificate and hostname verification while allowing the legacy TLS
 # renegotiation profile required by the official API host.
 context=ssl.create_default_context()
 context.set_ciphers("DEFAULT:@SECLEVEL=1")
 context.options |= 0x4  # OP_LEGACY_SERVER_CONNECT; certificate verification remains enabled
 opener=urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
 with opener.open(req,timeout=30) as r:
  b=r.read(8000000);return r.status,r.headers.get("Content-Type",""),b
def main():
 out=Path("artifacts/esankhyiki_iip_catalogue_api");out.mkdir(parents=True,exist_ok=True)
 requests=[
  ("distinct",BASE+"distinct-products?"+urllib.parse.urlencode({"product":"IIP"})),
  ("list",BASE+"list?"+urllib.parse.urlencode({"product":"IIP","page":1,"limit":1000})),
 ]
 report={"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"source":"official MoSPI e-Sankhyiki public catalogue API","responses":[]}
 for name,url in requests:
  try:
   status,ct,b=get(url);(out/(name+".json")).write_bytes(b)
   try: payload=json.loads(b.decode("utf-8-sig"))
   except Exception: payload=None
   report["responses"].append({"name":name,"url":url,"status":status,"content_type":ct,"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"json":payload is not None,"top_keys":list(payload)[:30] if isinstance(payload,dict) else [],"payload":payload})
  except Exception as e: report["responses"].append({"name":name,"url":url,"error":str(e)})
 (out/"catalogue_api_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 for r in report["responses"]:
  print(json.dumps({k:r.get(k) for k in ("name","url","status","content_type","bytes","json","top_keys","error")},ensure_ascii=False))
  p=r.get("payload")
  if p:
   print(json.dumps(p,ensure_ascii=False)[:10000])
if __name__=="__main__":main()
