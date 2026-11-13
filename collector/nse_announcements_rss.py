#!/usr/bin/env python3
"""Bounded, raw-first NSE announcements RSS acquisition. Standard library only."""
from __future__ import annotations
import hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import xml.etree.ElementTree as ET

SOURCE_URL = "https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml"
OUT = Path("outputs/corporate_events/rss")
MAX_BYTES = 10 * 1024 * 1024
TIMEOUT_SECONDS = 15

def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

def local_name(tag):
    return tag.rsplit("}", 1)[-1].lower()

def child_text(node, wanted):
    for child in list(node):
        if local_name(child.tag) == wanted:
            return "".join(child.itertext())
    return None

def parse_rss(raw: bytes):
    if re.search(br"<!\s*(DOCTYPE|ENTITY)\b", raw, flags=re.IGNORECASE):
        raise ValueError("DTD_OR_ENTITY_DECLARATION_REJECTED")
    root = ET.fromstring(raw)
    if local_name(root.tag) != "rss":
        raise ValueError("UNEXPECTED_XML_ROOT:" + local_name(root.tag))
    channel = next((x for x in list(root) if local_name(x.tag) == "channel"), None)
    if channel is None:
        raise ValueError("RSS_CHANNEL_MISSING")
    items = []
    for node in list(channel):
        if local_name(node.tag) != "item":
            continue
        guid_node = next((x for x in list(node) if local_name(x.tag) == "guid"), None)
        items.append({
            "title": child_text(node, "title"),
            "link": child_text(node, "link"),
            "guid": child_text(node, "guid"),
            "guid_is_permalink": (guid_node.attrib.get("isPermaLink") if guid_node is not None else None),
            "pubDate_original": child_text(node, "pubdate"),
            "description_original": child_text(node, "description"),
            "raw_item_xml": ET.tostring(node, encoding="unicode"),
        })
    return items

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "source": "NSE official Announcements RSS",
        "requested_url": SOURCE_URL,
        "retrieved_at_utc_start": utc_now(),
        "retrieved_at_utc_end": None,
        "http_status": None, "final_url": None, "content_type": None,
        "byte_count": 0, "sha256": None, "artifact_path": None,
        "item_count": None, "parse_status": "NOT_RUN", "acquisition_status": "FAILED",
        "error": None, "timeout_seconds": TIMEOUT_SECONDS, "max_bytes": MAX_BYTES,
        "synthetic_data": False,
    }
    try:
        req = Request(SOURCE_URL, headers={
            "User-Agent": "PRECISION-WIRES-NSE200-COLLECTOR/1.0 (read-only research)",
            "Accept": "application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.1",
        })
        with urlopen(req, timeout=TIMEOUT_SECONDS) as response:
            status, final_url = response.status, response.geturl()
            content_type = response.headers.get("Content-Type")
            raw = response.read(MAX_BYTES + 1)
        manifest.update(http_status=status, final_url=final_url, content_type=content_type)
        if len(raw) > MAX_BYTES:
            raise ValueError("RESPONSE_EXCEEDS_10MiB_LIMIT")
        if status < 200 or status >= 300:
            raise ValueError("HTTP_STATUS_NOT_SUCCESS:" + str(status))
        raw_path = OUT / "announcements.xml"
        raw_path.write_bytes(raw)
        manifest.update(byte_count=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
                        artifact_path=str(raw_path), acquisition_status="ACQUIRED")
        items = parse_rss(raw)
        jsonl_path = OUT / "announcements.jsonl"
        with jsonl_path.open("w", encoding="utf-8", newline="\n") as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")
        guids = [x["guid"] for x in items if x["guid"]]
        manifest.update(item_count=len(items), parse_status="PASS",
                        parsed_artifact_path=str(jsonl_path), guid_count=len(guids),
                        duplicate_guid_values=sorted({g for g in guids if guids.count(g) > 1}),
                        items_without_guid=sum(1 for x in items if not x["guid"]),
                        pubDate_original_values=[x["pubDate_original"] for x in items])
    except HTTPError as exc:
        manifest.update(http_status=exc.code, final_url=exc.geturl(), error="HTTP_ERROR:" + str(exc))
    except (URLError, TimeoutError, OSError, ValueError, ET.ParseError) as exc:
        manifest["error"] = type(exc).__name__ + ":" + str(exc)
        if isinstance(exc, ET.ParseError) or manifest["acquisition_status"] == "ACQUIRED":
            manifest["parse_status"] = "FAIL"
    finally:
        manifest["retrieved_at_utc_end"] = utc_now()
        (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: manifest.get(k) for k in ("acquisition_status","http_status","final_url","byte_count","sha256","item_count","parse_status","error")}, ensure_ascii=False))
    return 0 if manifest["acquisition_status"] == "ACQUIRED" and manifest["parse_status"] == "PASS" else 2

if __name__ == "__main__":
    sys.exit(main())
