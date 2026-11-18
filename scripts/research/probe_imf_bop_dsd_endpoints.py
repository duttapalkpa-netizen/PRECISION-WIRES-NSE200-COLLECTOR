#!/usr/bin/env python3
"""Probe official IMF SDMX Central BOP DSD endpoints; archive raw responses and metadata."""
from __future__ import annotations
import hashlib, json, os, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OUT = Path("artifacts/imf_bop_dsd_probe")
OUT.mkdir(parents=True, exist_ok=True)
BASES = [
    ("current", "https://sdmxcentral.imf.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true"),
    ("legacy", "https://sdmxcentral.imf.org/ws/public/sdmxapi/rest/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&detail=full&references=children"),
]
results = []
for label, url in BASES:
    retrieved = datetime.now(timezone.utc).isoformat()
    record = {"label": label, "requested_url": url, "retrieved_at_utc": retrieved}
    try:
        req = Request(url, headers={"User-Agent": "PRECISION-WIRES-research/1.0", "Accept": "application/vnd.sdmx.structure+xml;version=2.1, application/xml, text/xml"})
        with urlopen(req, timeout=25) as response:
            body = response.read()
            headers = response.headers
            status = response.status
            final_url = response.geturl()
        ctype = headers.get("Content-Type", "")
        sha = hashlib.sha256(body).hexdigest()
        record.update({"http_status": status, "final_url": final_url, "content_type": ctype, "byte_length": len(body), "sha256": sha})
        (OUT / f"{label}.response").write_bytes(body)
        # Structural XML check without relying on external packages.
        try:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(body)
            record["xml_parse"] = "PASS"
            record["xml_root_tag"] = root.tag
            structures = [
                node for node in root.iter()
                if node.tag.rsplit("}", 1)[-1] == "DataStructure"
                and node.attrib.get("agencyID") == "IMF"
                and node.attrib.get("id") == "BOP"
                and node.attrib.get("version") == "2.6.0"
            ]
            record["contains_bop_dsd_id"] = bool(structures)
            if structures:
                dsd = structures[0]
                components = next(
                    (node for node in dsd if node.tag.rsplit("}", 1)[-1] == "DataStructureComponents"),
                    None,
                )
                dimension_list = next(
                    (node for node in components or [] if node.tag.rsplit("}", 1)[-1] == "DimensionList"),
                    None,
                )
                attribute_list = next(
                    (node for node in components or [] if node.tag.rsplit("}", 1)[-1] == "AttributeList"),
                    None,
                )
                dimensions = [
                    {"id": node.attrib.get("id"), "position": node.attrib.get("position")}
                    for node in dimension_list or []
                    if node.tag.rsplit("}", 1)[-1] in ("Dimension", "TimeDimension")
                ]
                attributes = [
                    {"id": node.attrib.get("id"), "assignment_status": node.attrib.get("assignmentStatus")}
                    for node in attribute_list or []
                    if node.tag.rsplit("}", 1)[-1] == "Attribute"
                ]
                record["dsd_version"] = dsd.attrib.get("version")
                record["dimension_count"] = len(dimensions)
                record["dimensions"] = dimensions
                record["attribute_count"] = len(attributes)
                record["attributes"] = attributes
        except Exception as exc:
            record["xml_parse"] = "FAIL"
            record["xml_error"] = str(exc)[:300]
    except HTTPError as exc:
        record.update({"http_status": exc.code, "error": "HTTPError", "detail": str(exc)[:500]})
    except (URLError, TimeoutError, OSError) as exc:
        record.update({"error": type(exc).__name__, "detail": str(exc)[:500]})
    results.append(record)
    time.sleep(1)

summary = {
    "schema_version": 1,
    "purpose": "route-discovery-only; no BOP observations downloaded or inferred",
    "source_host_allowlist": ["sdmxcentral.imf.org"],
    "results": results,
    "decision": "METADATA_ROUTE_UNVERIFIED"
}
(OUT / "probe_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2))
if not any(
    r.get("http_status") == 200
    and r.get("xml_parse") == "PASS"
    and r.get("contains_bop_dsd_id") is True
    and r.get("dsd_version") == "2.6.0"
    for r in results
):
    raise SystemExit("No official endpoint returned the expected IMF:BOP(2.6.0) DSD; route remains UNKNOWN")
