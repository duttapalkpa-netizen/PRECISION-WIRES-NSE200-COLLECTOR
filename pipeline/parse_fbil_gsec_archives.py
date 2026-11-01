#!/usr/bin/env python3
"""Parse official FBIL G-Sec published XLSX archives without inventing release times."""
import csv, hashlib, io, json, re
from datetime import datetime, timezone
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path("artifacts/fbil_10y_provenance")
OUT_CSV = ROOT / "fbil_10y_archive_observations.csv"
REPORT = ROOT / "fbil_10y_archive_parse_report.json"

def parse_workbook(data: bytes, source_name: str):
    wb = load_workbook(io.BytesIO(data), data_only=True, read_only=True)
    if "Par Yield" not in wb.sheetnames:
        raise ValueError(f"{source_name}: missing 'Par Yield' sheet")
    ws = wb["Par Yield"]
    title = ws.cell(3, 1).value
    date_value = ws.cell(3, 3).value
    if not isinstance(title, str) or "Par Yield" not in title:
        raise ValueError(f"{source_name}: unexpected Par Yield title")
    if isinstance(date_value, datetime):
        obs_date = date_value.date().isoformat()
    elif date_value:
        obs_date = datetime.strptime(str(date_value), "%d-%b-%Y").date().isoformat()
    else:
        raise ValueError(f"{source_name}: missing publisher observation date")
    matches = []
    for row in ws.iter_rows(min_row=5, values_only=True):
        if not row or row[0] is None:
            continue
        try:
            tenor = float(row[0])
        except (TypeError, ValueError):
            continue
        if abs(tenor - 10.0) < 1e-9:
            matches.append(row)
    if len(matches) != 1:
        raise ValueError(f"{source_name}: expected exactly one 10Y tenor row, got {len(matches)}")
    row = matches[0]
    semi, annual = row[1], row[2]
    if not isinstance(semi, (int, float)) or not isinstance(annual, (int, float)):
        raise ValueError(f"{source_name}: 10Y yield values are not numeric")
    return {
        "OBSERVATION_DATE": obs_date,
        "TENOR": "10YR",
        "YTM_SEMI_ANNUAL_PCT": float(semi),
        "YTM_ANNUALIZED_PCT": float(annual),
        # The XLSX carries a date but no publisher clock time. Do not substitute
        # fetch time, website display time, or a guessed 18:30 timestamp.
        "PUBLISHED_AT_IST": "",
        "RELEASED_AT_UTC": "",
        "SOURCE_FILE": source_name,
        "SOURCE_FILE_SHA256": hashlib.sha256(data).hexdigest(),
        "SOURCE_SHEET": "Par Yield",
    }

def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    files = sorted(ROOT.glob("fbil_gsec_published_*.bin"))
    rows, errors = [], []
    for path in files:
        try:
            item = parse_workbook(path.read_bytes(), path.name)
            expected = re.search(r"(20\\d{6})", path.name)
            if expected:
                filename_date = datetime.strptime(expected.group(1), "%Y%m%d").date().isoformat()
                if filename_date != item["OBSERVATION_DATE"]:
                    raise ValueError(f"{path.name}: filename date != workbook publisher date")
            rows.append(item)
        except Exception as exc:
            errors.append({"file": path.name, "error": str(exc)})
    dates = [r["OBSERVATION_DATE"] for r in rows]
    if len(set(dates)) != len(dates):
        errors.append({"error": "duplicate observation dates in archive inputs"})
    rows.sort(key=lambda x: x["OBSERVATION_DATE"])
    fields = ["OBSERVATION_DATE","TENOR","YTM_SEMI_ANNUAL_PCT","YTM_ANNUALIZED_PCT",
              "PUBLISHED_AT_IST","RELEASED_AT_UTC","SOURCE_FILE","SOURCE_FILE_SHA256","SOURCE_SHEET"]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    report = {
        "status": "FBIL_ARCHIVE_10Y_ROWS_PARSED_RELEASE_TIMESTAMP_MISSING" if rows and not errors else "FBIL_ARCHIVE_PARSE_BLOCKED",
        "source": "Official FBIL /wasdm/gsec/downloadPublished XLSX archive",
        "input_files": len(files), "parsed_rows": len(rows), "errors": errors,
        "date_min": min(dates) if dates else None, "date_max": max(dates) if dates else None,
        "unique_dates": len(set(dates)), "release_timestamp_coverage": 0,
        "timestamp_gap": "Publisher XLSX exposes observation date but no release clock time; no timestamp inferred.",
        "factor_registry_promotion": "NOT_PROMOTED_PENDING_PUBLISHER_RELEASE_TIMESTAMP_AND_WRITTEN_USE_PERMISSION",
        "normalized_csv_sha256": hashlib.sha256(OUT_CSV.read_bytes()).hexdigest(),
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not rows or errors:
        raise RuntimeError("FBIL archive parse failed; inspect retained diagnostics")
if __name__ == "__main__":
    main()
