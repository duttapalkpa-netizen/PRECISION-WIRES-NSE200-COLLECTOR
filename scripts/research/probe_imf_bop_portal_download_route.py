#!/usr/bin/env python3
"""Inspect public IMF BOP dataset page for actual View Data/Download route.

No login, cookies, API keys or guessed observation keys. Captures public HTML
and a bounded set of same-origin JS bundles, then inventories literal links,
forms, buttons and download-related endpoint strings.
"""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from html.parser import HTMLParser
from urllib.parse import urljoin,urlparse
import hashlib,json,re

BASE="https://data.imf.org"
PAGE=BASE+"/en/datasets/IMF.STA%3ABOP?sc_site=idata"
OUT=Path("imf_bop_portal_route_probe"); OUT.mkdir(parents=True,exist_ok=True)

class Scan(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]; self.scripts=[]; self.forms=[]; self.buttons=[]; self.metas=[]; self._button=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=="a": self.links.append({"href":a.get("href"),"text":""})
  if tag=="script" and a.get("src"): self.scripts.append(a["src"])
  if tag=="form": self.forms.append({"action":a.get("action"),"method":a.get("method")})
  if tag=="meta": self.metas.append({"name":a.get("name"),"property":a.get("property"),"content":a.get("content")})
  if tag in ("button","input"):
   self.buttons.append({"tag":tag,"type":a.get("type"),"id":a.get("id"),"name":a.get("name"),"value":a.get("value"),"aria_label":a.get("aria-label"),"data":{k:v for k,v in a.items() if k.startswith("data-")}})
 def handle_data(self,data):
  if self.links and data.strip() and self.links[-1].get("text") is not None: self.links[-1]["text"]+=data.strip()+" "

def fetch(url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-public-route-audit/1.0","Accept":"text/html,application/javascript,application/json,*/*"})
 try:
  with urlopen(req,timeout=30) as r: status=r.status; headers=dict(r.headers.items()); final=r.geturl(); body=r.read()
 except HTTPError as e: status=e.code; headers=dict(e.headers.items()) if e.headers else {}; final=e.geturl(); body=e.read()
 except (URLError,TimeoutError) as e: status=0; headers={}; final=url; body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 return {"requested_url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"body":body}

def main():
 p=fetch(PAGE); html=p["body"]; (OUT/"dataset_page.html").write_bytes(html)
 parser=Scan(); parser.feed(html.decode("utf-8","replace"))
 same=[]
 for src in parser.scripts:
  u=urljoin(PAGE,src)
  if urlparse(u).netloc==urlparse(BASE).netloc and u not in same: same.append(u)
 # Bound to first 12 same-origin bundles; record all discovered script URLs.
 bundles=[]
 for i,u in enumerate(same[:16]):
  r=fetch(u); b=r.pop("body"); name=f"bundle_{i:02d}.js"; (OUT/name).write_bytes(b)
  txt=b.decode("utf-8","replace")
  pats=sorted(set(re.findall(r"""[^"'\\s]{0,120}(?:download|export|view.?data|dataset|sdmx|odata)[^"'\\s]{0,180}""",txt,re.I)))
  bundles.append({**r,"file":name,"byte_count":len(b),"sha256":hashlib.sha256(b).hexdigest(),"candidate_strings":pats[:150]})
 # Inline HTML strings around route/action labels, preserving literal context.
 raw=html.decode("utf-8","replace")
 hits=[]
 for m in re.finditer(r"download|view data|export|odata|sdmx|api\.imf",raw,re.I):
  hits.append(raw[max(0,m.start()-180):min(len(raw),m.end()+300)])
 summary={"scope":"anonymous public page inspection only; no authentication",
  "page":{"requested_url":p["requested_url"],"final_url":p["final_url"],"retrieved_at_utc":p["retrieved_at_utc"],"http_status":p["http_status"],"headers":p["headers"],"byte_count":len(html),"sha256":hashlib.sha256(html).hexdigest()},
  "anchors":parser.links,"forms":parser.forms,"buttons":parser.buttons,"meta":parser.metas,
  "script_urls":same,"bundles":bundles,"inline_route_contexts":hits[:100],
  "conclusion":"No route is considered verified unless a literal public endpoint is identified and separately requested successfully."}
 (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,ensure_ascii=False))
 if p["http_status"]!=200: raise SystemExit("Dataset page did not return HTTP 200")
if __name__=="__main__": main()
