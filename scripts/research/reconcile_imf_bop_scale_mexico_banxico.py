#!/usr/bin/env python3
"""Mexico Banxico CE174 BPM6 quarterly portfolio flow benchmark against IMF BOP panel."""
from datetime import datetime,timezone
from decimal import Decimal
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import hashlib,json,csv,re
URL="https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CE174&locale=en&sector=1"
PANEL=Path("docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv")
OUT=Path("banxico_mexico_scale_reconciliation");RAW=OUT/"raw";RAW.mkdir(parents=True,exist_ok=True)
PERIODS={"2025-Q4":"Oct-Dec 2025","2026-Q1":"Jan-Mar 2026","2026-Q2":"Apr-Jun 2026"}
LABELS={"A_NFA_T":"A. Net acquisition of financial assets","L_NIL_T":"B. Net incurrence of liabilities"}
def clean(s):return " ".join(str(s).replace("\xa0"," ").split())
def tokens(s):return re.findall(r"(?<![A-Za-z])[-−]?\d[\d,]*(?:\.\d+)?",s)
def num(s):return Decimal(s.replace(",","").replace("−","-"))
def main():
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(URL,headers={"User-Agent":"Mozilla/5.0 PRECISION-WIRES independent audit","Accept":"text/html,application/xhtml+xml,*/*"})
 try:
  with urlopen(req,timeout=60) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=URL;headers={};body=str(e).encode()
 (RAW/"banxico_ce174.html").write_bytes(body)
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 receipt={"url":URL,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"raw_file":"raw/banxico_ce174.html"}
 if status!=200:raise SystemExit(f"Banxico HTTP {status}")
 soup=BeautifulSoup(body,"html.parser"); page=clean(soup.get_text(" ",strip=True))
 if not all(v in page for v in PERIODS.values()):raise SystemExit("Expected Banxico quarter headers missing")
 rows=[]
 for i,tr in enumerate(soup.find_all("tr")):
  cells=[clean(x.get_text(" ",strip=True)) for x in tr.find_all(["th","td"],recursive=False)]
  txt=clean(" ".join(cells))
  if txt and len(cells)>=6:rows.append({"index":i,"cells":cells,"text":txt})
 parent=next((i for i,x in enumerate(rows) if "II. Portfolio investment (A - B)" in x["text"]),None)
 if parent is None:raise SystemExit("Portfolio investment parent row not found")
 extracted={};debug=[]
 for key,label in LABELS.items():
  hit=next((x for x in rows[parent+1:] if label in x["text"]),None)
  if hit is None:raise SystemExit(f"Portfolio child row not found: {label}")
  tsx=tokens(hit["cells"][-1]);debug.append({"key":key,"row_index":hit["index"],"cells":hit["cells"],"value_cell":hit["cells"][-1],"numeric_tokens":tsx})
  if len(tsx)<3:raise SystemExit(f"Not enough values in row: {hit['text']}")
  extracted[key]=[num(x) for x in tsx[-3:]]
 imf={}
 with PANEL.open(encoding="utf-8-sig",newline="") as f:
  for x in csv.DictReader(f):
   if x.get("COUNTRY")=="MEX" and x.get("INDICATOR")=="P_F" and x.get("UNIT")=="USD" and x.get("FREQUENCY")=="Q" and x.get("TIME_PERIOD") in PERIODS and x.get("BOP_ACCOUNTING_ENTRY") in LABELS:
    imf[(x["BOP_ACCOUNTING_ENTRY"],x["TIME_PERIOD"])]=x
 results=[]
 for entry in ("A_NFA_T","L_NIL_T"):
  for i,(q,label) in enumerate(PERIODS.items()):
   row=imf.get((entry,q))
   if row is None:raise SystemExit(f"Missing IMF row {entry} {q}")
   raw=Decimal(row["OBS_VALUE"]);scaled=raw/Decimal(1000000);reference=extracted[entry][i];diff=scaled-reference
   results.append({"country":"MEX","quarter":q,"entry":entry,"banxico_row":LABELS[entry],"imf_obs_value_raw_usd":str(raw),"imf_scale":row.get("SCALE"),"imf_unit":row.get("UNIT"),"imf_raw_div_1e6_usd_million":str(scaled),"banxico_usd_million":str(reference),"difference_imf_minus_banxico":str(diff),"tolerance_usd_million":"0.5","status":"PASS" if row.get("SCALE")=="6" and row.get("UNIT")=="USD" and abs(diff)<=Decimal("0.5") else "REVIEW"})
 with (OUT/"reconciliation.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
 summary={"scope":"Mexico Banxico CE174 BPM6 quarterly portfolio flows vs IMF BOP P_F","banxico_receipt":receipt,"banxico_table":"CE174","banxico_unit":"Millions of U.S. Dollar","banxico_frequency":"Quarterly","period_headers":list(PERIODS.values()),"portfolio_parent_row_index":rows[parent]["index"],"parsed_rows":debug,"imf_dataflow":"IMF.STA:BOP(21.0.0)","imf_dsd":"IMF.STA:DSD_BOP(24.0.0)","imf_country":"MEX","imf_indicator":"P_F","imf_unit":"USD","imf_scale":"6","comparison_count":len(results),"pass_count":sum(x["status"]=="PASS" for x in results),"review_count":sum(x["status"]!="PASS" for x in results),"max_abs_difference_usd_million":str(max(abs(Decimal(x["difference_imf_minus_banxico"])) for x in results)),"tolerance":"±0.5 USD million; Banxico table values are integer-million rounded","decision":"MEXICO_SCALE_AND_SIGN_EMPIRICAL_CHECK_PASS" if len(results)==6 and all(x["status"]=="PASS" for x in results) else "MEXICO_CHECK_NOT_CLOSED","scope_limit":"Three published quarters only; does not establish a universal transform or resolve all revision-vintage differences."}
 (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,ensure_ascii=False))
 if summary["decision"]!="MEXICO_SCALE_AND_SIGN_EMPIRICAL_CHECK_PASS":raise SystemExit("Mexico benchmark did not pass")
if __name__=="__main__":main()
