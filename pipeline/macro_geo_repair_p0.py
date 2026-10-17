#!/usr/bin/env python3
"""Audit-only repair for four missing Macro-Geo P0 groups.

Crude and USD/INR use explicitly labelled FRED series. Corporate events are
normalized from raw NSE corporate filing rows with URL/timestamp provenance.
FPI/DII is accepted only from a successful official NSE response with mapped
date/group/net-value columns; otherwise it stays BLOCKED. No synthetic rows.
"""
from pathlib import Path
from datetime import datetime, timezone
from io import StringIO
import json, re
import pandas as pd
import requests

RAW=Path("data/external"); RAW.mkdir(parents=True,exist_ok=True)
REPORT=Path("outputs/macro_geo/p0_repair_report.json"); REPORT.parent.mkdir(parents=True,exist_ok=True)
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36"
def fred(series_id,label,outfile):
 url="https://fred.stlouisfed.org/graph/fredgraph.csv"
 r=requests.get(url,params={"id":series_id,"cosd":"2006-01-01","coed":datetime.now(timezone.utc).date().isoformat()},
  headers={"User-Agent":UA,"Accept":"text/csv,*/*","Referer":"https://fred.stlouisfed.org/"},timeout=45)
 r.raise_for_status(); df=pd.read_csv(StringIO(r.content.decode("utf-8-sig",errors="replace")))
 if not {"observation_date",series_id}.issubset({str(c).lower() for c in df.columns}):
  # FRED may uppercase DATE or series identifier; normalize then check.
  df.columns=[str(c).strip().upper() for c in df.columns]
  datecol=next((c for c in df if c in ("DATE","OBSERVATION_DATE")),None)
  valcol=next((c for c in df if c==series_id.upper()),None)
 else:
  df.columns=[str(c).strip().upper() for c in df.columns]; datecol="OBSERVATION_DATE"; valcol=series_id.upper()
 if not datecol or not valcol: raise RuntimeError("FRED schema mismatch: "+str(list(df.columns)))
 out=pd.DataFrame({"DATE":pd.to_datetime(df[datecol],errors="coerce").dt.date.astype("string"),
  "CLOSE":pd.to_numeric(df[valcol],errors="coerce"),"SERIES":label,"SOURCE":"FRED",
  "SOURCE_SERIES":series_id,"SOURCE_URL":r.url,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
 out=out.dropna(subset=["DATE","CLOSE"]); out=out[out.CLOSE>0].drop_duplicates(["DATE","SERIES"])
 if out.empty: raise RuntimeError("FRED returned zero valid rows")
 out.to_csv(RAW/outfile,index=False)
 return {"status":"AVAILABLE_SECONDARY","rows":len(out),"date_min":str(out.DATE.min()),"date_max":str(out.DATE.max()),"source":"FRED "+series_id,"url":r.url,"path":str(RAW/outfile)}
def main():
 report={"observed_at_utc":datetime.now(timezone.utc).isoformat(),"groups":{},"policy":"Secondary series remain explicitly labelled; no missing values are fabricated."}
 for name,series,label,file in [("crude_oil","DCOILBRENTEU","BRENT_CRUDE_USD_PER_BBL","brent_crude.csv"),("usd_inr","DEXINUS","USD_INR_INR_PER_USD","usd_inr.csv")]:
  try: report["groups"][name]=fred(series,label,file)
  except Exception as e: report["groups"][name]={"status":"BLOCKED","rows":0,"error":type(e).__name__+": "+str(e)[:300]}
 # NSE announcement rows were fetched and preserved by the quarterly collector.
 source=Path("data/raw/quarterly_results_raw_responses/result_disclosure.json")
 if source.exists():
  try:
   payload=json.loads(source.read_text(encoding="utf-8")); rows=payload.get("payload",[])
   if isinstance(rows,dict):
    for k in ("data","rows","results"):
     if isinstance(rows.get(k),list): rows=rows[k]; break
   normalized=[]
   for row in rows if isinstance(rows,list) else []:
    def pick(*keys):
     return next((row.get(k) for k in keys if row.get(k) not in (None,"")), "")
    symbol=pick("symbol","sm_symbol","ticker"); desc=pick("subject","purpose","description","desc","attchmntText")
    stamp=pick("broadcastDateTime","broadcastDate","broadcast_date","an_dt","sort_date","date")
    link=pick("attchmntFile","attachment","attachmentUrl","detailsUrl","xbrl","pdfUrl")
    if symbol and desc and stamp and link:
     if str(link).startswith("/"): link="https://www.nseindia.com"+str(link)
     normalized.append({"DATE":stamp,"SYMBOL":str(symbol).upper(),"EVENT_TYPE":str(desc),"PUBLISHED_AT":stamp,
      "SOURCE_URL":str(link),"SOURCE":"NSE corporate announcements","ISIN":pick("sm_isin","isin")})
   ev=pd.DataFrame(normalized)
   if not ev.empty:
    ev.to_csv(RAW/"corporate_events.csv",index=False)
    report["groups"]["corporate_events"]={"status":"AVAILABLE","rows":len(ev),"path":str(RAW/"corporate_events.csv"),"source":"NSE corporate announcements","note":"Timestamp and URL retained; raw filing rows only."}
   else: report["groups"]["corporate_events"]={"status":"BLOCKED","rows":0,"reason":"No rows with symbol, description, publication timestamp and attachment URL"}
  except Exception as e: report["groups"]["corporate_events"]={"status":"BLOCKED","rows":0,"error":type(e).__name__+": "+str(e)[:250]}
 else: report["groups"]["corporate_events"]={"status":"BLOCKED","rows":0,"reason":"NSE raw disclosure response missing"}
 # Try official NSE FPI/DII API. Schema must map; failure is explicitly retained.
 endpoints=["/api/fiidiiTradeReact","/api/fiidiiTradeReact?"]
 sess=requests.Session(); sess.headers.update({"User-Agent":UA,"Accept":"application/json,*/*","Referer":"https://www.nseindia.com/market-data/fii-dii"})
 flow=None; flow_meta={}
 try:
  sess.get("https://www.nseindia.com/",timeout=15)
  errors=[]
  for endpoint in endpoints[:1]:
   try:
    resp=sess.get("https://www.nseindia.com"+endpoint,timeout=25); resp.raise_for_status(); payload=resp.json()
    rows=payload if isinstance(payload,list) else next((payload[k] for k in ("data","records","result") if isinstance(payload,dict) and isinstance(payload.get(k),list)),[])
    if rows:
     df=pd.DataFrame(rows); df.columns=[str(c).strip().upper().replace(" ","_") for c in df.columns]
     datecol=next((c for c in df if c in ("DATE","TRADE_DATE","TRADING_DATE","TIMESTAMP")),None)
     groupcol=next((c for c in df if c in ("CATEGORY","GROUP","INVESTOR_TYPE","INVESTOR","CLIENT_TYPE")),None)
     netcol=next((c for c in df if c in ("NETVALUE","NET_VALUE","NET","NETAMOUNT","NET_AMOUNT")),None)
     if datecol and groupcol and netcol:
      flow=pd.DataFrame({"DATE":df[datecol],"GROUP":df[groupcol],"NET_VALUE":pd.to_numeric(df[netcol],errors="coerce"),
       "SOURCE":"NSE FPI/DII activity","SOURCE_URL":resp.url,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
      flow=flow.dropna(subset=["DATE","GROUP","NET_VALUE"])
      if not flow.empty: break
     errors.append("response schema not mapped: "+str(list(df.columns)))
    else: errors.append("empty NSE response")
   except Exception as e: errors.append(type(e).__name__+": "+str(e)[:200])
  if flow is not None and not flow.empty:
   flow.to_csv(RAW/"fpi_dii_flows.csv",index=False)
   flow_meta={"status":"AVAILABLE","rows":len(flow),"path":str(RAW/"fpi_dii_flows.csv"),"source":"NSE official API","url":flow.SOURCE_URL.iloc[0]}
  else: flow_meta={"status":"BLOCKED","rows":0,"reason":"; ".join(errors)}
 except Exception as e: flow_meta={"status":"BLOCKED","rows":0,"error":type(e).__name__+": "+str(e)[:250]}
 report["groups"]["fpi_dii_flows"]=flow_meta
 report["status"]="ALL_FOUR_AVAILABLE" if all(v.get("status") in ("AVAILABLE","AVAILABLE_SECONDARY") and v.get("rows",0)>0 for v in report["groups"].values()) else "REPAIR_WITH_GAPS"
 REPORT.write_text(json.dumps(report,indent=2),encoding="utf-8")
 print(json.dumps(report,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
