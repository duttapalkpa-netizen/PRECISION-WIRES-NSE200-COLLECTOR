# NSE FBIL Reference-Rate Public CSV Access Audit — 2026-11-11

## Outcome

- Page discovery: **PASS**
- Public CSV control presence: **PASS**
- Download URL / raw CSV bytes / retrieval timestamp / SHA-256: **UNKNOWN — NOT ACQUIRED**
- Historical coverage completeness: **UNKNOWN**
- RBI interbank OHLC coverage: **NOT PROVIDED BY THIS SOURCE**
- USD/INR reference-rate ingestion: **NOT DONE**
- Factor Registry connection: **NOT CONNECTED**

## Verified source

NSE India exposes a page titled **RBI Reference Rates Statistics**:
https://www.nseindia.com/report-detail/rbi-reference-rate-statistics

The page labels the dataset **“Reference rate-FBIL”** and displays a **“Download (.csv)”** control. The page itself notes that currency turnover is calculated using the latest available Reference rate-FBIL. The rendered page was inspected on 2026-11-11. The web-rendered page does not expose the underlying CSV URL or file bytes, so this audit does not claim a successful download.

NSE search indexing showed a displayed date window of 06-Oct-2026 to 06-Nov-2026, with daily observations including 05-Nov-2026. This is evidence of a recent public display, not evidence of complete historical coverage or a captured raw CSV.

## RBI archive boundary

RBI's own Reference Rate Archive remains:
https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx

The page exposes currency selection, From Date / To Date controls, and an Excel download image/control. It is explicitly identified as owned and managed by RBI and shows a website update date of 11-Nov-2026. The rendered page did not reveal the actual Excel export URL or file bytes.

RBI's RTI disclosure log states that since 10-Jul-2018 FBIL computes and publishes the major-currency reference rates, while RBI discontinued computing/publishing its own reference rates from that date:
https://www.rbi.org.in/scripts/FS_RTI_Diclosure_Logs.aspx?fn=6

Therefore, for post-10-Jul-2018 observations, describe the field as **FBIL reference rate published/displayed by RBI/NSE**, not as an RBI-computed interbank rate.

## Strict source semantics

1. NSE's FBIL reference-rate CSV is a candidate public exchange-distributed reference-rate source, suitable for a future matched-date cross-check after raw acquisition and QA.
2. It is **not** the daily interbank USD/INR OHLC series.
3. It cannot replace the unresolved RBI-primary DBIE interbank open/high/low/close source.
4. The DBIE mirror at dbie.rbihub.in remains secondary/prototype evidence only, per the previously recorded source-authority correction. Its 6,319 metadata vs 6,308 displayed-row discrepancy remains unresolved and must not be promoted to RBI-primary evidence.
5. No rows are admitted to production or research observations from this page audit.

## Required acquisition QA before promotion

- Download the CSV through a supported browser/manual export route; preserve original bytes unchanged.
- Record exact URL, retrieval timestamp with timezone, HTTP/content metadata where available, byte count, and SHA-256.
- Parse date, currency, unit/quote convention, value, and source label without silently normalizing away the original fields.
- Check duplicate date-currency keys, missing business dates, blank/non-numeric values, and unit consistency (notably JPY quotation convention).
- Cross-check overlapping dates against RBI's displayed archive and an independent exchange/FBIL display; record disagreements, do not overwrite.
- Keep the reference-rate series separate from interbank OHLC.

## Progress accounting

This is a source-access discovery and semantics clarification only. It does **not** increase actual observations acquired, macro ingestion, event-study maturity, Factor Registry coverage, production integration, or the overall V11.3 project percentage. No existing selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostic, engine, hard gate, or prior PASS artifact is changed.

## Evidence checked

- NSE page: https://www.nseindia.com/report-detail/rbi-reference-rate-statistics
- RBI archive: https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx
- RBI RTI disclosure log: https://www.rbi.org.in/scripts/FS_RTI_Diclosure_Logs.aspx?fn=6
- NSE rendered page evidence: page labels “Reference rate-FBIL” and “Download (.csv)”.
- RBI rendered archive evidence: currency selector, date controls, Excel control, RBI ownership footer, update date 11-Nov-2026.
