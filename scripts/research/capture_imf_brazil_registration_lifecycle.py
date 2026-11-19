#!/usr/bin/env python3
"""Capture and independently validate all public history events for Brazil PA registration.

Fetches the registration URN history, then retrieves each exact transaction item
as a ZIP. It preserves raw history JSON, every ZIP, every embedded XML, hashes,
transaction timestamps/actions, and SDMX RegistrationRequest fields. Registry
history Action and SDMX RegistrationRequest@action are stored separately.
"""
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from urllib.parse import quote
import csv,hashlib,io,json,zipfile,xml.etree.ElementTree as ET

BASE="https://sdmxcentral.imf.org"
REG="urn:sdmx:org.sdmx.infomodel.registry.Registration=IMF:D429E36CD161E2F2A34ECAF137994E89(1.0)"
TARGET_PA="urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)"
TARGET_URL="https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
OUT=Path("imf_brazil_registration_lifecycle")
RAW=OUT/"transactions"; XML=OUT/"xml"
RAW.mkdir(parents=True,exist_ok=True); XML.mkdir(parents=True,exist_ok=True)
q=lambda x:quote(x,safe="")

def request(url,timeout=40):
    retrieved=datetime.now(timezone.utc).isoformat()
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-independent-audit/1.4","Accept":"application/zip, application/json, application/xml, text/xml, */*"})
    try:
        with urlopen(req,timeout=timeout) as r:
            status=r.status; headers=dict(r.headers.items()); body=r.read()
    except HTTPError as e:
        status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
    except (URLError,TimeoutError) as e:
        status=0; headers={}; body=str(e).encode()
    safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
    return {"retrieved_at_utc":retrieved,"http_status":status,"headers":safe,"body":body}

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    history_url=BASE+"/ws/registry/tx/history?urn="+q(REG)
    hr=request(history_url)
    (OUT/"registration_history.json").write_bytes(hr["body"])
    if hr["http_status"]!=200: raise SystemExit(f"history HTTP {hr['http_status']}")
    history=json.loads(hr["body"])
    if not isinstance(history,list) or not history: raise SystemExit("history response empty or invalid")
    history.sort(key=lambda x:int(x["Date"]))
    records=[]
    for item in history:
        records.append({"tx_id":int(item["Id"]),"transaction_date_epoch_ms":int(item["Date"]),
          "transaction_date_utc":datetime.fromtimestamp(int(item["Date"])/1000,timezone.utc).isoformat(),
          "registry_history_action":item.get("Action"),"registry_history_type":item.get("Type")})
    def fetch_event(event):
        txid=event["tx_id"]
        url=BASE+"/ws/registry/tx/transaction?txId="+str(txid)+"&urn="+q(REG)
        result=request(url)
        raw=result.pop("body")
        zip_name=f"tx_{txid:05d}.zip"
        (RAW/zip_name).write_bytes(raw)
        row={**event,"transaction_item_url":url,**result,"zip_file":"transactions/"+zip_name,
             "zip_byte_count":len(raw),"zip_sha256":sha(raw)}
        if result["http_status"]!=200:
            row["item_parse_status"]="HTTP_NOT_200"
            return row
        try:
            z=zipfile.ZipFile(io.BytesIO(raw))
            members=z.namelist()
            row["zip_member_count"]=len(members)
            row["zip_members"]=members
            if len(members)!=1: raise ValueError(f"expected one ZIP member, got {len(members)}")
            xml_bytes=z.read(members[0])
            xml_name=f"tx_{txid:05d}.xml"
            (XML/xml_name).write_bytes(xml_bytes)
            row["xml_file"]="xml/"+xml_name
            row["xml_byte_count"]=len(xml_bytes)
            row["xml_sha256"]=sha(xml_bytes)
            root=ET.fromstring(xml_bytes)
            row["xml_root"]=root.tag
            # namespace agnostic lookup
            def local(el,name):
                return next((x for x in el.iter() if x.tag.split("}")[-1]==name),None)
            rr=local(root,"RegistrationRequest")
            reg=local(root,"Registration")
            pa=local(root,"ProvisionAgreement")
            datasource=local(root,"SimpleDataSource")
            ref=local(pa,"Ref") if pa is not None else None
            row["sdmx_registration_request_action"]=rr.attrib.get("action") if rr is not None else None
            row["registration_id"]=reg.attrib.get("id") if reg is not None else None
            row["registration_lastUpdated"]=reg.attrib.get("lastUpdated") if reg is not None else None
            row["provision_agreement_ref"]=(dict(ref.attrib) if ref is not None else None)
            row["data_url"]=datasource.text if datasource is not None else None
            row["registration_id_match"]=row["registration_id"]=="D429E36CD161E2F2A34ECAF137994E89"
            row["provision_agreement_match"]=bool(ref is not None and ref.attrib.get("agencyID")=="IMF" and ref.attrib.get("id")=="BR_BOP_BP6" and ref.attrib.get("version")=="1.0")
            row["data_url_match"]=row["data_url"]==TARGET_URL
            row["item_parse_status"]="PASS"
        except Exception as e:
            row["item_parse_status"]="FAIL"; row["parse_error"]=str(e)
        return row
    out=[]
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures=[pool.submit(fetch_event,x) for x in records]
        for f in as_completed(futures): out.append(f.result())
    out.sort(key=lambda x:x["tx_id"])
    (OUT/"event_index.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    fields=["tx_id","transaction_date_epoch_ms","transaction_date_utc","registry_history_action","registry_history_type",
      "http_status","zip_byte_count","zip_sha256","xml_byte_count","xml_sha256","sdmx_registration_request_action",
      "registration_id","registration_lastUpdated","provision_agreement_ref","data_url",
      "registration_id_match","provision_agreement_match","data_url_match","item_parse_status"]
    with (OUT/"event_index.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for x in out:
            y=dict(x)
            if isinstance(y.get("provision_agreement_ref"),dict): y["provision_agreement_ref"]=json.dumps(y["provision_agreement_ref"],sort_keys=True)
            w.writerow({k:y.get(k) for k in fields})
    ok=[x for x in out if x.get("item_parse_status")=="PASS"]
    summary={"scope":"all events returned by public /ws/registry/tx/history for exact Brazil Registration URN as retrieved at runtime",
      "registration_urn":REG,"target_pa_urn":TARGET_PA,"target_data_url":TARGET_URL,
      "history_http_status":hr["http_status"],"history_retrieved_at_utc":hr["retrieved_at_utc"],
      "history_byte_count":len(hr["body"]),"history_sha256":sha(hr["body"]),
      "history_event_count":len(history),"transaction_item_http_200_count":sum(x["http_status"]==200 for x in out),
      "transaction_item_parse_pass_count":len(ok),"registration_id_match_count":sum(x.get("registration_id_match") is True for x in ok),
      "pa_match_count":sum(x.get("provision_agreement_match") is True for x in ok),
      "data_url_match_count":sum(x.get("data_url_match") is True for x in ok),
      "all_events_have_same_registration_identity":bool(ok) and all(x.get("registration_id_match") and x.get("provision_agreement_match") and x.get("data_url_match") for x in ok),
      "first_event":out[0] if out else None,"last_event":out[-1] if out else None,
      "failed_items":[{"tx_id":x["tx_id"],"status":x["http_status"],"parse":x.get("item_parse_status")} for x in out if x.get("item_parse_status")!="PASS"],
      "important_semantics":"registry_history_action and SDMX RegistrationRequest@action are separate source fields; do not conflate them."}
    (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    if summary["history_event_count"]!=summary["transaction_item_http_200_count"] or summary["transaction_item_parse_pass_count"]!=summary["history_event_count"]:
        raise SystemExit("Lifecycle capture incomplete: some transaction item downloads/parses failed")

if __name__=="__main__": main()
