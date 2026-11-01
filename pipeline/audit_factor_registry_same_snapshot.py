#!/usr/bin/env python3
"""Same-snapshot Factor Registry coverage audit; missing snapshots remain UNKNOWN."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path("."); BASE=Path("artifacts/macro_full_history_discovery")
COVERAGE=Path("outputs/macro_geo/source_coverage.json")
REGISTRY=Path("config/macro_factor_registry.csv")
MAP_SOURCE=Path("pipeline/macro_geo_factor_coverage_audit.py")
OUT=BASE/"factor_registry_same_snapshot_coverage_audit.json"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    result={"generated_at_utc":datetime.now(timezone.utc).isoformat(),
      "registry_sha256":sha(REGISTRY),"factor_mapping_sha256":sha(MAP_SOURCE),
      "coverage_snapshot_path":str(COVERAGE),
      "hard_gate":"UNCHANGED_BLOCKED_UNTIL_ALL_REQUIRED_P0_AND_FACTOR_EVIDENCE_GATES_PASS"}
    if not COVERAGE.is_file():
        result.update({"status":"BLOCKED_MISSING_SOURCE_COVERAGE_SNAPSHOT",
          "coverage_snapshot_sha256":None,"coverage_as_of_utc":None,
          "factor_groups":35,"coverage_rows_written":False,
          "blocker":"outputs/macro_geo/source_coverage.json is not present in this workflow checkout; no substitute or fabricated coverage snapshot was created.",
          "F14":{"mapped_source_groups":["macro_indicators","us_yields","india_bond_yields","inflation_components"],
                "decision":"UNKNOWN_NOT_REEVALUABLE_WITHOUT_SAME_SNAPSHOT_COVERAGE"} })
    else:
        cov=json.loads(COVERAGE.read_text())
        # Run canonical audit against this exact source_coverage snapshot.
        import subprocess,sys
        p=subprocess.run([sys.executable,"pipeline/macro_geo_factor_coverage_audit.py"],capture_output=True,text=True)
        result.update({"status":"SAME_SNAPSHOT_FACTOR_COVERAGE_AUDIT_EXECUTED" if p.returncode==0 else "SAME_SNAPSHOT_FACTOR_COVERAGE_AUDIT_FAILED",
          "coverage_snapshot_sha256":sha(COVERAGE),"coverage_as_of_utc":cov.get("as_of_utc"),
          "factor_groups":35,"canonical_audit_returncode":p.returncode,
          "canonical_audit_stdout":p.stdout[-4000:],"canonical_audit_stderr":p.stderr[-4000:]})
        if p.returncode==0:
            q=Path("outputs/macro_geo/factor_coverage_audit.json")
            if q.exists():
                x=json.loads(q.read_text()); result["canonical_report_sha256"]=sha(q)
                result["canonical_report_status"]=x.get("status")
                result["F14"]=next((r for r in x.get("missing_factors",[]) if r.get("factor_id")=="F14"),{"decision":"SEE_CANONICAL_REPORT"})
    OUT.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
