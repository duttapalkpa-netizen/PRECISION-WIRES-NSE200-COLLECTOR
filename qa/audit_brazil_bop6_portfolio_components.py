#!/usr/bin/env python3
"""Component-level portfolio reconciliation across BCB archive, SGS and IMF SDMX."""
import argparse
import datetime as dt
import hashlib
import io
import json
import math
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
import openpyxl

SERIES = {
    "22905": {"label": "Portfolio investment", "imf": "BFP_BP6_USD"},
    "22906": {"label": "Net acquisition of financial assets", "imf": "BFPA_BP6_USD"},
    "22909": {"label": "Equity – assets", "imf": "BFPAEEO_BP6_USD"},
    "22912": {"label": "Investment fund shares – assets", "imf": "BFPAEIS_BP6_USD"},
    "22915": {"label": "Debt securities", "imf": "BFPAD_BP6_USD"},
    "22924": {"label": "Net incurrence of liabilities", "imf": "BFPL_BP6_USD"},
    "22927": {"label": "Equity – liabilities", "imf": "BFPLEEO_BP6_USD"},
    "22936": {"label": "Investment fund shares – liabilities", "imf": "BFPLEIS_BP6_USD"},
    "22939": {"label": "Debt securities", "imf": "BFPLD_BP6_USD"},
}
ROLLUPS = {
    "assets": {"parent": "22906", "children": ["22909", "22912", "22915"]},
    "liabilities": {"parent": "22924", "children": ["22927", "22936", "22939"]},
    "net": {"parent": "22905", "children": ["22906", "22924"], "operation": "subtract"},
}
MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


def local(tag):
    return tag.rsplit("}", 1)[-1]


def compare(left, right, tolerance=0.051):
    common = sorted(set(left) & set(right))
    mismatches = [{"period": p, "left": left[p], "right": right[p],
                   "difference": left[p] - right[p]}
                  for p in common if right[p] is not None and abs(left[p] - right[p]) > tolerance]
    missing = [p for p in common if right[p] is None]
    pre = [p for p in common if p < "2010-01"]
    post = [p for p in common if p >= "2010-01"]
    return {
        "common_period_count": len(common),
        "left_only_period_count": len(set(left) - set(right)),
        "right_only_period_count": len(set(right) - set(left)),
        "right_missing_count": len(missing),
        "match_count": len(common) - len(missing) - len(mismatches),
        "mismatch_count": len(mismatches),
        "mismatch_pre_2010_count": sum(p in {x["period"] for x in mismatches} for p in pre),
        "mismatch_2010_onward_count": sum(p in {x["period"] for x in mismatches} for p in post),
        "first_mismatch": mismatches[0]["period"] if mismatches else None,
        "last_mismatch": mismatches[-1]["period"] if mismatches else None,
        "max_abs_difference": max((abs(x["difference"]) for x in mismatches), default=0.0),
        "mismatch_samples_first_5": mismatches[:5]
    }


def load_archive(path):
    raw = Path(path).read_bytes()
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        bad = z.testzip()
        if bad:
            raise ValueError(f"Archive CRC failure: {bad}")
        if z.namelist() != ["BalPayM.xlsx"]:
            raise ValueError(f"Unexpected workbook member list: {z.namelist()}")
        xlsx = z.read("BalPayM.xlsx")
    wb = openpyxl.load_workbook(io.BytesIO(xlsx), read_only=True, data_only=True)
    ws = wb["Balance"]
    yr = next(ws.iter_rows(min_row=6, max_row=6, values_only=True))
    mo = next(ws.iter_rows(min_row=7, max_row=7, values_only=True))
    code_col = next((i + 1 for i, v in enumerate(yr) if v == "SGS Code"), None)
    if code_col is None:
        raise ValueError("Missing SGS Code column")
    periods, year = {}, None
    for col in range(2, code_col):
        if isinstance(yr[col - 1], int):
            year = yr[col - 1]
        month = mo[col - 1]
        if year is not None and month in MONTHS:
            periods[col] = f"{year:04d}-{MONTHS[month]:02d}"
    found = {}
    for row in ws.iter_rows(values_only=True):
        if len(row) < code_col:
            continue
        code = str(row[code_col - 1])
        if code not in SERIES:
            continue
        if code in found:
            raise ValueError(f"Duplicate BCB workbook SGS row {code}")
        if str(row[0]).strip() != SERIES[code]["label"]:
            raise ValueError(f"Unexpected workbook label for {code}: {row[0]!r}")
        values = {}
        for col, period in periods.items():
            v = row[col - 1]
            if v is not None:
                n = float(v)
                if not math.isfinite(n):
                    raise ValueError(f"Non-finite workbook value {code}/{period}")
                values[period] = n
        found[code] = values
    if set(found) != set(SERIES):
        raise ValueError(f"Missing workbook SGS rows: {sorted(set(SERIES)-set(found))}")
    return found, {"zip_bytes": len(raw), "zip_sha256": hashlib.sha256(raw).hexdigest(),
                   "xlsx_bytes": len(xlsx), "xlsx_sha256": hashlib.sha256(xlsx).hexdigest(),
                   "sheets": wb.sheetnames, "period_min": min(min(x) for x in found.values()),
                   "period_max": max(max(x) for x in found.values())}


def load_imf(path):
    root = ET.parse(path).getroot()
    if local(root.tag) != "StructureSpecificData":
        raise ValueError("Expected StructureSpecificData")
    reverse = {v["imf"]: k for k, v in SERIES.items()}
    out = {}
    for node in root.iter():
        if local(node.tag) != "Series" or node.get("INDICATOR") not in reverse:
            continue
        code = reverse[node.get("INDICATOR")]
        if code in out:
            raise ValueError(f"Duplicate IMF series {node.get('INDICATOR')}")
        if node.get("REF_AREA") != "BR" or node.get("FREQ") != "M" or node.get("UNIT_MULT") != "6":
            raise ValueError(f"Unexpected attributes for {node.get('INDICATOR')}")
        vals = {}
        for obs in node:
            if local(obs.tag) == "Obs":
                period, token = obs.get("TIME_PERIOD"), obs.get("OBS_VALUE")
                if not period or token in (None, ""):
                    raise ValueError("Missing IMF period/value")
                vals[period] = None if token == "..." else float(token)
        out[code] = vals
    if set(out) != set(SERIES):
        raise ValueError(f"Missing IMF portfolio series: {sorted(set(SERIES)-set(out))}")
    return out


def load_sgs(path, code):
    rows = json.loads(Path(path).read_text(encoding="utf-8"))
    vals = {}
    for row in rows:
        p = dt.datetime.strptime(row["data"], "%d/%m/%Y").strftime("%Y-%m")
        if p in vals:
            raise ValueError(f"Duplicate SGS {code}/{p}")
        n = float(row["valor"])
        if not math.isfinite(n):
            raise ValueError(f"Non-finite SGS {code}/{p}")
        vals[p] = n
    return vals


def rollup(source, tolerance=0.051):
    out = {}
    for name, spec in ROLLUPS.items():
        parent = spec["parent"]
        children = spec["children"]
        common = set(source[parent])
        for child in children:
            common &= set(source[child])
        mismatches = []
        for p in sorted(common):
            if spec.get("operation") == "subtract":
                expected = source[children[0]][p] - source[children[1]][p]
            else:
                expected = sum(source[c][p] for c in children)
            actual = source[parent][p]
            if actual is not None and expected is not None and abs(actual - expected) > tolerance:
                mismatches.append({"period": p, "reported_parent": actual,
                                   "component_calculation": expected,
                                   "difference": actual - expected})
        out[name] = {"parent_sgs_code": parent, "child_sgs_codes": children,
                     "common_period_count": len(common), "match_count": len(common)-len(mismatches),
                     "mismatch_count": len(mismatches),
                     "first_mismatch": mismatches[0]["period"] if mismatches else None,
                     "last_mismatch": mismatches[-1]["period"] if mismatches else None,
                     "mismatch_samples_first_5": mismatches[:5],
                     "status": "PASS_WITHIN_TOLERANCE" if not mismatches else "FAIL"}
    return out


def audit(monthly_zip, imf_xml, sgs_dir):
    archive, archive_meta = load_archive(monthly_zip)
    imf = load_imf(imf_xml)
    sgs = {c: load_sgs(Path(sgs_dir) / f"{c}.json", c) for c in SERIES}
    comparisons = {}
    for code, meta in SERIES.items():
        comparisons[code] = {
            "label": meta["label"], "imf_indicator": meta["imf"],
            "archive_vs_imf": compare(archive[code], imf[code]),
            "archive_vs_sgs": compare(archive[code], sgs[code]),
            "sgs_vs_imf": compare(sgs[code], imf[code])
        }
    return {
        "schema_version": 1,
        "status": "PASS_COMPONENT_AUDIT_EXECUTED",
        "scope": "Nine official BCB portfolio parent/component series compared across the historical workbook, current SGS API and BCB-published IMF-SDMX XML. Diagnostic only.",
        "comparison_tolerance_million_usd": 0.051,
        "rollup_tolerance_million_usd": {"BCB_monthly_archive": 0.051, "BCB_current_SGS": 0.151, "BCB_published_IMF_SDMX": 0.051},
        "archive_provenance": archive_meta,
        "component_rollups": {"BCB_monthly_archive": rollup(archive),
                              "BCB_current_SGS": rollup(sgs, tolerance=0.151),
                              "BCB_published_IMF_SDMX": rollup(imf)},
        "series_comparisons": comparisons,
        "interpretation": "Any mismatch is retained as evidence; it is not automatically a source error. Historical vintage, revisions and source lineage remain distinct.",
        "admission": {"brazil_portfolio_flow_panel": "NOT_AUTHORIZED",
                      "global_em_aggregate": "NOT_AUTHORIZED", "trading_signal": "NOT_AUTHORIZED"}
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--monthly-zip", required=True, type=Path)
    p.add_argument("--imf-xml", required=True, type=Path)
    p.add_argument("--sgs-dir", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    result = audit(a.monthly_zip, a.imf_xml, a.sgs_dir)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "component_rollups": result["component_rollups"],
                      "series_comparison_counts": {c: {k: v["mismatch_count"] for k, v in x.items() if isinstance(v, dict)}
                                                   for c, x in result["series_comparisons"].items()}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
