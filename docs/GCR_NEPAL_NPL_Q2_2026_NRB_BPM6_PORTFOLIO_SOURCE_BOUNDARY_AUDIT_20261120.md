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
