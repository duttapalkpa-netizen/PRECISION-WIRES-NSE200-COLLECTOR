#!/usr/bin/env python3
"""Cross-check Brazil BOP6 IMF-SDMX portfolio series against BCB SGS APIs.

Concept matches are provisional. Raw JSON is preserved by the workflow; this
script does not rescale, repair, or admit observations.
"""
import argparse
import datetime as dt
import hashlib
import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path

SERIES = {
    "22905": {"indicator": "BFP_BP6_USD", "label": "Portfolio investment - monthly - net"},
    "22906": {"indicator": "BFPA_BP6_USD", "label": "Portfolio investment - net acquisition of financial assets"},
    "22924": {"indicator": "BFPL_BP6_USD", "label": "Portfolio investment - net incurrence of liabilities"},
}


def local(tag):
    return tag.rsplit("}", 1)[-1]


def parse_month(date_text):
    return dt.datetime.strptime(date_text, "%d/%m/%Y").strftime("%Y-%m")


def load_sgs(path, code):
    raw = Path(path).read_bytes()
    rows = json.loads(raw)
    if not isinstance(rows, list) or not rows:
        raise ValueError(f"SGS {code}: expected non-empty JSON array")
    values = {}
    for row in rows:
        if "data" not in row or "valor" not in row:
            raise ValueError(f"SGS {code}: missing data/valor fields")
        period = parse_month(row["data"])
        if period in values:
            raise ValueError(f"SGS {code}: duplicate period {period}")
        value = float(row["valor"])
        if not math.isfinite(value):
            raise ValueError(f"SGS {code}: non-finite value at {period}")
        values[period] = value
    return values, {"sgs_code": code, "label": SERIES[code]["label"],
                    "raw_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
                    "observation_count": len(values),
                    "first_period": min(values), "last_period": max(values)}


def load_imf_xml(path):
    raw = Path(path).read_bytes()
    root = ET.parse(path).getroot()
    if local(root.tag) != "StructureSpecificData":
        raise ValueError("Expected StructureSpecificData root")
    out = {}
    for node in root.iter():
        if local(node.tag) != "Series":
            continue
        code = node.get("INDICATOR")
        if code not in {v["indicator"] for v in SERIES.values()}:
            continue
        if code in out:
            raise ValueError(f"Duplicate IMF series for {code}")
        if node.get("REF_AREA") != "BR" or node.get("FREQ") != "M" or node.get("UNIT_MULT") != "6":
            raise ValueError(f"Unexpected IMF series attributes for {code}: {node.attrib}")
        values = {}
        for obs in node:
            if local(obs.tag) != "Obs":
                continue
            period, token = obs.get("TIME_PERIOD"), obs.get("OBS_VALUE")
            if not period or token in (None, ""):
                raise ValueError(f"Missing IMF period/value for {code}")
            if token == "...":
                values[period] = None
            else:
                values[period] = float(token)
        out[code] = values
    expected = {v["indicator"] for v in SERIES.values()}
    if set(out) != expected:
        raise ValueError(f"Missing IMF portfolio series: {sorted(expected - set(out))}")
    return out, {"raw_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def compare(sgs_values, imf_values, tolerance=0.051):
    reports = {}
    for sgs_code, meta in SERIES.items():
        indicator = meta["indicator"]
        sgs, imf = sgs_values[sgs_code], imf_values[indicator]
        common = sorted(set(sgs) & set(imf))
        only_sgs, only_imf = sorted(set(sgs) - set(imf)), sorted(set(imf) - set(sgs))
        diffs, missing_imf = [], []
        for period in common:
            if imf[period] is None:
                missing_imf.append(period)
                continue
            delta = sgs[period] - imf[period]
            if abs(delta) > tolerance:
                diffs.append({"period": period, "sgs_value": sgs[period],
                              "imf_sdmx_value": imf[period], "sgs_minus_imf": delta})
        reports[sgs_code] = {
            "indicator": indicator, "common_period_count": len(common),
            "sgs_only_period_count": len(only_sgs), "imf_only_period_count": len(only_imf),
            "imf_missing_value_count": len(missing_imf),
            "match_within_rounding_tolerance_count": len(common) - len(missing_imf) - len(diffs),
            "mismatch_count": len(diffs),
            "first_mismatch_period": diffs[0]["period"] if diffs else None,
            "last_mismatch_period": diffs[-1]["period"] if diffs else None,
            "max_absolute_difference": max((abs(x["sgs_minus_imf"]) for x in diffs), default=0.0),
            "mismatch_samples_first_10": diffs[:10]
        }
    return reports


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--imf-xml", required=True, type=Path)
    p.add_argument("--sgs-dir", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    imf_values, imf_meta = load_imf_xml(a.imf_xml)
    sgs_values, sgs_meta = {}, {}
    for code in SERIES:
        sgs_values[code], sgs_meta[code] = load_sgs(a.sgs_dir / f"{code}.json", code)
    comparisons = compare(sgs_values, imf_values)
    sgs_periods = sorted(set.intersection(*(set(sgs_values[c]) for c in SERIES)))
    identity_diffs = []
    for period in sgs_periods:
        net, assets, liabilities = (sgs_values["22905"].get(period),
                                    sgs_values["22906"].get(period),
                                    sgs_values["22924"].get(period))
        delta = net - (assets - liabilities)
        if abs(delta) > 0.151:
            identity_diffs.append({"period": period, "net": net,
                                   "assets_minus_liabilities": assets - liabilities,
                                   "difference": delta})
    all_match = all(x["mismatch_count"] == 0 and x["sgs_only_period_count"] == 0
                    and x["imf_only_period_count"] == 0 and x["imf_missing_value_count"] == 0
                    for x in comparisons.values())
    result = {
        "schema_version": 1,
        "status": "PASS_CROSS_SOURCE_MATCH" if all_match else "FAIL_SOURCE_DIVERGENCE",
        "scope": "Provisional BCB SGS concept crosswalk versus IMF-SDMX Brazil BOP series; not an approved capital-flow signal.",
        "rounding_tolerance_million_usd": 0.051,
        "source_provenance": {"imf_bcb_xml": imf_meta, "bcb_sgs": sgs_meta},
        "comparisons": comparisons,
        "bcb_sgs_internal_identity": {
            "rule": "SGS 22905 net = SGS 22906 assets - SGS 22924 liabilities",
            "common_period_count": len(sgs_periods),
            "mismatch_count": len(identity_diffs),
            "mismatch_samples_first_10": identity_diffs[:10],
            "status": "PASS_WITHIN_ROUNDING" if not identity_diffs else "FAIL"
        },
        "admission": {"brazil_portfolio_flow_panel": "NOT_AUTHORIZED",
                      "global_em_aggregate": "NOT_AUTHORIZED",
                      "trading_signal": "NOT_AUTHORIZED"},
        "guardrail": "No data source is overwritten or substituted. A match does not establish quality/status attributes or authorize flow admission."
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "comparisons": {
        k: {kk: vv for kk, vv in v.items() if kk != "mismatch_samples_first_10"}
        for k, v in comparisons.items()},
        "bcb_sgs_internal_identity": result["bcb_sgs_internal_identity"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
