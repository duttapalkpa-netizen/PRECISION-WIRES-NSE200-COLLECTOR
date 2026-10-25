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
        slash = chr(92)
        body = '<script>const data = "https:' + slash + '/' + slash + '/www.bbc.com' + slash + '/news' + slash + '/world-123456?x=1' + slash + 'u0026y=2";</script>'
        found = backfill.extract_article_urls("https://news.google.com/rss/articles/CBMi", body)
        self.assertTrue(any(u.startswith("https://www.bbc.com/news/world-123456") for u in found), found)

    def test_html_encoded_href_publisher_url_is_extracted(self):
        slash = chr(92)
        body = '<a href="https:' + slash + '/' + slash + '/www.bbc.com' + slash + '/news' + slash + '/world-123456">article</a>'
        found = backfill.extract_article_urls("https://news.google.com/rss/articles/CBMi", body)
        self.assertTrue(any(u.startswith("https://www.bbc.com/news/world-123456") for u in found), found)

    def test_gdelt_direct_publisher_url_can_be_verified_without_google_wrapper(self):
        from unittest.mock import Mock
        published_html = '<html><head><meta property="article:published_time" content="2026-08-12T09:15:00+00:00"></head></html>'
        client = Mock()
        response = Mock()
        response.url = "https://www.bbc.com/news/world-123456"
        response.text = published_html
        client.get.return_value = response
        row, reason = backfill.normalize_item(
            "Oil tanker shipping disruption in the Red Sea",
            "https://www.bbc.com/news/world-123456",
            "2026-08-12T09:15:00Z",
            "bbc.com",
            "bbc.com",
            client,
        )
        self.assertIsNone(reason)
        self.assertEqual(row["SOURCE_URL"], "https://www.bbc.com/news/world-123456")
        self.assertEqual(row["PUBLISHED_AT"], "2026-08-12T09:15:00+00:00")
        self.assertEqual(row["EVENT_DATE_BASIS"], "PUBLISHER_ARTICLE_PUBLICATION_TIMESTAMP")

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
