#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, io, json, time, zipfile
from datetime import date, timedelta
from pathlib import Path
import requests

# NSE discontinued the old CM bhavcopy/common-bhavcopy formats from 08-Jul-2024.
# Prefer the current CM-UDiFF Common Bhavcopy Final archive; keep the legacy
# Full Bhavcopy endpoint only as a fallback because the latter is still exposed
# on NSE's reports/archive pages.
UDIFF = "https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_{yyyymmdd}_F_0000.csv.zip"
LEGACY = "https://archives.nseindia.com/products/content/sec_bhavdata_full_{ddmmyyyy}.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
    "Connection": "keep-alive",
}

def looks_blocked(content: bytes) -> bool:
    head = content[:500].lstrip().lower()
    return head.startswith(b"<") or b"access denied" in head or b"akamai" in head

def normalize_udiff(raw: bytes, stamp: str, out: Path) -> bool:
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            names = [n for n in z.namelist() if n.lower().endswith(".csv")]
            if not names:
                return False
            with z.open(names[0]) as f:
                text = io.TextIOWrapper(f, encoding="utf-8-sig", errors="replace").read()
        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
        if not rows:
            return False
        fields = {x.strip().upper() for x in (reader.fieldnames or [])}
        # UDiFF names vary slightly; map the fields we need into the existing schema.
        def pick(row, *names):
            upper = {str(k).strip().upper(): v for k, v in row.items()}
            for n in names:
                if n in upper:
                    return upper[n]
            return ""

        sample = rows[:20]
        has_symbol = any(pick(r, "TCKR_SYMB", "SYMBOL") for r in sample)
        has_close = any(pick(r, "CLSPRIC", "CLOSE_PRICE", "CLOSE") for r in sample)
        if not (has_symbol and has_close):
            return False

        out_rows = []
        for r in rows:
            sym = pick(r, "TCKR_SYMB", "SYMBOL").strip()
            series = pick(r, "SCTY_SERIES", "SERIES").strip()
            if not sym or (series and series != "EQ"):
                continue
            out_rows.append({
                "SYMBOL": sym,
                "SERIES": "EQ",
                "DATE1": pick(r, "TRADG_DATE", "DATE1", "DATE"),
                "PREV_CLOSE": pick(r, "PREV_CL_PR", "PREV_CLOSE"),
                "OPEN_PRICE": pick(r, "OPEN_PRICE", "OPEN"),
                "HIGH_PRICE": pick(r, "HIGH_PRICE", "HIGH"),
                "LOW_PRICE": pick(r, "LOW_PRICE", "LOW"),
                "CLOSE_PRICE": pick(r, "CLSPRIC", "CLOSE_PRICE", "CLOSE"),
                "TTL_TRD_QNTY": pick(r, "TTLT_TRAD_QTY", "TTL_TRD_QNTY", "TOTTRDQTY"),
                "TURNOVER_LACS": pick(r, "TRAD_VAL", "TURNOVER_LACS"),
                "DELIV_QTY": pick(r, "DELIV_QTY", "DELIV_QTY"),
                "DELIV_PER": pick(r, "DELIV_PER", "DELIV_PER"),
            })
        if not out_rows:
            return False
        # Preserve the collector's established filename/schema so downstream stages stay unchanged.
        target = out / f"sec_bhavdata_full_{stamp}.csv"
        import pandas as pd
        df = pd.DataFrame(out_rows)
        # Ensure a useful date even when the UDiFF date field is formatted differently.
        df["DATE1"] = df["DATE1"].astype(str).replace({"": stamp})
        df.to_csv(target, index=False)
        return True
    except Exception:
        return False

def validate_legacy(content: bytes) -> bool:
    if looks_blocked(content) or len(content) < 1000:
        return False
    try:
        import pandas as pd
        df = pd.read_csv(io.BytesIO(content), nrows=20)
        cols = {str(c).strip().upper() for c in df.columns}
        return {"SYMBOL", "SERIES", "CLOSE_PRICE"}.issubset(cols) and df["SERIES"].astype(str).str.strip().eq("EQ").any()
    except Exception:
        return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions", type=int, default=200)
    ap.add_argument("--lookback-days", type=int, default=500)
    ap.add_argument("--out", default="data/raw")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    s.headers.update(HEADERS)

    # Establish NSE cookies before archive requests.
    for home in ("https://www.nseindia.com/", "https://www.nseindia.com/all-reports"):
        try:
            r = s.get(home, timeout=(10, 20))
            print(f"BOOTSTRAP {r.status_code} {home}")
        except Exception as e:
            print(f"BOOTSTRAP_WARN {type(e).__name__}: {e}")

    today = date.today()
    valid = []
    diagnostics = []

    for offset in range(args.lookback_days + 1):
        if len(valid) >= args.sessions:
            break
        d = today - timedelta(days=offset)
        if d.weekday() >= 5:
            continue

        stamp = d.strftime("%d%m%Y")
        ymd = d.strftime("%Y%m%d")
        target = out / f"sec_bhavdata_full_{stamp}.csv"

        if target.exists() and validate_legacy(target.read_bytes()):
            valid.append(d)
            print(f"CACHED {d.isoformat()} ({len(valid)}/{args.sessions})", flush=True)
            continue

        got = False
        # Current UDiFF archive: one request, then a short retry only for transient errors.
        for attempt in range(2):
            try:
                url = UDIFF.format(yyyymmdd=ymd)
                r = s.get(url, timeout=(10, 30))
                ctype = r.headers.get("Content-Type", "")
                print(f"UDIFF {d.isoformat()} status={r.status_code} bytes={len(r.content)} type={ctype}", flush=True)
                if r.status_code == 200 and not looks_blocked(r.content) and r.content[:2] == b"PK":
                    if normalize_udiff(r.content, stamp, out):
                        got = True
                        break
                if r.status_code in (403, 404):
                    break
            except requests.RequestException as e:
                print(f"UDIFF_WARN {d.isoformat()} attempt={attempt+1}: {type(e).__name__}", flush=True)
            time.sleep(1.0 + attempt)

        # Legacy fallback only if UDiFF did not produce a valid file.
        if not got:
            try:
                url = LEGACY.format(ddmmyyyy=stamp)
                r = s.get(url, timeout=(10, 25))
                print(f"LEGACY {d.isoformat()} status={r.status_code} bytes={len(r.content)} type={r.headers.get('Content-Type','')}", flush=True)
                if r.status_code == 200 and validate_legacy(r.content):
                    target.write_bytes(r.content)
                    got = True
                elif target.exists():
                    target.unlink()
            except requests.RequestException as e:
                print(f"LEGACY_WARN {d.isoformat()}: {type(e).__name__}", flush=True)

        if got:
            valid.append(d)
            diagnostics.append({"date": d.isoformat(), "status": "OK"})
            print(f"OK {d.isoformat()} ({len(valid)}/{args.sessions})", flush=True)
        else:
            diagnostics.append({"date": d.isoformat(), "status": "MISS"})
            print(f"MISS {d.isoformat()} ({len(valid)}/{args.sessions})", flush=True)

        # Keep request rate modest to reduce WAF pressure.
        time.sleep(0.6)

    valid.sort()
    (out / "sessions.txt").write_text("\n".join(d.isoformat() for d in valid) + "\n")
    (out / "acquisition_diagnostics.json").write_text(json.dumps({
        "requested_sessions": args.sessions,
        "lookback_days": args.lookback_days,
        "valid_sessions": len(valid),
        "first_session": valid[0].isoformat() if valid else None,
        "last_session": valid[-1].isoformat() if valid else None,
        "diagnostics": diagnostics,
    }, indent=2))

    print(f"VALID_SESSIONS={len(valid)}", flush=True)
    if len(valid) < args.sessions:
        raise SystemExit(f"Need {args.sessions} sessions; got {len(valid)}. See data/raw/acquisition_diagnostics.json")

if __name__ == "__main__":
    main()
