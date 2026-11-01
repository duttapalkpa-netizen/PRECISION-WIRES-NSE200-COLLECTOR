import unittest
from unittest.mock import patch

import requests

from collector.nse_download import get_with_bounded_retry


class FakeResponse:
    def __init__(self, status, headers=None, content=b"payload"):
        self.status_code = status
        self.headers = headers or {}
        self.content = content


class FakeSession:
    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.calls = 0

    def get(self, url, timeout):
        self.calls += 1
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


class BoundedRetryTests(unittest.TestCase):
    def test_429_then_200_honors_retry_after_and_records_each_attempt(self):
        session = FakeSession([
            FakeResponse(429, {"Retry-After": "2"}),
            FakeResponse(200),
        ])
        diagnostics = []
        with patch("collector.nse_download.time.sleep") as sleep:
            response = get_with_bounded_retry(
                session, "https://example.test/nse", (1, 2), diagnostics,
                max_attempts=3, max_delay=5,
            )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(session.calls, 2)
        self.assertEqual([x["http_status"] for x in diagnostics], [429, 200])
        self.assertEqual([x["attempt"] for x in diagnostics], [1, 2])
        sleep.assert_called_once_with(2.0)

    def test_403_is_permanent_and_not_retried(self):
        session = FakeSession([FakeResponse(403)])
        diagnostics = []
        with patch("collector.nse_download.time.sleep") as sleep:
            response = get_with_bounded_retry(session, "https://example.test/nse", 2, diagnostics)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(session.calls, 1)
        self.assertEqual(len(diagnostics), 1)
        sleep.assert_not_called()

    def test_500_retries_but_stops_at_attempt_cap(self):
        session = FakeSession([FakeResponse(500), FakeResponse(503), FakeResponse(500)])
        diagnostics = []
        with patch("collector.nse_download.time.sleep") as sleep:
            response = get_with_bounded_retry(
                session, "https://example.test/nse", 2, diagnostics, max_attempts=3
            )
        self.assertEqual(response.status_code, 500)
        self.assertEqual(session.calls, 3)
        self.assertEqual(len(diagnostics), 3)
        self.assertEqual([x["attempt"] for x in diagnostics], [1, 2, 3])
        self.assertEqual([c.args[0] for c in sleep.call_args_list], [0.5, 1.0])

    def test_timeout_retries_and_records_error_then_success(self):
        session = FakeSession([requests.Timeout("read timed out"), FakeResponse(200)])
        diagnostics = []
        with patch("collector.nse_download.time.sleep"):
            response = get_with_bounded_retry(
                session, "https://example.test/nse", 2, diagnostics, max_attempts=3
            )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(session.calls, 2)
        self.assertIn("Timeout", diagnostics[0]["error"])
        self.assertEqual(diagnostics[1]["http_status"], 200)

    def test_retry_after_is_capped(self):
        session = FakeSession([FakeResponse(429, {"Retry-After": "999"}), FakeResponse(200)])
        with patch("collector.nse_download.time.sleep") as sleep:
            response = get_with_bounded_retry(
                session, "https://example.test/nse", 2, max_attempts=2, max_delay=3
            )
        self.assertEqual(response.status_code, 200)
        sleep.assert_called_once_with(3.0)


if __name__ == "__main__":
    unittest.main()
