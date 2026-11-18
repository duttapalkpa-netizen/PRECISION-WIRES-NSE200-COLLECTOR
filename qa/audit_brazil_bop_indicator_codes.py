#!/usr/bin/env python3
"""Fail-closed ECOFIN INDICATOR vs IMF CL_INDICATOR audit.

A country-prefixed local code can be ECOFIN-compliant while its economic
meaning remains UNKNOWN. This script never promotes code-list compliance to
portfolio-flow eligibility.
"""
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path


def local(tag):
    return tag.rsplit("}", 1)[-1]


def parse_ecofin(path):
    root = ET.parse(path).getroot()
    dsds = [e for e in root.iter() if local(e.tag) == "DataStructure" and e.get("id") == "ECOFIN_DSD"]
    if len(dsds) != 1:
        raise ValueError(f"Expected exactly one IMF:ECOFIN_DSD; found {len(dsds)}")
    dsd = dsds[0]
    identity = {k: dsd.get(k) for k in ("agencyID", "id", "version")}
    if identity != {"agencyID": "IMF", "id": "ECOFIN_DSD", "version": "1.0"}:
        raise ValueError(f"Unexpected ECOFIN DSD identity: {identity}")
    dims = [e for e in dsd.iter() if local(e.tag) == "Dimension" and e.get("id") == "INDICATOR"]
    if len(dims) != 1:
        raise ValueError(f"Expected one INDICATOR dimension; found {len(dims)}")
    refs = [{k: e.get(k) for k in ("agencyID", "id", "version")}
            for e in dims[0].iter() if local(e.tag) == "Ref"]
    expected = {"agencyID": "IMF", "id": "CL_INDICATOR", "version": "1.0"}
    if expected not in refs:
        raise ValueError(f"INDICATOR does not reference IMF:CL_INDICATOR:1.0; got {refs}")
    lists = [e for e in root.iter() if local(e.tag) == "Codelist" and e.get("id") == "CL_INDICATOR"]
    if len(lists) != 1:
        raise ValueError(f"Expected one CL_INDICATOR; found {len(lists)}")
    cl = lists[0]
    if cl.get("agencyID") != "IMF" or cl.get("version") != "1.0":
        raise ValueError("CL_INDICATOR identity/version does not match DSD reference")
    codes = {}
    for node in cl:
        if local(node.tag) != "Code":
            continue
        code = node.get("id")
        if not code or code in codes:
            raise ValueError(f"Missing or duplicate CL_INDICATOR code: {code!r}")
        names = [(e.text or "").strip() for e in node.iter() if local(e.tag) == "Name" and (e.text or "").strip()]
        descriptions = [(e.text or "").strip() for e in node.iter()
                        if local(e.tag) in {"Description", "AnnotationText"} and (e.text or "").strip()]
        codes[code] = {"names": names, "descriptions": descriptions}
    if not codes:
        raise ValueError("CL_INDICATOR contains no codes")
    return codes, {"agency": "IMF", "id": "CL_INDICATOR", "version": "1.0", "code_count": len(codes)}


def parse_brazil(path, ref_area):
    root = ET.parse(path).getroot()
    if local(root.tag) != "StructureSpecificData":
        raise ValueError(f"Unexpected root element: {local(root.tag)}")
    # BCB compact payload encodes the dataflow in Structure/@namespace.
    structures = [e for e in root.iter() if local(e.tag) == "Structure"]
    refs = []
    for node in structures:
        m = re.search(r"Dataflow=([^:]+):([^:(]+)\(([^)]+)\)", node.get("namespace", ""))
        if m:
            refs.append({"agencyID": m.group(1), "id": m.group(2), "version": m.group(3)})
    expected = {"agencyID": "IMF", "id": "BOP_BPM6", "version": "1.0"}
    if refs != [expected]:
        raise ValueError(f"Unexpected/missing BOP_BPM6 dataflow reference: {refs}")
    series = [e for e in root.iter() if local(e.tag) == "Series"]
    counts = Counter()
    obs_count = 0
    areas = set()
    for node in series:
        code, area = node.get("INDICATOR"), node.get("REF_AREA")
        if not code or not area:
            raise ValueError("Series missing INDICATOR or REF_AREA")
        counts[code] += 1
        areas.add(area)
        obs_count += sum(1 for e in node if local(e.tag) == "Obs")
    if not series or areas != {ref_area}:
        raise ValueError(f"Expected REF_AREA={ref_area}; found {sorted(areas)}")
    return counts, {"dataflow": expected, "ref_area": ref_area, "series_count": len(series),
                    "unique_indicator_count": len(counts), "observation_count": obs_count}


def audit(brazil_xml, ecofin_xml, ref_area, country_iso3):
    if not re.fullmatch(r"[A-Z]{2}", ref_area) or not re.fullmatch(r"[A-Z]{3}", country_iso3):
        raise ValueError("REF_AREA must be alpha-2 and country ISO must be alpha-3")
    counts, data = parse_brazil(brazil_xml, ref_area)
    codes, cl_meta = parse_ecofin(ecofin_xml)
    rows = []
    for code in sorted(counts):
        if code in codes:
            validation, semantic = "OFFICIAL_CL_INDICATOR_MATCH", "LABEL_AVAILABLE_REVIEW_REQUIRED"
            metadata = codes[code]
        elif code.startswith(country_iso3 + "_"):
            validation, semantic = "COUNTRY_SPECIFIC_ALLOWED_WARNING", "UNKNOWN_NO_IMF_LABEL"
            metadata = {"names": [], "descriptions": []}
        else:
            validation, semantic = "FAIL_NOT_IN_CODELIST_OR_COUNTRY_PREFIX", "UNKNOWN_QUARANTINE"
            metadata = {"names": [], "descriptions": []}
        rows.append({"indicator": code, "series_count": counts[code],
                     "imf_validation_status": validation, "semantic_status": semantic, **metadata})
    tally = Counter(r["imf_validation_status"] for r in rows)
    bad = tally["FAIL_NOT_IN_CODELIST_OR_COUNTRY_PREFIX"] > 0
    local_codes = tally["COUNTRY_SPECIFIC_ALLOWED_WARNING"] > 0
    return {
        "status": "FAIL" if bad else ("PASS_WITH_WARNINGS" if local_codes else "PASS"),
        "scope": "ECOFIN code-list compliance only; not economic classification or flow admission",
        "data": data, "codelist": cl_meta, "status_counts": dict(tally), "indicators": rows,
        "admission": {"portfolio_flow_panel": "NOT_AUTHORIZED", "global_em_aggregate": "NOT_AUTHORIZED",
                      "trading_signal": "NOT_AUTHORIZED",
                      "reason": "Code-list compliance does not establish portfolio meaning, transaction direction, unit, sign, quality, or vintage."}
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--brazil-xml", required=True, type=Path)
    p.add_argument("--ecofin-dsd-xml", required=True, type=Path)
    p.add_argument("--ref-area", required=True)
    p.add_argument("--country-iso3", required=True)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    try:
        result = audit(a.brazil_xml, a.ecofin_dsd_xml, a.ref_area, a.country_iso3)
    except (OSError, ValueError, ET.ParseError) as exc:
        result = {"status": "FAIL", "error": str(exc), "admission": "NOT_AUTHORIZED"}
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: result.get(k) for k in ("status", "data", "codelist", "status_counts", "admission", "error")}, indent=2))
    return 1 if result["status"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
