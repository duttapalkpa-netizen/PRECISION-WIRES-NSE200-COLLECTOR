# Macro Variable–Source Matrix V1
Audit date: 2026-11-10 (Asia/Kolkata)
Scope: Milestone 6 design and source-access audit; research-only; free/public/authorized sources only.
Branch: research/global-capital-rotation-overlay-v1
Status semantics: VERIFIED_SOURCE = official route/source identified; OBSERVATION_VERIFIED = actual dated observations retrieved and checked; UNKNOWN = not yet verified; BLOCKED = access/permission or required evidence prevents use. A source URL alone is never an observation PASS.

## Gate rules
- No paid feeds, paid APIs, CEIC, Bloomberg, Capitaline, ACE Equity, or proprietary PMI content.
- No authentication bypass, prohibited scraping, or external contact without explicit user approval.
- Preserve source vintage, publication timestamp, observation/as-of date, retrieval timestamp, unit, frequency, revision status, raw-file SHA-256, row counts, missing/conflict report, and parser validation.
- Stock levels are not flows. Reserves stock/change is not reserve-currency flow. Nominal and real yields must remain separate.
- Never forward-fill missing observations. Different frequencies must not be treated as synchronized daily triggers.
- Data availability/access terms must be verified at the series/file level before ingestion. If uncertain, keep UNKNOWN/BLOCKED.

## Prioritized variable matrix

| ID | Group | Variable / operational definition | Unit | Expected frequency | Preferred official source / route | Current evidence state | Required validation / gate |
|---|---|---|---|---|---|---|---|
| M01 | Cross-border flows | Global EM portfolio investment transactions; country aggregate from BOP portfolio assets/liabilities, with documented country membership and sign convention | USD mn/bn | Quarterly/annual (dataset-specific) | IMF BOP SDMX; IMF Data Portal / SDMX Central | DSD V2.6.0 and schema validated; Dataflow ID, anonymous observation route, observations and EM aggregate UNKNOWN/BLOCKED | Resolve current dataflow and constraints through public/authorized route; retrieve observations; verify country coverage, instrument, sign, revisions, vintage; no positions-as-flows |
| M02 | Cross-border positions | Portfolio investment positions by counterpart economy (PIP/CPIS) | USD mn/bn | Annual/half-yearly | IMF PIP/CPIS | Source identified; observations not yet ingested in this overlay | Treat as stock/allocation context only; reconcile counterpart economy, instrument and reporting vintage |
| M03 | India capital flow | FPI equity net purchases/sales | INR crore | Daily/monthly | CDSL archive; NSDL; SEBI | CDSL snapshot through 2026-11-09 reconciled in existing overlay; daily source is custodian-reported with reporting lag | Preserve gross buy/sell and net; reconcile reporting date vs trade date; retain MTD/YTD separately |
| M04 | India capital flow | FPI debt by General, VRR, FAR and total | INR crore | Daily/monthly | CDSL; NSDL; SEBI | CDSL snapshot through 2026-11-09 includes debt components; existing snapshot evidence | Validate category definitions, gross/net signs, reporting lag and missing dates |
| M05 | India domestic flow | DII equity net purchases/sales | INR crore | Daily/monthly | NSE/SEBI official disclosures | Source routes identified; consistent daily series not yet ingested | Confirm official dataset, field definition, gross buys/sells, publication date and complete daily coverage |
| M06 | Policy/liquidity | Federal funds target range / effective policy rate | % p.a. | Event-driven/daily series | Federal Reserve FOMC statements; FRED | Existing overlay records 2026-10-28 +25bp event; revalidate primary statement before treating as event PASS | Store announcement/effective date separately; preserve target range vs effective rate distinction |
| M07 | Policy/liquidity | Fed total assets / balance-sheet size | USD mn | Weekly | Federal Reserve H.4.1; FRED WALCL | Official series route known; this audit has not validated a fresh observation vintage | Check release date, observation date, revisions; balance-sheet stock change is not automatically liquidity impulse |
| M08 | Policy/liquidity | Foreign-exchange reserves by currency / reserve composition | % / USD mn | Quarterly | IMF COFER | Official dataset identified; no current observations ingested | Respect publication lag and confidentiality; composition share is not currency-flow data |
| M09 | Growth | Real GDP growth | % y/y or q/q saar (keep definitions separate) | Quarterly | MoSPI National Accounts; IMF WEO/IFS; World Bank WDI | Official source families identified; series-level access, vintages and observations not audited in this matrix | Preserve release date, reference quarter, base/revision vintage; no daily trigger from quarterly release without event timestamp |
| M10 | Growth | Industrial production (India IIP) | Index / % y/y | Monthly | MoSPI IIP | User-provided IIP data work exists; current source vintage/series mapping must be joined to existing audit ledger | Validate NIC-2 mapping, base year, sector/industry codes, release date and revisions; avoid duplicate ingestion |
| M11 | Inflation | Consumer price index / CPI inflation | Index / % y/y | Monthly | MoSPI CPI; official release tables | Source family identified; series-level observation ingestion not evidenced here | Validate rural/urban/combined, base year, item weights, release/vintage and revisions |
| M12 | Inflation | Wholesale price index / WPI inflation | Index / % y/y | Monthly | Office of Economic Adviser, DPIIT | Source family identified; series-level observation ingestion not evidenced here | Validate base year, item/commodity codes, provisional/final status and publication date |
| M13 | Growth/survey | Manufacturing and services PMI | Index | Monthly | Only publicly and lawfully released official/authorized series | No verified free official full-history series in current evidence; UNKNOWN | Do not scrape or reproduce paywalled S&P Global reports; exclude until public access and license terms verified |
| M14 | Yield curve | US 2-year nominal Treasury yield | % p.a. | Daily | US Treasury daily par yield curve / Federal Reserve H.15 | Official route identified; synchronized vintage not yet validated | Confirm tenor, par/constant maturity definition, observation date and publication time |
| M15 | Yield curve | US 10-year nominal Treasury yield | % p.a. | Daily | FRED DGS10 / US Treasury | Source verified; surfaced DGS10 observation 2026-11-02 = 4.91% in existing register | Re-fetch synchronized 2Y/10Y observations; do not calculate spread from mismatched dates |
| M16 | Yield curve | US 10-year real Treasury yield | % p.a. | Daily | FRED DFII10 / US Treasury real yield curve | Source verified; surfaced observation 2026-09-10 = 2.55% is stale | Fresh synchronized vintage required; keep real yield separate from nominal yield |
| M17 | FX | Broad trade-weighted US dollar index (not ICE DXY) | Index / % change | Daily | Federal Reserve H.10 / FRED DTWEXBGS | Source and latest surfaced observation 2026-11-06 = 121.8803 verified in existing register | Keep label distinct from ICE DXY; preserve index vintage and calendar |
| M18 | FX | USD/INR RBI reference rate | INR per USD | Daily/business day | RBI Reference Rate Archive | Source verified; archive route searchable/downloadable | Keep RBI reference rate distinct from interbank close/intraday spot; validate date and missing days |
| M19 | FX | USD/INR interbank rate | INR per USD | Daily | RBI DBIE / RBI official statistical tables | DBIE table observed only through 2026-06-30 in existing audit snapshot; current route/vintage stale/UNKNOWN | Verify current RBI DBIE/CIMS route and authorized downloadable series; do not substitute reference rate |
| M20 | Commodities | Brent crude spot FOB | USD/barrel | Daily | US EIA series RBRTED | Source verified; existing surfaced latest week 2026-11-02 to 06 was partial | Wait for complete dates; preserve series definition and revisions; calculate returns only on complete windows |
| M21 | Risk | Cboe VIX close | Index points | Daily | Cboe historical data | Primary exchange source identified; not a government statistical series | Check download terms, close definition, dates and completeness; no inference of directional flow |
| M22 | India rates | India 10-year government security yield | % p.a. | Daily | RBI DBIE / FBIL official publication (series-specific) | Route/series not fully verified in current overlay; UNKNOWN | Verify benchmark security, generic vs specific bond, timestamp and stale rules; no mixing with US yield |
| M23 | India liquidity | RBI balance-sheet / reserve money / liquidity operations | INR crore | Weekly/monthly/event | RBI Weekly Statistical Supplement, DBIE, RBI liquidity operation releases | Official source family identified; series mapping and observations not audited | Distinguish reserve money, net liquidity injection, assets and stocks; preserve release date and revisions |
| M24 | Relative equity | India broad equity total-return index | TRI points / % return | Daily | NSE Indices historical TRI / NSE All Reports | NSE historical index/TRI source identified | Use TRI for dividend-inclusive comparison; verify public download rights, exact index and matched calendar |
| M25 | Relative equity | World/EM benchmark total-return index | TRI points / % return | Daily/monthly | Official index provider only if free/public terms verified | No full matched free official TRI panel established; UNKNOWN | Do not substitute price-only index or reconstruct licensed index data; compare only matched dates/currencies |
| M26 | Sector transmission | NSE sector index TRI/price series | TRI/index points | Daily | NSE Indices historical reports | Source identified; systematic sector panel not yet ingested | Verify series definitions, TRI availability, constituents and historical coverage; retain price vs TRI distinction |
| M27 | Policy events | Tariffs, immigration/H-1B, AI/semiconductor/export controls, enacted/proposed/stayed status | Categorical + dates | Event-driven | Federal Register, Congress.gov, White House, USCIS, official court orders | Primary-source-only rule established; event-by-event evidence required | Store publication/effective/stay dates, jurisdiction, legal status, source text and sector channel; political commentary is not law |

## Milestone 6 completion checklist
1. Source register crosswalked to this matrix: PARTIAL — existing source register reused; no duplicate source discovery claimed.
2. Variable definitions and measurement cautions documented: PASS (design artifact only).
3. Free/public/authorized access status: PARTIAL — explicitly unknown where not proven.
4. Actual raw observation ingestion: NOT COMPLETE.
5. Vintage/timestamp/revision validation: NOT COMPLETE for most rows.
6. SHA-256 manifests, row counts, missing/conflict reports and parser QA: NOT COMPLETE for this matrix's data series.

## Current milestone status
- Milestone 6 (Global Macro Data Ingestion): 20% design/source mapping only; observation ingestion remains 0% until raw series are lawfully retrieved and validated.
- Milestone 7 (Relative Attraction + Sector–Stock Bridge): 0%.
- Milestone 8 (Historical Event Study / Backtest): 0%.
- Overlay progress: do not increase the previously verified 62.5% (5/8) based on this design artifact alone.
- Overall PRECISION-WIRES V11.3 progress: NOT_CALCULABLE until the master acceptance denominator and all gates are reconciled.

## Next non-duplicate action
Resolve and test only the highest-priority unresolved official series access routes (IMF BOP dataflow/observations; RBI current DBIE/CIMS and reference-rate downloads; MoSPI GDP/CPI/IIP/WPI release series). Do not rerun completed XML/XSD validation or re-ingest the already reconciled CDSL snapshot. Store raw responses before parsing; if access is not public/authorized, retain UNKNOWN/BLOCKED and move to the next source.


## 2026-11-10 evidence addendum — MoSPI release metadata and access boundaries
This addendum supplements (does not replace) the original 27-variable matrix.

### Verified official catalogue facts
- eSankhyiki catalogue exposes 4,784 catalogue entries in the current search snapshot and includes IIP, CPI and NAS product families. Catalogue existence is not equivalent to a machine-readable API response.
- IIP catalogue entry: monthly indices and growth rates by use-based classification through August 2026; reference period August 2026; release date 28-Sep-2026; stated publication lag approximately six weeks.
- CPI catalogue entry: All-India general group-wise indices/inflation for August 2026 (provisional), base year 2024; release date 14-Sep-2026. July 2026 entry release date 12-Aug-2026. CPI must therefore carry provisional/final status and base-year metadata.
- MoSPI CPI National Metadata Structure states monthly public dissemination for aggregated CPI (item/subclass/class/group/division levels for All India and States/UTs), normally 4 PM on the 12th of the following month or next working day. Unit-level basket price data are not public.
- MoSPI GSDD FAQ classifies aggregated National Accounts, CPI and IIP at NIC 2-digit level as Category A Open Access, free without registration. Anonymized unit/item-level data are Category B and require Microdata Portal registration; commercial use may be priced. Restricted data require authorization.
- NAS catalogue exposes an official quarterly current-statement workbook snapshot dated 05-Jun-2026. This is a downloadable publication artifact, not yet normalized into a time-series observation panel.

### API schema inspection outcome
- Official IIP API documentation page identifies OpenAPI 3.0.0 and GET `/api/iip/getIIPData`.
- The page's Swagger UI says its preview returns only the first 10 records. Therefore preview output must never be treated as complete history.
- The page links to `../../layout/swagger_user_iip.yaml`, but the raw YAML could not be retrieved through the available inspection route in this audit. Exact query parameters, required fields, pagination, authentication and response schema remain UNKNOWN.
- A separately discovered GitHub implementation is non-government code and is not accepted as the authoritative API contract. It may be used only as a discovery clue, never to fill missing official schema fields.
- An attempted raw-YAML open returned an unsupported-content-type/tool fetch error; this is a tooling limitation, not evidence that the MoSPI endpoint is down or that the YAML is invalid.

### Updated variable-level gate decisions
| Variable | New evidence | Gate |
|---|---|---|
| India IIP (M10) | Official catalogue coverage through Aug-2026; release date and approximate six-week lag documented; API endpoint named but exact schema not retrieved | SOURCE + RELEASE METADATA VERIFIED; API PARAMETER SCHEMA UNKNOWN; OBSERVATIONS NOT INGESTED |
| India CPI (M11) | Official catalogue exposes Aug-2026 provisional 2024-base dataset and release date; monthly release timing documented; aggregate open-access policy verified | SOURCE + RELEASE METADATA VERIFIED; OBSERVATIONS NOT INGESTED |
| India GDP/NAS (M09) | Official NAS quarterly statement workbook exists as a downloadable catalogue artifact; new 2022-23 base series must be kept distinct from 2011-12 historical series | SOURCE ARTIFACT VERIFIED; OBSERVATION PANEL NOT INGESTED; SERIES BRIDGE UNKNOWN |
| India WPI (M12) | No new official series-level route or observation evidence in this audit | UNKNOWN; unchanged |

### Quality controls before first ingestion
1. Preserve the original downloaded bytes and SHA-256 before opening/parsing.
2. Record catalogue table ID, product, reference period, release date, base year, provisional/final flag and source URL.
3. For IIP, obtain the complete API response with documented pagination; compare row count and coverage with the matching catalogue table before accepting it.
4. For CPI, keep Rural/Urban/Combined and base-year 2024 series separate; do not splice 2012-base and 2024-base without an official linking method.
5. For NAS, distinguish quarterly/annual estimates, current-price/constant-price series, base year, and first/revised/provisional vintages.
6. No API key, registration or authentication bypass is to be attempted where terms do not permit it. Public aggregate data only.

### Progress control
- This addendum: completed as source/release-metadata audit; not an observation ingestion.
- Milestone 6 stays at 20% design/source mapping; observation ingestion remains 0%.
- Overlay remains 62.5% (5/8); overall V11.3 remains NOT_CALCULABLE.
