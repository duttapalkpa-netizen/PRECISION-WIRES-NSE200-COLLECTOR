import tempfile
import unittest
from pathlib import Path
import pandas as pd
from pipeline import macro_geo_corporate_events_bridge as bridge

class CorporateEventsBridgeTests(unittest.TestCase):
    def test_requires_official_source_symbol_and_publication_time(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"rows.csv"
            pd.DataFrame([
                {"SYMBOL":"ABC","PUBLICATION_TIMESTAMP":"2026-10-28T10:00:00Z","SOURCE_URL":"https://www.nseindia.com/disclosure","SUBJECT":"Results"},
                {"SYMBOL":"XYZ","PUBLICATION_TIMESTAMP":"2026-10-28T10:00:00Z","SOURCE_URL":"https://example.com/x"},
                {"SYMBOL":"","PUBLICATION_TIMESTAMP":"2026-10-28T10:00:00Z","SOURCE_URL":"https://www.nseindia.com/x"},
                {"SYMBOL":"DEF","PUBLICATION_TIMESTAMP":"","SOURCE_URL":"https://www.nseindia.com/y"},
            ]).to_csv(p,index=False)
            rows,report=bridge.read_rows(p,"TEST")
            self.assertEqual(len(rows),1)
            self.assertEqual(rows[0]["SYMBOL"],"ABC")
            self.assertEqual(rows[0]["DATE"],"2026-10-28")
            self.assertEqual(rows[0]["EVENT_DATE_BASIS"],"PUBLICATION_DATE_NOT_CONFIRMED_OCCURRENCE_DATE")
            self.assertEqual(report["rejected"]["non_official_source_url"],1)
            self.assertEqual(report["rejected"]["missing_symbol"],1)
            self.assertEqual(report["rejected"]["missing_publication_timestamp"],1)
    def test_missing_input_does_not_invent_rows(self):
        rows,report=bridge.read_rows(Path("/does/not/exist.csv"),"TEST")
        self.assertEqual(rows,[])
        self.assertEqual(report["status"],"MISSING_INPUT")

if __name__=="__main__": unittest.main()
