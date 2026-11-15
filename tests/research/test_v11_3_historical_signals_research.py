import unittest
import pandas as pd
from pipeline.v11_3_historical_signals_research import calibration_for_cutoff, dynamic_ret20_v11_3


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


    def test_dynamic_ret20_matches_v11_3_short_history_window(self):
        frame = pd.DataFrame({
            "SYMBOL": ["A", "A", "A", "B"] + ["B"] * 21,
            "CLOSE_PRICE": [100, 110, 120] + [100 + i for i in range(22)],
        })
        grouped = frame.groupby("SYMBOL", sort=False)["CLOSE_PRICE"]
        depth = frame.groupby("SYMBOL", sort=False).cumcount() + 1
        result = dynamic_ret20_v11_3(grouped, depth)
        # A has only 3 rows, so row 3 uses a 2-session lookback (120/100 - 1).
        self.assertAlmostEqual(result.iloc[2], 20.0)
        # B's 22nd row uses the 20-session lookback, not a shorter expanding window.
        self.assertAlmostEqual(result.iloc[-1], ((121 / 101) - 1) * 100)

    def test_no_matured_window_returns_unknown(self):
        rows = [{"SESSION_IDX": 2, "STATE": "A", "SAMPLES": 500, "HITS": 250}]
        mapping, meta = calibration_for_cutoff(pd.DataFrame(rows), 4, 100)
        self.assertEqual(mapping, {})
        self.assertEqual(meta["matured_samples"], 0)


if __name__ == "__main__":
    unittest.main()
