# IIP acceptance evidence reconciliation — batches 001–005, Batch 014, and 693/431 accounting
Date: 2026-11-08
Branch: fix/iip-41-vintage-audit-clean
Status: RECONCILED_WITH_QUARANTINE; IIP HARD GATE BLOCKED

## Purpose
This is a no-rerun evidence reconciliation of existing committed reports. It corrects ambiguous summaries without changing any historic ledger, source value, hash declaration, production input, or gate.

## Batch 001–005: correct interpretation
The batch-specific reports/summaries record **54 bounded source-cell certifications**, not merely 54 structural rows:
- Batch 001: 9 cells; 18/18 workbook-cell and PIB statement value comparisons.
- Batch 002: 6 cells; exact workbook/PIB matches.
- Batch 003: 5 cells; exact workbook/PIB matches.
- Batch 004: 14 cells; exact two-sided workbook/PIB matches.
- Batch 005: 20 cells; exact two-sided workbook/PIB matches.
- Total: 54 unique transition keys; zero reported cell mismatches.

The original source workbook payload hashes for the four distinct XLSX vintages were independently rechecked against immutable Run 41640521553 / Artifact 13232127900 (ZIP SHA-256 e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c). The exact four workbook SHA-256 values are retained in the source binary verification report.

**Important integrity limitation:** the consolidated audit Run 42389793415 / outputs/audits/iip_certified_batches_001_005_integrity_2026-11-07.json reports 54 rows and 54 unique keys, but status PASS_WITH_HASH_DRIFT_QUARANTINED. Current committed CSV byte hashes differ from four legacy declared digests (batches 001, 003, 004, 005). Batch 002 has no declared summary hash. The mismatch investigation says the cause is not inferred; batch 001 may refer to a separate data/macro copy, but that mapping is not certified. Therefore:
- preserve the historic 54 bounded certifications as recorded;
- preserve and quarantine the affected ledger CSV digest mismatch;
- do not overwrite legacy digests or call the current consolidated ledger provenance fully clean;
- do not promote additional rows;
- do not reduce the 54 historical bounded certifications to "structural only"—that earlier summary was inaccurate;
- do not call the entire 693 candidate population certified.

## Corrected candidate accounting
- Original policy-stage-aligned candidate universe: 693 transitions.
- Existing bounded batch certifications: 54 unique rows (001–005).
- Remaining policy-stage candidates: 639 (=693−54).
- Historical-panel/out-of-window transitions unresolved: 431.
- Total observed differences: 1,124 (=693+431=54+639+431).
These counts are supported by IIP_POLICY_CANDIDATE_ACCOUNTING_RECONCILIATION_2026-11-07.md; they are not a claim that all 639/431 rows have been individually reviewed.

## Batch 014 — March 2024 cohort
Existing Batch 014 reports record 19/19 candidate NIC codes matched against both official PIB Quick and First Revision values, and 19/19 delta arithmetic. A separate PDF content crosscheck also reports 19/19 each side. However:
- original XLSX workbook binaries were not recovered in that pass;
- raw PDF binary SHA-256 was not acquired;
- full NIC-2 cohort coverage is UNKNOWN / out of scope;
- workbook declared hashes remain unverified;
- Batch 014 full provenance remains BLOCKED.
Do not combine Batch 014's 19-row cohort into the 693/54/639 population without a verified unique-key crosswalk and proof it belongs to the same denominator.

## Batch 006 and master-ledger availability
- Batch 006 two-sided PIB crosswalk remains a final-paper acceptance requirement; no Batch 006 evidence was located in the current branch tree during this reconciliation. Status: PENDING / NOT LOCATED IN CURRENT BRANCH TREE, not FAIL.
- The named IIP_693_POLICY_ALIGNED_CANDIDATE_MASTER_LEDGER.csv is referenced by Batch 014 documentation, but is not present in the current branch tree snapshot (157 paths inspected). Its durable location/current version and hash must be resolved before row-level 693 reconciliation can be certified.
- Do not infer that a file was deleted; this finding is limited to the inspected branch tree.

## Reconciliation outcome
- Historical bounded certifications 001–005: 54 recorded, preserved, with CSV-hash quarantine.
- Workbook binary identity for source vintages used in 001–005: PASS (4 distinct XLSX payloads).
- Consolidated current ledger byte integrity: QUARANTINED due to four declared/current hash mismatches.
- Candidate population accounting: reconciled (693 = 54 + 639; 1,124 = 693 + 431).
- Batch 014 PIB content crosswalk: PASS for its 19-row cohort only; full provenance BLOCKED.
- Batch 006: PENDING.
- 693 master ledger file availability in inspected branch: NOT LOCATED.
- IIP source audit and Master Hard Gate: BLOCKED.

## Exact source references
1. research/continuity/IIP_CELL_LEVEL_REVISION_BATCH_001_2023-04.md
2. research/continuity/IIP_CELL_LEVEL_REVISION_BATCH_001_SUMMARY.json
3. research/continuity/IIP_CELL_LEVEL_REVISION_BATCH_002_README.md and _SUMMARY.json
4. research/continuity/IIP_CELL_LEVEL_REVISION_BATCH_003_README.md and _SUMMARY.json
5. research/continuity/IIP_CELL_LEVEL_REVISION_BATCH_004_README.md and _SUMMARY.json
6. research/continuity/IIP_CELL_LEVEL_REVISION_BATCH_005_README.md and _SUMMARY.json
7. research/continuity/IIP_BATCHES_001_005_HASH_MISMATCH_INVESTIGATION_2026-11-07.md
8. research/continuity/IIP_BATCHES_001_005_SOURCE_WORKBOOK_BINARY_HASH_VERIFICATION_2026-11-07.md
9. research/continuity/IIP_POLICY_CANDIDATE_ACCOUNTING_RECONCILIATION_2026-11-07.md
10. outputs/audits/iip_certified_batches_001_005_integrity_2026-11-07.json
11. research/continuity/IIP_BATCH014_MARCH2024_OFFICIAL_PIB_TWO_SIDED_CELL_CROSSWALK_2026-11-05.md
12. research/continuity/IIP_BATCH014_MARCH2024_OFFICIAL_PDF_CONTENT_CROSSCHECK_2026-11-05.md

## Invariants
No source values, legacy digests, ledger bytes, or historical artifacts were overwritten. No synthetic rows, inferred IDs, fabricated timestamps, unsupported certification or Hard Gate relaxation. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and A/B/C/D/E production logic unchanged. ₹0 spend; free official sources only.
