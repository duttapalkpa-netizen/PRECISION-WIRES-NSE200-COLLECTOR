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


## Follow-up: source-window and production-use boundary

A current connector/tool reference describing the FBIL public feed reports that the feed exposes only a rolling window of approximately two days and that no bulk historical archive was found through that feed. This is **secondary implementation documentation**, not an FBIL-published service-level guarantee. Treat the exact retention window as **UNVERIFIED** until tested against the official endpoint.

Operational implication:
- First live test should request a very short date interval, not a multi-year range.
- If the endpoint is rolling-window only, use a daily/weekday collector with immutable raw-response archive and explicit missed-day recovery; do not expect the API to backfill arbitrarily old observations.
- A missed polling window must create a visible gap / UNKNOWN status, never a synthetic or forward-filled observation.
- Historical data acquisition must be handled separately through FBIL/NSE public archive routes or another source whose provenance is explicitly accepted.

## Benchmark construction facts (IMF metadata)

IMF SDDS/DQAF metadata describes:
- USD/INR reference rate based on actual spot transaction data from electronic platforms during 11:30–12:30 IST on Mumbai business days.
- FBIL publishes USD/INR, EUR/INR, GBP/INR and JPY/INR around 13:30 IST on Mumbai business days.
- Cross-currency rates use the corresponding spot cross rates from the same selected time window.
- The published reference rate is a benchmark observation, not an OHLC bar or a continuous intraday price.

This reinforces the hard separation:
1. FBIL reference-rate factor: daily benchmark fixing.
2. Interbank OHLC factor: separate market-data series, still unresolved at RBI-primary source level.
3. Never derive open/high/low/close from the FBIL fixing.

## Current acquisition result

No live FBIL API JSON body was retrieved in this turn. The web retrieval service could not open the candidate API URL, and the FBIL homepage itself rendered without extractable page lines. Therefore the live API request, response status, content type, response byte count, raw bytes, retrieval timestamp and SHA-256 remain **NOT ACQUIRED / UNKNOWN**. No observations are admitted.

Evidence:
- IMF SDDS/DQAF India Exchange Rates: https://dsbb.imf.org/sdds/dqaf-base/country/IND/category/EXR00
- RBI press release confirming transition effective 10-Jul-2018: https://www.rbi.org.in/commonman/Upload/English/PressRelease/PDFs/PR3504072018.PDF
- FBIL official homepage: https://www.fbil.org.in/
- Secondary feed-window note (discovery lead only): DalalOS FX reference-rate tool documentation, https://glama.ai/mcp/connectors/in.dalalos/mcp/tools/get_fx_reference_rates

No changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, existing accepted observations or prior PASS artifacts.


## Live endpoint acquisition — 2026-11-11 (new evidence)

A GitHub Actions runner successfully reached the FBIL endpoint over HTTPS.

### Known historical overlap window: 2026-10-15 to 2026-10-16

- HTTP status: **200**
- Content-Type: **application/json**
- JSON root: array
- Records: **14**
- Distinct dates: **2**
- Product labels: USD, GBP, EUR, JPY, AED, IDR and RUB
- Retrieval UTC: **2026-11-11T07:55:32.114141+00:00**
- Retrieval IST: **2026-11-11T13:25:32.114141+05:30**
- Raw response bytes: **1,919**
- Raw response SHA-256: **aeec99630a30d4b5961755c35e05b1e795dec1c39a373e48d95eca5edd165e27**
- Validator: **PASS** after adding the observed `INR / 1 RUB` product label to the accepted mapping.
- Duplicate date-currency keys: none in this sample.
- Positive numeric rates and requested-date bounds: PASS.

The raw response is preserved unchanged at:
`data/raw/fbil_reference_rate_api_20261015_20261016.json`

Provenance is preserved at:
`data/raw/fbil_reference_rate_api_20261015_20261016.provenance.json`

GitHub Actions:
- Workflow run: **42983033561** — success
- Artifact ID: **13837574133**
- Artifact ZIP SHA-256: **48340a456b11aa8b3cc7e6133d00dcd92794b08c8460cbe65742cc25986c56f4**
- Artifact retained raw response, request metadata, and validated CSV.
- Re-fetched GitHub raw file blob SHA: `63830f63507b51bf5377fd9de72e8f1ef425669e`
- Re-fetched provenance blob SHA: `8f49369671989cd24a0b4815b022679fd69aed56`

### Recent window: 2026-11-09 to 2026-11-11

- HTTP status: **200**
- Content-Type: **application/json**
- Raw bytes: **2**
- Body: `[]`
- Raw SHA-256: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- Status: **EMPTY_ARRAY / UNKNOWN cause**

The empty recent response is not interpreted as a missing market observation, endpoint outage, or definitive retention limit. Possible causes (publication lag, server-side filter/data availability, or a feed coverage boundary) remain unresolved. The historical sample proves that the candidate endpoint can return data for a known window; it does not prove recent freshness or full history.

### Updated gate

- Live HTTPS reachability: **PASS**
- Historical JSON acquisition: **PASS — 14 raw records**
- Raw bytes + SHA-256 + retrieval timestamps: **PASS**
- Fail-closed parser/validator: **PASS — scoped sample**
- FBIL/NSE displayed overlap for USD/GBP/EUR/JPY on 15–16 Oct: **PASS — 8/8 values**
- Recent-window freshness: **UNKNOWN — HTTP 200 empty array**
- Full historical backfill: **NOT DONE**
- Interbank OHLC: **NOT PROVIDED**
- Factor Registry / production integration: **NOT CONNECTED**

No raw records are promoted into production. The sample is archived as research evidence only. No gap filling, forward filling, fabricated rows, or OHLC derivation. No changes to selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, or Hard Gate.
