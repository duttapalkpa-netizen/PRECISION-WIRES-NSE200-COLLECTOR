#!/usr/bin/env python3
"""Bounded CGA FY2026-27 September capital-expenditure live collection."""
from __future__ import annotations
import hashlib,json,ssl,urllib.request,re
from datetime import datetime,timezone
from html.parser import HTMLParser
from pathlib import Path
CGA_URL="https://cga.nic.in/writereaddata/MonthAccount/92026/DATA2627.htm"
PIB_URL="https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2330455&lang=1&reg=3"
OUT=Path("artifacts/cga_capex_fy2026_27_smoke")
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-CGA-Capex-Smoke/1.2)"
EXPECTED={"budget_estimate_crore":1221821,"actual_ytd_crore":654547,"be_utilization_percent":53.6,"coppy_percent":51.8}
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[]
 def handle_data(self,d):
  s=" ".join(d.split())
  if s:self.parts.append(s)
 def text(self): return re.sub(r"\s+"," "," ".join(self.parts)).strip()
def sha(b): return hashlib.sha256(b).hexdigest()
def get(url):
 ctx=ssl.create_default_context()
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml"})
 with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx)).open(req,timeout=35) as r:
  b=r.read(10_000_000); m={"http_status":r.status,"content_type":r.headers.get("Content-Type",""),"final_url":r.geturl(),"bytes":len(b)}
 if m["http_status"]!=200 or not b: raise RuntimeError(f"Official source HTTP failure: {m}")
 p=Text(); p.feed(b.decode("utf-8-sig",errors="replace"))
 return b,p.text(),m
def capex_row_values(text):
 i=text.lower().find("capital expenditure")
 if i<0:return []
 segment=text[i:i+300]
 tokens=re.findall(r"(?<!\d)\d[\d,]*(?:\.\d+)?%?",segment)
 return tokens[:4]
def capex_row_matches(text):
 return capex_row_values(text)==["1221821","654547","53.6%","51.8%"]
def main():
 OUT.mkdir(parents=True,exist_ok=True); retrieved=datetime.now(timezone.utc).isoformat()
 cga_raw,cga_text,cga_meta=get(CGA_URL); pib_raw,pib_text,pib_meta=get(PIB_URL)
 if not cga_meta["final_url"].startswith("https://cga.nic.in/") or not pib_meta["final_url"].startswith("https://www.pib.gov.in/"):
  raise RuntimeError("CGA/PIB final host mismatch")
 norm=re.sub(r"\s+"," ",cga_text)
 checks={"CGA_official_host":True,"PIB_official_host":True,
  "CGA_report_as_at_end_September_2026":"AS AT THE END OF SEPTEMBER 2026" in norm.upper(),
  "FY_2026_27_present":"2026-2027" in norm,
  "capex_BE_actual_percent_row_matches":capex_row_matches(norm),
  "PIB_release_30_Oct_2026":"30 OCT 2026 5:02PM" in pib_text.upper(),
  "PIB_capital_account_actual_654547":"6,54,547 crore" in pib_text,
  "PIB_capital_account_share_47_7":"47.7%" in pib_text,
  "CGA_provisional_unaudited_notice":"unaudited provisional figures" in norm.lower()}
 if not all(checks.values()):
  i=norm.lower().find("capital expenditure")
  raise RuntimeError(f"CGA capex domain QA failed: {[k for k,v in checks.items() if not v]}; row={norm[i:i+300]}")
 (OUT/"CGA_Monthly_Accounts_September_2026.html").write_bytes(cga_raw)
 (OUT/"PIB_Monthly_Accounts_Review_September_2026.html").write_bytes(pib_raw)
 (OUT/"CGA_text.txt").write_text(cga_text+"\n"); (OUT/"PIB_text.txt").write_text(pib_text+"\n")
 qa={"status":"PASS","source_group":"macro_indicators","series":"Union Government Capital Expenditure",
  "financial_year":"2026-27","reference_period":"April-September 2026 cumulative YTD","period_end":"2026-09-30",
  "release_date":"2026-10-30","release_time":"17:02 IST","release_timestamp_basis":"PIB publication timestamp",
  "unit":"INR_CRORE","provisional_unaudited":True,"expected":EXPECTED,
  "observed":{"budget_estimate_crore":1221821,"actual_ytd_crore":654547,"be_utilization_percent":round(654547/1221821*100,1),"coppy_percent":51.8},
  "arithmetic_check":{"computed_percent":round(654547/1221821*100,1),"published_percent":53.6,
   "within_0_05_percentage_point":abs(654547/1221821*100-53.6)<0.05},
  "domain_checks":checks,"limitations":["YTD cumulative capex, not September standalone monthly flow.",
   "CGA states actuals are unaudited provisional figures and may be revised.",
   "Bounded smoke captures official CGA HTML and PIB release; CGA dashboard Excel ingestion remains separate.",
   "No Factor Registry promotion or production logic change."]}
 manifest={"retrieved_at_utc":retrieved,"publisher":"Controller General of Accounts, Ministry of Finance",
  "cga_source_url":CGA_URL,"cga_final_url":cga_meta["final_url"],"cga_http_status":cga_meta["http_status"],
  "cga_bytes":len(cga_raw),"cga_sha256":sha(cga_raw),"pib_source_url":PIB_URL,
  "pib_final_url":pib_meta["final_url"],"pib_http_status":pib_meta["http_status"],
  "pib_bytes":len(pib_raw),"pib_sha256":sha(pib_raw),"qa_status":"PASS"}
 (OUT/"domain_qa.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n")
 (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"status":"PASS","observed":qa["observed"],"arithmetic":qa["arithmetic_check"],"checks":checks},indent=2))
if __name__=="__main__": main()
