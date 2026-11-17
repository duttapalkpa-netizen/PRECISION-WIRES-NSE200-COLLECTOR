# BCB Monthly Balance-of-Payments Historical ZIP — Independent Cross-Check
Date: 2026-11-17
Status: IMPLEMENTED ON RESEARCH BRANCH; RUNTIME NOT YET VERIFIED

## Official route
The BCB official page “Série Histórica do Balanço de Pagamentos” provides a Monthly ZIP link. The resolved official download URL is:
`https://www.bcb.gov.br/ftp/notaecon/balpagm.zip`
The page presents monthly, quarterly and annual historical ZIP downloads.

## Purpose
Acquire this separate official BCB monthly historical archive as a candidate independent cross-check for the seven SGS series already captured. Do not assume it contains the same BPM6 perimeter or that its series are directly comparable until archive members, dates, units, definitions and vintages are inspected.

## New files
- `scripts/research/capture_bcb_monthly_bop_history_zip.py`
- `.github/workflows/bcb_monthly_bop_history_zip_capture.yml`

## Capture contract
Capture raw ZIP bytes, HTTP status/headers, final URL, UTC retrieval start/end, byte length and SHA-256. Verify ZIP signature and CRC. Record archive member names and compressed/uncompressed sizes. Upload artifact even on failure; 8-minute timeout and 90-day retention.

## Acceptance
- Official monthly ZIP link resolved: PASS.
- Raw ZIP bytes / SHA-256: NOT_DONE until runtime artifact inspected.
- ZIP member inventory and schema: NOT_DONE.
- BPM6/perimeter applicability to SGS 22905–22926: UNKNOWN.
- Independent date/value cross-check: NOT_RUN.
- Accounting sign acceptance: NOT_DONE.
- Production integration: NOT_AUTHORIZED.

## Next action
Inspect the push-triggered run and artifact. If capture succeeds, inspect the ZIP members first and identify the relevant monthly BPM6 tables/series before writing any parser. Do not force a join if the archive uses a different vintage, base or reporting perimeter.
