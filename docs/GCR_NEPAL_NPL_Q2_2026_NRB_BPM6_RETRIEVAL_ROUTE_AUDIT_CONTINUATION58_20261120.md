# Nepal (NPL) Q2-2026 NRB BPM6 Retrieval-Route Audit — Continuation 58 / Part-1
Date: 2026-11-20
Status: **OFFICIAL SOURCE ROUTE CONFIRMED; XLSX BYTE RETRIEVAL BLOCKED; NPL remains PARTIAL / NOT PASS.**

## 1. Continuity and scope
- Reopened the existing NPL source-boundary report and GCR master priority queue before work.
- Reused the existing fixed 63-country Q2-2026 cohort and prior IMF archive. No cohort rebuild, no IMF re-query, no duplicate extraction.
- The Continuation 57 correction remains binding: NRB Chaitra 2082, Baisakh 2083 and Jestha 2083 Monthly Statistics files are Banking & Financial Statistics (Monthly) (Provisional), not External Sector BOP. They remain rejected.

## 2. Official route re-verification
- NRB External Sector database page: https://www.nrb.org.np/database-on-nepalese-economy/external-sector/
  - Page explicitly lists Monthly “Balance of Payments (BPM 6)” as a separate dataset.
  - The BPM6 dataset link resolves to the exact official workbook:
    https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx
- NRB NSDP page: https://www.nrb.org.np/nsdp/
  - Official page lists Balance of Payments Browse Data and Download in SDMX.
  - The current SDMX link resolves to NEPAL_BOP_2024_Q1.xml, so it is stale for Q2-2026 and is not admitted.
- Official page links were reopened on 2026-11-20. The direct workbook request through the web retrieval route returned HTTP 400 “Unsupported content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet”.
- A separate direct byte-download attempt against the same exact official XLSX URL also failed in the execution environment. No workbook bytes, ZIP package, sheets, rows, values, metadata, or SHA-256 were obtained. This is a retrieval failure, not evidence that the workbook is absent or empty.
- The NSDP Browse Data link resolves to the general NRB macroeconomic situation archive rather than a directly accessible BOP result in the inspected page; it did not provide a usable Q2 portfolio export in this bounded check. Do not infer that an API endpoint exists from the generic SDMX link.

## 3. Retrieval-route conclusion
The official dataset discovery gate remains PASS. No supported XLSX-capable byte route or current Q2-2026 official API/export endpoint was verified in this run. The exact workbook URL is known, but its contents remain uninspected. Do not repeat the same unsupported-MIME request or claim that a workbook inspection occurred.

## 4. Gate matrix
| Gate | Status |
|---|---|
| Official NRB External Sector BPM6 source discovery | PASS |
| Exact official BPM6 XLSX locator | PASS |
| Browser/XLSX byte retrieval | BLOCKED |
| Independent byte retrieval | BLOCKED |
| Workbook bytes / SHA-256 / sheets | NOT_CAPTURED |
| Separate Q2-2026 portfolio asset leg | NOT_EXTRACTED |
| Separate Q2-2026 portfolio liability leg | NOT_EXTRACTED |
| Monthly-vs-cumulative basis / period alignment | NOT_ESTABLISHED |
| Sign, units, BPM6 concept, publication vintage | NOT_ESTABLISHED |
| Numeric dual-leg comparison | NOT_DONE |
| NPL national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 5. Next exact action
1. Stop repeated attempts against the same XLSX MIME endpoint.
2. Resume only when a supported, byte-preserving XLSX-capable route or a distinct official NRB API/export route is available; acquire the exact official workbook bytes and calculate SHA-256 before parsing.
3. Inspect workbook sheet names, dimensions, period labels, portfolio investment asset/liability lines, units, sign convention, publication/revision metadata, and monthly-versus-cumulative basis.
4. Only after Q2 comparable legs are explicitly identified, reuse the already archived IMF NPL exact rows and compare assets and liabilities separately. No netting, no stock substitution, no unsupported cumulative-to-quarter arithmetic.
5. If no official route becomes available, preserve NPL as PARTIAL / NOT PASS and move to the next eligible fixed-cohort country.

## 6. Protected invariants
No synthetic values, fabricated timestamps, stock-as-flow substitution, IMF re-query, cohort rebuild, paid API, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.

## Evidence surfaces
- NRB External Sector page: https://www.nrb.org.np/database-on-nepalese-economy/external-sector/
- Exact official BPM6 workbook: https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx
- NRB NSDP: https://www.nrb.org.np/nsdp/
- NRB NSDP currently linked BOP SDMX XML: https://www.nrb.org.np/contents/uploads/2024/05/NEPAL_BOP_2024_Q1.xml
