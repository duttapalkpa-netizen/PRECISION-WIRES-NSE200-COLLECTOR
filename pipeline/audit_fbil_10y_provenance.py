#!/usr/bin/env python3
"""Fail-closed FBIL daily GOI par-yield provenance audit with response diagnostics."""
import csv, hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
import requests
from bs4 import BeautifulSoup

URL = "https://www.fbil.org.in/"
OUT = Path("artifacts/fbil_10y_provenance")
FIELDS = ["OBSERVATION_DATE","TENOR","YIELD_PCT","UNIT","COMPOUNDING","SOURCE","SOURCE_URL","PUBLISHED_AT_IST","RELEASED_AT_UTC","OBSERVED_AT_UTC","RELEASE_TIME_EVIDENCE","SOURCE_HTML_SHA256"]

def norm(value):
    return re.sub(r"[^a-z0-9]+", "", value.lower())

def parse_date(value):
    for fmt in ("%d %b %Y", "%d %B %Y", "%Y-%m-%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(value.strip(), fmt).date()
        except ValueError:
            pass
    return None

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    observed=datetime.now(timezone.utc).isoformat()
    response=requests.get(URL,headers={"User-Agent":"Mozilla/5.0 (compatible; PRECISION-WIRES provenance audit)"},timeout=(10,40))
    response.raise_for_status()
    raw=response.content
    (OUT/"fbil_official_page.html").write_bytes(raw)
    html_sha=hashlib.sha256(raw).hexdigest()
    soup=BeautifulSoup(raw,"html.parser")
    diagnostics={"http_status":response.status_code,"final_url":response.url,"content_type":response.headers.get("Content-Type"),
      "response_bytes":len(raw),"html_sha256":html_sha,"table_count":len(soup.find_all("table")),
      "tables":[],"candidate_rows":0,"matched_10yr_rows":0,"observed_at_utc":observed}
    found=[]
    for ti,table in enumerate(soup.find_all("table")):
        trs=table.find_all("tr")
        row_cells=[[c.get_text(" ",strip=True) for c in tr.find_all(["th","td"],recursive=False)] for tr in trs]
        row_cells=[x for x in row_cells if x]
        if not row_cells: continue
        header_index=None; mapping={}
        for ri,cells in enumerate(row_cells[:4]):
            keys=[norm(x) for x in cells]
            date_i=next((i for i,k in enumerate(keys) if k in ("date","observationdate")),None)
            time_i=next((i for i,k in enumerate(keys) if k in ("time","publishtime","publicationtime")),None)
            tenor_i=next((i for i,k in enumerate(keys) if k in ("tenor","maturity")),None)
            rate_i=next((i for i,k in enumerate(keys) if k in ("rate","ratepercent","yield","yieldpercent","paryield")),None)
            if None not in (date_i,time_i,tenor_i,rate_i):
                header_index=ri; mapping={"date":date_i,"time":time_i,"tenor":tenor_i,"rate":rate_i}; break
        diagnostics["tables"].append({"index":ti,"row_count":len(row_cells),"first_rows":row_cells[:2],"header_row":header_index,"column_map":mapping})
        if header_index is None: continue
        for cells in row_cells[header_index+1:]:
            diagnostics["candidate_rows"]+=1
            try:
                d=parse_date(cells[mapping["date"]])
                t=datetime.strptime(cells[mapping["time"]].strip(),"%I:%M:%S %p").time()
                tenor=re.sub(r"\s+","",cells[mapping["tenor"]]).upper()
                if d is None or tenor not in ("10YR","10YEAR","10YEARS"): continue
                y=float(cells[mapping["rate"]].replace(",",""))
                if not 0<y<30: continue
                local=datetime.combine(d,t,ZoneInfo("Asia/Kolkata"))
                found.append((local,y,cells[mapping["time"]].strip()))
            except (ValueError,IndexError):
                continue
    diagnostics["matched_10yr_rows"]=len(found)
    (OUT/"fbil_fetch_diagnostics.json").write_text(json.dumps(diagnostics,indent=2)+"\n")
    if not found:
        raise RuntimeError("No FBIL GOI Par Yield 10YR rows with publisher Date+Time found; diagnostics retained; refusing to infer timestamp")
    records=[]
    for local,y,_ in sorted(set(found),key=lambda x:x[0]):
        records.append({"OBSERVATION_DATE":local.date().isoformat(),"TENOR":"10YR","YIELD_PCT":f"{y:.4f}",
          "UNIT":"PERCENT_PER_ANNUM","COMPOUNDING":"SEMI_ANNUAL","SOURCE":"Financial Benchmarks India Limited",
          "SOURCE_URL":URL,"PUBLISHED_AT_IST":local.isoformat(),"RELEASED_AT_UTC":local.astimezone(timezone.utc).isoformat(),
          "OBSERVED_AT_UTC":observed,"RELEASE_TIME_EVIDENCE":"FBIL official page row Date+Time fields",
          "SOURCE_HTML_SHA256":html_sha})
    dates=[x["OBSERVATION_DATE"] for x in records]
    if len(dates)!=len(set(dates)): raise RuntimeError("Duplicate FBIL 10YR observation dates")
    with (OUT/"fbil_10y_daily.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(records)
    csv_sha=hashlib.sha256((OUT/"fbil_10y_daily.csv").read_bytes()).hexdigest()
    report={"status":"FBIL_DAILY_10Y_PUBLISHER_TIMESTAMP_AUDIT_PASS","source_url":URL,"source_html_sha256":html_sha,
      "normalized_csv_sha256":csv_sha,"rows":len(records),"date_min":min(dates),"date_max":max(dates),
      "distinct_dates":len(set(dates)),"release_timestamp_field":"Publisher Date + Time, Asia/Kolkata; converted to UTC",
      "frequency":"DAILY_ON_PUBLISHED_BUSINESS_DAYS","missing_days":"Not interpolated",
      "licensing_status":"WRITTEN_PERMISSION_REQUIRED_BEFORE_COMMERCIAL_OR_PRODUCTION_USE",
      "factor_registry_promotion":"NOT_PROMOTED_PENDING_WRITTEN_USE_PERMISSION_AND_CANONICAL_SOURCE_REVIEW",
      "observed_at_utc":observed}
    (OUT/"fbil_10y_provenance_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
