import unittest
import numpy as np
import pandas as pd
from pipeline.walk_forward_backtest import future_outcomes

class ForwardTargetLabelTests(unittest.TestCase):
    def test_forward_window_and_incomplete_horizon(self):
        dates = pd.date_range('2026-01-01', periods=6, freq='B')
        df = pd.DataFrame({'SYMBOL':['AAA']*6,'DATE':dates,'OPEN_PRICE':[100.]*6,'CLOSE_PRICE':[100.]*6,'HIGH_PRICE':[100.,102.,110.,104.,130.,106.],'LOW_PRICE':[99.]*6,'TTL_TRD_QNTY':[1000]*6,'DELIV_PER':[50.]*6})
        out = future_outcomes(df)
        self.assertAlmostEqual(out.loc[0,'FUT1_HIGH_PCT'],2.0)
        self.assertAlmostEqual(out.loc[0,'FUT3_HIGH_PCT'],10.0)
        self.assertAlmostEqual(out.loc[0,'FUT5_HIGH_PCT'],30.0)
        self.assertAlmostEqual(out.loc[1,'FUT3_HIGH_PCT'],30.0)
        self.assertTrue(np.isnan(out.loc[1,'FUT5_HIGH_PCT']))
        self.assertTrue(np.isnan(out.loc[3,'FUT3_HIGH_PCT']))
        self.assertTrue(np.isnan(out.loc[5,'FUT1_HIGH_PCT']))

if __name__ == '__main__':
    unittest.main()
