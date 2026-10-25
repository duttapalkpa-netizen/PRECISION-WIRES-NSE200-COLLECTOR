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
    return item.get("status") == "AVAILABLE" and rows > 0


def reconcile(manifest, coverage, repair=None, nsdl=None):
    """Return a refreshed manifest; missing or incomplete evidence stays blocked."""
    p0 = coverage.get("p0_coverage", {})
    groups = p0.get("groups", {})
    availability = {
        name: group_is_available(groups, name)
        for name in REQUIRED_P0
    }
    all_available = all(availability.values())

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
