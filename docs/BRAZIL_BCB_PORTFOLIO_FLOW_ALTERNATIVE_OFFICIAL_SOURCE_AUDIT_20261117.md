# Brazil BCB Portfolio-Flow Alternative Official Source Audit — 2026-11-17

## Why this task was selected
The IMF-registered Brazil BOP XML route remains blocked at raw-byte retrieval and DSD compatibility is unproven. Instead of repeating that failed route, this audit examined the same national compiler's official open-data portal for independently published portfolio-investment transaction series. This directly advances the overlay's need for real cross-border portfolio-flow evidence.

## New official source discovery
The Banco Central do Brasil Open Data Portal external-sector catalogue exposes 55 datasets. Its visible entries include:
- Portfolio investment — Net acquisition of financial assets — monthly — outflows
- Portfolio investment — Net acquisition of financial assets — monthly — inflows
- Portfolio investment — Net acquisition of financial assets — monthly — net
- Portfolio investment — Net incurrence of liabilities — monthly — outflows
- Portfolio investment — Net incurrence of liabilities — monthly — net
- Portfolio investment — Debt securities — monthly — inflows/outflows
Each catalogue item exposes JSON, CSV and WSDL resource formats. The portal descriptions state that portfolio investment is divided into assets and liabilities and includes transactions and positions. The exact selected dataset must be checked to ensure it is a transaction series, not a position series.

Official catalogue:
https://opendata.bcb.gov.br/dataset/?_tags_limit=0&sort=views_recent+desc&tags=external-sector

The official Brazil NSDP page independently lists Balance of Payments as a BCB-supplied External Sector category with SDMX-ML dissemination. This corroborates the source institution and data category but does not by itself validate a particular observation series.

## Research design decision
For the overlay, prefer two separate transaction directions rather than one ambiguous net figure:
1. Portfolio investment — net acquisition of financial assets (Brazilian residents' acquisition of foreign portfolio assets).
2. Portfolio investment — net incurrence of liabilities (foreign acquisition of Brazilian portfolio liabilities).

Do not label either series alone as "capital inflow". Preserve the compiler's published direction and sign. A combined net-flow metric may be derived only after confirming units, currency, frequency, transaction definitions, instrument coverage and sign convention from dataset metadata.

Monthly series are slow-moving macro context, not a 1–3 day trading trigger. Do not promote them into the live selector.

## Current status
| Gate | Status |
|---|---|
| Official BCB external-sector catalogue inspected | VERIFIED_OFFICIAL |
| Portfolio investment asset-side monthly transaction candidates identified | VERIFIED_OFFICIAL at catalogue-description level |
| Portfolio investment liability-side monthly transaction candidates identified | VERIFIED_OFFICIAL at catalogue-description level |
| JSON/CSV/WSDL resource availability advertised | VERIFIED_OFFICIAL at catalogue level |
| Exact dataset resource ID and API URL captured | NOT_DONE |
| Dataset-specific metadata, unit, currency, sign, period, revisions captured | NOT_DONE |
| Raw observation payload, HTTP status, bytes, SHA-256 | NOT_DONE |
| Transaction vs position confirmed for chosen resources | UNKNOWN |
| Independent country-period pilot | NOT_DONE |
| IMF BOP6 registration crosswalk compatibility | UNKNOWN |
| EM-wide panel | UNKNOWN / NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Next bounded action
Open the BCB portal's exact portfolio-investment dataset entries, capture their dataset IDs and resource URLs, and choose one asset-side and one liability-side monthly transaction resource. Retrieve a small bounded period from the official JSON/CSV API and archive raw bytes plus a manifest (request/final URL, UTC retrieval time, HTTP status, content type, byte length, SHA-256). Verify the data dictionary and reconcile at least one period with the BCB BOP publication/NSDP. If portal resources are only positions or lack source metadata, do not use them as transactions.

## Hard controls
No synthetic observations, no inferred values, no guessed resource URLs, no sign inversion, no unit/currency conversion in the raw layer. Keep assets and liabilities separate. Do not confuse transactions with positions or CPIS/IIP stocks. Do not substitute BOP_AGG estimates. Keep UNKNOWN as UNKNOWN. No paid API, no external contact, and no changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A–E.
