# Global Capital Rotation — H.10 / FRED Raw Byte Capture Attempt
Date: 2026-11-17 (Asia/Kolkata)
Status: OFFICIAL FULL-HISTORY ENDPOINTS VERIFIED; BYTE CAPTURE FAILED IN AVAILABLE RUNTIME; NO RECONCILIATION

## Previous work not repeated
- Existing H.10 raw capture #8 and its SHA-256 remain the prior verified capture; not re-downloaded or re-hashed here.
- Existing five-date preview comparison, 72-test regression, 2019 index-base explanation, DDP/FRED crosswalk route/schema, and prior route qualification are not repeated.

## New official evidence
- Federal Reserve H.10 DDP Choose page (last release Monday 2026-11-16): https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10
- The page offers 'Download all G5/H10 data as a single XML file' in SDMX/ZIP format, currently displayed as 26.2 MB. Web reader resolved its link to https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=H10 but cannot parse application/x-zip-compressed (HTTP 400 unsupported content type in reader).
- Official H.10 DDP Review page lists H10/H10/JRXWTFB_N.B, available 2006-01-02 to 2026-11-13, 5,445 observations, description Nominal Broad Dollar Index.
- FRED series page identifies DTWEXBGS as daily Nominal Broad U.S. Dollar Index, Jan 2006=100, source Board of Governors, release H.10. It also states all data are subject to revision.
- FRED public graph CSV endpoint attempted: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS . Runtime byte download failed; no raw CSV or hash produced.
- Federal Reserve DDP retirement FAQ states release XML files are overwritten as releases update and older versions are not available from the release page. Archive each vintage at retrieval time.
- Federal Reserve H.10 RSS records historical corrections, including August 2026 and May 2026 corrections. This makes revision/vintage control a mandatory requirement.

## Runtime acquisition attempts
- container.download FRED public CSV: FAILED (download tool returned download failed).
- container.download Federal Reserve H.10 XML ZIP: FAILED (download tool returned download failed).
- Web open/click of official H.10 ZIP: FAILED at binary content handling; HTTP 400 unsupported content type application/x-zip-compressed.
- These are acquisition-tool failures, not evidence that the official endpoints or files are invalid.

## Acceptance state
- Official H.10 full-history XML endpoint discovery: PASS.
- H.10 series coverage metadata: PASS (5,445 observations, 2006-01-02 through 2026-11-13).
- FRED DTWEXBGS identity/units/frequency/source metadata: PASS.
- Raw H.10 ZIP bytes and SHA-256 in this work unit: NOT_DONE.
- Raw FRED CSV bytes and SHA-256: NOT_DONE.
- Full date-level reconciliation: NOT_RUN.
- Exact DDP crosswalk row: NOT_VERIFIED.
- Revision/vintage archive: NOT_DONE.
- Registry/collector migration: BLOCKED / NOT_AUTHORIZED.

## Key decision
Do not claim that the full-history comparison is complete. The next useful technical step is to use a byte-capable GitHub Actions runner or user-provided raw files to acquire both official payloads, record response metadata and SHA-256, then run a deterministic date/value/status reconciliation. Keep the current H.10 Board release as primary until acceptance gates pass.

## Protected invariants
Research-only; no production change. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN never PASS. No synthetic data, fabricated timestamps or hashes. ₹0 spend.