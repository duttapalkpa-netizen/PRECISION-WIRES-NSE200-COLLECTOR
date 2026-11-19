#!/usr/bin/env python3
"""Capture official IMF SDMX Central registration inventory and isolate BOP/BR1 rows."""
import hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import xml.etree.ElementTree as ET
OUT=Path("artifacts/imf_registration_inventory");OUT.mkdir(parents=True,exist_ok=True)
URL="https://sdmxcentral.imf.org/data/registrations.html"
ts=datetime.now(timezone.utc).isoformat();req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-registration-inventory/1.0","Accept":"text/html"})
try:
 with urlopen(req,timeout=45) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read(20*1024*1024+1)
except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
except (URLError,TimeoutError) as e:status=0;final=URL;headers={};body=str(e).encode()
(OUT/"registrations.html").write_bytes(body)
html=body.decode("utf-8","replace")
# Extract visible table rows and anchor metadata without interpreting JS-generated UI state.
rows=[]
for tr in re.findall(r"<tr\b[^>]*>(.*?)</tr>",html,re.I|re.S):
 cells=[re.sub(r"<[^>]+>"," ",x) for x in re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>",tr,re.I|re.S)]
 cells=[" ".join(re.sub(r"&nbsp;"," ",x).split()) for x in cells]
 if len(cells)>=4:rows.append(cells[:6])
filtered=[x for x in rows if any("BOP" in c.upper() for c in x) or any("BR1" in c.upper() for c in x)]
manifest={"url":URL,"retrieved_at_utc":ts,"http_status":status,"content_type":headers.get("Content-Type"),"last_modified":headers.get("Last-Modified"),"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"html_parse":"PASS" if "<html" in html.lower() else "REVIEW","visible_table_rows":len(rows),"filtered_bop_or_br1_rows":filtered,"note":"This is only the server-rendered HTML snapshot; JavaScript-backed pagination/search may not be included."}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")
print(json.dumps(manifest,indent=2,ensure_ascii=False))
if status!=200:raise SystemExit("Registration inventory fetch failed")
