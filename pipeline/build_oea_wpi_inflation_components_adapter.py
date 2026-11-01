#!/usr/bin/env python3
"""Build full-schema inflation_components rows from OEA WPI snapshot with honest provenance."""
import csv, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
BASE=Path("artifacts/macro_full_history_discovery")
EVIDENCE=Path("data/reference/oea_wpi_release_status_evidence.json")
OUT=BASE/"inflation_components.csv"
CANONICAL=Path("data/external/inflation_components.csv")
REPORT=BASE/"oea_wpi_inflation_components_adapter.json"
FIELDS=["DATE","COUNTRY","COMPONENT","VALUE","RELEASED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC",
        "ITEM_CODE","ITEM_LABEL","REVISION_STATUS","REVISION_EVIDENCE_SCOPE","RELEASE_EVIDENCE_URL","RELEASED_AT_SCOPE","SOURCE_ROW","SOURCE_SHEET"]
def main():
    manifest=json.loads((BASE/"oea_wpi_itemwise_manifest.json").read_text())
    evidence=json.loads(EVIDENCE.read_text())
    cross=json.loads((BASE/"oea_wpi_release_status_crosswalk.json").read_text())
    observed_at=manifest["retrieved_at_utc"]
    # Official PIB releases establish publication timestamps at month level, not per item.
    # Back-series months Apr-2023..Mar-2026 were disseminated on 15 Jun 2026; later
    # months use the exact PIB monthly release that supplied the latest observed status/value vintage.
    backseries_release="2026-06-15T12:00:00+05:30"
    release_events={
      "2026-04":("2026-07-14T12:00:00+05:30","https://www.pib.gov.in/PressReleasePage.aspx?PRID=2284374&lang=2&reg=48"),
      "2026-05":("2026-08-14T12:00:00+05:30","https://www.pib.gov.in/PressReleasePage.aspx?PRID=2299305&lang=2&reg=48"),
      "2026-06":("2026-09-14T12:01:00+05:30","https://www.pib.gov.in/PressReleasePage.aspx?PRID=2309977&lang=2&reg=48"),
      "2026-07":("2026-10-14T12:00:00+05:30","https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2323098&lang=1&reg=1"),
      "2026-08":("2026-09-14T12:01:00+05:30","https://www.pib.gov.in/PressReleasePage.aspx?PRID=2309977&lang=2&reg=48"),
      "2026-09":("2026-10-14T12:00:00+05:30","https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2323098&lang=1&reg=1")
    }
    backseries_url="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2272872&lang=1&reg=3"
    status_by_period={r["period"]:r["revision_status"] for r in csv.DictReader((BASE/"oea_wpi_release_status_crosswalk.csv").open(encoding="utf-8"))}
    input_path=BASE/manifest["normalized_csv"]["file"]
    rows=[]
    with input_path.open(newline="",encoding="utf-8") as f:
        for r in csv.DictReader(f):
            p=r["period"]
            # For all historic monthly rows, only the back-series dissemination time is
            # proven. Later month-specific press releases prove aggregate status, not
            # item-level value revisions; preserve that distinction explicitly.
            if p in release_events:
                released_at, release_url = release_events[p]
            elif p <= "2026-03":
                released_at, release_url = backseries_release, backseries_url
            else:
                released_at, release_url = "", ""
            rows.append({
              "DATE":p+"-01","COUNTRY":"IN","COMPONENT":r["item_label"] or r["item_code"] or "UNSPECIFIED_ITEM",
              "VALUE":r["value"],"RELEASED_AT":released_at,
              "SOURCE":"Office of Economic Adviser, DPIIT, Government of India",
              "SOURCE_URL":manifest["source"]["url"],"OBSERVED_AT_UTC":observed_at,
              "ITEM_CODE":r["item_code"] or "","ITEM_LABEL":r["item_label"] or "",
              "REVISION_STATUS":status_by_period.get(p,"UNKNOWN"),
              "REVISION_EVIDENCE_SCOPE":"MONTH_LEVEL_ONLY; ITEM_LEVEL_REVISION_HISTORY_NOT_PUBLISHED",
              "RELEASE_EVIDENCE_URL":release_url,
              "RELEASED_AT_SCOPE":"OFFICIAL_MONTH_LEVEL_RELEASE_TIME_NOT_ITEM_LEVEL_TIMESTAMP",
              "SOURCE_ROW":r["source_row"],"SOURCE_SHEET":r["source_sheet"]})
    with OUT.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
    CANONICAL.parent.mkdir(parents=True,exist_ok=True)
    with CANONICAL.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
    if any(not row["RELEASED_AT"] or not row["RELEASE_EVIDENCE_URL"] for row in rows):
        raise RuntimeError("A WPI observation lacks a verified month-level release timestamp/source; refusing blank or inferred timestamps")
    digest=hashlib.sha256(OUT.read_bytes()).hexdigest()
    canonical_digest=hashlib.sha256(CANONICAL.read_bytes()).hexdigest()
    if digest != canonical_digest: raise RuntimeError("Canonical adapter output hash mismatch")
    report={"status":"INFLATION_COMPONENTS_ADAPTER_PASS_SCHEMA_COMPLETE",
      "rows":len(rows),"fields":FIELDS,"required_fields_present":True,
      "month_level_release_timestamp_rows":sum(1 for row in rows if row["RELEASED_AT"]),
      "item_level_timestamp_claimed":False,
      "released_at_semantics":"Exact official PIB publication time for the relevant monthly release; back-series months use the 15 June 2026 release. This is month-level publication time, not item-specific revision time.",
      "observed_at_semantics":"Actual collector retrieval timestamp copied from the successful itemwise ingestion manifest.",
      "revision_history_boundary":"PIB/OEA evidence reviewed here is month-level aggregate status only. Item-wise revision history is not published in the reviewed sources; item-level revision status remains UNKNOWN where no direct evidence exists.",
      "source_url":manifest["source"]["url"],"release_evidence_urls":["https://www.pib.gov.in/PressReleasePage.aspx?PRID=2272872&lang=1&reg=3","https://www.pib.gov.in/PressReleasePage.aspx?PRID=2284374&lang=2&reg=48","https://www.pib.gov.in/PressReleasePage.aspx?PRID=2299305&lang=2&reg=48","https://www.pib.gov.in/PressReleasePage.aspx?PRID=2309977&lang=2&reg=48","https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2323098&lang=1&reg=1"],
      "rows_sha256":digest,"canonical_path":str(CANONICAL),"canonical_sha256":canonical_digest,"promotion":"SOURCE_EVIDENCE_ONLY_NOT_PROMOTED"}
    REPORT.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
