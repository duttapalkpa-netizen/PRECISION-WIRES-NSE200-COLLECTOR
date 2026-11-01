#!/usr/bin/env python3
"""Reconcile P0, macro-series, Factor Registry and Event Study from one workflow snapshot."""
import hashlib,json,os
from pathlib import Path
import pandas as pd

ROOT=Path(".")
OUT=ROOT/"outputs/macro_geo"
REQUIRED=[
 "outputs/macro_geo/source_coverage.json",
 "outputs/macro_geo/india_macro_series_source_audit.json",
 "outputs/macro_geo/macro_series_observation_qa.json",
 "data/external/macro_series_observations.csv",
 "outputs/macro_geo/factor_coverage_audit.json",
 "outputs/macro_geo/event_study_report.json",
 "outputs/macro_geo/event_level_window_audit.json",
 "outputs/macro_geo/historical_regime_study_report.json",
 "outputs/macro_geo/hard_gate_report.json",
]
def digest(path):
 h=hashlib.sha256()
 with Path(path).open("rb") as f:
  for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
 return h.hexdigest()
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 missing=[p for p in REQUIRED if not Path(p).exists()]
 items={p:{"sha256":digest(p),"bytes":Path(p).stat().st_size} for p in REQUIRED if Path(p).exists()}
 report={"schema_version":"1.0","workflow_run_id":os.environ.get("GITHUB_RUN_ID"),"workflow_head_sha":os.environ.get("GITHUB_SHA"),"files":items,"missing_required_files":missing,"checks":{}}
 if not missing:
  coverage=json.loads(Path(REQUIRED[0]).read_text())
  source=json.loads(Path(REQUIRED[1]).read_text())
  macroqa=json.loads(Path(REQUIRED[2]).read_text())
  factor=json.loads(Path(REQUIRED[4]).read_text())
  hard=json.loads(Path(REQUIRED[8]).read_text())
  cov_asof=coverage.get("as_of_utc")
  report["checks"]["macro_source_timestamp_matches_snapshot"]=coverage.get("macro_series_source_audit_as_of_utc")==cov_asof
  report["checks"]["factor_audit_uses_same_source_snapshot"]=factor.get("source_coverage_as_of")==cov_asof
  report["checks"]["normalized_observation_hash_matches"]=macroqa.get("sha256")==items[REQUIRED[3]]["sha256"]
  report["checks"]["normalized_duplicate_keys_zero"]=int(macroqa.get("duplicate_keys",-1))==0
  report["checks"]["factor_group_count_35"]=int(factor.get("factor_groups",0))==35
  report["checks"]["hard_gate_report_present"]=bool(hard.get("status"))
  report["source_snapshot_as_of_utc"]=cov_asof
  report["factor_coverage"]={k:factor.get(k) for k in ("factor_groups","fully_available_schema_groups","partial_source_coverage","not_connected")}
  report["hard_gate"]={"status":hard.get("status"),"blockers":hard.get("blockers",[])}
  passed=all(report["checks"].values())
  report["status"]="RECONCILED_SAME_WORKFLOW_SNAPSHOT" if passed else "SAME_WORKFLOW_SNAPSHOT_WITH_RECONCILIATION_GAPS"
 else:
  report["status"]="INCOMPLETE_REQUIRED_EVIDENCE_MISSING"
 report["created_at_utc"]=pd.Timestamp.now(tz="UTC").isoformat()
 p=OUT/"same_snapshot_reconciliation.json"
 p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 Path(str(p)+".sha256").write_text(digest(p)+"  "+p.name+"\n")
 print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
