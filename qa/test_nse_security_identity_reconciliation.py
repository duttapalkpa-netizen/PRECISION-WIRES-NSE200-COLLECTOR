import csv, json, subprocess, sys, tempfile, unittest
from pathlib import Path
from pipeline.nse_security_identity_reconciliation import read_csv, clean

SCRIPT = Path("pipeline/nse_security_identity_reconciliation.py")

class IdentityHelpersTest(unittest.TestCase):
    def write_csv(self, root, name, header, rows):
        p = root / name
        with p.open("w", newline="") as f:
            w = csv.writer(f); w.writerow(header); w.writerows(rows)
        return p

    def run_reconciliation(self, root, stale_rows, equity_rows, changes_rows,
                           equity_header=("SYMBOL", "ISIN"), stale_header=("SYMBOL", "ISIN")):
        stale = self.write_csv(root, "stale.csv", stale_header, stale_rows)
        equity = self.write_csv(root, "equity.csv", equity_header, equity_rows)
        changes = self.write_csv(root, "changes.csv", ["Old Symbol", "New Symbol"], changes_rows or [["", ""]])
        out = root / "out"
        proc = subprocess.run([sys.executable, str(SCRIPT), "--stale", str(stale),
            "--equity", str(equity), "--symbol-changes", str(changes), "--out", str(out)],
            capture_output=True, text=True)
        return proc, out

    def test_normalizes_symbol(self):
        self.assertEqual(clean("  abc "), "ABC")

    def test_csv_headers_normalized(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "x.csv"
            p.write_text("Trading Symbol,ISIN\nABC,INEX\n")
            self.assertIn("TRADINGSYMBOL", read_csv(p).columns)

    def test_end_to_end_direct_rename_unknown_and_isin_conflict(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            proc, out = self.run_reconciliation(root,
                [["DIRECT","INE000000001"],["OLDNAME","INE000000002"],
                 ["MISSING","INE000000003"],["CONFLICT","INE000000004"]],
                [["DIRECT","INE000000001"],["NEWNAME","INE000000002"],
                 ["CONFLICT","INE999999999"]], [["OLDNAME","NEWNAME"]])
            self.assertEqual(proc.returncode, 0, proc.stderr)
            import pandas as pd
            result = pd.read_csv(out/"nse_identity_reconciliation.csv").set_index("OLD_SYMBOL")
            self.assertEqual(result.loc["DIRECT","STATUS"], "MATCHED_CURRENT_NSE_LIST")
            self.assertEqual(result.loc["OLDNAME","STATUS"], "MATCHED_RENAMED_SYMBOL")
            self.assertEqual(result.loc["OLDNAME","RESOLVED_SYMBOL"], "NEWNAME")
            self.assertEqual(result.loc["MISSING","STATUS"], "UNKNOWN_NOT_IN_PROVIDED_SNAPSHOTS")
            self.assertEqual(result.loc["CONFLICT","STATUS"], "UNKNOWN_ISIN_CONFLICT")
            report = json.loads((out/"nse_identity_reconciliation_report.json").read_text())
            self.assertEqual(report["rows"], 4)
            self.assertEqual(len(report["inputs"]), 3)
            self.assertEqual(len(report["output"]["sha256"]), 64)

    def test_same_symbol_in_multiple_security_lists_is_ambiguous(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            stale=self.write_csv(root,"stale.csv",["SYMBOL","ISIN"],[["DUAL","INE000000010"]])
            equity=self.write_csv(root,"equity.csv",["SYMBOL","ISIN"],[["DUAL","INE000000010"]])
            etf=self.write_csv(root,"etf.csv",["SYMBOL","ISIN"],[["DUAL","INE000000010"]])
            changes=self.write_csv(root,"changes.csv",["Old Symbol","New Symbol"],[["",""]])
            out=root/"out"
            proc=subprocess.run([sys.executable,str(SCRIPT),"--stale",str(stale),
                "--equity",str(equity),"--etf",str(etf),"--symbol-changes",str(changes),
                "--out",str(out)],capture_output=True,text=True)
            self.assertEqual(proc.returncode,0,proc.stderr)
            import pandas as pd
            result=pd.read_csv(out/"nse_identity_reconciliation.csv")
            self.assertEqual(result.loc[0,"STATUS"],"UNKNOWN_AMBIGUOUS_CATEGORY")

    def test_multiple_rename_targets_remain_unknown(self):
        with tempfile.TemporaryDirectory() as d:
            proc,out=self.run_reconciliation(Path(d),[["OLD","INE000000020"]],
                [["NEW_A","INE000000020"],["NEW_B","INE000000020"]],
                [["OLD","NEW_A"],["OLD","NEW_B"]])
            self.assertEqual(proc.returncode,0,proc.stderr)
            import pandas as pd
            result=pd.read_csv(out/"nse_identity_reconciliation.csv")
            self.assertEqual(result.loc[0,"STATUS"],"UNKNOWN_AMBIGUOUS_RENAME_OR_CATEGORY")
            self.assertTrue(pd.isna(result.loc[0,"RESOLVED_SYMBOL"]))

    def test_duplicate_stale_symbols_fail_closed(self):
        with tempfile.TemporaryDirectory() as d:
            proc,_=self.run_reconciliation(Path(d),
                [["DUP","INE000000030"],["DUP","INE000000030"]],
                [["DUP","INE000000030"]],[])
            self.assertNotEqual(proc.returncode,0)
            self.assertIn("duplicate stale candidate symbols",proc.stderr)

    def test_blank_stale_symbol_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            proc,_=self.run_reconciliation(Path(d),[["","INE000000040"]],
                [["X","INE000000040"]],[])
            self.assertNotEqual(proc.returncode,0)
            self.assertIn("blank stale candidate symbol",proc.stderr)

    def test_missing_required_source_column_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            proc,_=self.run_reconciliation(Path(d),[["X","INE000000050"]],
                [["X","INE000000050"]],[],equity_header=("NAME","ISIN"))
            self.assertNotEqual(proc.returncode,0)
            self.assertIn("missing required column",proc.stderr)


    def test_matching_isin_does_not_override_conflicting_isin_rows(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            proc, out = self.run_reconciliation(root,
                [["DUAL_ISIN", "INE000000060"]],
                [["DUAL_ISIN", "INE000000060"], ["DUAL_ISIN", "INE999999999"]],
                [])
            self.assertEqual(proc.returncode, 0, proc.stderr)
            import pandas as pd
            result = pd.read_csv(out / "nse_identity_reconciliation.csv")
            self.assertEqual(result.loc[0, "STATUS"], "UNKNOWN_ISIN_CONFLICT")
            self.assertEqual(result.loc[0, "RESOLVED_SYMBOL"], "")

    def test_no_production_mutation(self):
        source=SCRIPT.read_text()
        for forbidden in ("RANKING_SCORE =","PRESSURE_FADE =","CORE_672 ="):
            self.assertNotIn(forbidden,source)

if __name__=="__main__":
    unittest.main()
