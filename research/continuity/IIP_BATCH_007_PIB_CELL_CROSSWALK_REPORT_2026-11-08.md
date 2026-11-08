# IIP Batch 007 — two-sided official PIB cell crosswalk (2026-11-08)

Status: **PASS_CELL_CROSSWALK_14_OF_14** (bounded to the 14 NIC rows present in Batch 007; not a full NIC-2 universe certification).

## Inputs and integrity
- Canonical master ledger: `IIP_693_POLICY_ALIGNED_CANDIDATE_MASTER_LEDGER.csv`
- Ledger SHA-256: `1a1d065f9dba2408f1ef4b8cd06aed78306873ba318294694fe3ec6d8d37c247`
- Selected 14 rows for period `2023-08`, batch `006-008`; unique NIC codes: 10,11,14,15,17,18,20,22,23,24,25,26,28,32.
- Input ledger read-only; no source values or prior artifacts modified.

## Official source evidence
1. August 2023 Quick Estimates, PIB PRID 1967120, Statement II, Aug'23* column:
   https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=1967120&lang=2&reg=48
   - Official release identifies August 2023 Quick Estimates and Statement II NIC-2008 2-digit index; rows/cells appear at lines 123–150.
2. September 2023 release, PIB PRID 1976207, Statement IV, Aug-23 column:
   https://www.pib.gov.in/PressReleasePage.aspx?PRID=1976207&lang=2&reg=3
   - Official release explicitly states August 2023 underwent first revision (lines 25–26); Statement IV Aug-23 column is shown at lines 289–314.
   - Statement II in PRID 1976207 is September Quick and was not used for August First Revision.

## Test performed
For each of the 14 ledger keys:
- Compare ledger `quick_value` to PRID 1967120 Statement II Aug'23*.
- Compare ledger `first_revision_value` to PRID 1976207 Statement IV Aug-23.
- Recompute `revision_delta = first_revision - quick` at published 0.1 precision.

## Results
- Quick-side official cell matches: **14/14**.
- First-Revision-side official cell matches: **14/14**.
- Recomputed revision-delta matches: **14/14**.
- Unique transition keys: **14/14**; duplicate keys: 0.
- Mismatches: 0; missing/ambiguous cells: 0.
- Every row result: `PASS_CELL_AND_DELTA`.

## Scope and caveats
- This certifies only the 14 Batch 007 rows present in the recovered master ledger. It does not certify omitted NIC-2 codes, full cohort universe coverage, original XLSX binary provenance, or legacy ledger CSV hash-drift quarantine.
- Do not modify the 693-row master ledger in place; evidence is append-only.
- Batch 006 result remains separately recorded; Batch 008 (20 rows) is still pending.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, and A/B/C/D/E unchanged. UNKNOWN remains neither PASS nor FAIL. No synthetic rows, inferred values, hash overwrite, or Hard Gate relaxation. Spend ₹0; official free sources only.

## Artifact
- Row-level CSV: `research/evidence/iip/IIP_BATCH_007_PIB_CELL_CROSSWALK_2026-11-08.csv`
- CSV byte SHA-256: `02ddbcd0c780b59dc8f4a64e5c697709c9b653bfe4926e898ac8af88cd79d63f`
- 14 rows + header; values at one decimal.
