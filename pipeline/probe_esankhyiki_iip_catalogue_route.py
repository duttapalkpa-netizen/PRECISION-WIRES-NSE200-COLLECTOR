#!/usr/bin/env python3
"""Inspect the public IIP catalogue route and preserve exact response evidence."""
import hashlib,json,urllib.request
from datetime import datetime,timezone
from pathlib import Path
BASE="https://esankhyiki.mospi.gov.in"
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-research/1.0)"
def get(url):
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"application/json,text/plain,*/*","Referer":BASE+"/catalogue-main/catalogue"})
 with urllib.request.urlopen(req,timeout=25) as r:
  b=r.read(5000001)
  return {"status":r.status,"content_type":r.headers.get("Content-Type",""),"url":r.geturl(),"body":b}
def main():
 out=Path("artifacts/esankhyiki_iip_catalogue_route");out.mkdir(parents=True,exist_ok=True)
 urls=[BASE+"/API/IIP",BASE+"/API/IIP?PageNumber=1&PageSize=10",BASE+"/API/IIP?page=1&limit=10"]
 results=[]
 for url in urls:
  try:
   r=get(url); (out/(str(len(results))+".bin")).write_bytes(r["body"])
   body=r["body"].decode("utf-8","replace")
   try:
    j=json.loads(body); summary={"json":True,"type":type(j).__name__,"keys":list(j)[:30] if isinstance(j,dict) else [],"sample":j[:2] if isinstance(j,list) else {k:v for k,v in list(j.items())[:8]} if isinstance(j,dict) else j}
   except Exception: summary={"json":False,"preview":body[:1500]}
   results.append({"request_url":url,"status":r["status"],"content_type":r["content_type"],"final_url":r["url"],"bytes":len(r["body"]),"sha256":hashlib.sha256(r["body"]).hexdigest(),"summary":summary})
  except Exception as e: results.append({"request_url":url,"error":str(e)})
 report={"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"source":"official MoSPI e-Sankhyiki","results":results,"decision":"ROUTE_RESPONSE_DISCOVERY_ONLY"}
 (out/"route_probe.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps(results,ensure_ascii=False,indent=2)[:12000])
if __name__=="__main__":main()
