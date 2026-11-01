#!/usr/bin/env python3
"""Build a provenance-preserving monthly RBI DBIE SGL yield curve adapter."""
import csv, hashlib, json, calendar
from datetime import datetime, timezone
from pathlib import Path
import requests

API="https://data-api.dbie.rbihub.in/api/tables/financial_markets/r217_month_end_yield_of_sgl_transactions_in_government_dated_se"
CSV_URL=API+"/csv"
OUT=Path("artifacts/india_bond_yields")
RAW=OUT/"rbi_dbie_raw.csv"
META=OUT/"rbi_dbie_table_metadata.json"
NORMAL=OUT/"india_bond_yields.csv"
REPORT=OUT/"rbi_dbie_source_adapter_report.json"
FIELDS=["DATE","COUNTRY","INSTRUMENT","TERM_YEARS","YIELD_PCT","UNIT","FREQUENCY","SOURCE","SOURCE_URL","OBSERVED_AT_UTC","RELEASED_AT","RELEASE_STATUS"]
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def month_end(value):
    d=datetime.strptime(value.strip(),"%b-%Y")
    return datetime(d.year,d.month,calendar.monthrange(d.year,d.month)[1]).date().isoformat()
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    s=requests.Session(); s.headers.update({"User-Agent":"PRECISION-WIRES-NSE200-COLLECTOR/1.0"})
    mr=s.get(API,timeout=(8,25)); mr.raise_for_status()
    cr=s.get(CSV_URL,timeout=(8,40)); cr.raise_for_status()
    META.write_bytes(mr.content); RAW.write_bytes(cr.content)
    metadata=json.loads(mr.content)
    data=metadata.get("data",{}); provenance=metadata.get("provenance",{})
    if data.get("frequency","").lower()!="monthly": raise RuntimeError("Unexpected DBIE frequency")
    if data.get("report_id")!=217 or data.get("width")!=32: raise RuntimeError("Unexpected DBIE report identity/width")
    tabs={x.get("name"):x for x in provenance.get("tabs",[])}
    if "New Format" not in tabs: raise RuntimeError("DBIE metadata does not identify New Format tab")
    raw=list(csv.DictReader(RAW.open(newline="",encoding="utf-8-sig")))
    new=[r for r in raw if r.get("tab")=="New Format"]
    if len(new)!=375: raise RuntimeError(f"Expected 375 New Format grid rows; got {len(new)}")
    header1=next((r for r in new if r.get("row_no")=="6"),None)
    header2=next((r for r in new if r.get("row_no")=="7"),None)
    if not header1 or header1.get("c1","").strip()!="Year/Month" or header1.get("c2","").strip()!="Term to maturity":
        raise RuntimeError("New Format primary header mismatch")
    expected={f"c{i}":f"{i-1} Year" if i==2 else f"{i-1} Years" for i in range(2,32)}
    actual={f"c{i}":header2.get(f"c{i}","").strip() for i in range(2,33)}
    if any(actual[k]!=v for k,v in expected.items()) or actual["c32"]:
        raise RuntimeError("New Format maturity header map mismatch: "+repr(actual))
    observed=datetime.now(timezone.utc).isoformat()
    out=[]; seen=set(); month_dates=set(); missing_by_tenor={str(i-1):0 for i in range(2,32)}
    invalid=0
    for r in new:
        try: date=month_end(r.get("c1",""))
        except ValueError: continue
        if date in month_dates: raise RuntimeError("Duplicate month in New Format tab: "+date)
        month_dates.add(date)
        for col,tenor_label in expected.items():
            value=(r.get(col) or "").strip().replace(",","")
            if not value or value in ("-","NA","N/A"):
                missing_by_tenor[str(int(col[1:])-1)]+=1
                continue
            try: y=float(value)
            except ValueError: invalid+=1; raise RuntimeError("Non-numeric yield at "+date+" "+tenor_label)
            if not (0<y<30): invalid+=1; raise RuntimeError("Out-of-domain yield at "+date+" "+tenor_label)
            tenor=int(col[1:])-1; key=(date,tenor)
            if key in seen: raise RuntimeError("Duplicate date/tenor key "+repr(key))
            seen.add(key)
            out.append({"DATE":date,"COUNTRY":"IN","INSTRUMENT":"CENTRAL_GOVERNMENT_DATED_SECURITY_SGL_MONTH_END",
              "TERM_YEARS":tenor,"YIELD_PCT":f"{y:.4f}","UNIT":"PERCENT_PER_ANNUM","FREQUENCY":"MONTHLY",
              "SOURCE":"Reserve Bank of India, Database on Indian Economy",
              "SOURCE_URL":CSV_URL,"OBSERVED_AT_UTC":observed,"RELEASED_AT":"",
              "RELEASE_STATUS":"UNKNOWN_NOT_SUPPLIED_PER_OBSERVATION"})
    if len(month_dates)!=365 or min(month_dates)!="1996-04-30" or max(month_dates)!="2026-08-31":
        raise RuntimeError(f"Unexpected month coverage: {len(month_dates)} {min(month_dates)}..{max(month_dates)}")
    if len(out)!=9477 or len(seen)!=len(out) or invalid:
        raise RuntimeError(f"Unexpected row-level QA: rows={len(out)}, unique={len(seen)}, invalid={invalid}")
    out.sort(key=lambda x:(x["DATE"],x["TERM_YEARS"]))
    with NORMAL.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(out)
    report={"status":"RBI_DBIE_MONTHLY_ADAPTER_PASS_EVIDENCE_ONLY","source_api":API,"source_csv":CSV_URL,
      "report_id":217,"tab":"New Format","frequency":"MONTHLY","date_min":min(month_dates),"date_max":max(month_dates),
      "distinct_months":len(month_dates),"mapped_columns":{k:v for k,v in expected.items()},
      "excluded_column":"c32 (blank in New Format header row)","source_raw_rows":len(raw),"new_format_grid_rows":len(new),
      "normalized_rows":len(out),"distinct_tenors":list(range(1,31)),"duplicate_date_tenor_keys":0,
      "invalid_numeric_rows":invalid,"missing_values_by_tenor":missing_by_tenor,
      "release_timestamp_status":"UNKNOWN_NOT_SUPPLIED_PER_OBSERVATION","observed_at_utc":observed,
      "raw_csv_sha256":sha(RAW),"metadata_sha256":sha(META),"normalized_csv_sha256":sha(NORMAL),
      "factor_registry_promotion":"NOT_PROMOTED_PENDING_CANONICAL_SCHEMA_AND_RELEASE_PROVENANCE_AUDIT",
      "scope_boundary":"RBI month-end SGL yield curve; not daily FBIL 10-year par-yield benchmark or auction cut-off yield."}
    REPORT.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
