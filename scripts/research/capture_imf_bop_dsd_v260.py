#!/usr/bin/env python3
"""Capture public official SDMx Global Registry IMF BOP DSD v2.6.0 metadata.

No observation endpoint or key is guessed. Captures DSD 2.1/3.0 with all
referenced artefacts, records provenance and hashes, parses component/codelist
references, and reports metadata coverage only.
"""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,xml.etree.ElementTree as ET

BASE="https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/"
OUT=Path("imf_bop_dsd_v260"); OUT.mkdir(parents=True,exist_ok=True)
TARGETS=[
 ("sdmx21",BASE+"?references=all&format=sdmx-2.1","application/vnd.sdmx.structure+xml;version=2.1"),
 ("sdmx30",BASE+"?references=all&format=sdmx-3.0","application/vnd.sdmx.structure+xml;version=3.0"),
]
def sha(b): return hashlib.sha256(b).hexdigest()
def local(tag): return tag.split("}")[-1]
results=[]
for name,url,accept in TARGETS:
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-GCR-independent-metadata-audit/1.0","Accept":accept})
 try:
  with urlopen(req,timeout=60) as r:
   status=r.status; headers=dict(r.headers.items()); final_url=r.geturl(); body=r.read()
 except HTTPError as e:
  status=e.code; headers=dict(e.headers.items()) if e.headers else {}; final_url=url; body=e.read()
 except (URLError,TimeoutError) as e:
  status=0; headers={}; final_url=url; body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 fn=name+".xml"; (OUT/fn).write_bytes(body)
 rec={"name":name,"requested_url":url,"final_url":final_url,"retrieved_at_utc":ts,
      "http_status":status,"headers":safe,"byte_count":len(body),"sha256":sha(body),"file":fn}
 if status==200:
  try:
   root=ET.fromstring(body); rec["xml_root"]=root.tag
   all_e=list(root.iter())
   rec["maintainable_count"]=sum(1 for e in all_e if local(e.tag) in ("DataStructure","Codelist","ConceptScheme","CategoryScheme","Dataflow","ContentConstraint","DataConstraint","StructureMap"))
   rec["codelist_count"]=sum(1 for e in all_e if local(e.tag)=="Codelist")
   rec["conceptscheme_count"]=sum(1 for e in all_e if local(e.tag)=="ConceptScheme")
   rec["dataflow_count"]=sum(1 for e in all_e if local(e.tag)=="Dataflow")
   rec["constraint_count"]=sum(1 for e in all_e if local(e.tag) in ("ContentConstraint","DataConstraint"))
   rec["structure_references"]=[]
   for e in all_e:
    if local(e.tag)=="Ref" and e.attrib:
     d=dict(e.attrib)
     if d.get("class") in ("Codelist","DataStructure","ConceptScheme","Dataflow","ContentConstraint","DataConstraint"):
      rec["structure_references"].append(d)
   rec["unique_references"]=len({json.dumps(x,sort_keys=True) for x in rec["structure_references"]})
   rec["xml_parse_status"]="PASS"
  except Exception as e:
   rec["xml_parse_status"]="FAIL"; rec["parse_error"]=str(e)
 else:
  rec["xml_parse_status"]="NOT_RUN"
 results.append(rec)
manifest={"scope":"official SDMx Global Registry public BOP DSD v2.6.0 metadata only; no observations",
 "source_page":"https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/",
 "dsd_agency":"IMF","dsd_id":"BOP","dsd_version":"2.6.0",
 "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"responses":results}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(manifest,indent=2,ensure_ascii=False))
if not all(x["http_status"]==200 and x.get("xml_parse_status")=="PASS" for x in results):
 raise SystemExit("BOP DSD metadata capture incomplete")
