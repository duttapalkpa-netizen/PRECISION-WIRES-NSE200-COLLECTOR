#!/usr/bin/env python3
"""Capture official BCB SGS portfolio-asset net/inflow/outflow series and test identity."""
import csv, hashlib, json, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

OUT=Path("artifacts/bcb_asset_gross_flow"); OUT.mkdir(parents=True, exist_ok=True)
SERIES={"net":22906,"inflows":22907,"outflows":22908}
START="01/01/1995"
END=datetime.now(timezone.utc).strftime("%d/%m/%Y")
def sha(b): return hashlib.sha256(b).hexdigest()
manifest={"source":"Banco Central do Brasil Open Data Portal / BCData SGS","retrieval_started_utc":datetime.now(timezone.utc).isoformat(),"series":{},"period_start_requested":START,"period_end_requested":END}
rows={}
for name,code in SERIES.items():
    url=f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json&dataInicial={START}&dataFinal={END}"
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-Brazil-asset-flow-audit/1.0","Accept":"application/json"})
    try:
        with urlopen(req,timeout=45) as r:
            status=r.status; final=r.geturl(); headers=dict(r.headers.items()); raw=r.read(30*1024*1024+1)
    except HTTPError as e:
        status=e.code; final=e.geturl(); headers=dict(e.headers.items()) if e.headers else {}; raw=e.read()
    except (URLError,TimeoutError) as e:
        status=0; final=url; headers={}; raw=str(e).encode()
    (OUT/f"{name}.json").write_bytes(raw)
    info={"code":code,"requested_url":url,"final_url":final,"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"http_status":status,"content_type":headers.get("Content-Type"),"byte_count":len(raw),"sha256":sha(raw)}
    try:
        data=json.loads(raw)
        if not isinstance(data,list): raise ValueError("JSON root is not an array")
        vals={}
        for item in data:
            d=datetime.strptime(item["data"],"%d/%m/%Y").strftime("%Y-%m")
            v=float(item["valor"].replace(".","").replace(",","."))
            if d in vals: raise ValueError(f"duplicate month {d}")
            vals[d]=v
        rows[name]=vals
        info.update({"parse_status":"PASS","row_count":len(vals),"first_period":min(vals) if vals else None,"last_period":max(vals) if vals else None,"duplicate_months":0})
    except Exception as e:
        info.update({"parse_status":"FAIL","parse_error":str(e)})
    manifest["series"][name]=info
    time.sleep(0.25)
checks={"status":"BLOCKED","common_months":0,"missing_by_series":{},"pass":0,"fail":0,"max_abs_residual":None,"tolerance_usd_million":0.15}
if all(manifest["series"].get(k,{}).get("http_status")==200 and manifest["series"].get(k,{}).get("parse_status")=="PASS" for k in SERIES):
    common=sorted(set(rows["net"]) & set(rows["inflows"]) & set(rows["outflows"]))
    union=set(rows["net"])|set(rows["inflows"])|set(rows["outflows"])
    checks["common_months"]=len(common)
    checks["missing_by_series"]={k:len(union-set(rows[k])) for k in SERIES}
    residuals=[(m,rows["net"][m]-(rows["inflows"][m]-rows["outflows"][m])) for m in common]
    checks["pass"]=sum(abs(x)<=checks["tolerance_usd_million"] for _,x in residuals)
    checks["fail"]=len(residuals)-checks["pass"]
    checks["max_abs_residual"]=max((abs(x) for _,x in residuals),default=None)
    checks["status"]="PASS" if common and checks["fail"]==0 and all(v==0 for v in checks["missing_by_series"].values()) else "PARTIAL_OR_FAIL"
    with (OUT/"identity_reconciliation.csv").open("w",newline="") as f:
        w=csv.writer(f); w.writerow(["period","net_22906_usd_million","inflows_22907_usd_million","outflows_22908_usd_million","calculated_net","residual","status"])
        for m,x in residuals:
            calc=rows["inflows"][m]-rows["outflows"][m]
            w.writerow([m,rows["net"][m],rows["inflows"][m],rows["outflows"][m],calc,x,"PASS" if abs(x)<=checks["tolerance_usd_million"] else "FAIL"])
manifest["identity_check"]=checks
manifest["retrieval_finished_utc"]=datetime.now(timezone.utc).isoformat()
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps(manifest,indent=2))
if checks["status"]!="PASS": raise SystemExit("Asset gross-flow identity did not meet full coverage/tolerance gate")
