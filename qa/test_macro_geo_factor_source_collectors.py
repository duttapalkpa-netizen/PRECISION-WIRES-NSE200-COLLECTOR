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
