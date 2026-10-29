#!/usr/bin/env python3
"""Reconcile factor-source repair evidence into source coverage conservatively."""
from pathlib import Path
import json, shutil
import pandas as pd

ROOT=Path(".")
REPORT=ROOT/"outputs/macro_geo/factor_source_collection_report.json"
COVERAGE=ROOT/"outputs/macro_geo/source_coverage.json"
OUT=ROOT/"outputs/macro_geo"
MAP={
 "us_yields":("us_yields.csv","us_yields"),
 "dxy":("dxy.csv","dxy"),
 "global_commodity_prices":("commodity_prices.csv","global_commodity_prices"),
 "global_policy_events":("global_policy_events.csv","global_policy_events"),
}
def main():
 if not REPORT.exists() or not COVERAGE.exists():
  raise SystemExit("Missing factor-source report or baseline source_coverage.json; refusing to invent coverage")
 report=json.loads(REPORT.read_text()); coverage=json.loads(COVERAGE.read_text())
 sources=coverage.setdefault("sources",[])
 by_name={}
 for x in sources:
  if not isinstance(x,dict):
   continue
  key=x.get("source")
  if isinstance(key,str) and key.strip():
   by_name[key.strip()]=x
 evidence={}
 for group,(filename,source_name) in MAP.items():
  item=report.get("groups",{}).get(group,{})
  src=ROOT/"data/external"/filename
  status=str(item.get("status","BLOCKED"))
  rows=int(item.get("rows") or 0)
  # Only collector's explicit complete domain-QA status can improve coverage.
  valid=status=="COLLECTED_AND_DOMAIN_QA_PASSED" and rows>0 and src.exists()
  if valid:
   frame=pd.read_csv(src)
   required={"DATE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"}
   if not required.issubset({str(c).strip().upper() for c in frame.columns}) or frame.empty:
    valid=False
  evidence[group]={"status":"AVAILABLE" if valid else ("DATA_QUALITY_WARN" if rows else "BLOCKED"),
    "rows":rows if valid else 0,"observed_rows":rows,"date_min":item.get("date_min"),"date_max":item.get("date_max"),
    "source":item.get("source"),"source_series":item.get("observed_source_series"),
    "freshness_age_calendar_days":item.get("freshness_age_calendar_days"),
    "evidence_path":str(src) if src.exists() else None,
    "reason":"Complete collector domain QA passed" if valid else "Not counted as available: source failure, incomplete domain QA, or missing evidence"}
  existing=by_name.get(source_name)
  if existing is None:
   existing={"source":source_name}; sources.append(existing); by_name[source_name]=existing
  existing.update(evidence[group])
 # Split commodity evidence by exact identity. A valid WTI row does not make the
 # combined WTI+gold group available, and absent gold stays UNKNOWN/BLOCKED.
 commodity_path=ROOT/"data/external/commodity_prices.csv"
 commodity_frame=pd.read_csv(commodity_path) if commodity_path.exists() else pd.DataFrame()
 for label, canonical, approved_source in [
  ("WTI_CRUDE_USD_PER_BBL","crude_oil","US Energy Information Administration"),
  ("GOLD_USD_PER_TROY_OUNCE","gold_prices","London Bullion Market Association"),
 ]:
  subset=commodity_frame[commodity_frame.get("COMMODITY",pd.Series(dtype=str)).astype(str).eq(label)] if not commodity_frame.empty and "COMMODITY" in commodity_frame.columns else pd.DataFrame()
  valid=False
  if not subset.empty:
   required={"DATE","CLOSE","SOURCE","SOURCE_SERIES","SOURCE_URL","OBSERVED_AT_UTC","COMMODITY"}
   cols={str(col).strip().upper() for col in subset.columns}
   dates=pd.to_datetime(subset["DATE"],errors="coerce")
   values=pd.to_numeric(subset["CLOSE"],errors="coerce")
   source_ok=subset["SOURCE"].astype(str).str.contains(approved_source,case=False,regex=False).all()
   provenance_ok=(subset["SOURCE_URL"].astype(str).str.strip().ne("").all()
                  and subset["OBSERVED_AT_UTC"].astype(str).str.strip().ne("").all())
   key_ok=not subset.duplicated(["DATE","COMMODITY"]).any()
   valid=(required.issubset(cols) and dates.notna().all() and values.notna().all()
          and (values>0).all() and source_ok and provenance_ok and key_ok)
  group_status="AVAILABLE" if valid else ("DATA_QUALITY_WARN" if not subset.empty else "BLOCKED")
  row={"source":canonical,"status":group_status,"rows":int(len(subset)) if valid else 0,
       "observed_rows":int(len(subset)),"source_series":sorted(set(subset["SOURCE_SERIES"].astype(str))) if not subset.empty and "SOURCE_SERIES" in subset else [],
       "date_min":str(subset["DATE"].min()) if not subset.empty and "DATE" in subset else None,
       "date_max":str(subset["DATE"].max()) if not subset.empty and "DATE" in subset else None,
       "evidence_path":str(commodity_path) if not subset.empty else None,
       "reason":"Exact-identity per-series provenance/schema/value/duplicate QA passed" if valid else "Not available: no observed rows or exact-source QA incomplete; missing data remains UNKNOWN"}
  existing=by_name.get(canonical)
  if existing is None:
   existing={"source":canonical}; sources.append(existing); by_name[canonical]=existing
  existing.update(row)
 # Policy feed publication timestamps are not event dates. Explicitly record
 # the independent event-date validation as pending rather than promoting rows.
 policy_item=report.get("groups",{}).get("global_policy_events",{})
 policy_path=ROOT/"data/external/global_policy_events.csv"
 policy_frame=pd.read_csv(policy_path) if policy_path.exists() else pd.DataFrame()
 policy_date_qa={"status":"PENDING_INDEPENDENT_EVENT_DATE_VALIDATION",
                 "observed_rows":int(len(policy_frame)),
                 "rows_eligible_for_event_study":0,
                 "reason":"Publication date proxy is not accepted as the actual policy decision/event date"}
 if not policy_frame.empty and "EVENT_DATE_BASIS" in policy_frame.columns:
  if policy_frame["EVENT_DATE_BASIS"].astype(str).eq("INDEPENDENTLY_VALIDATED_EVENT_DATE").all():
   policy_date_qa.update({"status":"VALIDATED","rows_eligible_for_event_study":int(len(policy_frame)),
                          "reason":"Every row explicitly carries independently validated event-date basis"})
 coverage["policy_event_date_qa"]=policy_date_qa
 coverage["factor_source_repair_reconciled_at_utc"]=pd.Timestamp.now(tz="UTC").isoformat()
 coverage["factor_source_repair_evidence"]=evidence
 COVERAGE.write_text(json.dumps(coverage,indent=2))
 # Re-run registry audit against reconciled observed coverage.
 print(json.dumps({"groups":evidence,"coverage_file":str(COVERAGE)},indent=2))
if __name__=="__main__": main()
