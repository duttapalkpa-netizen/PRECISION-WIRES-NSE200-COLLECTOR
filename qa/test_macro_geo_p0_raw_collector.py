import importlib.util
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("collector", Path("pipeline/macro_geo_p0_raw_collector.py"))
collector = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(collector)

def test_csv_expected_date_and_index_name_pass():
    body = b"Date,Index Name,Close\n01-Oct-2025,NIFTY 50,25000\n"
    ok, detail = collector.validate_csv(body, {
        "expected_date": "2025-10-01",
        "index_name_column": "Index Name",
        "expected_index_names": ["NIFTY 50"],
        "required_columns": ["Close"],
    })
    assert ok, detail

def test_csv_wrong_date_fails():
    body = b"Date,Index Name,Close\n02-Oct-2025,NIFTY 50,25000\n"
    ok, detail = collector.validate_csv(body, {"expected_date": "2025-10-01"})
    assert not ok and detail["reason"] == "EXPECTED_DATE_NOT_FOUND"

def test_csv_wrong_index_fails():
    body = b"Date,Index Name,Close\n01-Oct-2025,NIFTY BANK,50000\n"
    ok, detail = collector.validate_csv(body, {
        "expected_date": "2025-10-01",
        "index_name_column": "Index Name",
        "expected_index_names": ["NIFTY 50"],
    })
    assert not ok and detail["reason"] == "EXPECTED_INDEX_NAMES_MISSING"

def test_html_is_not_valid_csv():
    ok, detail = collector.validate_csv(b"<html>Access denied</html>", {"expected_date": "2025-10-01"})
    assert not ok and detail["reason"] in {"CSV_PARSE_ERROR", "CSV_NO_DATA_ROWS", "DATE_COLUMN_MISSING"}

def test_official_host_allowlist():
    assert collector.allowed("https://www.nseindia.com/reports-indices-historical-vix")
    assert collector.allowed("https://www.pib.gov.in/PressReleasePage.aspx?PRID=2175552")
    assert not collector.allowed("http://www.nseindia.com/file.csv")
    assert not collector.allowed("https://example.com/file.csv")
