#!/usr/bin/env python3
"""Offline integrity audit of the immutable 40-event Brazil IMF registration artifact."""
import argparse,csv,hashlib,json,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime,timezone
EXPECTED_ZIP="2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41"
EXPECTED_REG="D429E36CD161E2F2A34ECAF137994E89"
EXPECTED_PA=("IMF","BR_BOP_BP6","1.0")
EXPECTED_URL="https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
def lname(x):return x.rsplit("}",1)[-1]
def main():
 ap=argparse.ArgumentParser();ap.add_argument("artifact_zip");ap.add_argument("--out",default="brazil_registration_history_audit");a=ap.parse_args()
 p=Path(a.artifact_zip);blob=p.read_bytes();zsha=hashlib.sha256(blob).hexdigest()
 if zsha!=EXPECTED_ZIP:raise SystemExit(f"FAIL artifact SHA mismatch: {zsha}")
 z=zipfile.ZipFile(p);hist=json.loads(z.read("imf_brazil_registration_lifecycle/registration_history.json"));events=json.loads(z.read("imf_brazil_registration_lifecycle/event_index.json"))
 if len(hist)!=40 or len(events)!=40:raise SystemExit("FAIL event count not 40/40")
 txids=[e["tx_id"] for e in events]
 if len(set(txids))!=40:raise SystemExit("FAIL duplicate transaction IDs")
 ordered=sorted(events,key=lambda e:e["transaction_date_epoch_ms"])
 if events!=ordered:raise SystemExit("FAIL event index not chronological")
 results=[];errors=[]
 for e in events:
  tid=e["tx_id"];xmlpath=f"imf_brazil_registration_lifecycle/xml/tx_{tid:05d}.xml"
  raw=z.read(xmlpath);root=ET.fromstring(raw)
  els=list(root.iter()); reg=[x for x in els if lname(x.tag)=="Registration"]
  if len(reg)!=1:errors.append(f"{tid}: expected one Registration element");continue
  r=reg[0];refs=[x for x in r.iter() if lname(x.tag)=="ProvisionAgreement"]
  if len(refs)!=1:errors.append(f"{tid}: expected one ProvisionAgreement ref");continue
  ref=refs[0];pa=(ref.attrib.get("agencyID"),ref.attrib.get("id"),ref.attrib.get("version"))
  urls=[(x.text or "").strip() for x in r.iter() if lname(x.tag)=="DataURL"]
  # XML SimpleDataSource uses text leaf under DataURL; fallback inspect all text for exact URL.
  has_url=any(EXPECTED_URL.lower()==(x.text or "").strip().lower() for x in r.iter())
  has_regid=any(EXPECTED_REG==v for x in r.iter() for v in list(x.attrib.values())+[x.text or ""])
  txdt=datetime.fromisoformat(e["transaction_date_utc"].replace("Z","+00:00"))
  upd=datetime.fromisoformat(e["registration_lastUpdated"]+"+00:00")
  delta=(txdt-upd).total_seconds()
  ok=(e["http_status"]==200 and e["item_parse_status"]=="PASS" and pa==EXPECTED_PA and has_url and has_regid and e["registry_history_action"]=="Replace" and e["sdmx_registration_request_action"]=="Information" and 0<=delta<=20)
  if not ok:errors.append(f"{tid}: semantic/timestamp check failed pa={pa} url={has_url} regid={has_regid} delta={delta}")
  results.append({"tx_id":tid,"event_utc":e["transaction_date_utc"],"registry_action":e["registry_history_action"],"registry_type":e.get("registry_history_type") or "MISSING_IN_HISTORY_ROW","request_action":e["sdmx_registration_request_action"],"registration_lastUpdated":e["registration_lastUpdated"],"event_minus_updated_seconds":delta,"pa_id":":".join(pa),"registered_url_match":has_url,"registration_id_match":has_regid,"xml_sha256":e["xml_sha256"],"status":"PASS" if ok else "FAIL"})
 # Completeness of returned snapshot only; do not infer events before/after.
 out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
 with (out/"event_audit.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
 types_missing=sum(not e.get("registry_history_type") for e in events)
 summary={"source_artifact_zip_sha256":zsha,"history_http_status":200,"history_retrieved_at_utc":json.loads(z.read("imf_brazil_registration_lifecycle/summary.json"))["history_retrieved_at_utc"],"event_count":len(events),"unique_transaction_ids":len(set(txids)),"chronological_order":True,"first_event_utc":ordered[0]["transaction_date_utc"],"last_event_utc":ordered[-1]["transaction_date_utc"],"registration_id_unique":len(set(e["registration_id"] for e in events))==1,"provision_agreement_unique":len(set((e["provision_agreement_ref"]["agencyID"],e["provision_agreement_ref"]["id"],e["provision_agreement_ref"]["version"]) for e in events))==1,"data_url_unique":len(set(e["data_url"] for e in events))==1,"all_registry_actions_replace":all(e["registry_history_action"]=="Replace" for e in events),"all_request_actions_information":all(e["sdmx_registration_request_action"]=="Information" for e in events),"history_type_missing_count":types_missing,"xml_semantic_checks_pass":len(results)-len(errors),"xml_semantic_checks_total":len(events),"errors":errors,"scope_note":"Audits the exact 40 events returned by the public history endpoint at retrieval time; does not prove events outside that returned set or resolve PA/Dataflow identity."}
 summary["overall_status"]="PASS" if not errors and len(results)==40 else "FAIL"
 (out/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
 print(json.dumps(summary,indent=2))
 if errors:raise SystemExit(1)
if __name__=="__main__":main()
