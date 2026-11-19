# GCR Daily FPI Endpoint Refinement + Brazil Gate — Continuation 71
Date: 2026-11-19 (Asia/Kolkata)
Research-only. No production admission.

## New official source finding
A fresh official-source discovery identified a distinct CDSL current-daily page:
https://www.cdslindia.com/eservices/publications/fiidaily
The page's indexed official snapshot displays "Daily Trends in FII / FPI Investments on 17-NOV-2026", with gross purchases, gross sales, net INR crore, net USD million and conversion rate, split by investment category and route. It explicitly distinguishes provisional exchange data from confirmed custodian/depository reports and describes RBI reference-rate conversion.
The official CDSL archive page independently displays daily investment data through 18-Nov-2026, but this archive/search rendering remains different from the current-daily endpoint date and prior direct-render conflict. Do not conflate reporting date, publication date, and indexed crawl date.
Official CDSL fortnightly sector page lists sector periods through 15-Nov-2026. It remains fortnightly; never daily-interpolate it.
SEBI official FPI directory lists NSDL Latest, Monthly, Archive, Yearwise and Fortnightly selector routes, confirming the route inventory.

## Engineering refinement
- Updated `scripts/research/capture_india_fpi_official_pages.py` to add:
  `https://www.cdslindia.com/eservices/publications/fiidaily`
- Script update commit: `4bf466a6542127bbd10bfce4e1ab052c8c3b98a7`
- Updated trigger marker to rerun the bounded capture with the new endpoint:
  `4bbb1bdc6be289079869a72c4ea79a460ac6b219`
- The original 6-minute workflow remains GET-only; script now targets seven pages. Existing paths-ignore already includes the script/workflow/trigger paths; no additional NSE collector change needed.
- Runtime workflow ID/conclusion/artifact still cannot be independently inspected with currently available GitHub Actions read functions in this session. Capture remains PENDING / NOT_VERIFIED. No source bytes/hashes are claimed.

## Interpretation and acceptance
- Official route discovery: PASS.
- CDSL current daily page snapshot through 17-Nov-2026: route and indexed page content observed; raw bytes still NOT_VERIFIED.
- CDSL archive snapshot through 18-Nov-2026: indexed archive content observed; prior direct-render conflict remains until byte-level capture.
- CDSL fortnightly sector dates through 15-Nov-2026: route/date listing observed; raw workbook schema/rows NOT_VERIFIED.
- NSDL raw page capture: PENDING.
- Seven-page raw capture artifact and SHA-256: PENDING / NOT_VERIFIED.
- Source-specific parser, historical coverage, date-level NSDL/CDSL/NSE reconciliation: NOT_DONE.
- GCR synchronized macro/benchmark panel, factor weights and OOS event study: BLOCKED / NOT_DONE.
- Brazil PA Changelog/transaction 2 and BOP6 vs BOP_BPM6 identity: BLOCKED; no repeated endpoint tests.
- Brazil registration 40-event lifecycle remains PASS.

## Brazil boundary
The official Provision Agreements UI statically exposes Changelog/Revisions/Compare/Export controls, but static page extraction does not select the exact Brazil PA row or return its history. Actual Brazil-specific export remains an owner-side UI evidence dependency. Do not claim the changelog is empty, unavailable, or authenticated-only without interacting with the selected record. Do not request credentials.

## Exact next action
1. Inspect the new seven-page capture workflow run and artifact when Actions read access is available.
2. Validate raw byte hashes against manifest, then parse the CDSL current-daily and archive tables independently.
3. Compare only matched reporting dates, dimensions, asset classes and provisional/confirmed status; preserve route and gross/net fields.
4. Use official PA GUI export for Brazil's exact URN and its Changelog/Revisions; reconcile its Dataflow/Provider/URL to existing 40-event registration evidence.
5. Keep all missing evidence BLOCKED/UNKNOWN; no production promotion.

## Invariants
₹0, free official sources only. No synthetic data, forward-fill, net-to-gross reconstruction, unapproved currency/scale/sign/BPM conversions or inferred timestamps. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
