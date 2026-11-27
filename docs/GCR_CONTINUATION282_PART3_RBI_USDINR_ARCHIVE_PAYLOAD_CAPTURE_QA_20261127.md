# GCR Continuation 282 — Part-3 RBI USD Reference Rate archive payload capture and QA (27-Nov-2026)

## 1. Library retrieval and duplicate check
The user directed us to the Library file for the RBI USD Reference Rate Archive export. A recent Library inventory identified two entries:
- `/BankWise.xls` — 57,289 bytes; Library file ID `libfile_cc2b8bee3e788191943727620d470757`.
- `/BankWise(1).xls` — 57,289 bytes; Library file ID `libfile_6d4f3bce48088191b403cc1264dc9ceb`.

Both were materialized read-only and byte-compared by SHA-256. They are exact duplicates. No additional upload, rename, overwrite, or deletion was performed.

## 2. Raw payload identity
- Both files identify as HTML documents containing a two-column HTML table, despite the `.xls` filename/Excel MIME label. This is not a native BIFF .xls or OOXML .xlsx workbook.
- Exact bytes: 57,289.
- SHA-256: `379318c3e4b048eeba63824bc09d26b2e6f5d9418e17bd589059d4c0b63e93e2`.
- Table header: `Date`, `USD (INR / 1 USD)`.
- The HTML table payload is consistent with the RBI Reference Rate Archive screen shown by the user (USD selected; date filter shown 15/07/2018 through 26/11/2026; visible latest observation 26/11/2026). Source URL for the archive: https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx.
- Exact browser request URL, response headers, retrieval timestamp at the source, and server-side content-disposition were not embedded in the saved HTML; provenance is supported by user-provided RBI page screenshots plus the Library export, not by an independently captured HTTP transaction.

## 3. Parsed row-level QA
- HTML table rows: 1 header + 1,119 data rows.
- Parsed records: 1,119; malformed rows: 0.
- Columns: exactly 2 on all data rows.
- Observation dates: earliest 24-Jul-2018; latest 26-Nov-2026.
- Calendar span: 3,047 days (more than 90 days).
- Distinct observation dates: 1,119.
- Duplicate dates: 0.
- Blank/null cells: 0.
- Numeric values: all parse as positive numbers; observed range 69.0530 to 96.8441 INR per USD.
- Date rows appear in descending order, consistent with the archive display.
- The requested From Date was 15-Jul-2018, but the earliest returned observation is 24-Jul-2018; preserve this boundary discrepancy as observed, do not synthesize missing rows.
- No attempt was made to flag weekends/market holidays as missing observations; a separate calendar-aware expected-business-day QA is still required.
- Native workbook sheet names, workbook formulas/styles, and BIFF/OOXML workbook schema are NOT_APPLICABLE because the captured payload is HTML table markup saved with an .xls extension.

## 4. Acceptance decision
- Official RBI Reference Rate Archive source identity: carried forward PASS.
- User-provided screenshot evidence of USD selection and date window: CONFIRMED.
- Exact saved payload bytes and SHA-256: CAPTURED / VERIFIED.
- Parsed table structure and row-level syntactic/numeric QA: PASS.
- Minimum distinct-date and 90-day coverage gates: PASS (1,119 dates; 3,047-day span).
- Full calendar-aware expected-session completeness, release/revision history, and independent source transaction headers: NOT_VERIFIED.
- This is an RBI USD/INR reference-rate fixing series, not interbank OHLC or turnover.
- Therefore RBI USD/INR reference-rate raw capture may be accepted as a captured/validated reference-rate payload for research staging, but full production ingestion certification remains pending provenance metadata, calendar-aware coverage, PIT/revision treatment and downstream integration tests. Do not mark the broader USD/INR interbank/OHLC series complete. GCR strict hard gate remains BLOCKED due separate unresolved blockers including FPI/DII and other P0 acceptance components.

## 5. Protected constraints and next actions
- Preserve the exact source payload and hash; do not convert/normalize or replace the original in Library.
- Keep the duplicate Library object untouched; record its identical hash and avoid further duplicate uploads.
- Create a derived normalized CSV only as a separate derivative with transformation manifest, never overwrite the raw payload.
- Next: calendar-aware gap audit against official RBI/FBIL publication calendar; capture retrieval metadata if available; retain reference fixing distinct from DBIE interbank rate; separately resolve FPI/DII and remaining GCR blockers.
- ₹0 spend, official/free sources only; UNKNOWN is neither PASS nor FAIL; CORE-672, Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged.
