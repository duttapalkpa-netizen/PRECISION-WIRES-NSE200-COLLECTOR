#!/usr/bin/env python3
"""Fail-closed evidence-only macro snapshot; never changes production selection."""
import argparse, hashlib, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

SOURCES = {
 "gdp": (41285765677,13074739522,"mospi-nas-gdp-bounded-live-smoke","domain_qa.json","PASS",
         [("Statement_Quarterly_Constant_31.08.2026.xlsx","sha256")]),
 "cpi": (41286559713,13074709251,"mospi-cpi-2024-bounded-live-smoke","domain_qa.json","PASS",
         [("CPI_Data_For_DIID_Sep26-12.10.2026.xlsx","sha256")]),
 "wpi": (41287256251,13075163044,"oea-wpi-2022-23-september-live-smoke","domain_qa.json","PASS",
         [("PIB_WPI_September_2026_release.html","sha256")]),
 "capex": (41287828206,13076111188,"cga-capex-fy2026-27-september-live-smoke","domain_qa.json","PASS",
         [("CGA_Monthly_Accounts_September_2026.html","cga_sha256"),("PIB_Monthly_Accounts_Review_September_2026.html","pib_sha256")]),
 "pmi": (41287685168,13076305289,"pmi-source-access-assessment","access_assessment.json","ACCESS_ASSESSMENT_PASS",
         [("product.response","sources.product.sha256"),("terms.response","sources.terms.sha256"),("calendar.response","sources.calendar.sha256")])
}
def digest(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()
def nested(d,key):
 for k in key.split("."): d=d.get(k,{}) if isinstance(d,dict) else {}
 return d
def load_source(name,root):
 run,aid,artifact,qa_name,expected,raws=SOURCES[name]; folder=root/name
 qa=json.loads((folder/qa_name).read_text()); m=json.loads((folder/"manifest.json").read_text())
 status=qa.get("status") or qa.get("assessment_status")
 if status!=expected: raise RuntimeError(f"{name}: QA status {status}, expected {expected}")
 captured=m.get("retrieved_at_utc")
 if not captured: raise RuntimeError(f"{name}: missing actual retrieval timestamp")
 datetime.fromisoformat(captured.replace("Z","+00:00"))
 verified=[]
 for filename,hkey in raws:
  p=folder/filename; want=nested(m,hkey)
  if not p.is_file() or not want: raise RuntimeError(f"{name}: missing raw file/hash {filename}")
  got=digest(p)
  if got.lower()!=str(want).lower(): raise RuntimeError(f"{name}: SHA-256 mismatch {filename}")
  size=nested(m,hkey.rsplit(".",1)[0]+".bytes") if "." in hkey else None
  if not size: size=m.get("bytes",m.get("cga_bytes" if hkey=="cga_sha256" else "pib_bytes" if hkey=="pib_sha256" else "bytes"))
  if size is not None and p.stat().st_size!=int(size): raise RuntimeError(f"{name}: byte-size mismatch {filename}")
  verified.append({"file":filename,"bytes":p.stat().st_size,"sha256":got})
 return {"workflow_run_id":run,"artifact_id":aid,"artifact_name":artifact,"qa_status":status,
         "captured_at_utc":captured,"manifest":m,"domain_qa":qa,"verified_raw_files":verified}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--input-root",default="inputs/macro_evidence"); ap.add_argument("--output-root",default="outputs/macro_geo"); a=ap.parse_args()
 root=Path(a.input_root); out=Path(a.output_root)
 evidence={n:load_source(n,root) for n in SOURCES}
 cp=out/"source_coverage.json"; rp=out/"factor_source_collection_report.json"
 if not cp.is_file() or not rp.is_file(): raise RuntimeError("Missing P0/factor-source baseline; refusing to invent coverage")
 coverage=json.loads(cp.read_text()); json.loads(rp.read_text())
 if not isinstance(coverage.get("sources"),list): raise RuntimeError("Invalid source coverage schema")
 by={x["source"]:x for x in coverage["sources"] if isinstance(x,dict) and isinstance(x.get("source"),str)}
 by.setdefault("macro_indicators",{"source":"macro_indicators"}).update(status="DATA_QUALITY_WARN",rows=0,observed_rows=3,selected_path="",evidence_path="inputs/macro_evidence/",reason="One GDP quarter, one CPI month and one WPI headline release only; complete continuous historical series/item-level data absent.")
 by.setdefault("government_capex",{"source":"government_capex"}).update(status="DATA_QUALITY_WARN",rows=0,observed_rows=1,selected_path="",evidence_path="inputs/macro_evidence/capex/",reason="CGA April-September FY2026-27 cumulative YTD only; no standalone monthly flow or historical panel.")
 by.setdefault("pmi_underlying_dataset",{"source":"pmi_underlying_dataset"}).update(status="NOT_CONNECTED",rows=0,observed_rows=0,selected_path="",reason="Public calendar/access assessment only; underlying PMI history requires licensed feed not supplied.")
 times=[datetime.fromisoformat(v["captured_at_utc"].replace("Z","+00:00")) for v in evidence.values()]
 if coverage.get("as_of_utc"): times.append(datetime.fromisoformat(coverage["as_of_utc"].replace("Z","+00:00")))
 snap=max(times).astimezone(timezone.utc).isoformat().replace("+00:00","Z")
 coverage["sources"]=[by.get(x.get("source"),x) if isinstance(x,dict) else x for x in coverage["sources"]]
 have={x.get("source") for x in coverage["sources"] if isinstance(x,dict)}
 for key in ("macro_indicators","government_capex","pmi_underlying_dataset"):
  if key not in have: coverage["sources"].append(by[key])
 coverage["as_of_utc"]=snap
 coverage["supplemental_macro_evidence"]={"snapshot_as_of_utc":snap,"semantics":"Composite inventory timestamp; individual source capture timestamps retained; not simultaneous collection.","sources":evidence,"invariants":["Production selector unchanged","RANKING_SCORE unchanged","+1 PRESSURE_FADE unchanged","672 diagnostics unchanged","UNKNOWN is neither PASS nor FAIL","No synthetic rows or fabricated timestamps"]}
 cp.write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+"\n")
 subprocess.run([sys.executable,"pipeline/macro_geo_factor_coverage_audit.py"],check=True)
 audit=json.loads((out/"factor_coverage_audit.json").read_text())
 if audit.get("source_coverage_as_of")!=snap or audit.get("factor_groups")!=35: raise RuntimeError("Same-snapshot/35-group audit assertion failed")
 result={"status":"SAME_SNAPSHOT_AUDIT_PASS_WITH_GAPS","snapshot_as_of_utc":snap,
 "factor_groups":audit["factor_groups"],"fully_available_schema_groups":audit["fully_available_schema_groups"],
 "partial_source_coverage":audit["partial_source_coverage"],"not_connected":audit["not_connected"],"unmapped":audit["unmapped"],
 "macro_indicators_status":by["macro_indicators"]["status"],"government_capex_status":by["government_capex"]["status"],
 "pmi_underlying_dataset_status":by["pmi_underlying_dataset"]["status"],"source_evidence":evidence,
 "invariants_preserved":True,"hard_gate":"BLOCKED",
 "interpretation":"Consistency PASS only; not full coverage, event-study validation, or candidate release approval."}
 op=out/"macro_indicator_evidence_snapshot.json"; op.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
 files=[cp,out/"factor_coverage_audit.json",out/"factor_coverage_audit.csv",op]
 man={"files":[{"path":str(p),"bytes":p.stat().st_size,"sha256":digest(p)} for p in files]}
 (out/"macro_indicator_evidence_snapshot_manifest.json").write_text(json.dumps(man,indent=2)+"\n")
 print(json.dumps({k:result[k] for k in ("status","snapshot_as_of_utc","factor_groups","fully_available_schema_groups","partial_source_coverage","not_connected","hard_gate")},indent=2))
if __name__=="__main__": main()
