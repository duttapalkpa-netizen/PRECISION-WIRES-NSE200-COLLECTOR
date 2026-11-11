# FBIL Public Reference-Rate API Route Discovery — 2026-11-11

## Result

**New endpoint candidate discovered:** `https://www.fbil.org.in/wasdm/refrates/fetchfiltered`

A publicly accessible, independently maintained updater script in `the-solipsist/rbi-forex-reference-rates` identifies this as the FBIL public reference-rate API and calls it with:
- `fromDate=YYYY-M-D`
- `toDate=YYYY-M-D`
- `authenticated=false`

The script parses JSON array records using:
- `processRunDate` (date prefix)
- `subProdName` labels: `INR / 1 USD`, `INR / 1 GBP`, `INR / 1 EUR`, `INR / 100 JPY`, `INR / 1 AED`, `INR / 10000 IDR`
- `rate`

This is a concrete endpoint and schema lead, not yet an independently verified successful raw acquisition in this project. A direct web-open attempt to the endpoint was not accessible through the current web retrieval tool. Therefore:
- endpoint identity: **STRONG SECONDARY CODE EVIDENCE**
- current anonymous reachability: **UNKNOWN**
- raw response bytes / HTTP status / retrieval timestamp / byte count / SHA-256: **NOT ACQUIRED**
- schema stability/current contract: **NOT VERIFIED**
- production ingestion: **NOT DONE**

## Authoritative source semantics

IMF SDDS/DQAF India Exchange Rates metadata states that FBIL computes USD/INR, EUR/INR, GBP/INR and JPY/INR reference rates daily on Mumbai business days, around 13:30 IST, using transaction-level data from electronic platforms in the 11:30–12:30 IST window; historical data from 10-Jul-2018 are publicly available on FBIL's website. It identifies CCIL and Refinitiv as normal input platforms and describes API/SFTP dissemination to users/data distributors/public.

FBIL's published methodology (2019-01-15, Version 2) says USD/INR uses actual spot transactions on electronic platforms during 11:30–12:30 Mumbai time, normally sourced from Refinitiv and CCIL.

RBI's own disclosure says FBIL took over computation/publication from 10-Jul-2018; do not label post-transition values as RBI-computed.

## Reproducible next verification

1. Request a short closed date window using the candidate endpoint from a supported HTTP-capable runtime.
2. Preserve response bytes before parsing; record request URL (redact no parameters unless sensitive), UTC and IST retrieval timestamps, HTTP status, content type, byte count, SHA-256.
3. Confirm JSON root type, required keys, date parsing, currency labels, rate numeric type, unit conventions, nulls, duplicates and date coverage.
4. Independently compare overlapping dates against NSE's FBIL reference-rate display and RBI archive where available.
5. Test the July 2018–March 2022 historical gap separately; do not infer coverage from recent records.
6. Keep FBIL reference rates as a separate factor series from interbank OHLC. Do not substitute it for missing open/high/low/close.
7. Promote only after raw acquisition, independent match, reproducibility and provenance QA.

## Evidence sources

- IMF India Exchange Rates SDDS/DQAF: https://dsbb.imf.org/sdds/dqaf-base/country/IND/category/EXR00
- FBIL Reference Rate Methodology: https://www.fbil.org.in/uploads/FBIL_REFERENCE_RATE_FINAL_fa318d5727.pdf
- FBIL homepage: https://www.fbil.org.in/
- RBI transition disclosure: https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx
- Independent updater source (secondary implementation evidence only): https://github.com/the-solipsist/rbi-forex-reference-rates/blob/main/scripts/update.sh
- Candidate API: https://www.fbil.org.in/wasdm/refrates/fetchfiltered

## Impact and gates

This discovery materially reduces endpoint/schema discovery uncertainty and provides a precise next acquisition test. It does not create observations and does not increase raw-ingestion, event-study, Factor Registry, production-integration, or overall V11.3 completion percentages. Existing production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, prior PASS artifacts, and research spend constraints remain unchanged.


## Follow-up: independent public-display parity check (2026-11-11)

A live web retrieval of FBIL's own homepage exposed its reference-rate table, and a separate NSE India retrieval exposed its FBIL reference-rate table.

Exact overlapping rows visible in both public displays:

| Trade date | Currency | FBIL homepage | NSE display | Result |
|---|---|---:|---:|---|
| 16-Oct-2026 | INR / 1 USD | 95.0194 | 95.0194 | MATCH |
| 16-Oct-2026 | INR / 1 GBP | 126.4081 | 126.4081 | MATCH |
| 16-Oct-2026 | INR / 1 EUR | 106.6995 | 106.6995 | MATCH |
| 16-Oct-2026 | INR / 100 JPY | 60.18 | 60.18 | MATCH |
| 15-Oct-2026 | INR / 1 USD | 95.0691 | 95.0691 | MATCH |
| 15-Oct-2026 | INR / 1 GBP | 125.8715 | 125.8715 | MATCH |
| 15-Oct-2026 | INR / 1 EUR | 106.5655 | 106.5655 | MATCH |
| 15-Oct-2026 | INR / 100 JPY | 60.19 | 60.19 | MATCH |

**Scoped result:** 8/8 displayed cells match across 2 dates and 4 currencies. This is a genuine independent-display parity check for the overlapping sample, not a full historical validation and not a raw-file/API response validation. The public displays have different latest dates (FBIL page's latest displayed date in the retrieved table: 16-Oct-2026; NSE page range ends 06-Nov-2026 and includes 05-Nov-2026), so do not infer identical freshness.

### Updated gate status

- FBIL public reference-rate display: **VERIFIED**
- NSE vs FBIL displayed overlap (2 dates × 4 currencies): **PASS, 8/8**
- Candidate API route from independent updater code: **DISCOVERY ONLY**
- Candidate API live response / anonymous access: **UNKNOWN**
- Raw JSON/CSV bytes, retrieval timestamp, byte count, SHA-256: **NOT ACQUIRED**
- Full historical completeness: **UNKNOWN**
- Interbank OHLC: **NOT PROVIDED**
- Production ingestion / Factor Registry: **NOT DONE**

Evidence:
- FBIL official homepage: https://www.fbil.org.in/
- NSE official page: https://www.nseindia.com/report-detail/rbi-reference-rate-statistics
- FBIL methodology: https://www.fbil.org.in/uploads/FBIL_REFERENCE_RATE_FINAL_fa318d5727.pdf

This follow-up adds a small, reproducible display-level cross-check. It does not promote any data rows into the project and does not alter any production invariant.
