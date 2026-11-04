#!/usr/bin/env python3
"""Backfill the 57 real NSE sessions immediately preceding the existing cache.
Downloads official Full Bhavcopy + Security Deliverable CSVs; no synthetic rows.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
import requests

BASES = [
    "https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_{stamp}.csv",
    "https://archives.nseindia.com/products/content/sec_bhavdata_full_{stamp}.csv",
]
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
    "Accept": "text/csv,application/octet-stream,*/*",
    "Referer": "https://www.nseindia.com/",
}
def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def valid_csv(raw: bytes, expected: date):
    if len(raw) < 1000 or raw.lstrip().startswith(b"<"):
        return None, "empty_or_html"
    try:
        text = raw.decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
        if not rows:
            return None, "no_rows"
        cols = {str(k).strip().upper(): k for k in (reader.fieldnames or [])}
        aliases = {
            "SYMBOL": ["SYMBOL"], "SERIES": ["SERIES"],
            "DATE": ["DATE1", "DATE", "TRADE_DATE"],
            "CLOSE": ["CLOSE_PRICE", "CLOSEPRICE", "CLSPRIC"],
            "DELIV_QTY": ["DELIV_QTY", "DELIVERY_QTY", "DELIVQTY"],
            "DELIV_PER": ["DELIV_PER", "DELIVERY_PER", "DELIVPER"],
        }
        found = {k: next((cols[a] for a in v if a in cols), None) for k,v in aliases.items()}
        if any(found[k] is None for k in aliases):
            return None, "required_columns_missing"
        eq = [r for r in rows if str(r.get(found["SERIES"], "")).strip().upper() == "EQ"]
        if not eq:
            return None, "no_EQ_rows"
        dates = {str(r.get(found["DATE"], "")).strip() for r in eq if str(r.get(found["DATE"], "")).strip()}
        # NSE historical file date format is DD-MMM-YYYY or DD-MM-YYYY.
        parsed = set()
        for v in dates:
            for fmt in ("%d-%b-%Y", "%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d"):
                try:
                    parsed.add(datetime.strptime(v, fmt).date()); break
                except ValueError:
                    pass
        if parsed != {expected}:
            return None, "date_mismatch:" + ",".join(sorted(x.isoformat() for x in parsed))
        close = [r.get(found["CLOSE"]) for r in eq]
        dq = [r.get(found["DELIV_QTY"]) for r in eq]
        dp = [r.get(found["DELIV_PER"]) for r in eq]
        def numeric(x):
            try: return float(str(x).replace(",", "").strip())
            except (ValueError, TypeError): return None
        if sum(numeric(x) is not None for x in close) < max(10, int(len(eq)*0.8)):
            return None, "close_coverage_below_80pct"
        if sum(numeric(x) is not None for x in dq) < max(10, int(len(eq)*0.8)):
            return None, "delivery_qty_coverage_below_80pct"
        if sum(numeric(x) is not None for x in dp) < max(10, int(len(eq)*0.8)):
            return None, "delivery_pct_coverage_below_80pct"
        return {"rows_total":len(rows), "eq_rows":len(eq),
                "delivery_qty_coverage":sum(numeric(x) is not None for x in dq)/len(eq),
                "delivery_pct_coverage":sum(numeric(x) is not None for x in dp)/len(eq)}, "ok"
    except Exception as e:
        return None, "parse_error:" + type(e).__name__

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--before", required=True, help="exclusive first cached session YYYY-MM-DD")
    ap.add_argument("--sessions", type=int, default=57)
    ap.add_argument("--lookback-days", type=int, default=500)
    ap.add_argument("--out", default="data/raw/nse_57_backfill")
    args=ap.parse_args()
    cutoff=date.fromisoformat(args.before.strip())
    out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    s=requests.Session(); s.headers.update(HEADERS)
    for home in ("https://www.nseindia.com/", "https://www.nseindia.com/all-reports"):
        try: s.get(home, timeout=(10,20))
        except requests.RequestException: pass
    records=[]; misses=[]
    d=cutoff-timedelta(days=1)
    for _ in range(args.lookback_days):
        if len(records)>=args.sessions: break
        if d.weekday()<5:
            stamp=d.strftime("%d%m%Y"); found=False
            for url_template in BASES:
                url=url_template.format(stamp=stamp)
                try:
                    r=s.get(url,timeout=(10,30))
                    retrieved=datetime.now(timezone.utc).isoformat()
                    if r.status_code != 200:
                        misses.append({"date":d.isoformat(),"url":url,"status":r.status_code}); continue
                    qa,reason=valid_csv(r.content,d)
                    if not qa:
                        misses.append({"date":d.isoformat(),"url":url,"status":r.status_code,"reason":reason}); continue
                    name=f"sec_bhavdata_full_{stamp}.csv"; path=out/name
                    path.write_bytes(r.content)
                    records.append({
                        "trading_date":d.isoformat(),"file":name,"source_url":r.url,
                        "retrieved_at_utc":retrieved,"http_status":r.status_code,
                        "content_type":r.headers.get("Content-Type"),
                        "last_modified":r.headers.get("Last-Modified"),
                        "bytes":len(r.content),"sha256":sha256(r.content),**qa})
                    found=True; break
                except requests.RequestException as e:
                    misses.append({"date":d.isoformat(),"url":url,"reason":type(e).__name__})
            if found: print(f"VERIFIED {d.isoformat()} {len(records)}/{args.sessions}",flush=True)
        d-=timedelta(days=1); time.sleep(0.25)
    records.sort(key=lambda x:x["trading_date"])
    dates=[x["trading_date"] for x in records]
    duplicates=sorted({x for x in dates if dates.count(x)>1})
    manifest={"source":"NSE official Full Bhavcopy and Security Deliverable archives",
      "cutoff_exclusive":args.before,"requested_sessions":args.sessions,
      "verified_sessions":len(records),"first_session":dates[0] if dates else None,
      "last_session":dates[-1] if dates else None,"duplicate_dates":duplicates,
      "missing_count":args.sessions-len(records),"files":records,"rejected_attempts":misses}
    (out/"NSE_57_SHA256_MANIFEST.json").write_text(json.dumps(manifest,indent=2))
    with (out/"NSE_57_RECONCILIATION.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["trading_date","file","sha256","bytes","rows_total","eq_rows","delivery_qty_coverage","delivery_pct_coverage","source_url","retrieved_at_utc"])
        w.writeheader()
        for x in records: w.writerow({k:x.get(k) for k in w.fieldnames})
    (out/"NSE_57_QA_REPORT.json").write_text(json.dumps({
      "status":"PASS" if len(records)==args.sessions and not duplicates else "BLOCKED",
      "verified_sessions":len(records),"required_sessions":args.sessions,
      "duplicates":duplicates,"missing_sessions":args.sessions-len(records),
      "delivery_coverage_minimum":0.8,
      "rolling_validation_authorized":len(records)==args.sessions and not duplicates},indent=2))
    print(f"FINAL verified={len(records)}/{args.sessions} duplicates={len(duplicates)}",flush=True)
    if len(records)!=args.sessions or duplicates: raise SystemExit(2)
if __name__=="__main__": main()
