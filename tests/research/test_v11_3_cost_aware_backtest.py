import unittest
import tempfile
from pathlib import Path
import pandas as pd
from pipeline.v11_3_cost_aware_backtest import simulate_one, run, COST_PCT

def bars(rows):
    return pd.DataFrame(rows,columns=["SYMBOL","DATE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"])

class CostAwareReplayTests(unittest.TestCase):
    def setUp(self):
        self.base=[
            ["ABC","2026-01-01",100,101,99,100,1000],
            ["ABC","2026-01-02",100,106,99,104,1000],
            ["ABC","2026-01-05",104,105,100,103,1000],
            ["ABC","2026-01-06",103,104,100,102,1000],
            ["ABC","2026-01-07",102,103,100,101,1000],
            ["ABC","2026-01-08",101,102,99,100,1000],
        ]
    def test_cost_once_and_target(self):
        r=simulate_one(bars(self.base),"2026-01-01","ABC",5,1)
        self.assertEqual(r["EXIT_REASON"],"TARGET")
        self.assertAlmostEqual(r["GROSS_RETURN_PCT"],5.0)
        self.assertAlmostEqual(r["NET_RETURN_PCT"],4.78)
        self.assertAlmostEqual(r["COST_PCT"],0.22)
    def test_stop_first_when_same_bar_hits_both(self):
        x=self.base.copy(); x[1]=["ABC","2026-01-02",100,106,96,103,1000]
        r=simulate_one(bars(x),"2026-01-01","ABC",5,1)
        self.assertEqual(r["EXIT_REASON"],"STOP_LOSS")
        self.assertAlmostEqual(r["GROSS_RETURN_PCT"],-3.0)
        self.assertAlmostEqual(r["NET_RETURN_PCT"],-3.22)
    def test_gap_below_stop_fills_open(self):
        x=self.base.copy(); x[1]=["ABC","2026-01-02",100,102,99,101,1000]; x[2]=["ABC","2026-01-05",95,97,94,96,1000]
        r=simulate_one(bars(x),"2026-01-01","ABC",5,3)
        self.assertEqual(r["EXIT_REASON"],"STOP_GAP")
        self.assertAlmostEqual(r["EXIT_PRICE"],95)
    def test_no_target_exits_horizon_close(self):
        x=self.base.copy(); x[1]=["ABC","2026-01-02",100,102,99,101,1000]
        r=simulate_one(bars(x),"2026-01-01","ABC",5,1)
        self.assertEqual(r["EXIT_REASON"],"HORIZON_CLOSE")
        self.assertAlmostEqual(r["EXIT_PRICE"],101)
    def test_missing_symbol_session_is_not_executable(self):
        x=self.base.copy(); x.pop(2); x.append(["OTHER","2026-01-05",50,51,49,50,1000])
        r=simulate_one(bars(x),"2026-01-01","ABC",10,3)
        self.assertFalse(r["EXECUTABLE"])
        self.assertEqual(r["DATA_STATUS"],"SYMBOL_SESSION_MISSING")
    def test_unmatured_horizon_fails_closed(self):
        r=simulate_one(bars(self.base[:3]),"2026-01-01","ABC",20,5)
        self.assertFalse(r["EXECUTABLE"])
        self.assertEqual(r["DATA_STATUS"],"HORIZON_NOT_MATURED")
    def test_zero_volume_invalid(self):
        x=self.base.copy(); x[1]=["ABC","2026-01-02",100,106,99,104,0]
        r=simulate_one(bars(x),"2026-01-01","ABC",5,1)
        self.assertEqual(r["DATA_STATUS"],"INVALID_OR_NONTRADED_OHLC")
    def test_invalid_cost_rejected(self):
        for cost in (-0.1, float("nan"), float("inf")):
            with self.subTest(cost=cost), self.assertRaises(ValueError):
                simulate_one(bars(self.base),"2026-01-01","ABC",5,1,cost)
    def test_invalid_target_and_horizon_rejected(self):
        with self.assertRaises(ValueError):
            simulate_one(bars(self.base),"2026-01-01","ABC",0,1)
        with self.assertRaises(ValueError):
            simulate_one(bars(self.base),"2026-01-01","ABC",5,1.5)
    def test_direct_duplicate_symbol_date_fails_closed(self):
        x=self.base.copy(); x.append(x[1].copy())
        with self.assertRaises(ValueError):
            simulate_one(bars(x),"2026-01-01","ABC",5,1)
    def test_target_hit_is_distinct_from_net_profitability(self):
        r=simulate_one(bars(self.base),"2026-01-01","ABC",0.1,1)
        self.assertEqual(r["EXIT_REASON"],"TARGET")
        self.assertTrue(r["TARGET_HIT"])
        self.assertLess(r["NET_RETURN_PCT"],0)
    def test_run_rejects_duplicate_signal_keys(self):
        with tempfile.TemporaryDirectory() as td:
            data=Path(td)/"bars.csv"; signals=Path(td)/"signals.csv"
            bars(self.base).to_csv(data,index=False)
            pd.DataFrame([["2026-01-01","ABC"],["2026-01-01","ABC"]],columns=["CUT_OFF","SYMBOL"]).to_csv(signals,index=False)
            with self.assertRaisesRegex(ValueError,"Duplicate CUT_OFF/SYMBOL"):
                run(data,signals,Path(td)/"out")
    def test_infinite_volume_is_invalid(self):
        x=self.base.copy(); x[1]=["ABC","2026-01-02",100,106,99,104,float("inf")]
        r=simulate_one(bars(x),"2026-01-01","ABC",5,1)
        self.assertEqual(r["DATA_STATUS"],"INVALID_OR_NONTRADED_OHLC")

if __name__=="__main__":
    unittest.main()
