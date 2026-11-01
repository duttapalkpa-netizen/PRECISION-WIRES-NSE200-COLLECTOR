#!/usr/bin/env python3
"""Build evidence-only macro-indicator overlay and same-snapshot Factor Registry audit.

Inputs are downloaded from pinned successful workflow runs. Partial releases are
kept DATA_QUALITY_WARN; PMI is NOT_CONNECTED without a licensed feed. No
production selector, ranking score, or factor state is changed.
"""
from __future__ import annotations
import hashlib,json
from pathlib import Path
import pandas as pd

ROOT=Path(".")
BASE=ROOT/"outputs/macro_geo"
INPUT=ROOT/"inputs/macro_evidence"
SOURCES={
 "gdp":{"dir":"gdp","qa":"domain_qa.json","manifest":"manifest.json","expected":"PASS"},
 "cpi":{"dir":"cpi","qa":"domain_qa.json","manifest":"manifest.json","expected":"PASS"},
 "wpi":{"dir":"wpi","qa":"domain_qa.json","manifest":"manifest.json","expected":"PASS"},
 "capex":{"dir":"capex","qa":"domain_qa.json","manifest":"manifest.json","expected":"PASS"},
 "pmi":{"dir":"pmi","qa":"access_assessment.json","manifest":"manifest.json","expected":"ACCESS_ASSESSMENT_PASS"},
}
def read_json(path):
 if not path.is_file(): raise RuntimeError(f"Missing required evidence file: {path}")
 return json.loads(path.read_text())
def verify_raw_hash(folder,manifest,keys):
 verified=[]
 for key in keys:
  name=manifest.get(key)
  if not name: continue
  p=folder/name
  if not p.is_file(): raise RuntimeError(f"Missing raw evidence file: {p}")
  digest=hashlib.sha256(p.read_bytes()).hexdigest()
  if digest!=manifest.get("sha256") and digest!=manifest.get(key.replace("raw_file","sha256")):
   # Some multi-source manifests carry per-source SHA fields.
   expected=manifest.get(key.replace("_raw_file","_sha256"))
   if not expected or digest!=expected: raise RuntimeError(f"Raw hash mismatch: {p}")
  verified.append({"file":name,"bytes":p.stat().st_size,"sha256":digest})
 return verified
def main():
 BASE.mkdir(parents=True,exist_ok=True)
 evidence={}
 times=[]
 for name,spec in SOURCES.items():
  folder=INPUT/spec["dir"]
  qa=read_json(folder/spec["qa"]); manifest=read_json(folder/spec["manifest"])
  if qa.get("status")!=spec["expected"] and qa.get("assessment_status")!=spec["expected"]:
   raise RuntimeError(f"{name} QA status mismatch: {qa.get('status') or qa.get('assessment_status')}")
  if name=="gdp":
   raw=manifest.get("raw_file")
   if not raw: raise RuntimeError("GDP manifest missing raw_file")
   hashes=verify_raw_hash(folder,manifest,["raw_file"])
  elif name=="cpi":
   hashes=verify_raw_hash(folder,manifest,["raw_file"])
  elif name=="wpi":
   hashes=verify_raw_hash(folder,manifest,["raw_file"])
  elif name=="capex":
   hashes=[]
   for rawkey,hashkey in [("cga_raw_file","cga_sha256"),("pib_raw_file","pib_sha256")]:
    raw=manifest.get(rawkey)
    if raw:
     p=folder/raw
     if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=manifest.get(hashkey):
      raise RuntimeError(f"Capex raw evidence hash mismatch: {raw}")
     hashes.append({"file":raw,"bytes":p.stat().st_size,"sha256":manifest[hashkey]})
  else:
   hashes=[]
   for k,v in qa.get("sources",{}).items():
    raw=v.get("raw_file")
    if raw:
     p=folder/raw
     if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=v.get("sha256"):
      raise RuntimeError(f"PMI raw source hash mismatch: {raw}")
     hashes.append({"file":raw,"bytes":p.stat().st_size,"sha256":v["sha256"]})
  captured=manifest.get("retrieved_at_utc")
  if captured: times.append(pd.to_datetime(captured,utc=True))
  evidence[name]={"qa_status":qa.get("status") or qa.get("assessment_status"),
    "captured_at_utc":captured,"workflow_run_id":spec["run_id"],
    "artifact_id":spec["artifact_id"],"artifact_name":spec["artifact_name"],
    "manifest":manifest,"domain_qa":qa,"verified_raw_files":hashes}
 # Reconcile existing P0/source-repair inventory; preserve its real observed timestamps.
 report=read_json(BASE/"factor_source_collection_report.json")
 coverage=read_json(BASE/"source_coverage.json")
 sources=coverage.setdefault("sources",[])
 by={x.get("source"):x for x in sources if isinstance(x,dict)}
 # These official monthly/headline collections are valid bounded evidence, but not
 # complete, continuous, normalized macro-indicator factor-series coverage.
 for source,notes in [
  ("macro_indicators","GDP single-quarter live table + CPI September 2026 + WPI September 2026 release; partial official evidence only, not complete monthly factor series."),
  ("government_capex","CGA FY2026-27 April-September cumulative YTD only; not standalone monthly capex flow or full history."),
 ]:
  row=by.get(source)
  if row is None: row={"source":source}; sources.append(row); by[source]=row
  row.update({"status":"DATA_QUALITY_WARN","rows":0,"observed_rows":1,
    "selected_path":"","evidence_path":"inputs/macro_evidence/",
    "reason":notes,"notes":notes})
 pmi=by.get("pmi_underlying_dataset")
 if pmi is None: pmi={"source":"pmi_underlying_dataset"}; sources.append(pmi)
 pmi.update({"status":"NOT_CONNECTED","rows":0,"observed_rows":0,"selected_path":"",
   "reason":"No licensed subscription/data feed/API credentials; only public headline/calendar access assessment passed.",
   "notes":"Underlying PMI dataset remains UNKNOWN, not negative."})
 # Compose an immutable evidence snapshot with per-source capture times retained.
 valid=[t for t in times if pd.notna(t)]
 baseline=pd.to_datetime(coverage.get("as_of_utc"),errors="coerce",utc=True)
 if pd.notna(baseline): valid.append(baseline)
 if not valid: raise RuntimeError("No real UTC snapshot timestamp")
 snapshot=max(valid).isoformat().replace("+00:00","Z")
 coverage["as_of_utc"]=snapshot
 coverage["supplemental_macro_evidence"]={
  "snapshot_created_at_utc":pd.Timestamp.now(tz="UTC").isoformat(),
  "snapshot_semantics":"Immutable composite evidence snapshot; individual source capture timestamps retained; not simultaneous collection.",
  "sources":evidence,
  "status_policy":{"macro_indicators":"DATA_QUALITY_WARN","government_capex":"DATA_QUALITY_WARN","pmi_underlying_dataset":"NOT_CONNECTED"},
  "invariants":["No production selector change","No RANKING_SCORE change","No +1 PRESSURE_FADE change",
    "No 672-diagnostic change","UNKNOWN is neither PASS nor FAIL","No synthetic observations or inferred release timestamps"]}
 BASE.joinpath("source_coverage.json").write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+"\n")
 # Run existing audited factor map against this exact as_of_utc.
 import subprocess,sys
 subprocess.run([sys.executable,"pipeline/macro_geo_factor_coverage_audit.py"],check=True)
 audit=read_json(BASE/"factor_coverage_audit.json")
 if audit.get("source_coverage_as_of")!=snapshot: raise RuntimeError("Factor audit/source coverage snapshot mismatch")
 if audit.get("factor_groups")!=35: raise RuntimeError("Factor Registry group count is not 35")
 if audit.get("fully_available_schema_groups")!=0: raise RuntimeError("Unexpected full schema availability; review before acceptance")
 result={"status":"SAME_SNAPSHOT_AUDIT_PASS_WITH_GAPS","snapshot_as_of_utc":snapshot,
  "factor_groups":audit["factor_groups"],"fully_available_schema_groups":audit["fully_available_schema_groups"],
  "partial_source_coverage":audit["partial_source_coverage"],"not_connected":audit["not_connected"],
  "macro_indicators_status":by["macro_indicators"]["status"],
  "government_capex_status":by["government_capex"]["status"],
  "pmi_underlying_dataset_status":by["pmi_underlying_dataset"]["status"],
  "source_evidence":{k:{"workflow_run_id":v["workflow_run_id"],"artifact_id":v["artifact_id"],
    "qa_status":v["qa_status"],"captured_at_utc":v["captured_at_utc"],
    "verified_raw_files":v["verified_raw_files"]} for k,v in evidence.items()},
  "invariants_preserved":True,"hard_gate":"BLOCKED",
  "interpretation":"Same-snapshot consistency PASS means the 35-factor audit is tied to one immutable composite inventory timestamp. It does not mean macro source groups are fully covered or that factor effects are validated."}
 (BASE/"macro_indicator_evidence_snapshot.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
