"""QA-only regression tests for delivery missingness vs rolling warm-up.

These tests intentionally do not modify production scoring or gate semantics.
"""
import unittest

import numpy as np
import pandas as pd

from pipeline import walk_forward_backtest as wf


def sample_frame(delivery_values):
    n = len(delivery_values)
    return pd.DataFrame({
        "SYMBOL": ["TEST"] * n,
        "DATE": pd.date_range("2026-01-01", periods=n, freq="B"),
        "OPEN_PRICE": [100.0 + i for i in range(n)],
        "HIGH_PRICE": [102.0 + i for i in range(n)],
        "LOW_PRICE": [99.0 + i for i in range(n)],
        "CLOSE_PRICE": [101.0 + i for i in range(n)],
        "TTL_TRD_QNTY": [1000.0] * n,
        "DELIV_PER": delivery_values,
    })


class DeliveryMissingnessPolicyTests(unittest.TestCase):
    def test_present_delivery_value_produces_numeric_gap(self):
        out = wf.add_features(sample_frame([40.0, 42.0, 41.0, 43.0, 44.0]))
        self.assertEqual(out.loc[4, "HISTORY_DEPTH_AT_T"], 5)
        self.assertTrue(np.isfinite(out.loc[4, "DELIV20"]))
        self.assertTrue(np.isfinite(out.loc[4, "DELIV_GAP"]))

    def test_missing_current_delivery_remains_unknown_not_zero(self):
        out = wf.add_features(sample_frame([40.0, 42.0, 41.0, 43.0, 44.0, np.nan]))
        row = out.iloc[5]
        self.assertEqual(row["HISTORY_DEPTH_AT_T"], 6)
        self.assertTrue(np.isnan(row["DELIV_PER"]))
        self.assertTrue(np.isnan(row["DELIV_GAP"]))
        # DELIV_GAP is feature slot 6 when step=0/filter=2.
        self.assertEqual(wf.diagnostic_state(row, 0, 2), "UNKNOWN")

    def test_rolling_history_warmup_is_distinct_from_missing_current_value(self):
        out = wf.add_features(sample_frame([40.0, 42.0, 41.0, 43.0, 44.0]))
        first = out.iloc[0]
        fifth = out.iloc[4]
        self.assertEqual(first["HISTORY_DEPTH_AT_T"], 1)
        self.assertTrue(np.isnan(first["DELIV20"]))
        self.assertTrue(np.isnan(first["DELIV_GAP"]))
        self.assertTrue(np.isfinite(fifth["DELIV20"]))
        self.assertTrue(np.isfinite(fifth["DELIV_GAP"]))
        # Both can be UNKNOWN in a diagnostic slot, but provenance differs:
        # warm-up has shallow history; a missing current input has sufficient history.
        self.assertEqual(wf.diagnostic_state(first, 0, 2), "UNKNOWN")
        self.assertEqual(wf.diagnostic_state(fifth, 0, 2), "POSITIVE" if fifth["DELIV_GAP"] > 0 else ("NEGATIVE" if fifth["DELIV_GAP"] < 0 else "UNKNOWN"))


if __name__ == "__main__":
    unittest.main()
