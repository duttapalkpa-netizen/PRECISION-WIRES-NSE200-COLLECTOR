# Nepal NPL Q2-2026 — NRB BPM6 Byte-Route Closure
Date: 2026-11-20
Status: OFFICIAL DATASET DISCOVERY PASS; XLSX BYTE CAPTURE BLOCKED; NATIONAL LEGS NOT_EXTRACTED; NPL PARTIAL / NOT PASS

## 1. Preflight
- Re-fetched Master Continuity Ledger, GCR Priority Queue, NPL Continuation 58 retrieval-route report and NPL source-boundary report.
- PASS work was not repeated. Fixed 63-country Q2-2026 cohort and existing IMF panel remain unchanged. No IMF re-query.
- NPL is the next country previously selected in the fixed-cohort queue after PER source-scope closure. The exact unresolved action is retrieval of the official NRB External Sector BPM6 workbook through a supported byte-preserving route.

## 2. Official source recheck
- NRB External Sector page: https://www.nrb.org.np/database-on-nepalese-economy/external-sector/ explicitly lists a separate Monthly “Balance of Payments (BPM 6)” dataset (web source inspected 2026-11-20).
- The BPM6 dataset link resolves to the exact official workbook:
  https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx
- NRB NSDP page: https://www.nrb.org.np/nsdp/ lists BOP Browse Data and Download in SDMX. The currently linked XML remains the stale NEPAL_BOP_2024_Q1.xml and is not admitted for Q2-2026.
- Exact workbook URL was re-opened with the web retrieval route; it returned HTTP 400 unsupported XLSX MIME. A separate container byte-download invocation against the exact URL also failed. No workbook bytes were obtained, so no size, MIME receipt, sheets, dimensions, rows, values or SHA-256 can be reported.
- The NRB Monthly Statistics PDF archive is a different Banking & Financial Statistics publication family, not External Sector BOP. Those prior candidates remain rejected under Continuation 57; they are not retried or substituted.

## 3. Fail-closed decision
- Official BPM6 dataset discovery remains PASS.
- XLSX retrieval remains BLOCKED; no supported byte-preserving route was established.
- Workbook content, period basis (monthly vs cumulative), Q2 Apr-Jun alignment, separate portfolio assets/liabilities, units, sign mapping and revision vintage remain NOT_INSPECTED / NOT_ESTABLISHED.
- No national Q2 values are extracted. No central-bank balance-sheet investment stocks, aggregate BOP, net-only series, third-party values or monthly banking statistics are substitutes.
- Existing IMF NPL rows are not copied or compared in this source-retrieval task. No new IMF query.

## 4. Gate matrix
| Gate | Status |
|---|---|
| NRB official External Sector BPM6 source discovery | PASS |
| Exact official XLSX locator | PASS |
| Browser byte retrieval | BLOCKED |
| Separate byte-download route | BLOCKED |
| Workbook bytes / SHA-256 / sheets | NOT_CAPTURED |
| Q2 calendar alignment / monthly-vs-cumulative basis | NOT_ESTABLISHED |
| Separate national portfolio asset leg | NOT_EXTRACTED |
| Separate national portfolio liability leg | NOT_EXTRACTED |
| Sign / unit / BPM6 concept crosswalk | NOT_ESTABLISHED |
| Same-vintage with IMF | NOT_ESTABLISHED |
| Numeric dual-leg comparison | NOT_DONE |
| NPL national validation | PARTIAL / NOT PASS |
| 63-country aggregate / production | NOT_AUTHORIZED |

## 5. Next action and handoff
- Close this exact NRB workbook URL route; do not repeat unsupported MIME or byte-download attempts without a genuinely new supported retrieval mechanism.
- Advance to the next eligible unvalidated member of the same fixed 63-country cohort, after repository preflight and review of existing country reports. Preserve NPL as PARTIAL / NOT PASS.
- Revisit NPL only if NRB exposes a distinct supported BOP API/export or an XLSX-capable byte route. Then hash original bytes before parsing and inspect period basis, legs, units, signs and revision metadata.
- No cohort rebuild, no IMF re-query, no paid data, no production changes, ₹0.

## 6. Sources
- NRB External Sector database: https://www.nrb.org.np/database-on-nepalese-economy/external-sector/
- NRB NSDP: https://www.nrb.org.np/nsdp/
- Exact official BPM6 workbook locator: https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx
- Prior retrieval boundary: docs/GCR_NEPAL_NPL_Q2_2026_NRB_BPM6_RETRIEVAL_ROUTE_AUDIT_CONTINUATION58_20261120.md

## 7. Protected invariants
Fixed 63-country cohort unchanged. No new IMF query, no fabricated values/timestamps, no stocks-as-flows, no netting, no cumulative-to-quarter arithmetic without source proof, no forward-fill, no guessed sign/scale, no production changes. UNKNOWN is never PASS.


## Continuation 94 — Final verification marker
- This report records the bounded NRB BPM6 byte-route closure. Official dataset discovery PASS; XLSX byte retrieval BLOCKED; workbook bytes/hash/sheets not captured; Q2 legs not extracted; NPL PARTIAL / NOT PASS; aggregate and production NOT_AUTHORIZED. No new IMF query or cohort rebuild.
