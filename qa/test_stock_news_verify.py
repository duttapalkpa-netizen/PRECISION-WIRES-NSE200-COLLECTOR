import json
from pathlib import Path

import pandas as pd
import requests

from pipeline import stock_news_verify as verifier


class FakeResponse:
    status_code = 200
    headers = {"Content-Type": "text/html; charset=utf-8"}
    text = "<html><head><title>Quarterly profit growth announced</title></head><body>Article</body></html>"

    def __init__(self, url):
        self.url = url

    def raise_for_status(self):
        return None


def test_google_news_url_is_decoded_and_canonicalized_after_headline_verification(tmp_path, monkeypatch):
    news = tmp_path / "news.csv"
    report = tmp_path / "verification.json"
    pd.DataFrame([{
        "HEADLINE": "Company announces quarterly profit growth",
        "CANONICAL_URL": "https://news.google.com/rss/articles/fake-id?oc=5",
        "VERIFICATION_STATUS": "UNVERIFIED_GOOGLE_NEWS_RSS_MATCH",
    }]).to_csv(news, index=False)
    monkeypatch.setattr(verifier, "NEWS", news)
    monkeypatch.setattr(verifier, "REPORT", report)
    monkeypatch.setattr(verifier, "gnewsdecoder", lambda url, interval=1, **kwargs: {
        "success": True, "decoded_url": "https://publisher.example/article"
    })
    monkeypatch.setattr(verifier.requests, "get", lambda url, **kwargs: FakeResponse(url))

    assert verifier.main() == 0
    result = pd.read_csv(news, dtype=str).fillna("")
    summary = json.loads(report.read_text(encoding="utf-8"))
    assert result.loc[0, "CANONICAL_URL"] == "https://publisher.example/article"
    assert result.loc[0, "VERIFICATION_STATUS"] == "VERIFIED"
    assert summary["verified_rows_total"] == 1
    assert summary["unverified_rows_remaining"] == 0


def test_failed_google_news_decode_remains_unverified(tmp_path, monkeypatch):
    news = tmp_path / "news.csv"
    report = tmp_path / "verification.json"
    pd.DataFrame([{
        "HEADLINE": "Company announces quarterly profit growth",
        "CANONICAL_URL": "https://news.google.com/rss/articles/fake-id?oc=5",
        "VERIFICATION_STATUS": "UNVERIFIED_GOOGLE_NEWS_RSS_MATCH",
    }]).to_csv(news, index=False)
    monkeypatch.setattr(verifier, "NEWS", news)
    monkeypatch.setattr(verifier, "REPORT", report)
    monkeypatch.setattr(verifier, "gnewsdecoder", lambda url, interval=1, **kwargs: {
        "status": False, "message": "simulated decode failure"
    })

    assert verifier.main() == 0
    result = pd.read_csv(news, dtype=str).fillna("")
    summary = json.loads(report.read_text(encoding="utf-8"))
    assert result.loc[0, "VERIFICATION_STATUS"] != "VERIFIED"
    assert summary["verified_rows_total"] == 0
    assert summary["unverified_rows_remaining"] == 1
