#!/usr/bin/env python3
"""Record NIC-2 IIP evidence as DATA_QUALITY_WARN, never AVAILABLE, in source coverage."""
from pathlib import Path
import json
import pandas as pd

ROOT=Path(".")
COVERAGE=ROOT/"outputs/macro_geo/source_coverage.json"
ADAPTER=ROOT/"outputs/macro_geo/sector_fundamentals_iip_adapter_qa.json"
PANEL=ROOT/"data/external/sector_fundamentals.csv"
OUT=ROOT/"outputs/macro_geo"

def reconcile(coverage, report, evidence_path="data/external/sector_fundamentals.csv"):
    if report.get("status")!="PARTIAL_SOURCE_COVERAGE" or report.get("promotion_allowed") is not False:
        raise ValueError("Adapter report must be explicitly partial and non-promotable")
    if int(report.get("observed_rows") or 0)!=966 or int(report.get("nic2_groups") or 0)!=23:
        raise ValueError("Unexpected NIC-2 evidence extent")
    sources=coverage.get("sources",[])
    matches=[x for x in sources if isinstance(x,dict) and x.get("source")=="sector_fundamentals"]
    if len(matches)!=1:
        raise ValueError(f"Expected exactly one sector_fundamentals source row; found {len(matches)}")
    row=matches[0]
    row.update({
        "status":"DATA_QUALITY_WARN",
        "rows":0,
        "observed_rows":int(report["observed_rows"]),
        "selected_path":"",
        "evidence_path":evidence_path,
        "date_min":report["date_min"],
        "date_max":report["date_max"],
        "missing_columns":[
            "RELEASED_AT (official release time not published; PUBLICATION_TIMESTAMP remains UNKNOWN)",
            "NSE symbol/ISIN to NIC-2 point-in-time mapping",
            "company-level sector financial metrics"
        ],
        "provider":"MoSPI e-Sankhyiki NIC-2 IIP catalogue + MoSPI PIB Statement IV",
        "source_urls":[
            "https://api.mospi.gov.in/api/esankhyiki/file/download/",
            report["pib_release_url"]
        ],
        "table_id":report["catalogue_table_id"],
        "release_date":report["catalogue_release_date"],
        "release_vintage":report["catalogue_release_vintage"],
        "observed_at_utc":report["observed_at_utc"],
        "source_file_sha256":report["output_sha256"],
        "notes":"Official NIC-2 industrial-production evidence is present (966 rows, 23 groups, Apr-2023 to Sep-2026) but does not provide point-in-time NSE symbol mapping or exact publication timestamps. Kept DATA_QUALITY_WARN; rows=0 for hard-gate availability."
    })
    coverage["as_of_utc"]=report["observed_at_utc"]
    counts=pd.Series([x.get("status","UNKNOWN") for x in sources]).value_counts().to_dict()
    coverage["sources_total"]=len(sources)
    coverage["available"]=int(counts.get("AVAILABLE",0)+counts.get("AVAILABLE_SECONDARY",0))
    coverage["not_connected"]=int(counts.get("NOT_CONNECTED",0))
    coverage["quality_warn"]=int(counts.get("DATA_QUALITY_WARN",0))
    coverage["blocked"]=int(counts.get("BLOCKED",0))
    coverage["sector_fundamentals_adapter"]={
        "status":"PARTIAL_SOURCE_COVERAGE",
        "evidence_rows":int(report["observed_rows"]),
        "hard_gate_rows":0,
        "promotion_allowed":False,
        "reason":"NIC-2 IIP only; no point-in-time NSE symbol mapping and exact publication time."
    }
    return coverage

def main():
    for p in (COVERAGE,ADAPTER,PANEL):
        if not p.is_file(): raise SystemExit(f"BLOCKED_MISSING_INPUT: {p}")
    coverage=json.loads(COVERAGE.read_text(encoding="utf-8"))
    report=json.loads(ADAPTER.read_text(encoding="utf-8"))
    panel=pd.read_csv(PANEL,dtype=str).fillna("")
    if len(panel)!=966 or panel.duplicated(["DATE","SECTOR","METRIC"]).any():
        raise SystemExit("BLOCKED_SECTOR_FUNDAMENTALS_PANEL_QA")
    updated=reconcile(coverage,report)
    OUT.mkdir(parents=True,exist_ok=True)
    COVERAGE.write_text(json.dumps(updated,indent=2),encoding="utf-8")
    result={"status":"RECONCILED_WITH_DATA_QUALITY_WARNING","source":"sector_fundamentals",
      "source_status":"DATA_QUALITY_WARN","hard_gate_rows":0,"observed_rows":966,
      "coverage_counts":{k:updated.get(k) for k in ("sources_total","available","not_connected","quality_warn","blocked")},
      "as_of_utc":updated["as_of_utc"],"factor_state_promotion":False}
    (OUT/"sector_fundamentals_source_coverage_reconciliation.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
