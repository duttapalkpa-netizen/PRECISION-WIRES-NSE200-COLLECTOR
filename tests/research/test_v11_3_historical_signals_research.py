import unittest
import pandas as pd
from pipeline.v11_3_historical_signals_research import calibration_for_cutoff, dynamic_ret20_v11_3, signal_time_fields
from pipeline.v11_3_cost_aware_backtest import simulate_one


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

    def test_signal_timestamp_is_unknown_not_midnight(self):
        fields = signal_time_fields("2026-01-21")
        self.assertEqual(fields["SIGNAL_AS_OF_DATE"], "2026-01-21")
        self.assertIsNone(fields["SIGNAL_TIMESTAMP"])

    def test_replay_preserves_null_timestamp_and_date_only_asof(self):
        bars = pd.DataFrame([
            {"SYMBOL":"ABC","DATE":"2026-01-21","OPEN_PRICE":100,"HIGH_PRICE":101,"LOW_PRICE":99,"CLOSE_PRICE":100,"TTL_TRD_QNTY":1000},
            {"SYMBOL":"ABC","DATE":"2026-01-22","OPEN_PRICE":100,"HIGH_PRICE":106,"LOW_PRICE":99,"CLOSE_PRICE":105,"TTL_TRD_QNTY":1200},
        ])
        result = simulate_one(bars, "2026-01-21", "ABC", 5, 1, global_dates=list(pd.to_datetime(["2026-01-21","2026-01-22"])))
        self.assertEqual(result["SIGNAL_AS_OF_DATE"], "2026-01-21")
        self.assertIsNone(result["SIGNAL_TIMESTAMP"])

    def test_empty_replay_keeps_timestamp_unknown(self):
        bars = pd.DataFrame([
            {"SYMBOL":"ABC","DATE":"2026-01-21","OPEN_PRICE":100,"HIGH_PRICE":101,"LOW_PRICE":99,"CLOSE_PRICE":100,"TTL_TRD_QNTY":1000},
        ])
        result = simulate_one(bars, "2026-01-21", "ABC", 5, 1)
        self.assertEqual(result["SIGNAL_AS_OF_DATE"], "2026-01-21")
        self.assertIsNone(result["SIGNAL_TIMESTAMP"])




class ForwardOutcomeWindowTests(unittest.TestCase):
    def test_h3_uses_exact_next_three_rows_not_trailing_window(self):
        from pipeline.walk_forward_backtest import future_outcomes
        frame = pd.DataFrame({
            "SYMBOL": ["A"] * 6,
            "DATE": pd.date_range("2026-01-01", periods=6),
            "CLOSE_PRICE": [100.0] * 6,
            "HIGH_PRICE": [101.0, 102.0, 110.0, 103.0, 104.0, 150.0],
        })
        out = future_outcomes(frame)
        # At T0, only T+1..T+3 are eligible; the 150 at T+5 is excluded.
        self.assertAlmostEqual(out.loc[0, "FUT3_HIGH_PCT"], 10.0)
        # At T1, T+1..T+3 = rows 2..4, max 110.
        self.assertAlmostEqual(out.loc[1, "FUT3_HIGH_PCT"], 10.0)

    def test_h5_requires_all_five_future_rows_and_no_partial_tail(self):
        from pipeline.walk_forward_backtest import future_outcomes
        frame = pd.DataFrame({
            "SYMBOL": ["A"] * 6,
            "DATE": pd.date_range("2026-01-01", periods=6),
            "CLOSE_PRICE": [100.0] * 6,
            "HIGH_PRICE": [101.0, 102.0, 103.0, 104.0, 105.0, 120.0],
        })
        out = future_outcomes(frame)
        self.assertAlmostEqual(out.loc[0, "FUT5_HIGH_PCT"], 20.0)
        self.assertTrue(out.loc[1:, "FUT5_HIGH_PCT"].isna().all())

    def test_h1_and_close_labels_use_next_session_only(self):
        from pipeline.walk_forward_backtest import future_outcomes
        frame = pd.DataFrame({
            "SYMBOL": ["A"] * 3,
            "DATE": pd.date_range("2026-01-01", periods=3),
            "CLOSE_PRICE": [100.0, 105.0, 130.0],
            "HIGH_PRICE": [101.0, 106.0, 131.0],
        })
        out = future_outcomes(frame)
        self.assertAlmostEqual(out.loc[0, "FUT1_HIGH_PCT"], 6.0)
        self.assertAlmostEqual(out.loc[0, "FUT1_CLOSE_PCT"], 5.0)
        self.assertTrue(pd.isna(out.loc[2, "FUT1_HIGH_PCT"]))


if __name__ == "__main__":
    unittest.main()
