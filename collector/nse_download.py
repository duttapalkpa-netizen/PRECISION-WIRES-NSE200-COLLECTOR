#!/usr/bin/env python3
from __future__ import annotations
import argparse, time
from datetime import date, timedelta
from pathlib import Path
import requests

BASE = "https://archives.nseindia.com/products/content/sec_bhavdata_full_{dt}.csv"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
    "Accept": "text/csv,text/plain,*/*",
    "Referer": "https://www.nseindia.com/",
    "Accept-Language": "en-US,en;q=0.9",
}

def is_valid_eq_csv(path: Path) -> bool:
    try:
        import pandas as pd
        df = pd.read_csv(path, nrows=20)
        cols = {str(c).strip().upper() for c in df.columns}
        return {"SYMBOL", "SERIES", "CLOSE_PRICE"}.issubset(cols) and df["SERIES"].astype(str).str.strip().eq("EQ").any()
    except Exception:
        return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions", type=int, default=200)
    ap.add_argument("--lookback-days", type=int, default=340)
    ap.add_argument("--out", default="data/raw")
    args = ap.parse_args()
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    s = requests.Session(); s.headers.update(HEADERS)
    try: s.get("https://www.nseindia.com/", timeout=20)
    except Exception: pass
    today = date.today()
    valid = []
    for offset in range(args.lookback_days + 1):
        if len(valid) >= args.sessions: break
        d = today - timedelta(days=offset)
        if d.weekday() >= 5: continue
        stamp = d.strftime("%d%m%Y")
        path = out / f"sec_bhavdata_full_{stamp}.csv"
        if path.exists() and is_valid_eq_csv(path):
            valid.append(d); continue
        ok = False
        for attempt in range(3):
            try:
                r = s.get(BASE.format(dt=stamp), timeout=30)
                if r.status_code == 200 and len(r.content) > 1000:
                    path.write_bytes(r.content)
                    if is_valid_eq_csv(path): ok = True; break
                if path.exists() and not ok: path.unlink()
            except Exception as e: print(f"WARN {stamp}: {e}")
            time.sleep(1.5 * (attempt + 1))
        print(f"{'OK' if ok else 'MISS'} {stamp} ({len(valid)+int(ok)}/{args.sessions})")
        if ok: valid.append(d)
    valid.sort()
    (out / "sessions.txt").write_text("\n".join(d.isoformat() for d in valid) + "\n")
    print(f"VALID_SESSIONS={len(valid)}")
    if len(valid) < args.sessions: raise SystemExit(f"Need {args.sessions} sessions; got {len(valid)}")

if __name__ == "__main__": main()
