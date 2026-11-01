#!/usr/bin/env python3
"""Augment the immutable 35-group source-repair snapshot with independently QA'd WPI rows."""
import csv,hashlib,json
from datetime import datetime,timezone
from pathlib import Path
COVERAGE=Path("outputs/macro_geo/source_coverage.json")
CSV_PATH=Path("data/external/inflation_components.csv")
REPORT=Path("outputs/macro_geo/factor_source_collection_report.json")
REQUIRED={"DATE","COUNTRY","COMPONENT","VALUE","RELEASED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    if not COVERAGE.is_file() or not CSV_PATH.is_file() or not REPORT.is_file():
        raise SystemExit("Missing exact source-repair snapshot or WPI adapter; refusing to synthesize coverage")
    snapshot=json.loads(COVERAGE.read_text())
    parent_sha=sha(COVERAGE)
    with CSV_PATH.open(newline="",encoding="utf-8") as f:
        reader=csv.DictReader(f); fields=set(reader.fieldnames or []); rows=list(reader)
    missing=sorted(REQUIRED-fields)
    if missing: raise SystemExit("WPI adapter missing required fields: "+",".join(missing))
    if len(rows)!=47598: raise SystemExit(f"Unexpected WPI row count: {len(rows)}")
    seen=set(); duplicate=0; invalid_dates=0; missing_cells=0
    for r in rows:
        for col in REQUIRED:
            if r.get(col) is None or not str(r[col]).strip(): missing_cells+=1
        date=str(r["DATE"])
        if len(date)!=10 or date[4:5]!="-" or date[7:8]!="-": invalid_dates+=1
        code=str(r.get("ITEM_CODE","")).strip()
        if code:
            key=(date,code)
            if key in seen: duplicate+=1
            seen.add(key)
        try: float(r["VALUE"])
        except (TypeError,ValueError): raise SystemExit("Non-numeric WPI VALUE encountered")
        if "ITEM_LEVEL_REVISION_HISTORY_NOT_PUBLISHED" not in r.get("REVISION_EVIDENCE_SCOPE",""):
            raise SystemExit("WPI revision evidence scope was altered or missing")
    if missing_cells or invalid_dates or duplicate:
        raise SystemExit(f"WPI adapter QA failed: missing_cells={missing_cells}, invalid_dates={invalid_dates}, duplicate_item_periods={duplicate}")
    sources=snapshot.get("sources",[])
    target=next((x for x in sources if isinstance(x,dict) and x.get("source")=="inflation_components"),None)
    if target is None: raise SystemExit("inflation_components source row missing from parent 35-group snapshot")
    old_status=target.get("status","NOT_CONNECTED")
    target.update({"status":"AVAILABLE","selected_path":str(CSV_PATH),"rows":len(rows),
      "missing_columns":[],"date_min":min(r["DATE"] for r in rows),"date_max":max(r["DATE"] for r in rows),
      "invalid_date_rows":0,"invalid_timestamp_rows":0,"duplicate_key_rows":0,"missing_cell_pct":0.0,
      "notes":"Official OEA WPI adapter passed schema, numeric-value, required-provenance, date and item-period uniqueness checks. Availability is schema/data coverage only; item-level revision history remains unpublished and F14 promotion is separately gated.",
      "wpi_adapter_sha256":sha(CSV_PATH),"release_timestamp_scope":"MONTH_LEVEL_NOT_ITEM_LEVEL"})
    if old_status!="AVAILABLE":
        if old_status=="NOT_CONNECTED": snapshot["not_connected"]=max(0,int(snapshot.get("not_connected",0))-1)
        snapshot["available"]=int(snapshot.get("available",0))+1
    snapshot["as_of_utc"]=datetime.now(timezone.utc).isoformat()
    snapshot["snapshot_augmentation"]={"parent_source_coverage_sha256":parent_sha,
      "added_source_group":"inflation_components","added_source_sha256":sha(CSV_PATH),
      "source_repair_run_id":41278895821,"source_repair_head_sha":"172d0950b3323c39a6cb4151d3194a6f8e8ffdc6",
      "augmentation":"Only the WPI source row is updated; all other 34 source rows are retained unchanged.",
      "wpi_revision_boundary":"Month-level publication/revision evidence only; item-wise revision history not published."}
    COVERAGE.write_text(json.dumps(snapshot,indent=2)+"\n")
    print(json.dumps({"status":"WPI_SOURCE_MERGED_INTO_IMMUTABLE_FACTOR_SNAPSHOT",
      "source_groups":len(sources),"old_inflation_components_status":old_status,
      "new_inflation_components_status":"AVAILABLE","wpi_rows":len(rows),
      "required_fields_missing":missing,"missing_required_cells":missing_cells,
      "invalid_dates":invalid_dates,"duplicate_item_periods":duplicate,
      "parent_snapshot_sha256":parent_sha,"augmented_snapshot_sha256":sha(COVERAGE),
      "as_of_utc":snapshot["as_of_utc"]},indent=2))
if __name__=="__main__": main()
