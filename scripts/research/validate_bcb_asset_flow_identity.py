#!/usr/bin/env python3
"""Empirically test BCB portfolio-asset gross inflow/outflow sign identity."""
from __future__ import annotations
import hashlib,json
from datetime import datetime,timezone
from decimal import Decimal
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError

OUT=Path("artifacts/bcb_asset_identity"); RAW=OUT/"raw"; RAW.mkdir(parents=True,exist_ok=True)
SERIES={
 "22906":{"role":"net_acquisition_financial_assets","metadata":"https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net"},
 "22907":{"role":"asset_inflows","metadata":"https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows"},
 "22908":{"role":"asset_outflows","metadata":"https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows"},
}
def sha(b):return hashlib.sha256(b).hexdigest()
def fetch(code):
 url=f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json"
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-Brazil-assets-identity/1.0","Accept":"application/json"})
 try:
  with urlopen(req,timeout=40) as r: status=r.status; final=r.geturl(); headers=dict(r.headers.items()); body=r.read()
 except HTTPError as e: status=e.code; final=e.geturl(); headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
 except (URLError,TimeoutError) as e: status=0; final=url; headers={}; body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 p=RAW/f"sgs_{code}.json";p.write_bytes(body)
 return {"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"file":f"raw/{p.name}","byte_count":len(body),"sha256":sha(body),"body":body}
def parse(body):
 rows=json.loads(body)
 if not isinstance(rows,list) or not rows:raise ValueError("empty_or_nonarray_json")
 out={}
 for i,x in enumerate(rows):
  d=datetime.strptime(x["data"],"%d/%m/%Y").strftime("%Y-%m")
  v=Decimal(str(x["valor"]).replace(",","."))
  if not v.is_finite() or d in out:raise ValueError(f"invalid_or_duplicate_row_{i}")
  out[d]=v
 if len(out)!=len(rows):raise ValueError("row_count_mismatch")
 return out,rows
manifest={"source":"Banco Central do Brasil SGS public API","candidate_identities":["22906 = 22908 - 22907","22906 = 22907 - 22908"],"retrieval_started_utc":datetime.now(timezone.utc).isoformat(),"series":{}}
data={}
for code,meta in SERIES.items():
 rec=fetch(code);body=rec.pop("body")
 item={**meta,**rec}
 if item["http_status"]!=200:item["status"]="FAIL";item["error"]=f"HTTP_{item['http_status']}"
 else:
  try:
   vals,rows=parse(body);data[code]=vals
   item.update({"status":"PASS","row_count":len(rows),"first_month":min(vals),"last_month":max(vals),"valid_rows":len(vals)})
  except Exception as e:item["status"]="FAIL";item["error"]=f"{type(e).__name__}: {e}"
 manifest["series"][code]=item
checks=[]
if len(data)==3:
 common=sorted(set(data["22906"])&set(data["22907"])&set(data["22908"]))
 for m in common:
  net,inf,out=(data[c][m] for c in ("22906","22907","22908"))
  # Both candidate conventions evaluated; do not assume which direction means acquisition.
  residual_a=net-(out-inf) # assets acquired abroad less disposal/repatriation
  residual_b=net-(inf-out)
  one_decimal=all(v.as_tuple().exponent==-1 for v in (net,inf,out))
  tol=Decimal("0.15")
  checks.append({"month":m,"net_22906_usd_million":str(net),"inflows_22907_usd_million":str(inf),"outflows_22908_usd_million":str(out),
   "candidate_outflows_minus_inflows":str(out-inf),"residual_net_minus_outflows_minus_inflows":str(residual_a),
   "candidate_inflows_minus_outflows":str(inf-out),"residual_net_minus_inflows_minus_outflows":str(residual_b),
   "all_values_one_decimal":one_decimal,"tolerance_usd_million":str(tol),
   "candidate_A_status":"PASS" if one_decimal and abs(residual_a)<=tol else "REVIEW",
   "candidate_B_status":"PASS" if one_decimal and abs(residual_b)<=tol else "REVIEW"})
else:common=[]
with (OUT/"monthly_identity.csv").open("w",encoding="utf-8") as f:
 fields=["month","net_22906_usd_million","inflows_22907_usd_million","outflows_22908_usd_million","candidate_outflows_minus_inflows","residual_net_minus_outflows_minus_inflows","candidate_inflows_minus_outflows","residual_net_minus_inflows_minus_outflows","all_values_one_decimal","tolerance_usd_million","candidate_A_status","candidate_B_status"]
 f.write(",".join(fields)+"\n")
 for x in checks:f.write(",".join(str(x[k]) for k in fields)+"\n")
def stat(k):
 rs=[Decimal(x[k]) for x in checks]
 passed=sum(abs(x)<=Decimal("0.15") and checks[i]["all_values_one_decimal"] for i,x in enumerate(rs))
 return {"pass_count":passed,"review_count":len(rs)-passed,"max_abs_residual_usd_million":str(max((abs(x) for x in rs),default=Decimal(0)))}
a=stat("residual_net_minus_outflows_minus_inflows");b=stat("residual_net_minus_inflows_minus_outflows")
if len(data)==3 and checks and a["pass_count"]==len(checks) and b["pass_count"]!=len(checks):decision="IDENTITY_PASS_NET_EQUALS_OUTFLOWS_MINUS_INFLOWS"
elif len(data)==3 and checks and b["pass_count"]==len(checks) and a["pass_count"]!=len(checks):decision="IDENTITY_PASS_NET_EQUALS_INFLOWS_MINUS_OUTFLOWS"
elif len(data)==3 and checks and a["pass_count"]==len(checks) and b["pass_count"]==len(checks):decision="AMBIGUOUS_BOTH_CANDIDATES_PASS"
else:decision="IDENTITY_NOT_CLOSED"
manifest.update({"common_month_count":len(common),"first_common_month":common[0] if common else None,"last_common_month":common[-1] if common else None,
 "candidate_A_outflows_minus_inflows":a,"candidate_B_inflows_minus_outflows":b,"decision":decision,
 "tolerance_rule":"0.15 USD million only where all three BCB source values are reported to one decimal",
 "retrieval_finished_utc":datetime.now(timezone.utc).isoformat()})
manifest["overall_status"]="PASS" if decision.startswith("IDENTITY_PASS_") else "REVIEW"
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"overall_status":manifest["overall_status"],"decision":decision,"series":{k:{q:v.get(q) for q in ("status","row_count","first_month","last_month","byte_count","sha256","error")} for k,v in manifest["series"].items()},"common_month_count":len(common),"candidate_A":a,"candidate_B":b},indent=2))
if manifest["overall_status"]!="PASS":raise SystemExit("BCB asset identity not uniquely established")
