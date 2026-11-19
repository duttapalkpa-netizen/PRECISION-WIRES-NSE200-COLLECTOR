#!/usr/bin/env python3
"""Retrieve IMF SCALE concept and its referenced code list, if any."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,xml.etree.ElementTree as ET
BASE="https://api.imf.org/external/sdmx/3.0/structure"
OUT=Path("imf_bop_scale_semantics");OUT.mkdir(parents=True,exist_ok=True)
def get(url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-scale-concept-audit/1.1","Accept":"application/vnd.sdmx.structure+xml, application/xml"})
 try:
  with urlopen(req,timeout=60) as r:status=r.status;headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 return {"url":url,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"body":body}
def local(x):return x.split("}")[-1]
def parse_concept(el):
 d={"id":el.attrib.get("id"),"attributes":el.attrib,"names":[],"descriptions":[],"annotations":[],"enumeration_refs":[],"text_formats":[]}
 for x in el.iter():
  t=local(x.tag)
  if t=="Name":d["names"].append({"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text})
  elif t=="Description":d["descriptions"].append({"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text})
  elif t=="Annotation":d["annotations"].append(" ".join(y.text or "" for y in x.iter() if local(y.tag) in {"AnnotationTitle","AnnotationText"}))
  elif t=="Ref":d["enumeration_refs"].append(x.attrib)
  elif t=="TextFormat":d["text_formats"].append(x.attrib)
 return d
def main():
 url=BASE+"/conceptscheme/IMF/CS_MASTER_SYSTEM/1.0.2?references=all"
 r=get(url);(OUT/"CS_MASTER_SYSTEM_1.0.2.xml").write_bytes(r["body"])
 rec={k:v for k,v in r.items() if k!="body"}
 if r["http_status"]!=200:raise SystemExit(f"Concept scheme HTTP {r['http_status']}")
 root=ET.fromstring(r["body"]);rec["xml_root"]=root.tag
 concepts={}
 for el in root.iter():
  if local(el.tag)=="Concept" and el.attrib.get("id") in {"SCALE","PRECISION","DECIMALS_DISPLAYED"}:
   concepts[el.attrib["id"]]=parse_concept(el)
 rec["target_concepts"]=concepts
 refs=concepts.get("SCALE",{}).get("enumeration_refs",[])
 code_lists=[]
 for ref in refs:
  agency=ref.get("agencyID");cid=ref.get("id");version=ref.get("version")
  if not agency or not cid or not version:continue
  cu=BASE+f"/codelist/{agency}/{cid}/{version}?references=none"
  cr=get(cu);fn=f"{cid}_{version}.xml";(OUT/fn).write_bytes(cr["body"])
  cinfo={k:v for k,v in cr.items() if k!="body"};cinfo["file"]=fn;cinfo["codes"]=[]
  if cr["http_status"]==200:
   rt=ET.fromstring(cr["body"])
   for cl in rt.iter():
    if local(cl.tag)=="Codelist" and cl.attrib.get("id")==cid:
     for code in cl.iter():
      if local(code.tag)=="Code":
       names=[{"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text} for x in code if local(x.tag)=="Name"]
       descriptions=[{"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text} for x in code if local(x.tag)=="Description"]
       cinfo["codes"].append({"id":code.attrib.get("id"),"names":names,"descriptions":descriptions})
  code_lists.append(cinfo)
 rec["referenced_scale_codelists"]=code_lists
 rec["scale_definition_found"]=bool(concepts.get("SCALE",{}).get("descriptions") or concepts.get("SCALE",{}).get("annotations") or any(x.get("codes") for x in code_lists))
 rec["decision"]="CONCEPT_AND_CODELIST_RETRIEVED" if rec["scale_definition_found"] else "CONCEPT_HAS_NO_DEFINITION_OR_CODELIST_LABELS"
 (OUT/"manifest.json").write_text(json.dumps(rec,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(rec,indent=2,ensure_ascii=False))
 if "SCALE" not in concepts:raise SystemExit("SCALE concept absent")
if __name__=="__main__":main()
