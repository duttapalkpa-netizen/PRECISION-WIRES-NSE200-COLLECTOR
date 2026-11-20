# India Benchmark Panel — Official Source Contract, Part 1
Date: 2026-11-20 (Asia/Kolkata)
Project: PRECISION-WIRES V11.3 / Global Capital Rotation & Relative-Attraction Overlay
Status: **SOURCE-LOCATOR AUDIT PARTIAL PASS; RAW INGESTION, SHA-256 ARCHIVE AND SYNCHRONIZED PANEL NOT YET RUN.**
Purpose: Execute the first dependency in the India Market Transmission Country Priority Layer: define the Indian outcome panel and the public/official external benchmark inputs before country-specific event studies.

## 1. Continuity and scope
- Reopened the India Market Transmission Country Priority Layer and current GCR Master Priority Queue before work.
- This task follows the documented execution order: India benchmark panel first, then Tier-0 country/benchmark coverage.
- This is a source contract and rights/freshness audit only. No market data were downloaded into the repository, no raw archive or SHA-256 was created, no panel was assembled, and no event study was run.
- No IMF re-query, 63-country cohort rebuild, national BOP validation repeat, or production code/selector/ranking/trade-alert modification.

## 2. India outcome panel — source register

| ID | Required series | Preferred official source | Frequency / observed capability | Gate |
|---|---|---|---|---|
| IN-EQ-01 | NIFTY 50 OHLC/close | NSE Historical Index Data / All Reports | Historical index page exposes date range and CSV download; NIFTY 50 history available from 03-Jul-1990 per NSE Indices FAQ | SOURCE LOCATOR PASS; raw capture NOT_DONE |
| IN-EQ-02 | NSE sector indices | NSE Historical Index Data | Index selector supports historical index series; exact selected sector list and raw coverage still to be enumerated at ingestion | SOURCE LOCATOR PASS; coverage NOT_AUDITED |
| IN-VOL-01 | India VIX | NSE Historical Data — India VIX | Separate historical data section and date-range export exposed | SOURCE LOCATOR PASS; raw capture NOT_DONE |
| IN-EQ-03 | S&P BSE SENSEX / sector indices | BSE / Asia Index Private Limited | Methodology establishes SENSEX history; BSE EOD/index-history materials identify licensed data distribution and commercial terms | RIGHTS GATE BLOCKED for automatic free archival use; do not scrape or assume free redistribution |
| IN-FX-01 | USD/INR | FBIL Reference Rate | FBIL methodology confirms actual spot transactions during 11:30–12:30 IST; RBI confirms FBIL took over publication from 10-Jul-2018 | METHODOLOGY PASS; repeatable historical raw-export path NOT_CAPTURED |
| IN-FX-02 | USD/INR independent cross-check | Federal Reserve H.10 via FRED series DEXINUS | Daily New York noon buying rate; updated weekly; latest observation seen 13-Nov-2026 | CROSS-CHECK ONLY; not a substitute for FBIL or Indian market close |
| IN-RATES-01 | India 10Y G-Sec | FBIL GOI Par Yield; RBI National Summary Data | FBIL archive exposes dated GOI prices including par yield; RBI summary explicitly reports 10Y G-Sec Par Yield (FBIL) | SOURCE LOCATOR PASS; full daily history/hash NOT_CAPTURED |
| IN-RATES-02 | Daily tenor cross-check | CCIL Tenorwise Indicative Yields | Indicative G-Sec/T-Bill/SDL tenor buckets; 9Y–10Y bucket displayed; CCIL states commercial use requires written permission | RESEARCH DISPLAY ONLY pending rights review; not a production feed |
| IN-FLOW-01 | Daily FPI/DII cash-market activity | NSE FII/FPI & DII trading activity | Daily combined and NSE-only CSV surfaces; explicitly provisional and subject to custodial confirmation/modifications | SOURCE LOCATOR PASS; freshness at execution must be checked; provisional flag mandatory |
| IN-FLOW-02 | Final/custodian-confirmed FPI flows | NSDL FPI portal / CDSL | NSDL exposes latest, archive, quarterly, country-wise and sector-wise reports; page result inspected showed an old dated example (30-Oct-2025), so current freshness not established | SOURCE FAMILY PASS; current daily freshness NOT_VERIFIED |
| IN-COM-01 | Indian crude basket | PPAC International Prices of Crude Oil (Indian Basket) | Official historical/current report download and FY/month selector exposed | SOURCE LOCATOR PASS; daily versus monthly granularity must be inspected before event use |
| GLB-RISK-01 | CBOE VIX | Cboe historical VIX data | Daily closing data, 1990 to present, updated daily | SOURCE LOCATOR PASS; raw capture NOT_DONE |
| GLB-FX-01 | Broad USD index proxy | Federal Reserve broad trade-weighted USD index via FRED | Daily nominal broad USD index available through 13-Nov-2026 | PROXY SOURCE PASS; explicitly not ICE DXY |
| GLB-RATES-01 | U.S. Treasury 2Y/10Y | U.S. Treasury Daily Treasury Par Yield Curve Rates | Official daily 2Y and 10Y CMT series and CSV/XML; derived from indicative bid-side quotes around 3:30 PM New York time | SOURCE LOCATOR PASS; methodology/timezone flag required |
| GLB-RATES-02 | Federal funds target/range and event time | Federal Reserve FOMC calendar, statements and implementation notes | Official dated decision statements and meeting archive | EVENT SOURCE PASS; no invented daily interpolation |
| GLB-COM-01 | Copper, aluminium, gold and other commodity benchmarks | World Bank Commodity Markets Pink Sheet | Official monthly XLS/XLSX history and monthly releases | MONTHLY SOURCE PASS; not suitable as an intraday/H+1 trigger |

## 3. Verified source facts and important caveats
1. NSE's historical reports surface exposes historical index data, India VIX history, NIFTY valuation series and Total Returns Index values. NSE Indices states NIFTY 50 history is available from 03-Jul-1990. Use NIFTY TRI for total-return research where available; do not mix price index and TRI.
2. BSE's published index methodology gives the SENSEX history/base information, but BSE data-product material identifies EOD index history as licensed/distributed data. Keep BSE SENSEX outside the zero-cost automated archive until exact permitted public access/rights are established. Do not silently substitute a third-party copy.
3. FBIL took over computation/dissemination of USD/INR and other major-currency reference rates from RBI effective 10-Jul-2018. The FBIL USD/INR methodology uses actual electronic-platform spot transactions in the 11:30–12:30 IST window. This is a benchmark observation, not the entire day's traded FX path.
4. FRED DEXINUS is sourced from the Federal Reserve H.10 release and is a New York noon buying rate; the H.10 daily data are updated weekly. It is an independent cross-check with a different observation time, not an interchangeable FBIL rate.
5. RBI National Summary Data identifies 10-Year G-Sec Par Yield (FBIL). CCIL's daily tenorwise page is indicative and explicitly restricts commercial use without written permission. Treat CCIL as a validation/reference surface only until rights are cleared.
6. NSE's daily FPI/DII activity is provisional, can change through custodial confirmation/modifications, and includes separate NSE-only and combined exchange figures. Preserve the exact scope and status; never merge them into one series. NSDL is the final/custodian-confirmed route, but its current freshness must be rechecked at every collection.
7. PPAC publishes the Indian Basket crude series with historical/current reports. The exact daily/monthly frequency and publication timestamp need inspection before using it in H+1 event alignment.
8. Cboe describes VIX historical closing data as daily and updated daily; its own page also disclaims guaranteed accuracy. Preserve source metadata and do not use a single VIX observation as a causal explanation.
9. Federal Reserve broad trade-weighted USD series are available daily via FRED. They are not the ICE U.S. Dollar Index (DXY). If exact DXY is ever required, a separate licensing/source-rights gate is mandatory.
10. U.S. Treasury CMT rates are interpolated from a par yield curve using indicative bid-side quotations from the Federal Reserve Bank of New York around 3:30 PM ET. Record U.S. timezone and publication/observation timestamp; do not treat them as Indian-session closing yields.
11. FOMC meeting calendars provide statements, minutes and implementation notes. Policy decisions are event observations; do not fill non-meeting dates with invented decision events.
12. World Bank Pink Sheet historical commodity data are monthly. They support monthly regime/context variables, not daily trigger timing.

## 4. Time alignment and panel contract
- Canonical India session key: NSE trading date, Asia/Kolkata.
- Every foreign observation must retain original source timezone, source observation timestamp, source publication timestamp, retrieval timestamp, reference date/period and revision/vintage metadata.
- For overnight foreign market closes, store both source-local date/time and the first eligible Indian session after publication. H+0 means the first Indian session that could actually react after public release; do not map a post-close release to an already completed Indian session.
- Keep observation time separate from publication time. Example: FBIL USD/INR reference rate is based on the 11:30–12:30 IST window; U.S. Treasury close is around 3:30 PM ET; these cannot be aligned merely by matching calendar dates.
- Do not forward-fill across Indian holidays, foreign holidays, stale/missing values or source outages. Keep explicit missingness and source freshness flags.
- Daily market prices, monthly macro data and event timestamps must remain separate frequency classes. Only use as-of joins with the exact release time; never expand monthly values into fake daily observations.
- Preserve both NIFTY price return and NIFTY TRI; preserve index methodology/version and constituent/sector taxonomy versions where available.
- Each downloaded object must be archived byte-for-byte with official URL, publisher, retrieved_at_UTC, source publication time, MIME/content length, SHA-256 and parser/schema version before parsing.

## 5. Freshness and rights gates
- NSE index CSV route: locator verified; actual historical range/CSV bytes and refresh schedule not yet verified in this task.
- NSE FPI/DII: provisional daily page observed with an example date 21-Aug-2026; do not assume current freshness. At ingestion, require report date and updated-at field to match the requested session.
- NSDL FPI: report families discovered; inspected latest example was dated 30-Oct-2025, so current freshness is NOT_VERIFIED.
- FBIL: methodology and archive surface discovered; repeatable daily USD/INR archive export not yet captured.
- PPAC: report download surfaces found; exact report frequency and raw data extraction not yet audited.
- BSE: SENSEX EOD history/data product rights remain a hard gate for free automated ingestion.
- CCIL: public indicative yield display exists, but commercial-use restriction must be respected.
- No source is declared fully ingested or hash-verified in this Part 1.

## 6. Acceptance matrix
| Gate | Status |
|---|---|
| India Market Transmission priority layer reopened | PASS |
| NIFTY / NSE sector / India VIX official locator | PASS |
| BSE SENSEX free-use rights | BLOCKED |
| FBIL USD/INR methodology | PASS |
| FBIL daily historical raw archive | NOT_CAPTURED |
| RBI 10Y G-Sec reference locator | PASS |
| CCIL indicative yield rights boundary | PASS (restriction recorded) |
| NSE FPI/DII provisional source and caveat | PASS |
| NSDL final FPI current freshness | NOT_VERIFIED |
| PPAC Indian Basket source locator | PASS |
| CBOE VIX daily history locator | PASS |
| Fed broad USD proxy locator | PASS (not DXY) |
| U.S. Treasury 2Y/10Y source and methodology | PASS |
| FOMC policy-event source | PASS |
| World Bank monthly commodity source | PASS |
| Raw-byte archive / SHA-256 manifest | NOT_DONE |
| Synchronized India benchmark panel | NOT_DONE |
| Event-study / causal validation | NOT_DONE |
| Production use | NOT_AUTHORIZED |

## 7. Next exact action
1. Build the first raw-source capture in a short, isolated workflow for only the freely accessible NSE historical NIFTY 50, NSE sector-index sample, and India VIX CSV surfaces; record actual returned date range, schema, bytes, SHA-256 and duplicate-date checks.
2. In a separate short workflow, capture public U.S. Treasury 2Y/10Y CSV, FRED broad USD and DEXINUS observations, Cboe VIX historical file and World Bank monthly Pink Sheet. Keep each native frequency and timestamp.
3. Separately audit FBIL public reference-rate export and PPAC report granularity; do not infer an API or scrape a protected feed.
4. Keep FPI provisional/final streams separate and establish a current-date NSDL/eligible CDSL retrieval route before admitting flow observations.
5. Keep BSE SENSEX out of the free automated panel unless the exact licence/permission allows the intended research/archive use.
6. Only after raw source hashes and timezone/revision QA pass, assemble a synchronized panel; then proceed to Tier-0 USA event-source capture and China/Japan/EU source coverage.

## 8. Protected invariants
No paid API/subscription, no synthetic data, no fabricated timestamps, no forward-fill, no unverified current value, no silent frequency conversion, no silent DXY substitution, no rights bypass, no new country impact weights. Do not alter the fixed 63-country IMF cohort, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, trade gates or alert behavior. UNKNOWN is never PASS.
