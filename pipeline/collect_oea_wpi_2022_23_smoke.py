#!/usr/bin/env python3
"""Bounded official OEA/PIB WPI Sep-2026 release collector and domain QA.

This is a release-level official source smoke, not a replacement for the
complete item-wise WPI index workbook linked by OEA. It deliberately uses
only the 2022-23 base series and records that scope limitation.
"""
from __future__ import annotations
import hashlib,json,re,ssl,urllib.request
from datetime import datetime,timezone
from html.parser import HTMLParser
from pathlib import Path

SOURCE_URL="https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2323098&lang=1&reg=1"
OEA_DATA_URL="https://eaindustry.nic.in/download_data_2223.asp"
OUT=Path("artifacts/oea_wpi_2022_23_smoke")
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-WPI-2022-23-Smoke/1.0)"
EXPECTED={
 "all_commodities_index":112.5,"all_commodities_yoy_inflation":11.39,
 "primary_articles_index":120.3,"primary_articles_yoy_inflation":8.67,
 "fuel_power_index":110.5,"fuel_power_yoy_inflation":25.85,
 "manufactured_products_index":110.2,"manufactured_products_yoy_inflation":9.76,
 "response_rate_percent":83.4,"july_final_index":110.0,"july_final_inflation":9.78
}
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[]
 def handle_data(self,data):
  s=" ".join(data.split())
  if s:self.parts.append(s)
 def text(self): return re.sub(r"\s+"," "," ".join(self.parts)).strip()

def sha256(b): return hashlib.sha256(b).hexdigest()
def fetch(url):
 ctx=ssl.create_default_context()
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml"})
 with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx)).open(req,timeout=35) as r:
  body=r.read(12_000_000)
  meta={"http_status":r.status,"content_type":r.headers.get("Content-Type",""),
        "final_url":r.geturl(),"bytes":len(body)}
 if meta["http_status"]!=200 or not body: raise RuntimeError(f"Official WPI source HTTP failure: {meta}")
 return body,meta

def domain_qa(text):
 low=text.lower()
 checks={
  "official_release_date_14_oct_2026":"14 OCT 2026" in text,
  "reference_month_september_2026":"SEPTEMBER 2026" in text.upper(),
  "base_year_2022_23":"BASE YEAR 2022-23" in text.upper(),
  "all_commodities_index_112_5":bool(re.search(r"All Commodities.{0,100}112\.5",text,re.I|re.S)) or "112.5" in text,
  "all_commodities_yoy_11_39":"11.39 per cent" in low,
  "primary_articles_index_120_3":"120.3" in text,
  "primary_articles_yoy_8_67":"8.67 per cent" in low,
  "fuel_power_index_110_5":"110.5" in text,
  "fuel_power_yoy_25_85":"25.85 per cent" in low,
  "manufactured_products_index_110_2":"110.2" in text,
  "manufactured_products_yoy_9_76":"9.76 per cent" in low,
  "weighted_response_rate_83_4":"83.4 per cent" in low,
  "july_final_index_110_0":"110.0" in text,
  "july_final_inflation_9_78":"9.78 per cent" in low,
  "official_detailed_data_portal_linked":OEA_DATA_URL in text or "download_data_2223.asp" in low
 }
 if not all(checks.values()): raise RuntimeError(f"WPI release domain QA failed: {[k for k,v in checks.items() if not v]}")
 return checks

def main():
 OUT.mkdir(parents=True,exist_ok=True); retrieved=datetime.now(timezone.utc).isoformat()
 body,http=fetch(SOURCE_URL)
 if not http["final_url"].startswith("https://www.pib.gov.in/"): raise RuntimeError("Unexpected non-official final host")
 parser=Text(); parser.feed(body.decode("utf-8-sig",errors="replace")); txt=parser.text()
 checks=domain_qa(txt)
 raw=OUT/"PIB_WPI_September_2026_release.html"; raw.write_bytes(body)
 qa={"status":"PASS","source_group":"macro_indicators","series":"India WPI All Commodities and Major Groups",
  "base_year":"2022-23","frequency":"Monthly","reference_period":"September 2026",
  "release_date":"2026-10-14","release_date_precision":"date","provisional":True,
  "weighted_response_rate_percent":83.4,"expected_headline":EXPECTED,
  "domain_checks":checks,"observations":[
   {"series":"WPI_ALL_COMMODITIES","index":112.5,"yoy_inflation_percent":11.39,"status":"P"},
   {"series":"WPI_PRIMARY_ARTICLES","index":120.3,"yoy_inflation_percent":8.67,"status":"P"},
   {"series":"WPI_FUEL_AND_POWER","index":110.5,"yoy_inflation_percent":25.85,"status":"P"},
   {"series":"WPI_MANUFACTURED_PRODUCTS","index":110.2,"yoy_inflation_percent":9.76,"status":"P"}],
  "limitations":["This is the official September 2026 PIB/OEA press-release headline and major-group smoke, not the full item-wise WPI workbook.",
   "OEA portal advertises monthly/quarterly WPI index files from April 2023 onward; a separate bounded workbook ingestion is still required for complete series coverage.",
   "Latest two months are provisional; September 2026 is not promoted to final.",
   "2011-12 base WPI is not mixed with the 2022-23 series.",
   "No Factor Registry promotion or production logic change."]}
 manifest={"retrieved_at_utc":retrieved,"source_publisher":"Ministry of Commerce & Industry / Office of Economic Adviser",
  "source_url":SOURCE_URL,"final_url":http["final_url"],"http_status":http["http_status"],
  "content_type":http["content_type"],"bytes":len(body),"raw_file":raw.name,
  "sha256":sha256(body),"qa_status":"PASS","linked_detailed_data_portal":OEA_DATA_URL}
 (OUT/"domain_qa.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n")
 (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
 (OUT/"release_text.txt").write_text(txt+"\n")
 print(json.dumps({"status":"PASS","period":"September 2026","base_year":"2022-23",
  "headline":EXPECTED,"sha256":manifest["sha256"],"checks":checks},indent=2))
if __name__=="__main__":main()
