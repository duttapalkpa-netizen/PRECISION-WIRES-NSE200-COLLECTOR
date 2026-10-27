import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from datetime import date
import requests
import pipeline.macro_geo_crude_oil_collector as collector

class FakeResponse:
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILBRENTEU"
    content = b"observation_date,DCOILBRENTEU\n2026-10-20,61.2\n2026-10-21,.\n2026-10-22,62.1\n"
    def raise_for_status(self): pass

class BrentCollectorTests(unittest.TestCase):
    def test_brent_schema_provenance_and_no_wti_substitution(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(collector, "OUT", Path(tmp)), patch.object(collector, "REPORT", Path(tmp)/"report.json"):
                result = collector.collect(session=type("S", (), {"headers":{}, "get":lambda self,*a,**k:FakeResponse()})(),
                                           start=date(2026,10,20), end=date(2026,10,22))
                import pandas as pd
                df = pd.read_csv(Path(tmp)/"brent_crude.csv")
        self.assertEqual(result["series"], "DCOILBRENTEU")
        self.assertEqual(df["DATE"].tolist(), ["2026-10-20","2026-10-22"])
        self.assertTrue((df["SOURCE_SERIES"] == "DCOILBRENTEU").all())
        self.assertTrue(df["SOURCE_URL"].str.contains("fred.stlouisfed.org").all())
        self.assertTrue((df["UNIT"] == "USD_PER_BARREL").all())

    def test_http_error_is_not_suppressed(self):
        class Bad:
            headers={}
            def get(self,*a,**k): raise requests.Timeout("timeout")
        with self.assertRaisesRegex(RuntimeError, "Yahoo futures fallback failed"):
            collector.collect(session=Bad(), start="2026-10-20", end="2026-10-22")


    def test_yahoo_brent_proxy_domain_qa_preserves_proxy_provenance(self):
        import pandas as pd
        frame = pd.DataFrame({
            "DATE": ["2026-10-23", "2026-10-26"],
            "CLOSE": [65.2, 66.1],
            "SOURCE": ["Yahoo Finance chart API; Brent crude futures proxy"] * 2,
            "SOURCE_SERIES": ["BZ=F"] * 2,
            "SOURCE_URL": ["https://query1.finance.yahoo.com/v8/finance/chart/BZ=F?period1=1"] * 2,
            "OBSERVED_AT_UTC": ["2026-10-27T00:00:00+00:00"] * 2,
            "UNIT": ["USD_PER_BARREL"] * 2,
        })
        result = collector.validate_brent_proxy(frame, "2026-10-26")
        self.assertEqual(result["status"], "COLLECTED_AND_DOMAIN_QA_PASSED")
        self.assertEqual(result["freshness_age_calendar_days"], 0)
        self.assertTrue(result["proxy_only"])
        self.assertIn("not equivalent to FRED Brent spot", result["domain_qa_boundary"])

    def test_yahoo_brent_proxy_domain_qa_rejects_future_or_stale_dates(self):
        import pandas as pd
        frame = pd.DataFrame({
            "DATE": ["2026-10-27"], "CLOSE": [66.1],
            "SOURCE": ["Yahoo Finance chart API; Brent crude futures proxy"],
            "SOURCE_SERIES": ["BZ=F"],
            "SOURCE_URL": ["https://query1.finance.yahoo.com/v8/finance/chart/BZ=F"],
            "OBSERVED_AT_UTC": ["2026-10-27T00:00:00+00:00"],
            "UNIT": ["USD_PER_BARREL"],
        })
        with self.assertRaisesRegex(ValueError, "freshness failed"):
            collector.validate_brent_proxy(frame, "2026-10-26")




    def test_fred_brent_domain_qa_accepts_provenance_and_freshness(self):
        import pandas as pd
        frame = pd.DataFrame({
            "DATE":["2026-10-26","2026-10-27"], "CLOSE":[65.2,66.0],
            "SOURCE":["Federal Reserve Bank of St. Louis FRED"]*2,
            "SOURCE_SERIES":["DCOILBRENTEU"]*2,
            "SOURCE_URL":["https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILBRENTEU"]*2,
            "OBSERVED_AT_UTC":["2026-10-27T00:00:00+00:00"]*2,
            "UNIT":["USD_PER_BARREL"]*2,
        })
        result = collector.validate_fred_brent(frame, "2026-10-27")
        self.assertEqual(result["status"], "COLLECTED_AND_DOMAIN_QA_PASSED")
        self.assertFalse(result["proxy_only"])
        self.assertEqual(result["freshness_age_calendar_days"], 0)

    def test_fred_brent_domain_qa_rejects_wrong_series(self):
        import pandas as pd
        frame = pd.DataFrame({
            "DATE":["2026-10-27"], "CLOSE":[66.0],
            "SOURCE":["Federal Reserve Bank of St. Louis FRED"],
            "SOURCE_SERIES":["DCOILWTICO"],
            "SOURCE_URL":["https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILWTICO"],
            "OBSERVED_AT_UTC":["2026-10-27T00:00:00+00:00"],
            "UNIT":["USD_PER_BARREL"],
        })
        with self.assertRaisesRegex(ValueError, "provenance must remain DCOILBRENTEU"):
            collector.validate_fred_brent(frame, "2026-10-27")


class BrentCoverageBoundaryTests(unittest.TestCase):
    def test_proxy_domain_qa_does_not_unblock_p0_as_fred_spot(self):
        from pipeline.macro_geo_source_coverage import apply_crude_oil_collector_report
        rows = [{"source":"crude_oil","rows":21,"status":"AVAILABLE","notes":"Generic QA passed."}]
        report = {"status":"COLLECTED_AND_DOMAIN_QA_PASSED","proxy_only":True,"series":"BZ=F"}
        out = apply_crude_oil_collector_report(rows, report)
        self.assertEqual(out[0]["status"], "DATA_QUALITY_WARN")
        self.assertIn("not FRED DCOILBRENTEU spot", out[0]["notes"])

    def test_missing_domain_qa_keeps_brent_warned(self):
        from pipeline.macro_geo_source_coverage import apply_crude_oil_collector_report
        rows = [{"source":"crude_oil","rows":21,"status":"AVAILABLE","notes":"Generic QA passed."}]
        out = apply_crude_oil_collector_report(rows, {"status":"COLLECTED_NEEDS_DOMAIN_QA"})
        self.assertEqual(out[0]["status"], "DATA_QUALITY_WARN")
        self.assertIn("domain QA not cleared", out[0]["notes"])

if __name__ == "__main__": unittest.main()
