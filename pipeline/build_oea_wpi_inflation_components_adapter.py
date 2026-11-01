#!/usr/bin/env python3
"""Build full-schema inflation_components rows from OEA WPI snapshot with honest provenance."""
import csv, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
BASE=Path("artifacts/macro_full_history_discovery")
EVIDENCE=Path("data/reference/oea_wpi_release_status_evidence.json")
OUT=BASE/"inflation_components.csv"
REPORT=BASE/"oea_wpi_inflation_components_adapter.json"
FIELDS=["DATE","COUNTRY","COMPONENT","VALUE","RELEASED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC",
        "ITEM_CODE","ITEM_LABEL","REVISION_STATUS","REVISION_EVIDENCE_SCOPE","SOURCE_ROW","SOURCE_SHEET"]
def main():
    manifest=json.loads((BASE/"oea_wpi_itemwise_manifest.json").read_text())
    evidence=json.loads(EVIDENCE.read_text())
    cross=json.loads((BASE/"oea_wpi_release_status_crosswalk.json").read_text())
    observed_at=manifest["retrieved_at_utc"]
    # The complete 2022-23 back-series was first publicly disseminated on 15 June 2026.
    # This is a source-level vintage timestamp, not an item-specific revision timestamp.
    backseries_release="2026-06-15T12:00:00+05:30"
    status_by_period={r["period"]:r["revision_status"] for r in csv.DictReader((BASE/"oea_wpi_release_status_crosswalk.csv").open(encoding="utf-8"))}
    input_path=BASE/manifest["normalized_csv"]["file"]
    rows=[]
    with input_path.open(newline="",encoding="utf-8") as f:
        for r in csv.DictReader(f):
            p=r["period"]
            # For all historic monthly rows, only the back-series dissemination time is
            # proven. Later month-specific press releases prove aggregate status, not
            # item-level value revisions; preserve that distinction explicitly.
            rows.append({
              "DATE":p+"-01","COUNTRY":"IN","COMPONENT":r["item_label"] or r["item_code"] or "UNSPECIFIED_ITEM",
              "VALUE":r["value"],"RELEASED_AT":backseries_release,
              "SOURCE":"Office of Economic Adviser, DPIIT, Government of India",
              "SOURCE_URL":manifest["source"]["url"],"OBSERVED_AT_UTC":observed_at,
              "ITEM_CODE":r["item_code"] or "","ITEM_LABEL":r["item_label"] or "",
              "REVISION_STATUS":status_by_period.get(p,"UNKNOWN"),
              "REVISION_EVIDENCE_SCOPE":"MONTH_LEVEL_ONLY; ITEM_LEVEL_REVISION_HISTORY_NOT_PUBLISHED",
              "SOURCE_ROW":r["source_row"],"SOURCE_SHEET":r["source_sheet"]})
    with OUT.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
    digest=hashlib.sha256(OUT.read_bytes()).hexdigest()
    report={"status":"INFLATION_COMPONENTS_ADAPTER_PASS_SCHEMA_COMPLETE",
      "rows":len(rows),"fields":FIELDS,"required_fields_present":True,
      "released_at_semantics":"Official first public dissemination of the OEA 2022-23 back-series; source-level vintage, not per-item revision timestamp.",
      "observed_at_semantics":"Actual collector retrieval timestamp copied from the successful itemwise ingestion manifest.",
      "revision_history_boundary":"PIB/OEA evidence reviewed here is month-level aggregate status only. Item-wise revision history is not published in the reviewed sources; item-level revision status remains UNKNOWN where no direct evidence exists.",
      "source_url":manifest["source"]["url"],"release_evidence_url":"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2272872&lang=1&reg=3",
      "rows_sha256":digest,"promotion":"SOURCE_EVIDENCE_ONLY_NOT_PROMOTED"}
    REPORT.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
