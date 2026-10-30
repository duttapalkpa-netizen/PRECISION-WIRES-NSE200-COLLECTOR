import unittest
from datetime import date

from pipeline.macro_geo_nsdl_flows import scheduled_dii_sessions, page_diagnostic


class NsdlDiiCalendarTests(unittest.TestCase):
    def test_only_canonical_nse_sessions_are_queried(self):
        panel_dates = [
            date(2026, 6, 25), date(2026, 6, 29),
            date(2026, 9, 11), date(2026, 9, 15),
        ]
        got = scheduled_dii_sessions(panel_dates, date(2026, 6, 1), date(2026, 9, 30))
        # 26-Jun and 14-Sep are exchange holidays and therefore absent from
        # the canonical session panel; no NSDL request should be sent for them.
        self.assertEqual(got, [date(2026, 6, 25), date(2026, 6, 29),
                               date(2026, 9, 11), date(2026, 9, 15)])

    def test_no_data_page_is_distinguished_from_schema_drift(self):
        diag = page_diagnostic("<html><body><p>No Data Found</p></body></html>")
        self.assertTrue(diag["explicit_no_data_found"])
        self.assertEqual(diag["table_headers"], [])

    def test_schema_diagnostic_keeps_headers_bounded(self):
        page = """<table><tr><th>Type of DII</th><th>Instrument Type</th>
        <th>Investment Route</th><th>Net Investment (Rs. Crore)</th></tr>
        <tr><td>Bank</td><td>Equity</td><td>Stock Exchange</td><td>12.5</td></tr></table>"""
        diag = page_diagnostic(page)
        self.assertFalse(diag["explicit_no_data_found"])
        self.assertTrue(diag["table_headers"])
        self.assertIn("Type of DII", diag["table_headers"][0])


if __name__ == "__main__":
    unittest.main()
