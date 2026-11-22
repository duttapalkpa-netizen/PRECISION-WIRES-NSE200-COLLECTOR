# NSE FII/FPI-DII CSV Route and Usage Boundary — Continuation 59
Date: 2026-11-23 (Asia/Kolkata)
Project: PRECISION-WIRES V11.3 / Macro-Geo P0

## 1. Continuity preflight
- Read Mother File through C57, current Master Ledger after C58, C58 FBIL audit and official NSE source/policy pages.
- Skipped all accepted NSE raw archive, provenance, QA and regression work. No Macro-Geo workflow rerun. P0 remains 6/8; strict Hard Gate BLOCKED; candidate_release_allowed=false.

## 2. Official source and CSV affordance
- NSE FII/FPI & DII page: https://www.nseindia.com/reports/fii-dii (redirected during inspection to https://www.nseindia.in/reports/fii-dii?os=roku..).
- The page exposes two distinct “Download (.csv)” controls:
  (a) FII/FPI & DII trading activity on NSE in Capital Market Segment;
  (b) FII/FPI & DII trading activity on NSE, BSE and MSEI in Capital Market Segment.
- Each table has Category, Date, Buy Value (₹ Crores), Sell Value (₹ Crores), Net Value (₹ Crores). The current rendered example is one date only; this is not historical coverage proof.
- The page states the FII/FPI data are based on activity compiled from PANs provided by NSDL and are provisional, subject to custodial confirmation and modifications. It directs users to NSDL/CDSL for final FPI data.
- Keep these as distinct exchange trading-activity series; do not call them final depository FPI investment flows.

## 3. Usage / rights boundary
- NSE's 28-Jul-2025 “Data List Under The NSE Data Sharing Policy for Research and Analysis” classifies FII/FPI and DII trading activity at https://www.nseindia.com/reports/fii-dii within its first basket described as freely available research data.
- NSE's current Data Sharing & Usage Policy (page updated 11-Dec-2025) states that market-data use, transmission, handling and dissemination are governed by relevant agreements; subscribers may need an agreement specifying intended use and handling; redistribution is restricted except as agreed. It also states researcher/research-institution data requests are routed through Economic Policy Research and may follow approved pricing norms; non-commercial/research users' limitations are set in underlying documentation.
- The first-basket classification and general policy text do not by themselves establish an unconditional right for this project to automate bulk archival, retain raw CSVs in GitHub, or redistribute them. No specific CSV licence/terms for this use was verified.

## 4. Endpoint and capture result
- Search-indexed/rendered page confirms CSV controls but browser-readable page representation did not expose their actual download target URLs or request method/parameters.
- No CSV download was initiated; no raw bytes, schema file, response metadata, retrieval timestamp, or SHA-256 captured.
- Historical archive route surfaced as a historical-report landing page with a generic “Click here” link, not a date-bounded CSV export contract. No >=60-date / >=90-day coverage verified.
- Decision: source identity and data definition CONFIRMED; separate CSV download affordance DISCOVERED; exact endpoint/schema NOT_VERIFIED; project-specific automated archive rights NOT_VERIFIED; raw history NOT_CAPTURED.
- Candidate status: PROVISIONAL EXCHANGE TRADING ACTIVITY only; not accepted as final FPI; not yet accepted for automated ingestion. Final FPI/DII P0 remains BLOCKED/UNKNOWN.

## 5. Exclusions
- No scraping, reverse engineering, guessed endpoint, request replay, or browser-control bypass.
- No use of provisional NSE values as final NSDL/CDSL FPI.
- No paid data, subscription, or third-party mirror.
- No production collector, selector, ranking, pressure-fade, CORE-672, Engines A–E or IPO-PLX change.

## 6. Exact next action
- Keep NSE CSV candidate on hold until a documented public download URL/schema and the applicable usage terms for automated internal archival are explicit. If terms do not authorize it, do not capture/retain it.
- Continue with CDSL only if its official archive becomes functional and terms permit the intended use; keep NSDL blocked pending explicit permission.
- Do not rerun source coverage/event study/hard gate until permitted raw daily source data meet >=60 distinct valid dates over >=90 calendar days.
- Preserve ₹0, official sources only, UNKNOWN never PASS, and all frozen production invariants.
