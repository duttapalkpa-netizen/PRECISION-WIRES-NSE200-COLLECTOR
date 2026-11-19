#!/usr/bin/env python3
"""Chile Central Bank official monthly portfolio investment flows vs IMF quarterly P_F."""
from datetime import datetime,timezone
from decimal import Decimal
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import hashlib,json,csv,re
BASE="https://si3.bcentral.cl/siete/ES/Siete/Cuadro/CAP_BDP/MN_BDP42"
SERIES={
 "A_NFA_T":{"id":"F068.G2.FLU.Z.0.S.A.Z.T.Z.Z.6.0.M","path":"BP6M_CF_ACT"},
 "L_NIL_T":{"id":"F068.G2.FLU.Z.0.S.P.Z.T.Z.Z.6.0.M","path":"BP6M_CF_PAS"}
}
PANEL=Path("docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv")
OUT=Path("chile_bcentral_scale_reconciliation");RAW=OUT/"raw";RAW.mkdir(parents=True,exist_ok=True)
QUARTERS=["2025-Q4","2026-Q1","2026-Q2","2026-Q3"]
def sha(b):return hashlib.sha256(b).hexdigest()
def clean(s):return " ".join(str(s).replace("\xa0"," ").split())
def main():
 receipts=[]; monthly={}
 for entry,cfg in SERIES.items():
  url=f"{BASE}/{cfg['path']}?idSerie={cfg['id']}"
  ts=datetime.now(timezone.utc).isoformat()
  req=Request(url,headers={"User-Agent":"Mozilla/5.0 PRECISION-WIRES official data audit","Accept":"text/html,application/xhtml+xml,*/*"})
  try:
   with urlopen(req,timeout=60) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
  except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
  except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
  fn=entry+".html";(RAW/fn).write_bytes(body)
  safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
  rec={"entry":entry,"series_id":cfg["id"],"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":sha(body),"file":"raw/"+fn}
  receipts.append(rec)
  if status!=200:raise SystemExit(f"{entry} HTTP {status}")
  soup=BeautifulSoup(body,"html.parser")
  # Search all visible tables for the observation table containing FECHA/VALOR.
  parsed={}
  month_map={"Ene":"Jan","Feb":"Feb","Mar":"Mar","Abr":"Apr","May":"May","Jun":"Jun","Jul":"Jul","Ago":"Aug","Sep":"Sep","Oct":"Oct","Nov":"Nov","Dic":"Dec"}
  for tr in soup.find_all("tr"):
   cells=[clean(x.get_text(" ",strip=True)) for x in tr.find_all(["td","th"],recursive=False)]
   if len(cells)>=2:
    date,value=cells[0],cells[1]
    m=re.match(r"^([A-Za-zÁÉÍÓÚáéíóú]{3})[.]?\s*(20\d\d)$",date)
    if m and m.group(1) in month_map:
     key=month_map[m.group(1)]+" "+m.group(2)
     parsed[key]=Decimal(value.replace(".","").replace(",","."))
  if not parsed:
   # Preserve HTML and emit visible table diagnostics; fail closed.
   tables=[]
   for t in soup.find_all("table")[:8]:
    tables.append(clean(t.get_text(" | ",strip=True))[:2500])
   raise SystemExit(f"No FECHA/VALOR observations parsed for {entry}; tables={tables}")
  monthly[entry]=parsed
  rec["parsed_month_count"]=len(parsed);rec["first_month"]=next(iter(parsed));rec["last_month"]=list(parsed)[-1]
 # Sum monthly values into quarters, with exact month coverage checks.
 def month_key(q,month):
  y,qq=q.split("-Q");return [(f"Jan {y}",f"Feb {y}",f"Mar {y}"),(f"Apr {y}",f"May {y}",f"Jun {y}"),(f"Jul {y}",f"Aug {y}",f"Sep {y}"),(f"Oct {y}",f"Nov {y}",f"Dec {y}")][int(qq)-1][month]
 imf={}
 with PANEL.open(encoding="utf-8-sig",newline="") as f:
  for x in csv.DictReader(f):
   if x.get("COUNTRY")=="CHL" and x.get("INDICATOR")=="P_F" and x.get("UNIT")=="USD" and x.get("FREQUENCY")=="Q" and x.get("TIME_PERIOD") in QUARTERS and x.get("BOP_ACCOUNTING_ENTRY") in SERIES:
    imf[(x["BOP_ACCOUNTING_ENTRY"],x["TIME_PERIOD"])]=x
 results=[]
 for entry in SERIES:
  for q in QUARTERS:
   year,quarter=q.split("-Q");months=month_key(q,0),month_key(q,1),month_key(q,2)
   vals=[monthly[entry].get(m) for m in months]
   if any(v is None for v in vals):raise SystemExit(f"Missing monthly source months for {entry} {q}: {dict(zip(months,vals))}")
   ref=imf.get((entry,q))
   source_sum=sum(vals)
   if ref is None:
    results.append({"country":"CHL","quarter":q,"entry":entry,"bcentral_series_id":SERIES[entry]["id"],"bcentral_months":";".join(months),"bcentral_monthly_values_usd_million":";".join(str(x) for x in vals),"bcentral_quarter_sum_usd_million":str(source_sum),"imf_obs_value_raw_usd":"","imf_scale":"","imf_unit":"","imf_raw_div_1e6_usd_million":"","difference_imf_minus_bcentral":"","tolerance_usd_million":"1.5","status":"IMF_PANEL_MISSING"})
   else:
    raw=Decimal(ref["OBS_VALUE"]);scaled=raw/Decimal(1000000);diff=scaled-source_sum
    results.append({"country":"CHL","quarter":q,"entry":entry,"bcentral_series_id":SERIES[entry]["id"],"bcentral_months":";".join(months),"bcentral_monthly_values_usd_million":";".join(str(x) for x in vals),"bcentral_quarter_sum_usd_million":str(source_sum),"imf_obs_value_raw_usd":str(raw),"imf_scale":ref.get("SCALE"),"imf_unit":ref.get("UNIT"),"imf_raw_div_1e6_usd_million":str(scaled),"difference_imf_minus_bcentral":str(diff),"tolerance_usd_million":"1.5","status":"PASS" if ref.get("SCALE")=="6" and ref.get("UNIT")=="USD" and abs(diff)<=Decimal("1.5") else "REVIEW"})
 with (OUT/"reconciliation.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
 summary={"scope":"Chile Banco Central official monthly BOP portfolio investment assets/liabilities summed to quarter vs IMF BOP P_F","source_receipts":receipts,"source_units":"Millions of U.S. dollars","frequency":"Monthly; summed to quarter","series":SERIES,"quarters":QUARTERS,"comparison_count":len(results),"pass_count":sum(x["status"]=="PASS" for x in results),"review_count":sum(x["status"]=="REVIEW" for x in results),"missing_imf_count":sum(x["status"]=="IMF_PANEL_MISSING" for x in results),"max_abs_difference_usd_million":str(max(abs(Decimal(x["difference_imf_minus_bcentral"])) for x in results if x["difference_imf_minus_bcentral"])),"tolerance":"±1.5 USD million; three monthly observations each published to whole USD million","decision":"CHILE_PARTIAL_Q4_2025_PASS_Q1Q2_REVIEW_Q3_IMF_MISSING" if sum(x["status"]=="PASS" for x in results)==2 and sum(x["status"]=="REVIEW" for x in results)==4 and sum(x["status"]=="IMF_PANEL_MISSING" for x in results)==2 else "CHILE_RECONCILIATION_REQUIRES_REVIEW","scope_limit":"Four quarterly windows only; any revisions/vintage mismatch must be logged."}
 (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,ensure_ascii=False))
 if summary["decision"]=="CHILE_RECONCILIATION_REQUIRES_REVIEW":raise SystemExit("Chile reconciliation classification failed")
if __name__=="__main__":main()
