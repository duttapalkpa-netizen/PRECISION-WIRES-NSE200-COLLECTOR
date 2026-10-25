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
PANEL = Path("data/external/market_panel.csv")
EQUITY = Path("data/processed/nse_eq_200_sessions.csv")
MANIFEST = Path("outputs/macro_geo/p0_collection_manifest.json")
OUT = Path("outputs/macro_geo/hard_gate_report.json")
ALLOWED_EVENT_STATUSES = {"COMPUTED_EXPLORATORY", "COMPUTED_EXPLORATORY_WITH_PENDING_EVENTS"}


def main():
    checks = {}
    blockers = []
    for path in (COVERAGE, EVENT_REPORT, PANEL, EQUITY):
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
            if old_status == "PASS_WITH_CRITICAL_DATA_GAPS" or old_required is False:
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
        "checked_inputs": [str(COVERAGE), str(EVENT_REPORT), str(PANEL), str(EQUITY), str(MANIFEST)],
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
