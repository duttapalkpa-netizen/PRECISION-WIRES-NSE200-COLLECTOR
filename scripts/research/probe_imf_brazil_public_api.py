#!/usr/bin/env python3
"""Probe public IMF SDMX Central transaction-history and structure routes.

This is a read-only endpoint discovery/capture. It does not submit or mutate
registrations. Every response (including non-200 responses) is archived with
request URL, retrieval UTC, status, headers, byte count and SHA-256.
"""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import quote
import hashlib, json, xml.etree.ElementTree as ET

OUT = Path("imf_brazil_public_api_probe")
OUT.mkdir(parents=True, exist_ok=True)
pa_urn = "urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)"
urls = [
    ("pa_transaction_history", "https://sdmxcentral.imf.org/ws/registry/tx/history?urn=" + quote(pa_urn, safe="")),
    ("pa_structure_v2", "https://sdmxcentral.imf.org/sdmx/v2/structure/provisionagreement/IMF/BR_BOP_BP6/1.0?references=all"),
    ("current_rss", "https://sdmxcentral.imf.org/rss.xml"),
]
records=[]
for name,url in urls:
    retrieved=datetime.now(timezone.utc).isoformat()
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-independent-audit/1.0","Accept":"application/json, application/vnd.sdmx.structure+xml;version=2.1, application/xml, text/xml, */*"})
    try:
        with urlopen(req,timeout=45) as response:
            status=response.status; headers=dict(response.headers.items()); body=response.read()
    except HTTPError as e:
        status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
    except (URLError, TimeoutError) as e:
        status=0; headers={}; body=str(e).encode()
    suffix=".xml" if (b"<" in body[:200] or "xml" in headers.get("Content-Type","").lower()) else ".json"
    (OUT/(name+suffix)).write_bytes(body)
    record={"name":name,"requested_url":url,"retrieved_at_utc":retrieved,"http_status":status,
            "response_headers":headers,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),
            "body_file":name+suffix}
    if name=="current_rss" and status==200:
        try:
            root=ET.fromstring(body)
            items=root.findall(".//item")
            record["rss_item_count"]=len(items)
            record["rss_items"]=[{"title":(x.findtext("title") or ""),"link":(x.findtext("link") or ""),"pubDate":(x.findtext("pubDate") or "")} for x in items]
        except ET.ParseError as e: record["parse_error"]=str(e)
    if name=="pa_transaction_history" and status==200:
        try:
            data=json.loads(body)
            record["history_item_count"]=len(data) if isinstance(data,list) else None
            record["history_preview"]=data[:10] if isinstance(data,list) else data
        except Exception as e: record["parse_error"]=str(e)
    records.append(record)
(OUT/"manifest.json").write_text(json.dumps({"scope":"public read-only IMF SDMX Central endpoint probe","pa_urn":pa_urn,"responses":records},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(records,indent=2,ensure_ascii=False))
