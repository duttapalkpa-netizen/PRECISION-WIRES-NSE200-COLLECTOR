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

    def test_gdelt_date_slices_are_bounded_and_cover_full_range(self):
        from datetime import date, timedelta
        slices=collector.build_date_slices(date(2026, 7, 1), date(2026, 9, 28), max_days=7)
        self.assertEqual(slices[0][0], date(2026, 7, 1))
        self.assertEqual(slices[-1][1], date(2026, 9, 28))
        self.assertEqual(slices[0][1], date(2026, 7, 7))
        self.assertTrue(all((end-start).days < 7 for start,end in slices))
        self.assertTrue(all(slices[i][1]+timedelta(days=1)==slices[i+1][0] for i in range(len(slices)-1)))
        with self.assertRaises(ValueError):
            collector.build_date_slices(date(2026, 1, 1), date(2026, 1, 2), max_days=0)

    def test_gdelt_timeout_falls_back_to_rss_and_preserves_auditable_fields(self):
        from datetime import date
        from unittest.mock import patch
        import requests

        class FakeResponse:
            def __init__(self, url, content=b"", status=200):
                self.url=url; self.content=content; self.status_code=status
                self.headers={}
            def raise_for_status(self):
                if self.status_code >= 400:
                    raise requests.HTTPError(f"HTTP {self.status_code}")
            def json(self):
                return {"articles": []}
            @property
            def text(self):
                return self.content.decode("utf-8", errors="replace")

        xml=(b'<?xml version="1.0"?><rss><channel><item>'
             b'<title>Oil tanker attack disrupts shipping near Strait of Hormuz</title>'
             b'<link>https://www.bbc.com/news/world-123</link>'
             b'<pubDate>Fri, 23 Oct 2026 12:30:00 GMT</pubDate>'
             b'</item></channel></rss>')

        def fake_get(url, *args, **kwargs):
            if "api.gdeltproject.org" in url:
                raise requests.Timeout("mock GDELT timeout")
            if "feeds.bbci.co.uk" in url:
                return FakeResponse(url, xml)
            return FakeResponse(url, b"blocked", status=403)

        with patch.object(collector.session, "get", side_effect=fake_get), patch.object(collector.time, "sleep", return_value=None):
            events, failures, start, metrics = collector.fetch_gdelt_events(
                date(2026, 7, 1), date(2026, 10, 24))

        self.assertGreater(metrics["gdelt"]["request_failures"], 0)
        self.assertGreaterEqual(metrics["rss"]["successful_feeds"], 1)
        self.assertEqual(len(events), 1)
        row=events.iloc[0]
        self.assertEqual(row["SOURCE_URL"], "https://www.bbc.com/news/world-123")
        self.assertEqual(row["PUBLISHED_AT"], "2026-10-23T12:30:00+00:00")
        self.assertEqual(row["EVENT_DATE_BASIS"], "PUBLISHER_FEED_PUBLICATION_TIMESTAMP")
        self.assertTrue(str(row["EVENT_ID"]).strip())
        self.assertIn("SOURCE_URL", events.columns)
        self.assertIn("PUBLISHED_AT", events.columns)
        self.assertTrue(any(x.get("provider") == "GDELT" for x in failures))

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

    def test_empty_exclusion_list_is_a_valid_zero_count(self):
        empty=pd.DataFrame()
        self.assertEqual(event.exclusion_count(empty, "PENDING_PANEL_NOT_YET_AVAILABLE"), 0)
        self.assertEqual(event.exclusion_count(empty, "EVENT_BEFORE_PANEL_HISTORY"), 0)

    def test_future_events_are_pending_not_input_qa_failure(self):
        panel=pd.DataFrame({"DATE":pd.to_datetime(["2026-10-13","2026-10-14"]),"SERIES":["NIFTY 50"]*2,"CLOSE":[100,101]})
        events=pd.DataFrame([
            {"EVENT_DATE":pd.Timestamp("2026-10-14"),"EVENT_ID":"MATURE","EVENT_TYPE":"GEO","PUBLISHED_AT":pd.Timestamp("2026-10-14T08:00:00Z"),"SOURCE":"test","SOURCE_URL":"https://example.com/a","CONFIDENCE":0.8,"EVENT_DATE_BASIS":"ACTUAL_EVENT_DATE"},
            {"EVENT_DATE":pd.Timestamp("2026-10-15"),"EVENT_ID":"PENDING","EVENT_TYPE":"GEO","PUBLISHED_AT":pd.Timestamp("2026-10-15T08:00:00Z"),"SOURCE":"test","SOURCE_URL":"https://example.com/b","CONFIDENCE":0.8,"EVENT_DATE_BASIS":"ACTUAL_EVENT_DATE"}
        ])
        eligible,excluded=event.split_events_by_panel_coverage(panel,events)
        self.assertEqual(eligible["EVENT_ID"].tolist(),["MATURE"])
        self.assertEqual(excluded["EVENT_ID"].tolist(),["PENDING"])
        self.assertEqual(excluded.iloc[0]["EXCLUSION_REASON"],"PENDING_PANEL_NOT_YET_AVAILABLE")

    def test_p0_freshness_uses_latest_market_session_not_wall_clock(self):
        # On Saturday 2026-10-24, a valid 2026-10-20 Brent observation is
        # three calendar days behind Friday's 2026-10-23 market close.
        result = coverage.macro_series_freshness("2026-10-20", "2026-10-23", max_age_days=3)
        self.assertEqual(result, {"data_age_days": 3, "freshness_status": "FRESH"})
        stale = coverage.macro_series_freshness("2026-10-19", "2026-10-23", max_age_days=3)
        self.assertEqual(stale["freshness_status"], "STALE_OR_FUTURE")
        future = coverage.macro_series_freshness("2026-10-24", "2026-10-23", max_age_days=3)
        self.assertEqual(future["freshness_status"], "STALE_OR_FUTURE")


class MacroGeoHardGateTests(unittest.TestCase):
    def setUp(self):
        import json
        import tempfile
        import sys
        from unittest.mock import patch
        self.json = json
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.coverage_path = self.root / "source_coverage.json"
        self.event_path = self.root / "event_study_report.json"
        self.audit_path = self.root / "event_level_window_audit.json"
        self.panel_path = self.root / "market_panel.csv"
        self.equity_path = self.root / "equity.csv"
        self.out_path = self.root / "hard_gate_report.json"
        self.manifest_path = self.root / "p0_collection_manifest.json"
        self.repair_path = self.root / "p0_repair_report.json"
        self.factor_path = self.root / "factor_coverage_audit.json"
        self.regime_path = self.root / "historical_regime_study_report.json"
        self.nsdl_path = self.root / "nsdl_fpi_dii_collection.json"
        self.factor_rows_path = self.root / "factor_coverage_audit.csv"
        self.repair_path.write_text(json.dumps({"groups": {
            "fpi_dii_flows": {"status": "AVAILABLE"},
            "corporate_events": {"status": "AVAILABLE"}
        }}), encoding="utf-8")
        self.factor_path.write_text(json.dumps({"factor_groups": 1, "fully_available_schema_groups": 1, "not_connected": 0}), encoding="utf-8")
        pd.DataFrame([{"factor_id": "F01", "coverage_status": "SOURCE_GROUPS_AVAILABLE_SCHEMA_ONLY"}]).to_csv(self.factor_rows_path, index=False)
        self.nsdl_path.write_text(json.dumps({
            "status": "AVAILABLE",
            "groups": {
                "FPI": {"unique_dates": 60, "span_days": 90, "rows": 60},
                "DII": {"unique_dates": 60, "span_days": 90, "rows": 60}
            }
        }), encoding="utf-8")
        self.regime_path.write_text(json.dumps({"research_status": "COMPUTED_EXPLORATORY", "window_rows": 1, "regime_anchors": 1, "regimes_with_windows": 1, "anchor_coverage_complete": True}), encoding="utf-8")
        groups = {f"group_{i}": {"status": "AVAILABLE", "rows": 1} for i in range(8)}
        self.coverage_path.write_text(json.dumps({"p0_coverage": {
            "status": "P0_COMPLETE", "available_count": 8, "required_count": 8, "groups": groups
        }}), encoding="utf-8")
        self.event_path.write_text(json.dumps({
            "status": "COMPUTED_EXPLORATORY_WITH_PENDING_EVENTS",
            "research_status": "COMPUTED_EXPLORATORY_WITH_PENDING_EVENTS",
            "event_rows": 3, "eligible_event_rows": 2, "window_rows": 12
        }), encoding="utf-8")
        self.audit_path.write_text(json.dumps({
            "unique_events_with_mature_h1": 2, "unique_events_with_mature_h5": 1
        }), encoding="utf-8")
        self.manifest_path.write_text(json.dumps({
            "status": "PASS_WITH_GAPS", "operational_status": "PASS_WITH_GAPS",
            "p0_coverage": {
                "required_series_available": True,
                "required_groups": ["benchmark_index", "sector_indices", "volatility", "crude_oil", "usd_inr", "fpi_dii_flows", "corporate_events", "geopolitical_events"],
                "group_availability_after_repair": {name: True for name in ["benchmark_index", "sector_indices", "volatility", "crude_oil", "usd_inr", "fpi_dii_flows", "corporate_events", "geopolitical_events"]},
                "fpi_dii_status": "AVAILABLE",
                "corporate_events_status": "AVAILABLE"
            },
            "final_manifest_reconciliation": {"status": "RECONCILED"}
        }), encoding="utf-8")
        pd.DataFrame({"DATE": ["2026-10-22", "2026-10-23"],
                      "SERIES": ["NIFTY 50", "NIFTY 50"],
                      "CLOSE": [25000.0, 25100.0]}).to_csv(self.panel_path, index=False)
        pd.DataFrame({"DATE": ["2026-10-22", "2026-10-23"]}).to_csv(self.equity_path, index=False)
        sys.path.insert(0, str(ROOT / "pipeline"))
        import macro_geo_hard_gate as hard_gate
        self.gate = hard_gate
        self.patches = [
            patch.object(hard_gate, "COVERAGE", self.coverage_path),
            patch.object(hard_gate, "EVENT_REPORT", self.event_path),
            patch.object(hard_gate, "EVENT_AUDIT", self.audit_path),
            patch.object(hard_gate, "PANEL", self.panel_path),
            patch.object(hard_gate, "EQUITY", self.equity_path),
            patch.object(hard_gate, "MANIFEST", self.manifest_path),
            patch.object(hard_gate, "REPAIR", self.repair_path),
            patch.object(hard_gate, "FACTOR_COVERAGE", self.factor_path),
            patch.object(hard_gate, "REGIME_REPORT", self.regime_path),
            patch.object(hard_gate, "NSDL_REPORT", self.nsdl_path),
            patch.object(hard_gate, "FACTOR_ROWS", self.factor_rows_path),
            patch.object(hard_gate, "OUT", self.out_path),
        ]
        for item in self.patches:
            item.start()

    def tearDown(self):
        for item in reversed(self.patches):
            item.stop()
        self.temp.cleanup()

    def report(self):
        return self.json.loads(self.out_path.read_text(encoding="utf-8"))

    def test_hard_gate_valid_inputs_pass_without_changing_invariants(self):
        self.assertEqual(self.gate.main(), 0)
        report = self.report()
        self.assertEqual(report["status"], "PASS")
        self.assertTrue(report["candidate_release_allowed"])
        self.assertFalse(report["production_selector_changed"])
        self.assertFalse(report["ranking_score_changed"])
        self.assertFalse(report["pressure_fade_changed"])

    def test_hard_gate_allows_verified_repair_over_pre_repair_manifest_gap(self):
        manifest = self.json.loads(self.manifest_path.read_text(encoding="utf-8"))
        manifest["status"] = "PASS_WITH_CRITICAL_DATA_GAPS"
        manifest["operational_status"] = "PASS_WITH_CRITICAL_DATA_GAPS"
        manifest["p0_coverage"]["required_series_available"] = True
        manifest["p0_coverage"]["group_availability_after_repair"] = {
            name: True for name in manifest["p0_coverage"]["required_groups"]
        }
        manifest["final_manifest_reconciliation"] = {"status": "RECONCILED"}
        self.manifest_path.write_text(self.json.dumps(manifest), encoding="utf-8")
        self.assertEqual(self.gate.main(), 0)
        report = self.report()
        self.assertTrue(report["checks"]["collector_manifest_final_snapshot_verified"])
        self.assertNotIn("COLLECTION_MANIFEST_REPORTS_CRITICAL_P0_GAPS", report["blockers"])
        self.assertTrue(report["candidate_release_allowed"])

    def test_hard_gate_manifest_critical_gaps_block_release(self):
        self.manifest_path.write_text(self.json.dumps({
            "status": "PASS_WITH_CRITICAL_DATA_GAPS",
            "operational_status": "PASS_WITH_CRITICAL_DATA_GAPS",
            "p0_coverage": {
                "required_series_available": False,
                "fpi_dii_status": "UNKNOWN/BLOCKED unless official source returns mapped rows",
                "corporate_events_status": "UNKNOWN/BLOCKED unless official source returns mapped rows"
            }
        }), encoding="utf-8")
        self.assertEqual(self.gate.main(), 1)
        report = self.report()
        self.assertEqual(report["status"], "BLOCKED")
        self.assertFalse(report["candidate_release_allowed"])
        self.assertIn("COLLECTION_MANIFEST_REPORTS_CRITICAL_P0_GAPS", report["blockers"])
        self.assertIn("COLLECTION_MANIFEST_FPI_DII_STATUS_UNRESOLVED", report["blockers"])
        self.assertIn("COLLECTION_MANIFEST_CORPORATE_EVENTS_STATUS_UNRESOLVED", report["blockers"])

    def test_hard_gate_incomplete_historical_anchor_coverage_blocks_release(self):
        regime = self.json.loads(self.regime_path.read_text(encoding="utf-8"))
        regime["anchor_coverage_complete"] = False
        regime["regimes_with_windows"] = 0
        self.regime_path.write_text(self.json.dumps(regime), encoding="utf-8")
        self.assertEqual(self.gate.main(), 1)
        report = self.report()
        self.assertIn("HISTORICAL_REGIME_ANCHOR_COVERAGE_INCOMPLETE", report["blockers"])
        self.assertFalse(report["candidate_release_allowed"])

    def test_hard_gate_missing_input_blocks_release(self):
        self.panel_path.unlink()
        self.assertEqual(self.gate.main(), 1)
        report = self.report()
        self.assertEqual(report["status"], "BLOCKED")
        self.assertFalse(report["candidate_release_allowed"])
        self.assertTrue(any(x.startswith("MISSING_REQUIRED_INPUT:") for x in report["blockers"]))

    def test_hard_gate_zero_mature_windows_blocks_release(self):
        self.event_path.write_text(self.json.dumps({
            "status": "COMPUTED_EXPLORATORY_WITH_PENDING_EVENTS",
            "research_status": "COMPUTED_EXPLORATORY_WITH_PENDING_EVENTS",
            "event_rows": 3, "eligible_event_rows": 0, "window_rows": 0
        }), encoding="utf-8")
        self.assertEqual(self.gate.main(), 1)
        report = self.report()
        self.assertIn("EVENT_STUDY_NOT_COMPUTED_WITH_MATURE_WINDOWS", report["blockers"])
        self.assertFalse(report["candidate_release_allowed"])

    def test_hard_gate_zero_mature_event_level_h1_h5_blocks_release(self):
        self.audit_path.write_text(self.json.dumps({
            "unique_events_with_mature_h1": 0, "unique_events_with_mature_h5": 0
        }), encoding="utf-8")
        self.assertEqual(self.gate.main(), 1)
        report = self.report()
        self.assertIn("EVENT_LEVEL_AUDIT_HAS_NO_MATURE_H1_WINDOWS", report["blockers"])
        self.assertIn("EVENT_LEVEL_AUDIT_HAS_NO_MATURE_H5_WINDOWS", report["blockers"])
        self.assertFalse(report["candidate_release_allowed"])

    def test_hard_gate_stale_panel_blocks_release(self):
        pd.DataFrame({"DATE": ["2026-10-10", "2026-10-13"],
                      "SERIES": ["NIFTY 50", "NIFTY 50"],
                      "CLOSE": [25000.0, 25100.0]}).to_csv(self.panel_path, index=False)
        self.assertEqual(self.gate.main(), 1)
        report = self.report()
        self.assertIn("MARKET_PANEL_STALE_OR_DATE_MISALIGNED", report["blockers"])
        self.assertFalse(report["candidate_release_allowed"])

    def test_hard_gate_invalid_close_blocks_release(self):
        pd.DataFrame({"DATE": ["2026-10-22", "2026-10-23"],
                      "SERIES": ["NIFTY 50", "NIFTY 50"],
                      "CLOSE": [25000.0, 0]}).to_csv(self.panel_path, index=False)
        self.assertEqual(self.gate.main(), 1)
        report = self.report()
        self.assertIn("MARKET_PANEL_HAS_INVALID_CLOSES", report["blockers"])
        self.assertFalse(report["candidate_release_allowed"])


if __name__=="__main__": unittest.main()
