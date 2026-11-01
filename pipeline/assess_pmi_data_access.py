#!/usr/bin/env python3
"""PMI source-access assessment; do not scrape or redistribute licensed survey data."""
from __future__ import annotations
import hashlib,json,ssl,urllib.request,urllib.error
from datetime import datetime,timezone
from html.parser import HTMLParser
from pathlib import Path
PRODUCT="https://www.spglobal.com/market-intelligence/en/solutions/products/pmi"
TERMS="https://www.spglobal.com/en/legal/licensing-tc"
CALENDAR="https://pmi.spglobal.com/Public/Release/ReleaseDates?language=en&os=0"
OUT=Path("artifacts/pmi_access_assessment")
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-PMI-Access-Audit/1.1)"
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,d):
  s=" ".join(d.split())
  if s:self.parts.append(s)
 def text(self):return " ".join(self.parts)
def sha(b):return hashlib.sha256(b).hexdigest()
def get(url,key):
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml"})
 try:
  with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl.create_default_context())).open(req,timeout=25) as r:
   b=r.read(5_000_000);status=r.status;final=r.geturl();ctype=r.headers.get("Content-Type","")
 except urllib.error.HTTPError as e:
  b=e.read(1_000_000);status=e.code;final=e.geturl();ctype=e.headers.get("Content-Type","")
 except Exception as e:
  b=(str(e)).encode();status=0;final=url;ctype="transport-error"
 fn=key+".response";(OUT/fn).write_bytes(b)
 parser=Text();parser.feed(b.decode("utf-8-sig",errors="replace"))
 return {"url":url,"final_url":final,"http_status":status,"content_type":ctype,
  "raw_file":fn,"bytes":len(b),"sha256":sha(b),"text":parser.text()}

def main():
 OUT.mkdir(parents=True,exist_ok=True);retrieved=datetime.now(timezone.utc).isoformat()
 sources={k:get(u,k) for k,u in [("product",PRODUCT),("terms",TERMS),("calendar",CALENDAR)]}
 for v in sources.values():
  if not (v["final_url"].startswith("https://www.spglobal.com/") or v["final_url"].startswith("https://pmi.spglobal.com/")):
   raise RuntimeError("PMI assessment resolved outside official S&P Global domains")
 product=sources["product"]["text"].lower();terms=sources["terms"]["text"].lower();calendar=sources["calendar"]["text"].lower()
 product_live=sources["product"]["http_status"]==200
 terms_live=sources["terms"]["http_status"]==200
 calendar_live=sources["calendar"]["http_status"]==200
 checks={"official_product_endpoint_attempted":sources["product"]["http_status"] in (200,403,429),
  "official_licensing_endpoint_attempted":sources["terms"]["http_status"] in (200,403,429),
  "official_calendar_endpoint_attempted":sources["calendar"]["http_status"] in (200,403,429),
  "product_license_disclosure_or_access_block":(("subscription" in product or "licens" in product) if product_live else sources["product"]["http_status"] in (403,429)),
  "apac_terms_or_access_block":(("apac" in terms and "data terms and conditions" in terms) if terms_live else sources["terms"]["http_status"] in (403,429)),
  "calendar_or_access_block":(("manufacturing pmi" in calendar and "services pmi" in calendar) if calendar_live else sources["calendar"]["http_status"] in (403,429))}
 if not all(checks.values()):raise RuntimeError(f"PMI access assessment incomplete: {checks}")
 report={"status":"ACCESS_ASSESSMENT_PASS","source_group":"macro_indicators",
  "series":"India S&P Global / HSBC PMI survey family",
  "access_classification":"PUBLIC_RELEASE_HEADLINES_AND_CALENDAR; FULL_HISTORICAL_SERIES_LICENSE_OR_SUBSCRIPTION_REQUIRED",
  "underlying_dataset_status":"NOT_CONNECTED","observed_rows":0,"promotable_rows":0,
  "license_status":"NO_LICENSE_OR_DATA_FEED_CREDENTIALS_PROVIDED_TO_THIS_PIPELINE",
  "automated_access_observation":{k:v["http_status"] for k,v in sources.items()},
  "policy":"Do not scrape, store, redistribute or infer licensed survey-level data. Public headline releases may be recorded individually only when an official public release page and exact timestamp are captured.",
  "domain_checks":checks,"sources":{k:{kk:vv for kk,vv in v.items() if kk!="text"} for k,v in sources.items()},
  "limitations":["This is a source access/rights assessment, not PMI data ingestion.",
   "The pipeline has no S&P PMI subscription, license, data feed or API credentials.",
   "HTTP 403/429 from an unauthenticated runner is recorded as an access limitation, not proof that the service is unavailable to licensed users.",
   "A public headline is not a full historical series or underlying survey dataset.",
   "PMI factor coverage remains NOT_CONNECTED / UNKNOWN; no negative signal is inferred.",
   "No Factor Registry promotion or production logic change."]}
 (OUT/"access_assessment.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 (OUT/"manifest.json").write_text(json.dumps({"retrieved_at_utc":retrieved,
  "sources":{k:{kk:vv for kk,vv in v.items() if kk!="text"} for k,v in sources.items()},
  "assessment_status":report["status"]},ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"status":report["status"],"underlying_dataset_status":"NOT_CONNECTED",
  "observed_rows":0,"http_statuses":report["automated_access_observation"],"checks":checks},indent=2))
if __name__=="__main__":main()
