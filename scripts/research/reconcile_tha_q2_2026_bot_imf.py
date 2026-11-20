#!/usr/bin/env python3
"""Thailand Q2-2026 BOT portfolio-flow comparison using the archived IMF panel."""
from __future__ import annotations
from datetime import datetime, timezone
from decimal import Decimal
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import csv, hashlib, json, re, sys

URL = "https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?language=ENG&reportID=1022"
PANEL = Path("docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv")
OUT = Path("artifacts/gcr_tha_q2_2026_bot_imf")
PERIOD = "2026-Q2"
TOLERANCE = Decimal("0.005")  # BOT table is displayed to two decimal USD millions

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows=[]; self.in_tr=False; self.in_cell=False; self.cell_parts=[]; self.cells=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower()=="tr":
            self.in_tr=True; self.cells=[]
        elif self.in_tr and tag.lower() in ("td","th"):
            self.in_cell=True; self.cell_parts=[]
    def handle_endtag(self, tag):
        if tag.lower() in ("td","th") and self.in_cell:
            self.cells.append(" ".join("".join(self.cell_parts).split()))
            self.in_cell=False
        elif tag.lower()=="tr" and self.in_tr:
            if self.cells: self.rows.append(self.cells)
            self.in_tr=False
    def handle_data(self, data):
        if self.in_cell: self.cell_parts.append(data)

def sha(b): return hashlib.sha256(b).hexdigest()
def dec(s):
    s=s.strip().replace(",","").replace("−","-")
    if s in ("", "-", "—", "n.a."): raise ValueError(f"not a numeric cell: {s!r}")
    return Decimal(s)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    retrieved=datetime.now(timezone.utc).isoformat()
    req=Request(URL,headers={"User-Agent":"PRECISION-WIRES research validation/1.0","Accept":"text/html,*/*"})
    try:
        with urlopen(req,timeout=25) as resp:
            body=resp.read(); status=resp.status; headers=dict(resp.headers.items()); final=resp.geturl()
    except (HTTPError,URLError,TimeoutError) as e:
        raise SystemExit(f"BOT official source fetch failed: {type(e).__name__}: {e}")
    (OUT/"bot_report_1022_raw.html").write_bytes(body)
    safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
    page=body.decode("utf-8",errors="replace")
    if status!=200: raise SystemExit(f"BOT HTTP {status}")
    if "Last Updated" not in page or "Q2/2026" not in page: raise SystemExit("BOT page metadata/header changed")
    parser=TableParser(); parser.feed(page)
    rows=parser.rows
    parent=next((i for i,r in enumerate(rows) if len(r)>1 and "2. Portfolio investment" in r[1]),None)
    if parent is None: raise SystemExit("Portfolio investment parent row not found")
    found={}
    for row in rows[parent+1:]:
        if len(row)>2 and row[1].strip()=="(1) Assets" and "A_NFA_T" not in found:
            found["A_NFA_T"]=dec(row[2])
        elif len(row)>2 and row[1].strip()=="(2) Liabilities" and "L_NIL_T" not in found:
            found["L_NIL_T"]=dec(row[2])
        if len(found)==2: break
    if set(found)!={"A_NFA_T","L_NIL_T"}: raise SystemExit(f"Portfolio child rows incomplete: {found}")
    update=re.search(r"Last Updated\s*:\s*([^<\r\n]+)",page,re.I)
    updated=update.group(1).strip() if update else None
    if not updated or "30 Sep 2026 14:33" not in updated:
        raise SystemExit(f"BOT revision/update metadata changed or missing: {updated!r}")
    if not re.search(r"positive figure indicates an increase in net financial assets or liabilities",page,re.I):
        raise SystemExit("BOT financial-account sign note missing")
    imf={}
    with PANEL.open(encoding="utf-8-sig",newline="") as f:
        for row in csv.DictReader(f):
            if row.get("COUNTRY")=="THA" and row.get("INDICATOR")=="P_F" and row.get("UNIT")=="USD" and row.get("FREQUENCY")=="Q" and row.get("TIME_PERIOD")==PERIOD and row.get("BOP_ACCOUNTING_ENTRY") in found:
                key=row["BOP_ACCOUNTING_ENTRY"]
                if key in imf: raise SystemExit(f"Duplicate IMF key: {key}")
                imf[key]=row
    results=[]
    for entry in ("A_NFA_T","L_NIL_T"):
        row=imf.get(entry)
        if row is None: raise SystemExit(f"Archived IMF panel missing THA {entry} {PERIOD}")
        raw=Decimal(row["OBS_VALUE"])
        derived=raw/Decimal(1_000_000)
        national=found[entry]
        diff=derived-national
        checks={
            "raw_obs_value_unchanged":str(raw),
            "unit":row.get("UNIT"),"scale":row.get("SCALE"),"precision":row.get("PRECISION"),
            "derivation_type":row.get("DERIVATION_TYPE"),
            "imf_derived_usd_million_obs_value_div_1e6":str(derived),
            "bot_usd_million":str(national),
            "difference_imf_minus_bot_usd_million":str(diff),
            "tolerance_usd_million":str(TOLERANCE),
            "status":"PASS" if row.get("UNIT")=="USD" and row.get("SCALE")=="6" and abs(diff)<=TOLERANCE else "REVIEW"
        }
        results.append({"country":"THA","quarter":PERIOD,"entry":entry,**checks})
    fields=list(results[0].keys())
    with (OUT/"tha_q2_2026_bot_imf_reconciliation.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(results)
    receipt={"url":URL,"final_url":final,"retrieved_at_utc":retrieved,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":sha(body),"raw_file":"bot_report_1022_raw.html"}
    summary={
        "task":"THA Q2-2026 BOT official USD portfolio asset/liability vs existing archived IMF panel",
        "source_owner":"Bank of Thailand","table_id":"EC_XT_049_S2","unit":"Millions of USD",
        "frequency":"Quarterly","source_last_updated":updated,"period_header":"Q2/2026 p",
        "bot_sign_note":"Positive figure indicates an increase in net financial assets or liabilities; negative indicates a decrease. Net financial account is assets minus liabilities.",
        "bot_raw_rows":{"A_NFA_T":str(found["A_NFA_T"]),"L_NIL_T":str(found["L_NIL_T"])},
        "bot_receipt":receipt,
        "imf_panel_file":str(PANEL),"imf_panel_sha256":sha(PANEL.read_bytes()),
        "imf_panel_artifact_source":"run 44474218174 / artifact 14505862034 / ZIP SHA-256 1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f",
        "imf_exact_rows":results,
        "numeric_leg_pass_count":sum(x["status"]=="PASS" for x in results),
        "numeric_leg_review_count":sum(x["status"]!="PASS" for x in results),
        "same_vintage_status":"NOT_ESTABLISHED",
        "same_vintage_reason":"BOT page exposes last-updated timestamp 30 Sep 2026 14:33 and Q2 provisional status; archived IMF panel was retrieved 19-Nov-2026 but no observation-level IMF source submission/revision timestamp is exposed in the public BOP dataset page.",
        "decision":"NUMERIC_2_OF_2_PASS_VINTAGE_NOT_ESTABLISHED" if all(x["status"]=="PASS" for x in results) else "THA_PARTIAL_REVIEW"
    }
    (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if summary["numeric_leg_review_count"]==0 else 1

if __name__=="__main__":
    sys.exit(main())
