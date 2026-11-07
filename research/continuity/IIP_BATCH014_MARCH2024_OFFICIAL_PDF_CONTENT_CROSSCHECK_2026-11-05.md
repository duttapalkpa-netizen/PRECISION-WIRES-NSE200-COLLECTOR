# IIP Batch 014 — March 2024 official PDF table cross-check
Date: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean

## Scope
This is an append-only evidence note for the existing 19-row March 2024 policy-aligned candidate ledger. It records a direct content-level cross-check against the two official MoSPI press-release PDFs. It does not replace the prior ledger QA, PIB crosswalk, or source-binary acquisition checkpoint.

## Official sources inspected
1. March 2024 Quick Estimate, dated 10 May 2024:
   https://mospi.gov.in/sites/default/files/iip/IIP_PR_10may24.pdf
   Relevant table: Statement II, NIC-2008 two-digit level. The PDF identifies March 2024 values as Quick Estimates.
2. April 2024 Quick Estimate release, dated 12 June 2024, containing March 2024 First Revision:
   https://www.mospi.gov.in/sites/default/files/iip/IIP_PR_12jun24.pdf
   Relevant table: Statement IV, monthly NIC-2 series, March-24 column. The release explicitly states that March 2024 underwent first revision and reports a 96% weighted response rate.

## Reconciliation result
The 19 candidate NIC codes already present in the Batch 014 ledger are:
10, 11, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32.

Official PDF content cross-check:
- Quick Estimate: 19/19 candidate code values agree with the Quick values already represented in the ledger/crosswalk.
- First Revision: 19/19 candidate code values agree with the March-24 column in Statement IV of the 12 June 2024 official PDF.
- Delta arithmetic: existing ledger deltas remain First Revision minus Quick; no recalculation or rewrite of the production ledger was performed.
- The NIC-27 March-24 First Revision value is 124.3. This is confirmed in the official PDF's Statement IV; do not substitute a later-vintage value.
- The full official table includes additional NIC-2 codes and aggregate rows not in the 19-row candidate ledger. This check does not certify full NIC-2 universe coverage.

## Evidence boundary
PASS: official PDF publication identity/date and relevant table content inspected; 19/19 candidate code values cross-checked at the published-PDF content level.

NOT CERTIFIED:
- Raw PDF payload bytes were not downloaded into the audit runtime; raw PDF SHA-256 values remain pending.
- Original XLSX workbook binaries were not located; the previously declared XLSX hashes remain unverified.
- The 19-row candidate cohort is not a complete NIC-2 cohort.
- No claim is made that a browser-rendered/extracted PDF text view is equivalent to raw binary provenance or workbook-cell provenance.

## Status
PDF_CONTENT_CROSSCHECK: PASS (19/19 Quick; 19/19 First Revision)
PDF_RAW_BINARY_SHA256: PENDING
SOURCE_XLSX_BINARY_AND_HASH_REVALIDATION: PENDING
FULL_NIC2_COHORT_COVERAGE: UNKNOWN
BATCH014_FULL_PROVENANCE: BLOCKED
MASTER_HARD_GATE: BLOCKED

## Invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or A/B/C/D/E engine logic changed. No synthetic rows, fabricated timestamps, unsupported source promotion, or hard-gate relaxation. Existing PASS artifacts and hashes remain untouched.
