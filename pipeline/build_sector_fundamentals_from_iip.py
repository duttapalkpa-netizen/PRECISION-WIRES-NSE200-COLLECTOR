#!/usr/bin/env python3
"""Build a provenance-rich, explicitly partial sector-fundamentals panel from MoSPI NIC-2 IIP."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, urllib.parse
import pandas as pd

ROOT=Path(".")
BASE=ROOT/"artifacts/esankhyiki_iip_backseries"
PANEL=BASE/"iip_nic2_monthly_panel_2023_04_to_2026_09.csv"
CATALOGUE=BASE/"catalogue_vintage_manifest.csv"
PIB_MANIFEST=BASE/"pib_september_2026/manifest.json"
OUT=ROOT/"data/external/sector_fundamentals.csv"
REPORT=ROOT/"outputs/macro_geo/sector_fundamentals_iip_adapter_qa.json"
DOWNLOAD="https://api.mospi.gov.in/api/esankhyiki/file/download/"
PIB_URL="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475&lang=1&reg=3"
SHA_RE=re.compile(r"^[0-9a-f]{64}$")

def sha256_file(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest()

def build_rows(panel, catalogue, pib, observed_at):
    required={"period","nic_2025","description","weight","index","base_year","frequency","unit",
              "source","table_id","release_date","release_vintage","source_file","source_sha256"}
    missing=required-set(panel.columns)
    if missing: raise ValueError("Missing panel columns: "+",".join(sorted(missing)))
    if len(panel)!=966: raise ValueError(f"Expected 966 NIC-2 monthly rows, got {len(panel)}")
    if panel["nic_2025"].nunique()!=23: raise ValueError("Expected 23 unique NIC-2 groups")
    if panel["period"].nunique()!=42: raise ValueError("Expected 42 monthly periods")
    if panel.duplicated(["nic_2025","period"]).any(): raise ValueError("Duplicate NIC-2/month keys")
    if panel["period"].min()!="2023-04" or panel["period"].max()!="2026-09":
        raise ValueError("NIC-2 panel period bounds do not match Apr-2023 to Sep-2026")
    cat=catalogue.iloc[0].to_dict()
    cat_url=str(cat.get("download_url") or "").strip()
    if not cat_url:
        rel=str(cat.get("file_path") or "").lstrip("/")+str(cat.get("file_name") or "")
        if not rel: raise ValueError("Catalogue vintage lacks exact file path/name")
        cat_url=DOWNLOAD+urllib.parse.quote(rel,safe="/")
    pib_url=str(pib.get("url") or PIB_URL)
    out=[]
    for row in panel.to_dict("records"):
        code=str(row["nic_2025"]).zfill(2)
        is_pib=str(row["source"]).startswith("MoSPI September 2026 PIB")
        source_url=pib_url if is_pib else cat_url
        release_date=str(row["release_date"])
        digest=str(row["source_sha256"]).lower()
        if not SHA_RE.fullmatch(digest): raise ValueError(f"Invalid SHA-256 for NIC {code}/{row['period']}")
        value=float(row["index"]); weight=float(row["weight"])
        if not (value>0 and weight>=0): raise ValueError(f"Invalid value/weight for NIC {code}/{row['period']}")
        out.append({
            "DATE":str(row["period"]),
            "SECTOR":f"NIC2_{code}",
            "METRIC":"IIP_INDEX",
            "VALUE":value,
            "NIC2_DESCRIPTION":str(row["description"]),
            "NIC2_CODE":code,
            "WEIGHT":weight,
            "UNIT":str(row["unit"]),
            "BASE_YEAR":str(row["base_year"]),
            "FREQUENCY":str(row["frequency"]),
            "SOURCE":str(row["source"]),
            "SOURCE_URL":source_url,
            "TABLE_ID":str(row["table_id"]),
            "RELEASE_DATE":release_date,
            "RELEASE_VINTAGE":str(row["release_vintage"]),
            "SOURCE_FILE":str(row["source_file"]),
            "SOURCE_SHA256":digest,
            "PUBLICATION_TIMESTAMP":"",
            "PUBLICATION_TIME_STATUS":"UNKNOWN_NOT_PUBLISHED_IN_SOURCE_METADATA",
            "OBSERVED_AT_UTC":observed_at
        })
    result=pd.DataFrame(out)
    if result.duplicated(["DATE","SECTOR","METRIC"]).any(): raise ValueError("Duplicate normalized DATE/SECTOR/METRIC keys")
    if result["SOURCE_URL"].isna().any() or not result["SOURCE_URL"].astype(str).str.startswith("https://").all():
        raise ValueError("Every row must have an official HTTPS source URL")
    if result["TABLE_ID"].astype(str).str.strip().eq("").any() or result["RELEASE_DATE"].astype(str).str.strip().eq("").any():
        raise ValueError("Every row must retain table ID and release date")
    return result

def main():
    for p in (PANEL,CATALOGUE,PIB_MANIFEST):
        if not p.is_file(): raise SystemExit(f"BLOCKED_MISSING_INPUT: {p}")
    panel=pd.read_csv(PANEL,dtype={"nic_2025":str}).fillna("")
    catalogue=pd.read_csv(CATALOGUE,dtype=str).fillna("")
    pib=json.loads(PIB_MANIFEST.read_text(encoding="utf-8"))
    if len(catalogue)!=1: raise SystemExit("Expected exactly one latest cumulative catalogue vintage")
    # Verify raw bytes for both official sources before adapting any observations.
    cat=catalogue.iloc[0].to_dict()
    raw_catalogue=BASE/"raw"/str(cat["file_name"])
    pib_raw=BASE/"pib_september_2026"/"mospi_iip_release_raw.html"
    expected_cat=str(cat["sha256"]).lower()
    expected_pib=str(pib["sha256_raw"]).lower()
    if sha256_file(raw_catalogue)!=expected_cat: raise SystemExit("BLOCKED_CATALOGUE_WORKBOOK_SHA256_MISMATCH")
    if sha256_file(pib_raw)!=expected_pib: raise SystemExit("BLOCKED_PIB_RAW_SHA256_MISMATCH")
    observed=datetime.now(timezone.utc).isoformat()
    out=build_rows(panel,catalogue,pib,observed)
    OUT.parent.mkdir(parents=True,exist_ok=True); REPORT.parent.mkdir(parents=True,exist_ok=True)
    out.to_csv(OUT,index=False)
    report={
      "status":"PARTIAL_SOURCE_COVERAGE",
      "source_group":"sector_fundamentals",
      "observed_rows":int(len(out)),
      "nic2_groups":int(out["NIC2_CODE"].nunique()),
      "monthly_periods":int(out["DATE"].nunique()),
      "date_min":str(out["DATE"].min()),
      "date_max":str(out["DATE"].max()),
      "metrics":sorted(out["METRIC"].unique().tolist()),
      "source_files_sha256_verified":2,
      "catalogue_table_id":str(cat["unique_id"]),
      "catalogue_release_date":str(cat["release_date"]),
      "catalogue_release_vintage":str(cat["ref_period"]),
      "pib_release_url":PIB_URL,
      "publication_timestamps_missing":int(out["PUBLICATION_TIMESTAMP"].eq("").sum()),
      "source_rows_by_provider":out.groupby("SOURCE")["DATE"].count().to_dict(),
      "promotion_allowed":False,
      "promotion_blockers":[
        "NIC-2 IIP is an official industrial-production indicator, not company financial statements.",
        "No point-in-time mapping from NSE symbols/ISINs to NIC-2 groups is present in the validated source inputs.",
        "Official release metadata supplies release dates but not exact publication timestamps; timestamps remain UNKNOWN."
      ],
      "coverage_policy":"Keep sector_fundamentals PARTIAL_SOURCE_COVERAGE; do not promote factor coverage or alter any factor state from this adapter alone.",
      "output_sha256":sha256_file(OUT),
      "observed_at_utc":observed
    }
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
