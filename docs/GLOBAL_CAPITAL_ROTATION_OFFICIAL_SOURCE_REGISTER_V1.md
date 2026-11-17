# Global Capital Rotation — Official/Primary Source Register V1
Audit date: 2026-11-10 (Asia/Kolkata)
Scope: free public sources only; research overlay, not production approval.

| Layer | Primary source / series | Frequency and coverage seen | Use | Current status / limitation |
|---|---|---|---|---|
| Cross-border portfolio transactions | IMF Balance of Payments (BOP), financial account, portfolio investment assets/liabilities | Annual and quarterly; country reporting | Net portfolio transactions by instrument and direction; derive EM aggregate only after documented country/region aggregation and consistent vintages | Dataset + SDMX 2.1/3.0 API route VERIFIED; IMF-maintained BOP DSD V2.6.0 public unauthenticated registry URL identified. Raw DSD XML not yet parsed/archived; BOP observation download, country panel and EM aggregation NOT YET DONE. IMF Data Portal Swagger explorer requires beta portal sign-in; no observation payload authenticated or validated in this audit. Not a daily trigger. |
| Cross-border portfolio positions | IMF Portfolio Investment Positions by Counterpart Economy (PIP, formerly CPIS) | Annual / half-yearly | Holdings by counterpart economy and instrument; structural allocation context | SOURCE VERIFIED; positions are stocks, NOT flows. Never substitute for BOP transactions. |
| India FPI | CDSL daily trends/archive; NSDL FPI data; SEBI | Daily/monthly | India equity, debt, hybrid FPI, separate reporting periods | CDSL snapshot through 2026-11-09 reconciled; India MTD +₹53,738.78cr, YTD -₹2,41,407.13cr. CDSL reports custodian data received 2026-11-10 for trades on/up to prior trading day(s). |
| India domestic institutional flow | NSE/SEBI exchange and depository publications | Daily/monthly, dataset-specific | DII equity purchases/sales; separate mutual fund flows where published | Source routes identified; consistent daily series not yet ingested. |
| US broad dollar | Federal Reserve H.10 / FRED DTWEXBGS (Nominal Broad U.S. Dollar Index) | Daily; latest observation surfaced 2026-11-06 = 121.8803 | Broad trade-weighted USD pressure proxy | SOURCE + latest observation verified. This is NOT ICE DXY. Keep separate indicator name; do not label as DXY. |
| US nominal yields | Federal Reserve H.15 / FRED DGS10; US Treasury daily par curve | Daily; latest surfaced DGS10 observation 2026-11-02 = 4.91% | US nominal rate / opportunity-cost channel | SOURCE VERIFIED; observation needs a synchronized vintage before calculating 20-day changes. |
| US real yields | Federal Reserve H.15 / FRED DFII10; Treasury real yield curve | Daily; latest surfaced FRED observation 2026-09-10 = 2.55% | Real-rate / discount-rate channel | SOURCE VERIFIED; surfaced observation is stale for live signal. Remain UNKNOWN until fresh series loaded. |
| USD/INR | RBI Reference Rate Archive; RBI DBIE daily interbank forex table | RBI archive searchable/downloadable; DBIE table observed through 2026-06-30 | INR translation and FX risk; reference rate distinct from intraday spot | SOURCE VERIFIED. DBIE table is stale beyond 2026-06-30 in current web snapshot; fetch RBI archive vintage for live dates. Do not mix reference and interbank close without field labels. |
| Crude | US EIA Europe Brent Spot Price FOB, daily series RBRTED | Daily; latest table surfaced partial week 2026-11-02 to 06 | Oil-import sensitivity | SOURCE VERIFIED; latest week incomplete in surfaced table. Wait for complete daily observations before 20-day return. |
| US equity volatility | Cboe VIX historical daily close | Daily, 1990–present | Risk appetite / volatility state | PRIMARY EXCHANGE SOURCE VERIFIED; not a government statistical series. Download historical data and preserve Cboe disclaimer. |
| India equity relative return | NSE historical index data / NSE Indices historical reports and TRI | Daily; selectable index and total-return series | India vs global/EM benchmark comparison; sector breadth | SOURCE VERIFIED. Need matched trading-day calendars and total-return series, not price-only index if comparing investment returns. |
| Global equity benchmark | Official index-provider historical total-return data, subject to free public availability | Daily or monthly depending provider | India vs World/EM comparison | Public free official coverage not yet established for a full matched TRI panel; remain UNKNOWN until verified. |
| Policy events | White House, Federal Register, Congress.gov, USCIS, official court orders | Event-driven | Tariffs, H-1B, AI policy, enacted/proposed/stayed status | Primary-source-only event status. Media reports are discovery/context, not enacted policy evidence. |
| Sector/company bridge | NSE filings, BSE filings, company annual reports/results/investor presentations, official order disclosures | Event/quarterly | Revenue geography, export mix, client concentration, order book, FX/input sensitivity | Not yet systematically extracted and reconciled to sector constituents. |

## Critical measurement rules
1. IMF BOP portfolio investment financial-account transactions are flow data. IMF PIP/CPIS is holdings/position data. Do not combine or relabel positions as flows.
2. The Federal Reserve's DTWEXBGS is a nominal broad trade-weighted dollar index. It is not the ICE US Dollar Index (DXY). Use distinct variable names and never silently substitute.
3. Treasury nominal yields and TIPS real yields are separate series. A fall in nominal 10Y alone does not establish lower real discount rates or risk-on conditions.
4. RBI reference rate, RBI DBIE interbank open/high/low/close, and other market spot rates are different observations. Keep source field and rate type explicit.
5. EIA's daily Brent spot series is not a futures settlement series. Preserve price type and incomplete-week handling.
6. Cboe VIX is a primary exchange-published volatility index, but not a government source. Mark source class as PRIMARY_EXCHANGE.
7. Relative returns must compare synchronized dates and comparable total-return indices; price-index comparisons can omit dividends.
8. All series need published_at, as_of_date, retrieved_at, source URL, units, source class, and revision/vintage fields. No forward-fill across holidays or missing observations.
9. IMF country/region aggregation must declare included economies, weights, instrument coverage, net/gross basis, and missing reporters before an EM aggregate is accepted.
10. Current verified source availability does not equal ingested observations, active signal, predictive edge, or production readiness.

## Current acceptance
- Source route discovery: PASS for CDSL, RBI, Fed/FRED, Treasury, EIA, Cboe, NSE/NSE Indices, IMF BOP and IMF PIP.
- Official global EM flow panel extraction and region aggregation: UNKNOWN / NOT DONE.
- Daily synchronized market series panel: NOT DONE.
- Relative-attraction computation: NOT DONE.
- Sector-to-stock event bridge: NOT DONE.
- Rolling event study/backtest: NOT DONE.
- Production integration: NOT AUTHORIZED / 0%.

IMF extraction contract: `docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md` records the raw-observation schema, metadata-first dimension mapping, EM membership/aggregation gates, validation rules, and current UNKNOWN states. IMF BOP DSD V2.6.0 public registry source pinned; an independent Eurostat Vademecum cross-check documents the shared DSD component meanings, transaction-vs-position dimension, unit multiplier, observation/confidentiality flags, and BPM6 financial-account sign convention. Raw IMF XML parsing and IMF dataflow comparison remain pending. No guessed SDMX keys or synthetic EM totals are permitted.

Register revision: 2026-11-10; automated QA guards the distinction between broad Fed dollar index vs ICE DXY and IMF portfolio positions vs transactions.

QA alignment note: register wording is asserted verbatim by the overlay unit test.


## NSE DII source qualification addendum — 2026-11-12

The NSE FII/FPI & DII report page exposes two distinct Capital Market CSV views:
- NSE-only Capital Market Segment.
- Combined NSE+BSE+MSEI Capital Market Segment.

Keep the two source scopes separate. The combined series is the candidate for cross-exchange domestic institutional trading activity; NSE-only is an exchange-specific cross-check. Do not splice, average, or silently substitute one for the other.

NSE states that DII activity is based on trading codes entered by Trading Members and the corresponding client-category classification supplied by Trading Members. Treat this as exchange-reported trading activity, not a depository-confirmed DII holdings/flow series. The page's provisional caveat must be retained for the report snapshot; do not merge the exchange DII series with NSDL/CDSL FPI data.

The page text extraction does not expose the actual CSV hrefs; its generic extracted link resolves back to the landing page. A direct network attempt from the current execution environment failed DNS resolution before an HTTP response. Neither outcome proves that NSE's download control or endpoint is broken. The candidate path `/api/fiidiiTradeReact` was found in third-party scraper code only and is NOT an officially documented/verified NSE endpoint in this audit.

Detailed immutable-ingestion schema and acceptance checks: `docs/NSE_FII_DII_DAILY_ACTIVITY_INGESTION_CONTRACT_V1.md`.

Current state: official source page and series semantics VERIFIED; exact CSV URL UNKNOWN; raw bytes/hash NOT DONE; daily DII panel NOT DONE; matched DII/FPI panel NOT DONE; predictive validation NOT DONE; production use NOT AUTHORIZED. Do not use displayed sample rows or third-party mirrors as raw observations.


## IMF API catalogue re-check — 2026-11-17

A fresh check of the official IMF API documentation and IMF SDMX Central catalogue confirms:
- The current IMF Data API documentation advertises SDMX 2.1 and SDMX 3.0, while API exploration is directed through a beta-portal Swagger sign-in. Anonymous access to BOP_AGG observations was not demonstrated.
- The public IMF SDMX Central catalogue visibly lists multiple `IMF:BOP` data-structure versions, including `2.6.0`. This is a distinct country-level Balance of Payments structure, not proof that the annual `IMF.STA:BOP_AGG` aggregate dataset is published through that legacy service.
- The legacy SDMX Central service guide documents a public REST entry point, but the exact live dataflow and observation URLs could not be retrieved by the available inspection layer. Therefore do not promote the legacy endpoint from DOCUMENTED to VERIFIED for BOP_AGG or BOP observations.
- A country-level IMF:BOP transaction panel could be evaluated as a separate fallback for a medium-frequency EM portfolio-flow aggregate only after live dataflow + DSD + observation response are acquired, dimension/key mapping is proven, country membership and weights are declared, and missing reporters are handled. It must not be described as the BOP_AGG World/Group Aggregate dataset.
- Neither BOP nor BOP_AGG observations were acquired in this re-check. No EM portfolio flow value is admitted; no daily signal, relative-attraction calculation, or overlay gate advances.

Current status: IMF API documentation/catalogue route discovery PASS; BOP_AGG anonymous observation access NOT_DEMONSTRATED; legacy BOP dataflow/observations NOT_VERIFIED; raw bytes/hash/series mapping NOT_DONE.


## IMF observation access correction — 2026-11-17
- IMF SDMX Central Web Services Guide (May 2025) defines `/sdmx/v2/` as a public structure/metadata REST service. It separately points to `/ws/public/data` for FMR data-processing tasks (validation, conversion, registration), not for a proven BOP observation feed.
- Accordingly, no IMF BOP or BOP_AGG observation endpoint has been verified. The modern IMF Data Portal API link redirects to developer-portal sign-in. Catalogue/DSD discovery must not be mistaken for observation access.
- Exact BOP DSD 2.6.0 XML request was attempted via browser reader but remained inaccessible; no raw XML/hash acquired.
- Current status: structure route documented; DSD raw retrieval NOT_DONE; BOP/BOP_AGG observation access NOT_VERIFIED; no observations admitted.


## IMF current BOP dataset and historic pilot qualification — 2026-11-17
- Current IMF country-level BOP dataset is separate from annual BOP_AGG; official page exposes API/VIEW DATA/DOWNLOAD but API redirects to developer sign-in and no direct download URL/raw response was obtained. Current observations NOT_ACQUIRED.
- IMF SDMX Central shows provider-specific national BPM6 BOP dataflows/registrations. These are not a unified IMF global panel; any use requires provider-specific source validation and explicit country/coverage reconciliation.
- Historic IMF BOP pilot regional SDMX files explicitly last updated 2013-01-09. REJECTED_FOR_CURRENT_SIGNAL; format/reference only, not current flow evidence.
- No BOP/BOP_AGG observations admitted; no EM flow panel or overlay calculation advanced.


## Brazil BCB official monthly portfolio-flow pilot — 2026-11-17

A live official open-data API response was successfully retrieved through the Banco Central do Brasil Open Data Portal resource links. This is a country-level source pilot, not an IMF BOP_AGG observation and not a global EM aggregate.

Accepted source endpoints (JSON):
- Assets: https://api.bcb.gov.br/dados/serie/bcdata.sgs.22906/dados?formato=json — SGS 22906, “Portfolio investment - Net acquisition of financial assets - monthly - net”, monthly, USD million, coverage starts 1995-01. Official portal page documents the definition and resource endpoint.
- Liabilities: https://api.bcb.gov.br/dados/serie/bcdata.sgs.22924/dados?formato=json — SGS 22924, “Portfolio investment - Net incurrence of liabilities - monthly - net”, monthly, USD million, coverage starts 1995-01. Official portal page documents the definition and resource endpoint.
- Both live JSON responses were returned by the official API. Latest visible observation in each response: 2026-09-01. SGS 22906 value: 3,269.3 USD million; SGS 22924 value: -1,698.5 USD million. These are source-reported monthly series values, not independently reconciled totals.
- Separate series are retained. Do not add/subtract assets and liabilities or label a combined “net inflow” until BCB metadata and BPM6 sign convention for these exact series are verified. Do not substitute the distinct SGS 22905 “Portfolio investment - net” series without mapping and reconciliation.
- The data are monthly, published with up to four weeks' lag for the BCB/Dstat net series; they are strategic context, not daily trading triggers. BCB's IMF SDMX registration URL for BR1 is a registered metadata document; it is not the same as the SGS observation endpoint.

Integrity boundary:
- API JSON endpoint retrieval: PASS (official live response observed).
- Raw response file archived in repository: NOT_DONE.
- Raw byte count / retrieval timestamp / SHA-256: NOT_DONE (browser response was inspected, not downloaded as an immutable file).
- Full-history row count, missing marker scan, revision/vintage capture and exact end-date cross-check: NOT_DONE.
- Financial-account sign reconciliation and combined portfolio net-flow derivation: UNKNOWN / NOT_DONE.
- This pilot may be admitted only as a Brazil monthly source after raw archive + QA; it is not an EM aggregate and does not unlock the global EM portfolio-flow input.


## BCB 22905 cross-series comparability guard — 2026-11-17

Official BCB catalogue review adds a critical classification boundary:
- SGS 22905 is a separate monthly “Portfolio investment - net” dataset under BCB/Dstat, associated with the BOP6/BPM6 hierarchy. Its official catalogue describes assets and liabilities, USD millions, monthly observations, and publication timeliness up to four weeks after the reference period.
- SGS 22906 and 22924 are separately catalogued BCB/Depec series (Department of Economics), respectively net acquisition of financial assets and net incurrence of liabilities. Their individual dataset pages provide monthly coverage from 1995-01 and USD-million units.
- Similar labels do not prove identical calculation, sign convention, compilation vintage, or reconciliation. 22905 is a cross-series control candidate only; it must not be used as a plug, replacement, or arithmetic identity for 22906/22924 without BCB methodology reconciliation and overlapping-period numeric testing.
- The BCB portal's stated four-week timeliness for 22905 confirms this is a delayed monthly macro series, not a daily capital-flow signal. Use the actual publication timestamp/vintage if acquired; do not assign the observation date as its publication timestamp.
- Evidence: official BCB dataset pages for 22905, 22906, 22924 and the official topic taxonomy. The direct 22905 JSON endpoint did not render in this browser inspection, so its live observations remain NOT_ACQUIRED in this verification step.
