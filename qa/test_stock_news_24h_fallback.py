import json
from pathlib import Path
from email.utils import format_datetime
from datetime import datetime, timezone

import pandas as pd
import pytest
import requests

from pipeline import stock_news_24h_collect as collector


class FakeResponse:
    def __init__(self, content=b"", status=200, payload=None):
        self.content = content
        self.status_code = status
        self.headers = {}
        self._payload = payload

    def raise_for_status(self):
        if self.status_code >= 400:
            response = requests.Response()
            response.status_code = self.status_code
            raise requests.HTTPError(f"HTTP {self.status_code}", response=response)

    def json(self):
        if isinstance(self._payload, Exception):
            raise self._payload
        return self._payload


class FakeSession:
    def __init__(self, responses):
        self.headers = {}
        self.responses = list(responses)
        self.calls = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        item = self.responses.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


@pytest.mark.parametrize("failure", ["429", "timeout"])
def test_gdelt_failure_falls_back_to_rss_and_writes_schema(tmp_path, monkeypatch, failure):
    picks = tmp_path / "picks.csv"
    pd.DataFrame([{"CUT_OFF": "2026-10-14", "SYMBOL": "TESTCO"}]).to_csv(picks, index=False)
    monkeypatch.setattr(collector, "PICKS", picks)
    monkeypatch.setattr(collector, "RAW", tmp_path / "raw")
    monkeypatch.setattr(collector, "NEWS_OUT", tmp_path / "raw" / "stock_news_events.csv")
    monkeypatch.setattr(collector, "COVERAGE_OUT", tmp_path / "raw" / "stock_news_coverage.csv")
    monkeypatch.setattr(collector, "REPORT_OUT", tmp_path / "out" / "report.json")
    monkeypatch.setattr(collector, "MAX_RETRIES", 1)
    monkeypatch.setattr(collector.time, "sleep", lambda *_: None)

    if failure == "429":
        gdelt_failure = requests.HTTPError("429", response=requests.Response())
        gdelt_failure.response.status_code = 429
    else:
        gdelt_failure = requests.Timeout("simulated timeout")

    # Within the 24h window before 2026-10-14 15:30 Asia/Kolkata.
    pub = format_datetime(datetime(2026, 10, 14, 8, 0, tzinfo=timezone.utc))
    xml = f"""<?xml version="1.0"?><rss><channel><item>
      <title>TESTCO announces a verified-looking but unverified update</title>
      <link>https://example.com/story</link><pubDate>{pub}</pubDate>
      <source>Example News</source>
    </item></channel></rss>""".encode()
    session = FakeSession([gdelt_failure, FakeResponse(xml)])
    monkeypatch.setattr(collector.requests, "Session", lambda: session)

    assert collector.main() == 0
    news = pd.read_csv(tmp_path / "raw" / "stock_news_events.csv", dtype=str).fillna("")
    coverage = pd.read_csv(tmp_path / "raw" / "stock_news_coverage.csv", dtype=str).fillna("")
    report = json.loads((tmp_path / "out" / "report.json").read_text())

    assert list(news.columns) == ["EVENT_ID", "CUT_OFF", "SYMBOL", "PUBLISHED_AT", "PUBLISHER", "HEADLINE", "CANONICAL_URL", "SOURCE_TYPE", "VERIFICATION_STATUS"]
    assert len(news) == 1
    assert news.iloc[0]["CANONICAL_URL"] == "https://example.com/story"
    assert news.iloc[0]["SOURCE_TYPE"] == "GOOGLE_NEWS_RSS_DISCOVERY"
    assert news.iloc[0]["VERIFICATION_STATUS"] == "UNVERIFIED_GOOGLE_NEWS_RSS_MATCH"
    assert pd.notna(pd.to_datetime(news.iloc[0]["PUBLISHED_AT"], utc=True, errors="coerce"))
    assert coverage.iloc[0]["COVERAGE_STATUS"] == "COMPLETE"
    assert coverage.iloc[0]["SOURCE_URL"].startswith("https://news.google.com/rss/search?")
    assert report["coverage_complete_rows"] == 1
    assert report["coverage_unknown_rows"] == 0
    assert "UNVERIFIED" in report["verification"]


def test_malformed_rss_keeps_coverage_unknown(tmp_path, monkeypatch):
    picks = tmp_path / "picks.csv"
    pd.DataFrame([{"CUT_OFF": "2026-10-14", "SYMBOL": "TESTCO"}]).to_csv(picks, index=False)
    monkeypatch.setattr(collector, "PICKS", picks)
    monkeypatch.setattr(collector, "RAW", tmp_path / "raw")
    monkeypatch.setattr(collector, "NEWS_OUT", tmp_path / "raw" / "stock_news_events.csv")
    monkeypatch.setattr(collector, "COVERAGE_OUT", tmp_path / "raw" / "stock_news_coverage.csv")
    monkeypatch.setattr(collector, "REPORT_OUT", tmp_path / "out" / "report.json")
    monkeypatch.setattr(collector, "MAX_RETRIES", 1)
    monkeypatch.setattr(collector.time, "sleep", lambda *_: None)
    failure = requests.Timeout("simulated GDELT timeout")
    session = FakeSession([failure, FakeResponse(b"<rss><channel>")])
    monkeypatch.setattr(collector.requests, "Session", lambda: session)

    assert collector.main() == 0
    coverage = pd.read_csv(tmp_path / "raw" / "stock_news_coverage.csv", dtype=str).fillna("")
    report = json.loads((tmp_path / "out" / "report.json").read_text())
    assert coverage.iloc[0]["COVERAGE_STATUS"] == "UNKNOWN"
    assert report["coverage_unknown_rows"] == 1
    assert report["queries_failed"] == 1


def test_ambiguous_english_symbol_requires_explicit_ticker_not_prose():
    assert not collector.headline_relevant_to_symbol(
        "FOCUS", "Mawana Sugars slides as counter tests lower end of range - comes into Focus"
    )
    assert not collector.headline_relevant_to_symbol(
        "FOCUS", "Groww in Focus as Jefferies sees bigger gains"
    )
    assert collector.headline_relevant_to_symbol(
        "FOCUS", "NSE:FOCUS announces quarterly results"
    )
    assert collector.headline_relevant_to_symbol(
        "FOCUS", "FOCUS.NS shares jump after results"
    )
