# GCR — Tajikistan (TJK) Q2-2026 National Bank of Tajikistan official BOP workbook locator and byte-access boundary

Date: 2026-11-25 (Asia/Kolkata)
Continuation: 240

Decision: **A distinct official National Bank of Tajikistan Q2-2026 Standard Representation BOP workbook locator is confirmed from the NBT's own Balance of Payments page. The current retrieval surface rejects the XLSX MIME type (HTTP 400 in the document reader), and a direct byte-download attempt also failed. No workbook bytes, table schema, Q2 portfolio asset/liability values, response headers, byte count or SHA-256 were captured. TJK remains SOURCE_FOUND / PARTIAL / NOT PASS; both national legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED.**

## 1. Continuity and duplicate-prevention preflight
- Re-fetched the current GitHub Master Continuity Ledger, GCR Priority Queue, 63-country national validation matrix and Historical Task Registry before selection.
- Searched the Library Mother File/GCR context. TJK is a member of the fixed 63-country Q2-2026 cohort; matrix status before this task was SOURCE_FOUND with both national legs NOT_CAPTURED.
- Registry search found no prior TJK-specific continuation or route fingerprint. Existing fixed cohort and archived IMF panel are reused; no IMF re-query or cohort rebuild.
- Previously accepted country validations and all PASS work were skipped. No C237–C239 route or report was repeated.

## 2. Official NBT source and exact workbook locators
- Official National Bank of Tajikistan Balance of Payments page: https://www.nbt.tj/en/payments_balance/
- The page states that compilation of the Republic's BOP is an NBT function and that the BOP is compiled using IMF BPM5/BPM6 methodological recommendations.
- The official page lists 2026 under both Analytical Representation and Standard Representation.
- Standard Representation 2026 link resolves to:
  https://www.nbt.tj/upload/iblock/d9d/6x5djzg70lrzfq0t9f3pibhv3vmkb71x/st_pr_2026_2.xlsx
- Analytical Representation 2026 link resolves to:
  https://www.nbt.tj/upload/iblock/1fd/gt06fcxjn5ilv466tnxmf28usqj9vnc5/an_pr_2026_2.xlsx
- The two are distinct official workbooks. The standard workbook is the primary candidate for the Q2 national comparison; the analytical workbook is recorded as a separate official locator only, not as a substitute or independently inspected dataset.

## 3. Retrieval and evidence boundary
- The official page was opened and its 2026 links followed.
- The document retrieval surface returned HTTP 400 / Unsupported content-type for the Standard Representation XLSX and also for the Analytical Representation XLSX.
- A separate direct byte-download attempt for the exact Standard Representation XLSX failed. No claim is made about the origin server's HTTP status or the workbook's internal content.
- No raw workbook bytes, HTTP response headers, content length, row count, sheet names, schema, data values, publication timestamp, or SHA-256 were obtained.
- Therefore the Q2 period, portfolio row labels, separate asset/liability transaction legs, unit/sign convention and observation-specific vintage have NOT been validated from the workbook.
- Do not substitute the NBT IIP stocks/operations table, annual IMF country-report projections, banking-sector asset/liability balances, or a net portfolio item for Q2 BOP transaction legs.

## 4. Acceptance boundary
| Gate | Status |
|---|---|
| Fixed 63-country TJK Q2-2026 membership | PASS (reused) |
| Official NBT BOP source family | PASS |
| Official Standard Representation 2026 XLSX locator | PASS |
| Official Analytical Representation 2026 XLSX locator | PASS (locator only) |
| Standard XLSX raw bytes / headers / SHA-256 | NOT_CAPTURED |
| Workbook sheets/schema and reporting period Q2-2026 | NOT_VERIFIED |
| Portfolio asset transaction leg | NOT_CAPTURED |
| Portfolio liability transaction leg | NOT_CAPTURED |
| Units/sign methodology from workbook | UNKNOWN |
| Observation-specific revision/vintage bridge | UNKNOWN |
| National dual-leg comparison | NOT_DONE |
| TJK national validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 5. Next exact action / duplicate prevention
- Reopen only through a genuinely different supported XLSX-capable byte-transfer/browser route or a distinct official NBT Q2-2026 downloadable representation that exposes the workbook bytes and revision metadata.
- Do not repeat the same document-reader click or the failed direct byte-download route.
- Once bytes are obtained, preserve exact URL, retrieval timestamp, response headers, byte count and SHA-256 before parsing. Inspect sheets/periods, identify separate portfolio assets/liabilities, preserve units/signs, and compare to the already archived IMF Q2 rows without a new IMF query.
- If no supported byte route exists, retain TJK PARTIAL / NOT PASS and move to the next eligible fixed-cohort member after a fresh route-history preflight.

## 6. Protected invariants
₹0; official/free sources only; no synthetic values, fabricated timestamps, net-to-leg back-solving, IIP stock-as-flow substitution, unsupported FX/sign/scale conversion, paid services or external contact. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 remain unchanged. No production integration or merge.
