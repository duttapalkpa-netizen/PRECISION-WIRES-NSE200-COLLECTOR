# FII/DII Raw API Capture — Bounded Access Attempt & Acceptance Gate

Date: 2026-11-16  
Status: **BLOCKED — exact raw API response not obtained through available retrieval channel**  
Scope: read-only access test and reproducible next-step contract. No production changes.

## 1. Objective
Resolve whether the collector endpoint `https://www.nseindia.com/api/fiidiiTradeReact` returns NSE-only FII/DII activity or the combined NSE+BSE+MSEI dataset, by capturing the exact raw response for a known date and reconciling it with the two official report tables.

## 2. Evidence already available (reused; not repeated)
- Collector source at Run #161 head: `collector/context_data.py`, blob SHA `f38e17979774d1439eea79e4dc7728ba92a790d1`.
- Run #161 / run ID `43696699698`; artifact ID `14154408713`.
- Archived normalized context member SHA-256: `83c811be558501bbfed7b2104658f2d3796bfd506b37149800a730384bed5dc8`.
- For 13-Nov-2026, archived values match the official NSE page's combined NSE+BSE+MSEI table values, not the separate NSE-only table values. This is a one-date reconciliation only.
- Official NSE report page: https://www.nseindia.in/reports/fii-dii . The rendered page clearly labels two separate datasets and two CSV download controls (page sections “FII/FPI & DII trading activity on NSE in Capital Market Segment” and “... on NSE, BSE and MSEI in Capital Market Segment”).
- Direct retrieval attempt for `https://www.nseindia.com/api/fiidiiTradeReact` via the available web retrieval channel returned an inaccessible/internal-error response. Clicking the rendered page's generic download control did not expose a distinct CSV URL or file payload; the page extraction represented both download controls with the same generic link reference.
- No raw JSON response body, HTTP response headers, resolved API URL, or endpoint documentation was obtained in this attempt.

## 3. What is and is not established
Established:
1. Collector code requests `/api/fiidiiTradeReact` and normalizes category/date/buy/sell/net values.
2. The official NSE report page distinguishes NSE-only and combined exchange tables.
3. Run #161's single-date values match the combined table for 13-Nov-2026.

Not established:
1. The API's authoritative market scope.
2. Whether the API endpoint behavior or payload schema changes by date/session.
3. Whether the normalized Run #161 artifact came from the same table selection or another server-side aggregation.
4. Any rolling-window aggregation or CORE-672 signal policy.

## 4. Safe raw-capture acceptance contract
A valid future capture must preserve, without normalization loss:
- exact request URL and query parameters;
- request date/time and timezone;
- response status code and response headers (redact cookies/session secrets);
- exact raw response bytes and SHA-256;
- parsed JSON body as a separate derived file, also hashed;
- source page/table scope used for comparison;
- official report CSV bytes and SHA-256 for NSE-only and combined datasets, with their date rows;
- deterministic row-level comparison by date, category, buy, sell and net values.

Do not store cookies, authentication tokens, session IDs or personal data in the repository. Never commit secrets. If NSE requires an interactive session, use the existing collector's runtime only with a redacted capture mode and explicit user authorization before changing its workflow/code. Prefer a one-off research-only capture script over changing the production collector.

## 5. Next safe action
Use a short, isolated, manually triggered research-only capture in a non-production branch/environment, with:
1. NSE website session bootstrap using the existing public-site request pattern;
2. one GET to the exact API endpoint;
3. response metadata and raw body archived with secrets removed from metadata;
4. same-date official CSV downloads from both distinct report controls;
5. exact comparison and hashes.

If the response remains inaccessible or the official controls do not expose their URLs, stop and record ACCESS_BLOCKED; do not reverse-engineer undocumented endpoints by guesswork or infer scope from matching one date.

## 6. Progress
- Official report page/table labels reconfirmed: 100%.
- Direct API retrieval attempt: 100% attempted; ACCESS_BLOCKED.
- Raw response bytes/hash: 0% / NOT_OBTAINED.
- Official NSE-only and combined CSV payload hashes: 0% / NOT_OBTAINED.
- API-to-table scope reconciliation: BLOCKED.
- CORE-672 aggregation policy: BLOCKED.
- Trading-state adapter: 0% / NOT_AUTHORIZED.

No production code, collector, workflow, dataset, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 56×12 contract, engines A–E, default branch or PR state changed. No CI run, no PR merge, no paid API/spend.
