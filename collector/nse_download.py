#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, io, json, time, zipfile
from datetime import date, timedelta
from pathlib import Path
import requests

# NSE discontinued the old CM bhavcopy/common-bhavcopy formats from 08-Jul-2024.
# Current source: CM-UDiFF Common Bhavcopy Final ZIP. NSE lists this as the
# replacement for the discontinued CM Bhavcopy/CM Common Bhavcopy. 
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
    head = content[:1000].lstrip().lower()
    return head.startswith(b"<") or b"access denied" in head or b"akamai" in head or b"request rejected" in head

def _clean_key(value) -> str:
    # UDiFF headers are terse (e.g. TckrSymb, SctySrs, TradDt).
    # Remove punctuation/underscores so aliases remain robust to format variants.
    return "".join(ch for ch in str(value).strip().upper() if ch.isalnum())

def _row_map(row):
    return {_clean_key(k): v for k, v in row.items()}

def _pick(row, *names):
    upper = _row_map(row)
    for name in names:
        key = _clean_key(name)
        if key in upper:
            return upper[key]
    return ""

def _parse_date(value):
    s = str(value or "").strip()
    for fmt in ("%Y-%m-%d", "%Y%m%d", "%d-%m-%Y", "%d/%m/%Y", "%d-%b-%Y"):
        try:
            from datetime import datetime
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None

def normalize_udiff(raw: bytes, stamp: str, out: Path) -> bool:
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            names = [n for n in z.namelist() if n.lower().endswith(".csv")]
            if not names:
                print("UDIFF_PARSE no CSV member", flush=True)
                return False
            # Prefer the largest CSV member if a ZIP contains auxiliary CSVs.
            name = max(names, key=lambda n: z.getinfo(n).file_size)
            with z.open(name) as f:
                text = io.TextIOWrapper(f, encoding="utf-8-sig", errors="replace").read()

        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
        if not rows:
            print("UDIFF_PARSE empty CSV", flush=True)
            return False

        header_keys = {_clean_key(x) for x in (reader.fieldnames or [])}
        print(f"UDIFF_PARSE member={name} rows={len(rows)} headers={sorted(header_keys)[:12]}...", flush=True)

        # Actual UDiFF CM Bhavcopy names include TckrSymb, SctySrs, TradDt,
        # OpnPric, HghPric, LwPric, ClsPric, PrvsClsgPric and TtlTradgVol.
        required = [
            {"TCKRSYMB", "SYMBOL"},
            {"SCTYSRS", "SERIES"},
            {"TRADDT", "DATE", "DATE1"},
            {"CLSPRIC", "CLOSEPRICE", "CLOSE"},
        ]
        if not any(x & header_keys for x in required):
            print("UDIFF_PARSE unsupported header schema", flush=True)
            return False

        expected_date = _parse_date(stamp)
        out_rows = []
        source_dates = set()

        for r in rows:
            sym = str(_pick(r, "TckrSymb", "TCKR_SYMB", "SYMBOL")).strip()
            series = str(_pick(r, "SctySrs", "SCTY_SERIES", "SERIES")).strip().upper()
            if not sym or (series and series != "EQ"):
                continue

            raw_date = _pick(r, "TradDt", "TRADG_DATE", "DATE1", "DATE")
            parsed_date = _parse_date(raw_date)
            if parsed_date:
                source_dates.add(parsed_date)

            def num(*aliases):
                return _pick(r, *aliases)

            turnover_rupees = num("TtlTrfVal", "TRAD_VAL", "TURNOVER_LACS")
            try:
                turnover_lacs = float(str(turnover_rupees).replace(",", "").strip()) / 100000.0 if turnover_rupees else ""
            except ValueError:
                turnover_lacs = ""

            out_rows.append({
                "SYMBOL": sym,
                "SERIES": "EQ",
                "ISIN": _pick(r, "ISIN"),
                "DATE1": raw_date,
                "PREV_CLOSE": num("PrvsClsgPric", "PREV_CL_PR", "PREV_CLOSE"),
                "OPEN_PRICE": num("OpnPric", "OPEN_PRICE", "OPEN"),
                "HIGH_PRICE": num("HghPric", "HIGH_PRICE", "HIGH"),
                "LOW_PRICE": num("LwPric", "LOW_PRICE", "LOW"),
                "CLOSE_PRICE": num("ClsPric", "CLSPRIC", "CLOSE_PRICE", "CLOSE"),
                "LAST_PRICE": num("LastPric", "LAST_PRICE", "LTP"),
                "TTL_TRD_QNTY": num("TtlTradgVol", "TTLT_TRAD_QTY", "TTL_TRD_QNTY", "TOTTRDQTY"),
                "TURNOVER_LACS": turnover_lacs,
                "NO_OF_TRADES": num("TtlNbOfTxsExctd", "NO_OF_TRADES"),
                # Delivery is not guaranteed to be present in CM UDiFF Bhavcopy.
                # It is left blank rather than fabricated; delivery can be joined
                # later from NSE Security-wise Delivery Positions.
                "DELIV_QTY": num("DlvryQty", "DELIV_QTY", "DELIVERY_QTY"),
                "DELIV_PER": num("DlvryPer", "DELIV_PER", "DELIVERY_PER"),
            })

        if not out_rows:
            print("UDIFF_PARSE no EQ rows", flush=True)
            return False

        # A valid daily file must identify the requested trade date when the
        # source exposes a date field. Never accept an unrelated cached date.
        if expected_date and source_dates and expected_date not in source_dates:
            print(f"UDIFF_PARSE date mismatch expected={expected_date} source={sorted(source_dates)[:3]}", flush=True)
            return False

        target = out / f"sec_bhavdata_full_{stamp}.csv"
        import pandas as pd
        df = pd.DataFrame(out_rows)
        df["DATE1"] = df["DATE1"].astype(str).replace({"": stamp})
        # Hard validation of the fields that downstream analysis actually needs.
        for col in ["OPEN_PRICE", "HIGH_PRICE", "LOW_PRICE", "CLOSE_PRICE", "TTL_TRD_QNTY"]:
            vals = pd.to_numeric(df[col], errors="coerce")
            if vals.notna().sum() < max(10, int(len(df) * 0.80)) or (vals.dropna() <= 0).any():
                print(f"UDIFF_PARSE invalid numeric field {col}", flush=True)
                return False

        df.to_csv(target, index=False)
        return target.exists() and target.stat().st_size > 1000

    except Exception as e:
        print(f"UDIFF_PARSE_ERROR {type(e).__name__}: {e}", flush=True)
        return False

def validate_legacy(content: bytes) -> bool:
    if looks_blocked(content) or len(content) < 1000:
        return False
    try:
        import pandas as pd
        df = pd.read_csv(io.BytesIO(content), nrows=50, dtype=str)
        normalized = {_clean_key(c): c for c in df.columns}
        series_col = normalized.get("SERIES")
        symbol_col = normalized.get("SYMBOL")
        close_col = normalized.get("CLOSEPRICE") or normalized.get("CLSPRIC")
        if not (series_col and symbol_col and close_col):
            return False
        series = df[series_col].astype(str).str.strip().str.upper()
        close = pd.to_numeric(df[close_col], errors="coerce")
        return series.eq("EQ").any() and close.notna().any() and (close.dropna() > 0).all()
    except Exception as e:
        print(f"LEGACY_VALIDATE_ERROR {type(e).__name__}: {e}", flush=True)
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

    for home in ("https://www.nseindia.com/", "https://www.nseindia.com/all-reports"):
        try:
            r = s.get(home, timeout=(10, 20))
            print(f"BOOTSTRAP {r.status_code} {home}", flush=True)
        except Exception as e:
            print(f"BOOTSTRAP_WARN {type(e).__name__}: {e}", flush=True)

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
            diagnostics.append({"date": d.isoformat(), "status": "CACHED"})
            print(f"CACHED {d.isoformat()} ({len(valid)}/{args.sessions})", flush=True)
            continue

        got = False
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
