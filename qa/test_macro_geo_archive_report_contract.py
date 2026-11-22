"""Regression: Macro-Geo NSE archive report producer/consumer schema stays aligned."""
import ast
from pathlib import Path


def test_nse_index_archive_report_schema_matches_consumer():
    source = Path("pipeline/macro_geo_collect_p0.py").read_text(encoding="utf-8")
    tree = ast.parse(source)

    producer_keys = set()
    consumer_keys = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "nse_index_history":
            for child in ast.walk(node):
                if isinstance(child, ast.Return) and isinstance(child.value, ast.Tuple):
                    report = child.value.elts[1]
                    if isinstance(report, ast.Dict):
                        producer_keys.update(
                            key.value for key in report.keys
                            if isinstance(key, ast.Constant) and isinstance(key.value, str)
                        )
        if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == "archive_report":
            key = node.slice
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                consumer_keys.add(key.value)

    assert "observed_session_requests" in producer_keys
    assert "rows" in producer_keys
    assert "failures" in producer_keys
    assert "observed_session_requests" in consumer_keys
    assert "weekday_requests" not in consumer_keys
