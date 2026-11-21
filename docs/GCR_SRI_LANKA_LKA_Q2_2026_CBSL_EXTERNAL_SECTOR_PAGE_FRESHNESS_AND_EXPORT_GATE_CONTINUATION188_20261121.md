# Sri Lanka (LKA) Q2-2026 — CBSL External Sector page freshness and export gate (Continuation 188)
Date: 2026-11-21 (Asia/Kolkata)
Decision: A NEW CBSL OFFICIAL SEARCH-INDEXED EXTERNAL-SECTOR PAGE UPDATE MARKER (01-Oct-2026) WAS FOUND; IT CONFIRMS THE PAGE HAS A CURRENT EXTERNAL-SECTOR CONTENT UPDATE AND LISTS BPM6 QUARTERLY BOP THROUGH “LATEST”, BUT DOES NOT EXPOSE A VERSIONED TABLE 2.10 FILE OR ITS RELEASE/VINTAGE. THE LEGACY SDDS BOP.XLSX ROUTE REMAINS STALE (NSDP PAGE LAST UPDATED 11-Nov-2017) AND BLOCKED FOR BYTES. LKA Q2 NATIONAL DUAL-LEG VALUES REMAIN STRONG PROVISIONAL RECONCILIATION; SAME-VINTAGE / PRIMARY CBSL RAW EXPORT NOT_ESTABLISHED; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, C175, C176, C177, C174 and immutable 63-country cohort before selection.
- Confirmed exact fixed cohort row: LKA, Q2-2026, both A_NFA_T and L_NIL_T present; national validation pending; aggregate NOT_AUTHORIZED. Cohort SHA-256 / Git blob retained: `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.
- C174 already established separate provisional Treasury Table 7 portfolio assets +26 USDm and liabilities -351 USDm, both matching archived IMF values at whole-million rounding. No IMF re-query.
- C175: exact CBSL Table 2.10 URL and third-party-reported 30-Sep-2026 marker found; direct official page/XLSX fetch returned 403; bytes/hash not captured.
- C176: secondary Macro Lab corroboration and instrument arithmetic completed; not primary evidence.
- C177: distinct official SDDS BOP.xlsx locator found, but its parent NSDP page explicitly last updated 11-Nov-2017 and showed Q2/17; bytes unavailable. Do not treat as current.
- No repeat of identical CBSL XLSX, SDDS BOP.xlsx, or Macro Lab JSON/CSV transfer attempts.

## 2. New official discovery
- CBSL official search result for its “External Sector” page reports page content updated by CBSL content manager on 01-Oct-2026 at 11:30.
- Search-indexed page text lists “Balance of Payments (BPM6 Basis) - Quarterly (2012 1Q to Latest)” within the External Sector statistical tables.
- Official search result/page locator: https://www.cbsl.gov.lk/en/search/node/2001%20-%202023
- The search-indexed result is evidence of the page's 01-Oct-2026 content-update marker and the current page description. Direct open of the search-result page returned HTTP 403 in this session. It does not expose a workbook locator, file release date, revision ID, raw bytes, or Q2 cell values.
- Important boundary: page content update date is not necessarily the statistical workbook's release/vintage date. It cannot bridge the 30-Sep-2026 Table 2.10 filename marker to the 12-Nov-2026 Treasury Table 7 report.

## 3. Acceptance matrix
| Gate | Status |
|---|---|
| Master Ledger / Priority Queue / Registry / prior LKA reports preflight | PASS |
| Fixed 63-country LKA cohort row | PASS (reused) |
| C174 dual-leg Treasury values and IMF rounded match | PASS at provisional published precision |
| CBSL External Sector page update marker 01-Oct-2026 | PASS (search-indexed official page metadata) |
| CBSL page describes BPM6 quarterly BOP through latest | PASS (search-indexed official page text) |
| Exact versioned current Table 2.10 workbook / export URL from new page | NOT_CAPTURED |
| Official workbook bytes, MIME, size, SHA-256 and cell coordinates | NOT_CAPTURED |
| Statistical series revision/vintage identifier | NOT_ESTABLISHED |
| Treasury 12-Nov report ↔ CBSL Table 2.10 same-vintage bridge | NOT_ESTABLISHED |
| LKA final national validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 4. Rejected shortcuts
- Do not treat a CBSL web-page update timestamp as the data vintage.
- Do not treat the secondary reported XLSX SHA as independently verified.
- Do not treat the stale 2017 SDDS workbook locator as Q2-2026 data.
- Do not promote secondary Macro Lab values to official raw-source evidence.
- No net-to-leg back-solving, IIP stock substitution, IMF re-query, cohort rebuild, FX conversion or acceptance relaxation.

## 5. Next exact action
- The C175–C177 access paths are closed for repeat attempts. Reopen LKA only if a distinct supported official file/API route or an actual current Table 2.10 release identifier is discovered. Otherwise preserve provisional dual-leg result and advance to the next eligible fixed-cohort country after full preflight.
- Do not claim this page-freshness discovery resolves the same-vintage gate.

## 6. Protected invariants
₹0; official/free sources only. No synthetic values/timestamps, no IMF re-query, no cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN never PASS.
