#!/usr/bin/env python3
"""Inventory macro/geo/sector source coverage and run generic quality checks."""
from pathlib import Path
import json
import pandas as pd

ROOT=Path("."); OUT=Path("outputs/macro_geo"); REPORT=OUT/"source_coverage.json"
SOURCES={
"nse_daily_equity":{"paths":["data/processed/nse_eq_200_sessions.csv"],"required":["DATE","SYMBOL","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"]},
"sector_indices":{"paths":["data/external/sector_indices.csv","data/context/sector_indices.csv"],"required":["DATE","SERIES","CLOSE"]},
"benchmark_index":{"paths":["data/external/benchmark_indices.csv","data/context/benchmark_indices.csv"],"required":["DATE","SERIES","CLOSE"]},
"crude_oil":{"paths":["data/external/brent_crude.csv","data/context/brent_crude.csv"],"required":["DATE","CLOSE"]},
"usd_inr":{"paths":["data/external/usd_inr.csv","data/context/usd_inr.csv"],"required":["DATE","CLOSE"]},
"us_yields":{"paths":["data/external/us_yields.csv","data/context/us_yields.csv"],"required":["DATE","SERIES","CLOSE","SOURCE","SOURCE_SERIES","SOURCE_URL","OBSERVED_AT_UTC"]},
"us_real_yields":{"paths":["data/external/us_real_yields.csv"],"required":["DATE","SERIES","CLOSE"]},
"dxy":{"paths":["data/external/dxy.csv","data/context/dxy.csv"],"required":["DATE","CLOSE","SOURCE","SOURCE_SERIES","SOURCE_URL","OBSERVED_AT_UTC"]},
"volatility":{"paths":["data/external/volatility.csv","data/context/volatility.csv"],"required":["DATE","SERIES","CLOSE"]},
"fpi_dii_flows":{"paths":["data/external/fpi_dii_flows.csv","data/context/fii_dii.csv"],"required":["DATE","GROUP","NET_VALUE"]},
"india_bond_yields":{"paths":["data/external/india_bond_yields.csv","data/context/india_bond_yields.csv"],"required":["DATE","YIELD_10Y","SOURCE","SOURCE_SERIES","SOURCE_URL","OBSERVED_AT_UTC"]},
"rbi_policy_liquidity":{"paths":["data/external/rbi_policy_liquidity.csv"],"required":["DATE","REPO_RATE","POLICY_SURPRISE"]},
"macro_indicators":{"paths":["data/external/macro_indicators.csv"],"required":["DATE","INDICATOR","VALUE","RELEASED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"]},
"fed_policy_surprises":{"paths":["data/external/fed_policy_surprises.csv"],"required":["DATE","ANNOUNCEMENT_AT","EXPECTED_RATE","ACTUAL_RATE","SURPRISE_BPS","SOURCE_URL","SOURCE","OBSERVED_AT_UTC"]},
"india_current_account":{"paths":["data/external/india_current_account.csv"],"required":["DATE","RELEASED_AT","CURRENT_ACCOUNT_USD","GDP_PCT","SOURCE_URL"]},
"valuation_snapshot":{"paths":["data/external/valuation_snapshot.csv"],"required":["DATE","SYMBOL","PE_TTM","PB","EV_EBITDA","MARKET_CAP","EPS_TTM"]},
"china_indicators":{"paths":["data/external/china_indicators.csv"],"required":["DATE","INDICATOR","VALUE","RELEASED_AT","SOURCE_URL","SOURCE","OBSERVED_AT_UTC"]},
"government_capex":{"paths":["data/external/government_capex.csv"],"required":["DATE","DEPARTMENT","ACTUAL_SPEND","BUDGET_SPEND","RELEASED_AT","SOURCE_URL","SOURCE","OBSERVED_AT_UTC"]},
"inflation_components":{"paths":["data/external/inflation_components.csv"],"required":["DATE","COUNTRY","COMPONENT","VALUE","RELEASED_AT","SOURCE_URL","SOURCE","OBSERVED_AT_UTC"]},
"sector_catalysts":{"paths":["data/external/sector_catalysts.csv"],"required":["DATE","SECTOR","SYMBOL","CATALYST_TYPE","PUBLISHED_AT","SOURCE_URL"]},
"domestic_policy_events":{"paths":["data/external/domestic_policy_events.csv"],"required":["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","AFFECTED_SECTOR","SOURCE_URL"]},
"shipping_route_risk":{"paths":["data/external/shipping_route_risk.csv"],"required":["DATE","ROUTE","STATUS","SOURCE_URL"]},
"earnings_revisions":{"paths":["data/external/earnings_revisions.csv"],"required":["DATE","SYMBOL","REVISION","PUBLISHED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"]},
"corporate_events":{"paths":["data/external/corporate_events.csv"],"required":["DATE","SYMBOL","EVENT_TYPE","PUBLISHED_AT","SOURCE_URL"]},
"geopolitical_events":{"paths":["data/external/geopolitical_events.csv"],"required":["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","SOURCE","SOURCE_URL","CONFIDENCE"]},
"sector_fundamentals":{"paths":["data/external/sector_fundamentals.csv"],"required":["DATE","SECTOR","METRIC","VALUE","RELEASED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"]},
"global_commodity_prices":{"paths":["data/external/commodity_prices.csv"],"required":["DATE","COMMODITY","CLOSE","SOURCE","SOURCE_SERIES","SOURCE_URL","OBSERVED_AT_UTC"]},
"market_microstructure":{"paths":["data/external/market_microstructure.csv"],"required":["DATE","SYMBOL","CIRCUIT_STATUS","SURVEILLANCE_STATUS","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"]},
"fx_carry_and_cross_currency":{"paths":["data/external/fx_carry.csv"],"required":["DATE","PAIR","VALUE","SOURCE","SOURCE_SERIES","SOURCE_URL","OBSERVED_AT_UTC"]},
"weather_agriculture":{"paths":["data/external/weather_agriculture.csv"],"required":["DATE","REGION","INDICATOR","VALUE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"]},
"global_freight_shipping":{"paths":["data/external/freight_shipping.csv"],"required":["DATE","INDICATOR","VALUE","SOURCE","SOURCE_SERIES","SOURCE_URL","OBSERVED_AT_UTC"]},
"global_policy_events":{"paths":["data/external/global_policy_events.csv"],"required":["EVENT_DATE","PUBLISHED_AT","COUNTRY","EVENT_TYPE","SOURCE_URL","SOURCE","TITLE","FEED_URL","EVENT_DATE_BASIS","OBSERVED_AT_UTC"]},
"ipo_float_unlocks":{"paths":["data/external/ipo_float_unlocks.csv"],"required":["DATE","SYMBOL","EFFECTIVE_FLOAT","EVENT_TYPE","PUBLISHED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"]},
"research_house_actions":{"paths":["data/external/research_house_actions.csv"],"required":["PUBLISHED_AT","SYMBOL","HOUSE","ACTION","SOURCE_URL","SOURCE","OBSERVED_AT_UTC"]},
}
def macro_series_freshness(source_date, reference_date, max_age_days=3):
    """Return freshness against an observed market-session date, never wall-clock time."""
    source = pd.Timestamp(source_date).normalize()
    reference = pd.Timestamp(reference_date).normalize()
    age = int((reference - source).days)
    return {"data_age_days": age, "freshness_status": "FRESH" if 0 <= age <= max_age_days else "STALE_OR_FUTURE"}


def apply_factor_collector_report(rows, collector_report):
    """Keep collected-but-unvalidated factor files out of clean AVAILABLE status."""
    groups = collector_report.get("groups", {}) if isinstance(collector_report, dict) else {}
    row_by_name = {row.get("source"): row for row in rows}
    for name in ("us_yields", "global_commodity_prices", "global_policy_events", "dxy"):
        observed = groups.get(name, {})
        state = observed.get("status")
        row = row_by_name.get(name)
        if not row:
            continue
        if not state:
            state = "UNKNOWN_NO_COLLECTOR_EVIDENCE"
        if state != "COLLECTED_AND_DOMAIN_QA_PASSED":
            if int(row.get("rows") or 0) > 0:
                # Do not downgrade a more specific schema/read failure to a generic warning.
                if row.get("status") == "AVAILABLE":
                    row["status"] = "DATA_QUALITY_WARN"
                note = f"Factor collector status={state}; domain/source QA not cleared."
                existing = str(row.get("notes") or "")
                row["notes"] = (existing + " " + note).strip()
    return rows


def apply_crude_oil_collector_report(rows, collector_report):
    """Require explicit Brent domain QA; a Yahoo futures proxy never silently equals FRED spot."""
    row = next((item for item in rows if item.get("source") == "crude_oil"), None)
    if row is None:
        return rows
    report = collector_report if isinstance(collector_report, dict) else {}
    state = report.get("status") or "UNKNOWN_NO_COLLECTOR_EVIDENCE"
    proxy_only = report.get("proxy_only") is True
    if state != "COLLECTED_AND_DOMAIN_QA_PASSED":
        if int(row.get("rows") or 0) > 0 and row.get("status") == "AVAILABLE":
            row["status"] = "DATA_QUALITY_WARN"
        row["notes"] = (str(row.get("notes") or "") +
            f" Brent collector status={state}; domain QA not cleared.").strip()
    elif proxy_only:
        # Bounded proxy QA establishes usability only, not source equivalence.
        if int(row.get("rows") or 0) > 0:
            row["status"] = "DATA_QUALITY_WARN"
        row["notes"] = (str(row.get("notes") or "") +
            " Yahoo BZ=F is a futures proxy, not FRED DCOILBRENTEU spot; P0 remains blocked pending explicit secondary-source contract approval.").strip()
    return rows


def main():
    OUT.mkdir(parents=True,exist_ok=True); rows=[]
    now=pd.Timestamp.now(tz="UTC")
    for name,spec in SOURCES.items():
        path=next((ROOT/p for p in spec["paths"] if (ROOT/p).exists()),None)
        row={"source":name,"candidate_paths":";".join(spec["paths"]),"status":"NOT_CONNECTED","selected_path":"",
             "rows":0,"missing_columns":spec["required"],"date_min":None,"date_max":None,"age_days":None,
             "missing_cell_pct":None,"duplicate_key_rows":None,"invalid_date_rows":None,"invalid_timestamp_rows":None,
             "notes":"No source file found; absence is UNKNOWN, not NEGATIVE."}
        if path:
            row["selected_path"]=str(path)
            try:
                df=pd.read_csv(path); df.columns=[str(c).strip().upper() for c in df.columns]
                missing=sorted(set(spec["required"])-set(df.columns))
                row.update(rows=int(len(df)),missing_columns=missing,
                           missing_cell_pct=round(float(df.isna().sum().sum()/max(1,df.shape[0]*df.shape[1])*100),4),
                           invalid_date_rows=0,invalid_timestamp_rows=0,duplicate_key_rows=0)
                dcol=next((c for c in ["DATE","EVENT_DATE"] if c in df.columns),None)
                if dcol and len(df):
                    parsed=pd.to_datetime(df[dcol],errors="coerce")
                    row["invalid_date_rows"]=int(parsed.isna().sum())
                    valid=parsed.dropna()
                    if len(valid):
                        latest=valid.max()
                        row.update(date_min=str(valid.min().date()),date_max=str(latest.date()),age_days=max(0,int((now.tz_localize(None)-latest).days)))
                # Corporate filings legitimately allow multiple event types per symbol/day.
                # Deduplicate by the filing identity, not DATE+SYMBOL alone.
                if name == "corporate_events" and {"DATE","SYMBOL","EVENT_TYPE","SOURCE_URL"}.issubset(df.columns):
                    key=["DATE","SYMBOL","EVENT_TYPE","SOURCE_URL"]
                else:
                    key=next((k for k in [["DATE","SYMBOL"],["DATE","SERIES"],["DATE","COMMODITY"],["DATE","INDICATOR"],["EVENT_ID"],["EVENT_DATE","EVENT_TYPE","SOURCE_URL"]] if set(k).issubset(df.columns)),None)
                if key: row["duplicate_key_rows"]=int(df.duplicated(key).sum())
                if "PUBLISHED_AT" in df.columns:
                    ts=pd.to_datetime(df["PUBLISHED_AT"],errors="coerce",utc=True)
                    row["invalid_timestamp_rows"]=int(ts.isna().sum())
                quality_issues=[]
                if df.empty: quality_issues.append("source file exists but contains zero data rows")
                if missing: quality_issues.append("missing required columns")
                if row["duplicate_key_rows"] not in (None,0): quality_issues.append("duplicate keys")
                if row["invalid_date_rows"] not in (None,0): quality_issues.append("invalid dates")
                if row["invalid_timestamp_rows"] not in (None,0): quality_issues.append("invalid publication timestamps")
                if row["missing_cell_pct"] is not None and row["missing_cell_pct"]>5: quality_issues.append("more than 5% missing cells")
                status="SCHEMA_FAIL" if missing else ("DATA_QUALITY_WARN" if quality_issues else "AVAILABLE")
                row.update(status=status,notes="; ".join(quality_issues) if quality_issues else "Generic QA passed; units, source authenticity, revisions, market-calendar alignment and point-in-time leakage still need domain-specific checks.")
            except Exception as e: row.update(status="READ_ERROR",notes=f"Could not read file: {type(e).__name__}: {e}")
        rows.append(row)
    # Brent has its own collector report and stricter source-equivalence boundary.
    crude_report_path = ROOT / "outputs/macro_geo/crude_oil_collection_report.json"
    if crude_report_path.exists():
        try:
            crude_report = json.loads(crude_report_path.read_text())
            rows = apply_crude_oil_collector_report(rows, crude_report)
        except Exception:
            for row in rows:
                if row.get("source") == "crude_oil" and int(row.get("rows") or 0) > 0:
                    row["status"] = "DATA_QUALITY_WARN"
                    row["notes"] = (str(row.get("notes") or "") + " Brent collector report unreadable; source QA UNKNOWN.").strip()
    else:
        for row in rows:
            if row.get("source") == "crude_oil" and int(row.get("rows") or 0) > 0:
                row["status"] = "DATA_QUALITY_WARN"
                row["notes"] = (str(row.get("notes") or "") + " Brent collector report missing; source QA UNKNOWN.").strip()

    # A newly collected factor file is not automatically clean source coverage.
    # Require a separate explicit domain-QA pass before factor audit may count it.
    collector_report_path = OUT / "factor_source_collection_report.json"
    if collector_report_path.exists():
        try:
            collector_report = json.loads(collector_report_path.read_text())
            rows = apply_factor_collector_report(rows, collector_report)
        except Exception:
            # Unreadable collector evidence cannot upgrade a source to AVAILABLE.
            for row in rows:
                if row.get("source") in ("us_yields", "global_commodity_prices") and int(row.get("rows") or 0) > 0:
                    row["status"] = "DATA_QUALITY_WARN"
                    row["notes"] = (str(row.get("notes") or "") + " Factor collector report unreadable; source QA UNKNOWN.").strip()
    frame=pd.DataFrame(rows)
    # Explicitly distinguish the P0 decision-support backbone from the wider
    # optional context inventory. A file's presence is not proof of officialness.
    by_name={r["source"]:r for r in rows}
    p0_required=["benchmark_index","sector_indices","volatility","crude_oil","usd_inr","fpi_dii_flows","corporate_events","geopolitical_events"]
    p0_rows={name:{"status":by_name.get(name,{}).get("status","NOT_CONNECTED"),
                   "rows":by_name.get(name,{}).get("rows",0),
                   "selected_path":by_name.get(name,{}).get("selected_path","")} for name in p0_required}
    # Domain-specific P0 evidence gates: a two-row flow snapshot is not
    # historical coverage. Compare macro-series freshness with the latest
    # observed market session, not wall-clock "today" (weekends/holidays and
    # source publication lags must not create false stale-data failures).
    reference_date = None
    for candidate in (ROOT/"data/external/market_panel.csv", ROOT/"data/processed/nse_eq_200_sessions.csv"):
        if candidate.exists():
            try:
                ref_df = pd.read_csv(candidate, usecols=lambda c: str(c).strip().upper()=="DATE")
                ref_dates = pd.to_datetime(ref_df.iloc[:, 0], errors="coerce").dropna() if not ref_df.empty else pd.Series(dtype="datetime64[ns]")
                if not ref_dates.empty:
                    reference_date = ref_dates.max().tz_localize(None).normalize() if ref_dates.max().tzinfo else ref_dates.max().normalize()
                    break
            except Exception:
                pass
    for name in ("crude_oil","usd_inr"):
        info=p0_rows.get(name,{})
        src=next((r for r in rows if r["source"]==name),{})
        if src.get("date_max"):
            try:
                source_date = pd.Timestamp(src["date_max"]).normalize()
                reference = reference_date if reference_date is not None else now.tz_localize(None).normalize()
                freshness = macro_series_freshness(source_date, reference, max_age_days=3)
                info["freshness_reference_date"]=reference.date().isoformat()
                info.update(freshness)
                if info["freshness_status"]!="FRESH": info["status"]="DATA_QUALITY_WARN"
            except Exception:
                info["freshness_status"]="UNKNOWN"; info["status"]="DATA_QUALITY_WARN"
    # A repair-layer secondary source may override a generic/proxy warning only
    # when its own explicit provenance, value, window, duplicate and freshness
    # contract passed. This is especially important when the collector's Yahoo
    # Brent proxy is replaced by the EIA official Brent spot series.
    repair_path=OUT/"p0_repair_report.json"
    if repair_path.exists():
        try:
            repair=json.loads(repair_path.read_text(encoding="utf-8"))
            for name in ("crude_oil","usd_inr"):
                evidence=repair.get("groups",{}).get(name,{})
                checks=set(evidence.get("domain_qa_checks",[]))
                required_checks={"source identity","valid positive values","unique date keys",
                                 "requested-window bounds","freshness <= 3 calendar days",
                                 "source URL provenance"}
                source=str(evidence.get("source",""))
                approved_source=(name=="crude_oil" and "EIA" in source and "Brent spot" in source) or (
                    name=="usd_inr" and "USD/FBIL reference rates" in source
                    or name=="usd_inr" and "RBI/FBIL reference rates" in source)
                if (evidence.get("status")=="AVAILABLE_SECONDARY" and int(evidence.get("rows",0) or 0)>0
                    and required_checks.issubset(checks) and evidence.get("freshness_status")=="FRESH"
                    and evidence.get("url") and approved_source):
                    p0_rows[name].update(status="AVAILABLE_SECONDARY",rows=int(evidence["rows"]),
                        selected_path=evidence.get("path",""),date_max=evidence.get("date_max"),
                        domain_qa_checks=sorted(checks),freshness_status="FRESH",
                        freshness_age_calendar_days=evidence.get("freshness_age_calendar_days"),
                        source=evidence.get("source"),source_url=evidence.get("url"),
                        notes="Secondary source accepted only under explicit domain-QA contract; source identity remains labelled.")
        except Exception:
            # Malformed repair evidence must not promote any P0 group.
            pass
    flow_path=ROOT/"data/external/fpi_dii_flows.csv"
    if flow_path.exists():
        try:
            flows=pd.read_csv(flow_path)
            flows.columns=[str(c).strip().upper() for c in flows.columns]
            # NSDL collector emits ISO YYYY-MM-DD. Parse ISO strictly first; dayfirst=True
            # silently reinterprets dates such as 2026-06-01 as 6 January.
            dates=pd.to_datetime(flows["DATE"],format="%Y-%m-%d",errors="coerce") if "DATE" in flows else pd.Series(dtype="datetime64[ns]")
            if "DATE" in flows and dates.isna().any():
                fallback_dates=pd.to_datetime(flows.loc[dates.isna(),"DATE"],errors="coerce",dayfirst=True)
                dates.loc[dates.isna()]=fallback_dates
            flow_info=p0_rows.get("fpi_dii_flows",{})
            flow_info["unique_dates"]=int(dates.dt.date.nunique())
            flow_info["date_span_days"]=int((dates.max()-dates.min()).days) if len(dates.dropna())>1 else 0
            group_coverage={}
            if {"GROUP","DATE"}.issubset(flows.columns):
                for group, subset in flows.assign(_PARSED_DATE=dates).groupby(flows["GROUP"].astype(str).str.upper()):
                    gd=subset["_PARSED_DATE"].dropna()
                    group_coverage[group]={"rows":int(len(subset)),"unique_dates":int(gd.dt.date.nunique()),
                        "date_span_days":int((gd.max()-gd.min()).days) if len(gd)>1 else 0}
            flow_info["group_coverage"]=group_coverage
            if (flow_info["unique_dates"] < 60 or flow_info["date_span_days"] < 90 or
                not group_coverage or any(v["unique_dates"] < 60 or v["date_span_days"] < 90 for v in group_coverage.values())):
                flow_info["status"]="INSUFFICIENT_HISTORICAL_COVERAGE"
                # Do not let generic schema QA or Factor Registry mistake a
                # one-day NSE FPI/DII snapshot for historical source coverage.
                for source_row in rows:
                    if source_row.get("source") == "fpi_dii_flows":
                        source_row["status"] = "DATA_QUALITY_WARN"
                        source_row["notes"] = (
                            str(source_row.get("notes") or "") +
                            " Historical coverage gate failed: requires >=60 distinct dates spanning >=90 calendar days for each investor group."
                        ).strip()
        except Exception:
            p0_rows["fpi_dii_flows"]["status"]="DATA_QUALITY_WARN"
    # Refresh available groups only after the strict per-group rules above.
    p0_available=[name for name,info in p0_rows.items() if info["status"] in ("AVAILABLE","AVAILABLE_SECONDARY") and info["rows"]>0]
    report={"status":"INVENTORY_COMPLETE_WITH_GAPS" if (frame.status!="AVAILABLE").any() else "SCHEMA_AND_GENERIC_QA_AVAILABLE",
            "as_of_utc":now.isoformat(),"sources_total":len(rows),"available":int((frame.status=="AVAILABLE").sum()),
            "not_connected":int((frame.status=="NOT_CONNECTED").sum()),"schema_fail":int((frame.status=="SCHEMA_FAIL").sum()),
            "quality_warn":int((frame.status=="DATA_QUALITY_WARN").sum()),"read_error":int((frame.status=="READ_ERROR").sum()),
            "p0_coverage":{"required_groups":p0_required,"available_groups":p0_available,
                "available_count":len(p0_available),"required_count":len(p0_required),
                "status":"P0_COMPLETE" if len(p0_available)==len(p0_required) else "P0_INCOMPLETE",
                "groups":p0_rows,
                "boundary":"AVAILABLE means file/schema/generic QA only; secondary-source provenance and point-in-time validity remain separately qualified."},
            "important_boundary":"This is a source inventory and generic QA only. It does not imply live-feed connectivity, verified units, causal validity or complete 20-year history. Missing data remains UNKNOWN.",
            "sources":rows}
    REPORT.write_text(json.dumps(report,indent=2)); frame.to_csv(OUT/"source_coverage.csv",index=False)
    print(json.dumps({k:report[k] for k in ["status","sources_total","available","not_connected","schema_fail","quality_warn","read_error"]}))
if __name__=="__main__": main()
