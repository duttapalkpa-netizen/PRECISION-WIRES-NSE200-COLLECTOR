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
