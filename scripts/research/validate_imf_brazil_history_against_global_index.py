#!/usr/bin/env python3
"""Cross-check all Brazil Registration URN history rows against global transaction index."""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from urllib.parse import quote
import hashlib,json,csv

BASE="https://sdmxcentral.imf.org"
REG="urn:sdmx:org.sdmx.infomodel.registry.Registration=IMF:D429E36CD161E2F2A34ECAF137994E89(1.0)"
OUT=Path("imf_brazil_history_index_reconciliation"); OUT.mkdir(parents=True,exist_ok=True)

def get(url):
    ts=datetime.now(timezone.utc).isoformat()
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-independent-audit/1.5","Accept":"application/json"})
    try:
        with urlopen(req,timeout=60) as r: status=r.status; headers=dict(r.headers.items()); body=r.read()
    except HTTPError as e: status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
    except (URLError,TimeoutError) as e: status=0; headers={}; body=str(e).encode()
    safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
    return {"retrieved_at_utc":ts,"http_status":status,"headers":safe,"body":body}

def sha(b): return hashlib.sha256(b).hexdigest()
q=quote(REG,safe="")
hurl=BASE+"/ws/registry/tx/history?urn="+q
iurl=BASE+"/ws/registry/tx/searchTransactions?max=50000&orderDesc=false"
h=get(hurl); i=get(iurl)
(OUT/"registration_history.json").write_bytes(h["body"])
(OUT/"global_transaction_index.json").write_bytes(i["body"])
if h["http_status"]!=200 or i["http_status"]!=200: raise SystemExit(f"HTTP failures history={h['http_status']} index={i['http_status']}")
history=json.loads(h["body"]); index=json.loads(i["body"])
if not isinstance(history,list) or not isinstance(index,list): raise SystemExit("JSON payloads are not arrays")
lookup={int(x["Id"]):x for x in index}
rows=[]; missing=[]
for x in history:
    tid=int(x["Id"]); g=lookup.get(tid)
    if g is None: missing.append(tid)
    rows.append({
      "tx_id":tid,
      "history_date_ms":int(x["Date"]),
      "history_date_utc":datetime.fromtimestamp(int(x["Date"])/1000,timezone.utc).isoformat(),
      "history_action":x.get("Action"),"history_type":x.get("Type"),
      "index_date_ms":int(g["Date"]) if g else None,
      "index_date_utc":datetime.fromtimestamp(int(g["Date"])/1000,timezone.utc).isoformat() if g else None,
      "index_action":g.get("Action") if g else None,"index_type":g.get("Type") if g else None,
      "date_match":bool(g and int(g["Date"])==int(x["Date"])),
      "action_match":bool(g and g.get("Action")==x.get("Action")),
      "type_available_in_index":bool(g and g.get("Type") is not None)
    })
(OUT/"reconciled_events.json").write_text(json.dumps(rows,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
with (OUT/"reconciled_events.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
summary={"registration_urn":REG,"history_http_status":h["http_status"],"history_retrieved_at_utc":h["retrieved_at_utc"],
 "history_byte_count":len(h["body"]),"history_sha256":sha(h["body"]),
 "global_index_http_status":i["http_status"],"global_index_retrieved_at_utc":i["retrieved_at_utc"],
 "global_index_byte_count":len(i["body"]),"global_index_sha256":sha(i["body"]),
 "global_index_record_count":len(index),"global_index_min_tx_id":min(int(x["Id"]) for x in index) if index else None,
 "global_index_max_tx_id":max(int(x["Id"]) for x in index) if index else None,
 "history_event_count":len(history),"matched_event_count":len(rows)-len(missing),"missing_tx_ids":missing,
 "date_matches":sum(x["date_match"] for x in rows),"action_matches":sum(x["action_match"] for x in rows),
 "index_type_registration_count":sum(x["index_type"]=="Registration" for x in rows),
 "index_type_missing_count":sum(x["index_type"] is None for x in rows),
 "mismatches":[x for x in rows if not x["date_match"] or not x["action_match"]]}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
if missing or summary["date_matches"]!=len(history) or summary["action_matches"]!=len(history):
    raise SystemExit("Reconciliation not complete; inspect summary and rows")
