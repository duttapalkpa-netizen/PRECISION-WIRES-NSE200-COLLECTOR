# PRECISION-WIRES NSE200 COLLECTOR

Automated NSE historical backbone, Security Master enrichment, adaptive V11.3 technical core and IPO-PLX V2.0 early-listing foundation.

## Master architecture
NSE Historical Backbone -> Security Listing-Age Detection -> Adaptive History Engine -> Track A V11.3 + Track B IPO-PLX V2.0 -> A/B/C/D/E -> Risk Modifier -> Live 1% -> Finalist

**200+ sessions is the market historical backbone, NOT a stock-level eligibility gate.**

The collector keeps securities with fewer than 200 observations. Missing long-history indicators are not treated as bearish: valid negative signal = NEGATIVE; unavailable because history is too short = NOT_APPLICABLE; unexpectedly missing data = UNKNOWN.

## Adaptive routing
200+ = FULL V11.3
100-199 = EXTENDED V11.3
50-99 = DEVELOPING V11.3
20-49 = EARLY V11.3
5-19 = EARLY EXPANSION ENGINE
1-4 = IPO-PLX V2.0
0 = DATA UNAVAILABLE

Every analysed security carries: SCORE + HISTORY_DEPTH + ANALYSIS_MODE + DATA_CONFIDENCE.
Additional metadata: LISTING_DATE, LISTING_DATE_SOURCE, AGE_SESSIONS, OBSERVATION_COVERAGE_PCT.

## Collector layers
collector/nse_download.py: current CM-UDiFF archive first, legacy fallback, NSE bootstrap, 200 valid market sessions, acquisition diagnostics.
collector/security_master.py: NSE equity master acquisition for SYMBOL, ISIN and LISTING_DATE.
collector/build_200_sessions.py: normalisation, EQ filtering, deduplication, security coverage, listing/age metadata and adaptive routing.

## Track A — V11.3
pipeline/v11_3_abcd_e.py is the current data-backed technical-core implementation of A/B/C/D/E. It is not claimed to be the complete 672-signal live system.

## Track B — IPO-PLX V2.0
pipeline/ipo_plx_v2.py is the current 1-4-session early-listing foundation. It measures listing-to-current expansion, OHLC structure, VWAP proxy, volume/RVOL proxy, HH/HL and absorption proxy.
Subscription, GMP, effective float, anchor lock-up, queue, first-hour ORB/VWAP and catalyst inputs are explicitly UNKNOWN until dedicated sources are wired.
Output: outputs/ipo_plx/ipo_plx_candidates.csv

## Risk Modifier
pipeline/risk_modifier.py keeps external risk inputs UNKNOWN until connected and explicitly preserves SCORE + HISTORY_DEPTH + ANALYSIS_MODE + DATA_CONFIDENCE.
Output: outputs/finalists/v11_3_risk_adjusted.csv

## Workflow
1. Acquire 200 NSE market sessions
2. Acquire NSE Security Master
3. Build normalized adaptive dataset
4. Strict QA
5. V11.3 A/B/C/D/E technical core
6. IPO-PLX V2.0 foundation
7. Risk Modifier
8. Upload processed data and outputs as artifact

## Explicit implementation boundary
The corrected adaptive collector architecture is implemented.
Still not claimed live: all 672 diagnostics; full corporate catalyst; research-house; FII/DII; macro/geo-shock; true first-hour Live 1%; full IPO historical cohort/winner separation lab; full IPO subscription/GMP/effective-float/queue integration.

These unavailable inputs are marked UNKNOWN rather than fabricated.

## Core principle
**Collect deep. Analyse adaptively. Preserve short-history opportunity. Never convert missing history into a negative signal.**