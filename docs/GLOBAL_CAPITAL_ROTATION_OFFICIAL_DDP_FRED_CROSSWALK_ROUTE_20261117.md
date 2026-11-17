# Global Capital Rotation — Official DDP–FRED Crosswalk Route
Date: 2026-11-17 (Asia/Kolkata)
Status: OFFICIAL MIGRATION ROUTE DOCUMENTED; ROW-LEVEL CROSSWALK NOT EXTRACTED
Scope: Source routing and migration design only; no collector or registry changes.

## Prior work not repeated
- H.10 capture #8 / run 44036104490; 5,231 valid rows and 214 ND rows excluded.
- Regression workflow #232 / run 44036012995: 72 tests PASS.
- H.10 20-prior-valid-observation derived result +0.8892047581% (research-only).
- FRED DTWEXBGS five-date match and 2019 base-year methodology resolution are documented in the preceding audits.
- DDP retirement timeline and XML fallback are already documented in H.10 source continuity checkpoint.

## Newly verified official migration documentation
- Federal Reserve DDP/FRED partnership page: https://www.federalreserve.gov/data/data-download-fred-information.htm
- Page last updated 2026-11-12. Lines 24-28 state Board-published crosswalk CSV translates Board series IDs to FRED series IDs for FRED downloads.
- Lines 78-80 describe the crosswalk as a comprehensive file mapping all DDP series to FRED counterparts, periodically updated; crosswalk and data definitions were updated 2026-07-06.
- Official crosswalk URL: https://www.federalreserve.gov/data/documents/DDP-FRED%20Data%20Series%20Crosswalk.csv
- Browser could identify the CSV link but could not parse its application/octet-stream response. Therefore the actual JRXWTFB_N.B -> DTWEXBGS row was NOT extracted or verified from the crosswalk in this checkpoint.
- Federal Reserve page says FRED API v2 can return full histories for FRED and DDP series in JSON/XML, but an API key is required. Do not assume API keyless bulk access.
- Federal Reserve page also confirms Board statistical-release XML remains a manual fallback while DDP is retired.
- FRED graph CSV download is an alternate public download mechanism for charted series, but this checkpoint did not retrieve raw bytes or validate its full-history output.

## Engineering decision
1. The official Board crosswalk is the authoritative next artifact for confirming the Board-to-FRED series-ID mapping; do not rely solely on name similarity.
2. Obtain the crosswalk CSV bytes and independently verify the exact Board series ID H10/H10/JRXWTFB_N.B maps to FRED DTWEXBGS. Archive bytes, retrieval timestamp, HTTP metadata, byte length and SHA-256.
3. Preserve both source IDs and original source lineage in the evidence manifest. The FRED route is an alias/transport route, not a replacement for the underlying Board source identity.
4. After exact mapping is proven, obtain full historical data from FRED graph CSV or official H.10 XML and perform date-by-date comparison; retain missing values and revisions.
5. Do not use FRED API v2 in the ₹0/no-paid constraint if a required API key/account workflow is unavailable or unsuitable; use free public CSV/XML downloads where technically permitted.
6. No source registry promotion, collector migration, or classifier integration is authorized by this route audit.

## Acceptance status
- Official migration/crosswalk documentation found: PASS.
- Exact row-level mapping extracted from crosswalk CSV: NOT_DONE.
- Crosswalk raw bytes + SHA-256 + immutable manifest: NOT_DONE.
- Full H.10/FRED daily overlap comparison: NOT_DONE.
- Historical vintage/revision comparison: NOT_DONE.
- Collector/registry migration: BLOCKED.
- PIT replay, classifier integration and predictive validation: NOT_DONE / NOT_AUTHORIZED.

## Next action
Fetch and parse the official crosswalk CSV with a supported file-download path, verify the exact mapping row and its column semantics, preserve its raw bytes and SHA-256, then use that mapping to authorize a bounded full-history overlap comparison. Do not repeat the already-completed five-date preview check.

## Invariants
Research-only. No production change. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN never PASS. No synthetic observations/timestamps/hashes. ₹0 spend.