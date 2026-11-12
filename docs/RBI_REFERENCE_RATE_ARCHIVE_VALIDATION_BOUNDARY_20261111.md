# RBI USD/INR official reference-rate archive — access and semantic boundary
Date: 2026-11-11

## Verified primary RBI interface
Official page: https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx
Page owner/manager: Reserve Bank of India (page footer). Last-updated label observed: 11-Nov-2026.
Visible controls:
- Currency selector: All, USD, GBP, EUR, JPY, AED, IDR, RUB.
- From Date and To Date inputs (DD/MM/YYYY).
- Calendar navigation controls.
- 'Download to: Excel' control.

## What this source can validate
The RBI archive is an RBI-owned primary source for its reference-rate series. It can support a date-matched validation of the `RBI Reference Rate` field in the daily interbank USD/INR dataset for dates actually present in the archive export.

## What it cannot validate
It does not expose the interbank market's Open, High, Low, and Close fields on this page. Do not use RBI reference rate as a proxy for interbank OHLC, and do not derive OHLC from reference rates.

## Retrieval status and limits
- Page and controls identified: PASS.
- Exact Excel export URL / request contract: UNKNOWN; the visible download icon is an image and the page's export behavior is client-side.
- Date-range selection and actual Excel bytes: NOT DONE.
- Retrieval timestamp, byte count, SHA-256: NOT DONE.
- Date-matched comparison against DBIE USD/INR reference-rate column: NOT DONE.
- No values have been copied from preview or reconstructed.

## Next bounded acceptance test
1. Use the RBI-owned page and choose USD with a bounded date interval that overlaps the target DBIE data.
2. Trigger the page's Excel download through its normal UI; preserve the original file bytes.
3. Record UTC retrieval time, selected date range, HTTP/browser filename, file size, and SHA-256.
4. Inspect sheet names, headers, date parsing, duplicate dates, missing dates, and numeric values.
5. Compare only matched dates and the reference-rate field. Report exact overlap, mismatches, and missing dates; do not silently round or forward-fill.
6. Keep RBI archive vintage separate from DBIE interbank-table vintage.

## Gate
- RBI primary reference-rate source: PASS.
- Reference-rate download contract: UNKNOWN.
- Raw Excel acquisition and SHA: NOT DONE.
- Matched-date QA: NOT DONE.
- DBIE interbank OHLC source: still NOT VERIFIED via RBI-owned route.
- USD/INR combined ingestion: BLOCKED.

## Safety
₹0 spend; free official source only. No synthetic data, fabricated timestamps, silent row deletion, or forward fill. Research-only; production invariants unchanged.