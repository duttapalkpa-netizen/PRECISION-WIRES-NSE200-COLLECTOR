#!/usr/bin/env python3
"""Download and audit the latest official OEA WPI 2022-23 monthly workbook.

This is source-ingestion QA only. It does not promote factors or alter production logic.
"""
import csv, hashlib, json, re, ssl, urllib.parse, urllib.request
from datetime import datetime, date, timezone
from pathlib import Path
from html.parser import HTMLParser
from openpyxl import load_workbook
import certifi

OUT = Path("artifacts/macro_full_history_discovery")
PAGE = OUT / "oea_download_data_2223.html"
UA = "Mozilla/5.0 (compatible; PRECISION-WIRES-OEA-WPI-Itemwise-Audit/1.0)"
MONTHS = {m.lower(): i for i, m in enumerate(
    ("January","February","March","April","May","June","July","August","September","October","November","December"), 1)}
MONTHS.update({k[:3]: v for k, v in list(MONTHS.items())})

class Anchors(HTMLParser):
    def __init__(self):
        super().__init__(); self.items=[]; self.href=None; self.text=[]
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.href = dict(attrs).get("href"); self.text=[]
    def handle_data(self, data):
        if self.href is not None: self.text.append(data.strip())
    def handle_endtag(self, tag):
        if tag == "a" and self.href is not None:
            self.items.append((self.href, " ".join(x for x in self.text if x)))
            self.href=None; self.text=[]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def period_label(value):
    if isinstance(value, (datetime, date)):
        return value.strftime("%Y-%m")
    if value is None:
        return None
    s = str(value).strip()
    m = re.search(r"(?i)\b(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s*[-/]?\s*(\d{2}|20\d{2})\b", s)
    if m:
        year = m.group(2)
        # OEA workbook headers use both Apr-2023 and Apr-23 conventions.
        year = int(year) + (2000 if len(year) == 2 else 0)
        return f"{year:04d}-{MONTHS[m.group(1).lower()[:3]]:02d}"
    m = re.search(r"\b(20\d{2})[-/](0?[1-9]|1[0-2])\b", s)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}"
    return None

def _header_score(row):
    tokens = [str(x).strip().lower() for x in row if x is not None]
    words = ("item", "commodity", "code", "description", "month", "year", "index", "weight", "group")
    return sum(any(w in x for w in words) for x in tokens) + sum(period_label(x) is not None for x in row)

def parse_sheet_rows(sheet_name, rows):
    """Return sheet metadata and normalized item-period observations."""
    rows = [list(r) for r in rows]
    if not rows:
        return {"sheet": sheet_name, "parse_status": "EMPTY_SHEET", "observations": []}
    scan = min(30, len(rows))
    header_idx = max(range(scan), key=lambda i: _header_score(rows[i]))
    headers = rows[header_idx]
    norm = [str(x).strip().lower() if x is not None else "" for x in headers]
    code_col = next((i for i, h in enumerate(norm) if re.search(r"(item|commodity|product)?\s*code|code\s*(no|number)", h)), None)
    label_col = next((i for i, h in enumerate(norm) if any(w in h for w in ("commodity", "item description", "item name", "description", "commodity name"))), None)
    if label_col is None:
        label_col = next((i for i, h in enumerate(norm) if h in ("item", "name", "group")), None)
    period_cols = [(i, period_label(v)) for i, v in enumerate(headers) if period_label(v)]
    period_cols = [(i, p) for i, p in period_cols if p]
    observations=[]; item_keys=set(); missing_code=0
    for ridx, row in enumerate(rows[header_idx+1:], header_idx+2):
        if not any(v is not None and str(v).strip() for v in row):
            continue
        code = row[code_col] if code_col is not None and code_col < len(row) else None
        label = row[label_col] if label_col is not None and label_col < len(row) else None
        if code is None and label is None:
            continue
        code_s = str(code).strip() if code is not None else ""
        label_s = str(label).strip() if label is not None else ""
        if not code_s: missing_code += 1
        key = (code_s, label_s)
        item_keys.add(key)
        for col, period in period_cols:
            value = row[col] if col < len(row) else None
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                observations.append({
                    "source_sheet": sheet_name, "source_row": ridx,
                    "item_code": code_s or None, "item_label": label_s or None,
                    "period": period, "value": value,
                    "revision_status": "NOT_STATED_IN_WORKBOOK"
                })
    status = "ITEM_PERIODS_PARSED" if observations else "NO_MONTHLY_OBSERVATIONS"
    return {
        "sheet": sheet_name, "parse_status": status, "header_row_1based": header_idx+1,
        "item_code_column": code_col, "item_label_column": label_col,
        "period_columns": [{"column_1based": i+1, "period": p} for i,p in period_cols],
        "item_keys": len(item_keys), "missing_item_code_rows": missing_code,
        "observation_count": len(observations), "observations": observations
    }

def strict_get(url, limit=120_000_000):
    ctx = ssl.create_default_context(cafile=certifi.where())
    host = urllib.parse.urlparse(url).hostname or ""
    if host not in ("eaindustry.nic.in", "www.eaindustry.nic.in"):
        raise RuntimeError("Refusing non-OEA host for WPI workbook")
    bundle = OUT / "tls_diagnostics" / "oea_untrusted_chain.pem"
    proof = OUT / "tls_diagnostics" / "oea_tls_chain_verification.json"
    if not bundle.is_file() or not proof.is_file():
        raise RuntimeError("Verified OEA certificate bundle/evidence missing; WPI remains NOT_CONNECTED")
    evidence = json.loads(proof.read_text())
    if evidence.get("status") != "STRICT_TLS_PASS" or evidence.get("hostname_checks") != {
        "eaindustry.nic.in": "PASS", "www.eaindustry.nic.in": "PASS"
    }:
        raise RuntimeError("Strict OEA TLS/hostname evidence did not PASS")
    ctx.load_verify_locations(cafile=str(bundle))
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,*/*"})
    with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx)).open(req, timeout=60) as r:
        final = urllib.parse.urlparse(r.geturl())
        if r.status != 200 or final.scheme != "https" or final.hostname not in ("eaindustry.nic.in", "www.eaindustry.nic.in"):
            raise RuntimeError("OEA workbook fetch failed approved HTTPS host/HTTP-200 check")
        body = r.read(limit)
        if not body.startswith(b"PK"):
            raise RuntimeError("OEA monthly WPI download is not an OOXML workbook")
        return body, {"http_status": r.status, "final_url": r.geturl(), "content_type": r.headers.get("Content-Type", ""), "bytes": len(body)}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if not PAGE.is_file():
        raise RuntimeError("Official OEA 2022-23 download page missing; run source discovery first")
    parser = Anchors(); parser.feed(PAGE.read_text(encoding="utf-8", errors="replace"))
    candidates=[]
    for href, text in parser.items:
        absolute=urllib.parse.urljoin("https://eaindustry.nic.in/download_data_2223.asp", href)
        m=re.search(r"/wpi_monthly_index_(20\d{4})\.xlsx$", urllib.parse.urlparse(absolute).path, re.I)
        if m and urllib.parse.urlparse(absolute).hostname == "eaindustry.nic.in":
            candidates.append((m.group(1), absolute, text))
    if not candidates:
        raise RuntimeError("No official OEA WPI 2022-23 monthly index workbook link found")
    period, url, link_text = sorted(candidates)[-1]
    body, meta = strict_get(url)
    raw = OUT / f"OEA_WPI_2022-23_monthly_index_{period}.xlsx"
    raw.write_bytes(body)
    wb = load_workbook(raw, read_only=True, data_only=True)
    sheet_reports=[]; all_obs=[]
    for ws in wb.worksheets:
        parsed = parse_sheet_rows(ws.title, ws.iter_rows(values_only=True))
        all_obs.extend(parsed.pop("observations"))
        sheet_reports.append(parsed)
    wb.close()
    csv_path = OUT / "OEA_WPI_2022-23_itemwise_monthly_observations.csv"
    fields=["source_sheet","source_row","item_code","item_label","period","value","revision_status"]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer=csv.DictWriter(f, fieldnames=fields); writer.writeheader(); writer.writerows(all_obs)
    item_pairs={(x["item_code"],x["item_label"]) for x in all_obs}
    item_codes={x["item_code"] for x in all_obs if x["item_code"]}
    periods=sorted({x["period"] for x in all_obs})
    report={
        "status": "ITEMWISE_INGESTION_PASS" if all_obs and item_pairs else "ITEMWISE_INGESTION_BLOCKED",
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": {"publisher":"Office of Economic Adviser, DPIIT, Government of India",
                   "series":"WPI 2022-23 base year", "period_suffix":period,
                   "link_text":link_text, "url":url, **meta,
                   "raw_file":raw.name, "raw_sha256":sha(body)},
        "workbook": {"sheet_count":len(sheet_reports), "sheets":sheet_reports,
                     "item_key_count":len(item_pairs), "distinct_item_code_count":len(item_codes),
                     "missing_item_code_observations":sum(1 for x in all_obs if not x["item_code"]),
                     "observation_count":len(all_obs), "period_count":len(periods),
                     "periods":periods, "latest_observation_period":max(periods) if periods else None,
                     "requested_period":f"{period[:4]}-{period[4:6]}",
                     "requested_period_included":f"{period[:4]}-{period[4:6]}" in periods,
                     "revision_status":"NOT_STATED_IN_WORKBOOK; no provisional/final label inferred"},
        "normalized_csv": {"file":csv_path.name, "rows":len(all_obs),
                           "sha256":sha(csv_path.read_bytes())},
        "classification": "SOURCE_EVIDENCE_ONLY_NOT_PROMOTED_TO_FACTOR_REGISTRY"
    }
    (OUT/"oea_wpi_itemwise_manifest.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("status","source","workbook","normalized_csv","classification")},ensure_ascii=False,indent=2))
    if report["status"] != "ITEMWISE_INGESTION_PASS":
        raise RuntimeError("WPI workbook downloaded but item-period extraction did not meet QA gate")

if __name__ == "__main__":
    main()
