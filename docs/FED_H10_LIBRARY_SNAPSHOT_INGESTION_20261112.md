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


## Full-history daily panel recovery — 2026-11-12

### Successful workflow evidence
- Workflow: Fed H10 full-history daily dollar and INR panel
- Run ID: 43276577238
- Commit: 35c73345fc55c5c6f7e4de24da291061e9d0c19f
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43276577238
- Artifact ID: 13970661965
- Artifact name: fed-h10-full-history-daily-panel-20261112
- Artifact ZIP bytes: 3,462,888
- Artifact ZIP SHA-256: a6f6af42226ed689ceba8e9c2d843867d82e9aa8f9a7761022c86bd719ef3691
- Artifact was downloaded and the ZIP SHA-256 independently recomputed; it matches GitHub's artifact digest.
- All 26 raw CSV SHA-256 values were independently recomputed from the downloaded artifact and match its manifest.

### Full-history series coverage
The FRED public daily currency list identifies 23 daily bilateral currency series. The H.10 Library snapshot contains the matching 23 H.10 identifiers. The new collector maps those 23 series separately from the three modern nominal dollar indices:
- 3 dollar indices: DTWEXBGS, DTWEXAFEGS, DTWEXEMEGS.
- 23 bilateral FX series: DEXUSAL, DEXUSEU, DEXUSNZ, DEXUSUK, DEXBZUS, DEXCAUS, DEXCHUS, DEXDNUS, DEXHKUS, DEXINUS, DEXJPUS, DEXMAUS, DEXMXUS, DEXNOUS, DEXSFUS, DEXSIUS, DEXKOUS, DEXSLUS, DEXSDUS, DEXSZUS, DEXTAUS, DEXTHUS, DEXVZUS.

FRED's daily FX list identifies 23 daily currency series; FRED table metadata identifies the dollar-index and INR series as Board of Governors H.10 data. See:
- https://fredaccount.stlouisfed.org/public/datalist/737
- https://fred.stlouisfed.org/data/DEXINUS
- https://fred.stlouisfed.org/series/DTWEXBGS
- https://fred.stlouisfed.org/series/DTWEXAFEGS
- https://fred.stlouisfed.org/series/DTWEXEMEGS

### QA summary
- 26/26 series downloaded with HTTP 200 and source URLs retained.
- 26/26 raw byte streams SHA-256 verified.
- 304,510 total dated observation rows across the 26 series.
- 291,831 numeric observations.
- 12,679 original missing-value markers retained as blanks; no forward-fill or synthetic rows.
- Date union: 14,570 unique dates, 1971-01-04 through 2026-11-06.
- Each series has unique, strictly increasing dates and valid finite numeric values or preserved missing markers.
- Retrieval timestamp: 2026-11-12T18:09:04.918538+00:00.
- Long panel: 8,078,212 bytes; SHA-256 3f144536ccf1b7e4e5b9f96e0db57eed26cbded7c6ab9a6eff1fd1626afbbb2c.
- Wide panel: 2,199,281 bytes; SHA-256 04d4b7e7ec1997bdc2e069dbc501c1304ed03a601cce0720c41694f9c6e3c406.
- Daily panel manifest SHA-256: f009090fde78a034916a54e3db78a8ccd1276749b1b5f5d96b27e9b610617d3b.

### Important limitations retained
- FRED is the public distribution interface; the underlying source owner is the Board of Governors, H.10. FRED observations are revisable. This artifact is one retrieval snapshot, not a full ALFRED point-in-time vintage history.
- The four original user-provided CSVs still have unknown exact original download timestamps and per-file download URLs. Their integrity is verified, but their direct original retrieval provenance is not.
- H.10 bilateral FX directions differ: AUD/EUR/NZD/GBP series are USD per foreign currency; the remaining pairs are foreign-currency units per USD. Do not invert or normalize without an explicit, versioned transformation.
- DEXINUS is the Federal Reserve H.10 noon buying rate in New York, not RBI's reference fixing and not RBI DBIE interbank close.
- The 3 Fed dollar indices are not ICE DXY and are not capital flows.
- The panel has not yet been joined to the exact NSE 200-session calendar. Do not forward-fill or infer missing session values.
- No global flow inference, overlay score, stock ranking, production selector change, or production integration is authorized.

### Updated H.10 panel milestone ledger
1. H.10 DDP-to-FRED migration/source identity lock — PASS.
2. Four Library CSV snapshots and archive integrity QA — PASS.
3. Mapping of all 3 dollar indices + 23 H.10 bilateral FX series — PASS.
4. Full-history daily retrieval for all 26 series — PASS.
5. Per-series schema, date-order, missingness and raw SHA-256 QA — PASS.
6. Long/wide panel build and independently verified GitHub artifact digest — PASS.
7. Exact NSE 200-session and point-in-time vintage reconciliation — PENDING.
8. Repository binary archive / overlay integration and matched diagnostic validation — PENDING.

H.10 panel milestone progress: 6/8 = 75%. The previous 70% figure referred to the Library-ingestion subtask and is superseded for this panel ledger. Global Capital Rotation Overlay remains 62.5% (5/8) because other non-H.10 inputs and cross-layer validation remain incomplete.

Status: PASS_H10_26_SERIES_FULL_HISTORY_RAW_AND_QA; research-only; no production integration.
