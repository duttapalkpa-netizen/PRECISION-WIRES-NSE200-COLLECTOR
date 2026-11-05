# Batch 014 March 2024 ledger QA and PRID correction overlay

Date: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean

## Input
IIP_693_POLICY_ALIGNED_CANDIDATE_MASTER_LEDGER.csv
Computed raw CSV SHA-256: `1a1d065f9dba2408f1ef4b8cd06aed78306873ba318294694fe3ec6d8d37c247`
Size: 566796 bytes.

## Structural QA
Filter period 2024-03: 19 rows, 19 unique NIC codes, zero duplicates, zero missing Quick values, zero missing First Revision values, and no missing declared workbook hashes. All rows are labelled QUICK and FIRST_REVISION. All 19 rows currently carry Quick PIB PRID 2020261 and First Revision PIB PRID 2024748. Recomputed First Revision minus Quick deltas match the stored revision_delta for all 19 rows (maximum absolute floating point discrepancy 4.45e-16).

Quick workbook declared SHA-256: `5c1fa4bfec7bec39a5a109660860924084069a46849af4042d12e554323844f7`.
First Revision workbook declared SHA-256: `db05a095e3b86cf4333ebae2fc2733931447dde7bd0fcde18c4122ca3c390963`.

## Append-only release-ID correction
Official PIB PRID 2020239 is the March 2024 Quick Estimates release (10 May 2024, 5:30 PM IST). Official PIB PRID 2024748 is the 12 June 2024 release that explicitly applies the First Revision to March 2024. Therefore, for all 19 candidate rows, the correction overlay sets quick_pib_prid_corrected=2020239 and retains first_revision_pib_prid=2024748. Values, deltas, source file names and declared workbook hashes remain unchanged. The historical CSV is not overwritten.

## Retained values
NIC 10: 141.5 -> 142.5, delta +1.0
NIC 11: 124.0 -> 124.3, delta +0.3
NIC 13: 109.3 -> 106.5, delta -2.8
NIC 14: 143.1 -> 143.2, delta +0.1
NIC 15: 95.3 -> 95.9, delta +0.6
NIC 18: 93.2 -> 92.3, delta -0.9
NIC 19: 139.6 -> 142.4, delta +2.8
NIC 20: 129.7 -> 130.3, delta +0.6
NIC 21: 227.3 -> 228.1, delta +0.8
NIC 22: 116.6 -> 116.8, delta +0.2
NIC 23: 164.6 -> 165.4, delta +0.8
NIC 24: 230.5 -> 232.1, delta +1.6
NIC 26: 132.7 -> 134.7, delta +2.0
NIC 27: 123.9 -> 124.3, delta +0.4
NIC 28: 144.9 -> 145.1, delta +0.2
NIC 29: 130.5 -> 130.3, delta -0.2
NIC 30: 174.5 -> 175.7, delta +1.2
NIC 31: 276.3 -> 278.6, delta +2.3
NIC 32: 89.9 -> 90.0, delta +0.1

## Certification boundary
This is ledger structure and arithmetic QA only. It does not certify all 19 values against the official PIB statements or workbook bytes. The input is a policy-aligned candidate ledger, not the full NIC-2 universe; 19 codes are present and several codes are absent. Do not claim full March 2024 NIC-2 cohort coverage.

Still pending: exact PIB cell verification for every row; reopening both workbook binaries and independently recomputing hashes; raw official PDF payload hashes; and confirmation of the full NIC-2 universe.

Status: LEDGER_STRUCTURE_AND_DELTA_QA_PASS; RELEASE_ID_CORRECTION_OVERLAY_READY; OFFICIAL_CELL_COHORT_AUDIT_PENDING; SOURCE_BINARY_HASH_PENDING. Hard Gate remains BLOCKED.

Controls unchanged: no synthetic rows, fabricated timestamps, unsupported source promotion, or gate relaxation. UNKNOWN is neither PASS nor FAIL. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and A/B/C/D/E production logic remain unchanged.