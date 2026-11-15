import unittest
import numpy as np
import pandas as pd

from pipeline.forward_outcome_integrity import add_forward_outcomes


class ForwardOutcomeIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.rows = [
            ["ABC", "2026-01-01", 101, 100],
            ["ABC", "2026-01-02", 102, 101],
            ["ABC", "2026-01-05", 106, 105],
            ["ABC", "2026-01-06", 104, 102],
            ["ABC", "2026-01-07", 103, 103],
            ["ABC", "2026-01-08", 101, 100],
            ["XYZ", "2026-01-01", 51, 50],
            ["XYZ", "2026-01-02", 55, 54],
            ["XYZ", "2026-01-05", 53, 52],
            ["XYZ", "2026-01-06", 52, 51],
        ]
        self.df = pd.DataFrame(
            self.rows, columns=["SYMBOL", "DATE", "HIGH_PRICE", "CLOSE_PRICE"]
        )

    def test_exact_forward_h1_h3_h5_high_and_close(self):
        out = add_forward_outcomes(self.df)
        self.assertAlmostEqual(out.loc[0, "FUT1_HIGH_PCT"], 2.0)
        self.assertAlmostEqual(out.loc[0, "FUT3_HIGH_PCT"], 6.0)
        self.assertAlmostEqual(out.loc[0, "FUT3_CLOSE_PCT"], 5.0)
        self.assertAlmostEqual(out.loc[0, "FUT5_HIGH_PCT"], 6.0)
        self.assertAlmostEqual(out.loc[0, "FUT5_CLOSE_PCT"], 5.0)

    def test_incomplete_horizons_are_unknown_not_partial(self):
        out = add_forward_outcomes(self.df)
        self.assertTrue(np.isnan(out.loc[5, "FUT1_HIGH_PCT"]))
        abc_tail = out[out["SYMBOL"] == "ABC"].iloc[3:]
        self.assertTrue(abc_tail["FUT3_HIGH_PCT"].isna().all())
        self.assertTrue(out.loc[1:, "FUT5_HIGH_PCT"].isna().all())

    def test_symbols_never_cross_contaminate(self):
        out = add_forward_outcomes(self.df)
        self.assertAlmostEqual(out.loc[6, "FUT1_HIGH_PCT"], 10.0)
        self.assertAlmostEqual(out.loc[6, "FUT3_HIGH_PCT"], 10.0)

    def test_unsorted_input_preserves_rows_and_uses_date_order(self):
        shuffled = self.df.sample(frac=1, random_state=17)
        out = add_forward_outcomes(shuffled)
        first_abc = out[(out["SYMBOL"] == "ABC") & (out["DATE"] == "2026-01-01")]
        self.assertAlmostEqual(float(first_abc.iloc[0]["FUT3_HIGH_PCT"]), 6.0)
        self.assertEqual(list(out.index), list(shuffled.index))

    def test_duplicate_symbol_date_fails_closed(self):
        duplicate = pd.concat([self.df, self.df.iloc[[0]]], ignore_index=True)
        with self.assertRaisesRegex(ValueError, "duplicate SYMBOL/DATE"):
            add_forward_outcomes(duplicate)

    def test_invalid_date_fails_closed(self):
        bad = self.df.copy()
        bad.loc[0, "DATE"] = "not-a-date"
        with self.assertRaisesRegex(ValueError, "invalid DATE"):
            add_forward_outcomes(bad)

    def test_invalid_future_price_makes_label_unknown(self):
        bad = self.df.copy()
        bad.loc[1, "HIGH_PRICE"] = np.inf
        out = add_forward_outcomes(bad)
        self.assertTrue(np.isnan(out.loc[0, "FUT1_HIGH_PCT"]))

    def test_invalid_horizons_rejected(self):
        for horizons in ((0,), (1.5,), (True,), (1, 1)):
            with self.subTest(horizons=horizons), self.assertRaises(ValueError):
                add_forward_outcomes(self.df, horizons=horizons)

    def test_missing_symbol_session_does_not_skip_forward(self):
        missing = self.df[~((self.df["SYMBOL"] == "ABC") &
                            (self.df["DATE"] == "2026-01-05"))].copy()
        out = add_forward_outcomes(missing)
        row = out[(out["SYMBOL"] == "ABC") &
                  (out["DATE"] == "2026-01-02")].iloc[0]
        self.assertTrue(np.isnan(row["FUT1_HIGH_PCT"]))
        self.assertTrue(np.isnan(row["FUT3_HIGH_PCT"]))

    def test_input_is_not_mutated(self):
        before = self.df.copy(deep=True)
        add_forward_outcomes(self.df)
        pd.testing.assert_frame_equal(self.df, before)


if __name__ == "__main__":
    unittest.main()
