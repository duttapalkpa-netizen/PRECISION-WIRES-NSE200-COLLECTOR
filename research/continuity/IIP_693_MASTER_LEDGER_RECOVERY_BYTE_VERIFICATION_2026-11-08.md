# IIP 693-candidate master ledger recovery and byte verification — 2026-11-08

## Result
Status: MASTER_LEDGER_RECOVERED_AND_BYTE_HASH_VERIFIED; ROW_POPULATION_QA_PASS; CELL_CERTIFICATION_NOT_COMPLETE.

The canonical file was found in the user's ChatGPT Library, not in the inspected Git branch tree:
- Name: `IIP_693_POLICY_ALIGNED_CANDIDATE_MASTER_LEDGER.csv`
- Library file ID: `libfile_90de2e0fd5988191a0de5d406069ba62`
- File ID: `file_000000000280821181783273200a01f8`
- Version: `1`
- Library created: `2026-11-03T18:49:17.524408+00:00`
- Size: `566796` bytes
- Independently computed SHA-256 from materialized raw bytes: `1a1d065f9dba2408f1ef4b8cd06aed78306873ba318294694fe3ec6d8d37c247`

The byte count and SHA-256 exactly match the immutable Batch 014 input declaration. This resolves the earlier *durable location/current version/hash unavailable* gap. It does not imply that the file is present in the current Git branch; the prior 159-path branch-tree inspection remains accurate for that branch snapshot.

## Independent CSV population QA
- Data rows: 693
- Columns: 32
- Unique transition keys `(period, quick_table_id, first_revision_table_id, nic_code)`: 693
- Duplicate transition keys: 0
- Batch 001: 9 rows
- Batch 002: 6 rows
- Batch 003: 5 rows
- Batch 004: 14 rows
- Batch 005: 20 rows
- Batch 006-008: 54 rows
- Blank batch_id: 585 rows
- Cell status counts:
  - `PIB_CELL_CERTIFIED_PRIOR_BATCH`: 54
  - `WORKBOOK_LEDGER_MATCH_ONLY_PIB_CELL_PENDING`: 54
  - `NOT_YET_BATCH_RECONCILED`: 585
- Two-sided PIB match field:
  - YES: 54
  - NO_PENDING: 639

## Correct interpretation
The 54 rows in Batches 001-005 are the previously recorded bounded source-cell certifications, retained with the separate legacy CSV hash-drift quarantine described in the 2026-11-08 evidence reconciliation.

The 54 rows labelled Batch 006-008 are *not* PIB-cell-certified: the ledger explicitly labels them `WORKBOOK_LEDGER_MATCH_ONLY_PIB_CELL_PENDING` and `NO_PENDING`. They remain part of the 639 pending policy-stage candidate rows. The remaining 585 rows have blank batch_id and are `NOT_YET_BATCH_RECONCILED`.

Thus the 693 denominator reconciles as:
- 54 prior bounded PIB-cell certifications (Batches 001-005)
- 54 Batch 006-008 workbook/ledger matches awaiting PIB cell crosswalk
- 585 not yet batch-reconciled
- 639 remaining PIB-cell candidates = 54 + 585
- Separate historical-panel/out-of-window population: 431
- Total observed differences: 1,124 = 693 + 431

No row-level PIB cell certification is granted by this recovery/structural QA. Batch 006 remains a final-paper acceptance requirement; do not mark it PASS based on the ledger's workbook/ledger-only label.

## Integrity and limitations
- Raw byte hash was computed after materializing the exact Library version; hash and size match the prior Batch 014 declaration.
- No rows or values were changed; no new ledger was synthesized.
- The Library copy is the recovered canonical source candidate. Git branch inclusion is still absent in the inspected tree; do not silently copy or overwrite it into the branch.
- This verification did not independently re-fetch source workbooks, reperform PIB comparisons, validate workbook binary hashes for every row, or reconcile all 639 pending rows.
- Legacy CSV hash drift for Batches 001, 003, 004, 005 remains separately quarantined; this master-ledger hash match does not clear that quarantine.
- Batch 014 full provenance remains BLOCKED as previously recorded; the matching hash here verifies the ledger bytes used, not its source workbook or PDF bytes.

## Progress
- Locate canonical ledger in Library: 100%.
- Recover exact raw bytes and verify size/SHA-256: 100%.
- Structural population/key uniqueness QA: 100%.
- 693-row official PIB cell reconciliation: 54/693 bounded rows historically recorded; 639/693 pending (not a percentage-based PASS claim).
- Batch 006 two-sided PIB crosswalk: PENDING.
- IIP full vintage audit / Master Hard Gate: BLOCKED.

## Invariants
No synthetic rows, fabricated timestamps, inferred IDs, unsupported source promotion, legacy hash overwrite, or Hard Gate relaxation. UNKNOWN is neither PASS nor FAIL. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and A/B/C/D/E production logic unchanged. Research spend ₹0; free official sources only.
