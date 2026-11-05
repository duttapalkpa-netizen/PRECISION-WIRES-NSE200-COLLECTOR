import csv, json, subprocess, sys, tempfile, unittest
from pathlib import Path
from pipeline.nse_security_identity_reconciliation import read_csv, clean

SCRIPT = Path("pipeline/nse_security_identity_reconciliation.py")

class IdentityHelpersTest(unittest.TestCase):
    def test_normalizes_symbol(self):
        self.assertEqual(clean("  abc "), "ABC")

    def test_csv_headers_normalized(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.csv"
            p.write_text("Trading Symbol,ISIN\nABC,INEX\n")
            df=read_csv(p)
            self.assertIn("TRADINGSYMBOL",df.columns)

    def test_end_to_end_direct_rename_unknown_and_isin_conflict(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            def write(name, header, rows):
                p=root/name
                with p.open("w",newline="") as f:
                    w=csv.writer(f); w.writerow(header); w.writerows(rows)
                return p
            stale=write("stale.csv",["SYMBOL","ISIN"],[
                ["DIRECT","INE000000001"],["OLDNAME","INE000000002"],
                ["MISSING","INE000000003"],["CONFLICT","INE000000004"]])
            equity=write("equity.csv",["SYMBOL","ISIN"],[
                ["DIRECT","INE000000001"],["NEWNAME","INE000000002"],
                ["CONFLICT","INE999999999"]])
            changes=write("changes.csv",["Old Symbol","New Symbol"],[["OLDNAME","NEWNAME"]])
            out=root/"out"
            subprocess.run([sys.executable,str(SCRIPT),"--stale",str(stale),
                "--equity",str(equity),"--symbol-changes",str(changes),
                "--out",str(out)],check=True,capture_output=True,text=True)
            import pandas as pd
            result=pd.read_csv(out/"nse_identity_reconciliation.csv").set_index("OLD_SYMBOL")
            self.assertEqual(result.loc["DIRECT","STATUS"],"MATCHED_CURRENT_NSE_LIST")
            self.assertEqual(result.loc["OLDNAME","STATUS"],"MATCHED_RENAMED_SYMBOL")
            self.assertEqual(result.loc["OLDNAME","RESOLVED_SYMBOL"],"NEWNAME")
            self.assertEqual(result.loc["MISSING","STATUS"],"UNKNOWN_NOT_IN_PROVIDED_SNAPSHOTS")
            self.assertEqual(result.loc["CONFLICT","STATUS"],"UNKNOWN_ISIN_CONFLICT")
            report=json.loads((out/"nse_identity_reconciliation_report.json").read_text())
            self.assertEqual(report["rows"],4)
            self.assertEqual(len(report["inputs"]),3)
            self.assertEqual(len(report["output"]["sha256"]),64)

    def test_no_production_mutation(self):
        source=SCRIPT.read_text()
        for forbidden in ("RANKING_SCORE =", "PRESSURE_FADE =", "CORE_672 ="):
            self.assertNotIn(forbidden,source)

if __name__=="__main__":
    unittest.main()
