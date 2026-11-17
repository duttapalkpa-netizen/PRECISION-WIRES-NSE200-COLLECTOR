#!/usr/bin/env python3
"""Compare current official BCB SGS JSON observations with immutable 15-series archive.

Research-only, read-only inputs. Fetches the official BCData/SGS API; it does not
change production selectors, scoring, raw archive files, or source admission.
"""
from __future__ import annotations
import csv, hashlib, json, os, sys, urllib.request
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFESTS = [
    ROOT / "data/raw/bcb/priority_series_capture_20261117/manifest.json",
    ROOT / "data/raw/bcb/instrument_net_capture_20261117/manifest.json",
]
EXPECTED_CODES = {
    "22905","22906","22907","22908","22924","22925","22926",
    "22909","22912","22915","22927","22936","22939","22942","22945",
}
FOCUS = {"22905","22930","22936","22942"}  # 22930 is a comparison series, loaded only if archived manifest contains it
API = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json"

def period_from_date(value: str) -> str:
    dd, mm, yyyy = value.split("/")
    return f"{yyyy}-{mm}"

def decimal_value(value: str) -> Decimal:
    return Decimal(str(value).replace(",", "."))

def read_archive(path: Path):
    raw = path.read_bytes()
    rows = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            date = (row.get('"data"') or row.get("data") or "").strip('"')
            value = (row.get('"valor"') or row.get("valor") or "").strip('"')
            if not date or not value:
                raise ValueError(f"blank archived observation: {path}")
            period = period_from_date(date)
            if period in rows:
                raise ValueError(f"duplicate archive period {period}: {path}")
            rows[period] = decimal_value(value)
    if not rows:
        raise ValueError(f"empty archived series: {path}")
    return raw, rows

def fetch_live(code: str):
    url = API.format(code=code)
    req = urllib.request.Request(url, headers={"User-Agent":"PRECISION-WIRES-research-audit/1.0","Accept":"application/json"})
    with urllib.request.urlopen(req, timeout=35) as response:
        status = response.status
        body = response.read()
        headers = dict(response.headers.items())
    if status != 200:
        raise RuntimeError(f"SGS {code}: HTTP {status}")
    payload = json.loads(body.decode("utf-8"))
    if not isinstance(payload, list) or not payload:
        raise RuntimeError(f"SGS {code}: empty or invalid JSON array")
    rows = {}
    for item in payload:
        period = period_from_date(item["data"])
        value = decimal_value(item["valor"])
        if period in rows:
            raise RuntimeError(f"SGS {code}: duplicate live period {period}")
        rows[period] = value
    ordered = list(rows)
    if ordered != sorted(ordered):
        raise RuntimeError(f"SGS {code}: non-ascending live observations")
    return url, body, headers, rows

def main():
    started = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00","Z")
    manifests, manifest_hashes, entries = {}, {}, {}
    for mp in MANIFESTS:
        raw = mp.read_bytes()
        manifest_hashes[str(mp.relative_to(ROOT))] = hashlib.sha256(raw).hexdigest()
        obj = json.loads(raw)
        if not str(obj.get("status","")).startswith("RAW_CAPTURE_"):
            raise RuntimeError(f"non-PASS raw capture manifest: {mp}")
        for code, meta in obj["series"].items():
            if code in entries:
                raise RuntimeError(f"duplicate series {code} across manifests")
            entries[code] = meta
    if not EXPECTED_CODES.issubset(entries):
        raise RuntimeError(f"missing archived series: {sorted(EXPECTED_CODES-set(entries))}")

    result = {
        "schema_version": 1,
        "purpose": "official_BCB_SGS_live_vs_immutable_archived_15_series_revision_detection",
        "capture_started_utc": started,
        "provider": "Banco Central do Brasil / BCData SGS",
        "api_pattern": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json",
        "archive_manifests_sha256": manifest_hashes,
        "series": {},
        "summary": {},
        "production_integration": "NOT_AUTHORIZED",
        "limitations": [
            "Current API observations are a current snapshot, not an as-published historical vintage.",
            "A difference detects snapshot change only; it does not identify revision date, reason, or responsible source.",
            "No source data are written back to or used to overwrite the immutable archive."
        ]
    }
    total_overlap = 0
    total_changed = 0
    failures = []
    for code in sorted(EXPECTED_CODES):
        meta = entries[code]
        rel = meta.get("path") or meta.get("relative_path")
        if not rel:
            raise RuntimeError(f"manifest lacks raw path for SGS {code}")
        archive_path = ROOT / rel
        archive_raw, archived = read_archive(archive_path)
        archive_sha = hashlib.sha256(archive_raw).hexdigest()
        if archive_sha != meta["sha256"] or len(archive_raw) != meta["byte_length"]:
            raise RuntimeError(f"archived raw integrity mismatch SGS {code}")
        url, body, headers, live = fetch_live(code)
        overlap = sorted(set(archived) & set(live))
        changed = [{"period":p,"archived":str(archived[p]),"live":str(live[p]),
                    "delta_live_minus_archive":str(live[p]-archived[p])}
                   for p in overlap if archived[p] != live[p]]
        total_overlap += len(overlap)
        total_changed += len(changed)
        feb = {"archived":str(archived["2026-02"]) if "2026-02" in archived else None,
               "live":str(live["2026-02"]) if "2026-02" in live else None}
        if feb["archived"] is not None and feb["live"] is not None:
            feb["delta_live_minus_archive"] = str(Decimal(feb["live"])-Decimal(feb["archived"]))
        result["series"][code] = {
            "source_url":url,"http_status":200,"response_bytes":len(body),
            "response_sha256":hashlib.sha256(body).hexdigest(),
            "etag":headers.get("ETag"),"last_modified":headers.get("Last-Modified"),
            "archived_path":rel,"archive_bytes":len(archive_raw),"archive_sha256":archive_sha,
            "archive_rows":len(archived),"live_rows":len(live),
            "archive_first":next(iter(archived)),"archive_last":next(reversed(archived)),
            "live_first":next(iter(live)),"live_last":next(reversed(live)),
            "overlap_rows":len(overlap),"changed_overlap_count":len(changed),
            "february_2026":feb,"changed_observations":changed
        }
    result["summary"] = {
        "series_count":len(result["series"]),
        "overlapping_series_month_observations":total_overlap,
        "changed_series_month_observations":total_changed,
        "unchanged_series_month_observations":total_overlap-total_changed,
        "result":"NO_DIFFERENCES_IN_OVERLAP" if total_changed==0 else "LIVE_ARCHIVE_DIFFERENCES_DETECTED",
        "feb_2026_sgs_22942_status":result["series"]["22942"]["february_2026"],
        "interpretation":"SNAPSHOT_COMPARISON_ONLY_NO_REVISION_CAUSE_ATTRIBUTION"
    }
    out = ROOT / "data/qa/BCB_SGS_LIVE_VS_ARCHIVED_15_SERIES_20261118.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(result["summary"],indent=2,ensure_ascii=False))
    print(f"QA_OUTPUT={out}")
    if len(result["series"]) != len(EXPECTED_CODES):
        raise SystemExit("incomplete live series coverage")
    if total_overlap == 0:
        raise SystemExit("no common archived/live observations")
if __name__ == "__main__":
    main()
