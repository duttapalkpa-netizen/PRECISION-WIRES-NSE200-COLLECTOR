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
 "gold_prices_monthly":("gold_prices_monthly.csv","gold_prices_monthly"),
}
def latest_evidence_timestamp(coverage, report, root=ROOT):
 """Return the latest real evidence timestamp represented in this reconciliation snapshot."""
 candidates=[]
 for raw in (coverage.get("as_of_utc"), report.get("observed_at_utc")):
  parsed=pd.to_datetime(raw,errors="coerce",utc=True)
  if pd.notna(parsed): candidates.append(parsed)
 for filename,_ in MAP.values():
  path=root/"data/external"/filename
  if not path.exists(): continue
  try:
   frame=pd.read_csv(path)
  except Exception:
   continue
  col=next((c for c in frame.columns if str(c).strip().upper()=="OBSERVED_AT_UTC"),None)
  if col is None: continue
  parsed=pd.to_datetime(frame[col],errors="coerce",utc=True).dropna()
  if not parsed.empty: candidates.append(parsed.max())
 if not candidates:
  raise RuntimeError("No valid UTC evidence timestamp; refusing to emit an undated factor snapshot")
 return max(candidates).isoformat().replace("+00:00","Z")


def policy_events_promotable(policy_date_qa, collector_status):
 """Promote policy events only when row-level checks AND collector domain QA pass."""
 return (collector_status == "COLLECTED_AND_DOMAIN_QA_PASSED"
         and policy_date_qa.get("status") == "VALIDATED"
         and int(policy_date_qa.get("rows_eligible_for_event_study") or 0) > 0)


def validate_policy_event_frame(policy_frame):
 """Validate each policy row against reviewed official URL/date/type and schema."""
 import sys
 sys.path.insert(0, str(ROOT.resolve()))
 from pipeline.macro_geo_factor_source_collectors import validate_official_policy_event_date
 required={"EVENT_DATE","PUBLISHED_AT","COUNTRY","EVENT_TYPE","SOURCE_URL","SOURCE","TITLE","FEED_URL","EVENT_DATE_BASIS","OBSERVED_AT_UTC"}
 cols={str(x).strip().upper() for x in policy_frame.columns}
 checks=[]
 schema_ok=required.issubset(cols) and not policy_frame.empty
 if schema_ok:
  for _, row in policy_frame.iterrows():
   reviewed=validate_official_policy_event_date(row.get("SOURCE_URL",""))
   published=pd.to_datetime(row.get("PUBLISHED_AT"),errors="coerce",utc=True)
   observed=pd.to_datetime(row.get("OBSERVED_AT_UTC"),errors="coerce",utc=True)
   event_date=pd.to_datetime(row.get("EVENT_DATE"),errors="coerce")
   valid=bool(reviewed) and str(row.get("EVENT_DATE_BASIS",""))=="INDEPENDENTLY_VALIDATED_EVENT_DATE"
   valid=valid and str(row.get("EVENT_DATE",""))==str(reviewed.get("event_date") if reviewed else "")
   valid=valid and str(row.get("EVENT_TYPE",""))==str(reviewed.get("event_type") if reviewed else "")
   valid=valid and pd.notna(published) and pd.notna(observed) and pd.notna(event_date)
   valid=valid and str(row.get("SOURCE","")).strip() in {"FEDERAL_RESERVE","EUROPEAN_CENTRAL_BANK"}
   checks.append({"source_url":str(row.get("SOURCE_URL","")),
                  "event_date":str(row.get("EVENT_DATE","")),
                  "event_type":str(row.get("EVENT_TYPE","")),
                  "validated":bool(valid)})
 observed_rows=int(len(policy_frame))
 eligible=sum(1 for item in checks if item["validated"])
 return {"status":"VALIDATED" if schema_ok and observed_rows>0 and eligible==observed_rows else ("PARTIALLY_VALIDATED" if eligible>0 else "PENDING_INDEPENDENT_EVENT_DATE_VALIDATION"),
         "observed_rows":observed_rows,"rows_eligible_for_event_study":eligible,
         "rows_not_eligible":observed_rows-eligible,"checks":checks,
         "schema_valid":bool(schema_ok),
         "reason":"Only rows with complete provenance/timestamps and exact reviewed official URL, event date and event type are eligible; publication-date proxies remain excluded."}


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
  valid=status in {"COLLECTED_AND_DOMAIN_QA_PASSED","COLLECTED_MONTHLY_DOMAIN_QA_PASSED"} and rows>0 and src.exists()
  if valid:
   frame=pd.read_csv(src)
   required={"DATE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"}
   if not required.issubset({str(c).strip().upper() for c in frame.columns}) or frame.empty:
    valid=False
   if valid and group=="gold_prices_monthly":
    cols={str(x).strip().upper() for x in frame.columns}
    dates=pd.to_datetime(frame["DATE"],errors="coerce")
    values=pd.to_numeric(frame["CLOSE"],errors="coerce")
    valid=( {"UNIT","FREQUENCY","REVISION_POLICY","SOURCE_SERIES"}.issubset(cols)
            and frame["FREQUENCY"].astype(str).eq("MONTHLY").all()
            and frame["UNIT"].astype(str).eq("USD_PER_TROY_OUNCE").all()
            and frame["SOURCE"].astype(str).str.contains("World Bank Prospects Group Pink Sheet",case=False,regex=False).all()
            and frame["SOURCE_SERIES"].astype(str).eq("GOLD").all()
            and dates.notna().all() and values.notna().all() and (values>0).all()
            and not frame.duplicated(["DATE"]).any()
            and frame["REVISION_POLICY"].astype(str).str.contains("MONTHLY_SOURCE_REVISIONS_POSSIBLE",regex=False).all())
  evidence[group]={"source":source_name,
    "status":"AVAILABLE" if valid else ("DATA_QUALITY_WARN" if rows else "BLOCKED"),
    "rows":rows if valid else 0,"observed_rows":rows,"date_min":item.get("date_min"),"date_max":item.get("date_max"),
    "provider":item.get("source"),"source_series":item.get("observed_source_series"),
    "freshness_age_calendar_days":item.get("freshness_age_calendar_days"),
    "evidence_path":str(src) if src.exists() else None,
    "selected_path":str(src) if valid else "",
    "missing_columns":[] if valid else ["domain/source QA incomplete"],
    "notes":("Collector domain QA passed; provider provenance and observed-series identity retained in evidence fields." if valid else "No clean domain-QA promotion; missing data remains UNKNOWN."),
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
 # Independently validate policy events and promote only complete, fully checked rows.
 policy_path=ROOT/"data/external/global_policy_events.csv"
 policy_frame=pd.read_csv(policy_path) if policy_path.exists() else pd.DataFrame()
 policy_date_qa=validate_policy_event_frame(policy_frame)
 coverage["policy_event_date_qa"]=policy_date_qa
 policy_collector_status=report.get("groups",{}).get("global_policy_events",{}).get("status","BLOCKED")
 policy_valid=policy_events_promotable(policy_date_qa,policy_collector_status)
 policy_group={"source":"global_policy_events",
               "status":"AVAILABLE" if policy_valid else ("DATA_QUALITY_WARN" if policy_date_qa["observed_rows"] else "BLOCKED"),
               "rows":policy_date_qa["rows_eligible_for_event_study"] if policy_valid else 0,
               "observed_rows":policy_date_qa["observed_rows"],
               "date_min":str(policy_frame["EVENT_DATE"].min()) if not policy_frame.empty and "EVENT_DATE" in policy_frame else None,
               "date_max":str(policy_frame["EVENT_DATE"].max()) if not policy_frame.empty and "EVENT_DATE" in policy_frame else None,
               "selected_path":str(policy_path) if policy_valid else "",
               "evidence_path":str(policy_path) if not policy_frame.empty else None,
               "missing_columns":[] if policy_valid else ["complete event-date/provenance validation"],
               "notes":("All observed policy events have complete provenance and exact official URL/date/type validation." if policy_valid else "Policy events remain excluded until exact official URL/date/type validation passes."),
               "provider":"Official Federal Reserve and ECB pages, independently URL/date/type validated",
               "reason":policy_date_qa["reason"] + (" Collector domain QA passed." if policy_valid else f" Collector domain QA status is {policy_collector_status}; event rows remain warning/unknown.")}
 existing=by_name.get("global_policy_events")
 if existing is None:
  existing={"source":"global_policy_events"}; sources.append(existing); by_name["global_policy_events"]=existing
 existing.update(policy_group)
 evidence["global_policy_events"]={**policy_group,"provider":"Official Federal Reserve and ECB RSS feeds"}
 coverage["as_of_utc"]=latest_evidence_timestamp(coverage,report)
 coverage["factor_source_repair_reconciled_at_utc"]=pd.Timestamp.now(tz="UTC").isoformat()
 coverage["factor_source_repair_evidence"]=evidence
 COVERAGE.write_text(json.dumps(coverage,indent=2))
 # Re-run registry audit against reconciled observed coverage.
 print(json.dumps({"groups":evidence,"coverage_file":str(COVERAGE)},indent=2))
if __name__=="__main__": main()
