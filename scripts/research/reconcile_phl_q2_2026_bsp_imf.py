#!/usr/bin/env python3
"""Philippines Q2-2026 BSP vs archived IMF portfolio asset/liability check."""
from __future__ import annotations
from datetime import datetime, timezone
from decimal import Decimal
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import csv, hashlib, json, re, sys

URL="https://www.bsp.gov.ph/Statistics/External/table1_data.aspx"
RELEASE_URL="https://www.bsp.gov.ph/Media_And_Research/Media%20Releases/2026_09/news-09112026a1.aspx"
PANEL=Path("docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv")
OUT=Path("artifacts/gcr_phl_q2_2026_bsp_imf")
PERIOD="2026-Q2"
TOL=Decimal("0.5")  # BSP publishes table values rounded to whole USD million

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.rows=[]; self.tr=False; self.cell=False; self.buf=[]; self.row=[]
    def handle_starttag(self,t,a):
        t=t.lower()
        if t=="tr": self.tr=True; self.row=[]
        elif self.tr and t in ("td","th"): self.cell=True; self.buf=[]
    def handle_data(self,d):
        if self.cell: self.buf.append(d)
    def handle_endtag(self,t):
        t=t.lower()
        if t in ("td","th") and self.cell:
            self.row.append(" ".join("".join(self.buf).split())); self.cell=False
        elif t=="tr" and self.tr:
            if self.row: self.rows.append(self.row)
            self.tr=False

def sha(b): return hashlib.sha256(b).hexdigest()
def get(url):
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES research validation/1.0","Accept":"text/html,*/*"})
    with urlopen(req,timeout=25) as r: return r.status,r.geturl(),dict(r.headers.items()),r.read()
def number(s):
    s=s.strip().replace(",","").replace("−","-")
    if not re.fullmatch(r"-?\d+(?:\.\d+)?",s): raise ValueError("not a numeric cell: "+repr(s))
    return Decimal(s)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    retrieved=datetime.now(timezone.utc).isoformat()
    status,final,headers,raw=get(URL)
    if status!=200: raise SystemExit("BSP table HTTP "+str(status))
    (OUT/"bsp_table1_raw.html").write_bytes(raw)
    page=raw.decode("utf-8",errors="replace")
    checks={"bop_phrase":"Balance of Payments" in page,"philippines_phrase":"Philippines" in page,"q2_phrase":"Q2" in page,"asset_phrase":"Net Acquisition" in page,"portfolio_phrase":"Portfolio" in page,"html_title":re.findall(r"<title[^>]*>(.*?)</title>",page,re.I|re.S)[:1],"first_1200_chars":page[:1200]}
    if not checks["bop_phrase"] or not checks["q2_phrase"] or not checks["portfolio_phrase"]:
        (OUT/"bsp_table_fetch_diagnostic.json").write_text(json.dumps({"url":URL,"http_status":status,"final_url":final,"headers":headers,"byte_count":len(raw),"sha256":sha(raw),"checks":checks},indent=2,ensure_ascii=False)+"\\n",encoding="utf-8")
        print(json.dumps(checks,indent=2,ensure_ascii=False))
        raise SystemExit("BSP table source identity check failed; diagnostic captured")
    parser=Parser(); parser.feed(page)
    targets={"Portfolio Investment":"net","Net Acquisition of Financial Assets":"asset","Net Incurrence of Liabilities":"liability"}
    vals={}
    for row in parser.rows:
        if row and row[0].strip() in targets:
            label=row[0].strip()
            if label in vals: raise SystemExit("duplicate BSP row: "+label)
            if len(row)<=11: raise SystemExit("unexpected BSP table columns for "+label+": "+repr(row))
            vals[targets[label]]=number(row[11])
    if set(vals)!={"net","asset","liability"}: raise SystemExit("missing exact BSP portfolio rows: "+repr(vals))
    # BSP technical note says financial account = net acquisition of financial assets less net incurrence of liabilities.
    identity=vals["asset"]-vals["liability"]
    release_status,release_final,release_headers,release_raw=get(RELEASE_URL)
    release_page=release_raw.decode("utf-8",errors="replace")
    if release_status!=200 or "Portfolio Investment" not in release_page or "Net Acquisition of Financial Assets" not in release_page:
        raise SystemExit("BSP Q2 release page could not be verified")
    # Extract Q2 2026 values from the dated release's three consecutive portfolio rows.
    rp=Parser(); rp.feed(release_page)
    release_vals={}
    for row in rp.rows:
        if row and row[0].strip() in ("Portfolio Investment","Net Acquisition of Financial Assets","Net Incurrence of Liabilities"):
            label=row[0].strip()
            if len(row)>2: release_vals[label]=row[2]
    if len(release_vals)!=3: raise SystemExit("BSP release portfolio row extraction incomplete: "+repr(release_vals))
    imf={}
    with PANEL.open(encoding="utf-8-sig",newline="") as f:
        for row in csv.DictReader(f):
            if row.get("COUNTRY")=="PHL" and row.get("INDICATOR")=="P_F" and row.get("UNIT")=="USD" and row.get("FREQUENCY")=="Q" and row.get("TIME_PERIOD")==PERIOD and row.get("BOP_ACCOUNTING_ENTRY") in ("A_NFA_T","L_NIL_T"):
                k=row["BOP_ACCOUNTING_ENTRY"]
                if k in imf: raise SystemExit("duplicate IMF key "+k)
                imf[k]=row
    results=[]
    for entry,bspkey in (("A_NFA_T","asset"),("L_NIL_T","liability")):
        row=imf.get(entry)
        if row is None: raise SystemExit("missing PHL IMF row "+entry)
        rawv=Decimal(row["OBS_VALUE"])
        derived=rawv/Decimal(1_000_000)
        diff=derived-vals[bspkey]
        ok=row.get("UNIT")=="USD" and row.get("SCALE")=="6" and abs(diff)<=TOL
        results.append({"country":"PHL","quarter":PERIOD,"entry":entry,"imf_raw_obs_value_usd":str(rawv),"unit":row.get("UNIT"),"scale":row.get("SCALE"),"precision":row.get("PRECISION"),"derivation_type":row.get("DERIVATION_TYPE"),"imf_derived_usd_million":str(derived),"bsp_usd_million":str(vals[bspkey]),"difference_imf_minus_bsp_usd_million":str(diff),"rounding_tolerance_usd_million":str(TOL),"status":"PASS" if ok else "REVIEW"})
    with (OUT/"phl_q2_2026_bsp_imf_reconciliation.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
    safe={k:v for k,v in headers.items() if k.lower() not in ("set-cookie","authorization")}
    summary={"task":"PHL Q2-2026 BSP official BOP vs archived IMF portfolio dual-leg","bsp_table_url":URL,"bsp_table_final_url":final,"bsp_table_http_status":status,"bsp_table_retrieved_at_utc":retrieved,"bsp_table_byte_count":len(raw),"bsp_table_sha256":sha(raw),"bsp_table_headers":safe,"bsp_release_url":RELEASE_URL,"bsp_release_http_status":release_status,"bsp_release_final_url":release_final,"bsp_release_rows":release_vals,"bsp_current_table_q2_2026_preliminary":bool(re.search(r"2026.{0,20}p",page,re.I)),"bsp_q2_values_usd_million":{k:str(v) for k,v in vals.items()},"bsp_asset_minus_liability_identity_usd_million":str(identity),"bsp_identity_difference_vs_reported_net":str(identity-vals["net"]),"imf_panel_file":str(PANEL),"imf_panel_sha256":sha(PANEL.read_bytes()),"imf_panel_archive_retrieved_2026_11_19":True,"imf_rows":results,"numeric_leg_pass_count":sum(x["status"]=="PASS" for x in results),"numeric_leg_review_count":sum(x["status"]!="PASS" for x in results),"same_vintage_status":"NOT_ESTABLISHED","same_vintage_reason":"BSP Q2 2026 release is dated 11-Sep-2026 and current table labels 2026 preliminary; archived IMF panel retrieval is 19-Nov-2026 but no observation-specific IMF source submission/revision timestamp is exposed. Retrieval time is not source vintage.","decision":"NUMERIC_2_OF_2_PASS_VINTAGE_NOT_ESTABLISHED" if all(x["status"]=="PASS" for x in results) else "PHL_PARTIAL_REVIEW"}
    (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (OUT/"bsp_table1_raw.html").write_bytes(raw)
    (OUT/"bsp_q2_release_raw.html").write_bytes(release_raw)
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if summary["numeric_leg_review_count"]==0 else 1
if __name__=="__main__": sys.exit(main())
