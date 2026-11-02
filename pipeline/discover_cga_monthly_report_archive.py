#!/usr/bin/env python3
"""Inventory CGA monthly-report archive routes and downloadable assets; evidence discovery only."""
import concurrent.futures, csv, hashlib, json, re, ssl, time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

ROOT="https://cga.gov.in"
OVERVIEW=ROOT+"/MonthlyReport/Published/8/{fy}.aspx"
OUT=Path("artifacts/cga_monthly_report_archive_discovery")
YEARS=[f"{y}-{y+1}" for y in range(2014,2026)]
MONTH_IDS=range(1,13)
ASSET_EXT=(".pdf",".xls",".xlsx",".xlsm",".csv",".zip")
UA="Mozilla/5.0 (compatible; PW-CGA-Archive-Discovery/1.0)"

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.items=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        for key in ("href","src","action","data"):
            value=a.get(key)
            if value: self.items.append({"tag":tag,"attribute":key,"value":value,"label":""})
    def handle_data(self, data):
        if self.items and data.strip():
            self.items[-1]["label"]=(self.items[-1]["label"]+" "+ " ".join(data.split())).strip()

def fetch(url):
    req=Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,*/*"})
    with urlopen(req,timeout=22,context=ssl.create_default_context()) as r:
        body=r.read(4_000_000)
        return body,{"http_status":r.status,"final_url":r.geturl(),"content_type":r.headers.get("Content-Type",""),"bytes":len(body),"sha256":hashlib.sha256(body).hexdigest()}

def parse(url, body, page_type):
    p=Links(); p.feed(body.decode("utf-8-sig",errors="replace"))
    found=[]
    for item in p.items:
        absolute=urljoin(url,item["value"])
        u=urlparse(absolute)
        if u.scheme not in ("http","https") or u.hostname not in ("cga.gov.in","www.cga.gov.in"): continue
        path=u.path.lower()
        candidate=path.endswith(ASSET_EXT) or any(x in path for x in ("/download","/writereaddata/","/monthlyreport/"))
        if candidate:
            found.append({"discovered_on":url,"page_type":page_type,"tag":item["tag"],"attribute":item["attribute"],
                          "label":item["label"],"url":absolute,"asset_candidate":path.endswith(ASSET_EXT)})
    return found

def main():
    OUT.mkdir(parents=True,exist_ok=True); started=datetime.now(timezone.utc).isoformat()
    pages=[]; routes=[]; errors=[]
    overview_jobs=[(fy,OVERVIEW.format(fy=fy)) for fy in YEARS]
    for fy,url in overview_jobs:
        try:
            body,meta=fetch(url); pages.append({"fy":fy,"kind":"year_overview","url":url,**meta})
            routes.extend(parse(url,body,"year_overview"))
        except Exception as e: errors.append({"url":url,"error":type(e).__name__+": "+str(e)})
    month_jobs=[]
    for fy in YEARS:
        for mid in MONTH_IDS:
            month_jobs.append((fy,mid,ROOT+f"/MonthlyReport/Published/{mid}/{fy}.aspx"))
    def one(job):
        fy,mid,url=job
        try:
            body,meta=fetch(url)
            return {"page":{"fy":fy,"month_id":mid,"kind":"month_page","url":url,**meta},
                    "routes":parse(url,body,"month_page"),"error":None}
        except Exception as e:
            return {"page":{"fy":fy,"month_id":mid,"kind":"month_page","url":url,"status":"FETCH_ERROR"},
                    "routes":[],"error":{"url":url,"error":type(e).__name__+": "+str(e)}}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(one,month_jobs):
            pages.append(result["page"]); routes.extend(result["routes"])
            if result["error"]: errors.append(result["error"])
    unique={}
    for row in routes:
        unique[(row["url"],row["discovered_on"])]=row
    routes=list(unique.values())
    # Candidate URLs are not fetched or promoted; this is a route inventory only.
    assets=[x for x in routes if x["asset_candidate"]]
    result={"status":"PASS_ROUTE_INVENTORY_WITH_LIMITATIONS" if pages else "BLOCKED_NO_PAGES",
      "publisher":"Controller General of Accounts, Ministry of Finance, Government of India",
      "started_at_utc":started,"completed_at_utc":datetime.now(timezone.utc).isoformat(),
      "scope":{"financial_years":YEARS,"overview_pages":len(overview_jobs),"month_pages_requested":len(month_jobs),
               "pages_fetched":sum(1 for p in pages if "sha256" in p),"page_fetch_errors":len(errors)},
      "counts":{"routes":len(routes),"download_asset_candidates":len(assets)},
      "routes":routes,"errors":errors,
      "limitations":["A route or link is not proof of an archived publication vintage.",
       "Candidate assets are not downloaded, content-validated, or assigned publication timestamps.",
       "Page last-updated dates and crawl timestamps are not treated as report release timestamps.",
       "No source is promoted into Factor Registry by this discovery artifact."]}
    (OUT/"archive_route_inventory.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    with (OUT/"archive_route_inventory.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["page_type","discovered_on","label","url","asset_candidate"]);w.writeheader()
        w.writerows([{k:x.get(k) for k in w.fieldnames} for x in routes])
    print(json.dumps({"status":result["status"],"scope":result["scope"],"counts":result["counts"]},indent=2))
if __name__=="__main__":main()
