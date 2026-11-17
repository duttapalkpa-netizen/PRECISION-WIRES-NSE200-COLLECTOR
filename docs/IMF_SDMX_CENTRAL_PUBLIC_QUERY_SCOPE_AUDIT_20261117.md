# IMF SDMX Central Public Query Scope Audit — 2026-11-17

## Research objective
Establish whether the official IMF SDMX Central public services provide a verified route to obtain the real BOP portfolio-investment observations needed as slow-moving macro context for the Global Capital Rotation & Relative-Attraction Overlay. Do not mistake public metadata/validation services for public observation dissemination.

## New official evidence
1. IMF SDMX Central Web Services (API) Guide, last updated May 2025:
   https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
   - The guide describes the IMF SDMX Central REST API and its public structure-query capabilities.
   - Structure API entry point: https://sdmxcentral.imf.org/sdmx/v2/
   - The guide explicitly says GET queries can be executed in a browser or with Python requests.
   - It documents public POST validation at https://sdmxcentral.imf.org/ws/public/data/validate and public POST transformation at https://sdmxcentral.imf.org/ws/public/data/transform.
   - Crucial distinction: these POST endpoints validate or transform a dataset supplied by the caller. They do not disseminate IMF country observations and cannot be used as evidence of a public BOP observation feed.
2. The current IMF SDMX Central web-service page advertises services for querying structures and data, but the May 2025 API guide section inspected here documents the structure-query service and processing endpoints; the actual public data-query URL/provider route for the required BOP flow observations has not been captured and validated.
3. The IMF SDMX Central dataflow catalogue currently shows 216 entries, with visible ESTAT BPM6_BOP_M and BPM6_BOP_Q examples. The page is paginated; the visible excerpt is not a complete IMF agency-filtered inventory. No conclusion that IMF BOP dataflow is absent is justified.
4. The IMF SDMX Central data structure catalogue lists IMF:BOP version 2.6.0.
5. The 2017 IMF ICS global SDMX submissions guide lists legacy submission identifiers BPM6_BOP_Q / IMF_BPM6_BOP_Q and historical structure references. These are legacy submission documentation, not proof of a current public dataflow, current observation coverage, or current DSD V2.6.0 compatibility. Do not reuse these identifiers as live query keys without current catalogue confirmation.

## Evidence links
- IMF SDMX Central API Guide (May 2025): https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- IMF SDMX Central web service: https://sdmxcentral.imf.org/webservice/schema.html
- IMF SDMX Central dataflow catalogue: https://sdmxcentral.imf.org/data/overview.html
- IMF SDMX Central DSD catalogue: https://sdmxcentral.imf.org/data/datastructure.html
- Legacy IMF global SDMX submission guide: https://www-ics.imf.org/Public/PDF/Global%20SDMX%20Submissions%20-%20How%20to.pdf

## Reconciled status
| Gate | Status |
|---|---|
| Public SDMX structure GET service | VERIFIED_OFFICIAL |
| Public validation/transform POST endpoints | VERIFIED_OFFICIAL — caller-supplied data processing only |
| Public BOP observation dissemination endpoint | UNKNOWN / NOT_VERIFIED |
| Current IMF BOP dataflow + provider + constraints | UNKNOWN |
| Legacy BPM6_BOP_Q identifiers as current usable dataflow | NOT_ADMISSIBLE without current confirmation |
| Raw DSD XML bytes/hash | NOT_DONE |
| Real country-period BOP portfolio transaction payload | NOT_DONE |
| Country-level EM portfolio-flow panel | UNKNOWN / NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Why this matters to the trading research
A public validator is not a market-flow source. A structure catalogue is not a dataset. A legacy submission code is not a live provider feed. Only an actual observation payload with source URL, provider, dataflow/DSD identity, frequency, time period, portfolio instrument, asset/liability direction, unit, currency, multiplier, observation status, vintage, retrieval timestamp, byte length and SHA-256 can support a research feature. BOP period data is macro context, not a daily 1–3 day trigger.

## Next bounded action
Inspect the current IMF SDMX Central catalogue with Agency=IMF filters and retrieve the exact IMF:BOP 2.6.0 structure plus referenced codelists through the official structure GET service. Separately identify current IMF or national-provider provision agreements/dataflows that explicitly reference a compatible BOP DSD. Only then test a single bounded country-period observation query. If no public observation endpoint/provider can be proven, record the precise blocker and stop; do not infer a route from the public validation endpoint.

## Hard controls
No guessed endpoint, query key, provider, observation, or timestamp. No synthetic data, paid API, or external contact. Do not confuse IIP positions with BOP transactions or BOP_AGG estimates with reported country observations. Keep UNKNOWN as UNKNOWN. Do not alter Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or Engines A–E.
