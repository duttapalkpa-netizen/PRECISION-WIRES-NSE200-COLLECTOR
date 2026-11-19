#!/usr/bin/env python3
"""Retrieve IMF BOP SCALE concept and its enumerated unit-multiplier codelist."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,xml.etree.ElementTree as ET,re
BASE="https://api.imf.org/external/sdmx/3.0/structure"
OUT=Path("imf_bop_scale_semantics");OUT.mkdir(parents=True,exist_ok=True)
def get(url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-scale-concept-audit/1.2","Accept":"application/vnd.sdmx.structure+xml, application/xml"})
 try:
  with urlopen(req,timeout=60) as r:status=r.status;headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 return {"url":url,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"body":body}
def local(x):return x.split("}")[-1]
def main():
 url=BASE+"/conceptscheme/IMF/CS_MASTER_SYSTEM/+?references=none"
 r=get(url);(OUT/"CS_MASTER_SYSTEM_latest.xml").write_bytes(r["body"])
 rec={k:v for k,v in r.items() if k!="body"}
 if r["http_status"]!=200:raise SystemExit(f"Concept scheme HTTP {r['http_status']}")
 root=ET.fromstring(r["body"]);rec["xml_root"]=root.tag
 concepts={}
 for el in root.iter():
  if local(el.tag)=="Concept" and el.attrib.get("id") in {"SCALE","PRECISION","DECIMALS_DISPLAYED"}:
   d={"id":el.attrib.get("id"),"names":[],"descriptions":[],"enumeration_urns":[]}
   for x in el.iter():
    t=local(x.tag)
    if t=="Name":d["names"].append({"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text})
    elif t=="Description":d["descriptions"].append({"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text})
    elif t=="Enumeration" and x.text:d["enumeration_urns"].append(x.text.strip())
   concepts[d["id"]]=d
 rec["target_concepts"]=concepts
 refs=concepts.get("SCALE",{}).get("enumeration_urns",[])
 codelists=[]
 for urn in refs:
  m=re.search(r"Codelist=([^:]+):([^ (]+)\(([^)]+)\)",urn)
  if not m:continue
  agency,cid,version=m.groups()
  url2=BASE+f"/codelist/{agency}/{cid}/+?references=none"
  cr=get(url2);(OUT/f"{cid}_latest.xml").write_bytes(cr["body"])
  ci={k:v for k,v in cr.items() if k!="body"};ci["requested_codelist_urn"]=urn;ci["codes"]=[]
  if cr["http_status"]==200:
   rt=ET.fromstring(cr["body"]);ci["xml_root"]=rt.tag
   for cl in rt.iter():
    if local(cl.tag)=="Codelist" and cl.attrib.get("id")==cid:
     ci["codelist_version"]=cl.attrib.get("version")
     for code in cl.iter():
      if local(code.tag)=="Code":
       names=[{"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text} for x in code if local(x.tag)=="Name"]
       desc=[{"lang":x.attrib.get("{http://www.w3.org/XML/1998/namespace}lang"),"text":x.text} for x in code if local(x.tag)=="Description"]
       ci["codes"].append({"id":code.attrib.get("id"),"names":names,"descriptions":desc})
  codelists.append(ci)
 rec["referenced_codelists"]=codelists
 code6=[c for cl in codelists for c in cl.get("codes",[]) if c.get("id")=="6"]
 rec["scale_code_6"]=code6
 rec["scale_semantics_status"]="PASS_CODE6_MILLIONS_10_POWER_6" if any(any(n.get("lang")=="en" and n.get("text")=="Millions" for n in c.get("names",[])) and any("10^6" in (d.get("text") or "") for d in c.get("descriptions",[]) if d.get("lang")=="en") for c in code6) else "UNKNOWN"
 (OUT/"manifest.json").write_text(json.dumps(rec,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(rec,indent=2,ensure_ascii=False))
 if rec["scale_semantics_status"]!="PASS_CODE6_MILLIONS_10_POWER_6":raise SystemExit("Could not verify SCALE code 6 as Millions (10^6)")
if __name__=="__main__":main()
