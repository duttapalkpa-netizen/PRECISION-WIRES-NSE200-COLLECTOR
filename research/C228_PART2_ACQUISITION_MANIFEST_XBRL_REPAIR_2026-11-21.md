# C228 Part 2 — Acquisition Manifest and XBRL Invocation Repair
Date: 2026-11-21 (Asia/Kolkata)
Branch: \`audit/prospective-selector-tracking\`
Scope: audit-only repair; no production selector, ranking, pressure-fade, CORE-672, engine A–E, or trading-gate changes.

## Preflight and evidence reused
- Re-opened the main-branch continuity acceptance ledger and the 2026-11-21 nightly research review before selecting work.
- Reused C228 Run 340 audit record: \`research/C228_RUN340_RAW_ARCHIVE_AUDIT_2026-11-21.md\`.
- Run 340 / ID \`44932899263\`; artifact \`14717569712\`; retained raw CSV count 200; raw-data QA reported PASS, while the workflow failed later at the quarterly XBRL extractor with \`ModuleNotFoundError: No module named 'pipeline'\`.
- Existing collector did not retain per-file contemporaneous source URL, UTC retrieval time, downloaded source byte count and source SHA-256. Cached files were recorded only as \`CACHED\`.
- Prior raw archive artifact hashes and Run 339/416 limitations were not re-labelled or upgraded.

## Implemented changes
1. \`collector/nse_download.py\`
   - Captures the actual final response URL and requested URL for successful Full Bhavcopy, UDiFF ZIP and legacy CSV downloads.
   - Captures UTC retrieval timestamp, downloaded source byte count, source content type and SHA-256 at acquisition time.
   - Separately hashes and sizes the retained CSV file. This matters because UDiFF ZIP source bytes are normalized into a CSV; source hash and retained-file hash are different evidence objects.
   - Writes \`data/raw/acquisition_manifest.json\` with one entry per valid session.
   - Existing cache files receive \`UNKNOWN_PREEXISTING_CACHE\` / \`UNKNOWN\`; no source URL or timestamp is reconstructed retrospectively.
2. \`qa/validate_acquisition_manifest.py\`
   - Requires exactly 200 manifest rows and exact agreement with \`sessions.txt\`.
   - Recomputes each retained file's byte count and SHA-256.
   - Requires HTTPS source URL, valid UTC-aware retrieval timestamp, positive source byte count and 64-character source SHA-256.
   - Fails closed when any row is cached/unknown or provenance is incomplete.
3. \`qa/test_acquisition_manifest.py\`
   - Tests the distinction between cached/unknown provenance and fresh acquisition provenance.
   - Tests separate source-payload and retained-CSV hashes.
4. \`.github/workflows/prospective_watchlist_tracking.yml\`
   - Runs the strict manifest validator immediately after NSE acquisition.
   - Includes the acquisition manifest and validation report in the artifact.
   - Invokes the quarterly XBRL extractor as \`python -m pipeline.quarterly_pdf_xbrl_metrics\`, ensuring repository-root module resolution instead of script-directory resolution.

## Commits written
- Collector provenance implementation: \`11e8aa5d004a31b6792ea2ade24d53fc80d3b625\`
- XBRL module invocation + artifact retention: \`49cc3ce001f1545647969caa28eab96418311f6e\`
- Manifest newline serialization correction: \`e409c703023d819e4f0874f73d6e9e7bce8c8d58\`
- Strict manifest validator: \`8fc54209b3a83c444db2645daadd389b449a20e7\`
- Workflow manifest gate: \`5291e5ab9462632175cd08aad05a1dce91e6e520\`
- Fresh/cache provenance unit tests: \`4a2cf59d773cfbcbd02bd25fb07afab033c7bd77\`

## Validation status
- Code and workflow files re-fetched from the audit branch after edits: PASS.
- Manifest newline serialization inspected: PASS.
- Strict validator and two unit tests committed: PASS (tests are committed; execution result not yet observed).
- GitHub Actions execution and artifact inspection: PENDING / UNKNOWN. No run ID or artifact hash is claimed for this repair.
- C228 acceptance: OPEN. It becomes PASS only after a workflow artifact proves 200/200 raw CSVs, 200/200 fully-provenanced manifest entries, retained-byte/hash parity, successful unit tests, and the XBRL step no longer fails at import.

## Learned failure-prevention rules
- Never treat a cached historical file as proof of its original acquisition URL or timestamp.
- Keep source-payload SHA-256 separate from the normalized/retained-file SHA-256.
- A manifest generator is not sufficient: an independent validator must reopen each retained file and recompute size/hash.
- Python package scripts should be invoked as modules from repository root when package resolution is required.
- Do not mark workflow PASS based only on earlier raw-data QA; downstream job failures remain workflow failures.
- Do not promote UNKNOWN provenance to PASS and do not modify protected production invariants.

## Next action
Inspect the first workflow run triggered by these audit-branch commits, retrieve its jobs/logs/artifact, and repair only the first new evidenced blocker. If any cached rows remain UNKNOWN, keep C228 BLOCKED rather than fabricating provenance.
