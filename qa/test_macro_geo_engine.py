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
collector=load_module(ROOT/"pipeline/macro_geo_collect_p0.py","collector")
factor_audit=load_module(ROOT/"pipeline/macro_geo_factor_coverage_audit.py","factor_audit")
regime_study=load_module(ROOT/"pipeline/historical_regime_event_study.py","regime_study")

class MacroGeoTests(unittest.TestCase):
    def test_factor_registry_has_source_mapping_for_every_factor(self):
        registry=pd.read_csv(ROOT/"config/macro_factor_registry.csv")
        self.assertGreaterEqual(len(registry),35)
        self.assertEqual(set(registry["factor_id"].astype(str)),set(factor_audit.MAP.keys()))

    def test_historical_regime_registry_covers_requested_stress_episodes(self):
        regimes=pd.read_csv(ROOT/"config/macro_geo_historical_regimes.csv")
        labels=set(regimes["regime_label"].astype(str))
        for expected in ["GFC_2008_09","TAPER_TANTRUM_2013","ILFS_NBFC_LIQUIDITY_2018",
                         "COVID_CRASH_2020","RUSSIA_UKRAINE_ENERGY_FOOD_2022","YEN_CARRY_UNWIND_2024"]:
            self.assertIn(expected,labels)
        self.assertTrue((pd.to_datetime(regimes["start_date"],errors="coerce")<=pd.to_datetime(regimes["end_date"],errors="coerce")).all())

    def test_sector_rotation_hypotheses_are_not_marked_validated(self):
        sectors=pd.read_csv(ROOT/"config/macro_geo_sector_transmission_map.csv")
        self.assertTrue(sectors["empirical_status"].astype(str).eq("HYPOTHESIS_NOT_VALIDATED").all())
        self.assertTrue(sectors["sector"].astype(str).str.contains("Pharma healthcare|Pharma",case=False).any())

    def test_gdelt_broad_query_false_positive_is_rejected(self):
        self.assertIsNone(collector.classify("I review smartwatches and my favorite Garmin is on sale", "ENERGY_SHIPPING_NEWS"))
        self.assertEqual(collector.classify("Oil tanker traffic disrupted near Strait of Hormuz", "ENERGY_SHIPPING_NEWS"), "ENERGY_SHIPPING_NEWS")

    def test_only_trusted_publisher_domains_are_kept(self):
        self.assertTrue(collector.is_trusted_news_url("https://www.reuters.com/world/example"))
        self.assertTrue(collector.is_trusted_news_url("https://www.bbc.co.uk/news/example"))
        self.assertFalse(collector.is_trusted_news_url("https://www.tomsguide.com/wellness/example"))
        self.assertFalse(collector.is_trusted_news_url("https://reuters.com.evil.example/news"))

    def test_missing_inputs_are_blocked_not_fabricated(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"panel.csv"; e=Path(td)/"events.csv"
            panel,events,error=event.load_inputs(p,e)
            self.assertIsNone(panel); self.assertIsNone(events); self.assertIn("Missing input",error)

    def test_event_window_returns_are_reproducible(self):
        panel=pd.DataFrame({"DATE":pd.to_datetime(["2026-01-01","2026-01-02","2026-01-05","2026-01-06","2026-01-07","2026-01-08"]),
                            "SERIES":["NIFTY 50"]*6,"CLOSE":[100,101,102,103,104,105]})
        events=pd.DataFrame([{"EVENT_DATE":pd.Timestamp("2026-01-02"),"EVENT_ID":"E1","EVENT_TYPE":"OIL_SHOCK",
                              "PUBLISHED_AT":pd.Timestamp("2026-01-02T03:00:00Z"),"SOURCE":"official","CONFIDENCE":0.9}])
        result=event.compute_event_windows(panel,events)
        self.assertEqual(len(result),1)
        self.assertAlmostEqual(result.iloc[0]["RETURN_H1_PCT"],1.0)
        self.assertAlmostEqual(result.iloc[0]["RETURN_H5_PCT"],5.0)

    def test_after_close_event_uses_same_day_close_as_base(self):
        panel=pd.DataFrame({"DATE":pd.to_datetime(["2026-01-01","2026-01-02","2026-01-05","2026-01-06"]),
                            "SERIES":["NIFTY 50"]*4,"CLOSE":[100,101,102,103]})
        events=pd.DataFrame([{"EVENT_DATE":pd.Timestamp("2026-01-02"),"EVENT_ID":"E_AFTER","EVENT_TYPE":"GEO_NEWS",
                              "PUBLISHED_AT":pd.Timestamp("2026-01-02T11:00:00Z"),"SOURCE":"test","CONFIDENCE":0.5}])
        result=event.compute_event_windows(panel,events)
        self.assertEqual(len(result),1)
        self.assertEqual(result.iloc[0]["BASE_DATE"],"2026-01-02")
        self.assertEqual(result.iloc[0]["TARGET_DATE_H1"],"2026-01-05")
        self.assertAlmostEqual(result.iloc[0]["RETURN_H1_PCT"],(102/101-1)*100)


    def test_empty_events_file_is_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"panel.csv"; e=Path(td)/"events.csv"
            pd.DataFrame({"DATE":["2026-01-01"],"SERIES":["NIFTY 50"],"CLOSE":[100]}).to_csv(p,index=False)
            pd.DataFrame(columns=["EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT","SOURCE","SOURCE_URL","CONFIDENCE","EVENT_DATE_BASIS"]).to_csv(e,index=False)
            panel,events,error=event.load_inputs(p,e)
            self.assertIsNone(panel); self.assertIsNone(events); self.assertIn("no rows",error)

    def test_publication_timestamp_requires_timezone(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"panel.csv"; e=Path(td)/"events.csv"
            pd.DataFrame({"DATE":["2026-01-01","2026-01-02"],"SERIES":["NIFTY 50"]*2,"CLOSE":[100,101]}).to_csv(p,index=False)
            pd.DataFrame([{"EVENT_DATE":"2026-01-01","EVENT_ID":"E1","EVENT_TYPE":"GEO","PUBLISHED_AT":"2026-01-01 10:00:00",
                           "SOURCE":"example","SOURCE_URL":"https://example.com/news","CONFIDENCE":0.5,
                           "EVENT_DATE_BASIS":"GDELT_SEENDATE_PUBLICATION_PROXY"}]).to_csv(e,index=False)
            panel,events,error=event.load_inputs(p,e)
            self.assertIsNone(panel); self.assertIsNone(events); self.assertIn("timezone",error)

    def test_duplicate_panel_rows_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"panel.csv"; e=Path(td)/"events.csv"
            pd.DataFrame({"DATE":["2026-01-01","2026-01-01"],"SERIES":["NIFTY 50"]*2,"CLOSE":[100,101]}).to_csv(p,index=False)
            pd.DataFrame([{"EVENT_DATE":"2026-01-01","EVENT_ID":"DUP1","EVENT_TYPE":"GEO","PUBLISHED_AT":"2026-01-01T03:00:00Z",
                           "SOURCE":"example","SOURCE_URL":"https://example.com/news","CONFIDENCE":0.5,
                           "EVENT_DATE_BASIS":"GDELT_SEENDATE_PUBLICATION_PROXY"}]).to_csv(e,index=False)
            panel,events,error=event.load_inputs(p,e)
            self.assertIsNone(panel); self.assertIn("Duplicate",error)

if __name__=="__main__": unittest.main()
