# Daily dollar-pressure and USD/INR source coverage audit
Date: 2026-11-11
Scope: official-source coverage/access verification only. No raw observations downloaded or ingested in this audit.

## 1. Federal Reserve H.10 — daily dollar indices
Official package review:
https://www.federalreserve.gov/datadownload/Review.aspx?filetype=csv&label=include&lastobs=10&layout=seriescolumn&rel=H10&series=122e3bcb627e8e53f1bf72a1a09cfb81&type=package

Verified package metadata:
- Release: G.5/H.10 Foreign Exchange Rates
- Last release displayed: 2026-11-09
- Selected series count: 3
- H10/H10/JRXWTFB_N.B — Nominal Broad Dollar Index
- H10/H10/JRXWTFN_N.B — Nominal Advanced Foreign Economies Dollar Index
- H10/H10/JRXWTFO_N.B — Nominal Emerging Market Economies Dollar Index
- Each series: 5,440 observations, 2006-01-02 through 2026-11-06.
- The preview for Broad Dollar Index shows latest values and unit Index (1997 Jan=100); this is a Fed index, not ICE DXY.

Important boundary:
The review page is explicitly a "Last 10 Obs" CSV package (0.79 KB). It proves series identity and available coverage, but is NOT the full historical CSV. Do not ingest it as the full series. The Federal Reserve page's preview is also not a raw full-history file.

## 2. RBI DBIE — daily interbank USD vis-a-vis INR
Official table:
https://dbie.rbihub.in/tables?table=financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr

Verified catalogue metadata from indexed official table:
- Source: Reserve Bank of India (DBIE)
- Frequency: Daily
- Period: 2000-08-08 through 2026-06-30
- Displayed rows: 6,319
- Fields include interbank open/high/low/close and RBI reference rate.
- CSV and JSON download controls are listed.

Boundary:
The table page's indexed metadata confirms the series and coverage. The actual CSV/JSON bytes, exact export URL, retrieval timestamp, file size and SHA-256 were not obtained in this audit. Therefore no observation ingestion or row-level QA is claimed.

## 3. BIS USD/INR cross-check route
BIS daily bilateral exchange-rate topic:
https://data.bis.org/topics/XRU
BIS overview states daily series cover around 80 economies; latest daily observations are sourced primarily from ECB and complemented by Federal Reserve, with historical periods also sourced from other central banks, Bundesbank and IMF IFS. BIS updates weekly.
The indexed India monthly series M.IN.INR.E is monthly, 1957-01 to 2026-09; it is NOT a substitute for the daily series. No daily raw BIS series bytes or checksum were captured here.

## 4. Source-use rules
- Fed H.10 broad dollar index is a broad trade-weighted USD index; do not label it DXY.
- Keep broad, advanced-economy, and EM dollar indices separate.
- RBI DBIE USD/INR interbank rates and RBI reference rates are distinct columns; preserve both.
- BIS USD/INR is an independent reference series with its own observation-time/source conventions; do not silently splice with RBI.
- Preserve holidays/missing observations; no forward fill, synthetic dates, or calendar alignment by fabrication.
- Record exact raw URL, query/export parameters, retrieval UTC, publication/vintage date, reference period, bytes, media type and SHA-256 before transformation.

## 5. Gate result
- Official source identity and coverage: PASS (scoped).
- Full raw historical CSV acquisition: NOT DONE.
- SHA-256/provenance manifest: NOT DONE.
- Schema and row-level QA: NOT DONE.
- Fed/RBI/BIS cross-source reconciliation: NOT DONE.
- Capital-flow inference: NOT ESTABLISHED.
- Overlay milestone 6 actual ingestion: remains 0% actual observations; design/source mapping progress remains 20% under the prior conservative ledger.
- Overlay overall: remains 62.5% (5/8 milestones); do not increase.
- Production integration: prohibited without explicit approval.

## 6. Invariants
No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), Engines A-E, or Hard Gate. No composite stock score/ranking, buy/sell instruction or automatic trading. ₹0 spend; public official sources only; no paid APIs; no synthetic data.
