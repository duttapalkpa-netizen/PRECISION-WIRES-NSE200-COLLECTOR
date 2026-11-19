#!/usr/bin/env python3
"""Anonymous browser probe of official IMF BOP dataset View Data / Download controls.

No login, cookies, credentials, or session tokens are supplied. Captures only
public UI state and public response metadata; downloads are saved if the portal
offers a direct anonymous file.
"""
import asyncio,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from playwright.async_api import async_playwright

URL="https://data.imf.org/en/datasets/IMF.STA%3ABOP?sc_site=idata"
OUT=Path("imf_bop_browser_route_probe"); OUT.mkdir(parents=True,exist_ok=True)
events=[]
def now(): return datetime.now(timezone.utc).isoformat()
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True)
  page=await browser.new_page(accept_downloads=True)
  page.set_default_timeout(15000)
  async def on_response(resp):
   try:
    u=resp.url
    if "data.imf.org" in u or "api.imf.org" in u:
     h=await resp.all_headers()
     events.append({"time_utc":now(),"url":u,"status":resp.status,
       "content_type":h.get("content-type"),"content_length":h.get("content-length"),
       "resource_type":resp.request.resource_type})
   except Exception as e: events.append({"response_event_error":str(e)})
  page.on("response",on_response)
  start=now()
  response=await page.goto(URL,wait_until="domcontentloaded",timeout=60000)
  await page.wait_for_timeout(8000)
  initial={"retrieved_at_utc":start,"requested_url":URL,"final_url":page.url,
   "http_status":response.status if response else None,"title":await page.title()}
  async def snapshot(label):
   return {"label":label,"url":page.url,
    "body_text":(await page.locator("body").inner_text())[:30000],
    "buttons":await page.locator("button").evaluate_all("(xs)=>xs.map(x=>({text:(x.innerText||'').trim(),aria:x.getAttribute('aria-label'),disabled:x.disabled,outer:x.outerHTML.slice(0,500)}))"),
    "links":await page.locator("a").evaluate_all("(xs)=>xs.map(x=>({text:(x.innerText||'').trim(),href:x.href,download:x.getAttribute('download')})).filter(x=>x.text||x.download)")}
  states=[await snapshot("initial")]
  for label in ["VIEW DATA","DOWNLOAD"]:
   loc=page.get_by_text(label,exact=True)
   count=await loc.count()
   action={"label":label,"matches":count}
   if count:
    try:
     async with page.expect_download(timeout=12000) as dl:
      await loc.first.click()
      await page.wait_for_timeout(2000)
     download=await dl.value
     suggested=download.suggested_filename
     dest=OUT/(label.lower().replace(" ","_")+"_"+suggested)
     await download.save_as(dest)
     b=dest.read_bytes()
     action.update({"result":"downloaded","suggested_filename":suggested,"file":dest.name,"byte_count":len(b),"sha256":hashlib.sha256(b).hexdigest()})
    except Exception as e:
     action.update({"click_result":"no_browser_download_event","detail":str(e)[:800]})
    await page.wait_for_timeout(4000)
    action["final_url"]=page.url
    states.append(await snapshot(label))
   else:
    action["result"]="exact_text_control_not_found"
   events.append({"action":action})
  (OUT/"ui_states.json").write_text(json.dumps(states,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
  manifest={"scope":"anonymous public browser interaction only; no authentication","initial":initial,
   "actions_and_responses":events,"ui_states_file":"ui_states.json",
   "downloads":[x for x in events if x.get("action",{}).get("result")=="downloaded"],
   "response_event_count":sum(1 for x in events if "status" in x),
   "response_events":[x for x in events if "status" in x]}
  (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
  print(json.dumps(manifest,indent=2,ensure_ascii=False))
  await browser.close()
if __name__=="__main__": asyncio.run(main())
