#!/usr/bin/env python3
"""Discover FBIL Angular bundle references and candidate API/archive routes; no auth bypass."""
import hashlib,json,re
from pathlib import Path
from urllib.parse import urljoin,urlparse
import requests
BASE="https://www.fbil.org.in/"
OUT=Path("artifacts/fbil_10y_provenance")
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 s=requests.Session();s.headers.update({"User-Agent":"Mozilla/5.0 (compatible; PRECISION-WIRES provenance audit)"})
 r=s.get(BASE,timeout=(10,40));r.raise_for_status()
 html=r.text
 assets=sorted(set(re.findall(r'<script[^>]+src=["\']([^"\']+\.js(?:\?[^"\']*)?)["\']',html,re.I)))
 report={"source_url":r.url,"http_status":r.status_code,"html_bytes":len(r.content),"html_sha256":hashlib.sha256(r.content).hexdigest(),"script_assets":[],"candidate_urls":[],"api_terms":[]}
 for asset in assets:
  u=urljoin(r.url,asset)
  try:
   x=s.get(u,timeout=(10,40));x.raise_for_status();body=x.text
   p=urlparse(u).path.rsplit("/",1)[-1]
   (OUT/p).write_bytes(x.content)
   urls=sorted(set(re.findall(r'https?[^"\'\s<>]+',body)))
   routes=sorted(set(re.findall(r'["\']([^"\']*(?:api|archive|download|goi|par.?yield)[^"\']*)["\']',body,re.I)))
   report["script_assets"].append({"url":u,"status":x.status_code,"bytes":len(x.content),"sha256":hashlib.sha256(x.content).hexdigest(),"file":p})
   report["candidate_urls"].extend(urls[:500]);report["api_terms"].extend(routes[:1000])
  except Exception as e:
   report["script_assets"].append({"url":u,"error":str(e)})
 report["candidate_urls"]=sorted(set(report["candidate_urls"]))
 report["api_terms"]=sorted(set(report["api_terms"]))
 (OUT/"fbil_js_endpoint_discovery.json").write_text(json.dumps(report,indent=2)+"\n")
 print(json.dumps(report,indent=2))
if __name__=="__main__":main()
