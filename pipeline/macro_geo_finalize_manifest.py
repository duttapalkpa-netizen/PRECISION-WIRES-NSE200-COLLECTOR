#!/usr/bin/env python3
"""Reconcile the P0 collector manifest after all repair and coverage audits.

This does not manufacture source coverage. It updates the early collector manifest
from the final source-coverage audit and preserves provenance from repair/NSDL reports.
"""
from pathlib import Path
import json

ROOT = Path(".")
MANIFEST = ROOT / "outputs/macro_geo/p0_collection_manifest.json"
COVERAGE = ROOT / "outputs/macro_geo/source_coverage.json"
REPAIR = ROOT / "outputs/macro_geo/p0_repair_report.json"
NSDL = ROOT / "outputs/macro_geo/nsdl_fpi_dii_collection.json"
REQUIRED_P0 = (
    "benchmark_index", "sector_indices", "volatility", "crude_oil",
    "usd_inr", "fpi_dii_flows", "corporate_events", "geopolitical_events",
)


def read_json(path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def group_is_available(groups, name):
    item = groups.get(name, {})
    try:
        rows = int(item.get("rows", 0) or 0)
    except (TypeError, ValueError):
        rows = 0
    if rows <= 0:
        return False
    if item.get("status") == "AVAILABLE":
        return True
    # Secondary data is eligible only under an explicit, machine-checkable
    # contract emitted by the repair collector. Never promote a bare proxy.
    if item.get("status") != "AVAILABLE_SECONDARY":
        return False
    checks = item.get("domain_qa_checks", [])
    required_checks = {"source identity", "valid positive values", "unique date keys",
                       "requested-window bounds", "freshness <= 3 calendar days",
                       "source URL provenance"}
    return (required_checks.issubset(set(checks))
            and bool(item.get("source"))
            and bool(item.get("url") or item.get("source_urls"))
            and item.get("freshness_status") == "FRESH")


def reconcile_fpi_dii_repair(repair, nsdl):
    """Promote only when official NSDL FPI and DII each meet dated-history thresholds."""
    if repair is None:
        return None
    result = dict(repair)
    groups = dict(result.get("groups", {}))
    details = (nsdl or {}).get("groups", {})
    valid = (nsdl or {}).get("source") == "NSDL official public FPI/DII archives"
    for name in ("FPI", "DII"):
        item = details.get(name, {})
        try:
            valid = valid and int(item.get("unique_dates", 0) or 0) >= 60 and int(item.get("span_days", 0) or 0) >= 90
        except (TypeError, ValueError):
            valid = False
    if valid and (nsdl or {}).get("status") == "AVAILABLE":
        old = dict(groups.get("fpi_dii_flows", {}))
        groups["fpi_dii_flows"] = {
            **old,
            "status": "AVAILABLE",
            "rows": int(details["FPI"].get("rows", 0) or 0) + int(details["DII"].get("rows", 0) or 0),
            "unique_dates": {"FPI": int(details["FPI"]["unique_dates"]), "DII": int(details["DII"]["unique_dates"])},
            "span_days": {"FPI": int(details["FPI"]["span_days"]), "DII": int(details["DII"]["span_days"])},
            "source": "NSDL official public FPI/DII archives",
            "source_urls": [(nsdl or {}).get("fpi_url"), (nsdl or {}).get("dii_url")],
            "fallback_reason": old.get("reason", "Primary NSE flow endpoint did not meet historical coverage threshold"),
            "reconciliation_rule": "Accepted only because FPI and DII independently meet >=60 distinct dates and >=90 calendar days; no values synthesized."
        }
        result["groups"] = groups
        result["status"] = "ALL_FOUR_AVAILABLE" if all(
            groups.get(k, {}).get("status") in ("AVAILABLE", "AVAILABLE_SECONDARY")
            and int(groups.get(k, {}).get("rows", 0) or 0) > 0
            for k in ("crude_oil", "usd_inr", "corporate_events", "fpi_dii_flows")
        ) else "REPAIR_WITH_GAPS"
    return result

def reconcile(manifest, coverage, repair=None, nsdl=None):
    """Return a refreshed manifest; missing or incomplete evidence stays blocked."""
    p0 = coverage.get("p0_coverage", {})
    groups = p0.get("groups", {})
    availability = {
        name: group_is_available(groups, name)
        for name in REQUIRED_P0
    }
    repair_groups = (repair or {}).get("groups", {})
    corporate_source_verified = (
        group_is_available(groups, "corporate_events")
        and repair_groups.get("corporate_events", {}).get("status") == "AVAILABLE"
        and int(repair_groups.get("corporate_events", {}).get("rows", 0) or 0) > 0
    )
    # Source-coverage audit enforces separate FPI and DII historical thresholds.
    # NSDL's overall status alone is not enough if the downstream coverage audit
    # flags the combined file as insufficient.
    flow_source_verified = group_is_available(groups, "fpi_dii_flows")
    # A file that exists is not enough for corporate disclosures: require the
    # repair report's mapped official-source records as well.
    availability["corporate_events"] = corporate_source_verified
    availability["fpi_dii_flows"] = flow_source_verified
    all_available = all(availability.values())
    manifest = dict(manifest)
    old_p0 = dict(manifest.get("p0_coverage", {}))
    old_p0.update({
        "required_series_available": all_available,
        "required_groups": list(REQUIRED_P0),
        "group_availability_after_repair": availability,
        "fpi_dii_status": "AVAILABLE" if flow_source_verified else "BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE",
        "corporate_events_status": "AVAILABLE" if corporate_source_verified else "BLOCKED_SOURCE_OR_SCHEMA_UNVERIFIED",
    })
    manifest["p0_coverage"] = old_p0
    manifest["operational_status"] = "PASS_WITH_GAPS" if all_available else "PASS_WITH_CRITICAL_DATA_GAPS"
    manifest["status"] = manifest["operational_status"]
    manifest["final_manifest_reconciliation"] = {
        "status": "RECONCILED",
        "stage": "AFTER_REPAIR_NSDL_AND_SOURCE_COVERAGE_AUDITS",
        "source_coverage_status": p0.get("status", "UNKNOWN"),
        "required_p0_groups": list(REQUIRED_P0),
        "available_p0_groups": [k for k, v in availability.items() if v],
        "blocked_p0_groups": [k for k, v in availability.items() if not v],
        "repair_report_present": repair is not None,
        "nsdl_report_present": nsdl is not None,
        "rule": "Manifest status is recalculated from final observed source coverage; no missing group is promoted to AVAILABLE.",
    }
    return manifest


def main():
    manifest = read_json(MANIFEST)
    coverage = read_json(COVERAGE)
    repair = read_json(REPAIR)
    nsdl = read_json(NSDL)
    if manifest is None or coverage is None:
        print(json.dumps({"status": "BLOCKED", "reason": "manifest or final source coverage report missing"}))
        return 1
    try:
        repair = reconcile_fpi_dii_repair(repair, nsdl)
        if repair is not None:
            REPAIR.write_text(json.dumps(repair, indent=2), encoding="utf-8")
        result = reconcile(manifest, coverage, repair, nsdl)
    except Exception as exc:
        print(json.dumps({"status": "BLOCKED", "reason": f"reconciliation error: {type(exc).__name__}: {exc}"}))
        return 1
    MANIFEST.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["final_manifest_reconciliation"], indent=2))
    print(json.dumps({"operational_status": result["operational_status"], "p0_coverage": result["p0_coverage"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
