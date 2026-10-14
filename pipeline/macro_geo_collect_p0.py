#!/usr/bin/env python3
"""Collect auditable P0 market series and timestamped geopolitical news events.

Market closes are retrieved from Yahoo Finance's chart endpoint as a transparent
public secondary source (not an NSE official feed). News articles come from the
GDELT DOC 2.0 API and are treated as timestamped media mentions, NOT verified
ground-truth event dates. Official NSE endpoints are attempted for corporate
announcements and FPI/DII flow data; failures remain explicit in the manifest.
"""
from __future__ import annotations
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote
import ast, hashlib, json, time
import requests
import pandas as pd

ROOT=Path(".")
RAW=ROOT/"data/external"
OUT=ROOT/"outputs/macro_geo"
PROCESSED=ROOT/"data/processed/nse_eq_200_sessions.csv"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36"
YAHOO="https://query1.finance.yahoo.com/v8/finance/chart/"
GDELT="https://api.gdeltproject.org/api/v2/doc/doc"
NSE="https://www.nseindia.com"
# Each label has a documented Yahoo symbol; sector indices are market proxies,
# not substitutes for official NSE data. Keep the exact symbol in the manifest.
SERIES={
    "NIFTY 50":{"symbol":"%5ENSEI","group":"benchmark_index"},
    "NIFTY IT":{"symbol":"%5ECNXIT","group":"sector_indices"},
    "NIFTY BANK":{"symbol":"%5ENSEBANK","group":"sector_indices"},
    "NIFTY AUTO":{"symbol":"%5ECNXAUTO","group":"sector_indices"},
    "NIFTY METAL":{"symbol":"%5ECNXMETAL","group":"sector_indices"},
    "NIFTY PHARMA":{"symbol":"%5ECNXPHARMA","group":"sector_indices"},
    "NIFTY ENERGY":{"symbol":"%5ECNXENERGY","group":"sector_indices"},
    "NIFTY FMCG":{"symbol":"%5ECNXFMCG","group":"sector_indices"},
    "NIFTY REALTY":{"symbol":"%5ECNXREALTY","group":"sector_indices"},
    "NIFTY INFRA":{"symbol":"%5ECNXINFRA","group":"sector_indices"},
    "INDIA VIX":{"symbol":"%5EINDIAVIX","group":"volatility"},
    "BRENT CRUDE FRONT MONTH":{"symbol":"BZ%3DF","group":"crude_oil"},
    "USD INR":{"symbol":"USDINR%3DX","group":"usd_inr"},
}
HEADERS={"User-Agent":UA,"Accept":"application/json,text/plain,*/*","Referer":"https://finance.yahoo.com/"}
session=requests.Session(); session.headers.update(HEADERS)

def session_bounds():
    if PROCESSED.exists():
        df=pd.read_csv(PROCESSED,usecols=["DATE"])
        dates=pd.to_datetime(df.DATE,errors="coerce").dropna()
        if not dates.empty: return dates.min().date(), dates.max().date()
    # The macro/geo-only workflow can run independently of the equity collector.
    # 400 calendar days normally cover ~200 NSE sessions; exact available dates
    # are determined by each source response and recorded in the manifest.
    end=datetime.now(timezone.utc).date()
    return end-timedelta(days=360),end

def yahoo_history(label,spec,start,end):
    # Yahoo chart period2 is exclusive. Keep provenance and never silently substitute symbols.
    period1=int(datetime.combine(start,datetime.min.time(),tzinfo=timezone.utc).timestamp())
    period2=int(datetime.combine(end+timedelta(days=1),datetime.min.time(),tzinfo=timezone.utc).timestamp())
    url=f"{YAHOO}{spec['symbol']}"
    resp=session.get(url,params={"period1":period1,"period2":period2,"interval":"1d","events":"history"},timeout=30)
    resp.raise_for_status()
    payload=resp.json()
    chart=payload.get("chart",{})
    if chart.get("error"): raise RuntimeError(str(chart["error"]))
    results=chart.get("result") or []
    if not results: raise RuntimeError("Yahoo returned no chart result")
    result=results[0]; timestamps=result.get("timestamp") or []
    quote_data=(result.get("indicators",{}).get("quote") or [{}])[0]
    closes=quote_data.get("close") or []
    rows=[]
    for ts,close in zip(timestamps,closes):
        if close is None: continue
        day=datetime.fromtimestamp(ts,timezone.utc).date()
        if start<=day<=end:
            rows.append({"DATE":day.isoformat(),"SERIES":label,"CLOSE":float(close),
                         "SOURCE":"Yahoo Finance chart API","SOURCE_URL":resp.url,
                         "SOURCE_SYMBOL":spec["symbol"],"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
    if not rows: raise RuntimeError("No usable closes in requested window")
    return rows,resp.url

def niftyindices_history(start,end):
    """Fetch official NSE Indices price-index OHLC history in one request per index."""
    index_map={
      "NIFTY 50":"NIFTY 50","NIFTY IT":"NIFTY IT","NIFTY BANK":"NIFTY BANK",
      "NIFTY AUTO":"NIFTY AUTO","NIFTY METAL":"NIFTY METAL","NIFTY PHARMA":"NIFTY PHARMA",
      "NIFTY ENERGY":"NIFTY ENERGY","NIFTY FMCG":"NIFTY FMCG","NIFTY REALTY":"NIFTY REALTY",
      "NIFTY INFRA":"NIFTY INFRASTRUCTURE"
    }
    start_text=start.strftime("%d-%b-%Y"); end_text=end.strftime("%d-%b-%Y")
    base="https://www.niftyindices.com/Backpage.aspx/"
    headers={"User-Agent":UA,"Accept":"application/json, text/plain, */*",
      "Content-Type":"application/json; charset=UTF-8","X-Requested-With":"XMLHttpRequest",
      "Referer":"https://www.niftyindices.com/reports/historical-data"}
    rows=[]; failures=[]
    for label,api_name in index_map.items():
        payload={"cinfo":f"{{'name':'{api_name}','startDate':'{start_text}','endDate':'{end_text}','indexName':'{api_name}'}}"}
        try:
            resp=session.post(base+"getHistoricaldatatabletoString",json=payload,headers=headers,timeout=(5,20))
            resp.raise_for_status(); body=resp.json(); raw_data=body.get("d","[]")
            try: data=raw_data if isinstance(raw_data,list) else json.loads(raw_data) if str(raw_data).strip().lower() not in ("false","none","null","") else []
            except Exception: data=ast.literal_eval(raw_data) if isinstance(raw_data,str) else []
            if not isinstance(data,list): data=[]
            for item in data:
                raw_date=item.get("HistoricalDate") or item.get("DATE")
                dt=pd.to_datetime(raw_date,errors="coerce",dayfirst=True)
                close=pd.to_numeric(pd.Series([item.get("CLOSE") or item.get("Closing")]),errors="coerce").iloc[0]
                if pd.isna(dt) or pd.isna(close) or close<=0: continue
                rows.append({"DATE":dt.date().isoformat(),"SERIES":label,"CLOSE":float(close),
                  "SOURCE":"NSE Indices historical data API","SOURCE_URL":resp.url,
                  "OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
        except Exception as exc:
            failures.append({"series":label,"api_index_name":api_name,"error":f"{type(exc).__name__}: {exc}"})
        time.sleep(0.15)
    # India VIX is served by a separate official endpoint.
    vix_payload=f"{{'name':'India VIX','startDate':'{start.strftime('%d %b %Y')}','endDate':'{end.strftime('%d %b %Y')}'}}"
    try:
        resp=session.post(base+"BindHistoricalIndiaVixData",data=vix_payload,
          headers=headers,timeout=(5,20))
        resp.raise_for_status(); body=resp.json(); raw=body.get("d","false")
        try: data=raw if isinstance(raw,list) else json.loads(raw) if str(raw).strip().lower() not in ("false","none","null","") else []
        except Exception: data=ast.literal_eval(raw) if isinstance(raw,str) else []
        if not isinstance(data,list): data=[]
        for item in data:
            dt=pd.to_datetime(item.get("date") or item.get("Date"),errors="coerce",dayfirst=True)
            close=pd.to_numeric(pd.Series([item.get("close") or item.get("CLOSE")]),errors="coerce").iloc[0]
            if pd.isna(dt) or pd.isna(close) or close<=0: continue
            rows.append({"DATE":dt.date().isoformat(),"SERIES":"INDIA VIX","CLOSE":float(close),
              "SOURCE":"NSE Indices India VIX historical API","SOURCE_URL":resp.url,
              "OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
    except Exception as exc:
        failures.append({"series":"INDIA VIX","error":f"{type(exc).__name__}: {exc}"})
    df=pd.DataFrame(rows)
    if not df.empty: df=df.drop_duplicates(["DATE","SERIES"]).sort_values(["DATE","SERIES"])
    return df.to_dict("records"),{"rows":len(df),"series":int(df.SERIES.nunique()) if not df.empty else 0,"failures":failures}

def nse_index_history(start,end):
    """Download official NSE daily multi-index close CSVs; no main-site session required."""
    aliases={
      "nifty50":"NIFTY 50","niftyit":"NIFTY IT","niftybank":"NIFTY BANK","niftyauto":"NIFTY AUTO",
      "niftymetal":"NIFTY METAL","niftypharma":"NIFTY PHARMA","niftyenergy":"NIFTY ENERGY",
      "niftyfmcg":"NIFTY FMCG","niftyrealty":"NIFTY REALTY","niftyinfrastructure":"NIFTY INFRA",
      "indiavix":"INDIA VIX"
    }
    rows=[]; failures=[]; days_seen=0
    day=start
    while day<=end:
        if day.weekday()<5:
            stamp=day.strftime("%d%m%Y")
            urls=[
              f"https://nsearchives.nseindia.com/content/indices/ind_close_all_{stamp}.csv",
              f"https://archives.nseindia.com/content/indices/ind_close_all_{stamp}.csv"
            ]
            found=False
            for url in urls:
                try:
                    resp=session.get(url,timeout=(4,8),headers={"User-Agent":UA,"Accept":"text/csv,*/*","Referer":NSE+"/all-reports"})
                    if resp.status_code==404: continue
                    resp.raise_for_status()
                    from io import StringIO
                    df=pd.read_csv(StringIO(resp.content.decode("utf-8-sig",errors="replace")))
                    df.columns=[str(c).strip().upper() for c in df.columns]
                    namecol=next((c for c in ["INDEX NAME","INDEX_NAME"] if c in df.columns),None)
                    datecol=next((c for c in ["INDEX DATE","INDEX_DATE","DATE"] if c in df.columns),None)
                    closecol=next((c for c in ["CLOSING","CLOSE","CLOSE VALUE"] if c in df.columns),None)
                    if not namecol or not datecol or not closecol:
                        failures.append({"date":day.isoformat(),"url":url,"error":"Unrecognized official NSE index CSV schema"})
                        found=True; break
                    df["_KEY"]=df[namecol].astype(str).str.lower().str.replace(r"[^a-z0-9]","",regex=True)
                    for _,row in df[df["_KEY"].isin(aliases)].iterrows():
                        close=pd.to_numeric(pd.Series([row[closecol]]),errors="coerce").iloc[0]
                        dt=pd.to_datetime(row[datecol],errors="coerce",dayfirst=True)
                        if pd.isna(close) or close<=0 or pd.isna(dt): continue
                        label=aliases[row["_KEY"]]
                        rows.append({"DATE":dt.date().isoformat(),"SERIES":label,"CLOSE":float(close),
                          "SOURCE":"NSE daily index close archive","SOURCE_URL":url,
                          "OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
                    found=True; days_seen+=1; break
                except Exception as exc:
                    failures.append({"date":day.isoformat(),"url":url,"error":f"{type(exc).__name__}: {exc}"})
            # A weekend/holiday 404 is normal. Keep a small pause for archive courtesy.
            time.sleep(0.08)
        day+=timedelta(days=1)
    return rows,{"weekday_requests":days_seen,"rows":len(rows),"failures":failures}

def fred_history(label,series_id,start,end):
    """Public FRED CSV observations with explicit series IDs and source URLs."""
    url="https://fred.stlouisfed.org/graph/fredgraph.csv"
    resp=session.get(url,params={"id":series_id,"cosd":start.isoformat(),"coed":end.isoformat()},
        timeout=(5,15),headers={"User-Agent":UA,"Accept":"text/csv,*/*","Referer":"https://fred.stlouisfed.org/"})
    resp.raise_for_status()
    from io import StringIO
    df=pd.read_csv(StringIO(resp.content.decode("utf-8-sig",errors="replace")))
    date_col=next((c for c in df.columns if str(c).strip().upper() in ("DATE","OBSERVATION_DATE")),None)
    value_col=next((c for c in df.columns if str(c).strip().upper()==series_id.upper()),None)
    if not date_col or not value_col: raise RuntimeError("FRED CSV schema mismatch: "+str(list(df.columns)))
    rows=[]
    for _,row in df.iterrows():
        dt=pd.to_datetime(row[date_col],errors="coerce")
        value=pd.to_numeric(pd.Series([row[value_col]]),errors="coerce").iloc[0]
        if pd.isna(dt) or pd.isna(value) or value<=0: continue
        rows.append({"DATE":dt.date().isoformat(),"SERIES":label,"CLOSE":float(value),
          "SOURCE":f"FRED series {series_id}","SOURCE_URL":resp.url,
          "OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
    if not rows: raise RuntimeError("FRED returned no valid observations for "+series_id)
    return rows,resp.url

def parse_gdelt_date(value):
    s=str(value or "").strip()
    for fmt in ("%Y%m%dT%H%M%SZ","%Y-%m-%dT%H:%M:%SZ","%Y-%m-%d %H:%M:%S"):
        try: return datetime.strptime(s,fmt).replace(tzinfo=timezone.utc)
        except ValueError: pass
    return None

def classify(title,query_label):
    t=title.lower()
    if any(k in t for k in ["oil","crude","strait of hormuz","red sea","shipping","tanker","opec"]): return "ENERGY_SHIPPING_NEWS"
    if any(k in t for k in ["sanction","tariff","trade war","export ban","export control"]): return "SANCTIONS_TARIFF_NEWS"
    if any(k in t for k in ["war","missile","attack","strike","conflict","military","ceasefire","border","iran","israel","ukraine","russia","pakistan"]): return "GEOPOLITICAL_CONFLICT_NEWS"
    return query_label

def fetch_gdelt_events(start,end):
    # Query the most recent 90 days using the DOC API's native timespan filter.
    # This avoids dozens of long historical-range requests and keeps timestamps/provenance.
    event_start=max(start,end-timedelta(days=90))
    queries=[
      ("GEOPOLITICAL_NEWS",'(war OR conflict OR military OR sanctions OR tariff OR "trade war" OR "Iran Israel" OR "Russia Ukraine" OR "India Pakistan")'),
      ("ENERGY_SHIPPING_NEWS",'(crude OR tanker OR shipping OR freight OR "oil supply" OR "Red Sea" OR "Strait of Hormuz")'),
    ]
    events=[]; failures=[]
    for query_label,query in queries:
        params={"query":query,"mode":"ArtList","format":"json","maxrecords":250,"sort":"DateDesc","timespan":"90d"}
        try:
            resp=session.get(GDELT,params=params,headers={"User-Agent":UA,"Accept":"application/json"},timeout=(5,20))
            resp.raise_for_status(); payload=resp.json()
            for article in payload.get("articles",[]):
                title=str(article.get("title") or "").strip(); url=str(article.get("url") or "").strip()
                published=parse_gdelt_date(article.get("seendate"))
                if not title or not url or not published or not event_start<=published.date()<=end: continue
                event_type=classify(title,query_label)
                event_id=hashlib.sha256((published.isoformat()+"|"+url).encode()).hexdigest()[:20]
                events.append({"EVENT_DATE":published.date().isoformat(),"EVENT_ID":event_id,"EVENT_TYPE":event_type,
                  "PUBLISHED_AT":published.isoformat(),"SOURCE":str(article.get("domain") or "GDELT-indexed source"),
                  "SOURCE_URL":url,"TITLE":title,"CONFIDENCE":0.5,
                  "EVIDENCE_TYPE":"MEDIA_MENTION_NOT_VERIFIED_EVENT",
                  "EVENT_DATE_BASIS":"GDELT_SEENDATE_PUBLICATION_PROXY",
                  "QUERY_GROUP":query_label,"SOURCE_COUNTRY":str(article.get("sourcecountry") or ""),
                  "GDELT_API_URL":resp.url})
        except Exception as exc:
            failures.append({"query_group":query_label,"error":f"{type(exc).__name__}: {exc}"})
        time.sleep(0.2)
    cols=["EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT","SOURCE","SOURCE_URL","TITLE","CONFIDENCE","EVIDENCE_TYPE","EVENT_DATE_BASIS","QUERY_GROUP","SOURCE_COUNTRY","GDELT_API_URL"]
    if events:
        df=pd.DataFrame(events,columns=cols).drop_duplicates(["EVENT_ID"]).sort_values(["PUBLISHED_AT","EVENT_ID"])
        return df,failures,event_start
    return pd.DataFrame(columns=cols),failures,event_start

def try_nse_json(endpoint,params,start,end):
    """Attempt official NSE endpoint; return rows or explicit failure without hiding access denial."""
    url=NSE+endpoint
    try:
        session.get(NSE,timeout=20,headers={"User-Agent":UA,"Accept":"text/html"}).raise_for_status()
        r=session.get(url,params=params,timeout=30,headers={"User-Agent":UA,"Accept":"application/json","Referer":NSE+"/"})
        r.raise_for_status()
        payload=r.json()
        if isinstance(payload,dict):
            for k in ("data","records","result"):
                if isinstance(payload.get(k),list): return payload[k],r.url
        if isinstance(payload,list): return payload,r.url
        return [],r.url
    except Exception as exc:
        return None,{"url":url,"error":f"{type(exc).__name__}: {exc}"}

def main():
    RAW.mkdir(parents=True,exist_ok=True); OUT.mkdir(parents=True,exist_ok=True)
    start,end=session_bounds()
    manifest={"status":"PARTIAL_COLLECTION","window_start":start.isoformat(),"window_end":end.isoformat(),
      "market_series":[],"event_collection":{},"official_nse_attempts":[],
      "important_boundary":"Indian benchmark/sector/VIX closes are from official NSE daily index archives. Brent/USDINR are attempted as secondary-source proxies. GDELT rows are timestamped media mentions, not independently verified event occurrence. Missing source stays UNKNOWN."}
    all_rows=[]
    # Prefer NSE Indices API; fall back to daily official index archive if the API
    # returns an empty/blocked payload. Never create placeholder market values.
    nse_rows,nse_report=niftyindices_history(start,end)
    nse_source="NSE Indices historical data API"
    if len(nse_rows)<100:
        archive_rows,archive_report=nse_index_history(start,end)
        if len(archive_rows)>len(nse_rows):
            nse_rows=archive_rows
            nse_source="NSE daily index close archive"
        manifest["nse_archive_fallback"]={"rows":len(archive_rows),"weekday_requests":archive_report["weekday_requests"],
            "failures":archive_report["failures"][-25:]}
    all_rows.extend(nse_rows)
    manifest["nse_market_data"]={"status":"AVAILABLE" if nse_rows else "BLOCKED","rows":len(nse_rows),
      "series":len(set(x["SERIES"] for x in nse_rows)) if nse_rows else 0,"source":nse_source,
      "api_failures":nse_report["failures"]}
    for label,spec in SERIES.items():
        if spec["group"] in ("benchmark_index","sector_indices","volatility"):
            found=[x for x in nse_rows if x["SERIES"]==label]
            manifest["market_series"].append({"series":label,"group":spec["group"],"status":"AVAILABLE" if found else "BLOCKED",
              "rows":len(found),"date_min":min((x["DATE"] for x in found),default=None),
              "date_max":max((x["DATE"] for x in found),default=None),"source":"NSE daily index close archive"})
        else:
            series_id="DCOILBRENTEU" if spec["group"]=="crude_oil" else "DEXINUS"
            try:
                rows,url=fred_history(label,series_id,start,end); all_rows.extend(rows)
                manifest["market_series"].append({"series":label,"group":spec["group"],"status":"AVAILABLE",
                  "rows":len(rows),"date_min":min(x["DATE"] for x in rows),"date_max":max(x["DATE"] for x in rows),
                  "source":f"FRED series {series_id}","source_url":url,
                  "units":"USD per barrel" if series_id=="DCOILBRENTEU" else "Indian rupees per USD"})
            except Exception as exc:
                manifest["market_series"].append({"series":label,"group":spec["group"],"status":"BLOCKED",
                  "source":f"FRED series {series_id}","error":f"{type(exc).__name__}: {exc}"})
    all_panel=pd.DataFrame(all_rows)
    panel=pd.DataFrame()
    if not all_panel.empty:
        all_panel=all_panel.drop_duplicates(["DATE","SERIES"]).sort_values(["DATE","SERIES"])
        panel=all_panel[all_panel["SERIES"].isin([x for x,s in SERIES.items() if s["group"] in ("benchmark_index","sector_indices","volatility")])].copy()
        panel.to_csv(RAW/"market_panel.csv",index=False)
        for group,labels in {
          "benchmark_indices":["NIFTY 50"],
          "sector_indices":[x for x,s in SERIES.items() if s["group"]=="sector_indices"],
          "volatility":["INDIA VIX"],"crude_oil":["BRENT CRUDE FRONT MONTH"],"usd_inr":["USD INR"]
        }.items():
            subset=all_panel[all_panel.SERIES.isin(labels)][["DATE","SERIES","CLOSE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"]].copy()
            if subset.empty: continue
            if group in ("crude_oil","usd_inr"):
                subset=subset.rename(columns={"SERIES":"INSTRUMENT"})
                subset.to_csv(RAW/("brent_crude.csv" if group=="crude_oil" else "usd_inr.csv"),index=False)
            else:
                subset.to_csv(RAW/("benchmark_indices.csv" if group=="benchmark_indices" else "sector_indices.csv" if group=="sector_indices" else "volatility.csv"),index=False)
    events,failures,event_start=fetch_gdelt_events(start,end)
    if not events.empty:
        events.to_csv(RAW/"events.csv",index=False)
        events[["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","SOURCE","SOURCE_URL","CONFIDENCE"]].to_csv(RAW/"geopolitical_events.csv",index=False)
    manifest["event_collection"]={"status":"AVAILABLE" if len(events) else "BLOCKED","rows":len(events),
      "window_start":event_start.isoformat(),"window_end":end.isoformat(),
      "date_min":events.EVENT_DATE.min() if len(events) else None,"date_max":events.EVENT_DATE.max() if len(events) else None,
      "source":"GDELT DOC 2.0 API","failures":failures,
      "warning":"EVENT_DATE is the article publication date proxy, not a verified occurrence timestamp; deduplicate and manually validate before causal interpretation."}
    for name,endpoint,params in [
      ("corporate_events","/api/corporates-announcements",{"index":"equities","from_date":start.strftime("%d-%m-%Y"),"to_date":end.strftime("%d-%m-%Y")}),
      ("fpi_dii_flows","/api/fiidiiTradeReact",{}),
    ]:
        data,detail=try_nse_json(endpoint,params,start,end)
        if data is None:
            manifest["official_nse_attempts"].append({"source":name,"status":"BLOCKED","detail":detail}); continue
        if not data:
            manifest["official_nse_attempts"].append({"source":name,"status":"NO_DATA_RETURNED","rows":0,"url":detail}); continue
        rawdf=pd.DataFrame(data); rawdf.columns=[str(c).strip().upper() for c in rawdf.columns]
        if name=="corporate_events":
            def first(row,candidates):
                return next((row[c] for c in candidates if c in row and pd.notna(row[c]) and str(row[c]).strip()),"")
            normalized=[]
            for _,row in rawdf.iterrows():
                day=first(row,["AN_DT","DATE","DT","SORT_DATE","ANNOUNCEMENT_DATE","BROADCAST_DATE"])
                symbol=first(row,["SYMBOL","SM_SYMBOL","TCKRSYMB"]); desc=first(row,["DESC","SUBJECT","PURPOSE"])
                pub=first(row,["AN_DT","PUBLISHED_AT","BROADCAST_DATE","DATE","SORT_DATE"])
                link=first(row,["ATTCHMNTFILE","ATTACHMENTFILE","ATTACHMENT","URL","LINK"])
                if day and symbol and desc:
                    normalized.append({"DATE":day,"SYMBOL":symbol,"EVENT_TYPE":desc,"PUBLISHED_AT":pub,
                      "SOURCE_URL":link if str(link).startswith("http") else (NSE+str(link) if link else ""),
                      "SOURCE":"NSE corporate announcements"})
            df=pd.DataFrame(normalized); required={"DATE","SYMBOL","EVENT_TYPE","PUBLISHED_AT","SOURCE_URL"}
        else:
            normalized=[]
            for _,row in rawdf.iterrows():
                day=next((row[c] for c in ["DATE","TRADE_DATE","TRADING_DATE"] if c in row and pd.notna(row[c])),"")
                group=next((row[c] for c in ["CATEGORY","GROUP","INVESTOR_TYPE","INVESTOR"] if c in row and pd.notna(row[c])),"")
                net=next((row[c] for c in ["NETVALUE","NET_VALUE","NET","NETAMOUNT"] if c in row and pd.notna(row[c])),"")
                if day and group and net!="": normalized.append({"DATE":day,"GROUP":group,"NET_VALUE":net,"SOURCE":"NSE FPI/DII activity"})
            df=pd.DataFrame(normalized); required={"DATE","GROUP","NET_VALUE"}
        if df.empty or not required.issubset(set(df.columns)):
            manifest["official_nse_attempts"].append({"source":name,"status":"SCHEMA_UNMAPPED","raw_rows":len(rawdf),
              "raw_columns":list(rawdf.columns),"url":detail}); continue
        df.to_csv(RAW/(name+".csv"),index=False)
        manifest["official_nse_attempts"].append({"source":name,"status":"AVAILABLE","rows":len(df),
          "date_min":str(df["DATE"].min()),"date_max":str(df["DATE"].max()),"url":detail})
    manifest["market_panel"]={"status":"AVAILABLE" if not panel.empty else "BLOCKED","rows":len(panel),
      "series":int(panel.SERIES.nunique()) if not panel.empty else 0,"path":str(RAW/"market_panel.csv")}
    manifest["events_file"]={"status":"AVAILABLE" if len(events) else "BLOCKED","rows":len(events),"path":str(RAW/"events.csv")}
    manifest["status"]="COLLECTED_WITH_GAPS" if not panel.empty and len(events) else "BLOCKED_INCOMPLETE"
    (OUT/"p0_collection_manifest.json").write_text(json.dumps(manifest,indent=2))
    print(json.dumps({"status":manifest["status"],"window_start":str(start),"window_end":str(end),
      "market_panel_rows":len(panel),"market_panel_series":int(panel.SERIES.nunique()) if not panel.empty else 0,
      "events_rows":len(events),"event_window_start":event_start.isoformat(),"gdelt_failures":len(failures),
      "official_nse_attempts":manifest["official_nse_attempts"]},indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
