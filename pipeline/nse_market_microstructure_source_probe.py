#!/usr/bin/env python3
"""Bounded official NSE price-band and surveillance-report URL/schema probe."""
from pathlib import Path
from datetime import datetime, timezone
from io import BytesIO
import csv, hashlib, json, time
import requests
import pandas as pd

DAY="02112026"
SHORT="021126"
ROOT=Path("artifacts/nse_market_microstructure_probe")
HEADERS={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
         "Accept":"text/csv,application/octet-stream,*/*","Referer":"https://www.nseindia.com/all-reports",
         "Accept-Language":"en-US,en;q=0.9"}
REPORTS={
 "price_band":[f"sec_list_{DAY}.csv"],
 "surveillance_old":[f"REG_IND{SHORT}.csv"],
 "surveillance_new":[f"REG1_IND{SHORT}.csv"],
 "circuit":[f"circuit_{DAY}.csv"]
}
HOSTS=["https://nsearchives.nseindia.com/content/equities/","https://archives.nseindia.com/content/equities/"]

def norm(x): return "".join(c for c in str(x).upper() if c.isalnum())

def inspect_csv(raw, expected):
    frame=pd.read_csv(BytesIO(raw),dtype=str,nrows=1000).fillna("")
    cols={norm(c):str(c) for c in frame.columns}
    symbol=next((cols[k] for k in ("SYMBOL","TCKRSYMB","SECURITY","SCRIP") if k in cols),None)
    series=next((cols[k] for k in ("SERIES","SCTYSRS") if k in cols),None)
    datecol=next((cols[k] for k in ("DATE","DATE1","TRADDT","EFFECTIVEDATE") if k in cols),None)
    if not symbol:
        raise ValueError(f"symbol column missing; columns={list(frame.columns)}")
    if expected=="price_band":
        band=next((cols[k] for k in ("PRICEBAND","PRICEBANDPERCENT","BAND","BANDPERCENT","PRICEBANDINDICATOR") if k in cols),None)
        lower=next((cols[k] for k in ("LOWERPRICEBAND","LOWERBAND","LOWERLIMIT","LOWERPRICE") if k in cols),None)
        upper=next((cols[k] for k in ("UPPERPRICEBAND","UPPERBAND","UPPERLIMIT","UPPERPRICE") if k in cols),None)
        if not any((band,lower,upper)):
            raise ValueError(f"price-band fields missing; columns={list(frame.columns)}")
    elif expected.startswith("surveillance"):
        if not any(k in cols for k in ("SURVEILLANCEINDICATOR","INDICATOR","STAGE","MEASURE","ACTION","CATEGORY")):
            raise ValueError(f"surveillance indicator/stage fields missing; columns={list(frame.columns)}")
    return {"columns":list(frame.columns),"sample_rows":len(frame),"symbol_column":symbol,
            "series_column":series,"date_column":datecol,"schema_status":"PASS"}

def main():
    ROOT.mkdir(parents=True,exist_ok=True)
    s=requests.Session();s.headers.update(HEADERS)
    results=[]
    for category,names in REPORTS.items():
        for name in names:
            found=False
            for base in HOSTS:
                url=base+name
                item={"category":category,"filename":name,"url":url}
                try:
                    r=s.get(url,timeout=(5,20))
                    item.update({"http_status":r.status_code,"content_type":r.headers.get("Content-Type",""),
                                 "bytes":len(r.content),"retrieved_at_utc":datetime.now(timezone.utc).isoformat()})
                    if r.status_code==200 and len(r.content)>20 and not r.content.lstrip().startswith(b"<"):
                        item["sha256"]=hashlib.sha256(r.content).hexdigest()
                        try:
                            item.update(inspect_csv(r.content,category))
                            (ROOT/name).write_bytes(r.content)
                            item["saved_path"]=str(ROOT/name)
                            item["result"]="PASS"
                            found=True
                            break
                        except Exception as e:
                            item["result"]="SCHEMA_FAIL";item["schema_error"]=f"{type(e).__name__}: {e}"
                    else:
                        item["result"]="HTTP_OR_CONTENT_FAIL"
                except Exception as e:
                    item.update({"result":"REQUEST_ERROR","error":f"{type(e).__name__}: {e}"})
                results.append(item)
                time.sleep(0.25)
            if found: results.append(item)
    bycat={}
    for x in results:
        if x.get("result")=="PASS": bycat[x["category"]]=x
    required=["price_band","surveillance_old","surveillance_new"]
    passed=[k for k in required if k in bycat]
    status="PASS" if len(passed)==len(required) else ("PARTIAL" if passed else "BLOCKED")
    report={"status":status,"requested_trade_date":"2026-11-02","requested_file_date":"02-Nov-2026",
      "required_categories":required,"passed_categories":passed,"missing_categories":[x for x in required if x not in bycat],
      "results":results,"observed_at_utc":datetime.now(timezone.utc).isoformat(),
      "policy":"Probe only. No status promotion until historical date coverage, symbol/date join, effective-date QA, source provenance and domain rules pass."}
    (ROOT/"probe_report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps({"status":status,"passed_categories":passed,"missing_categories":report["missing_categories"],
                      "results":results},indent=2))
    if status=="BLOCKED": raise SystemExit("No official report category could be validated")
if __name__=="__main__":main()
