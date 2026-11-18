#!/usr/bin/env python3
"""Three-way audit: official BCB BPM6 monthly ZIP vs BCB SGS vs BCB-published IMF SDMX.

The monthly workbook is a historical vintage. The audit compares, never merges,
source values. All units remain million USD as published.
"""
import argparse
import datetime as dt
import hashlib
import io
import json
import math
import zipfile
from pathlib import Path

import openpyxl
import xml.etree.ElementTree as ET

SERIES = {
    "22905": {"label": "Portfolio investment", "imf": "BFP_BP6_USD"},
    "22906": {"label": "Net acquisition of financial assets", "imf": "BFPA_BP6_USD"},
    "22924": {"label": "Net incurrence of liabilities", "imf": "BFPL_BP6_USD"},
}
MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


def local(tag):
    return tag.rsplit("}", 1)[-1]


def read_archive(zip_path):
    raw_zip = Path(zip_path).read_bytes()
    zip_sha = hashlib.sha256(raw_zip).hexdigest()
    with zipfile.ZipFile(io.BytesIO(raw_zip)) as zf:
        bad = zf.testzip()
        if bad:
            raise ValueError(f"BCB monthly ZIP CRC failure: {bad}")
        candidates = [n for n in zf.namelist() if n.lower().endswith(".xlsx")]
        if candidates != ["BalPayM.xlsx"]:
            raise ValueError(f"Unexpected monthly workbook members: {candidates}")
        info = zf.getinfo(candidates[0])
        xlsx_raw = zf.read(candidates[0])
    xlsx_sha = hashlib.sha256(xlsx_raw).hexdigest()
    wb = openpyxl.load_workbook(io.BytesIO(xlsx_raw), read_only=True, data_only=True)
    if "Balance" not in wb.sheetnames:
        raise ValueError(f"Missing Balance sheet; found {wb.sheetnames}")
    ws = wb["Balance"]
    year_row = next(ws.iter_rows(min_row=6, max_row=6, values_only=True))
    month_row = next(ws.iter_rows(min_row=7, max_row=7, values_only=True))
    code_col = next((i + 1 for i, x in enumerate(year_row) if x == "SGS Code"), None)
    if code_col is None:
        raise ValueError("Could not find SGS Code column in row 6")
    periods = {}
    year = None
    for col in range(2, code_col):
        y = year_row[col - 1] if col - 1 < len(year_row) else None
        if isinstance(y, int) and not isinstance(y, bool):
            year = y
        m = month_row[col - 1] if col - 1 < len(month_row) else None
        if year is not None and m in MONTHS:
            period = f"{year:04d}-{MONTHS[m]:02d}"
            if period in periods.values():
                raise ValueError(f"Duplicate workbook period: {period}")
            periods[col] = period
    if not periods:
        raise ValueError("No monthly periods found in workbook headers")
    rows = {code: [] for code in SERIES}
    found = {code: 0 for code in SERIES}
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, values_only=True):
        label = row[0] if row else None
        if not isinstance(label, str):
            continue
        for code, meta in SERIES.items():
            if str(label).strip() == meta["label"] and len(row) >= code_col and str(row[code_col - 1]) == code:
                found[code] += 1
                if found[code] > 1:
                    raise ValueError(f"Duplicate workbook series row for SGS {code}")
                for col, period in periods.items():
                    value = row[col - 1] if col - 1 < len(row) else None
                    if value is None:
                        continue
                    number = float(value)
                    if not math.isfinite(number):
                        raise ValueError(f"Non-finite workbook value {code}/{period}")
                    rows[code].append((period, number))
    missing = [code for code, count in found.items() if count != 1]
    if missing:
        raise ValueError(f"Expected exactly one row for SGS codes: {missing}; found {found}")
    out = {code: dict(values) for code, values in rows.items()}
    return out, {
        "source_url": "https://www.bcb.gov.br/ftp/notaecon/balpaym.zip",
        "archive_raw_bytes": len(raw_zip), "archive_sha256": zip_sha,
        "workbook_member": candidates[0], "workbook_member_bytes": len(xlsx_raw),
        "workbook_member_sha256": xlsx_sha, "workbook_member_timestamp": list(info.date_time),
        "sheet_names": wb.sheetnames, "period_count_by_series": {k: len(v) for k, v in out.items()},
        "period_min": min(min(v) for v in out.values()),
        "period_max": max(max(v) for v in out.values()),
        "units_label": "US$ million"
    }


def read_sgs(path, code):
    rows = json.loads(Path(path).read_text(encoding="utf-8"))
    out = {}
    for row in rows:
        period = dt.datetime.strptime(row["data"], "%d/%m/%Y").strftime("%Y-%m")
        if period in out:
            raise ValueError(f"Duplicate SGS {code} period {period}")
        value = float(row["valor"])
        if not math.isfinite(value):
            raise ValueError(f"Non-finite SGS {code} value {period}")
        out[period] = value
    return out


def read_imf(path):
    root = ET.parse(path).getroot()
    if local(root.tag) != "StructureSpecificData":
        raise ValueError("Expected IMF StructureSpecificData")
    out = {}
    wanted = {v["imf"]: k for k, v in SERIES.items()}
    for node in root.iter():
        if local(node.tag) != "Series" or node.get("INDICATOR") not in wanted:
            continue
        code = wanted[node.get("INDICATOR")]
        if code in out:
            raise ValueError(f"Duplicate IMF series {node.get('INDICATOR')}")
        if node.get("REF_AREA") != "BR" or node.get("FREQ") != "M" or node.get("UNIT_MULT") != "6":
            raise ValueError(f"Unexpected IMF attributes for {node.get('INDICATOR')}")
        values = {}
        for obs in node:
            if local(obs.tag) == "Obs":
                period, token = obs.get("TIME_PERIOD"), obs.get("OBS_VALUE")
                if not period or token in (None, ""):
                    raise ValueError("Missing IMF period/value")
                values[period] = None if token == "..." else float(token)
        out[code] = values
    if set(out) != set(SERIES):
        raise ValueError(f"Missing IMF series: {sorted(set(SERIES)-set(out))}")
    return out


def compare(left, right, tolerance=0.051):
    common = sorted(set(left) & set(right))
    diffs = [{"period": p, "left": left[p], "right": right[p], "difference": left[p] - right[p]}
             for p in common if right[p] is not None and abs(left[p] - right[p]) > tolerance]
    missing = [p for p in common if right[p] is None]
    pre = [p for p in common if p < "2010-01"]
    post = [p for p in common if p >= "2010-01"]
    def count_mismatch(periods):
        return sum(1 for p in periods if right[p] is not None and abs(left[p] - right[p]) > tolerance)
    return {
        "common_period_count": len(common), "left_only_period_count": len(set(left)-set(right)),
        "right_only_period_count": len(set(right)-set(left)), "right_missing_count": len(missing),
        "match_within_tolerance_count": len(common)-len(missing)-len(diffs),
        "mismatch_count": len(diffs), "mismatch_pre_2010_count": count_mismatch(pre),
        "mismatch_2010_onward_count": count_mismatch(post),
        "first_mismatch": diffs[0]["period"] if diffs else None,
        "last_mismatch": diffs[-1]["period"] if diffs else None,
        "max_abs_difference": max((abs(x["difference"]) for x in diffs), default=0.0),
        "mismatch_samples_first_5": diffs[:5]
    }


def audit(zip_path, imf_xml, sgs_dir, tolerance=0.051):
    archive, archive_meta = read_archive(zip_path)
    imf = read_imf(imf_xml)
    sgs = {code: read_sgs(Path(sgs_dir) / f"{code}.json", code) for code in SERIES}
    reports = {}
    identity = []
    for code, meta in SERIES.items():
        a, s, i = archive[code], sgs[code], imf[code]
        reports[code] = {
            "label": meta["label"], "imf_indicator": meta["imf"],
            "archive_vs_sgs": compare(a, s, tolerance),
            "archive_vs_imf_sdmx": compare(a, i, tolerance),
            "sgs_vs_imf_sdmx": compare(s, i, tolerance)
        }
    common = sorted(set(archive["22905"]) & set(archive["22906"]) & set(archive["22924"]))
    for period in common:
        delta = archive["22905"][period] - (archive["22906"][period] - archive["22924"][period])
        if abs(delta) > tolerance:
            identity.append({"period": period, "net": archive["22905"][period],
                             "assets_minus_liabilities": archive["22906"][period]-archive["22924"][period],
                             "difference": delta})
    return {
        "schema_version": 1,
        "status": "PASS_ARCHIVE_CAPTURE_AND_THREE_WAY_DIAGNOSTIC",
        "scope": "Historical BCB BPM6 monthly workbook vs current BCB SGS API vs BCB-published IMF-SDMX XML; no source substitution or production admission.",
        "rounding_tolerance_million_usd": tolerance,
        "archive_provenance": archive_meta,
        "comparisons": reports,
        "archive_internal_identity": {
            "rule": "BCB monthly archive 22905 = 22906 - 22924",
            "common_period_count": len(common), "mismatch_count": len(identity),
            "mismatch_samples_first_5": identity[:5],
            "status": "PASS_WITHIN_ROUNDING" if not identity else "FAIL"
        },
        "interpretation": {
            "source_vintage_note": "Workbook member timestamp is archive metadata only; it is not treated as a formal publication timestamp.",
            "divergence_cause": "UNKNOWN_NOT_ESTABLISHED",
            "instruction": "Differences may reflect vintage/revisions or source lineage; do not infer cause from matching patterns alone."
        },
        "admission": {"brazil_portfolio_flow_panel": "NOT_AUTHORIZED",
                      "global_em_aggregate": "NOT_AUTHORIZED", "trading_signal": "NOT_AUTHORIZED"}
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--monthly-zip", required=True, type=Path)
    ap.add_argument("--imf-xml", required=True, type=Path)
    ap.add_argument("--sgs-dir", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()
    result = audit(args.monthly_zip, args.imf_xml, args.sgs_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "comparisons"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
