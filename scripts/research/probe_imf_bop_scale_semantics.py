#!/usr/bin/env python3
"""Retrieve the exact IMF concept scheme referenced by BOP DSD SCALE attribute."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,xml.etree.ElementTree as ET
URL="https://api.imf.org/external/sdmx/3.0/structure/conceptscheme/IMF/CS_MASTER_SYSTEM/1.0.2?references=all"
OUT=Path("imf_bop_scale_semantics");OUT.mkdir(parents=True,exist_ok=True)
ts=datetime.now(timezone.utc).isoformat()
req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-scale-concept-audit/1.0","Accept":"application/vnd.sdmx.structure+xml, application/xml"})
try:
 with urlopen(req,timeout=60) as r:status=r.status;headers=dict(r.headers.items());body=r.read()
except HTTPError as e:status=e.code;headers=dict(e.headers.items()) if e.headers else {};body=e.read()
except (URLError,TimeoutError) as e:status=0;headers={};body=str(e).encode()
safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
(OUT/"CS_MASTER_SYSTEM_1.0.2.xml").write_bytes(body)
record={"url":URL,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest()}
concepts={}
if status==200:
 root=ET.fromstring(body);record["xml_root"]=root.tag
 for el in root.iter():
  if el.tag.split("}")[-1]=="Concept" and el.attrib.get("id") in {"SCALE","PRECISION","DECIMALS_DISPLAYED","UNIT_MULT"}:
   d={"id":el.attrib.get("id"),"attributes":el.attrib,"names":[],"descriptions":[],"annotations":[],"representations":[]}
   for x in el.iter():
    t=x.tag.split("}")[-1]
    if t=="Name":d["names"].append({"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text})
    elif t=="Description":d["descriptions"].append({"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text})
    elif t=="Annotation":d["annotations"].append(" ".join(y.text or "" for y in x.iter() if y.tag.split("}")[-1] in {"AnnotationTitle","AnnotationText"}))
    elif t in {"TextFormat","Enumeration","LocalRepresentation"}:d["representations"].append({"tag":t,"attributes":x.attrib})
   concepts[d["id"]]=d
record["target_concepts"]=concepts
record["scale_definition_found"]=bool(concepts.get("SCALE",{}).get("descriptions") or concepts.get("SCALE",{}).get("annotations"))
record["decision"]="DEFINITION_RETRIEVED" if record["scale_definition_found"] else "CONCEPT_SCHEME_RESPONSE_HAS_NO_SCALE_DEFINITION"
(OUT/"manifest.json").write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(record,indent=2,ensure_ascii=False))
if status!=200:raise SystemExit(f"Concept scheme HTTP {status}")
if "SCALE" not in concepts:raise SystemExit("SCALE concept absent from referenced concept scheme")
