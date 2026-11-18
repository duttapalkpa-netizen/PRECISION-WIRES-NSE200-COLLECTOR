# Brazil Reconstruction + Global Capital Rotation — Retrieval Boundary Checkpoint Part-37
Date: 2026-11-19
Branch: qa/imf-brazil-parser-schema-path-hardening
Scope: executable raw-data retrieval attempt after Part-36; no production changes.

## New official source contracts verified
- U.S. Treasury publishes a documented XML feed for daily nominal and real yield curves. Its official contract specifies GET requests, year-scoped retrieval, and all-years pagination (300 rows/page, zero-based page index). Nominal yield curve coverage begins 1990; real par yield curve begins 2003.
- Treasury's current daily rates page documents separate nominal and TIPS real curve views and CSV/XML access.
- RBI Reference Rate Archive provides currency/date filters and Excel export.
- IMF API documentation confirms SDMX 2.1 and 3.0 APIs; IMF SDMX Central exposes structure-query tooling.

## Raw retrieval attempts (this checkpoint)
1. Treasury nominal XML, 2026:
   https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
2. Treasury real XML, 2026:
   https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_real_yield_curve&field_tdr_date_value=2026
3. BCB SGS 22707 date-filtered JSON, Sep-2026:
   https://api.bcb.gov.br/dados/serie/bcdata.sgs.22707/dados?formato=json&dataInicial=01%2F09%2F2026&dataFinal=30%2F09%2F2026

- Browser fetch rejected Treasury XML as unsupported content-type text/xml; BCB JSON URL was inaccessible to browser fetch.
- Container HTTP attempts for all three failed before HTTP response with DNS resolution error (Temporary failure in name resolution).
- Therefore no response body, HTTP status, row count, or raw-byte SHA-256 was captured. This is a runtime network boundary, not evidence that official endpoints are invalid.
- No fabricated substitute data, cached secondary values, or estimated timestamps were inserted.

## Brazil acceptance
- Existing exact Brazil PA crosswalk remains verified in three uploaded IMF registry XML snapshots.
- Unresolved: live BCB XML payload bytes; authoritative BR1 transaction/PA changelog export; explicit BOP6 vs BOP_BPM6 mapping/history; recursive pinned SDMX 2.1 XSD closure and offline validation; exact SGS 22707 raw observations/hash.
- Status: INCOMPLETE / BLOCKED. No PASS promotion.

## Global Capital Rotation acceptance
- Treasury nominal/real XML feed contracts are now confirmed as machine-readable acquisition paths, with distinct series and historical coverage.
- Still not acquired: raw Treasury XML, RBI/FBIL historical exports, NSDL/CDSL flow archives, AMFI monthly flows/AUM, NSE VIX/index/TRI history, EIA Brent raw rows, World Bank commodity/freight series, DXY/carry and geopolitical-event evidence.
- 35-factor registry, point-in-time vintage joins, rolling H+1/H+3/H+5 cost-adjusted backtest, ablation and sector-to-stock transmission remain NOT_DONE/UNKNOWN.
- Status: INCOMPLETE / BLOCKED. No PASS promotion.

## Next actions
1. Run the official-source acquisition job in a GitHub Actions runner or other network-enabled execution environment, with pinned URLs, response headers, row counts, raw-byte SHA-256, retrieval timestamp and immutable archive manifest.
2. Capture IMF BR1 transaction export and Brazil PA changelog through the official interactive UI; if authentication/permissions block exports, record exact dependency without requesting credentials in chat.
3. Complete pinned SDMX 2.1 schema closure and offline validation after obtaining exact source XML.
4. Build GCR factor contracts only from acquired raw vintages; preserve provisional/final status and source frequency. Do not calculate factors from missing inputs.

## Invariants
₹0 spend; official free sources only; no synthetic data, guessed timestamps, forward-fill, or inference of equivalence; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; no production integration, trading admission, or PR merge. PR #39 remains open/draft/unmerged. UNKNOWN is not PASS.

## Source references
- Treasury XML feed contract: https://home.treasury.gov/treasury-daily-interest-rate-xml-feed
- Treasury CSV archive: https://home.treasury.gov/interest-rates-data-csv-archive/
- RBI Reference Rate Archive: https://rbi.org.in/scripts/ReferenceRateArchive.aspx
- IMF API: https://data.imf.org/en/Resource-Pages/IMF-API
- IMF SDMX Central schema UI: https://sdmxcentral.imf.org/webservice/schema.html
- BCB SGS 22707 dataset/resource: https://dadosabertos.bcb.gov.br/dataset/22707-balanca-comercial---balanco-de-pagamentos---mensal---saldo
