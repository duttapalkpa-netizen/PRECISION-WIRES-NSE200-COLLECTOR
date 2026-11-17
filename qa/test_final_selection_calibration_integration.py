"""End-to-end isolated tests for final_selection calibration readiness.

Runs the real final_selection.main() with tiny non-market fixtures. No network
or production workflow is used; the calibration artifact is checked against
the exact bytes of the consumer dataset fixture.
"""
import csv
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = [
    {"SYMBOL": "BETA", "RISK_ADJUSTED_SCORE": 80, "ENERGY": 70, "LEAD_TIME": 60, "RVOL20": 2, "DELIV20_AVG": 55, "RISK_MACRO": "LOW", "RISK_FII_DII": "LOW", "RISK_GEO": "LOW"},
    {"SYMBOL": "ALPHA", "RISK_ADJUSTED_SCORE": 90, "ENERGY": 60, "LEAD_TIME": 50, "RVOL20": 1, "DELIV20_AVG": 50, "RISK_MACRO": "LOW", "RISK_FII_DII": "LOW", "RISK_GEO": "LOW"},
    {"SYMBOL": "GAMMA", "RISK_ADJUSTED_SCORE": 80, "ENERGY": 70, "LEAD_TIME": 60, "RVOL20": 2, "DELIV20_AVG": 55, "RISK_MACRO": "LOW", "RISK_FII_DII": "LOW", "RISK_GEO": "LOW"},
]

class FinalSelectionCalibrationIntegrationTests(unittest.TestCase):
    def run_selection(self, calibration_case):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for folder in ("outputs/finalists", "outputs/backtest", "outputs/diagnostics",
                           "data/qa", "data/live", "data/processed"):
                (root / folder).mkdir(parents=True, exist_ok=True)
            with (root / "outputs/finalists/v11_3_risk_adjusted.csv").open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(CANDIDATES[0]))
                writer.writeheader()
                writer.writerows(CANDIDATES)
            dataset = root / "data/processed/nse_eq_200_sessions.csv"
            dataset.write_bytes(b"small isolated dataset fixture; not market observations")
            if calibration_case in ("valid", "mismatch"):
                artifact_hash = hashlib.sha256(dataset.read_bytes()).hexdigest()
                if calibration_case == "mismatch":
                    artifact_hash = "b" * 64
                payload = {
                    "schema_version": "1.0", "producer_engine": "V11.3",
                    "producer_engine_version": "11.3", "feature_contract_version": "1",
                    "producer_run_id": "43051456434", "producer_commit_sha": "a" * 40,
                    "dataset_sha256": artifact_hash, "cutoff_start": "2026-01-01",
                    "cutoff_end": "2026-01-30", "generated_at_utc": "2026-02-01T00:00:00+00:00",
                    "target_definition": "hit10_h3", "label_maturity_cutoff": "2026-02-01",
                    "states": {"CONTINUATION_READY": {
                        "sample_count": 10, "hit10_h3_count": 2, "hit10_h3_rate": 0.2}}
                }
                (root / "outputs/backtest/behavioral_dna_library.json").write_text(
                    json.dumps(payload), encoding="utf-8")
            elif calibration_case == "malformed":
                (root / "outputs/backtest/behavioral_dna_library.json").write_text(
                    "{bad-json", encoding="utf-8")

            (root / "data/qa/qa_report.json").write_text(
                json.dumps({"delivery_ready_for_final_selection": True}), encoding="utf-8")
            (root / "outputs/diagnostics/diagnostics_672.csv").write_text(
                "SYMBOL,DIAG\nALPHA,POSITIVE\n", encoding="utf-8")
            (root / "data/live/intraday_1m.csv").write_text(
                "SYMBOL,TIMESTAMP,CLOSE,DAY_VWAP,DAY_RVOL,ORB_HIGH_15\nALPHA,2026-01-01T10:00:00,100,99,2,101\n",
                encoding="utf-8")
            (root / "data/live/live_1m_status.json").write_text(
                json.dumps({"status": "LIVE_1M_CAPTURED", "rows": 1}), encoding="utf-8")

            env = os.environ.copy()
            env["PYTHONPATH"] = str(REPO_ROOT) + os.pathsep + env.get("PYTHONPATH", "")
            proc = subprocess.run(
                [sys.executable, "-c", "from pipeline.final_selection import main; main()"],
                cwd=root, env=env, text=True, capture_output=True, check=False, timeout=30)
            self.assertEqual(proc.returncode, 0, msg=proc.stdout + "\n" + proc.stderr)
            report = json.loads((root / "outputs/finalists/final_selection_status.json").read_text())
            validation = json.loads((root / "outputs/backtest/calibration_validation.json").read_text())
            with (root / "outputs/finalists/ranked_candidates_all.csv").open(newline="", encoding="utf-8") as f:
                ranked = list(csv.DictReader(f))
            return report, ranked, validation

    def assert_original_rank_order(self, ranked):
        self.assertEqual([r["SYMBOL"] for r in ranked], ["ALPHA", "BETA", "GAMMA"])
        self.assertEqual([int(r["SELECTION_RANK"]) for r in ranked], [1, 2, 3])

    def test_missing_artifact_blocks_but_preserves_ranking(self):
        report, ranked, validation = self.run_selection(None)
        self.assertEqual(validation["status"], "UNKNOWN_MISSING")
        self.assertEqual(report["state"], "PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED")
        self.assertIn("CALIBRATION_EVIDENCE_INVALID_OR_UNKNOWN", report["blockers"])
        self.assert_original_rank_order(ranked)

    def test_malformed_artifact_blocks_but_preserves_ranking(self):
        report, ranked, validation = self.run_selection("malformed")
        self.assertEqual(validation["status"], "UNKNOWN_MALFORMED")
        self.assertEqual(report["state"], "PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED")
        self.assertIn("CALIBRATION_EVIDENCE_INVALID_OR_UNKNOWN", report["blockers"])
        self.assert_original_rank_order(ranked)

    def test_matching_artifact_and_dataset_allow_calibration_gate_only(self):
        report, ranked, validation = self.run_selection("valid")
        self.assertEqual(validation["status"], "VALID")
        self.assertEqual(report["state"], "FINAL_SELECTION_READY")
        self.assertNotIn("CALIBRATION_EVIDENCE_INVALID_OR_UNKNOWN", report["blockers"])
        self.assert_original_rank_order(ranked)

    def test_dataset_mismatch_blocks_even_with_valid_artifact_metadata(self):
        report, ranked, validation = self.run_selection("mismatch")
        self.assertEqual(validation["status"], "PROVENANCE_MISMATCH")
        self.assertEqual(report["state"], "PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED")
        self.assertIn("CALIBRATION_EVIDENCE_INVALID_OR_UNKNOWN", report["blockers"])
        self.assert_original_rank_order(ranked)

if __name__ == "__main__":
    unittest.main(verbosity=2)
