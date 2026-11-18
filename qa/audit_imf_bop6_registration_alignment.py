#!/usr/bin/env python3
"""Compare IMF SDMX Central Brazil registration with the actual BCB XML dataflow ID.

A registry/payload ID difference is reported as an unresolved alignment issue,
not automatically treated as an invalid payload or a confirmed alias.
"""
import argparse
import json
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


class RegistrationTable(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.row = None
        self.cell = None
        self.href = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "tr":
            self.row = []
        elif tag in {"td", "th"} and self.row is not None:
            self.cell = {"text": "", "hrefs": []}
        elif tag == "a" and self.cell is not None and attrs.get("href"):
            self.cell["hrefs"].append(attrs["href"])

    def handle_data(self, data):
        if self.cell is not None:
            self.cell["text"] += data

    def handle_endtag(self, tag):
        if tag in {"td", "th"} and self.cell is not None and self.row is not None:
            self.cell["text"] = " ".join(self.cell["text"].split())
            self.row.append(self.cell)
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.rows.append(self.row)
            self.row = None


def parse_registration(path):
    parser = RegistrationTable()
    parser.feed(Path(path).read_text(encoding="utf-8", errors="replace"))
    matches = []
    for row in parser.rows:
        texts = [c["text"] for c in row]
        if len(texts) >= 3 and texts[0] == "IMF:BOP6(1.0)" and texts[1] == "IMF:BR1":
            urls = row[2]["hrefs"] + [texts[2]]
            matches.append({
                "dataflow": texts[0], "provider": texts[1],
                "url_candidates": list(dict.fromkeys(urls)),
                "last_updated": texts[3] if len(texts) > 3 else None
            })
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one IMF:BOP6(1.0)/IMF:BR1 registration row; found {len(matches)}")
    return matches[0]


def parse_dataflow(path, expected_id):
    root = ET.parse(path).getroot()
    nodes = [e for e in root.iter() if e.tag.rsplit("}", 1)[-1] == "Dataflow"
             and e.get("agencyID") == "IMF" and e.get("id") == expected_id and e.get("version") == "1.0"]
    if len(nodes) != 1:
        raise ValueError(f"Expected exactly one IMF:{expected_id}:1.0 dataflow; found {len(nodes)}")
    refs = []
    for node in nodes[0].iter():
        if node.tag.rsplit("}", 1)[-1] == "Structure":
            for ref in node.iter():
                if ref.tag.rsplit("}", 1)[-1] == "Ref":
                    refs.append({k: ref.get(k) for k in ("agencyID", "id", "version")})
    return {"agencyID": "IMF", "id": expected_id, "version": "1.0",
            "data_structure_refs": refs}


def parse_constraint(path, expected_id):
    root = ET.parse(path).getroot()
    nodes = [e for e in root.iter() if e.tag.rsplit("}", 1)[-1] == "ContentConstraint"
             and e.get("agencyID") == "IMF" and e.get("id") == expected_id and e.get("version") == "1.0"]
    if len(nodes) != 1:
        raise ValueError(f"Expected exactly one IMF:{expected_id}:1.0 constraint; found {len(nodes)}")
    refs = []
    for node in nodes[0].iter():
        if node.tag.rsplit("}", 1)[-1] == "Dataflow":
            for ref in node:
                if ref.tag.rsplit("}", 1)[-1] == "Ref":
                    refs.append({k: ref.get(k) for k in ("agencyID", "id", "version")})
    return {"agencyID": "IMF", "id": expected_id, "version": "1.0",
            "attached_dataflow_refs": refs}


def parse_bcb_payload(path):
    root = ET.parse(path).getroot()
    structures = [e for e in root.iter() if e.tag.rsplit("}", 1)[-1] == "Structure"]
    refs = []
    for node in structures:
        match = re.search(r"Dataflow=([^:]+):([^:(]+)\(([^)]+)\)", node.get("namespace", ""))
        if match:
            refs.append({"agencyID": match.group(1), "id": match.group(2), "version": match.group(3)})
    if len(refs) != 1:
        raise ValueError(f"Expected one BCB payload Dataflow namespace; found {refs}")
    return refs[0]


def audit(registration_html, bop6_dataflow, bop6_constraint, bop_bpm6_dataflow,
          bop_bp6_constraint, bcb_payload):
    registration = parse_registration(registration_html)
    reg_url = "https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
    if reg_url not in registration["url_candidates"]:
        raise ValueError(f"Brazil registration row does not list expected BCB URL: {registration['url_candidates']}")
    reg_flow = parse_dataflow(bop6_dataflow, "BOP6")
    reg_constraint = parse_constraint(bop6_constraint, "BOP6_CONSTRAINT")
    payload_flow = parse_bcb_payload(bcb_payload)
    payload_dataflow = parse_dataflow(bop_bpm6_dataflow, "BOP_BPM6")
    payload_constraint = parse_constraint(bop_bp6_constraint, "BOP_BP6_CONSTRAINT")
    return {
        "status": "PASS_REGISTRATION_PAYLOAD_ALIGNMENT_AUDIT_EXECUTED",
        "scope": "IMF SDMX Central registration row, BOP6 registration dataflow/constraint, BCB payload Structure namespace, and BOP_BPM6 dataflow/constraint compared; no alias inferred.",
        "registration": registration,
        "registered_dataflow": reg_flow,
        "registered_constraint": reg_constraint,
        "bcb_payload_dataflow_reference": payload_flow,
        "payload_dataflow_metadata": payload_dataflow,
        "payload_constraint_metadata": payload_constraint,
        "alignment": {
            "registry_dataflow_id": "BOP6",
            "bcb_payload_dataflow_id": payload_flow["id"],
            "ids_equal": payload_flow["id"] == "BOP6",
            "relationship": "MATCH" if payload_flow["id"] == "BOP6" else "UNRESOLVED_REGISTRY_PAYLOAD_ID_DIFFERENCE",
            "alias_or_mapping_proven": False
        },
        "admission": {"brazil_portfolio_flow_panel": "NOT_AUTHORIZED",
                      "global_em_aggregate": "NOT_AUTHORIZED", "trading_signal": "NOT_AUTHORIZED"}
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--registration-html", required=True, type=Path)
    p.add_argument("--bop6-dataflow", required=True, type=Path)
    p.add_argument("--bop6-constraint", required=True, type=Path)
    p.add_argument("--bop-bpm6-dataflow", required=True, type=Path)
    p.add_argument("--bop-bp6-constraint", required=True, type=Path)
    p.add_argument("--bcb-payload", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    try:
        result = audit(a.registration_html, a.bop6_dataflow, a.bop6_constraint,
                       a.bop_bpm6_dataflow, a.bop_bp6_constraint, a.bcb_payload)
    except (OSError, ValueError, ET.ParseError) as exc:
        result = {"status": "FAIL", "error": str(exc), "admission": "NOT_AUTHORIZED"}
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS_REGISTRATION_PAYLOAD_ALIGNMENT_AUDIT_EXECUTED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
