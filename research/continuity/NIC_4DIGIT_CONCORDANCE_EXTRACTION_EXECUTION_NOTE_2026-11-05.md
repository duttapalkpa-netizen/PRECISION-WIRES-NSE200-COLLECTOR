# NIC-2025 / NIC-2008 Concordance Extraction — Research Execution Note
Date: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean

## New source-grounded finding
MoSPI's official NIC-2025 PDF contains a 4-digit NIC-2025 ↔ NIC-2008 concordance table on printed pages 232–238. The table explicitly defines `(p)` as part and `+` as aggregation of classes. NIC-2025 contains 463 four-digit classes; NIC-2008 contains 403 four-digit classes. These counts are official publication totals, not counts independently extracted from the concordance.

## Extraction implementation committed
- `pipeline/extract_nic_4digit_concordance.py` extracts the concordance from the downloaded official PDF, retains the original NIC-2008 expression verbatim after whitespace normalization, stores page provenance and source PDF SHA-256, classifies direct / partial / aggregation / mixed rows, and emits CSV plus JSON QA report.
- The extractor fails closed if the PDF is missing, heading is missing, no rows are extracted, a NIC-2025 code is duplicated, or the final unique row count is not exactly 463.
- The CSV is not treated as proof of 2-digit IIP comparability. NIC-2 roll-up remains explicitly NOT CERTIFIED because partial and aggregated mappings are not one-to-one and the earlier official IIP series-break evidence only supports general/sector-level linking factors.

## Workflow updated
- `.github/workflows/nic_concordance_source_acquisition.yml` now installs `openpyxl` and `pymupdf`, runs source acquisition/hash, then runs the PDF concordance extractor, and uploads all raw files and audit outputs.
- Workflow timeout remains 10 minutes; manual dispatch only; no production workflow is triggered by push.

## Read-back verification
- Extractor blob SHA: `7ea2939db7fc8176296940ac5b949443c002824e`.
- Workflow blob SHA: `70b357764969efbac221cf0da99b63ab9560b574`.
- Workflow update commit: `2ee06810134bfc4d59a6b14e7339467840ecfe95`.
- Both files were fetched back from the target GitHub branch and their content was verified.

## What is not claimed
- No GitHub Actions run was dispatched in this session; the current GitHub tool connection does not expose workflow dispatch.
- No raw PDF or XLSX binary was acquired in this session, and no source binary SHA-256 is claimed.
- The 463-row concordance CSV has not yet been generated or independently validated; that requires the manual Actions run and its artifact.
- NIC-2 roll-up, new-series March 2024 cell reconciliation, Batch014 full provenance and Master Hard Gate remain BLOCKED.

## Next execution
Run Actions > Official NIC Concordance Source Acquisition and Extraction > Run workflow on `fix/iip-41-vintage-audit-clean`. Review `nic_concordance_extraction_audit.json`: require status PASS, 463 rows, 463 unique codes, no duplicates, then inspect the CSV and compare every extracted raw mapping expression against the official PDF table. Only after independent row-by-row reconciliation may the 4-digit concordance be certified. NIC-2 mapping must remain separate and not inferred by dropping trailing digits.

## Protected invariants
Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, and V11.3(A/B/C/D/E) remain unchanged. No historical PASS evidence was deleted or rewritten. No synthetic rows, fabricated timestamps, unsupported source promotion, or Hard Gate relaxation.