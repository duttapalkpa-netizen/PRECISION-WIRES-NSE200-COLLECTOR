#!/usr/bin/env python3
"""Small live FRED smoke test; fetches two series for the last 21 calendar days only."""
from datetime import datetime, timezone, timedelta
from io import StringIO
import json
import pandas as pd
import requests

URL = "https://fred.stlouisfed.org/graph/fredgraph.csv"
end = datetime.now(timezone.utc).date()
start = end - timedelta(days=21)
session = requests.Session()
session.headers.update({"User-Agent": "PRECISION-WIRES-NSE200-COLLECTOR/1.0 (bounded source smoke)", "Accept": "text/csv,*/*"})
results = []
for series in ("DGS10", "DCOILWTICO"):
    response = session.get(URL, params={"id": series, "cosd": start.isoformat(), "coed": end.isoformat()}, timeout=(8, 18))
    response.raise_for_status()
    frame = pd.read_csv(StringIO(response.content.decode("utf-8-sig", errors="replace")))
    frame.columns = [str(c).strip().upper() for c in frame.columns]
    date_col = next((c for c in ("DATE", "OBSERVATION_DATE") if c in frame.columns), None)
    if date_col is None or series not in frame.columns:
        raise SystemExit(json.dumps({"status": "FAIL", "series": series, "reason": "schema mismatch", "columns": list(frame.columns)}))
    dates = pd.to_datetime(frame[date_col], errors="coerce")
    values = pd.to_numeric(frame[series], errors="coerce")
    valid = [(dates.iloc[i].date().isoformat(), float(values.iloc[i])) for i in range(len(frame))
             if pd.notna(dates.iloc[i]) and pd.notna(values.iloc[i]) and start <= dates.iloc[i].date() <= end]
    if not valid:
        raise SystemExit(json.dumps({"status": "FAIL", "series": series, "reason": "no valid observed values", "url": response.url}))
    results.append({"series": series, "rows": len(valid), "date_min": valid[0][0], "date_max": valid[-1][0], "url": response.url})
print(json.dumps({"status": "PASS", "window_start": start.isoformat(), "window_end": end.isoformat(), "series": results}, indent=2))
