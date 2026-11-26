# GCR Continuation 268 — FBIL USD/INR public reference-rate archive/export boundary
Date: 2026-11-26

## Preflight
- Re-read current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, immutable 63-country matrix, C267 progress-baseline reconciliation, and Library Mother File addenda 55–57.
- C267 established the next unfinished programme item as Milestone 6 (Global Macro Data Ingestion). Existing RBI/FBIL route checks and NSDL terms boundary were reviewed; this task was limited to a fresh official FBIL public-site and methodology inspection, not a retry of RBI form submission, NSDL archive automation, or prior failed export calls.
- No IMF query, cohort rebuild, paid service, workflow dispatch, or production change.

## Official FBIL evidence
1. FBIL official homepage: https://www.fbil.org.in/
   - The publicly indexed homepage exposes a Reference Rates table with INR/1 USD entries. Search-rendered rows included 16-Oct-2026 at 1:00 PM (INR 95.0194 per USD) and 15-Oct-2026 (INR 95.0691), plus another recent pair dated 06-Nov/05-Nov at 4:00 PM (93.9234/94.4776). These are displayed public rows, not a verified complete daily archive or Q2 historical export.
   - Homepage retrieval through the browser text reader returned no readable lines; search rendering showed tables but did not expose a documented historical API/export route, request schema, complete date range, or downloadable raw payload. No raw bytes or SHA-256 captured.
   - Homepage also displays a “TERMS OF USE AND SUBSCRIPTION DISCLAIMER FOR FBIL BENCHMARKS” notice. The actual terms content was not retrieved/parsed in this task, so reuse/archival permission is NOT_ESTABLISHED.
2. FBIL Reference Rate Methodology (Version 1, 11-Jun-2018):
   https://www.fbil.org.in/uploads/Methodology_Document_on_Reference_Rate_Dated_11th_June2018_Version1_6db1a143aa.pdf
   - Official method: USD/INR based on actual spot USD/INR transactions on electronic platforms during 11:30–12:30 Mumbai business-day window; normally Thomson Reuters and CCIL sources (PDF lines 18–24).
   - A randomly selected 15-minute slice is used; threshold is 10 transactions and aggregate USD25m; +/-3SD outlier filter and volume-weighted average (lines 27–34).
   - Fallback can use bank polled submissions if transaction data unavailable (lines 35–50).
   - Published around 13:30 on Mumbai business days from 10-Jul-2018 (lines 52–58).
   - This is a benchmark observation, not intraday OHLC, DXY, or a cross-currency carry series. Preserve methodology/version and any fallback/revision semantics if a raw archive becomes available.
3. NSE / SEBI data-sharing list:
   https://nsearchives.nseindia.com/web/sites/default/files/inline-files/Data%20list%20under%20NSE%20Data%20Sharing%20Policy%20for%20Research%20and%20Analysis_20250728.pdf
   - NSE list places FII/FPI and DII trading activity under first-basket research data (PDF lines 1–4, 50–52), while voluminous datasets above 2GB are separately identified as chargeable (lines 230–240).
   - NSE research data access page says research-oriented access is limited to academic/non-commercial use and restricted to accredited academic institutions, recognized research organizations and think tanks; request form route is stated (https://betanseapi.nseindia.com/static/research/initiatives-data-for-research). No eligibility or access is assumed for this project. This is a potential permission/eligibility check only, not data capture or a substitute for final depository FPI.
   - NSE FII/FPI/DII exchange trading activity remains a separately labelled provisional exchange series; it must not be substituted for final depository FPI investment flow.
   
## Acceptance
- FBIL USD/INR source identity and benchmark methodology: CONFIRMED.
- Public reference-rate rows visible: DISCOVERED.
- Complete historical daily archive/export endpoint and schema: NOT_VERIFIED.
- Q2/required-period raw daily observations and provenance receipt: NOT_CAPTURED.
- Raw bytes / SHA-256: NOT_CAPTURED.
- Terms/reuse/archival permission: NOT_ESTABLISHED.
- USD/INR macro P0 source group remains BLOCKED / UNKNOWN; no promotion to AVAILABLE.
- FPI/DII remains separately blocked/insufficient pending permitted raw history and source qualification.
- No collector mapping, parser, fixture, or source-coverage status changed; no workflow was run.

## Next action
Reopen only if FBIL publishes a documented public historical export/API with an explicit date range, schema and permissible internal archival terms, or provides written permission/documented access. If NSE research-data route is considered, first establish that the project/user qualifies under the official eligibility terms and obtain the applicable access permission; do not assume. Only after lawful, permitted raw capture with date, publication time, units, source URL, schema, vintage and SHA-256 should collector mapping and regression fixtures be considered.

## Invariants
₹0 spend; official/free sources only; no paid API, no reverse engineering, no untrusted mirrors, no fabricated or synthetic rows, no interpolation/forward-fill; UNKNOWN never PASS; daily FPI/DII coverage gate remains >=60 distinct dates spanning >=90 calendar days; H+3 minimum 50 matured observations per State; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; no merge, workflow dispatch or production integration without explicit approval.
