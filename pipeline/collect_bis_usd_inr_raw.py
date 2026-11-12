#!/usr/bin/env python3
"""Archive the official BIS daily USD/INR SDMX-CSV series unchanged."""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

SOURCE_URL = "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_XRU/1.0/D.IN.INR.A?format=csv"
APPROVED_HOST = "stats.bis.org"
MAX_BYTES = 10 * 1024 * 1024
SERIES = "D.IN.INR.A"
DATAFLOW = "BIS,WS_XRU,1.0"


def _approved(url: str) -> bool:
    try:
        p = urlsplit(url)
        port = p.port
    except (TypeError, ValueError):
        return False
    return (
        p.scheme.lower() == "https"
        and p.hostname is not None
        and p.hostname.lower() == APPROVED_HOST
        and port in (None, 443)
        and p.username is None
        and p.password is None
    )


def retrieve(url: str = SOURCE_URL, timeout: int = 45) -> tuple[bytes, str, str]:
    if not _approved(url):
        raise ValueError("BIS source URL is outside the approved HTTPS origin")
    request = Request(url, headers={"User-Agent": "PRECISION-WIRES-research-archive/1.0", "Accept": "text/csv"})
    with urlopen(request, timeout=timeout) as response:
        final_url = response.geturl()
        if not _approved(final_url):
            raise ValueError("BIS redirect left the approved HTTPS origin")
        content_type = response.headers.get("Content-Type", "")
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("BIS USD/INR response exceeds 10 MiB safety limit")
    try:
        decoded = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("BIS CSV response is not UTF-8") from exc
    if not decoded.strip():
        raise ValueError("BIS CSV response is empty")
    reader = csv.reader(io.StringIO(decoded))
    first = next(reader, [])
    if not first or "OBS_VALUE" not in first or "TIME_PERIOD" not in first:
        raise ValueError(f"BIS response does not have expected SDMX-CSV columns: {first[:20]}")
    return raw, content_type, final_url


def archive(output_dir: Path, retrieved_at: datetime | None = None) -> dict:
    raw, content_type, final_url = retrieve()
    stamp = (retrieved_at or datetime.now(timezone.utc)).astimezone(timezone.utc)
    stamp_text = stamp.isoformat(timespec="seconds").replace("+00:00", "Z")
    digest = hashlib.sha256(raw).hexdigest()
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_path = output_dir / f"bis_usd_inr_daily_{stamp.strftime('%Y%m%dT%H%M%SZ')}_{digest[:12]}.csv"
    manifest_path = raw_path.with_suffix(".manifest.json")
    if raw_path.exists() or manifest_path.exists():
        raise FileExistsError("append-only BIS archive target already exists")
    raw_path.write_bytes(raw)
    manifest = {
        "source": "Bank for International Settlements",
        "source_class": "OFFICIAL_INTERNATIONAL_ORGANIZATION",
        "source_url": SOURCE_URL,
        "final_url": final_url,
        "retrieved_at_utc": stamp_text,
        "content_type": content_type,
        "archive_file": raw_path.name,
        "archive_bytes": len(raw),
        "sha256": digest,
        "dataflow": DATAFLOW,
        "series": SERIES,
        "frequency": "DAILY_BUSINESS_DAY",
        "quotation": "Indian rupees per US dollar",
        "interpretation_limit": "BIS reference exchange rate series; not a transaction execution price.",
        "raw_payload_parsed": False,
        "status": "RAW_CSV_ARCHIVED_PARSE_AND_CALENDAR_RECONCILIATION_PENDING",
        "attribution": "Source: Bank for International Settlements (BIS), WS_XRU. Cite BIS in any reproduced output."
    }
    temp = manifest_path.with_suffix(".manifest.json.tmp")
    temp.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, manifest_path)
    return {"status": manifest["status"], "archive": str(raw_path), "manifest": str(manifest_path), "bytes": len(raw), "sha256": digest, "series": SERIES}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output-dir", default="artifacts/raw/bis_usd_inr")
    args = p.parse_args()
    print(json.dumps(archive(Path(args.output_dir)), indent=2))


if __name__ == "__main__":
    main()
