#!/usr/bin/env python3
"""Crosswalk a cache-only NSE snapshot to an exact prior source-verified snapshot."""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

APPROVED_HOSTS = {"nsearchives.nseindia.com", "archives.nseindia.com"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest(root: Path) -> tuple[Path, dict]:
    candidates = sorted(root.rglob("nse_snapshot_manifest_*.json"))
    if len(candidates) != 1:
        raise ValueError(f"expected exactly one NSE snapshot manifest in {root}, found {len(candidates)}")
    path = candidates[0]
    return path, json.loads(path.read_text(encoding="utf-8"))


def validate_record_file(root: Path, record: dict, label: str) -> Path:
    filename = record.get("file")
    if not isinstance(filename, str) or Path(filename).name != filename:
        raise ValueError(f"{label}: unsafe or missing manifest filename")
    matches = list(root.rglob(filename))
    if len(matches) != 1:
        raise ValueError(f"{label}: expected one file {filename}, found {len(matches)}")
    path = matches[0]
    if path.stat().st_size != int(record.get("bytes", -1)):
        raise ValueError(f"{label}: byte-size mismatch for {filename}")
    digest = sha256(path)
    if digest != record.get("sha256"):
        raise ValueError(f"{label}: SHA-256 mismatch for {filename}")
    return path


def verify_reference_record(record: dict) -> dict:
    if record.get("acquisition_status") != "OK_FULL_BHAVCOPY_DELIVERY":
        raise ValueError(f"reference record is not a successful Full Bhavcopy delivery: {record.get('trade_date')}")
    if record.get("cache_origin") != "network":
        raise ValueError(f"reference record was not acquired from network: {record.get('trade_date')}")
    url = record.get("source_url")
    from urllib.parse import urlsplit
    parsed = urlsplit(url or "")
    if parsed.scheme != "https" or parsed.hostname not in APPROVED_HOSTS:
        raise ValueError(f"reference source URL is not an approved official NSE host: {url!r}")
    response = record.get("successful_response")
    if not isinstance(response, dict):
        raise ValueError(f"missing successful response evidence: {record.get('trade_date')}")
    if response.get("url") != url or response.get("http_status") != 200 or response.get("error") is not None:
        raise ValueError(f"successful response URL/status mismatch: {record.get('trade_date')}")
    if response.get("response_sha256") != record.get("sha256"):
        raise ValueError(f"response hash does not match normalized source file hash: {record.get('trade_date')}")
    if response.get("bytes") != record.get("bytes"):
        raise ValueError(f"response byte count does not match source file: {record.get('trade_date')}")
    retrieved = response.get("retrieved_at_utc")
    if not isinstance(retrieved, str) or not retrieved.endswith("+00:00"):
        raise ValueError(f"missing explicit UTC network retrieval timestamp: {record.get('trade_date')}")
    return response


def reconcile(reference_dir: Path, candidate_dir: Path, output_dir: Path) -> dict:
    ref_path, ref = load_manifest(reference_dir)
    cand_path, cand = load_manifest(candidate_dir)
    for label, manifest in (("reference", ref), ("candidate", cand)):
        if manifest.get("expected_sessions") != 200 or manifest.get("actual_sessions") != 200 or len(manifest.get("records", [])) != 200:
            raise ValueError(f"{label} manifest is not exactly 200 sessions")
    ref_records = {x.get("trade_date"): x for x in ref["records"]}
    cand_records = {x.get("trade_date"): x for x in cand["records"]}
    if len(ref_records) != 200 or len(cand_records) != 200:
        raise ValueError("duplicate or missing trade_date keys in one of the manifests")
    if set(ref_records) != set(cand_records):
        missing = sorted(set(ref_records) - set(cand_records))
        extra = sorted(set(cand_records) - set(ref_records))
        raise ValueError(f"snapshot date sets differ; missing={missing[:5]}, extra={extra[:5]}")

    crosswalk = []
    for trade_date in sorted(ref_records):
        rr, cr = ref_records[trade_date], cand_records[trade_date]
        if rr.get("file") != cr.get("file") or rr.get("bytes") != cr.get("bytes") or rr.get("sha256") != cr.get("sha256"):
            raise ValueError(f"reference/candidate record metadata differs for {trade_date}")
        if rr.get("schema_validation") != "validated" or cr.get("schema_validation") != "validated":
            raise ValueError(f"schema validation is not PASS for {trade_date}")
        validate_record_file(reference_dir, rr, "reference")
        validate_record_file(candidate_dir, cr, "candidate")
        response = verify_reference_record(rr)
        if cr.get("acquisition_status") != "CACHED":
            raise ValueError(f"candidate snapshot was expected to be cache-only for {trade_date}")
        if cr.get("source_url") is not None or cr.get("successful_response") is not None:
            raise ValueError(f"candidate cache record unexpectedly claims direct source retrieval: {trade_date}")
        crosswalk.append({
            "trade_date": trade_date,
            "file": rr["file"],
            "bytes": rr["bytes"],
            "sha256": rr["sha256"],
            "schema_validation": "PASS_IN_BOTH_SNAPSHOTS",
            "candidate_acquisition_status": "CACHED",
            "source_evidence_origin": "EXACT_HASH_MATCH_TO_REFERENCE_NETWORK_SNAPSHOT",
            "official_source_url": rr["source_url"],
            "http_status": response["http_status"],
            "reference_network_retrieved_at_utc": response["retrieved_at_utc"],
            "response_sha256": response["response_sha256"],
        })

    output_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "schema_version": 1,
        "status": "PASS_CONTENT_IDENTICAL_TO_PREVIOUSLY_SOURCE_VERIFIED_SNAPSHOT",
        "audit_created_at_utc": datetime.now(timezone.utc).isoformat(),
        "reference_snapshot": {
            "snapshot_id": ref["snapshot_id"],
            "manifest": ref_path.name,
            "manifest_sha256": sha256(ref_path),
            "run_id": 43245527846,
            "artifact_id": 13955899352,
            "artifact_sha256": "1833c75c09c89e7610ad3fbdff62bbdf9a67737e2b39c1e4bf223bddc3a1e070",
            "acquisition_status": "200_OF_200_OFFICIAL_NSE_NETWORK_RESPONSES_VERIFIED",
        },
        "candidate_snapshot": {
            "snapshot_id": cand["snapshot_id"],
            "manifest": cand_path.name,
            "manifest_sha256": sha256(cand_path),
            "run_id": 43248356512,
            "artifact_id": 13957867109,
            "artifact_sha256": "74923fac8aacb60ac82fba0bd955cae018847adae08294babfec1daf5d7375c0",
            "acquisition_status": "200_OF_200_PREEXISTING_CACHE_FILES_SCHEMA_AND_HASH_VALIDATED",
            "direct_source_retrieval_claimed": False,
        },
        "reconciliation": {
            "expected_sessions": 200,
            "matched_trade_dates": 200,
            "identical_file_names": 200,
            "identical_byte_counts": 200,
            "identical_content_sha256": 200,
            "reference_official_http_200_records": 200,
            "reference_source_url_records": 200,
            "reference_network_retrieval_timestamps": 200,
            "candidate_schema_validated_records": 200,
            "candidate_cache_records_crosswalked": 200,
            "unmatched_records": 0,
        },
        "timestamp_semantics": "reference_network_retrieved_at_utc is copied only from the earlier exact-hash-matched official network evidence. Candidate file mtime and candidate retrieved_at_utc are not treated as original network retrieval or publication timestamps.",
        "provenance_policy": "The candidate run did not itself retrieve the 200 files. Provenance is inherited only through exact trade-date, filename, byte-count and SHA-256 identity with the independently source-verified reference artifact. No new source retrieval is claimed.",
        "production_integration": "NOT_AUTHORIZED",
        "records": crosswalk,
    }
    out = output_dir / "nse_200_session_provenance_crosswalk.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    digest = sha256(out)
    (output_dir / "nse_200_session_provenance_crosswalk.sha256").write_text(
        f"{digest}  {out.name}\n", encoding="utf-8"
    )
    report["report_file"] = out.name
    report["report_sha256"] = digest
    print(json.dumps({k: v for k, v in report.items() if k != "records"}, indent=2))
    return report


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--reference-dir", required=True)
    p.add_argument("--candidate-dir", required=True)
    p.add_argument("--output-dir", default="outputs/nse_provenance_crosswalk")
    args = p.parse_args()
    reconcile(Path(args.reference_dir), Path(args.candidate_dir), Path(args.output_dir))


if __name__ == "__main__":
    main()
