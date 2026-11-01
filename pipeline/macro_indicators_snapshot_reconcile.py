#!/usr/bin/env python3
"""Pinned macro-series evidence ledger and conservative same-snapshot Factor Registry reconciliation."""
# PRODUCTION_SELECTOR, RANKING_SCORE, +1 PRESSURE_FADE and all 672 diagnostics are read-only invariants.
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
I=Path("inputs"); O=Path("outputs/macro_geo")
PINS={
"macro_series":(41283471652,13073712835),"gdp":(41285765677,13074739522),
"cpi":(41286559713,13074709251),"wpi":(41287256251,13075163044),
"cga":(41287828206,13076111188),"pmi":(41287685168,13076305289),
"factor_source":(41282726166,13074122025)}
def j(p):
 p=Path(p)
 if not p.is_file(): raise RuntimeError("Missing evidence "+str(p))
 return json.loads(p.read_text())
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def require(x,msg):
 if not x: raise RuntimeError(msg)
def main():
 # Verify each exact artifact's own QA and raw evidence, retaining source-specific times.
 mroot=I/"macro_series"; mq=j(mroot/"outputs/macro_geo/macro_series_observation_qa.json")
 require(mq["status"]=="NORMALIZED_PARTIAL_SERIES_WITH_PROVENANCE_LIMITS","macro-series QA changed")
 for f,k in [("data/external/macro_series_observations.csv","sha256"),("data/external/macro_indicators.csv","registry_macro_sha256"),("data/external/inflation_components.csv","inflation_components_sha256")]:
  require(h(mroot/f)==mq[k],"macro series hash mismatch "+f)
 g=I/"gdp"; gq=j(g/"domain_qa.json"); gm=j(g/"manifest.json")
 require(gq["status"]=="PASS" and gq["table_id"]=="AEQEAFY2607QTR" and h(g/gm["raw_file"])==gm["sha256"],"GDP QA/hash mismatch")
 c=I/"cpi"; cq=j(c/"domain_qa.json"); cm=j(c/"manifest.json")
 require(cq["status"]=="PASS" and all(cq["domain_checks"].values()) and h(c/cm["raw_file"])==cm["sha256"],"CPI QA/hash mismatch")
 require(cq["workbook"]["headline_observation"]=={"base_year":2024,"state_code":"00","state_name":"All India","sector":"Combined","year":2026,"month":"September","index":109.49,"inflation_percent":5.54,"status":"P"},"CPI headline mismatch")
 w=I/"wpi"; wq=j(w/"domain_qa.json"); wm=j(w/"manifest.json")
 require(wq["status"]=="PASS" and all(wq["domain_checks"].values()) and h(w/wm["raw_file"])==wm["sha256"],"WPI QA/hash mismatch")
 cap=I/"cga"; capq=j(cap/"domain_qa.json"); capm=j(cap/"manifest.json")
 require(capq["status"]=="PASS" and all(capq["domain_checks"].values()),"CGA QA mismatch")
 require(h(cap/"CGA_Monthly_Accounts_September_2026.html")==capm["cga_sha256"] and h(cap/"PIB_Monthly_Accounts_Review_September_2026.html")==capm["pib_sha256"],"CGA/PIB hash mismatch")
 p=I/"pmi"; pq=j(p/"access_assessment.json"); pm=j(p/"manifest.json")
 require(pq["status"]=="ACCESS_ASSESSMENT_PASS" and pq["underlying_dataset_status"]=="NOT_CONNECTED" and pq["promotable_rows"]==0,"PMI must remain NOT_CONNECTED")
 for k,v in pm["sources"].items(): require(h(p/v["raw_file"])==v["sha256"],"PMI hash mismatch "+k)
 f=I/"factor_source"; cov=j(f/"outputs/macro_geo/source_coverage.json"); report=j(f/"outputs/macro_geo/factor_source_collection_report.json")
 require(report["observed_at_utc"]=="2026-11-01T06:55:50.179961+00:00" and cov["as_of_utc"]=="2026-11-01T06:58:34.877945+00:00","Unexpected factor-source baseline snapshot")
 # Fail closed: these are bounded smokes/partial normalized series, not complete series.
 by={x.get("source"):x for x in cov.get("sources",[]) if isinstance(x,dict)}
 def setrow(name,status,obs,why,detail):
  row=by.get(name)
  if row is None: row={"source":name}; cov.setdefault("sources",[]).append(row); by[name]=row
  row.update({"status":status,"rows":0,"observed_rows":obs,"selected_path":"",
    "missing_columns":["complete historical series and point-in-time publication provenance"],
    "reason":why,"notes":"Evidence is preserved in the immutable snapshot ledger; bounded evidence is not promoted to AVAILABLE."})
  row["bounded_evidence"]=detail
 macro={"run_id":PINS["macro_series"][0],"artifact_id":PINS["macro_series"][1],"status":mq["status"],"rows":mq["total_observations"],"sha256":mq["sha256"],"sources":mq["sources"]}
 gd={"run_id":PINS["gdp"][0],"artifact_id":PINS["gdp"][1],"status":"PASS_BOUNDED_SMOKE_ONLY","table_id":gq["table_id"],"period":"Q1 FY2026-27","raw_sha256":gm["sha256"],"retrieved_at_utc":gm["retrieved_at_utc"]}
 ci={"run_id":PINS["cpi"][0],"artifact_id":PINS["cpi"][1],"status":"PASS_BOUNDED_SMOKE_ONLY","period":"September 2026","headline":cq["workbook"]["headline_observation"],"raw_sha256":cm["sha256"],"retrieved_at_utc":cm["retrieved_at_utc"],"scope":"Other dimensional tabs primarily August; no full history."}
 wi={"run_id":PINS["wpi"][0],"artifact_id":PINS["wpi"][1],"status":"PASS_BOUNDED_RELEASE_SMOKE_ONLY","period":wq["reference_period"],"base_year":wq["base_year"],"provisional":wq["provisional"],"observations":wq["observations"],"raw_sha256":wm["sha256"],"retrieved_at_utc":wm["retrieved_at_utc"]}
 cg={"run_id":PINS["cga"][0],"artifact_id":PINS["cga"][1],"status":"PASS_BOUNDED_YTD_SMOKE_ONLY","period":capq["reference_period"],"observed":capq["observed"],"raw_sha256":{"cga":capm["cga_sha256"],"pib":capm["pib_sha256"]},"retrieved_at_utc":capm["retrieved_at_utc"],"scope":"Cumulative Apr-Sep YTD, provisional; not standalone September flow."}
 pi={"run_id":PINS["pmi"][0],"artifact_id":PINS["pmi"][1],"status":"ACCESS_ASSESSMENT_PASS_DATA_NOT_CONNECTED","classification":pq["access_classification"],"http_statuses":{k:v["http_status"] for k,v in pm["sources"].items()},"retrieved_at_utc":pm["retrieved_at_utc"]}
 setrow("macro_indicators","DATA_QUALITY_WARN",mq["total_observations"],"GDP/CPI/WPI evidence is bounded or partial; no complete point-in-time historical macro series.",{"gdp":gd,"cpi":ci,"wpi":wi,"normalized_panel":macro})
 setrow("inflation_components","DATA_QUALITY_WARN",mq["inflation_component_rows"],"CPI/WPI components remain partial; complete monthly dimensions and release-vintage alignment pending.",{"cpi":ci,"wpi":wi})
 setrow("government_capex","DATA_QUALITY_WARN",capq["observed"]["actual_ytd_crore"] and mq["sources"]["government_capex"]["rows"],"CGA September YTD smoke passes but complete historical monthly vintages are not available.",cg)
 setrow("pmi","NOT_CONNECTED",0,"Underlying PMI history is licensed; no license/feed credentials supplied.",pi)
 # Recompute inventory counters after conservative overrides; BLOCKED remains separate.
 statuses=[x.get("status") for x in cov.get("sources",[]) if isinstance(x,dict)]
 cov["sources_total"]=len(statuses)
 cov["available"]=sum(x in ("AVAILABLE","AVAILABLE_SECONDARY") for x in statuses)
 cov["not_connected"]=sum(x=="NOT_CONNECTED" for x in statuses)
 cov["schema_fail"]=sum(x=="SCHEMA_FAIL" for x in statuses)
 cov["quality_warn"]=sum(x=="DATA_QUALITY_WARN" for x in statuses)
 cov["read_error"]=sum(x=="READ_ERROR" for x in statuses)
 cov["blocked"]=sum(x=="BLOCKED" for x in statuses)
 # Deterministic identity of exact artifact IDs; snapshot clock is assembly time.
 snapshot=json.dumps(PINS,sort_keys=True,separators=(",",":")).encode()
 sid=hashlib.sha256(snapshot).hexdigest()
 asof=datetime.now(timezone.utc).isoformat().replace("+00:00","Z")
 cov["as_of_utc"]=asof; cov["evidence_snapshot_id"]=sid
 cov["snapshot_semantics"]="Composite immutable artifact set; source retrieval timestamps are retained individually and are not claimed to be simultaneous."
 cov["macro_indicators_snapshot_ledger"]={"snapshot_id":sid,"snapshot_as_of_utc":asof,"pinned_artifacts":PINS,"evidence":{"macro_series":macro,"gdp":gd,"cpi":ci,"wpi":wi,"cga":cg,"pmi":pi},"factor_source_baseline":{"run_id":PINS["factor_source"][0],"artifact_id":PINS["factor_source"][1],"observed_at_utc":report["observed_at_utc"],"baseline_as_of_utc":report["observed_at_utc"]}}
 O.mkdir(parents=True,exist_ok=True)
 (O/"source_coverage.json").write_text(json.dumps(cov,indent=2)+chr(10))
 (O/"macro_indicators_snapshot_ledger.json").write_text(json.dumps(cov["macro_indicators_snapshot_ledger"],indent=2)+chr(10))
 print(json.dumps({"snapshot_id":sid,"snapshot_as_of_utc":asof,"evidence_inputs_verified":7,"macro_indicators":"DATA_QUALITY_WARN","inflation_components":"DATA_QUALITY_WARN","government_capex":"DATA_QUALITY_WARN","pmi":"NOT_CONNECTED"},indent=2))
if __name__=="__main__": main()
