"""Counterfactual characterization of downstream delivery-missingness effects.

These tests lock the observed behavior for review; they do not approve a new
production missingness policy and do not modify production scoring code.
"""
import unittest

import numpy as np

from pipeline import walk_forward_backtest as wf
from qa.test_delivery_missingness_policy import sample_frame


class DownstreamDeliveryCounterfactualTests(unittest.TestCase):
    def _missing_and_neutral_scenarios(self):
        source = sample_frame([40.0, 42.0, 41.0, 43.0, 44.0, np.nan])
        missing = wf.add_features(source)
        neutral = missing.copy()

        # QA-only counterfactual: explicitly set only the final DELIV_GAP to
        # neutral zero and recompute its directly dependent ABSORPTION term.
        neutral.loc[neutral.index[-1], "DELIV_GAP"] = 0.0
        i = neutral.index[-1]
        neutral.loc[i, "ABSORPTION"] = (
            25 * int(neutral.loc[i, "CLOSE_PRICE"] >= neutral.loc[i, "EMA20"])
            + 25 * int(neutral.loc[i, "RANGE_POS20"] >= 0.55)
            + 25 * int(neutral.loc[i, "DELIV_GAP"] >= 0)
            + 25 * int(neutral.loc[i, "RVOL20"] >= 1.2)
        )

        return (
            wf.add_tomorrow_features(missing),
            wf.add_tomorrow_features(neutral),
        )

    def test_missing_gap_is_zero_filled_only_in_repr_pressure_component(self):
        missing, neutral = self._missing_and_neutral_scenarios()
        m = missing.iloc[-1]
        n = neutral.iloc[-1]

        # Production code fills DELIV_GAP NaN with 0 in REPRICING_PRESSURE.
        self.assertAlmostEqual(m["REPRICING_PRESSURE"], n["REPRICING_PRESSURE"], places=12)
        # But ABSORPTION compares NaN >= 0, which is False: 25 points disappear.
        self.assertAlmostEqual(n["ABSORPTION"] - m["ABSORPTION"], 25.0, places=12)

    def test_missing_delivery_propagates_into_readiness_and_tomorrow_score(self):
        missing, neutral = self._missing_and_neutral_scenarios()
        m = missing.iloc[-1]
        n = neutral.iloc[-1]

        # READINESS weights ABSORPTION at 20%; TOMORROW score separately
        # weights ABSORPTION directly at 15% (25 * 0.15 = 3.75 points).
        self.assertAlmostEqual(n["READINESS"] - m["READINESS"], 5.0, places=12)
        self.assertAlmostEqual(
            n["TOMORROW_EXPANSION_SCORE"] - m["TOMORROW_EXPANSION_SCORE"],
            3.75,
            places=12,
        )

    def test_counterfactual_does_not_mutate_original_missing_feature(self):
        missing, _ = self._missing_and_neutral_scenarios()
        self.assertTrue(np.isnan(missing.iloc[-1]["DELIV_GAP"]))


if __name__ == "__main__":
    unittest.main()
