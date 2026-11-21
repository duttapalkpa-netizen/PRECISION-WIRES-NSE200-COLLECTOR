#!/usr/bin/env python3
"""Fail-closed validation for the retained legacy NSE equity master."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from urllib.parse import urlparse
import hashlib, json, sys
import pandas as pd

MASTER=Path("data/reference/security_master.csv")
MANIFEST=Path("data/reference/security_master_manifest.json")
ALLOWED_HOSTS={"nsearchives.nseindia.com","archives.nseindia.com"}

def validate(master_path=MASTER, manifest_path=MANIFEST, now=None):
    now=now or datetime.now(timezone.utc)
    if not master_path.is_file() or not manifest_path.is_file():
        raise ValueError("master or provenance manifest missing")
    manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    parsed=urlparse(str(manifest.get("source_url","")))
    if parsed.scheme!="https" or parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError("source URL is not an approved official NSE host")
    if manifest.get("source_family")!="LEGACY_EQUITY_L_CSV" or manifest.get("daily_mii_equivalence")!="NOT_ESTABLISHED":
        raise ValueError("source-family boundary missing or altered")
    retrieved=datetime.fromisoformat(manifest["retrieved_at_utc"].replace("Z","+00:00"))
    if retrieved.tzinfo is None:
        raise ValueError("retrieval timestamp must be timezone-aware")
    age=now-retrieved.astimezone(timezone.utc)
    if age < timedelta(minutes=-5) or age > timedelta(days=7):
        raise ValueError("master provenance is future-dated or stale (>7 days)")
    raw=master_path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=manifest.get("normalized_sha256"):
        raise ValueError("normalized master SHA-256 mismatch")
    df=pd.read_csv(master_path,dtype=str).fillna("")
    df.columns=[str(c).strip().upper() for c in df.columns]
    if not {"SYMBOL","ISIN","LISTING_DATE"}.issubset(df.columns):
        raise ValueError("normalized master missing required columns")
    if df.empty or (df["SYMBOL"].str.strip()=="").any() or (df["ISIN"].str.strip()=="").any():
        raise ValueError("master has empty rows or missing SYMBOL/ISIN")
    if df["SYMBOL"].duplicated().any():
        raise ValueError("duplicate SYMBOL values")
    if len(df)!=int(manifest.get("rows",-1)):
        raise ValueError("manifest row count mismatch")
    if int(manifest.get("source_bytes",0))<=0 or len(str(manifest.get("source_sha256","")))!=64:
        raise ValueError("source-byte provenance incomplete")
    return {"status":"PASS","rows":len(df),"source_family":"LEGACY_EQUITY_L_CSV","daily_mii_equivalence":"NOT_ESTABLISHED"}

if __name__=="__main__":
    try:
        print(json.dumps(validate(),sort_keys=True))
    except Exception as exc:
        print(f"SECURITY_MASTER_BLOCKED: {exc}",file=sys.stderr)
        raise SystemExit(1)
