import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from pipeline.calibration_gate import REQUIRED_METADATA, validate_calibration_artifact

def valid_payload(rate=0.0, dataset_sha=None):
    data = {key: "test" for key in REQUIRED_METADATA}
    data.update({
        "schema_version": "1.0", "producer_engine": "V11.3",
        "producer_engine_version": "11.3", "feature_contract_version": "1",
        "producer_run_id": "run-test", "producer_commit_sha": "a" * 40,
        "dataset_sha256": dataset_sha or "b" * 64, "cutoff_start": "2026-01-01",
        "cutoff_end": "2026-10-01", "generated_at_utc": "2026-10-02T00:00:00+00:00",
        "target_definition": "hit10_h3", "label_maturity_cutoff": "2026-10-01",
    })
    hits = int(rate * 10) if isinstance(rate, (int, float)) and not isinstance(rate, bool) and 0 <= rate <= 1 else 0
    data["states"] = {"CONTINUATION_READY": {"sample_count": 10, "hit10_h3_count": hits, "hit10_h3_rate": rate}}
    return data

class CalibrationGatePolicyTests(unittest.TestCase):
    def check(self, payload=None, missing=False, dataset_bytes=None):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "calibration.json"
            dataset = Path(td) / "dataset.csv"
            if dataset_bytes is not None:
                dataset.write_bytes(dataset_bytes)
            if not missing:
                path.write_text(payload if isinstance(payload, str) else json.dumps(payload), encoding="utf-8")
            return validate_calibration_artifact(path, dataset_path=dataset if dataset_bytes is not None else None)

    def test_missing_blocks(self):
        self.assertEqual(self.check(missing=True)["status"], "UNKNOWN_MISSING")
        self.assertTrue(self.check(missing=True)["block_selection"])

    def test_malformed_blocks(self):
        self.assertEqual(self.check("{bad-json")["status"], "UNKNOWN_MALFORMED")

    def test_missing_provenance_blocks(self):
        data = valid_payload()
        del data["producer_run_id"]
        self.assertEqual(self.check(data)["status"], "UNKNOWN_PROVENANCE")

    def test_measured_zero_is_valid_and_distinct(self):
        result = self.check(valid_payload(0.0))
        self.assertEqual(result["status"], "VALID")
        self.assertFalse(result["block_selection"])

    def test_invalid_rates_block(self):
        for rate in (-0.1, 1.1, float("nan"), float("inf"), True):
            self.assertEqual(self.check(valid_payload(rate))["status"], "INVALID_VALUE")

    def test_incomplete_state_blocks(self):
        data = valid_payload()
        data["states"] = {"CONTINUATION_READY": {}}
        self.assertEqual(self.check(data)["status"], "UNKNOWN_INCOMPLETE")

    def test_zero_sample_count_is_unknown(self):
        data = valid_payload()
        data["states"]["CONTINUATION_READY"]["sample_count"] = 0
        self.assertEqual(self.check(data)["status"], "UNKNOWN_INCOMPLETE")

    def test_rate_count_mismatch_blocks(self):
        data = valid_payload(0.2)
        data["states"]["CONTINUATION_READY"]["hit10_h3_count"] = 1
        self.assertEqual(self.check(data)["status"], "INVALID_VALUE")

    def test_exact_consumer_dataset_hash_is_required(self):
        raw = b"official dataset fixture bytes"
        digest = hashlib.sha256(raw).hexdigest()
        result = self.check(valid_payload(0.2, digest), dataset_bytes=raw)
        self.assertEqual(result["status"], "VALID")
        self.assertEqual(result["dataset_sha256"], digest)

    def test_mismatched_consumer_dataset_hash_blocks(self):
        result = self.check(valid_payload(0.2, "b" * 64), dataset_bytes=b"different dataset bytes")
        self.assertEqual(result["status"], "PROVENANCE_MISMATCH")
        self.assertTrue(result["block_selection"])

    def test_missing_consumer_dataset_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "calibration.json"
            path.write_text(json.dumps(valid_payload()), encoding="utf-8")
            result = validate_calibration_artifact(path, dataset_path=Path(td) / "missing.csv")
            self.assertEqual(result["status"], "UNKNOWN_DATASET")

if __name__ == "__main__":
    unittest.main(verbosity=2)
