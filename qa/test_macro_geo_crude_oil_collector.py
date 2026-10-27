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
            collector.collect(session=Bad())

if __name__ == "__main__": unittest.main()
