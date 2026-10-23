#!/usr/bin/env python3
"""Strict artifact-backed validation for four Macro-Geo source groups."""
from pathlib import Path
import json
import pandas as pd

ROOT=Path(".")
OUT=ROOT/"outputs/macro_geo"
SPECS={
 "benchmark_index":{"path":"data/external/benchmark_indices.csv","required":["DATE","SERIES","CLOSE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"],"key":["DATE","SERIES"],"date":"DATE"},
 "sector_indices":{"path":"data/external/sector_indices.csv","required":["DATE","SERIES","CLOSE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"],"key":["DATE","SERIES"],"date":"DATE"},
 "volatility":{"path":"data/external/volatility.csv","required":["DATE","SERIES","CLOSE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"],"key":["DATE","SERIES"],"date":"DATE"},
 "geopolitical_events":{"path":"data/external/geopolitical_events.csv","required":["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","SOURCE","SOURCE_URL","CONFIDENCE"],"key":["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","SOURCE_URL"],"date":"EVENT_DATE"},
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 report={"status":"PASS","source_groups":{},"validation_scope":"schema, row/date coverage, positive numeric closes, duplicate keys, source URL/provenance, timestamp validity; not proof of underlying event occurrence"}
 for name,spec in SPECS.items():
  path=ROOT/spec["path"]; item={"path":spec["path"],"status":"BLOCKED","rows":0,"date_min":None,"date_max":None,"schema":[],"missing_columns":spec["required"],"provenance":{},"blockers":[]}
  if not path.exists():
   item["blockers"].append("FILE_MISSING")
  else:
   try:
    df=pd.read_csv(path); df.columns=[str(c).strip().upper() for c in df.columns]
    item["rows"]=int(len(df)); item["schema"]=list(df.columns)
    missing=sorted(set(spec["required"])-set(df.columns)); item["missing_columns"]=missing
    if missing: item["blockers"].append("MISSING_REQUIRED_COLUMNS")
    if df.empty: item["blockers"].append("ZERO_ROWS")
    dcol=spec["date"]
    if dcol in df:
     dates=pd.to_datetime(df[dcol],errors="coerce",utc=True)
     item["invalid_date_rows"]=int(dates.isna().sum())
     valid=dates.dropna()
     if len(valid): item["date_min"]=str(valid.min().date()); item["date_max"]=str(valid.max().date())
     if dates.isna().any(): item["blockers"].append("INVALID_DATES")
    if name!="geopolitical_events" and "CLOSE" in df:
     close=pd.to_numeric(df["CLOSE"],errors="coerce")
     item["invalid_close_rows"]=int((close.isna() | (close<=0)).sum())
     if (close.isna() | (close<=0)).any(): item["blockers"].append("INVALID_CLOSE")
    key=spec["key"]
    if set(key).issubset(df.columns):
     item["duplicate_key_rows"]=int(df.duplicated(key).sum())
     if item["duplicate_key_rows"]: item["blockers"].append("DUPLICATE_KEYS")
    urlcol="SOURCE_URL"
    if urlcol in df:
     urls=df[urlcol].fillna("").astype(str).str.strip()
     item["provenance"]={"source_values":sorted(df["SOURCE"].fillna("").astype(str).unique().tolist()) if "SOURCE" in df else [],"url_rows":int(urls.str.match(r"^https?://",case=False).sum()),"missing_or_invalid_url_rows":int((~urls.str.match(r"^https?://",case=False)).sum())}
     if item["provenance"]["missing_or_invalid_url_rows"]: item["blockers"].append("SOURCE_URL_MISSING_OR_INVALID")
    if "OBSERVED_AT_UTC" in df:
     observed=pd.to_datetime(df["OBSERVED_AT_UTC"],errors="coerce",utc=True)
     item["provenance"]["observed_at_valid_rows"]=int(observed.notna().sum())
     item["provenance"]["observed_at_invalid_rows"]=int(observed.isna().sum())
     if observed.isna().any(): item["blockers"].append("OBSERVATION_TIMESTAMP_INVALID")
    if name=="geopolitical_events":
     pub=pd.to_datetime(df["PUBLISHED_AT"],errors="coerce",utc=True) if "PUBLISHED_AT" in df else pd.Series(dtype="datetime64[ns, UTC]")
     item["invalid_publication_timestamp_rows"]=int(pub.isna().sum())
     if pub.isna().any(): item["blockers"].append("PUBLICATION_TIMESTAMP_INVALID")
     if "CONFIDENCE" in df:
      conf=pd.to_numeric(df["CONFIDENCE"],errors="coerce")
      item["invalid_confidence_rows"]=int((conf.isna() | (conf<0) | (conf>1)).sum())
      if item["invalid_confidence_rows"]: item["blockers"].append("CONFIDENCE_OUT_OF_RANGE")
     item["provenance"]["event_semantics"]="Publisher/RSS/GDELT media mention; occurrence independently unverified"
    item["status"]="AVAILABLE_VALIDATED" if not item["blockers"] else "BLOCKED"
   except Exception as exc:
    item["blockers"].append("READ_OR_VALIDATION_ERROR: "+type(exc).__name__+": "+str(exc))
  if item["status"]!="AVAILABLE_VALIDATED": report["status"]="BLOCKED"
  report["source_groups"][name]=item
 (OUT/"four_group_validation.json").write_text(json.dumps(report,indent=2))
 print(json.dumps(report,indent=2))
 return 0
if __name__=="__main__": raise SystemExit(main())
