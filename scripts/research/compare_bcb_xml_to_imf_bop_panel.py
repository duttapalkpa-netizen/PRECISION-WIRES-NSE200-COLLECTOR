#!/usr/bin/env python3
"""BCB monthly source versus IMF quarterly API; verify operational SCALE handling.

BCB BCA_BP6_USD is monthly current-account balance in USD millions (UNIT_MULT=6).
For each quarter, sum the three BCB monthly values and multiply by 10^6 to USD,
then compare with IMF BOP API CAB quarterly values. This tests whether IMF API
OBS_VALUE is already expanded to USD despite retaining SCALE=6 metadata.
No scaling is applied to the portfolio pilot panel.
"""
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
from decimal import Decimal
import hashlib,json,xml.etree.ElementTree as ET,csv,io
URL="https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
OUT=Path("bcb_bop_scale_crosscheck");OUT.mkdir(exist_ok=True)
def local(t):return t.split("}")[-1]
def sha(b):return hashlib.sha256(b).hexdigest()
ts=datetime.now(timezone.utc).isoformat()
req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-BCB-IMF-BOP-crosscheck/1.1","Accept":"application/xml, text/xml, */*"})
try:
 with urlopen(req,timeout=90) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
except (URLError,TimeoutError) as e:status=0;final=URL;headers={};body=str(e).encode()
safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
raw=OUT/"bcb_bop_bpm6.xml";raw.write_bytes(body)
manifest={"url":URL,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,
 "byte_count":len(body),"sha256":sha(body),"raw_file":raw.name}
monthly={};bcb_series=[]
header_info={};root_tag=None
if status==200:
 root=ET.fromstring(body);root_tag=root.tag
 for e in root.iter():
  if local(e.tag)=="Header":header_info={local(x.tag):x.text for x in e if x.text}
 for s in root.iter():
  if local(s.tag)!="Series":continue
  if s.attrib.get("INDICATOR")=="BCA_BP6_USD" and s.attrib.get("REF_AREA")=="BR" and s.attrib.get("FREQ")=="M":
   bcb_series.append(dict(s.attrib))
   for o in s:
    if local(o.tag)=="Obs":
     monthly[o.attrib["TIME_PERIOD"]]=Decimal(o.attrib["OBS_VALUE"])
# Independent IMF public API quarterly current account series, same BOP DSD.
imf_file=Path("imf_bop_broad_probe/BRA_current_account_quarterly.csv")
imf={}
if imf_file.exists():
 with imf_file.open(encoding="utf-8-sig",newline="") as f:
  for x in csv.DictReader(f):
   if x.get("BOP_ACCOUNTING_ENTRY")=="NETCD_T" and x.get("INDICATOR")=="CAB" and x.get("UNIT")=="USD" and x.get("FREQUENCY")=="Q":
    if "2015-Q1"<=x["TIME_PERIOD"]<="2026-Q3":imf[x["TIME_PERIOD"]]=Decimal(x["OBS_VALUE"])
checks=[]
for q,api_value in sorted(imf.items()):
 y,qn=q.split("-Q");m=[f"{y}-{i:02d}" for i in range((int(qn)-1)*3+1,(int(qn)-1)*3+4)]
 if all(x in monthly for x in m):
  bcb_million=sum(monthly[x] for x in m)
  bcb_usd=bcb_million*Decimal(10**6)
  diff=bcb_usd-api_value
  checks.append({"quarter":q,"bcb_monthly_sum_usd_millions":str(bcb_million),
   "bcb_sum_converted_to_usd":str(bcb_usd),"imf_api_obs_value_usd":str(api_value),
   "difference_usd":str(diff),"match_within_0_01_usd":abs(diff)<=Decimal("0.01")})
summary={"scope":"BCB official monthly current account versus IMF quarterly API current account; operational SCALE test",
 "bcb_manifest":manifest,"bcb_xml_root":root_tag,"bcb_header":header_info,
 "bcb_series":bcb_series,"bcb_month_count":len(monthly),
 "bcb_unit_multiplier":"6","bcb_unit_multiplier_label":"Millions",
 "imf_dataflow":"IMF.STA:BOP(21.0.0)","imf_dsd":"IMF.STA:DSD_BOP(24.0.0)",
 "imf_series_key":"BRA.NETCD_T.CAB.USD.Q","imf_scale_attribute":"6",
 "imf_obs_value_unit_dimension":"USD","period_window":["2015-Q1","2026-Q3"],
 "imf_quarter_count":len(imf),"quarter_comparison_count":len(checks),
 "matches_within_0_01_usd":sum(x["match_within_0_01_usd"] for x in checks),
 "mismatches":[x for x in checks if not x["match_within_0_01_usd"]],
 "decision":"API_OBS_VALUE_ALREADY_USD_NO_SECOND_SCALE_MULTIPLICATION" if checks and len(checks)==len(imf) and all(x["match_within_0_01_usd"] for x in checks) else "SCALE_APPLICATION_NOT_CLOSED",
 "scope_limit":"This proves operational scale handling for the tested CAB series in this BOP API. It is not a direct BCB portfolio-investment series crosswalk; do not claim that portfolio source series was separately reconciled.",
 "portfolio_panel_policy":"Keep P_F OBS_VALUE as returned in USD; preserve SCALE=6 as source metadata; do not multiply by 10^6 again.",
 "scale_conversion_applied_to_panel":False}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
with (OUT/"comparison.csv").open("w",newline="",encoding="utf-8") as f:
 fields=["quarter","bcb_monthly_sum_usd_millions","bcb_sum_converted_to_usd","imf_api_obs_value_usd","difference_usd","match_within_0_01_usd"]
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for x in checks:w.writerow(x)
print(json.dumps(summary,indent=2,ensure_ascii=False))
if status!=200 or not bcb_series or len(checks)!=len(imf) or not all(x["match_within_0_01_usd"] for x in checks):
 raise SystemExit("BCB-to-IMF scale reconciliation did not pass")
