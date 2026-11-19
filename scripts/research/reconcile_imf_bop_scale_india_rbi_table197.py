#!/usr/bin/env python3
"""Reconcile IMF India BOP portfolio-flow scale/sign against RBI Table 197.

RBI Table 197 is official BPM6 quarterly BoP in USD million. Values are
published as integer USD millions. The source rows are transcribed from the
official page and source-text assertions are checked against the captured raw
HTML. IMF raw panel values are not modified.
"""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from decimal import Decimal
import csv,json,hashlib

URL="https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=24022"
IMF_PANEL="docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv"
OUT=Path("india_rbi_table197_reconciliation"); RAW=OUT/"raw"; RAW.mkdir(parents=True,exist_ok=True)
# Published Table 197 values: RBI net = Credit - Debit, in US$ million.
# 3.2.A Portfolio Investment in India maps to liabilities.
# 3.2.B Portfolio Investment by India maps to assets; IMF A_NFA_T is the
# negative of RBI's Credit-minus-Debit net for this asset row.
RBI={
 "2024-Q2":{"quarter_label":"April-June 2024","assets_by_india_net":48,"liabilities_in_india_net":897},
 "2024-Q3":{"quarter_label":"July-September 2024","assets_by_india_net":35,"liabilities_in_india_net":19815},
 "2024-Q4":{"quarter_label":"October-December 2024","assets_by_india_net":63,"liabilities_in_india_net":-11435},
 "2025-Q1":{"quarter_label":"January-March 2025","assets_by_india_net":136,"liabilities_in_india_net":-5995},
 "2025-Q2":{"quarter_label":"April-June 2025","assets_by_india_net":-872,"liabilities_in_india_net":2481},
 "2025-Q3":{"quarter_label":"July-September 2025","assets_by_india_net":-279,"liabilities_in_india_net":-5468}
}
TOL=Decimal("0.5") # RBI Table 197 values are integer USD millions.

def fetch(url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-India-BOP-crosscheck/1.0","Accept":"text/html"})
 try:
  with urlopen(req,timeout=45) as r: status=r.status; headers=dict(r.headers.items()); body=r.read(); final=r.geturl()
 except HTTPError as e: status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read(); final=e.geturl()
 except (URLError,TimeoutError) as e: status=0; headers={}; body=str(e).encode(); final=url
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 return {"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"body":body}

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
 r=fetch(URL); body=r.pop("body"); (RAW/"RBI_Table197_20260731.html").write_bytes(body)
 source={**r,"file":"raw/RBI_Table197_20260731.html","byte_count":len(body),"sha256":sha(body)}
 if source["http_status"]!=200: raise SystemExit(f"RBI Table197 HTTP {source['http_status']}")
 page=body.decode("utf-8","replace")
 required=["Table 197","Standard Presentation of India","BPM6","April-June 2024","July-September 2024",
  "October-December 2024","January-March 2025","April-June 2025","July-September 2025",
  "Portfolio Investment in India","Portfolio Investment by India"]
 absent=[x for x in required if x.lower() not in page.lower()]
 if absent: raise SystemExit(f"RBI source page missing expected labels: {absent}")
 # Check all manually transcribed net values are present in the source page text.
 expected_values=sorted({str(v) for q in RBI.values() for v in (q["assets_by_india_net"],q["liabilities_in_india_net"])},key=lambda x:(len(x),x))
 absent_values=[x for x in expected_values if x not in page]
 if absent_values: raise SystemExit(f"RBI page does not contain expected numeric values: {absent_values}")
 with open(IMF_PANEL,newline="",encoding="utf-8") as f: panel=list(csv.DictReader(f))
 imf={(x["COUNTRY"],x["BOP_ACCOUNTING_ENTRY"],x["TIME_PERIOD"]):x for x in panel
      if x["COUNTRY"]=="IND" and x["INDICATOR"]=="P_F" and x["UNIT"]=="USD" and x["FREQUENCY"]=="Q"}
 rows=[]
 for q,rb in RBI.items():
  for entry in ("A_NFA_T","L_NIL_T"):
   x=imf.get(("IND",entry,q))
   if not x:
    rows.append({"quarter":q,"rbi_quarter_label":rb["quarter_label"],"entry":entry,"status":"BLOCKED_MISSING_IMF"})
    continue
   raw=Decimal(x["OBS_VALUE"]); scale=x.get("SCALE",""); imf_million=raw/Decimal("1000000")
   rbi_net=Decimal(rb["assets_by_india_net"] if entry=="A_NFA_T" else rb["liabilities_in_india_net"])
   rbi_comparable=(-rbi_net if entry=="A_NFA_T" else rbi_net)
   residual=imf_million-rbi_comparable
   passed=scale=="6" and abs(residual)<=TOL
   rows.append({"quarter":q,"rbi_quarter_label":rb["quarter_label"],"entry":entry,
    "rbi_row":"3.2.B Portfolio Investment by India" if entry=="A_NFA_T" else "3.2.A Portfolio Investment in India",
    "rbi_credit_minus_debit_net_usd_million":str(rbi_net),
    "rbi_comparable_to_imf_usd_million":str(rbi_comparable),
    "imf_obs_value_raw":str(raw),"imf_scale":scale,
    "imf_obs_value_div_1e6_usd_million":str(imf_million),
    "residual_imf_minus_rbi_usd_million":str(residual),
    "tolerance_usd_million":str(TOL),"status":"PASS" if passed else "REVIEW"})
 (OUT/"quarter_reconciliation.json").write_text(json.dumps(rows,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 with (OUT/"quarter_reconciliation.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 summary={"scope":"India IMF BOP P_F assets/liabilities scale and sign cross-check against RBI Table 197",
  "source":source,"imf_panel_file":IMF_PANEL,"rbi_table197_publication_date":"2026-07-31",
  "quarter_count":len(RBI),"comparison_count":len(rows),"pass_count":sum(x.get("status")=="PASS" for x in rows),
  "review_count":sum(x.get("status")=="REVIEW" for x in rows),
  "blocked_count":sum(x.get("status","").startswith("BLOCKED") for x in rows),
  "rbi_rounding_tolerance_usd_million":"0.5 (integer USD million publication)",
  "mapping":{"A_NFA_T":"negative of RBI 3.2.B Portfolio Investment by India (credit-debit net)",
   "L_NIL_T":"RBI 3.2.A Portfolio Investment in India (credit-debit net)"},
  "all_pass":len(rows)==12 and all(x.get("status")=="PASS" for x in rows),
  "limitations":"Six published quarters only; source page values are integer USD millions. This validates India scale/sign for these six quarters, not all 154 EMDE members or every vintage."}
 (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,ensure_ascii=False));print(json.dumps(rows,indent=2,ensure_ascii=False))
 if not summary["all_pass"]: raise SystemExit("India scale/sign reconciliation did not fully PASS")
if __name__=="__main__": main()
