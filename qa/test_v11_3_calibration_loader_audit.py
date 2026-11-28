"""Isolated audit reproducer for the current V11.3 calibration loader.

This executes the loader statements extracted from the supplied production
source AST. It documents the existing defect; it is not a fix and must not be
interpreted as approval of a production fallback policy.
"""
import ast
import json
import os
import tempfile
import unittest
from pathlib import Path
from pipeline.calibration_gate import validate_calibration_artifact

SOURCE = Path(os.environ.get("V11_3_SOURCE", "pipeline/v11_3_abcd_e.py"))


def extract_loader(source_path=SOURCE):
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    body = main.body
    start = next(i for i, n in enumerate(body) if isinstance(n, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == "calib" for t in n.targets))
    end = next(i for i, n in enumerate(body[start + 1:], start + 1)
               if isinstance(n, ast.Assign) and any(
                   isinstance(t, ast.Name) and t.id == "df" for t in n.targets))
    module = ast.Module(body=body[start:end], type_ignores=[])
    ast.fix_missing_locations(module)
    return compile(module, str(source_path), "exec")


class CalibrationLoaderAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loader_code = extract_loader()

    def load(self, payload=None, create=True):
        with tempfile.TemporaryDirectory() as td:
            old = os.getcwd()
            try:
                os.chdir(td)
                target = Path("outputs/backtest/behavioral_dna_library.json")
                if create:
                    target.parent.mkdir(parents=True)
                    target.write_text(payload, encoding="utf-8")
                ns = {"Path": Path, "json": json, "validate_calibration_artifact": validate_calibration_artifact}
                exec(self.loader_code, ns)
                return ns["calib"]
            finally:
                os.chdir(old)

    def test_missing_file_silently_becomes_empty_mapping(self):
        self.assertEqual(self.load(create=False), {})

    def test_malformed_json_silently_becomes_empty_mapping(self):
        self.assertEqual(self.load("{not-json"), {})

    def test_valid_zero_rate_produces_neutral_calibration(self):
        data = {"CONTINUATION_READY": {"hit10_h3": 0.0}}
        loaded = self.load(json.dumps(data))
        self.assertEqual(loaded, data)
        hist_rate = float(loaded.get("CONTINUATION_READY", {}).get("hit10_h3", 0))
        max_rate = max([float(x.get("hit10_h3", 0)) for x in loaded.values()], default=0.0)
        calibration = max(0.0, min(100.0, 50 + 50 * (hist_rate / max_rate if max_rate else 0)))
        self.assertEqual(calibration, 50.0)

    def test_missing_and_malformed_are_indistinguishable_after_loader(self):
        self.assertEqual(self.load(create=False), self.load("not-json"))

    def test_missing_state_defaults_to_zero_rate(self):
        loaded = self.load(json.dumps({"OTHER_STATE": {"hit10_h3": 0.4}}))
        hist_rate = float(loaded.get("CONTINUATION_READY", {}).get("hit10_h3", 0))
        self.assertEqual(hist_rate, 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
