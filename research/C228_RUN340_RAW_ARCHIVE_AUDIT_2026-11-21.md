# C228 Run 340 Raw NSE Archive Audit — 2026-11-21

## Scope
Audit-only evidence record for workflow run 340 / run ID 44932899263 on branch `audit/prospective-selector-tracking`, head commit `46f4a359f21da676cb0c92e874fb08f14ee20d90`. This note does not modify the production selector, ranking score, pressure-fade logic, CORE-672 diagnostics, or trading gates.

## Verified artifact
- Workflow: Audit-only Prospective Watchlist Tracking
- Run: 340 (ID `44932899263`), conclusion: **FAILURE**
- Artifact: `prospective-watchlist-audit`, ID `14717569712`
- Artifact ZIP size: 30,814,565 bytes
- Artifact ZIP SHA-256: `959831b1a3d94350c06ca9c847f4166f9f33a9c760ec35169b90ed57653edb6a`
- Artifact file count: 212
- Raw NSE CSV count: **200**
- Each of the 200 raw CSVs is non-empty (>1,000 bytes) and has a SYMBOL header.
- `data/raw/acquisition_diagnostics.json`: requested_sessions=200, valid_sessions=200, date range 2026-02-16 through 2026-11-20.
- `data/qa/qa_report.json`: status PASS; raw_files=200; sessions=200; processed_dates=200; symbols=2,999; delivery quantity coverage=100%; delivery percentage coverage=100%; issues=[].

## Failure isolation
The raw acquisition, normalized dataset build, and strict dataset QA steps completed successfully. The workflow then failed at `pipeline/quarterly_pdf_xbrl_metrics.py` with:
`ModuleNotFoundError: No module named 'pipeline'`
The subsequent steps were skipped. This is a Python package/import-path failure, not a raw NSE acquisition failure.

## C228 acceptance status
- Raw-file retention in Run 340 artifact: **PASS (200/200 verified)**.
- Dataset QA: **PASS** (as reported by the artifact).
- Acquisition-time per-file manifest with exact source URL, retrieval timestamp, byte count, and SHA-256: **NOT_DONE / BLOCKED**. The artifact contains `acquisition_diagnostics.json` but no acquisition manifest. The downloader logs do not establish which of the two fallback source URLs succeeded for each file, so source URLs and acquisition timestamps must not be reconstructed or fabricated retrospectively.
- Run 339 and Run 416 evidence remains unchanged; this Run 340 evidence does not prove that their missing raw bytes were recovered.

## Next exact work
1. Update the collector to record the successful response URL, UTC retrieval timestamp, downloaded source-byte count, and source SHA-256 at the moment each raw file is acquired.
2. Emit a per-file acquisition manifest and verify every manifest row against the retained raw file.
3. Correct the import-path invocation for `quarterly_pdf_xbrl_metrics.py` (for example, execute with repository root on PYTHONPATH), then run a bounded audit-only workflow.
4. Accept C228 only when the new artifact contains all 200 raw CSVs plus a complete, hash-verified acquisition-time manifest. Unknown provenance remains UNKNOWN, never PASS.

