"""Research-only FII/DII schema tests; deliberately computes no market signal."""
import json, math, re, unittest
from pathlib import Path

FIXTURE = Path(__file__).parent / "fixtures" / "run161_fii_dii_excerpt.json"
ALLOWED_GROUPS = {"FII_FPI", "DII"}
DATE_RE = re.compile(r"^\\d{2}-[A-Z][a-z]{2}-\\d{4}$")

def validate_context(payload):
    """Validate structure only. Never aggregates or emits POSITIVE/NEGATIVE."""
    if not isinstance(payload, dict): raise ValueError("context must be an object")
    if not isinstance(payload.get("generated_at"), str) or not payload["generated_at"].strip():
        raise ValueError("missing generated_at")
    if not isinstance(payload.get("source"), str) or "NSE /api/fiidiiTradeReact" not in payload["source"]:
        raise ValueError("missing/unrecognized source provenance")
    rows = payload.get("rows")
    if not isinstance(rows, list) or not rows: raise ValueError("fii_dii rows missing or empty")
    seen = set()
    for row in rows:
        if not isinstance(row, dict): raise ValueError("row must be an object")
        group, date = row.get("group"), row.get("date")
        if group not in ALLOWED_GROUPS: raise ValueError("unknown/missing group")
        if not isinstance(date, str) or not DATE_RE.fullmatch(date):
            raise ValueError("invalid/date-only observation date required")
        key = (group, date)
        if key in seen: raise ValueError("duplicate group/date")
        seen.add(key)
        value = row.get("net_value")
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError("net_value must be finite numeric")
    return {"status": "SCHEMA_VALIDATED_ONLY", "row_count": len(rows),
            "groups": sorted({r["group"] for r in rows})}

class FiiDiiContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    def test_01_real_run161_excerpt_schema(self):
        result = validate_context(self.fixture)
        self.assertEqual(result["status"], "SCHEMA_VALIDATED_ONLY")
        self.assertEqual(result["row_count"], 2)
        self.assertEqual(result["groups"], ["DII", "FII_FPI"])
    def test_02_no_legacy_field_dependency(self):
        for row in self.fixture["rows"]:
            self.assertIn("net_value", row)
            self.assertNotIn("fii_net", row); self.assertNotIn("dii_net", row)
    def test_03_missing_category_not_zero_filled(self):
        p = dict(self.fixture, rows=[self.fixture["rows"][0]])
        self.assertEqual(validate_context(p)["groups"], ["DII"])
    def test_04_duplicate_group_date_rejected(self):
        p = dict(self.fixture, rows=self.fixture["rows"] + [dict(self.fixture["rows"][0])])
        with self.assertRaisesRegex(ValueError, "duplicate"): validate_context(p)
    def test_05_unknown_group_rejected(self):
        p = json.loads(json.dumps(self.fixture)); p["rows"][0]["group"] = "OTHER"
        with self.assertRaisesRegex(ValueError, "unknown"): validate_context(p)
    def test_06_invalid_net_values_rejected(self):
        for bad in (None, "-2253.58", float("nan"), float("inf"), True):
            p = json.loads(json.dumps(self.fixture)); p["rows"][0]["net_value"] = bad
            with self.subTest(value=bad), self.assertRaisesRegex(ValueError, "finite numeric"):
                validate_context(p)
    def test_07_missing_provenance_rejected(self):
        p = dict(self.fixture); p.pop("source")
        with self.assertRaisesRegex(ValueError, "provenance"): validate_context(p)
    def test_08_invalid_date_rejected(self):
        p = json.loads(json.dumps(self.fixture)); p["rows"][0]["date"] = "2026-11-13T08:00:00Z"
        with self.assertRaisesRegex(ValueError, "date-only"): validate_context(p)
    def test_09_missing_generated_at_rejected(self):
        p = dict(self.fixture); p.pop("generated_at")
        with self.assertRaisesRegex(ValueError, "generated_at"): validate_context(p)
    def test_10_missing_or_empty_rows_rejected(self):
        for rows in (None, [], "bad"):
            p = dict(self.fixture, rows=rows)
            with self.subTest(rows=rows), self.assertRaises(ValueError): validate_context(p)

if __name__ == "__main__": unittest.main(verbosity=2)
