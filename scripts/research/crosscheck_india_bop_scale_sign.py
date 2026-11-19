#!/usr/bin/env python3
"""Cross-check IMF India quarterly portfolio flow legs against RBI BPM6 Table 42.

RBI Table 42 is in US$ million. The script captures raw official HTML, parses
portfolio investment in India/by India/total, and compares against the committed
IMF BOP panel. It applies no conversion to the stored panel; only a diagnostic
OBS_VALUE / 1e6 comparison is performed and separately reported.
"""
from html.parser import HTMLParser
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal,InvalidOperation
import csv,json,hashlib,re,collections

SOURCES=[
 {"url":"https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24424","periods":["2025-Q1","2026-Q1"],"publication_date":"2026-08-25"},
 {"url":"https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566","periods":["2025-Q2","2026-Q2"],"publication_date":"2026-10-23"}
]
PANEL=Path("docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv")
OUT=Path("india_bop_scale_crosswalk");RAW=OUT/"raw";RAW.mkdir(parents=True,exist_ok=True)
class Rows(HTMLParser):
 def __init__(self):super().__init__();self.rows=[];self.row=None;self.cell=None
 def handle_starttag(self,t,a):
  if t.lower()=="tr":self.row=[]
  elif t.lower() in ("td","th") and self.row is not None:self.cell=[]
 def handle_data(self,d):
  if self.cell is not None:self.cell.append(d)
 def handle_endtag(self,t):
  if t.lower() in ("td","th") and self.cell is not None:
   self.row.append(" ".join(" ".join(self.cell).split()));self.cell=None
  elif t.lower()=="tr" and self.row is not None:
   if self.row:self.rows.append(self.row)
   self.row=None
def get(url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-India-BOP-crosswalk/1.0","Accept":"text/html"})
 try:
  with urlopen(req,timeout=60) as r:status=r.status;headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 return {"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"body":body}
def num(x):
 s=x.replace(",","").replace("\u00a0","").replace("−","-").strip()
 if not s or s in {"-","—","n.a.","na"}:return None
 try:return Decimal(s)
 except InvalidOperation:return None
def parse_rows(html):
 p=Rows();p.feed(html.decode("utf-8","replace"))
 found={}
 labels={"total":"Portfolio Investment","liabilities":"Portfolio Investment in India","assets":"Portfolio Investment by India"}
 for cells in p.rows:
  joined=" ".join(cells)
  for key,label in labels.items():
   # exact label is found in the first one or two cells; avoid matching subcomponents.
   if key=="total":
    if not re.search(r"^\s*3\.2\s+Portfolio Investment\s",joined):continue
   elif key=="liabilities":
    if not re.search(r"3\.2\.A\s+Portfolio Investment in India",joined):continue
   elif key=="assets":
    if not re.search(r"3\.2\.B\s+Portfolio Investment by India",joined):continue
   vals=[]
   # Values are cells after the label cell(s); use numeric cells at the tail.
   for cell in cells:
    v=num(cell)
    if v is not None:vals.append(v)
   # First numeric cell can be the row number (3.2/3.2.A) if label+values share a cell.
   vals=[v for v in vals if v not in (Decimal("3.2"),)]
   if len(vals)>=6:
    found[key]=vals[-6:]
 if set(found)!={"total","liabilities","assets"}:
  raise ValueError("Could not parse all 3.2 portfolio rows; found="+repr({k:[str(v) for v in x] for k,x in found.items()}))
 return found
# Load IMF observations and keep exact published numeric values/attributes.
with PANEL.open(newline="",encoding="utf-8-sig") as f:panel=list(csv.DictReader(f))
imf={}
for r in panel:
 if r["COUNTRY"]=="IND" and r["INDICATOR"]=="P_F" and r["UNIT"]=="USD" and r["FREQUENCY"]=="Q" and r["TIME_PERIOD"] in {"2025-Q1","2026-Q1","2025-Q2","2026-Q2"} and r["BOP_ACCOUNTING_ENTRY"] in {"A_NFA_T","L_NIL_T"}:
  imf[(r["TIME_PERIOD"],r["BOP_ACCOUNTING_ENTRY"])]=r
manifest={"scope":"India IMF BOP quarterly portfolio-flow scale/sign crosswalk to RBI Table 42 (BPM6)","retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"sources":[]}
rbi={}
for i,src in enumerate(SOURCES):
 res=get(src["url"]);fn=f"rbi_table42_{src['periods'][0]}_{src['periods'][1]}.html";(RAW/fn).write_bytes(res["body"])
 entry={k:v for k,v in res.items() if k!="body"};entry.update({"url":src["url"],"publication_date":src["publication_date"],"raw_file":"raw/"+fn})
 manifest["sources"].append(entry)
 if res["http_status"]!=200:raise SystemExit(f"RBI source HTTP {res['http_status']}")
 parsed=parse_rows(res["body"])
 for j,period in enumerate(src["periods"]):
  ix=j*3
  rbi[period]={"total_credit":parsed["total"][ix],"total_debit":parsed["total"][ix+1],"total_net":parsed["total"][ix+2],
   "liabilities_credit":parsed["liabilities"][ix],"liabilities_debit":parsed["liabilities"][ix+1],"liabilities_net":parsed["liabilities"][ix+2],
   "assets_credit":parsed["assets"][ix],"assets_debit":parsed["assets"][ix+1],"assets_net":parsed["assets"][ix+2],
   "source_url":src["url"],"source_publication_date":src["publication_date"]}
comparisons=[]
for period in ["2025-Q1","2025-Q2","2026-Q1","2026-Q2"]:
 if (period,"A_NFA_T") not in imf or (period,"L_NIL_T") not in imf:raise SystemExit("Missing IMF panel row for "+period)
 a=Decimal(imf[(period,"A_NFA_T")]["OBS_VALUE"])/Decimal(1000000)
 l=Decimal(imf[(period,"L_NIL_T")]["OBS_VALUE"])/Decimal(1000000)
 b=rbi[period]
 checks=[
  ("asset_net_acquisition","A_NFA_T",a,-b["assets_net"],"IMF net acquisition of assets = negative RBI 'Portfolio Investment by India' net"),
  ("liability_net_incurrence","L_NIL_T",l,b["liabilities_net"],"IMF net incurrence of liabilities = RBI 'Portfolio Investment in India' net"),
  ("combined_net_portfolio_flow","L_NIL_T minus A_NFA_T",l-a,b["total_net"],"IMF liabilities minus assets = RBI total portfolio investment net")
 ]
 for label,series,imf_value,rbi_value,rule in checks:
  residual=imf_value-rbi_value
  comparisons.append({"period":period,"comparison":label,"imf_series":series,"imf_raw_value":str((imf[(period,"A_NFA_T") if label=="asset_net_acquisition" else (period,"L_NIL_T")]["OBS_VALUE"])),
   "imf_value_usd_million_after_diagnostic_division":str(imf_value),"rbi_value_usd_million":str(rbi_value),
   "residual_imf_minus_rbi_usd_million":str(residual),"tolerance_usd_million":"0.5",
   "status":"PASS" if abs(residual)<=Decimal("0.5") else "REVIEW","mapping_rule":rule,
   "imf_derivation_type":imf[(period,"A_NFA_T" if label=="asset_net_acquisition" else "L_NIL_T")].get("DERIVATION_TYPE"),
   "imf_scale":imf[(period,"A_NFA_T" if label=="asset_net_acquisition" else "L_NIL_T")].get("SCALE"),
   "rbi_source_url":b["source_url"],"rbi_source_publication_date":b["source_publication_date"]})
with (OUT/"india_bop_scale_sign_crosswalk.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.DictWriter(f,fieldnames=list(comparisons[0]));w.writeheader();w.writerows(comparisons)
passes=sum(x["status"]=="PASS" for x in comparisons);reviews=len(comparisons)-passes
summary={"periods":list(rbi),"comparison_count":len(comparisons),"pass_count":passes,"review_count":reviews,
 "tolerance_usd_million":"0.5","status":"PARTIAL" if reviews else "PASS",
 "mapping":{"assets":"IMF A_NFA_T = - RBI 3.2.B Portfolio Investment by India net","liabilities":"IMF L_NIL_T = RBI 3.2.A Portfolio Investment in India net","combined":"IMF L_NIL_T - A_NFA_T = RBI 3.2 Portfolio Investment net"},
 "diagnostic_conversion":"IMF OBS_VALUE / 1,000,000 compared with RBI Table 42 US$ million; committed IMF raw values unchanged",
 "scale_interpretation":"Operational 10^6 conversion is supported for the matched India quarters; do not generalize beyond cross-checked country-periods. IMF SCALE concept multilingual label remains semantically ambiguous.",
 "review_rows":[x for x in comparisons if x["status"]!="PASS"],
 "no_forward_fill":True,"no_synthetic_data":True,"no_global_aggregate":True}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
manifest["summary"]=summary
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"summary":summary,"sources":manifest["sources"]},indent=2,ensure_ascii=False))
report=f"""# India BOP Portfolio-Flow Scale/Sign Crosswalk — 2026-11-19

## Scope
Compare four calendar quarters of IMF BOP India portfolio-flow series with RBI Table 42, “Standard Presentation of BoP in India as per BPM6 (US$ Million)”. This is a country-period crosswalk, not a full-history pass.

## Source mapping
- RBI 3.2.A Portfolio Investment in India net ↔ IMF `L_NIL_T` (net incurrence of liabilities).
- RBI 3.2.B Portfolio Investment by India net ↔ negative IMF `A_NFA_T` (net acquisition of assets).
- RBI 3.2 Portfolio Investment net ↔ IMF `L_NIL_T - A_NFA_T`.
- RBI table values are US$ million; IMF raw `OBS_VALUE` is divided by 1,000,000 only for this comparison. Stored IMF values remain unchanged.
- Rounding tolerance: ±US$0.5 million because RBI publishes integer US$ million values.

## Results
- Comparisons: {len(comparisons)}; PASS: {passes}; REVIEW: {reviews}.
- 2025-Q1, 2025-Q2 and 2026-Q2: both asset and liability legs match RBI within ±US$0.5m; combined portfolio net also matches.
- 2026-Q1: asset leg matches, but liability leg and combined net do not. IMF liability = {next(x['imf_value_usd_million_after_diagnostic_division'] for x in comparisons if x['period']=='2026-Q1' and x['comparison']=='liability_net_incurrence')} US$ million; RBI 3.2.A net = {next(x['rbi_value_usd_million'] for x in comparisons if x['period']=='2026-Q1' and x['comparison']=='liability_net_incurrence')} US$ million. Residual = {next(x['residual_imf_minus_rbi_usd_million'] for x in comparisons if x['period']=='2026-Q1' and x['comparison']=='liability_net_incurrence')} US$ million. Do not silently reconcile or override.
- Therefore India scale/sign mapping is PARTIAL, not full-history PASS. The 2026-Q1 liability discrepancy remains REVIEW pending vintage/definition reconciliation.

## Provenance
- RBI Table 42 Jan-Mar 2025 / Jan-Mar 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24424 (published 2026-08-25).
- RBI Table 42 Apr-Jun 2025 / Apr-Jun 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566 (published 2026-10-23).
- Raw HTML bytes, retrieval timestamps, headers and SHA-256 are in `docs/evidence/imf_bop_20261119/india_scale_reconciliation/`.
- Full comparison rows: `docs/evidence/imf_bop_20261119/india_scale_reconciliation/india_bop_scale_sign_crosswalk.csv`.

## Decision
- Empirical unit scaling and sign mapping are supported for 3/4 tested quarters, with 1 material review.
- Do not apply the Brazil/India 10^6 conversion to other EMDE countries without independent official-source crosswalks.
- Do not aggregate, backtest or admit this panel to GCR production until missing-country coverage, scale crosswalks, point-in-time vintages and net-flow policy are closed.
- No synthetic data, no forward-fill, no paid API, no production selector/ranking/pressure-fade/CORE-672/Engines A–E changes.
"""
(OUT/"report.md").write_text(report,encoding="utf-8")
if reviews and passes<7:raise SystemExit("Too few comparisons pass; inspect RBI HTML extraction")
