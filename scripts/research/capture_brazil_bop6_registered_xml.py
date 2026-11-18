#!/usr/bin/env python3
"""Bounded raw capture of the official Brazil BOP6 registered SDMX XML."""
import hashlib, json, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

URL = "https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
OUT = Path("artifacts/brazil_bop6_raw_capture")
OUT.mkdir(parents=True, exist_ok=True)
started = datetime.now(timezone.utc).isoformat()
req = urllib.request.Request(URL, headers={
    "Accept": "application/xml,text/xml,application/vnd.sdmx.structure+xml, */*",
    "User-Agent": "PRECISION-WIRES-research-metadata-audit/1.0"
})
result = {"requested_url": URL, "request_started_at_utc": started, "status": "BLOCKED"}
try:
    with urllib.request.urlopen(req, timeout=20) as response:
        body = response.read()
        headers = dict(response.headers.items())
        result.update({
            "http_status": response.status, "final_url": response.geturl(),
            "response_headers": headers, "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
            "content_type": response.headers.get("Content-Type", ""),
            "byte_length": len(body), "sha256": hashlib.sha256(body).hexdigest()
        })
        if response.status != 200 or not body:
            result["status"] = "FAIL_HTTP_OR_EMPTY"
        else:
            (OUT / "response.xml").write_bytes(body)
            try:
                root = ET.fromstring(body)
                result["xml_parse"] = "PASS"
                result["root_tag"] = root.tag
                result["status"] = "PASS_RAW_CAPTURE_XML_PARSE"
            except ET.ParseError as exc:
                result["xml_parse"] = "FAIL"
                result["xml_error"] = str(exc)
                result["status"] = "FAIL_XML_PARSE"
except Exception as exc:
    result.update({
        "error_type": type(exc).__name__, "error": str(exc),
        "completed_at_utc": datetime.now(timezone.utc).isoformat()
    })
    result["status"] = "BLOCKED_NETWORK_OR_HTTP"
(OUT / "capture_manifest.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2, sort_keys=True))
