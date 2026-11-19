#!/usr/bin/env python3
"""No-credential IMF BOP public-route probe.

Only tests documented landing pages and SDMX metadata discovery routes. It does
not send API keys, cookies, guessed observation keys or user credentials. A
data endpoint is not queried until DSD dimensions and valid codelists are
independently established.
"""
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
from urllib.parse import urlparse
import hashlib,json,re,xml.etree.ElementTree as ET

OUT=Path("imf_bop_public_route_probe"); OUT.mkdir(exist_ok=True)
URLS=[
 ("official_bop_dataset","https://data.imf.org/en/datasets/IMF.STA:BOP","text/html"),
 ("official_bop_aggregate_dataset","https://data.imf.org/en/datasets/IMF.STA:BOP_AGG","text/html"),
 ("official_imf_api_docs","https://data.imf.org/en/Resource-Pages/IMF-API","text/html"),
 ("sdmxcentral_bop_dataflow_v2","https://sdmxcentral.imf.org/sdmx/v2/structure/dataflow/IMF.STA/BOP/21.0.0?references=all","application/vnd.sdmx.structure+xml"),
 ("api_imf_bop_dataflow_v3","https://api.imf.org/external/sdmx/3.0/structure/dataflow/IMF.STA/BOP/21.0.0?references=all","application/vnd.sdmx.structure+xml"),\n ("api_imf_bop_dsd_v3","https://api.imf.org/external/sdmx/3.0/structure/datastructure/IMF.STA/DSD_BOP/24.0.0?references=all","application/vnd.sdmx.structure+xml"),
 ("sdmxcentral_bop_agg_dataflow_v2","https://sdmxcentral.imf.org/sdmx/v2/structure/dataflow/IMF.STA/BOP_AGG/1.0?references=all","application/vnd.sdmx.structure+xml"),
 ("api_imf_bop_agg_dataflow_v3","https://api.imf.org/external/sdmx/3.0/structure/dataflow/IMF.STA/BOP_AGG/+/","application/vnd.sdmx.structure+xml"),
]
def sha(b): return hashlib.sha256(b).hexdigest()
results=[]
for name,url,accept in URLS:
    ts=datetime.now(timezone.utc).isoformat()
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-IMF-public-route-audit/1.0","Accept":accept+", application/xml, text/xml, text/html, */*"})
    try:
        with urlopen(req,timeout=35) as r:
            status=r.status; final=r.geturl(); headers=dict(r.headers.items()); body=r.read()
    except HTTPError as e:
        status=e.code; final=e.geturl(); headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
    except (URLError,TimeoutError) as e:
        status=0; final=url; headers={}; body=str(e).encode()
    safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
    ext="html" if "html" in (safe.get("Content-Type","").lower()) or "dataset" in name or "docs" in name else "xml"
    fn=name+"."+ext; (OUT/fn).write_bytes(body)
    row={"name":name,"requested_url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,
         "headers":safe,"byte_count":len(body),"sha256":sha(body),"file":fn}
    if status==200 and ext=="xml":
        try:
            root=ET.fromstring(body); row["xml_parse"]="PASS"; row["xml_root"]=root.tag
            local=lambda t:t.split("}")[-1]
            row["dataflows"]=[]
            for el in root.iter():
                if local(el.tag)=="Dataflow":
                    row["dataflows"].append({"attributes":el.attrib,
                      "name":" ".join((x.text or "") for x in el if local(x.tag)=="Name"),
                      "structure_refs":[x.attrib for x in el.iter() if local(x.tag)=="Ref"]})
            row["dimension_names"]=sorted({el.attrib.get("id") for el in root.iter() if local(el.tag)=="Dimension" and el.attrib.get("id")})
        except Exception as e: row["xml_parse"]="FAIL"; row["parse_error"]=str(e)
    if status==200 and ext=="html":
        txt=body.decode("utf-8","replace")
        row["html_title"]=(re.search(r"<title[^>]*>(.*?)</title>",txt,re.I|re.S).group(1).strip() if re.search(r"<title[^>]*>(.*?)</title>",txt,re.I|re.S) else None)
        row["hrefs"]=re.findall(r'''href=["']([^"'#]+)["']''',txt,re.I)[:200]
        row["script_srcs"]=re.findall(r'''<script[^>]+src=["']([^"']+)["']''',txt,re.I)[:100]
        row["contains_download_label"]="DOWNLOAD" in txt.upper()
        row["contains_view_data_label"]="VIEW DATA" in txt.upper()
    results.append(row)
(OUT/"manifest.json").write_text(json.dumps({"scope":"public no-credential IMF BOP landing-page and SDMX metadata route probe; no observations queried","responses":results},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(results,indent=2,ensure_ascii=False))
