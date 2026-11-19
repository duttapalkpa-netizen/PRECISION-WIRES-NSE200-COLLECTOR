#!/usr/bin/env python3
"""Independent Nigeria CBN vs IMF BOP P_F assets/liabilities scale/sign check.

Source: CBN Q2 2026 BOP Highlights, Table 2, p.6.
Only the three published quarters are checked. Values transcribed from the
official PDF are retained in USD billions; IMF raw OBS_VALUE is never changed.
"""
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
import hashlib,json,csv,io,re,subprocess,sys

OUT=Path("nigeria_bop_crosscheck"); RAW=OUT/"raw"; RAW.mkdir(parents=True,exist_ok=True)
PDF_URL="https://www.cbn.gov.ng/Out/2026/STD/Q2%202026%20BOP%20Highlights_%20revised.pdf"
IMF_BASE="https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0"
PERIODS=["2025-Q2","2026-Q1","2026-Q2"]
# Table 2, page 6; USD billions. Q2-2025 provisional, Q1-2026 revised.
CBN={
 "A_NFA_T":{"2025-Q2":-0.66,"2026-Q1":0.26,"2026-Q2":0.70},
 "L_NIL_T":{"2025-Q2":5.28,"2026-Q1":6.03,"2026-Q2":7.09}
}
def sha(b): return hashlib.sha256(b).hexdigest()
def get(url,accept):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-Nigeria-BOP-independent-check/1.0","Accept":accept})
 try:
  with urlopen(req,timeout=90) as r: status=r.status; final=r.geturl(); headers=dict(r.headers.items()); body=r.read()
 except HTTPError as e: status=e.code; final=e.geturl(); headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
 except (URLError,TimeoutError) as e: status=0; final=url; headers={}; body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 return {"requested_url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":sha(body),"body":body}
# Capture CBN primary source.
pr=get(PDF_URL,"application/pdf")
(RAW/"CBN_Q2_2026_BOP_Highlights_revised.pdf").write_bytes(pr["body"])
if pr["http_status"]!=200 or not pr["body"].startswith(b"%PDF"): raise SystemExit("CBN PDF download/format failure")
# Install/use pypdf only for text-presence QA; no OCR or inferred values.
try:
 from pypdf import PdfReader
except ImportError:
 subprocess.check_call([sys.executable,"-m","pip","install","pypdf"])
 from pypdf import PdfReader
pdf=PdfReader(io.BytesIO(pr["body"]))
if len(pdf.pages)<6: raise SystemExit("CBN PDF has fewer than 6 pages")
page=pdf.pages[6].extract_text() or ""
(OUT/"cbn_table2_page6_extracted.txt").write_text(page,encoding="utf-8")
# Verify table label and every transcribed numeric token is present in the original page text.
normalized_page=re.sub(r"\s+"," ",page).replace("−","-").replace("–","-")
if not normalized_page.strip(): raise SystemExit("CBN Table 2 page text extraction is empty")
tokens=["(0.66)","0.26","0.70","5.28","6.03","7.09"]
missing=[t for t in tokens if t not in normalized_page]
if missing: raise SystemExit("CBN transcribed table values not verified in extracted PDF page: "+str(missing))
responses={}; rows=[]
for entry in ("A_NFA_T","L_NIL_T"):
 key=f"NGA.{entry}.P_F.*.Q"
 url=f"{IMF_BASE}/{key}?c%5BTIME_PERIOD%5D=ge%3A2025-Q2&c%5BTIME_PERIOD%5D=le%3A2026-Q2&format=csvdata"
 rr=get(url,"text/csv, */*")
 fn=f"IMF_NGA_{entry}_P_F_Q.csv"; (RAW/fn).write_bytes(rr["body"])
 meta={k:v for k,v in rr.items() if k!="body"}; meta["file"]=fn
 if rr["http_status"]!=200: raise SystemExit(f"IMF {entry} HTTP {rr['http_status']}: {rr['body'][:200]!r}")
 txt=rr["body"].decode("utf-8-sig")
 if txt.lstrip().startswith("<"): raise SystemExit("IMF returned non-CSV payload")
 parsed=list(csv.DictReader(io.StringIO(txt)))
 chosen={}
 for x in parsed:
  if x.get("COUNTRY")!="NGA" or x.get("BOP_ACCOUNTING_ENTRY")!=entry or x.get("INDICATOR")!="P_F" or x.get("FREQUENCY")!="Q": raise SystemExit("Unexpected IMF dimensions in response")
  if x.get("UNIT")!="USD": raise SystemExit("Unexpected IMF unit")
  p=x.get("TIME_PERIOD")
  if p in PERIODS and (x.get("OBS_VALUE") or "").strip(): 
   if p in chosen: raise SystemExit(f"Duplicate IMF period {entry} {p}")
   chosen[p]=x
 meta["parsed_rows"]=len(parsed); meta["selected_periods"]=sorted(chosen); responses[entry]=meta
 for p in PERIODS:
  if p not in chosen:
   rows.append({"country":"NGA","period":p,"entry":entry,"cbn_usd_bn":CBN[entry][p],"imf_obs_value_raw":None,"imf_scale":None,"imf_usd_million_derived":None,"cbn_usd_million":CBN[entry][p]*1000,"residual_usd_million":None,"tolerance_usd_million":5.0,"status":"MISSING_IMF"})
   continue
  x=chosen[p]; raw=float(x["OBS_VALUE"]); scale=x.get("SCALE")
  imf_m=raw/1_000_000
  cbn_m=CBN[entry][p]*1000
  residual=imf_m-cbn_m
  # CBN published to 0.01 USD billion = 10 USD million rounding quantum.
  status="PASS" if abs(residual)<=5.0 else "REVIEW"
  rows.append({"country":"NGA","period":p,"entry":entry,"cbn_usd_bn":CBN[entry][p],"imf_obs_value_raw":raw,"imf_scale":scale,"imf_usd_million_derived":imf_m,"cbn_usd_million":cbn_m,"residual_usd_million":residual,"tolerance_usd_million":5.0,"status":status})
with (OUT/"comparison.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
summary={"scope":"Nigeria national-source cross-check of IMF quarterly P_F assets/liabilities",
 "cbn_source_url":PDF_URL,"cbn_pdf":{"retrieved_at_utc":pr["retrieved_at_utc"],"http_status":pr["http_status"],"byte_count":pr["byte_count"],"sha256":pr["sha256"],"page_count":len(pdf.pages),"table_page_index_zero_based":6,"table_page_number":6},
 "cbn_publication":"Central Bank of Nigeria, BOP Highlights Q2 2026, Table 2, page 6; values USD billions; Q2 2025 provisional and Q1 2026 revised per footnotes",
 "imf_dataflow":"IMF.STA:BOP(21.0.0)","indicator":"P_F","periods":PERIODS,"unit":"USD","entries":["A_NFA_T","L_NIL_T"],
 "imf_requests":responses,"comparison_count":len(rows),"pass_count":sum(x["status"]=="PASS" for x in rows),"review_count":sum(x["status"]=="REVIEW" for x in rows),"missing_count":sum(x["status"]=="MISSING_IMF" for x in rows),
 "comparisons":rows,"conversion_test":"IMF OBS_VALUE / 1,000,000 compared with CBN USD billion * 1,000; tolerance ±5 USD million due CBN two-decimal USD-billion publication",
 "limitations":["Only three quarters; two CBN columns have explicit provisional/revised flags","CBN source does not provide transaction-level subcomponent detail in this table","No conclusion about all-country universalization","No aggregation, fill, production use or modification of raw IMF values"]}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
if summary["pass_count"]+summary["review_count"]+summary["missing_count"]!=6 or summary["missing_count"]:
 raise SystemExit("Incomplete Nigeria comparison")
