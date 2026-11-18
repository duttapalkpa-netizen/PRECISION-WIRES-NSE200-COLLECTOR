# IMF Brazil SGS 22707 live date-filter request attempt — Part 30
Date: 2026-11-18
Branch: qa/imf-brazil-parser-schema-path-hardening
Status: BLOCKED_BY_NETWORK_DNS; no live endpoint result.

## Objective
Test the official BCB SGS 22707 JSON endpoint for the exact September 2026 observation, distinguishing a live response from previously indexed/cached search snapshots.

## Official endpoint attempted
Date-filtered JSON:
`https://api.bcb.gov.br/dados/serie/bcdata.sgs.22707/dados?formato=json&dataInicial=01%2F09%2F2026&dataFinal=30%2F09%2F2026`
Equivalent unescaped date form was also attempted.
Latest-ten JSON:
`https://api.bcb.gov.br/dados/serie/bcdata.sgs.22707/dados/ultimos/10?formato=json`

The official dataset metadata describes SGS 22707 as monthly balance on goods, USD million, and publishes JSON/CSV resources. The API query convention uses DD/MM/YYYY date parameters. Official dataset: https://opendata.bcb.gov.br/dataset/22707-balance-on-goods---balance-of-payments---monthly---net

## Execution evidence
- Web open of the exact date-filtered URL returned an inaccessible/internal-error response from the retrieval tool; no HTTP status or response body from BCB was exposed.
- Three direct urllib requests from the working container (encoded date filter, unescaped date filter, and latest-ten endpoint) each failed before HTTP connection with `Temporary failure in name resolution` for the API host.
- Therefore this environment did not reach the BCB API. This is a local DNS/network access failure, not evidence that BCB returned an empty response, a 404, stale data, or a live endpoint ending February 2026.
- No response bytes, HTTP headers/status, byte count, or SHA-256 exist for these attempts. No raw-data artifact is claimed.

## Evidence interpretation
- Official dataset identity, unit, frequency and API resource discovery remain PASS.
- Live date-filtered September 2026 query: BLOCKED_BY_NETWORK_DNS.
- Live latest-ten query: BLOCKED_BY_NETWORK_DNS.
- Exact primary September value: NOT_VERIFIED / NOT_DONE.
- Secondary 6,869m value remains SECONDARY_ONLY; do not promote.
- BCB's official September bulletin rounded goods surplus (~USD 6.9bn) remains independent bulletin-level corroboration, not a substitute for the exact SGS observation.

## Required next step
Run the exact date-filtered URL in a normal browser or network with DNS access. Save the unmodified response bytes and record retrieval time with timezone, HTTP status, response headers, byte count and SHA-256. If response is successful, validate the date/value row and compare to the official BCB September bulletin. If empty or failed, retain exact response and investigate from that network; do not infer the reason from this blocked environment.

## Controls
No synthetic data, guessed timestamps, paid APIs, or third-party primary-source promotion. No production integration, PR merge, workflow changes, or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), and Engines A–E unchanged. UNKNOWN is not PASS.
