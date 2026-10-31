#!/usr/bin/env python3
"""Incremental, provenance-preserving e-Sankhyiki NIC-2 IIP back-series ingestion.

Downloads every public monthly NIC-2 catalogue vintage from Apr-2023 onward,
extracts the latest catalogue vintage (Aug-2026 currently), and appends the
Sep-2026 quick estimate from the official PIB Statement IV collector.
No API credentials are sent. Certificate validation remains enabled.
"""
from __future__ import annotations
import csv, hashlib, json, re, ssl, time, urllib.parse, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path
from io import BytesIO
import pandas as pd

API="https://api.mospi.gov.in/api/esankhyiki/"
LIST=API+"cms/golden-sheet/list"
DOWNLOAD=API+"file/download/"
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-IIP-Backseries/1.0)"
START="2023-04"
NIC_RE=re.compile(r"^(?:1[0-9]|2[0-9]|3[0-2])$")
def ssl_opener():
    ctx=ssl.create_default_context()
    ctx.set_ciphers("DEFAULT:@SECLEVEL=1")
    ctx.options |= 0x4  # legacy server connect; CERT_REQUIRED and hostname checking remain enabled
    return urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
OPENER=ssl_opener()
def request(url, accept="application/json, */*", attempts=3):
    last=None
    for attempt in range(attempts):
        req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":accept,
          "Content-Type":"application/json","Origin":"https://esankhyiki.mospi.gov.in",
          "Referer":"https://esankhyiki.mospi.gov.in/catalogue-main/catalogue"})
        try:
            with OPENER.open(req,timeout=45) as r:
                body=r.read(40_000_000)
                return r.status,r.headers.get("Content-Type",""),r.geturl(),body
        except urllib.error.HTTPError as e:
            body=e.read(2_000_000)
            if e.code not in (429,500,502,503,504): return e.code,e.headers.get("Content-Type",""),e.geturl(),body
            last=e
        except Exception as e: last=e
        if attempt+1<attempts: time.sleep(1.5*(attempt+1))
    raise RuntimeError(f"Request failed after {attempts} attempts: {url}: {last}")
def sha(b): return hashlib.sha256(b).hexdigest()
def month_key(value):
    dt=pd.to_datetime(value,errors="coerce")
    return None if pd.isna(dt) else dt.strftime("%Y-%m")
def catalogue_records():
    first=request(LIST+"?"+urllib.parse.urlencode({"product":"IIP","page":1,"limit":10}))
    if first[0]!=200: raise RuntimeError(f"IIP catalogue list returned HTTP {first[0]}")
    p=json.loads(first[3].decode("utf-8-sig"))
    meta=p.get("meta_data") or {}
    pages=int(meta.get("totalPages") or 0)
    total=int(meta.get("totalRecords") or 0)
    if pages<1 or total<1: raise RuntimeError("IIP catalogue pagination metadata missing")
    records=list(p.get("data") or [])
    for page in range(2,pages+1):
        time.sleep(0.15)
        status,ct,fu,b=request(LIST+"?"+urllib.parse.urlencode({"product":"IIP","page":page,"limit":10}))
        if status!=200: raise RuntimeError(f"IIP catalogue page {page}/{pages} HTTP {status}")
        q=json.loads(b.decode("utf-8-sig"))
        records.extend(q.get("data") or [])
    if len(records)<total: raise RuntimeError(f"Catalogue pagination incomplete: {len(records)}/{total}")
    return records,{"total_records":total,"total_pages":pages,"records_returned":len(records),
                    "first_page_sha256":sha(first[3])}
def is_monthly_nic_record(r):
    title=" ".join(str(r.get("table_name","")).lower().split())
    period=month_key(r.get("ref_period"))
    return ("monthly nic-2 digit and sectoral indices and growth rates of industrial production" in title
            and period is not None and period>=START and r.get("product")=="IIP"
            and r.get("file_name") and r.get("file_path") and r.get("unique_id"))
def parse_latest_workbook(path, record):
    xl=pd.ExcelFile(path)
    candidates=[]
    for sheet in xl.sheet_names:
        frame=pd.read_excel(path,sheet_name=sheet,header=None,dtype=object)
        header_i=None
        for i,row in frame.iterrows():
            vals=[str(x).strip().lower() if pd.notna(x) else "" for x in row.iloc[:3]]
            if vals[:3]==["nic 2025","description","weights"]:
                header_i=i;break
        if header_i is None: continue
        header=frame.iloc[header_i].tolist()
        periods=[]
        for col_i,val in enumerate(header):
            if col_i<3: continue
            period=month_key(val)
            if period: periods.append((col_i,period))
        rows=[]
        for _,row in frame.iloc[header_i+1:].iterrows():
            nic=str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else ""
            if not NIC_RE.fullmatch(nic): continue
            desc=str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else ""
            weight=pd.to_numeric(pd.Series([row.iloc[2]]),errors="coerce").iloc[0]
            for col_i,period in periods:
                value=pd.to_numeric(pd.Series([row.iloc[col_i]]),errors="coerce").iloc[0]
                if pd.isna(value): raise ValueError(f"Missing IIP value {nic}/{period} in {path.name}")
                rows.append({"period":period,"nic_2025":nic,"description":desc,"weight":float(weight),
                  "index":float(value),"base_year":"2022-23","frequency":"M","unit":"index",
                  "source":"MoSPI e-Sankhyiki Data Catalogue","table_id":record["unique_id"],
                  "release_date":record["release_date"],"release_vintage":record["ref_period"],
                  "source_file":record["file_name"],"source_sha256":sha(path.read_bytes())})
        candidates.append((sheet,rows,sorted(set(x[1] for x in periods))))
    if not candidates: raise RuntimeError("No NIC-2025 monthly index sheet found in latest workbook")
    sheet,rows,periods=max(candidates,key=lambda x:len(x[1]))
    codes=sorted({x["nic_2025"] for x in rows})
    if len(codes)!=23: raise RuntimeError(f"Expected 23 NIC-2 groups; found {len(codes)}: {codes}")
    expected=[]; y,m=2023,4
    while f"{y:04d}-{m:02d}"<=max(periods):
        expected.append(f"{y:04d}-{m:02d}");m+=1
        if m==13:y+=1;m=1
    for nic in codes:
        have=sorted(x["period"] for x in rows if x["nic_2025"]==nic)
        if have!=expected: raise RuntimeError(f"NIC {nic} monthly coverage mismatch: {len(have)}/{len(expected)}")
    if min(periods)!=START: raise RuntimeError(f"Back-series starts {min(periods)}, expected {START}")
    if len(rows)!=23*len(expected): raise RuntimeError(f"Unexpected monthly panel rows {len(rows)}")
    return rows,{"sheet":sheet,"nic_codes":len(codes),"periods":len(expected),
                 "period_min":min(periods),"period_max":max(periods),"rows":len(rows)}
def main():
    out=Path("artifacts/esankhyiki_iip_backseries");rawdir=out/"raw";rawdir.mkdir(parents=True,exist_ok=True)
    records,pagination=catalogue_records()
    selected=[r for r in records if is_monthly_nic_record(r)]
    selected.sort(key=lambda r:(month_key(r["ref_period"]),str(r.get("release_date",""))))
    if not selected: raise RuntimeError("No monthly NIC-2 catalogue records from Apr-2023 found")
    download_manifest=[]
    for i,r in enumerate(selected,1):
        name=r["file_name"];target=rawdir/name
        meta={k:r.get(k) for k in ("catalogue_code","unique_id","product","table_name","ref_period","release_date","frequency","data_source","file_path","file_name","created_at","updated_at","status")}
        if target.exists() and target.stat().st_size>1000 and target.read_bytes()[:2]==b"PK":
            body=target.read_bytes();status="CACHED_VERIFIED_ZIP"
        else:
            url=DOWNLOAD+urllib.parse.quote(r["file_path"].lstrip("/")+name,safe="/")
            code,ct,final,body=request(url,"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/octet-stream")
            if code!=200 or not body.startswith(b"PK"):
                raise RuntimeError(f"Excel download invalid {r['unique_id']}: HTTP {code}, type={ct}, bytes={len(body)}")
            target.write_bytes(body);status="DOWNLOADED"
            meta.update({"download_url":url,"download_final_url":final,"content_type":ct})
        meta.update({"bytes":len(body),"sha256":sha(body),"local_file":str(target.relative_to(out)),"download_status":status})
        download_manifest.append(meta)
        time.sleep(0.12)
    # Choose the most recent release vintage from the actual catalogue metadata.
    latest=max(selected,key=lambda r:(month_key(r["ref_period"]),str(r.get("release_date",""))))
    latest_path=rawdir/latest["file_name"]
    latest_rows,latest_qa=parse_latest_workbook(latest_path,latest)
    # Append the current September 2026 quick estimate from the official PIB release.
    import sys
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
    from pipeline.collect_mospi_iip_public_release import collect
    pib_dir=out/"pib_september_2026"
    collect(pib_dir)
    pib=pd.read_csv(pib_dir/"iip_nic2_monthly_panel.csv",dtype={"nic_2025":str})
    sep=pib[pib["period"].eq("2026-09")].copy()
    if len(sep)!=23 or sep["nic_2025"].nunique()!=23: raise RuntimeError("September 2026 PIB NIC-2 quick estimate is incomplete")
    for _,r in sep.iterrows():
        latest_rows.append({"period":"2026-09","nic_2025":str(r["nic_2025"]),"description":r["description"],
          "weight":float(r["weight"]),"index":float(r["index"]),"base_year":"2022-23","frequency":"M","unit":"index",
          "source":"MoSPI September 2026 PIB Statement IV","table_id":f"PIB_PRID_2329475_STATEMENT_IV",
          "release_date":"28 Oct 2026","release_vintage":"2026-09_quick_estimate",
          "source_file":"mospi_iip_release_raw.html","source_sha256":json.loads((pib_dir/"manifest.json").read_text())["sha256_raw"]})
    panel=pd.DataFrame(latest_rows).sort_values(["nic_2025","period"]).reset_index(drop=True)
    if len(panel)!=23*42 or panel.duplicated(["nic_2025","period"]).any():
        raise RuntimeError(f"Combined panel key/row QA failed: rows={len(panel)}")
    # All NIC codes must cover every month Apr-2023 through Sep-2026.
    expected=[];y,m=2023,4
    while f"{y:04d}-{m:02d}"<="2026-09":
        expected.append(f"{y:04d}-{m:02d}");m+=1
        if m==13:y+=1;m=1
    for nic,g in panel.groupby("nic_2025"):
        if sorted(g["period"].tolist())!=expected: raise RuntimeError(f"Combined panel gap for NIC {nic}")
    panel.to_csv(out/"iip_nic2_monthly_panel_2023_04_to_2026_09.csv",index=False)
    with (out/"catalogue_vintage_manifest.csv").open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(download_manifest[0].keys()));w.writeheader();w.writerows(download_manifest)
    qa={"status":"PASS","catalogue_records_total":pagination["total_records"],"monthly_nic2_vintage_files":len(selected),
        "downloaded_or_cached_files":len(download_manifest),"latest_catalogue_table_id":latest["unique_id"],
        "latest_catalogue_release_date":latest["release_date"],"latest_catalogue_reference_period":latest["ref_period"],
        "catalogue_panel":latest_qa,"combined_rows":len(panel),"unique_nic_codes":int(panel["nic_2025"].nunique()),
        "unique_periods":int(panel["period"].nunique()),"period_min":min(panel["period"]),"period_max":max(panel["period"]),
        "duplicate_nic_period_keys":int(panel.duplicated(["nic_2025","period"]).sum()),
        "sep_2026_vintage":"quick_estimate","sep_2026_rows":len(sep),"base_year":"2022-23",
        "source_provenance":"Every catalogue workbook has its official table ID, release date, reference period, file name/path, SHA-256 and source; September 2026 is separately tagged from PIB Statement IV.",
        "pagination":pagination}
    (out/"backseries_qa.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(qa,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
