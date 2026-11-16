"""Contract tests use the provenance-pinned Run #161 excerpt; invalid cases are mutations only."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "fii_dii_contract.py"
spec = importlib.util.spec_from_file_location("fii_dii_contract", MODULE_PATH)
contract = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contract)
validate_rows = contract.validate_rows
maturity_status = contract.maturity_status

FIXTURE = Path(__file__).parents[3] / "tests" / "research_fii_dii_run161" / "fixtures" / "run161_fii_dii_excerpt.json"


class FiiDiiMappingContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.rows = cls.payload["rows"]

    def test_run161_combined_scope_structure_only(self):
        result = validate_rows(self.rows, "NSE_BSE_MSEI_COMBINED")
        self.assertEqual(result["status"], "STRUCTURE_VALIDATED_ONLY")
        self.assertEqual(result["row_count"], 2)
        self.assertEqual(result["groups"], ["DII", "FII_FPI"])
        self.assertEqual(result["distinct_dates"], 1)

    def test_nse_only_scope_is_explicit_not_inferred(self):
        result = validate_rows(self.rows, "NSE_ONLY")
        self.assertEqual(result["declared_scope"], "NSE_ONLY")
        self.assertEqual(result["status"], "STRUCTURE_VALIDATED_ONLY")

    def test_scope_is_reported_as_caller_declared_not_authenticated(self):
        result = validate_rows(self.rows, "NSE_BSE_MSEI_COMBINED")
        self.assertIn("declared_scope", result)
        self.assertNotIn("authenticated_scope", result)

    def test_unknown_scope_rejected(self):
        with self.assertRaisesRegex(ValueError, "scope"):
            validate_rows(self.rows, "ALL_EXCHANGES")

    def test_missing_rows_rejected(self):
        for rows in (None, [], "bad"):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                validate_rows(rows, "NSE_ONLY")

    def test_missing_or_unknown_category_rejected(self):
        for group in (None, "FII", "OTHER"):
            rows = copy.deepcopy(self.rows)
            rows[0]["group"] = group
            with self.subTest(group=group), self.assertRaisesRegex(ValueError, "category"):
                validate_rows(rows, "NSE_BSE_MSEI_COMBINED")

    def test_duplicate_scope_date_category_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows.append(copy.deepcopy(rows[0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_rows(rows, "NSE_BSE_MSEI_COMBINED")

    def test_timestamp_not_accepted_as_observation_date(self):
        rows = copy.deepcopy(self.rows)
        rows[0]["date"] = "2026-11-13T08:00:00Z"
        with self.assertRaisesRegex(ValueError, "date"):
            validate_rows(rows, "NSE_BSE_MSEI_COMBINED")

    def test_invalid_numeric_and_boolean_rejected(self):
        for value in (None, "1.2", float("nan"), float("inf"), True):
            rows = copy.deepcopy(self.rows)
            rows[0]["net_value"] = value
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "numeric"):
                validate_rows(rows, "NSE_BSE_MSEI_COMBINED")

    def test_buy_sell_net_arithmetic_mismatch_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[0]["net_value"] = rows[0]["net_value"] + 1
        with self.assertRaisesRegex(ValueError, "arithmetic"):
            validate_rows(rows, "NSE_BSE_MSEI_COMBINED")

    def test_one_observation_date_is_not_mature_for_twenty_sessions(self):
        self.assertEqual(maturity_status(self.rows, 20), "UNKNOWN")

    def test_maturity_threshold_must_be_explicit_positive_integer(self):
        for threshold in (0, -1, 1.5, True):
            with self.subTest(threshold=threshold), self.assertRaisesRegex(ValueError, "positive integer"):
                maturity_status(self.rows, threshold)

    def test_distinct_date_count_not_row_count_controls_maturity(self):
        duplicated_categories_same_date = self.rows + [copy.deepcopy(self.rows[0])]
        self.assertEqual(maturity_status(duplicated_categories_same_date, 2), "UNKNOWN")

    def test_validation_never_emits_market_direction(self):
        result = validate_rows(self.rows, "NSE_BSE_MSEI_COMBINED")
        self.assertNotIn("signal", result)
        self.assertNotIn("state", result)
        self.assertNotIn("POSITIVE", result.values())
        self.assertNotIn("NEGATIVE", result.values())


if __name__ == "__main__":
    unittest.main(verbosity=2)
