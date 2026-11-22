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
# NSE Capital Market holidays verified against circular NSE/CMTR/71775 (2025-12-12).
NSE_TRADING_HOLIDAYS_2026 = {
    date(2026,6,26): "Muharram",
    date(2026,9,14): "Ganesh Chaturthi",
    date(2026,10,2): "Mahatma Gandhi Jayanti",
    date(2026,10,20): "Dussehra",
    date(2026,11,10): "Diwali-Balipratipada",
}
NSE_TRADING_HOLIDAY_SOURCE = "https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf"

def nse_trading_holiday_name(day):
    """Return the officially declared 2026 NSE cash-market holiday name, if any."""
    return NSE_TRADING_HOLIDAYS_2026.get(day)

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

def clip_to_window(df, start, end):
    """Keep only valid source dates inside the declared collection window."""
    if df.empty:
        return df.copy()
    dates = pd.to_datetime(df["DATE"], errors="coerce").dt.date
    keep = dates.notna() & dates.ge(start) & dates.le(end)
    out = df.loc[keep].copy()
    out["DATE"] = dates.loc[keep].astype("string")
    return out

def coverage_audit(df, start, end, dii_query_attempts=None):
    """Compare official FPI archive dates and separately expose each DII date-query outcome."""
    fpi = set(df.loc[df["GROUP"] == "FPI", "DATE"].dropna().astype(str))
    dii = set(df.loc[df["GROUP"] == "DII", "DATE"].dropna().astype(str))
    missing = sorted(fpi - dii)
    attempts = list(dii_query_attempts or [])
    failed = sorted(str(x.get("date")) for x in attempts if x.get("status") == "FAILED")
    succeeded = sum(x.get("status") == "SUCCESS" for x in attempts)
    return {
        "window_start": start.isoformat(),
        "window_end": end.isoformat(),
        "fpi_archive_dates": len(fpi),
        "dii_archive_dates": len(dii),
        "dii_missing_fpi_archive_dates": missing,
        "dii_coverage_vs_fpi_archive_dates_pct": round(100 * len(fpi & dii) / len(fpi), 2) if fpi else None,
        "dii_query_attempts": len(attempts),
        "dii_query_successes": succeeded,
        "dii_query_failures": len(failed),
        "dii_query_failed_dates": failed,
        "dii_query_attempt_log": attempts,
        "comparison_basis": "FPI archive-date alignment is separate from exact DII query outcomes; attempted dates are not asserted to be a complete official exchange-session calendar",
        "quality": "AVAILABLE_WITH_GAPS" if missing or failed else "AVAILABLE"
    }


def derive_collection_status(complete, errors, audit):
    """Never label a partial or failed source collection simply AVAILABLE."""
    if not complete:
        return "BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE"
    if errors or audit.get("quality") == "AVAILABLE_WITH_GAPS":
        return "AVAILABLE_WITH_GAPS"
    return "AVAILABLE"
def main():
    OUT.parent.mkdir(parents=True,exist_ok=True); REPORT.parent.mkdir(parents=True,exist_ok=True)
    report={"status":"BLOCKED","source":"NSDL official public FPI/DII archives","fpi_url":FPI_URL,"dii_url":DII_URL,"groups":{},"errors":[],"non_trading_holidays":[],"holiday_calendar_source":NSE_TRADING_HOLIDAY_SOURCE}
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
    client=Nsdl(); rows=[]; fpi_dates=0; dii_dates=0; dii_query_attempts=[]
    # FPI archive: one WebForms query per month returns daily rows for that month.
    fpi_ok=0
    for qday in month_ends(start,end):
        try:
            page,url=client.post_date(FPI_URL,qday)
            got=find_flow_rows(page,"FPI",qday,url)
            rows.extend(got); fpi_ok+=1
        except Exception as e: report["errors"].append(f"FPI {qday}: {type(e).__name__}: {str(e)[:220]}")
    # DII archive: NSDL publishes daily DII rows only from 2026-06-01.
    dii_ok=0; day=start
    while day<=end:
        if day.weekday()<5:
            holiday_name=nse_trading_holiday_name(day)
            if holiday_name:
                report["non_trading_holidays"].append({"date":day.isoformat(),"name":holiday_name,"source":NSE_TRADING_HOLIDAY_SOURCE})
                day+=timedelta(days=1)
                continue
            try:
                page,url=client.post_date(DII_URL,day)
                got=find_flow_rows(page,"DII",day,url)
                rows.extend(got); dii_ok+=1
                dii_query_attempts.append({"date":day.isoformat(),"status":"SUCCESS","rows":len(got),"source_url":url})
            except Exception as e:
                error=f"{type(e).__name__}: {str(e)[:180]}"
                report["errors"].append(f"DII {day}: {error}")
                dii_query_attempts.append({"date":day.isoformat(),"status":"FAILED","error":error,"source_url":DII_URL})
        day+=timedelta(days=1)
    df=pd.DataFrame(rows,columns=["DATE","GROUP","NET_VALUE","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"])
    if not df.empty:
        df["DATE"]=pd.to_datetime(df["DATE"],errors="coerce").dt.date.astype("string")
        df["NET_VALUE"]=pd.to_numeric(df["NET_VALUE"],errors="coerce")
        df=df.dropna(subset=["DATE","GROUP","NET_VALUE"]).drop_duplicates(["DATE","GROUP"]).sort_values(["DATE","GROUP"])
        # Monthly FPI postbacks return the entire month; clip to the declared P0 window.
        df=clip_to_window(df,start,end)
    report["coverage_audit"]=coverage_audit(df,start,end,dii_query_attempts)
    details={}
    for group in ("FPI","DII"):
        g=df[df["GROUP"]==group] if not df.empty else pd.DataFrame()
        nd=int(g["DATE"].nunique()) if not g.empty else 0
        span=(pd.to_datetime(g["DATE"],errors="coerce").max()-pd.to_datetime(g["DATE"],errors="coerce").min()).days if nd>1 else 0
        details[group]={"rows":len(g),"unique_dates":nd,"span_days":int(span)}
    report["groups"]=details
    report["fpi_month_queries_succeeded"]=fpi_ok
    report["dii_day_queries_succeeded"]=dii_ok
    report["dii_day_queries_failed"]=sum(x["status"]=="FAILED" for x in dii_query_attempts)
    report["dii_query_attempts"]=len(dii_query_attempts)
    report["range"]={"start":start.isoformat(),"end":end.isoformat()}
    # Both series independently meet the same maturity threshold before replacing
    # any existing P0 file. Partial snapshots are diagnostic only and cannot pass.
    complete=all(details[g]["unique_dates"]>=60 and details[g]["span_days"]>=90 for g in ("FPI","DII"))
    if complete:
        df.to_csv(OUT,index=False)
        report["status"]=derive_collection_status(complete,report["errors"],report["coverage_audit"])
        report["output"]=str(OUT)
    else:
        report["status"]="BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE"
        report["reason"]="Both FPI and DII independently require >=60 distinct dates spanning >=90 calendar days; existing file was not overwritten."
    REPORT.write_text(json.dumps(report,indent=2)); print(json.dumps(report))
    return 0

if __name__=="__main__":
    main()
