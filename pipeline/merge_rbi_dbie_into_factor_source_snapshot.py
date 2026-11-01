#!/usr/bin/env python3
"""Attach RBI DBIE 10Y monthly evidence to an exact factor snapshot without promotion."""
import csv,hashlib,json
from pathlib import Path
BASE=Path("artifacts/factor_source_baseline/outputs/macro_geo/source_coverage.json")
ADAPTER=Path("artifacts/rbi_adapter/india_bond_yields.csv")
REPORT=Path("artifacts/rbi_adapter/rbi_dbie_source_adapter_report.json")
OUT=Path("outputs/macro_geo/source_coverage.json")
CANON=Path("data/external/india_bond_yields.csv")
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    if not all(p.is_file() for p in (BASE,ADAPTER,REPORT)):
        raise SystemExit("Missing pinned baseline or successful RBI adapter artifact; refusing substitute data")
    baseline=json.loads(BASE.read_text()); report=json.loads(REPORT.read_text())
    if report.get("status")!="RBI_DBIE_MONTHLY_ADAPTER_PASS_EVIDENCE_ONLY":
        raise SystemExit("RBI adapter report is not PASS")
    if sha(ADAPTER)!=report.get("normalized_csv_sha256"):
        raise SystemExit("RBI adapter SHA-256 mismatch")
    with ADAPTER.open(newline="",encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    ten=[r for r in rows if r["TERM_YEARS"]=="10"]
    if len(ten)!=361: raise SystemExit(f"Unexpected 10Y month-end row count: {len(ten)}")
    fields=["DATE","YIELD_10Y","UNIT","FREQUENCY","SOURCE","SOURCE_SERIES","SOURCE_URL","OBSERVED_AT_UTC","RELEASED_AT","RELEASE_STATUS"]
    CANON.parent.mkdir(parents=True,exist_ok=True)
    with CANON.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for r in ten:
            w.writerow({"DATE":r["DATE"],"YIELD_10Y":r["YIELD_PCT"],"UNIT":r["UNIT"],
              "FREQUENCY":"MONTHLY","SOURCE":r["SOURCE"],"SOURCE_SERIES":"RBI_DBIE_MONTH_END_SGL_YTM_10Y",
              "SOURCE_URL":r["SOURCE_URL"],"OBSERVED_AT_UTC":r["OBSERVED_AT_UTC"],
              "RELEASED_AT":"","RELEASE_STATUS":"UNKNOWN_NOT_SUPPLIED_PER_OBSERVATION"})
    snapshot=json.loads(BASE.read_text())
    sources=snapshot.get("sources",[])
    target=next((x for x in sources if isinstance(x,dict) and x.get("source")=="india_bond_yields"),None)
    if target is None: raise SystemExit("india_bond_yields group absent from pinned 36-source baseline")
    # It is connected as an observed monthly data file, but not AVAILABLE for
    # factor hard gates: no original per-observation release timestamp and not daily.
    target.update({"status":"DATA_QUALITY_WARN","selected_path":"",
      "rows":0,"observed_rows":len(ten),"date_min":min(r["DATE"] for r in ten),
      "date_max":max(r["DATE"] for r in ten),
      "missing_columns":["RELEASED_AT (not supplied per observation)","DAILY_YIELD_10Y_BENCHMARK (source is monthly SGL curve)"],
      "evidence_path":str(CANON),"evidence_sha256":sha(CANON),
      "source":"Reserve Bank of India, Database on Indian Economy",
      "source_series":"RBI_DBIE_MONTH_END_SGL_YTM_10Y","frequency":"MONTHLY",
      "notes":"361 observed 10Y month-end SGL yields from official New Format tab. Not equivalent to daily FBIL par-yield benchmark. Original per-observation release timestamps are not supplied; retained as DATA_QUALITY_WARN and not counted as connected for factor hard gates."})
    snapshot["as_of_utc"]=report["observed_at_utc"]
    snapshot["snapshot_augmentation"]={"baseline_run_id":41282726166,
      "baseline_head_sha":"a7dd9161b887b7f79111e610291b1e0935379aa7",
      "baseline_source_coverage_sha256":sha(BASE),
      "added_evidence":"RBI DBIE monthly SGL yield curve; only india_bond_yields row annotated",
      "rbi_adapter_run_id":41314656919,
      "rbi_adapter_head_sha":"46dd002b279a3a63fa102096a53a72a716741670",
      "rbi_adapter_sha256":report["normalized_csv_sha256"],
      "rbi_10y_rows":len(ten),"rbi_10y_frequency":"MONTHLY",
      "promotion":"NOT_PROMOTED; release timestamp unknown and daily benchmark mismatch"}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(snapshot,indent=2)+"\n")
    print(json.dumps({"status":"RBI_EVIDENCE_ATTACHED_TO_EXACT_FACTOR_SNAPSHOT_NO_PROMOTION",
      "baseline_sha256":sha(BASE),"augmented_snapshot_sha256":sha(OUT),
      "source_groups":len(sources),"india_bond_yields_status":target["status"],
      "observed_10y_months":len(ten),"factor_gate_eligible_rows":0,
      "other_source_rows_unchanged":True},indent=2))
if __name__=="__main__": main()
