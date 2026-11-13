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


## IMF BOP observation-access requalification — 2026-11-13
The DSD metadata file and its schema-validation evidence are already archived; this is not an outstanding DSD download task. The remaining blocker is dissemination linkage and observation access:
- IMF:BOP DSD 2.6.0 structure file SHA-256: 4f5102b4a36a93fa1d60c7dc29fdfcbfa4296e3b1e42325c413fc8daeca64771; schema-validation manifest records 18 dimensions, 15 attributes, 22 embedded codelists and SDMX-ML 2.1 validation PASS.
- IMF SDMX Central registers IMF:BOP6(1.0) for provider IMF:IMF, but its registered URL is a sample compact XML file (last updated 2023-09-22); this does not establish an IMF global observation feed or a link to BOP DSD 2.6.0.
- Official constraints distinguish BOP6[1.0] from BOP_BPM6[1.0]; ESTAT:BPM6_BOP_Q/M are different ESTAT dataflows. Do not substitute them.
- Exact BOP6-to-DSD structure probe was blocked before an HTTP response; no endpoint failure is inferred. IMF Data API documentation confirms SDMX 2.1/3.0 but its Swagger explorer requires beta-portal sign-in.
- India BOP observation rows accepted: 0. Global EM flow extraction and aggregation: NOT DONE. em_portfolio_flow_usd_bn remains UNKNOWN. No guessed key, sample payload, positions series or third-party source is promoted.

Official references: https://sdmxcentral.imf.org/data/overview.html ; https://sdmxcentral.imf.org/data/registrations.html ; https://sdmxcentral.imf.org/data/constraints.html ; https://data.imf.org/en/Resource-Pages/IMF-API . Detailed checkpoint: docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md.


## IMF BOP/IIP World and Country-Group Aggregates qualification — 2026-11-13
A separate official IMF dataset was identified: `IMF.STA:BOP_AGG`, titled “Balance of Payments and International Investment Position Statistics (BOP/IIP), World and Country Group Aggregates” (historically BOPSY). Official dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG . It is an annual November publication under BPM6. IMF states that country-group aggregates (other than Euro Area) combine reported country data with estimates for nonreporting economies, drawing on sources including WEO and External Wealth of Nations; country-level data are reported to IMF or obtained from National Summary Data Pages, with certain IMF-account transactions replaced from Fund Accounts.

**Research-use decision:** register this as a distinct official annual aggregate benchmark candidate, NOT as the missing IMF.STA:BOP country-level transaction panel and NOT as a daily/weekly trading trigger. Estimated nonreporter coverage and group construction must be retained as dataset semantics. Do not use BOP_AGG to backfill missing country observations, infer daily flows, or claim a clean observed-only EM flow sum. Its annual frequency makes it unsuitable for 1–5 trading-day signal timing; it may only support low-frequency macro regime/context after vintage, table, series definition, and download provenance are independently verified.

Current evidence boundary: public dataset page confirms title, annual frequency, November release cadence, BPM6 basis, and estimation caveat. No BOP_AGG table or observation file has yet been downloaded, checksum-verified, or reconciled. Thus source identification = VERIFIED; raw data acquisition = NOT DONE; specific EM group series coverage = UNKNOWN; production use = NOT AUTHORIZED. IMF API link routes to a sign-in page in this inspection; no anonymous observation endpoint is claimed.

Official source references: https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG ; https://data.imf.org/en/Resource-Pages/IMF-API .


## BOP_AGG methodology and reporting-vintage gate — 2026-11-13
The official IMF November 2025 BOPSY Explanatory Notes were inspected directly (31-page PDF). They add material details that must be retained in any later BOP_AGG use:

1. **Nonreporter estimates are part of the published group aggregate.** For financial-account transaction gaps, IMF says WEO data are used. For other BOP components, its documented procedures include WEO gross/net substitutions and carry-forward adjustments. Therefore the aggregate is not an observed-only sum of country-reported flows. Do not interpret a BOP_AGG group value as a clean real-time foreign portfolio flow observation.
2. **Global discrepancies are explicit quality diagnostics.** The notes explain that global financial-account discrepancies compare net acquisition of financial assets with net incurrence of liabilities. Preserve this diagnostic separately; do not force assets and liabilities to balance or silently net away the discrepancy.
3. **Group membership is vintage-defined.** The November 2025 notes list Emerging and Developing Economies by regional group (Emerging and Developing Asia, Europe, Middle East and Central Asia, and Sub-Saharan Africa). Do not import a current WEO/MSCI/World Bank classification or treat the membership as invariant across vintages. If a country-level aggregate is ever independently reconstructed, store the exact membership list and edition.
4. **Country reporting coverage is heterogeneous.** In the November 2025 reporting overview, India’s last reported BOP period is 2024 and IIP period is 2024. This is annual macro coverage, not a timely 2026 daily/weekly flow input. Country-level reported data may be combined with group-level estimates; maintain a reported-vs-estimated flag only where the source actually exposes one. Do not infer a per-country estimate flag from the aggregate total.
5. **Frequency/timing gate:** BOP_AGG is annual and released each November. It is context-only for long-horizon regime description and cannot serve as a 1–5 trading-day trigger or point-in-time daily overlay.

Official evidence: IMF BOPSY Explanatory Notes, November 2025, sections 1, 2 and 3, especially PDF pages 3–5 and 11–13: https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf . IMF dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG .

**Current acceptance:** methodology inspection = PASS; raw BOP_AGG workbook/table bytes, publication vintage, retrieval timestamp and SHA-256 = NOT ACQUIRED; machine-readable EMDE membership artifact = NOT CREATED; observed-only EMDE flow reconstruction = NOT AUTHORIZED; daily trigger suitability = FAIL. No value or observation was fabricated or downloaded in this checkpoint.


## BOP_AGG 2026 publication-vintage and download-route checkpoint — 2026-11-13
This checkpoint resolves the publication-timing and access status without inventing a data download.

### Official page inspection
- IMF BOP_AGG dataset page identifies the dataset as annual, released each November, BPM6-based; its current latest-update listing links the BOPSY Dashboard and November 2025 Explanatory Notes. The linked dashboard page itself reports publication date 19 November 2025.
- As at 13 November 2026, the official dashboard page inspected still identifies 19 November 2025 as its publication date. No 2026 dashboard/release date or 2026 BOP_AGG vintage is exposed by the inspected official pages. This is **2026 vintage NOT VERIFIED**, not proof that no unpublished or separately posted release exists. Do not label the November 2025 vintage as 2026.
- The dataset page exposes an API link, but the linked API portal redirects to a sign-in page. The dataset page's visible VIEW DATA / DOWNLOAD controls do not expose a direct static workbook URL in the text response. The 2025 explanatory notes say users can customize and download tables, naming Global Discrepancies, Summary of International Transactions and Positions, World and Regional Tables—USD, and World and Regional Tables—Percent of GDP. No actual workbook/table bytes were retrieved in this checkpoint.
- The November 2025 notes list India's latest reported BOP period as 2024 and IIP period as 2024. This is a clear reporting-lag constraint for India and must be retained separately from the release publication year.

### Acceptance and handling
- Official dataset identity and annual cadence: VERIFIED.
- 19-Nov-2025 dashboard publication vintage: VERIFIED.
- 2026 release vintage as of 13-Nov-2026: NOT VERIFIED / PENDING.
- Public anonymous API download route: NOT VERIFIED (API portal sign-in redirect).
- Static downloadable BOP_AGG raw workbook/table, exact URL, retrieval timestamp, HTTP headers, byte count and SHA-256: NOT ACQUIRED.
- India latest reporting year in Nov-2025 overview: BOP 2024; IIP 2024.
- No BOP_AGG observation rows or aggregate values are imported from third-party mirrors. Do not use search-engine snippets, DBnomics, Subsets, or other redistributors as official raw evidence.
- Next permitted acquisition path: use the official IMF dashboard/table download UI if a direct downloadable file can be obtained without account/API restrictions; capture the exact generated URL, final URL, UTC retrieval time, headers, raw bytes and SHA-256. If it requires sign-in, stop and retain NOT ACQUIRED; do not bypass access controls or use a mirror.

Official references: https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG ; https://data.imf.org/en/dashboards/bopsy%20dashboard ; https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf .


## IMF WEO October 2026 country-group portfolio-flow candidate — qualification only (2026-11-13)
Official IMF WEO page identifies an October 2026 vintage and exposes an official Excel dataset with three sheets: Countries, Country Groups, Commodity Prices. The page says data/projections are available from 1980 to present, with projections for most series for five years. Direct Excel target exposed by the official page: `https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx`. The web document viewer returned an unsupported XLSX content-type and the direct file transfer attempt did not retrieve bytes in this run. Therefore exact workbook bytes, retrieval timestamp, size and SHA-256 remain NOT ACQUIRED.

The official October 2026 WEO Database Appendix (31 pages) supplies strong qualification metadata:
- Estimates/projections are based on statistical information available through 30 September 2026 (Appendix pp.1–2); this is a cutoff, not a promise that each series is updated to that date.
- Historical results vs IMF staff projections are distinguished by shading in the workbook (p.3); do not merge projection values with actual outturns.
- For some economies, 2025 and earlier can still be estimates rather than actual outturns; latest actual outturns are documented in country-information notes (p.3). Thus year alone cannot classify an observation as actual.
- Country-group composites are normally computed only when at least 90% of group weights are represented (p.3 and p.9). Missingness/coverage metadata is therefore a hard gate; a group aggregate must not be assumed complete.
- External-sector composites are sums of individual country data converted to USD at average market exchange rates for the relevant years (p.9). This differs from WEO domestic aggregates and must be preserved in series metadata.
- WEO October 2026 EMDE classification and regional membership are vintage-specific; Appendix lists Emerging and Developing Economies and regional groups, including Emerging and Developing Asia (pp.6–8). Do not borrow BOPSY group membership or a current external classification.
- WEO methodology documents BPM6 net portfolio investment and other net financial account series at group level as available (historical methodology note, p.24), but exact October 2026 workbook series code, unit, coverage, country group rows, actual/projection flags and value semantics have NOT been verified because the workbook bytes were not acquired.

Decision: register WEO October 2026 as a **separate candidate macro context source**, not a BOP_AGG replacement and not an observed-only flow source. It is annual and may include staff estimates/projections; it cannot trigger 1–5 day trades. No WEO value is ingested or used. Acceptance remains metadata qualification PASS; workbook/raw data and exact portfolio series mapping PENDING; point-in-time trading use NOT AUTHORIZED.

Official references: https://data.imf.org/Datasets/WEO ; https://data.imf.org/-/media/iData/External-Storage/Documents/C4182C5C54794FC48892DE8F6C74FF82/en/October-2026-WEO-Database-Appendix.pdf .


## WEO country-group actual-vs-projection metadata correction and acquisition result — 2026-11-13
A stricter read of the official WEO FAQ (last updated October 2026) changes the acceptance boundary from the preliminary appendix-only qualification above:
- For individual country-series, the portal's `Latest Actual Annual Data` metadata distinguishes latest actual from later IMF staff estimates; full-dataset CSV includes this field.
- **IMF explicitly says it does NOT provide this actual/projection metadata for WEO country-group data.** At country-group level, the publication year is assumed to be the start of the forecast period. Consequently, the previous note suggesting workbook shading alone could identify group-level actual/projection values is not an acceptable classification method. Country-group values must be treated as NOT_POINT_IN_TIME_VERIFIED for actual-vs-estimate status unless an official series-specific metadata field explicitly says otherwise. Do not infer actuals from year, report shading, or country-level metadata.
- WEO online database is annual only; IMF states it does not publish monthly or quarterly data there. Historical series can contain IMF staff estimates as proxies when complete information is unavailable; WEO and IFS can differ.
- WEO country group compositions are recalculated through time using the publication's current group membership (the FAQ gives EU/euro area as examples and says the same concept applies to other WEO groups). Do not interpret the historical group series as a fixed-membership constant panel; preserve each vintage's membership and the IMF's restatement convention.
- The official IMF Excel URL was attempted directly from the IMF-hosted URL in this run; transfer failed before any file bytes were obtained. No HTTP response/header, file size, retrieval timestamp or SHA-256 can be asserted. An unrelated third-party package/repository checksum is not a substitute for a local copy and is not adopted.

Revised decision: October 2026 WEO country-group series is unsuitable as an observed-only EM portfolio-flow series and cannot be used as a point-in-time flow trigger. It remains at most a low-frequency published-vintage macro context series, with group-level actual-vs-estimate state UNKNOWN. Do not infer net portfolio investment series availability or semantics until the official workbook is locally acquired and parsed. This correction supersedes any contrary implication in the immediately preceding WEO qualification addendum.

Official evidence: IMF WEO FAQ, October 2026, especially questions “How do I know if data are actual, preliminary, or projected?”, “Do you have higher frequency data?”, “What explains differences between WEO and IFS?”, and country group composition; https://data.imf.org/Datasets/WEO/Frequently-Asked-Questions . IMF WEO dataset page: https://data.imf.org/Datasets/WEO .


## NSE FII/FPI–DII official report page live semantics and download-control audit — 2026-11-13
A fresh inspection of the official NSE FII/DII page confirms two distinct downloadable CSV controls: (1) NSE-only Capital Market Segment and (2) combined NSE+BSE+MSEI Capital Market Segment. The page also renders sample/current table rows, but the browser text extraction exposes only the generic download-control link and does not reveal either CSV's actual href, final URL, or bytes. A click on the generic link resolves back to the same page, so it is not a verified file URL. Exact CSV URL remains UNKNOWN; do not infer it from the page route or from a third-party scraper.

The official page's own definitions and caveats are explicit: both series are collated from trades executed by FIIs/FPIs and DIIs; FII/FPI data are based on PANs provided by NSDL; the page data are provisional and may change due to custodial confirmation/modifications; expiry-day physical-settlement obligations may be included. DII classification uses trading codes entered by Trading Members and the client-category classification they supply via unique-client-code upload. Therefore this NSE DII series is provisional exchange-reported trading activity, not depository-confirmed DII holdings/flows. NSE directs users to NSDL/CDSL for final FPI data. Keep NSE-only and combined exchange scopes separate and do not treat either provisional FPI field as final custodian data.

Visible sample snapshot in the official page inspection: NSE-only table dated 09-Oct-2026; combined table dated 30-Oct-2026. These are page-rendered sample rows only, not a complete archive or acquired CSV, and are NOT ingested as raw observations. No retrieval timestamp, byte count, raw file or SHA-256 created.

Acceptance: official page + series semantics + provisional caveats VERIFIED; separate download controls VERIFIED; exact CSV hrefs/raw bytes/hash UNKNOWN/NOT ACQUIRED; historical daily panel NOT DONE; final FPI reconciliation NOT DONE; predictive validation NOT DONE; production use NOT AUTHORIZED.

Official source: https://www.nseindia.com/reports/fii-dii .


## CDSL custodian-confirmed FPI daily flow qualification — 2026-11-13
Official CDSL eServices daily page `https://www.cdslindia.com/eservices/publications/fiidaily` is accessible and displays a reporting-date table by asset bucket and route. At the time of inspection, the page showed reporting date 12-NOV-2026. CDSL states these data are compiled from reports submitted to depositories by custodians on the reporting date and represent trades conducted on and up to the previous trading day(s). This is materially distinct from NSE's same-day provisional trading-member compilation. Treat `reporting_date` as publication/reporting date, not automatically as trade/as-of date; exact underlying trade-date coverage remains a lagged window until the custodian report's underlying period is documented.

The daily table separates Equity, Debt-General Limit, Debt-VRR, Debt-FAR, Hybrid, Mutual Funds and AIFs, and separates Stock Exchange from Primary market & others where applicable. For an equity FPI flow factor, use only the Equity subtotal after verifying category/route semantics; do not use grand Total as equity or as FPI-only because it includes other asset buckets, Mutual Funds and AIFs. `Primary market & others` includes multiple non-secondary-market events (rights, preferential allotments, bonus, redemptions, buybacks, corporate actions, etc.); retain it separately from Stock Exchange secondary-market trades. Hybrid includes REITs and InvITs.

CDSL uses the RBI reference exchange rate prevailing on the trading day for USD conversion, or the immediately preceding working-day rate when trading day is a bank holiday. Preserve original INR crore values as primary; do not recompute USD using another FX series. Aggregate discrepancies may be rounding. The report also has a separate FPI derivatives table compiled from reports submitted by NSE/BSE/MSEI/NCDEX/MCX and refers to previous trading-day trading/positions; do not mix derivative notional/open interest with cash equity flows.

The official CDSL page's explanatory note explicitly distinguishes exchange provisional data (trading-member reports on T day) from confirmed FPI trades compiled from custodian reports to depositories. This supports using CDSL custodian-confirmed data as a separate, higher-provenance validation/reference series, but not as a zero-lag signal. CDSL page provides public daily report view; direct raw-file export URL/bytes, retrieval timestamp, file size and SHA-256 were not acquired in this checkpoint. The page values are a live display snapshot only and are not ingested into the panel.

At inspection the page displayed a reporting-date 12-NOV-2026 Equity table with separate Stock Exchange and Primary market & others rows and a subtotal. Numeric display values are deliberately not persisted in this source register, avoiding confusion between route-level net and category subtotal. The live display is NOT imported as a historical observation or trading signal. Reporting-date-to-trade-date mapping and vintage archive acquisition remain pending.

CDSL monthly calendar page separately states its monthly net investment data are based on SEBI/depository reports submitted by DDPs/custodians and trades up to previous trading day(s); do not mix monthly aggregates with daily rows without overlap/deduplication rules. NSDL's current search-indexed portal listing includes Latest, Current Month and Archive navigation, but its listing page says website updated 05-Oct-2020 and contains an FPI disclaimer restricting reproduction/redistribution; therefore do not scrape or redistribute NSDL data unless terms and current status are independently resolved. CDSL is the preferred public reference route for this checkpoint.

Acceptance: CDSL official daily source and semantics VERIFIED; reporting-date/previous-trade-day lag gate VERIFIED; asset-bucket/route split VERIFIED; direct raw file and checksum NOT ACQUIRED; exact trade-date mapping UNKNOWN; no daily signal or production use authorized.

Official references: https://www.cdslindia.com/eservices/publications/fiidaily ; https://www.cdslindia.com/eservices/Publications/FIICalendar ; https://pilot.fpi.nsdl.co.in/Reports/ReportsListing.aspx .


## CDSL daily report arithmetic reconciliation — live display snapshot 12-NOV-2026 (2026-11-13 audit)
A point-in-time read of the official CDSL daily page on 13-Nov-2026 displayed reporting date 12-NOV-2026. This is a live-page QA snapshot only, not a downloaded immutable raw file and not a backfilled observation. Independently recalculated the published component subtotals against the grand total:
- Equity subtotal: INR +14,693.72 crore (Stock Exchange +14,678.72; Primary market & others +15.00).
- Debt-General: +445.65; Debt-VRR: -173.22; Debt-FAR: +1,022.81; Hybrid: +34.86; Mutual Funds: +9.59; AIFs: -5.20 (all INR crore).
- Sum of asset-bucket subtotals = INR +16,028.21 crore, matching published Total +16,028.21.
- Sum of gross purchases across asset buckets = INR 36,138.01 crore, matching published gross purchases; gross sales sum = INR 20,109.80 crore, matching published gross sales.
- Sum of USD net figures across displayed buckets = USD 1,708.6278 million, rounding to published USD 1,708.628 million.
- Arithmetic reconciliation PASS within published precision. This validates internal arithmetic only; it does not validate trade-date mapping, custodian completeness, raw-file immutability, or predictive value.
- Keep equity cash flow as Equity subtotal only; never use grand total as equity. The reporting-date lag note on the page remains applicable: custodians report on reporting date, covering trades on/up to previous trading day(s).
- The live page currently has a 12-NOV-2026 report. No raw file bytes or checksum acquired; do not ingest this displayed snapshot into historical panel.

Official source: https://www.cdslindia.com/eservices/publications/fiidaily . Snapshot evidence: page reporting date and bucket rows; published rounding note says aggregate discrepancies may be due to rounding.


## 18. CDSL historical Daily Trends archive route and coverage boundary — 2026-11-13

- Re-inspected the official archive landing page: https://www.cdslindia.com/Publications/ForeignPortInvestor.html . Its page metadata says last updated 05-Nov-2026. The **Daily Trends in FII/FPI Investments (New Format)** archive exposes dated report links from 02-Sep-2024 through 04-Apr-2025; the newest listed daily file is 04-Apr-2025. This archive coverage is not continuous to the current live daily page.
- Followed the official 04-Apr-2025 archive item. The resolved official file target is `https://www.cdslindia.com/downloads/Publications/Latest/latest_04042025.xls`. The browser retrieval refused the XLS response as unsupported content type (HTTP-like 400 in the retrieval wrapper); an independent direct file-transfer attempt also failed before bytes were obtained. Therefore the URL is confirmed from the official archive link, but **raw XLS bytes were NOT ACQUIRED**; byte count, HTTP headers, retrieval timestamp, file hash, workbook sheet/schema and report contents remain UNKNOWN.
- The official current daily page remains a separate live view (observed search snapshot dated 11-NOV-2026). It does not prove that the archive is populated for dates after 04-Apr-2025. Do not backfill the gap using live page snapshots, search snippets, monthly/fortnightly/quarterly totals or inferred filenames.
- Archive list dates are report labels, not independently verified underlying trade dates. CDSL daily semantics remain: custodian reports submitted on reporting date represent trades on and up to previous trading day(s); exact trade-date mapping remains UNKNOWN until a raw report and its internal metadata/notes are inspected.
- Acceptance: official archive page + one exact dated XLS link + visible archive coverage boundary = VERIFIED. Raw bytes/SHA-256 = NOT ACQUIRED. Historical daily coverage after 04-Apr-2025 = NOT VERIFIED. Exact trade-date mapping = UNKNOWN. No data rows ingested; no production use.
- Next permitted path: obtain the official XLS through an accessible browser/download session or user-provided original file, then hash and inspect it before any ingestion. If the binary remains inaccessible, stop; do not use mirrors or fabricate an export.

Official references: https://www.cdslindia.com/Publications/ForeignPortInvestor.html ; https://www.cdslindia.com/eservices/publications/fiidaily ; https://www.cdslindia.com/downloads/Publications/Latest/latest_04042025.xls .


## 19. CDSL fortnightly sector-wise FPI report — frequency and measurement qualification (2026-11-13)

- Official archive page lists fortnightly sector-wise reports through 31-Oct-2026, while the New Format Daily Trends archive list ends 04-Apr-2025. These are distinct products and frequencies; fortnightly availability does not establish daily archive continuity.
- Opened official 31-Oct-2026 report: https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Oct%2031%202026.html . Report columns explicitly distinguish AUC as of 15-Oct-2026, net investment for 01–15 Oct, net investment for 16–31 Oct, and AUC as of 31-Oct-2026. It is a fortnightly sector aggregate and AUC is a stock/position, not transaction flow.
- The report provides 23 named sector rows plus Others and a Grand Total. Sector taxonomy is the BSE common industry classification adopted by NSE/BSE from 30-Apr-2022; issuers outside the approximately 4,800 classified issuers are placed in Others. Do not equate these sectors to NSE sector indices, NIFTY industry indices, or individual issuer flows without an explicit mapping.
- Measurement/vintage change: report notes Debt-VRR net investment and AUC included from 30-Apr-2020; Debt-FAR, Mutual Funds and AIF AUC from 31-Aug-2024; their net investment from 15-Sep-2024. Historical comparisons before these dates have differing category coverage.
- INR-to-USD conversion is based on daily RBI reference rates for daily CDSL trends, but this fortnightly report uses the end-of-period RBI reference rate for the fortnightly net-investment values and AUC. Preserve INR crore as primary; do not compare its USD values directly with daily conversions without rate-basis normalization.
- Monthly calendar page opened at https://www.cdslindia.com/eservices/Publications/FIICalendar shows monthly net investments by Equity, Debt-General, Debt-VRR, Debt-FAR, Hybrid, Mutual Funds and AIF, and says custodian/DDP reports reflect trades on and up to previous trading day(s). Its page footer still states “last updated May 20, 2020” while live extracted data are shown for calendar 2026; treat footer as page metadata, not the dataset's observation vintage. No raw monthly export/bytes or exact downloadable URL was obtained in this checkpoint.
- Research-use decision: fortnightly sector report is a candidate for low-frequency sector-allocation/rotation context and sector bridge research only. It is NOT a daily/1–5 day trigger, not an issuer-level net-flow table, and not a substitute for daily FPI equity flow. AUC must remain a separate stock measure from fortnightly net investment flow.
- Acceptance: official report route, latest listed report date, table frequency/period columns, sector classification, category start-date caveats and USD conversion basis = VERIFIED. Raw report file bytes/SHA-256 = NOT ACQUIRED; machine-readable extraction = NOT DONE; sector-to-stock bridge = UNKNOWN; predictive validation = NOT DONE; production use = NOT AUTHORIZED.

Official references: https://www.cdslindia.com/Publications/ForeignPortInvestor.html ; https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Oct%2031%202026.html ; https://www.cdslindia.com/eservices/Publications/FIICalendar .


## 20. BSE industry-classification hierarchy qualification for CDSL fortnightly sector bridge — 2026-11-13

- Inspected BSE's official Industry Classification Structure PDF: https://www.bseindia.com/Downloads1/India_Industry_Classification_Structure.pdf . The published table defines a hierarchy with MEI_CODE / Macro Economic Indicator, SECT_CODE / Sector, IND_CODE / Industry, BASIC_IND_CODE / Basic Industry, and textual definitions. Example codes distinguish sector/industry/basic-industry levels; this is a taxonomy dictionary, not by itself a dated issuer-to-code membership file.
- The BSE legacy Industry_Classification.aspx landing URL returned HTTP 403 to the public page retrieval used in this audit. This is an access limitation, not proof that BSE has no other issuer membership data. No official issuer-level membership export, dated security identifier mapping, effective dates, or NSE/BSE security master join was acquired in this checkpoint.
- CDSL's 31-Oct-2026 fortnightly HTML report is directly rendered as a sector aggregate table (23 named sectors plus Others); inspected page has no separate raw downloadable file link in the retrieved page content: https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Oct%2031%202026.html . HTML page route is confirmed, but no downloadable binary/raw export bytes or SHA-256 acquired.
- Critical distinction: BSE hierarchy definitions can support a future taxonomy crosswalk design, but cannot assign any listed issuer to a sector without official, date-effective issuer membership. Similar-looking names are not a verified mapping. CDSL "Others" cannot be redistributed to named sectors or stocks.
- Acceptance: official BSE hierarchy dictionary and its field/code structure = VERIFIED; issuer membership file + effective dates = NOT ACQUIRED; CDSL raw binary export = NOT EXPOSED/NOT ACQUIRED in inspected page; sector-to-issuer bridge = UNKNOWN; CDSL-to-BSE taxonomy crosswalk = PARTIAL/NOT VALIDATED; NSE security mapping = UNKNOWN. No synthetic mapping, no inferred company assignments, no data ingestion, no predictive use, no production authorization.
- Next permitted path: seek an official dated BSE issuer classification/membership file and a matching official NSE security master; require stable identifiers and effective dates before constructing a bridge. If unavailable, preserve UNKNOWN and do not map.

Official references: https://www.bseindia.com/Downloads1/India_Industry_Classification_Structure.pdf ; https://www.bseindia.com/static/about/Industry_Classification.aspx ; https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Oct%2031%202026.html .


## 21. NSE Indices issuer-classification source and bulk-membership gap — 2026-11-13

- Located and opened NSE's official Industry Classification page: https://www.nseindia.com/static/products-services/industry-classification . It describes the four-level Macro-Economic Sector / Sector / Industry / Basic Industry taxonomy, currently described as 12 macro-economic sectors, 22 sectors, 59 industries and 197 basic industries. NSE Indices says assignment is based primarily on audited consolidated annual revenue; single-business issuers use that business, multi-segment issuers use the >50% revenue segment where applicable, otherwise diversified rules apply. It states all listed-company classifications are reviewed annually after annual reports and may also change after significant corporate events.
- The official BSE-hosted common taxonomy PDF remains a hierarchy dictionary only: https://www.bseindices.com/Downloads/India_Industry_Classification_Structure.pdf . Its columns are MEI_CODE, SECT_CODE, IND_CODE, BASIC_IND_CODE and definitions; it does not contain issuer identifiers or effective-dated company membership rows.
- Search of official NSE/BSE sources in this checkpoint found individual issuer disclosures/ratings documents that reproduce a company's four-level classification, but no official bulk, machine-readable, effective-dated issuer-to-classification roster or downloadable API contract. Individual company disclosure examples are not a complete universe and cannot be used to infer missing companies. The NSE page is an authoritative methodology/source, not proof of an accessible bulk membership export.
- BSE CDSL report refers to around 4,800 issuers classified into 22 sectors; the NSE Indices page's taxonomy structure and annual review process do not establish that the issuer roster can be retrieved from that page. Do not assume BSE and NSE current membership lists or effective dates are identical from taxonomy adoption alone.
- Mapping decision: no issuer mapping constructed. Require official file/API with at minimum stable issuer identifier (prefer ISIN + exchange security/symbol), classification codes, valid_from / valid_to or dated snapshot, publication/vintage timestamp, and coverage universe. If source offers only a current company profile or individual disclosures, retain point-in-time limitations and do not treat as complete historical bridge.
- Acceptance: NSE official taxonomy and classification methodology = VERIFIED; BSE hierarchy dictionary = VERIFIED; official complete issuer membership dataset = NOT LOCATED/NOT ACQUIRED; effective-dated historical roster = NOT LOCATED/NOT ACQUIRED; NSE/BSE roster equivalence = UNKNOWN; CDSL sector-to-issuer bridge = UNKNOWN. No scraping of individual issuer reports to fabricate a complete list, no synthetic joins, no ingestion, no predictive/production use.

Official references: https://www.nseindia.com/static/products-services/industry-classification ; https://www.bseindices.com/Downloads/India_Industry_Classification_Structure.pdf ; https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Oct%2031%202026.html .


## 22. Official NSE/BSE security-master identifier bridge candidate — 2026-11-13

- NSE official Securities Available for Trading page exposes `Securities available for Equity segment (.csv)`; exact official file target: https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv . Page catalogue updated 09-Nov-2026. Browser retrieval of CSV failed due unsupported text/csv content type; URL/listing verified, raw CSV bytes, row count, schema, file vintage, retrieval timestamp and SHA-256 NOT ACQUIRED.
- NSE All Reports page lists separate `CM - MII - Security File (.gz)` files for NSE-listed securities and for NSE-listed + BSE-exclusive securities. These are different universes and must not be conflated. Listing page is not raw gzip acquisition.
- NSE master-data specification describes daily Capital Market `security.txt` gzip with header/version/date and token, symbol, series. Token is unique to symbol-series, not a permanent issuer key. NSE's security-master description includes symbol, ISIN, security code and series.
- BSE official Standardised Security Master format specifies dated `BSE_EQ_SCRIP_DDMMYYYY.csv`, with Scrip Code, Instrument Code (symbol), Group Name, Scrip Name and ISIN CODE. The inspected schema does not provide industry codes or classification valid_from/valid_to.
- Future join rule: ISIN is the primary security-level cross-exchange candidate; preserve exchange symbol/security code/series with source and snapshot date. Never join on name or symbol alone. ISIN identifies a security, not necessarily a unique issuer across share classes; issuer aggregation needs a verified security-to-issuer relation. NSE Token and BSE Scrip Code are exchange-local keys, not cross-exchange permanent keys.
- These masters can potentially establish traded-security universe and ISIN crosswalk, but do NOT provide missing four-tier industry membership and cannot alone map CDSL sector totals to issuers. No issuer mapping or sector assignment inferred.
- Acceptance: NSE equity-list route and exact CSV URL = VERIFIED; raw CSV bytes/hash/schema = NOT ACQUIRED; NSE daily MII security-master candidate/spec = VERIFIED at documentation level; BSE dated scrip-master schema = VERIFIED; raw NSE/BSE files and hashes = NOT ACQUIRED; cross-exchange ISIN reconciliation = NOT DONE; issuer-to-industry membership = NOT ACQUIRED; CDSL sector-to-stock bridge = UNKNOWN. No ingestion, synthetic rows or production use.

Official references: https://betanseapi.nseindia.com/static/market-data/securities-available-for-trading ; https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv ; https://www.nseindia.com/all-reports ; https://nsearchives.nseindia.com/web/sites/default/files/inline-files/NSE-Masters%20Data-v1.6.pdf ; https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?attachedId=e99e2ca5-95d7-4173-83da-7774412bbb2d&id=20220531-44 .



## 23. BSE 2026 security-master schema change and NSE dated MII report-scope verification — 2026-11-13

- New official BSE Notice 20260422-15, dated 22-Apr-2026, updates the Standardised Scrip Master format. Field 24 changes from Filler to Closing Auction Session (CAS) Indicator, Char(1), ISO tag `ElgbltyClsgAuctnSsn`; values 0/1 mean not-in-CAS / in-CAS. Field 59 retains the BSE Exclusive flag and Char(1) value/data type, but its ISO tag changes from `Rsyd01` to `XchgExclsv`. BSE states the CAS-enabled master becomes live end-of-day Friday 31-Jul-2026.
- This is a material schema-version boundary for any BSE master parser: a parser built only from the earlier format may treat Field 24 as filler and miss the CAS eligibility field; ISO-tag consumers must recognize the Field 59 rename. Do not infer the physical CSV header or positional layout beyond the notice's explicit field mapping; validate against an acquired dated raw file before parser implementation.
- NSE official All Reports page, inspected on 13-Nov-2026, separately lists the MII security file for “NSE Listed securities” and “NSE Listed and BSE Exclusive securities”. The inspected page's latest displayed dated examples include `NSE_CM_security_11112026.csv.gz` for both variants, with distinct displayed sizes (1.22 MB and 1.49 MB). Preserve the two report universes as separate datasets; same displayed basename does not make the contents interchangeable. The page is a live catalogue snapshot, not proof that either gzip payload was acquired.
- Acquisition attempt: direct transfer of the known official NSE equity CSV target `https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv` failed in the available download path; a separate direct HTTPS attempt failed at DNS resolution in the execution environment. No raw bytes were returned. This is an environment/access failure, not evidence that NSE's source is absent or that the file is empty.
- BSE's official notice and schema update are verified, but no current dated BSE raw Scrip Master download URL or bytes were obtained. Do not guess a date-based URL or use a third-party master provider.
- Acceptance: BSE 2026 field-24/field-59 change and effective date = VERIFIED; NSE two MII universes and dated catalogue examples = VERIFIED; NSE/BSE raw master bytes, sizes, schemas and SHA-256 = NOT ACQUIRED; parser compatibility against raw 2026 BSE file = NOT TESTED; NSE/BSE ISIN reconciliation = NOT DONE; issuer classification membership = NOT ACQUIRED; CDSL sector-to-stock bridge = UNKNOWN.
- Research use: this section updates schema/version controls only. No security rows ingested, no identifier matches created, no sector mappings inferred, no predictive claim, no production authorization.
- Defined schema-change and report-scope qualification = 100%; raw master acquisition = 0%; raw-file parser validation = 0%; cross-exchange ISIN reconciliation = 0%; issuer classification roster = 0%; CDSL bridge = UNKNOWN.

Official references: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?attachedId=20260422-15 ; https://avantiscdnprodstorage.blob.core.windows.net/legalupdatedocs/55077/BSE-issued-a-notification-regarding-an-update-in-the-enhancement-in-the-Scrip-Master-File-format-April232026.pdf ; https://www.nseindia.com/all-reports ; https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv .


## 24. Exchange security-master raw-file intake validator — 2026-11-13
- Added `pipeline/security_master_intake.py` as a local, offline, fail-closed intake audit for user-supplied or otherwise locally available raw files. It hashes exact original bytes before decompression; detects gzip from magic bytes; rejects a false `.gz` extension, empty input, gzip integrity failure, invalid UTF-8, ambiguous delimiter, implausible/duplicate headers; reports row-width errors, row count, blank rows, detected header, and duplicate ISIN occurrences where an ISIN header is explicitly present.
- The generic validator does not authenticate source/publisher, infer vintage or publication time, assume exchange-specific schema/column positions, assert official provenance, map issuers/industries, or promote data to research evidence. Structural PASS is explicitly `PASS_STRUCTURAL_ONLY`; row-width defects are `FAIL_ROW_WIDTH`.
- The NSE All Reports catalogue inspected 13-Nov-2026 continues to distinguish NSE-listed-only and NSE-listed + BSE-exclusive MII master files; the catalogue is not raw-byte acquisition. NSE master technical specification documents a pipe-delimited header/detail format for its separate `security.txt` master, so this parser deliberately detects delimiter and does not conflate that format with the CSV.gz MII report.
- Regression tests cover original-byte SHA-256, gzip magic detection, duplicate ISIN reporting without issuer inference, false gzip extension rejection and ragged-row failure. CI is triggered by the QA-file push; final run status must be checked before claiming PASS.
- Acceptance: intake code persisted = PASS; test definitions persisted = PASS; executed CI result = PENDING / NOT VERIFIED; official NSE/BSE raw file acquisition = NOT DONE; exchange-specific schema validation = NOT DONE; cross-exchange ISIN reconciliation = NOT DONE; issuer/industry membership = NOT ACQUIRED; production ingestion = NOT AUTHORIZED.
- This is a reusable intake control, not a substitute for the missing raw exchange files. No synthetic data, guessed source URL, paid source, external contact, production integration, PR or merge. Protected invariants unchanged.


### Section 24 parser hardening — delimiter detection with isolated malformed rows
- Review/testing exposed a deeper issue: Python `csv.Sniffer` may fail to infer a delimiter when the sample includes a ragged row, preventing the validator from reporting the row-width defect it is designed to detect. A first QA fixture adjustment alone was insufficient.
- Replaced the Sniffer heuristic with conservative repeated-field-count voting over up to 40 nonblank lines and four explicit delimiter candidates (comma, pipe, semicolon, tab). Requires at least two records agreeing on a multi-column width and rejects ties/ambiguous layouts. Parsing then counts all row-width deviations; it does not silently discard malformed rows.
- Local focused check: comma CSV with row widths 3,3,2,3 now selects comma and exposes the single malformed row; a pipe-delimited sample selects pipe; a two-row comma sample remains detectable. This is a focused algorithm check, not GitHub CI.
- Parser hardening commit: `7f61ac0d29fcef6426988c2d73deef7245f8e6eb`, blob `7ba5a000e82d6174cda98f9bfbc13ad477eb20af`.
- CI remains PENDING / NOT VERIFIED. No raw NSE/BSE file acquired; no exchange-specific schema certification or issuer/industry mapping inferred.

 
## 2026-11-13 — Generic security-master intake validator correction
- Code review found that the structural intake report attempted to read an undefined `dialect` object after successful parsing; the report now returns the locally inferred delimiter.
- Tab-delimited detection now tests the actual tab character. QA fixture line endings were corrected, and regression cases cover tab format plus delimiter reporting for comma, pipe, semicolon, and tab.
- Validator commit `95b106d04a084c9ba2833cfa6ea66eb84cd55816` (blob `5cae180e1f279215e6926a538e8be799896c98eb`); QA commit `28d642007055e4f621327ca864d85d95cabd06b9` (blob `623e561da19816ddf293eeeceb6fee719b422b84`).
- Full suite/CI remain unverified. This remains a generic structural parser only; no exchange schema semantics or source provenance are certified.

 
## 2026-11-13 — Strict malformed-quote rejection in security-master intake
- Both delimiter sample parsing and full CSV record parsing now enable Python CSV strict mode. Unclosed/malformed quoted records fail closed with `csv.Error`.
- Validator commit `7206989479284205bcee24afbfd9c4923c8d2e30` (blob `75246bc91d84da293100532bb4061d4b69523dfb`).
- Regression test and fixture correction final QA commit `eedbee83b9afc019aaf9ec84b13fee4403fc4195` (blob `86d82597c511f286a173cbda4625d59b2d728a25`).
- Full test suite and GitHub Actions are not verified; no source-data/schema status promoted.

 
## 2026-11-13 — Tab-delimiter and blank-only input fail-closed correction
- Fixed parser's tab candidate to an actual tab character; whitespace-only files now fail with a controlled no-nonblank-record error.
- Validator commit `64aad36ed09688716dcf7b5c30cdffedf9dfcbd8` (blob `bb15dd80ccba3933f147967b5df6b995c5ec923a`).
- Added blank-only regression and corrected fixture to actual whitespace/newline characters. QA commit `69fb2a1bb6c5f670f144d9135b3f2c2c5801e0a8` (blob `f929f8b6a0f4225577d2306dd6c2a69b148983fa`).
- Test suite and CI remain NOT RUN / NOT VERIFIED; source persistence is not test evidence.

 
## 2026-11-13 — Final tab delimiter source-encoding audit
- Character-code inspection found the candidate delimiter remained a literal backslash+t sequence. Replaced it with `chr(9)` to ensure an actual tab delimiter.
- Validator commit `86edc76f30a04fc78408cc45af2c46d1456a9c7e` (blob `a625908d5701f5f95a717582dcf10913f1cbbb08`).
- Existing QA tab regression uses a Python `\t` escape and yields an actual tab at runtime; no new test method added. Full suite remains NOT RUN and CI NOT VERIFIED.

 
## 2026-11-13 — Logical-record CSV delimiter inference
- Replaced physical-line delimiter sampling with strict CSV parsing over logical records, supporting valid quoted fields containing embedded newlines while preserving ragged-row detection and fail-closed malformed quoting.
- Validator commit `fa65175e011c36711b94193513a0b7507c2cae72` (blob `b97516e076c60a0b4e659ccc0fd7606c0c79fb80`).
- Added quoted multiline-field regression test: QA commit `1db674e9ce57e20953432c0a622a00336a2bb074` (blob `7260b5210b5171a6facdb132b0b2470e9fd78520`).
- Full test suite and CI remain NOT RUN / NOT VERIFIED. Official Python CSV docs: https://docs.python.org/3/library/csv.html .


## 2026-11-13 — Security-master intake CI defect closure
- Latest 50-test run `43438875821` (head `b24395ac514d88ffb116d74bb9939ca1f98241a0`) completed SUCCESS; 50 tests in 0.083s. The two prior failures were isolated to blank-only precheck ordering and an incorrectly escaped multiline fixture.
- Validator correction `ad5037a9825313422f3faf7dc8aa89aa8ee0237f` (blob `2e2f48eeeab3d9a05b0e7f5e5499ae8c3c326cbf`): explicit whitespace-only guard before delimiter inference.
- QA fixture correction `b24395ac514d88ffb116d74bb9939ca1f98241a0` (blob `c7a72386f9633b09841e0f1630fa3e2ae24bd01d`): actual embedded newline escapes; both regression tests pass.
- CI run `43438865632` failed on validator-only commit before the fixture correction; superseded by successful run `43438875821`.
- Structural validator test success does not establish official source acquisition or exchange-specific schema certification. Raw NSE/BSE master bytes/hash, source authentication, ISIN reconciliation and issuer/industry bridge remain NOT ACQUIRED / UNKNOWN.


## 2026-11-13 — CDSL daily FPI archive retrieval retry and date-boundary reconciliation
- Re-opened official CDSL archive landing page: metadata last updated 05-Nov-2026; New Format Daily Trends dated links range from 02-Sep-2024 through 04-Apr-2025. Latest listed daily report remains 04-Apr-2025 despite separate live page data in November 2026.
- Re-followed official 04-Apr-2025 link (landing-page link 24) and retried exact target `https://www.cdslindia.com/downloads/Publications/Latest/latest_04042025.xls`. Browser open/click rejects XLS as unsupported `application/vnd.ms-excel`; direct file-download attempt also failed. Raw bytes, file size, successful-transfer timestamp, workbook schema/content and SHA-256 remain NOT ACQUIRED/UNKNOWN.
- Current Daily Trends snapshot displays reporting date 11-NOV-2026. CDSL's own note states custodian-confirmed data reflect trades on and up to previous trading day(s); reporting date is not automatically an exact trade date.
- Coverage decision: dated archive boundary VERIFIED (02-Sep-2024–04-Apr-2025); daily completeness within that boundary NOT MACHINE-RECONCILED; post-04-Apr-2025 daily archive coverage NOT VERIFIED; exact trade-date mapping UNKNOWN. No inferred files, synthetic rows, mirror sources, or fortnightly/monthly substitution.
- No ingestion or production authorization. Next acceptable acquisition route is an official browser download or original user-provided CDSL XLS; then preserve original bytes and compute SHA-256 before parsing.


## 26. Research QA CI execution evidence — 2026-11-13
- GitHub Actions run 43443062681; branch research/global-capital-rotation-overlay-mainline-20261113; head 218119c4d8c549579b06904a655ba9d0ea5d2238; push event; job 131945376329 SUCCESS.
- Retrieved full job log. Exact command: python -m unittest qa.test_global_capital_rotation_overlay -v. Result: 50 tests in 0.240s; OK; zero failures/errors.
- Tests include fail-closed source/date/vintage boundaries, CDSL reporting/archive semantics, NSE/BSE security-master identity boundaries, industry-roster coverage boundaries and generic intake validator regressions.
- CI PASS verifies this research QA suite only. It does not verify or acquire raw exchange payloads, authenticate source bytes, certify raw exchange schema, build an issuer membership roster, reconcile ISINs, or create a CDSL sector-to-issuer bridge.
- Earlier CI PENDING notes for Section 23/24 are superseded only for this verified head/run; retain all underlying raw-data and mapping gaps unchanged. No production changes, PR/merge, paid sources, synthetic data or external contact.
- Latest branch run and log evidence: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43443062681 .


## 27. NSE List of Active Securities CM and Debt — official link and raw-payload access boundary (2026-11-13)
- Re-opened the official NSE Securities Available for Trading page. It separately lists “List of Active Securities CM And Debt (.csv)” with displayed size 373 KB and page update date 09-Nov-2026. This is a distinct catalogue item from “Securities available for Equity segment (.csv)” (147 KB) and from the two NSE MII security-file universes; do not conflate their populations or semantics.
- Exact official link target resolved from the page: https://nsearchives.nseindia.com/content/equities/List_of_Active_Securities_CM_DEBT.csv . The link click was attempted once; retrieval failed at the content gateway with HTTP 400 / unsupported content-type text/csv. No raw bytes were obtained.
- Verified metadata only: official page listing, file label, displayed size, page update date, and exact target URL. File row count, columns/schema, ISIN coverage, universe composition, date/vintage embedded in payload, retrieval timestamp, byte size and SHA-256 remain NOT ACQUIRED / UNKNOWN. The displayed 373 KB is page metadata, not an independently measured downloaded file size.
- Classification: candidate active-security identity/universe source only. It is not evidence of issuer-industry membership, sector classification, security eligibility on a specific historical date, or actual daily trading activity unless its payload schema/semantics establish those properties. No symbol/name-derived industry mapping.
- Decision: source-discovery and link-resolution PASS; raw acquisition BLOCKED at content-type boundary; schema/coverage/ISIN audit NOT DONE; cross-exchange reconciliation NOT DONE; issuer-industry bridge UNKNOWN. Do not retry unchanged CSV gateway through alternate unofficial mirrors. Reattempt only if an official browser download or original user-provided file becomes available; hash exact original bytes before parsing.
- This checkpoint adds a distinct NSE catalogue source candidate and closes no data-acceptance gate. No ingestion, synthetic data, production use, PR or merge. No change to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, 56x12=672 diagnostics, Engines A-E or Hard Gate. ₹0 spend; free official source only.


## 28. NSE FII/FPI–DII live-page freshness boundary — 2026-11-13
- Re-opened the official NSE FII/FPI & DII report page and checked the current rendered/search-visible report rows without repeating the previously blocked generic CSV-link click. Official page: https://www.nseindia.com/reports/fii-dii .
- The latest visible NSE-only Capital Market sample row in the retrieved page snapshot is dated 09-Oct-2026; the latest visible combined NSE+BSE+MSEI sample row is dated 30-Oct-2026. As of this audit date 13-Nov-2026, these visible samples are stale by 35 and 14 calendar days respectively. These are page-rendered sample rows, not downloaded raw CSV observations; do not treat them as latest actual daily records or infer missing daily values.
- The official page explicitly keeps two scopes separate: NSE-only and combined NSE+BSE+MSEI. It states the combined data are collated from trades executed across the exchanges; FII/FPI data are based on PANs provided by NSDL and are provisional subject to custodial confirmation/modifications; DII data use trading-member-entered trading codes and client-category classification. Preserve provisional status and scope. Do not relabel this as final custodian-confirmed FPI flow or merge with CDSL/NSDL final data.
- Page link map exposes two “Download (.csv)” controls but does not expose their distinct final URLs in the retrieved link map (both appear through generic link id 17). No CSV download was attempted in this checkpoint, to avoid repeating the previously recorded generic-link retrieval failure. Exact CSV URLs, raw bytes, retrieval timestamps, file sizes, SHA-256, full row history and daily continuity remain UNKNOWN / NOT ACQUIRED.
- Decision: official page and scope/semantics = VERIFIED; visible sample freshness warning = VERIFIED for the retrieved snapshot; current daily raw data availability = NOT VERIFIED; CSV endpoint resolution and raw ingestion = NOT DONE; DII/FPI historical panel and calendar/arithmetic QA = NOT DONE. The stale visible sample must remain display-only and must not be ingested as current data.
- Next acceptable path remains a browser-capable session using the actual page download controls or a documented official NSE export route; capture each scope separately, hash original bytes before parsing, then test date freshness, schema, duplicate keys, buy-sell-net arithmetic and trading-calendar continuity. Do not use third-party scraper endpoints or infer URLs.
- No production use, synthetic data, unofficial mirror, paid API, PR or merge. No change to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, 56x12=672 diagnostics, Engines A-E or Hard Gate. ₹0 spend.


## 29. NSE 2026 Capital Market holiday-calendar addendum reconciliation (2026-11-13)
- Compared the original official NSE Capital Market holiday circular NSE/CMTR/71775 dated 12-Dec-2025 with the later official NSE addendum NSE/CMTR/72260 dated 12-Jan-2026 and the current official NSE equities holiday page.
- The original circular lists 15 holidays but omits 15-Jan-2026. The addendum explicitly states, “in partial modification” of circular 71775, that Thursday 15-Jan-2026 is a Capital Market trading holiday due to Municipal Corporation Election in Maharashtra. The current NSE holiday page includes 15-Jan-2026 as well as the original dates. Therefore the addendum must be applied; the original circular alone is incomplete for the final 2026 CM calendar.
- This is a verified calendar correction with direct consequences for NSE session counts, missing-session tests, rolling horizons H+1/H+3/H+5, daily flow/FX joins, and backtest date indexing. 15-Jan-2026 must be excluded as a regular Capital Market trading session. Do not use the Debt, F&O, SLBS or settlement-only notices as substitutes for the CM trading holiday source.
- Official evidence: base circular https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf ; CM-specific addendum https://nsearchives.nseindia.com/content/circulars/CMTR72260.pdf ; current NSE equities holiday page https://www.nseindia.com/resources/exchange-communication-holidays?apiversion=v2 .
- Scope: this verifies the 15-Jan addendum and reconciles the official holiday page against the base circular. It is not a full audit of every 2026 special session, Muhurat session, segment-specific holiday, or every historical year. The 08-Nov-2026 Muhurat session is a separate Sunday special session; its exact timings require its own official circular and must not be counted as an ordinary weekday session.
- Acceptance: addendum identity and date = VERIFIED; 15-Jan CM holiday = VERIFIED; base-circular omission reconciled = VERIFIED; complete multi-year session calendar archive and special-session manifest = NOT DONE; session-count recomputation over all 317/other historical records = NOT DONE; backtest reindexing = NOT DONE. Do not assert the user-reported 317-session count from this calendar check alone.
- No data rows fabricated, no forward-fill, no raw market observations ingested, no production selector/ranking/pressure-fade/672-diagnostic/engine/Hard-Gate changes, no PR or merge. ₹0 spend, official source only.
