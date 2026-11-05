import json, tempfile, unittest
from pathlib import Path
from pipeline.nse_source_provenance import build_entry, parse_time

class SourceProvenanceTest(unittest.TestCase):
    def test_retrieval_and_publication_times_are_distinct(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); p=root/"equity.csv"
            p.write_text("SYMBOL,ISIN\nABC,INE000000001\n",encoding="utf-8")
            item={"name":"equity","path":"equity.csv","source_url":"https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
                  "report_date":"2026-11-04","retrieved_at":"2026-11-05T10:00:00+05:30",
                  "published_at":"","content_type":"text/csv"}
            got=build_entry(item,root)
            self.assertIsNone(got["published_at"])
            self.assertEqual(got["record_count"],1)
            self.assertEqual(len(got["sha256"]),64)
            self.assertEqual(got["columns"],["SYMBOL","ISIN"])

    def test_timezone_required(self):
        with self.assertRaisesRegex(ValueError,"timezone"):
            parse_time("2026-11-05T10:00:00","retrieved_at",True)

    def test_non_https_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/"x.csv").write_text("A\n1\n")
            item={"name":"x","path":"x.csv","source_url":"http://example.com/x.csv",
                  "report_date":"2026-11-04","retrieved_at":"2026-11-05T10:00:00Z","content_type":"text/csv"}
            with self.assertRaisesRegex(ValueError,"HTTPS"):
                build_entry(item,root)

    def test_duplicate_normalized_headers_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/"x.csv").write_text("Trading Symbol,TRADING-SYMBOL\nA,A\n")
            item={"name":"x","path":"x.csv","source_url":"https://example.com/x.csv",
                  "report_date":"2026-11-04","retrieved_at":"2026-11-05T10:00:00Z","content_type":"text/csv"}
            with self.assertRaisesRegex(ValueError,"duplicate normalized"):
                build_entry(item,root)

    def test_missing_file_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            item={"name":"x","path":"missing.csv","source_url":"https://example.com/x.csv",
                  "report_date":"2026-11-04","retrieved_at":"2026-11-05T10:00:00Z","content_type":"text/csv"}
            with self.assertRaisesRegex(ValueError,"not found"):
                build_entry(item,Path(d))

if __name__ == "__main__":
    unittest.main()
