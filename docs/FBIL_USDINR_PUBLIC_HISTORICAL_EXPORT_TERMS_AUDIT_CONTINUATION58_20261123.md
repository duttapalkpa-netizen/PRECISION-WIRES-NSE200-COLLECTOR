# FBIL USD/INR Public Historical Export and Terms Audit — Continuation 58
Date: 2026-11-23 (Asia/Kolkata)
Project: PRECISION-WIRES V11.3 / Macro-Geo P0

## 1. Continuity preflight and duplicate prevention
- Re-read Library Mother File through Continuation 57 and GitHub Master Continuity Ledger through Continuation 57 before selecting work.
- Skipped accepted Run #398 NSE 200-session raw archive/provenance/QA, canonical panel rebuild, archive schema regression, source-coverage fail-closed regression and Macro-Geo artifact #14765264055 SHA acceptance.
- Existing status remains P0 6/8; strict Hard Gate BLOCKED; candidate_release_allowed=false. No workflow rerun or production change.

## 2. Official FBIL surfaces inspected
1. Official production site: https://www.fbil.org.in/
   - Search-indexed page exposes a benchmark table labelled INR / 1 USD with observation dates and rates (examples displayed for 05-Nov-2026 and 06-Nov-2026 at 4:00 PM, and a different Reference Rate table with 16-Oct-2026 at 1:00 PM).
   - This is evidence that recent benchmark observations are publicly rendered, not evidence of a complete historical daily archive. The searchable page did not expose a stable date-bounded USD/INR export endpoint, API documentation, response schema or downloadable raw payload.
2. Distinct FBIL UAT frontend: https://uatfrontend.fbil.org.in/
   - Search-indexed page explicitly says “Please enter your details to download the data” and exposes “Download Excel csv” and “Download CSV” controls.
   - It also shows Reference Rate trend controls for 3, 6 and 12 months.
   - This is a data-download interface requiring details; it is not a documented public API. The available rendered inspection did not reveal the exact form fields, export URL, request method/parameters, whether download is anonymous or account/consent-gated, historical date-range limits, response bytes, schema, or permission to automate/store the downloaded data.
   - Do not submit personal details, create an account, reverse-engineer client code/postbacks, or infer a download endpoint. No form was submitted and no file was downloaded.
3. FBIL Terms of Use / Subscription Disclaimer:
   - The production site search rendering lists “TERMS OF USE AND SUBSCRIPTION DISCLAIMER FOR FBIL BENCHMARKS” under What’s New.
   - The exact linked document and its clauses could not be retrieved in this inspection. Therefore automated archival/republication/internal machine storage rights remain NOT_VERIFIED; do not assume public visibility grants those rights.

## 3. Methodology boundary
- Official FBIL methodology document: https://www.fbil.org.in/uploads/Methodology_Document_on_Reference_Rate_Dated_11th_June2018_Version1_6db1a143aa.pdf
- USD/INR Reference Rate is based on actual spot USD/INR transactions during a one-hour Mumbai business-day window from 11:30 to 12:30; a randomly selected 15-minute period is used, subject to transaction thresholds and outlier handling. Publication is around 13:30 on Mumbai business days, excluding weekends and Mumbai bank holidays.
- This series is a benchmark reference rate, not interbank OHLC, DXY, or a cross-currency carry series. Preserve benchmark identity and publication/observation semantics.

## 4. Evidence and decision
- Official source identity and methodology: CONFIRMED.
- Recent public daily values: DISCOVERED in search-indexed production page; not captured as immutable raw bytes.
- UAT CSV/Excel download controls: DISCOVERED; personal-details gate indicated.
- Documented public API / exact export request contract: NOT_FOUND in inspected official materials.
- Terms permitting automated internal archival: NOT_VERIFIED; terms document link surfaced but clauses not retrieved.
- Historical raw daily coverage >=60 distinct dates over >=90 calendar days: NOT_CAPTURED.
- No raw payload, response metadata, retrieval timestamp, or SHA-256 exists from this audit.
- USD/INR source remains BLOCKED / UNKNOWN. Do not promote P0 coverage or Hard Gate.
- No ingestion, collector mapping, fixture, source-coverage, selector, ranking, pressure-fade, CORE-672, Engines A–E or IPO-PLX changes.

## 5. Rejected / excluded approaches
- No paid data, paid API, subscription, or third-party mirror.
- No personal details submitted or account created.
- No guessed API URL, endpoint probing, browser-script/postback reverse engineering, or automated form bypass.
- No manual copying of isolated displayed rates into the historical archive.
- No substitution of monthly newsletter averages for daily observations.
- No mapping of FBIL reference rate into OHLC, DXY, or cross-currency carry.

## 6. Exact next action
1. Continue only through a documented public download route with terms that explicitly permit the intended automated internal archival, or an official written permission/licence already available without paid spend or external contact.
2. If no such permission/documented route is available, keep USD/INR BLOCKED/UNKNOWN and proceed to the next independent permitted task: inspect NSE CSV endpoint and its terms solely for a separately labelled PROVISIONAL EXCHANGE TRADING ACTIVITY series; it cannot close final FPI.
3. Keep NSDL archive blocked pending written permission; no reverse engineering. Retry CDSL only when its official archive route is functional and terms are verified.
4. Only after permitted raw bytes are obtained, validate schema, date semantics, units, byte count, SHA-256 and >=60 dates / >=90-day span before any collector mapping or coverage promotion.

## 7. Invariants
₹0; official/free sources only; no synthetic data or fabricated timestamps; UNKNOWN never PASS; H+3 State threshold >=50 fully matured observations; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX unchanged; no merge or production integration.
