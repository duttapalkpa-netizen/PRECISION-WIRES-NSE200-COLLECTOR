# Global Capital Rotation — India Daily FPI vs NSE FII/DII Source Semantics Checkpoint
Date: 2026-11-17 (Asia/Kolkata)
Scope: Research-only official-source reconciliation. This is a displayed-source evidence checkpoint, NOT raw-byte ingestion, not a historical panel, not a capital-rotation signal and not production approval.

## 1. Why this checkpoint exists
The overlay must not merge CDSL custodian/depository-compiled FPI data with NSE provisional exchange trading activity as though they were the same observation population, confirmation stage, reporting clock or category set. The current official pages expose materially different definitions and timing.

## 2. CDSL daily FPI evidence — displayed official page snapshot
Official daily page: https://www.cdslindia.com/eservices/publications/fiidaily
Official archive: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
Displayed reporting date: 16-NOV-2026. CDSL says the figures are compiled from reports submitted to depositories by custodians on 16-Nov-2026 and constitute trades conducted on and up to the previous trading day(s). The reporting date must not be treated as an intraday timestamp or same-day trade execution timestamp.

Displayed investment subtotals (INR crore):
- Equity: gross purchases 18,571.97; gross sales 13,007.07; net +5,564.90.
- Debt-General Limit: gross purchases 417.84; gross sales 28.37; net +389.47.
- Debt-VRR: gross purchases 289.44; gross sales 237.84; net +51.60.
- Debt-FAR: gross purchases 644.44; gross sales 1,808.11; net -1,163.67.
- Hybrid: gross purchases 29.06; gross sales 25.43; net +3.63.
- Mutual Funds (separately disclosed): gross purchases 5.99; gross sales 24.73; net -18.74.
- Page Total: gross purchases 19,958.74; gross sales 15,131.55; net +4,827.19.

Arithmetic checks:
- Equity net: 18,571.97 - 13,007.07 = +5,564.90.
- Debt-General: 417.84 - 28.37 = +389.47.
- Debt-VRR: 289.44 - 237.84 = +51.60.
- Debt-FAR: 644.44 - 1,808.11 = -1,163.67.
- Hybrid: 29.06 - 25.43 = +3.63.
- Mutual Funds: 5.99 - 24.73 = -18.74.
- FPI investment categories subtotal (Equity + Debt-General + Debt-VRR + Debt-FAR + Hybrid) = +4,845.93.
- Adding separately shown Mutual Funds net (-18.74) reconciles to page Total +4,827.19.
- Therefore the page Total must NOT be labelled FPI net investment; it includes the separately presented Mutual Funds line.

CDSL notes that its conversion rate uses the daily RBI reference exchange rate prevailing on the trading day, with the immediately preceding working-day rate applied when the trading day is a bank holiday. Preserve displayed INR crore and USD million as separate published fields; do not recompute one from the other without recording the source conversion convention.

## 3. NSE FII/FPI & DII daily activity — separate provisional exchange series
Official NSE report page: https://www.nseindia.com/reports/fii-dii
The page exposes two distinct Capital Market Segment downloads: NSE-only; and combined NSE + BSE + MSEI. They must remain separate series. NSE states FII/FPI activity is based on PANs provided by NSDL and is provisional, subject to custodial confirmation/modifications. DII activity is compiled from Trading Member codes and client-category classification supplied by Trading Members. Do not relabel this as custodian-confirmed DII or unique beneficial-owner net subscriptions.
A currently surfaced NSE page snapshot showed a sample report date of 21-Aug-2026. This is not evidence of a current 16-Nov matched DII observation. Do not extrapolate the NSE sample to later dates.
The existing repository contract docs/NSE_FII_DII_DAILY_ACTIVITY_INGESTION_CONTRACT_V1.md remains authoritative for raw-ingestion acceptance. It records that the exact final CSV href and raw bytes were not acquired in the prior audit. Do not repeat generic link-clicking or blocked direct-network attempts. A browser-capable actual download or independently documented official export route is still required.

## 4. SEBI source directory cross-check
SEBI FPI curation page lists NSDL and CDSL links for daily trends, current month and archive data: https://www.sebi.gov.in/curation/fpi.html . This corroborates official source routing for FPI. It does not create a DII series and does not prove NSE daily CSV ingestion.

## 5. Permitted overlay treatment
- Keep CDSL_CONFIRMED_FPI separate from NSE_PROVISIONAL_FII_FPI.
- Keep NSE_DII_PROVISIONAL_EXCHANGE_ACTIVITY separate from both FPI series and from DII holdings/subscription concepts.
- Keep NSE_ONLY and COMBINED_NSE_BSE_MSEI as separate scopes.
- Preserve reporting_date, source publication/retrieval timestamp, actual trade-period wording, confirmation status, category, route, gross buys, gross sales, net value, currency/unit and source URL.
- Do not use CDSL page Total as pure FPI; exclude its separately displayed Mutual Funds line when deriving the FPI-only category subtotal.
- Do not infer global EM flows, US-to-India capital transfer, or investor residence from Indian domestic FPI net purchases.
- Do not align on reporting date alone if source notes indicate different trade coverage or confirmation stages.
- No forward-fill. Missing matched dates remain UNKNOWN.

## 6. Evidence boundary
The 16-Nov-2026 CDSL values above are a web-visible official page snapshot and arithmetic cross-check. In this checkpoint:
- Original downloadable raw CDSL file bytes: NOT ACQUIRED.
- Exact file URL for a raw downloadable snapshot: NOT CAPTURED.
- Retrieval timestamp of raw file: NOT CAPTURED.
- Raw file size and SHA-256: NOT AVAILABLE.
- Full daily historical CDSL panel: NOT RECONSTRUCTED.
- NSE-only CSV raw ingestion: NOT DONE.
- Combined NSE+BSE+MSEI CSV raw ingestion: NOT DONE.
- Matched daily CDSL/NSE FPI/DII panel: NOT DONE.
- Historical predictive/event-study validation: NOT DONE.
Therefore this checkpoint is SOURCE SEMANTICS + DISPLAYED VALUE ARITHMETIC PASS only. It is NOT a raw-ingestion PASS, NOT a daily-panel PASS and NOT overlay acceptance.

## 7. Next bounded actions
1. Acquire CDSL official archive raw bytes for a defined date range; retain original file, exact URL, retrieval timestamp, byte count, SHA-256 and vintage metadata.
2. Acquire both NSE CSV downloads through an actual browser-capable session or independently verified official export route; do not guess endpoints.
3. Validate each series independently: schema, category, units, arithmetic, duplicate keys, source calendar and missing dates.
4. Build a matched-date comparison table with explicit reporting/coverage lag and provisional-vs-custodian source status.
5. Only after those gates, integrate the matched flow panel into the research-only overlay and run a matured historical validation.

## 8. Protected invariants
No change to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, or project Hard Gate. No PR merge, production integration, composite stock score, buy/sell instruction, automatic trading, paid API, external contact, synthetic observation, fabricated timestamp or forward-fill. ₹0 spend.

## 9. Scoped progress
- Official source semantics review: 100%.
- CDSL displayed arithmetic reconciliation: 100%.
- Raw CDSL archival and SHA-256: 0%.
- NSE-only / combined raw CSV acquisition: 0%.
- Matched daily FPI/DII panel: 0%.
- Historical relative-attraction validation: 0%.
- Overall Global Capital Rotation overlay: NOT RE-CALCULATED; this bounded checkpoint does not change the prior 62.5% status.

## 10. MSEI combined FPI/DII snapshot — 17-Nov-2026

Official source: https://www.msei.in/downloads/equity-reports/fii-dii-activities

The official MSEI page displays combined MSE+NSE+BSE capital-market activity for 17-Nov-2026:
- FII/FPI: buy ₹19,930.98cr; sell ₹15,735.60cr; net +₹4,195.38cr.
- DII: buy ₹14,903.80cr; sell ₹14,706.87cr; net +₹196.93cr.
- Arithmetic checks: 19,930.98 - 15,735.60 = +4,195.38; 14,903.80 - 14,706.87 = +196.93.
- MSEI states FII/DII classifications use trading-member client codes/UCC classification and are provisional, subject to custodial confirmation and modifications. NSE and BSE data use their respective exchange classification fields.

This is a combined exchange-provisional cash-market series. Keep it separate from CDSL custodian-confirmed FPI, NSE-only scope and any NSDL/other custodian final series. CDSL 17-Nov reporting page covers trades on/up to previous trading day(s), while MSEI page is dated 17-Nov; displayed dates alone do not prove identical trade-period coverage. Do not reconcile CDSL Equity +₹5,107.61cr to MSEI combined provisional FPI +₹4,195.38cr as though they were the same population or vintage.

Evidence: official MSEI page opened 17-Nov-2026, turn591741view0 lines 335-364. This is displayed-page evidence only. No official downloadable raw file, exact export URL, raw bytes, retrieval timestamp, byte count or SHA-256 was captured. Raw ingestion = NOT_DONE; displayed arithmetic = PASS; matched panel admission = BLOCKED.

## 11. NSE-only vs combined NSE+BSE+MSEI CSV snapshot — byte and arithmetic QA — 2026-11-17

The two Library-held CSV files were materialized as original raw bytes and independently hashed:
- Combined snapshot `fii-dii-combined-latest.csv`: 218 bytes; SHA-256 `2697546fa012f4c08449b37a3eb7d0f8298f296c25fd8ce4b7ca134c37999eb2`.
- NSE-only snapshot `fii-dii-nse-latest.csv`: 218 bytes; SHA-256 `b733444b5a846abb672226bc96448bc0baea2da0ad15fe810207fbe93aad7f18`.
- Both contain only 13-Nov-2026 DII and FII/FPI rows, in INR crore. These are one-date snapshots, not historical panels.

Recomputed net = buy - sell; 4/4 values match the stored net:
- Combined FII/FPI: 18,339.57 - 12,603.02 = +5,736.55.
- Combined DII: 11,745.95 - 13,999.53 = -2,253.58.
- NSE-only FII/FPI: 17,376.50 - 12,122.52 = +5,253.98.
- NSE-only DII: 10,561.32 - 12,532.05 = -1,970.73.

Combined minus NSE-only scope differences (crore): FII/FPI buy +963.07, sell +480.50, net +482.57; DII buy +1,184.63, sell +1,467.48, net -282.85. These are differences between two provisional exchange-scope datasets, not a third flow series or CDSL residual.

Important hash-label correction: `2697546f...99eb2` is COMBINED; `b733444b...7f18` is NSE-ONLY. Preserve this mapping.

Official NSE report page separately exposes the two CSV downloads and notes provisional/custodial-confirmation semantics: https://www.nseindia.com/reports/fii-dii . Evidence: `turn119296view0` lines 128-134 and 118-127. The exact original download URLs and HTTP response metadata were not captured; Library byte integrity is verified, upstream transport provenance remains PARTIAL. Do not claim full raw-ingestion or daily-panel PASS.
