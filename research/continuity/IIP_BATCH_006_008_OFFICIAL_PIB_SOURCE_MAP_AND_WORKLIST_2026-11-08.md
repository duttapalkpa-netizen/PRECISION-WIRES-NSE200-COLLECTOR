# IIP Batch 006-008 official PIB source map and row-level worklist — 2026-11-08

Status: SOURCE_IDENTITY_AND_WORKLIST_READY; OFFICIAL_CELL_CROSSWALK_PENDING.

## Input integrity
Input is the recovered Library master ledger version 1:
- 693 rows / 32 columns
- SHA-256: 1a1d065f9dba2408f1ef4b8cd06aed78306873ba318294694fe3ec6d8d37c247
- Selected 54 rows where batch_id = 006-008 and cell_verification_status = WORKBOOK_LEDGER_MATCH_ONLY_PIB_CELL_PENDING.
- No input values modified.

## Exact worklist and source map

| Ledger cohort | Period | Rows | NIC codes in ledger | Quick source / required table | First Revision source / required table |
|---|---|---:|---|---|---|
| Batch 006 | 2023-07 | 20 | 10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,32 | PIB PRID 1956663, Statement II (July 2023 Quick) | PIB PRID 1967120, Statement IV, Jul-23 column (July 2023 First Revision) |
| Batch 007 | 2023-08 | 14 | 10,11,14,15,17,18,20,22,23,24,25,26,28,32 | PIB PRID 1967120, Statement II (August 2023 Quick) | PIB PRID 1976207, Statement IV, Aug-23 column (August 2023 First Revision) |
| Batch 008 | 2023-09 | 20 | 10,11,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,31,32 | PIB PRID 1976207, Statement II (September 2023 Quick) | PIB PRID 1985484, Statement IV, Sep-23 column (September 2023 First Revision) |
| **Total** | | **54** | | | |

## Official PIB URLs and source-identity checks
1. Quick July 2023 — PRID 1956663: https://www.pib.gov.in/PressReleasePage.aspx?PRID=1956663&lang=2&reg=3
   - Official page title identifies Quick Estimates for July 2023, posted 12 Sep 2023.
   - Statement II contains NIC-2008 2-digit July 2023 index.
2. First Revision July 2023 / Quick August 2023 — PRID 1967120: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=1967120&lang=2&reg=48
   - Official page identifies August 2023 Quick Estimates and explicitly states July 2023 underwent first revision.
   - Statement IV includes month-wise NIC-2008 indices; use Jul-23 column for Batch 006 First Revision.
3. Quick September 2023 / First Revision August 2023 — PRID 1976207: https://www.pib.gov.in/PressReleasePage.aspx?PRID=1976207&lang=2&reg=3
   - Official page identifies September 2023 Quick Estimates and explicitly states August 2023 underwent first revision.
   - Statement II is September Quick; Statement IV Aug-23 column is August First Revision.
4. First Revision September 2023 / Quick October 2023 — PRID 1985484: https://www.pib.gov.in/PressReleasePage.aspx?PRID=1985484&lang=2&reg=48
   - Official page identifies October 2023 Quick Estimates and explicitly states September 2023 underwent first revision.
   - Statement IV Sep-23 column is September First Revision.

## Source identity result
- Four official PIB pages successfully opened and their release/month identity confirmed.
- Correct Statement selection is critical: Quick values are in Statement II of the release for that month; First Revision values are in Statement IV of the following month's release.
- Do not mistakenly compare a Quick value with the following release's Statement II (that would be the next month's Quick index).
- No full 54+54 cell value comparison is claimed in this report.
- NIC code membership is ledger-derived and cohort-specific; it is not asserted to equal the full NIC-2 universe.
- Source-page availability does not validate the ledger's declared workbook hashes or original workbook binaries.

## Next cell-level execution boundary
Execute the 20 Batch 006 NIC rows first, pairing July 2023 Quick Statement II (PRID 1956663) with July 2023 First Revision in Statement IV (PRID 1967120). For each NIC, compare both stored values and recompute First Revision minus Quick against revision_delta at published 0.1 precision. Record row-level results in a new append-only artifact. If any table value is inaccessible/ambiguous, leave that row PENDING; never infer or fill.

## Progress
- Recovered master ledger identity/hash: 100% (prior checkpoint).
- Batch 006-008 exact cohort extraction and grouping: 100%.
- Official PIB release identity and statement mapping: 100%.
- Batch 006-008 two-sided cell comparison: 0% completed in this task; pending.
- Batch 006 first crosswalk: READY TO EXECUTE; not PASS.
- Overall IIP source audit / Master Hard Gate: BLOCKED.

## Controls
No synthetic rows, fabricated timestamps, inferred values, hash overwrites, unsupported PASS promotion, or Hard Gate relaxation. UNKNOWN is neither PASS nor FAIL. Prior 001-005 and Batch 014 work not repeated. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and A/B/C/D/E unchanged. ₹0 spend; official free sources only.
