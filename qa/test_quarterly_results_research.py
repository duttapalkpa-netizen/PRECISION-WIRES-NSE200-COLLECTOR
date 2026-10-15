import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

import pipeline.quarterly_results_research as stage


class QuarterlyResultsResearchTests(unittest.TestCase):
    def test_board_meeting_is_not_a_declared_result(self):
        row = {
            "symbol": "ABC", "companyName": "ABC Limited",
            "purpose": "To consider and approve financial results for the quarter ended September 30, 2026",
            "meetingDate": "15-Oct-2026",
        }
        normalized = stage.normalize_event(row, "BOARD_MEETING", "https://www.nseindia.com/example")
        self.assertFalse(normalized["RESULT_DECLARED"])
        self.assertEqual(normalized["EVENT_KIND"], "BOARD_MEETING")

    def test_results_disclosure_flag_requires_result_event_type(self):
        row = {
            "symbol": "ABC", "companyName": "ABC Limited",
            "subject": "Outcome: Unaudited financial results for the quarter",
            "broadcastDate": "15-Oct-2026", "attachment": "https://example.test/result.pdf",
        }
        normalized = stage.normalize_event(row, "RESULT_DISCLOSURE", "https://www.nseindia.com/example")
        self.assertTrue(normalized["RESULT_DECLARED"])
        self.assertTrue(normalized["SOURCE_RECORD_SHA256"])

    def test_nse_announcement_date_alias_is_normalized(self):
        row = {
            "symbol": "ABC", "companyName": "ABC Limited",
            "subject": "Outcome: Unaudited financial results for the quarter",
            "an_dt": "15-Oct-2026",
        }
        normalized = stage.normalize_event(row, "RESULT_DISCLOSURE", "https://www.nseindia.com/api/corporates-announcements")
        self.assertTrue(normalized["RESULT_DECLARED"])
        self.assertTrue(normalized["BROADCAST_AT"])

    def test_event_study_accepts_normalized_close_price_column(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            events_path = root / "events.csv"
            panel_path = root / "panel.csv"
            pd.DataFrame([{
                "SYMBOL": "ABC", "RESULT_DECLARED": True,
                "BROADCAST_AT": "2026-10-01T12:00:00Z",
                "SOURCE_URL": "https://example.test/result.pdf",
            }]).to_csv(events_path, index=False)
            pd.DataFrame([
                {"SYMBOL":"ABC","DATE":"2026-10-01","CLOSE_PRICE":100},
                {"SYMBOL":"ABC","DATE":"2026-10-02","CLOSE_PRICE":101},
                {"SYMBOL":"ABC","DATE":"2026-10-05","CLOSE_PRICE":105},
                {"SYMBOL":"ABC","DATE":"2026-10-06","CLOSE_PRICE":106},
                {"SYMBOL":"ABC","DATE":"2026-10-07","CLOSE_PRICE":107},
            ]).to_csv(panel_path, index=False)
            study, report = stage.build_event_study(events_path, panel_path)
            self.assertEqual(report["status"], "COMPUTED_EXPLORATORY")
            self.assertEqual(report["matched_result_events"], 1)

    def test_financial_features_calculate_yoy_and_only_consensus_surprise_when_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "quarterly_financial_metrics.csv"
            pd.DataFrame([
                {"SYMBOL":"ABC","PERIOD_END":"2025-09-30","BASIS":"CONSOLIDATED",
                 "SOURCE_URL":"https://example.test/old.pdf","DISCLOSED_AT":"2025-10-15T12:00:00Z",
                 "REVENUE":100,"PAT":10,"EPS":1,"CONSENSUS_REVENUE":None,"CONSENSUS_PAT":None,"CONSENSUS_EPS":None},
                {"SYMBOL":"ABC","PERIOD_END":"2026-09-30","BASIS":"CONSOLIDATED",
                 "SOURCE_URL":"https://example.test/new.pdf","DISCLOSED_AT":"2026-10-15T12:00:00Z",
                 "REVENUE":120,"PAT":15,"EPS":1.5,"CONSENSUS_REVENUE":110,"CONSENSUS_PAT":12,"CONSENSUS_EPS":1.2},
            ]).to_csv(path, index=False)
            features, report = stage.build_financial_features(path)
            self.assertEqual(report["status"], "COMPUTED")
            latest = features.iloc[-1]
            self.assertAlmostEqual(latest["REVENUE_YOY_PCT"], 20.0)
            self.assertAlmostEqual(latest["PAT_YOY_PCT"], 50.0)
            self.assertAlmostEqual(latest["EPS_SURPRISE_PCT"], 25.0)
            self.assertFalse(bool(features.iloc[0]["FINANCIALS_STATUS"] == "BLOCKED_MISSING_SOURCE_URL"))


if __name__ == "__main__":
    unittest.main()
