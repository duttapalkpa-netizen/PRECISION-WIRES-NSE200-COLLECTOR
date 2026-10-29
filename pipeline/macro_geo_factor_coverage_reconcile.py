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
 by_name={x.get("source"):x for x in sources if isinstance(x,dict)}
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
 coverage["factor_source_repair_reconciled_at_utc"]=pd.Timestamp.now(tz="UTC").isoformat()
 coverage["factor_source_repair_evidence"]=evidence
 COVERAGE.write_text(json.dumps(coverage,indent=2))
 # Re-run registry audit against reconciled observed coverage.
 print(json.dumps({"groups":evidence,"coverage_file":str(COVERAGE)},indent=2))
if __name__=="__main__": main()
