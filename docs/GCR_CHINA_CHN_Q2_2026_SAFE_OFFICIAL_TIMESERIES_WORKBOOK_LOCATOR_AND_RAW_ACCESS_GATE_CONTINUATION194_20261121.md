# China (CHN) Q2-2026 — SAFE official time-series workbook locator and raw-access gate (Continuation 194)
Date: 2026-11-21
Decision: A DISTINCT OFFICIAL SAFE TIME-SERIES WORKBOOK LOCATOR WAS RECOVERED, BUT RAW XLSX BYTES COULD NOT BE RETRIEVED THROUGH THE AVAILABLE WEB/CONTAINER ACCESS PATHS. THE LOCATOR IS VERIFIED; WORKBOOK CONTENT, HASH, DETAILED PORTFOLIO SERIES, SIGN CROSSWALK AND OBSERVATION VINTAGE REMAIN NOT_CAPTURED. CHN PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity and duplicate-prevention preflight
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue and Historical Task Registry.
- Re-opened the existing CHN Q2-2026 SAFE-vs-IMF comparison report and reused its archived IMF exact-key evidence; no IMF GET or cohort rebuild.
- Rejected completed PASS work: IMF DSD/registry capture, fixed 63-country cohort, exact-key receipts, SAFE abridged Q2 release extraction, and existing rounded-magnitude arithmetic.
- Selected only the prior report's open action: follow SAFE's official Data and Statistics → Balance of Payments time-series attachment and inspect its detailed BPM6 portfolio transaction rows/sign convention.

## 2. Distinct official SAFE route recovered
- Official SAFE Data and Statistics index: https://www.safe.gov.cn/en/DataandStatistics/index.html. It lists Balance of Payments and the time-series data of China's Balance of Payments with dispatch date 2026-09-29.
- Official SAFE Balance of Payments time-series landing page: https://www.safe.gov.cn/en/2019/0329/1496.html. The page identifies the publisher as State Administration of Foreign Exchange, index 000014453-2019-0016, dispatch date 2026-09-29, and names the time-series data of Balance of Payments of China.
- The landing page's actual attachment link resolves to this exact XLSX target: https://www.safe.gov.cn/en/file/file/20260929/20c1e5e45d704a77b302ba234211a75b.xlsx
- This is a newly recovered official workbook locator, not a guessed filename or an IIP stock substitute.

## 3. Raw access test and evidence boundary
- Opening the official attachment through the web retrieval surface returned an unsupported-content-type error for `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`.
- A direct container download attempt to the exact same official XLSX URL failed. No workbook bytes, HTTP status/headers from the raw download, byte count, MIME receipt, SHA-256, worksheet names, table cells or hidden-sheet contents were obtained.
- The exact URL is therefore VERIFIED as a page-linked official attachment locator; workbook retrieval is BLOCKED in the current execution environment. Do not label the workbook or its contents PASS.
- No alternate/derived data source, unofficial mirror, IIP stock table, net-to-leg inference, or invented attachment URL was substituted.

## 4. Existing CHN comparison preserved (not recalculated)
- Existing IMF exact-key receipt (19-Nov-2026) and C190 CHN report remain the source for prior figures; no IMF request was made.
- Existing SAFE abridged Q2-2026 release (29-Sep-2026), BPM6, USD 100m units: portfolio assets -488; liabilities +433; balance -55 (all × USD 100m).
- Existing IMF raw values (SCALE=6): A_NFA_T +48,794.459104 USDm; L_NIL_T +43,286.600714 USDm.
- Prior report's magnitude residuals remain 5.540896 USDm assets and 13.399286 USDm liabilities, within the ±50 USDm half-unit rounding bound of SAFE's 100-million-USD display. Liability signed comparison was consistent; asset sign/direction remained unresolved. This locator audit supplies no new evidence to alter that conclusion.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| Current Ledger / Queue / Registry and CHN prior report preflight | PASS |
| Fixed cohort and existing IMF exact-key evidence reused | PASS |
| Official SAFE time-series landing page and attachment href | PASS — locator only |
| Exact XLSX URL identity | PASS — page-linked URL |
| Raw XLSX retrieval / bytes / MIME receipt / SHA-256 | BLOCKED / NOT_CAPTURED |
| Workbook worksheet and detailed Q2 portfolio rows | NOT_CAPTURED |
| Detailed SAFE asset sign convention / IMF crosswalk | NOT_ESTABLISHED |
| Observation-level vintage and revision identity | NOT_ESTABLISHED |
| CHN full national dual-leg validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 6. Next action and protected invariants
- Reopen only when a supported browser/file workflow can retrieve the exact official XLSX target above, or SAFE publishes a distinct official machine-readable export. Then preserve original bytes, MIME, retrieval timestamp and SHA-256 before parsing workbook sheets and comparing detailed Q2 portfolio asset/liability transaction lines.
- Do not repeat the same unsupported XLSX fetch through the same retrieval surface. Do not infer sign from the abridged balance, use IIP stocks, or back-solve legs from the net line.
- ₹0; official/free sources only. No IMF GET, cohort rebuild, synthetic data/timestamps, net-to-leg inference, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN never PASS.