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

    def test_official_treasury_fallback_parses_three_maturities_with_provenance(self):
        response = FakeResponse(
            "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve",
            b"Date,2 Yr,10 Yr,30 Yr\\n10/20/2026,3.51,4.01,4.62\\n10/21/2026,3.50,4.03,4.61\\n")
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

    def test_collected_factor_files_remain_warning_until_domain_qa_passes(self):
        import pipeline.macro_geo_source_coverage as coverage
        rows = [
            {"source": "us_yields", "rows": 25, "status": "AVAILABLE", "notes": "Generic QA passed."},
            {"source": "global_commodity_prices", "rows": 40, "status": "AVAILABLE", "notes": "Generic QA passed."},
        ]
        report = {"groups": {
            "us_yields": {"status": "COLLECTED_NEEDS_DOMAIN_QA", "rows": 25},
            "global_commodity_prices": {"status": "AVAILABLE_WITH_SOURCE_FAILURES", "rows": 40},
        }}
        result = coverage.apply_factor_collector_report(rows, report)
        self.assertTrue(all(row["status"] == "DATA_QUALITY_WARN" for row in result))
        self.assertTrue(all("domain/source QA not cleared" in row["notes"] for row in result))

    def test_factor_audit_does_not_count_warnings_or_missing_rows_as_connected(self):
        import pipeline.macro_geo_factor_coverage_audit as audit
        self.assertTrue(audit.source_is_connected({"status": "AVAILABLE", "rows": 3}))
        self.assertFalse(audit.source_is_connected({"status": "DATA_QUALITY_WARN", "rows": 3}))
        self.assertFalse(audit.source_is_connected({"status": "AVAILABLE", "rows": 0}))
        self.assertFalse(audit.source_is_connected({"status": "NOT_CONNECTED", "rows": 0}))

    def test_observed_window_blocks_without_real_panel(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(collector, "PANEL_CANDIDATES", (Path(tmp) / "missing.csv",)):
                with self.assertRaisesRegex(RuntimeError, "No observed NSE equity or benchmark panel"):
                    collector.observed_window()


if __name__ == "__main__":
    unittest.main()
