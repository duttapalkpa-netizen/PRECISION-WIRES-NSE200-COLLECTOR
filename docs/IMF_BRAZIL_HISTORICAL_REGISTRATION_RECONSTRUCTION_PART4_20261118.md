# IMF Brazil Historical Registration Reconstruction — Part 4
Date: 2026-11-18 (Asia/Kolkata)
Continuation: গবেষণা যাচাই অব্যাহত 38
Scope: official IMF historical-registration surface and documented service boundary; no production change, no repeated RSS/BCB downloads.

## 1. Reused evidence — not repeated
- Part 1/2 registration listing and BCB payload contract mismatch remains CONFIRMED:
  - Registry Dataflow: `IMF:BOP6(1.0)`, Provider `IMF:BR1`, BCB registered URL.
  - BCB payload Dataflow: `IMF:BOP_BPM6(1.0)`.
  - Same DSD does not make distinct Dataflow identities equivalent.
  - Constraint compatibility: 234/237 = 98.7342% for BOP6; 27/237 = 11.3924% for BOP_BPM6.
  - Brazil admission remains BLOCKED pending authoritative IMF-side explanation/correction.
- Part 3 recent RSS transaction window: 33/33 HTTP 200, XML well-formed and QueryRegistrationResponse Success; no Brazil marker in this bounded window. Historical events outside the 33-item window remain UNKNOWN.
- No re-download of RSS, BCB XML, or the same 33 transaction links in this part.

## 2. Official historical-registration view discovered and inspected
- IMF Data Registrations historical activity view: https://sdmxcentral.imf.org/activity/data-log.html
- The rendered page labels itself "Showing historical activity for provision agreements".
- It exposes columns/fields: Agency, Id, Version; Date, Data URL, Action, Data Store, Series; Registration Details: Data URL, Provision URN, Dataflow URN, Data Provider URN, User.
- The static/readable page extraction did not expose any data rows; it displayed the table schema only. No Brazil event row or event timestamp can be claimed from this inspection.
- IMF Provision Agreements listing: https://sdmxcentral.imf.org/data/provisionAgreements.html . Public rendered listing includes IMF Provision Agreement records, but static page extraction does not provide a validated complete Brazil historical change chronology.
- IMF SDMX Transactions view: https://sdmxcentral.imf.org/activity/activity-log.html . The public page supports date-range selection and transaction download in its UI; static extraction is not a complete Brazil-specific transaction ledger.

## 3. Official API boundary
- IMF SDMX Central Web Services Guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- Documented public REST entry point supports SDMX structure/data queries.
- Guide explicitly states there is no official REST API for data-processing services such as validation, conversion, or registration; those services use a separate FMR entry point.
- Therefore no undocumented internal AJAX route, guessed API, or guessed transaction identifier is accepted as an official source.
- The public historical activity GUI is a legitimate next route, but its data must be obtained from actual visible/downloadable records, not inferred from the page shell.

## 4. Part-4 acceptance
| Check | Status |
|---|---|
| Official Data Registrations history page located | PASS |
| Fields needed for Brazil reconstruction identified | PASS |
| Actual Brazil historical rows retrieved from static page | NOT_DONE |
| Brazil-specific historical timestamps verified | UNKNOWN |
| Official documented registration REST API available | NO — guide says none |
| Undocumented endpoint use | REJECTED |
| Brazil Dataflow mismatch | CONFIRMED |
| Brazil admission | BLOCKED |
| EM aggregation / trading admission | NOT_AUTHORIZED |

## 5. Exact next action — Brazil first
1. Use the official Data Registrations GUI and Provision Agreements listing to filter/search exact agency `IMF`, provider `IMF:BR1`, and relevant `BOP6` / `BOP_BPM6` identifiers.
2. Download or capture only actual Brazil-specific history rows and linked official registration documents; record date, action, Data URL, Provision URN, Dataflow URN, provider URN, source URL, retrieval time, raw bytes and SHA-256.
3. Compare historical rows against the already archived current registry listing and BCB payload. Determine whether the mismatch arose from create/replace/delete/re-registration, stale URL, provider reassignment, or an unexplained current inconsistency. Do not choose a cause before evidence.
4. If the official GUI cannot expose/export the required rows without authentication or no Brazil rows exist in its available window, record the exact limitation and keep chronology UNKNOWN; do not scrape undocumented endpoints.
5. Only after Brazil reconstruction reaches evidence-backed closure should the high-impact India macro overlay phases begin. Do not start lower-impact country overlays ahead of this gate.

## 6. Deferred high-priority India-market macro queue (not yet integrated)
Based on the user's requested focus and the existing source register, the following are queued for the post-Brazil phase. This is a gap map, not a claim that these factors already have validated predictive power.

| Priority | Factor / geography | Existing research coverage seen | Gap / next research |
|---|---|---|---|
| P0 | US 10Y yield, broad USD/DXY distinction, USD/INR, Brent | Fed H.10 broad dollar and US 10Y source routes registered; RBI FX and EIA Brent source routes identified | Complete synchronized daily observations, precise series identity, freshness gates, 1/5/20-day changes and India-sector response tests. H.10 broad dollar is NOT ICE DXY. |
| P0 | US Fed policy / US CPI event dates | Existing official source registry covers US macro/policy routes generally; specific event-study integration not evidenced in the inspected source register | Build exact official release/meeting calendar, preserve announcement timestamps and surprise-vs-consensus only if an official/free source exists. |
| P1 | China stimulus, tariffs, China/India EM allocation | No validated China-vs-India allocation series or tariff event-to-sector panel evidenced in inspected source register | Use official PBOC/NBS/Ministry of Finance/Customs and official tariff notices; separate policy announcement, implementation, and retaliation dates. |
| P1 | South Korea/Taiwan semiconductor & AI rotation | No validated KOSPI/TAIEX matched total-return series or foreign-flow panel evidenced in inspected source register | Verify official exchange/provider public data, FX-normalized returns, matched calendars, and India-vs-Korea/Taiwan relative performance. |
| P1 | Japan BOJ / JPY carry stress | No validated JPY funding/carry proxy or BOJ event panel evidenced in inspected source register | BOJ policy/yield/FX sources plus USD/JPY and volatility; do not infer leveraged unwind from a rate change alone. |
| P0 | Middle East/OPEC+ / Brent supply shock | EIA Brent spot source route identified; geopolitical headline status alone not a validated shock variable | OPEC official decisions, EIA price series, shipping/supply facts only where official; test India sector sensitivity (OMC, paints, tyres, aviation, chemicals). |
| P0 | India FPI / DII and sector flow | CDSL daily FPI and NSDL/SEBI sources identified; daily DII series not yet consistently ingested in the source register | Acquire consistent FPI/DII series; NSDL fortnightly sector data only at its actual publication frequency; do not interpolate to daily. |
| P1 | Relative-strength ratios | NSE index historical sources identified; no validated NIFTY/EEM, NIFTY/KOSPI or NIFTY/TAIEX matched TRI panel | Verify free official total-return benchmark availability, currency treatment and trading-calendar alignment. EEM is an ETF benchmark, not a pure index series. |
| P0 | Event study with 200-session NSE archive | Historical NSE backbone exists; the requested global-event sector bridge is not yet accepted | Map official event timestamps to Indian sessions; test H+1/H+3 sector returns, low-beta and DII support, costs, false positives and missed winners. |

### Macro integration guardrails
- Research-only overlay. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or Engines A-E changes.
- No automatic country-weight assumptions. Country importance must be measured against Indian market/sector returns, not assigned by narrative.
- Daily macro gate must use synchronized and fresh values; stale/missing data => UNKNOWN, never forward-fill.
- Separate US broad trade-weighted dollar index from ICE DXY; separate nominal Treasury yield from real yield; separate RBI reference rate from interbank/spot; separate EIA Brent spot from futures settlement.
- Sector flow frequency must match its actual publication frequency. Fortnightly data must not be fabricated into daily data.
- Relative ratios must use comparable total-return series and matched dates; currency effects must be explicit.
- Event studies must use publication timestamps, matured outcomes, rolling out-of-sample validation and cost-aware returns.
- A factor receives weight only after incremental predictive value is demonstrated over existing NSE/sector signals; otherwise keep it research-only or reject it.

## 7. Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), Engines A-E unchanged. No PR merge, production integration, paid API, synthetic data, invented timestamp, undocumented endpoint, guessed event ID, or trading admission. UNKNOWN is not PASS.
