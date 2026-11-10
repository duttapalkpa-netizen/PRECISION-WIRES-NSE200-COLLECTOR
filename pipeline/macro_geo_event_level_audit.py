#!/usr/bin/env python3
"""Event-level audit explaining why each historical media event can/cannot form a return window."""
from pathlib import Path
import json
import pandas as pd

PANEL=Path("data/external/market_panel.csv")
EVENTS=Path("data/external/events.csv")
OUT=Path("outputs/macro_geo/event_level_window_audit.csv")
REPORT=Path("outputs/macro_geo/event_level_window_audit.json")
IST="Asia/Kolkata"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if not PANEL.exists() or not EVENTS.exists():
        report={"status":"BLOCKED_MISSING_INPUTS","panel_exists":PANEL.exists(),"events_exists":EVENTS.exists(),"rows":0}
        REPORT.write_text(json.dumps(report,indent=2))
        print(json.dumps(report)); return 2
    panel=pd.read_csv(PANEL); events=pd.read_csv(EVENTS)
    panel.columns=[str(c).strip().upper() for c in panel.columns]
    events.columns=[str(c).strip().upper() for c in events.columns]
    required_panel={"DATE","SERIES","CLOSE"}
    required_events={"EVENT_ID","EVENT_DATE","PUBLISHED_AT","SOURCE","SOURCE_URL","EVENT_DATE_BASIS"}
    if required_panel-set(panel.columns) or required_events-set(events.columns):
        report={"status":"BLOCKED_SCHEMA","missing_panel":sorted(required_panel-set(panel.columns)),
                "missing_events":sorted(required_events-set(events.columns)),"rows":0}
        REPORT.write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 2
    panel["DATE"]=pd.to_datetime(panel["DATE"],errors="coerce").dt.normalize()
    panel["CLOSE"]=pd.to_numeric(panel["CLOSE"],errors="coerce")
    panel=panel.dropna(subset=["DATE","SERIES","CLOSE"]).sort_values(["SERIES","DATE"])
    panel=panel.loc[panel["CLOSE"]>0]
    events["PUBLISHED_AT"]=pd.to_datetime(events["PUBLISHED_AT"],errors="coerce",utc=True)
    rows=[]
    for _,ev in events.iterrows():
        pub=ev["PUBLISHED_AT"]
        if pd.isna(pub):
            rows.append({"EVENT_ID":ev.get("EVENT_ID",""),"SOURCE":ev.get("SOURCE",""),
                "SOURCE_URL":ev.get("SOURCE_URL",""),"PUBLISHED_AT":"","EVENT_DATE":ev.get("EVENT_DATE",""),
                "EVENT_DATE_BASIS":ev.get("EVENT_DATE_BASIS",""),"SERIES":"ALL",
                "BASE_CLOSE_DATE":"","BASE_CLOSE":None,"H1_CLOSE_DATE":"","H1_CLOSE":None,"H5_CLOSE_DATE":"","H5_CLOSE":None,"H20_CLOSE_DATE":"","H20_CLOSE":None,
                "H1_MATURE":False,"H5_MATURE":False,"H20_MATURE":False,"WINDOW_STATUS":"BLOCKED_INVALID_PUBLICATION_TIMESTAMP"})
            continue
        pub_ist=pub.tz_convert(IST)
        for series,g in panel.groupby("SERIES"):
            close_times=g["DATE"].map(lambda d: d.tz_localize(IST)+pd.Timedelta(hours=15,minutes=30))
            base=g.loc[close_times<=pub_ist]
            post=g.loc[close_times>pub_ist]
            if base.empty:
                status="BLOCKED_NO_PRE_PUBLICATION_CLOSE"
                base_date=""; base_close=None
            else:
                b=base.iloc[-1]; base_date=b["DATE"].date().isoformat(); base_close=float(b["CLOSE"])
                status="MATURE_WINDOW_AVAILABLE" if len(post)>=1 else "PENDING_NEXT_MARKET_CLOSE"
            post_rows=post.head(20)
            def close_at(n):
                if len(post_rows)>=n:
                    q=post_rows.iloc[n-1]; return q["DATE"].date().isoformat(),float(q["CLOSE"])
                return "",None
            h1d,h1c=close_at(1); h5d,h5c=close_at(5); h20d,h20c=close_at(20)
            rows.append({"EVENT_ID":ev.get("EVENT_ID",""),"SOURCE":ev.get("SOURCE",""),
                "SOURCE_URL":ev.get("SOURCE_URL",""),"PUBLISHED_AT":pub.isoformat(),
                "EVENT_DATE":str(ev.get("EVENT_DATE","")),"EVENT_DATE_BASIS":str(ev.get("EVENT_DATE_BASIS","")),
                "SERIES":series,"BASE_CLOSE_DATE":base_date,"BASE_CLOSE":base_close,
                "H1_CLOSE_DATE":h1d,"H1_CLOSE":h1c,"H5_CLOSE_DATE":h5d,"H5_CLOSE":h5c,"H20_CLOSE_DATE":h20d,"H20_CLOSE":h20c,
                "H1_MATURE":bool(h1d),"H5_MATURE":bool(h5d),"H20_MATURE":bool(h20d),"WINDOW_STATUS":status})
    audit=pd.DataFrame(rows)
    audit.to_csv(OUT,index=False)
    counts=audit["WINDOW_STATUS"].value_counts().to_dict() if not audit.empty else {}
    report={"status":"AUDIT_COMPLETE","event_rows":int(events.shape[0]),"series_count":int(panel["SERIES"].nunique()),
        "panel_min_date":panel["DATE"].min().date().isoformat() if not panel.empty else None,
        "panel_max_date":panel["DATE"].max().date().isoformat() if not panel.empty else None,
        "event_series_audit_rows":int(len(audit)),"window_status_counts":counts,
        "unique_events_with_mature_h1":int(audit.loc[audit.get("H1_MATURE",False)==True,"EVENT_ID"].nunique()) if not audit.empty else 0,
        "unique_events_with_mature_h5":int(audit.loc[audit.get("H5_MATURE",False)==True,"EVENT_ID"].nunique()) if not audit.empty else 0,
        "unique_events_with_mature_h20":int(audit.loc[audit.get("H20_MATURE",False)==True,"EVENT_ID"].nunique()) if not audit.empty else 0,
        "historical_source_gap":"This audit diagnoses maturity only; it does not fabricate publication timestamps or backfill historical events."}
    REPORT.write_text(json.dumps(report,indent=2)); print(json.dumps(report))
    return 0

if __name__=="__main__": raise SystemExit(main())
