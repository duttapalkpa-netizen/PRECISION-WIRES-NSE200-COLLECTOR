# Macro-Geo P0 source recovery checkpoint — 2026-11-12

## Purpose
Record source-level findings that materially affect the next recovery attempt. This is a discovery/acceptance checkpoint, not a data-ingestion PASS and not a Hard Gate clearance.

## USD/INR: official RBI DBIE source and freshness limitation
Official DBIE table:
- URL: https://dbie.rbihub.in/tables?table=financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr
- Table: Daily interbank forex rates (USD vis-a-vis INR)
- Source: Reserve Bank of India / DBIE
- Frequency: Daily
- Available period currently displayed by DBIE: 2000-08-08 through 2026-06-30
- Rows displayed: 6,319 (table UI says 6,308 records in current page listing; discrepancy must be resolved against downloaded raw export before counting)
- Fields: date, interbank open, high, low, close, RBI reference rate
- Unit: INR per USD
- DBIE page offers CSV and JSON download controls.

Important: the latest verified NSE 200-session snapshot ends 2026-11-12. The DBIE table's currently indexed latest observation (2026-06-30) does not cover the last part of this NSE window. Do not call it full-window coverage. It is the right official interbank source for its available dates, with a separately disclosed stale tail.

RBI Reference Rate Archive:
- URL: https://rbi.org.in/scripts/ReferenceRateArchive.aspx
- Offers date-bounded USD and other currency reference-rate archive download in Excel.
- RBI's own archive page is a distinct reference-rate series. Since 2018-07-10, FBIL is the official benchmark administrator and RBI publishes the rates. Do not combine reference rates with interbank open/high/low/close as if they are one series.
- Next ingestion must retain series identity, publication date/time availability and raw workbook bytes. If publication timestamps cannot be established for a given vintage, mark point-in-time eligibility UNKNOWN.

MoSPI dataset-catalogue evidence (RBI daily interbank forex table):
- Official catalogue describes the DBIE forex turnover dataset as daily, with about one-month dissemination lag, downloadable as Excel/PDF through DBIE. This is a separate table from the interbank USD/INR rate and must not be used as rate data.

## Crude oil
PPAC official page:
- URL: https://ppac.gov.in/prices/international-prices-of-crude-oil
- Product: Crude Oil FOB Price (Indian Basket)
- Page exposes a historical report and current report.
- Indian Basket is a blended import basket (Brent Dated + Oman/Dubai), not Brent front-month futures and not FRED DCOILBRENTEU spot Brent. Keep separate identifiers and units. Monthly/yearly report aggregation is not daily observation.
- Existing collector pipeline already has FRED DCOILBRENTEU spot and a separate Yahoo BZ=F proxy. Neither is silently relabelled as PPAC Indian Basket or as an official Brent futures contract.

## FPI/DII and corporate events
- Existing NSDL collector code queries NSDL FPI archive by month and DII daily report by date, restricting to equity / stock-exchange routes. It is a research adapter, not yet accepted evidence for 200-session history.
- Latest fresh P0 collection found only two FPI/DII rows on 2026-11-12 (one FPI and one DII). This is one date, not a historical panel.
- Corporate events bridge accepts only NSE/archives official URLs with a parseable publication timestamp and symbol; its current input ledger has to be verified for completeness and historical session alignment.
- Fresh P0 collector's NSE corporate-announcement API timed out. This is BLOCKED, not empty/zero.

## Concrete next execution order
1. Export RBI DBIE interbank table and RBI reference-rate archive as two separate raw source artifacts. Validate hashes, dates, numeric fields, unit INR/USD, duplicate dates, missingness, max dates, and intersection against the exact 200-session NSE calendar.
2. Export PPAC historical Indian Basket file, inspect whether each sheet/column is daily or monthly, hash the original workbook, and preserve it as a distinct proxy series.
3. Run the existing NSDL FPI/DII collector against the pinned 200-session calendar with bounded timeouts. Report per-series unique dates, missing NSE sessions and provenance. No weekday-generated rows.
4. Reconcile official NSE disclosure source ledgers and bridge only rows with official URL, symbol and publication timestamp. Retain publication-date-vs-event-date distinction.
5. Only then update same-snapshot P0 coverage and factor registry. Do not use the existence of a file as proof of point-in-time or full-history coverage.

## Current accepted status
- RBI DBIE interbank USD/INR: OFFICIAL_SOURCE_IDENTIFIED; DOWNLOAD_AND_FULL_WINDOW_COVERAGE_NOT_VERIFIED; latest indexed date 2026-06-30.
- RBI reference rate: OFFICIAL_ARCHIVE_IDENTIFIED; distinct series; raw archive not ingested in this checkpoint.
- PPAC Indian Basket: OFFICIAL_SOURCE_IDENTIFIED; raw workbook not ingested in this checkpoint.
- FPI/DII: COLLECTOR_CODE_EXISTS; only 1 date observed in latest fresh P0 run; full history BLOCKED.
- Corporate events: BRIDGE_CODE_EXISTS; latest official endpoint timed out; historical coverage BLOCKED.
- P0: 4/8 available in last successful same-snapshot audit.
- Hard Gate: BLOCKED.

## Invariants
₹0 spend; official free sources only for promoted factors; no synthetic observations or timestamps; no forward-fill; no proxy substitution; no paid APIs; no PR merge without explicit approval; production selector, RANKING_SCORE, +1 PRESSURE_FADE and 672 diagnostics unchanged.
