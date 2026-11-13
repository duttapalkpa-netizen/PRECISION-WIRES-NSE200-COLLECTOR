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
