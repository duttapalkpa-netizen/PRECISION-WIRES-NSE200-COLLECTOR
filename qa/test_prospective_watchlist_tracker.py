import tempfile
import unittest
from pathlib import Path
import pandas as pd
from prospective_watchlist_tracker import run_tracker

class ProspectiveLedgerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.picks, self.prices, self.ledger = (self.root / n for n in ("latest.csv", "prices.csv", "ledger.csv"))
        pd.DataFrame([
            {"CUT_OFF":"2026-01-01","TARGET":"BOTH_TARGETS_DIAGNOSTIC","SELECTOR":"CURRENT_WINNER_PROB","SYMBOL":"ABC","BASE_RANK":35,"WATCH_RANK":1,"SELECTION_SCORE_VALUE":99.0,"STATUS":"PROSPECTIVE_UNRESOLVED"},
            {"CUT_OFF":"2026-01-01","TARGET":"BOTH_TARGETS_DIAGNOSTIC","SELECTOR":"P10_P20_MEAN","SYMBOL":"XYZ","BASE_RANK":38,"WATCH_RANK":1,"SELECTION_SCORE_VALUE":98.0,"STATUS":"PROSPECTIVE_UNRESOLVED"},
        ]).to_csv(self.picks,index=False)
        rows=[]
        for sym, highs in [("ABC",[100,106,103,112,110,122]),("XYZ",[100,102,103,104,105,106])]:
            for j, high in enumerate(highs):
                rows.append({"SYMBOL":sym,"DATE":f"2026-01-0{j+1}","CLOSE_PRICE":100,"HIGH_PRICE":high})
        pd.DataFrame(rows).to_csv(self.prices,index=False)
    def tearDown(self): self.tmp.cleanup()
    def test_outcomes_mature_and_append_is_idempotent(self):
        first=run_tracker(self.picks,self.prices,self.ledger)
        self.assertEqual(len(first),2)
        abc=first[first.SYMBOL=="ABC"].iloc[0]
        self.assertTrue(str(abc.MATURED_T1).lower()=="true")
        self.assertTrue(str(abc.MATURED_T3).lower()=="true")
        self.assertTrue(str(abc.MATURED_T5).lower()=="true")
        self.assertTrue(str(abc.T5_H1_HIT).lower()=="true")
        self.assertTrue(str(abc.T10_H3_HIT).lower()=="true")
        self.assertTrue(str(abc.T20_H5_HIT).lower()=="true")
        second=run_tracker(self.picks,self.prices,self.ledger)
        self.assertEqual(len(second),2)
        self.assertEqual(first.loc[first.SYMBOL=="ABC","WATCH_RANK"].iloc[0],second.loc[second.SYMBOL=="ABC","WATCH_RANK"].iloc[0])
    def test_latest_cutoff_stays_unresolved_without_future_rows(self):
        prices=pd.read_csv(self.prices); prices=prices[prices.DATE<="2026-01-01"]; prices.to_csv(self.prices,index=False)
        result=run_tracker(self.picks,self.prices,self.ledger)
        self.assertFalse(result.MATURED_T1.astype(str).str.lower().eq("true").any())

if __name__ == "__main__":
    unittest.main()
