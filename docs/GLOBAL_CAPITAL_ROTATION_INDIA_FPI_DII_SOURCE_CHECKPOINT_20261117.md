# CORRECTION — India FPI/DII Source Checkpoint
Date: 2026-11-17 (Asia/Kolkata)
Branch: research/global-capital-rotation-overlay-v1
Supersedes the unsupported 17-Nov CDSL figures in the earlier draft.

## Correction notice
Fresh official-source recheck shows CDSL's latest visible investment reporting date is 16-NOV-2026, not 17-NOV-2026. The earlier draft's 17-Nov values (+₹5,107.61 crore Equity; +₹2,436.14 crore FPI subtotal; +₹2,473.82 crore page total) are NOT VERIFIED and are withdrawn from accepted evidence.

## CDSL verified displayed observation
Official URL: https://www.cdslindia.com/eservices/publications/fiidaily
Visible reporting date: 16-NOV-2026.
Net investment (INR crore): Equity +5,564.90; Debt-General +389.47; Debt-VRR +51.60; Debt-FAR -1,163.67; Hybrid +3.63. FPI category subtotal +4,845.93. Mutual Funds, separately displayed, -18.74. Page Total +4,827.19.
Arithmetic: 5,564.90 + 389.47 + 51.60 - 1,163.67 + 3.63 = 4,845.93; adding MF -18.74 = page Total +4,827.19.
CDSL says figures are compiled from custodian reports received on 16-Nov and represent trades conducted on and up to previous trading day(s); reporting date is not intraday execution timestamp.

## NSE verified displayed observation
Official URL: https://www.nseindia.in/reports/fii-dii
Latest visible date: 13-NOV-2026.
NSE-only Capital Market Segment: DII buy ₹10,561.32 crore; sell ₹12,532.05 crore; net -₹1,970.73 crore. FII/FPI buy ₹17,376.50 crore; sell ₹12,122.52 crore; net +₹5,253.98 crore.
Combined NSE+BSE+MSEI Capital Market Segment: DII buy ₹11,745.95 crore; sell ₹13,999.53 crore; net -₹2,253.58 crore. FII/FPI buy ₹18,339.57 crore; sell ₹12,603.02 crore; net +₹5,736.55 crore.
NSE explicitly says these values are provisional and subject to custodial confirmation/modifications. DII classification is based on trading-member-entered codes and client-category classification. Keep both exchange scopes separate.

## Evidence boundary
- CDSL displayed-page arithmetic for 16-Nov: PASS (bounded display check).
- NSE displayed-table arithmetic for 13-Nov: PASS (bounded display check).
- CDSL raw response bytes, retrieval timestamp, byte count and SHA-256: NOT_DONE.
- NSE-only and combined CSV raw bytes, exact final download URLs, byte counts and SHA-256: NOT_DONE.
- Matched lag-aware daily panel: NOT_DONE.
- IMF BOP actual observation payload, country coverage and reproducible EM aggregate: NOT_DONE. IMF BOP is transaction data; PIP/CPIS is positions and cannot substitute.
- This checkpoint is not a full overlay gate and does not update overall percentage.

## Next bounded actions
1. Acquire official CDSL and NSE raw files via actual official download routes; record final URL, retrieved_at, byte count, SHA-256 and source publication/reporting date.
2. Parse each source separately; validate schema, categories, buy/sell/net arithmetic, duplicate dates and calendar.
3. Build matched panel distinguishing CDSL custodian-reported values, NSE provisional values and exchange scopes.
4. Acquire IMF BOP DSD/codelists and actual transaction observations; declare instrument, sign, currency, reporter coverage, country membership, weights and missingness before any EM aggregate.
5. Only then continue synchronized rates/FX/oil/volatility and India-vs-world relative-return analysis.

## Protected invariants
No change to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E or Hard Gate. Research-only; no stock score/ranking, buy/sell instruction, automatic trigger, PR merge or production integration. ₹0 spend; official/free sources only. Missing/stale data remains UNKNOWN; no synthetic observations or forward-fill.

## Official sources
- CDSL daily: https://www.cdslindia.com/eservices/publications/fiidaily
- NSE FII/DII: https://www.nseindia.in/reports/fii-dii
- IMF BOP: https://data.imf.org/Datasets/BOP
- IMF BOP DSD registry information: https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/
