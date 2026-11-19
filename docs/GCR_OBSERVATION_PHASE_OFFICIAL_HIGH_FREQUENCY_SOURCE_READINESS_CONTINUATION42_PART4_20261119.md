# GCR Observation Phase — Official High-Frequency Source Readiness Matrix (Continuation 42, Part-4)
Date: 2026-11-19
Stage: OBSERVATION ONLY
Scope: Verify whether a zero-cost, source-grounded daily event-study panel can be assembled for global shock → India FX/market/flow transmission. This is a source-readiness audit, not a dataset ingestion or event-study result.

## 1. Verified public source inventory

| Required variable | Official/public source | Frequency/coverage stated by source | Observation status |
|---|---|---|---|
| NIFTY / NSE index history | NSE Historical Reports / Historical Index Data; NSE Indices historical data | Date-range query and CSV output; NSE page demonstrates NIFTY 50 sample rows (2019) | ACCESS PATH VERIFIED; actual full-period export not acquired |
| India VIX | NSE Historical Data - India VIX | Date-range query; daily historical page | ACCESS PATH VERIFIED; actual export not acquired |
| Indian equity security/market context | NSE daily reports, full bhavcopy, delivery positions, security-wise price-volume | Daily archives; NSE lists full bhavcopy and security delivery reports | ACCESS PATH VERIFIED; archive acquisition/coverage QA remains |
| FPI daily flow | SEBI FPI data curation page links NSDL Latest/Monthly/Archive and CDSL Daily/Monthly/Trends archive | Daily/latest and monthly/archive paths explicitly listed | ACCESS PATH VERIFIED; NSDL/CDSL overlap, units and revisions not reconciled |
| USD/INR | RBI DBIE, Daily interbank forex rates (USD vis-à-vis INR) | Daily, from 2000-08-08 through 2026-06-30 in page snapshot; CSV/JSON downloads | COVERAGE METADATA VERIFIED; raw CSV and hash not acquired |
| US 10Y yield | FRED DGS10, source: US Federal Reserve Board H.15 | Daily, percent, not seasonally adjusted; observations subject to revision | SERIES DEFINITION VERIFIED; vintage snapshot and raw file not acquired |
| Global risk / VIX | FRED VIXCLS, source: CBOE Market Statistics | Daily close; CBOE VIX; copyright/citation terms apply | SERIES DEFINITION VERIFIED; reuse/copyright conditions must be respected |
| Indian Basket crude | PPAC International Prices of Crude Oil (Indian Basket) | Official historical report download and FY/monthly table | OFFICIAL PATH VERIFIED; monthly/FY presentation is not sufficient evidence of a daily series |
| DII daily activity | NSE FII/DII trading activity reports | NSE reports section lists FII/DII; daily report path | ACCESS PATH IDENTIFIED; raw historical coverage/definitions not yet inspected |

## 2. What is genuinely ready vs not ready
READY AS SOURCE DISCOVERY:
- NSE historical index, India VIX, daily market archive paths exist.
- SEBI officially links both NSDL and CDSL FPI daily/monthly/archive data sources.
- RBI DBIE page explicitly reports daily USD/INR interbank rates from 2000-08-08 to 2026-06-30 and CSV/JSON download.
- FRED series metadata identifies DGS10 as daily US Treasury 10Y yield and VIXCLS as daily CBOE VIX close.
- PPAC offers official Indian Basket crude historical report, but the surfaced page is fiscal-year/monthly layout.

NOT YET DATA-READY:
- No raw file has been downloaded in this task; no row count, first/last record, missingness, revision vintage, timestamp, timezone, SHA-256 or duplicate test is claimed.
- NSE index/VIX interactive date-range forms have not been executed/exported.
- NSDL and CDSL daily FPI feeds have not been reconciled; do not sum both or assume they are independent.
- NSE FII/DII “trading activity” definitions and historical completeness need source-file inspection.
- RBI DBIE latest snapshot currently ends 2026-06-30 in the captured page; do not silently extend it using third-party data.
- FRED DGS10 and VIXCLS are daily but have different calendars/closing conventions from NSE; alignment requires explicit date mapping and no forward-fill across market holidays.
- PPAC Indian Basket monthly/FY table is too coarse for a daily event study unless a separate official daily source is independently verified.
- FRED VIXCLS is CBOE copyrighted series; attribution/reuse terms must be observed.

## 3. Minimum event-study source panel — observation-stage proposal only
A future reproducible panel should keep separate fields:
- India outcome: NIFTY 50 price return and (where available) total-return index; India VIX; sector indices; USD/INR.
- Global push: US 10Y yield (DGS10), CBOE VIX (VIXCLS), and separately sourced global dollar index/energy benchmarks only after exact official source validation.
- Capital flows: NSDL and CDSL FPI records retained as separate source streams until overlapping definitions, units, net/gross and coverage are reconciled; NSE FII/DII trading activity kept separate from custody-based FPI investment flows.
- Domestic controls: DII flow, domestic earnings/event flags, RBI policy dates, India macro releases, market holidays and sector exposure.
- Commodity channel: PPAC Indian Basket monthly observation can support low-frequency context; it cannot be interpolated into daily observations.

## 4. Synchronization and no-look-ahead rules
1. Preserve each source's original observation date, publication/retrieval timestamp, timezone, frequency, unit and vintage.
2. Distinguish event date from first public availability date. A data point published after Indian market close cannot be treated as known before that close.
3. Map global US close t to the next Indian trading session only where chronology supports it; do not merge by date string alone.
4. Do not forward-fill missing market days, manufacture daily crude observations from monthly values, or convert a monthly flow into daily flow by interpolation.
5. Keep price returns, index points, flow currency/units, yields in percentage points, and volatility index levels in separate typed fields.
6. Keep source-native raw data immutable; all normalized panels must have a reproducible transformation manifest and hashes.
7. Use event windows with pre-event, event, and post-event trading sessions, and report overlapping-event/confounder flags before any attribution.
8. Separate source availability and data completeness from predictive usefulness; no variable is admitted to production solely because a download exists.

## 5. Primary source register
- NSE Historical Reports (index, India VIX, daily reports, security price/volume/delivery): https://www.nseindia.in/static/resources/historical-reports-capital-market-daily-monthly-archives
- NSE All Reports / historical index and India VIX interfaces: https://www.nseindia.in/all-reports
- NSE Indices Historical Data: https://www.niftyindices.com/reports/historical-data
- SEBI FPI data curation page (NSDL/CDSL links): https://www.sebi.gov.in/curation/fpi.html
- RBI DBIE daily interbank USD/INR table: https://dbie.rbihub.in/tables?table=financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr
- RBI Reference Rate Archive: https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx
- FRED DGS10 (source: US Federal Reserve Board): https://fred.stlouisfed.org/series/DGS10
- FRED VIXCLS (source: CBOE): https://fred.stlouisfed.org/series/VIXCLS
- PPAC Indian Basket crude oil prices: https://ppac.gov.in/index.php/prices/international-prices-of-crude-oil

## 6. Stage decision and remaining blockers
- This task completes a documented source-discovery/readiness matrix only.
- No event-study observations, returns, flow series, or hashes were generated; therefore no statistical or pipeline PASS is claimed.
- Daily event-study acquisition should proceed in small bounded jobs: (A) NSE index/VIX export, (B) RBI DBIE USD/INR export, (C) NSDL/CDSL FPI archive reconciliation, (D) DII/NSE daily reports, (E) FRED DGS10/VIXCLS snapshot, (F) PPAC low-frequency commodity context.
- Do not start country scoring or production weights before source files are acquired, validated and timestamp-aligned.
- Observation overall remains OPEN; Planning and Organizing NOT STARTED; GCR NOT COMPLETE; aggregate/production admission NOT AUTHORIZED.

## 7. Invariants
₹0 spend; free official/public sources prioritized; no synthetic data, fabricated timestamps, guessed daily interpolation, or unsupported country weights. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
