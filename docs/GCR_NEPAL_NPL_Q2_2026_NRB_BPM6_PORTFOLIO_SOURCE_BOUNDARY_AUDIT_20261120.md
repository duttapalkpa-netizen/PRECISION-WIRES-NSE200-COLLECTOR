# Nepal (NPL) Q2-2026 NRB BPM6 Portfolio Source-Boundary Audit
Date: 2026-11-20
Status: PARTIAL / NOT PASS — official monthly source route identified; workbook bytes and portfolio legs not inspected.

## Scope and continuity
- NPL belongs to the fixed 63-country synchronous dual-leg Q2-2026 cohort. No cohort rebuild.
- GitHub repository search for a dedicated NPL Q2-2026 national portfolio reconciliation returned no matching dedicated report in the current search.
- Reuse the existing IMF archive only; no IMF re-query. Exact NPL raw rows were not extracted in this bounded source-boundary step.

## Official NRB source routes
1. NRB External Sector database: https://www.nrb.org.np/database-on-nepalese-economy/external-sector/ . Official page explicitly lists Monthly Balance of Payments (BPM 6) and BPM 5, plus yearly datasets.
2. NRB National Summary Data Page: https://www.nrb.org.np/nsdp/ . It explicitly lists Balance of Payments with Browse Data and Download in SDMX; the currently linked XML file is NEPAL_BOP_2024_Q1.xml, which is stale for Q2-2026 and not admitted.
3. NRB Monthly Statistics archive: https://www.nrb.org.np/category/monthly-statistics/ . Archive exposes downloadable XLSX for 2082-12 (mid-Apr 2026), 2083-01 (mid-May 2026), 2083-02 (mid-Jun 2026), and 2083-03 (mid-Jul 2026). Relevant XLSX URLs:
   - https://www.nrb.org.np/contents/uploads/2026/05/Chaitra_2082_Publish.xlsx
   - https://www.nrb.org.np/contents/uploads/2026/06/Baisakh_2083_Publish.xlsx
   - https://www.nrb.org.np/contents/uploads/2026/07/Jestha_2083_Publish-1.xlsx
- The three XLSX retrieval attempts failed at the browser content handler (unsupported XLSX MIME for Chaitra/Jestha; timeout for Baisakh). No workbook bytes were inspected; no values, workbook sheet names, or file SHA-256 are claimed.
- NRB monthly statistics archive labels the releases as mid-April, mid-May and mid-June 2026. These are monthly statistical publications, not proof that the included BOP series are monthly flows or that their rows are not cumulative.

## Rejected substitutes and scope risks
- NRB July 2026 macroeconomic report's chart reports monthly overall BOP, but does not provide the separate portfolio investment asset/liability legs in the extracted page. Aggregate BOP cannot substitute.
- NRB monthly balance sheet investment-in-foreign-securities rows are stocks, not BOP transaction flows; excluded.
- NSDP-linked XML is dated 2024 Q1; not current Q2-2026 evidence.
- No third-party or republished values admitted.

## Gate matrix
| Gate | Status |
|---|---|
| Fixed cohort membership | PASS (existing cohort) |
| Official NRB BPM6 source family | PASS (discovery) |
| Official monthly XLSX links for Apr–Jun 2026 | PASS (link discovery) |
| XLSX raw bytes / sheets / source SHA-256 | NOT_CAPTURED |
| Q2 calendar period alignment and monthly-vs-cumulative basis | NOT_ESTABLISHED |
| Separate national portfolio assets | NOT_EXTRACTED |
| Separate national portfolio liabilities | NOT_EXTRACTED |
| Sign / unit / BPM6 concept crosswalk | NOT_ESTABLISHED |
| Same-vintage with IMF | NOT_ESTABLISHED |
| Numeric dual-leg comparison | NOT_DONE |
| NPL national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## Next exact action
Retrieve the three official NRB monthly XLSX workbooks through an XLSX-capable route, inspect workbook sheets and exact portfolio asset/liability rows, and establish whether the observations are monthly flows or cumulative fiscal-year values. Only if comparable Q2 calendar-period legs are explicitly available should Apr–Jun observations be combined. Reuse existing IMF raw rows after national extraction; do not query IMF again. If the workbooks contain only net BOP or no portfolio legs, retain BLOCKED/PARTIAL and move to the next eligible country.

## Invariants
No synthetic data, no netting, no FX inference, no stock-as-flow substitution, no cumulative-to-quarter transform without documented source basis, no cohort rebuild, no IMF re-query, no production changes. UNKNOWN is never PASS.


## Continuation 57 correction — monthly archive document type verified (2026-11-20)

### Correction to prior source-boundary interpretation
- Opened the exact NRB Monthly Statistics archive PDF entries for 2082-12 (Mid-April 2026), 2083-01 (Mid-May 2026), and 2083-02 (Mid-June 2026). All three PDFs are titled **Banking & Financial Statistics (Monthly) (Provisional)** and their contents are banking/financial-institution balance sheets, P&L, credit and deposit statistics; not the External Sector BPM6 Balance of Payments workbook. The PDFs have 69, 69 and 70 pages respectively. Exact official PDF surfaces: https://www.nrb.org.np/bfr/2082-12mid-april-2026/ ; https://www.nrb.org.np/bfr/2083-01mid-may-2026/ ; https://www.nrb.org.np/bfr/2083-02mid-june-2026/ . Full-PDF text search found no “portfolio” or “Balance of Payments” match in the April PDF and no “Balance of Payments” match in the May/June PDFs. These three XLSX links must be REMOVED from the NPL BOP candidate list; they are not BOP evidence. This corrects the prior Continuation 56 inference that they might contain the necessary BOP rows.
- The correct official NRB External Sector page is https://www.nrb.org.np/database-on-nepalese-economy/external-sector/ . It lists Monthly Balance of Payments (BPM 6) as a distinct dataset. The official direct linked workbook is https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx . Attempted official retrieval returns unsupported XLSX MIME (400); no bytes/sheets/values/hash inspected.
- NRB NSDP page https://www.nrb.org.np/nsdp/ lists BOP Browse Data and SDMX Download. Browse Data route timed out; SDMX download link points to NEPAL_BOP_2024_Q1.xml (stale) and XML MIME is unsupported. Neither supplies Q2-2026 values.

### Corrected NPL gates
- Official External Sector BPM6 dataset discovery: PASS.
- Candidate monthly-statistics PDFs/XLSX: REJECTED as wrong document family (BFR, not BOP).
- Actual BPM6 XLSX bytes/sheets/rows: NOT_CAPTURED.
- Separate Q2-2026 national portfolio assets/liabilities: NOT_EXTRACTED.
- Monthly-vs-cumulative basis, sign/unit, vintage: NOT_ESTABLISHED.
- Numeric comparison: NOT_DONE; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

### Next exact action
- Stop using the monthly Banking & Financial Statistics archive for BOP. Find an XLSX-capable route for the single official External Sector BPM6 workbook or an official NRB API/export surface. If unavailable, keep NPL blocked and move to the next country; no repeated MIME retries, no balance-sheet stock substitution, no IMF re-query.


## Continuation 130 — NRB alternate publication-route check (2026-11-21)
- Re-fetched the current Master Ledger, GCR Priority Queue, fixed 63-country cohort, Batch-1 report and this NPL report before work. Existing batch order retained; NPL was the next unfinished country.
- Re-opened the official NRB External Sector page. It explicitly lists Monthly Balance of Payments (BPM 6) as the relevant dataset and its linked workbook remains the September-2026 Balance-of-Payments-BPM6.xlsx URL. The direct official link still fails at the retrieval bridge with HTTP 400 unsupported XLSX MIME; no workbook bytes/sheets/values/hash captured.
- Tested the distinct NRB National Summary Data Page (NSDP) route. Its BOP row advertises Browse Data and SDMX Download, but the actual Browse Data link resolves to the general Current Macro-Economic and Financial Situation archive, not a BOP series browser. The SDMX Download link resolves to NEPAL_BOP_2024_Q1.xml (2024-Q1), which is stale for Q2-2026 and its XML MIME is unsupported by the current retrieval bridge. IMF DSBB metadata link is metadata only, not a transaction dataset.
- NRB's latest macroeconomic report search result reports aggregate BOP/current-account context only; no separate Q2 portfolio transaction asset/liability observations. No proxy admitted.
- Result: no genuinely usable alternate official Q2 export/API route found in this bounded attempt. NPL national Q2 portfolio assets/liabilities remain NOT_EXTRACTED; period basis/sign/unit/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; NPL PARTIAL / BLOCKED; aggregate NOT_AUTHORIZED. Do not retry the same XLSX, NSDP XML or BFR monthly archive route. Advance to RWA.
- Official evidence: NRB External Sector page https://www.nrb.org.np/database-on-nepalese-economy/external-sector/ ; NSDP https://www.nrb.org.np/nsdp/ ; official Q2 candidate workbook https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx .
- No IMF re-query, no cohort rebuild, no annual/monthly cumulative allocation, no stock-as-flow, no synthetic values. ₹0; production invariants unchanged; UNKNOWN is never PASS.
