import sys
import unittest
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))
import macro_geo_historical_news_backfill as backfill


class HistoricalNewsBackfillTests(unittest.TestCase):
    def test_encoded_destination_query_extracts_trusted_article_url(self):
        url = "https://news.google.com/rss/articles/CBMi?url=https%3A%2F%2Fwww.bbc.com%2Fnews%2Fworld-123456"
        found = backfill.extract_article_urls(url)
        self.assertIn("https://www.bbc.com/news/world-123456", found)

    def test_escaped_publisher_url_in_google_page_body_is_normalized(self):
        body = r'''<script>const data = "https:\\/\\/www.bbc.com\\/news\\/world-123456?x=1\\u0026y=2";</script>'''
        found = backfill.extract_article_urls("https://news.google.com/rss/articles/CBMi", body)
        self.assertTrue(any(u.startswith("https://www.bbc.com/news/world-123456") for u in found), found)

    def test_html_encoded_href_publisher_url_is_extracted(self):
        body = r'''<a href="https:\\/\\/www.bbc.com\\/news\\/world-123456">article</a>'''
        found = backfill.extract_article_urls("https://news.google.com/rss/articles/CBMi", body)
        self.assertTrue(any(u.startswith("https://www.bbc.com/news/world-123456") for u in found), found)

    def test_untrusted_or_non_article_url_is_not_accepted(self):
        url = "https://news.google.com/rss/articles/CBMi?url=https%3A%2F%2Fexample.com%2Fshort"
        self.assertEqual(backfill.extract_article_urls(url), [])

    def test_publisher_timestamp_from_article_published_metadata(self):
        html = '<html><head><meta property="article:published_time" content="2026-07-28T09:15:00+00:00"></head></html>'
        stamp = backfill.parse_publisher_timestamp(html)
        self.assertEqual(stamp, datetime(2026, 7, 28, 9, 15, tzinfo=timezone.utc))

    def test_rss_timestamp_alone_is_not_used_as_publisher_timestamp(self):
        self.assertIsNone(backfill.parse_publisher_timestamp("<html><head></head><body>no timestamp</body></html>"))


if __name__ == "__main__":
    unittest.main()
