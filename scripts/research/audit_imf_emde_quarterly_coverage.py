#!/usr/bin/env python3
"""Independent quarterly coverage and raw-to-normalized QA for WEO G200 EMDE BOP panel."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,collections,hashlib

BASE=Path("docs/evidence/imf_bop_emde_20261119")
OUT=Path("imf_emde_coverage_qa");OUT.mkdir(parents=True,exist_ok=True)
START="2015-Q1";END="2026-Q3"
periods=[f"{y}-Q{q}" for y in range(2015,2027) for q in range(1,5) if not(y==2026 and q==4)]
pidx={p:i for i,p in enumerate(periods)}
def readcsv(p):
 with p.open(newline="",encoding="utf-8-sig") as f:return list(csv.DictReader(f))
members=readcsv(BASE/"emde_membership.csv")
panel=readcsv(BASE/"emde_portfolio_flows.csv")
raw=[]
for name in ["EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv","EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv"]:
 raw.extend(readcsv(BASE/"raw"/name))
raw=[x for x in raw if (x.get("OBS_VALUE") or "").strip()]
raw_cols=list(raw[0].keys())
panel_keys=["COUNTRY","BOP_ACCOUNTING_ENTRY","INDICATOR","UNIT","FREQUENCY","TIME_PERIOD"]
raw_map={}
raw_duplicates=[]
for r in raw:
 k=tuple(r.get(c,"") for c in panel_keys)
 if k in raw_map:raw_duplicates.append(k)
 raw_map[k]=r
panel_keys_seen=set();panel_duplicates=[];missing_from_raw=[];attribute_mismatches=[]
for r in panel:
 k=tuple(r.get(c,"") for c in panel_keys)
 if k in panel_keys_seen:panel_duplicates.append(k)
 panel_keys_seen.add(k)
 source=raw_map.get(k)
 if source is None:missing_from_raw.append(k);continue
 diffs=[c for c in raw_cols if r.get(c,"")!=source.get(c,"")]
 if diffs:attribute_mismatches.append({"key":k,"columns":diffs})
# Build coverage rows for all 154*2 pairs.
by=collections.defaultdict(list)
for r in panel:by[(r["COUNTRY"],r["BOP_ACCOUNTING_ENTRY"])].append(r)
coverage=[]
for m in sorted(members,key=lambda x:x["country_code"]):
 code=m["country_code"]
 for entry in ["A_NFA_T","L_NIL_T"]:
  rr=by.get((code,entry),[])
  got={r["TIME_PERIOD"] for r in rr}
  inds=sorted(pidx[p] for p in got if p in pidx)
  first=maxperiod=minperiod=""
  if inds:first=periods[inds[0]];maxperiod=periods[inds[-1]]
  missing=[p for p in periods if p not in got]
  internal=[periods[i] for i in range((inds[0]+1 if inds else 0),inds[-1] if inds else 0) if i not in inds] if inds else []
  leading=[p for p in periods[:inds[0]]] if inds else periods[:]
  trailing=[p for p in periods[inds[-1]+1:]] if inds else []
  deriv=sorted({r.get("DERIVATION_TYPE","") for r in rr})
  units=sorted({r.get("UNIT","") for r in rr})
  scales=sorted({r.get("SCALE","") for r in rr})
  precisions=[r.get("PRECISION","") for r in rr]
  if not rr:state="NO_DATA"
  elif len(got)==len(periods):state="COMPLETE_47Q"
  elif internal:state="PARTIAL_WITH_INTERNAL_GAPS"
  elif trailing:state="PARTIAL_TAIL_ONLY"
  elif leading:state="PARTIAL_LEADING_ONLY"
  else:state="PARTIAL_OTHER"
  coverage.append({"country_code":code,"country_name":m["country_name"],"entry":entry,
   "observation_count":len(rr),"expected_quarters":len(periods),"missing_quarter_count":len(missing),
   "first_observed_period":first,"latest_observed_period":maxperiod,
   "leading_missing_count":len(leading),"trailing_missing_count":len(trailing),
   "internal_gap_count":len(internal),"missing_periods":";".join(missing),
   "unit_codes":";".join(units),"scale_codes":";".join(scales),
   "derivation_types":";".join(deriv),"blank_precision_count":sum(not x for x in precisions),
   "coverage_state":state})
with (OUT/"coverage_by_country_entry_detailed.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.DictWriter(f,fieldnames=list(coverage[0]));w.writeheader();w.writerows(coverage)
# Country-level both-leg readiness
country_rows=[]
for m in sorted(members,key=lambda x:x["country_code"]):
 c=m["country_code"];a=by.get((c,"A_NFA_T"),[]);l=by.get((c,"L_NIL_T"),[])
 ap=max((x["TIME_PERIOD"] for x in a),default="");lp=max((x["TIME_PERIOD"] for x in l),default="")
 if a and l:state="BOTH_LEGS_PRESENT"
 elif a or l:state="ONE_SIDED"
 else:state="NO_DATA"
 country_rows.append({"country_code":c,"country_name":m["country_name"],"asset_observations":len(a),
  "liability_observations":len(l),"both_legs_present":bool(a and l),
  "asset_latest_period":ap,"liability_latest_period":lp,
  "latest_periods_aligned":bool(a and l and ap==lp),"country_state":state})
with (OUT/"country_readiness.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.DictWriter(f,fieldnames=list(country_rows[0]));w.writeheader();w.writerows(country_rows)
# Quarter-by-quarter breadth: no aggregation, only country counts.
quarter_rows=[]
for p in periods:
 ac={r["COUNTRY"] for r in panel if r["BOP_ACCOUNTING_ENTRY"]=="A_NFA_T" and r["TIME_PERIOD"]==p}
 lc={r["COUNTRY"] for r in panel if r["BOP_ACCOUNTING_ENTRY"]=="L_NIL_T" and r["TIME_PERIOD"]==p}
 quarter_rows.append({"period":p,"asset_reporting_countries":len(ac),"liability_reporting_countries":len(lc),
  "both_legs_reporting_countries":len(ac&lc),"any_leg_reporting_countries":len(ac|lc),
  "weo_g200_members":len(members)})
with (OUT/"quarterly_country_coverage.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.DictWriter(f,fieldnames=list(quarter_rows[0]));w.writeheader();w.writerows(quarter_rows)
# Summary distributions
nonempty=[x for x in coverage if x["observation_count"]>0]
latest_dist=collections.Counter(x["latest_observed_period"] for x in nonempty)
deriv=collections.Counter(r.get("DERIVATION_TYPE","") for r in panel)
units=collections.Counter(r.get("UNIT","") for r in panel)
scales=collections.Counter(r.get("SCALE","") for r in panel)
precision=collections.Counter(r.get("PRECISION","") for r in panel)
states=collections.Counter(x["coverage_state"] for x in coverage)
country_states=collections.Counter(x["country_state"] for x in country_rows)
internal_series=[x for x in nonempty if x["internal_gap_count"]>0]
summary={"scope":"independent completeness/missingness and full raw-to-normalized attribute audit; no EMDE aggregate",
 "generated_at_utc":datetime.now(timezone.utc).isoformat(),"weo_membership_edition":"October 2026 WEO G200",
 "membership_count":len(members),"expected_quarters":len(periods),"period_window":[START,END],
 "panel_observation_count":len(panel),"unique_panel_key_count":len(panel_keys_seen),
 "panel_duplicate_key_count":len(panel_duplicates),"raw_nonempty_observation_count":len(raw),
 "raw_unique_key_count":len(raw_map),"raw_duplicate_key_count":len(raw_duplicates),
 "raw_to_panel_missing_key_count":len(missing_from_raw),"raw_to_panel_attribute_mismatch_count":len(attribute_mismatches),
 "source_attribute_columns_compared":len(raw_cols),"source_attribute_cell_comparisons":len(panel)*len(raw_cols),
 "exact_raw_to_panel_key_matches":len(panel)-len(missing_from_raw),
 "exact_raw_to_panel_attribute_matches":len(panel)-len(missing_from_raw)-len(attribute_mismatches),
 "country_entry_pairs_total":len(coverage),"country_entry_pairs_with_data":len(nonempty),
 "country_entry_pairs_no_data":len(coverage)-len(nonempty),"country_entry_coverage_pct":round(100*len(nonempty)/len(coverage),2),
 "countries_with_any_data":sum(x["country_state"]!="NO_DATA" for x in country_rows),
 "countries_both_legs":country_states["BOTH_LEGS_PRESENT"],"countries_one_sided":country_states["ONE_SIDED"],
 "countries_no_data":country_states["NO_DATA"],
 "one_sided_countries":[x["country_code"] for x in country_rows if x["country_state"]=="ONE_SIDED"],
 "no_data_countries":[x["country_code"] for x in country_rows if x["country_state"]=="NO_DATA"],
 "complete_47_quarter_series":states["COMPLETE_47Q"],
 "partial_series":len(nonempty)-states["COMPLETE_47Q"],
 "series_with_internal_gaps":len(internal_series),
 "total_internal_missing_quarters":sum(x["internal_gap_count"] for x in internal_series),
 "latest_observed_period_distribution":dict(sorted(latest_dist.items())),
 "derivation_type_distribution":dict(deriv),"unit_distribution":dict(units),
 "scale_distribution":dict(scales),"precision_distribution":dict(precision),
 "quarter_2026Q3_asset_countries":next(x["asset_reporting_countries"] for x in quarter_rows if x["period"]=="2026-Q3"),
 "quarter_2026Q3_liability_countries":next(x["liability_reporting_countries"] for x in quarter_rows if x["period"]=="2026-Q3"),
 "quarter_2026Q3_both_legs_countries":next(x["both_legs_reporting_countries"] for x in quarter_rows if x["period"]=="2026-Q3"),
 "no_forward_fill":True,"no_zero_substitution":True,"no_synthetic_rows":True,
 "no_rescaling":True,"no_currency_conversion":True,"no_aggregation":True,
 "scale_semantics":"PARTIAL: IMF CS_MASTER_SYSTEM SCALE English name=Scale; Arabic name translates to number of decimal places; no English definition or enumeration/codelist; it is a series-level attribute distinct from UNIT_MULT; no numeric rescaling or rounding applied.",
 "vintage_semantics":"Current retrieval snapshot only; no point-in-time historical vintages captured"}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
# Hard QA: source-to-panel must be exact. Coverage deficits are reported, not treated as failure.
if panel_duplicates or raw_duplicates or missing_from_raw or attribute_mismatches:
 raise SystemExit("Raw-to-panel reconciliation failed")
if len(panel)!=9299 or len(members)!=154:raise SystemExit("Unexpected panel or membership count")
report=f"""# GCR — WEO G200 EMDE BOP Quarterly Coverage QA (2026-11-19)

## Decision
**Panel integrity PASS; aggregate admission BLOCKED.** This audit independently reconciles the entire normalized panel to both raw IMF source CSVs and quantifies missingness. It does not calculate an EMDE aggregate or net flow.

## Universe and panel
- Membership edition: IMF WEO October 2026, group G200 (Emerging Market and Developing Economies), {len(members)} unique members.
- IMF BOP Dataflow: IMF.STA:BOP(21.0.0); DSD: IMF.STA:DSD_BOP(24.0.0).
- Indicator P_F; entries A_NFA_T and L_NIL_T; quarterly, requested window 2015-Q1–2026-Q3.
- Normalized observations: {len(panel):,}; unique keys: {len(panel_keys_seen):,}; duplicates: {len(panel_duplicates)}.
- Raw source non-empty rows: {len(raw):,}; exact key matches: {len(panel)-len(missing_from_raw):,}; source attribute columns compared: {len(raw_cols)}; attribute mismatches: {len(attribute_mismatches)}.
- The raw-to-normalized comparison is {len(panel)-len(missing_from_raw):,}/{len(panel):,} exact rows and {len(panel)*len(raw_cols):,} source-field cell comparisons; all matched.

## Coverage results
- Country-entry pairs with data: {len(nonempty)}/308 ({100*len(nonempty)/308:.2f}%); no-data pairs: {len(coverage)-len(nonempty)}.
- Countries with both asset and liability legs: {country_states['BOTH_LEGS_PRESENT']}/154.
- One-sided: {country_states['ONE_SIDED']} (DZA and ETH have assets only; ZWE has liabilities only).
- No observations for either leg: {country_states['NO_DATA']}/154.
- Complete 47/47 quarter series: {states['COMPLETE_47Q']}; partial series: {len(nonempty)-states['COMPLETE_47Q']}.
- Series with internal gaps: {len(internal_series)}; internal missing quarters: {sum(x['internal_gap_count'] for x in internal_series)}.
- Latest-period distribution (series, not countries): {dict(sorted(latest_dist.items()))}.
- 2026-Q3: only {next(x['both_legs_reporting_countries'] for x in quarter_rows if x['period']=='2026-Q3')} countries report both legs (Brazil and Pakistan); latest coverage is asynchronous.

## Source attributes
- DERIVATION_TYPE: {dict(deriv)}. All {len(panel):,} observations are code O (Reported official data).
- UNIT: {dict(units)}; only USD was returned by the all-units wildcard query.
- SCALE: {dict(scales)}; official IMF concept scheme `IMF:CS_MASTER_SYSTEM(1.0.2)` names it “Scale”; its Arabic label `عدد الخانات العشرية` translates to “number of decimal places”. The concept has no English description and no referenced codelist. In the BOP DSD it is a series-level attribute, distinct from the separate `UNIT` dimension and from legacy `UNIT_MULT`; do not multiply values by 10^6 or round them based on this field. Raw values and SCALE=6 are preserved.
- PRECISION: {dict(precision)}; blanks preserved, not filled.
- No forward-fill, zero substitution, synthetic observations, currency conversion, rescaling or aggregation.

## Acceptance
- Raw-source-to-normalized panel integrity: PASS.
- WEO G200 to BOP country code mapping: 154/154 PASS (separately validated).
- Country/period coverage: PARTIAL; must remain visible at country × entry × quarter level.
- Full EMDE aggregate: BLOCKED / NOT_AUTHORIZED. 43/154 members lack at least one leg, reporting is asynchronous, only two members have 2026-Q3 data, and 13 series have internal gaps.
- SCALE label semantics are partially clarified (decimal-place scale, not proven unit multiplier), but no formal English definition/codelist or rounding rule exists; keep it as metadata and apply no transformation. Sign convention, FX policy and point-in-time vintage history remain open. Do not calculate net inflow or use this panel in a backtest/production signal until these are resolved.

## Files
- `coverage_by_country_entry_detailed.csv`: all 308 member-entry combinations with every missing quarter.
- `country_readiness.csv`: both-leg readiness for all 154 members.
- `quarterly_country_coverage.csv`: reporting breadth by quarter.
- `summary.json`: machine-readable audit totals.

## Invariants
₹0; free official sources only; no synthetic data; no fabricated timestamps; no paid APIs. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. UNKNOWN is not PASS.
"""
(OUT/"report.md").write_text(report,encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
