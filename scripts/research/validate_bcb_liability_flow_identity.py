#!/usr/bin/env python3
"""Verify BCB portfolio-liability accounting identity from official SGS series."""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

OUT=Path("artifacts/bcb_liability_identity")
RAW=OUT/"raw"
RAW.mkdir(parents=True,exist_ok=True)
SERIES={
 "22924":{"role":"net_incurrence_liabilities","expected":"net","metadata":"https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net"},
 "22925":{"role":"liability_inflows","expected":"inflows","metadata":"https://opendata.bcb.gov.br/dataset/22925-portfolio-investment---net-incurrence-of-liabilities---monthly---inflows"},
 "22926":{"role":"liability_outflows","expected":"outflows","metadata":"https://opendata.bcb.gov.br/dataset/22926-portfolio-investment---net-incurrence-of-liabilities---monthly---outflows"},
}
def sha(b): return hashlib.sha256(b).hexdigest()
def fetch(code):
 url=f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json"
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-Brazil-liability-identity/1.0","Accept":"application/json"})
 try:
  with urlopen(req,timeout=40) as r:
   status=r.status; final=r.geturl(); headers=dict(r.headers.items()); body=r.read()
 except HTTPError as e:
  status=e.code; final=e.geturl(); headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
 except (URLError,TimeoutError) as e:
  status=0; final=url; headers={}; body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 path=RAW/f"sgs_{code}.json"; path.write_bytes(body)
 return {"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,
         "headers":safe,"file":f"raw/{path.name}","byte_count":len(body),"sha256":sha(body),"body":body}

manifest={"source":"Banco Central do Brasil SGS public API","identity":"SGS 22924 net liabilities = SGS 22925 inflows - SGS 22926 outflows","retrieval_started_utc":datetime.now(timezone.utc).isoformat(),"series":{}}
data={}
for code,meta in SERIES.items():
 receipt=fetch(code); body=receipt.pop("body")
 item={**meta,**receipt}
 if receipt["http_status"]!=200:
  item["status"]="FAIL"; item["error"]=f"HTTP_{receipt['http_status']}"
 else:
  try:
   rows=json.loads(body)
   if not isinstance(rows,list) or not rows: raise ValueError("empty_or_nonarray_json")
   values={}
   invalid=[]
   for i,row in enumerate(rows):
    try:
     dt=datetime.strptime(row["data"],"%d/%m/%Y").strftime("%Y-%m")
     value=Decimal(str(row["valor"]).replace(",","."))
     if not value.is_finite(): raise ValueError("nonfinite")
     if dt in values: raise ValueError("duplicate_month")
     values[dt]=value
    except Exception as e: invalid.append(f"row_{i}:{type(e).__name__}")
   months=sorted(values)
   if invalid or len(values)!=len(rows) or months!=[datetime.strptime(m,"%Y-%m").strftime("%Y-%m") for m in months]:
    raise ValueError("row_schema_or_duplicate_failure")
   item.update({"status":"PASS","row_count":len(rows),"valid_rows":len(values),"first_month":months[0],"last_month":months[-1],"invalid_rows":invalid[:10]})
   data[code]=values
  except Exception as e:
   item["status"]="FAIL"; item["error"]=f"{type(e).__name__}: {e}"
 manifest["series"][code]=item

checks=[]
if len(data)==3:
 common=sorted(set(data["22924"]) & set(data["22925"]) & set(data["22926"]))
 for month in common:
  net=data["22924"][month]; inflow=data["22925"][month]; outflow=data["22926"][month]
  residual=net-(inflow-outflow)
  one_decimal=all(v.as_tuple().exponent==-1 for v in (net,inflow,outflow))
  tol=Decimal("0.15")
  checks.append({"month":month,"net_22924_usd_million":str(net),"inflows_22925_usd_million":str(inflow),"outflows_22926_usd_million":str(outflow),"inflow_minus_outflow_usd_million":str(inflow-outflow),"residual_net_minus_decomposition":str(residual),"all_values_one_decimal":one_decimal,"tolerance_usd_million":str(tol),"status":"PASS" if one_decimal and abs(residual)<=tol else "REVIEW"})
else:
 common=[]
OUT.joinpath("monthly_identity.csv").write_text(
  "month,net_22924_usd_million,inflows_22925_usd_million,outflows_22926_usd_million,inflow_minus_outflow_usd_million,residual_net_minus_decomposition,all_values_one_decimal,tolerance_usd_million,status\n"+
  "".join(",".join(str(x[k]) for k in ("month","net_22924_usd_million","inflows_22925_usd_million","outflows_22926_usd_million","inflow_minus_outflow_usd_million","residual_net_minus_decomposition","all_values_one_decimal","tolerance_usd_million","status"))+"\n" for x in checks),encoding="utf-8")
manifest["common_month_count"]=len(common)
manifest["first_common_month"]=common[0] if common else None
manifest["last_common_month"]=common[-1] if common else None
manifest["identity_checks"]={"expected_formula":"22924 = 22925 - 22926","comparison_count":len(checks),"pass_count":sum(x["status"]=="PASS" for x in checks),"review_count":sum(x["status"]=="REVIEW" for x in checks),"max_abs_residual_usd_million":str(max((abs(Decimal(x["residual_net_minus_decomposition"])) for x in checks),default=Decimal(0))),"tolerance_rule":"0.15 USD million when each of the three source values is rounded to one decimal"}
manifest["overall_status"]="PASS" if len(data)==3 and checks and len(checks)==len(common) and all(x["status"]=="PASS" for x in checks) else "FAIL"
manifest["retrieval_finished_utc"]=datetime.now(timezone.utc).isoformat()
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"overall_status":manifest["overall_status"],"series":{k:{x:v.get(x) for x in ("status","row_count","first_month","last_month","byte_count","sha256","error")} for k,v in manifest["series"].items()},"identity_checks":manifest["identity_checks"]},indent=2))
if manifest["overall_status"]!="PASS": raise SystemExit("BCB liability identity gate did not PASS")
