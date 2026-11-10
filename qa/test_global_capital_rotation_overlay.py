import csv, tempfile, unittest
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
        out=classify(load_observations(self.make([])),"2026-11-07")
        self.assertEqual(out["global_em_flow"],"UNKNOWN"); self.assertEqual(out["fx_transmission"],"UNKNOWN")
    def test_em_outflow_can_coexist_with_india_fpi_buy(self):
        rows=[self.row("em_portfolio_flow_usd_bn",-33.8,asof="2026-10-31"),self.row("india_fpi_equity_inr_cr",16277.99)]
        out=classify(load_observations(self.make(rows)),"2026-11-07")
        self.assertEqual(out["global_em_flow"],"EM_NET_OUTFLOW"); self.assertEqual(out["india_fpi_equity"],"FPI_EQUITY_NET_BUY")
    def test_fx_requires_both_inputs_and_uses_explicit_direction(self):
        rows=[self.row("dxy_change_pct_20d",-1.2)]
        self.assertEqual(classify(load_observations(self.make(rows)),"2026-11-07")["fx_transmission"],"UNKNOWN")
        rows.append(self.row("usd_inr_change_pct_20d",-0.4))
        self.assertEqual(classify(load_observations(self.make(rows)),"2026-11-07")["fx_transmission"],"USD_WEAKENING_INR_STRENGTHENING")
    def test_unknown_quality_rows_are_not_used(self):
        out=classify(load_observations(self.make([self.row("em_portfolio_flow_usd_bn",50,"UNKNOWN")])),"2026-11-07")
        self.assertEqual(out["global_em_flow"],"UNKNOWN")
    def test_bad_quality_fails_closed(self):
        with self.assertRaises(ValueError): load_observations(self.make([self.row("em_portfolio_flow_usd_bn",1,"GUESSED")]))
    def test_stale_fpi_is_excluded(self):
        row=self.row("india_fpi_equity_inr_cr",999,asof="2026-10-01")
        out=classify(load_observations(self.make([row])),"2026-11-07")
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
    def test_conflicting_same_vintage_fails_closed(self):
        rows=[self.row("em_portfolio_flow_usd_bn",1),self.row("em_portfolio_flow_usd_bn",-1)]
        with self.assertRaises(ValueError): classify(load_observations(self.make(rows)),"2026-11-07")
    def test_latest_publication_wins_deterministically(self):
        rows=[self.row("india_fpi_equity_inr_cr",10,published="2026-11-07T00:00:00Z"),
              self.row("india_fpi_equity_inr_cr",-5,published="2026-11-07T01:00:00Z")]
        out=classify(load_observations(self.make(rows)),"2026-11-07")
        self.assertEqual(out["india_fpi_equity"],"FPI_EQUITY_NET_SELL")

    def test_short_term_fpi_inflow_does_not_hide_ytd_outflow(self):
        rows=[self.row("india_fpi_equity_mtd_inr_cr",53738.78),
              self.row("india_fpi_equity_ytd_inr_cr",-241407.13)]
        out=classify(load_observations(self.make(rows)),"2026-11-07")
        self.assertEqual(out["india_fpi_horizon_divergence"],"SHORT_TERM_INFLOW_LONG_TERM_OUTFLOW")
if __name__=="__main__": unittest.main()
