# NSE FII/FPI-DII Official CSV Basket and Usage Boundary — Continuation 60
Date: 2026-11-23 (Asia/Kolkata)
Project: PRECISION-WIRES V11.3 / Macro-Geo P0

## 1. Continuity and duplicate prevention
- Continued from Mother File Continuation 57 and GitHub Continuations 58–59.
- Skipped accepted NSE 200-session raw archive, provenance/QA, canonical panel, source-coverage regression and Run #45050554515 artifact acceptance.
- Skipped repeating CDSL archive capture/freshness work: Continuation 78 already proved the retained CDSL archive response was a stale static snapshot through 02-Mar-2026 with no date controls in captured HTML; Continuations 72–78 preserve raw captures and bounded arithmetic checks.
- No CDSL request, NSDL form submission, Macro-Geo workflow rerun or production change in this continuation.

## 2. Official NSE page observation
- Official page: https://www.nseindia.com/reports/fii-dii (redirects to https://www.nseindia.in/reports/fii-dii).
- Rendered page exposes two separate CSV controls:
  1. “FII/FPI & DII trading activity on NSE in Capital Market Segment”.
  2. “FII/FPI & DII trading activity on NSE, BSE and MSEI in Capital Market Segment”.
- The previously inspected table schema is Category, Date, Buy Value (₹ Crores), Sell Value (₹ Crores), Net Value (₹ Crores).
- Rendered web inspection does not expose the actual CSV target URLs, request parameters, HTTP response, or raw CSV bytes. No download was initiated and no endpoint was guessed.

## 3. Official NSE policy classification — material clarification
- NSE “Data List Under The NSE Data Sharing Policy For Research And Analysis”, dated 28-Jul-2025:
  - Lines 4–5 define the first basket as freely available research data (with voluminous datasets treated separately).
  - Lines 50–52 explicitly list “FII/FPI and DII trading activity” at https://www.nseindia.com/reports/fii-dii within the First Basket.
  - Lines 230–240 separately classify “FII/FPI and DII trading activity on NSE, BSE and MSEI (Capital Market segment)” under “First Basket (Voluminous data; >2GB; Chargeable)”.
- NSE Data Sharing & Usage Policy page, updated 11-Dec-2025, says use, handling, transmission and dissemination are governed by relevant agreements; research requests are routed through Economic Policy Research; underlying documentation defines non-commercial/research use restrictions; redistribution is restricted except as agreed.
- Decision: the NSE-only CSV is the eligible zero-cost research candidate for further verification. The combined NSE+BSE+MSEI voluminous dataset is excluded under the ₹0 constraint. The first-basket listing does not by itself prove an unrestricted right to bulk automated archival or redistribution.

## 4. Data-definition boundary
- NSE FII/FPI values are exchange trading-activity data, not final depository-confirmed FPI investment flows.
- NSE's own page states FII/FPI data are provisional and subject to custodial confirmation/modification and directs users to NSDL/CDSL for final FPI.
- Keep the NSE-only CSV as a separately named PROVISIONAL_EXCHANGE_TRADING_ACTIVITY series. Never substitute it for final FPI investment flow or NSDL DII history.

## 5. Acceptance matrix
| Gate | Status | Evidence |
|---|---|---|
| Official NSE page and two separate CSV controls | PASS | Rendered official page |
| NSE-only FII/FPI-DII research-basket classification | PASS | 28-Jul-2025 official NSE data list |
| Combined NSE/BSE/MSEI chargeable classification | PASS | Same official NSE data list, >2GB |
| General policy/redistribution boundary identified | PASS | NSE policy updated 11-Dec-2025 |
| Exact NSE-only CSV href/request contract | NOT_VERIFIED | Rendered page did not expose target |
| Raw CSV bytes, response metadata and SHA-256 | NOT_CAPTURED | No download performed |
| Historical >=60 distinct dates / >=90 calendar days | UNKNOWN | No raw archive evidence |
| Final FPI / NSDL DII acceptance | BLOCKED | NSE series is provisional exchange activity |
| Macro-Geo P0 / strict Hard Gate | BLOCKED | No new data accepted; remains 6/8 |

## 6. Exact next action
- Use only the visible official NSE-only “Download (.csv)” control through an auditable standard browser/runner; capture the exact final URL, request method, response status, content type, retrieval UTC/IST, report date, byte count, raw bytes and SHA-256.
- Do not inspect hidden scripts, replay undocumented requests, bypass controls or use the combined chargeable dataset.
- Verify schema, date uniqueness, category, units, arithmetic and whether the official public CSV itself supplies a dated historical series. Require >=60 valid dates spanning >=90 calendar days before any source-coverage promotion.
- If the visible download is only a one-day snapshot, retain it as a daily provisional observation only; it does not satisfy historical P0 coverage.
- Only after permitted raw data are captured should a bounded parser/fixture and coverage regression be considered. Do not rerun event study or Hard Gate before upstream source coverage is satisfied.

## 7. Protected invariants
₹0; official/free sources only; no synthetic data, guessed endpoints, fabricated timestamps or proxy substitution; UNKNOWN never PASS; >=50 fully matured H+3 observations per State; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2.0 unchanged; no merge or production integration.
