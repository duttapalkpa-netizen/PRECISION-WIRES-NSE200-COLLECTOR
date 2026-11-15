import unittest
import pandas as pd
from pipeline.v11_3_historical_signals_research import calibration_for_cutoff


class CutoffSafeCalibrationTests(unittest.TestCase):
    def test_only_fully_matured_cutoffs_are_used(self):
        # At cutoff session 8, only signal cutoffs through session 5 (8-3)
        # are eligible. Session 6 is deliberately high-performing but immature.
        rows = [
            {"SESSION_IDX": 5, "STATE": "A", "SAMPLES": 100, "HITS": 25},
            {"SESSION_IDX": 6, "STATE": "A", "SAMPLES": 100, "HITS": 100},
            {"SESSION_IDX": 5, "STATE": "B", "SAMPLES": 100, "HITS": 50},
        ]
        mapping, meta = calibration_for_cutoff(pd.DataFrame(rows), 8, 100)
        self.assertEqual(mapping["A"]["hit_rate"], 0.25)
        self.assertEqual(mapping["B"]["hit_rate"], 0.50)
        self.assertEqual(mapping["A"]["calibration_score"], 75.0)
        self.assertEqual(meta["matured_samples"], 200)

    def test_below_minimum_sample_remains_unknown(self):
        rows = [{"SESSION_IDX": 1, "STATE": "A", "SAMPLES": 99, "HITS": 50}]
        mapping, meta = calibration_for_cutoff(pd.DataFrame(rows), 4, 100)
        self.assertEqual(mapping, {})
        self.assertEqual(meta["eligible_states"], 0)

    def test_no_matured_window_returns_unknown(self):
        rows = [{"SESSION_IDX": 2, "STATE": "A", "SAMPLES": 500, "HITS": 250}]
        mapping, meta = calibration_for_cutoff(pd.DataFrame(rows), 4, 100)
        self.assertEqual(mapping, {})
        self.assertEqual(meta["matured_samples"], 0)


if __name__ == "__main__":
    unittest.main()
