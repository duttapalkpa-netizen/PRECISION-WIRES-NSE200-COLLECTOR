#!/usr/bin/env python3
"""Read-only capture of official IMF SDMX Central RSS transaction archive."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import hashlib, json, xml.etree.ElementTree as ET

URL = "https://sdmxcentral.imf.org/rss.xml"
OUT = Path("imf_brazil_rss_transaction_archive")
OUT.mkdir(parents=True, exist_ok=True)
retrieved = datetime.now(timezone.utc).isoformat()
req = Request(URL, headers={"User-Agent":"PRECISION-WIRES-independent-audit/1.6","Accept":"application/rss+xml, application/xml, text/xml, */*"})
try:
    with urlopen(req, timeout=20) as response:
        status, headers, raw = response.status, dict(response.headers.items()), response.read(5_000_001)
except HTTPError as exc:
    status, headers, raw = exc.code, dict(exc.headers.items()) if exc.headers else {}, exc.read(5_000_001)
except (URLError, TimeoutError) as exc:
    status, headers, raw = 0, {}, str(exc).encode()
if len(raw) > 5_000_000:
    raise SystemExit("RSS exceeds 5 MB safety cap; preserve as bounded failure, do not parse truncated feed")
(OUT/"imf_sdmxcentral_rss_raw.xml").write_bytes(raw)
safe_headers = {k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
result = {"url":URL,"retrieved_at_utc":retrieved,"http_status":status,"headers":safe_headers,
          "byte_count":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"entries":[]}
if status == 200:
    try:
        root = ET.fromstring(raw)
        for item in root.findall(".//item"):
            fields = {}
            for child in list(item):
                key = child.tag.split("}")[-1]
                fields[key] = (child.text or "").strip()
            haystack = " ".join(str(v) for v in fields.values()).lower()
            if any(term in haystack for term in ("br_bop_bp6","bop6","bop_bpm6","brazil","transaction id 2","txid=2","tx id 2")):
                fields["matched_terms"] = [term for term in ("br_bop_bp6","bop6","bop_bpm6","brazil","transaction id 2","txid=2","tx id 2") if term in haystack]
                result["entries"].append(fields)
        result["feed_entry_count"] = len(root.findall(".//item"))
        result["matched_entry_count"] = len(result["entries"])
        result["xml_parse_status"] = "PASS"
    except Exception as exc:
        result["xml_parse_status"] = "FAIL"
        result["xml_parse_error"] = str(exc)
else:
    result["xml_parse_status"] = "NOT_RUN_HTTP_FAILURE"
(OUT/"manifest.json").write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2, ensure_ascii=False))
