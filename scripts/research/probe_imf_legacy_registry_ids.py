#!/usr/bin/env python3
"""Probe whether IMF SDMX Central exposes the exact legacy Data Portal artefact IDs.
Read-only; preserves every response body, status, headers, retrieval time and SHA-256.
"""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import hashlib, json, xml.etree.ElementTree as ET

OUT=Path("imf_legacy_registry_probe"); OUT.mkdir(exist_ok=True)
BASE="https://sdmxcentral.imf.org/sdmx/v2/structure"
targets=[
 ("legacy_dsd_v24", f"{BASE}/datastructure/IMF/DSD_BOP/24.0.0/?format=sdmx-3.0&detail=full&references=all"),
 ("legacy_flow_v21", f"{BASE}/dataflow/IMF/BOP/21.0.0/?format=sdmx-3.0&detail=full&references=all"),
]
rows=[]
for name,url in targets:
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-GCR-legacy-registry-probe/1.0","Accept":"application/vnd.sdmx.structure+xml;version=3.0"})
 ts=datetime.now(timezone.utc).isoformat()
 try:
  with urlopen(req,timeout=35) as r: status=r.status; headers=dict(r.headers.items()); final=r.geturl(); body=r.read()
 except HTTPError as e: status=e.code; headers=dict(e.headers.items()) if e.headers else {}; final=url; body=e.read()
 except (URLError,TimeoutError) as e: status=0; headers={}; final=url; body=str(e).encode()
 fn=name+".xml"; (OUT/fn).write_bytes(body)
 rec={"name":name,"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":headers,"bytes":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":fn}
 try:
  root=ET.fromstring(body); rec["xml_parse"]="PASS"; rec["root"]=root.tag
  rec["maintainable_ids"]=[{"id":e.attrib.get("id"),"agencyID":e.attrib.get("agencyID"),"version":e.attrib.get("version")} for e in root.iter() if e.tag.split("}")[-1] in ("DataStructure","Dataflow")]
 except Exception as e: rec["xml_parse"]="FAIL" if status==200 else "NOT_XML"; rec["parse_error"]=str(e)[:500]
 rows.append(rec)
manifest={"scope":"public IMF SDMX Central registry probe for exact legacy Data Portal artefact identifiers; no observations","retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"responses":rows}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps(manifest,indent=2))
# Transport errors are archived, not conflated with absence; artifact always uploads.
