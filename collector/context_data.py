#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import json, requests, feedparser

ROOT=Path(".")
OUT=ROOT/"data/context"
OUT.mkdir(parents=True, exist_ok=True)

H={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
    "Accept":"application/json,text/plain,*/*",
    "Referer":"https://www.nseindia.com/",
}

def num(v):
    try:
        return float(str(v).replace(",","").strip())
    except Exception:
        return None

def main():
    s=requests.Session()
    s.headers.update(H)
    try:
        s.get("https://www.nseindia.com/", timeout=(10,20))
    except Exception:
        pass

    out={"generated_at":datetime.now(timezone.utc).isoformat(),"sources":{}}

    # NSE FII/FPI + DII. The API returns separate category rows; never infer
    # FII/DII from row position because the order can change.
    try:
        r=s.get("https://www.nseindia.com/api/fiidiiTradeReact", timeout=(10,20))
        r.raise_for_status()
        raw=r.json()
        rows=raw if isinstance(raw,list) else raw.get("data",[])
        norm=[]
        for x in rows[:60]:
            category=str(x.get("category") or x.get("Category") or "").strip().upper()
            net=num(x.get("netValue") if x.get("netValue") is not None else x.get("net_value"))
            buy=num(x.get("buyValue") if x.get("buyValue") is not None else x.get("buy_value"))
            sell=num(x.get("sellValue") if x.get("sellValue") is not None else x.get("sell_value"))
            if category in {"FII/FPI","FII","FPI"}:
                group="FII_FPI"
            elif category=="DII":
                group="DII"
            else:
                group=category or "UNKNOWN"
            norm.append({
                "category":category,
                "group":group,
                "date":x.get("date") or x.get("Date"),
                "buy_value":buy,
                "sell_value":sell,
                "net_value":net
            })
        out["fii_dii"]=norm
        out["sources"]["fii_dii"]="NSE /api/fiidiiTradeReact (category-normalized)"
        out["fii_dii_coverage"]={
            "rows":len(norm),
            "fii_rows":sum(x["group"]=="FII_FPI" for x in norm),
            "dii_rows":sum(x["group"]=="DII" for x in norm),
            "fii_dates":len({x["date"] for x in norm if x["group"]=="FII_FPI" and x["date"]}),
            "dii_dates":len({x["date"] for x in norm if x["group"]=="DII" and x["date"]})
        }
    except Exception as e:
        out["fii_dii_error"]=type(e).__name__

    # NSE market status
    try:
        r=s.get("https://www.nseindia.com/api/marketStatus", timeout=(10,20))
        r.raise_for_status()
        out["market_status"]=r.json()
        out["sources"]["market_status"]="NSE /api/marketStatus"
    except Exception as e:
        out["market_status_error"]=type(e).__name__

    # NSE indices / VIX
    try:
        r=s.get("https://www.nseindia.com/api/allIndices", timeout=(10,20))
        r.raise_for_status()
        data=r.json().get("data",[])
        keep=[]
        for x in data:
            n=str(x.get("index",""))
            if n in {"NIFTY 50","INDIA VIX","NIFTY BANK","NIFTY MIDCAP 100"}:
                keep.append({k:x.get(k) for k in ["index","last","variation","percentChange","previousClose"]})
        out["indices"]=keep
        out["sources"]["indices"]="NSE /api/allIndices"
    except Exception as e:
        out["indices_error"]=type(e).__name__

    # Geo/news context: GDELT DOC is primary; GDELT Context and Google News RSS
    # are fallbacks. This is a coverage signal, not proof that an event occurred.
    query='(India geopolitical OR India sanctions OR Iran OR "Russia Ukraine" OR "China Taiwan" OR "trade war")'
    articles=[]
    geo_provider=None
    geo_errors=[]

    try:
        r=requests.get(
            "https://api.gdeltproject.org/api/v2/doc/doc",
            params={"query":query,"mode":"artlist","format":"json","maxrecords":75,"sort":"datedesc","timespan":"24h"},
            timeout=(10,25)
        )
        r.raise_for_status()
        j=r.json()
        articles=j.get("articles",[])
        if isinstance(articles,list):
            geo_provider="GDELT_DOC_24H"
    except Exception as e:
        geo_errors.append("GDELT_DOC_"+type(e).__name__)

    if not articles:
        try:
            r=requests.get(
                "https://api.gdeltproject.org/api/v2/context/context",
                params={"query":query,"mode":"artlist","format":"json","maxrecords":75,"timespan":"24h"},
                timeout=(10,25)
            )
            r.raise_for_status()
            j=r.json()
            articles=j.get("articles",[])
            if isinstance(articles,list):
                geo_provider="GDELT_CONTEXT_24H"
        except Exception as e:
            geo_errors.append("GDELT_CONTEXT_"+type(e).__name__)

    if not articles:
        try:
            rss=requests.get(
                "https://news.google.com/rss/search",
                params={"q":"India geopolitical OR sanctions OR Iran OR Russia Ukraine OR China Taiwan","hl":"en-IN","gl":"IN","ceid":"IN:en"},
                headers={"User-Agent":H["User-Agent"]},
                timeout=(10,20)
            )
            rss.raise_for_status()
            feed=feedparser.parse(rss.content)
            articles=[{"title":e.get("title",""),"url":e.get("link",""),"seendate":e.get("published","")} for e in feed.entries[:75]]
            geo_provider="GOOGLE_NEWS_RSS"
        except Exception as e:
            geo_errors.append("GOOGLE_NEWS_RSS_"+type(e).__name__)

    if articles:
        out["geo_news"]={
            "provider":geo_provider,
            "article_count":len(articles),
            "latest_titles":[str(a.get("title",""))[:220] for a in articles[:15]],
            "verified_context_source":True,
            "errors":geo_errors
        }
        out["sources"]["geo_news"]=geo_provider
    else:
        out["geo_news_error"]=";".join(geo_errors) or "NO_RESULTS"

    (OUT/"market_context.json").write_text(json.dumps(out,indent=2,default=str), encoding="utf-8")
    print(json.dumps({
        "fii_rows":len(out.get("fii_dii",[])),
        "fii_dates":out.get("fii_dii_coverage",{}).get("fii_dates"),
        "dii_dates":out.get("fii_dii_coverage",{}).get("dii_dates"),
        "geo_provider":out.get("geo_news",{}).get("provider"),
        "geo_articles":out.get("geo_news",{}).get("article_count"),
        "status":"OK"
    },indent=2))

if __name__=="__main__":
    main()
