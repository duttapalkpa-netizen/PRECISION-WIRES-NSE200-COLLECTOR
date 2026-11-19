#!/usr/bin/env python3
"""Capture public IMF registration page and its own JS module to discover exact read-only route."""
import hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
OUT=Path("artifacts/imf_registration_inventory");OUT.mkdir(parents=True,exist_ok=True)
URL="https://sdmxcentral.imf.org/data/registrations.html"
JS_URL="https://sdmxcentral.imf.org/assets/js/pages/data/registrations.js?v=11.24.0"
def fetch(url,accept):
 ts=datetime.now(timezone.utc).isoformat();req=Request(url,headers={"User-Agent":"PRECISION-WIRES-registration-inventory/1.0","Accept":accept})
 try:
  with urlopen(req,timeout=45) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read(10*1024*1024+1)
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
 return {"url":url,"retrieved_at_utc":ts,"http_status":status,"content_type":headers.get("Content-Type"),"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"final_url":final},body
page_meta,page=fetch(URL,"text/html");(OUT/"registrations.html").write_bytes(page)
js_meta,jsbody=fetch(JS_URL,"application/javascript");(OUT/"registrations.js").write_bytes(jsbody);js=jsbody.decode("utf-8","replace")
# Capture endpoint-like literals from the exact page-owned module; do not call an inferred route.
routes=sorted(set(re.findall(r'.{0,100}(?:registration|registrations|/ws/).{0,180}',js,re.I)))
manifest={"page":page_meta,"page_sha256":page_meta["sha256"],"page_module":js_meta,"page_module_route_candidates":routes,"server_rendered_html_rows":len(re.findall(r"<tr\\b",page.decode("utf-8","replace"),re.I)),"note":"Static HTML omitted the JS-populated inventory. Route candidates are evidence only; do not call until inspected."}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\\n")
print(json.dumps(manifest,indent=2,ensure_ascii=False))
if page_meta["http_status"]!=200 or js_meta["http_status"]!=200:raise SystemExit("Page or module capture failed")
