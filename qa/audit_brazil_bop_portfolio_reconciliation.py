#!/usr/bin/env python3
"""Independent BPM6 portfolio-flow reconciliation diagnostic.

Diagnostic only: it never repairs, fills, rescales or admits observations.
A FAIL is retained as evidence and does not abort the acquisition artifact.
"""
import argparse
import hashlib
import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path


def local(tag):
    return tag.rsplit("}", 1)[-1]


def read_series(path, codes):
    root = ET.parse(path).getroot()
    if local(root.tag) != "StructureSpecificData":
        raise ValueError("Expected SDMX StructureSpecificData")
    out = {}
    for node in root.iter():
        if local(node.tag) != "Series":
            continue
        code = node.get("INDICATOR")
        if code not in codes:
            continue
        if code in out:
            raise ValueError(f"Duplicate series for {code}")
        if node.get("REF_AREA") != "BR":
            raise ValueError(f"Unexpected REF_AREA for {code}: {node.get('REF_AREA')}")
        if node.get("FREQ") != "M" or node.get("UNIT_MULT") != "6":
            raise ValueError(f"Unexpected frequency/unit multiplier for {code}")
        values = {}
        for obs in node:
            if local(obs.tag) != "Obs":
                continue
            period, token = obs.get("TIME_PERIOD"), obs.get("OBS_VALUE")
            if not period or not token:
                raise ValueError(f"Missing period/value for {code}")
            if token == "...":
                values[period] = None
            else:
                try:
                    number = float(token)
                except ValueError as exc:
                    raise ValueError(f"Non-numeric token for {code}/{period}: {token}") from exc
                if not math.isfinite(number):
                    raise ValueError(f"Non-finite value for {code}/{period}")
                values[period] = number
        out[code] = values
    missing = sorted(set(codes) - set(out))
    if missing:
        raise ValueError(f"Missing required series: {missing}")
    return out


def reconcile(values, tolerance=1e-8):
    total, assets, liabilities = ("BFP_BP6_USD", "BFPA_BP6_USD", "BFPL_BP6_USD")
    common = sorted(set(values[total]) & set(values[assets]) & set(values[liabilities]))
    if not common:
        raise ValueError("No common periods across portfolio total/assets/liabilities")
    mismatches, missing = [], []
    for period in common:
        a, l, t = values[assets][period], values[liabilities][period], values[total][period]
        if a is None or l is None or t is None:
            missing.append(period)
            continue
        delta = t - (a - l)
        if abs(delta) > tolerance:
            mismatches.append({
                "period": period, "reported_total": t,
                "assets_minus_liabilities": a - l,
                "difference_reported_minus_expected": delta
            })
    return {
        "rule": "BPM6 financial-account balance diagnostic: net acquisition of financial assets minus net incurrence of liabilities",
        "official_sign_rule": "Positive values indicate increases in assets or liabilities; negative values indicate decreases. Financial-account balance is assets minus liabilities.",
        "official_reference": "https://www.imf.org/external/pubs/ft/bop/2013/13-13.pdf",
        "unit_interpretation": "Millions of US dollars: official CL_UNIT_MULT code 6 is labelled Millions and the matched CL_INDICATOR labels specify US Dollars. Raw values were not rescaled.",
        "series_semantics_caveat": "The BFP label is 'Portfolio investment' and does not explicitly say 'balance'. This is a BPM6-consistent reconciliation diagnostic, not proof that the source's BFP total is contractually defined as assets minus liabilities.",
        "series": {"total": total, "assets": assets, "liabilities": liabilities},
        "common_period_count": len(common),
        "matched_period_count": len(common) - len(missing) - len(mismatches),
        "mismatch_count": len(mismatches),
        "missing_period_count": len(missing),
        "first_mismatch_period": mismatches[0]["period"] if mismatches else None,
        "last_mismatch_period": mismatches[-1]["period"] if mismatches else None,
        "max_absolute_difference": max((abs(x["difference_reported_minus_expected"]) for x in mismatches), default=0.0),
        "mean_absolute_difference": (sum(abs(x["difference_reported_minus_expected"]) for x in mismatches) / len(mismatches) if mismatches else 0.0),
        "mismatch_samples_first_10": mismatches[:10],
        "missing_periods": missing,
        "status": "FAIL_RECONCILIATION" if mismatches else ("UNKNOWN_MISSING_VALUES" if missing else "PASS_DIAGNOSTIC_ONLY"),
        "admission": "NOT_AUTHORIZED",
        "next_required_evidence": "Obtain BCB/IMF series metadata or source clarification for BFP_BP6_USD and the 2010-01 structural break before using BFP as a balance or deriving portfolio net flows."
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--brazil-xml", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    raw = a.brazil_xml.read_bytes()
    result = reconcile(read_series(a.brazil_xml, ["BFP_BP6_USD", "BFPA_BP6_USD", "BFPL_BP6_USD"]))
    result["source"] = {
        "source_url": "https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml",
        "raw_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
        "ref_area": "BR", "frequency": "M", "unit_multiplier": "6"
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "mismatch_samples_first_10"}, indent=2))
    # The diagnostic must be retained even when it detects a discrepancy.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
