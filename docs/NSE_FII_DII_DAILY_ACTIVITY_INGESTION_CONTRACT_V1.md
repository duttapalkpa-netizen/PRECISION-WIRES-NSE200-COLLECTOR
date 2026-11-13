# NSE FII/FPI & DII Daily Activity — Research Ingestion Contract V1

Audit date: 2026-11-12 (Asia/Kolkata)
Status: SOURCE_PAGE_VERIFIED / RAW_INGESTION_NOT_DONE
Scope: Global Capital Rotation research overlay only; no production integration.

## 1. Primary source

Official NSE report page:
- https://www.nseindia.com/reports/fii-dii

The page publishes two distinct Capital Market Segment views and CSV download controls:
1. NSE-only.
2. Combined NSE + BSE + MSEI.

Keep these as separate source series. For a cross-exchange domestic institutional activity proxy, the combined series is the candidate; the NSE-only series is an exchange-specific cross-check. Do not splice, average, or silently switch between them.

NSE describes the combined FII/FPI and DII activity as collated from trades executed across the exchanges. The page states that FII/FPI activity is based on PANs provided by NSDL and that the trade data is provisional and subject to custodial confirmation/modifications. It separately states that DII activity is compiled from trading codes entered by Trading Members and the corresponding client-category classification supplied by Trading Members. Therefore:
- Treat this as exchange-reported trading activity, not a depository-confirmed DII holdings/flow series.
- Preserve the NSE provisional status label for the report snapshot.
- Do not merge DII with NSDL/CDSL FPI data or relabel exchange DII as final custodian-confirmed flow.
- Do not interpret DII net buying as a unique beneficial-owner net subscription measure.

## 2. Candidate raw schema

Retain the downloaded source bytes unchanged. Parse into a normalized table with at least:
- source_scope: `NSE_ONLY` or `COMBINED_NSE_BSE_MSEI`
- segment: `CAPITAL_MARKET`
- report_date: source-reported trading date, parsed without timezone conversion
- category: source label, e.g. `DII` or `FII/FPI`
- buy_value_inr_cr: source-reported buy value
- sell_value_inr_cr: source-reported sell value
- net_value_inr_cr: source-reported net value
- source_url: exact final CSV URL, not merely the landing page
- landing_page_url: official NSE report page
- retrieved_at_ist: actual retrieval timestamp with +05:30 offset
- source_status: `PROVISIONAL` where the NSE report caveat applies
- raw_sha256, raw_bytes, parser_version

Never manufacture a final CSV URL from the page URL or from a third-party scraper. If the download control's href is not exposed, leave exact final URL UNKNOWN until a real browser download or an independently documented official export route supplies it.

## 3. Ingestion and QA acceptance

A raw-ingestion PASS requires all of the following:
1. Actual bytes obtained from the official NSE download action or a documented official NSE export route.
2. Exact final URL, retrieval timestamp (IST), byte count, SHA-256, and immutable raw archive.
3. CSV encoding, delimiter, header, and row schema recorded from the actual file.
4. Only expected categories and segment retained; no accidental derivatives/other segment rows.
5. Report dates parsed strictly; invalid dates rejected, not coerced.
6. Duplicate key check on (source_scope, segment, report_date, category).
7. Buy/sell/net numeric parsing with explicit units; verify net = buy - sell within source rounding tolerance, otherwise quarantine the row and record the discrepancy.
8. Missing trading dates assessed against the official NSE trading calendar; exchange holidays are not treated as missing observations.
9. NSE-only and combined files independently hashed and validated.
10. Raw bytes and parsed outputs linked by manifest; no overwrite of earlier vintages.

A displayed sample row, search snippet, third-party mirror, or scraper repository is not raw ingestion evidence.

## 4. Known limitations and failure-avoidance record

- The official NSE page text extraction shows two CSV controls but does not expose their actual hrefs in the available link map; clicking the generic extracted link returns the landing page. This is an extraction limitation, not evidence that the NSE download control itself is broken.
- A direct network attempt from the current execution environment failed DNS resolution for www.nseindia.com before an HTTP response. This does not prove NSE endpoint failure.
- `https://www.nseindia.com/api/fiidiiTradeReact` was observed in third-party scraper code only. It is NOT an officially documented/verified endpoint in this audit. Do not use it as an official source until independently corroborated by NSE-owned page JavaScript/network contract or official documentation.
- Do not repeat the same generic-link click or the same blocked direct-network attempt. Next acceptable acquisition path: use the actual NSE page download control in a browser-capable session, or establish a separately documented official NSE export route.
- No raw DII observations, retrieval timestamp, file size, or DII CSV SHA-256 have been obtained as of this audit.

## 5. Current acceptance state

| Gate | State |
|---|---|
| Official landing page and two series identified | PASS |
| Source semantics and DII classification caveat recorded | PASS |
| Exact CSV download URL | UNKNOWN |
| Raw CSV bytes and SHA-256 | NOT DONE |
| Parsed historical DII panel | NOT DONE |
| Calendar, duplicate, arithmetic and schema QA | NOT DONE |
| Matched DII/FPI/market panel | NOT DONE |
| Predictive/event-study validation | NOT DONE |
| Production use | NOT AUTHORIZED |

Research-only. This contract does not modify the Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, Engine A–E, or any hard gate.
