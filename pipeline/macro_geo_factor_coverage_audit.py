#!/usr/bin/env python3
"""Audit factor registry coverage against observed source-coverage outputs; never imply live scoring."""
from pathlib import Path
import json
import pandas as pd

ROOT=Path(".")
REGISTRY=ROOT/"config/macro_factor_registry.csv"
GAPS=ROOT/"config/macro_geo_data_gap_register.csv"
COVERAGE=ROOT/"outputs/macro_geo/source_coverage.json"
OUT=ROOT/"outputs/macro_geo"
MAP={
"F01":["fpi_dii_flows","dxy","us_yields","volatility","fx_carry_and_cross_currency"],
"F02":["crude_oil","global_commodity_prices","global_freight_shipping"],
"F03":["earnings_revisions","corporate_events","valuation_snapshot"],
"F04":["usd_inr","india_bond_yields","macro_indicators","india_current_account","inflation_components"],
"F05":["us_yields","dxy","global_policy_events","fed_policy_surprises"],
"F06":["rbi_policy_liquidity","india_bond_yields","fpi_dii_flows"],
"F07":["macro_indicators","global_policy_events","sector_fundamentals","government_capex"],
"F08":["corporate_events","sector_fundamentals","sector_catalysts"],
"F09":["global_commodity_prices","macro_indicators","global_policy_events","china_indicators"],
"F10":["global_policy_events","corporate_events","market_microstructure","domestic_policy_events"],
"F11":["geopolitical_events","global_policy_events"],
"F12":["global_policy_events","geopolitical_events","global_commodity_prices"],
"F13":["global_freight_shipping","crude_oil","global_commodity_prices","shipping_route_risk"],
"F14":["macro_indicators","us_yields","india_bond_yields","inflation_components"],
"F15":["global_policy_events","fx_carry_and_cross_currency","us_yields"],
"F16":["global_commodity_prices","macro_indicators"],
"F17":["weather_agriculture","macro_indicators"],
"F18":["macro_indicators","sector_fundamentals"],
"F19":["fpi_dii_flows","india_bond_yields","rbi_policy_liquidity","market_microstructure"],
"F20":["global_policy_events","macro_indicators","corporate_events","domestic_policy_events","government_capex"],
"F21":["global_freight_shipping","global_commodity_prices","sector_fundamentals"],
"F22":["sector_fundamentals","corporate_events","global_policy_events"],
"F23":["geopolitical_events","macro_indicators","global_policy_events"],
"F24":["global_commodity_prices","gold_prices_monthly","us_yields","usd_inr"],
"F25":["benchmark_index","sector_indices","volatility","market_microstructure","valuation_snapshot"],
"F26":["corporate_events","market_microstructure"],
"F27":["market_microstructure","nse_daily_equity"],
"F28":["macro_indicators","global_commodity_prices","global_freight_shipping"],
"F29":["fx_carry_and_cross_currency","usd_inr","dxy"],
"F30":["global_policy_events","sector_fundamentals"],
"F31":["corporate_events","global_policy_events","sector_fundamentals"],
"F32":["global_policy_events","corporate_events","global_freight_shipping"],
"F33":["ipo_float_unlocks","market_microstructure"],
"F34":["research_house_actions","earnings_revisions"],
"F35":["volatility","dxy","fx_carry_and_cross_currency","fpi_dii_flows"],
}
def source_is_connected(item):
    """Only a clean, nonempty source-coverage row counts as connected."""
    try:
        return item.get("status") == "AVAILABLE" and int(item.get("rows") or 0) > 0
    except (TypeError, ValueError):
        return False


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    registry=pd.read_csv(REGISTRY).fillna("")
    gaps=pd.read_csv(GAPS).fillna("")
    cov=json.loads(COVERAGE.read_text()) if COVERAGE.exists() else {}
    # Older P0 manifests can store source identifiers as lists (multiple providers).
    # Normalize them safely; never use a list as a dictionary key.
    observed={}
    for item in cov.get("sources",[]):
        if not isinstance(item,dict):
            continue
        source=item.get("source")
        names=source if isinstance(source,list) else [source]
        for name in names:
            if isinstance(name,str) and name.strip():
                observed[name.strip()]=item
        # Reconciliation rows use canonical factor-group names as source identifiers.
        if isinstance(source,str) and source.strip():
            observed[source.strip()]=item
    rows=[]
    for _,f in registry.iterrows():
        fid=str(f["factor_id"]); sources=MAP.get(fid,[])
        source_status=[]
        for name in sources:
            item=observed.get(name,{})
            status=item.get("status","NOT_CONNECTED")
            # A warning is not source availability for hard-gate purposes.
            # Keep the observed warning visible, but never count it as a connected
            # group. Missing or uncertain inputs remain UNKNOWN, not negative.
            if source_is_connected(item):
                source_status.append((name,"AVAILABLE"))
            else:
                source_status.append((name,status))
        available=sum(s=="AVAILABLE" for _,s in source_status)
        if not sources: state="UNMAPPED"
        elif available==len(sources): state="SOURCE_GROUPS_AVAILABLE_SCHEMA_ONLY"
        elif available>0: state="PARTIAL_SOURCE_COVERAGE"
        else: state="NOT_CONNECTED"
        rows.append({"factor_id":fid,"factor":f["factor"],"provisional_priority":f["provisional_priority"],
          "mapped_source_groups":";".join(sources),"source_statuses":";".join(n+":"+s for n,s in source_status),
          "mapped_groups_total":len(sources),"mapped_groups_available":available,"coverage_status":state,
          "evidence_boundary":"Only status AVAILABLE with nonzero rows counts as connected. DATA_QUALITY_WARN, missing provenance, stale data, schema failures and absent files do not count as available; absence remains UNKNOWN, never negative. Even AVAILABLE is schema/generic-QA coverage, not proof of factor effect or live scoring."})
    df=pd.DataFrame(rows)
    df.to_csv(OUT/"factor_coverage_audit.csv",index=False)
    missing=df[df.coverage_status!="SOURCE_GROUPS_AVAILABLE_SCHEMA_ONLY"]
    report={"status":"FACTOR_COVERAGE_AUDITED_WITH_GAPS" if len(missing) else "ALL_MAPPED_SOURCE_GROUPS_SCHEMA_AVAILABLE",
      "factor_groups":len(df),"fully_available_schema_groups":int((df.coverage_status=="SOURCE_GROUPS_AVAILABLE_SCHEMA_ONLY").sum()),
      "partial_source_coverage":int((df.coverage_status=="PARTIAL_SOURCE_COVERAGE").sum()),
      "not_connected":int((df.coverage_status=="NOT_CONNECTED").sum()),"unmapped":int((df.coverage_status=="UNMAPPED").sum()),
      "source_coverage_as_of":cov.get("as_of_utc"),
      "missing_factors":missing[["factor_id","factor","mapped_source_groups","source_statuses","coverage_status"]].to_dict("records"),
      "rule":"Missing source remains UNKNOWN, never negative. This audit does not assign factor states or alter production ranking."}
    (OUT/"factor_coverage_audit.json").write_text(json.dumps(report,indent=2))
    print(json.dumps({k:report[k] for k in ["status","factor_groups","fully_available_schema_groups","partial_source_coverage","not_connected","unmapped"]},indent=2))
if __name__=="__main__": main()
