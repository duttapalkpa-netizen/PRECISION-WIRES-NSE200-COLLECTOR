# Global Capital Rotation — Automated H.10/FRED Capture Implementation
Date: 2026-11-17 (Asia/Kolkata)
Status: IMPLEMENTED AND FETCH-VERIFIED; FIRST RUN IN PROGRESS AT CHECKPOINT

## Prior evidence reused; not repeated
- Existing H.10 raw capture #8 / run 44036104490 and SHA-256 c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77.
- Existing 5-date preview match, 72-test suite, 2019 re-indexing analysis, DDP/FRED crosswalk schema, H.10 current-release base-unit check, and failed manual runtime downloads.
- Existing source lifecycle finding: H.10 XML is overwritten with current revisions; previous vintages must be archived at retrieval time.

## New implementation
- Added scripts/capture_h10_fred_raw_sources.py. It downloads three official/public sources with Python stdlib urllib: Board H.10 XML ZIP, FRED DTWEXBGS public graph CSV, and Board DDP/FRED crosswalk CSV.
- Preserves raw response bytes before parsing; records final URL, HTTP status, content type, content-length header, UTC retrieval timestamp, byte length and SHA-256.
- Checks FRED CSV schema/date coverage; checks crosswalk target row uniqueness for H10/H10/JRXWTFB_N.B -> DTWEXBGS; validates ZIP integrity and records members.
- Missing FRED values remain blank/dot; no forward-fill or zero substitution.
- Added .github/workflows/h10_fred_raw_capture.yml with 5-minute timeout and 90-day artifact retention.
- Integrated capture job into existing Global Capital Rotation overlay test workflow so a push on the research branch triggers a byte-capable GitHub Actions runner.

## GitHub implementation evidence
- Branch: research/taxonomy-crosswalk-contract-20261117.
- Capture script commit: 3f6e5ecd523ec39d998d0e8176905fe6466fd0d2; verified blob: b07b6f52f41097da975fbe700c0767e00ac6aa7e.
- Standalone workflow commit: 516b22bbae7cfa92d4b658a9335ab4ba352a358f.
- Existing overlay workflow integration commit: 7f21fbcc0102654823a82efae7c35e3b21ab454a; verified workflow blob: f5b1503e5cb4fa8c8a214c8c150716923b53f64d.
- Standalone capture workflow run #1 / Run ID 44059623660: in_progress at checkpoint; job 133957796299 was downloading raw sources. No conclusion or artifact SHA is claimed yet.
- Overlay regression workflow run #236 / Run ID 44059652999: queued at checkpoint.

## Acceptance status at checkpoint
- Capture utility implementation: PASS (code committed and re-fetched).
- Workflow implementation: PASS (workflow committed and re-fetched).
- Raw H.10 ZIP capture: IN_PROGRESS / NOT_YET_VERIFIED.
- Raw FRED CSV capture: IN_PROGRESS / NOT_YET_VERIFIED.
- Crosswalk exact mapping row: IN_PROGRESS / NOT_YET_VERIFIED.
- Raw SHA-256 manifest and ZIP integrity: NOT_YET_VERIFIED.
- Full daily H.10/FRED comparison: NOT_RUN (capture utility deliberately does not claim equivalence).
- Vintage/revision archive: NOT_DONE; current run artifact retention is 90 days only.
- Registry/collector migration: BLOCKED / NOT_AUTHORIZED.

## Known implementation boundaries
- The action stores raw files and manifest in a 90-day artifact, not a permanent archive. A later durable archival decision is needed; do not claim long-term retention.
- This first utility checks the FRED CSV and crosswalk row and ZIP integrity, but does not yet extract/normalize the H.10 XML observations or execute full-history date/value reconciliation.
- A crosswalk mapping match is a separate identity gate, not proof that every historical value/revision matches.

## Next actions
1. Wait for run 44059623660 to finish; download artifact and verify all three raw file hashes against capture_manifest.json.
2. If capture is partial, inspect job logs and fix only the failed endpoint; do not rerun already verified source captures unnecessarily.
3. Parse the H.10 XML target series and reconcile all overlapping dates with FRED, preserving ND/missingness and duplicate-date checks.
4. Add revision/vintage snapshots and a durable archive strategy before any production migration.

## Invariants
Research-only. No production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN never PASS. No synthetic values, fabricated timestamps or hashes. ₹0 spend.