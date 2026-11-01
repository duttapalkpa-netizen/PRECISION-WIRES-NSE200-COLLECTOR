#!/usr/bin/env python3
"""PMI source-access assessment; never scrape or redistribute licensed survey microdata."""
from __future__ import annotations
import hashlib,json,ssl,urllib.request
from datetime import datetime,timezone
from html.parser import HTMLParser
from pathlib import Path
PRODUCT="https://www.spglobal.com/market-intelligence/en/solutions/products/pmi"
TERMS="https://www.spglobal.com/en/legal/licensing-tc"
CALENDAR="https://pmi.spglobal.com/Public/Release/ReleaseDates?language=en&os=0"
OUT=Path("artifacts/pmi_access_assessment")
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-PMI-Access-Audit/1.0)"
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,d):
  s=" ".join(d.split())
  if s:self.parts.append(s)
 def text(self):return " ".join(self.parts)
def get(url):
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml"})
 with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl.create_default_context())).open(req,timeout=35) as r:
  b=r.read(8_000_000);meta={"status":r.status,"final_url":r.geturl(),"content_type":r.headers.get("Content-Type","")}
 if meta["status"]!=200 or not b:raise RuntimeError(f"PMI access source fetch failed: {url} {meta}")
 p=Text();p.feed(b.decode("utf-8-sig",errors="replace"));return b,p.text(),meta
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
 OUT.mkdir(parents=True,exist_ok=True);retrieved=datetime.now(timezone.utc).isoformat()
 sources={}
 for key,url in [("product",PRODUCT),("terms",TERMS),("calendar",CALENDAR)]:
  raw,text,meta=get(url)
  if not meta["final_url"].startswith("https://www.spglobal.com/") and not meta["final_url"].startswith("https://pmi.spglobal.com/"):
   raise RuntimeError(f"Unexpected PMI source host: {meta['final_url']}")
  fn=key+".html";(OUT/fn).write_bytes(raw)
  sources[key]={"url":url,"final_url":meta["final_url"],"http_status":meta["status"],
   "content_type":meta["content_type"],"raw_file":fn,"bytes":len(raw),"sha256":sha(raw),"text":text}
 p=sources["product"]["text"].lower();t=sources["terms"]["text"].lower();c=sources["calendar"]["text"].lower()
 checks={
  "S&P_Global_product_page_live":sources["product"]["http_status"]==200,
  "product_describes_subscription_or_licensing":("subscription" in p or "licens" in p),
  "APAC_data_terms_listed":("apac" in t and "data terms and conditions" in t),
  "official_PMI_calendar_live":sources["calendar"]["http_status"]==200,
  "manufacturing_release_schedule_published":("manufacturing pmi" in c and "first working day" in c),
  "services_release_schedule_published":("services pmi" in c and "third working day" in c)}
 if not all(checks.values()):raise RuntimeError(f"PMI access assessment checks failed: {[k for k,v in checks.items() if not v]}")
 report={"status":"ACCESS_ASSESSMENT_PASS","source_group":"macro_indicators",
  "series":"India S&P Global / HSBC PMI survey family",
  "access_classification":"PUBLIC_RELEASE_HEADLINES_AND_CALENDAR; FULL_HISTORICAL_SERIES_LICENSE_OR_SUBSCRIPTION_REQUIRED",
  "underlying_dataset_status":"NOT_CONNECTED","observed_rows":0,"promotable_rows":0,
  "license_status":"NO_LICENSE_OR_DATA_FEED_CREDENTIALS_PROVIDED_TO_THIS_PIPELINE",
  "policy":"Do not scrape, store, redistribute or infer licensed survey-level data. Public release headlines may be recorded individually with release URL, exact publication timestamp, survey month, preliminary/final status and revision history when official public source is captured.",
  "domain_checks":checks,"sources":{k:{kk:vv for kk,vv in v.items() if kk!="text"} for k,v in sources.items()},
  "limitations":["This is an access-rights and endpoint assessment, not a PMI data ingestion.",
   "A public headline release is not a full monthly history or underlying survey dataset.",
   "No S&P PMI license, subscription entitlement, data feed or API credentials were supplied.",
   "PMI factor coverage remains NOT_CONNECTED / UNKNOWN; no negative signal is inferred.",
   "No production logic or Factor Registry status is changed."]}
 (OUT/"access_assessment.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 (OUT/"manifest.json").write_text(json.dumps({"retrieved_at_utc":retrieved,"sources":{k:{kk:vv for kk,vv in v.items() if kk!="text"} for k,v in sources.items()},"assessment_status":report["status"]},ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"status":report["status"],"underlying_dataset_status":report["underlying_dataset_status"],
  "observed_rows":report["observed_rows"],"checks":checks},indent=2))
if __name__=="__main__":main()
