# Brazil BCB SGS Portfolio-Flow Pilot Discovery — 2026-11-17

## Research objective
Advance the Global Capital Rotation & Relative-Attraction Overlay with real official portfolio-flow data. This audit follows the prior Brazil provider-candidate audit but uses the Banco Central do Brasil Open Data Portal's exact dataset resources and SGS series identifiers rather than retrying the unsupported IMF-registered XML route.

## Exact official series discovered
### Asset-side series
- Dataset title: Portfolio investment - Net acquisition of financial assets - monthly - inflows
- Dataset ID / slug: 22907
- SGS series code: 22907
- JSON resource ID: 2cc6689a-5a3a-4652-aeaf-d60726e6b2e8
- API URL (unbounded catalogue resource): https://api.bcb.gov.br/dados/serie/bcdata.sgs.22907/dados?formato=json
- Unit: Million US dollars
- Frequency: Monthly
- Temporal coverage from: 01-01-1995
- Metadata last updated: 2026-03-26 18:34 (-0300)
- Source/maintainer: Banco Central do Brasil / Department of Economics
- Dataset resource license: Open Data Commons Open Database License (ODbL)
- The exact resource endpoint returned JSON via the web retrieval layer. Visible observations include 2026-01 through 2026-08. This confirms a live, real payload was served through the API route, but this audit did not capture raw response bytes or HTTP metadata suitable for SHA-256 evidence.

### Liability-side series
- Dataset title: Portfolio investment - Net incurrence of liabilities - monthly - outflows
- Dataset ID / slug: 22926
- SGS series code: 22926
- JSON resource ID: f448decb-91d4-44bb-9d4f-6ab8e966ab17
- API URL (unbounded catalogue resource): https://api.bcb.gov.br/dados/serie/bcdata.sgs.22926/dados?formato=json
- Unit: Million US dollars
- Frequency: Monthly
- Temporal coverage from: 01-01-1995
- Metadata last updated: 2026-03-26 18:34 (-0300)
- Source/maintainer: Banco Central do Brasil / Department of Economics
- Dataset resource license: ODbL
- The API resource link is confirmed by the official dataset page. The web retrieval layer opened the JSON endpoint but did not expose a readable body in this inspection. No raw bytes or SHA-256 captured.

## Bounded interpretation and caveats
- The selected asset series is explicitly labelled net acquisition of financial assets, monthly inflows. The liability series is explicitly labelled net incurrence of liabilities, monthly outflows. Keep them separate.
- The portal's general concept text describes portfolio investment as both transactions and positions. The selected dataset titles specify monthly inflow/outflow, but the exact SGS series-specific methodology and sign conventions still require reconciliation with BCB's methodological notes before any combined measure is created.
- The two selected series are not a complete decomposition of all portfolio investment: instrument scope, equity/debt coverage and any omitted categories need to be confirmed.
- Monthly frequency means macro context only, not a 1–3 day trading trigger.
- Do not infer net foreign inflow by subtracting or adding these series until signs, definitions, coverage and accounting identities are verified.

## Evidence sources inspected
1. Official BCB Open Data external-sector catalogue: https://opendata.bcb.gov.br/dataset/?_tags_limit=0&sort=views_recent+desc&tags=external-sector
2. Asset-side dataset detail: https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows
3. Asset-side JSON API: https://api.bcb.gov.br/dados/serie/bcdata.sgs.22907/dados?formato=json
4. Liability-side dataset detail: https://opendata.bcb.gov.br/dataset/22926-portfolio-investment---net-incurrence-of-liabilities---monthly---outflows
5. Liability-side JSON API: https://api.bcb.gov.br/dados/serie/bcdata.sgs.22926/dados?formato=json
6. Brazil NSDP: https://www.bcb.gov.br/en/statistics/nsdp
7. API date-range syntax cross-check: https://seriesbr.readthedocs.io/en/latest/demos/BCB.html and https://github.com/rteoo/bcb-data/blob/main/BCB_API_REFERENCE.md. These are secondary implementation references, not the source of the observations.

## Gate outcome
| Gate | Status |
|---|---|
| Official BCB external-sector catalogue | VERIFIED_OFFICIAL |
| Exact asset-side dataset and SGS code 22907 | VERIFIED_OFFICIAL |
| Exact liability-side dataset and SGS code 22926 | VERIFIED_OFFICIAL |
| Monthly frequency and USD-million unit | VERIFIED_OFFICIAL |
| Asset-side JSON observation payload served | PARTIAL — JSON response visible; raw bytes/HTTP metadata not archived |
| Liability-side JSON observation payload | PARTIAL — endpoint opened; body not exposed in readable result |
| Raw response bytes, status, content type, byte length, SHA-256 | NOT_DONE |
| Series-specific methodology and sign reconciliation | NOT_DONE |
| Instrument/coverage decomposition | UNKNOWN |
| Combined portfolio flow calculation | NOT_AUTHORIZED |
| Country-period pilot acceptance | PARTIAL / NOT_ACCEPTED |
| EM-wide panel | UNKNOWN / NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Next exact acceptance action
Use a raw-byte-capable transport against the two exact BCB SGS codes, in short bounded date windows. Capture raw response bytes and a manifest with request/final URL, HTTP status, content type, retrieval UTC, byte length and SHA-256. Validate JSON schema, date ordering, duplicate/missing periods, numeric parsing and last available period. Obtain BCB methodology notes and reconcile asset/liability direction and instrument coverage. Keep the two series separate until this is complete.

## Hard controls
No synthetic observations, guessed values, inferred timestamps, unverified signs, or unsupported combined net flow. No unit conversion in raw storage. Do not confuse BOP transactions with IIP/CPIS positions. No paid API or external contact. UNKNOWN remains UNKNOWN. No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A–E.
