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

    def test_approved_source_run_and_artifact_are_pinned(self):
        self.assertIn("43016431808", self.text)
        self.assertIn("13854135591", self.text)
        self.assertIn("precision-wires-adaptive-112", self.text)
        self.assertIn("7d7f3075b65eca66d606f06b39ed8c7e375c0e28", self.text)
        self.assertIn("b29c3da9b5c4ed082519b025c7844d151e2e0f874cf61e5cb00c63e6b0c8617e", self.text)
        self.assertIn("f3d259302cd44af4b402734db7aa43829208430978679be66f11cb2928d304c8", self.text)

    def test_dataset_is_verified_before_producer_runs(self):
        self.assertIn("unzip -tq /tmp/source-artifact.zip", self.text)
        self.assertIn("sha256sum --check -", self.text)
        self.assertIn('df["DATE"].nunique()!=200', self.text)
        self.assertIn('df.duplicated(["SYMBOL","DATE"]).any()', self.text)
        self.assertIn('df["SYMBOL"].nunique()!=2994 or len(df)!=501476', self.text)

    def test_exact_run_commit_and_dataset_are_bound(self):
        self.assertIn("GITHUB_RUN_ID: ${{ github.run_id }}", self.text)
        self.assertIn("GITHUB_SHA: ${{ github.sha }}", self.text)
        self.assertIn('payload["producer_run_id"]', self.text)
        self.assertIn('payload["producer_commit_sha"]', self.text)
        self.assertIn('payload["dataset_sha256"] != sha(src)', self.text)

    def test_no_synthetic_input_or_fallback(self):
        self.assertIn("if-no-files-found: error", self.text)
        self.assertNotIn("continue-on-error: true", self.text)
        self.assertIn("raise SystemExit", self.text)

    def test_producer_is_not_auto_triggered_on_pull_request(self):
        self.assertIn("workflow_dispatch:", self.text)
        self.assertNotIn("pull_request:", self.text)

    def test_manifest_binds_source_and_producer_lineage(self):
        self.assertIn("calibration_producer_manifest.json", self.text)
        self.assertIn('"source_run_id":43016431808', self.text)
        self.assertIn('"source_artifact_id":13854135591', self.text)
        self.assertIn('"producer_run_id":os.environ["GITHUB_RUN_ID"]', self.text)
        self.assertIn("actions/upload-artifact@v4", self.text)
        self.assertIn("retention-days: 14", self.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)
