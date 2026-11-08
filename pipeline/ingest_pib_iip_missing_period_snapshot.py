#!/usr/bin/env python3
"""Supplement missing legacy NIC-2008 IIP observations from an official PIB snapshot.

This sidecar does NOT backfill or impersonate missing MoSPI catalogue vintages.
It records only the three missing reference periods from PIB's later March-2026
release, explicitly labelled as a later published snapshot, not first-release
values. Legacy base 2011-12 ends at March 2026; the 2022-23/NIC-2025 series is
kept separate.
"""
from __future__ import annotations
import csv, hashlib, json, re, urllib.request
from html.parser import HTMLParser
from pathlib import Path

URL = "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2256241&lang=2&reg=48"
OUT = Path("artifacts/iip_41_vintage_audit")
TARGETS = {"Apr-25":"2025-04", "Sep-25":"2025-09", "Feb-26":"2026-02"}
EXPECTED_CODES = {str(x) for x in range(10, 33)}
UA = "Mozilla/5.0 (compatible; PRECISION-WIRES-IIP-PIB-Snapshot-Audit/1.0)"

class Tables(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables=[]; self.table_depth=0; self.row=None; self.cell=None; self.rows=None
    def handle_starttag(self, tag, attrs):
        if tag=="table":
            if self.table_depth==0: self.rows=[]
            self.table_depth+=1
        elif self.table_depth and tag=="tr":
            self.row=[]
        elif self.table_depth and tag in ("td","th"):
            self.cell=[]
    def handle_data(self, data):
        if self.cell is not None: self.cell.append(data)
    def handle_endtag(self, tag):
        if tag in ("td","th") and self.cell is not None:
            self.row.append(" ".join("".join(self.cell).split())); self.cell=None
        elif tag=="tr" and self.row is not None:
            if any(self.row): self.rows.append(self.row)
            self.row=None
        elif tag=="table" and self.table_depth:
            self.table_depth-=1
            if self.table_depth==0:
                self.tables.append(self.rows); self.rows=None

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    req=urllib.request.Request(URL,headers={"User-Agent":UA,"Accept":"text/html"})
    with urllib.request.urlopen(req,timeout=25) as response:
        raw=response.read()
        if response.status!=200: raise RuntimeError(f"PIB HTTP {response.status}")
        final_url=response.geturl()
    page=raw.decode("utf-8","replace")
    parser=Tables(); parser.feed(page)
    target=None; header=None
    for table in parser.tables:
        for idx,row in enumerate(table):
            low=[x.lower().replace("\u00a0"," ").strip() for x in row]
            if "industry code" in low and "description" in low and "apr-25" in low and "sep-25" in low and "feb-26" in low:
                target=table; header=low; break
        if target: break
    if target is None:
        raise RuntimeError("Statement IV header not found; source schema changed")
    positions={name:header.index(name) for name in ["industry code","description",*TARGETS.keys()]}
    rows=[]
    for row in target:
        if len(row)<=max(positions.values()): continue
        code=row[positions["industry code"]].strip()
        if code not in EXPECTED_CODES: continue
        for label,period in TARGETS.items():
            raw_value=row[positions[label]].replace(",","").strip()
            if not re.fullmatch(r"\d+(?:\.\d+)?",raw_value):
                raise RuntimeError(f"Invalid numeric value for NIC {code} {period}: {raw_value!r}")
            rows.append({
                "base_year":"2011-12","classification":"NIC-2008","period":period,
                "nic_code":code,"description":row[positions["description"]],
                "index_value":float(raw_value),"source_type":"PIB_LATER_RELEASE_SNAPSHOT",
                "first_release_status":"NOT_ESTABLISHED_FROM_THIS_SNAPSHOT",
                "source_release_id":"PRID=2256241","source_release_date":"2026-04-28",
                "source_statement":"STATEMENT IV: MONTHLY INDEX OF INDUSTRIAL PRODUCTION (2-DIGIT LEVEL)",
                "source_url":URL,"retrieved_final_url":final_url,
                "source_page_sha256":hashlib.sha256(raw).hexdigest()
            })
    got={r["nic_code"] for r in rows}
    if got!=EXPECTED_CODES or len(rows)!=len(EXPECTED_CODES)*len(TARGETS):
        raise RuntimeError(f"Coverage mismatch: NIC codes={sorted(got)}, rows={len(rows)}")
    out=OUT/"pib_later_snapshot_missing_iip_periods.csv"
    with out.open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    report={
        "status":"PASS","source_type":"SUPPLEMENTARY_LATER_RELEASE_SNAPSHOT_NOT_ORIGINAL_CATALOGUE_VINTAGE",
        "source_release_id":"PRID=2256241","source_release_date":"2026-04-28",
        "base_year":"2011-12","classification":"NIC-2008",
        "periods_covered":list(TARGETS.values()),"nic_codes":len(got),"observation_rows":len(rows),
        "source_page_sha256":hashlib.sha256(raw).hexdigest(),
        "file":str(out),"interpretation":"These values are from one later PIB snapshot. They establish published values for the missing periods as of 2026-04-28; they do not recreate missing original MoSPI catalogue releases or prove first-release vintage values.",
        "legacy_series_boundary":"2026-03; 2026-04 onward belongs to the separate 2022-23/NIC-2025 series and must not be spliced into this series."
    }
    (OUT/"pib_later_snapshot_missing_iip_periods.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
