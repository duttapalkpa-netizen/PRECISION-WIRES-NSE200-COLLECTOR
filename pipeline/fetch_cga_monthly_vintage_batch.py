#!/usr/bin/env python3
"""Fetch a bounded CGA FY2025-26 monthly report batch; preserve raw HTML and vintage limits."""
import concurrent.futures, hashlib, json, re, ssl
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

ROOT="https://cga.gov.in"
FY="2025-2026"
MONTHS={"April":4,"May":5,"June":6,"July":7,"August":8,"September":9}
OUT=Path("artifacts/cga_monthly_report_vintage_batch")
UA="Mozilla/5.0 (compatible; PW-CGA-Vintage-Batch/1.0)"

class FrameParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.src=[]
    def handle_starttag(self,tag,attrs):
        if tag.lower()=="iframe":
            value=dict(attrs).get("src")
            if value: self.src.append(value)

def fetch(url):
    req=Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,*/*"})
    with urlopen(req,timeout=25,context=ssl.create_default_context()) as r:
        body=r.read(8_000_000)
        return body,{"http_status":r.status,"final_url":r.geturl(),"content_type":r.headers.get("Content-Type",""),
                     "bytes":len(body),"sha256":hashlib.sha256(body).hexdigest()}

def one(item):
    month,mid=item
    page=ROOT+f"/MonthlyReport/Published/{mid}/{FY}.aspx"
    page_body,page_meta=fetch(page)
    parser=FrameParser(); parser.feed(page_body.decode("utf-8-sig",errors="replace"))
    if len(parser.src)!=1: raise RuntimeError(f"{month}: expected exactly one iframe, got {len(parser.src)}")
    report_url=urljoin(page,parser.src[0])
    parsed=urlparse(report_url)
    if parsed.scheme!="https" or parsed.hostname not in ("cga.gov.in","www.cga.gov.in") or "/writereaddata/MonthAccount/" not in parsed.path:
        raise RuntimeError(f"{month}: iframe URL failed official-host/path allowlist")
    body,meta=fetch(report_url)
    text=body.decode("windows-1252",errors="replace")
    if "GOVERNMENT OF INDIA" not in text.upper() or "UNION GOVERNMENT ACCOUNTS" not in text.upper():
        raise RuntimeError(f"{month}: downloaded content failed CGA report identity check")
    safe=f"{mid:02d}_{month.lower()}.html"
    (OUT/safe).write_bytes(body)
    def meta_date(name):
        m=re.search(rf"<o:{name}>([^<]+)</o:{name}>",text,re.I)
        return m.group(1).strip() if m else None
    return {"financial_year":FY,"report_month":month,"archive_page_url":page,"archive_page_sha256":page_meta["sha256"],
            "report_url":report_url,"report_sha256":meta["sha256"],"report_bytes":meta["bytes"],
            "http_status":meta["http_status"],"content_type":meta["content_type"],
            "document_created":meta_date("Created"),"document_last_printed":meta_date("LastPrinted"),
            "release_timestamp":None,"release_timestamp_status":"UNKNOWN_NOT_SUPPLIED_AS_PUBLICATION_TIMESTAMP",
            "document_metadata_status":"INTERNAL_DOCUMENT_METADATA_ONLY_NOT_RELEASE_TIMESTAMP",
            "snapshot_file":safe}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        rows=list(pool.map(one,MONTHS.items()))
    rows.sort(key=lambda x:list(MONTHS).index(x["report_month"]))
    result={"status":"PASS_BOUNDED_CGA_RAW_SNAPSHOT_BATCH_WITH_VINTAGE_LIMITS",
            "publisher":"Controller General of Accounts, Ministry of Finance, Government of India",
            "financial_year":FY,"months_requested":list(MONTHS),"months_fetched":len(rows),
            "records":rows,"created_at_utc":datetime.now(timezone.utc).isoformat(),
            "limitations":["The report month is not its publication date.",
             "Document Created/LastPrinted metadata are not treated as official release timestamps.",
             "No archived historical vintage is certified from a single current retrieval.",
             "No data is promoted to Factor Registry by this batch."]}
    (OUT/"vintage_batch_manifest.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+")
    print(json.dumps({"status":result["status"],"months_fetched":len(rows),
                      "release_timestamp_statuses":sorted({x["release_timestamp_status"] for x in rows})},indent=2))
if __name__=="__main__": main()
