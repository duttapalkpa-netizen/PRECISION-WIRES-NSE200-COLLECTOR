#!/usr/bin/env python3
"""Build conservative monthly WPI revision-status crosswalk from official PIB evidence."""
import csv, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(".")
BASE=ROOT/"artifacts/macro_full_history_discovery"
EVIDENCE=ROOT/"data/reference/oea_wpi_release_status_evidence.json"
MANIFEST=BASE/"oea_wpi_itemwise_manifest.json"
OBS=BASE/"OEA_WPI_2022-23_itemwise_monthly_observations.csv"
OUT=BASE/"oea_wpi_release_status_crosswalk.csv"
REPORT=BASE/"oea_wpi_release_status_crosswalk.json"

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def build_crosswalk(manifest, evidence, observations):
    observed={}
    for row in observations:
        p=row["period"]
        x=observed.setdefault(p,{"observation_rows":0,"distinct_item_codes":set(),"missing_code_rows":0})
        x["observation_rows"]+=1
        if row.get("item_code"): x["distinct_item_codes"].add(row["item_code"])
        else: x["missing_code_rows"]+=1
    periods=list(manifest["workbook"]["periods"])
    if not periods: raise ValueError("No observed WPI periods")
    requested=evidence["release_schedule"]["2026-10"]
    if "2026-10" in periods:
        raise ValueError("October 2026 observations present despite official release schedule; require review")
    result=[]
    for p in periods+["2026-10"]:
        stats=observed.get(p,{"observation_rows":0,"distinct_item_codes":set(),"missing_code_rows":0})
        if p in evidence["official_month_status"]:
            status=evidence["official_month_status"][p]
            basis="PIB_ANNEXURE_EXPLICIT_F_OR_P"
        elif p=="2026-10":
            status=requested["status"]
            basis="PIB_RELEASE_SCHEDULE; NO_OBSERVATION_EXPECTED_YET"
        else:
            status="UNKNOWN_NOT_COVERED_BY_REVIEWED_RELEASE"
            basis="NO_MONTH_SPECIFIC_OFFICIAL_REVISION_EVIDENCE_IN_REVIEWED_RELEASE"
        result.append({
          "period":p,"revision_status":status,"status_evidence_basis":basis,
          "observation_rows":stats["observation_rows"],
          "distinct_item_codes":len(stats["distinct_item_codes"]),
          "missing_item_code_rows":stats["missing_code_rows"],
          "official_source_url":evidence["source_url"],
          "official_source_published_date":evidence["published_date"],
          "scheduled_release_date":requested["scheduled_release_date"] if p=="2026-10" else ""
        })
    return result

def main():
    if not all(x.exists() for x in (EVIDENCE,MANIFEST,OBS)):
        raise SystemExit("Missing WPI source evidence, ingestion manifest or normalized observations")
    evidence=json.loads(EVIDENCE.read_text())
    manifest=json.loads(MANIFEST.read_text())
    if manifest.get("status")!="ITEMWISE_INGESTION_PASS":
        raise SystemExit("Itemwise WPI ingestion is not PASS")
    with OBS.open(newline="",encoding="utf-8") as f: observations=list(csv.DictReader(f))
    if len(observations)!=manifest["workbook"]["observation_count"]:
        raise SystemExit("Normalized observation count does not match ingestion manifest")
    rows=build_crosswalk(manifest,evidence,observations)
    fields=list(rows[0])
    with OUT.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
    status_counts={}
    for r in rows: status_counts[r["revision_status"]]=status_counts.get(r["revision_status"],0)+1
    report={
      "status":"WPI_RELEASE_STATUS_CROSSWALK_PASS",
      "generated_at_utc":datetime.now(timezone.utc).isoformat(),
      "source_evidence":evidence,
      "input_manifest_sha256":sha(MANIFEST),
      "input_raw_workbook_sha256":manifest["source"]["raw_sha256"],
      "input_normalized_csv_sha256":manifest["normalized_csv"]["sha256"],
      "crosswalk_csv_sha256":sha(OUT),
      "crosswalk_rows":len(rows),
      "status_counts":status_counts,
      "october_2026":{"status":evidence["release_schedule"]["2026-10"]["status"],
        "scheduled_release_date":evidence["release_schedule"]["2026-10"]["scheduled_release_date"],
        "observation_rows":next(r["observation_rows"] for r in rows if r["period"]=="2026-10")},
      "promotion":"SOURCE_EVIDENCE_ONLY_NOT_PROMOTED_TO_FACTOR_REGISTRY",
      "safety":"Month-level official revision status only. Unreviewed months remain UNKNOWN; no status inferred for item-level rows."
    }
    REPORT.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"status":report["status"],"crosswalk_rows":len(rows),
      "status_counts":status_counts,"october_2026":report["october_2026"],
      "crosswalk_csv_sha256":report["crosswalk_csv_sha256"]},indent=2))
if __name__=="__main__": main()
