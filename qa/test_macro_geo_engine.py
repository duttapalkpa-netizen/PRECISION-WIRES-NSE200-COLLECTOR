import importlib.util
from pathlib import Path
import tempfile
import unittest
import pandas as pd

def load_module(path, name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

ROOT=Path(__file__).resolve().parents[1]
coverage=load_module(ROOT/"pipeline/macro_geo_source_coverage.py","coverage")
event=load_module(ROOT/"pipeline/macro_geo_event_study.py","event")

class MacroGeoTests(unittest.TestCase):
    def test_missing_inputs_are_blocked_not_fabricated(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"panel.csv"; e=Path(td)/"events.csv"
            panel,events,error=event.load_inputs(p,e)
            self.assertIsNone(panel); self.assertIsNone(events); self.assertIn("Missing input",error)

    def test_event_window_returns_are_reproducible(self):
        panel=pd.DataFrame({"DATE":pd.to_datetime(["2026-01-01","2026-01-02","2026-01-05","2026-01-06","2026-01-07"]),
                            "SERIES":["NIFTY 50"]*5,"CLOSE":[100,101,102,103,105]})
        events=pd.DataFrame([{"EVENT_DATE":pd.Timestamp("2026-01-02"),"EVENT_ID":"E1","EVENT_TYPE":"OIL_SHOCK",
                              "PUBLISHED_AT":pd.Timestamp("2026-01-02T03:00:00Z"),"SOURCE":"official","CONFIDENCE":0.9}])
        result=event.compute_event_windows(panel,events)
        self.assertEqual(len(result),1)
        self.assertAlmostEqual(result.iloc[0]["RETURN_H1_PCT"],2.0)
        self.assertAlmostEqual(result.iloc[0]["RETURN_H5_PCT"],5.0)

    def test_duplicate_panel_rows_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"panel.csv"; e=Path(td)/"events.csv"
            pd.DataFrame({"DATE":["2026-01-01","2026-01-01"],"SERIES":["NIFTY 50"]*2,"CLOSE":[100,101]}).to_csv(p,index=False)
            pd.DataFrame(columns=["EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT","SOURCE","CONFIDENCE"]).to_csv(e,index=False)
            panel,events,error=event.load_inputs(p,e)
            self.assertIsNone(panel); self.assertIn("Duplicate",error)

if __name__=="__main__": unittest.main()
