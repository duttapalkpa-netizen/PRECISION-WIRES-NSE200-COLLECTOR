#!/usr/bin/env python3
"""Bounded, read-only IMF SDMX Central Brazil history/API probe.

Captures PA, linked Dataflow and Data Provider history; the exact historical
transaction payload for the PA history ID; PA-item ZIP export; a narrow
transaction search around the reported event; and the current RSS window.
No credentials/cookies are retained. Every response has URL, UTC retrieval
time, status, safe headers, bytes, SHA-256 and parse summary.
"""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import quote
import hashlib, json, zipfile, io, xml.etree.ElementTree as ET

OUT = Path("imf_brazil_public_api_probe")
OUT.mkdir(parents=True, exist_ok=True)
BASE = "https://sdmxcentral.imf.org"
PA = "urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)"
DF = "urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP6(1.0)"
DP = "urn:sdmx:org.sdmx.infomodel.base.DataProvider=IMF:DATA_PROVIDERS(1.0).BR1"
q = lambda x: quote(x, safe="")
urls = [
 ("pa_history", BASE+"/ws/registry/tx/history?urn="+q(PA), "json"),
 ("dataflow_history", BASE+"/ws/registry/tx/history?urn="+q(DF), "json"),
 ("provider_history", BASE+"/ws/registry/tx/history?urn="+q(DP), "json"),
 ("transaction_2_full", BASE+"/ws/registry/tx/transactions?txId=2", "xml"),
 ("transaction_2_pa_item", BASE+"/ws/registry/tx/transaction?txId=2&urn="+q(PA), "zip"),
 ("transaction_search_2023_sep", BASE+"/ws/registry/tx/searchTransactions?dateFrom=1693526400000&dateTo=1696118399999&max=1000&orderDesc=false", "json"),
 ("current_rss", BASE+"/rss.xml", "xml"),
]
records=[]
for name,url,kind in urls:
    retrieved=datetime.now(timezone.utc).isoformat()
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-independent-audit/1.1","Accept":"application/json, application/xml, text/xml, application/zip, */*"})
    try:
        with urlopen(req,timeout=45) as response:
            status=response.status; headers=dict(response.headers.items()); body=response.read()
    except HTTPError as e:
        status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
    except (URLError, TimeoutError) as e:
        status=0; headers={}; body=str(e).encode()
    # Never retain cookies or authentication-related response headers.
    safe_headers={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
    ext={"json":"json","xml":"xml","zip":"zip"}[kind]
    filename=name+"."+ext
    (OUT/filename).write_bytes(body)
    rec={"name":name,"requested_url":url,"retrieved_at_utc":retrieved,"http_status":status,
         "response_headers":safe_headers,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),
         "body_file":filename}
    if status==200 and kind=="json":
        try:
            data=json.loads(body)
            rec["item_count"]=len(data) if isinstance(data,list) else None
            if isinstance(data,list):
                rec["items"]=[]
                for x in data:
                    y=dict(x)
                    if isinstance(y.get("Date"),(int,float)):
                        y["Date_UTC"]=datetime.fromtimestamp(y["Date"]/1000,timezone.utc).isoformat()
                    rec["items"].append(y)
            else: rec["json_preview"]=data
        except Exception as e: rec["parse_error"]=str(e)
    if status==200 and kind=="xml":
        try:
            root=ET.fromstring(body)
            rec["xml_root"]=root.tag
            rec["xml_bytes_parse"]="PASS"
            rec["brazil_markers"]=[s for s in ("BR_BOP_BP6","BOP6(1.0)","BOP_BPM6(1.0)","DATA_PROVIDERS(1.0).BR1","bcb.gov.br") if s.encode().lower() in body.lower()]
            rec["transaction_request_elements"]=[x.tag.split("}")[-1] for x in root.iter() if "Request" in x.tag.split("}")[-1]]
        except Exception as e: rec["parse_error"]=str(e)
    if status==200 and kind=="zip":
        try:
            z=zipfile.ZipFile(io.BytesIO(body))
            rec["zip_members"]=[{"name":x.filename,"byte_count":x.file_size,"sha256":hashlib.sha256(z.read(x)).hexdigest()} for x in z.infolist()]
        except Exception as e: rec["zip_parse_error"]=str(e)
    records.append(rec)
(OUT/"manifest.json").write_text(json.dumps({"scope":"bounded read-only public IMF SDMX Central Brazil PA/Dataflow/Provider history and transaction retrieval","pa_urn":PA,"linked_dataflow_urn":DF,"linked_provider_urn":DP,"responses":records},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(records,indent=2,ensure_ascii=False))
