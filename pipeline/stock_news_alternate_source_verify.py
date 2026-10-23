#!/usr/bin/env python3
"""Fast, artifact-only independent verification of alternate publisher leads.

Never changes the original news ledger or promotes original rows. It verifies
candidate article URLs and writes a separate report for human/audit review.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json, re
import pandas as pd
import requests

INPUT = Path("artifact/outputs/news_24h/stock_news_alternate_source_candidates.csv")
OUT = Path("outputs/news_24h/alternate_source_verification_report.json")
CSV_OUT = Path("outputs/news_24h/alternate_source_verification_results.csv")
UA = "Mozilla/5.0 (compatible; PRECISION-WIRES-audit/1.0)"
STOP = {"the","and","for","with","from","after","before","into","over","says","said","its","this","that","will","has","have","are","was","were","about","india","indian","stock","stocks","share","shares","nse","bse","limited","ltd","company","market"}

class Meta(HTMLParser):
    def __init__(self):
        super().__init__(); self.in_title=False; self.title=[]; self.meta=[]
    def handle_starttag(self, tag, attrs):
        a={str(k).lower():str(v or "") for k,v in attrs}
        if tag.lower()=="title": self.in_title=True
        if tag.lower()=="meta" and (a.get("property","").lower() in {"og:title","twitter:title"} or a.get("name","").lower() in {"og:title","twitter:title"}) and a.get("content"):
            self.meta.append(a["content"])
    def handle_endtag(self, tag):
        if tag.lower()=="title": self.in_title=False
    def handle_data(self, data):
        if self.in_title and data.strip(): self.title.append(data.strip())
    def best(self): return (self.meta[0] if self.meta else " ".join(self.title)).strip()
    def published_at(self): return self.published[0].strip() if self.published else ""

def toks(s):
    return {x for x in re.findall(r"[a-z0-9]+",str(s or "").lower()) if len(x)>2 and x not in STOP}

def verify(row):
    url=str(row.get("ALTERNATE_ARTICLE_URL","")).strip()
    headline=str(row.get("ALTERNATE_HEADLINE","")).strip()
    if urlparse(url).scheme not in {"http","https"} or not urlparse(url).hostname:
        return {**row.to_dict(),"VERIFICATION_STATUS":"UNVERIFIED","REASON":"INVALID_URL","RESOLVED_URL":""}
    resolved=url
    try:
        host=(urlparse(url).hostname or "").lower()
        if host=="news.google.com" or host.endswith(".news.google.com"):
            from googlenewsdecoder import gnewsdecoder
            decoded=gnewsdecoder(url,interval=1,timeout=15.0)
            if not isinstance(decoded,dict) or not decoded.get("success") or not decoded.get("decoded_url"):
                raise ValueError("GOOGLE_NEWS_URL_NOT_DECODED")
            resolved=str(decoded["decoded_url"]).strip()
            parts=urlparse(resolved)
            if parts.scheme not in {"http","https"} or not parts.hostname or parts.hostname.lower().endswith("google.com"):
                raise ValueError("INVALID_PUBLISHER_URL")
        response=requests.get(resolved,timeout=(5,12),allow_redirects=True,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml"})
        response.raise_for_status()
        final=urlparse(response.url)
        if not final.hostname or final.hostname.lower()=="google.com" or final.hostname.lower().endswith(".google.com"):
            raise ValueError("NOT_PUBLISHER_URL")
        if "html" not in response.headers.get("Content-Type","").lower():
            raise ValueError("PUBLISHER_RESPONSE_NOT_HTML")
        parser=Meta(); parser.feed(response.text[:300000]); title=parser.best(); publisher_published_at=parser.published_at()\n        # Also inspect JSON-LD datePublished/dateCreated when present.\n        if not publisher_published_at:\n            match=re.search(r'"datePublished"\\s*:\\s*"([^"]+)"', response.text[:500000], re.I)\n            if match: publisher_published_at=match.group(1)
        ht,pt=toks(headline),toks(title)
        overlap=(len(ht & pt)/len(ht)) if ht else 0.0
        if len(ht)<3 or not title or overlap<0.5:
            raise ValueError(f"TITLE_MISMATCH:overlap={overlap:.3f}")
        return {**row.to_dict(),"VERIFICATION_STATUS":"VERIFIED","REASON":"","RESOLVED_URL":response.url,"PUBLISHER_PAGE_TITLE":title,"PUBLISHER_PUBLISHED_AT":publisher_published_at,"HEADLINE_TOKEN_OVERLAP":round(overlap,3)}
    except Exception as exc:
        return {**row.to_dict(),"VERIFICATION_STATUS":"UNVERIFIED","REASON":f"{type(exc).__name__}:{str(exc)[:180]}","RESOLVED_URL":resolved}

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    if not INPUT.is_file():
        report={"status":"BLOCKED_MISSING_ALTERNATE_CANDIDATE_ARTIFACT","input":str(INPUT),"checked_rows":0,"verified_rows":0,"unverified_rows":0,"policy":"No original news rows are modified; candidate leads cannot auto-promote research rows."}
        OUT.write_text(json.dumps(report,indent=2),encoding="utf-8"); print(json.dumps(report,sort_keys=True)); raise SystemExit(2)
    df=pd.read_csv(INPUT,dtype=str).fillna("")
    needed={"ALTERNATE_HEADLINE","ALTERNATE_ARTICLE_URL","ALTERNATE_PUBLISHER","SYMBOL","CUT_OFF"}
    if not needed.issubset(df.columns):
        report={"status":"BLOCKED_BAD_ALTERNATE_CANDIDATE_SCHEMA","missing_columns":sorted(needed-set(df.columns)),"checked_rows":0}
        OUT.write_text(json.dumps(report,indent=2),encoding="utf-8"); print(json.dumps(report,sort_keys=True)); raise SystemExit(2)
    rows=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures=[pool.submit(verify,row) for _,row in df.iterrows()]
        for f in as_completed(futures): rows.append(f.result())
    result=pd.DataFrame(rows)
    result.to_csv(CSV_OUT,index=False)
    verified=int(result.get("VERIFICATION_STATUS",pd.Series(dtype=str)).eq("VERIFIED").sum())
    report={"status":"PASS_ALTERNATE_LEADS_VERIFIED" if verified else "NO_ALTERNATE_LEADS_VERIFIED","checked_rows":len(result),"verified_rows":verified,"unverified_rows":len(result)-verified,"results_csv":str(CSV_OUT),"verification_rule":"Decoded URL resolves to non-Google publisher HTML, HTTP success, page title overlap >= 0.50; publication timestamp extracted from publisher meta/time/JSON-LD when exposed; max 4 concurrent requests.","policy":"This report verifies candidate leads only. It does not alter stock_news_events.csv or promote any original row to VERIFIED. Original row promotion requires a separate audited join to the matching symbol, cutoff, headline and publication timestamp.","results":result[[c for c in ["SYMBOL","CUT_OFF","ALTERNATE_PUBLISHER","ALTERNATE_ARTICLE_URL","VERIFICATION_STATUS","REASON","RESOLVED_URL","PUBLISHER_PAGE_TITLE","PUBLISHER_PUBLISHED_AT","HEADLINE_TOKEN_OVERLAP"] if c in result.columns]].to_dict("records")}
    OUT.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    print("ALTERNATE_SOURCE_VERIFICATION="+json.dumps(report,sort_keys=True,ensure_ascii=False))
if __name__=="__main__": main()
