#!/usr/bin/env python3
"""Archive and compare official SDMx-BOP DSD v2.6.0 serialization availability."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import xml.etree.ElementTree as ET
OUT=Path("artifacts/sdmx_bop_260");OUT.mkdir(parents=True,exist_ok=True)
URLS={
 "sdmx_21":"https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1",
 "sdmx_30":"https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-3.0",
}
def sha(b):return hashlib.sha256(b).hexdigest()
m={"source":"SDMx Global Registry official BOP DSD","maintainer":"IMF","maintainable_id":"BOP","version":"2.6.0","retrieval_started_utc":datetime.now(timezone.utc).isoformat(),"responses":{}}
for k,u in URLS.items():
 ts=datetime.now(timezone.utc).isoformat();req=Request(u,headers={"User-Agent":"PRECISION-WIRES-SDMx-BOP-DSD-audit/1.0","Accept":"application/xml"})
 try:
  with urlopen(req,timeout=45) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());b=r.read(50*1024*1024+1)
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};b=e.read()
 except (URLError,TimeoutError) as e:status=0;final=u;headers={};b=str(e).encode()
 p=OUT/f"{k}.xml";p.write_bytes(b)
 row={"requested_url":u,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"content_type":headers.get("Content-Type"),"etag":headers.get("ETag"),"last_modified":headers.get("Last-Modified"),"byte_count":len(b),"sha256":sha(b),"file":p.name}
 if status==200:
  try:
   root=ET.fromstring(b);row["xml_root"]=root.tag
   counts={}
   for e in root.iter():
    name=e.tag.rsplit("}",1)[-1];counts[name]=counts.get(name,0)+1
   row["element_counts"]={x:counts.get(x,0) for x in ("DataStructure","DataStructureComponents","Dimension","TimeDimension","PrimaryMeasure","Attribute","Codelist","Concept","Dataflow","ProvisionAgreement")}
   row["xml_parse"]="PASS"
  except Exception as e:row["xml_parse"]="FAIL";row["parse_error"]=str(e)
 m["responses"][k]=row
m["retrieval_finished_utc"]=datetime.now(timezone.utc).isoformat()
ok=all(x.get("http_status")==200 and x.get("xml_parse")=="PASS" for x in m["responses"].values())
m["overall_status"]="PASS" if ok else "PARTIAL_OR_BLOCKED"
(OUT/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
print(json.dumps(m,indent=2))
if not ok:raise SystemExit("One or more official DSD serialization captures did not parse")
