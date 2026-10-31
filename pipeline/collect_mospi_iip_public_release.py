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
    """Normalize NIC-2 monthly index panel only when the release headers identify it."""
    month_re = re.compile(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[-'](\\d{2})$", re.I)
    for table_id, rows in enumerate(tables, start=1):
        for header_i, row in enumerate(rows):
            cells=[re.sub(r"\\s+"," ",x).strip() for x in row]
            joined=" | ".join(cells).lower()
            if "nic 2025" not in joined or "description" not in joined or "weight" not in joined:
                continue
            month_cols=[]
            for i,cell in enumerate(cells):
                m=month_re.match(cell)
                if m:
                    year=int(m.group(2)); year += 2000 if year < 80 else 1900
                    month_cols.append((i,f"{year:04d}-{ {'jan':'01','feb':'02','mar':'03','apr':'04','may':'05','jun':'06','jul':'07','aug':'08','sep':'09','oct':'10','nov':'11','dec':'12'}[m.group(1).lower()] }"))
            if len(month_cols)<12:
                continue
            weight_i=next(i for i,x in enumerate(cells) if x.lower()=="weight")
            nic_i=next(i for i,x in enumerate(cells) if x.lower()=="nic 2025")
            desc_i=next(i for i,x in enumerate(cells) if x.lower()=="description")
            output=[]
            seen=set()
            for data_row in rows[header_i+1:]:
                if len(data_row)<=max([weight_i,nic_i,desc_i]+[i for i,_ in month_cols]):
                    continue
                nic=data_row[nic_i].strip()
                if not re.fullmatch(r"\\d{2}",nic):
                    continue
                desc=data_row[desc_i].strip()
                try: weight=float(data_row[weight_i].replace(",","").strip())
                except ValueError: continue
                for col,period in month_cols:
                    raw_value=data_row[col].replace(",","").strip()
                    if not raw_value: continue
                    value=float(raw_value)
                    key=(nic,period)
                    if key in seen: raise ValueError(f"Duplicate NIC-period key: {key}")
                    seen.add(key)
                    output.append({"period":period,"nic_2025":nic,"description":desc,
                      "weight":weight,"index":value,"base_year":"2022-23",
                      "frequency":"M","unit":"index","source_table_id":table_id})
            if output:
                return table_id,output
    return None,[]

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
    if not normalized: raise RuntimeError("Could not identify a NIC-2025 monthly index table with >=12 month columns")
    with (out/"iip_nic2_monthly_panel.csv").open("w",encoding="utf-8-sig",newline="") as handle:
        writer=csv.DictWriter(handle,fieldnames=list(normalized[0].keys()))
        writer.writeheader(); writer.writerows(normalized)
    qa={"status":"PASS","table_count":len(tables),"normalized_table_id":normalized_table_id,
      "normalized_rows":len(normalized),"unique_nic_codes":len(set(x["nic_2025"] for x in normalized)),
      "unique_periods":len(set(x["period"] for x in normalized)),
      "duplicate_nic_period_keys":0,"base_year":"2022-23","frequency":"M",
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
"verification":"PUBLIC_HTML_CAPTURE_TABLE_INVENTORY_AND_NIC2_MONTHLY_PANEL_QA",
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
