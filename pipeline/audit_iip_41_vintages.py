#!/usr/bin/env python3
"""Strict audit of all monthly NIC-2 IIP catalogue vintages from MoSPI.
Audit contract revision: v5; index-only parser, duplicate-key rejection, vintage gap audit. fail-closed ingestion and revision comparison.
Every catalogue row receives an explicit download/parse status. A cumulative
panel is never treated as multiple downloaded vintages.
"""
from __future__ import annotations
import concurrent.futures,csv,hashlib,json,re,ssl,time,threading,urllib.parse,urllib.request,urllib.error
from datetime import datetime,timezone
from pathlib import Path
import pandas as pd
API="https://api.mospi.gov.in/api/esankhyiki/"
LIST=API+"cms/golden-sheet/list"; DOWNLOAD=API+"file/download/"
START="2023-04"; UA="Mozilla/5.0 (compatible; PRECISION-WIRES-IIP-Vintage-Audit/1.0)"
OUT=Path("artifacts/iip_41_vintage_audit"); RAW=OUT/"raw"
TLS_CONTEXT=ssl.create_default_context()
TLS_CONTEXT.set_ciphers("DEFAULT:@SECLEVEL=1")
TLS_CONTEXT.options |= 0x4
OPENER=urllib.request.build_opener(urllib.request.HTTPSHandler(context=TLS_CONTEXT))\nPARSE_LOCK=threading.Lock()
def sha(b): return hashlib.sha256(b).hexdigest()
def req(url,accept,attempts=2,timeout=12):
    last=""
    for n in range(attempts):
        q=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":accept,"Origin":"https://esankhyiki.mospi.gov.in","Referer":"https://esankhyiki.mospi.gov.in/catalogue-main/catalogue"})
        try:
            with OPENER.open(q,timeout=timeout) as r:
                return {"status":r.status,"type":r.headers.get("Content-Type",""),"final":r.geturl(),"body":r.read(40000000),"error":""}
        except urllib.error.HTTPError as e:
            body=e.read(1000000)
            if e.code not in (429,500,502,503,504): return {"status":e.code,"type":e.headers.get("Content-Type",""),"final":e.geturl(),"body":body,"error":f"HTTP_{e.code}"}
            last=f"HTTP_{e.code}"
        except Exception as e: last=f"{type(e).__name__}:{e}"
        if n+1<attempts: time.sleep(1+n)
    return {"status":0,"type":"","final":url,"body":b"","error":"RETRY_EXHAUSTED:"+last}
def month(v):
    d=pd.to_datetime(v,errors="coerce")
    return None if pd.isna(d) else d.strftime("%Y-%m")
def get_catalogue():
    first=req(LIST+"?"+urllib.parse.urlencode({"product":"IIP","page":1,"limit":10}),"application/json")
    if first["status"]!=200: raise RuntimeError(f"catalogue page 1 HTTP {first['status']}")
    p=json.loads(first["body"].decode("utf-8-sig")); meta=p.get("meta_data") or {}
    pages,total=int(meta.get("totalPages") or 0),int(meta.get("totalRecords") or 0)
    if pages<1 or total<1: raise RuntimeError("pagination metadata missing")
    records=list(p.get("data") or []); page_hashes=[{"page":1,"sha256":sha(first["body"]),"bytes":len(first["body"])}]
    for page in range(2,pages+1):
        time.sleep(.12); x=req(LIST+"?"+urllib.parse.urlencode({"product":"IIP","page":page,"limit":10}),"application/json")
        if x["status"]!=200: raise RuntimeError(f"catalogue page {page}/{pages} HTTP {x['status']}")
        j=json.loads(x["body"].decode("utf-8-sig")); records.extend(j.get("data") or [])
        page_hashes.append({"page":page,"sha256":sha(x["body"]),"bytes":len(x["body"])})
    if len(records)!=total: raise RuntimeError(f"pagination count mismatch {len(records)}/{total}")
    return records,{"total_records":total,"total_pages":pages,"records_returned":len(records),"page_payloads":page_hashes}
def qualifies(r):
    title=" ".join(str(r.get("table_name","")).lower().split()); period=month(r.get("ref_period"))
    return ("monthly nic-2 digit and sectoral indices and growth rates of industrial production" in title and period and period>=START and r.get("product")=="IIP" and r.get("unique_id") and r.get("file_name") and r.get("file_path"))
def parse_xlsx(path):
    # Parse ONLY the monthly index table. The workbook also contains a growth-rate
    # table with the same NIC codes; mixing the two doubles observations and
    # manufactures false "revisions".
    with PARSE_LOCK:
        xl=pd.ExcelFile(path)
        candidates=[]
        for sheet in xl.sheet_names:
            df=pd.read_excel(path,sheet_name=sheet,header=None,dtype=object)
            title_row=None
            for i,row in df.iterrows():
                title=str(row.iloc[0]).strip().lower() if pd.notna(row.iloc[0]) else ""
                if title.startswith("monthly nic-2 digit and sectoral indices of industrial production"):
                    title_row=i
                    break
            if title_row is None:
                continue
            header_row=None
            for i in range(title_row+1,min(title_row+5,len(df))):
                vals=[str(x).strip().lower() if pd.notna(x) else "" for x in df.iloc[i,:3]]
                if vals[0] in ("nic 2008","nic 2025") and vals[1]=="description" and vals[2]=="weights":
                    header_row=i
                    break
            if header_row is None:
                continue
            periods=[(ci,month(v)) for ci,v in enumerate(df.iloc[header_row].tolist()) if ci>=3 and month(v)]
            rows=[]
            for _,row in df.iloc[header_row+1:].iterrows():
                label=str(row.iloc[0]).strip().lower() if pd.notna(row.iloc[0]) else ""
                if label.startswith("monthly nic-2 digit and sectoral growth rates"):
                    break
                nic_value=pd.to_numeric(pd.Series([row.iloc[0]]),errors="coerce").iloc[0]
                if pd.isna(nic_value) or int(nic_value)!=nic_value or not 10<=int(nic_value)<=99:
                    # Blank separator or next section: do not continue across a section boundary.
                    if not label:
                        continue
                    if label.startswith("monthly "):
                        break
                    continue
                nic=str(int(nic_value)).zfill(2)
                for ci,period in periods:
                    val=pd.to_numeric(pd.Series([row.iloc[ci]]),errors="coerce").iloc[0]
                    if pd.notna(val):
                        rows.append({"period":period,"nic_code":nic,"value":float(val),"measure":"index"})
            if rows:
                candidates.append((sheet,rows))
        if not candidates:
            raise ValueError("no supported monthly NIC-2 index table found")
        sheet,rows=max(candidates,key=lambda x:len(x[1]))
        keys=[(x["period"],x["nic_code"]) for x in rows]
        if len(keys)!=len(set(keys)):
            raise ValueError("duplicate period/NIC keys inside index table")
        return sheet,rows
def fetch_one(r):
    uid=str(r.get("unique_id","")); fname=str(r.get("file_name",""))
    local=RAW/(re.sub(r"[^A-Za-z0-9._-]+","_",uid)+"__"+Path(fname).name)
    url=DOWNLOAD+urllib.parse.quote(str(r.get("file_path","")).lstrip("/")+fname,safe="/")
    row={k:r.get(k) for k in ("catalogue_code","unique_id","product","table_name","ref_period","release_date","frequency","data_source","file_path","file_name","created_at","updated_at","status")}
    row.update({"request_url":url,"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"http_status":None,"content_type":"","final_url":"","raw_bytes":0,"sha256":"","local_file":"","download_status":"","parse_status":"","parsed_rows":0,"sheet":"","error":""})
    try:
        if local.exists() and local.stat().st_size>1000 and local.read_bytes()[:2]==b"PK":
            body=local.read_bytes(); x={"status":200,"type":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet","final":url,"body":body,"error":""}; row["download_status"]="CACHE_HIT_RAW_HASH_RECHECKED"
        else:
            x=req(url,"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/octet-stream",attempts=1,timeout=12)
            row["download_status"]="DOWNLOADED" if x["status"]==200 and x["body"].startswith(b"PK") else "FAILED"
        row.update({"http_status":x["status"],"content_type":x["type"],"final_url":x["final"],"raw_bytes":len(x["body"]),"sha256":sha(x["body"]) if x["body"] else "","error":x["error"]})
        if x["status"]!=200 or not x["body"].startswith(b"PK"):
            row["parse_status"]="NOT_PARSED"; row["error"]=row["error"] or "NON_XLSX_OR_NON_200_RESPONSE"; return row,[]
        local.write_bytes(x["body"]); row["local_file"]=str(local.relative_to(OUT))
        sheet,obs=parse_xlsx(local); row.update({"parse_status":"PASS","parsed_rows":len(obs),"sheet":sheet})
        return row,obs
    except Exception as e:
        row["parse_status"]="FAIL"; row["error"]=f"{type(e).__name__}:{e}"[:500]; return row,[]
def main():
    RAW.mkdir(parents=True,exist_ok=True); allr,pagination=get_catalogue()
    selected=sorted([r for r in allr if qualifies(r)],key=lambda r:(month(r.get("ref_period")) or "",str(r.get("release_date","")),str(r.get("unique_id",""))))
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        fs=[pool.submit(fetch_one,r) for r in selected]
        for f in concurrent.futures.as_completed(fs): results.append(f.result())
    manifest=[x[0] for x in results]; manifest.sort(key=lambda x:(month(x.get("ref_period")) or "",str(x.get("release_date","")),str(x.get("unique_id",""))))
    obs=[]
    for row,items in results:
        for o in items: o.update({"table_id":row.get("unique_id"),"release_date":row.get("release_date"),"release_ref_period":row.get("ref_period"),"source_sha256":row.get("sha256"),"source_file":row.get("file_name")}); obs.append(o)
    fields=list(manifest[0].keys()) if manifest else ["unique_id","ref_period","release_date","download_status","parse_status","error"]
    with (OUT/"vintage_ingestion_manifest.csv").open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(manifest)
    pd.DataFrame(obs).to_csv(OUT/"all_vintage_observations.csv",index=False)
    # Remove duplicate catalogue entries from value comparison while preserving every manifest row.
    obs_by_vintage={}
    for o in obs:
        obs_by_vintage.setdefault((o["table_id"],o["period"],o["nic_code"]),o)
    obs=list(obs_by_vintage.values())
    pd.DataFrame(obs).to_csv(OUT/"all_vintage_observations.csv",index=False)
    by={}
    for o in obs:
        by.setdefault((o["period"],o["nic_code"]),[]).append(o)
    diffs=[]
    for (period,nic),items in sorted(by.items()):
        items.sort(key=lambda x:(month(x["release_ref_period"]) or "",str(x.get("release_date","")),str(x.get("table_id",""))))
        for prev,cur in zip(items,items[1:]):
            if prev["table_id"] != cur["table_id"] and prev["value"] != cur["value"]:
                diffs.append({"period":period,"nic_code":nic,"previous_table_id":prev["table_id"],"previous_release_date":prev["release_date"],"previous_value":prev["value"],"current_table_id":cur["table_id"],"current_release_date":cur["release_date"],"current_value":cur["value"],"revision_delta":cur["value"]-prev["value"],"previous_sha256":prev["source_sha256"],"current_sha256":cur["source_sha256"]})
    pd.DataFrame(diffs,columns=["period","nic_code","previous_table_id","previous_release_date","previous_value","current_table_id","current_release_date","current_value","revision_delta","previous_sha256","current_sha256"]).to_csv(OUT/"revision_differences.csv",index=False)
    downloaded=sum(x["download_status"] in ("DOWNLOADED","CACHE_HIT_RAW_HASH_RECHECKED") for x in manifest)
    parsed=sum(x["parse_status"]=="PASS" for x in manifest)
    period_keys=sorted({month(x.get("ref_period")) for x in manifest if month(x.get("ref_period"))})
    expected_periods=pd.date_range(start=period_keys[0]+"-01",end=period_keys[-1]+"-01",freq="MS") if period_keys else []
    missing_periods=sorted(set(x.strftime("%Y-%m") for x in expected_periods)-set(period_keys))
    unique_ids={x.get("unique_id") for x in manifest}
    duplicate_ids=sorted(k for k in unique_ids if sum(1 for x in manifest if x.get("unique_id")==k)>1)
    status="PASS" if len(selected)==41 and len(unique_ids)==41 and len(period_keys)==41 and not missing_periods and downloaded==41 and parsed==41 else "BLOCKED_WITH_GAPS"
    qa={"audit_status":status,"hard_gate":"BLOCKED","catalogue_total_records":pagination["total_records"],"catalogue_pages":pagination["total_pages"],"qualifying_vintage_records":len(selected),"manifest_rows":len(manifest),"unique_vintage_ids":len(unique_ids),"unique_reference_periods":len(period_keys),"duplicate_catalogue_ids":duplicate_ids,"missing_reference_periods":missing_periods,"raw_files_downloaded_or_cache_verified":downloaded,"workbooks_parsed":parsed,"failed_downloads":sum(x["download_status"]=="FAILED" for x in manifest),"parse_failures":sum(x["parse_status"]=="FAIL" for x in manifest),"parsed_observations":len(obs),"unique_observation_keys":len({(x["table_id"],x["period"],x["nic_code"]) for x in obs}),"revision_differences_detected":len(diffs),"unique_table_ids":len(unique_ids),"unique_release_dates":len({x.get("release_date") for x in manifest}),"first_release_period":period_keys[0] if period_keys else None,"last_release_period":period_keys[-1] if period_keys else None,"pagination":pagination,"policy":"Missing vintage is not inferred; duplicate catalogue rows are retained in manifest but excluded from independent vintage count; only monthly index table is compared; missing/failed source files remain explicit."}
    (OUT/"revision_audit.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\\n")
    print(json.dumps(qa,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
