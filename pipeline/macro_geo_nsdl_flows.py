#!/usr/bin/env python3
"""Collect official NSDL daily FPI and DII flows into the Macro-Geo P0 schema.

NSDL's FPI archive is queried monthly; its DII archive is queried per weekday
(starting 2026-06-01, when NSDL began publishing daily DII data). Only rows
explicitly identified as Equity / Stock Exchange are aggregated. Missing data
or schema drift remains BLOCKED; no values are inferred or synthesized.
"""
from __future__ import annotations
import calendar, html, json, re, time
from datetime import date, datetime, timedelta, timezone
from io import StringIO
from pathlib import Path
import pandas as pd
import requests

ROOT=Path(".")
OUT=ROOT/"data/external/fpi_dii_flows.csv"
REPORT=ROOT/"outputs/macro_geo/nsdl_fpi_dii_collection.json"
PANEL=ROOT/"data/processed/nse_eq_200_sessions.csv"
FPI_URL="https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx"
DII_URL="https://www.fpi.nsdl.co.in/web/Users/DIIGenerateReport.aspx?Rep=A"
BASE="https://www.fpi.nsdl.co.in/web/"
UA=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
FIRST_DII=date(2026,6,1)

def norm(s):
    return re.sub(r"[^a-z0-9]+"," ",str(s).lower()).strip()

def number(v):
    if pd.isna(v): return None
    s=str(v).strip().replace(",","").replace("₹","").replace("−","-")
    if s.upper() in {"","-","--","NA","N/A","NIL","NONE"}: return None
    neg=s.startswith("(") and s.endswith(")")
    s=s.strip("()")
    try:
        n=float(s)
        return -n if neg else n
    except (TypeError,ValueError): return None

def month_ends(start,end):
    out=[]; y,m=start.year,start.month
    while date(y,m,1)<=end:
        out.append(min(date(y,m,calendar.monthrange(y,m)[1]),end))
        y,m=(y+1,1) if m==12 else (y,m+1)
    return out

def hidden_fields(page):
    fields={}
    for tag in re.findall(r"<input\b[^>]*>",page,re.I|re.S):
        attrs={}
        for k,q,v in re.findall(r"""([\w:-]+)\s*=\s*(["'])(.*?)\2""",tag,re.I|re.S):
            attrs[k.lower()]=html.unescape(v)
        name=attrs.get("name")
        if name: fields[name]=attrs.get("value","")
    return fields

class Nsdl:
    def __init__(self):
        self.s=requests.Session()
        self.s.headers.update({"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":"en-US,en;q=0.9"})
        self.state={}
    def post_date(self,url,day):
        if url not in self.state:
            r=self.s.get(url,timeout=(8,25)); r.raise_for_status()
            self.state[url]=hidden_fields(r.text)
        text=day.strftime("%d-%b-%Y")
        payload={**self.state[url],"__EVENTTARGET":"btnSubmit1","__EVENTARGUMENT":"","txtDate":text,"hdnDate":text}
        r=self.s.post(url,data=payload,timeout=(8,30)); r.raise_for_status()
        page=r.text
        state=hidden_fields(page)
        if "__VIEWSTATE" not in state:
            # One clean re-bootstrap is permitted; a rejected postback is not treated as data.
            self.state.pop(url,None)
            r=self.s.get(url,timeout=(8,25)); r.raise_for_status()
            self.state[url]=hidden_fields(r.text)
            payload={**self.state[url],"__EVENTTARGET":"btnSubmit1","__EVENTARGUMENT":"","txtDate":text,"hdnDate":text}
            r=self.s.post(url,data=payload,timeout=(8,30)); r.raise_for_status()
            page=r.text; state=hidden_fields(page)
        if "__VIEWSTATE" not in state:
            raise RuntimeError("NSDL form postback returned no refreshed VIEWSTATE")
        self.state[url]=state
        time.sleep(0.25)
        return page, r.url

def scheduled_dii_sessions(panel_dates,start,end):
    """Use actual canonical NSE sessions; weekdays alone include exchange holidays."""
    out=set()
    for value in panel_dates:
        d=pd.to_datetime(value,errors="coerce")
        if pd.notna(d):
            day=d.date()
            if FIRST_DII<=day and start<=day<=end:
                out.add(day)
    return sorted(out)

def page_diagnostic(page):
    """Capture bounded schema evidence without storing full HTML responses."""
    raw=str(page or "")
    plain=re.sub(r"<[^>]+>"," ",raw)
    plain=re.sub(r"\s+"," ",html.unescape(plain)).strip()
    headers=[]
    for table in re.findall(r"<table\b.*?</table>",raw,re.I|re.S)[:8]:
        first_row=re.search(r"<tr\b.*?</tr>",table,re.I|re.S)
        if not first_row:
            continue
        cells=re.findall(r"<(?:th|td)\b[^>]*>(.*?)</(?:th|td)>",first_row.group(0),re.I|re.S)
        labels=[]
        for cell in cells[:12]:
            label=re.sub(r"<[^>]+>"," ",cell)
            label=re.sub(r"\s+"," ",html.unescape(label)).strip()
            labels.append(label[:120])
        if labels:
            headers.append(labels)
    return {
        "explicit_no_data_found":bool(re.search(r"\bno\s+data\s+found\b",plain,re.I)),
        "page_text_preview":plain[:320],
        "table_headers":headers,
    }

def table_records(page):
    tables=pd.read_html(StringIO(page),displayed_only=False)
    out=[]
    for t in tables:
        if isinstance(t.columns,pd.MultiIndex):
            t.columns=[" | ".join(str(x).strip() for x in col if str(x)!="nan" and str(x).strip()) for col in t.columns]
        else: t.columns=[str(c).strip() for c in t.columns]
        out.append(t)
    return out

def col_for(cols,tests,exclude=()):
    for c in cols:
        n=norm(c)
        if all(x in n for x in tests) and not any(x in n for x in exclude): return c
    return None

def find_flow_rows(page,group,query_date,source_url):
    tables=table_records(page)
    for df in tables:
        cols=list(df.columns); normcols={c:norm(c) for c in cols}
        net=col_for(cols,["net investment"],["usd","million","us mn"])
        instrument=col_for(cols,["instrument"]) or col_for(cols,["debt equity"]) or col_for(cols,["asset class"])
        route=col_for(cols,["investment route"]) or col_for(cols,["route"])
        datecol=col_for(cols,["reporting date"]) or col_for(cols,["date"])
        # DII table is marked Type of DII; FPI archive is marked Reporting Date.
        joined=" ".join(normcols.values())
        if not net or not instrument or not route: continue
        if group=="DII" and "type of dii" not in joined: continue
        if group=="FPI" and not datecol: continue
        x=df.copy()
        x["_instrument"]=x[instrument].astype(str).map(norm)
        x["_route"]=x[route].astype(str).map(norm)
        x=x[x["_instrument"].str.contains(r"\bequity\b",regex=True,na=False)]
        x=x[x["_route"].str.contains("stock exchange",regex=False,na=False)]
        if x.empty: continue
        vals=pd.to_numeric(x[net].map(number),errors="coerce").dropna()
        if vals.empty: continue
        if group=="FPI":
            if datecol:
                ds=pd.to_datetime(x[datecol],errors="coerce",dayfirst=True).dropna()
                if ds.empty: continue
                # Keep only the requested monthly query's date range.
                x=x.loc[pd.to_datetime(x[datecol],errors="coerce",dayfirst=True).notna()].copy()
                x["_date"]=pd.to_datetime(x[datecol],errors="coerce",dayfirst=True).dt.date
                x=x[(x["_date"]>=date(query_date.year,query_date.month,1))&(x["_date"]<=query_date)]
                vals=pd.to_numeric(x[net].map(number),errors="coerce").dropna()
                if vals.empty: continue
                bydate=x.assign(_net=pd.to_numeric(x[net].map(number),errors="coerce")).dropna(subset=["_net"]).groupby("_date")["_net"].sum()
                return [{"DATE":d.isoformat(),"GROUP":"FPI","NET_VALUE":float(v),"SOURCE":"NSDL official FPI daily archive","SOURCE_URL":source_url,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()} for d,v in bydate.items()]
        else:
            # DII archive is queried for one exact date; sum institution rows for
            # Equity / Stock Exchange, not subtotal rows that would double-count.
            return [{"DATE":query_date.isoformat(),"GROUP":"DII","NET_VALUE":float(vals.sum()),"SOURCE":"NSDL official DII daily archive","SOURCE_URL":source_url,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()}]
    raise RuntimeError(f"NSDL {group} schema not recognized for {query_date}; no Equity/Stock Exchange net-investment table")

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True); REPORT.parent.mkdir(parents=True,exist_ok=True)
    report={"status":"BLOCKED","source":"NSDL official public FPI/DII archives","fpi_url":FPI_URL,"dii_url":DII_URL,"groups":{},"errors":[]}
    if not PANEL.exists():
        report["errors"].append(f"Missing canonical panel: {PANEL}")
        REPORT.write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 0
    panel=pd.read_csv(PANEL,usecols=lambda c:str(c).strip().upper()=="DATE")
    dates=pd.to_datetime(panel.iloc[:,0],errors="coerce").dropna()
    if dates.empty:
        report["errors"].append("Canonical panel contains no valid dates")
        REPORT.write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 0
    end=min(date.today(),max(dates.dt.date))
    start=max(FIRST_DII,end-timedelta(days=150))
    client=Nsdl(); rows=[]; fpi_dates=0; dii_dates=0
    # FPI archive: one WebForms query per month returns daily rows for that month.
    fpi_ok=0
    for qday in month_ends(start,end):
        try:
            page,url=client.post_date(FPI_URL,qday)
            got=find_flow_rows(page,"FPI",qday,url)
            rows.extend(got); fpi_ok+=1
        except Exception as e: report["errors"].append(f"FPI {qday}: {type(e).__name__}: {str(e)[:220]}")
    # DII archive: query only dates present in the canonical NSE session panel.
    # Weekday iteration incorrectly queried exchange holidays and mislabeled
    # the expected absence of a daily report as a schema mismatch.
    dii_query_dates=scheduled_dii_sessions(dates.dt.date.tolist(),start,end)
    report["dii_query_dates_from_canonical_nse_sessions"]=len(dii_query_dates)
    report["dii_weekdays_skipped_not_in_nse_panel"]=[
        d.isoformat() for d in pd.date_range(start,end,freq="B").date if d not in set(dii_query_dates)
    ]
    dii_ok=0; dii_diagnostics=[]
    for day in dii_query_dates:
        page=None; url=DII_URL
        try:
            page,url=client.post_date(DII_URL,day)
            got=find_flow_rows(page,"DII",day,url)
            rows.extend(got); dii_ok+=1
        except Exception as e:
            diag=page_diagnostic(page) if page is not None else {"request_completed":False}
            dii_diagnostics.append({"date":day.isoformat(),"url":url,
                "error_type":type(e).__name__,"error":str(e)[:220],**diag})
            report["errors"].append(f"DII {day}: {type(e).__name__}: {str(e)[:180]}")
    report["dii_query_diagnostics"]=dii_diagnostics
    df=pd.DataFrame(rows,columns=["DATE","GROUP","NET_VALUE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"])
    if not df.empty:
        df["DATE"]=pd.to_datetime(df["DATE"],errors="coerce").dt.date.astype("string")
        df["NET_VALUE"]=pd.to_numeric(df["NET_VALUE"],errors="coerce")
        df=df.dropna(subset=["DATE","GROUP","NET_VALUE"]).drop_duplicates(["DATE","GROUP"]).sort_values(["DATE","GROUP"])
    details={}
    for group in ("FPI","DII"):
        g=df[df["GROUP"]==group] if not df.empty else pd.DataFrame()
        nd=int(g["DATE"].nunique()) if not g.empty else 0
        span=(pd.to_datetime(g["DATE"],errors="coerce").max()-pd.to_datetime(g["DATE"],errors="coerce").min()).days if nd>1 else 0
        details[group]={"rows":len(g),"unique_dates":nd,"span_days":int(span)}
    report["groups"]=details
    report["fpi_month_queries_succeeded"]=fpi_ok
    report["dii_day_queries_succeeded"]=dii_ok
    report["range"]={"start":start.isoformat(),"end":end.isoformat()}
    # Both series independently meet the same maturity threshold before replacing
    # any existing P0 file. Partial snapshots are diagnostic only and cannot pass.
    complete=all(details[g]["unique_dates"]>=60 and details[g]["span_days"]>=90 for g in ("FPI","DII"))
    if complete:
        df.to_csv(OUT,index=False)
        report["status"]="AVAILABLE"
        report["output"]=str(OUT)
    else:
        report["status"]="BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE"
        report["reason"]="Both FPI and DII independently require >=60 distinct dates spanning >=90 calendar days; existing file was not overwritten."
    REPORT.write_text(json.dumps(report,indent=2)); print(json.dumps(report))
    return 0

if __name__=="__main__":
    main()
