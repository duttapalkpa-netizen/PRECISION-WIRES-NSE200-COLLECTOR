#!/usr/bin/env python3
"""Create an auditable manifest for locally acquired official NSE source files.

This records retrieval time separately from publisher release time. It never
infers publication timestamps or treats an unverified file as official.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def parse_time(value: str, field: str, required: bool = False):
    if not value:
        if required:
            raise ValueError(f"{field} is required")
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{field} must be ISO-8601") from exc
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError(f"{field} must include timezone offset")
    return dt.isoformat()

def inspect_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError(f"empty CSV: {path}")
        norm = [re.sub(r"[^A-Z0-9]", "", x.strip().upper()) for x in header]
        if not header or any(not x for x in norm):
            raise ValueError(f"blank CSV header: {path}")
        if len(norm) != len(set(norm)):
            raise ValueError(f"duplicate normalized CSV headers: {path}")
        rows = sum(1 for _ in reader)
    return {"columns": norm, "record_count": rows}

def build_entry(item, base: Path):
    required = ("name", "path", "source_url", "report_date", "retrieved_at", "content_type")
    missing = [k for k in required if not item.get(k)]
    if missing:
        raise ValueError(f"missing fields for source: {missing}")
    parsed = urlparse(item["source_url"])
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("source_url must be an absolute HTTPS URL")
    try:
        datetime.strptime(item["report_date"], "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("report_date must be YYYY-MM-DD") from exc
    retrieved = parse_time(item["retrieved_at"], "retrieved_at", True)
    published = parse_time(item.get("published_at", ""), "published_at")
    p = Path(item["path"])
    if not p.is_absolute():
        p = base / p
    if not p.is_file():
        raise ValueError(f"source file not found: {p}")
    size = p.stat().st_size
    if size <= 0:
        raise ValueError(f"zero-byte source file: {p}")
    ctype = item["content_type"].split(";")[0].strip().lower()
    if ctype not in {"text/csv", "application/csv", "application/gzip", "application/x-gzip"}:
        raise ValueError(f"unsupported content_type: {ctype}")
    result = {"name": item["name"], "source_url": item["source_url"],
              "report_date": item["report_date"], "published_at": published,
              "retrieved_at": retrieved, "content_type": ctype,
              "path": str(p), "bytes": size, "sha256": sha256(p)}
    if ctype in {"text/csv", "application/csv"}:
        result.update(inspect_csv(p))
    else:
        result["record_count"] = None
        result["columns"] = None
        result["compressed_file_requires_separate_verified_parse"] = True
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="JSON list of source descriptors")
    ap.add_argument("--out", default="outputs/qa/nse_source_provenance_manifest.json")
    args = ap.parse_args()
    input_path = Path(args.input)
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(payload, list) or not payload:
        raise ValueError("input must be a non-empty JSON list")
    entries = [build_entry(x, input_path.parent) for x in payload]
    names = [x["name"] for x in entries]
    if len(names) != len(set(names)):
        raise ValueError("source names must be unique")
    output = {"status": "PASS_SOURCE_FILE_INTEGRITY_METADATA",
              "source_count": len(entries),
              "timestamp_policy": "retrieved_at is collector time; published_at is only recorded when explicitly supplied; no inference",
              "sources": entries}
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": output["status"], "source_count": len(entries),
                      "manifest": str(out), "manifest_sha256": sha256(out)}, indent=2))

if __name__ == "__main__":
    main()
