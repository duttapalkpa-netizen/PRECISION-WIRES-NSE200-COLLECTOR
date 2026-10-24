#!/usr/bin/env python3
"""Audit-only repair for four missing Macro-Geo P0 groups.

Crude and USD/INR use explicitly labelled FRED series. Corporate events are
normalized from raw NSE corporate filing rows with URL/timestamp provenance.
FPI/DII is accepted only from a successful official NSE response with mapped
date/group/net-value columns; otherwise it stays BLOCKED. No synthetic rows.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from io import StringIO
import json, re
import pandas as pd
import requests

RAW=Path("data/external"); RAW.mkdir(parents=True,exist_ok=True)
REPORT=Path("outputs/macro_geo/p0_repair_report.json"); REPORT.parent.mkdir(parents=True,exist_ok=True)
EQUITY_PANEL=Path("data/processed/nse_eq_200_sessions.csv")
BENCHMARK_PANEL=Path("data/external/benchmark_indices.csv")
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36"
def p0_window():
 """Bound macro retrieval to a real observed research-panel date range.

 Prefer the canonical NSE equity panel. In clean audit runners where that
 dataset is not present, use observed dates from the NSE benchmark archive,
 never wall-clock dates or fabricated market sessions. Historical regime
 studies remain separate from this bounded P0 retrieval.
 """
 source=EQUITY_PANEL if EQUITY_PANEL.exists() else BENCHMARK_PANEL
 if not source.exists():
  raise RuntimeError("Cannot bound P0 series: neither NSE equity panel nor benchmark index archive exists")
 panel=pd.read_csv(source,usecols=lambda c: str(c).strip().upper()=="DATE")
 if panel.empty or "DATE" not in panel.columns:
  raise RuntimeError("Cannot bound P0 series: selected panel has no DATE rows")
 dates=pd.to_datetime(panel["DATE"],errors="coerce").dropna()
 if dates.empty: raise RuntimeError("Cannot bound P0 series: selected panel DATE values are invalid")
 # Use up to 200 distinct observed sessions, with a 30-calendar-day macro
 # lookback and 3-day freshness pad. The fallback is explicitly benchmark-
 # bounded and does not claim to be the NSE-200 stock universe.
 sessions=sorted(dates.dt.date.unique())
 recent=sessions[-200:]
 return (max(pd.Timestamp("1990-01-01").date(), recent[0]-timedelta(days=30)),
         min(datetime.now(timezone.utc).date(), recent[-1]+timedelta(days=3)))

def fallback_public_series(series_id,label,outfile,start,end):
 """Use explicitly labelled, auditable public mirrors only when FRED times out."""
 rows=[]
 if series_id=="DCOILBRENTEU":
  url="https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls"
  response=requests.get(url,headers={"User-Agent":UA},timeout=(8,35)); response.raise_for_status()
  book=pd.ExcelFile(StringIO("")) if False else None
  from io import BytesIO
  xls=pd.ExcelFile(BytesIO(response.content),engine="xlrd")
  found=None
  for sheet in xls.sheet_names:
   raw=pd.read_excel(xls,sheet_name=sheet,header=None)
   for i in range(min(12,len(raw))):
    vals=[str(v).strip().lower() for v in raw.iloc[i].tolist()]
    if any(v=="date" for v in vals) and any("brent spot price" in v for v in vals):
     found=(raw,i); break
   if found: break
  if not found: raise RuntimeError("EIA RBRTE workbook schema not recognized")
  raw,i=found; headers=[str(v).strip() for v in raw.iloc[i].tolist()]
  df=raw.iloc[i+1:].copy(); df.columns=headers
  datecol=next((x for x in df.columns if str(x).strip().lower()=="date"),None)
  valcol=next((x for x in df.columns if "brent spot price" in str(x).lower()),None)
  if not datecol or not valcol: raise RuntimeError("EIA RBRTE columns missing")
  for _,r in df.iterrows():
   dt=pd.to_datetime(r[datecol],errors="coerce"); val=pd.to_numeric(pd.Series([r[valcol]]),errors="coerce").iloc[0]
   if pd.notna(dt) and pd.notna(val) and start<=dt.date()<=end:
    rows.append({"DATE":dt.date().isoformat(),"CLOSE":float(val),"SERIES":label,"SOURCE":"US EIA RBRTE daily Brent spot (official XLS)","SOURCE_SERIES":"RBRTE","SOURCE_URL":url,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
 elif series_id=="DEXINUS":
  url="https://raw.githubusercontent.com/the-solipsist/rbi-forex-reference-rates/main/rbi_forex_reference_rates_long.csv"
  response=requests.get(url,headers={"User-Agent":UA},timeout=(8,35)); response.raise_for_status()
  df=pd.read_csv(StringIO(response.content.decode("utf-8-sig",errors="replace")))
  df.columns=[str(x).strip().lower() for x in df.columns]
  if not {"date","currency","rate"}.issubset(df.columns): raise RuntimeError("RBI/FBIL mirror schema mismatch")
  df=df[df["currency"].astype(str).str.upper().eq("USD")].copy()
  for _,r in df.iterrows():
   dt=pd.to_datetime(r["date"],errors="coerce"); val=pd.to_numeric(pd.Series([r["rate"]]),errors="coerce").iloc[0]
   if pd.notna(dt) and pd.notna(val) and start<=dt.date()<=end:
    rows.append({"DATE":dt.date().isoformat(),"CLOSE":float(val),"SERIES":label,"SOURCE":"Community mirror of RBI/FBIL reference rates (secondary; not direct RBI feed)","SOURCE_SERIES":"USD_INR_REFERENCE","SOURCE_URL":url,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
 if not rows: raise RuntimeError(f"No valid fallback rows for {series_id}")
 out=pd.DataFrame(rows).drop_duplicates(["DATE","SERIES"]).sort_values(["DATE","SERIES"])
 out.to_csv(RAW/outfile,index=False)
 return {"status":"AVAILABLE_SECONDARY","rows":len(out),"date_min":str(out.DATE.min()),"date_max":str(out.DATE.max()),"source":str(out.SOURCE.iloc[0]),"url":str(out.SOURCE_URL.iloc[0]),"path":str(RAW/outfile)}

def fred(series_id,label,outfile):
 url="https://fred.stlouisfed.org/graph/fredgraph.csv"
 rows=[]; urls=[]; cursor, end_date=p0_window()
 sess=requests.Session(); sess.headers.update({"User-Agent":UA,"Accept":"text/csv,*/*","Referer":"https://fred.stlouisfed.org/"})
 while cursor<=end_date:
  chunk_end=min(end_date,cursor+timedelta(days=29))
  response=None; last_error=None
  for timeout in (12,20):
   try:
    response=sess.get(url,params={"id":series_id,"cosd":cursor.isoformat(),"coed":chunk_end.isoformat()},
      headers={"User-Agent":UA,"Accept":"text/csv,*/*","Referer":"https://fred.stlouisfed.org/"},timeout=(8,timeout))
    response.raise_for_status(); break
   except Exception as exc:
    last_error=exc; response=None
  if response is None: raise RuntimeError(f"FRED {series_id} failed {cursor}..{chunk_end}: {type(last_error).__name__}: {last_error}")
  df=pd.read_csv(StringIO(response.content.decode("utf-8-sig",errors="replace")))
  df.columns=[str(c).strip().upper() for c in df.columns]
  datecol=next((c for c in df if c in ("DATE","OBSERVATION_DATE")),None)
  valcol=next((c for c in df if c==series_id.upper()),None)
  if not datecol or not valcol: raise RuntimeError("FRED schema mismatch: "+str(list(df.columns)))
  urls.append(response.url)
  for _,row in df.iterrows():
   dt=pd.to_datetime(row[datecol],errors="coerce")
   value=pd.to_numeric(pd.Series([row[valcol]]),errors="coerce").iloc[0]
   if pd.isna(dt) or pd.isna(value) or not cursor<=dt.date()<=chunk_end: continue
   rows.append({"DATE":dt.date().isoformat(),"CLOSE":float(value),"SERIES":label,"SOURCE":"FRED",
    "SOURCE_SERIES":series_id,"SOURCE_URL":response.url,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
  cursor=chunk_end+pd.Timedelta(days=1).to_pytimedelta()
 out=pd.DataFrame(rows)
 if not out.empty: out=out.drop_duplicates(["DATE","SERIES"]).sort_values(["DATE","SERIES"])
 if out.empty: raise RuntimeError("FRED returned zero valid rows")
 out.to_csv(RAW/outfile,index=False)
 return {"status":"AVAILABLE_SECONDARY","rows":len(out),"date_min":str(out.DATE.min()),"date_max":str(out.DATE.max()),
  "source":"FRED "+series_id,"url":";".join(urls),"path":str(RAW/outfile)}

def main():
 report={"observed_at_utc":datetime.now(timezone.utc).isoformat(),"groups":{},"p0_window":None,"policy":"Secondary series remain explicitly labelled; no missing values are fabricated. P0 series are bounded to the NSE 200-session panel; longer regime studies are separate."}
 try: report["p0_window"]={"start":p0_window()[0].isoformat(),"end":p0_window()[1].isoformat(),"basis":"NSE 200-session panel +/- 30-day lookback and 3-day freshness pad"}
 except Exception as e: report["p0_window"]={"status":"BLOCKED","error":type(e).__name__+": "+str(e)[:250]}
 for name,series,label,file in [("crude_oil","DCOILBRENTEU","BRENT_CRUDE_USD_PER_BBL","brent_crude.csv"),("usd_inr","DEXINUS","USD_INR_INR_PER_USD","usd_inr.csv")]:
  try:
   report["groups"][name]=fred(series,label,file)
  except Exception as e:
   primary_error=type(e).__name__+": "+str(e)[:220]
   try:
    start,end=p0_window()
    fallback=fallback_public_series(series,label,file,start,end)
    fallback["primary_error"]=primary_error
    report["groups"][name]=fallback
   except Exception as fallback_error:
    report["groups"][name]={"status":"BLOCKED","rows":0,"primary_error":primary_error,"fallback_error":type(fallback_error).__name__+": "+str(fallback_error)[:220]}
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
    stamp_parsed=pd.to_datetime(stamp,errors="coerce",dayfirst=True,utc=True)
    if pd.isna(stamp_parsed): continue
    stamp=stamp_parsed.isoformat()
    event_date=stamp_parsed.date().isoformat()
    link=pick("attchmntFile","attachment","attachmentUrl","detailsUrl","xbrl","pdfUrl")
    if symbol and desc and stamp and link:
     if str(link).startswith("/"): link="https://www.nseindia.com"+str(link)
     normalized.append({"DATE":event_date,"SYMBOL":str(symbol).upper(),"EVENT_TYPE":str(desc),"PUBLISHED_AT":stamp,
      "SOURCE_URL":str(link),"SOURCE":"NSE corporate announcements"})
   ev=pd.DataFrame(normalized)
   if not ev.empty:
    ev.to_csv(RAW/"corporate_events.csv",index=False)
    report["groups"]["corporate_events"]={"status":"AVAILABLE","rows":len(ev),"path":str(RAW/"corporate_events.csv"),"source":"NSE corporate announcements","note":"Publication timestamps normalized to ISO-8601 UTC; source URL retained. Event semantics still require downstream classification."}
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
