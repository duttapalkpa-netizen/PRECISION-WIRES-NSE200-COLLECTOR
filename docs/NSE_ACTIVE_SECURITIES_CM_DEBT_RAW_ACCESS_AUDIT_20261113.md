# NSE Active Securities CM and Debt — Raw Access Audit
Date: 2026-11-13 (Asia/Kolkata)
Research page: গবেষণা যাচাই অব্যাহত 25
Repository: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Status: SOURCE_DISCOVERY_PASS / RAW_ACQUISITION_BLOCKED

## Scope
Continue Section 27 without repeating completed source discovery. Determine whether the official combined NSE active-securities CSV can be retrieved and whether raw-byte validation can begin.

## Official source evidence
- Official NSE page: https://www.nseindia.com/static/market-data/securities-available-for-trading
- Page title: Securities available for Trading.
- Listed resource: "List of Active Securities CM And Debt (.csv)".
- NSE page displayed size: 373 KB.
- NSE page displayed update date: 09/11/2026.
- The link target was resolved from the official page:
  https://nsearchives.nseindia.com/content/equities/List_of_Active_Securities_CM_DEBT.csv
- NSE alternate page also lists the same resource:
  https://betanseapi.nseindia.com/static/market-data/securities-available-for-trading

## Retrieval attempts and outcome
1. Official page link retrieval was attempted through the browser retrieval path. The resource request returned HTTP 400 with the retrieval layer reporting "Unsupported content-type: text/csv".
2. A direct container download attempt failed.
3. Direct container HTTP requests to the archive host, main NSE host, alternate NSE host, and HTTP archive URL could not resolve DNS in the execution environment. This is an execution-environment network limitation and is not evidence that NSE returned an HTTP status for those attempts.
4. No raw CSV bytes were obtained in this audit.

## Evidence status (fail-closed)
| Item | Status | Evidence |
|---|---|---|
| Official source discovery | PASS | Official NSE page and named resource verified |
| Source update date | PASS | NSE page displays 09/11/2026 |
| Displayed file size | PASS | NSE page displays 373 KB |
| Exact CSV URL | PASS | Link target resolved |
| Raw download | BLOCKED | No bytes retrieved |
| Raw SHA-256 | UNKNOWN | Cannot hash unavailable bytes |
| Encoding / delimiter / schema | UNKNOWN | No raw bytes |
| Header and row count | UNKNOWN | No raw bytes |
| ISIN uniqueness / coverage | UNKNOWN | No raw bytes |
| Issuer–industry bridge | UNKNOWN | No raw bytes |

## Non-substitution rule
The official NSE page separately lists Equity-segment CSV and Debt Instruments CSV resources. These are separate datasets and must not be silently concatenated or represented as the combined "List of Active Securities CM And Debt" file. No reconstructed or synthetic combined rows are permitted. A separate source may be evaluated only under a separately named source contract with explicit lineage and scope.

## Prior evidence retained
- Section 27 Continuity Ledger commit: c43635e8bf20e9d40beee4f89c586acdb1b35d8b
- Continuity Ledger blob: 81504a3af96d7eccb8c8becaf8effd6f3615dd11
- Section 27 Source Register commit: 3d58770f1e30ca21cad03885b4342f20a6281010
- Source Register blob: f9d2b262faf35e4afdc3d752d14a4b824dc9dcbd

## Page 25 completion and next action
- This bounded source-access recheck and failure classification: 100% complete.
- Raw acquisition work package: 0% complete.
- SHA-256 work package: 0% complete.
- Schema / row-count QA: 0% complete.
- ISIN reconciliation: UNKNOWN.
- Issuer–industry bridge: UNKNOWN.
- Next action: obtain the exact official CSV bytes through an authorized retrieval path that preserves the original response bytes and headers; then hash the untouched file before parsing. Until then, keep the source blocked and do not promote it into a validated master.

## Project invariants
CORE-672 remains 56 Steps × 12 Filters. Production Selector, RANKING_SCORE and +1 PRESSURE_FADE remain unchanged. UNKNOWN is neither PASS nor FAIL. No synthetic data, fabricated timestamps, unsupported source promotion, paid API, spend, PR merge, or production integration is authorized by this audit. Overall project progress remains NOT_CALCULABLE until the complete acceptance ledger and weights are reconciled.
