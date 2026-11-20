# NSE MCP / SEBI market-data use gate — 20 November 2026
Page: গবেষণা যাচাই অব্যাহত 41, Part 1

## Objective
Determine whether NSE's newly documented free MCP service can legitimately and technically replace the missing V11.3 live 1-minute feed, and prevent accidental promotion of a research-only data source into a trading selector.

## Primary-source facts
1. NSE's official NSE MCP page states:
   - Bhavcopy service: prior trading day's final EOD numbers, with up to five years of history.
   - CM Market service: current market prices approximately 1–3 minutes behind real time.
   - No tick-by-tick or order-book data.
   - Intended for information and learning, not real-time trading, investment advice, or commercial products.
   - MCP access does not grant a license/right/permission to commercially exploit the data or train/fine-tune AI systems.
   - Endpoints shown by NSE: `https://mcp.nseindia.in/bhavcopy/cm/mcp` and `https://mcp.nseindia.in/cmmkt/mcp`.
2. SEBI Circular HO/47/17/12(11)2025-MRD-POD3/I/11107/2026 dated 08-May-2026 states that the time lag for both sharing and usage of market-price data for investor education and awareness activities is 30 days (with a specific one-day exception for NISM's simulation lab). The circular explains that the earlier one-day and three-month provisions are replaced by 30 days for those educational/awareness activities.
3. NSE's data-sharing policy says subscribers access market data through an order/contract process; commercial market data is priced. NSE's real-time data page lists 1-minute/5-minute snapshots and real-time feeds as formal data products, distinct from the MCP's 1–3 minute snapshot service.

## Interpretation boundary
The SEBI circular's application to the NSE MCP's particular terms and to a private, non-commercial research workflow is a legal/data-rights question; this technical audit does not issue a legal opinion. Because NSE labels the MCP data as informational/learning and the circular regulates sharing/usage for educational/awareness purposes, we must not assume that 1–3 minute MCP data is automatically permissible for a private trading-selection pipeline. Written NSE permission/terms or qualified legal clarification is required before ingesting it into PRECISION-WIRES selection, model training, backtests, or alerts.

## Acceptance gate
| Proposed use | Decision | Reason |
|---|---|---|
| Replace missing live 1-minute feed | REJECTED | MCP is not a 1-minute candle feed; NSE says no tick/order-book data |
| Production selector / ranking / ignition confirmation | BLOCKED | NSE's stated information/learning purpose does not establish trading-use permission |
| Backtest/model training using near-real-time MCP data | BLOCKED | NSE explicitly disclaims permission to train/fine-tune AI systems; SEBI educational-use lag applicability needs clarification |
| Research/learning display | CONDITIONAL / NOT AUTHORIZED YET | Must first establish terms and applicable SEBI delay/usage conditions; no assumed exemption |
| Official historical EOD data | SEPARATE REVIEW | Prior-day Bhavcopy history may be used only within applicable NSE terms and data rights; no commercial redistribution or model-training rights assumed |

## Consequence for stock selection
- The NSE MCP discovery does not resolve Run #407's `LIVE_INTRADAY_1M_FEED_MISSING` blocker.
- Do not integrate the MCP endpoint into `collector/live_1m.py`, the V11.3 selector, any engine, or the backtest pipeline.
- Keep live feed status BLOCKED and today's actionable qualified-candidate count at 0 unless a separate, properly authorized feed and all selection gates pass.
- No stock is designated reliable/A+ merely because a delayed or informational snapshot exists.

## Next permissible task
Maintain a source-permission register for every candidate data source (official owner, source endpoint, allowed purpose, delay, retention, redistribution, model-training rights, authentication, and written permission evidence). This is a documentation/acceptance gate only; it must not alter production selection logic.

## Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2 unchanged. No paid APIs, no synthetic data, no access-control bypass. UNKNOWN is never PASS.

## Sources
- NSE MCP: https://www.nseindia.com/nse-mcp
- SEBI Circular, 08-May-2026: https://www.sebi.gov.in/legal/circulars/may-2026/norms-for-sharing-and-usage-of-price-data-for-educational-purposes_101293.html
- SEBI circular PDF: https://www.sebi.gov.in/sebi_data/attachdocs/may-2026/1778242522289.pdf
- NSE Data Sharing & Usage Policy: https://www.nseindia.in/static/market-data/nse-data-policy
- NSE real-time data products: https://www.nse.in/static/market-data/real-time-data-subscription
