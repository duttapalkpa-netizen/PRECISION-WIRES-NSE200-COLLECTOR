# Continuation 26B — Batch 006 PIB cell crosswalk completed (2026-11-08)

Continuation page: গবেষণা যাচাই অব্যাহত 26

## Completed task
Executed the next non-duplicative high-value task from Continuation 26: exact two-sided official PIB cell crosswalk for Batch 006 (July 2023).

### Source evidence
- Quick: PIB PRID 1956663, Statement II, Jul'23* index column.
  URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=1956663&lang=2&reg=3
  Source identity/month confirmed; NIC-2 rows visible in Statement II.
- First Revision: PIB PRID 1967120, Statement IV, Jul-23 column.
  URL: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=1967120&lang=2&reg=48
  Release explicitly states July 2023 underwent first revision; Statement IV Jul-23 column used, not Statement II (which is August Quick).

### Input
- Canonical master ledger: 693 rows × 32 columns.
- SHA-256: 1a1d065f9dba2408f1ef4b8cd06aed78306873ba318294694fe3ec6d8d37c247
- Batch 006: 20 unique NIC rows: 10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,32.
- Ledger was read-only; not edited.

### Exact test and result
For all 20 rows:
1. ledger Quick value vs PIB PRID 1956663 Statement II Jul'23*: 20/20 match.
2. ledger First Revision value vs PIB PRID 1967120 Statement IV Jul-23: 20/20 match.
3. recomputed First Revision minus Quick at published 0.1 precision vs ledger revision_delta: 20/20 match.
4. Duplicate keys: 0; missing/ambiguous source cells: 0; mismatches: 0.
Bounded outcome: PASS_CELL_CROSSWALK_20_OF_20. This is not a full NIC-2 universe certification.

### Append-only artifacts (read-back verified)
1. Row-level CSV:
   Path: research/evidence/iip/IIP_BATCH_006_PIB_CELL_CROSSWALK_2026-11-08.csv
   GitHub commit: d1f97666c21f879b851c37cd2c99b62d282988a1
   Git blob SHA: 94845d80f062f499fd474f1f1def2340bcbc84bd
   CSV byte SHA-256: 0f72c43f1270f276d39cd0d947a0805ab12b501a3b6e25c22a4a0e04a62a04ea
   URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/fix/iip-41-vintage-audit-clean/research/evidence/iip/IIP_BATCH_006_PIB_CELL_CROSSWALK_2026-11-08.csv
2. Report:
   Path: research/continuity/IIP_BATCH_006_PIB_CELL_CROSSWALK_REPORT_2026-11-08.md
   GitHub commit: 9a2cc82d59e0c7974253a0e83658e12fa1a0debf
   Git blob SHA: ee4899f258b51b55c7267fda2bc5bc6c19e42597
   URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/fix/iip-41-vintage-audit-clean/research/continuity/IIP_BATCH_006_PIB_CELL_CROSSWALK_REPORT_2026-11-08.md

### Progress
- This bounded task (Batch 006 20-row two-sided cell crosswalk): 100% complete.
- Batch 006–008 combined crosswalk: 20/54 rows completed = 37.04%; remaining 34 rows (Batch 007 14 + Batch 008 20) pending.
- IIP 693-row reconciliation: 54 previously bounded rows in Batch 001–005, plus Batch 006 now independently crosswalked in a separate append-only artifact. Do not silently update master ledger statuses or erase prior CSV hash-drift quarantine.
- Overall PRECISION-WIRES V11.3 research percentage: NOT CERTIFIABLE from current evidence. Master Acceptance Register V1 has 721 evidence/status rows, and full status reconciliation remains incomplete. Historical 36% is stale and must not be presented as current.
- Overall IIP source audit / Master Hard Gate remains BLOCKED; Batch 006 bounded cell test does not clear workbook binary provenance, legacy ledger hash-drift quarantine, Batch 007/008, remaining 639 candidates, 431 historical/out-of-window rows, or other final-paper gates.

### Invariants and controls
Production selector, RANKING_SCORE, +1 PRESSURE_FADE, 56×12 CORE-672, and V11.3 A/B/C/D/E unchanged. UNKNOWN is neither PASS nor FAIL. No synthetic rows, fabricated timestamps, inferred values, unsupported source promotion, hash overwrite, or Hard Gate relaxation. No main merge/automation. ₹0 spend; official free sources only. Keep old PASS artifacts and run IDs.

### Next task
Continue with Batch 007 (August 2023) exact two-sided PIB cell crosswalk: Quick = PRID 1967120 Statement II Aug'23*; First Revision = PRID 1976207 Statement IV Aug-23 column. Do not repeat Batch 006.
