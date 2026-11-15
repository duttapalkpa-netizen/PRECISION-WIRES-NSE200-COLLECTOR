#!/usr/bin/env python3
"""Acquire the official MoSPI NIC-2025 PDF and produce a provenance-preserving text extract.

No synthetic rows are generated. The PDF is archived locally with SHA-256;
pdftotext is used only for pages 256-262 (printed pages 232-238).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

SOURCE_URL = "https://www.mospi.gov.in/sites/default/files/main_menu/national_industrial_classification/NIC_2025Final_18112025.pdf"
ALLOWED_HOSTS = {"mospi.gov.in", "www.mospi.gov.in", "new.mospi.gov.in"}
PDF_FIRST_PAGE = 256
PDF_LAST_PAGE = 262


def acquire_pdf(destination: Path, timeout: int = 45) -> dict:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = Request(SOURCE_URL, headers={"User-Agent": "PRECISION-WIRES-NIC-research/1.0"})
    digest = hashlib.sha256()
    size = 0
    with urlopen(request, timeout=timeout) as response:
        final_url = response.geturl()
        host = (urlparse(final_url).hostname or "").lower()
        if host not in ALLOWED_HOSTS:
            raise ValueError(f"Unexpected redirect host: {host}")
        content_type = response.headers.get("Content-Type", "").split(";")[0].strip().lower()
        if content_type not in {"application/pdf", "application/octet-stream"}:
            raise ValueError(f"Unexpected content type: {content_type}")
        with tempfile.NamedTemporaryFile(dir=destination.parent, prefix=".nic2025-", delete=False) as tmp:
            temp_path = Path(tmp.name)
            first = response.read(8)
            if not first.startswith(b"%PDF-"):
                raise ValueError("Downloaded payload does not have a PDF signature")
            tmp.write(first)
            digest.update(first)
            size += len(first)
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                tmp.write(chunk)
                digest.update(chunk)
                size += len(chunk)
    if size < 100_000:
        temp_path.unlink(missing_ok=True)
        raise ValueError(f"PDF payload unexpectedly small: {size} bytes")
    temp_path.replace(destination)
    return {
        "source_url": SOURCE_URL,
        "final_url": final_url,
        "content_type": content_type,
        "bytes": size,
        "sha256": digest.hexdigest(),
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "archive_file": destination.name,
    }


def extract_pages(pdf_path: Path, text_path: Path) -> dict:
    result = subprocess.run(
        ["pdftotext", "-layout", "-f", str(PDF_FIRST_PAGE), "-l", str(PDF_LAST_PAGE), str(pdf_path), "-"],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    pages = result.stdout.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    expected_pages = PDF_LAST_PAGE - PDF_FIRST_PAGE + 1
    if len(pages) != expected_pages:
        raise ValueError(f"Expected {expected_pages} extracted pages, got {len(pages)}")
    out_lines = []
    source_line = 1
    for offset, page_text in enumerate(pages):
        pdf_page = PDF_FIRST_PAGE + offset
        for line in page_text.splitlines():
            out_lines.append(f"L{source_line}@P{pdf_page}: {line.rstrip()}")
            source_line += 1
    text_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    return {
        "pdf_page_start": PDF_FIRST_PAGE,
        "pdf_page_end": PDF_LAST_PAGE,
        "extracted_page_count": len(pages),
        "text_line_count": len(out_lines),
        "text_file": text_path.name,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", type=Path, default=Path("nic_concordance_source"))
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = args.out_dir / "NIC_2025Final_18112025.pdf"
    text_path = args.out_dir / "nic2025_concordance_pages_256_262.txt"
    manifest_path = args.out_dir / "source_manifest.json"
    manifest = acquire_pdf(pdf_path)
    manifest.update(extract_pages(pdf_path, text_path))
    manifest["status"] = "SOURCE_ACQUIRED_AND_TEXT_EXTRACTED_NOT_YET_PARSER_ACCEPTED"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
