#!/usr/bin/env python3
"""Probe public IMF concept-scheme routes for the DSD_BOP SCALE concept."""
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
URLS=[
 ("api_wildcard","https://api.imf.org/external/sdmx/3.0/structure/conceptscheme/IMF/CS_MASTER_SYSTEM/+?references=all"),
 ("api_1_0","https://api.imf.org/external/sdmx/3.0/structure/conceptscheme/IMF/CS_MASTER_SYSTEM/1.0?references=all"),
 ("api_1_0_0","https://api.imf.org/external/sdmx/3.0/structure/conceptscheme/IMF/CS_MASTER_SYSTEM/1.0.0?references=all"),
 ("central_1_0","https://sdmxcentral.imf.org/sdmx/v2/structure/conceptscheme/IMF/CS_MASTER_SYSTEM/1.0?references=all"),
 ("central_1_0_0","https://sdmxcentral.imf.org/sdmx/v2/structure/conceptscheme/IMF/CS_MASTER_SYSTEM/1.0.0?references=all"),
]
OUT=Path("imf_scale_concept_route_probe");OUT.mkdir(exist_ok=True)
def local(t):return t.split("}")[-1]
def sha(b):return hashlib.sha256(b).hexdigest()
rows=[]
for name,url in URLS:
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-IMF-SCALE-audit/1.0","Accept":"application/xml, application/vnd.sdmx.structure+xml, */*"})
 try:
  with urlopen(req,timeout=35) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 fn=name+".xml";(OUT/fn).write_bytes(body)
 row={"name":name,"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":sha(body),"file":fn}
 if status==200:
  try:
   root=ET.fromstring(body);row["xml_parse"]="PASS";row["root"]=root.tag
   concepts=[]
   for e in root.iter():
    if local(e.tag)=="Concept" and e.attrib.get("id")=="SCALE":
     concepts.append({"attributes":e.attrib,"xml":ET.tostring(e,encoding="unicode")})
   row["scale_concepts"]=concepts
  except Exception as e:row["xml_parse"]="FAIL";row["parse_error"]=str(e)
 rows.append(row)
summary={"scope":"public route probe for exact IMF CS_MASTER_SYSTEM SCALE concept; no value conversion","responses":rows}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
