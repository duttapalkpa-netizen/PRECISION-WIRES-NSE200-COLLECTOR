"""Static safety contract for the manually dispatched calibration producer workflow."""
import unittest
from pathlib import Path

WORKFLOW = Path(".github/workflows/calibration_evidence_producer.yml")

class CalibrationProducerWorkflowContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = WORKFLOW.read_text(encoding="utf-8")

    def test_manual_dispatch_only_and_ten_minute_limit(self):
        self.assertIn("workflow_dispatch:", self.text)
        self.assertNotIn("pull_request:", self.text)
        self.assertIn("timeout-minutes: 10", self.text)

    def test_exact_run_commit_and_dataset_are_bound(self):
        self.assertIn("GITHUB_RUN_ID: ${{ github.run_id }}", self.text)
        self.assertIn("GITHUB_SHA: ${{ github.sha }}", self.text)
        self.assertIn('payload["producer_run_id"] != os.environ["GITHUB_RUN_ID"]', self.text)
        self.assertIn('payload["producer_commit_sha"] != os.environ["GITHUB_SHA"]', self.text)
        self.assertIn('payload["dataset_sha256"] != sha(src)', self.text)

    def test_no_synthetic_input_or_fallback(self):
        self.assertIn("test -s data/processed/nse_eq_200_sessions.csv", self.text)
        self.assertIn("if-no-files-found: error", self.text)
        self.assertNotIn("continue-on-error: true", self.text)

    def test_manifest_and_artifact_are_uploaded(self):
        self.assertIn("calibration_producer_manifest.json", self.text)
        self.assertIn("behavioral_dna_library.json", self.text)
        self.assertIn("actions/upload-artifact@v4", self.text)
        self.assertIn("retention-days: 14", self.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)
