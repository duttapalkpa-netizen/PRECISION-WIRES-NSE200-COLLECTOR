import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

import pipeline.quarterly_results_research as stage


class QuarterlyResultsResearchTests(unittest.TestCase):
    def test_step1_endpoint_schema_pass_is_separate_from_step2_period_validation(self):
        sources = {
            "RESULT_DISCLOSURE": {"status": "AVAILABLE",
                "request_url": "https://www.nseindia.com/api/corporate-announcements"},
            "BOARD_MEETING": {"status": "AVAILABLE",
                "request_url": "https://www.nseindia.com/api/corporate-announcements"},
        }
        result_rows = [{
            "SYMBOL": "ADROITIND", "ISIN": "INE505M01015",
            "BROADCAST_AT": "2026-10-12T15:38:52+00:00",
            "ATTACHMENT_URL": "https://nsearchives.nseindia.com/corporate/result.pdf",
            "RAW_RECORD_JSON": "{\"symbol\":\"ADROITIND\"}", "PERIOD_END": "",
        }]
        calendar_rows = [{
            "SYMBOL": "ABC", "BROADCAST_AT": "2026-10-15T10:00:00+00:00",
            "RAW_RECORD_JSON": "{\"symbol\":\"ABC\"}",
        }]
        report = stage.evaluate_endpoint_schema(sources, result_rows, calendar_rows)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["source_mode"], "ANNOUNCEMENT_FALLBACK")
        self.assertEqual(report["schema_contract"]["reporting_period_validation"],
                         "DEFERRED_TO_STEP_2_RECORD_VALIDATION")
        # Missing reporting period is not silently made valid by Step 1 PASS.
        self.assertFalse(bool(result_rows[0]["PERIOD_END"]))

    def test_step1_endpoint_schema_blocks_missing_required_schema_field(self):
        sources = {
            "RESULT_DISCLOSURE": {"status": "AVAILABLE", "request_url": "https://www.nseindia.com/api/x"},
            "BOARD_MEETING": {"status": "AVAILABLE", "request_url": "https://www.nseindia.com/api/y"},
        }
        result_rows = [{"SYMBOL": "ABC", "ISIN": "", "BROADCAST_AT": "2026-10-15",
                        "ATTACHMENT_URL": "https://example.test/a.pdf", "RAW_RECORD_JSON": "{}"}]
        calendar_rows = [{"SYMBOL": "ABC", "BROADCAST_AT": "2026-10-15", "RAW_RECORD_JSON": "{}"}]
        report = stage.evaluate_endpoint_schema(sources, result_rows, calendar_rows)
        # Empty record-level values belong to Step 2, not endpoint schema.
        self.assertEqual(report["status"], "PASS")
        self.assertTrue(report["checks"]["result_schema_fields_present"])
        # A genuinely absent normalized field remains a schema blocker.
        del result_rows[0]["ISIN"]
        report = stage.evaluate_endpoint_schema(sources, result_rows, calendar_rows)
        self.assertEqual(report["status"], "BLOCKED")
        self.assertFalse(report["checks"]["result_schema_fields_present"])


    def test_integrated_financials_route_variants_are_tried_before_announcement_fallback(self):
        from unittest.mock import MagicMock
        session = MagicMock()
        def get(url, params=None, **kwargs):
            response = MagicMock()
            response.url = url
            response.raise_for_status.return_value = None
            response.json.return_value = ([{"symbol":"ABC","xbrlFileUrl":"https://example.test/a.xbrl"}]
                                          if params and params.get("type") == "Integrated Filing- Financials"
                                          else [])
            return response
        session.get.side_effect = get
        with patch.object(stage.requests, "Session", return_value=session):
            rows, url, payload = stage.fetch_nse(
                stage.RESULTS_URL, pd.Timestamp("2026-10-01").date(),
                pd.Timestamp("2026-10-17").date())
        self.assertTrue(rows)
        self.assertIn("integrated-filing-results", url)
        self.assertEqual(rows[0]["symbol"], "ABC")

    def test_integrated_rows_without_xbrl_url_are_not_accepted_as_structured_financial_source(self):
        from unittest.mock import MagicMock
        session = MagicMock()
        def get(url, params=None, **kwargs):
            response = MagicMock()
            response.url = url
            response.status_code = 200
            response.raise_for_status.return_value = None
            if "integrated-filing-results" in url and params and params.get("type") == "Integrated Filing- Financials":
                response.json.return_value = [{"symbol": "ABC", "quarterEndDate": "30-Sep-2026"}]
            elif "corporate-announcements" in url:
                response.json.return_value = [{"symbol": "ABC", "attchmntFile": "https://nsearchives.nseindia.com/corporate/a.pdf",
                                               "an_dt": "16-Oct-2026", "attchmntText": "financial results"}]
            else:
                response.json.return_value = []
            return response
        session.get.side_effect = get
        with patch.object(stage.requests, "Session", return_value=session):
            rows, url, payload = stage.fetch_nse(
                stage.RESULTS_URL, pd.Timestamp("2026-10-01").date(),
                pd.Timestamp("2026-10-17").date())
        self.assertIn("corporate-announcements", url)
        diag = [d for d in stage.FETCH_DIAGNOSTICS if "integrated-filing-results" in d["endpoint"]]
        self.assertTrue(diag)
        self.assertTrue(all(d.get("rows_with_xbrl_url", 0) == 0 for d in diag if d.get("row_count", 0)))
        self.assertTrue(any("no explicit XBRL URL field" in x for x in [
            f for d in diag for f in ([d.get("error", "")] + [str(d.get("row_count", ""))])
        ]) or any(d.get("row_count", 0) > 0 for d in diag))

    def test_integrated_financials_explicit_page_query_is_tried_before_pdf_fallback(self):
        from unittest.mock import MagicMock
        session = MagicMock()
        seen = []
        def get(url, params=None, **kwargs):
            response = MagicMock()
            response.url = url
            response.raise_for_status.return_value = None
            seen.append((url, dict(params or {})))
            response.json.return_value = ([{
                "symbol": "ABC", "sm_isin": "INE123A01011",
                "quarterEndDate": "30-Sep-2026",
                "broadcastDateTime": "16-Oct-2026 20:00:00",
                "xbrlFileUrl": "https://nsearchives.nseindia.com/corporate/ABC.xbrl"
            }] if params and params.get("size") == "500" and
                 params.get("page") == "1" and
                 params.get("type") == "Integrated Filing- Financials"
                 else [])
            return response
        session.get.side_effect = get
        with patch.object(stage.requests, "Session", return_value=session):
            rows, url, payload = stage.fetch_nse(
                stage.RESULTS_URL, pd.Timestamp("2026-10-01").date(),
                pd.Timestamp("2026-10-17").date())
        self.assertTrue(rows)
        self.assertIn("integrated-filing-results", url)
        self.assertTrue(any(p.get("size") == "500" and p.get("page") == "1" and p.get("type") == "Integrated Filing- Financials" for _, p in seen))
        self.assertIn("xbrlFileUrl", rows[0])

    def test_board_meeting_is_not_a_declared_result(self):
        row = {
            "symbol": "ABC", "companyName": "ABC Limited",
            "purpose": "To consider and approve financial results for the quarter ended September 30, 2026",
            "meetingDate": "15-Oct-2026",
        }
        normalized = stage.normalize_event(row, "BOARD_MEETING", "https://www.nseindia.com/example")
        self.assertFalse(normalized["RESULT_DECLARED"])
        self.assertEqual(normalized["EVENT_KIND"], "BOARD_MEETING")

    def test_official_historical_isin_evidence_resolves_legacy_symbol_and_keeps_unknown_unresolved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ref = root / "data" / "reference"
            ref.mkdir(parents=True)
            (ref / "historical_security_isin_evidence.csv").write_text(
                "SYMBOL,ISIN,COMPANY,SOURCE_URL,EVIDENCE_TYPE,EVIDENCE_NOTE\\n"
                "BALLARPUR,INE294A01037,BALLARPUR INDUSTRIES LIMITED,"
                "https://nsearchives.nseindia.com/corporate/ixbrl/example.html,"
                "OFFICIAL_NSE_IXBRL,official\\n",
                encoding="utf-8",
            )
            with patch.object(stage, "ROOT", root), patch.object(stage, "_SECURITY_ISIN_MAP", None):
                self.assertEqual(stage.security_isin("BALLARPUR", {"symbol": "BALLARPUR"}),
                                 "INE294A01037")
                self.assertEqual(stage.security_isin("KUNDANMM", {"symbol": "KUNDANMM"}), "")

    def test_structured_integrated_filing_is_result_and_uses_official_security_master_isin(self):
        row = {
            "symbol": "ABC", "companyName": "ABC Limited",
            "qe_Date": "30-SEP-2026", "broadcast_Date": "16-Oct-2026 20:00:00",
            "consolidated": "Consolidated",
            "xbrl": "https://nsearchives.nseindia.com/corporate/ABC.xbrl",
            "ixbrl": "https://nsearchives.nseindia.com/corporate/ABC.html",
        }
        with patch.object(stage, "_SECURITY_ISIN_MAP", {"ABC": "INE123A01011"}):
            normalized = stage.normalize_event(
                row, "RESULT_DISCLOSURE",
                "https://www.nseindia.com/api/integrated-filing-results")
        self.assertTrue(normalized["RESULT_DECLARED"])
        self.assertEqual(normalized["PERIOD_END"], "30-SEP-2026")
        self.assertEqual(normalized["ISIN"], "INE123A01011")
        self.assertEqual(normalized["SOURCE_URL"], row["xbrl"])

    def test_results_disclosure_flag_requires_result_event_type(self):
        row = {
            "symbol": "ABC", "companyName": "ABC Limited",
            "subject": "Outcome: Unaudited financial results for the quarter",
            "broadcastDate": "15-Oct-2026", "quarterEndDate": "30-Sep-2026", "attachment": "https://nsearchives.nseindia.com/corporate/result.pdf",
        }
        normalized = stage.normalize_event(row, "RESULT_DISCLOSURE", "https://www.nseindia.com/example")
        self.assertTrue(normalized["RESULT_DECLARED"])
        self.assertTrue(normalized["SOURCE_RECORD_SHA256"])

    def test_nse_announcement_date_alias_is_normalized(self):
        row = {
            "symbol": "ABC", "companyName": "ABC Limited",
            "subject": "Outcome: Unaudited financial results for the quarter",
            "an_dt": "15-Oct-2026", "periodEndDate": "30-Sep-2026",
        }
        normalized = stage.normalize_event(row, "RESULT_DISCLOSURE", "https://www.nseindia.com/api/corporates-announcements")
        self.assertTrue(normalized["RESULT_DECLARED"])
        self.assertTrue(normalized["BROADCAST_AT"])


    def test_clarification_and_delayed_submission_are_not_result_events(self):
        for subject in ("Reply to Clarification- Financial results",
                        "Reasons for Delayed/Non-submission of Financial Results"):
            row = {"symbol": "ABC", "subject": subject, "an_dt": "15-Oct-2026",
                   "periodEndDate": "30-Sep-2026"}
            normalized = stage.normalize_event(row, "RESULT_DISCLOSURE",
                                               "https://www.nseindia.com/api/integrated-filing-results")
            self.assertFalse(normalized["RESULT_DECLARED"])

    def test_reporting_period_alias_and_nse_attachment_source_are_preserved(self):
        row = {"symbol": "ABC", "subject": "Outcome: Unaudited financial results",
               "broadcastDateTime": "15-Oct-2026", "quarterEndDate": "30-Sep-2026",
               "xbrl": "https://nsearchives.nseindia.com/corporate/result.xml"}
        normalized = stage.normalize_event(row, "RESULT_DISCLOSURE",
                                           "https://www.nseindia.com/api/integrated-filing-results")
        self.assertTrue(normalized["RESULT_DECLARED"])
        self.assertEqual(normalized["PERIOD_END"], "30-Sep-2026")
        self.assertEqual(normalized["SOURCE_URL"], "https://nsearchives.nseindia.com/corporate/result.xml")


    def test_result_period_can_be_parsed_from_explicit_nse_filing_metadata(self):
        row = {"symbol": "ABC", "sm_isin": "INE123A01011",
               "desc": "Outcome of Board Meeting",
               "attchmntText": "The company has submitted financial results for the period ended September 30, 2026.",
               "an_dt": "16-Oct-2026 20:49:34"}
        normalized = stage.normalize_event(row, "RESULT_DISCLOSURE",
                                           "https://www.nseindia.com/api/corporate-announcements")
        self.assertEqual(normalized["PERIOD_END"], "2026-09-30")
        self.assertTrue(normalized["RESULT_DECLARED"])

    def test_board_calendar_reporting_period_is_not_mandatory(self):
        row = {"symbol": "ABC", "sm_isin": "INE123A01011",
               "desc": "Outcome of Board Meeting", "an_dt": "16-Oct-2026"}
        normalized = stage.normalize_event(row, "BOARD_MEETING",
                                           "https://www.nseindia.com/api/corporate-announcements")
        self.assertFalse(normalized["RESULT_DECLARED"])

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


    def test_run121_four_invalid_disclosures_preserve_provenance_and_unknown(self):
        """Exact Run #121 filing metadata; never guess a missing period."""
        cases = [
            ("MWL", "INE0JYY01011", "15-Oct-2026 19:27:10",
             "Submission of standalone and consolidated Unaudited Financial Results of the Company for the Quarter and half year ended on September 30, 2026.",
             "MWL_15102026192701_OUTCOMEOFBM15102026FINALSIGNED.pdf", "2026-09-30"),
            ("ADROITIND", "INE505M01015", "12-Oct-2026 15:38:52",
             "Outcome and financial results",
             "ADROIT_12102026153818_Outcome_of_Board_Meeting.pdf", ""),
            ("PRANAV", "INE0H4201019", "01-Oct-2026 19:48:20",
             "Integrated Filing (Financials) for the quarter ended 30th June, 2026",
             "PCPL_01102026194801_Integrated_Filing_Financials_Q1_30_June_2026.pdf", "2026-06-30"),
            ("TEMPSENS", "INE1KZI01025", "16-Sep-2026 19:26:26",
             "Unaudited Financial Results Standalone and Consolidated  for the Quarter ended 30th June, 2026",
             "TEMPSENS_16092026192542_Outcome__-_Copy.pdf", "2026-06-30"),
        ]
        for symbol, isin, timestamp, attachment_text, filename, expected_period in cases:
            with self.subTest(symbol=symbol):
                url = "https://nsearchives.nseindia.com/corporate/" + filename
                row = {"symbol": symbol, "sm_isin": isin, "an_dt": timestamp,
                       "desc": "Integrated Filing- Financial",
                       "attchmntText": attachment_text, "attchmntFile": url}
                normalized = stage.normalize_event(
                    row, "RESULT_DISCLOSURE",
                    "https://www.nseindia.com/api/corporate-announcements")
                self.assertEqual(normalized["SYMBOL"], symbol)
                self.assertEqual(normalized["ISIN"], isin)
                self.assertEqual(normalized["SOURCE_URL"], url)
                self.assertTrue(normalized["BROADCAST_AT"])
                self.assertEqual(normalized["PERIOD_END"], expected_period)
                self.assertEqual(normalized["RESULT_DECLARED"], bool(expected_period))
                self.assertEqual(normalized["SOURCE_RECORD_SHA256"], stage.digest(row))

    def test_period_aliases_are_explicit_and_conflicts_remain_unknown(self):
        examples = [
            ("quarter ended 30th June, 2026", "2026-06-30"),
            ("half-year ended on September 30, 2026", "2026-09-30"),
            ("period ended 2026-09-30", "2026-09-30"),
            ("financial year ended 31 March 2026", "2026-03-31"),
            ("quarter ended June 30, 2026 and half year ended September 30, 2026", ""),
            ("Q1 2026-27 results", ""),
        ]
        for text, expected in examples:
            with self.subTest(text=text):
                self.assertEqual(stage.parse_reporting_period({"attchmntText": text}), expected)




    def test_missing_broadcast_does_not_fall_back_to_creation_or_revision_time(self):
        row = {
            "symbol": "ABC", "sm_isin": "INE123A01011",
            "subject": "Unaudited financial results for the quarter ended September 30, 2026",
            "qe_Date": "30-SEP-2026", "broadcast_Date": None,
            "creation_Date": "16-Oct-2026 18:00:00",
            "revised_Date": "17-Oct-2026 09:30:00",
            "xbrl": "https://nsearchives.nseindia.com/corporate/ABC.xbrl",
        }
        normalized = stage.normalize_event(row, "RESULT_DISCLOSURE",
                                           "https://www.nseindia.com/api/integrated-filing-results")
        self.assertEqual(normalized["BROADCAST_AT"], "")
        self.assertEqual(normalized["REVISION_TIMESTAMP"], "2026-10-17T09:30:00+00:00")
        self.assertEqual(normalized["ORIGINAL_BROADCAST_AT"], "")
        self.assertEqual(normalized["PERIOD_END"], "30-SEP-2026")

    def test_revision_record_uses_revised_time_as_its_own_publication_time_only(self):
        row = {
            "symbol": "ABC", "sm_isin": "INE123A01011",
            "type_Sub": "Revision", "broadcast_Date": None,
            "creation_Date": "17-Oct-2026 09:31:00",
            "revised_Date": "17-Oct-2026 09:30:00",
            "qe_Date": "30-SEP-2026",
            "subject": "Financial results revised",
            "xbrl": "https://nsearchives.nseindia.com/corporate/ABC.xbrl",
        }
        normalized = stage.normalize_event(row, "RESULT_DISCLOSURE",
                                           "https://www.nseindia.com/api/integrated-filing-results")
        self.assertEqual(normalized["BROADCAST_AT"], "")
        self.assertEqual(normalized["REVISION_TIMESTAMP"], "2026-10-17T09:30:00+00:00")
        self.assertEqual(normalized["PUBLICATION_TIMESTAMP"], "2026-10-17T09:30:00+00:00")
        self.assertNotEqual(normalized["PUBLICATION_TIMESTAMP"], "2026-10-17T09:31:00+00:00")

    def test_revision_timestamp_is_preserved_separately_from_original_broadcast(self):
        row = {
            "symbol": "ABC", "sm_isin": "INE123A01011",
            "subject": "Unaudited financial results for the quarter ended September 30, 2026",
            "broadcast_Date": "16-Oct-2026 18:00:00",
            "originalBroadcastDateTime": "16-Oct-2026 17:55:00",
            "revised_Date": "17-Oct-2026 09:30:00",
            "qe_Date": "30-SEP-2026",
            "xbrl": "https://nsearchives.nseindia.com/corporate/ABC.xbrl",
        }
        normalized = stage.normalize_event(row, "RESULT_DISCLOSURE",
                                           "https://www.nseindia.com/api/integrated-filing-results")
        self.assertEqual(normalized["BROADCAST_AT"], "2026-10-16T18:00:00+00:00")
        self.assertEqual(normalized["ORIGINAL_BROADCAST_AT"], "2026-10-16T17:55:00+00:00")
        self.assertEqual(normalized["REVISION_TIMESTAMP"], "2026-10-17T09:30:00+00:00")

    def test_unresolved_isin_remains_unknown_without_official_mapping(self):
        row = {
            "symbol": "LEGACYXYZ", "subject": "Unaudited financial results for the quarter ended September 30, 2026",
            "broadcast_Date": "16-Oct-2026 18:00:00", "qe_Date": "30-SEP-2026",
            "xbrl": "https://nsearchives.nseindia.com/corporate/LEGACYXYZ.xbrl",
        }
        with patch.object(stage, "_SECURITY_ISIN_MAP", {}):
            normalized = stage.normalize_event(row, "RESULT_DISCLOSURE",
                                               "https://www.nseindia.com/api/integrated-filing-results")
        self.assertEqual(normalized["ISIN"], "")
        self.assertTrue(normalized["BROADCAST_AT"])
        self.assertEqual(normalized["RESULT_DECLARED"], True)

if __name__ == "__main__":
    unittest.main()
