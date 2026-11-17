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


## Correction: BCB SGS 22905 catalogue ownership and resource verification — 2026-11-17

Correction to the immediately preceding 22905 comparability note: the official Open Data Portal page identifies SGS 22905 as organization BCB/Depec (Department of Economics), not BCB/Dstat. The official SGS 22906 page also identifies BCB/Depec; the 22924 catalogue entry likewise identifies BCB/Depec. Therefore the earlier statement that 22905 was a Dstat series distinct by organization from 22906/22924 is withdrawn. The prior claim that 22905 was in a separate BOP6/Dstat hierarchy is not supported by the official catalogue page and must not be used.

Verified catalogue facts for 22905: title “Portfolio investment - monthly - net”; source/author/maintainer Central Bank of Brazil / Department of Economics; monthly; unit million US dollars; temporal coverage from 1995-01-01. The portal's JSON resource link resolves to `https://api.bcb.gov.br/dados/serie/bcdata.sgs.22905/dados?formato=json` and the browser identifies `application/json`, but it did not expose the response rows in readable text. Therefore live observation values, latest period, raw archive, byte count and SHA-256 remain NOT_ACQUIRED / NOT_DONE in this verification.

22905 remains a third BCB/Depec series that may be compared against 22906 and 22924, but no algebraic identity, sign convention, or aggregation relation is inferred from titles. Reconcile BCB methodology and overlapping raw observations before calculating or replacing any series. Prior reported Sep-2026 22906/22924 figures remain historical claims from earlier response inspection and are not revalidated by this catalogue correction.

Official evidence: BCB 22905 dataset page (organization, definition, resources, coverage, frequency, unit); BCB 22906 dataset page (same organization, coverage, frequency, unit); BCB 22924 dataset catalogue (same organization and unit/frequency/coverage).


## Critical dual-catalogue conflict for SGS 22905 — 2026-11-17

A second official BCB portal instance was inspected and reveals an unresolved catalogue conflict for the same SGS code 22905:
- `opendata.bcb.gov.br` page title “Portfolio investment - monthly - net” classifies it as BCB/Depec, with metadata updated 2026-03-26; it links the JSON resource for SGS 22905.
- `dadosabertos.bcb.gov.br` page title “Investimentos em carteira - líquido” classifies it as BCB/Dstat, explicitly places it under Balanço de Pagamentos - BPM6 / Conta financeira / Investimentos em carteira, reports timeliness up to four weeks, and metadata updated 2026-09-08; it also links a JSON resource for SGS 22905.
- Both pages identify monthly frequency, USD million, and start date 1995-01. Both resource links refer to the same SGS code family. This is not safely resolvable from catalogue text alone. Do not assert that 22905 is definitively Depec or Dstat, do not assume the pages describe distinct numerical series, and do not merge or select either taxonomy as authoritative until the exact resource URLs, live payloads, series metadata and publication vintages are compared.
- The latest metadata date on the Dstat page is later, but recency alone does not prove ownership or supersession. Treat classification as CONFLICT / UNKNOWN.
- Next validation: resolve each portal's JSON resource link and capture final URL, HTTP status, content type, response bytes, retrieval timestamp and SHA-256; compare payload values/date keys and SGS series metadata. If payloads are byte/value-identical, treat as duplicate catalogue records and preserve both provenance records. If payloads differ, quarantine both until BCB methodology clarifies the canonical series.
- Evidence: official BCB portal pages `opendata.bcb.gov.br` SGS 22905 and `dadosabertos.bcb.gov.br` SGS 22905. Both catalogues are official but disagree on organization and classification.
- Current decision: SGS 22905 excluded from any calculation; SGS 22906 and 22924 remain separate Depec series pending their own raw archive and reconciliation. No net-flow identity inferred.


## BCB SGS 22905 dual-catalogue resource comparison — 2026-11-17 (follow-up)

The JSON resource links on both official catalogue instances were followed directly:
- `dadosabertos.bcb.gov.br` resource link resolves to `https://api.bcb.gov.br/dados/serie/bcdata.sgs.22905/dados?formato=json` and the browser returned a readable JSON response (application/json).
- `opendata.bcb.gov.br` resource link resolves to the exact same URL. The browser identifies the same API host/path/query and application/json resource; the second click did not render a separate body excerpt.
- Therefore the two catalogue records do not point to distinct resource URLs in this check. The earlier hypothesis that they may deliver different payloads is not supported by the resolved URLs. Because the final endpoint is identical, the canonical SGS API route is common to both catalogue records.
- The official JSON response visible from the first resource begins at 1995-01-01 and includes monthly observations through 2026-09-01 in the returned browser excerpt. This is a browser-inspected response, not an immutable raw archive; byte count, retrieval timestamp, full response length and SHA-256 remain NOT_DONE.
- CSV resource links on both pages resolve to `https://api.bcb.gov.br/dados/serie/bcdata.sgs.22905/dados?formato=csv`; the browser could not parse the `text/csv` response (HTTP/content-type reader limitation). This is not evidence of a BCB API failure.
- Remaining conflict: the catalogue metadata records still disagree on organization (Depec vs Dstat), description/title language, classification hierarchy and metadata update date. The shared JSON endpoint establishes resource identity, not which catalogue metadata record is authoritative or whether the series methodology changed. Preserve both provenance records; classification remains CONFLICT / UNKNOWN pending BCB methodology/version metadata reconciliation.
- Do not infer any arithmetic identity or sign mapping between SGS 22905 and 22906/22924. No values admitted to global EM aggregate or relative-attraction calculations.

Integrity status: same JSON endpoint across both portals = VERIFIED; visible JSON response = INSPECTED; raw archive + SHA-256 = NOT_DONE; CSV body comparison = NOT_DONE; metadata authority/methodology reconciliation = UNKNOWN; production impact = NONE.



## BCB live observation cross-check — SGS 22905 and 22906 — 2026-11-17

Direct official API JSON inspection in this verification:
- SGS 22905, 2026-09-01: +4,967.8 million USD.
- SGS 22906, 2026-09-01: +3,269.3 million USD.
- Difference 22905 minus 22906 = +1,698.5 million USD.
- A prior inspection recorded SGS 22924 for 2026-09-01 as -1,698.5 million USD; that 22924 value was not independently re-fetched successfully in this turn. The numerical magnitude therefore matches the prior 22924 observation, but this is a single-vintage candidate relationship, NOT a verified algebraic identity or sign convention.
- Do not calculate, net, combine, or admit these series into an overlay flow feature until 22924 is freshly fetched and the BCB methodology, signs, scope and historical overlap are reconciled over the full common sample.
- Important correction: 22905 latest visible value is 4,967.8 (not the earlier Sep-2026 value 4,967.8 was previously absent; previous checkpoint had no acquired value). The 22906 latest visible value is 3,269.3, independently matching the earlier inspected value.
- Official API JSON endpoints: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.22905/dados?formato=json` and `https://api.bcb.gov.br/dados/serie/bcdata.sgs.22906/dados?formato=json`. Source evidence: BCB Open Data Portal SGS 22905 catalogue and both official API JSON responses.

Integrity boundary unchanged: browser response inspection only; no immutable raw bytes, extraction timestamp file, byte count, SHA-256, full-history structural QA, vintage archive or methodology reconciliation. The values are not admitted to the overlay. Metadata owner/classification conflict for 22905 remains CONFLICT / UNKNOWN.



## BCB portfolio-liability component discovery — SGS 22924/22925/22926 — 2026-11-17

Further official BCB catalogue inspection identifies three distinct monthly USD-million series, each beginning 1995-01 and maintained by BCB/Depec:
- SGS 22924: “Portfolio investment - Net incurrence of liabilities - monthly - net”.
- SGS 22925: “Portfolio investment - Net incurrence of liabilities - monthly - inflows”.
- SGS 22926: “Portfolio investment - Net incurrence of liabilities - monthly - outflows”.
The official 22924 catalogue describes portfolio investment liabilities as transactions/positions in equity and investment-fund shares and debt securities; it links the BCB SGS JSON and CSV resources. The 22925 and 22926 catalogue pages confirm separate inflow and outflow series. Their existence provides a better methodology cross-check path, but titles alone do not establish whether 22924 equals inflows minus outflows, the sign orientation, gross/net adjustments, revisions or common observation coverage.

Direct API open for SGS 22924 was inaccessible to the browser reader in this verification (tool-level inaccessible URL). This is not evidence that the BCB endpoint is down. No fresh 22924 value or raw payload was acquired. Therefore the earlier Sep-2026 -1,698.5 value remains a prior browser observation, not freshly revalidated in this turn.

BCB official External Sector Statistics release for September 2026 (published 26-Oct-2026) reports domestic-market portfolio investment liabilities net outflows of USD 2.1bn; equity/fund outflows USD 1.7bn and debt-security outflows USD 0.4bn; 12-month net inflows USD 5.1bn. This is a separate aggregate/statistical publication and is not assumed equivalent to SGS 22924 without scope and period reconciliation.

Integrity decision: 22924 live API refresh = NOT_ACQUIRED in this turn; 22925/22926 catalogue discovery = PASS; component formula = UNKNOWN; external publication cross-check = contextual only; no data admitted to overlay. Preserve separate series and do not derive a net-flow feature until raw common-period QA and BCB methodology establish the formula.



## Brazil–India portfolio flow context: official source references — 2026-11-17

- BCB, External Sector Statistics, September 2026, press release 26-Oct-2026: domestic-market portfolio investment net outflow USD 2.1bn (equity/funds -USD 1.7bn; debt securities -USD 0.4bn); trailing 12-month net inflow USD 5.1bn. Official page: `https://www.bcb.gov.br/estatisticas/estatisticassetorexterno?mode=light`; official PDF: `https://www.bcb.gov.br/content/statistics/externalsectorstatistics_prev/202610_External_sector_statistics_text.pdf`.
- RBI, Developments in India's Balance of Payments for September 2026, press release 13-Nov-2026: net FPI -USD 6.7bn, FPI in India -USD 6.5bn; Apr-Sep cumulative net FPI -USD 8.9bn. Official page: `https://www.rbi.org.in/scripts/bs_pressreleasedisplay.aspx/BS_PressReleaseDisplay.aspx?prid=63974`.
- RBI official commentary on global risk-off / EM portfolio flow selling since September cites West Asia tensions, elevated crude and rising global bond yields; Indian equities bearish Sep-Oct through 19-Oct with DII net buying offsetting part of FII selling. Official RBI Bulletin source: `https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24516`.
- Scope: Brazil monthly country-specific portfolio liabilities are contextual cross-country evidence only; they are not a synchronized global flow panel or direct India FPI observation. Do not compare raw USD magnitudes as impact weights without harmonized definitions and denominators.
