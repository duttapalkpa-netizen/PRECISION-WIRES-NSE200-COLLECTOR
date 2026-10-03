#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import json, re, requests

ROOT=Path("."); OUT=ROOT/"data/context"; OUT.mkdir(parents=True,exist_ok=True)
H={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36","Accept":"application/json,text/plain,*/*","Referer":"https://www.nseindia.com/"}

def main():
    s=requests.Session(); s.headers.update(H)
    try: s.get("https://www.nseindia.com/",timeout=(10,20))
    except Exception: pass
    out={"generated_at":datetime.now(timezone.utc).isoformat(),"sources":{}}
    # NSE FII/DII
    try:
        r=s.get("https://www.nseindia.com/api/fiidiiTradeReact",timeout=(10,20)); r.raise_for_status()
        raw=r.json(); rows=raw if isinstance(raw,list) else raw.get("data",[])
        norm=[]
        for x in rows[:30]:
            def num(*ks):
                for k in ks:
                    if k in x:
                        try:return float(str(x[k]).replace(",",""))
                        except: pass
                return None
            norm.append({"date":x.get("date"),"fii_net":num("fiiNet","fiinet","netValue"),"dii_net":num("diiNet","diinet")})
        out["fii_dii"]=norm; out["sources"]["fii_dii"]="NSE /api/fiidiiTradeReact"
    except Exception as e: out["fii_dii_error"]=type(e).__name__
    # NSE market status
    try:
        r=s.get("https://www.nseindia.com/api/marketStatus",timeout=(10,20)); r.raise_for_status()
        out["market_status"]=r.json(); out["sources"]["market_status"]="NSE /api/marketStatus"
    except Exception as e: out["market_status_error"]=type(e).__name__
    # NSE indices / VIX context
    try:
        r=s.get("https://www.nseindia.com/api/allIndices",timeout=(10,20)); r.raise_for_status()
        data=r.json().get("data",[])
        keep=[]
        for x in data:
            n=str(x.get("index",""))
            if n in {"NIFTY 50","INDIA VIX","NIFTY BANK","NIFTY MIDCAP 100"}:
                keep.append({k:x.get(k) for k in ["index","last","variation","percentChange","previousClose"]})
        out["indices"]=keep; out["sources"]["indices"]="NSE /api/allIndices"
    except Exception as e: out["indices_error"]=type(e).__name__
    # Transparent geopolitical news context: signal is a news-count modifier, never a claim about an event.
    try:
        q='https://api.gdeltproject.org/api/v2/doc/doc?query=(India%20geopolitical%20OR%20India%20sanctions%20OR%20Iran%20OR%20Russia%20Ukraine%20OR%20China%20Taiwan)&mode=ArtList&format=json&maxrecords=50&sort=datedesc'
        r=requests.get(q,timeout=(10,20)); r.raise_for_status(); j=r.json()
        arts=j.get("articles",[])
        out["geo_news"]={"article_count":len(arts),"latest_titles":[str(a.get("title",""))[:180] for a in arts[:10]]}
        out["sources"]["geo_news"]="GDELT DOC API keyword news context"
    except Exception as e: out["geo_news_error"]=type(e).__name__
    (OUT/"market_context.json").write_text(json.dumps(out,indent=2,default=str))
    print(json.dumps({"fii_dii":len(out.get("fii_dii",[])),"geo_articles":out.get("geo_news",{}).get("article_count"),"status":"OK"},indent=2))

if __name__=="__main__": main()
