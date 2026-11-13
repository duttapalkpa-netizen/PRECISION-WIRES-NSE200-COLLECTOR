import csv, tempfile, unittest
from decimal import Decimal
from pathlib import Path
from pipeline.global_capital_rotation_overlay import load_observations, classify
FIELDS=["date","indicator","value","unit","source","source_url","published_at","as_of_date","quality_status"]
class TestGlobalCapitalRotation(unittest.TestCase):
    def make(self,rows):
        d=tempfile.TemporaryDirectory(); self.addCleanup(d.cleanup); p=Path(d.name)/"in.csv"
        with p.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader()
            for r in rows: w.writerow({k:r.get(k,"") for k in FIELDS})
        return p
    def row(self,k,v,q="VERIFIED_OFFICIAL",asof="2026-11-06",published="2026-11-07T00:00:00Z"):
        return dict(date=asof,indicator=k,value=v,unit="test",source="test-source",source_url="https://example.org/data",published_at=published,as_of_date=asof,quality_status=q)
    def test_unknowns_stay_unknown(self):
        out=classify(load_observations(self.make([])),"2026-11-07",decision_at="2026-11-07T23:59:59Z")
        self.assertEqual(out["global_em_flow"],"UNKNOWN"); self.assertEqual(out["fx_transmission"],"UNKNOWN")
    def test_em_outflow_can_coexist_with_india_fpi_buy(self):
        rows=[self.row("em_portfolio_flow_usd_bn",-33.8,asof="2026-10-31"),self.row("india_fpi_equity_inr_cr",16277.99)]
        out=classify(load_observations(self.make(rows)),"2026-11-07",decision_at="2026-11-07T23:59:59Z")
        self.assertEqual(out["global_em_flow"],"EM_NET_OUTFLOW"); self.assertEqual(out["india_fpi_equity"],"FPI_EQUITY_NET_BUY")
    def test_fx_requires_both_inputs_and_uses_explicit_direction(self):
        rows=[self.row("dxy_change_pct_20d",-1.2)]
        self.assertEqual(classify(load_observations(self.make(rows)),"2026-11-07",decision_at="2026-11-07T23:59:59Z")["fx_transmission"],"UNKNOWN")
        rows.append(self.row("usd_inr_change_pct_20d",-0.4))
        self.assertEqual(classify(load_observations(self.make(rows)),"2026-11-07",decision_at="2026-11-07T23:59:59Z")["fx_transmission"],"USD_WEAKENING_INR_STRENGTHENING")
    def test_unknown_quality_rows_are_not_used(self):
        out=classify(load_observations(self.make([self.row("em_portfolio_flow_usd_bn",50,"UNKNOWN")])),"2026-11-07",decision_at="2026-11-07T23:59:59Z")
        self.assertEqual(out["global_em_flow"],"UNKNOWN")
    def test_bad_quality_fails_closed(self):
        with self.assertRaises(ValueError): load_observations(self.make([self.row("em_portfolio_flow_usd_bn",1,"GUESSED")]))
    def test_stale_fpi_is_excluded(self):
        row=self.row("india_fpi_equity_inr_cr",999,asof="2026-10-01")
        out=classify(load_observations(self.make([row])),"2026-11-07",decision_at="2026-11-07T23:59:59Z")
        self.assertEqual(out["india_fpi_equity"],"UNKNOWN")
        self.assertIn("india_fpi_equity_inr_cr",out["stale_observations_excluded"])
    def test_rejects_nan_and_infinity(self):
        for value in ("nan","inf","-inf"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                load_observations(self.make([self.row("em_portfolio_flow_usd_bn",value)]))
    def test_rejects_observation_after_asof(self):
        with self.assertRaises(ValueError):
            load_observations(self.make([{**self.row("em_portfolio_flow_usd_bn",1,asof="2026-11-07"),"date":"2026-11-08"}]))
    def test_rejects_non_https_source(self):
        row=self.row("em_portfolio_flow_usd_bn",1); row["source_url"]="http://example.org"
        with self.assertRaises(ValueError): load_observations(self.make([row]))
    def test_duplicate_same_source_observation_key_fails_closed(self):
        row=self.row("india_fpi_equity_inr_cr",25)
        with self.assertRaisesRegex(ValueError,"duplicate observation key"):
            load_observations(self.make([row,row]))

    def test_conflicting_same_vintage_fails_closed(self):
        rows=[self.row("em_portfolio_flow_usd_bn",1),self.row("em_portfolio_flow_usd_bn",-1)]
        with self.assertRaises(ValueError): classify(load_observations(self.make(rows)),"2026-11-07",decision_at="2026-11-07T23:59:59Z")
    def test_latest_publication_wins_deterministically(self):
        rows=[self.row("india_fpi_equity_inr_cr",10,published="2026-11-07T00:00:00Z"),
              self.row("india_fpi_equity_inr_cr",-5,published="2026-11-07T01:00:00Z")]
        out=classify(load_observations(self.make(rows)),"2026-11-07",decision_at="2026-11-07T23:59:59Z")
        self.assertEqual(out["india_fpi_equity"],"FPI_EQUITY_NET_SELL")

    def test_short_term_fpi_inflow_does_not_hide_ytd_outflow(self):
        rows=[self.row("india_fpi_equity_mtd_inr_cr",53738.78),
              self.row("india_fpi_equity_ytd_inr_cr",-241407.13)]
        out=classify(load_observations(self.make(rows)),"2026-11-07",decision_at="2026-11-07T23:59:59Z")
        self.assertEqual(out["india_fpi_horizon_divergence"],"SHORT_TERM_INFLOW_LONG_TERM_OUTFLOW")

    def test_latest_publication_orders_equivalent_instants_in_utc(self):
        # 01:00 at UTC+02 is 23:00Z on the prior day; 00:30Z is later.
        rows=[self.row("india_fpi_equity_inr_cr",10,published="2026-11-07T01:00:00+02:00"),
              self.row("india_fpi_equity_inr_cr",-5,published="2026-11-07T00:30:00Z")]
        out=classify(load_observations(self.make(rows)),"2026-11-07",decision_at="2026-11-07T23:59:59Z")
        self.assertEqual(out["india_fpi_equity"],"FPI_EQUITY_NET_SELL")

    def test_equivalent_timezone_instants_are_duplicate_vintages(self):
        first=self.row("india_fpi_equity_inr_cr",10,published="2026-11-07T01:00:00+02:00")
        second=self.row("india_fpi_equity_inr_cr",10,published="2026-11-06T23:00:00Z")
        with self.assertRaisesRegex(ValueError,"duplicate observation key"):
            load_observations(self.make([first,second]))

    def test_non_government_iif_seed_is_not_promoted_to_official_flow(self):
        seed=Path(__file__).resolve().parents[1]/"data"/"global_capital_rotation"/"2026-11-07_seed_observations.csv"
        grouped=load_observations(seed)
        self.assertNotIn("em_portfolio_flow_usd_bn",grouped)

    def test_source_register_preserves_measurement_boundaries(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("NOT ICE DXY",content)
        self.assertIn("positions are stocks, NOT flows",content)
        self.assertIn("UNKNOWN / NOT DONE",content)
        self.assertIn("SDMX 2.1/3.0 API route VERIFIED",content)
        self.assertIn("BOP DSD V2.6.0",content)

    def test_bop_agg_methodology_is_context_only_and_estimation_is_not_observed_flow(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("For financial-account transaction gaps, IMF says WEO data are used",content)
        self.assertIn("not an observed-only sum of country-reported flows",content)
        self.assertIn("cannot serve as a 1–5 trading-day trigger",content)
        self.assertIn("raw BOP_AGG workbook/table bytes",content)

    def test_bop_agg_vintage_and_download_access_are_not_overstated(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("2026 vintage NOT VERIFIED",content)
        self.assertIn("19 November 2025",content)
        self.assertIn("API portal redirects to a sign-in page",content)
        self.assertIn("raw workbook/table, exact URL, retrieval timestamp",content)
    def test_imf_bop_spec_pins_public_dsd_but_keeps_data_unknown(self):
        spec=Path(__file__).resolve().parents[1]/"docs"/"IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md"
        content=spec.read_text(encoding="utf-8")
        self.assertIn("BOP DSD V2.6.0",content)
        self.assertIn("registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/",content)
        self.assertIn("XML payload itself was not parsed",content)
        self.assertIn("Country-level portfolio transaction panel extracted | UNKNOWN / NOT DONE",content)
        self.assertIn("FLOW_STOCK_ENTRY",content)
        self.assertIn("UNIT_MULT",content)
        self.assertIn("positive values indicate an increase",content)
        self.assertIn("Eurostat-specific dataset IDs",content)
    def test_imf_bop_extraction_contract_is_explicitly_not_an_extracted_panel(self):
        spec=Path(__file__).resolve().parents[1]/"docs"/"IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md"
        content=spec.read_text(encoding="utf-8")
        self.assertIn("NO COUNTRY OBSERVATIONS EXTRACTED",content)
        self.assertIn("metadata-first",content.lower())
        self.assertIn("UNKNOWN / NOT DONE",content)
        self.assertIn("positions",content.lower())
        self.assertIn("Daily trading trigger suitability",content)
        self.assertIn("no synthetic",content.lower())

    def test_imf_bop_spec_documents_public_structure_api_retrieval_contract(self):
        spec=Path(__file__).resolve().parents[1]/"docs"/"IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md"
        content=spec.read_text(encoding="utf-8")
        self.assertIn("public access for the Structure Web Service",content)
        self.assertIn("structure/datastructure/IMF/BOP/2.6.0/",content)
        self.assertIn("references=children",content)
        self.assertIn("saveAs=IMF_BOP_DSD_2_6_0",content)
        self.assertIn("ws/public/sdmxapi/rest/datastructure/IMF/BOP/2.6.0/",content)
        self.assertIn("IMF_BOP_DSD_2_6_0_legacy",content)
        self.assertIn("candidate to test, not as a verified response URL",content)
        self.assertIn("response HTTP status: UNKNOWN",content)
        self.assertIn("SHA-256: NOT AVAILABLE",content)
        self.assertIn("not evidence that this audit successfully retrieved the response",content)
        self.assertIn("Observation extraction requires a separately verified",content)
    def test_decision_cutoff_is_mandatory(self):
        with self.assertRaisesRegex(ValueError,"decision_at is required"):
            classify(load_observations(self.make([])),"2026-11-07")

    def test_asof_date_is_mandatory(self):
        with self.assertRaisesRegex(ValueError,"as_of_date is required"):
            classify(load_observations(self.make([])),decision_at="2026-11-07T23:59:59Z")

    def test_asof_date_must_be_iso_date(self):
        with self.assertRaisesRegex(ValueError,"as_of_date must be an ISO date"):
            classify(load_observations(self.make([])),"07-11-2026",decision_at="2026-11-07T23:59:59Z")

    def test_decision_cutoff_excludes_future_publication(self):
        rows=[self.row("india_fpi_equity_inr_cr",10,published="2026-11-06T20:00:00Z"),
              self.row("india_fpi_equity_inr_cr",-20,published="2026-11-07T02:00:00Z")]
        grouped=load_observations(self.make(rows))
        early=classify(grouped,"2026-11-07",decision_at="2026-11-06T21:00:00Z")
        late=classify(grouped,"2026-11-07",decision_at="2026-11-07T03:00:00Z")
        self.assertEqual(early["india_fpi_equity"],"FPI_EQUITY_NET_BUY")
        self.assertEqual(late["india_fpi_equity"],"FPI_EQUITY_NET_SELL")

    def test_decision_cutoff_all_future_remains_unknown(self):
        rows=[self.row("usd_inr_change_pct_20d",-1,published="2026-11-07T03:00:00Z")]
        out=classify(load_observations(self.make(rows)),"2026-11-07",decision_at="2026-11-07T02:00:00Z")
        self.assertIsNone(out["latest_observations"]["usd_inr_change_pct_20d"])
        self.assertEqual(out["fx_transmission"],"UNKNOWN")

    def test_decision_cutoff_normalizes_timezone_offsets(self):
        rows=[self.row("india_fpi_equity_inr_cr",10,published="2026-11-07T04:00:00+05:30")]
        grouped=load_observations(self.make(rows))
        before=classify(grouped,"2026-11-07",decision_at="2026-11-06T22:29:59Z")
        after=classify(grouped,"2026-11-07",decision_at="2026-11-06T22:30:00Z")
        self.assertEqual(before["india_fpi_equity"],"UNKNOWN")
        self.assertEqual(after["india_fpi_equity"],"FPI_EQUITY_NET_BUY")

    def test_rejects_decision_cutoff_after_asof_utc_date(self):
        with self.assertRaisesRegex(ValueError,"decision_at UTC date"):
            classify(load_observations(self.make([])),"2026-11-07",decision_at="2026-11-08T00:00:00Z")

    def test_weo_october_2026_candidate_is_separate_and_estimates_are_gated(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("IMF WEO October 2026 country-group portfolio-flow candidate",content)
        self.assertIn("at least 90% of group weights",content)
        self.assertIn("actual/projection flags",content)
        self.assertIn("not a BOP_AGG replacement",content)
        self.assertIn("workbook/raw data and exact portfolio series mapping PENDING",content)

    def test_weo_country_group_actual_projection_metadata_is_unknown(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("does NOT provide this actual/projection metadata for WEO country-group data",content)
        self.assertIn("NOT_POINT_IN_TIME_VERIFIED",content)
        self.assertIn("transfer failed before any file bytes were obtained",content)
        self.assertIn("This correction supersedes any contrary implication",content)

    def test_nse_fii_dii_page_controls_do_not_imply_csv_url_or_final_data(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("two distinct downloadable CSV controls",content)
        self.assertIn("Exact CSV URL remains UNKNOWN",content)
        self.assertIn("provisional exchange-reported trading activity",content)
        self.assertIn("NOT ACQUIRED",content)

    def test_cdsl_confirmed_fpi_flow_keeps_reporting_lag_and_asset_buckets_separate(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("CDSL custodian-confirmed FPI daily flow qualification",content)
        self.assertIn("reporting_date` as publication/reporting date",content)
        self.assertIn("do not use grand Total as equity or as FPI-only",content)
        self.assertIn("Primary market & others` includes multiple non-secondary-market events",content)
        self.assertIn("direct raw-file export URL/bytes, retrieval timestamp, file size and SHA-256 were not acquired",content)

    def test_cdsl_12nov2026_live_snapshot_bucket_arithmetic_reconciles(self):
        buckets=[Decimal("14693.72"),Decimal("445.65"),Decimal("-173.22"),Decimal("1022.81"),Decimal("34.86"),Decimal("9.59"),Decimal("-5.20")]
        self.assertEqual(sum(buckets),Decimal("16028.21"))
        purchases=[Decimal("32902.51"),Decimal("717.30"),Decimal("44.73"),Decimal("2368.61"),Decimal("95.23"),Decimal("9.63"),Decimal("0.00")]
        sales=[Decimal("18208.79"),Decimal("271.65"),Decimal("217.95"),Decimal("1345.80"),Decimal("60.37"),Decimal("0.04"),Decimal("5.20")]
        self.assertEqual(sum(purchases),Decimal("36138.01"))
        self.assertEqual(sum(sales),Decimal("20109.80"))
        usd=[Decimal("1566.3694"),Decimal("47.5069"),Decimal("-18.4655"),Decimal("109.0329"),Decimal("3.7161"),Decimal("1.0223"),Decimal("-0.5543")]
        self.assertEqual(sum(usd).quantize(Decimal("0.001")),Decimal("1708.628"))

    def test_cdsl_daily_archive_exact_link_and_coverage_boundary_do_not_imply_raw_acquisition(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("CDSL historical Daily Trends archive route and coverage boundary",content)
        self.assertIn("02-Sep-2024 through 04-Apr-2025",content)
        self.assertIn("https://www.cdslindia.com/downloads/Publications/Latest/latest_04042025.xls",content)
        self.assertIn("raw XLS bytes were NOT ACQUIRED",content)
        self.assertIn("Historical daily coverage after 04-Apr-2025 = NOT VERIFIED",content)
        self.assertIn("Exact trade-date mapping = UNKNOWN",content)

    def test_cdsl_fortnightly_sector_report_is_not_daily_or_issuer_flow(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("CDSL fortnightly sector-wise FPI report — frequency and measurement qualification",content)
        self.assertIn("AUC is a stock/position, not transaction flow",content)
        self.assertIn("NOT a daily/1–5 day trigger",content)
        self.assertIn("BSE common industry classification",content)
        self.assertIn("end-of-period RBI reference rate",content)
        self.assertIn("their net investment from 15-Sep-2024",content)
        self.assertIn("Raw report file bytes/SHA-256 = NOT ACQUIRED",content)

    def test_bse_industry_hierarchy_is_not_issuer_membership_or_verified_sector_bridge(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("BSE industry-classification hierarchy qualification for CDSL fortnightly sector bridge",content)
        self.assertIn("taxonomy dictionary, not by itself a dated issuer-to-code membership file",content)
        self.assertIn("issuer membership file + effective dates = NOT ACQUIRED",content)
        self.assertIn("sector-to-issuer bridge = UNKNOWN",content)
        self.assertIn("No synthetic mapping, no inferred company assignments",content)

    def test_nse_classification_methodology_does_not_imply_complete_effective_dated_roster(self):
        register=Path(__file__).resolve().parents[1]/"docs"/"GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md"
        content=register.read_text(encoding="utf-8")
        self.assertIn("NSE Indices issuer-classification source and bulk-membership gap",content)
        self.assertIn("official bulk, machine-readable, effective-dated issuer-to-classification roster",content)
        self.assertIn("official complete issuer membership dataset = NOT LOCATED/NOT ACQUIRED",content)
        self.assertIn("NSE/BSE roster equivalence = UNKNOWN",content)
        self.assertIn("No scraping of individual issuer reports to fabricate a complete list",content)

if __name__=="__main__": unittest.main()
