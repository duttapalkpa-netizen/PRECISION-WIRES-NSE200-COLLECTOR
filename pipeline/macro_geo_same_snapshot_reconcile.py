#!/usr/bin/env python3
"""Strictly reconcile P0, canonical macro, Factor Registry, Event Study and Hard Gate."""
import hashlib,json,os
from pathlib import Path
import pandas as pd
import numpy as np

OUT=Path("outputs/macro_geo")
FILES={
 "coverage_json":"outputs/macro_geo/source_coverage.json",
 "nse_200_session_panel":"data/processed/nse_eq_200_sessions.csv",
 "coverage_csv":"outputs/macro_geo/source_coverage.csv",
 "macro_indicators":"data/external/macro_indicators.csv",
 "inflation_components":"data/external/inflation_components.csv",
 "government_capex":"data/external/government_capex.csv",
 "macro_source_audit":"outputs/macro_geo/india_macro_series_source_audit.json",
 "macro_qa":"outputs/macro_geo/macro_series_observation_qa.json",
 "macro_observations":"data/external/macro_series_observations.csv",
 "factor":"outputs/macro_geo/factor_coverage_audit.json",
 "event":"outputs/macro_geo/event_study_report.json",
 "event_windows":"outputs/macro_geo/event_level_window_audit.json",
 "regime":"outputs/macro_geo/historical_regime_study_report.json",
 "hard_gate":"outputs/macro_geo/hard_gate_report.json",
}
def digest(path):
 h=hashlib.sha256()
 with Path(path).open("rb") as f:
  for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
 return h.hexdigest()
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 missing=[p for p in FILES.values() if not Path(p).exists()]
 items={k:{"path":p,"sha256":digest(p),"bytes":Path(p).stat().st_size} for k,p in FILES.items() if Path(p).exists()}
 report={"schema_version":"2.0","workflow_run_id":os.environ.get("GITHUB_RUN_ID"),"workflow_head_sha":os.environ.get("GITHUB_SHA"),"files":items,"missing_required_files":missing,"checks":{}}
 if not missing:
  coverage=json.loads(Path(FILES["coverage_json"]).read_text())
  macroqa=json.loads(Path(FILES["macro_qa"]).read_text())
  factor=json.loads(Path(FILES["factor"]).read_text())
  hard=json.loads(Path(FILES["hard_gate"]).read_text())
  csv=pd.read_csv(FILES["coverage_csv"])
  csv_names=csv["source"].astype(str).str.strip()
  json_rows=coverage.get("sources",[])
  json_names=[str(r.get("source","")).strip() for r in json_rows]
  csv_status={str(r["source"]).strip():str(r["status"]) for _,r in csv.iterrows()}
  json_status={str(r.get("source","")).strip():str(r.get("status","")) for r in json_rows}
  exact_keys=(len(csv_names)==len(set(csv_names)) and len(json_names)==len(set(json_names))
              and set(csv_status)==set(json_status))
  report["checks"]["macro_source_audit_belongs_to_p0_run"]=str(coverage.get("macro_series_source_audit_run_id",""))==str(coverage.get("p0_workflow_run_id","")) and bool(coverage.get("p0_workflow_run_id"))
  report["checks"]["factor_audit_uses_same_source_snapshot"]=factor.get("source_coverage_as_of")==coverage.get("as_of_utc")
  report["checks"]["source_coverage_csv_json_statuses_match"]=exact_keys and all(csv_status[k]==json_status[k] for k in json_status)
  macro=pd.read_csv(FILES["macro_indicators"])
  capex=pd.read_csv(FILES["government_capex"])
  inflation=pd.read_csv(FILES["inflation_components"])
  obs_hash=digest(FILES["macro_observations"])
  report["checks"]["normalized_observation_hash_matches"]=macroqa.get("sha256")==obs_hash
  report["checks"]["normalized_duplicate_keys_zero"]=int(macroqa.get("duplicate_keys",-1))==0
  report["checks"]["macro_indicator_release_timestamps_present"]=bool(len(macro)) and macro["RELEASED_AT"].notna().all()
  report["checks"]["inflation_component_release_timestamps_present"]=bool(len(inflation)) and inflation["RELEASED_AT"].notna().all()
  report["checks"]["capex_unverified_release_times_not_promoted"]=("RELEASED_AT" in capex.columns and capex["RELEASED_AT"].isna().all())
  report["checks"]["factor_group_count_35"]=int(factor.get("factor_groups",0))==35
  report["checks"]["hard_gate_report_present"]=bool(hard.get("status"))
  report["macro_rows"]={"canonical_macro_indicators":int(len(macro)),"government_capex":int(len(capex)),"inflation_components":int(len(inflation)),"raw_normalized_observations":int(len(pd.read_csv(FILES["macro_observations"])))}
  report["factor_coverage"]={k:factor.get(k) for k in ("factor_groups","fully_available_schema_groups","partial_source_coverage","not_connected")}
  report["hard_gate"]={"status":hard.get("status"),"blockers":hard.get("blockers",[])}
  report["source_snapshot_as_of_utc"]=coverage.get("as_of_utc")
  report["status"]="RECONCILED_SAME_WORKFLOW_SNAPSHOT" if all(report["checks"].values()) else "SAME_WORKFLOW_SNAPSHOT_WITH_RECONCILIATION_GAPS"
 else:
  report["status"]="INCOMPLETE_REQUIRED_EVIDENCE_MISSING"
 report["created_at_utc"]=pd.Timestamp.now(tz="UTC").isoformat()
 p=OUT/"same_snapshot_reconciliation.json"
 p.write_text(json.dumps(report,ensure_ascii=False,indent=2,default=lambda value: value.item() if isinstance(value,np.generic) else str(value))+"\n")
 Path(str(p)+".sha256").write_text(digest(p)+"  "+p.name+"\n")
 print(json.dumps(report,ensure_ascii=False,indent=2,default=lambda value: value.item() if isinstance(value,np.generic) else str(value)))
if __name__=="__main__": main()
