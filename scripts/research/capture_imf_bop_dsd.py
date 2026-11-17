#!/usr/bin/env python3
"""Capture and qualify official IMF BOP SDMX structure metadata.

Captures untouched response bytes plus request/final URL, HTTP headers,
retrieval timestamp, byte length and SHA-256. No observations are fabricated
or inferred. A successful structure capture does not qualify a data panel.
"""
from __future__ import annotations

import hashlib
import json
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "evidence" / "imf_bop_dsd"
SOURCES = {
    "dsd": "https://sdmxcentral.imf.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true",
    "dataflow": "https://sdmxcentral.imf.org/sdmx/v2/structure/dataflow/IMF/BOP_BPM6/1.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true",
    "constraint": "https://sdmxcentral.imf.org/sdmx/v2/structure/contentconstraint/IMF/BOP_BP6_CONSTRAINT/1.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true",
}
HEADERS = {"Accept": "application/vnd.sdmx.structure+xml;version=2.1, application/xml;q=0.9, */*;q=0.1", "User-Agent": "PRECISION-WIRES-research-metadata-audit/1.0"}
TIMEOUT = 45
RETRIES = 2


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def fetch(name: str, url: str, out: Path) -> dict:
    request_time = datetime.now(timezone.utc).isoformat()
    last_error = None
    for attempt in range(RETRIES + 1):
        req = urllib.request.Request(url, headers=HEADERS, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                body = response.read()
                meta = {
                    "source_name": name,
                    "requested_url": url,
                    "final_url": response.geturl(),
                    "http_status": response.status,
                    "content_type": response.headers.get("Content-Type", ""),
                    "content_length_header": response.headers.get("Content-Length", ""),
                    "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
                    "request_started_at_utc": request_time,
                    "attempt": attempt + 1,
                    "byte_length": len(body),
                    "sha256": hashlib.sha256(body).hexdigest(),
                    "response_headers": {k: v for k, v in response.headers.items()},
                }
                (out / f"{name}.xml").write_bytes(body)
                (out / f"{name}.http.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                if response.status != 200 or not body:
                    raise RuntimeError(f"{name}: HTTP {response.status} or empty response")
                return meta
        except (urllib.error.URLError, TimeoutError, OSError, RuntimeError) as exc:
            last_error = str(exc)
            if attempt < RETRIES:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"{name}: acquisition failed after {RETRIES + 1} attempts: {last_error}")


def parse_xml(path: Path) -> ET.Element:
    raw = path.read_bytes()
    if not raw:
        raise RuntimeError(f"{path.name}: empty XML")
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        raise RuntimeError(f"{path.name}: malformed XML: {exc}") from exc
    return root


def verify_dsd(root: ET.Element) -> dict:
    nodes = [e for e in root.iter() if local(e.tag) == "DataStructure" and e.attrib.get("id") == "BOP"]
    if len(nodes) != 1:
        raise RuntimeError(f"Expected exactly one IMF BOP DSD, found {len(nodes)}")
    node = nodes[0]
    identity = {k: node.attrib.get(k) for k in ("agencyID", "id", "version")}
    if identity != {"agencyID": "IMF", "id": "BOP", "version": "2.6.0"}:
        raise RuntimeError(f"Unexpected DSD identity: {identity}")
    codelists = [e for e in root.iter() if local(e.tag) == "Codelist"]
    if not codelists:
        raise RuntimeError("DSD response contains no referenced codelists")
    component_names = {"Dimension", "TimeDimension", "MeasureDimension", "PrimaryMeasure", "Attribute"}
    components = [e for e in root.iter() if local(e.tag) in component_names]
    if not components:
        raise RuntimeError("DSD response contains no component definitions")
    return {
        "status": "PASS",
        "identity": identity,
        "component_count": len(components),
        "codelist_count": len(codelists),
        "codelists": [{"agencyID": e.attrib.get("agencyID"), "id": e.attrib.get("id"), "version": e.attrib.get("version"),
                       "code_count": sum(1 for c in e.iter() if local(c.tag) == "Code")} for e in codelists],
    }


def verify_dataflow(root: ET.Element) -> dict:
    flows = [e for e in root.iter() if local(e.tag) == "Dataflow" and e.attrib.get("id") == "BOP_BPM6"]
    if len(flows) != 1:
        raise RuntimeError(f"Expected exactly one IMF BOP_BPM6 dataflow, found {len(flows)}")
    flow = flows[0]
    identity = {k: flow.attrib.get(k) for k in ("agencyID", "id", "version")}
    if identity != {"agencyID": "IMF", "id": "BOP_BPM6", "version": "1.0"}:
        raise RuntimeError(f"Unexpected dataflow identity: {identity}")
    refs = []
    for element in flow.iter():
        if local(element.tag) == "Ref":
            refs.append({k: element.attrib.get(k) for k in ("agencyID", "id", "version", "class", "package")})
    if not any(r.get("agencyID") == "IMF" and r.get("id") == "BOP" and r.get("version") == "2.6.0" for r in refs):
        raise RuntimeError(f"Dataflow does not explicitly reference IMF:BOP:2.6.0: {refs}")
    return {"status": "PASS", "identity": identity, "structure_refs": refs}


def verify_constraint(root: ET.Element) -> dict:
    constraints = [e for e in root.iter() if local(e.tag) == "ContentConstraint" and e.attrib.get("id") == "BOP_BP6_CONSTRAINT"]
    if len(constraints) != 1:
        raise RuntimeError(f"Expected exactly one IMF BOP_BP6_CONSTRAINT, found {len(constraints)}")
    constraint = constraints[0]
    identity = {k: constraint.attrib.get(k) for k in ("agencyID", "id", "version", "type")}
    if identity.get("agencyID") != "IMF" or identity.get("id") != "BOP_BP6_CONSTRAINT":
        raise RuntimeError(f"Unexpected constraint identity: {identity}")
    refs = []
    for e in constraint.iter():
        if local(e.tag) == "Ref":
            refs.append({k: e.attrib.get(k) for k in ("agencyID", "id", "version")})
    if not any(r == {"agencyID": "IMF", "id": "BOP_BPM6", "version": "1.0"} for r in refs):
        raise RuntimeError(f"Constraint does not explicitly attach to IMF:BOP_BPM6:1.0: {refs}")
    regions = [e for e in constraint.iter() if local(e.tag) == "CubeRegion"]
    if not regions:
        raise RuntimeError("Constraint has no CubeRegion")
    return {"status": "PASS", "identity": identity, "dataflow_refs": refs, "cube_region_count": len(regions)}


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = BASE / stamp
    out.mkdir(parents=True, exist_ok=False)
    manifest = {
        "schema_version": 1,
        "capture_id_utc": stamp,
        "capture_started_at_utc": datetime.now(timezone.utc).isoformat(),
        "sources": {},
        "semantic_qa": {},
        "overall_status": "FAIL",
        "limitations": [
            "Structure metadata capture is not observation-data capture.",
            "A registered dataflow is not proof of a public country-level portfolio-investment panel.",
            "No BOP observations, country coverage, or trading feature are admitted by this workflow."
        ],
    }
    errors = []
    for name, url in SOURCES.items():
        try:
            manifest["sources"][name] = fetch(name, url, out)
        except Exception as exc:
            errors.append(str(exc))
    if not errors:
        try:
            manifest["semantic_qa"]["dsd"] = verify_dsd(parse_xml(out / "dsd.xml"))
            manifest["semantic_qa"]["dataflow"] = verify_dataflow(parse_xml(out / "dataflow.xml"))
            manifest["semantic_qa"]["constraint"] = verify_constraint(parse_xml(out / "constraint.xml"))
            manifest["overall_status"] = "PASS_STRUCTURE_METADATA_ONLY"
        except Exception as exc:
            errors.append(str(exc))
    manifest["errors"] = errors
    manifest["capture_completed_at_utc"] = datetime.now(timezone.utc).isoformat()
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"capture_id_utc": stamp, "status": manifest["overall_status"], "sources_captured": len(manifest["sources"]), "errors": errors, "output": str(out)}, sort_keys=True))
    return 0 if manifest["overall_status"] == "PASS_STRUCTURE_METADATA_ONLY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
