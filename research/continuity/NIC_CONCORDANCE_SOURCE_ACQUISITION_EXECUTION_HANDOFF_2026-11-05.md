# NIC Concordance Source Acquisition — Execution Handoff
Date: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean

## Objective
Create a bounded, reproducible route to obtain the official NIC-2025 workbook, NIC-2008 workbook and NIC-2025 final PDF, compute SHA-256 over downloaded raw bytes, and inventory workbook sheets without modifying any production data.

## Official source endpoints configured
- NIC-2025 XLSX: https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763618655097_29a4a622-fa4c-47e9-abba-b549e27a1bbb_NIC_2025.xlsx
- NIC-2008 XLSX: https://www.mospi.gov.in/uploads/documents/publicDocuments/1760616763355-NIC_2008.xlsx
- NIC-2025 final PDF: https://www.mospi.gov.in/sites/default/files/main_menu/national_industrial_classification/NIC_2025Final_18112025.pdf
- NIC-2025 PDF confirms the official 4-digit concordance section is pages 232–238; (p) and + are source-defined mapping markers.

## New execution assets
1. pipeline/acquire_nic_official_sources.py
   - Three bounded attempts per source; 35-second connection/read timeout per attempt.
   - Downloads into artifacts/nic_concordance_audit/raw/.
   - Computes SHA-256 from raw downloaded bytes and records byte size.
   - Inventories workbook sheet names, dimensions and first five rows.
   - Writes nic_source_sha256_and_workbook_inventory.json.
   - Overall status is PASS only if all three official sources are downloaded; otherwise BLOCKED_WITH_SOURCE_ACCESS_GAPS.
2. .github/workflows/nic_concordance_source_acquisition.yml
   - workflow_dispatch only; no push trigger.
   - 10-minute job timeout.
   - uploads raw files and manifest as a run artifact with 90-day retention.

## Verification performed in this turn
- Both new files were committed to the target branch and fetched back from GitHub.
- Script blob SHA: c1803061589c8d4b8107e00ac4def444ab15c3d7.
- Workflow blob SHA: fc4ec0d50cb6c838934b345b01e66685200282ee.
- Script and workflow content round-trip verified.

## Execution limitation / honest status
The available GitHub connection in this session supports repository file reads/writes and workflow-run/artifact reads, but does not expose a workflow-dispatch action. Therefore this session did not start a GitHub Actions run and did not obtain the binary files or calculate their SHA-256 values. The workflow is committed and ready for manual dispatch from GitHub Actions. No run ID or artifact ID is claimed.

## Next exact operation
Manually run Actions > Official NIC Concordance Source Acquisition > Run workflow on branch fix/iip-41-vintage-audit-clean. After completion, inspect the uploaded manifest and raw binaries; only then parse the workbook concordance sheet and independently reconcile it against the PDF table on pages 232–238. Do not mark concordance extraction or NIC-2 roll-up PASS until row counts, unique codes, partial markers, aggregation expressions, missing/duplicate codes and code-set coverage are independently checked.

## Status
OFFICIAL_SOURCE_ENDPOINTS: CONFIGURED
ACQUISITION_SCRIPT: COMMITTED_AND_READBACK_VERIFIED
10_MINUTE_WORKFLOW: COMMITTED_AND_READBACK_VERIFIED
WORKFLOW_RUN: NOT_DISPATCHED_FROM_THIS_SESSION
RAW_SOURCE_SHA256: PENDING
FULL_CONCORDANCE_EXTRACTION: PENDING
NIC2_ROLLUP_AUDIT: PENDING
BATCH014_FULL_PROVENANCE: BLOCKED
MASTER_HARD_GATE: BLOCKED

## Invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or V11.3(A/B/C/D/E) logic changed. No historical PASS evidence deleted or rewritten. No synthetic rows, fabricated timestamps, unsupported source promotion, or hard-gate relaxation.