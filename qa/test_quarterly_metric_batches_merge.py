import unittest
import pandas as pd
from pipeline.quarterly_metric_batches_merge import apply_global_revision_policy

def row(symbol, disclosed, status="SOURCE_LINKED_XBRL_FACTS", digest="a"*64, value="100", content_type="application/xml"):
    return {
        "SYMBOL": symbol, "PERIOD_END": "2026-09-30", "BASIS": "STANDALONE",
        "DISCLOSED_AT": disclosed, "SOURCE_URL": f"https://nsearchives.nseindia.com/{symbol}/{disclosed}",
        "SOURCE_SHA256": digest, "SOURCE_CONTENT_TYPE": content_type,
        "REVENUE": value, "PAT": "10", "EPS": "1",
        "EXTRACTION_STATUS": status
    }

class GlobalQuarterlyRevisionTests(unittest.TestCase):
    def test_cross_batch_later_disclosure_supersedes_earlier_row(self):
        d = pd.DataFrame([
            row("ABC", "2026-10-20T10:00:00Z", "SUPERSEDED_BY_LATER_DISCLOSURE"),
            row("ABC", "2026-10-22T10:00:00Z")
        ])
        out = apply_global_revision_policy(d)
        self.assertEqual(out.iloc[0]["EXTRACTION_STATUS"], "SUPERSEDED_BY_LATER_DISCLOSURE")
        self.assertEqual(out.iloc[1]["EXTRACTION_STATUS"], "SOURCE_LINKED_XBRL_FACTS")

    def test_equal_latest_timestamps_fail_closed(self):
        d = pd.DataFrame([
            row("ABC", "2026-10-22T10:00:00Z", digest="a"*64),
            row("ABC", "2026-10-22T10:00:00Z", digest="b"*64)
        ])
        out = apply_global_revision_policy(d)
        self.assertTrue(out["EXTRACTION_STATUS"].eq("BLOCKED_AMBIGUOUS_LATEST_PERIOD_BASIS").all())
        self.assertTrue(out[["REVENUE", "PAT", "EPS"]].eq("").all().all())

    def test_incomplete_superseded_row_is_not_promoted(self):
        d = pd.DataFrame([
            row("ABC", "2026-10-20T10:00:00Z", "SUPERSEDED_BY_LATER_DISCLOSURE", digest="", value=""),
            row("ABC", "2026-10-22T10:00:00Z")
        ])
        out = apply_global_revision_policy(d)
        self.assertEqual(out.iloc[0]["EXTRACTION_STATUS"], "BLOCKED_SUPERSEDED_ROW_WITH_INCOMPLETE_EVIDENCE")

    def test_nse_html_table_source_is_retained_and_participates_in_revision_policy(self):
        d = pd.DataFrame([
            row("ABC", "2026-10-20T10:00:00Z", "SOURCE_LINKED_NSE_HTML_TABLE_FACTS",
                content_type="text/html"),
            row("ABC", "2026-10-22T10:00:00Z", "SOURCE_LINKED_XBRL_FACTS")
        ])
        out = apply_global_revision_policy(d)
        self.assertEqual(out.iloc[0]["EXTRACTION_STATUS"], "SUPERSEDED_BY_LATER_DISCLOSURE")
        self.assertEqual(out.iloc[1]["EXTRACTION_STATUS"], "SOURCE_LINKED_XBRL_FACTS")

    def test_prior_superseded_html_fact_restores_as_html_not_xbrl(self):
        d = pd.DataFrame([
            row("ABC", "2026-10-20T10:00:00Z", "SUPERSEDED_BY_LATER_DISCLOSURE",
                content_type="text/html")
        ])
        out = apply_global_revision_policy(d)
        self.assertEqual(out.iloc[0]["EXTRACTION_STATUS"], "SOURCE_LINKED_NSE_HTML_TABLE_FACTS")

if __name__ == "__main__":
    unittest.main()
