#!/usr/bin/env python3
"""Resolve IMF Data Portal BOP SCALE semantics from its exact DSD/concept/codelist."""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,xml.etree.ElementTree as ET
BASE="https://api.imf.org/external/sdmx/3.0/structure"
TARGETS=[
 ("bop_dsd",f"{BASE}/datastructure/IMF.STA/DSD_BOP/24.0.0?references=none"),
 ("master_concept_scheme",f"{BASE}/conceptscheme/IMF/CS_MASTER_SYSTEM/+?references=none"),
 ("unit_multiplier_codelist",f"{BASE}/codelist/IMF/CL_UNIT_MULT/+?references=none")
]
OUT=Path("imf_bop_scale_semantics");OUT.mkdir(exist_ok=True)
def local(t):return t.split("}")[-1]
def get(name,url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-IMF-SCALE-semantics/1.0","Accept":"application/vnd.sdmx.structure+xml, application/xml, */*"})
 try:
  with urlopen(req,timeout=60) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 (OUT/(name+".xml")).write_bytes(body)
 row={"name":name,"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":name+".xml"}
 if status==200:
  root=ET.fromstring(body);row["xml_parse"]="PASS";row["root"]=root.tag
  if name=="bop_dsd":
   attrs=[]
   for e in root.iter():
    if local(e.tag)=="Attribute" and e.attrib.get("id")=="SCALE":
     item={"id":e.attrib.get("id"),"attributes":e.attrib,"children":[]}
     for x in e:
      item["children"].append({"tag":local(x.tag),"attributes":x.attrib,"text":(x.text or "").strip()})
      if local(x.tag) in ("ConceptIdentity","LocalRepresentation"):
       item[local(x.tag)] = [{"tag":local(y.tag),"attributes":y.attrib,"text":(y.text or "").strip()} for y in x.iter()]
     attrs.append(item)
   row["scale_attribute_definitions"]=attrs
  elif name=="master_concept_scheme":
   concepts=[]
   for e in root.iter():
    if local(e.tag)=="Concept" and e.attrib.get("id") in ("SCALE","UNIT_MULT","PREFERRED_SCALE"):
     concepts.append({"id":e.attrib.get("id"),"urn":e.attrib.get("urn"),
      "names":[{"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":(x.text or "").strip()} for x in e if local(x.tag)=="Name"],
      "descriptions":[{"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":(x.text or "").strip()} for x in e if local(x.tag)=="Description"],
      "enumerations":[{"tag":local(y.tag),"attributes":y.attrib,"text":(y.text or "").strip()} for y in e.iter() if local(y.tag) in ("Enumeration","Ref")]})
   row["target_concepts"]=concepts
  elif name=="unit_multiplier_codelist":
   lists=[]
   for cl in root.iter():
    if local(cl.tag)=="Codelist" and cl.attrib.get("id")=="CL_UNIT_MULT":
     codes=[]
     for e in cl.iter():
      if local(e.tag)=="Code" and e.attrib.get("id"):
       codes.append({"id":e.attrib["id"],
        "names":[{"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":(x.text or "").strip()} for x in e if local(x.tag)=="Name"],
        "descriptions":[{"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":(x.text or "").strip()} for x in e if local(x.tag)=="Description"]})
     lists.append({"attributes":cl.attrib,"code_count":len(codes),"codes":codes})
   row["codelists"]=lists
 else:row["xml_parse"]="NOT_RUN"
 return row
rows=[get(n,u) for n,u in TARGETS]
for r in rows:
 if r["http_status"]!=200 or r.get("xml_parse")!="PASS":raise SystemExit(f"{r['name']} failed HTTP/XML")
summary={"scope":"Resolve IMF Data Portal DSD_BOP SCALE concept and exact enumerated codelist; no numeric transformation",
 "responses":rows,
 "decision_rule":"Do not rescale values until DSD attachment level and SCALE concept meaning are reconciled with source observation units and an independent official benchmark."}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
