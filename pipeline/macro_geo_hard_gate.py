#!/usr/bin/env python3
"""Strict audit-branch Macro-Geo hard gate for releasing prospective candidates.

This gate fails closed. It does not modify RANKING_SCORE or +1 PRESSURE_FADE.
Research diagnostics may run, but live prospective picks are withheld unless
P0 source coverage, event-study status, and panel freshness all pass.
"""
from pathlib import Path
import json
import pandas as pd

COVERAGE = Path("outputs/macro_geo/source_coverage.json")
EVENT_REPORT = Path("outputs/macro_geo/event_study_report.json")
EVENT_AUDIT = Path("outputs/macro_geo/event_level_window_audit.json")
PANEL = Path("data/external/market_panel.csv")
EQUITY = Path("data/processed/nse_eq_200_sessions.csv")
MANIFEST = Path("outputs/macro_geo/p0_collection_manifest.json")
REPAIR = Path("outputs/macro_geo/p0_repair_report.json")
FACTOR_COVERAGE = Path("outputs/macro_geo/factor_coverage_audit.json")
REGIME_REPORT = Path("outputs/macro_geo/historical_regime_study_report.json")
NSDL_REPORT = Path("outputs/macro_geo/nsdl_fpi_dii_collection.json")
FACTOR_ROWS = Path("outputs/macro_geo/factor_coverage_audit.csv")
OUT = Path("outputs/macro_geo/hard_gate_report.json")
ALLOWED_EVENT_STATUSES = {"COMPUTED_EXPLORATORY", "COMPUTED_EXPLORATORY_WITH_PENDING_EVENTS"}


def main():
    checks = {}
    blockers = []
    for path in (COVERAGE, EVENT_REPORT, EVENT_AUDIT, PANEL, EQUITY, REPAIR, FACTOR_COVERAGE, REGIME_REPORT):
        if not path.exists():
            blockers.append(f"MISSING_REQUIRED_INPUT:{path}")

    coverage = event = panel = equity = None
    if COVERAGE.exists():
        try:
            coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
            p0 = coverage.get("p0_coverage", {})
            checks["p0_coverage_status"] = p0.get("status", "UNKNOWN")
            checks["p0_available_groups"] = p0.get("available_count", 0)
            checks["p0_required_groups"] = p0.get("required_count", 8)
            missing_groups = [
                name for name, info in p0.get("groups", {}).items()
                if info.get("status") != "AVAILABLE" or int(info.get("rows", 0) or 0) <= 0
            ]
            checks["missing_or_unavailable_p0_groups"] = missing_groups
            if p0.get("status") != "P0_COMPLETE" or missing_groups:
                blockers.append("P0_SOURCE_COVERAGE_INCOMPLETE")
        except Exception as exc:
            blockers.append(f"INVALID_SOURCE_COVERAGE_REPORT:{type(exc).__name__}:{exc}")

    # Collector manifest is written before later repair/NSDL steps. Never ignore its pre-repair critical-gap state.
    if MANIFEST.exists():
        try:
            manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
            old_status = manifest.get("operational_status", manifest.get("status", "UNKNOWN"))
            old_required = manifest.get("p0_coverage", {}).get("required_series_available")
            checks["collector_manifest_pre_repair_status"] = old_status
            checks["collector_manifest_pre_repair_required_series_available"] = old_required
            # The collector manifest is a pre-repair snapshot. Preserve its
            # original state as audit evidence, but do not let a stale pre-repair
            # status override a reconciled final manifest. Release remains blocked
            # by observed final source coverage below if any required group is absent.
            final_reconciliation = manifest.get("final_manifest_reconciliation", {})
            final_p0_meta = manifest.get("p0_coverage", {})
            final_groups = final_p0_meta.get("group_availability_after_repair", {})
            required_names = final_p0_meta.get("required_groups", [])
            final_snapshot_verified = (
                final_reconciliation.get("status") == "RECONCILED"
                and final_p0_meta.get("required_series_available") is True
                and bool(required_names)
                and all(final_groups.get(name) is True for name in required_names)
            )
            checks["collector_manifest_final_snapshot_verified"] = final_snapshot_verified
            if (old_status == "PASS_WITH_CRITICAL_DATA_GAPS" or old_required is False) and not final_snapshot_verified:
                blockers.append("COLLECTION_MANIFEST_REPORTS_CRITICAL_P0_GAPS")
            p0_meta = manifest.get("p0_coverage", {})
            if p0_meta.get("fpi_dii_status") != "AVAILABLE":
                blockers.append("COLLECTION_MANIFEST_FPI_DII_STATUS_UNRESOLVED")
            if p0_meta.get("corporate_events_status") != "AVAILABLE":
                blockers.append("COLLECTION_MANIFEST_CORPORATE_EVENTS_STATUS_UNRESOLVED")
        except Exception as exc:
            blockers.append(f"INVALID_COLLECTION_MANIFEST:{type(exc).__name__}:{exc}")
    else:
        blockers.append(f"MISSING_REQUIRED_INPUT:{MANIFEST}")

    if EVENT_REPORT.exists():
        try:
            event = json.loads(EVENT_REPORT.read_text(encoding="utf-8"))
            status = event.get("research_status", event.get("status", "UNKNOWN"))
            checks["event_study_status"] = status
            # Keep total, panel-eligible and actually computed windows separate:
            # eligibility by date alone is not evidence of a mature return window.
            checks["event_study_total_event_rows"] = int(event.get("event_rows", 0) or 0)
            checks["event_study_eligible_event_rows"] = int(event.get("eligible_event_rows", 0) or 0)
            checks["event_study_window_rows"] = int(event.get("window_rows", 0) or 0)
            if (status not in ALLOWED_EVENT_STATUSES
                    or checks["event_study_eligible_event_rows"] < 1
                    or checks["event_study_window_rows"] < 1):
                blockers.append("EVENT_STUDY_NOT_COMPUTED_WITH_MATURE_WINDOWS")
        except Exception as exc:
            blockers.append(f"INVALID_EVENT_STUDY_REPORT:{type(exc).__name__}:{exc}")

    if EVENT_AUDIT.exists():
        try:
            audit = json.loads(EVENT_AUDIT.read_text(encoding="utf-8"))
            h1 = int(audit.get("unique_events_with_mature_h1", 0) or 0)
            h5 = int(audit.get("unique_events_with_mature_h5", 0) or 0)
            checks["event_level_unique_events_with_mature_h1"] = h1
            checks["event_level_unique_events_with_mature_h5"] = h5
            if h1 < 1:
                blockers.append("EVENT_LEVEL_AUDIT_HAS_NO_MATURE_H1_WINDOWS")
            if h5 < 1:
                blockers.append("EVENT_LEVEL_AUDIT_HAS_NO_MATURE_H5_WINDOWS")
        except Exception as exc:
            blockers.append(f"INVALID_EVENT_LEVEL_AUDIT:{type(exc).__name__}:{exc}")

    if REPAIR.exists():
        try:
            repair = json.loads(REPAIR.read_text(encoding="utf-8"))
            repair_groups = repair.get("groups", {})
            for name in ("fpi_dii_flows", "corporate_events"):
                info = repair_groups.get(name, {})
                rstatus = str(info.get("status", "UNKNOWN"))
                checks[f"repair_{name}_status"] = rstatus
                if rstatus.startswith("BLOCKED") or rstatus in {"UNKNOWN", "INSUFFICIENT_HISTORICAL_COVERAGE"}:
                    blockers.append(f"REPAIR_REPORT_BLOCKS_{name.upper()}")
        except Exception as exc:
            blockers.append(f"INVALID_P0_REPAIR_REPORT:{type(exc).__name__}:{exc}")
    else:
        blockers.append(f"MISSING_REQUIRED_INPUT:{REPAIR}")

    # Cross-report consistency: compare final manifest, official NSDL evidence,
    # repair state, and factor CSV/JSON counts. A green individual report cannot
    # override contradictory provenance or counts in another report.
    if NSDL_REPORT.exists():
        try:
            nsdl = json.loads(NSDL_REPORT.read_text(encoding="utf-8"))
            checks["nsdl_status"] = nsdl.get("status", "UNKNOWN")
            nsdl_groups = nsdl.get("groups", {})
            for group in ("FPI", "DII"):
                item = nsdl_groups.get(group, {})
                dates = int(item.get("unique_dates", 0) or 0)
                span = int(item.get("span_days", 0) or 0)
                checks[f"nsdl_{group.lower()}_unique_dates"] = dates
                checks[f"nsdl_{group.lower()}_span_days"] = span
                if nsdl.get("status") == "AVAILABLE" and (dates < 60 or span < 90):
                    blockers.append(f"NSDL_{group}_HISTORY_BELOW_DECLARED_THRESHOLD")
            if nsdl.get("status") == "AVAILABLE":
                for group in ("FPI", "DII"):
                    item = nsdl_groups.get(group, {})
                    if int(item.get("unique_dates", 0) or 0) < 60 or int(item.get("span_days", 0) or 0) < 90:
                        blockers.append("NSDL_AVAILABLE_STATUS_CONTRADICTS_GROUP_COVERAGE")
        except Exception as exc:
            blockers.append(f"INVALID_NS DL_REPORT:{type(exc).__name__}:{exc}".replace("NS DL","NSDL"))
    else:
        blockers.append(f"MISSING_REQUIRED_INPUT:{NSDL_REPORT}")

    if FACTOR_COVERAGE.exists():
        try:
            factors = json.loads(FACTOR_COVERAGE.read_text(encoding="utf-8"))
            checks["factor_groups_total"] = int(factors.get("factor_groups", 0) or 0)
            checks["factor_groups_fully_available"] = int(factors.get("fully_available_schema_groups", 0) or 0)
            checks["factor_groups_not_connected"] = int(factors.get("not_connected", 0) or 0)
            if checks["factor_groups_fully_available"] < checks["factor_groups_total"]:
                blockers.append("FACTOR_REGISTRY_HAS_INCOMPLETE_SOURCE_COVERAGE")
            if FACTOR_ROWS.exists():
                factor_rows = pd.read_csv(FACTOR_ROWS)
                checks["factor_csv_rows"] = int(len(factor_rows))
                if len(factor_rows) != checks["factor_groups_total"]:
                    blockers.append("FACTOR_CSV_JSON_COUNT_MISMATCH")
            else:
                blockers.append(f"MISSING_REQUIRED_INPUT:{FACTOR_ROWS}")
            if MANIFEST.exists():
                final_manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
                reconciliation = final_manifest.get("final_manifest_reconciliation", {})
                checks["final_manifest_reconciliation_status"] = reconciliation.get("status", "UNKNOWN")
                if reconciliation.get("status") != "RECONCILED":
                    blockers.append("FINAL_MANIFEST_NOT_RECONCILED")
                final_p0 = final_manifest.get("p0_coverage", {})
                available_groups = final_p0.get("group_availability_after_repair", {})
                if final_p0.get("required_series_available") is True and any(v is not True for v in available_groups.values()):
                    blockers.append("FINAL_MANIFEST_P0_BOOLEAN_CONTRADICTS_GROUP_STATUS")
                repair_status = checks.get("repair_fpi_dii_flows_status", "UNKNOWN")
                manifest_flow_status = final_p0.get("fpi_dii_status", "UNKNOWN")
                if manifest_flow_status == "AVAILABLE" and repair_status != "AVAILABLE":
                    blockers.append("MANIFEST_REPAIR_FPI_DII_STATUS_MISMATCH")
                manifest_corp_status = final_p0.get("corporate_events_status", "UNKNOWN")
                repair_corp_status = checks.get("repair_corporate_events_status", "UNKNOWN")
                if manifest_corp_status == "AVAILABLE" and repair_corp_status != "AVAILABLE":
                    blockers.append("MANIFEST_REPAIR_CORPORATE_EVENTS_STATUS_MISMATCH")
        except Exception as exc:
            blockers.append(f"INVALID_FACTOR_COVERAGE_REPORT:{type(exc).__name__}:{exc}")
    else:
        blockers.append(f"MISSING_REQUIRED_INPUT:{FACTOR_COVERAGE}")

    if REGIME_REPORT.exists():
        try:
            regime = json.loads(REGIME_REPORT.read_text(encoding="utf-8"))
            checks["historical_regime_study_status"] = regime.get("research_status", regime.get("status", "UNKNOWN"))
            checks["historical_regime_windows"] = int(regime.get("window_rows", 0) or 0)
            if checks["historical_regime_windows"] < 1 or checks["historical_regime_study_status"] == "BLOCKED":
                blockers.append("HISTORICAL_REGIME_STUDY_NOT_VALIDATED")
        except Exception as exc:
            blockers.append(f"INVALID_HISTORICAL_REGIME_REPORT:{type(exc).__name__}:{exc}")
    else:
        blockers.append(f"MISSING_REQUIRED_INPUT:{REGIME_REPORT}")

    if PANEL.exists() and EQUITY.exists():
        try:
            panel = pd.read_csv(PANEL)
            equity = pd.read_csv(EQUITY)
            panel.columns = [str(c).strip().upper() for c in panel.columns]
            equity.columns = [str(c).strip().upper() for c in equity.columns]
            if not {"DATE", "SERIES", "CLOSE"}.issubset(panel.columns):
                blockers.append("MARKET_PANEL_SCHEMA_INVALID")
            elif "DATE" not in equity.columns:
                blockers.append("EQUITY_PANEL_SCHEMA_INVALID")
            else:
                pdate = pd.to_datetime(panel["DATE"], errors="coerce").dropna()
                edate = pd.to_datetime(equity["DATE"], errors="coerce").dropna()
                if pdate.empty or edate.empty:
                    blockers.append("MARKET_OR_EQUITY_PANEL_HAS_NO_VALID_DATES")
                else:
                    pmax, emax = pdate.max().normalize(), edate.max().normalize()
                    gap = int((emax - pmax).days)
                    checks["market_panel_latest_date"] = pmax.date().isoformat()
                    checks["equity_panel_latest_date"] = emax.date().isoformat()
                    checks["equity_minus_market_calendar_days"] = gap
                    if gap > 3 or gap < -3:
                        blockers.append("MARKET_PANEL_STALE_OR_DATE_MISALIGNED")
                    bad = panel[pd.to_numeric(panel["CLOSE"], errors="coerce").isna() | (pd.to_numeric(panel["CLOSE"], errors="coerce") <= 0)]
                    checks["invalid_market_close_rows"] = int(len(bad))
                    if len(bad):
                        blockers.append("MARKET_PANEL_HAS_INVALID_CLOSES")
        except Exception as exc:
            blockers.append(f"MARKET_PANEL_QA_ERROR:{type(exc).__name__}:{exc}")

    status = "PASS" if not blockers else "BLOCKED"
    report = {
        "status": status,
        "gate_type": "STRICT_MACRO_GEO_HARD_GATE_AUDIT_BRANCH_ONLY",
        "checked_inputs": [str(COVERAGE), str(EVENT_REPORT), str(EVENT_AUDIT), str(PANEL), str(EQUITY), str(MANIFEST), str(REPAIR), str(FACTOR_COVERAGE), str(REGIME_REPORT), str(NSDL_REPORT), str(FACTOR_ROWS)],
        "checks": checks,
        "blockers": sorted(set(blockers)),
        "candidate_release_allowed": status == "PASS",
        "missing_data_semantics": "UNKNOWN/BLOCKED; never interpreted as negative evidence",
        "production_selector_changed": False,
        "ranking_score_changed": False,
        "pressure_fade_changed": False,
        "note": "A PASS means the defined P0 coverage, event-study and freshness gates passed; it is not a guarantee of stock returns or proof of causal geopolitical effects."
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
