# GCR CDSL 15-Nov-2026 Sector Report Capture Continuation 73
Date: 2026-11-19

## Objective
Capture the exact dated CDSL fortnightly sector-wise FPI report rather than treating the generic landing page/DDP pendency tables as sector observations.

## Official source discovery
- Landing page: https://www.cdslindia.com/Publications/ForeignPortInvestor.html
- Exact dated report: https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Nov%2015%202026.html
- The dated report is directly accessible as an official CDSL HTML page (web inspection ref turn900033view0).
- Header explicitly separates:
  1. AUC as on 31-Oct-2026
  2. Net Investment 16-Oct to 31-Oct-2026
  3. Net Investment 01-Nov to 15-Nov-2026
  4. AUC as on 15-Nov-2026
- Values are separated by asset/route dimensions including Equity, Debt General Limit, Debt VRR, Debt-FAR, Hybrid, Mutual Funds (Solution oriented/Other), and AIF; INR crore and USD million are separately labelled.
- Sector rows include Automobile and Auto Components, Capital Goods, Chemicals, Construction, Construction Materials, Consumer Durables, Consumer Services, Diversified, FMCG, Financial Services, Forest Materials, Healthcare, Information Technology, Media/Entertainment/Publication, Metals & Mining, Oil/Gas/Consumable Fuels, Power, etc.
- Example visible values (retain source's exact labels): Metals & Mining, 01-Nov–15-Nov net investment: Equity INR -904 crore / USD -95m; 15-Nov AUC Equity INR 2,75,253 crore / USD 29,220m. These are sector/asset-class observations, not daily cash flow.
- Do not collapse the fortnightly period into daily observations, and do not mix AUC stock with net-investment flow.

## Code and workflow
- Added exact dated report URL as an additional GET-only source in `scripts/research/capture_india_fpi_official_pages.py`.
- Script commit: `0c4a2115b38c4b70eda0fb404858f57dea35d159`.
- Updated existing research trigger marker only after script commit: `abb848a203bd21d0be03fd8eaa2362edc8028953`.
- Existing workflow: `.github/workflows/gcr_india_fpi_raw_capture.yml`, timeout 6 minutes; no POST/form submission/credentials/production ingestion.
- Triggered run ID `44519322726`; at report preparation, run status was `in_progress`, capture step in progress, artifact pending. Runtime/artifact status therefore PENDING, not PASS.

## India FPI evidence status
- Previous seven-page capture: run `44515445620` SUCCESS; artifact `14524707532`; 7/7 HTTP 200; artifact SHA-256 `29530f3d0913f3eed93afbeb0759ecb8131b4192c71e5928d79961df77c24c69`.
- Previous schema finding: CDSL eServices cash table displayed 18-Nov-2026; CDSL archive cash rows started 02-Nov despite derivative table reaching 18-Nov; NSDL Latest heading/data included 19-Nov and explicit provisional-vs-confirmed caveat; NSDL archive GET required ASP.NET interaction not attempted.
- New exact sector page discovery: schema/date periods DOCUMENTED; raw artifact PENDING.
- Matched-date NSDL/CDSL confirmed-flow reconciliation NOT_DONE.
- Sector observations captured/hashed NOT_DONE until run artifact verification.
- India production ingestion BLOCKED.

## Brazil Reconstruction status (unchanged)
- IMF Registration lifecycle 40/40 PASS (history events, ZIPs and embedded SDMX-ML reconciled).
- PA transaction-2 Changelog remains BLOCKED after known HTTP 500 responses; do not repeat.
- BOP6 vs BOP_BPM6 identity mismatch remains BLOCKED; no alias/rewrite/admission.
- Exact PA owner-side GUI/export evidence remains an external dependency. No credentials requested or stored.
- No new Brazil evidence claimed in this continuation.

## Acceptance / invariants
- This continuation does not claim either GCR or Brazil 100% complete.
- UNKNOWN is never PASS. No synthetic data, interpolation, inferred gross legs, unapproved conversion or alias.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E unchanged.
- Research spend ₹0; no paid APIs.
- Next: verify run `44519322726` and artifact/hash; then parse raw dated report schema and independently reconcile matched dates/periods. Brazil next action remains obtain exact PA changelog through the official UI/export route or mark the external dependency explicitly.


## Runtime verification addendum
- Actions run `44519322726` completed SUCCESS at `2026-11-19T11:57:17Z`; capture job and artifact upload steps SUCCESS.
- Artifact ID `14527092174`, name `gcr-india-fpi-raw-pages-3`, 196,057 bytes.
- GitHub artifact digest and independently recomputed ZIP SHA-256 match: `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd`.
- Manifest summary: 8 sources, 8 HTTP 200, zero non-200/error.
- Exact dated sector report body: 327,522 bytes; SHA-256 `3f77f3896a95b8cff3a7728049127493814e1b503eb39dcb75b0e8fe145cf84e`; final URL exact; retrieval UTC `2026-11-19T11:57:11.677237+00:00`; Last-Modified header `Wed, 18 Nov 2026 15:21:02 GMT`.
- Parsed HTML structure: main sector table 29 rows (3 header rows, 24 numbered sector/category rows, grand total); separate notes, company AUC table, conversion-rate table and classification note. Raw HTML retained; parsed table remains research-only pending independent QA and reconciliation.
- The page notes RBI reference rate for INR/USD conversion. Conversion rates shown by period include 95.2492 for 31-Oct AUC and 94.1997 for 15-Nov AUC; do not apply one period's rate to another.
- Acceptance updated: exact dated page raw capture PASS; raw schema inventory PASS; independent arithmetic/reconciliation and mapping to daily flow NOT_DONE.
