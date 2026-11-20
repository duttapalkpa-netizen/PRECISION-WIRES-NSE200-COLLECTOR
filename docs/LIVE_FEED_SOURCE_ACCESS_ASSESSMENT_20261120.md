# Live-feed source-access assessment — 20 November 2026

## Question
Can the Run #407 / Run #338 live intraday gate be satisfied using a free, official, permitted source without bypassing NSE access controls or using a paid API?

## Findings from official exchange documentation
1. NSE's official NSE MCP page describes a no-account/no-API-key connection with 35+ tools and 1–3 minute delayed intraday data. It lists bulk quotes for up to 50 stocks and live market tools. The same page explicitly says the data is for information and learning and is not meant for real-time trading, investment advice, or commercial products. It is therefore useful for research/context and a possible delayed-data shadow monitor, but it does not qualify as a substitute for the current live 1-minute ignition/confirmation gate.
2. NSE's official real-time data page describes Level 1/2/3/tick feeds, real-time stock-wise feeds, and 1-minute/5-minute snapshot data as products distributed through NSE Data & Analytics. The page identifies dedicated leased-line or authorized-vendor delivery for real-time feeds and SFTP/binary delivery for snapshot feeds. The page also lists 15-minute delayed snapshot data as a separate product. No free downloadable official 1-minute feed for unrestricted trading use was established by this review.
3. NSE's Data Sharing & Usage Policy says subscribers access market data through an order/contract process and that commercial market data is priced. This reinforces that a blocked public web endpoint should not be treated as an entitlement to scrape an exchange feed.

## Existing collector diagnosis
The current collector source `collector/live_1m.py` requests NSE `quote-equity` and `chart-databyindex`. It stops after a 403 quote response and writes `BLOCKED_SOURCE_ACCESS_403`, zero rows. This is correct fail-closed behavior. Do not retry aggressively, rotate identities, evade access controls, or fabricate rows. The final selector correctly blocks when the intraday file/status is missing or invalid.

## Decision
- Keep `LIVE_INTRADAY_1M_FEED_MISSING` BLOCKED.
- Do not treat the 1–3 minute delayed NSE MCP data as a live trading confirmation feed. It may be considered for a separately labeled research-only shadow/context layer after an authorized connector is available and freshness is validated.
- Do not use the paid NSE 1-minute snapshot or paid real-time data products under the user's no-paid-data constraint.
- No stock is promoted to A+/reliable/actionable from the 19-Nov archive or stale provisional shortlist. The 20-Nov Daily Unified Top-5 audit already recorded zero qualified candidates.

## Next permissible work
1. If an authorized NSE MCP connector becomes available in the user's ChatGPT environment, validate its official tool schema, symbol coverage, returned timestamps, delay, market status, and 50-symbol bulk-quote consistency; keep it shadow-only.
2. For the production 1-minute gate, require a genuinely authorized 1-minute source. If none is available within the no-paid constraint, preserve the BLOCKED gate and issue no actionable alert rather than weakening the acceptance criteria.

## Sources
- NSE MCP: https://www.nseindia.in/nse-mcp (official page: free/no API key, 1–3 minute delay, information/learning use only)
- NSE real-time data products: https://www.nse.in/static/market-data/real-time-data-subscription
- NSE Data Sharing & Usage Policy: https://www.nseindia.in/static/market-data/nse-data-policy

## Invariants
No production selector/ranking/pressure-fade/CORE-672/engine changes. No paid API, no synthetic data, no access-control bypass. UNKNOWN is never PASS.
