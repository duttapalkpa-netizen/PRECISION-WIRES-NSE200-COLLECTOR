# IIP Batch 006 — two-sided official PIB cell crosswalk (2026-11-08)

Status: **PASS_CELL_CROSSWALK_20_OF_20** (bounded to the 20 NIC rows present in Batch 006; not a full NIC-2 universe certification).

## Inputs and integrity
- Canonical master ledger: `IIP_693_POLICY_ALIGNED_CANDIDATE_MASTER_LEDGER.csv`
- Ledger SHA-256: `1a1d065f9dba2408f1ef4b8cd06aed78306873ba318294694fe3ec6d8d37c247`
- Rows selected: period `2023-07`, batch `006-008`, 20 unique NIC codes: 10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,32.
- Input ledger was read-only; no source values or prior artifacts were changed.

## Official source evidence
1. July 2023 Quick Estimates, PIB PRID 1956663, Statement II, Jul'23* index column: https://www.pib.gov.in/PressReleasePage.aspx?PRID=1956663&lang=2&reg=3
   - PIB lines 14–25 identify July 2023 Quick release; lines 64–91 contain NIC-2 Statement II and the July 2023 index column.
2. August 2023 release, PIB PRID 1967120, Statement IV, Jul-23 column: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=1967120&lang=2&reg=48
   - PIB lines 81–82 explicitly state July 2023 underwent first revision; lines 347–373 contain Statement IV with Jul-23 column for the required NIC codes.
   - Correct vintage mapping: Statement IV Jul-23 is July First Revision; Statement II of PRID 1967120 is August Quick and was not used for this crosswalk.

## Test performed
For each of the 20 ledger keys:
- Compare ledger `quick_value` to official PRID 1956663 Statement II Jul'23*.
- Compare ledger `first_revision_value` to official PRID 1967120 Statement IV Jul-23.
- Recompute `revision_delta = first_revision - quick` at published one-decimal precision.
- No rounding beyond the published 0.1 index precision.

## Results
- Quick-side official cell matches: **20/20**.
- First-Revision-side official cell matches: **20/20**.
- Recomputed revision-delta matches: **20/20**.
- Unique transition keys: **20/20**; duplicate keys: 0.
- Mismatches: 0.
- Missing/ambiguous source cells: 0.
- Row status: all 20 `PASS_CELL_AND_DELTA`.

## Scope and caveats
- This certifies only the 20 Batch 006 rows in the recovered master ledger. It does not certify omitted NIC-2 codes, full cohort universe coverage, original XLSX binary provenance, or the ledger's legacy CSV hash-drift quarantine.
- The source page and cell crosswalk do not independently verify original workbook payload hashes.
- Do not modify the 693-row master ledger in place; evidence is append-only. The 54-row Batch 006–008 pending cohort is not wholly certified by this Batch 006 result.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, and A/B/C/D/E unchanged. UNKNOWN remains neither PASS nor FAIL. No synthetic data, no inferred values, no Hard Gate relaxation. Spend ₹0; official free sources only.

## Artifact
- Row-level CSV: `research/evidence/iip/IIP_BATCH_006_PIB_CELL_CROSSWALK_2026-11-08.csv`
- CSV SHA-256: `0f72c43f1270f276d39cd0d947a0805ab12b501a3b6e25c22a4a0e04a62a04ea`
- 20 rows + header; values recorded to one decimal.
