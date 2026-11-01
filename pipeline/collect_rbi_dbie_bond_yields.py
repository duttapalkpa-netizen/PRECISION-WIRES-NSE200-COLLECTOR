#!/usr/bin/env python3
"""Collect RBI DBIE month-end G-Sec yield curve; monthly data is never labelled daily."""
import csv, hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
import requests
API="https://data-api.dbie.rbihub.in/api/tables/financial_markets/r217_month_end_yield_of_sgl_transactions_in_government_dated_se"
CSV_URL=API+"/csv"
OUT=Path("artifacts/india_bond_yields/rbi_dbie_month_end_gsec_yields.csv")
REPORT=Path("artifacts/india_bond_yields/rbi_dbie_source_adapter_report.json")
FIELDS=["DATE","COUNTRY","INSTRUMENT","TERM_YEARS","YIELD_PCT","UNIT","FREQUENCY","SOURCE","SOURCE_URL","OBSERVED_AT_UTC","RELEASED_AT","RELEASE_STATUS"]
def period_date(v):
    s=str(v).strip()
    for fmt in ("%b-%Y","%B-%Y","%b %Y","%B %Y","%Y-%m","%Y-%m-%d"):
        try:
            d=datetime.strptime(s,fmt)
            if fmt in ("%b-%Y","%B-%Y","%b %Y","%B %Y","%Y-%m"): 
                import calendar
                return datetime(d.year,d.month,calendar.monthrange(d.year,d.month)[1]).date().isoformat()
            return d.date().isoformat()
        except ValueError: pass
    return None
def main():
    s=requests.Session(); s.headers.update({"User-Agent":"PRECISION-WIRES-NSE200-COLLECTOR/1.0"})
    meta=s.get(API,timeout=(8,25)); meta.raise_for_status(); metadata=meta.json()
    response=s.get(CSV_URL,timeout=(8,40)); response.raise_for_status()
    text=response.content.decode("utf-8-sig")
    raw=list(csv.reader(text.splitlines()))
    if len(raw)<3: raise RuntimeError("DBIE CSV unexpectedly short")
    headers=[x.strip() for x in raw[0]]
    # Identify month-period and maturity columns from the actual published CSV header.
    period_idx=next((i for i,h in enumerate(headers) if re.search(r"year.?/?month|period|month",h,re.I)),None)
    if period_idx is None: period_idx=0
    tenor_cols=[]
    for i,h in enumerate(headers):
        m=re.search(r"^(\d{1,2})\s*years?$",h,re.I)
        if m: tenor_cols.append((i,int(m.group(1))))
    if len(tenor_cols)<5:
        raise RuntimeError("DBIE schema mismatch: expected maturity columns such as 1 Year..10 Years; headers="+repr(headers))
    observed=datetime.now(timezone.utc).isoformat()
    rows=[]
    for line_no,row in enumerate(raw[1:],start=2):
        if len(row)<len(headers): continue
        date=period_date(row[period_idx])
        if not date: continue
        for idx,tenor in tenor_cols:
            value=row[idx].strip().replace(",","")
            if not value or value in ("-","NA","N/A"): continue
            try: y=float(value)
            except ValueError: raise RuntimeError(f"Non-numeric yield at CSV row {line_no}, tenor {tenor}")
            if not (0 < y < 30): raise RuntimeError(f"Out-of-domain yield {y} at CSV row {line_no}")
            rows.append({"DATE":date,"COUNTRY":"IN","INSTRUMENT":"CENTRAL_GOVERNMENT_DATED_SECURITY_SGL_MONTH_END",
              "TERM_YEARS":tenor,"YIELD_PCT":y,"UNIT":"PERCENT_PER_ANNUM","FREQUENCY":"MONTHLY",
              "SOURCE":"Reserve Bank of India, Database on Indian Economy",
              "SOURCE_URL":CSV_URL,"OBSERVED_AT_UTC":observed,"RELEASED_AT":"",
              "RELEASE_STATUS":"UNKNOWN_RELEASE_TIMESTAMP_NOT_SUPPLIED_BY_DBIE"})
    if not rows: raise RuntimeError("No valid DBIE month-end yield rows parsed")
    keys=[(r["DATE"],r["TERM_YEARS"]) for r in rows]
    if len(keys)!=len(set(keys)): raise RuntimeError("Duplicate month/tenor keys in DBIE response")
    rows.sort(key=lambda r:(r["DATE"],r["TERM_YEARS"]))
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
    digest=hashlib.sha256(OUT.read_bytes()).hexdigest()
    report={"status":"RBI_DBIE_MONTH_END_GSEC_ADAPTER_PASS_EVIDENCE_ONLY","rows":len(rows),
      "distinct_months":len(set(r["DATE"] for r in rows)),"distinct_tenors":sorted(set(r["TERM_YEARS"] for r in rows)),
      "date_min":min(r["DATE"] for r in rows),"date_max":max(r["DATE"] for r in rows),
      "frequency":"MONTHLY","instrument_scope":"RBI SGL transactions in central government dated securities; month-end residual maturity curve.",
      "not_equivalent_to":"Daily FBIL 10-year par-yield benchmark or auction cut-off yield.",
      "released_at":"UNKNOWN; DBIE CSV/API does not expose per-observation original release timestamps in the retrieved payload.",
      "observed_at_utc":observed,"source_api":API,"source_csv":CSV_URL,
      "metadata_title":metadata.get("title"),"metadata_provenance":metadata.get("provenance"),
      "csv_sha256":digest,"factor_registry_promotion":"NOT_PROMOTED_PENDING_CANONICAL_SCHEMA_AND_RELEASE_PROVENANCE_AUDIT"}
    REPORT.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
