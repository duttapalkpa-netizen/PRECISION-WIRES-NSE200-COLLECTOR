# Global Capital Rotation — Official DDP/FRED Crosswalk Row Retrieval Blocker
Date: 2026-11-17 (Asia/Kolkata)
Status: CROSSWALK SCHEMA VERIFIED; TARGET ROW NOT RETRIEVED; NO MIGRATION

## Prior evidence not repeated
- H.10 capture #8 / run 44036104490; raw SHA-256 c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77; 5,231 valid A observations; 214 ND excluded.
- Regression #232 / run 44036012995: 72 tests PASS.
- Five-date FRED DTWEXBGS / H.10 JRXWTFB_N.B preview comparison already recorded (5/5 exact).
- 2019 re-indexing explanation and Broad factor 1.014163 already recorded; do not apply the factor twice.
- DDP retirement and source-continuity risks already recorded.

## New official source evidence
- Federal Reserve DDP/FRED partnership page: https://www.federalreserve.gov/data/data-download-fred-information.htm
- Federal Reserve FRED user guide: https://www.federalreserve.gov/data/ddp-fred-user-guide.htm
- Official crosswalk CSV: https://www.federalreserve.gov/data/documents/DDP-FRED%20Data%20Series%20Crosswalk.csv
- Official crosswalk data definitions PDF: https://www.federalreserve.gov/data/documents/ddp-fred-data-definitions.pdf
- Data definitions identify columns: ddp_release, board_series_id, fred_series_id. The crosswalk maps Board DDP series IDs to equivalent FRED series IDs.
- The Federal Reserve describes the crosswalk as a comprehensive mapping of DDP series and FRED counterparts, periodically updated; page notes update date 2026-07-06.
- The official CSV endpoint returned an unsupported application/octet-stream response in the web reader, and direct raw download failed in the available runtime. The CSV bytes were not acquired; no hash or manifest can truthfully be recorded.
- Official H.10 DDP Review page lists H10/H10/JRXWTFB_N.B as Nominal Broad Dollar Index, available from 2006-01-02, with 5,445 observations through 2026-11-13.
- FRED DTWEXBGS page identifies the series as Nominal Broad U.S. Dollar Index, daily, Jan-2006=100, source Board of Governors, release H.10 Foreign Exchange Rates.
- These independent official pages strongly support the candidate mapping but are not a substitute for the actual row from the Board's crosswalk CSV.

## Decision
- Crosswalk schema and official purpose: PASS.
- Exact target row JRXWTFB_N.B -> DTWEXBGS: NOT_VERIFIED_FROM_CSV.
- CSV raw bytes / response metadata / byte length / SHA-256: NOT_DONE.
- Candidate mapping status: PROVISIONAL_ONLY, supported by source descriptions and matching preview values.
- Registry promotion, collector migration, classifier integration: BLOCKED / NOT_AUTHORIZED.

## Additional source-integrity warning
- Federal Reserve RSS records historical corrections to H.10 (including 2026-08-12 correction for 2026-08-03, and other prior corrections). This demonstrates that point-in-time vintage/revision handling is material. Current XML and current FRED series values cannot alone reconstruct what was known on an earlier decision date.
- H.10 XML on release pages is overwritten on each release and reflects latest available history; previous versions are not archived there. Preserve each retrieved raw vintage independently before future releases overwrite it.

## Next actions
1. Retrieve the official CSV through a supported byte-download mechanism; preserve response headers, retrieval timestamp, byte count, SHA-256 and manifest.
2. Parse exact row by named columns ddp_release, board_series_id, fred_series_id; verify H10 + JRXWTFB_N.B maps to DTWEXBGS. Reject duplicate or conflicting rows.
3. Download full daily FRED DTWEXBGS CSV using a public no-key graph CSV route if permitted; preserve raw bytes and SHA-256. Independently obtain current official H.10 XML and compare all dates.
4. Separately compare pre-2019 goods-only and post-2019 broad-index series semantics; do not splice or scale distinct economic concepts without the official bridge.
5. Add dated immutable snapshots and a revision-diff report. Do not claim historical PIT replay until multiple dated vintages are archived.

## Protected invariants
Research-only; no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN never PASS. No synthetic data, fabricated hashes or timestamps. ₹0 spend.