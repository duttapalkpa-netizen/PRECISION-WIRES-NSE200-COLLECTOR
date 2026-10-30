import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

import pandas as pd
import requests
import pipeline.macro_geo_factor_source_collectors as collector


class FakeResponse:
    def __init__(self, url, content, status=200):
        self.url = url
        self.content = content
        self.text = content.decode("utf-8", errors="replace") if isinstance(content, bytes) else str(content)
        self.status_code = status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")


class FactorSourceCollectorTests(unittest.TestCase):
    def test_fred_parser_keeps_only_valid_observed_values_and_source_url(self):
        response = FakeResponse(
            "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10",
            b"observation_date,DGS10\n2026-10-20,4.01\n2026-10-21,.\n2026-10-22,4.03\n")
        session = type("Session", (), {"get": lambda self, *a, **kw: response})()
        rows = collector.fetch_fred(session, "DGS10", date(2026, 10, 20), date(2026, 10, 22))
        self.assertEqual([r[0] for r in rows], ["2026-10-20", "2026-10-22"])
        self.assertEqual(rows[0][1], 4.01)
        self.assertIn("fred.stlouisfed.org", rows[0][2])

    def test_fred_collector_recovers_from_two_transient_timeouts(self):
        response = FakeResponse(
            "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10",
            b"observation_date,DGS10\n2026-10-20,4.01\n")
        class FlakySession:
            def __init__(self):
                self.calls = 0
            def get(self, *args, **kwargs):
                self.calls += 1
                self.last_timeout = kwargs.get("timeout")
                if self.calls < 3:
                    raise requests.Timeout("transient upstream timeout")
                return response
        session = FlakySession()
        with patch("time.sleep", return_value=None):
            rows = collector.fetch_fred(session, "DGS10", date(2026, 10, 20), date(2026, 10, 20))
        self.assertEqual(len(rows), 1)
        self.assertEqual(session.calls, 3)
        self.assertEqual(session.last_timeout, (5, 12))
        self.assertEqual(rows[0][1], 4.01)

    def test_eia_wti_fallback_preserves_official_spot_identity_and_provenance(self):
        raw = pd.DataFrame([
            ["Series Description", "Cushing, OK WTI Spot Price FOB (Dollars per Barrel)"],
            ["Date", "Cushing, OK WTI Spot Price FOB (Dollars per Barrel)"],
            ["2026-10-20", 60.25],
            ["2026-10-21", 61.10],
        ])
        class FakeBook:
            sheet_names = ["Data 1"]
        response = FakeResponse("https://www.eia.gov/dnav/pet/hist_xls/RWTCd.xls", b"mock-xls")
        session = type("Session", (), {"get": lambda self, *a, **kw: response})()
        with patch.object(collector.pd, "ExcelFile", return_value=FakeBook()), \
             patch.object(collector.pd, "read_excel", return_value=raw):
            rows, report = collector.fetch_commodity_fallback(
                session, "DCOILWTICO", "WTI_CRUDE_USD_PER_BBL",
                date(2026, 10, 20), date(2026, 10, 21))
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["SOURCE_SERIES"], "RWTC")
        self.assertIn("US Energy Information Administration", rows[0]["SOURCE"])
        self.assertEqual(rows[0]["CLOSE"], 60.25)
        self.assertEqual(report["freshness_age_calendar_days"], 0)
        qa = collector.validate_observed_series_group(
            "global_commodity_prices", pd.DataFrame(rows), date(2026, 10, 20), date(2026, 10, 21),
            {"DCOILWTICO": "WTI_CRUDE_USD_PER_BBL"})
        self.assertEqual(qa["status"], "COLLECTED_AND_DOMAIN_QA_PASSED")

    def test_lbma_gold_fallback_preserves_exact_series_identity_and_provenance(self):
        payload = [
            {"d": "2026-10-20", "v": [4012.5, 3010.2, 3450.1]},
            {"d": "2026-10-21", "v": [4020.0, 3014.0, 3455.0]},
        ]
        class LBMAResponse:
            url = "https://prices.lbma.org.uk/json/gold_am.json"
            def raise_for_status(self): pass
            def json(self): return payload
        session = type("Session", (), {"get": lambda self, *a, **kw: LBMAResponse()})()
        rows, report = collector.fetch_commodity_fallback(
            session, "GOLDAMGBD228NLBM", "GOLD_USD_PER_TROY_OUNCE",
            date(2026, 10, 20), date(2026, 10, 21))
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["SOURCE_SERIES"], "LBMA_GOLD_AM_USD")
        self.assertIn("London Bullion Market Association", rows[0]["SOURCE"])
        self.assertEqual(rows[0]["CLOSE"], 4012.5)
        self.assertEqual(report["freshness_age_calendar_days"], 0)
        frame = pd.DataFrame(rows)
        qa = collector.validate_observed_series_group(
            "global_commodity_prices", frame, date(2026, 10, 20), date(2026, 10, 21),
            {"GOLDAMGBD228NLBM": "GOLD_USD_PER_TROY_OUNCE"})
        self.assertEqual(qa["status"], "COLLECTED_AND_DOMAIN_QA_PASSED")

    def test_dxy_collector_preserves_exchange_session_date_and_provider(self):
        from datetime import datetime, timezone, date
        class ChartResponse:
            url = "https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?interval=1d"
            def raise_for_status(self): pass
            def json(self):
                ts = [int(datetime(2026, 10, 20, 16, tzinfo=timezone.utc).timestamp()),
                      int(datetime(2026, 10, 21, 16, tzinfo=timezone.utc).timestamp())]
                return {"chart": {"result": [{
                    "timestamp": ts,
                    "meta": {"exchangeTimezoneName": "America/New_York"},
                    "indicators": {"quote": [{"close": [98.4, 98.7]}]}
                }], "error": None}}
        session = type("Session", (), {"get": lambda self, *a, **kw: ChartResponse()})()
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(collector, "OUT", Path(tmp)):
                report = collector.fetch_dxy_yahoo(session, date(2026, 10, 20), date(2026, 10, 21))
                frame = pd.read_csv(Path(tmp) / "dxy.csv")
        self.assertEqual(report["status"], "COLLECTED_AND_DOMAIN_QA_PASSED")
        self.assertIn("unique date keys", report["domain_qa_checks"])
        self.assertEqual(report["freshness_age_calendar_days"], 0)
        self.assertEqual(frame["DATE"].tolist(), ["2026-10-20", "2026-10-21"])
        self.assertEqual(frame["SOURCE_SERIES"].unique().tolist(), ["DX-Y.NYB"])
        self.assertTrue(frame["SOURCE_URL"].iloc[0].startswith("https://query1.finance.yahoo.com/"))

    def test_policy_rss_collector_preserves_url_and_publication_time_without_claiming_event_date(self):
        from datetime import date
        xml = (b'<?xml version="1.0"?><rss><channel><item>'
               b'<title>Federal Reserve announces monetary policy decision</title>'
               b'<link>https://www.federalreserve.gov/newsevents/pressreleases/monetary20261021a.htm</link>'
               b'<pubDate>Wed, 21 Oct 2026 18:00:00 GMT</pubDate>'
               b'</item></channel></rss>')
        response = FakeResponse("https://www.federalreserve.gov/feeds/press_all.xml", xml)
        session = type("Session", (), {"get": lambda self, *a, **kw: response})()
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(collector, "OUT", Path(tmp)):
                report = collector.fetch_global_policy_events(session, date(2026, 10, 20), date(2026, 10, 22))
                self.assertEqual(report["status"], "COLLECTED_NEEDS_DOMAIN_QA")
                frame = pd.read_csv(Path(tmp) / "global_policy_events.csv")
        self.assertEqual(len(frame), 1)
        self.assertEqual(frame.iloc[0]["PUBLISHED_AT"], "2026-10-21T18:00:00+00:00")
        self.assertEqual(frame.iloc[0]["EVENT_DATE_BASIS"], "PUBLICATION_DATE_PROXY_NOT_CONFIRMED_EVENT_DATE")
        self.assertTrue(frame.iloc[0]["SOURCE_URL"].startswith("https://www.federalreserve.gov/"))

    def test_official_treasury_fallback_parses_three_maturities_with_provenance(self):
        response = FakeResponse(
            "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve",
            b"Date,2 Yr,10 Yr,30 Yr\n10/20/2026,3.51,4.01,4.62\n10/21/2026,3.50,4.03,4.61\n")
        session = type("Session", (), {"get": lambda self, *a, **kw: response})()
        rows = collector.fetch_treasury_yields(session, date(2026, 10, 20), date(2026, 10, 21))
        self.assertEqual(len(rows), 6)
        self.assertEqual({r["SERIES"] for r in rows},
                         {"US_TREASURY_2Y", "US_TREASURY_10Y", "US_TREASURY_30Y"})
        self.assertTrue(all(r["SOURCE"] == "US Department of the Treasury" for r in rows))
        self.assertTrue(all(r["SOURCE_URL"].startswith("https://home.treasury.gov/") for r in rows))

    def test_schema_mismatch_fails_closed(self):
        response = FakeResponse("https://example.test", b"wrong,value\n2026-10-20,4.01\n")
        session = type("Session", (), {"get": lambda self, *a, **kw: response})()
        with self.assertRaisesRegex(ValueError, "schema mismatch"):
            collector.fetch_fred(session, "DGS10", date(2026, 10, 20), date(2026, 10, 22))

    def test_empty_or_missing_observations_do_not_create_rows(self):
        response = FakeResponse("https://example.test", b"observation_date,DGS10\n2026-10-20,.\n")
        session = type("Session", (), {"get": lambda self, *a, **kw: response})()
        with self.assertRaisesRegex(ValueError, "no valid observations"):
            collector.fetch_fred(session, "DGS10", date(2026, 10, 20), date(2026, 10, 22))

    def test_all_18_run145_missing_groups_have_explicit_source_inventory_contracts(self):
        import pipeline.macro_geo_source_coverage as coverage
        required = {
            "us_yields", "dxy", "global_policy_events", "fed_policy_surprises",
            "macro_indicators", "sector_fundamentals", "government_capex",
            "global_commodity_prices", "china_indicators", "india_bond_yields",
            "inflation_components", "fx_carry_and_cross_currency", "weather_agriculture",
            "global_freight_shipping", "ipo_float_unlocks", "market_microstructure",
            "research_house_actions", "earnings_revisions",
        }
        self.assertEqual(required - set(coverage.SOURCES), set())
        for name in required:
            self.assertTrue(coverage.SOURCES[name]["paths"], name)
            self.assertTrue(coverage.SOURCES[name]["required"], name)
            self.assertTrue({"SOURCE_URL", "OBSERVED_AT_UTC"}.issubset(set(coverage.SOURCES[name]["required"])), name)

    def test_collected_factor_files_remain_warning_until_domain_qa_passes(self):
        import pipeline.macro_geo_source_coverage as coverage
        rows = [
            {"source": "us_yields", "rows": 25, "status": "AVAILABLE", "notes": "Generic QA passed."},
            {"source": "global_commodity_prices", "rows": 40, "status": "AVAILABLE", "notes": "Generic QA passed."},
            {"source": "global_policy_events", "rows": 12, "status": "AVAILABLE", "notes": "Generic QA passed."},
        ]
        report = {"groups": {
            "us_yields": {"status": "COLLECTED_NEEDS_DOMAIN_QA", "rows": 25},
            "global_commodity_prices": {"status": "AVAILABLE_WITH_SOURCE_FAILURES", "rows": 40},
            "global_policy_events": {"status": "COLLECTED_NEEDS_DOMAIN_QA", "rows": 12},
        }}
        result = coverage.apply_factor_collector_report(rows, report)
        self.assertTrue(all(row["status"] == "DATA_QUALITY_WARN" for row in result))
        self.assertTrue(all("domain/source QA not cleared" in row["notes"] for row in result))
        failed_rows = [{"source": "us_yields", "rows": 3, "status": "SCHEMA_FAIL", "notes": "Missing SOURCE_URL"}]
        coverage.apply_factor_collector_report(failed_rows, {"groups": {"us_yields": {"status": "COLLECTED_NEEDS_DOMAIN_QA"}}})
        self.assertEqual(failed_rows[0]["status"], "SCHEMA_FAIL")

    def test_factor_audit_does_not_count_warnings_or_missing_rows_as_connected(self):
        import pipeline.macro_geo_factor_coverage_audit as audit
        self.assertTrue(audit.source_is_connected({"status": "AVAILABLE", "rows": 3}))
        self.assertFalse(audit.source_is_connected({"status": "DATA_QUALITY_WARN", "rows": 3}))
        self.assertFalse(audit.source_is_connected({"status": "AVAILABLE", "rows": 0}))
        self.assertFalse(audit.source_is_connected({"status": "NOT_CONNECTED", "rows": 0}))

    def test_every_factor_registry_mapping_resolves_to_a_source_contract(self):
        import pandas as pd
        import pipeline.macro_geo_factor_coverage_audit as audit
        import pipeline.macro_geo_source_coverage as coverage

        registry = pd.read_csv("config/macro_factor_registry.csv", dtype=str)
        factor_ids = set(registry["factor_id"].astype(str))
        self.assertEqual(factor_ids - set(audit.MAP), set(),
                         "Every registry factor must have an explicit source mapping")
        self.assertEqual(set(audit.MAP) - factor_ids, set(),
                         "Mapping must not reference a factor absent from the registry")
        mapped_groups = {name for names in audit.MAP.values() for name in names}
        self.assertEqual(mapped_groups - set(coverage.SOURCES), set(),
                         "Every mapped source group must have an explicit path/schema contract")
        for name in mapped_groups:
            self.assertTrue(coverage.SOURCES[name]["paths"], name)
            self.assertTrue(coverage.SOURCES[name]["required"], name)

    def test_observed_window_blocks_without_real_panel(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(collector, "PANEL_CANDIDATES", (Path(tmp) / "missing.csv",)):
                with self.assertRaisesRegex(RuntimeError, "No observed NSE equity or benchmark panel"):
                    collector.observed_window()


    def test_only_exact_reviewed_official_policy_pages_promote_event_dates(self):
        expected = {
            "https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm":
                ("2026-09-16", "FED_FOMC_POLICY_STATEMENT"),
            "https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm":
                ("2026-10-28", "FED_FOMC_POLICY_STATEMENT"),
            "https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp261029~9a493adf17.en.html":
                ("2026-10-29", "ECB_MONETARY_POLICY_DECISION"),
            "https://www.ecb.europa.eu/press/press_conference/monetary-policy-statement/2026/html/ecb.is261029~5c5ffe99e5.en.html":
                ("2026-10-29", "ECB_POLICY_PRESS_CONFERENCE"),
        }
        for url, (event_date, event_type) in expected.items():
            with self.subTest(url=url):
                result = collector.validate_official_policy_event_date(url)
                self.assertEqual(result["event_date"], event_date)
                self.assertEqual(result["event_type"], event_type)
                self.assertEqual(result["validation_method"],
                                 "EXACT_MATCH_TO_INDEPENDENTLY_REVIEWED_OFFICIAL_EVENT_PAGE")
        self.assertIsNone(collector.validate_official_policy_event_date(
            "https://www.federalreserve.gov/newsevents/pressreleases/monetary20261101a.htm"))
        self.assertIsNone(collector.validate_official_policy_event_date(
            "https://example.com/monetary20261028a.htm"))
        # RSS provider emits duplicate separators in some ECB href values;
        # canonicalization must still match only the same official host/path.
        normalized = collector.validate_official_policy_event_date(
            "https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.mp261029~9a493adf17.en.html")
        self.assertEqual(normalized["event_date"], "2026-10-29")
        self.assertEqual(normalized["event_type"], "ECB_MONETARY_POLICY_DECISION")

    def test_ecb_decision_and_press_conference_are_distinct_event_types_same_day(self):
        decision = collector.validate_official_policy_event_date(
            "https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp261029~9a493adf17.en.html")
        conference = collector.validate_official_policy_event_date(
            "https://www.ecb.europa.eu/press/press_conference/monetary-policy-statement/2026/html/ecb.is261029~5c5ffe99e5.en.html")
        self.assertEqual(decision["event_date"], conference["event_date"])
        self.assertNotEqual(decision["event_type"], conference["event_type"])


    def test_policy_event_reconciliation_promotes_only_complete_exactly_validated_rows(self):
        from pipeline.macro_geo_factor_coverage_reconcile import validate_policy_event_frame
        rows = [
            ("2026-09-16", "2026-09-16T18:00:00Z", "United States", "FED_FOMC_POLICY_STATEMENT",
             "https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm", "FEDERAL_RESERVE"),
            ("2026-10-28", "2026-10-28T18:00:00Z", "United States", "FED_FOMC_POLICY_STATEMENT",
             "https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm", "FEDERAL_RESERVE"),
            ("2026-10-29", "2026-10-29T12:15:00Z", "Euro Area", "ECB_MONETARY_POLICY_DECISION",
             "https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.mp261029~9a493adf17.en.html", "EUROPEAN_CENTRAL_BANK"),
            ("2026-10-29", "2026-10-29T13:45:00Z", "Euro Area", "ECB_POLICY_PRESS_CONFERENCE",
             "https://www.ecb.europa.eu//press/press_conference/monetary-policy-statement/2026/html/ecb.is261029~5c5ffe99e5.en.html", "EUROPEAN_CENTRAL_BANK"),
        ]
        frame = pd.DataFrame(rows, columns=["EVENT_DATE", "PUBLISHED_AT", "COUNTRY", "EVENT_TYPE", "SOURCE_URL", "SOURCE"])
        frame["TITLE"] = "Official policy release"
        frame["FEED_URL"] = "https://official.example/rss"
        frame["EVENT_DATE_BASIS"] = "INDEPENDENTLY_VALIDATED_EVENT_DATE"
        frame["OBSERVED_AT_UTC"] = "2026-10-30T06:00:00Z"
        result = validate_policy_event_frame(frame)
        self.assertEqual(result["status"], "VALIDATED")
        self.assertEqual(result["rows_eligible_for_event_study"], 4)
        self.assertTrue(result["schema_valid"])
        frame.loc[3, "EVENT_DATE"] = "2026-10-28"
        failed = validate_policy_event_frame(frame)
        self.assertEqual(failed["status"], "PARTIALLY_VALIDATED")
        self.assertEqual(failed["rows_eligible_for_event_study"], 3)
        self.assertEqual(failed["rows_not_eligible"], 1)


    def test_world_bank_gold_is_collected_as_monthly_not_daily_series(self):
        from datetime import date
        html = b'<a href="https://thedocs.worldbank.org/en/doc/example/related/CMO-Historical-Data-Monthly.xlsx">Monthly</a>'
        workbook = b"fake-xlsx"
        class Session:
            def __init__(self):
                self.calls = 0
            def get(self, url, **kwargs):
                self.calls += 1
                return FakeResponse(url, html if self.calls == 1 else workbook)
        monthly = pd.DataFrame({"Period": ["2026M08", "2026M09", "2026M10"],
                                "GOLD": [3400.0, 3450.0, 3500.0]})
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(collector, "OUT", Path(tmp)), patch.object(pd, "read_excel", return_value=monthly) as read:
                result = collector.fetch_world_bank_monthly_gold(
                    Session(), date(2026, 8, 1), date(2026, 10, 30))
                saved = pd.read_csv(Path(tmp) / "gold_prices_monthly.csv")
        self.assertEqual(result["status"], "COLLECTED_MONTHLY_DOMAIN_QA_PASSED")
        self.assertEqual(result["frequency"], "MONTHLY")
        self.assertEqual(result["unit"], "USD_PER_TROY_OUNCE")
        self.assertEqual(list(saved["DATE"]), ["2026-08-01", "2026-09-01"])
        self.assertTrue(saved["FREQUENCY"].eq("MONTHLY").all())
        self.assertTrue(saved["SOURCE"].str.contains("World Bank").all())
        self.assertEqual(read.call_args.kwargs["sheet_name"], "Monthly Prices")
        self.assertEqual(read.call_args.kwargs["skiprows"], 4)



if __name__ == "__main__":
    unittest.main()
