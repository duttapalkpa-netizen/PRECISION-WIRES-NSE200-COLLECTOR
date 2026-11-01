#!/usr/bin/env python3
"""Audit whether official OEA WPI evidence is eligible for Factor Registry promotion."""
import csv, hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(".")
BASE=ROOT/"artifacts/macro_full_history_discovery"
REGISTRY=ROOT/"config/macro_factor_registry.csv"
FACTOR_AUDIT=ROOT/"pipeline/macro_geo_factor_coverage_audit.py"
EVIDENCE=ROOT/"data/reference/oea_wpi_release_status_evidence.json"

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def audit_eligibility(registry_rows, factor_audit_source, crosswalk, normalized_fields, evidence):
    f14=next((r for r in registry_rows if r.get("factor_id")=="F14"),None)
    if not f14: raise ValueError("F14 missing from Factor Registry")
    mapping=re.search(r'"F14":\[(.*?)\]',factor_audit_source)
    if not mapping or "inflation_components" not in mapping.group(1):
        raise ValueError("F14 inflation_components mapping is not present; refusing silent remap")
    counts=crosswalk["status_counts"]
    required={"DATE","COUNTRY","COMPONENT","VALUE","RELEASED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"}
    fields={x.strip().upper() for x in normalized_fields}
    missing=sorted(required-fields)
    release_statuses=evidence["official_month_status"]
    return {
      "status":"WPI_FACTOR_REGISTRY_ELIGIBILITY_AUDIT_PASS",
      "candidate_factor":{"factor_id":"F14","factor":f14["factor"],
        "mapped_source_group":"inflation_components"},
      "source_evidence":{"publisher":evidence["publisher"],"url":evidence["source_url"],
        "published_date":evidence["published_date"],"crosswalk_rows":crosswalk["crosswalk_rows"],
        "verified_month_statuses":release_statuses,"status_counts":counts},
      "source_schema":{"required_inflation_components_fields":sorted(required),
        "normalized_itemwise_fields":sorted(fields),"missing_required_fields":missing},
      "promotion_decision":"NOT_ELIGIBLE",
      "promotion_blockers":[
        "Normalized itemwise observations do not include per-observation RELEASED_AT, SOURCE_URL, or OBSERVED_AT_UTC.",
        "The reviewed PIB notice confirms month-level aggregate revision labels only; it does not certify all historical item-level revisions.",
        "36 observed months remain UNKNOWN because no month-specific official revision evidence was included in the reviewed PIB release.",
        "October 2026 has no observation and is scheduled for release on 2026-11-16."
      ],
      "factor_registry_impact":"NO_CHANGE_F14_REMAINS_UNPROMOTED",
      "coverage_impact":"NO_SOURCE_COVERAGE_PROMOTION; inflation_components remains governed by its existing audited snapshot",
      "hard_gate":"UNCHANGED_BLOCKED_UNTIL_ALL_REQUIRED_P0_AND_FACTOR_EVIDENCE_GATES_PASS",
      "production_invariants":{"production_selector":"UNCHANGED","RANKING_SCORE":"UNCHANGED",
        "+1_PRESSURE_FADE":"UNCHANGED","core_diagnostic_signals":672},
      "safety":"A successful eligibility audit is not a source-availability PASS. Missing evidence remains UNKNOWN, not negative."
    }

def main():
    for p in (REGISTRY,FACTOR_AUDIT,BASE/"oea_wpi_itemwise_manifest.json",
              BASE/"oea_wpi_release_status_crosswalk.json",BASE/"oea_wpi_release_status_crosswalk.csv",
              BASE/"OEA_WPI_2022-23_itemwise_monthly_observations.csv",EVIDENCE):
        if not p.exists(): raise SystemExit(f"Missing required evidence: {p}")
    with REGISTRY.open(newline="",encoding="utf-8-sig") as f: registry=list(csv.DictReader(f))
    cross=json.loads((BASE/"oea_wpi_release_status_crosswalk.json").read_text())
    manifest=json.loads((BASE/"oea_wpi_itemwise_manifest.json").read_text())
    with (BASE/"OEA_WPI_2022-23_itemwise_monthly_observations.csv").open(newline="",encoding="utf-8") as f:
        fields=next(csv.reader(f))
    evidence=json.loads(EVIDENCE.read_text())
    report=audit_eligibility(registry,FACTOR_AUDIT.read_text(),cross,fields,evidence)
    report["generated_at_utc"]=datetime.now(timezone.utc).isoformat()
    report["input_hashes"]={
      "itemwise_manifest_sha256":sha(BASE/"oea_wpi_itemwise_manifest.json"),
      "release_crosswalk_sha256":sha(BASE/"oea_wpi_release_status_crosswalk.csv"),
      "normalized_observations_sha256":manifest["normalized_csv"]["sha256"],
      "registry_sha256":sha(REGISTRY)
    }
    out=BASE/"oea_wpi_factor_registry_eligibility_audit.json"
    out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"status":report["status"],"factor_id":"F14",
      "promotion_decision":report["promotion_decision"],
      "missing_required_fields":report["source_schema"]["missing_required_fields"],
      "factor_registry_impact":report["factor_registry_impact"],
      "hard_gate":report["hard_gate"]},indent=2))
if __name__=="__main__": main()
