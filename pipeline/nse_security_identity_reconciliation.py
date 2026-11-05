#!/usr/bin/env python3
"""Research-only NSE symbol identity reconciliation; absence is never proof of suspension/delisting."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
import pandas as pd

def norm_col(v):
    return re.sub(r"[^A-Z0-9]", "", str(v).strip().upper())

def read_csv(path):
    # Preserve identifiers and tolerate BOM; do not silently accept empty/malformed inputs.
    df = pd.read_csv(path, dtype=str, encoding="utf-8-sig").fillna("")
    df.columns = [norm_col(c) for c in df.columns]
    if df.empty or not len(df.columns):
        raise ValueError(f"empty source: {path}")
    return df

def choose(df, aliases, required=True):
    for a in aliases:
        if a in df.columns:
            return a
    if required:
        raise ValueError(f"missing required column; expected one of {aliases}, got {list(df.columns)}")
    return None

def clean(v):
    return str(v or "").strip().upper()

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--stale",required=True,help="249 stale candidate rows CSV")
    p.add_argument("--equity",required=True,help="official NSE equity securities CSV")
    p.add_argument("--symbol-changes",required=True,help="official NSE changes-in-symbols CSV")
    p.add_argument("--etf",help="official NSE ETF CSV")
    p.add_argument("--sme",help="official NSE SME CSV")
    p.add_argument("--out",default="outputs/qa/nse_identity_reconciliation")
    a=p.parse_args()
    inputs={"stale_candidates":a.stale,"equity":a.equity,"symbol_changes":a.symbol_changes}
    if a.etf: inputs["etf"]=a.etf
    if a.sme: inputs["sme"]=a.sme
    frames={k:read_csv(v) for k,v in inputs.items()}
    stale=frames["stale_candidates"]
    sc=choose(stale,["SYMBOL","OLD_SYMBOL"])
    si=choose(stale,["ISIN","ISINNO","ISINNUMBER"],False)
    if not si: stale["_ISIN"]=""
    else: stale["_ISIN"]=stale[si].map(clean)
    stale["_SYMBOL"]=stale[sc].map(clean)
    if (stale["_SYMBOL"]=="").any(): raise ValueError("blank stale candidate symbol")
    if stale["_SYMBOL"].duplicated().any(): raise ValueError("duplicate stale candidate symbols; resolve before reconciliation")
    lists={}
    for cat in ("equity","etf","sme"):
        if cat not in frames: continue
        df=frames[cat]
        symc=choose(df,["SYMBOL","TRADINGSYMBOL","TCKRSYMBL"])
        isinc=choose(df,["ISIN","ISINNO","ISINNUMBER"],False)
        lists[cat]={}
        for _,r in df.iterrows():
            s=clean(r[symc])
            if not s: continue
            lists[cat].setdefault(s,set()).add(clean(r[isinc]) if isinc else "")
    changes=frames["symbol_changes"]
    oldc=choose(changes,["OLDSYMBOL","PREVIOUSSYMBOL","FROM"])
    newc=choose(changes,["NEWSYMBOL","TRADINGSYMBOL","TOSYMBOL","TO"])
    rename={}
    for _,r in changes.iterrows():
        old,new=clean(r[oldc]),clean(r[newc])
        if old and new: rename.setdefault(old,set()).add(new)
    all_current={s:cats for cat,mp in lists.items() for s in mp for cats in [set([cat])]}
    def current_matches(sym, isin):
        found=[]
        for cat,mp in lists.items():
            if sym in mp:
                vals=mp[sym]
                # A matching ISIN does not override conflicting/blank identity rows
                # for the same symbol in the same official snapshot.
                if not isin or not any(vals):
                    found.append((cat,"SYMBOL_MATCH_ISIN_UNAVAILABLE"))
                elif vals == {isin}:
                    found.append((cat,"ISIN_MATCH"))
                else:
                    found.append((cat,"SYMBOL_MATCH_ISIN_CONFLICT"))
        return found
    rows=[]
    for _,r in stale.iterrows():
        old,isin=r["_SYMBOL"],r["_ISIN"]
        direct=current_matches(old,isin)
        resolved=old; path=[old]; status="UNKNOWN_NOT_IN_PROVIDED_SNAPSHOTS"; cats=[]; evidence=""
        if len(direct)==1:
            cats=[direct[0][0]]; evidence=direct[0][1]
            status="MATCHED_CURRENT_NSE_LIST" if evidence!="SYMBOL_MATCH_ISIN_CONFLICT" else "UNKNOWN_ISIN_CONFLICT"
        elif len(direct)>1:
            status="UNKNOWN_AMBIGUOUS_CATEGORY"; cats=[x[0] for x in direct]; evidence="SYMBOL_PRESENT_IN_MULTIPLE_LISTS"
        else:
            seen={old}; frontier=[old]; targets=[]
            for _ in range(5):
                nxt=[]
                for s in frontier:
                    for t in rename.get(s,set()):
                        if t not in seen: seen.add(t); nxt.append(t)
                if not nxt: break
                frontier=nxt
                for t in frontier:
                    m=current_matches(t,isin)
                    if m: targets.append((t,m))
                if targets: break
            if len(targets)==1 and len(targets[0][1])==1:
                resolved=targets[0][0]; path.append(resolved); cats=[targets[0][1][0][0]]
                ev=targets[0][1][0][1]
                status="MATCHED_RENAMED_SYMBOL" if ev!="SYMBOL_MATCH_ISIN_CONFLICT" else "UNKNOWN_ISIN_CONFLICT"
                evidence=ev
            elif targets:
                status="UNKNOWN_AMBIGUOUS_RENAME_OR_CATEGORY"
                path.extend(sorted({t for t,_ in targets}))
                cats=sorted({m[0] for _,ms in targets for m in ms})
                evidence="MULTIPLE_RENAME_TARGETS_OR_CATEGORIES"
            else:
                status="UNKNOWN_NOT_IN_PROVIDED_SNAPSHOTS"; evidence="NO_DIRECT_OR_VERIFIED_RENAME_MATCH"
        rows.append({"OLD_SYMBOL":old,"ISIN":isin,"RESOLVED_SYMBOL":resolved if status.startswith("MATCHED_") else "",
                     "MATCHED_CATEGORIES":";".join(sorted(cats)),"STATUS":status,"MATCH_EVIDENCE":evidence,
                     "RENAME_PATH":"->".join(path)})
    out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    result=pd.DataFrame(rows).sort_values("OLD_SYMBOL")
    csvout=out/"nse_identity_reconciliation.csv"; result.to_csv(csvout,index=False)
    counts=result.STATUS.value_counts().sort_index().to_dict()
    report={"status":"PASS_RECONCILIATION_OUTPUT_WITH_UNKNOWNS" if not result.STATUS.str.startswith("UNKNOWN_").any() else "PARTIAL_EVIDENCE_RECONCILIATION_PASS_UNRESOLVED",
            "rows":len(result),"status_counts":counts,
            "policy":"Absence from supplied snapshots is UNKNOWN; it is not evidence of suspension, delisting, or ineligibility. No ranking, selector, score, CORE-672, or production gate is modified.",
            "inputs":{k:{"path":v,"sha256":sha256(v),"bytes":Path(v).stat().st_size} for k,v in inputs.items()},
            "output":{"path":str(csvout),"sha256":sha256(csvout),"bytes":csvout.stat().st_size}}
    (out/"nse_identity_reconciliation_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
