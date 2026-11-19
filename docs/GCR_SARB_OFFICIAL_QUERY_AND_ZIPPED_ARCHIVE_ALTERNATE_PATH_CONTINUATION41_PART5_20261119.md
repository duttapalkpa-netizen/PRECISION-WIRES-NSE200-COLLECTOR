# GCR South Africa — Official SARB query workflow and alternate BOP archive path
Date: 2026-11-19
Continuation: 41, Part-5
Scope: resolve Part-4 archive timeout by documenting the official interactive query path and a second official BOP archive route. No series values or national validation claimed.

## Progress log
- Reused Part-4 candidate KBP codes; did not re-derive the cohort.
- Freshly rechecked SARB's official Online Statistical Query page. It explicitly supports numeric KBP-code entry (the KBP prefix is added automatically), wildcard searches, version selection, frequency/date-range selection, and export to Excel/CSV/PDF/DOC.
- This confirms a public official retrieval workflow but the page is a multi-step interactive interface; the web retrieval view does not execute its controls or return the requested KBP series results. The live page open also timed out. Therefore no claim that KBP5756–5759 were accepted, found, or exported.
- Found a second official SARB archive index for zipped data files (published 2026-09-29). It lists KBP5-BOPD-Sep-20.zip alongside other Quarterly Bulletin data archives. The listing alone does not prove this file contains the exact KBP series values/metadata for Q2-2026; it is an alternate official artifact to inspect, not a validated substitute.
- Official September 2026 Quarterly Bulletin listing confirms the issue date 29-09-2026 and provides access to the issue and its data archive pages.

## Official sources
1. SARB Online Statistical Query: https://www.resbank.co.za/en/home/what-we-do/statistics/releases/online-statistical-query
   - Step 1 accepts numeric KBP code; prefix is added automatically; wildcard is supported.
   - Steps 2–3 expose available series versions; step 4 date/frequency options; step 5 shows unit and description and exports CSV/XLSX/PDF/DOC.
2. SARB zipped-data archive index, published 2026-09-29:
   https://www.resbank.co.za/en/home/publications/publication-detail-pages/quarterly-bulletins/download-information-from-zipped-data-files/2026/Downloadinformationfromzippeddatafiles1
   - Lists KBP5-BOPD-Sep-20.zip as an official attachment. Its internal content and coverage are not yet inspected.
3. SARB Quarterly Bulletin index:
   https://www.sarb.co.za/en/home/what-we-do/statistics/QuarterlyBulletins
   - September 2026 bulletin published 29-09-2026.
4. Prior candidate discovery (secondary only): https://dataguide.beranalytics.co.za/datasets/sarb/chapters/quarterly/balance_of_payments.html
   - Candidate codes KBP5756–KBP5759 remain unverified in SARB's own series catalogue.

## Gate assessment
- Official query workflow documented: PASS (workflow existence only).
- KBP5756–5759 official code/description/version/unit verification: NOT_DONE.
- Official query result/export bytes: NOT_OBTAINED.
- Alternate official zipped BOP archive identified: PASS (listing only).
- Archive internal content and Q2-2026 coverage: NOT_DONE.
- ZAF national source gate: PARTIAL / NOT PASS.
- GCR aggregate: NOT_AUTHORIZED.

## Exact next action
Use an authorized ordinary public browser session (no login/credentials expected) to enter numeric codes 5756, 5757, 5758, 5759 individually, inspect all available versions and select the version corresponding to the September 2026 vintage; export CSV/XLSX for Q2-2026 and record file bytes/SHA-256. In parallel inspect the official KBP5-BOPD-Sep-20.zip attachment only to establish its actual vintage and contents; do not assume its abbreviated filename means September 2026. Compare component asset and liability lines to IMF only after source descriptions, units, sign conventions, and period are matched. If UI interaction or download is unavailable, preserve PARTIAL and do not request credentials.

## Invariants
₹0; free official sources only for acceptance. Secondary sources are discovery leads only. No inferred sign/scale conversion, no net-to-gross substitution, no stock/flow substitution, no aggregate. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
