# IMF Brazil SGS 22707 primary API response-boundary audit — Part 29
Date: 2026-11-18
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: qa/imf-brazil-parser-schema-path-hardening
Status: PARTIAL / OPEN; no production admission.

## Objective
Attempt a primary-source value-level verification of BCB SGS series 22707 for September 2026, without promoting secondary mirrors.

## Official source identity and API contract
The official BCB Open Data dataset identifies SGS 22707 as the monthly BPM6 balance-on-goods balance, measured in USD millions, sourced from SGS and maintained by BCB Statistics. Its stated timeliness is up to four weeks after the reference period. The official dataset page lists JSON and CSV resources. Source: https://dadosabertos.bcb.gov.br/dataset/22707-balanca-comercial---balanco-de-pagamentos---mensal---saldo
The official JSON resource page specifies the BCData/SGS endpoint and date-filter parameters `dataInicial` and `dataFinal` in DD/MM/YYYY format, plus an `ultimos/{N}` endpoint. Source: https://dadosabertos.bcb.gov.br/dataset/22707-balanca-comercial---balanco-de-pagamentos---mensal---saldo/resource/999ce9e2-ee0c-4910-b4f9-0a1d1fbdfa66

## What was directly observed
The official JSON resource link was followed to:
https://api.bcb.gov.br/dados/serie/bcdata.sgs.22707/dados?formato=json
The browser-retrieved response snapshot displayed historical rows from 1995-01 through 2026-02. Its web retrieval record itself was crawled seven months ago; it is therefore a cached/stale response snapshot, NOT proof of the live endpoint's current latest observation on 2026-11-18.
The official `ultimos/10` resource response snapshot likewise ended at 2026-02. This confirms the same response-boundary issue in the cached snapshot only.
A direct date-filtered September-2026 URL attempt could not be retrieved by the available browser tool. No live API response, HTTP headers, raw JSON/CSV bytes, response size, or raw-byte SHA-256 was captured.

## Cross-check and interpretation
- BCB's official 2026-10-26 External Sector Statistics bulletin reports the September-2026 goods trade balance as approximately USD 6.9bn, with exports USD 34.6bn and imports USD 27.7bn. Source: https://www.bcb.gov.br/content/statistics/externalsectorstatistics_prev/202610_External_sector_statistics_text.pdf
- A secondary page (Econograma) reports SGS 22707 September-2026 = USD 6,869m. This remains SECONDARY_ONLY and is not promoted as the exact primary SGS observation: https://econograma.com.br/escuro/graficos/balanca-comercial-bp/
- The BCB bulletin corroborates the rounded magnitude only. It does not establish that the exact SGS 22707 value is 6,869m.
- Official BCB metadata says expected timeliness is up to four weeks. That makes a Sep-2026 observation expected by the audit date, but timeliness metadata does not itself prove that the SGS endpoint served it.

## Acceptance matrix
- Official series identity / unit / frequency / provenance: PASS.
- Official API query contract and date filter syntax: PASS.
- Cached official JSON snapshot ending 2026-02: OBSERVED, but stale snapshot; not live freshness evidence.
- Live official SGS 22707 latest observation through Sep-2026: NOT_VERIFIED.
- Exact official September-2026 JSON/CSV value: NOT_DONE.
- Exact 6,869m value: SECONDARY_ONLY.
- BCB official September bulletin rounded goods balance (~USD 6.9bn): PASS.
- Raw response archive, byte count, headers, SHA-256: NOT_DONE.
- Value-level reconciliation: PARTIAL / OPEN.

## Next action
Use a normal browser or local network to call the official date-filtered endpoint for 01/09/2026–30/09/2026, export the raw response bytes, record HTTP status/headers/byte count/SHA-256, and independently compare the exact row with the official BCB bulletin. If the live endpoint still ends at Feb-2026, preserve the returned response and investigate endpoint publication lag or service routing; do not replace it with third-party values.

## Project controls
No synthetic data, inferred timestamps, paid APIs, or third-party primary-source promotion. No production integration, merge, trading admission, or workflow changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), and Engines A–E unchanged. UNKNOWN is not PASS. PR #39 remains research-only and unmerged.
