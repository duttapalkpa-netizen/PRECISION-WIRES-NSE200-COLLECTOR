#!/usr/bin/env python3
"""Re-evaluate F14 only after adapter and same-snapshot coverage evidence."""
import csv,json,hashlib
from datetime import datetime,timezone
from pathlib import Path
B=Path("artifacts/macro_full_history_discovery")
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    adapter=json.loads((B/"oea_wpi_inflation_components_adapter.json").read_text())
    coverage=json.loads((B/"factor_registry_same_snapshot_coverage_audit.json").read_text())
    cross=json.loads((B/"oea_wpi_release_status_crosswalk.json").read_text())
    fields=next(csv.reader((B/"inflation_components.csv").open(encoding="utf-8")))
    required={"DATE","COUNTRY","COMPONENT","VALUE","RELEASED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"}
    missing=sorted(required-set(fields))
    blockers=[]
    if missing: blockers.append("Adapter schema missing required fields: "+",".join(missing))
    if adapter.get("status")!="INFLATION_COMPONENTS_ADAPTER_PASS_SCHEMA_COMPLETE": blockers.append("Adapter did not pass")
    if "ITEM_LEVEL_REVISION_HISTORY_NOT_PUBLISHED" in adapter.get("revision_history_boundary",""):
        blockers.append("Official source evidence does not provide item-wise revision history; month-level status cannot be promoted as item-level history.")
    if coverage.get("status")!="SAME_SNAPSHOT_FACTOR_COVERAGE_AUDIT_EXECUTED":
        blockers.append("Same-snapshot Factor Registry coverage is not executable/complete: "+str(coverage.get("status")))
    result={"status":"F14_ELIGIBILITY_RECHECK_PASS_NOT_ELIGIBLE" if blockers else "F14_ELIGIBLE_FOR_COVERAGE_REVIEW",
      "factor_id":"F14","mapped_group":"inflation_components",
      "adapter_schema":{"required_fields":sorted(required),"missing_required_fields":missing,"fields":fields},
      "same_snapshot_coverage_status":coverage.get("status"),
      "same_snapshot_sha256":coverage.get("coverage_snapshot_sha256"),
      "wpi_crosswalk_status_counts":cross.get("status_counts"),
      "promotion_decision":"NOT_ELIGIBLE" if blockers else "ELIGIBLE_FOR_SEPARATE_APPROVAL",
      "blockers":blockers,
      "factor_registry_change":"NONE; F14 mapping and registry remain unchanged",
      "hard_gate":"UNCHANGED_BLOCKED_UNTIL_ALL_REQUIRED_P0_AND_FACTOR_EVIDENCE_GATES_PASS",
      "production_invariants":{"production_selector":"UNCHANGED","RANKING_SCORE":"UNCHANGED","+1_PRESSURE_FADE":"UNCHANGED","core_diagnostic_signals":672},
      "generated_at_utc":datetime.now(timezone.utc).isoformat(),
      "input_hashes":{"adapter_csv":sha(B/"inflation_components.csv"),"adapter_report":sha(B/"oea_wpi_inflation_components_adapter.json"),
       "coverage_report":sha(B/"factor_registry_same_snapshot_coverage_audit.json"),"crosswalk":sha(B/"oea_wpi_release_status_crosswalk.csv")}}
    (B/"f14_eligibility_recheck.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
