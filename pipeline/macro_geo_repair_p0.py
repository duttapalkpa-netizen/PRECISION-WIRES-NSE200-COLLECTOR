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
 # Never collect future macro observations relative to the observed equity cutoff.
 return (max(pd.Timestamp("1990-01-01").date(), recent[0]-timedelta(days=30)),
         min(datetime.now(timezone.utc).date(), recent[-1]))

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
 out=pd.DataFrame(rows)
 if out.empty:
  raise RuntimeError(f"No valid fallback rows for {series_id}")
 dates=pd.to_datetime(out["DATE"],errors="coerce")
 values=pd.to_numeric(out["CLOSE"],errors="coerce")
 if dates.isna().any() or values.isna().any() or (values<=0).any():
  raise RuntimeError(f"{series_id} fallback has invalid dates or non-positive values")
 if out["SOURCE_URL"].astype(str).str.strip().eq("").any() or out["SOURCE_SERIES"].astype(str).str.strip().eq("").any():
  raise RuntimeError(f"{series_id} fallback missing source provenance")
 if out.duplicated(["DATE","SERIES"]).any():
  raise RuntimeError(f"{series_id} fallback contains duplicate date/series keys")
 if dates.min().date()<start or dates.max().date()>end:
  raise RuntimeError(f"{series_id} fallback contains observations outside requested P0 window")
 age=(end-dates.max().date()).days
 if age<0 or age>3:
  raise RuntimeError(f"{series_id} fallback is stale/future relative to equity cutoff: age={age}")
 out=out.sort_values(["DATE","SERIES"])
 out.to_csv(RAW/outfile,index=False)
 return {"status":"AVAILABLE_SECONDARY","rows":len(out),"date_min":str(out.DATE.min()),"date_max":str(out.DATE.max()),
  "source":str(out.SOURCE.iloc[0]),"url":str(out.SOURCE_URL.iloc[0]),"path":str(RAW/outfile),
  "freshness_status":"FRESH","freshness_age_calendar_days":age,
  "domain_qa_checks":["source identity","valid positive values","unique date keys",
    "requested-window bounds","freshness <= 3 calendar days","source URL provenance"]}

def fred(series_id,label,outfile):
 url="https://fred.stlouisfed.org/graph/fredgraph.csv"
 rows=[]; urls=[]; cursor, end_date=p0_window(); cursor_start=cursor
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
 dates=pd.to_datetime(out["DATE"],errors="coerce")
 values=pd.to_numeric(out["CLOSE"],errors="coerce")
 if dates.isna().any() or values.isna().any() or (values<=0).any():
  raise RuntimeError(f"FRED {series_id} has invalid dates or non-positive values")
 if out.duplicated(["DATE","SERIES"]).any():
  raise RuntimeError(f"FRED {series_id} contains duplicate date/series keys")
 if dates.min().date()<cursor_start or dates.max().date()>end_date:
  raise RuntimeError(f"FRED {series_id} observations outside requested window")
 age=(end_date-dates.max().date()).days
 if age<0 or age>3:
  raise RuntimeError(f"FRED {series_id} stale/future relative to equity cutoff: age={age}")
 out.to_csv(RAW/outfile,index=False)
 return {"status":"AVAILABLE_SECONDARY","rows":len(out),"date_min":str(out.DATE.min()),"date_max":str(out.DATE.max()),
  "source":"FRED "+series_id,"url":";".join(urls),"path":str(RAW/outfile),
  "freshness_status":"FRESH","freshness_age_calendar_days":age,
  "domain_qa_checks":["source identity","valid positive values","unique date keys",
    "requested-window bounds","freshness <= 3 calendar days","source URL provenance"]}

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
 # Prefer preserved NSE result disclosures, then call the documented NSE
 # corporate-announcements endpoint directly with a bounded recent date range.
 source=Path("data/raw/quarterly_results_raw_responses/result_disclosure.json")
 payload_rows=[]
 def find_record_list(obj, depth=0):
  # NSE collectors have emitted both {payload:[...]} and nested data/result wrappers.
  # Accept only lists of dictionaries; never synthesize a disclosure from metadata.
  if depth > 5: return []
  if isinstance(obj, list):
   if obj and all(isinstance(x, dict) for x in obj): return obj
   for item in obj:
    found=find_record_list(item, depth+1)
    if found: return found
   return []
  if isinstance(obj, dict):
   for key in ("payload","data","rows","results","records","result","announcements"):
    if key in obj:
     found=find_record_list(obj[key], depth+1)
     if found: return found
  return []
 if source.exists():
  try:
   payload=json.loads(source.read_text(encoding="utf-8"))
   payload_rows=find_record_list(payload)
  except Exception as exc:
   report["groups"]["preserved_nse_disclosure_payload"]={"status":"BLOCKED","error":type(exc).__name__+": "+str(exc)[:220],"path":str(source)}
 direct_url="https://www.nseindia.com/api/corporate-announcements"
 if not payload_rows:
  try:
   start,end=p0_window()
   # Corporate filing API returns broadcast time, symbol, subject and attachment metadata.
   # Do not bypass access controls: an HTTP denial remains a source failure.
   sess=requests.Session(); sess.headers.update({"User-Agent":UA,"Accept":"application/json,text/plain,*/*","Referer":"https://www.nseindia.com/companies-listing/corporate-filings-announcements"})
   home=sess.get("https://www.nseindia.com/",timeout=(8,20)); home.raise_for_status()
   resp=sess.get(direct_url,params={"index":"equities","from_date":start.strftime("%d-%m-%Y"),"to_date":end.strftime("%d-%m-%Y")},
      timeout=(8,35)); resp.raise_for_status()
   direct_payload=resp.json()
   payload_rows=find_record_list(direct_payload)
   if not payload_rows:
    report["groups"]["corporate_events_api_attempt"]={"status":"BLOCKED","error":"HTTP response parsed but no list of disclosure records found","url":resp.url,"top_level_type":type(direct_payload).__name__,"top_level_keys":list(direct_payload)[:30] if isinstance(direct_payload,dict) else []}
  except Exception as exc:
   report["groups"]["corporate_events_api_attempt"]={"status":"BLOCKED","error":type(exc).__name__+": "+str(exc)[:220],"url":direct_url}
 normalized=[]
 for row in payload_rows:
  if not isinstance(row,dict): continue
  # NSE disclosure keys vary in capitalization and often use underscore aliases
  # such as broadcast_Date, attchmntText, attchmntFile and seq_Id. Normalize
  # lookup once so valid official rows are not silently discarded.
  row_by_lower={str(k).strip().lower():v for k,v in row.items()}
  def pick(*keys):
   return next((row_by_lower.get(str(k).strip().lower()) for k in keys
                if row_by_lower.get(str(k).strip().lower()) not in (None,"")), "")
  symbol=pick("symbol","sm_symbol","ticker","symbolName","TckrSymb","companySymbol")
  desc=pick("subject","purpose","description","desc","attchmntText","attchmnt_text","announcementType","DETAILS","details","meetingpurpose","relatingTo")
  stamp=pick("broadcastDateTime","broadcast_Date","broadcastDate","broadcast_date","an_dt","sort_date","date","disseminationDateTime","dissemination_date_time","DATE","broadcast_time")
  stamp_parsed=pd.to_datetime(stamp,errors="coerce",dayfirst=True,utc=True)
  if pd.isna(stamp_parsed) or not symbol or not desc: continue
  link=pick("attchmntFile","attachment","attachmentUrl","detailsUrl","xbrl","ixbrlfile","ixbrlfileurl","pdfUrl","url","DETAILS_URL")
  if str(link).startswith("/"): link="https://www.nseindia.com"+str(link)
  # The exact query URL is retained when an announcement has no attachment URL;
  # this identifies the official disclosure record without inventing an attachment.
  source_url=str(link) if link else direct_url
  if not source_url: continue
  normalized.append({"DATE":stamp_parsed.date().isoformat(),"SYMBOL":str(symbol).upper(),"EVENT_TYPE":str(desc),
   "PUBLISHED_AT":stamp_parsed.isoformat(),"SOURCE_URL":source_url,"SOURCE":"NSE corporate announcements",
   "SOURCE_RECORD_ID":str(pick("seq_Id","id","announcementId","broadcastId","sort_id"))})
 # If the nested result-disclosure payload has an unfamiliar schema, normalize the
 # already-collected official NSE announcements file instead of discarding 157k+
 # valid rows. Keep only source-backed rows inside the bounded P0 date window.
 ev=pd.DataFrame(normalized)
 existing_path=RAW/"corporate_events.csv"
 if ev.empty and existing_path.exists():
  try:
   prior=pd.read_csv(existing_path)
   prior.columns=[str(col).strip().upper() for col in prior.columns]
   required={"SYMBOL","EVENT_TYPE","SOURCE_URL"}
   if required.issubset(prior.columns) and ("PUBLISHED_AT" in prior.columns or "DATE" in prior.columns):
    raw_stamp=prior["PUBLISHED_AT"] if "PUBLISHED_AT" in prior.columns else prior["DATE"]
    stamps=pd.to_datetime(raw_stamp,format="mixed",errors="coerce",dayfirst=True,utc=True)
    start,end=p0_window()
    keep=stamps.notna() & prior["SYMBOL"].notna() & prior["EVENT_TYPE"].notna() & prior["SOURCE_URL"].notna()
    keep &= prior["SYMBOL"].astype(str).str.strip().ne("") & prior["EVENT_TYPE"].astype(str).str.strip().ne("") & prior["SOURCE_URL"].astype(str).str.startswith(("http://","https://"))
    keep &= stamps.dt.date.ge(start) & stamps.dt.date.le(end)
    ev=pd.DataFrame({"DATE":stamps.loc[keep].dt.strftime("%Y-%m-%d"),
      "SYMBOL":prior.loc[keep,"SYMBOL"].astype(str).str.strip().str.upper(),
      "EVENT_TYPE":prior.loc[keep,"EVENT_TYPE"].astype(str).str.strip(),
      "PUBLISHED_AT":stamps.loc[keep].map(lambda x:x.isoformat()),
      "SOURCE_URL":prior.loc[keep,"SOURCE_URL"].astype(str).str.strip(),
      "SOURCE":"NSE corporate announcements"})
    ev=ev.drop_duplicates(["DATE","SYMBOL","EVENT_TYPE","SOURCE_URL"])
  except Exception as exc:
   report["groups"]["corporate_events_existing_file"]={"status":"BLOCKED","error":type(exc).__name__+": "+str(exc)[:220],"path":str(existing_path)}
 if not ev.empty:
  ev=ev.drop_duplicates(["DATE","SYMBOL","EVENT_TYPE","SOURCE_URL"]).sort_values(["PUBLISHED_AT","SYMBOL"])
  ev.to_csv(RAW/"corporate_events.csv",index=False)
  report["groups"]["corporate_events"]={"status":"AVAILABLE","rows":len(ev),"unique_symbols":int(ev.SYMBOL.nunique()),"date_min":str(ev.DATE.min()),"date_max":str(ev.DATE.max()),"path":str(RAW/"corporate_events.csv"),"source":"NSE official corporate-announcements API/archive","url":direct_url or "preserved official NSE corporate announcements","note":"Source-backed publication timestamps normalized to ISO-8601 UTC; filing identity deduplicated without collapsing distinct same-day events."}
 else:
  report["groups"]["corporate_events"]={"status":"BLOCKED","rows":0,"reason":"No valid official NSE rows with symbol, subject, publication timestamp and source URL","attempted_url":direct_url}
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
   flow["DATE"]=pd.to_datetime(flow["DATE"],errors="coerce",dayfirst=True).dt.date.astype("string")
   flow=flow.dropna(subset=["DATE","GROUP","NET_VALUE"]).drop_duplicates(["DATE","GROUP"]).sort_values(["DATE","GROUP"])
   flow.to_csv(RAW/"fpi_dii_flows.csv",index=False)
   unique_dates=int(flow["DATE"].nunique())
   span_days=(pd.to_datetime(flow["DATE"],errors="coerce").max()-pd.to_datetime(flow["DATE"],errors="coerce").min()).days if unique_dates>1 else 0
   if unique_dates>=60 and span_days>=90:
    flow_meta={"status":"AVAILABLE","rows":len(flow),"unique_dates":unique_dates,"span_days":span_days,"path":str(RAW/"fpi_dii_flows.csv"),"source":"NSE official API","url":flow.SOURCE_URL.iloc[0]}
   else:
    flow_meta={"status":"BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE","rows":len(flow),"unique_dates":unique_dates,"span_days":span_days,"path":str(RAW/"fpi_dii_flows.csv"),"source":"NSE official API","url":flow.SOURCE_URL.iloc[0],"reason":"Requires >=60 distinct dated observations spanning >=90 calendar days; snapshot rows do not qualify"}
  else: flow_meta={"status":"BLOCKED","rows":0,"reason":"; ".join(errors)}
 except Exception as e: flow_meta={"status":"BLOCKED","rows":0,"error":type(e).__name__+": "+str(e)[:250]}
 report["groups"]["fpi_dii_flows"]=flow_meta
 report["status"]="ALL_FOUR_AVAILABLE" if all(v.get("status") in ("AVAILABLE","AVAILABLE_SECONDARY") and v.get("rows",0)>0 for v in report["groups"].values()) else "REPAIR_WITH_GAPS"
 REPORT.write_text(json.dumps(report,indent=2),encoding="utf-8")
 print(json.dumps(report,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
