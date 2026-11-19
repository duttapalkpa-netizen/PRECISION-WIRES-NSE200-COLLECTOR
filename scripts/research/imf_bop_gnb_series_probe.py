#!/usr/bin/env python3
"""Bounded read-only IMF BOP GNB series probe. No transformation/admission."""
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, csv, io

BASE = "https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0"
OUT = Path("imf_gnb_bop_probe"); OUT.mkdir(exist_ok=True)
SPECS = [
    ("GNB.A_NFA_T.P_F.USD.Q", "2024-Q1", "2024-Q4"),
    ("GNB.L_NIL_T.P_F.USD.Q", "2024-Q1", "2024-Q4"),
    ("GNB.A_NFA_T.P_F.USD.A", "2024", "2024"),
    ("GNB.L_NIL_T.P_F.USD.A", "2024", "2024"),
]
def sha(b): return hashlib.sha256(b).hexdigest()
results=[]
for key,start,end in SPECS:
    url=f"{BASE}/{key}?c%5BTIME_PERIOD%5D=ge%3A{start}&c%5BTIME_PERIOD%5D=le%3A{end}&format=csvdata"
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-GNB-BOP-probe/1.0","Accept":"text/csv, */*"})
    ts=datetime.now(timezone.utc).isoformat()
    try:
        with urlopen(req,timeout=35) as r:
            status=r.status; final=r.geturl(); headers=dict(r.headers.items()); body=r.read()
    except HTTPError as e:
        status=e.code; final=e.geturl(); headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
    except (URLError,TimeoutError) as e:
        status=0; final=url; headers={}; body=str(e).encode()
    fn=key.replace(".","_")+".raw"; (OUT/fn).write_bytes(body)
    row={"key":key,"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,
         "headers":{k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization"}},
         "byte_count":len(body),"sha256":sha(body),"file":fn}
    if status==200:
        try:
            txt=body.decode("utf-8-sig")
            if txt.lstrip().startswith("<"): raise ValueError("non-CSV response")
            rows=list(csv.DictReader(io.StringIO(txt)))
            obs=[x for x in rows if (x.get("OBS_VALUE") or "").strip()]
            row.update({"parse":"PASS","rows":len(rows),"nonempty_observations":len(obs),
                        "periods":[x.get("TIME_PERIOD") for x in obs],
                        "sample":obs[:4]})
        except Exception as e: row.update({"parse":"FAIL","error":str(e)})
    results.append(row)
summary={"scope":"GNB IMF BOP exact-key availability probe; not a country admission","dataflow":"IMF.STA:BOP(21.0.0)",
         "requests":results,"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
         "no_conversion":True,"no_interpolation":True,"no_production_admission":True}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
