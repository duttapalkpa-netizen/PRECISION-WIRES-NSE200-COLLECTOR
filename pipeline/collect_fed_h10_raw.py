#!/usr/bin/env python3
"""Archive the Federal Reserve Board H.10 bulk package unchanged with provenance."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from zipfile import ZipFile, BadZipFile

SOURCE_URL = "https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=h10"
SERIES = {
    "H10/H10/JRXWTFB_N.B": "Nominal Broad Dollar Index",
    "H10/H10/JRXWTFN_N.B": "Nominal Advanced Foreign Economies Dollar Index",
    "H10/H10/JRXWTFO_N.B": "Nominal Emerging Market Economies Dollar Index",
}
MAX_BYTES = 40 * 1024 * 1024


def retrieve(url: str = SOURCE_URL, timeout: int = 45) -> tuple[bytes, str]:
    if not url.startswith("https://www.federalreserve.gov/"):
        raise ValueError("source URL is outside the approved Federal Reserve HTTPS host")
    request = Request(url, headers={"User-Agent": "PRECISION-WIRES-research-archive/1.0"})
    with urlopen(request, timeout=timeout) as response:
        final_url = response.geturl()
        if not final_url.startswith("https://www.federalreserve.gov/"):
            raise ValueError("redirect left the approved Federal Reserve host")
        content_type = response.headers.get("Content-Type", "")
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("H.10 archive exceeds 40 MiB safety limit")
    if not raw.startswith(b"PK\\x03\\x04") or not ZipFile(io.BytesIO(raw)).namelist():
        raise ValueError(f"response is not a valid ZIP archive (Content-Type={content_type!r})")
    return raw, content_type


def archive(output_dir: Path, retrieved_at: datetime | None = None) -> dict:
    raw, content_type = retrieve()
    stamp = (retrieved_at or datetime.now(timezone.utc)).astimezone(timezone.utc)
    stamp_text = stamp.isoformat(timespec="seconds").replace("+00:00", "Z")
    digest = hashlib.sha256(raw).hexdigest()
    day = stamp.strftime("%Y%m%d")
    target_dir = output_dir / day
    target_dir.mkdir(parents=True, exist_ok=True)
    raw_path = target_dir / f"fed_h10_bulk_{stamp.strftime('%H%M%S')}Z_{digest[:12]}.zip"
    manifest_path = raw_path.with_suffix(".manifest.json")
    if raw_path.exists() or manifest_path.exists():
        raise FileExistsError("append-only archive target already exists")
    with ZipFile(io.BytesIO(raw)) as zf:
        members = sorted(zf.namelist())
        if not members or any(name.startswith("/") or ".." in Path(name).parts for name in members):
            raise ValueError("ZIP member list is empty or contains unsafe paths")
        bad_member = zf.testzip()
        if bad_member:
            raise BadZipFile(f"CRC failure in archive member: {bad_member}")
    raw_path.write_bytes(raw)
    manifest = {
        "source": "Board of Governors of the Federal Reserve System",
        "source_class": "OFFICIAL_GOVERNMENT",
        "source_url": SOURCE_URL,
        "retrieved_at_utc": stamp_text,
        "content_type": content_type,
        "archive_file": raw_path.name,
        "archive_bytes": len(raw),
        "sha256": digest,
        "container_format": "ZIP",
        "series": SERIES,
        "series_observation_window_verified_on_2026_11_11": {
            "start": "2006-01-02", "end": "2026-11-06",
            "note": "Federal Reserve DDP package review; refreshed package may extend the end date."
        },
        "zip_members": members,
        "data_type": "PRICE_INDEX",
        "frequency": "DAILY",
        "interpretation_limit": "Dollar indices are FX indices, not capital flows; Fed Broad Dollar is not ICE DXY.",
        "raw_payload_parsed": False,
        "observation_panel_created": False,
        "status": "RAW_ARCHIVE_ONLY_SCHEMA_AND_OBSERVATION_EXTRACTION_PENDING"
    }
    temp = manifest_path.with_suffix(".manifest.json.tmp")
    temp.write_text(json.dumps(manifest, indent=2) + "\\n", encoding="utf-8")
    os.replace(temp, manifest_path)
    return {"status": manifest["status"], "archive": str(raw_path), "manifest": str(manifest_path),
            "bytes": len(raw), "sha256": digest, "series_count": len(SERIES)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="artifacts/raw/fed_h10")
    args = parser.parse_args()
    print(json.dumps(archive(Path(args.output_dir)), indent=2))


if __name__ == "__main__":
    main()
