#!/usr/bin/env python3
"""Probe tx2 structure items and current IMF BOP dataflow/DSD references.

Read-only. Separates Provision Agreement, Dataflow, Provider scheme and DSD
maintainables. Captures each raw response with safe headers, UTC time, status,
byte count, SHA-256 and parsed XML references.
"""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from urllib.parse import quote
import hashlib,json,xml.etree.ElementTree as ET

BASE="https://sdmxcentral.imf.org"
OUT=Path("imf_brazil_pa_structure_revision"); OUT.mkdir(parents=True,exist_ok=True)
PA="urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)"
DF="urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP6(1.0)"
DSD="urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=IMF:ECOFIN_DSD(1.0)"
DPS="urn:sdmx:org.sdmx.infomodel.base.DataProviderScheme=IMF:DATA_PROVIDERS(1.0)"
q=lambda x:quote(x,safe="")
targets=[
 ("tx2_pa_item",BASE+"/ws/registry/tx/transaction?txId=2&urn="+q(PA),"zip"),
 ("tx2_full_fusion_json",BASE+"/ws/registry/tx/transactions?txId=2&format=fusion-json","json"),
 ("tx2_full_sdmx_json",BASE+"/ws/registry/tx/transactions?txId=2&format=sdmx-json","json"),
 ("tx2_bop6_dataflow_item",BASE+"/ws/registry/tx/transaction?txId=2&urn="+q(DF),"zip"),
 ("tx2_ecofin_dsd_item",BASE+"/ws/registry/tx/transaction?txId=2&urn="+q(DSD),"zip"),
 ("tx2_provider_scheme_item",BASE+"/ws/registry/tx/transaction?txId=2&urn="+q(DPS),"zip"),
 ("current_bop6_dataflow",BASE+"/sdmx/v2/structure/dataflow/IMF/BOP6/1.0?references=all","xml"),
 ("current_bop_bpm6_dataflow",BASE+"/sdmx/v2/structure/dataflow/IMF/BOP_BPM6/1.0?references=all","xml"),
 ("current_ecofin_dsd",BASE+"/sdmx/v2/structure/datastructure/IMF/ECOFIN_DSD/1.0?references=all","xml"),
]
records=[]
for name,url,kind in targets:
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-independent-audit/1.6","Accept":"application/zip, application/xml, text/xml, */*"})
 try:
  with urlopen(req,timeout=45) as r: status=r.status; headers=dict(r.headers.items()); body=r.read()
 except HTTPError as e: status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
 except (URLError,TimeoutError) as e: status=0; headers={}; body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 ext="zip" if kind=="zip" else "xml"; fn=name+"."+ext;(OUT/fn).write_bytes(body)
 rec={"name":name,"url":url,"retrieved_at_utc":ts,"http_status":status,"headers":safe,
      "byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":fn}
 if status==200 and kind=="json":
  try:
   doc=json.loads(body); rec["json_root_type"]=type(doc).__name__
   rec["json_top_level_keys"]=list(doc.keys()) if isinstance(doc,dict) else []
   for key in ("ProvisionAgreement","Dataflow","DataStructure","DataProviderScheme","DataProvider","Registration"):
    val=doc.get(key,[]) if isinstance(doc,dict) else []
    if isinstance(val,dict): val=[val]
    if isinstance(val,list): rec[key+"_count"]=len(val); rec[key+"_ids"]=[x.get("urn") or x.get("id") for x in val if isinstance(x,dict)]
   rec["json_parse_status"]="PASS"
  except Exception as e: rec["json_parse_status"]="FAIL"; rec["json_parse_error"]=str(e)
 if status==200 and kind=="xml":
  try:
   root=ET.fromstring(body); rec["xml_root"]=root.tag
   refs=[]
   for e in root.iter():
    tag=e.tag.split("}")[-1]
    if tag in ("Dataflow","DataStructure","ProvisionAgreement","DataProviderScheme","Ref","Structure"):
     if e.attrib: refs.append({"tag":tag,"attributes":e.attrib})
   rec["structure_references"]=refs
  except Exception as e: rec["parse_error"]=str(e)
 if status==200 and kind=="zip":
  import zipfile,io
  try:
   z=zipfile.ZipFile(io.BytesIO(body)); rec["members"]=[]
   for item in z.infolist():
    b=z.read(item); rec["members"].append({"name":item.filename,"byte_count":len(b),"sha256":hashlib.sha256(b).hexdigest()})
    (OUT/(name+"_"+item.filename)).write_bytes(b)
  except Exception as e: rec["zip_parse_error"]=str(e)
 records.append(rec)
(OUT/"manifest.json").write_text(json.dumps({"scope":"tx2 historical item retrieval and current BOP structure route compatibility probe","responses":records},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(records,indent=2,ensure_ascii=False))
