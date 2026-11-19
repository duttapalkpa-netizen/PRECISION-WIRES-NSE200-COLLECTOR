#!/usr/bin/env python3
"""Compare BCB-registered source XML with IMF public BOP exact-key Brazil series.

This is a source-to-source check only. It does not infer that BOP6 and
BOP_BPM6 dataflows are equivalent and does not apply SCALE transformations.
"""
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET,csv,io
URL="https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
OUT=Path("bcb_bop_scale_crosscheck");OUT.mkdir(exist_ok=True)
def local(t):return t.split("}")[-1]
def sha(b):return hashlib.sha256(b).hexdigest()
ts=datetime.now(timezone.utc).isoformat()
req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-BCB-IMF-BOP-crosscheck/1.0","Accept":"application/xml, text/xml, */*"})
try:
 with urlopen(req,timeout=90) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
except (URLError,TimeoutError) as e:status=0;final=URL;headers={};body=str(e).encode()
safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
raw=OUT/"bcb_bop_bpm6.xml";raw.write_bytes(body)
manifest={"url":URL,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,
 "byte_count":len(body),"sha256":sha(body),"raw_file":raw.name}
matches=[];root_tag=None;header_info={}
if status==200:
 root=ET.fromstring(body);root_tag=root.tag
 for e in root.iter():
  if local(e.tag)=="Header":
   header_info={local(x.tag):x.text for x in e if x.text}
 for s in root.iter():
  if local(s.tag)!="Series":continue
  dims={}
  for e in s.iter():
   if local(e.tag)=="Value" and e.attrib.get("id"):dims[e.attrib["id"]]=e.attrib.get("value")
  if dims.get("REF_AREA")=="BRA" and dims.get("BOP_ACCOUNTING_ENTRY") in ("A_NFA_T","L_NIL_T") and dims.get("INDICATOR")=="P_F" and dims.get("UNIT")=="USD" and dims.get("FREQUENCY")=="Q":
   obs=[]
   for o in s.iter():
    if local(o.tag)=="Obs":
     t=next((x.attrib.get("value") for x in o.iter() if local(x.tag) in ("ObsDimension","TimeDimension")),None)
     v=next((x.attrib.get("value") for x in o.iter() if local(x.tag)=="ObsValue"),None)
     if t and v is not None:obs.append({"TIME_PERIOD":t,"OBS_VALUE":v})
   matches.append({"dimensions":dims,"observations":obs})
# Load IMF exact panel generated earlier in this workflow.
imf=[]
p=Path("imf_bop_portfolio_exact_panel/portfolio_flows_panel.csv")
if p.exists():
 with p.open(encoding="utf-8-sig",newline="") as f:
  for x in csv.DictReader(f):
   if x["COUNTRY"]=="BRA":imf.append(x)
comparison=[]
for m in matches:
 for o in m["observations"]:
  k=(m["dimensions"].get("BOP_ACCOUNTING_ENTRY"),o["TIME_PERIOD"])
  q=next((x for x in imf if (x["BOP_ACCOUNTING_ENTRY"],x["TIME_PERIOD"])==k),None)
  comparison.append({"entry":k[0],"period":k[1],"bcb_value":o["OBS_VALUE"],
    "imf_api_value":q["OBS_VALUE"] if q else None,
    "exact_value_match":bool(q and float(o["OBS_VALUE"])==float(q["OBS_VALUE"]))})
summary={"scope":"BCB registered source XML versus IMF BOP6 public API Brazil portfolio flow values; no scale transformation",
 "manifest":manifest,"xml_root":root_tag,"header":header_info,
 "dataflow_identity_warning":"BCB header previously identified BOP_BPM6(1.0); IMF public API panel uses BOP(21.0.0)/DSD_BOP(24.0.0). Similar values do not establish dataflow identity.",
 "target_series_count":len(matches),"target_observation_count":sum(len(x["observations"]) for x in matches),
 "series":matches,"imf_brazil_panel_rows":len(imf),
 "comparison_rows":len(comparison),"exact_value_matches":sum(x["exact_value_match"] for x in comparison),
 "value_mismatches":[x for x in comparison if x["imf_api_value"] is not None and not x["exact_value_match"]],
 "scale_values_in_imf_panel":sorted({x.get("SCALE","") for x in imf}),
 "unit_values_in_imf_panel":sorted({x.get("UNIT","") for x in imf}),
 "scale_conversion_applied":False,
 "decision":"SOURCE_MATCH_REVIEW_REQUIRED" if comparison else "NO_EXACT_SERIES_MATCH_FOUND"}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
with (OUT/"comparison.csv").open("w",newline="",encoding="utf-8") as f:
 fields=["entry","period","bcb_value","imf_api_value","exact_value_match"]
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(comparison)
print(json.dumps(summary,indent=2,ensure_ascii=False))
