#!/usr/bin/env python3
"""Capture exact Brazil registration lifecycle evidence for IMF tx 667.

Read-only. Separates transaction index Date from Registration.lastUpdated.
Archives raw responses, safe headers, UTC retrieval timestamps, byte counts,
SHA-256, parse outcomes and any registration history entries. Never stores
Set-Cookie/authentication headers.
"""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from urllib.parse import quote
import hashlib,json,zipfile,io,xml.etree.ElementTree as ET

BASE="https://sdmxcentral.imf.org"
PA="urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)"
REG="urn:sdmx:org.sdmx.infomodel.registry.Registration=IMF:D429E36CD161E2F2A34ECAF137994E89(1.0)"
OUT=Path("imf_brazil_exact_registration")
OUT.mkdir(parents=True,exist_ok=True)
q=lambda x:quote(x,safe="")
URLS=[
 ("registration_history",BASE+"/ws/registry/tx/history?urn="+q(REG),"json"),
 ("transaction_667_full",BASE+"/ws/registry/tx/transactions?txId=667","xml"),
 ("transaction_667_fusion",BASE+"/ws/registry/tx/transactions?txId=667&format=fusion-json","json"),
 ("transaction_667_registration_item",BASE+"/ws/registry/tx/transaction?txId=667&urn="+q(REG),"zip"),
 ("registration_structure_v2",BASE+"/sdmx/v2/structure/registration/IMF/D429E36CD161E2F2A34ECAF137994E89/1.0","xml"),
 ("transaction_index_2023_09_22",BASE+"/ws/registry/tx/searchTransactions?dateFrom=1695340800000&dateTo=1695427199999&max=5000&orderDesc=false","json"),
]
records=[]
for name,url,kind in URLS:
    retrieved=datetime.now(timezone.utc).isoformat()
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-independent-audit/1.3","Accept":"application/json, application/xml, text/xml, application/zip, */*"})
    try:
        with urlopen(req,timeout=40) as r:
            status=r.status; headers=dict(r.headers.items()); body=r.read()
    except HTTPError as e:
        status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
    except (URLError,TimeoutError) as e:
        status=0; headers={}; body=str(e).encode()
    safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
    ext={"json":"json","xml":"xml","zip":"zip"}[kind]
    fn=name+"."+ext
    (OUT/fn).write_bytes(body)
    rec={"name":name,"requested_url":url,"retrieved_at_utc":retrieved,"http_status":status,
         "response_headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"body_file":fn}
    if status==200 and kind=="json":
        try:
            data=json.loads(body)
            if isinstance(data,list):
                rec["item_count"]=len(data); rec["items"]=[]
                for x in data:
                    y=dict(x)
                    if isinstance(y.get("Date"),(int,float)):
                        y["Date_UTC"]=datetime.fromtimestamp(y["Date"]/1000,timezone.utc).isoformat()
                    rec["items"].append(y)
                if name=="transaction_index_2023_09_22":
                    rec["target_transaction"]=[x for x in rec["items"] if x.get("Id")==667]
            else:
                rec["json_preview"]=data
                if name=="transaction_667_fusion":
                    regs=data.get("Registration",[])
                    if isinstance(regs,dict): regs=[regs]
                    rec["registrations"]=[{"urn":x.get("urn"),"id":x.get("id"),
                        "provisionAgreementReference":x.get("provisionAgreementReference"),
                        "dataUrl":(x.get("dataSource") or {}).get("dataUrl"),
                        "lastUpdated":x.get("lastUpdated")} for x in regs]
        except Exception as e: rec["parse_error"]=str(e)
    elif status==200 and kind=="xml":
        try:
            root=ET.fromstring(body); rec["xml_root"]=root.tag
            rec["xml_parse_status"]="PASS"
            rec["contains_registration_request"]=b"SubmitRegistrationRequest" in body
            rec["contains_query_registration_response"]=b"QueryRegistrationResponse" in body
            rec["target_markers"]=[s for s in (PA,REG,"bcb.gov.br") if s.encode().lower() in body.lower()]
        except Exception as e: rec["parse_error"]=str(e)
    elif status==200 and kind=="zip":
        try:
            z=zipfile.ZipFile(io.BytesIO(body))
            rec["zip_members"]=[{"name":x.filename,"byte_count":x.file_size,"sha256":hashlib.sha256(z.read(x)).hexdigest()} for x in z.infolist()]
        except Exception as e: rec["zip_parse_error"]=str(e)
    records.append(rec)
summary={"scope":"exact Brazil registration lifecycle probe; read-only",
         "target_pa_urn":PA,"registration_urn":REG,"transaction_id":667,
         "response_count":len(records),"http_200_count":sum(x["http_status"]==200 for x in records),
         "responses":records}
(OUT/"manifest.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
