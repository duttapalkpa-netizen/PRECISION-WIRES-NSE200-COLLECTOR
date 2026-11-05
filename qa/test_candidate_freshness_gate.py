import unittest
import pandas as pd
from qa.evaluate_candidate_freshness_gate import evaluate, ELIGIBLE, NOT_ELIGIBLE, UNKNOWN

class FreshnessGateTests(unittest.TestCase):
    def setUp(self):
        self.universe = pd.DataFrame([
            ("AAA", "2026-11-04"), ("AAA", "2026-11-05"),
            ("BBB", "2026-11-04"), ("CCC", "2026-11-05")
        ], columns=["SYMBOL", "DATE"])
        self.candidates = pd.DataFrame([
            ("AAA", "2026-11-05", 90.0),
            ("BBB", "2026-11-04", 95.0),
            ("CCC", "2026-11-04", 80.0),
            ("MISSING", "2026-11-05", 70.0)
        ], columns=["SYMBOL", "DATE", "RISK_ADJUSTED_SCORE"])

    def test_current_candidate_is_eligible(self):
        x, _ = evaluate(self.universe, self.candidates)
        self.assertEqual(x.loc[0, "FRESHNESS_READINESS"], ELIGIBLE)

    def test_stale_symbol_is_not_eligible(self):
        x, _ = evaluate(self.universe, self.candidates)
        self.assertEqual(x.loc[1, "FRESHNESS_READINESS"], NOT_ELIGIBLE)
        self.assertEqual(int(x.loc[1, "DATA_LAG_SESSIONS"]), 1)

    def test_candidate_date_mismatch_is_not_eligible(self):
        x, _ = evaluate(self.universe, self.candidates)
        self.assertEqual(x.loc[2, "FRESHNESS_READINESS"], NOT_ELIGIBLE)
        self.assertEqual(x.loc[2, "FRESHNESS_REASON"], "CANDIDATE_ROW_DATE_MISMATCH")

    def test_missing_source_symbol_remains_unknown(self):
        x, _ = evaluate(self.universe, self.candidates)
        self.assertEqual(x.loc[3, "FRESHNESS_READINESS"], UNKNOWN)

    def test_preserves_order_scores_and_does_not_filter(self):
        x, report = evaluate(self.universe, self.candidates)
        self.assertEqual(x["SYMBOL"].tolist(), self.candidates["SYMBOL"].tolist())
        self.assertEqual(x["RISK_ADJUSTED_SCORE"].tolist(), self.candidates["RISK_ADJUSTED_SCORE"].tolist())
        self.assertEqual(len(x), len(self.candidates))
        self.assertTrue(report["ranking_preserved"])
        self.assertFalse(report["production_selector_modified"])
        self.assertFalse(report["score_modified"])
        self.assertFalse(report["core_672_modified"])

    def test_duplicate_universe_key_blocks(self):
        bad = pd.concat([self.universe, self.universe.iloc[[0]]], ignore_index=True)
        with self.assertRaisesRegex(ValueError, "duplicate universe"):
            evaluate(bad, self.candidates)

    def test_invalid_date_blocks(self):
        bad = self.universe.copy()
        bad.loc[0, "DATE"] = "not-a-date"
        with self.assertRaisesRegex(ValueError, "invalid symbol/date"):
            evaluate(bad, self.candidates)

    def test_top_n_is_assessment_only_not_reranked(self):
        x, report = evaluate(self.universe, self.candidates)
        self.assertEqual(report["top_n"]["3"]["rows"], 3)
        self.assertEqual(report["top_n"]["3"]["eligible"], 1)
        self.assertEqual(x.iloc[0]["SYMBOL"], "AAA")

if __name__ == "__main__":
    unittest.main()
