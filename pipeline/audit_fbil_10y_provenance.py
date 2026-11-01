#!/usr/bin/env python3
"""Audit FBIL daily GOI par-yield page and retain publisher-provided release timestamps."""
import csv, hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
import requests
from bs4 import BeautifulSoup

URL = "https://www.fbil.org.in/"
OUT = Path("artifacts/fbil_10y_provenance")
FIELDS = ["OBSERVATION_DATE","TENOR","YIELD_PCT","UNIT","COMPOUNDING","SOURCE","SOURCE_URL","PUBLISHED_AT_IST","RELEASED_AT_UTC","OBSERVED_AT_UTC","RELEASE_TIME_EVIDENCE","SOURCE_HTML_SHA256"]
def main():
    r=requests.get(URL,headers={"User-Agent":"Mozilla/5.0 PRECISION-WIRES source audit"},timeout=(10,40))
    r.raise_for_status()
    html=r.content
    soup=BeautifulSoup(html,"html.parser")
    tables=soup.find_all("table")
    found=[]
    for table in tables:
        heads=[x.get_text(" ",strip=True).lower() for x in table.find_all("th")]
        if not heads: continue
        if not all(any(k in h for h in heads) for k in ("date","time","tenor")): continue
        for tr in table.find_all("tr"):
            cells=[x.get_text(" ",strip=True) for x in tr.find_all(["td","th"])]
            if len(cells)<4: continue
            # Publisher table order is Date | Time | Tenor | Rate(%) | Comments.
            if not re.fullmatch(r"\d{1,2} [A-Za-z]{3} \d{4}",cells[0]): continue
            tenor=re.sub(r"\s+","",cells[2]).upper()
            if tenor not in ("10YR","10YEAR","10YEARS"): continue
            try:
                date=datetime.strptime(cells[0],"%d %b %Y").date()
                tm=datetime.strptime(cells[1].strip(),"%I:%M:%S %p").time()
                y=float(cells[3].replace(",",""))
            except (ValueError,IndexError):
                continue
            if not 0<y<30: raise RuntimeError("10YR yield outside allowed domain")
            local=datetime.combine(date,tm,ZoneInfo("Asia/Kolkata"))
            found.append((local,y,cells[1].strip()))
    if not found:
        raise RuntimeError("No FBIL GOI Par Yield 10YR rows with publisher Date+Time found; refusing to infer timestamp")
    observed=datetime.now(timezone.utc).isoformat()
    html_sha=hashlib.sha256(html).hexdigest()
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"fbil_official_page.html").write_bytes(html)
    records=[]
    for local,y,t in sorted(set(found),key=lambda x:x[0]):
        records.append({"OBSERVATION_DATE":local.date().isoformat(),"TENOR":"10YR","YIELD_PCT":f"{y:.4f}",
          "UNIT":"PERCENT_PER_ANNUM","COMPOUNDING":"SEMI_ANNUAL","SOURCE":"Financial Benchmarks India Limited",
          "SOURCE_URL":URL,"PUBLISHED_AT_IST":local.isoformat(),"RELEASED_AT_UTC":local.astimezone(timezone.utc).isoformat(),
          "OBSERVED_AT_UTC":observed,"RELEASE_TIME_EVIDENCE":"FBIL official page row Date+Time fields; exact row-level publisher timestamp",
          "SOURCE_HTML_SHA256":html_sha})
    # No duplicate observation-date keys.
    dates=[x["OBSERVATION_DATE"] for x in records]
    if len(dates)!=len(set(dates)): raise RuntimeError("Duplicate FBIL 10YR observation dates")
    with (OUT/"fbil_10y_daily.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(records)
    csv_sha=hashlib.sha256((OUT/"fbil_10y_daily.csv").read_bytes()).hexdigest()
    report={"status":"FBIL_DAILY_10Y_PUBLISHER_TIMESTAMP_AUDIT_PASS","source_url":URL,
      "source_html_sha256":html_sha,"normalized_csv_sha256":csv_sha,"rows":len(records),
      "date_min":min(dates),"date_max":max(dates),"distinct_dates":len(set(dates)),
      "release_timestamp_field":"Publisher Date + Time, Asia/Kolkata; converted to UTC",
      "latest_records":[{"date":x["OBSERVATION_DATE"],"yield_pct":x["YIELD_PCT"],"published_at_ist":x["PUBLISHED_AT_IST"]} for x in records[-5:]],
      "frequency":"DAILY_ON_PUBLISHED_BUSINESS_DAYS","missing_days":"Not interpolated; holidays/unpublished dates remain absent",
      "licensing_status":"REVIEW_REQUIRED_BEFORE_COMMERCIAL_OR_PRODUCTION_USE; FBIL website disclaimer states commercial use requires written permission",
      "factor_registry_promotion":"NOT_PROMOTED_PENDING_WRITTEN_USE_PERMISSION_AND_CANONICAL_SOURCE_REVIEW",
      "observed_at_utc":observed}
    (OUT/"fbil_10y_provenance_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
