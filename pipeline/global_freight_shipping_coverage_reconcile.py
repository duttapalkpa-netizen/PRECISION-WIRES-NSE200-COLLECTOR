#!/usr/bin/env python3
"""Conservatively reconcile IMF PortWatch chokepoint activity into factor coverage."""
from pathlib import Path
import hashlib,json
import pandas as pd

PANEL=Path("data/external/global_freight_shipping.csv")
QA=Path("outputs/macro_geo/global_freight_shipping_200_session_qa.json")
COVERAGE=Path("outputs/macro_geo/source_coverage.json")

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def reconcile(coverage,report,panel,panel_sha):
    if report.get("status")!="PASS_BACKFILL_WITH_EXPLICIT_COVERAGE_AUDIT":
        raise ValueError("PortWatch backfill did not pass source QA")
    if report.get("snapshot_id")!="1f6d79d9bcdf3a6aa11dd9a80033276061447401dac6c708ab6622b6258b7534":
        raise ValueError("Unexpected NSE snapshot identity")
    if report.get("nse_sessions")!=200 or report.get("distinct_chokepoints")!=28:
        raise ValueError("Unexpected 200-session/chokepoint dimensions")
    if report.get("records_retrieved")!=report.get("query_total_records") or report.get("duplicate_date_chokepoint_keys")!=0:
        raise ValueError("PortWatch query pagination or key integrity failed")
    if report.get("nse_session_rows")!=5432 or report.get("missing_nse_session_keys")!=168:
        raise ValueError("Unexpected provider coverage profile; requires re-audit")
    required={"DATE","CHOKEPOINT_ID","CHOKEPOINT","n_total","capacity","SOURCE_URL","OBSERVED_AT_UTC","NSE_SNAPSHOT_ID"}
    if not required.issubset(panel.columns): raise ValueError("PortWatch panel schema incomplete")
    selected=panel[panel["IS_NSE_SESSION"].astype(str).str.lower().eq("true")]
    if len(selected)!=5432 or selected["DATE"].nunique()!=194:
        raise ValueError("PortWatch NSE-session subset does not match QA report")
    if selected.duplicated(["DATE","CHOKEPOINT_ID"]).any():
        raise ValueError("Duplicate PortWatch date/chokepoint keys")
    if not selected["SOURCE_URL"].astype(str).str.startswith("https://services9.arcgis.com/").all():
        raise ValueError("Unexpected PortWatch provenance URL")
    sources=coverage.setdefault("sources",[])
    item=next((x for x in sources if x.get("source")=="global_freight_shipping"),None)
    if item is None:
        item={"source":"global_freight_shipping"};sources.append(item)
    item.update({
      "status":"DATA_QUALITY_WARN","rows":0,"observed_rows":int(len(selected)),
      "provider_rows_total":int(len(panel)),"selected_path":"",
      "evidence_path":str(PANEL),"source_sha256":panel_sha,
      "snapshot_id":report["snapshot_id"],"date_min":str(selected["DATE"].min()),
      "date_max":str(selected["DATE"].max()),"distinct_chokepoints":report["distinct_chokepoints"],
      "nse_session_coverage_pct":report["nse_session_coverage_pct"],
      "expected_nse_session_keys":report["expected_nse_session_keys"],
      "observed_nse_session_keys":report["observed_nse_session_keys"],
      "missing_nse_session_keys":report["missing_nse_session_keys"],
      "provider_last_edit_date_epoch_ms":report["metadata_last_edit_date_epoch_ms"],
      "observed_at_utc":report["observed_at_utc"],
      "notes":"200-session IMF PortWatch AIS-derived chokepoint activity joined to the frozen NSE calendar. 194/200 NSE dates observed across 28 chokepoints; 168 date/chokepoint keys absent because latest activity date is 2026-10-25. Missing observations remain gaps, not zero. AIS-derived activity is a proxy, not a freight-rate quote; exact publication timestamps are unavailable.",
      "reason":"DATA_QUALITY_WARN: 97% date/chokepoint coverage with 6 missing NSE sessions and no exact provider publication timestamp; zero hard-gate rows."
    })
    coverage["as_of_utc"]=report["observed_at_utc"]
    statuses=[str(x.get("status","")) for x in sources]
    coverage["sources_total"]=len(sources)
    coverage["available"]=sum(x=="AVAILABLE" for x in statuses)
    coverage["not_connected"]=sum(x=="NOT_CONNECTED" for x in statuses)
    coverage["quality_warn"]=sum(x=="DATA_QUALITY_WARN" for x in statuses)
    coverage["schema_fail"]=sum(x=="SCHEMA_FAIL" for x in statuses)
    coverage["read_error"]=sum(x=="READ_ERROR" for x in statuses)
    coverage["blocked"]=sum(x in {"BLOCKED","BLOCKED_MISSING_INPUT"} for x in statuses)
    coverage["global_freight_shipping_reconciled_at_utc"]=report["observed_at_utc"]
    return coverage

def main():
    if not PANEL.is_file() or not QA.is_file() or not COVERAGE.is_file():
        raise SystemExit("BLOCKED_MISSING_PORTWATCH_OR_BASELINE_INPUT")
    report=json.loads(QA.read_text())
    panel=pd.read_csv(PANEL,dtype=str).fillna("")
    cov=json.loads(COVERAGE.read_text())
    cov=reconcile(cov,report,panel,sha(PANEL))
    COVERAGE.write_text(json.dumps(cov,indent=2))
    result={"status":"RECONCILED_WITH_DATA_QUALITY_WARNING","source":"global_freight_shipping",
      "nse_sessions":200,"distinct_chokepoints":28,"observed_nse_session_keys":5432,
      "expected_nse_session_keys":5600,"missing_nse_session_keys":168,
      "coverage_pct":97.0,"hard_gate_rows":0,"factor_state_promotion":False,
      "source_sha256":sha(PANEL)}
    Path("outputs/macro_geo/global_freight_shipping_source_coverage_reconciliation.json").write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
