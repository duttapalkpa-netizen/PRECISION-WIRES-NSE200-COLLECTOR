import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "iip_ledger_guard", ROOT / "qa" / "iip_certified_cell_ledger_guard.py")
GUARD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUARD)

LEDGER = ROOT / "data/macro/IIP_CELL_LEVEL_REVISION_BATCH_001_2023-04.csv"
SUMMARY = ROOT / "data/macro/IIP_CELL_LEVEL_REVISION_BATCH_001_SUMMARY.json"

class LedgerGuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        with SUMMARY.open(encoding="utf-8") as f:
            self.summary = json.load(f)
        with LEDGER.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.fields = reader.fieldnames
            self.rows = list(reader)

    def tearDown(self):
        self.tmp.cleanup()

    def write_ledger(self, name, rows, fields=None):
        path = self.root / name
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields or self.fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        return path

    def write_summary(self, summary=None):
        path = self.root / "summary.json"
        path.write_text(json.dumps(summary or self.summary), encoding="utf-8")
        return path

    def test_real_batch_001_passes(self):
        result = GUARD.audit([LEDGER], SUMMARY)
        self.assertEqual(result["status"], "PASS_LEDGER_GUARD")
        self.assertEqual(result["certified_rows_checked"], 9)
        self.assertEqual(result["unique_transition_keys"], 9)

    def test_duplicate_across_batches_is_blocked(self):
        first = self.write_ledger("batch_a.csv", self.rows)
        second = self.write_ledger("batch_b.csv", [self.rows[0]])
        result = GUARD.audit([first, second], self.write_summary())
        self.assertEqual(result["status"], "BLOCKED_LEDGER_GUARD")
        self.assertTrue(any("duplicate" in e for e in result["errors"]))

    def test_accounting_mismatch_is_blocked(self):
        bad = dict(self.summary)
        bad["remaining_policy_aligned_candidates_not_certified"] += 1
        ledger = self.write_ledger("ledger.csv", self.rows)
        result = GUARD.audit([ledger], self.write_summary(bad))
        self.assertEqual(result["status"], "BLOCKED_LEDGER_GUARD")
        self.assertTrue(any("partition" in e for e in result["errors"]))

    def test_missing_provenance_column_is_blocked(self):
        fields = [x for x in self.fields if x != "previous_workbook_cell"]
        ledger = self.write_ledger("ledger.csv", self.rows, fields)
        result = GUARD.audit([ledger], self.write_summary())
        self.assertEqual(result["status"], "BLOCKED_LEDGER_GUARD")
        self.assertTrue(any("missing columns" in e for e in result["errors"]))

    def test_hard_gate_cannot_be_promoted(self):
        bad = dict(self.summary)
        bad["hard_gate"] = "PASS"
        ledger = self.write_ledger("ledger.csv", self.rows)
        result = GUARD.audit([ledger], self.write_summary(bad))
        self.assertEqual(result["status"], "BLOCKED_LEDGER_GUARD")
        self.assertEqual(result["hard_gate"], "BLOCKED")

if __name__ == "__main__":
    unittest.main(verbosity=2)
