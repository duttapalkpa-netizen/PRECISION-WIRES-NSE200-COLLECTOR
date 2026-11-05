#!/usr/bin/env python3
"""Acquire and validate NSE's official equity security master.

Writes a minimal SYMBOL universe for existing consumers plus an enriched
SYMBOL/ISIN/company/listing-date reference table and raw-response provenance.
No inferred business-segment or NIC classification is produced.
"""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import io
import json
import os
import tempfile
import pandas as pd
import requests

OUT=Path("data/reference/security_master.csv")
UNIVERSE=Path("config/universe.csv")
MANIFEST=Path("data/reference/security_master_manifest.json")
URLS=[
    "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
    "https://archives.nseindia.com/content/equities/EQUITY_L.csv",
]
HEAD={
    "User-Agent":"Mozilla/5.0 (compatible; PRECISION-WIRES-research/1.0)",
    "Accept":"text/csv,text/plain,*/*",
    "Referer":"https://www.nseindia.com/",
}
REQUIRED={"SYMBOL","SERIES","ISIN NUMBER","NAME OF COMPANY"}

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def atomic_csv(frame: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix=path.name+".",suffix=".tmp",dir=str(path.parent))
    os.close(fd)
    try:
        frame.to_csv(tmp,index=False)
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)

def main() -> None:
    session=requests.Session()
    session.headers.update(HEAD)
    failures=[]
    for url in URLS:
        try:
            response=session.get(url,timeout=(10,30))
            response.raise_for_status()
            raw=response.content
            if not raw or raw.lstrip().startswith((b"<",b"{")):
                raise ValueError("response is empty or not a CSV payload")
            df=pd.read_csv(io.BytesIO(raw),dtype=str,keep_default_na=False)
            df.columns=[str(c).strip().upper() for c in df.columns]
            missing=sorted(REQUIRED-set(df.columns))
            if missing: raise ValueError(f"required columns missing: {missing}")
            df["SYMBOL"]=df["SYMBOL"].str.strip().str.upper()
            df["SERIES"]=df["SERIES"].str.strip().str.upper()
            df["ISIN NUMBER"]=df["ISIN NUMBER"].str.strip().str.upper()
            df["NAME OF COMPANY"]=df["NAME OF COMPANY"].str.strip()
            # EQ cash-equity shares only. ETFs, preference shares, debt and SME
            # are not silently mixed into the listed-company swing universe.
            eq=df[df["SERIES"]=="EQ"].copy()
            if eq.empty: raise ValueError("no SERIES=EQ rows found")
            if (eq["SYMBOL"]=="").any(): raise ValueError("blank EQ symbol")
            if (eq["ISIN NUMBER"]=="").any(): raise ValueError("blank EQ ISIN")
            if (eq["NAME OF COMPANY"]=="").any(): raise ValueError("blank EQ company name")
            if eq["SYMBOL"].duplicated().any(): raise ValueError("duplicate EQ symbols")
            if eq["ISIN NUMBER"].duplicated().any(): raise ValueError("duplicate EQ ISINs")
            listing_col=next((c for c in ("DATE OF LISTING","LISTING DATE","LISTING_DATE") if c in df.columns),None)
            if listing_col:
                eq["LISTING_DATE"]=eq[listing_col].astype(str).str.strip()
            else:
                eq["LISTING_DATE"]=""
            out=pd.DataFrame({
                "SYMBOL":eq["SYMBOL"],
                "ISIN":eq["ISIN NUMBER"],
                "COMPANY_NAME":eq["NAME OF COMPANY"],
                "SERIES":eq["SERIES"],
                "LISTING_DATE":eq["LISTING_DATE"],
            }).sort_values("SYMBOL").reset_index(drop=True)
            # Existing universe contract remains a one-column SYMBOL file.
            universe=out[["SYMBOL"]].copy()
            retrieved=datetime.now(timezone.utc).isoformat(timespec="seconds")
            manifest={
                "status":"ACQUIRED_AND_SCHEMA_VALIDATED",
                "source_url":url,
                "retrieved_at_utc":retrieved,
                "http_status":response.status_code,
                "raw_response_bytes":len(raw),
                "raw_response_sha256":sha256_bytes(raw),
                "source_file":"NSE EQUITY_L.csv",
                "series_filter":"EQ",
                "rows_total_source":int(len(df)),
                "rows_series_eq":int(len(out)),
                "unique_symbols":int(out["SYMBOL"].nunique()),
                "unique_isins":int(out["ISIN"].nunique()),
                "required_source_columns":sorted(REQUIRED),
                "listing_date_column":listing_col,
                "outputs":{
                    "security_master":"data/reference/security_master.csv",
                    "universe":"config/universe.csv",
                },
                "scope_note":"Exchange security identity only; no NIC-2 or business-segment exposure inferred."
            }
            atomic_csv(out,OUT)
            atomic_csv(universe,UNIVERSE)
            MANIFEST.parent.mkdir(parents=True,exist_ok=True)
            MANIFEST.write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
            print(json.dumps(manifest,indent=2))
            return
        except Exception as exc:
            failures.append({"url":url,"error":f"{type(exc).__name__}: {exc}"})
    raise SystemExit("NSE security master acquisition failed: "+json.dumps(failures))

if __name__=="__main__":
    main()
