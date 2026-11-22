import unittest
import pandas as pd

from pipeline.walk_forward_backtest import _matured_state_target_metrics


class MaturedStateDenominatorTests(unittest.TestCase):
    def _frame(self, n, state="EXPANSION_READY", null_outcomes=0):
        rows = []
        for i in range(n):
            rows.append({
                "STATE": state,
                "FUT1_HIGH_PCT": None if i < null_outcomes else (6.0 if i % 2 == 0 else 2.0),
                "FUT1_END_DATE": None if i < null_outcomes else "2026-11-01",
                "FUT3_HIGH_PCT": None if i < null_outcomes else (11.0 if i % 2 == 0 else 3.0),
                "FUT3_END_DATE": None if i < null_outcomes else "2026-11-03",
                "FUT5_HIGH_PCT": None if i < null_outcomes else (16.0 if i % 2 == 0 else 4.0),
                "FUT5_END_DATE": None if i < null_outcomes else "2026-11-05",
            })
        return pd.DataFrame(rows)

    def test_h3_calibration_requires_50_fully_matured_observations(self):
        result = _matured_state_target_metrics(self._frame(55, null_outcomes=6))
        h3 = result["EXPANSION_READY"]["T10_H3"]
        self.assertEqual(h3["matured_observations"], 49)
        self.assertEqual(h3["denominator"], 49)
        self.assertFalse(h3["calibration_eligible"])
        self.assertEqual(h3["calibration_status"], "UNKNOWN")

    def test_exactly_50_matured_h3_observations_is_eligible(self):
        result = _matured_state_target_metrics(self._frame(50))
        h3 = result["EXPANSION_READY"]["T10_H3"]
        self.assertEqual(h3["numerator"], 25)
        self.assertEqual(h3["denominator"], 50)
        self.assertTrue(h3["calibration_eligible"])
        self.assertEqual(h3["calibration_status"], "CALIBRATED")

    def test_state_denominators_are_independent(self):
        frame = pd.concat([
            self._frame(60, "EXPANSION_READY", null_outcomes=5),
            self._frame(80, "EXHAUSTION", null_outcomes=35),
        ], ignore_index=True)
        result = _matured_state_target_metrics(frame)
        self.assertEqual(result["EXPANSION_READY"]["T10_H3"]["denominator"], 55)
        self.assertTrue(result["EXPANSION_READY"]["T10_H3"]["calibration_eligible"])
        self.assertEqual(result["EXHAUSTION"]["T10_H3"]["denominator"], 45)
        self.assertFalse(result["EXHAUSTION"]["T10_H3"]["calibration_eligible"])

    def test_target_denominators_are_separate_and_missing_horizon_is_excluded(self):
        frame = self._frame(52)
        frame.loc[0, "FUT5_END_DATE"] = None
        result = _matured_state_target_metrics(frame)["EXPANSION_READY"]
        self.assertEqual(result["T5_H1"]["denominator"], 52)
        self.assertEqual(result["T10_H3"]["denominator"], 52)
        self.assertEqual(result["T15_H5"]["denominator"], 51)
        self.assertEqual(result["T20_H5"]["denominator"], 51)


if __name__ == "__main__":
    unittest.main()
