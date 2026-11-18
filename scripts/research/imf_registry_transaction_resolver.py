#!/usr/bin/env python3
"""Read-only resolver for the 33 transaction links in archived IMF RSS evidence.

No new RSS/BCB payload acquisition. The transaction IDs, titles, links and
publication timestamps below were extracted from archived Run #1 RSS bytes.
"""
from __future__ import annotations

import concurrent.futures
import datetime as dt
import hashlib
import json
import pathlib
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

OUT = pathlib.Path("imf_transaction_evidence")
OUT.mkdir(parents=True, exist_ok=True)

# Exact entries parsed from archived imf_rss.xml (Run 44301482210).
ITEMS = [
    {"tx_id": 38646, "title": "Transaction #38646 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38646", "pub_date": "Wed, 18 Nov 2026 12:01:46 GMT"},
    {"tx_id": 38645, "title": "Transaction #38645 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38645", "pub_date": "Wed, 18 Nov 2026 12:01:37 GMT"},
    {"tx_id": 38644, "title": "Transaction #38644 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38644", "pub_date": "Wed, 18 Nov 2026 12:01:25 GMT"},
    {"tx_id": 38643, "title": "Transaction #38643 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38643", "pub_date": "Wed, 18 Nov 2026 12:01:14 GMT"},
    {"tx_id": 38642, "title": "Transaction #38642 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38642", "pub_date": "Wed, 18 Nov 2026 12:00:59 GMT"},
    {"tx_id": 38641, "title": "Transaction #38641", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38641", "pub_date": "Wed, 18 Nov 2026 11:17:45 GMT"},
    {"tx_id": 38640, "title": "Transaction #38640", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38640", "pub_date": "Wed, 18 Nov 2026 11:01:34 GMT"},
    {"tx_id": 38639, "title": "Transaction #38639", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38639", "pub_date": "Wed, 18 Nov 2026 11:01:14 GMT"},
    {"tx_id": 38638, "title": "Transaction #38638", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38638", "pub_date": "Wed, 18 Nov 2026 09:12:01 GMT"},
    {"tx_id": 38637, "title": "Transaction #38637", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38637", "pub_date": "Wed, 18 Nov 2026 09:11:47 GMT"},
    {"tx_id": 38636, "title": "Transaction #38636 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38636", "pub_date": "Wed, 18 Nov 2026 08:57:41 GMT"},
    {"tx_id": 38635, "title": "Transaction #38635 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38635", "pub_date": "Tue, 17 Nov 2026 17:02:45 GMT"},
    {"tx_id": 38634, "title": "Transaction #38634 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38634", "pub_date": "Tue, 17 Nov 2026 17:02:37 GMT"},
    {"tx_id": 38633, "title": "Transaction #38633 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38633", "pub_date": "Tue, 17 Nov 2026 17:02:31 GMT"},
    {"tx_id": 38632, "title": "Transaction #38632 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38632", "pub_date": "Tue, 17 Nov 2026 17:02:24 GMT"},
    {"tx_id": 38631, "title": "Transaction #38631 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38631", "pub_date": "Tue, 17 Nov 2026 17:02:15 GMT"},
    {"tx_id": 38630, "title": "Transaction #38630 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38630", "pub_date": "Tue, 17 Nov 2026 17:02:09 GMT"},
    {"tx_id": 38629, "title": "Transaction #38629 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38629", "pub_date": "Tue, 17 Nov 2026 17:02:00 GMT"},
    {"tx_id": 38628, "title": "Transaction #38628 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38628", "pub_date": "Tue, 17 Nov 2026 17:01:53 GMT"},
    {"tx_id": 38627, "title": "Transaction #38627 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38627", "pub_date": "Tue, 17 Nov 2026 17:01:46 GMT"},
    {"tx_id": 38626, "title": "Transaction #38626 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38626", "pub_date": "Tue, 17 Nov 2026 17:01:36 GMT"},
    {"tx_id": 38625, "title": "Transaction #38625 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38625", "pub_date": "Tue, 17 Nov 2026 17:01:30 GMT"},
    {"tx_id": 38624, "title": "Transaction #38624 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38624", "pub_date": "Tue, 17 Nov 2026 17:01:24 GMT"},
    {"tx_id": 38623, "title": "Transaction #38623 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38623", "pub_date": "Tue, 17 Nov 2026 17:01:16 GMT"},
    {"tx_id": 38622, "title": "Transaction #38622 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38622", "pub_date": "Tue, 17 Nov 2026 17:01:09 GMT"},
    {"tx_id": 38621, "title": "Transaction #38621 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38621", "pub_date": "Tue, 17 Nov 2026 17:01:02 GMT"},
    {"tx_id": 38620, "title": "Transaction #38620 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38620", "pub_date": "Tue, 17 Nov 2026 17:00:54 GMT"},
    {"tx_id": 38619, "title": "Transaction #38619 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38619", "pub_date": "Tue, 17 Nov 2026 17:00:46 GMT"},
    {"tx_id": 38618, "title": "Transaction #38618 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38618", "pub_date": "Tue, 17 Nov 2026 17:00:38 GMT"},
    {"tx_id": 38617, "title": "Transaction #38617 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38617", "pub_date": "Tue, 17 Nov 2026 17:00:31 GMT"},
    {"tx_id": 38616, "title": "Transaction #38616 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38616", "pub_date": "Tue, 17 Nov 2026 17:00:25 GMT"},
    {"tx_id": 38615, "title": "Transaction #38615 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38615", "pub_date": "Tue, 17 Nov 2026 17:00:16 GMT"},
    {"tx_id": 38614, "title": "Transaction #38614 Registration", "link": "https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38614", "pub_date": "Tue, 17 Nov 2026 16:01:08 GMT"},
]

MARKERS = {
    "provider_imf_br1": "imf:br1",
    "registered_dataflow_bop6": "imf:bop6(1.0)",
    "payload_dataflow_bop_bpm6": "imf:bop_bpm6(1.0)",
    "bcb_registered_url": "www.bcb.gov.br/content/statistics/sddsdocuments/4 external sector/ext 1 imf sdmx bop bpm6.xml",
}
BCB_URL_LOWER = "https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20external%20sector/ext%201%20imf%20sdmx%20bop%20bpm6.xml".lower()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].split(":")[-1]


def fetch_one(item: dict) -> dict:
    url = item["link"]
    parsed = urllib.parse.urlparse(url)
    q = urllib.parse.parse_qs(parsed.query)
    if parsed.scheme != "https" or parsed.hostname != "sdmxcentral.imf.org":
        return {**item, "http_status": None, "parse_status": "NOT_DONE", "error": "Rejected non-IMF transaction URL"}
    if q.get("txId") != [str(item["tx_id"])]:
        return {**item, "http_status": None, "parse_status": "NOT_DONE", "error": "Transaction ID does not match archived RSS item"}
    req = urllib.request.Request(url, headers={
        "User-Agent": "PRECISION-WIRES-IMF-Registry-Audit/1.0",
        "Accept": "application/xml, text/xml;q=0.9, */*;q=0.1",
    })
    retrieved = dt.datetime.now(dt.timezone.utc).isoformat()
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            body = response.read(12 * 1024 * 1024 + 1)
            if len(body) > 12 * 1024 * 1024:
                raise ValueError("Response exceeds 12 MiB safety cap")
            status = response.status
            content_type = response.headers.get("Content-Type")
            final_url = response.geturl()
        if body:
            (OUT / f"transaction_{item['tx_id']}.xml").write_bytes(body)
        result = {
            **item, "requested_url": url, "final_url": final_url,
            "retrieved_at_utc": retrieved, "http_status": status,
            "content_type": content_type, "byte_count": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
            "parse_status": "NOT_DONE", "request_types": [],
            "matches": [], "registration_candidates": [],
        }
        root = ET.fromstring(body)
        result["parse_status"] = "PASS"
        result["root_element"] = local_name(root.tag)
        text_fragments = []
        request_types = set()
        matches = []
        registrations = []
        for elem in root.iter():
            lname = local_name(elem.tag)
            if lname in ("SubmitRegistrationRequest", "SubmitStructureRequest",
                         "SubmitRegistrationResponse", "SubmitStructureResponse",
                         "QueryRegistrationRequest", "QueryRegistrationResponse",
                         "QueryStructureRequest", "QueryStructureResponse"):
                request_types.add(lname)
            vals = []
            if elem.text and elem.text.strip():
                vals.append(("text", elem.text.strip()))
            vals.extend((f"attr:{k}", v) for k, v in elem.attrib.items() if v)
            for field, value in vals:
                low = value.lower()
                for marker_name, marker in MARKERS.items():
                    if marker in low or (marker_name == "bcb_registered_url" and "www.bcb.gov.br/content/statistics/sddsdocuments" in low):
                        matches.append({
                            "element": lname, "field": field,
                            "value": value[:1200], "marker": marker_name,
                        })
            if lname in ("Registration", "DataRegistration", "ProvisionAgreement",
                         "ProvisionAgreementRef", "DataflowRef", "DataProviderRef",
                         "DataSource", "Datasource", "SimpleDataSource",
                         "QueryableDataSource", "Ref", "StatusMessage"):
                registrations.append({
                    "element": lname, "text": (elem.text or "").strip()[:500],
                    "attributes": dict(elem.attrib),
                })
        result["request_types"] = sorted(request_types)
        result["matches"] = matches[:250]
        result["registration_elements"] = registrations[:500]
        is_registration_result = "QueryRegistrationResponse" in request_types and any(
            entry["element"] == "Registration" for entry in registrations
        )
        has_brazil_marker = any(
            m["marker"] in ("provider_imf_br1", "bcb_registered_url") for m in matches
        )
        result["registration_response_status"] = next(
            (entry["attributes"].get("status") for entry in registrations
             if entry["element"] == "StatusMessage"), None
        )
        result["provision_agreement_urns"] = [
            entry["text"] for entry in registrations if entry["element"] == "ProvisionAgreement"
        ]
        result["datasource_urls"] = [
            entry["text"] for entry in registrations if entry["element"] == "SimpleDataSource"
        ]
        result["brazil_registration_candidate"] = bool(is_registration_result and has_brazil_marker)
        return result
    except Exception as exc:
        return {
            **item, "requested_url": url, "retrieved_at_utc": retrieved,
            "http_status": locals().get("status"), "content_type": locals().get("content_type"),
            "parse_status": "FAIL", "error": repr(exc),
        }


def main() -> None:
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch_one, ITEMS))
    results.sort(key=lambda x: x["tx_id"])
    successful = [x for x in results if x.get("http_status") == 200 and x.get("parse_status") == "PASS"]
    candidates = [x for x in results if x.get("brazil_registration_candidate")]
    matches = [x for x in results if x.get("matches")]
    summary = {
        "scope": "Resolve only the 33 transaction links in the archived IMF RSS response from Run 44301482210",
        "source_rss_run_id": 44301482210,
        "source_rss_artifact_id": 14426565546,
        "source_rss_sha256": "8dcad0ed2f284ad6a3326a031ab81d6a311aa94cb1ab44eb4ad65fa36e3e69a2",
        "transaction_count": len(ITEMS),
        "http_200_and_xml_parse_pass_count": len(successful),
        "transaction_detail_failures": [x for x in results if x not in successful],
        "transactions_with_any_target_marker": [x["tx_id"] for x in matches],
        "query_registration_response_count": sum("QueryRegistrationResponse" in x.get("request_types", []) for x in results),
        "successful_registration_record_count": sum(
            x.get("registration_response_status") == "Success" for x in results
        ),
        "brazil_registration_candidate_tx_ids": [x["tx_id"] for x in candidates],
        "bounded_window_conclusion": (
            "BRAZIL_REGISTRATION_EVENT_FOUND_IN_WINDOW" if candidates
            else "NO_BRAZIL_REGISTRATION_MATCH_IN_THIS_33_TRANSACTION_WINDOW"
            if len(successful) == len(ITEMS)
            else "INCOMPLETE_WINDOW_NO_CONCLUSION"
        ),
        "historical_registration_outside_window": "UNKNOWN",
        "dataflow_registry_compatibility": "BLOCKED_PENDING_AUTHORITATIVE_RESOLUTION",
        "trading_admission": "NOT_AUTHORIZED",
        "started_at_utc": started,
        "completed_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "transactions": results,
    }
    (OUT / "transaction_resolution.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in summary.items() if k != "transactions"}, indent=2, ensure_ascii=False))
    if len(successful) != len(ITEMS):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
