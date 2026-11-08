#!/usr/bin/env python3
"""Strict audit of all monthly NIC-2 IIP catalogue vintages from MoSPI.
Audit contract revision: v6; index-only parser, explicit base-year/classification lineage, within-series revision audit.
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
START="2023-04"; END="2026-08"; UA="Mozilla/5.0 (compatible; PRECISION-WIRES-IIP-Vintage-Audit/1.0)"
OUT=Path("artifacts/iip_41_vintage_audit"); RAW=OUT/"raw"
TLS_CONTEXT=ssl.create_default_context()
TLS_CONTEXT.set_ciphers("DEFAULT:@SECLEVEL=1")
TLS_CONTEXT.options |= 0x4
OPENER=urllib.request.build_opener(urllib.request.HTTPSHandler(context=TLS_CONTEXT))
PARSE_LOCK=threading.Lock()
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
    return ("monthly nic-2 digit and sectoral indices and growth rates of industrial production" in title and period and START<=period<=END and r.get("product")=="IIP" and r.get("unique_id") and r.get("file_name") and r.get("file_path"))
def catalogue_scope_diagnostic(records):
    # Preserve near-miss catalogue rows so absent periods can be distinguished
    # from title/schema variants without silently promoting them into the audit.
    out=[]
    for r in records:
        if r.get("product")!="IIP":
            continue
        period=month(r.get("ref_period"))
        if not period or not (START<=period<=END):
            continue
        title=" ".join(str(r.get("table_name","")).lower().split())
        exact=("monthly nic-2 digit and sectoral indices and growth rates of industrial production" in title)
        file_hint=" ".join(str(r.get("file_name","")).lower().split())
        nic_hint=("nic" in title or "sectoral" in title or "nic" in file_hint)
        annual_nic2=(nic_hint and ("annual" in title or "sectoralannual" in file_hint or "sectoral annual" in file_hint))
        reason=("EXACT_TITLE_CANDIDATE" if exact else
                "NIC2_ANNUAL_NON_TARGET" if annual_nic2 else
                "NEAR_MATCH_TITLE_REVIEW_REQUIRED" if nic_hint else
                "OTHER_IIP_TABLE_NOT_NIC2")
        if exact and not (r.get("unique_id") and r.get("file_name") and r.get("file_path")):
            reason="EXACT_TITLE_MISSING_FILE_METADATA"
        out.append({
            "reference_period":period,"catalogue_code":r.get("catalogue_code"),
            "unique_id":r.get("unique_id"),"table_name":r.get("table_name"),
            "release_date":r.get("release_date"),"frequency":r.get("frequency"),
            "file_path":r.get("file_path"),"file_name":r.get("file_name"),
            "qualification_diagnostic":reason
        })
    return sorted(out,key=lambda x:(x["reference_period"],str(x.get("release_date","")),str(x.get("unique_id",""))))
def parse_xlsx(path):
    # Supports the legacy NIC-2 heading and the newer NIC-2025 sectoral heading.
    # Parse only the index table; growth-rate sections are not index observations.
    with PARSE_LOCK:
        xl=pd.ExcelFile(path)
        candidates=[]
        for sheet in xl.sheet_names:
            df=pd.read_excel(path,sheet_name=sheet,header=None,dtype=object)
            base_text=str(df.iloc[1,0]) if len(df)>1 and pd.notna(df.iloc[1,0]) else ""
            base_match=re.search(r"base\s+([0-9]{4}-[0-9]{2})",base_text,re.I)
            base_year=base_match.group(1) if base_match else ""
            title_row=None
            for i,row in df.iterrows():
                title=str(row.iloc[0]).strip().lower() if pd.notna(row.iloc[0]) else ""
                if (title.startswith("monthly nic-2 digit and sectoral indices of industrial production")
                    or title.startswith("monthly sectoral, sub-sectoral/nic 2 digit indices of industrial production")):
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
            classification=str(df.iloc[header_row,0]).strip().upper().replace(" ","-")
            if classification not in ("NIC-2008","NIC-2025") or not base_year:
                raise ValueError(f"missing/unsupported series lineage: base_year={base_year!r}, classification={classification!r}")
            periods=[(ci,month(v)) for ci,v in enumerate(df.iloc[header_row].tolist()) if ci>=3 and month(v)]
            rows=[]
            for _,row in df.iloc[header_row+1:].iterrows():
                label=str(row.iloc[0]).strip().lower() if pd.notna(row.iloc[0]) else ""
                if "growth rates" in label or label.startswith("monthly nic-2 digit and sectoral growth"):
                    break
                code=str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else ""
                # NIC-2025 includes combined divisions such as 05-06 as well as 2-digit codes.
                if not re.fullmatch(r"[0-9]{2}(?:-[0-9]{2})?",code):
                    if label.startswith("monthly "):
                        break
                    continue
                nic=code
                for ci,period in periods:
                    val=pd.to_numeric(pd.Series([row.iloc[ci]]),errors="coerce").iloc[0]
                    if pd.notna(val):
                        rows.append({"base_year":base_year,"classification":classification,"period":period,"nic_code":nic,"value":float(val),"measure":"index"})
            if rows:
                candidates.append((sheet,rows,base_year,classification))
        if not candidates:
            raise ValueError("no supported monthly NIC-2/NIC-2025 index table found")
        sheet,rows,base_year,classification=max(candidates,key=lambda x:len(x[1]))
        keys=[(x["base_year"],x["classification"],x["period"],x["nic_code"]) for x in rows]
        if len(keys)!=len(set(keys)):
            raise ValueError("duplicate period/NIC keys inside index table")
        return sheet,rows,base_year,classification
def fetch_one(r):
    uid=str(r.get("unique_id","")); fname=str(r.get("file_name",""))
    local=RAW/(re.sub(r"[^A-Za-z0-9._-]+","_",uid)+"__"+Path(fname).name)
    url=DOWNLOAD+urllib.parse.quote(str(r.get("file_path","")).lstrip("/")+fname,safe="/")
    row={k:r.get(k) for k in ("catalogue_code","unique_id","product","table_name","ref_period","release_date","frequency","data_source","file_path","file_name","created_at","updated_at","status")}
    row.update({"request_url":url,"retrieved_at_utc":"","audit_checked_at_utc":"","http_status":None,"content_type":"","final_url":"","raw_bytes":0,"sha256":"","local_file":"","download_status":"","parse_status":"","parsed_rows":0,"sheet":"","error_response_sha256":"","error_response_excerpt":"","error":""})
    try:
        cache_hit=local.exists() and local.stat().st_size>1000 and local.read_bytes()[:2]==b"PK"
        if cache_hit:
            body=local.read_bytes(); x={"status":200,"type":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet","final":url,"body":body,"error":""}; row["download_status"]="CACHE_HIT_RAW_HASH_RECHECKED"
        else:
            x=req(url,"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/octet-stream",attempts=1,timeout=12)
            row["download_status"]="DOWNLOADED" if x["status"]==200 and x["body"].startswith(b"PK") else "FAILED"
        row["audit_checked_at_utc"]=datetime.now(timezone.utc).isoformat()
        if not cache_hit and row["download_status"]=="DOWNLOADED":
            row["retrieved_at_utc"]=row["audit_checked_at_utc"]
        row.update({"http_status":x["status"],"content_type":x["type"],"final_url":x["final"],"raw_bytes":len(x["body"]),"sha256":sha(x["body"]) if x["body"] else "","error_response_sha256":sha(x["body"]) if x["status"]>=400 and x["body"] else "","error_response_excerpt":re.sub(r"\\s+"," ",x["body"].decode("utf-8","replace"))[:300] if x["status"]>=400 and x["body"] else "","error":x["error"]})
        if x["status"]!=200 or not x["body"].startswith(b"PK"):
            row["parse_status"]="NOT_PARSED"; row["error"]=row["error"] or "NON_XLSX_OR_NON_200_RESPONSE"; return row,[]
        local.write_bytes(x["body"]); row["local_file"]=str(local.relative_to(OUT))
        sheet,obs,base_year,classification=parse_xlsx(local)
        row.update({"parse_status":"PASS","parsed_rows":len(obs),"sheet":sheet,"base_year":base_year,"classification":classification})
        return row,obs
    except Exception as e:
        row["parse_status"]="FAIL"; row["error"]=f"{type(e).__name__}:{e}"[:500]; return row,[]
def main():
    RAW.mkdir(parents=True,exist_ok=True); allr,pagination=get_catalogue()
    scope_diag=catalogue_scope_diagnostic(allr)
    pd.DataFrame(scope_diag).to_csv(OUT/"catalogue_scope_diagnostics.csv",index=False)
    qualifying=sorted([r for r in allr if qualifies(r)],key=lambda r:(month(r.get("ref_period")) or "",str(r.get("release_date","")),str(r.get("unique_id",""))))
    # One fetch/parse per unique table ID prevents duplicate catalogue rows racing on the same raw path.
    by_id={}
    for r in qualifying:
        uid=str(r.get("unique_id",""))
        if uid not in by_id or str(r.get("updated_at",""))>str(by_id[uid].get("updated_at","")):
            by_id[uid]=r
    selected=sorted(by_id.values(),key=lambda r:(month(r.get("ref_period")) or "",str(r.get("release_date","")),str(r.get("unique_id",""))))
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
        obs_by_vintage.setdefault((o["table_id"],o["base_year"],o["classification"],o["period"],o["nic_code"]),o)
    obs=list(obs_by_vintage.values())
    pd.DataFrame(obs).to_csv(OUT/"all_vintage_observations.csv",index=False)
    by={}
    for o in obs:
        by.setdefault((o["base_year"],o["classification"],o["period"],o["nic_code"]),[]).append(o)
    diffs=[]
    for (base_year,classification,period,nic),items in sorted(by.items()):
        items.sort(key=lambda x:(month(x["release_ref_period"]) or "",str(x.get("release_date","")),str(x.get("table_id",""))))
        for prev,cur in zip(items,items[1:]):
            if prev["table_id"] != cur["table_id"] and prev["value"] != cur["value"]:
                diffs.append({"base_year":base_year,"classification":classification,"period":period,"nic_code":nic,"previous_table_id":prev["table_id"],"previous_release_date":prev["release_date"],"previous_value":prev["value"],"current_table_id":cur["table_id"],"current_release_date":cur["release_date"],"current_value":cur["value"],"revision_delta":cur["value"]-prev["value"],"previous_sha256":prev["source_sha256"],"current_sha256":cur["source_sha256"]})
    pd.DataFrame(diffs,columns=["base_year","classification","period","nic_code","previous_table_id","previous_release_date","previous_value","current_table_id","current_release_date","current_value","revision_delta","previous_sha256","current_sha256"]).to_csv(OUT/"revision_differences.csv",index=False)
    downloaded=sum(x["download_status"] in ("DOWNLOADED","CACHE_HIT_RAW_HASH_RECHECKED") for x in manifest)
    parsed=sum(x["parse_status"]=="PASS" for x in manifest)
    period_keys=sorted({month(x.get("ref_period")) for x in manifest if month(x.get("ref_period"))})
    # Fixed acceptance window: Apr-2023 through Aug-2026 (41 months).
    # Later catalogue additions must not silently change the audit denominator.
    expected_periods=pd.date_range(start=START+"-01",end=END+"-01",freq="MS")
    missing_periods=sorted(set(x.strftime("%Y-%m") for x in expected_periods)-set(period_keys))
    # Separate a missing release vintage from whether its reference-month
    # observations survive in later official workbooks. Later values never
    # backfill the missing vintage or enter its revision history as if original.
    coverage_rows=[]
    coverage_summary=[]
    for target_period in missing_periods:
        by_series={}
        for o in obs:
            if o["period"]!=target_period or (month(o.get("release_ref_period")) or "")<=target_period:
                continue
            key=(o["base_year"],o["classification"],o["nic_code"])
            by_series.setdefault(key,[]).append(o)
        stable=0; revised=0
        for (base_year,classification,nic_code),items in sorted(by_series.items()):
            items.sort(key=lambda x:(month(x.get("release_ref_period")) or "",str(x.get("release_date","")),str(x.get("table_id",""))))
            values=[x["value"] for x in items]
            is_revised=len(set(values))>1
            stable+=0 if is_revised else 1
            revised+=1 if is_revised else 0
            coverage_rows.append({
                "missing_release_period":target_period,"base_year":base_year,
                "classification":classification,"nic_code":nic_code,
                "later_vintage_count":len({x["table_id"] for x in items}),
                "later_vintage_ids":";".join(dict.fromkeys(x["table_id"] for x in items)),
                "first_later_vintage_id":items[0]["table_id"],
                "first_later_release_date":items[0]["release_date"],
                "first_later_value":items[0]["value"],
                "last_later_vintage_id":items[-1]["table_id"],
                "last_later_release_date":items[-1]["release_date"],
                "last_later_value":items[-1]["value"],
                "later_values_stable":not is_revised,
                "later_vintage_observation_count":len(items)
            })
        coverage_summary.append({
            "missing_release_period":target_period,
            "series_keys_available_in_later_vintages":len(by_series),
            "series_keys_stable_across_later_vintages":stable,
            "series_keys_revised_across_later_vintages":revised,
            "later_vintage_ids":sorted({x["table_id"] for x in coverage_rows if x["missing_release_period"]==target_period})
        })
    coverage_path=OUT/"missing_vintage_period_observation_coverage.csv"
    pd.DataFrame(coverage_rows,columns=["missing_release_period","base_year","classification","nic_code","later_vintage_count","later_vintage_ids","first_later_vintage_id","first_later_release_date","first_later_value","last_later_vintage_id","last_later_release_date","last_later_value","later_values_stable","later_vintage_observation_count"]).to_csv(coverage_path,index=False)
    unique_ids={x.get("unique_id") for x in manifest}
    duplicate_ids=sorted(k for k in unique_ids if sum(1 for x in manifest if x.get("unique_id")==k)>1)
    status="PASS" if len(qualifying)==41 and len(selected)==41 and len(unique_ids)==41 and len(period_keys)==41 and not missing_periods and downloaded==41 and parsed==41 else "BLOCKED_WITH_GAPS"
    qa={"audit_status":status,"iip_vintage_gate":"PASS" if status=="PASS" else "BLOCKED","hard_gate":"BLOCKED","hard_gate_scope":"PROJECT_GLOBAL_GATE_NOT_EVALUATED_BY_IIP_SUBAUDIT","audit_window_start":START,"audit_window_end":END,"expected_reference_periods":len(expected_periods),"series_definitions":sorted({(x.get("base_year"),x.get("classification")) for x in manifest if x.get("parse_status")=="PASS"}),"revision_comparison_policy":"same base_year + classification + NIC code + reference period only","catalogue_total_records":pagination["total_records"],"catalogue_pages":pagination["total_pages"],"catalogue_scope_diagnostic_rows":len(scope_diag),"near_match_title_rows":sum(x["qualification_diagnostic"]=="NEAR_MATCH_TITLE_REVIEW_REQUIRED" for x in scope_diag),"nic2_annual_non_target_rows":sum(x["qualification_diagnostic"]=="NIC2_ANNUAL_NON_TARGET" for x in scope_diag),"exact_title_missing_metadata_rows":sum(x["qualification_diagnostic"]=="EXACT_TITLE_MISSING_FILE_METADATA" for x in scope_diag),"qualifying_catalogue_rows":len(qualifying),"qualifying_vintage_records":len(selected),"manifest_rows":len(manifest),"duplicate_catalogue_rows_excluded_from_download":len(qualifying)-len(selected),"unique_vintage_ids":len(unique_ids),"unique_reference_periods":len(period_keys),"duplicate_catalogue_ids":duplicate_ids,"missing_reference_periods":missing_periods,"missing_vintage_period_observation_coverage":coverage_summary,"missing_vintage_period_coverage_rows":len(coverage_rows),"raw_files_downloaded_or_cache_verified":downloaded,"workbooks_parsed":parsed,"failed_downloads":sum(x["download_status"]=="FAILED" for x in manifest),"failed_download_evidence":[{"reference_period":x.get("ref_period"),"unique_id":x.get("unique_id"),"http_status":x.get("http_status"),"request_url":x.get("request_url"),"error_response_sha256":x.get("error_response_sha256"),"error_response_excerpt":x.get("error_response_excerpt")} for x in manifest if x.get("download_status")=="FAILED"],"parse_failures":sum(x["parse_status"]=="FAIL" for x in manifest),"parsed_observations":len(obs),"unique_observation_keys":len({(x["table_id"],x["base_year"],x["classification"],x["period"],x["nic_code"]) for x in obs}),"revision_differences_detected":len(diffs),"unique_table_ids":len(unique_ids),"unique_release_dates":len({x.get("release_date") for x in manifest}),"first_release_period":period_keys[0] if period_keys else None,"last_release_period":period_keys[-1] if period_keys else None,"pagination":pagination,"policy":"Missing vintage is not inferred; duplicate catalogue rows are retained in manifest but excluded from independent vintage count; only monthly index table is compared; missing/failed source files remain explicit."}
    audit_path=OUT/"revision_audit.json"
    audit_path.write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    # Validate the serialized artifact itself; never upload malformed JSON.
    json.loads(audit_path.read_text(encoding="utf-8"))
    print(json.dumps(qa,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
