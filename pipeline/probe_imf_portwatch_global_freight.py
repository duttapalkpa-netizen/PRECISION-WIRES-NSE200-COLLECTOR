#!/usr/bin/env python3
"""Bounded, read-only IMF PortWatch source probe. No coverage promotion."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import requests

ROOT=Path("artifacts/global_freight_shipping_probe")
BASE="https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services"
LAYERS={
 "chokepoints":f"{BASE}/Daily_Chokepoints_Data/FeatureServer/0",
 "ports":f"{BASE}/Daily_Trade_Data/FeatureServer/0",
}
HEADERS={"User-Agent":"PRECISION-WIRES-research/1.0 (read-only source validation)",
         "Accept":"application/json"}

def sha(b): return hashlib.sha256(b).hexdigest()

def get_json(session,url,params=None):
    r=session.get(url,params=params,timeout=(8,25))
    r.raise_for_status()
    body=r.content
    if len(body)<2: raise ValueError("empty ArcGIS response")
    data=r.json()
    if "error" in data: raise ValueError(f"ArcGIS error: {data['error']}")
    return data,body,r.url,datetime.now(timezone.utc).isoformat()

def inspect_layer(session,name,url):
    meta,raw,final_url,observed=get_json(session,url,{"f":"pjson"})
    fields=[{"name":x.get("name"),"type":x.get("type"),"alias":x.get("alias")} for x in meta.get("fields",[])]
    field_names={x["name"].lower() for x in fields}
    if not {"date","portid"}.issubset(field_names):
        raise ValueError(f"{name}: required date/portid fields absent: {sorted(field_names)}")
    sample,raw_sample,sample_url,sample_observed=get_json(session,url+"/query",{
        "where":"1=1","outFields":"*","orderByFields":"date DESC",
        "resultRecordCount":5,"returnGeometry":"false","f":"json"})
    features=sample.get("features",[])
    if not features:
        raise ValueError(f"{name}: empty sample query")
    attrs=[x.get("attributes",{}) for x in features]
    if any(not a.get("date") or not a.get("portid") for a in attrs):
        raise ValueError(f"{name}: sample missing date/portid")
    return {
      "layer":name,"layer_url":url,"metadata_url":final_url,
      "metadata_http_status":200,"metadata_sha256":sha(raw),
      "metadata_retrieved_at_utc":observed,"object_id_field":meta.get("objectIdField"),
      "max_record_count":meta.get("maxRecordCount"),
      "capabilities":meta.get("advancedQueryCapabilities",{}),
      "fields":fields,"sample_query_url":sample_url,
      "sample_http_status":200,"sample_sha256":sha(raw_sample),
      "sample_retrieved_at_utc":sample_observed,"sample_rows":len(attrs),
      "sample_attributes":attrs,"sample_exceeded_transfer_limit":sample.get("exceededTransferLimit",False),
      "last_edit_date_epoch_ms":meta.get("editingInfo",{}).get("lastEditDate"),
      "status":"PASS_METADATA_AND_SAMPLE"
    }

def main():
    ROOT.mkdir(parents=True,exist_ok=True)
    s=requests.Session();s.headers.update(HEADERS)
    results=[]
    for name,url in LAYERS.items():
        results.append(inspect_layer(s,name,url))
    observed=datetime.now(timezone.utc).isoformat()
    report={
      "status":"PASS_SOURCE_PROBE_ONLY",
      "provider":"IMF PortWatch / UN Global Platform AIS-derived maritime activity",
      "provider_home":"https://portwatch.imf.org/",
      "official_methodology":"https://www.imf.org/en/publications/wp/issues/2025/05/02/nowcasting-global-trade-from-space-566971",
      "observed_at_utc":observed,"layers":results,
      "promotion_allowed":False,
      "limitations":[
       "This probe verifies public ArcGIS layer metadata and sample accessibility only; it does not establish historical completeness or source freshness.",
       "AIS-derived port calls and chokepoint transits are shipping-activity proxies, not market freight-rate quotations.",
       "AIS coverage gaps, missing transmissions, revisions and chokepoint observation limitations must be audited before any coverage promotion.",
       "No paid freight-rate feeds, API keys or subscriptions are used."
      ]
    }
    (ROOT/"probe_report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps({"status":report["status"],"layers":[{"name":x["layer"],"fields":len(x["fields"]),"sample_rows":x["sample_rows"],"max_record_count":x["max_record_count"]} for x in results],"promotion_allowed":False},indent=2))
if __name__=="__main__": main()
