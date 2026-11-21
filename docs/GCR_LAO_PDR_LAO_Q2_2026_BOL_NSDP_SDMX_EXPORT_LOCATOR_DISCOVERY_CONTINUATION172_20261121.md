# Lao PDR LAO — Q2-2026 BOL NSDP / SDMX export locator discovery (Continuation 172)
Date: 2026-11-21 (Asia/Kolkata)
Status: CONTINUITY PREFLIGHT PASS; NEW OFFICIAL NSDP BOP DOWNLOAD LOCATORS DISCOVERED (XLSX + SDMX XML); IMF DSBB METADATA ROUTE CONFIRMED; BOL DOWNLOAD ATTEMPTS TIMED OUT (HTTP 400 TIMEOUT); NO RAW BYTES / OBSERVATIONS / SHA-256; Q2-2026 PORTFOLIO DUAL LEGS NOT_VERIFIED; LAO PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `172478d7dd9d9a0ebe32d65f4756f20ea7c204bc`.
- Re-fetched GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `553ba88c614c9624bae9c62f3037f1bcc515846b`.
- Re-fetched Historical Task Registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`, pre-task blob SHA `34659e2bddc47efd78773c51bb13bd8e1d395f21`.
- Re-fetched Continuation 171 LAO report: `docs/GCR_LAO_PDR_LAO_Q2_2026_BOL_OFFICIAL_BOP_DUAL_LEG_SOURCE_BOUNDARY_CONTINUATION171_20261121.md`, blob SHA `0d4df2a646242b9ccfb6a2a1e5047c56d124797e`.
- Reused immutable cohort `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`. Exact LAO row: A_NFA_T_PRESENT, L_NIL_T_PRESENT, BOTH_LEGS_PRESENT_IN_IMF_PANEL, NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING, NOT_AUTHORIZED.
- No cohort rebuild, IMF re-query or new IMF raw extraction.

## 2. New official NSDP discovery — exact BOP export locators
- Official Lao PDR National Summary Data Page (NSDP), hosted by Lao Statistics Bureau: https://www.lsb.gov.la/lsb-en.htm .
- The page explicitly lists “Balance of Payments” with three separate links: Browse Data, Download in SDMX, and DSBB Metadata. The links were followed from the official NSDP page (not inferred from naming).
- Exact official BOL XLSX download URL exposed by the Browse Data link: https://www.bol.gov.la/statistics/BOP6_Lao%20PDR.xlsx .
- Exact official BOL SDMX XML download URL exposed by the Download in SDMX link: https://www.bol.gov.la/statistics2/BOP6_Lao%20PDR.xml .
- Exact IMF DSBB metadata route exposed by the Metadata link: https://dsbb.imf.org/egdds/dqaf-base/country/LAO/category/BOP00 .
- This resolves the key gap from Continuation 171: actual XLSX and XML locators are now known. It does NOT prove the files contain Q2-2026 or portfolio asset/liability rows.

## 3. Retrieval test and evidence boundary
- Web click on the official NSDP Browse Data link resolved to the exact BOL XLSX URL but returned HTTP 400 “Timeout fetching”.
- Web click on the official NSDP Download in SDMX link resolved to the exact BOL XML URL but returned HTTP 400 “Timeout fetching”.
- A separate container-side direct HTTP request to the official BOL External Sector Statistics page failed at DNS resolution in this execution environment; no HTTP response or bytes were received. This is an environment retrieval failure, not a source-side HTTP status.
- The DSBB metadata link resolved to the official IMF DSBB page. The opened page exposed a general DSBB shell but did not render the country-specific metadata fields in the extracted view. No specific LAO periodicity, timeliness, methodology, or vintage claim is newly accepted from that view.
- No XLSX/XML raw bytes, workbook sheets, XML series keys, period observations, response headers, content length, byte count, or SHA-256 captured.
- Do not repeatedly retry these identical XLSX/XML URLs through the same timed-out fetch path. Reopen only through a genuinely different supported byte-transfer capability or a distinct official mirror/export.

## 4. Historical layout evidence remains historical only
- Official BOL Annual Economic Report 2023 Table 13: https://www.bol.gov.la/en/fileupload/28-06-2024_1719576615.pdf .
- It historically presents portfolio investment net, assets and liabilities separately, in millions of USD; this is schema/layout evidence only and not Q2-2026 observation evidence.
- Historical Q4/2016 BOL report showed a net-only portfolio row, so current XLSX/XML layout must be inspected and not presumed.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| LAO immutable Q2-2026 cohort membership | PASS |
| Prior Continuation 171 re-fetched | PASS |
| Official Lao NSDP Balance of Payments page | PASS |
| Exact official BOL XLSX download locator | PASS |
| Exact official BOL SDMX XML download locator | PASS |
| Official IMF DSBB metadata link locator | PASS |
| XLSX raw bytes / response metadata / SHA-256 | NOT_CAPTURED (HTTP 400 timeout) |
| SDMX XML raw bytes / response metadata / SHA-256 | NOT_CAPTURED (HTTP 400 timeout) |
| Q2-2026 period present in file | NOT_VERIFIED |
| Q2-2026 portfolio assets transaction leg | NOT_VERIFIED |
| Q2-2026 portfolio liabilities transaction leg | NOT_VERIFIED |
| Sign, units, BPM6 classification, revision vintage | NOT_ESTABLISHED |
| Comparison to archived IMF exact rows | NOT_DONE |
| LAO full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 6. Rejected list
- Do not mark source-data validation PASS merely because official XLSX/XML URLs are resolved.
- Do not treat a timeout as evidence that the files are empty, absent, or not published.
- Do not use 2023 annual portfolio asset/liability figures as Q2-2026 values.
- Do not back-solve legs from a net balance, use IIP stocks, annual/H1 values, or IMF-only rows as national Q2 transaction evidence.
- Do not repeat the identical timed-out downloads absent a genuinely new retrieval path.

## 7. Next exact action
1. Retrieve the exact official XLSX or XML bytes through a distinct supported public byte-transfer route; preserve exact URL, retrieval timestamp, HTTP status, content type, byte count and SHA-256.
2. Inspect the XLSX sheets or SDMX XML structure for time period Q2-2026, BPM6 portfolio investment, financial assets and liabilities separately, units and sign convention.
3. Confirm release/revision vintage and metadata before numeric comparison.
4. Only after national observations are captured, reuse archived IMF LAO Q2 rows and reconcile the two legs independently.
5. If no distinct transfer route is available, retain LAO PARTIAL / NOT PASS and advance to another unvalidated fixed-cohort member after a full preflight.

## 8. Protected invariants
No production code/configuration, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, gates or alerts changed. No IMF re-query, cohort rebuild, paid API, synthetic data, fabricated timestamp, unsupported sign/scale/FX conversion, stock-as-flow substitution or relaxation of acceptance criteria. Research spend ₹0. UNKNOWN is never PASS.
