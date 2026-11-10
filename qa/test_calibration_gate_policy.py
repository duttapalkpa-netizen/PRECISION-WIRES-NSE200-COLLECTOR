import json
import tempfile
import unittest
from pathlib import Path
from pipeline.calibration_gate import REQUIRED_METADATA, validate_calibration_artifact

def valid_payload(rate=0.0):
    data = {key: "test" for key in REQUIRED_METADATA}
    data["states"] = {"CONTINUATION_READY": {"hit10_h3_rate": rate}}
    return data

class CalibrationGatePolicyTests(unittest.TestCase):
    def check(self, payload=None, missing=False):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "calibration.json"
            if not missing:
                path.write_text(payload if isinstance(payload, str) else json.dumps(payload), encoding="utf-8")
            return validate_calibration_artifact(path)

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

if __name__ == "__main__":
    unittest.main(verbosity=2)
