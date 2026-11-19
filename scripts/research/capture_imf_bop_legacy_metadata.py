#!/usr/bin/env python3
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
OUT=Path("imf_bop_legacy_metadata"); OUT.mkdir(exist_ok=True)
BASE="https://api.imf.org/external/sdmx/3.0/structure"
targets=[
 ("dsd_bop_v24","/datastructure/IMF.STA/DSD_BOP/24.0.0?references=all&format=xml"),
 ("bop_flow_v21","/dataflow/IMF.STA/BOP/21.0.0?references=all&format=xml"),
]
rows=[]
for name,path in targets:
 url=BASE+path; ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-GCR-legacy-structure-audit/1.0","Accept":"application/vnd.sdmx.structure+xml;version=3.0"})
 try:
  with urlopen(req,timeout=45) as r: status=r.status; headers=dict(r.headers.items()); final=r.geturl(); body=r.read()
 except HTTPError as e: status=e.code; headers=dict(e.headers.items()) if e.headers else {}; final=url; body=e.read()
 except (URLError,TimeoutError) as e: status=0; headers={}; final=url; body=str(e).encode()
 fn=name+".xml"; (OUT/fn).write_bytes(body)
 rec={"name":name,"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":{k:v for k,v in headers.items() if k.lower() not in ("set-cookie","authorization")},"bytes":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":fn}
 if status==200:
  try:
   root=ET.fromstring(body); rec["root"]=root.tag; names=[e.tag.split("}")[-1] for e in root.iter()]
   rec["local_element_counts"]={x:names.count(x) for x in sorted(set(names)) if x in ("DataStructure","Dataflow","Dimension","Codelist","Code","ContentConstraint","DataConstraint","Ref")}
   rec["xml_parse"]="PASS"
  except Exception as e: rec["xml_parse"]="FAIL"; rec["error"]=str(e)
 else: rec["xml_parse"]="NOT_RUN"
 rows.append(rec)
manifest={"scope":"IMF Data Portal legacy BOP metadata only; no observations; exact versions","retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"responses":rows}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps(manifest,indent=2))
if not all(x["http_status"]==200 and x["xml_parse"]=="PASS" for x in rows): raise SystemExit("one or more legacy metadata requests not verified")
