# Global Capital Rotation — H.10 / FRED Full-History Retrieval Route
Date: 2026-11-17 (Asia/Kolkata)
Status: OFFICIAL RETRIEVAL ROUTES IDENTIFIED; RAW BYTES NOT ACQUIRED; FULL-HISTORY AUDIT NOT_RUN
Scope: Research-only data acquisition route qualification. No source registry/collector migration.

## Prior work not repeated
- H.10 capture #8 / run 44036104490; raw SHA-256 c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77.
- 5,231 valid OBS_STATUS=A rows; 214 ND sentinel rows excluded.
- Regression workflow #232 / run 44036012995: 72 tests PASS.
- Five-date FRED/H.10 preview comparison, 2019 re-indexing explanation and official crosswalk route/schema are already recorded.

## New official evidence: H.10 current release
- Current H.10 release page: https://www.federalreserve.gov/releases/h10/current/default.htm
- Current release date: 2026-11-16.
- The official HTML release explicitly labels the daily Broad, AFE and EME index units as JAN06=100 (not Jan-1997=100).
- For Broad, 2026-11-09=121.6623; 2026-11-10=122.1143; 2026-11-11=ND; 2026-11-12=122.5433; 2026-11-13=122.6503.
- The HTML release defines ND as No data for this date.
- The same release page links the native XML ZIP: https://www.federalreserve.gov/releases/h10/data/FRB_h10_xml.zip
- The XML ZIP link was resolved but the web reader cannot parse application/x-zip-compressed; raw bytes have not been acquired in this checkpoint.

## New FRED public CSV route
- Candidate series: DTWEXBGS, Nominal Broad U.S. Dollar Index.
- Public graph CSV endpoint pattern: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS
- The web reader rejected application/csv content type; this is a reader limitation, not evidence that the endpoint is unavailable.
- FRED API v2 bulk-history access requires an API key/account; do not depend on it for the no-cost/no-key path.
- Federal Reserve DDP/FRED partnership page confirms that historical data remain available as XML on Board statistical release pages and that FRED offers CSV/Excel downloads; DDP preformatted packages are planned for retirement 2027-03-31 and DDP page removal 2027-07-01.

## Important correction to earlier metadata interpretation
- The H.10 Preview endpoint labels the series Unit as Index:_1997_Jan_100, but the actual current H.10 release HTML table explicitly states JAN06=100.
- Therefore the earlier Preview unit label is a stale/inconsistent metadata field; it must not be used to describe the current published observations.
- Current H.10 release HTML and FRED DTWEXBGS both support Jan-2006=100. This resolves the current-release base-year discrepancy at the displayed release level.
- This does not by itself prove all-history equivalence, pre-2019 bridge correctness, revisions/vintages or exact crosswalk row mapping.

## Retrieval route decision
1. For the Board-native source, use the H.10 XML ZIP linked from the current release page; preserve the raw archive and hash every captured vintage.
2. For the FRED candidate, use the public graph CSV endpoint for DTWEXBGS; preserve raw CSV, response headers, retrieval timestamp, byte length and SHA-256.
3. Parse both into date/value/status tables without converting ND/missing values to zero or forward-filling.
4. Compare every overlapping date and report row counts, date coverage, exact matches, mismatches, missingness differences and duplicates.
5. Treat the crosswalk row as a separate acceptance gate; do not promote FRED mapping solely from similar name or preview values.

## Acceptance status
- Official current H.10 HTML route and JAN06=100 unit: PASS.
- H.10 XML ZIP route identified: PASS; raw bytes NOT_DONE.
- FRED public CSV route identified: PASS; raw bytes NOT_DONE.
- Full-history raw capture and SHA-256: NOT_DONE.
- Full date-by-date overlap comparison: NOT_RUN.
- Exact DDP crosswalk row: NOT_VERIFIED.
- Vintage/revision archive and PIT replay: NOT_DONE.
- Registry/collector migration: BLOCKED / NOT_AUTHORIZED.

## Next action
Use a byte-capable download mechanism to retrieve both official H.10 XML ZIP and public FRED CSV. Hash and archive each raw file before parsing; then run deterministic full-history reconciliation, retaining missing values and vintage provenance.

## Invariants
Research-only. No production change. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN never PASS. No synthetic data, fabricated timestamps or hashes. ₹0 spend.