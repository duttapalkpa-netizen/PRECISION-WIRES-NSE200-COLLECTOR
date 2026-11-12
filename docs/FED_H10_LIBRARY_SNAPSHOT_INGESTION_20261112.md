# Fed H.10 Library Snapshot Ingestion — 2026-11-12

## Scope
Research-only intake record for four user-provided Federal Reserve H.10 CSV snapshots located in ChatGPT Library. No production integration, selector/ranking change, or capital-flow inference.

## Verified snapshot contents
- Daily nominal dollar indices: 10 dates, 2026-10-26 through 2026-11-06; three series (Broad, Advanced Foreign Economies, Emerging Market Economies).
- Daily bilateral FX: 10 dates over the same period; 23 currency columns, including Indian Rupee (H10/H10/RXI_N.B.IN).
- Monthly nominal dollar indices: 120 months, 2016-11 through 2026-10.
- Monthly bilateral FX: 120 months, 2016-11 through 2026-10; 23 currency columns, including Indian Rupee (H10/H10/RXI_N.M.IN).

## Integrity and QA
All four original CSV byte streams were materialized from Library and hashed. SHA-256 values and byte sizes are in `data/global_capital_rotation/fed_h10/library_snapshot_manifest_20261112.json`. A ZIP archive containing the four unchanged CSV files was created and retained in the user's Library:
- Name: `fed_h10_library_raw_20261112.zip`
- Size: 15,322 bytes
- SHA-256: `59a79209a6602a6cf6bc2022f8361ee7d86a0817e2d01540fc4e8dafbad7421c`

CSV structural QA: consistent row widths, zero duplicate periods, zero missing numeric cells, zero nonnumeric observation cells; monthly periods contiguous. Daily files contain only 10 observations and must not be mistaken for a full daily historical panel.

## Provenance boundary
The files were supplied from the user's Library. The exact original download timestamp and per-file download URLs were not supplied, so direct Federal Reserve retrieval provenance remains UNKNOWN. The repository change records hashes and metadata but does not claim the raw ZIP binary has been committed into Git. The archive is currently retained in Library under file ID `file_00000000d80082118df044084445d454`.

## Interpretation constraints
- H.10 nominal dollar indices are FX price indices, not capital flows.
- Bilateral INR observations are H.10 spot exchange-rate series, not RBI reference rates.
- Do not substitute Fed Broad Dollar for ICE DXY.
- Do not forward-fill monthly observations into daily values.
- Keep missing source provenance UNKNOWN.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, or Hard Gate changes.

## Status
- Library snapshot integrity: PASS.
- CSV structural QA: PASS.
- Repository raw binary ingestion: PENDING (Library archive retained; binary ZIP not committed in this documentation-only change).
- Source provenance validation: PENDING.
- Daily observation panel and matched benchmark/event study: PENDING.
- Production integration: PROHIBITED without separate explicit approval.
