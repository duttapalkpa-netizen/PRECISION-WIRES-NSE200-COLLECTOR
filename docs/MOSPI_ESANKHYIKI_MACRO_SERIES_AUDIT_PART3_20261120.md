# MoSPI / e-Sankhyiki Macro Series Audit — Part 3
Date: 2026-11-20
Research page: গবেষণা যাচাই অব্যাহত 41, Part 3
Scope: source-grounded audit of IIP, CPI, National Accounts/GDP and PLFS. Read-only review of official MoSPI/e-Sankhyiki catalogue, API documentation, releases and GSDD 2026 FAQ. No API calls, data downloads, production integration, model training or selector changes were performed.

## 1. Critical policy correction — GSDD 2026 supersedes the earlier assumption
MoSPI's official FAQ says Revised Guidelines for Statistical Data Dissemination (GSDD) 2026 supersede GSDD 2019. It classifies:
- Category A (Open Access): aggregated/analysed information and publications; examples expressly include National Accounts, CPI, IIP at NIC 2-digit level, ASI Volume I, NSS reports/factsheets and central statistics reports. Free on MoSPI website without registration.
- Category B (Registered Access): anonymized unit-level/item-level data, including NSS unit-level, Economic Census unit-level and item-level IIP; registration on Microdata Portal required; free for non-commercial use and priced for commercial use.
- Category C (Restricted Access): examples include UFS block maps, Statistical Business Register data, ASI frame/panel data; only with MoSPI authorization.
- Non-shareable: data compromising privacy/national security, identifiers, certain restricted survey frames/intermediate worksheets, etc.
- FAQ clarifies that GSDD dissemination provisions do not govern secondary-source datasets received by MoSPI; dissemination remains with the original source owner.

**Correction to Part 2:** The previous blanket "MoSPI/e-Sankhyiki conditional GO where GODL-India is present" was incomplete. GSDD 2026 is an access/dissemination classification, not by itself a blanket copyright/reuse/model-training/redistribution licence. Do not assign GODL-India to every e-Sankhyiki series. Apply GODL only where the exact resource metadata explicitly names it; otherwise keep reuse/training/redistribution permissions UNKNOWN pending the applicable terms.

## 2. Series-by-series findings as of 2026-11-20

### A. IIP — Index of Industrial Production
- Current series base year: 2022-23=100. New series first press release was 01-Jun-2026; classification for new series uses NIC-2025 and six use-based categories continue. New series source release explains the revised basket/weights and sector coverage.
- Latest verified release on cutoff: September 2026 quick estimates, published 28-Oct-2026. Headline IIP growth 6.7% YoY; manufacturing +7.6%, electricity & gas supply +11.2%. The next scheduled IIP release is 28-Nov-2026, so October IIP was not yet due/available on this audit date.
- Official release cadence: 28th each month (or next working day). MoSPI e-Sankhyiki Macro Indicators page states roughly four-week lag; individual catalogue text in older records describes six weeks. Use actual release timestamps as the operational truth and treat generic lag text as inconsistent pending MoSPI clarification.
- API documentation: e-Sankhyiki IIP API v1.0.0, endpoint `GET /api/iip/getIIPData`. OpenAPI YAML was not machine-readable through this audit; query parameters, pagination, authentication, rate limits and exact schema fields are therefore **NOT VERIFIED**. Do not implement a client from guessed parameters.
- Catalogue consistency issue: current indexed IIP catalogue result surfaced August 2026 tables (e.g. IIPMFY26020AUG, IIPMFY26017AUG, IIPMFY26019AUG, IIPMFY26018AUG; release date 28-Sep-2026), while the official September press release and Macro Indicators visualisation show September 2026 already released on 28-Oct-2026. This is a catalogue indexing/update lag; catalogue search must not be treated as the latest-release authority.
- Historical coverage: the new series uses 2022-23 base; the first new-series press release contains annual/period tables back into FY 2023-24 and a 13-month chart, but a complete monthly back-series start/end and machine-readable vintage history were not established in this audit. Record the actual downloadable table coverage at ingestion.

### B. CPI — Consumer Price Index
- Current CPI series base year 2024=100; basket/weights use HCES 2023-24; price reference period Jan-Dec 2024; COICOP 2018 structure and 12 divisions. Monthly rural/urban market price collection is described in CPI 2024 FAQ.
- Latest verified release: October 2026, published 12-Nov-2026. Headline combined CPI inflation 6.09% provisional; rural 6.63%, urban 5.41%; CFPI combined 8.94% provisional. September 2026 is final (combined CPI 5.54%, CFPI 7.74%).
- API documentation: e-Sankhyiki CPI API v2.0.0; endpoint `GET /api/cpi/getCPIData`; covers base years 2010, 2012 and 2024; paginated JSON envelope with `statusCode` and `msg`. Documentation states bearer token optional (guest access) and IP rate limits apply. Exact parameter names, page limits and full schema were not independently extracted from the OpenAPI YAML; do not guess them.
- Catalogue consistency issue: current indexed CPI catalogue page surfaced September 2026 records (e.g. CPIMCY26004SEP, CPIMCY26003SEP, CPIMCY26001SEP; release date 12-Oct-2026), while the official October press release exists from 12-Nov-2026 and the e-Sankhyiki macro indicator displays October 2026. The catalogue index is behind the latest release.
- Historical coverage: API supports legacy base years 2010 and 2012 as well as 2024; this does not mean the series are directly spliceable. Maintain separate base-year series and use only official overlap/linked series methodology where explicitly published. Exact earliest/latest date and revision vintage require data-level export audit.

### C. National Accounts Statistics (NAS) / GDP
- New annual and quarterly National Accounts series base year 2022-23 replaced 2011-12 series. The new series includes changes in sources and methodology, including improved coverage, double deflation for agriculture/manufacturing, improved quarterly benchmarking and GST/administrative data.
- e-Sankhyiki NAS catalogue has 1,724 records. A current catalogue example shows Q1 FY 2026-27 quarterly GDP expenditure-component tables at constant and current prices (table IDs AEQEAFY2607QTR and AEQEAFY2608QTR), released 31-Aug-2026. Macro Indicators homepage shows Q1 FY 2026-27 GDP growth 7.8%.
- Advance Release Calendar updated through October 2026 schedules Q2 FY 2026-27 quarterly GDP estimates for 30-Nov-2026. Thus Q2 is not yet available as of 20-Nov.
- GDP new series release (27-Feb-2026) covers annual estimates FY 2022-23 to FY 2024-25 and quarterly estimates Q1 FY 2022-23 through Q3 FY 2025-26; later quarterly releases add newer periods.
- Back-series: MoSPI FAQ for new GDP series states back series was expected by December 2026; exact release and final methodology not confirmed as of audit cutoff. Do not splice old 2011-12 base and new 2022-23 base directly.
- No dedicated public NAS API endpoint/schema was identified in the reviewed e-Sankhyiki API pages. e-Sankhyiki catalogue supports table downloads; actual NAS data are also published in tables/press-note annexures. API availability is **NOT ESTABLISHED**, not assumed absent.
- Catalogue rows may include state domestic product data still based on 2011-12. Never mix those with new national GDP base 2022-23 series merely because both appear under NAS.

### D. PLFS — Periodic Labour Force Survey
- Survey design revamped from January 2025. Monthly all-India estimates of LFPR, WPR and UR are released under Current Weekly Status (CWS), disaggregated by gender, rural/urban sector and broad age group; quarterly estimates extend to rural and urban areas.
- Latest verified monthly bulletin: October 2026 (MB-19), dated 16-Nov-2026. LFPR for persons aged 15+ was 55.7% all India; rural 58.4%; urban 50.5%. These are survey estimates, not daily market indicators.
- October 2026 bulletin confirms monthly series April 2025–October 2026, nineteenth bulletin. CWS uses the preceding 7 days; usual status uses 365 days. Do not mix CWS and usual-status series.
- Catalogue indexed records were still September 2026 (PLFSFY26003SEP etc.) with release 15-Oct-2026, while October bulletin dated 16-Nov exists. Catalogue update lag identified.
- No public PLFS API schema was found in the reviewed API pages. e-Sankhyiki catalogue offers Excel/CSV downloads and the bulletin links detailed Excel tables. Treat API status as NOT VERIFIED, not a claim of no API.
- PLFS monthly and quarterly indicators should be low-frequency macro context only; not a direct short-horizon stock-entry signal. Monthly/quarterly estimates should carry sample design, CWS/US status, revision and publication-time metadata.

## 3. Cross-series ingestion readiness matrix
| Series | Current base/method | Latest verified reference | Release/publication | Access class evidence | API/schema | Historical continuity | Decision |
|---|---|---|---|---|---|---|---|
| IIP | 2022-23=100; NIC-2025 | Sep-2026 | 28-Oct-2026 | Category A explicitly includes IIP NIC-2; item-level IIP Category B | API v1.0.0 endpoint known; params/schema not verified | Full monthly back-series and vintage archive not verified | CONDITIONAL — aggregated NIC-2 only; schema + exact table licence/terms + vintage audit |
| CPI | 2024=100; COICOP 2018; HCES 2023-24 weights | Oct-2026 | 12-Nov-2026 | Category A explicitly includes CPI | API v2.0.0 endpoint known; base years 2010/2012/2024; optional bearer token; rate limited | 2010/2012/2024 bases exposed; splice/continuity not established | CONDITIONAL — preserve each base separately; validate schema, revisions, licence/terms |
| NAS/GDP | 2022-23=100 | Q1 FY 2026-27 | 31-Aug-2026 | Category A explicitly includes National Accounts | No dedicated API endpoint verified; table download/press release | New series 2022-23 base; back series expected Dec-2026 | CONDITIONAL — table-based ingestion only; wait for back-series and preserve vintages |
| PLFS | Revamped design from Jan-2025; monthly CWS | Oct-2026 | Bulletin dated 16-Nov-2026 | Aggregated public bulletin likely Category A, but exact category metadata not explicitly confirmed on the record inspected | No API schema verified; catalogue Excel/CSV/bulletin tables | Monthly bulletins Apr-2025–Oct-2026; quarterly rural+urban; don't mix CWS/usual status | CONDITIONAL — context only; verify category and preserve survey design/vintage |

## 4. Release calendar / freshness controls
As of 20-Nov-2026:
- CPI October 2026 released 12-Nov-2026.
- PLFS October 2026 bulletin dated 16-Nov-2026.
- IIP September 2026 released 28-Oct-2026; October IIP scheduled 28-Nov-2026.
- GDP Q1 FY 2026-27 tables released 31-Aug-2026; Q2 scheduled 30-Nov-2026.
- GDP back series expected by December 2026 per FAQ, not yet verified as released.
Use the latest official release/press note timestamp, not a stale catalogue search result. Record both catalogue indexed period and press-release period and alert on divergence.

## 5. Required per-series ingestion contract
Before connecting any series to GCR:
1. Capture exact dataset/table ID, official URL, table title, base year, classification, units, reference period, release date, status (provisional/quick/final/revised), and revision vintage.
2. Capture the GSDD 2026 access class (A/B/C/non-shareable) and whether the record is MoSPI-produced or secondary-source material whose dissemination is controlled by the original source owner.
3. Capture source-specific reuse, model-training, publication, redistribution and retention terms separately. GSDD Category A/free download does not by itself settle all downstream rights.
4. For APIs, use only published OpenAPI schema and exact parameter names. CPI optional token/rate limit and IIP API endpoint are documented, but parameters/schema still need direct technical validation. Do not invent request payloads.
5. Archive immutable raw bytes and exact response metadata; compute SHA-256; retain manifest, parser version, QA report, and previous vintage.
6. Validate schema, pagination completeness, duplicate keys, missing periods, units, base-year consistency, release-vintage changes, and table totals.
7. For IIP and CPI, keep index level and YoY growth as separate fields; do not calculate growth across different base-year series without official linking methodology.
8. For PLFS, keep CWS monthly, CWS quarterly, and usual-status annual indicators separate.
9. For NAS, keep current-price and constant-price series, annual and quarterly periods, and GDP/GVA/expenditure components separately.
10. Only after the above pass may a dataset be proposed for GCR input. This audit does not authorize production ingestion or scoring boosts.

## 6. Corrections and prior lessons preserved
- Corrected Part 2 source register: MoSPI GSDD 2026 supersedes GSDD 2019. Category A/B/C are access/dissemination classifications, not blanket GODL or model-training licences. GODL applies only when exact resource metadata says so.
- e-Sankhyiki catalogue index is behind official latest releases for IIP, CPI and PLFS in the examples checked. Always reconcile catalogue index with dated press release and release calendar.
- Run #407 T20_H5 threshold audit must use `pd.read_csv(..., float_precision="round_trip")`.
- NSE HTTP 403 remains fail-closed. NSE MCP 1–3 minute snapshot is not a 1-minute candle feed and is not trading-use permission.
- SEBI educational price-data lag is not assumed to create a private research exemption.
- No paid APIs, no synthetic observations, no access-control bypass, no fabricated timestamps.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## 7. Sources (official)
- MoSPI GSDD 2026 FAQ: https://mospi.gov.in/faq
- e-Sankhyiki catalogue: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue
- e-Sankhyiki IIP API documentation: https://esankhyiki.mospi.gov.in/macroindicators?product=iip&tab=api
- e-Sankhyiki CPI API documentation: https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api
- IIP September 2026 press release (28-Oct): https://mospi.gov.in/uploads/latestReleases/latest_release_1793182514284_e9b71fc1-c565-480f-81c2-91618ea42c2f_IIP_Press_Release_September_2026.pdf
- CPI October 2026 press release (12-Nov): https://mospi.gov.in/uploads/latestreleasesfiles/1794480048335-Press%20Release%20of%20CPI%20for%20October%202026%20.pdf
- PLFS October 2026 monthly bulletin (16-Nov): https://mospi.gov.in/uploads/publications_reports/publications_reports1794821821618_7cec3a56-a5c5-4a5e-a347-3b5e1b5f4a63_Monthly_Bulletin_PLFS_Oct_2026.pdf
- MoSPI Advance Release Calendar 2026-27 (updated October 2026): https://www.mospi.gov.in/uploads/documents/releaseCalender/1793948871564-ARC%202026-27%20updated%20till%20October%202026.pdf
- New GDP series press note (27-Feb): https://mospi.gov.in/uploads/latestReleases/latest_release_1772189865181_f040336d-bc57-4aed-b80f-586d9ccb279e_Press_Note_on_New_Series_of_GDP_Estimates_with_Base_Year_2022-23_27022026.pdf
- e-Sankhyiki catalogue NAS: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?page=0&product=NAS

## 8. Final audit status
- Policy classification correction: COMPLETED.
- Latest release/vintage cross-check for IIP/CPI/NAS/PLFS: COMPLETED from official indexed records/press releases.
- API endpoint inventory: PARTIAL (IIP/CPI endpoint names verified; full OpenAPI parameters/schema not verified; NAS/PLFS API not established).
- Historical depth and full downloadable table completeness: NOT YET VERIFIED.
- Resource-level exact reuse/model-training rights: NOT YET VERIFIED for each table.
- Production GCR integration: NOT AUTHORIZED / NOT PERFORMED.
- Stock-selection readiness: unaffected; no live stock promoted.
