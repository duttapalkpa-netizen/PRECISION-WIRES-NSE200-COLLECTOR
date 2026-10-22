import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock
import pandas as pd
import requests

import pipeline.stock_news_24h_collect as collector


RSS = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
<title>Google News</title>
<item><title>Example Co announces quarterly results</title>
<link>https://example.com/story</link>
<pubDate>Wed, 14 Oct 2026 10:00:00 +0000</pubDate>
<source>Example News</source></item>
<item><title>Out of window article</title>
<link>https://example.com/old</link>
<pubDate>Mon, 12 Oct 2026 10:00:00 +0000</pubDate>
<source>Example News</source></item>
</channel></rss>"""


class FakeResponse:
    def __init__(self, status=200, content=b"", payload=None):
        self.status_code = status
        self.content = content
        self._payload = payload
        self.headers = {}

    def raise_for_status(self):
        if self.status_code >= 400:
            error = requests.HTTPError("HTTP {}".format(self.status_code))
            error.response = self
            raise error

    def json(self):
        return self._payload


class GoogleNewsFallbackTests(unittest.TestCase):
    def run_collector(self, first_gdelt_response):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            picks = root / "picks.csv"
            picks.parent.mkdir(parents=True, exist_ok=True)
            pd.DataFrame([{"CUT_OFF": "2026-10-14", "SYMBOL": "TESTCO"}]).to_csv(picks, index=False)
            news_out = root / "news.csv"
            coverage_out = root / "coverage.csv"
            report_out = root / "report.json"

            session = MagicMock()
            session.__enter__.return_value = session
            session.__exit__.return_value = False
            session.headers = {}
            session.get.side_effect = [first_gdelt_response, FakeResponse(content=RSS)]

            with patch.object(collector, "PICKS", picks), \
                 patch.object(collector, "NEWS_OUT", news_out), \
                 patch.object(collector, "COVERAGE_OUT", coverage_out), \
                 patch.object(collector, "REPORT_OUT", report_out), \
                 patch.object(collector.requests, "Session", return_value=session), \
                 patch.object(collector, "MAX_RETRIES", 1), \
                 patch.object(collector.time, "sleep"):
                self.assertEqual(collector.main(), 0)

            news = pd.read_csv(news_out)
            coverage = pd.read_csv(coverage_out)
            report = __import__("json").loads(report_out.read_text())
            return news, coverage, report, session

    def test_http_429_falls_back_to_rss_and_preserves_unverified_status(self):
        response = FakeResponse(status=429)
        news, coverage, report, session = self.run_collector(response)
        self.assertEqual(len(coverage), 1)
        self.assertEqual(coverage.iloc[0]["COVERAGE_STATUS"], "COMPLETE")
        self.assertEqual(coverage.iloc[0]["SOURCE_SCOPE"], "GOOGLE_NEWS_RSS_SYMBOL_QUERY")
        self.assertTrue(str(coverage.iloc[0]["SOURCE_URL"]).startswith("https://news.google.com/rss/search?"))
        self.assertEqual(len(news), 1, "only in-window RSS article should be retained")
        self.assertEqual(news.iloc[0]["CANONICAL_URL"], "https://example.com/story")
        self.assertEqual(news.iloc[0]["SOURCE_TYPE"], "GOOGLE_NEWS_RSS_DISCOVERY")
        self.assertEqual(news.iloc[0]["VERIFICATION_STATUS"], "UNVERIFIED_GOOGLE_NEWS_RSS_MATCH")
        self.assertEqual(report["queries_failed"], 0)
        self.assertEqual(report["coverage_unknown_rows"], 0)
        self.assertEqual(session.get.call_count, 2)

    def test_timeout_falls_back_to_rss(self):
        news, coverage, report, _ = self.run_collector(requests.Timeout("mock timeout"))
        self.assertEqual(coverage.iloc[0]["COVERAGE_STATUS"], "COMPLETE")
        self.assertEqual(len(news), 1)
        self.assertIn("GDELT fallback used", coverage.iloc[0]["ERROR"])

    def test_invalid_rss_xml_keeps_coverage_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            picks = root / "picks.csv"
            pd.DataFrame([{"CUT_OFF": "2026-10-14", "SYMBOL": "TESTCO"}]).to_csv(picks, index=False)
            session = MagicMock()
            session.__enter__.return_value = session
            session.__exit__.return_value = False
            session.headers = {}
            session.get.side_effect = [FakeResponse(status=429), FakeResponse(content=b"<rss><channel>")]
            with patch.object(collector, "PICKS", picks), \
                 patch.object(collector, "NEWS_OUT", root / "news.csv"), \
                 patch.object(collector, "COVERAGE_OUT", root / "coverage.csv"), \
                 patch.object(collector, "REPORT_OUT", root / "report.json"), \
                 patch.object(collector.requests, "Session", return_value=session), \
                 patch.object(collector, "MAX_RETRIES", 1), \
                 patch.object(collector.time, "sleep"):
                collector.main()
            coverage = pd.read_csv(root / "coverage.csv")
            self.assertEqual(coverage.iloc[0]["COVERAGE_STATUS"], "UNKNOWN")
            self.assertIn("GoogleNewsRSS", coverage.iloc[0]["ERROR"])
            report = __import__("json").loads((root / "report.json").read_text())
            self.assertEqual(report["queries_failed"], 1)
            self.assertEqual(report["coverage_unknown_rows"], 1)


if __name__ == "__main__":
    unittest.main()
