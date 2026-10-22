#!/usr/bin/env python3
"""Discover alternate publisher URLs for unverified 403 news rows.

Discovery leads are never promoted to VERIFIED here. The existing verifier must
independently fetch the candidate page and match its title before promotion.
"""
from datetime import timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlencode
import json
import re
import time
import xml.etree.ElementTree as ET

import pandas as pd
import requests

NEWS = Path("data/raw/stock_news_events.csv")
OUT = Path("outputs/news_24h/stock_news_alternate_source_candidates.csv")
REPORT = Path("outputs/news_24h/stock_news_alternate_source_discovery.json")
RSS = "https://news.google.com/rss/search"
UA = "Mozilla/5.0 (compatible; PRECISION-WIRES-audit/1.0)"
STOP = {"the","and","for","with","from","after","before","into","over","says","said",
        "its","this","that","will","has","have","are","was","were","about","india",
        "indian","stock","stocks","share","shares","nse","bse","limited","ltd","company","market"}

def tokens(value):
    return {x for x in re.findall(r"[a-z0-9]+", str(value or "").lower())
            if len(x) > 2 and x not in STOP}

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if not NEWS.exists():
        report = {"status":"BLOCKED_MISSING_NEWS_FILE","input":str(NEWS),"candidate_rows":0}
        REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print("ALTERNATE_SOURCE_DISCOVERY=" + json.dumps(report, sort_keys=True))
        return 0
    df = pd.read_csv(NEWS, dtype=str).fillna("")
    required = {"CUT_OFF","SYMBOL","PUBLISHED_AT","PUBLISHER","HEADLINE","CANONICAL_URL","VERIFICATION_STATUS"}
    if not required.issubset(df.columns):
        report = {"status":"BLOCKED_BAD_NEWS_SCHEMA","missing_columns":sorted(required-set(df.columns)),"candidate_rows":0}
        REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print("ALTERNATE_SOURCE_DISCOVERY=" + json.dumps(report, sort_keys=True))
        return 0
    pending = df[df["VERIFICATION_STATUS"].str.upper().ne("VERIFIED")].copy()
    rows, errors = [], []
    with requests.Session() as session:
        session.headers.update({"User-Agent":UA,"Accept":"application/rss+xml, application/xml, text/xml"})
        for row_index, row in pending.iterrows():
            headline = row["HEADLINE"].strip()
            symbol = row["SYMBOL"].strip().upper()
            if not headline or not symbol:
                continue
            # Quote the collected headline and add the symbol as a disambiguator.
            query = f'"{headline}" "{symbol}"'
            params = {"q":query,"hl":"en-IN","gl":"IN","ceid":"IN:en"}
            try:
                response = session.get(RSS, params=params, timeout=(10,25))
                response.raise_for_status()
                root = ET.fromstring(response.content)
                channel = root.find("channel")
                if channel is None:
                    raise ValueError("RSS missing channel")
                for item in channel.findall("item"):
                    alt_title = (item.findtext("title") or "").strip()
                    alt_url = (item.findtext("link") or "").strip()
                    raw_date = (item.findtext("pubDate") or "").strip()
                    source_el = item.find("source")
                    alt_publisher = (source_el.text or "").strip() if source_el is not None else ""
                    source_url = source_el.attrib.get("url","") if source_el is not None else ""
                    if not alt_title or not alt_url.startswith(("http://","https://")):
                        continue
                    try:
                        published = parsedate_to_datetime(raw_date).isoformat()
                    except Exception:
                        published = ""
                    a, b = tokens(headline), tokens(alt_title)
                    overlap = len(a & b) / len(a) if a else 0.0
                    rows.append({
                        "SOURCE_ROW_INDEX":int(row_index),"CUT_OFF":row["CUT_OFF"],"SYMBOL":symbol,
                        "ORIGINAL_PUBLISHED_AT":row["PUBLISHED_AT"],"ORIGINAL_PUBLISHER":row["PUBLISHER"],
                        "ORIGINAL_HEADLINE":headline,"ORIGINAL_URL":row["CANONICAL_URL"],
                        "ALTERNATE_HEADLINE":alt_title,"ALTERNATE_PUBLISHER":alt_publisher,
                        "ALTERNATE_SOURCE_URL":source_url,"ALTERNATE_ARTICLE_URL":alt_url,
                        "ALTERNATE_PUBLISHED_AT":published,"HEADLINE_TOKEN_OVERLAP":round(overlap,4),
                        "DISCOVERY_STATUS":"LEAD_ONLY_REQUIRES_INDEPENDENT_VERIFICATION"
                    })
                time.sleep(1.0)
            except Exception as exc:
                errors.append({"row":int(row_index),"symbol":symbol,"reason":f"{type(exc).__name__}:{str(exc)[:160]}"})
    columns = ["SOURCE_ROW_INDEX","CUT_OFF","SYMBOL","ORIGINAL_PUBLISHED_AT","ORIGINAL_PUBLISHER","ORIGINAL_HEADLINE","ORIGINAL_URL","ALTERNATE_HEADLINE","ALTERNATE_PUBLISHER","ALTERNATE_SOURCE_URL","ALTERNATE_ARTICLE_URL","ALTERNATE_PUBLISHED_AT","HEADLINE_TOKEN_OVERLAP","DISCOVERY_STATUS"]
    result = pd.DataFrame(rows, columns=columns)
    if not result.empty:
        result = result.sort_values(["SOURCE_ROW_INDEX","HEADLINE_TOKEN_OVERLAP"], ascending=[True,False])
    result.to_csv(OUT,index=False)
    report = {
        "status":"DISCOVERY_COMPLETE" if not errors else "DISCOVERY_COMPLETE_WITH_ERRORS",
        "unverified_input_rows":int(len(pending)),"alternate_candidate_rows":int(len(result)),
        "rows_with_candidates":int(result["SOURCE_ROW_INDEX"].nunique()) if not result.empty else 0,
        "error_count":len(errors),"error_samples":errors[:10],"output":str(OUT),
        "policy":"Candidates are discovery leads only; no row is promoted to VERIFIED by this script."
    }
    REPORT.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("ALTERNATE_SOURCE_DISCOVERY="+json.dumps(report,sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
