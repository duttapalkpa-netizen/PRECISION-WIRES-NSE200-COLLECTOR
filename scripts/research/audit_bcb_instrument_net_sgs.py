#!/usr/bin/env python3
"""Audit BCB instrument-level net series against seven parent SGS series."""
from __future__ import annotations
import argparse, csv, hashlib, json
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

CHILD_CODES=("22909","22912","22915","22927","22936","22939","22942","22945")
PARENT_CODES=("22905","22906","22907","22908","22924","22925","22926")
START,END=(1995,1),(2026,9)

def parse_value(s):
    s=s.strip().strip('"').strip()
    if not s: raise ValueError("empty numeric value")
    return Decimal(s.replace(".","").replace(",", "."))

def months_expected():
    y,m=START; out=[]
    while (y,m)<=END:
        out.append(date(y,m,1)); m+=1
        if m==13:y,m=y+1,1
    return out

def load_series(root,code,manifest=None):
    p=root/f"sgs_{code}.csv"; raw=p.read_bytes()
    if manifest:
        meta=manifest["series"][code]
        if len(raw)!=meta["byte_length"] or hashlib.sha256(raw).hexdigest()!=meta["sha256"]:
            raise ValueError(f"{code}: manifest byte/hash mismatch")
    out={}
    with p.open(encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f,delimiter=";")
        if reader.fieldnames != ["data","valor"]: raise ValueError(f"{code}: unexpected header {reader.fieldnames}")
        for r in reader:
            d=datetime.strptime(r["data"].strip().strip('"'),"%d/%m/%Y").date()
            if d in out: raise ValueError(f"{code}: duplicate date {d}")
            if d.day!=1: raise ValueError(f"{code}: non-month-start date {d}")
            out[d]=parse_value(r["valor"])
    ds=sorted(out)
    if ds!=months_expected(): raise ValueError(f"{code}: missing/extra monthly coverage")
    return out,{"byte_length":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"rows":len(out),"first_date":ds[0].isoformat(),"last_date":ds[-1].isoformat()}

def audit(child_root:Path,parent_root:Path):
    cm=json.loads((child_root/"manifest.json").read_text(encoding="utf-8"))
    pm=json.loads((parent_root/"manifest.json").read_text(encoding="utf-8"))
    if cm.get("status")!="RAW_CAPTURE_8_OF_8_PASS": raise ValueError("child manifest not 8/8 PASS")
    if pm.get("status")!="RAW_CAPTURE_7_OF_7_PASS": raise ValueError("parent manifest not 7/7 PASS")
    series={}; metadata={}
    for code in CHILD_CODES: series[code],metadata[code]=load_series(child_root,code,cm)
    for code in PARENT_CODES: series[code],metadata[code]=load_series(parent_root,code,pm)
    common=sorted(set.intersection(*(set(x) for x in series.values())))
    identities=[
      ("asset_instrument_net_sum","22906",("22909","22912","22915")),
      ("liability_instrument_net_sum","22924",("22927","22936","22939")),
      ("liability_debt_domestic_external_split","22939",("22942","22945")),
    ]
    diagnostics={}
    for name,target,components in identities:
        diffs=[series[target][d]-sum((series[c][d] for c in components),Decimal(0)) for d in common]
        diagnostics[name]={
          "target":target,"components":list(components),"observations_tested":len(diffs),
          "exact_matches":sum(x==0 for x in diffs),
          "within_plus_minus_0_1":sum(abs(x)<=Decimal("0.1") for x in diffs),
          "greater_than_0_1":sum(abs(x)>Decimal("0.1") for x in diffs),
          "max_absolute_difference":str(max(abs(x) for x in diffs)),
          "difference_counts":{str(x):diffs.count(x) for x in sorted(set(diffs))},
          "status":"ROUNDING_CONSISTENT_NOT_FORMAL_PASS"
        }
    return {
      "schema_version":1,"purpose":"research_only_bcb_instrument_net_reconciliation",
      "child_manifest_status":cm["status"],"parent_manifest_status":pm["status"],
      "common_months":len(common),"first_date":common[0].isoformat(),"last_date":common[-1].isoformat(),
      "series":metadata,"identity_diagnostics":diagnostics,
      "rounding_tolerance_formally_approved":False,
      "instrument_sum_reconciliation":"PARTIAL_EMPIRICAL_ALIGNMENT",
      "country_period_qa":"NOT_DONE","brazil_pilot_acceptance":"NOT_ACCEPTED",
      "em_wide_panel":"NOT_DONE","production_integration":"NOT_AUTHORIZED","errors":[]
    }

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--child-root",type=Path,default=Path("data/raw/bcb/instrument_net_capture_20261117"))
    ap.add_argument("--parent-root",type=Path,default=Path("data/raw/bcb/priority_series_capture_20261117"))
    ap.add_argument("--output",type=Path,default=Path("bcb_instrument_net_capture/qa_report.json"))
    args=ap.parse_args()
    result=audit(args.child_root,args.parent_root)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
    print(json.dumps(result,indent=2,sort_keys=True))
