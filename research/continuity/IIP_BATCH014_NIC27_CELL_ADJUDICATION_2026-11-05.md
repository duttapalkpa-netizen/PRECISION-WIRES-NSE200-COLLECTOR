# IIP Batch 014 — March 2024 NIC-27 official cell adjudication
Date: 2026-11-05
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: fix/iip-41-vintage-audit-clean
Scope: append-only source reconciliation; no production or master-ledger mutation.

## Result
The previously flagged NIC-27 discrepancy is resolved at the official PIB publication-text level. The earlier apparent value 124.7 was a misread of the search extract and is not supported by the exact Statement IV row returned from PIB PRID 2024748.

For March 2024, NIC-27 (Manufacture of electrical equipment):
- Quick estimate: 123.9, official PIB PRID 2020239 (10 May 2024, 17:30 IST), Statement II row for NIC-27. PIB search result explicitly shows the 2023-24 March Quick value 123.9.
- First Revision: 124.3, official PIB PRID 2024748 (12 Jun 2024, 17:30 IST), Statement IV, NIC-27 row, Mar-24 column. PIB page states March 2024 underwent first revision.
- Revision delta: +0.4 (124.3 - 123.9).
- The Master Ledger row index 209 currently stores 123.9 and 124.3, so both NIC-27 values agree with the official PIB page text. Do not alter these values.
- The ledger's Quick PRID for the March 2024 event is incorrectly recorded as 2020261. The verified official Quick release reference is PRID 2020239. Correct this only in a future append-only reconciliation overlay; do not rewrite the historical ledger.

## Evidence
1. PIB PRID 2020239: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2020239&lang=2&reg=48
   - Release title: India's Index of Industrial Production grows by 4.9% in March 2024.
   - Posted 10 MAY 2024 5:30PM.
   - Release text identifies March 2024 as Quick Estimates.
   - NIC-27 line: Manufacture of electrical equipment; March 2024 Quick index = 123.9.
2. PIB PRID 2024748: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2024748&lang=2&reg=48
   - Posted 12 JUN 2024 5:30PM.
   - Release text explicitly says indices for March 2024 underwent first revision.
   - Statement IV, row 27, March-24 column = 124.3.
3. Master Ledger source record:
   - File: IIP_693_POLICY_ALIGNED_CANDIDATE_MASTER_LEDGER.csv
   - Row index: 209; period 2024-03; NIC code 27.
   - Quick value 123.9; First Revision value 124.3.
   - Quick workbook declared SHA-256: 5c1fa4bfec7bec39a5a109660860924084069a46849af4042d12e554323844f7.
   - First Revision workbook declared SHA-256: db05a095e3b86cf4333ebae2fc2733931447dde7bd0fcde18c4122ca3c390963.

## Verification boundary
- Official PIB publication text cross-check for the NIC-27 Quick and First Revision values: MATCH.
- Quick PRID mapping in existing master ledger: MISMATCH; correction target is 2020239 (append-only overlay only).
- Raw PDF binary SHA-256 values: NOT CAPTURED in this pass.
- Workbook bytes re-opened and independently re-hashed in this pass: NO. The hashes above are the declared ledger hashes, not a newly recomputed digest.
- Full March 2024 NIC-2 cohort (all rows) and both workbook cell ranges: NOT YET CERTIFIED.
- Therefore Batch 014 is not fully certified. Status: PIB_CELL_PAIR_CONFIRMED_NIC27; SOURCE_PROVENANCE_HASH_PENDING; COHORT_AUDIT_PENDING.

## Required next bounded action
Reconcile all March-2024 NIC-2 ledger rows against the exact Quick and First Revision official PIB statements, then reopen both workbook payloads and recompute their SHA-256 values. Capture raw PDF payload hashes if a permitted official download path is available. Preserve any remaining mismatch as UNKNOWN/UNRESOLVED; do not infer or overwrite values.

## Controls
- Historical artifacts, Run IDs, hashes and the source master ledger remain immutable.
- No synthetic rows, fabricated timestamps, unsupported source promotion or Hard Gate relaxation.
- UNKNOWN is neither PASS nor FAIL.
- No changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or A/B/C/D/E production logic.
- Hard Gate remains BLOCKED pending all outstanding P0, factor, provenance, event-study and coverage evidence.
