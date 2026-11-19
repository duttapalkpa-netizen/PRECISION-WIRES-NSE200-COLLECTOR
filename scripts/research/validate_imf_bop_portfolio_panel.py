#!/usr/bin/env python3
"""Independent validator for IMF BOP portfolio panel versus broad raw captures."""
from pathlib import Path
from decimal import Decimal
from datetime import datetime
import csv,json,hashlib
ROOT=Path(".")
OUT=ROOT/"imf_bop_portfolio_panel_validation";OUT.mkdir(exist_ok=True)
PANEL=ROOT/"imf_bop_portfolio_exact_panel"
BROAD=ROOT/"imf_bop_broad_probe"
def read(path):
 with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def qindex(s):
 y,q=s.split("-Q");return int(y)*4+int(q)-1
panel=read(PANEL/"portfolio_flows_panel.csv")
keycols=["COUNTRY","BOP_ACCOUNTING_ENTRY","INDICATOR","UNIT","FREQUENCY","TIME_PERIOD"]
seen=set();dups=[]
for r in panel:
 k=tuple(r[x] for x in keycols)
 if k in seen:dups.append(k)
 seen.add(k)
checks=[];all_ok=True
panel_map={tuple(r[x] for x in keycols):r for r in panel}
attribute_mismatches=[]
for country in ["BRA","IND"]:
 broad=read(BROAD/(country+"_quarterly_all.csv"))
 for entry in ["A_NFA_T","L_NIL_T"]:
  exact=read(PANEL/f"{country}_{entry}_P_F_USD_Q.csv")
  exact_obs=[x for x in exact if (x.get("OBS_VALUE") or "").strip()]
  broad_map={(x["COUNTRY"],x["BOP_ACCOUNTING_ENTRY"],x["INDICATOR"],x["UNIT"],x["FREQUENCY"],x["TIME_PERIOD"]):x for x in broad
    if x["COUNTRY"]==country and x["BOP_ACCOUNTING_ENTRY"]==entry and x["INDICATOR"]=="P_F" and x["UNIT"]=="USD" and x["FREQUENCY"]=="Q" and "2015-Q1"<=x["TIME_PERIOD"]<="2026-Q3" and (x.get("OBS_VALUE") or "").strip()}
  exact_map={(x["COUNTRY"],x["BOP_ACCOUNTING_ENTRY"],x["INDICATOR"],x["UNIT"],x["FREQUENCY"],x["TIME_PERIOD"]):x for x in exact_obs}
  attr_matches=0
  for k,x in exact_map.items():
   y=panel_map.get(k)
   if y is None: attribute_mismatches.append({"key":k,"field":"<row>","raw":"present","normalized":"missing"})
   else:
    bad=[col for col,val in x.items() if y.get(col)!=val]
    if bad: attribute_mismatches.extend({"key":k,"field":col,"raw":x.get(col),"normalized":y.get(col)} for col in bad)
    else: attr_matches+=1
  missing=[k for k in exact_map if k not in broad_map]
  mismatch=[]
  for k,x in exact_map.items():
   y=broad_map.get(k)
   if y and Decimal(x["OBS_VALUE"])!=Decimal(y["OBS_VALUE"]):mismatch.append({"key":k,"exact":x["OBS_VALUE"],"broad":y["OBS_VALUE"]})
  periods=sorted(x["TIME_PERIOD"] for x in exact_obs)
  contiguous=bool(periods) and all(qindex(b)-qindex(a)==1 for a,b in zip(periods,periods[1:]))
  expected_min="2015-Q1"; expected_max=periods[-1] if periods else None
  row={"country":country,"entry":entry,"exact_nonempty_count":len(exact_obs),
   "broad_matching_count":len(broad_map),"exact_period_min":periods[0] if periods else None,
   "exact_period_max":expected_max,"exact_broad_value_matches":len(exact_map)-len(mismatch),"raw_to_normalized_attribute_matches":attr_matches,
   "missing_from_broad":len(missing),"value_mismatches":mismatch,
   "quarterly_periods_contiguous":contiguous,"exact_csv_sha256":sha(PANEL/f"{country}_{entry}_P_F_USD_Q.csv")}
  checks.append(row)
  if missing or mismatch or len(exact_obs)!=len(broad_map) or not contiguous or (periods and periods[0]!=expected_min):all_ok=False
normalized_sha=sha(PANEL/"portfolio_flows_panel.csv")
result={"scope":"independent raw-to-normalized and exact-query-to-broad-raw reconciliation",
 "normalized_panel_sha256":normalized_sha,"panel_rows":len(panel),"unique_keys":len(seen),"duplicate_key_count":len(dups),
 "series_checks":checks,"series_count":len(checks),
 "exact_to_broad_value_matches":sum(x["exact_broad_value_matches"] for x in checks),
 "missing_or_mismatched_values":sum(x["missing_from_broad"]+len(x["value_mismatches"]) for x in checks),
 "raw_to_normalized_attribute_mismatch_count":len(attribute_mismatches),"raw_to_normalized_attribute_mismatches":attribute_mismatches[:50],
 "all_series_quarters_contiguous":all(x["quarterly_periods_contiguous"] for x in checks),
 "status":"PASS" if all_ok and not dups else "FAIL",
 "limitations":["Pilot only: Brazil and India, not an emerging-market aggregate.",
 "SCALE and all source attributes preserved; no rescaling or currency conversion.",
 "No aggregation, position/flow substitution, or investment/trading signal inferred."]}
(OUT/"validation.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"
",encoding="utf-8")
print(json.dumps(result,indent=2,ensure_ascii=False))
if result["status"]!="PASS" or attribute_mismatches:raise SystemExit("Independent BOP panel reconciliation failed")
