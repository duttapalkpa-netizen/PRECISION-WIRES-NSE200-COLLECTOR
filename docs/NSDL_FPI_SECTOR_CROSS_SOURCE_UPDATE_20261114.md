# NSDL FPI Sector-wise Cross-source Update — 2026-11-14

## Official latest report identified
- Official NSDL fortnightly sector-wise FPI report for 31-Oct-2026 is available at https://pilot.fpi.nsdl.co.in/StaticReports/Fortnightly_Sector_wise_FII_Investment_Data/FIIInvestSector_Oct312026.html (web evidence turn177159search2).
- It reports the 01–15 Oct and 16–31 Oct fortnight windows, AUC as at 15-Oct and 31-Oct, with separate Equity, Debt, Hybrid, Mutual Funds and AIF categories.
- Grand Total net Equity investment for 16–31 Oct 2026: +₹13,112 crore. Equity AUC at 31-Oct: ₹65,25,808 crore. The same official report shows 01–15 Oct equity net investment −₹47,955 crore and 15-Oct equity AUC ₹65,94,378 crore.
- Sequential equity flow arithmetic across the two reported fortnights: −₹47,955 + ₹13,112 = −₹34,843 crore net across 01–31 Oct. This is a derived two-window sum, not a daily flow or a separate source observation.
- The NSDL report identifies itself as FPI sector-wise data and the report's full category structure should be retained; do not add debt/hybrid/MF/AIF flows into equity.
- Official report page's visible Automobile and Auto Components row: equity AUC ₹4,77,593 crore at 15-Oct; equity net investment −₹6,533 crore for 01–15 Oct; equity net investment −₹1,098 crore for 16–31 Oct; equity AUC ₹4,74,488 crore at 31-Oct. This is a single row check, not full sector-table reconciliation.
- NSDL 31-Oct data is later than CDSL's 15-Oct sector report. It extends the sector timeline but does not establish a CDSL-vs-NSDL same-date discrepancy. The two official depository reports' date, coverage and methodology must be explicitly aligned before any reconciliation.

## Research interpretation
- The sequence shows large first-half October equity outflow (−₹47,955cr) followed by a second-half inflow (+₹13,112cr); full-month net remains −₹34,843cr. This is a flow-horizon observation, not a price forecast.
- Auto & Auto Components second-half outflow slowed from −₹6,533cr to −₹1,098cr in the NSDL report. Do not call this a reversal to inflow.
- Do not infer sector stock returns, issuer-level exposures, causality or H+1/H+3/H+5 probabilities from flow alone.

## Status
- Official NSDL 31-Oct report discovery and key total/one-row extraction: DOCUMENTED; arithmetic PASS.
- Complete 24-sector extraction, all-category arithmetic, CDSL/NSDL method reconciliation, raw file bytes/hash, multi-period time series, NSE sector-index return joins and rolling predictive validation: NOT RUN / NOT ACQUIRED.
- No synthetic data, no production selector/ranking/CORE-672 changes, no PR/merge. Hard Gate remains BLOCKED.


## Full NSDL Grand Total and same-period CDSL/NSDL aggregate cross-check — 2026-11-14

- Official NSDL report Grand Total row (turn683882view0 line 32): equity AUC at 15-Oct ₹65,94,378cr; equity net investment 01–15 Oct −₹47,955cr; equity net investment 16–31 Oct +₹13,112cr; equity AUC at 31-Oct ₹65,25,808cr.
- NSDL report total net investment across all reported categories is −₹45,828cr for 01–15 Oct and +₹21,354cr for 16–31 Oct; these are NOT equity-only totals. Preserve this distinction.
- NSDL Grand Total equity net flow for 01–15 Oct (−₹47,955cr) exactly matches the CDSL 15-Oct report Grand Total equity net flow (−₹47,955cr) recorded in the prior CDSL sector audit. This is an aggregate same-period cross-source arithmetic/consistency check: MATCH at displayed ₹ crore precision. It is not proof of row-by-row identical classification, raw source identity or full historical completeness.
- NSDL full report also shows the 16–31 Oct total equity inflow +₹13,112cr. Two-period equity sum: −₹47,955 + ₹13,112 = −₹34,843cr (derived; arithmetic PASS). The NSDL all-category total across the same two windows is a different measure and must not be substituted.
- The report lists 22 BSE Common Industry sectors plus Sovereign and Others (24 rows). Sovereign is government securities, not an industry sector; Others contains exposures outside the ~4,800 BSE-classified issuer universe. Do not map these two rows into industry equity buckets.
- Critical correction to previous wording: the prior summary used “full 24-sector panel”; the source actually has 22 industry sectors plus Sovereign and Others. Use this exact taxonomy in all future analyses.
- The source page's line 32 displays first-period all-category total −₹45,828cr, while equity-only is −₹47,955cr; second-period all-category total +₹21,354cr, while equity-only is +₹13,112cr. This difference is expected because the totals include debt, hybrid, MF and AIF categories.
- USD conversion in this report uses period-end RBI rates: 95.0691 for 15-Oct and 95.2492 for 31-Oct; daily FPI net investment USD conversion uses daily RBI reference rate. Preserve INR as the primary comparison unit.
- Official source: https://pilot.fpi.nsdl.co.in/StaticReports/Fortnightly_Sector_wise_FII_Investment_Data/FIIInvestSector_Oct312026.html (turn199115view0 lines 3–32; turn683882view0 lines 32–63).


## NSE sector-index mapping and return-panel specification — 2026-11-14

### Official index inventory
- NSE's historical reports directory links Historical Index Data to NSE Indices and separately exposes historical India VIX and daily/monthly index report archives (web evidence turn783238view2 lines 187–196).
- NSE Indices historical-data selector lists sectoral indices including NIFTY AUTO, NIFTY CAPITAL GOODS, NIFTY CHEMICALS, NIFTY CONSTRUCTION, NIFTY CONSUMER DURABLES, NIFTY CONSUMER SERVICES, NIFTY FINANCIAL SERVICES, NIFTY FMCG, NIFTY HEALTHCARE, NIFTY IT, NIFTY MEDIA, NIFTY METAL, NIFTY OIL AND GAS, NIFTY POWER, NIFTY REALTY, NIFTY TELECOMMUNICATIONS and NIFTY SERVICES SECTOR (web evidence turn250731view0 lines 59–88, 112–129). Historical-data page provides date-range selection and CSV format for index observations (lines 383–432).
- NSE All Reports page separately exposes daily CM-UDiFF bhavcopy, security-wise delivery positions, historical index data and India VIX; the old CM common bhavcopy is marked discontinued since 08-Jul-2024 and replaced by CM-UDiFF (web evidence turn783238view1 lines 169–225; turn783238view2 lines 187–196).

### 22-sector mapping contract (candidate index only; no constituent equivalence implied)
| NSDL/BSE sector label | Candidate NSE/Nifty index | Mapping status |
| Automobile and Auto Components | NIFTY AUTO | Label-aligned candidate |
| Capital Goods | NIFTY CAPITAL GOODS | Label-aligned candidate |
| Chemicals | NIFTY CHEMICALS | Label-aligned candidate |
| Construction | NIFTY CONSTRUCTION | Label-aligned candidate |
| Construction Materials | NIFTY CEMENT | Proxy only; not equivalent |
| Consumer Durables | NIFTY CONSUMER DURABLES | Label-aligned candidate |
| Consumer Services | NIFTY CONSUMER SERVICES | Label-aligned candidate |
| Diversified | None identified | No direct index |
| Financial Services | NIFTY FINANCIAL SERVICES | Label-aligned candidate; constituent scope may differ |
| Forest Materials | None identified | No direct index |
| FMCG | NIFTY FMCG | Label-aligned candidate |
| Healthcare | NIFTY HEALTHCARE | Label-aligned candidate; not interchangeable with Pharma |
| Information Technology | NIFTY IT | Label-aligned candidate |
| Media, Entertainment & Publication | NIFTY MEDIA | Label-aligned candidate |
| Metals & Mining | NIFTY METAL | Label-aligned candidate |
| Oil, Gas & Consumable Fuels | NIFTY OIL AND GAS | Label-aligned candidate |
| Power | NIFTY POWER | Label-aligned candidate |
| Realty | NIFTY REALTY | Label-aligned candidate |
| Services | NIFTY SERVICES SECTOR | Broad proxy candidate; classification scope may differ |
| Telecommunication | NIFTY TELECOMMUNICATIONS | Label-aligned candidate |
| Textiles | None identified | No direct index |
| Utilities | None identified | No direct index; do not substitute NIFTY POWER |

### Required validation before any return join
- Index names above are candidate benchmarks, not proven identical constituent universes. Obtain dated constituent files and methodology effective dates before calculating constituent overlap or assigning a sector return.
- Keep a separate mapping_status field: LABEL_ALIGNED_CANDIDATE / PROXY_ONLY / NO_DIRECT_INDEX / UNVALIDATED_CONSTITUENTS. Do not force the four no-direct rows or the proxy row into a benchmark.
- Use Nifty Indices historical CSV for index OHLC and preserve price-index vs total-return-index distinction. NSE historical index page exposes separate historical index data and total-return index values; do not mix them.
- NSDL flow observation window is 16–31 Oct 2026. It is not a daily observation. A backtest signal is usable only after the report's actual public availability timestamp is established. The first eligible NSE session is the next trading session after that timestamp, not automatically 01-Nov or 31-Oct.
- For each eligible sector, calculate forward index returns from the next eligible close: H+1, H+3, H+5 trading sessions; apply 0.22% transaction cost consistently. Preserve unadjusted vs total-return benchmark choice and pre-register one primary benchmark per sector.
- Global controls to be lagged as-of decision time: NIFTY 50 regime, India VIX, USD/INR, Brent, US yields/Fed event, FPI cash flow, domestic institutional flow and sector breadth. These are control variables, not a licence to infer causality.
- This mapping is a research design deliverable only. No historical return series downloaded or joined in this step; no model performance, predictive edge or trading signal is claimed.


## Full NSDL 16–31 Oct 2026 equity sector panel and row-sum QA

Source: official NSDL report, lines 8–32 (web evidence turn381834view0 and turn198123view0).

| BSE common-industry sector | Equity net flow 16–31 Oct 2026 (₹ crore) |
|---|---:|
| Automobile and Auto Components | −1,098 |
| Capital Goods | −825 |
| Chemicals | −862 |
| Construction | −516 |
| Construction Materials | −196 |
| Consumer Durables | −402 |
| Consumer Services | −662 |
| Diversified | −16 |
| Fast Moving Consumer Goods | −1,559 |
| Financial Services | −883 |
| Forest Materials | −58 |
| Healthcare | −57 |
| Information Technology | +10,915 |
| Media, Entertainment & Publication | +140 |
| Metals & Mining | −904 |
| Oil, Gas & Consumable Fuels | −970 |
| Power | −765 |
| Realty | −438 |
| Services | +658 |
| Telecommunication | +11,065 |
| Textiles | −21 |
| Utilities | −27 |

### Row-sum reconciliation
- Sum of the 22 industry-sector equity rows above = +₹12,519 crore.
- NSDL Others-category equity net investment = +₹594 crore.
- Sovereign-category equity = ₹0 crore.
- Sum of displayed rows including Others and Sovereign = +₹13,113 crore.
- NSDL Grand Total equity net investment = +₹13,112 crore.
- Difference = +₹1 crore (row-sum exceeds displayed Grand Total). Treat as a ₹1 crore displayed-value rounding/reconciliation residual; do not force-adjust any sector or classify it as an error without source precision evidence. The aggregate Grand Total remains the authoritative reported value.
- This explicit row-sum check improves QA: the table does not reconcile exactly at integer-crore display precision. Keep reconciliation_status = ROUNDING_RESIDUAL_1CR, not PASS_EXACT.

### Interpretation
- The second-half October equity flow is concentrated in Information Technology (+₹10,915cr) and Telecommunication (+₹11,065cr), while many other sectors remain net sellers. This is descriptive allocation concentration, not a sector price-return signal or proof of causal rotation.
- Full 22-sector 16–31 Oct equity panel: TRANSCRIBED. Displayed row-sum reconciliation: 1 crore residual. No historical NSE index return series has been downloaded or joined. No H+1/H+3/H+5 performance claim.



## Appendix: NSE sector benchmark methodology revalidation and crosswalk risk correction — 2026-11-14

### Source-level findings
- NSE Indices Historical Data page provides a selector containing sector/thematic indices, date-range inputs and CSV-format output; it also exposes a separate Total Returns Index Values section (official page https://www.niftyindices.com/reports/historical-data; web evidence turn256653view0 and turn879354search1).
- The selector includes NIFTY AUTO, CAPITAL GOODS, CEMENT, CHEMICALS, CONSTRUCTION, CONSUMER DURABLES, CONSUMER SERVICES, FINANCIAL SERVICES, FMCG, HEALTHCARE, IT, MEDIA, METAL, OIL AND GAS, POWER, REALTY, TELECOMMUNICATIONS and SERVICES SECTOR (turn256653view0 lines 59–88, 112–129).
- The March 2026 NSE Indices Equity Index Methodology PDF's sectoral index contents explicitly enumerate Auto, Bank, Chemicals, Consumer Durables, FMCG, IT, Media, Metal, Oil & Gas, Pharma, PSU Bank, Private Bank, Realty, Cement, Financial Services, Healthcare, etc. It does not list NIFTY CONSTRUCTION, NIFTY CAPITAL GOODS, NIFTY POWER or NIFTY TELECOMMUNICATIONS as sectoral indices in its sectoral index contents (turn256653view1 lines 29–56). The same document separately lists thematic indices including Nifty Capital Markets, Commodities, Energy, Infrastructure and Services Sector (lines 57–84).
- Therefore, a selector-visible index name alone is not sufficient to certify an NSDL BSE sector mapping or a sectoral classification. The previously recorded label-aligned candidates for Capital Goods, Construction, Power and Telecommunications must be downgraded to SELECTOR_VISIBLE_METHODOLOGY_SCOPE_UNVERIFIED pending their own current methodology/factsheet and constituent files. Do not silently call them confirmed sectoral benchmark matches.
- Construction Materials → NIFTY CEMENT remains PROXY_ONLY; NIFTY CEMENT's presence in sectoral index contents does not prove identical BSE Construction Materials constituents. Healthcare → NIFTY HEALTHCARE also requires constituent overlap validation; methodology PDF lists Nifty Healthcare, while the historical selector uses the label “Nifty HEALTHCARE”. Do not assume name-only equivalence.
- Methodology document states index reconstitution/rebalancing schedules differ by index; for example, sectoral indices include semiannual reviews and some thematic indices have separate schedules (turn302571view1 lines 1468–1472; turn256653view1 lines 29–84). Historical constituent universe must be point-in-time and effective-date aligned, not current constituents projected backwards.
- NSE methodology PDF documents free-float weighting and capping rules; constituent weights can drift between rebalances (turn879354search9; turn302571view1). Thus index returns can be used as benchmark observations, but not as proof that NSDL sector classification has matching constituents.
- Historical-data page has separate historical index price/OHLC and Total Returns Index values. Pre-register TRI as primary performance measure where available, retain price index as a separate series, and never mix them (turn879354search1; turn256653view0).

### Acquisition status and next gate
- UI/source availability and benchmark taxonomy revalidation: DOCUMENTED.
- No date-range was submitted and no historical CSV bytes were downloaded in this audit. No file size, response headers, source-file SHA-256 or row-level date continuity is available. This step does not count as index-data acquisition.
- Next eligible action: obtain each candidate index's own factsheet/methodology and point-in-time constituent file, then acquire date-bounded TRI/price-index CSVs through official interface; hash original bytes and validate session calendar, duplicate dates, missing dates, OHLC constraints and TRI continuity.
- Do not calculate any FPI-to-sector-return relationship until NSDL publication timestamp, period-end date, next eligible NSE session and index-specific mapping status are verified.



## Return-series definition and transaction-cost convention audit — 2026-11-14

### NSE official return-series distinction
- NSE Indices historical-data page exposes separate Historical Index Data and Total Returns Index Values outputs; the latter table contains both “Total Returns Index” and “Net Total Return Index” columns (official source https://www.niftyindices.com/reports/historical-data; web evidence turn476755search2).
- NSE's TRI explainer states a price index captures constituent price movement but excludes dividends; Total Returns Index incorporates dividend receipts and reinvests indexed dividends on ex-dates. NSE says investors should benchmark against TRI rather than price index for actual investment returns (https://www.nseindia.com/static/products-services/indices-total-returns-index; web evidence turn476755search3).
- Therefore, the earlier phrase “TRI as primary” is refined: acquire and preserve **Price Index**, **TRI**, and **NTRI** as distinct series wherever the official source provides them. Do not relabel NTRI as TRI or combine their levels/returns.
- Before selecting the primary benchmark, record the exact NSE series definition and availability for each candidate index. For a gross market-performance study, TRI is the dividend-inclusive series explained by NSE; NTRI must remain separately available and its net-return treatment must be confirmed from its own official definition before primary selection. Price-index results remain a sensitivity/price-only comparator.
- The NSE historical-data page's generic table is OHLC for index price data; its TRI section has Date, Total Returns Index and Net Total Return Index. Do not assume TRI/NTRI has OHLC fields or manufacture them from closes.

### Transaction-cost convention (pre-registration, not a new measured result)
- For a long-only entry/exit round trip, a 0.22% total round-trip cost is applied once to gross forward return: net return = (1 + gross return) × (1 − 0.0022) − 1. If the project's 0.22% convention is instead per-side, the two-sided cost must be explicitly recalculated and documented before results are produced; never subtract 0.22% twice by assumption.
- If using simple-return approximation only, net ≈ gross − 0.22 percentage points; exact multiplicative calculation above is preferred.
- No index CSV or daily return observations were downloaded in this audit. This is a methodology/control correction only; no performance results or predictive edge claimed.



## Official NSE historical-data interface schema and eligible benchmark inventory — 2026-11-14

### Direct official-page reinspection
- Re-opened https://www.niftyindices.com/reports/historical-data (web evidence turn100955view0, lines 383–432 and 561–567).
- Official page separates four report groups: Historical Index Data, Archives of Daily/Monthly Reports, P/E/P/B/Dividend Yield values, and Total Returns Index Values.
- Historical Index Data output schema shown by the page: Date, Open, High, Low, Close. The TRI output schema is separate and shows Date, Total Returns Index, Net Total Return Index. The TRI section does not show OHLC fields. Do not manufacture TRI OHLC.
- The same page's navigation classifies Equity index families into Broad Based, Sectoral, Thematic and Strategy (lines 9–16). It lists many candidate names, including NIFTY AUTO, CAPITAL GOODS, CEMENT, CHEMICALS, COMMERCIAL & TRANSPORT SERVICES, CONSTRUCTION, CONSUMER DURABLES, CONSUMER SERVICES, FINANCIAL SERVICES, FMCG, HEALTHCARE, IT, MEDIA, METAL, OIL AND GAS INDEX, PHARMA, POWER, REALTY, TELECOMMUNICATIONS and SERVICES SECTOR (lines 59–89, 112–129).
- This page's navigation is an index directory, not by itself evidence of the selected index's subcategory or methodology. Category membership must be established from index-specific factsheet/methodology and dated constituents; navigation presence alone does not upgrade a mapping.
- Page currently shows “Select an Index and Time Period to view data” and “No Data Found” before user selects index/date (lines 417–422, 465–471, 554–567). This is a blank unselected UI state, not proof that historical data is unavailable.
- Page provides CSV format controls for historical data and TRI sections (lines 426, 452, 521, 561), but no selected index/date or CSV payload was returned in this static inspection. Therefore no raw CSV bytes, row counts, headers, byte size or SHA-256 were acquired.

### Benchmark inventory status (no overclaim)
- Candidate name inventory revalidated; actual sector mapping still depends on category/methodology and point-in-time constituent overlap.
- Historical price-index schema is confirmed as OHLC; TRI/NTRI schema is confirmed as date + separate index values only.
- Empirical return panel remains NOT ACQUIRED. Next step must use the official UI with a selected eligible index and bounded date range, download the CSV, preserve original bytes and metadata, hash it, then validate dates and values.
- No undocumented POST endpoint or third-party reverse-engineered API specification is adopted as an official source contract.


## 54. Walk-forward backtest transaction-cost implementation audit — 2026-11-14

### Scope and exact source
- Audited branch `research/corporate-events-rss-collector-v1-20261114`, source file `pipeline/walk_forward_backtest.py`.
- Source blob SHA at audit: `d085f7a2d35a88b4c4eaba65144a429a06961b09`.
- This is a read-only code audit; no code, selector, ranking, thresholds, dataset or workflow changed.

### Findings
- Script header identifies the engine as “PRECISION-WIRES V11.4 Walk-Forward Behavioural Validation”; do not silently label this artifact as V11.3 production-parity.
- Forward outcomes are calculated as `FUT{h}_HIGH_PCT` and `FUT{h}_CLOSE_PCT` from future high/close observations relative to current close. Metrics then evaluate thresholds against `FUT{h}_HIGH_PCT`.
- Full-file literal scan found no transaction-cost, fee, commission, slippage, 0.22 or 0.0022 implementation in this script.
- Therefore the currently implemented target/precision/recall/lift calculations are gross-price excursion measures, not verified net-of-cost returns. The 0.22% convention is not implemented in this script.
- Applying a flat cost to the future-high excursion alone would not establish executable round-trip net return: the high is a maximum excursion, not a defined exit fill. Keep gross excursion targets distinct from executable entry/exit net-return metrics.
- Do not patch production or this research script in this audit. Before any net-performance claim, resolve whether 0.22% is round-trip or per-side from an authoritative project specification, define entry and exit execution prices (including same-session/next-session convention), then implement a separately labelled net-return metric with tests. Preserve gross target labels for comparability.
- This finding does not prove that no other project component applies costs; it establishes only that this inspected walk-forward script does not.

### Status
- Scoped script inspection and cost-presence audit: 100% complete.
- Authoritative 0.22% convention resolution: NOT RESOLVED.
- Executable net-of-cost backtest and tests: 0% / NOT RUN.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED. No PR/merge; no production invariants changed.
