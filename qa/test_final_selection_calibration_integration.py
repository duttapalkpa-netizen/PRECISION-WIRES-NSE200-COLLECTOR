"""End-to-end isolated tests for final_selection calibration readiness.

Runs the real final_selection.main() in temporary directories with tiny,
non-market QA fixtures. No NSE data, network, or production workflow is used.
"""
import csv
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
    def run_selection(self, calibration):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "outputs/finalists").mkdir(parents=True)
            (root / "outputs/backtest").mkdir(parents=True)
            (root / "outputs/diagnostics").mkdir(parents=True)
            (root / "data/qa").mkdir(parents=True)
            (root / "data/live").mkdir(parents=True)

            with (root / "outputs/finalists/v11_3_risk_adjusted.csv").open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(CANDIDATES[0]))
                writer.writeheader()
                writer.writerows(CANDIDATES)

            (root / "data/qa/qa_report.json").write_text(
                json.dumps({"delivery_ready_for_final_selection": True}), encoding="utf-8")
            (root / "outputs/diagnostics/diagnostics_672.csv").write_text("SYMBOL,DIAG\nALPHA,POSITIVE\n", encoding="utf-8")
            (root / "data/live/intraday_1m.csv").write_text(
                "SYMBOL,TIMESTAMP,CLOSE,DAY_VWAP,DAY_RVOL,ORB_HIGH_15\nALPHA,2026-01-01T10:00:00,100,99,2,101\n",
                encoding="utf-8")
            (root / "data/live/live_1m_status.json").write_text(
                json.dumps({"status": "LIVE_1M_CAPTURED", "rows": 1}), encoding="utf-8")

            if calibration is not None:
                (root / "outputs/backtest/calibration_validation.json").write_text(
                    json.dumps(calibration), encoding="utf-8")

            env = os.environ.copy()
            env["PYTHONPATH"] = str(REPO_ROOT) + os.pathsep + env.get("PYTHONPATH", "")
            proc = subprocess.run(
                [sys.executable, "-c", "from pipeline.final_selection import main; main()"],
                cwd=root, env=env, text=True, capture_output=True, check=False, timeout=30)
            self.assertEqual(proc.returncode, 0, msg=proc.stdout + "\n" + proc.stderr)

            report = json.loads((root / "outputs/finalists/final_selection_status.json").read_text())
            with (root / "outputs/finalists/ranked_candidates_all.csv").open(newline="", encoding="utf-8") as f:
                ranked = list(csv.DictReader(f))
            return report, ranked

    def assert_original_rank_order(self, ranked):
        self.assertEqual([r["SYMBOL"] for r in ranked], ["ALPHA", "BETA", "GAMMA"])
        self.assertEqual([int(r["SELECTION_RANK"]) for r in ranked], [1, 2, 3])

    def test_missing_calibration_blocks_but_preserves_ranking(self):
        report, ranked = self.run_selection(None)
        self.assertEqual(report["state"], "PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED")
        self.assertIn("CALIBRATION_EVIDENCE_STATUS_MISSING", report["blockers"])
        self.assert_original_rank_order(ranked)

    def test_invalid_calibration_blocks_but_preserves_ranking(self):
        report, ranked = self.run_selection({"status": "UNKNOWN_MALFORMED", "block_selection": True})
        self.assertEqual(report["state"], "PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED")
        self.assertIn("CALIBRATION_EVIDENCE_INVALID_OR_UNKNOWN", report["blockers"])
        self.assert_original_rank_order(ranked)

    def test_valid_calibration_removes_only_calibration_blocker(self):
        report, ranked = self.run_selection({"status": "VALID", "block_selection": False})
        self.assertEqual(report["state"], "FINAL_SELECTION_READY")
        self.assertNotIn("CALIBRATION_EVIDENCE_INVALID_OR_UNKNOWN", report["blockers"])
        self.assertNotIn("CALIBRATION_EVIDENCE_STATUS_MISSING", report["blockers"])
        self.assert_original_rank_order(ranked)

if __name__ == "__main__":
    unittest.main(verbosity=2)
