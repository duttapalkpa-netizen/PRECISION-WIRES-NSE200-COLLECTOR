import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from pipeline.reconcile_nse_snapshot_provenance import reconcile


def write_snapshot(root: Path, *, reference: bool, alter_hash: bool = False, bad_source: bool = False):
    raw = root / "raw"
    raw.mkdir(parents=True)
    records = []
    for i in range(200):
        trade_date = f"2026-01-{(i % 28) + 1:02d}"
        # Unique date keys while keeping fixture compact and deterministic.
        trade_date = f"2026-{(i // 28) + 1:02d}-{(i % 28) + 1:02d}"
        filename = f"sec_bhavdata_full_{i:03d}.csv"
        payload = f"SYMBOL,SERIES,DATE1,OPEN_PRICE,HIGH_PRICE,LOW_PRICE,CLOSE_PRICE,TTL_TRD_QNTY\nA,EQ,{trade_date},1,2,1,2,100\n".encode()
        (raw / filename).write_bytes(payload)
        digest = hashlib.sha256(payload).hexdigest()
        if alter_hash and i == 199:
            digest = "0" * 64
        url = f"https://nsearchives.nseindia.com/products/content/{filename}"
        response = {
            "url": url, "http_status": 200, "error": None, "bytes": len(payload),
            "response_sha256": hashlib.sha256(payload).hexdigest(),
            "retrieved_at_utc": "2026-11-12T15:16:58.252719+00:00"
        }
        if reference:
            rec = {
                "trade_date": trade_date, "file": filename, "bytes": len(payload), "sha256": digest,
                "schema_validation": "validated", "acquisition_status": "OK_FULL_BHAVCOPY_DELIVERY",
                "cache_origin": "network", "source_url": "https://attacker.example/file" if bad_source and i == 0 else url,
                "successful_response": response, "retrieved_at_utc": response["retrieved_at_utc"]
            }
        else:
            rec = {
                "trade_date": trade_date, "file": filename, "bytes": len(payload), "sha256": digest,
                "schema_validation": "validated", "acquisition_status": "CACHED",
                "cache_origin": "pre-existing-cache", "source_url": None, "successful_response": None,
                "retrieved_at_utc": "2026-11-12T15:16:58.000000+00:00"
            }
        records.append(rec)
    manifest = {"expected_sessions": 200, "actual_sessions": 200, "snapshot_id": "fixture-ref" if reference else "fixture-candidate", "records": records}
    (raw / f"nse_snapshot_manifest_{'ref' if reference else 'candidate'}.json").write_text(json.dumps(manifest))
    return root


class TestNseSnapshotProvenanceCrosswalk(unittest.TestCase):
    def test_exact_hash_crosswalk_passes_without_claiming_candidate_download(self):
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            ref = write_snapshot(base / "ref", reference=True)
            cand = write_snapshot(base / "cand", reference=False)
            result = reconcile(ref, cand, base / "out")
            self.assertEqual(result["status"], "PASS_CONTENT_IDENTICAL_TO_PREVIOUSLY_SOURCE_VERIFIED_SNAPSHOT")
            self.assertEqual(result["reconciliation"]["identical_content_sha256"], 200)
            self.assertFalse(result["candidate_snapshot"]["direct_source_retrieval_claimed"])
            self.assertEqual(len(result["records"]), 200)
            self.assertEqual(result["records"][0]["source_evidence_origin"], "EXACT_HASH_MATCH_TO_REFERENCE_NETWORK_SNAPSHOT")

    def test_rejects_changed_candidate_content(self):
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            ref = write_snapshot(base / "ref", reference=True)
            cand = write_snapshot(base / "cand", reference=False)
            path = next((base / "cand").rglob("sec_bhavdata_full_199.csv"))
            path.write_bytes(path.read_bytes() + b"changed")
            with self.assertRaisesRegex(ValueError, "byte-size mismatch|SHA-256 mismatch"):
                reconcile(ref, cand, base / "out")

    def test_rejects_unapproved_reference_source(self):
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            ref = write_snapshot(base / "ref", reference=True, bad_source=True)
            cand = write_snapshot(base / "cand", reference=False)
            with self.assertRaisesRegex(ValueError, "approved official NSE host"):
                reconcile(ref, cand, base / "out")

    def test_rejects_reference_without_http_200(self):
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            ref = write_snapshot(base / "ref", reference=True)
            manifest_path = next((base / "ref").rglob("nse_snapshot_manifest_*.json"))
            m = json.loads(manifest_path.read_text())
            m["records"][0]["successful_response"]["http_status"] = 404
            manifest_path.write_text(json.dumps(m))
            cand = write_snapshot(base / "cand", reference=False)
            with self.assertRaisesRegex(ValueError, "successful response URL/status mismatch"):
                reconcile(ref, cand, base / "out")


if __name__ == "__main__":
    unittest.main()
