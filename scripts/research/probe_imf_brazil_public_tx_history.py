#!/usr/bin/env python3
"""Public IMF SDMX Central transaction-history probe for Brazil PA and related flows."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from urllib.parse import urlencode
OUT=Path("artifacts/imf_brazil_public_tx_history");OUT.mkdir(parents=True,exist_ok=True)
BASE="https://sdmxcentral.imf.org/ws/registry/tx"
URNS={
 "brazil_pa":"urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)",
 "bop6_dataflow":"urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP6(1.0)",
 "bop_bpm6_dataflow":"urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP_BPM6(1.0)",
}
def get(url):
 ts=datetime.now(timezone.utc).isoformat();req=Request(url,headers={"User-Agent":"PRECISION-WIRES-public-registry-history/1.0","Accept":"application/json"})
 try:
  with urlopen(req,timeout=30) as r: status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
 p=OUT/(hashlib.sha256(url.encode()).hexdigest()[:12]+".json");p.write_bytes(body)
 return {"requested_url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":{k:v for k,v in headers.items() if k.lower() not in ("set-cookie","authorization")},"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":p.name,"body":body}
manifest={"source":"IMF SDMX Central public Fusion Registry transaction web service","base":BASE,"urns":{},"started_utc":datetime.now(timezone.utc).isoformat()}
for key,urn in URNS.items():
 u=BASE+"/history?"+urlencode({"urn":urn});r=get(u);body=r.pop("body");item=r
 if r["http_status"]==200:
  try:
   j=json.loads(body);item["parsed"]=j if isinstance(j,list) else {"response_type":type(j).__name__}
   item["row_count"]=len(j) if isinstance(j,list) else None
  except Exception as e:item["parse_error"]=str(e)
 manifest["urns"][key]={"urn":urn,**item}
# For any transaction IDs returned for PA, retrieve public transaction payload XML (the API is read-only).
pa=manifest["urns"]["brazil_pa"];transactions=pa.get("parsed",[])
details=[]
if isinstance(transactions,list):
 for t in transactions:
  tx=t.get("Id")
  if tx is None:continue
  url=BASE+"/transactions?"+urlencode({"urn":URNS["brazil_pa"],"format":"sdmx-ml"})
  # Transaction endpoint requires transactionId; use documented parameter name after probing query contract.
  url=BASE+"/transactions?"+urlencode({"transactionId":tx,"format":"sdmx-ml"})
  d=get(url);body=d.pop("body");d["transaction_id"]=tx
  details.append(d)
manifest["transaction_details"]=details
manifest["finished_utc"]=datetime.now(timezone.utc).isoformat()
success=pa.get("http_status")==200 and isinstance(transactions,list)
manifest["overall_status"]="PASS" if success else "BLOCKED"
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"overall_status":manifest["overall_status"],"urns":{k:{x:v.get(x) for x in ("http_status","byte_count","sha256","row_count","parsed","parse_error")} for k,v in manifest["urns"].items()},"transaction_details":[{k:v.get(k) for k in ("transaction_id","http_status","byte_count","sha256")} for v in details]},indent=2))
if not success:raise SystemExit("Public PA transaction history unavailable")
