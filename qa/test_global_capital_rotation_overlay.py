import csv, tempfile, unittest
from pathlib import Path
from pipeline.global_capital_rotation_overlay import load_observations, classify

FIELDS=["date","indicator","value","unit","source","source_url","published_at","as_of_date","quality_status"]
class TestGlobalCapitalRotation(unittest.TestCase):
    def make(self, rows):
        d=tempfile.TemporaryDirectory(); self.addCleanup(d.cleanup)
        p=Path(d.name)/"in.csv"
        with p.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader()
            for r in rows: w.writerow({k:r.get(k,"") for k in FIELDS})
        return p
    def row(self,k,v,q="VERIFIED_OFFICIAL"):
        return dict(date="2026-11-06",indicator=k,value=v,unit="test",source="test-source",source_url="https://example.org/data",published_at="2026-11-07T00:00:00Z",as_of_date="2026-11-06",quality_status=q)
    def test_unknowns_stay_unknown(self):
        out=classify(load_observations(self.make([])))
        self.assertEqual(out["global_em_flow"],"UNKNOWN")
        self.assertEqual(out["fx_transmission"],"UNKNOWN")
        self.assertEqual(out["status"],"RESEARCH_ONLY_NO_PRODUCTION_SCORE")
    def test_em_outflow_can_coexist_with_india_fpi_buy(self):
        rows=[self.row("em_portfolio_flow_usd_bn",-33.8),self.row("india_fpi_equity_inr_cr",16277.99)]
        out=classify(load_observations(self.make(rows)))
        self.assertEqual(out["global_em_flow"],"EM_NET_OUTFLOW")
        self.assertEqual(out["india_fpi_equity"],"FPI_EQUITY_NET_BUY")
    def test_fx_requires_both_inputs(self):
        rows=[self.row("dxy_change_pct_20d",-1.2)]
        out=classify(load_observations(self.make(rows)))
        self.assertEqual(out["fx_transmission"],"UNKNOWN")
        rows.append(self.row("usd_inr_change_pct_20d",-0.4))
        out=classify(load_observations(self.make(rows)))
        self.assertEqual(out["fx_transmission"],"USD_AND_INR_TAILWIND")
    def test_unknown_quality_rows_are_not_used(self):
        rows=[self.row("em_portfolio_flow_usd_bn",50,"UNKNOWN")]
        out=classify(load_observations(self.make(rows)))
        self.assertEqual(out["global_em_flow"],"UNKNOWN")
    def test_bad_quality_fails_closed(self):
        with self.assertRaises(ValueError):
            load_observations(self.make([self.row("em_portfolio_flow_usd_bn",1,"GUESSED")]))
if __name__=="__main__": unittest.main()
