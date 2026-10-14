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
import hashlib, json, time
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
    raise RuntimeError("Validated 200-session dataset is missing; collect/build NSE history first.")

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
    # DOC API date range is queried in 14-day chunks to reduce truncation risk.
    # The API's observed/published timestamp is used as the event-date proxy.
    queries=[
      ("GEOPOLITICAL_NEWS",'(war OR conflict OR military OR missile OR attack OR sanctions OR tariff OR "trade war")'),
      ("ENERGY_SHIPPING_NEWS",'("oil supply" OR crude OR tanker OR "Red Sea" OR "Strait of Hormuz" OR shipping OR freight)'),
      ("REGIONAL_RISK_NEWS",'("Iran Israel" OR "Russia Ukraine" OR "India Pakistan" OR "South China Sea" OR Taiwan)'),
    ]
    events=[]; failures=[]
    cursor=start
    while cursor<=end:
        chunk_end=min(end,cursor+timedelta(days=13))
        for query_label,query in queries:
            params={"query":query,"mode":"ArtList","format":"json","maxrecords":250,"sort":"DateDesc",
                    "startdatetime":cursor.strftime("%Y%m%d")+"000000",
                    "enddatetime":chunk_end.strftime("%Y%m%d")+"235959"}
            try:
                r=session.get(GDELT,params=params,headers={"User-Agent":UA,"Accept":"application/json"},timeout=45)
                r.raise_for_status()
                payload=r.json()
                for article in payload.get("articles",[]):
                    title=str(article.get("title") or "").strip()
                    url=str(article.get("url") or "").strip()
                    published=parse_gdelt_date(article.get("seendate"))
                    if not title or not url or not published: continue
                    pub_day=published.date()
                    if pub_day<start or pub_day>end: continue
                    event_type=classify(title,query_label)
                    event_id=hashlib.sha256((published.isoformat()+"|"+url).encode()).hexdigest()[:20]
                    events.append({
                        "EVENT_DATE":pub_day.isoformat(),"EVENT_ID":event_id,"EVENT_TYPE":event_type,
                        "PUBLISHED_AT":published.isoformat(),"SOURCE":str(article.get("domain") or "GDELT-indexed source"),
                        "SOURCE_URL":url,"TITLE":title,"CONFIDENCE":0.5,
                        "EVIDENCE_TYPE":"MEDIA_MENTION_NOT_VERIFIED_EVENT",
                        "EVENT_DATE_BASIS":"GDELT_SEENDATE_PUBLICATION_PROXY",
                        "QUERY_GROUP":query_label,"SOURCE_COUNTRY":str(article.get("sourcecountry") or ""),
                        "GDELT_API_URL":r.url,
                    })
            except Exception as exc:
                failures.append({"query_group":query_label,"start":cursor.isoformat(),"end":chunk_end.isoformat(),
                                 "error":f"{type(exc).__name__}: {exc}"})
            time.sleep(0.15)
        cursor=chunk_end+timedelta(days=1)
    if events:
        df=pd.DataFrame(events).drop_duplicates(["EVENT_ID"]).sort_values(["PUBLISHED_AT","EVENT_ID"])
        return df,failures
    return pd.DataFrame(columns=["EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT","SOURCE","SOURCE_URL","TITLE","CONFIDENCE","EVIDENCE_TYPE","EVENT_DATE_BASIS","QUERY_GROUP","SOURCE_COUNTRY","GDELT_API_URL"]),failures

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
              "important_boundary":"Yahoo chart data are public secondary-source market proxies; GDELT rows are news mentions, not independently verified event occurrence. Missing source stays UNKNOWN."}
    panel_rows=[]
    for label,spec in SERIES.items():
        try:
            rows,url=yahoo_history(label,spec,start,end)
            panel_rows.extend(rows)
            dates={r["DATE"] for r in rows}
            manifest["market_series"].append({"series":label,"group":spec["group"],"symbol":spec["symbol"],
                "status":"AVAILABLE","rows":len(rows),"date_min":min(dates),"date_max":max(dates),
                "source":"Yahoo Finance chart API","source_url":url})
        except Exception as exc:
            manifest["market_series"].append({"series":label,"group":spec["group"],"symbol":spec["symbol"],
                "status":"BLOCKED","error":f"{type(exc).__name__}: {exc}"})
        time.sleep(0.2)
    all_panel=pd.DataFrame(panel_rows)
    if not all_panel.empty:
        all_panel=all_panel.drop_duplicates(["DATE","SERIES"]).sort_values(["DATE","SERIES"])
        # Event-study panel is restricted to NSE-traded Indian series that share the
        # 15:30 IST close convention. Foreign-market commodities/FX stay in separate
        # files until their own close timestamps and calendars are modelled.
        panel=all_panel[~all_panel["SERIES"].map(lambda name: SERIES[name]["group"] in ("crude_oil","usd_inr"))].copy()
        panel.to_csv(RAW/"market_panel.csv",index=False)
        # Keep standardized group-level input files for the coverage inventory.
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
    events,failures=fetch_gdelt_events(start,end)
    if not events.empty:
        events.to_csv(RAW/"events.csv",index=False)
        events[["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","SOURCE","SOURCE_URL","CONFIDENCE"]].to_csv(RAW/"geopolitical_events.csv",index=False)
    manifest["event_collection"]={"status":"AVAILABLE" if len(events) else "BLOCKED","rows":len(events),
        "date_min":events.EVENT_DATE.min() if len(events) else None,"date_max":events.EVENT_DATE.max() if len(events) else None,
        "source":"GDELT DOC 2.0 API","failures":failures,
        "warning":"EVENT_DATE is the article publication date proxy, not a verified occurrence timestamp; deduplicate and manually validate before causal interpretation."}
    # Official NSE endpoints are attempted but never represented as successful without data.
    for name,endpoint,params in [
        ("corporate_events","/api/corporates-announcements",{"index":"equities","from_date":start.strftime("%d-%m-%Y"),"to_date":end.strftime("%d-%m-%Y")}),
        ("fpi_dii_flows","/api/fiidiiTradeReact",{}),
    ]:
        data,detail=try_nse_json(endpoint,params,start,end)
        if data is None:
            manifest["official_nse_attempts"].append({"source":name,"status":"BLOCKED","detail":detail})
            continue
        if not data:
            manifest["official_nse_attempts"].append({"source":name,"status":"NO_DATA_RETURNED","rows":0,"url":detail})
            continue
        rawdf=pd.DataFrame(data)
        rawdf.columns=[str(c).strip().upper() for c in rawdf.columns]
        if name=="corporate_events":
            def first(row, candidates):
                return next((row[c] for c in candidates if c in row and pd.notna(row[c]) and str(row[c]).strip()), "")
            normalized=[]
            for _,row in rawdf.iterrows():
                day=first(row,["AN_DT","DATE","DT","SORT_DATE","ANNOUNCEMENT_DATE","BROADCAST_DATE"])
                symbol=first(row,["SYMBOL","SM_SYMBOL","TCKRSYMB"])
                desc=first(row,["DESC","SUBJECT","ATTACHMENT","PURPOSE"])
                pub=first(row,["AN_DT","PUBLISHED_AT","BROADCAST_DATE","DATE","SORT_DATE"])
                link=first(row,["ATTCHMNTFILE","ATTACHMENTFILE","ATTACHMENT","URL","LINK"])
                if day and symbol and desc:
                    normalized.append({"DATE":day,"SYMBOL":symbol,"EVENT_TYPE":desc,"PUBLISHED_AT":pub,
                        "SOURCE_URL":link if str(link).startswith("http") else (NSE+str(link) if link else ""),
                        "SOURCE":"NSE corporate announcements"})
            df=pd.DataFrame(normalized)
            required={"DATE","SYMBOL","EVENT_TYPE","PUBLISHED_AT","SOURCE_URL"}
        else:
            normalized=[]
            for _,row in rawdf.iterrows():
                day=next((row[c] for c in ["DATE","TRADE_DATE","TRADING_DATE"] if c in row and pd.notna(row[c])), "")
                group=next((row[c] for c in ["CATEGORY","GROUP","INVESTOR_TYPE","INVESTOR"] if c in row and pd.notna(row[c])), "")
                net=next((row[c] for c in ["NETVALUE","NET_VALUE","NET","NETAMOUNT"] if c in row and pd.notna(row[c])), "")
                if day and group and net!="":
                    normalized.append({"DATE":day,"GROUP":group,"NET_VALUE":net,"SOURCE":"NSE FPI/DII activity"})
            df=pd.DataFrame(normalized)
            required={"DATE","GROUP","NET_VALUE"}
        if df.empty or not required.issubset(set(df.columns)):
            manifest["official_nse_attempts"].append({"source":name,"status":"SCHEMA_UNMAPPED","raw_rows":len(rawdf),
                "raw_columns":list(rawdf.columns),"url":detail})
            continue
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
        "events_rows":len(events),"gdelt_failures":len(failures),
        "official_nse_attempts":manifest["official_nse_attempts"]},indent=2))
    # Do not fail the whole audit on a third-party source outage; manifest exposes it.
    return 0
if __name__=="__main__": raise SystemExit(main())
