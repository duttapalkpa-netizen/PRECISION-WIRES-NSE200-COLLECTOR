#!/usr/bin/env python3
"""Bounded IMF PortWatch chokepoint activity backfill for the frozen NSE 200-session window.

Activity indicators are AIS-derived proxies, not freight-rate quotations.
No coverage promotion is performed here.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time
import requests
import pandas as pd

SNAPSHOT_ID="1f6d79d9bcdf3a6aa11dd9a80033276061447401dac6c708ab6622b6258b7534"
MANIFEST=Path("inputs/nse_snapshot/raw/nse_snapshot_manifest_1f6d79d9bcdf3a6a.json")
ROOT=Path("artifacts/global_freight_shipping")
URL="https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0"
PAGE_SIZE=1000
MAX_PAGES=20
HEADERS={"User-Agent":"PRECISION-WIRES-research/1.0 (read-only public data acquisition)","Accept":"application/json"}

def sha(b): return hashlib.sha256(b).hexdigest()

def request_json(session, params, label):
    last=None
    for attempt in range(3):
        try:
            r=session.get(URL+"/query",params=params,timeout=(10,45))
            r.raise_for_status()
            raw=r.content
            data=r.json()
            if "error" in data: raise ValueError(f"ArcGIS {label} error: {data['error']}")
            return data,raw,r.url,datetime.now(timezone.utc).isoformat()
        except Exception as exc:
            last=exc
            if attempt<2: time.sleep(1+attempt*2)
    raise RuntimeError(f"{label} failed after bounded retries: {type(last).__name__}: {last}")

def main():
    if not MANIFEST.is_file(): raise SystemExit("BLOCKED_MISSING_PINNED_NSE_SNAPSHOT")
    snap=json.loads(MANIFEST.read_text())
    if snap.get("snapshot_id")!=SNAPSHOT_ID or snap.get("actual_sessions")!=200 or len(snap.get("records",[]))!=200:
        raise SystemExit("BLOCKED_NSE_SNAPSHOT_ID_OR_SESSION_COUNT_MISMATCH")
    sessions=sorted({str(x["trade_date"]) for x in snap["records"]})
    if len(sessions)!=200: raise SystemExit("BLOCKED_DUPLICATE_NSE_SESSION_DATES")
    start,end=sessions[0],sessions[-1]
    where=f"date >= DATE '{start}' AND date <= DATE '{end}'"
    ROOT.mkdir(parents=True,exist_ok=True)
    rawdir=ROOT/"raw_pages";rawdir.mkdir(parents=True,exist_ok=True)
    s=requests.Session();s.headers.update(HEADERS)
    meta,meta_raw=s.get(URL,params={"f":"pjson"},timeout=(10,45)),None
    meta.raise_for_status();meta_raw=meta.content;metadata=meta.json()
    if "error" in metadata: raise RuntimeError(metadata["error"])
    fields={x["name"] for x in metadata.get("fields",[])}
    required={"date","portid","portname","n_total","capacity"}
    if not required.issubset(fields): raise SystemExit(f"BLOCKED_LAYER_SCHEMA_MISMATCH:{sorted(required-fields)}")
    count,raw,url,observed=request_json(s,{"where":where,"returnCountOnly":"true","f":"json"},"count")
    expected_count=int(count.get("count",-1))
    if expected_count<1 or expected_count>PAGE_SIZE*MAX_PAGES:
        raise SystemExit(f"BLOCKED_UNEXPECTED_QUERY_COUNT:{expected_count}")
    ids,ids_raw,ids_url,ids_observed=request_json(s,{
        "where":where,"outFields":"portid,portname","returnDistinctValues":"true",
        "returnGeometry":"false","orderByFields":"portid ASC","resultRecordCount":1000,"f":"json"},"distinct chokepoints")
    port_rows=[x.get("attributes",{}) for x in ids.get("features",[])]
    port_ids=sorted({str(x.get("portid","")) for x in port_rows if x.get("portid")})
    if not 1<=len(port_ids)<=40: raise SystemExit(f"BLOCKED_UNEXPECTED_CHOKEPOINT_COUNT:{len(port_ids)}")
    all_rows=[];page_reports=[];offset=0
    while offset<expected_count and len(page_reports)<MAX_PAGES:
        data,body,query_url,observed_at=request_json(s,{
            "where":where,"outFields":"*","orderByFields":"date ASC,portid ASC",
            "resultOffset":offset,"resultRecordCount":PAGE_SIZE,
            "returnGeometry":"false","f":"json"},"data page")
        feats=data.get("features",[])
        rows=[x.get("attributes",{}) for x in feats]
        if not rows: break
        rawfile=rawdir/f"portwatch_chokepoints_offset_{offset}.json"
        rawfile.write_bytes(body)
        page_reports.append({"offset":offset,"rows":len(rows),"url":query_url,
          "sha256":sha(body),"retrieved_at_utc":observed_at,
          "exceeded_transfer_limit":bool(data.get("exceededTransferLimit",False)),
          "raw_file":str(rawfile.relative_to(ROOT))})
        all_rows.extend(rows)
        offset+=len(rows)
        if len(rows)<PAGE_SIZE and not data.get("exceededTransferLimit",False): break
    if len(all_rows)!=expected_count:
        raise SystemExit(f"BLOCKED_INCOMPLETE_PAGINATION: expected={expected_count} retrieved={len(all_rows)}")
    d=pd.DataFrame(all_rows)
    d["DATE"]=pd.to_datetime(d["date"],errors="coerce").dt.strftime("%Y-%m-%d")
    d["CHOKEPOINT_ID"]=d["portid"].astype(str)
    d["CHOKEPOINT"]=d["portname"].astype(str)
    if d[["DATE","CHOKEPOINT_ID","CHOKEPOINT"]].isna().any().any() or d.duplicated(["DATE","CHOKEPOINT_ID"]).any():
        raise SystemExit("BLOCKED_INVALID_OR_DUPLICATE_DATE_CHOKEPOINT_KEYS")
    if not set(d["CHOKEPOINT_ID"]).issubset(set(port_ids)):
        raise SystemExit("BLOCKED_DISTINCT_CHOKEPOINT_ID_MISMATCH")
    session_set=set(sessions)
    d["IS_NSE_SESSION"]=d["DATE"].isin(session_set)
    d["SOURCE"]="IMF PortWatch / UN Global Platform AIS-derived estimates"
    d["SOURCE_URL"]=URL
    d["SOURCE_QUERY_URL"]=URL+"/query"
    d["SOURCE_DATA_LAST_EDIT_DATE_UTC"]=pd.to_datetime(metadata.get("editingInfo",{}).get("lastEditDate"),unit="ms",utc=True,errors="coerce").isoformat()
    d["OBSERVED_AT_UTC"]=datetime.now(timezone.utc).isoformat()
    d["NSE_SNAPSHOT_ID"]=SNAPSHOT_ID
    d["ACTIVITY_DATE_BASIS"]="PROVIDER_DAILY_AIS_ACTIVITY_DATE"
    out=ROOT/"imf_portwatch_chokepoint_activity_2026.csv"
    d.to_csv(out,index=False)
    selected=d[d["IS_NSE_SESSION"]].copy()
    expected_keys=200*len(port_ids)
    present_keys=set(zip(selected["DATE"],selected["CHOKEPOINT_ID"]))
    all_keys={(day,pid) for day in sessions for pid in port_ids}
    missing=sorted(all_keys-present_keys)
    report={
      "status":"PASS_BACKFILL_WITH_EXPLICIT_COVERAGE_AUDIT",
      "provider":"IMF PortWatch / UN Global Platform",
      "snapshot_id":SNAPSHOT_ID,"nse_sessions":200,"nse_date_min":start,"nse_date_max":end,
      "date_range_query":where,"query_total_records":expected_count,"records_retrieved":len(d),
      "distinct_chokepoints":len(port_ids),"chokepoint_ids":port_ids,
      "all_calendar_rows":len(d),"nse_session_rows":len(selected),
      "expected_nse_session_keys":expected_keys,"observed_nse_session_keys":len(present_keys),
      "missing_nse_session_keys":len(missing),"missing_key_examples":missing[:25],
      "nse_session_coverage_pct":round(100*len(present_keys)/expected_keys,4) if expected_keys else 0,
      "duplicate_date_chokepoint_keys":int(d.duplicated(["DATE","CHOKEPOINT_ID"]).sum()),
      "metadata_sha256":sha(meta_raw),"metadata_url":URL+"?f=pjson",
      "metadata_retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
      "metadata_last_edit_date_epoch_ms":metadata.get("editingInfo",{}).get("lastEditDate"),
      "page_reports":page_reports,"output_sha256":sha(out.read_bytes()),
      "promotion_allowed":False,
      "limitations":[
        "PortWatch data are AIS-derived port/chokepoint activity estimates, not quoted freight rates.",
        "Missing date/chokepoint observations remain gaps; they are not converted to zero.",
        "The provider may revise AIS-derived estimates; retrieval and provider edit timestamps are kept separate.",
        "No exact source publication timestamp is asserted."
      ],
      "observed_at_utc":datetime.now(timezone.utc).isoformat()
    }
    (ROOT/"backfill_qa.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps({k:report[k] for k in ("status","nse_sessions","query_total_records","records_retrieved","distinct_chokepoints","nse_session_rows","expected_nse_session_keys","observed_nse_session_keys","missing_nse_session_keys","nse_session_coverage_pct","promotion_allowed")},indent=2))
if __name__=="__main__": main()
