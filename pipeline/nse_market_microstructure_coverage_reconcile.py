#!/usr/bin/env python3
"""Conservatively reconcile 200-session NSE market-microstructure evidence.

Raw official joins are preserved. Unknown circuit/surveillance/free-float values
remain UNKNOWN and the source group is DATA_QUALITY_WARN, never AVAILABLE.
"""
from pathlib import Path
import hashlib, json
import pandas as pd

ROOT=Path(".")
PANEL=ROOT/"data/external/market_microstructure.csv"
QA=ROOT/"outputs/macro_geo/market_microstructure_200_session_qa.json"
COVERAGE=ROOT/"outputs/macro_geo/source_coverage.json"

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def reconcile(coverage, report, panel, panel_sha):
    if report.get("status")!="PARTIAL_SOURCE_COVERAGE":
        raise ValueError("Market microstructure must remain partial until every blocker is closed")
    if report.get("sessions")!=200 or report.get("panel_rows")!=len(panel):
        raise ValueError("200-session panel row/session mismatch")
    if report.get("promotion_allowed") is not False:
        raise ValueError("Collector report unexpectedly allows promotion")
    if report.get("snapshot_id")!="1f6d79d9bcdf3a6aa11dd9a80033276061447401dac6c708ab6622b6258b7534":
        raise ValueError("Unexpected NSE snapshot identity")
    required={"DATE","SYMBOL","SERIES","CIRCUIT_STATUS","SURVEILLANCE_STATUS","FREE_FLOAT",
              "BHAVCOPY_SOURCE_URL","BHAVCOPY_SOURCE_SHA256","PRICE_BAND_SOURCE_URL",
              "PRICE_BAND_SOURCE_SHA256","REG_IND_SOURCE_URL","REG_IND_SOURCE_SHA256",
              "REG1_IND_SOURCE_URL","REG1_IND_SOURCE_SHA256"}
    if not required.issubset(panel.columns):
        raise ValueError("Market microstructure panel schema incomplete")
    if panel[["DATE","SYMBOL","SERIES"]].isna().any().any() or panel.duplicated(["DATE","SYMBOL","SERIES"]).any():
        raise ValueError("Market microstructure panel keys invalid")
    if panel["DATE"].nunique()!=200:
        raise ValueError("Expected exactly 200 distinct session dates")
    for col in ("BHAVCOPY_SOURCE_SHA256","PRICE_BAND_SOURCE_SHA256","REG_IND_SOURCE_SHA256","REG1_IND_SOURCE_SHA256"):
        if not panel[col].astype(str).str.fullmatch(r"[0-9a-f]{64}").all():
            raise ValueError(f"Invalid source SHA-256 in {col}")
    if not panel["BHAVCOPY_SOURCE_URL"].astype(str).str.startswith("https://archives.nseindia.com/products/content/").all():
        raise ValueError("Unexpected bhavcopy source URL")
    if not panel["CIRCUIT_STATUS"].eq("UNKNOWN").all() or not panel["SURVEILLANCE_STATUS"].eq("UNKNOWN").all() or not panel["FREE_FLOAT"].eq("UNKNOWN").all():
        raise ValueError("Unknown-state preservation mismatch")
    sources=coverage.setdefault("sources",[])
    item=next((x for x in sources if x.get("source")=="market_microstructure"),None)
    if item is None:
        item={"source":"market_microstructure"}; sources.append(item)
    item.update({
      "status":"DATA_QUALITY_WARN","rows":0,"observed_rows":int(len(panel)),
      "selected_path":"","evidence_path":str(PANEL),
      "missing_columns":["CIRCUIT_STATUS (validated hit/limit state)","SURVEILLANCE_STATUS (interpreted effective status)","FREE_FLOAT (security-level float history)","PUBLICATION_TIMESTAMP (not published in daily source files)"],
      "date_min":report["date_min"],"date_max":report["date_max"],
      "snapshot_id":report["snapshot_id"],"source_sha256":panel_sha,
      "bhavcopy_sha256_revalidated_sessions":report["bhavcopy_sha256_revalidated_sessions"],
      "price_band_files":report["price_band_files"],
      "surveillance_old_files":report["surveillance_old_files"],
      "surveillance_new_files":report["surveillance_new_files"],
      "price_band_join_coverage":report["price_band_join_coverage"],
      "reg_ind_join_coverage":report["reg_ind_join_coverage"],
      "reg1_ind_join_coverage":report["reg1_ind_join_coverage"],
      "circuit_status_unknown_rows":report["circuit_status_unknown_rows"],
      "surveillance_status_unknown_rows":report["surveillance_status_unknown_rows"],
      "free_float_unknown_rows":report["free_float_unknown_rows"],
      "observed_at_utc":report["observed_at_utc"],
      "notes":"200-session official-source raw join evidence verified. Price bands and REG_IND/REG1_IND raw indicators retained, but circuit status, interpreted surveillance status and free float remain UNKNOWN; source publication timestamps unavailable. Zero hard-gate rows until blockers are independently resolved.",
      "reason":"DATA_QUALITY_WARN: raw official evidence only; unknown fields are not promoted."
    })
    coverage["as_of_utc"]=report["observed_at_utc"]
    coverage["market_microstructure_reconciled_at_utc"]=report["observed_at_utc"]
    return coverage

def main():
    if not PANEL.is_file() or not QA.is_file() or not COVERAGE.is_file():
        raise SystemExit("BLOCKED_MISSING_INPUT_ARTIFACT")
    report=json.loads(QA.read_text())
    panel=pd.read_csv(PANEL,dtype=str).fillna("")
    panel_sha=sha(PANEL)
    cov=json.loads(COVERAGE.read_text())
    cov=reconcile(cov,report,panel,panel_sha)
    COVERAGE.write_text(json.dumps(cov,indent=2))
    result={"status":"RECONCILED_WITH_DATA_QUALITY_WARNING","source":"market_microstructure",
      "observed_rows":len(panel),"hard_gate_rows":0,"source_sha256":panel_sha,
      "sessions":report["sessions"],"price_band_join_coverage":report["price_band_join_coverage"],
      "reg_ind_join_coverage":report["reg_ind_join_coverage"],"reg1_ind_join_coverage":report["reg1_ind_join_coverage"],
      "unknown_circuit_status_rows":report["circuit_status_unknown_rows"],
      "unknown_surveillance_status_rows":report["surveillance_status_unknown_rows"],
      "unknown_free_float_rows":report["free_float_unknown_rows"],
      "factor_state_promotion":False}
    out=Path("outputs/macro_geo/market_microstructure_source_coverage_reconciliation.json")
    out.write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
