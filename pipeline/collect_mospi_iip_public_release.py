#!/usr/bin/env python3
"""Fetch and preserve a public MoSPI IIP aggregate release page; no credentials."""
from __future__ import annotations
import argparse, csv, hashlib, json, os, re, urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

URL = "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475&lang=1&reg=3"

class Tables(HTMLParser):
    def __init__(self):
        super().__init__(); self.tables=[]; self.in_table=False; self.in_cell=False
        self.table=[]; self.row=[]; self.cell=[]
    def handle_starttag(self, tag, attrs):
        if tag=="table":
            self.in_table=True; self.table=[]
        elif self.in_table and tag=="tr": self.row=[]
        elif self.in_table and tag in ("td","th"):
            self.in_cell=True; self.cell=[]
    def handle_data(self, data):
        if self.in_table and self.in_cell: self.cell.append(data)
    def handle_endtag(self, tag):
        if self.in_table and tag in ("td","th") and self.in_cell:
            self.row.append(" ".join(" ".join(self.cell).split())); self.in_cell=False
        elif self.in_table and tag=="tr":
            if self.row: self.table.append(self.row)
        elif tag=="table" and self.in_table:
            if self.table: self.tables.append(self.table)
            self.in_table=False

def parse_html(raw: bytes):
    text=raw.decode("utf-8", errors="replace")
    p=Tables(); p.feed(text)
    return text, p.tables


def normalize_statement_iv(tables):
    """Normalize a 13-month NIC-2 index table, independent of table header wrapping."""
    month_names = {"jan":"01","feb":"02","mar":"03","apr":"04","may":"05","jun":"06",
                   "jul":"07","aug":"08","sep":"09","oct":"10","nov":"11","dec":"12"}

    def parse_month(label):
        token = " ".join(label.split()).strip().replace("’", "'")
        for separator in ("-", "'", " "):
            parts = token.split(separator)
            if len(parts) == 2 and parts[0][:3].lower() in month_names and parts[1].isdigit():
                year = int(parts[1])
                year += 2000 if year < 80 else 1900
                return f"{year:04d}-{month_names[parts[0][:3].lower()]}"
        return None

    for table_id, rows in enumerate(tables, start=1):
        for header_i, row in enumerate(rows):
            cells = [" ".join(str(x).split()).strip() for x in row]
            lowered = [x.lower() for x in cells]
            if not any("nic 2025" in x for x in lowered):
                continue
            if not any("description" in x for x in lowered):
                continue
            if not any(x == "weight" or x.startswith("weight ") for x in lowered):
                continue

            month_cols = []
            for i, cell in enumerate(cells):
                period = parse_month(cell)
                if period:
                    month_cols.append((i, period))
            # The requested September 2026 Statement IV is a 13-month window.
            if len(month_cols) != 13:
                continue

            nic_i = next(i for i, x in enumerate(lowered) if "nic 2025" in x)
            desc_i = next(i for i, x in enumerate(lowered) if "description" in x)
            weight_i = next(i for i, x in enumerate(lowered) if x == "weight" or x.startswith("weight "))
            required_i = max([nic_i, desc_i, weight_i] + [i for i, _ in month_cols])
            output = []
            seen = set()
            for data_row in rows[header_i + 1:]:
                if len(data_row) <= required_i:
                    continue
                nic = " ".join(str(data_row[nic_i]).split()).strip()
                if len(nic) != 2 or not nic.isdigit():
                    continue
                desc = " ".join(str(data_row[desc_i]).split()).strip()
                try:
                    weight = float(str(data_row[weight_i]).replace(",", "").strip())
                except ValueError:
                    continue
                for col, period in month_cols:
                    raw_value = str(data_row[col]).replace(",", "").strip()
                    if not raw_value:
                        raise ValueError(f"Missing index for NIC {nic}, period {period}")
                    try:
                        value = float(raw_value)
                    except ValueError as exc:
                        raise ValueError(f"Invalid index for NIC {nic}, period {period}: {raw_value}") from exc
                    key = (nic, period)
                    if key in seen:
                        raise ValueError(f"Duplicate NIC-period key: {key}")
                    seen.add(key)
                    estimate_status = (
                        "quick_estimate" if period == "2026-09" else
                        "final_revision" if period == "2026-08" else
                        "historical_value_as_published_in_2026-09_release"
                    )
                    output.append({
                        "period": period, "nic_2025": nic, "description": desc,
                        "weight": weight, "index": value, "base_year": "2022-23",
                        "frequency": "M", "unit": "index", "source_table_id": table_id,
                        "release_vintage": "2026-09_release",
                        "estimate_status": estimate_status
                    })
            if output:
                expected_periods = []
                year, month = 2025, 9
                for _ in range(13):
                    expected_periods.append(f"{year:04d}-{month:02d}")
                    month += 1
                    if month == 13:
                        year += 1
                        month = 1
                by_nic = {}
                for item in output:
                    by_nic.setdefault(item["nic_2025"], []).append(item["period"])
                for nic, periods in sorted(by_nic.items()):
                    if len(periods) != len(set(periods)):
                        raise ValueError(f"Duplicate periods for NIC {nic}")
                return table_id, output
    return None, []

def collect(out: Path, opener=urllib.request.urlopen):
    req=urllib.request.Request(URL, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":"en-IN,en;q=0.9","Cache-Control":"no-cache"})
    with opener(req, timeout=30) as response:
        raw=response.read()
        status=getattr(response,"status",200)
        content_type=response.headers.get("Content-Type","")
        final_url=response.geturl()
    if status != 200: raise RuntimeError(f"HTTP status {status}")
    if "html" not in content_type.lower(): raise RuntimeError(f"Unexpected content type: {content_type}")
    html, tables=parse_html(raw)
    required=("September 2026","6.7","Base: 2022-23=100","STATEMENT II A")
    missing=[x for x in required if x.lower() not in html.lower()]
    if missing: raise RuntimeError(f"Official release content markers missing: {missing}")
    out.mkdir(parents=True, exist_ok=True)
    (out/"mospi_iip_release_raw.html").write_bytes(raw)
    (out/"mospi_iip_tables.json").write_text(json.dumps(tables,ensure_ascii=False,indent=2),encoding="utf-8")
    inventory=[]
    for table_id, rows in enumerate(tables, start=1):
        width=max((len(row) for row in rows),default=0)
        csv_path=out/f"table_{table_id:02d}.csv"
        with csv_path.open("w",encoding="utf-8-sig",newline="") as handle:
            writer=csv.writer(handle)
            writer.writerow([f"COL_{i:02d}" for i in range(1,width+1)])
            for row in rows: writer.writerow(row+[""]*(width-len(row)))
        inventory.append({"table_id":table_id,"rows":len(rows),"columns":width,
          "nonempty_cells":sum(bool(c.strip()) for r in rows for c in r),"file":csv_path.name})
    (out/"table_inventory.json").write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
    normalized_table_id, normalized=normalize_statement_iv(tables)
    if not normalized: raise RuntimeError("Could not identify a NIC-2025 monthly index table with 13 month columns")
    expected_periods=[]
    year,month=2025,9
    for _ in range(13):
        expected_periods.append(f"{year:04d}-{month:02d}")
        month+=1
        if month==13:
            year+=1
            month=1
    by_nic={}
    for item in normalized:
        by_nic.setdefault(item["nic_2025"],[]).append(item["period"])
    if len(by_nic)!=23:
        raise RuntimeError(f"Expected 23 NIC-2 groups in official Statement IV; found {len(by_nic)}")
    for nic,periods in sorted(by_nic.items()):
        if sorted(periods)!=expected_periods:
            missing=sorted(set(expected_periods)-set(periods))
            extra=sorted(set(periods)-set(expected_periods))
            raise RuntimeError(f"NIC {nic} coverage failure; missing={missing}, extra={extra}")
    if len(normalized)!=299:
        raise RuntimeError(f"Expected 299 NIC-period observations; found {len(normalized)}")
    with (out/"iip_nic2_monthly_panel.csv").open("w",encoding="utf-8-sig",newline="") as handle:
        writer=csv.DictWriter(handle,fieldnames=list(normalized[0].keys()))
        writer.writeheader(); writer.writerows(normalized)
    nic_coverage = {}
    for item in normalized:
        nic_coverage.setdefault(item["nic_2025"], set()).add(item["period"])
    expected_periods = sorted({x["period"] for x in normalized})
    coverage_rows = []
    for nic in sorted(nic_coverage):
        missing = sorted(set(expected_periods) - nic_coverage[nic])
        coverage_rows.append({"nic_2025":nic,"months_present":len(nic_coverage[nic]),
          "expected_months":13,"missing_periods":missing,"status":"PASS" if not missing and len(nic_coverage[nic]) == 13 else "BLOCKED"})
    with (out/"nic_coverage.csv").open("w",encoding="utf-8-sig",newline="") as handle:
        writer=csv.DictWriter(handle,fieldnames=["nic_2025","months_present","expected_months","missing_periods","status"])
        writer.writeheader()
        for row in coverage_rows:
            writer.writerow({**row,"missing_periods":";".join(row["missing_periods"])})
    vintage_rows=[x for x in normalized if x["period"] in ("2026-08","2026-09")]
    with (out/"iip_nic2_vintage_observations.csv").open("w",encoding="utf-8-sig",newline="") as handle:
        writer=csv.DictWriter(handle,fieldnames=list(vintage_rows[0].keys()))
        writer.writeheader(); writer.writerows(vintage_rows)
    qa={"status":"PASS" if len(coverage_rows)==23 and all(x["status"]=="PASS" for x in coverage_rows) else "BLOCKED",
      "table_count":len(tables),"normalized_table_id":normalized_table_id,
      "normalized_rows":len(normalized),"unique_nic_codes":len(nic_coverage),
      "unique_periods":len(set(x["period"] for x in normalized)),
      "duplicate_nic_period_keys":0,"nic_coverage_pass_count":sum(x["status"]=="PASS" for x in coverage_rows),
      "nic_coverage_blocked_count":sum(x["status"]!="PASS" for x in coverage_rows),
      "vintage_counts":{"2026-08_final_revision":sum(x["estimate_status"]=="final_revision" for x in normalized),
        "2026-09_quick_estimate":sum(x["estimate_status"]=="quick_estimate" for x in normalized)},
      "base_year":"2022-23","frequency":"M",
      "period_min":min(x["period"] for x in normalized),"period_max":max(x["period"] for x in normalized)}
    (out/"domain_qa.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
    manifest={
      "source":"MoSPI release via Press Information Bureau",
      "url":URL,"final_url":final_url,"http_status":status,"content_type":content_type,
      "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
      "sha256_raw":hashlib.sha256(raw).hexdigest(),"raw_bytes":len(raw),
      "table_count":len(tables),"release_reference_period":"2026-09",
      "release_posted_ist":"2026-10-28 16:00",
      "base_year":"2022-23","series_deflator":"Output PPI",
"verification":"PUBLIC_HTML_CAPTURE_TABLE_INVENTORY_NIC2_13_MONTH_COVERAGE_AND_VINTAGE_TAGGING",
"normalized_rows":len(normalized),
"normalized_table_id":normalized_table_id,
      "limitations":["No e-Sankhyiki CSV/API response captured in this run.",
        "HTML table extraction is archival diagnostic; numeric schema/domain normalization remains pending.",
        "Quick estimates are revisable; preserve each release vintage."]
    }
    (out/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return manifest

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--out",default="artifacts/mospi_iip_public_smoke")
    args=ap.parse_args(); print(json.dumps(collect(Path(args.out)),indent=2))
