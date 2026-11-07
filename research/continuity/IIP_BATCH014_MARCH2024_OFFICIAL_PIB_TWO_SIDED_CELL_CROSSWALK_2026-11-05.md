# Batch 014 March 2024 — official PIB two-sided cell crosswalk

Date: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean
Input ledger: IIP_693_POLICY_ALIGNED_CANDIDATE_MASTER_LEDGER.csv
Input size: 566,796 bytes
Independently recomputed CSV SHA-256: 1a1d065f9dba2408f1ef4b8cd06aed78306873ba318294694fe3ec6d8d37c247

## Scope and method
Filtered the immutable candidate master ledger to period 2024-03. The cohort contains 19 rows and 19 unique NIC codes: 10, 11, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32. Compared each stored Quick value with official PIB PRID 2020239 Statement II (March 2024 Quick Estimates), and each stored First Revision value with official PIB PRID 2024748 Statement IV (March 2024 monthly index after the first revision). Recomputed First Revision minus Quick and compared to the stored revision_delta.

Official Quick source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2020239&lang=2&reg=48
Official Quick Statement IV/HTML source: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2020239&lang=2&reg=3
Official First Revision source: https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2024748&lang=2&reg=48
Official First Revision page: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2024748&lang=2&reg=3

## Exact two-sided crosswalk
All values below are official PIB table values as displayed in the respective release. Values are index points (base 2011-12=100).

| NIC | Quick PRID 2020239 | First Revision PRID 2024748 | Delta |
|---:|---:|---:|---:|
| 10 | 141.5 | 142.5 | +1.0 |
| 11 | 124.0 | 124.3 | +0.3 |
| 13 | 109.3 | 106.5 | -2.8 |
| 14 | 143.1 | 143.2 | +0.1 |
| 15 | 95.3 | 95.9 | +0.6 |
| 18 | 93.2 | 92.3 | -0.9 |
| 19 | 139.6 | 142.4 | +2.8 |
| 20 | 129.7 | 130.3 | +0.6 |
| 21 | 227.3 | 228.1 | +0.8 |
| 22 | 116.6 | 116.8 | +0.2 |
| 23 | 164.6 | 165.4 | +0.8 |
| 24 | 230.5 | 232.1 | +1.6 |
| 26 | 132.7 | 134.7 | +2.0 |
| 27 | 123.9 | 124.3 | +0.4 |
| 28 | 144.9 | 145.1 | +0.2 |
| 29 | 130.5 | 130.3 | -0.2 |
| 30 | 174.5 | 175.7 | +1.2 |
| 31 | 276.3 | 278.6 | +2.3 |
| 32 | 89.9 | 90.0 | +0.1 |

## QA result
- Official PIB Quick cells matched: 19/19.
- Official PIB First Revision cells matched: 19/19.
- NIC code-set equality between ledger and crosswalk: PASS (19/19).
- Stored revision_delta arithmetic: PASS (19/19; no rounded discrepancy at 0.01 index-point precision).
- The previously suspected NIC-27 value conflict is resolved for this release pair: 123.9 Quick -> 124.3 First Revision. The 124.7 figure surfaced in a later release vintage and is not the June 2024 first-revision value. Do not substitute later-vintage values into this batch.
- Release mapping correction remains append-only: Quick PRID 2020239; First Revision PRID 2024748. Historical master ledger remains unchanged.

## Certification boundary
This completes the two-sided official PIB HTML table crosswalk for the 19-row policy-aligned candidate cohort. It does NOT certify the full NIC-2 universe: codes absent from this candidate cohort remain outside scope. It also does NOT independently certify the declared source-workbook binary hashes or raw official PDF payload hashes. The two exact source workbook binaries were not located in the Library during this pass; declared hashes remain declarations until bytes are obtained and rehashed. Raw PDF payload SHA-256 values likewise remain pending.

Status:
- OFFICIAL_PIB_HTML_TWO_SIDED_CELL_CROSSWALK: PASS (19/19 each side)
- DELTA_ARITHMETIC: PASS (19/19)
- POLICY_ALIGNED_CANDIDATE_COHORT: PASS (19/19)
- FULL_NIC2_COHORT_COVERAGE: UNKNOWN / OUT OF SCOPE
- WORKBOOK_BINARY_SHA256_REVALIDATION: PENDING
- RAW_OFFICIAL_PDF_SHA256: PENDING
- BATCH_014_FULL_SOURCE_PROVENANCE_CERTIFICATION: BLOCKED
- MASTER HARD GATE: BLOCKED

Controls: old source ledger and historical PASS artifacts are preserved; no synthetic rows, fabricated timestamps, unsupported source promotion or gate relaxation. UNKNOWN is neither PASS nor FAIL. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and A/B/C/D/E production logic remain unchanged.
