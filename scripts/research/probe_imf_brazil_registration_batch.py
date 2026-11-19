#!/usr/bin/env python3
"""Capture a bounded range of IMF registration transactions as Fusion-JSON.

The old IMF FMR transaction endpoint supports format=fusion-json. This batch
scanner captures every response (no cookie/auth headers), verifies JSON, and
extracts PA/URL/registration URN/lastUpdated to identify exact Brazil matches.
It does not infer event timestamps from Registration.lastUpdated; transaction
timestamps remain those returned by searchTransactions.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import argparse, hashlib, json, csv

BASE="https://sdmxcentral.imf.org"
TARGET_PA="urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)"
OUT=Path("imf_brazil_registration_batch")
OUT.mkdir(parents=True,exist_ok=True)

def fetch(txid):
    url=f"{BASE}/ws/registry/tx/transactions?txId={txid}&format=fusion-json"
    retrieved=datetime.now(timezone.utc).isoformat()
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-independent-audit/1.2","Accept":"application/json, */*"})
    try:
        with urlopen(req,timeout=25) as r:
            status=r.status; headers=dict(r.headers.items()); body=r.read()
    except HTTPError as e:
        status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
    except (URLError,TimeoutError) as e:
        status=0; headers={}; body=str(e).encode()
    safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
    fn=f"transaction_{txid:05d}.json"
    (OUT/fn).write_bytes(body)
    rec={"tx_id":txid,"url":url,"retrieved_at_utc":retrieved,"http_status":status,
         "headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":fn}
    regs=[]
    if status==200:
        try:
            doc=json.loads(body)
            raw=doc.get("Registration",[])
            if isinstance(raw,dict): raw=[raw]
            for reg in raw:
                row={"tx_id":txid,"registration_urn":reg.get("urn"),"registration_id":reg.get("id"),
                     "provision_agreement_urn":reg.get("provisionAgreementReference"),
                     "data_url":(reg.get("dataSource") or {}).get("dataUrl"),
                     "registration_lastUpdated":reg.get("lastUpdated")}
                regs.append(row)
            rec["parse_status"]="PASS"
            rec["registration_count"]=len(regs)
            rec["brazil_pa_match"]=any(x["provision_agreement_urn"]==TARGET_PA for x in regs)
        except Exception as e:
            rec["parse_status"]="FAIL"; rec["parse_error"]=str(e)
    else:
        rec["parse_status"]="HTTP_NOT_200"
    return rec,regs

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start-id",type=int,default=13)
    ap.add_argument("--end-id",type=int,default=112)
    ap.add_argument("--workers",type=int,default=12)
    a=ap.parse_args()
    if a.start_id<1 or a.end_id<a.start_id or a.end_id-a.start_id>199:
        raise SystemExit("Require 1 <= start <= end and batch size <= 200")
    records=[]; registrations=[]
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        futures={pool.submit(fetch,i):i for i in range(a.start_id,a.end_id+1)}
        for f in as_completed(futures):
            rec,regs=f.result(); records.append(rec); registrations.extend(regs)
    records.sort(key=lambda x:x["tx_id"])
    registrations.sort(key=lambda x:x["tx_id"])
    matches=[x for x in registrations if x["provision_agreement_urn"]==TARGET_PA]
    summary={"scope":"bounded transaction ID batch; no completeness beyond supplied ID range",
             "start_id":a.start_id,"end_id":a.end_id,"requested_count":a.end_id-a.start_id+1,
             "http_200_count":sum(x["http_status"]==200 for x in records),
             "parse_pass_count":sum(x.get("parse_status")=="PASS" for x in records),
             "registration_object_count":len(registrations),"brazil_pa_match_count":len(matches),
             "brazil_pa_matches":matches,
             "non_200_or_parse_fail":[x for x in records if x.get("parse_status")!="PASS"]}
    (OUT/"manifest.json").write_text(json.dumps({"target_pa_urn":TARGET_PA,"responses":records},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (OUT/"registration_index.json").write_text(json.dumps(registrations,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    with (OUT/"registration_index.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["tx_id","registration_urn","registration_id","provision_agreement_urn","data_url","registration_lastUpdated"])
        w.writeheader(); w.writerows(registrations)
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    if summary["http_200_count"]!=summary["requested_count"] or summary["parse_pass_count"]!=summary["requested_count"]:
        raise SystemExit("Batch incomplete: HTTP/parse failures exist; inspect manifest")

if __name__=="__main__": main()
