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
    "GLOBAL VIX":{"symbol":"%5EVIX","group":"volatility","fred_id":"VIXCLS"},
    "BRENT CRUDE FRONT MONTH":{"symbol":"BZ%3DF","group":"crude_oil","fred_id":"DCOILBRENTEU"},
    "USD INR":{"symbol":"USDINR%3DX","group":"usd_inr","fred_id":"DEXINUS"},
    "USD STRENGTH PROXY":{"symbol":"DX-Y.NYB","group":"dollar_index","fred_id":"DTWEXBGS"},
    "US 2Y TREASURY YIELD":{"symbol":"%5EIRX","group":"us_yields","fred_id":"DGS2","fallback_allowed":False},
    "US 10Y TREASURY YIELD":{"symbol":"%5ETNX","group":"us_yields","fred_id":"DGS10","fallback_allowed":False},
    "US 10Y REAL YIELD":{"symbol":"%5EIRX","group":"us_real_yields","fred_id":"DFII10","fallback_allowed":False},
    "GOLD FRONT MONTH":{"symbol":"GC%3DF","group":"global_commodities","fred_id":"GOLDAMGBD228NLBM"},
    "COPPER FRONT MONTH":{"symbol":"HG%3DF","group":"global_commodities","fred_id":"PCOPPUSDM"},
    "USD JPY":{"symbol":"JPY%3DX","group":"fx_carry","fred_id":"DEXJPUS"},
    "USD CNY":{"symbol":"CNY%3DX","group":"fx_carry","fred_id":"DEXCHUS"},
}
HEADERS={"User-Agent":UA,"Accept":"application/json,text/plain,*/*","Referer":"https://finance.yahoo.com/"}
session=requests.Session(); session.headers.update(HEADERS)

def session_bounds():
    # Macro/Geo research has its own long-history requirement; never inherit the
    # 200-session equity file's short date range. Keep the equity cutoff separate.
    end=datetime.now(timezone.utc).date()
    return datetime(2006,1,1).date(),end

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
                    closecol=next((c for c in ["CLOSING INDEX VALUE","CLOSING","CLOSE","CLOSE VALUE"] if c in df.columns),None)
                    if not namecol or not datecol or not closecol:
                        failures.append({"date":day.isoformat(),"url":url,"error":"Unrecognized official NSE index CSV schema",
                          "columns":list(df.columns),"preview":resp.text[:180]})
                        # A 200 response can still be an HTML/block page; try the alternate archive host.
                        continue
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
    """Fetch public FRED CSV in bounded 5-year windows to avoid long-request timeouts."""
    from io import StringIO
    url="https://fred.stlouisfed.org/graph/fredgraph.csv"
    rows=[]; source_urls=[]; cursor=start
    while cursor<=end:
        chunk_end=min(end,cursor+timedelta(days=365-1))
        resp=None; last_error=None
        for attempt,wait in enumerate((0,2,5),start=1):
            if wait: time.sleep(wait)
            try:
                resp=session.get(url,params={"id":series_id,"cosd":cursor.isoformat(),"coed":chunk_end.isoformat()},
                    timeout=(5,20),headers={"User-Agent":UA,"Accept":"text/csv,*/*","Referer":"https://fred.stlouisfed.org/"})
                resp.raise_for_status()
                break
            except Exception as exc:
                last_error=exc
                if attempt==3: raise RuntimeError(
                    f"FRED {series_id} failed for {cursor.isoformat()}..{chunk_end.isoformat()}: {type(last_error).__name__}: {last_error}"
                ) from exc
        df=pd.read_csv(StringIO(resp.content.decode("utf-8-sig",errors="replace")))
        date_col=next((c for c in df.columns if str(c).strip().upper() in ("DATE","OBSERVATION_DATE")),None)
        value_col=next((c for c in df.columns if str(c).strip().upper()==series_id.upper()),None)
        if not date_col or not value_col:
            raise RuntimeError(f"FRED CSV schema mismatch for {series_id}: {list(df.columns)}")
        source_urls.append(resp.url)
        for _,row in df.iterrows():
            dt=pd.to_datetime(row[date_col],errors="coerce")
            value=pd.to_numeric(pd.Series([row[value_col]]),errors="coerce").iloc[0]
            if pd.isna(dt) or pd.isna(value): continue
            if not cursor<=dt.date()<=chunk_end: continue
            rows.append({"DATE":dt.date().isoformat(),"SERIES":label,"CLOSE":float(value),
              "SOURCE":f"FRED series {series_id}","SOURCE_URL":resp.url,
              "OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
        cursor=chunk_end+timedelta(days=1)
    df_rows=pd.DataFrame(rows)
    if df_rows.empty: raise RuntimeError("FRED returned no valid observations for "+series_id)
    df_rows=df_rows.drop_duplicates(["DATE","SERIES"]).sort_values(["DATE","SERIES"])
    return df_rows.to_dict("records"),";".join(source_urls)

def parse_gdelt_date(value):
    s=str(value or "").strip()
    for fmt in ("%Y%m%dT%H%M%SZ","%Y-%m-%dT%H:%M:%SZ","%Y-%m-%d %H:%M:%S"):
        try: return datetime.strptime(s,fmt).replace(tzinfo=timezone.utc)
        except ValueError: pass
    return None

def classify(title,query_label):
    """Reject broad-query false positives; label only titles with explicit market-relevant terms."""
    t=str(title or "").lower()
    energy_terms=["oil","crude","strait of hormuz","red sea","shipping","tanker","opec","lng","natural gas","refinery","fuel supply","energy infrastructure"]
    policy_terms=["sanction","tariff","trade war","export ban","export control","embargo","trade restriction"]
    conflict_terms=["war","missile","attack","airstrike","strike","conflict","military","ceasefire","invasion","border clash","iran","israel","ukraine","russia","pakistan","taiwan","china","drone strike","blockade","bombing"]
    if any(k in t for k in energy_terms): return "ENERGY_SHIPPING_NEWS"
    if any(k in t for k in policy_terms): return "SANCTIONS_TARIFF_NEWS"
    if any(k in t for k in conflict_terms): return "GEOPOLITICAL_CONFLICT_NEWS"
    return None

TRUSTED_NEWS_DOMAINS={
    "reuters.com","reutersagency.com","apnews.com","bbc.com","bbc.co.uk","aljazeera.com","bloomberg.com",
    "cnbc.com","theguardian.com","ft.com","dw.com","france24.com","npr.org",
    "abc.net.au","thehindu.com","indianexpress.com","economictimes.indiatimes.com",
    "business-standard.com","moneycontrol.com","hindustantimes.com","nytimes.com","wsj.com"
}

def is_trusted_news_url(url):
    try:
        from urllib.parse import urlparse
        host=(urlparse(str(url)).hostname or "").lower().split(":")[0]
        return any(host==domain or host.endswith("."+domain) for domain in TRUSTED_NEWS_DOMAINS)
    except Exception:
        return False

def fetch_gdelt_events(start,end):
    """Collect timestamped trusted media mentions from GDELT plus public publisher RSS feeds."""
    event_start=max(start,end-timedelta(days=90))
    queries=[
      ("GEOPOLITICAL_NEWS",'(war OR conflict OR military OR sanctions OR tariff OR "trade war" OR "Iran Israel" OR "Russia Ukraine" OR "India Pakistan" OR missile OR invasion OR ceasefire)'),
      ("ENERGY_SHIPPING_NEWS",'(crude OR tanker OR shipping OR freight OR "oil supply" OR "Red Sea" OR "Strait of Hormuz" OR OPEC OR refinery OR LNG)'),
    ]
    metrics={"gdelt":{"requests_attempted":0,"request_failures":0,"successful_responses":0,
      "successful_empty_responses":0,"articles_seen":0,"filtered_untrusted_publisher":0,
      "filtered_irrelevant_title":0,"filtered_invalid_timestamp":0,"accepted_articles":0},
      "rss":{"feeds_attempted":0,"feed_failures":0,"successful_feeds":0,"successful_empty_feeds":0,
      "articles_seen":0,"filtered_untrusted_publisher":0,"filtered_irrelevant_title":0,
      "filtered_invalid_timestamp":0,"accepted_articles":0,"feed_results":[]}}
    events=[]; failures=[]
    slices=[]; cursor=event_start
    while cursor<=end:
        slice_end=min(end,cursor+timedelta(days=29))
        slices.append((cursor,slice_end)); cursor=slice_end+timedelta(days=1)
    cols=["EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT","SOURCE","SOURCE_URL","TITLE","CONFIDENCE",
      "EVIDENCE_TYPE","EVENT_DATE_BASIS","QUERY_GROUP","SOURCE_COUNTRY","GDELT_API_URL"]
    def add_article(title,url,published,provider,group,evidence,basis,confidence,metric_group,source_country=""):
        m=metrics[metric_group]
        if not title or not url:
            m["filtered_invalid_timestamp"]+=1
            return
        if published is None:
            m["filtered_invalid_timestamp"]+=1
            return
        if not is_trusted_news_url(url):
            m["filtered_untrusted_publisher"]+=1
            return
        event_type=classify(title,group)
        if event_type is None:
            m["filtered_irrelevant_title"]+=1
            return
        event_id=hashlib.sha256((published.isoformat()+"|"+url).encode()).hexdigest()[:20]
        events.append({"EVENT_DATE":published.date().isoformat(),"EVENT_ID":event_id,"EVENT_TYPE":event_type,
          "PUBLISHED_AT":published.isoformat(),"SOURCE":provider or "trusted publisher",
          "SOURCE_URL":url,"TITLE":title,"CONFIDENCE":confidence,"EVIDENCE_TYPE":evidence,
          "EVENT_DATE_BASIS":basis,"QUERY_GROUP":group,"SOURCE_COUNTRY":source_country,
          "GDELT_API_URL":""})
        m["accepted_articles"]+=1
    for slice_start,slice_end in slices:
      for query_label,query in queries:
        params={"query":query,"mode":"ArtList","format":"json","maxrecords":100,"sort":"DateDesc",
          "startdatetime":slice_start.strftime("%Y%m%d")+"000000",
          "enddatetime":slice_end.strftime("%Y%m%d")+"235959"}
        last_error=None
        metrics["gdelt"]["requests_attempted"]+=1
        for attempt in range(3):
            try:
                resp=session.get(GDELT,params=params,headers={"User-Agent":UA,"Accept":"application/json"},timeout=30)
                if resp.status_code==429:
                    retry_after=resp.headers.get("Retry-After","")
                    try: wait=min(90,max(10,int(float(retry_after))))
                    except (TypeError,ValueError): wait=15*(attempt+1)
                    last_error=f"HTTP 429 rate limit; slice {slice_start}/{slice_end}; retry {attempt+1}/3 after {wait}s"
                    if attempt<2:
                        time.sleep(wait)
                        continue
                    break
                resp.raise_for_status()
                payload=resp.json()
                if not isinstance(payload,dict) or not isinstance(payload.get("articles"),list):
                    raise RuntimeError("GDELT response did not contain a valid articles list")
                articles=payload.get("articles",[])
                metrics["gdelt"]["successful_responses"]+=1
                if len(articles)==0: metrics["gdelt"]["successful_empty_responses"]+=1
                metrics["gdelt"]["articles_seen"]+=len(articles)
                for article in articles:
                    title=str(article.get("title") or "").strip(); url=str(article.get("url") or "").strip()
                    published=parse_gdelt_date(article.get("seendate"))
                    if published is None or not slice_start<=published.date()<=slice_end:
                        metrics["gdelt"]["filtered_invalid_timestamp"]+=1
                        continue
                    before=len(events)
                    add_article(title,url,published,str(article.get("domain") or "trusted publisher via GDELT"),
                      query_label,"TRUSTED_MEDIA_MENTION_NOT_VERIFIED_EVENT",
                      "GDELT_SEENDATE_PUBLICATION_PROXY",0.75,"gdelt",str(article.get("sourcecountry") or ""))
                    if len(events)>before:
                        events[-1]["GDELT_API_URL"]=resp.url
                last_error=None
                break
            except Exception as exc:
                last_error=f"{type(exc).__name__}: {exc}; slice {slice_start}/{slice_end}"
                if attempt<2: time.sleep(8*(attempt+1))
        if last_error:
            metrics["gdelt"]["request_failures"]+=1
            failures.append({"provider":"GDELT","query_group":query_label,"slice_start":slice_start.isoformat(),
              "slice_end":slice_end.isoformat(),"error":last_error})
        time.sleep(8.0)

    # Public RSS/Atom feeds are a fallback and are audited independently.
    # Publication times are feed publication timestamps, not verified event-occurrence times.
    feeds=[
      ("Reuters","https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best"),
      ("AP News","https://apnews.com/hub/world-news?output=rss"),
      ("BBC","https://feeds.bbci.co.uk/news/world/rss.xml"),
      ("Al Jazeera","https://www.aljazeera.com/xml/rss/all.xml"),
      ("Bloomberg","https://feeds.bloomberg.com/markets/news.rss"),
    ]
    import xml.etree.ElementTree as ET
    from email.utils import parsedate_to_datetime
    def parse_feed_date(value):
        if not value: return None
        try:
            dt=pd.to_datetime(value,utc=True,errors="coerce")
            if not pd.isna(dt): return dt.to_pydatetime()
        except Exception: pass
        try:
            dt=parsedate_to_datetime(value)
            if dt.tzinfo is None: return None
            return dt.astimezone(timezone.utc)
        except Exception: return None
    for publisher,feed_url in feeds:
        rm=metrics["rss"]; rm["feeds_attempted"]+=1
        try:
            response=session.get(feed_url,headers={"User-Agent":UA,"Accept":"application/rss+xml, application/atom+xml, application/xml, text/xml, */*"},timeout=(5,15))
            response.raise_for_status()
            root=ET.fromstring(response.content)
            items=root.findall(".//item")
            atom_ns={"atom":"http://www.w3.org/2005/Atom"}
            if not items:
                items=root.findall(".//atom:entry",atom_ns)
            rm["successful_feeds"]+=1
            if not items: rm["successful_empty_feeds"]+=1
            rm["articles_seen"]+=len(items)
            accepted_before=rm["accepted_articles"]
            for item in items:
                def child_text(names):
                    for name in names:
                        el=item.find(name)
                        if el is not None and (el.text or "").strip(): return (el.text or "").strip()
                    return ""
                title=child_text(["title","{http://www.w3.org/2005/Atom}title"])
                url=child_text(["link","{http://www.w3.org/2005/Atom}link"])
                if not url:
                    el=item.find("{http://www.w3.org/2005/Atom}link")
                    if el is not None: url=str(el.attrib.get("href") or "")
                pub=child_text(["pubDate","published","updated","{http://www.w3.org/2005/Atom}published","{http://www.w3.org/2005/Atom}updated"])
                published=parse_feed_date(pub)
                before=len(events)
                add_article(title,url,published,publisher,"PUBLISHER_RSS",
                  "TRUSTED_PUBLISHER_RSS_MENTION_NOT_VERIFIED_EVENT",
                  "PUBLISHER_FEED_PUBLICATION_TIMESTAMP",0.80,"rss")
                if len(events)>before:
                    events[-1]["GDELT_API_URL"]=feed_url
            rm["feed_results"].append({"publisher":publisher,"feed_url":feed_url,"status":"AVAILABLE",
              "items_seen":len(items),"accepted":rm["accepted_articles"]-accepted_before})
        except Exception as exc:
            rm["feed_failures"]+=1
            err=f"{type(exc).__name__}: {exc}"
            failures.append({"provider":"RSS","publisher":publisher,"feed_url":feed_url,"error":err})
            rm["feed_results"].append({"publisher":publisher,"feed_url":feed_url,"status":"BLOCKED","error":err})
    if events:
        df=pd.DataFrame(events,columns=cols).drop_duplicates(["EVENT_ID"]).sort_values(["PUBLISHED_AT","EVENT_ID"])
        # Accepted counters are article-level before deduplication; report final unique event count too.
        metrics["unique_events_after_deduplication"]=int(len(df))
        return df,failures,event_start,metrics
    metrics["unique_events_after_deduplication"]=0
    return pd.DataFrame(columns=cols),failures,event_start,metrics
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
    # Bootstrap official sites with browser-like headers before their data endpoints.
    bootstrap_headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language":"en-US,en;q=0.9","Referer":"https://www.nseindia.com/","Connection":"keep-alive"}
    for home in ("https://www.niftyindices.com/reports/historical-data","https://www.nseindia.com/","https://www.nseindia.com/all-reports"):
        try: session.get(home,headers=bootstrap_headers,timeout=8)
        except Exception: pass
    # Prefer NSE Indices API; fall back to daily official index archive if the API
    # returns an empty/blocked payload. Never create placeholder market values.
    nse_rows,nse_report=niftyindices_history(start,end)
    nse_source="NSE Indices historical data API"
    # Avoid thousands of day-by-day archive requests for a 20-year panel.
    # The official index API is preferred where it responds; public Yahoo history
    # fills only missing date+series keys and remains explicitly labelled secondary.
    if len(nse_rows)<100:
        # The index API may return a WAF/HTML response instead of JSON.
        # Bound the official day-by-day fallback to the recent ~18 months;
        # a 2006-to-present loop can make thousands of requests and stall CI.
        # Longer history is filled separately from labelled Yahoo/FRED sources.
        archive_start=max(start,end-timedelta(days=550))
        archive_rows,archive_report=nse_index_history(archive_start,end)
        existing={(x["DATE"],x["SERIES"]) for x in nse_rows}
        nse_rows.extend(x for x in archive_rows if (x["DATE"],x["SERIES"]) not in existing)
        if archive_rows: nse_source="NSE Indices API + official daily index close archive (recent fallback)"
        manifest["nse_archive_fallback"]={"window_start":archive_start.isoformat(),"window_end":end.isoformat(),
            "rows":len(archive_rows),"weekday_requests":archive_report["weekday_requests"],
            "failures":archive_report["failures"][-25:]}
    all_rows.extend(nse_rows)
    official_keys={(x["DATE"],x["SERIES"]) for x in nse_rows}
    historical_fill={"available":0,"blocked":[]}
    for label,spec in SERIES.items():
        if spec["group"] not in ("benchmark_index","sector_indices","volatility"): continue
        try:
            hist,url=yahoo_history(label,spec,start,end)
            missing=[x for x in hist if (x["DATE"],x["SERIES"]) not in official_keys]
            all_rows.extend(missing)
            historical_fill["available"]+=len(missing)
            manifest.setdefault("secondary_historical_series",[]).append({"series":label,"rows_added":len(missing),
              "source":"Yahoo Finance chart API; fills dates absent from official NSE index archive/API",
              "source_url":url,"date_min":min((x["DATE"] for x in missing),default=None),
              "date_max":max((x["DATE"] for x in missing),default=None)})
        except Exception as exc:
            # FRED's VIX close is an explicit alternative for GLOBAL VIX only;
            # never use it as a substitute for India VIX or NSE sector indices.
            if spec.get("fred_id"):
                try:
                    hist,url=fred_history(label,spec["fred_id"],start,end)
                    all_rows.extend(hist)
                    historical_fill["available"]+=len(hist)
                    manifest.setdefault("secondary_historical_series",[]).append({"series":label,"rows_added":len(hist),
                      "source":f"FRED series {spec['fred_id']} (alternative source)","source_url":url,
                      "date_min":min(x["DATE"] for x in hist),"date_max":max(x["DATE"] for x in hist)})
                    continue
                except Exception as fred_exc:
                    historical_fill["blocked"].append({"series":label,"error":f"Yahoo {type(exc).__name__}: {exc}; FRED {type(fred_exc).__name__}: {fred_exc}"})
            else:
                historical_fill["blocked"].append({"series":label,"error":f"{type(exc).__name__}: {exc}"})
    manifest["historical_index_fill"]=historical_fill
    manifest["nse_market_data"]={"status":"AVAILABLE" if nse_rows else "BLOCKED","rows":len(nse_rows),
      "series":len(set(x["SERIES"] for x in nse_rows)) if nse_rows else 0,"source":nse_source,
      "api_failures":nse_report["failures"]}
    for label,spec in SERIES.items():
        if spec["group"] in ("benchmark_index","sector_indices","volatility"):
            # GLOBAL VIX is not part of the NSE index archive. The old generic
            # volatility branch skipped it before its FRED VIXCLS fallback could run.
            # Collect it independently; never substitute INDIA VIX for GLOBAL VIX.
            if label == "GLOBAL VIX":
                try:
                    rows,url=fred_history(label,spec["fred_id"],start,end)
                    all_rows.extend(rows)
                    manifest["market_series"].append({"series":label,"group":spec["group"],"status":"AVAILABLE",
                      "rows":len(rows),"date_min":min(x["DATE"] for x in rows),"date_max":max(x["DATE"] for x in rows),
                      "source":f"FRED series {spec['fred_id']}","source_url":url,"fred_series_id":spec["fred_id"]})
                except Exception as exc:
                    manifest["market_series"].append({"series":label,"group":spec["group"],"status":"BLOCKED",
                      "rows":0,"date_min":None,"date_max":None,"source":f"FRED series {spec['fred_id']}",
                      "error":f"{type(exc).__name__}: {exc}; India VIX is not an acceptable substitute"})
                continue
            found=[x for x in all_rows if x["SERIES"]==label]
            sources=sorted(set(x["SOURCE"] for x in found))
            manifest["market_series"].append({"series":label,"group":spec["group"],"status":"AVAILABLE" if found else "BLOCKED",
              "rows":len(found),"date_min":min((x["DATE"] for x in found),default=None),
              "date_max":max((x["DATE"] for x in found),default=None),"sources":sources})
            continue
        series_id=spec.get("fred_id")
        fred_exc=None
        if series_id:
            try:
                rows,url=fred_history(label,series_id,start,end)
                all_rows.extend(rows)
                manifest["market_series"].append({"series":label,"group":spec["group"],"status":"AVAILABLE",
                  "rows":len(rows),"date_min":min(x["DATE"] for x in rows),"date_max":max(x["DATE"] for x in rows),
                  "source":f"FRED series {series_id}","source_url":url,"fred_series_id":series_id})
                continue
            except Exception as exc:
                fred_exc=exc
        if spec.get("fallback_allowed") is False:
            manifest["market_series"].append({"series":label,"group":spec["group"],"status":"BLOCKED",
              "source":f"FRED series {series_id}","error":f"FRED unavailable: {type(fred_exc).__name__}: {fred_exc}; Yahoo fallback deliberately disabled to avoid incompatible units/proxies"})
            continue
        try:
            rows,url=yahoo_history(label,spec,start,end)
            all_rows.extend(rows)
            manifest["market_series"].append({"series":label,"group":spec["group"],"status":"AVAILABLE_SECONDARY",
              "rows":len(rows),"date_min":min(x["DATE"] for x in rows),"date_max":max(x["DATE"] for x in rows),
              "source":"Yahoo Finance chart API (secondary source/fallback)","source_url":url,
              "source_symbol":spec["symbol"],"fred_series_id":series_id,
              "fred_failure":f"{type(fred_exc).__name__}: {fred_exc}" if fred_exc else None})
        except Exception as fallback_exc:
            manifest["market_series"].append({"series":label,"group":spec["group"],"status":"BLOCKED",
              "source":f"FRED series {series_id}; Yahoo fallback" if series_id else "Yahoo Finance chart API",
              "error":f"FRED {type(fred_exc).__name__}: {fred_exc}; Yahoo {type(fallback_exc).__name__}: {fallback_exc}" if fred_exc else f"{type(fallback_exc).__name__}: {fallback_exc}"})
    all_panel=pd.DataFrame(all_rows)
    panel=pd.DataFrame()
    if not all_panel.empty:
        all_panel=all_panel.drop_duplicates(["DATE","SERIES"]).sort_values(["DATE","SERIES"])
        # The event-study panel includes all successfully collected P0 series:
        # benchmark, sectors, volatility, crude and USD/INR. Missing series stay absent/UNKNOWN.
        panel=all_panel[all_panel["SERIES"].isin(list(SERIES.keys()))].copy()
        panel.to_csv(RAW/"market_panel.csv",index=False)
        group_labels={
          "benchmark_indices":["NIFTY 50"],
          "sector_indices":[x for x,s in SERIES.items() if s["group"]=="sector_indices"],
          "volatility":[x for x,s in SERIES.items() if s["group"]=="volatility"],
          "crude_oil":["BRENT CRUDE FRONT MONTH"],"usd_inr":["USD INR"],
          "us_yields":[x for x,s in SERIES.items() if s["group"]=="us_yields"],
          "us_real_yields":[x for x,s in SERIES.items() if s["group"]=="us_real_yields"],
          "dollar_index":["USD STRENGTH PROXY"],
          "global_commodities":[x for x,s in SERIES.items() if s["group"]=="global_commodities"],
          "fx_carry":[x for x,s in SERIES.items() if s["group"]=="fx_carry"]
        }
        group_files={"benchmark_indices":"benchmark_indices.csv","sector_indices":"sector_indices.csv",
          "volatility":"volatility.csv","crude_oil":"brent_crude.csv","usd_inr":"usd_inr.csv",
          "us_yields":"us_yields.csv","us_real_yields":"us_real_yields.csv",
          "dollar_index":"dxy.csv","global_commodities":"commodity_prices.csv","fx_carry":"fx_carry.csv"}
        for group,labels in group_labels.items():
            subset=all_panel[all_panel.SERIES.isin(labels)][["DATE","SERIES","CLOSE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"]].copy()
            if subset.empty: continue
            if group in ("crude_oil","usd_inr"):
                subset=subset.rename(columns={"SERIES":"INSTRUMENT"})
            elif group=="dollar_index":
                subset=subset.drop(columns=["SERIES"])
            elif group=="global_commodities":
                subset=subset.rename(columns={"SERIES":"COMMODITY"})
            elif group=="fx_carry":
                subset=subset.rename(columns={"SERIES":"PAIR","CLOSE":"VALUE"})
            subset.to_csv(RAW/group_files[group],index=False)
    events,failures,event_start,event_metrics=fetch_gdelt_events(start,end)
    # Always materialize header-only files on an empty collection so QA can
    # distinguish "connected but zero rows" from a missing file.
    events.to_csv(RAW/"events.csv",index=False)
    events[["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","SOURCE","SOURCE_URL","CONFIDENCE"]].to_csv(RAW/"geopolitical_events.csv",index=False)
    manifest["event_collection"]={"status":"AVAILABLE" if len(events) else "BLOCKED","rows":len(events),"collection_metrics":event_metrics,
      "window_start":event_start.isoformat(),"window_end":end.isoformat(),
      "date_min":events.EVENT_DATE.min() if len(events) else None,"date_max":events.EVENT_DATE.max() if len(events) else None,
      "source":"GDELT DOC 2.0 API plus direct public RSS feeds from Reuters, AP News, BBC, Al Jazeera, Bloomberg; trusted-domain and relevance filtering applied","failures":failures,
      "trusted_domains":sorted(TRUSTED_NEWS_DOMAINS),
      "quality_filter":"Only explicit market-relevant title keywords plus trusted publisher domain; broad-query false positives are excluded.",
      "warning":"PUBLISHED_AT/EVENT_DATE are publication-time proxies, not verified occurrence timestamps; this remains a media-publication event study, not causal identification."}
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
    p0_series_ok=all(any(x.get("series")==name and x.get("status") in ("AVAILABLE","AVAILABLE_SECONDARY") for x in manifest["market_series"])
      for name in ("NIFTY 50","NIFTY IT","NIFTY BANK","INDIA VIX","BRENT CRUDE FRONT MONTH","USD INR"))
    manifest["historical_research_window"]={"requested_start":start.isoformat(),"requested_end":end.isoformat(),
      "series_with_rows":sum(bool(x.get("rows")) for x in manifest["market_series"]),
      "series_coverage":{x["series"]:{"status":x["status"],"date_min":x.get("date_min"),"date_max":x.get("date_max"),"rows":x.get("rows",0)} for x in manifest["market_series"]},
      "boundary":"Requested 2006 onward; each series may start later. A complete 20-year study is not claimed unless panel coverage supports it."}
    manifest["p0_coverage"]={"required_series":["NIFTY 50","NIFTY IT","NIFTY BANK","INDIA VIX","BRENT CRUDE FRONT MONTH","USD INR"],
      "required_series_available":p0_series_ok,"trusted_event_rows":len(events),
      "fpi_dii_status":"UNKNOWN/BLOCKED unless official source returns mapped rows",
      "corporate_events_status":"UNKNOWN/BLOCKED unless official source returns mapped rows"}
    manifest["operational_status"]="PASS_WITH_GAPS" if not panel.empty and p0_series_ok else "PASS_WITH_CRITICAL_DATA_GAPS"
    manifest["research_status"]="READY_FOR_EXPLORATORY_EVENT_STUDY" if len(events) else "BLOCKED_NO_VALID_EVENTS"
    manifest["status"]=manifest["operational_status"]
    (OUT/"p0_collection_manifest.json").write_text(json.dumps(manifest,indent=2))
    print(json.dumps({"operational_status":manifest["operational_status"],"research_status":manifest["research_status"],"status":manifest["status"],"window_start":str(start),"window_end":str(end),
      "market_panel_rows":len(panel),"market_panel_series":int(panel.SERIES.nunique()) if not panel.empty else 0,
      "events_rows":len(events),"event_window_start":event_start.isoformat(),"event_collection_metrics":event_metrics,"total_source_failures":len(failures),
      "official_nse_attempts":manifest["official_nse_attempts"]},indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
