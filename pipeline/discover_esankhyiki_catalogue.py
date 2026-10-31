#!/usr/bin/env python3
"""Discover public e-Sankhyiki Data Catalogue Excel links without authentication."""
from __future__ import annotations
import hashlib, json, re, urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
BASE="https://esankhyiki.mospi.gov.in"
CAT=BASE+"/catalogue-main/catalogue"
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-research/1.0)"
class Links(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]; self.scripts=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=="a" and a.get("href"): self.links.append(a["href"])
  if tag=="script" and a.get("src"): self.scripts.append(a["src"])
def get(url):
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/javascript,application/json,*/*"})
 with urllib.request.urlopen(req,timeout=25) as r: return r.status,r.headers.get("Content-Type",""),r.geturl(),r.read(5000001)
def main():
 out=Path("artifacts/esankhyiki_catalogue_discovery"); out.mkdir(parents=True,exist_ok=True)
 status,ct,final,body=get(CAT); html=body.decode("utf-8","replace")
 p=Links(); p.feed(html)
 report={"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"catalogue":{"url":CAT,"status":status,"content_type":ct,"final_url":final,"bytes":len(body),"sha256":hashlib.sha256(body).hexdigest()},
 "script_urls":[],"catalogue_excel_links":[],"api_route_candidates":[],"notes":[]}
 for href in p.links:
  u=href if href.startswith("http") else BASE+"/"+href.lstrip("/")
  if ".xlsx" in u.lower() or ".xls" in u.lower(): report["catalogue_excel_links"].append(u)
 for src in p.scripts:
  u=src if src.startswith("http") else BASE+"/"+src.lstrip("/")
  report["script_urls"].append(u)
  try:
   s,typ,fu,b=get(u); txt=b.decode("utf-8","replace")
   (out/"catalogue_app_bundle.js").write_bytes(b)
   for marker in ("/API/IIP","IIPMFY","catalogue-main","download"):
    start=0
    while True:
     pos=txt.lower().find(marker.lower(),start)
     if pos<0: break
     report.setdefault("bundle_context",[]).append({"marker":marker,"offset":pos,"context":txt[max(0,pos-1200):pos+2400]})
     start=pos+len(marker)
     if len(report.get("bundle_context",[]))>=40: break
   for m in re.finditer(r'(?i)(?:/api/[A-Za-z0-9_./?=&-]+|[A-Za-z0-9_./-]+\.xlsx(?:\?[A-Za-z0-9_=&-]+)?)',txt):
    v=m.group(0)
    if any(k in v.lower() for k in ("catalog","download","table","excel","iip","dataset","file")):
     report["api_route_candidates"].append({"bundle":fu,"candidate":v[:500]})
  except Exception as e: report["notes"].append({"script":u,"error":str(e)})
 report["api_route_candidates"]=list({(x["bundle"],x["candidate"]):x for x in report["api_route_candidates"]}.values())[:250]
 report["catalogue_excel_links"]=sorted(set(report["catalogue_excel_links"]))
 (out/"catalogue_discovery.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 (out/"catalogue_landing.html").write_bytes(body)
 print(json.dumps({"catalogue_status":status,"script_count":len(p.scripts),"excel_links":len(report["catalogue_excel_links"]),"route_candidates":len(report["api_route_candidates"]),"first_candidates":report["api_route_candidates"][:15]},indent=2))
if __name__=="__main__": main()
