#!/usr/bin/env python3
"""Capture official U.S. Treasury daily nominal and real par-yield XML histories.

Research-only. Raw pages are retained before parsing. No imputation, forward-fill,
synthetic observations, or source promotion occurs here.
"""
from __future__ import annotations
import csv, datetime as dt, hashlib, json, pathlib, re, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path("treasury_macro_evidence")
RAW = ROOT / "raw"
RAW.mkdir(parents=True, exist_ok=True)
BASE = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml"
FEEDS = {
    "nominal": "daily_treasury_yield_curve",
    "real": "daily_treasury_real_yield_curve",
}
MAX_PAGES = 100
TIMEOUT = 30

def lname(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].split(":")[-1]

def digest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def fetch_page(feed_key: str, page: int) -> tuple[bytes, dict]:
    query = urllib.parse.urlencode({
        "data": FEEDS[feed_key], "field_tdr_date_value": "all", "page": str(page)
    })
    url = BASE + "?" + query
    req = urllib.request.Request(url, headers={
        "User-Agent": "PRECISION-WIRES-Treasury-Research-Capture/1.0",
        "Accept": "application/xml,text/xml;q=0.9,*/*;q=0.1",
    })
    with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
        body = response.read(32 * 1024 * 1024 + 1)
        if len(body) > 32 * 1024 * 1024:
            raise ValueError("Treasury XML page exceeds 32 MiB safety cap")
        meta = {
            "requested_url": url,
            "final_url": response.geturl(),
            "http_status": response.status,
            "content_type": response.headers.get("Content-Type"),
            "content_length_header": response.headers.get("Content-Length"),
            "retrieved_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "byte_count": len(body),
            "sha256": digest(body),
        }
    return body, meta

def parse_page(body: bytes) -> list[dict[str, str]]:
    root = ET.fromstring(body)
    rows = []
    for entry in root.iter():
        if lname(entry.tag) != "entry":
            continue
        props = {}
        for child in entry.iter():
            name = lname(child.tag)
            if name in ("properties",):
                for field in child:
                    props[lname(field.tag)] = (field.text or "").strip()
        if props:
            rows.append(props)
    return rows

def normalize_date(raw: str) -> str:
    # Treasury OData commonly emits datetime'YYYY-MM-DDT00:00:00'.
    m = re.search(r"(\d{4}-\d{2}-\d{2})", raw)
    if not m:
        raise ValueError(f"Cannot parse Treasury observation date: {raw!r}")
    return dt.date.fromisoformat(m.group(1)).isoformat()

def validate_and_write(feed_key: str, rows: list[dict[str, str]]) -> dict:
    if not rows:
        raise ValueError(f"No observations acquired for {feed_key}")
    all_fields = sorted({k for row in rows for k in row})
    date_fields = [k for k in all_fields if k.upper() in {"NEW_DATE", "DATE", "OBS_DATE"} or k.upper().endswith("_DATE")]
    if len(date_fields) != 1:
        raise ValueError(f"Expected exactly one date field; found {date_fields}")
    date_field = date_fields[0]
    seen = set()
    normalized = []
    for row in rows:
        if date_field not in row or not row[date_field]:
            raise ValueError("Missing observation date")
        date = normalize_date(row[date_field])
        if date in seen:
            raise ValueError(f"Duplicate observation date {date} in {feed_key}")
        seen.add(date)
        out = {"date": date}
        for key in all_fields:
            if key == date_field:
                continue
            value = row.get(key, "")
            if value.lower() in {"null", "none"}:
                value = ""
            if value:
                # Verify numeric values without changing the original lexical value.
                try:
                    number = float(value.rstrip("mMdDfF"))
                except ValueError:
                    raise ValueError(f"Non-numeric Treasury yield field {key}={value!r}")
                if number != number or number in (float("inf"), float("-inf")):
                    raise ValueError(f"Non-finite Treasury value {key}={value!r}")
            out[key] = value
        normalized.append(out)
    normalized.sort(key=lambda r: r["date"])
    fields = ["date"] + [k for k in all_fields if k != date_field]
    path = ROOT / f"treasury_{feed_key}_yield_curve.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(normalized)
    return {
        "feed_key": feed_key,
        "data_key": FEEDS[feed_key],
        "date_field": date_field,
        "columns": fields,
        "row_count": len(normalized),
        "first_date": normalized[0]["date"],
        "last_date": normalized[-1]["date"],
        "duplicate_date_count": 0,
        "csv_path": str(path),
        "csv_bytes": path.stat().st_size,
        "csv_sha256": digest(path.read_bytes()),
        "status": "PASS",
    }

def main() -> None:
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    manifest = {"source": "U.S. Department of the Treasury Daily Interest Rate XML Feed",
                "started_at_utc": started, "feeds": {}, "guardrails": {
                    "no_forward_fill": True, "no_imputation": True,
                    "no_synthetic_observations": True, "research_only": True}}
    summaries = []
    for feed_key in FEEDS:
        pages, rows, page_no = [], [], 0
        while page_no < MAX_PAGES:
            body, meta = fetch_page(feed_key, page_no)
            page_path = RAW / f"{feed_key}_page_{page_no:03d}.xml"
            page_path.write_bytes(body)
            meta.update({"feed_key": feed_key, "page": page_no,
                         "raw_path": str(page_path), "raw_sha256_recomputed": digest(page_path.read_bytes())})
            if meta["http_status"] != 200:
                raise RuntimeError(f"HTTP {meta['http_status']} for {meta['requested_url']}")
            page_rows = parse_page(body)
            meta["entry_count"] = len(page_rows)
            pages.append(meta)
            if not page_rows:
                break
            rows.extend(page_rows)
            page_no += 1
            time.sleep(0.15)
        else:
            raise RuntimeError(f"Pagination exceeded {MAX_PAGES} pages for {feed_key}")
        if not pages or pages[-1]["entry_count"] != 0:
            raise RuntimeError(f"Missing explicit empty-page pagination terminator for {feed_key}")
        summary = validate_and_write(feed_key, rows)
        summary["pages_including_empty_terminator"] = len(pages)
        summary["raw_page_entries"] = sum(p["entry_count"] for p in pages)
        manifest["feeds"][feed_key] = {"pages": pages, "summary": summary}
        summaries.append(summary)
    manifest["completed_at_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2)+"\n", encoding="utf-8")
    (ROOT / "summary.json").write_text(json.dumps({"status":"PASS","feeds":summaries}, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status":"PASS","feeds":summaries,
                      "manifest_sha256":digest((ROOT/"manifest.json").read_bytes())}, indent=2))

if __name__ == "__main__":
    main()
