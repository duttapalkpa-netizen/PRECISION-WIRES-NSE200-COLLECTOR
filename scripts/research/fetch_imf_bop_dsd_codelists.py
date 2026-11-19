#!/usr/bin/env python3
"""Fetch exact BOP DSD concept scheme and candidate codelists; no observation query."""
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
BASE="https://api.imf.org/external/sdmx/3.0/structure"
OUT=Path("imf_bop_dsd_codelists"); OUT.mkdir(exist_ok=True)
TARGETS=[
 ("DSD_BOP","datastructure","IMF.STA","DSD_BOP","24.0.0"),
 ("CS_BOP","conceptscheme","IMF.STA","CS_BOP","17.0.0"),
 ("CS_MASTER_SYSTEM","conceptscheme","IMF","CS_MASTER_SYSTEM","+"),
 ("CL_UNIT_MULT","codelist","IMF","CL_UNIT_MULT","+"),
 ("CL_BOP_COUNTRY","codelist","IMF.STA","CL_BOP_COUNTRY","1.0.0"),
 ("CL_BOP_ACCOUNTING_ENTRY","codelist","IMF.STA","CL_BOP_ACCOUNTING_ENTRY","3.3.0"),
 ("CL_BOP_INDICATOR","codelist","IMF.STA","CL_BOP_INDICATOR","10.0.0"),
 ("CL_UNIT","codelist","IMF","CL_UNIT","2.13.0"),
 ("CL_FREQ","codelist","IMF","CL_FREQ","1.2.0"),
 ("CL_BOP_CURRENCY","codelist","IMF.STA","CL_BOP_CURRENCY","3.1.1"),
]
def sha(b):return hashlib.sha256(b).hexdigest()
def local(t):return t.split("}")[-1]
results=[]
for name,typ,agency,obj,ver in TARGETS:
 url=f"{BASE}/{typ}/{agency}/{obj}/{ver}?references=all"
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-IMF-BOP-DSD-audit/1.0","Accept":"application/vnd.sdmx.structure+xml, application/xml"})
 try:
  with urlopen(req,timeout=45) as r: status=r.status; final=r.geturl(); headers=dict(r.headers.items()); body=r.read()
 except HTTPError as e: status=e.code; final=e.geturl(); headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
 except (URLError,TimeoutError) as e: status=0; final=url; headers={}; body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 fn=name+".xml";(OUT/fn).write_bytes(body)
 row={"name":name,"requested_url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":sha(body),"file":fn}
 if status==200:
  try:
   root=ET.fromstring(body);row["xml_parse"]="PASS";row["root"]=root.tag
   if typ=="codelist":
    codes=[]
    for e in root.iter():
     if local(e.tag)=="Code" and e.attrib.get("id"):
      names=[(x.text or "").strip() for x in e if local(x.tag)=="Name" and (x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang","en")=="en")]
      codes.append({"id":e.attrib["id"],"name":names[0] if names else None})
    row["code_count"]=len(codes);row["codes"]=codes
   elif typ=="conceptscheme":
    concepts=[]
    for e in root.iter():
     if local(e.tag)=="Concept" and e.attrib.get("id"):
      concepts.append({"id":e.attrib["id"],"children":[{"tag":local(x.tag),"attributes":x.attrib,"text":(x.text or "").strip()} for x in e]})
    row["concept_count"]=len(concepts);row["concepts"]=concepts
   elif typ=="datastructure":
    dims=[]
    for e in root.iter():
     if local(e.tag)=="Dimension" and e.attrib.get("id"):
      dims.append({"id":e.attrib["id"],"position":e.attrib.get("position"),"concept_identity":next(((x.text or "").strip() for x in e if local(x.tag)=="ConceptIdentity"),None),
        "children":[{"tag":local(x.tag),"attributes":x.attrib,"text":(x.text or "").strip()} for x in e]})
    row["dimensions"]=sorted(dims,key=lambda x:int(x["position"]))
    row["maintainables"]=[{"tag":local(e.tag),"attributes":e.attrib} for e in root.iter() if local(e.tag) in ("Codelist","ConceptScheme","DataStructure") and e.attrib.get("id")]
  except Exception as e:row["xml_parse"]="FAIL";row["parse_error"]=str(e)
 results.append(row)
(OUT/"manifest.json").write_text(json.dumps({"scope":"BOP DSD exact dimension order and concept/codelist validation; no data observations queried","responses":results},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(results,indent=2,ensure_ascii=False))
