#!/usr/bin/env python3
"""Acquire the legacy NSE equity master and retain observed source provenance.

This is NOT the daily CM-MII gzip feed. Do not claim equivalence to that feed.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import io
import json
import pandas as pd
import requests

OUT=Path("data/reference/security_master.csv")
MANIFEST=Path("data/reference/security_master_manifest.json")
URLS=[
 "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
 "https://archives.nseindia.com/content/equities/EQUITY_L.csv",
]
HEAD={"User-Agent":"Mozilla/5.0","Accept":"text/csv,text/plain,*/*","Referer":"https://www.nseindia.com/"}

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    # Remove any prior-run pair before attempting a fresh acquisition. Otherwise
    # a failed fetch could leave a still-fresh old manifest/master that passes QA.
    OUT.unlink(missing_ok=True)
    MANIFEST.unlink(missing_ok=True)
    s=requests.Session();s.headers.update(HEAD)
    errors=[]
    for url in URLS:
        try:
            r=s.get(url,timeout=(10,30))
            r.raise_for_status()
            if not r.content or r.content[:1]==b"<":
                raise ValueError("empty or HTML response")
            df=pd.read_csv(io.BytesIO(r.content),dtype=str)
            df.columns=[str(c).strip().upper() for c in df.columns]
            if "SYMBOL" not in df.columns:
                raise ValueError("CSV missing SYMBOL header")
            isin=next((c for c in ["ISIN NUMBER","ISIN"] if c in df.columns),None)
            if isin is None:
                raise ValueError("CSV missing ISIN NUMBER/ISIN header")
            listing=next((c for c in ["LISTING DATE","LISTING_DATE"] if c in df.columns),None)
            out=pd.DataFrame({
                "SYMBOL":df["SYMBOL"].fillna("").astype(str).str.strip().str.upper(),
                "ISIN":df[isin].fillna("").astype(str).str.strip().str.upper(),
                "LISTING_DATE":df[listing].fillna("").astype(str).str.strip() if listing else ""
            })
            out=out[(out["SYMBOL"]!="") & (out["ISIN"]!="")].drop_duplicates("SYMBOL")
            if out.empty:
                raise ValueError("no rows with both SYMBOL and ISIN")
            payload=out.to_csv(index=False).encode("utf-8")
            # Write atomically so a failed acquisition cannot leave a partial master.
            tmp=OUT.with_suffix(".csv.tmp");tmp.write_bytes(payload);tmp.replace(OUT)
            manifest={
                "schema_version":1,
                "source_url":url,
                "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
                "http_status":r.status_code,
                "content_type":r.headers.get("Content-Type",""),
                "source_bytes":len(r.content),
                "source_sha256":hashlib.sha256(r.content).hexdigest(),
                "normalized_file":"data/reference/security_master.csv",
                "normalized_sha256":hashlib.sha256(payload).hexdigest(),
                "rows":int(len(out)),
                "source_family":"LEGACY_EQUITY_L_CSV",
                "daily_mii_equivalence":"NOT_ESTABLISHED"
            }
            mtmp=MANIFEST.with_suffix(".json.tmp")
            mtmp.write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8");mtmp.replace(MANIFEST)
            print(f"SECURITY_MASTER_OK rows={len(out)} source={url} sha256={manifest['source_sha256']}")
            return
        except Exception as e:
            errors.append(f"{url}: {type(e).__name__}: {e}")
            print(f"SECURITY_MASTER_WARN {errors[-1]}")
    raise SystemExit("Security Master acquisition failed; no PASS: "+" | ".join(errors))

if __name__=="__main__":main()
