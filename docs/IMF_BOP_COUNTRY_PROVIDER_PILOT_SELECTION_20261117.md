# IMF BOP Country-Provider Pilot Selection — 2026-11-17

## Research objective
Choose a defensible single-country pilot route for the Global Capital Rotation & Relative-Attraction Overlay, using the live IMF SDMX Central registration catalogue. This is a provider-selection milestone only; it is not an observation extraction or flow-panel PASS.

## Material new finding: current Brazil registration candidate
The IMF SDMX Central Registered Data Sources catalogue was inspected on 2026-11-17. It lists:
- Dataflow: `IMF:BOP6(1.0)`
- Data Provider: `IMF:BR1`
- Registered URL: `https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml`
- Catalogue Last Updated: `2026-10-26T11:47:29.000Z`
- Provider identity is the Brazilian Central Bank (Banco Central do Brasil) by the official registered URL/domain and catalogue record.

This is materially better than an unscoped generic IMF query: it is a current, country-specific provider registration for a BOP6 dataflow and offers a concrete official-source pilot candidate.

## Important compatibility limitation
The registration is attached to `IMF:BOP6(1.0)`, while the current shared IMF BOP DSD catalogue separately lists `IMF:BOP(2.6.0)`. No evidence in the inspected registration row proves that BOP6(1.0) uses or is structurally compatible with BOP DSD 2.6.0. Do not silently equate these structures or their codelists. The registration's latest-updated timestamp is catalogue metadata, not the observation payload's publication timestamp or retrieval time.

## Pilot fetch result
The exact registered Brazil XML URL was opened through the available web retrieval layer. The retrieval layer returned an unsupported content-type error for `text/xml`. No HTTP status, response bytes, content length, final URL, raw payload, or SHA-256 was exposed. This does not establish that the origin is unavailable; it establishes only that this retrieval route could not inspect the XML payload.

## Other candidate routes considered
- IMF's legacy pilot dissemination site (https://sdmx.imf.org/bop/) states that it provides SDMX compact instances for all jurisdictions reporting to IMF, with 75 series per country, but its page says Last Update: 2013-01-09. This is too stale to be selected as the current pilot source without an independent currentness check.
- The registrations catalogue also lists other national providers, but no second country has been fetched or compared in this bounded audit. Brazil is selected as the first candidate solely because the official catalogue shows a recent registration timestamp (2026-10-26) and an official central-bank URL.

## Gate outcome
| Gate | Status |
|---|---|
| Official IMF SDMX registration catalogue inspected | VERIFIED_OFFICIAL |
| Brazil BOP6(1.0) / IMF:BR1 registration row identified | VERIFIED_OFFICIAL |
| Official registered URL and catalogue timestamp captured | VERIFIED_OFFICIAL |
| Current BOP6(1.0) DSD compatibility with IMF:BOP(2.6.0) | UNKNOWN |
| Raw Brazil XML bytes captured | NOT_DONE |
| HTTP response metadata / byte length / SHA-256 | NOT_DONE |
| Portfolio-investment transaction dimensions and codes confirmed in payload | UNKNOWN |
| Actual observation period / vintage / status confirmed | NOT_DONE |
| Brazil country-period portfolio-flow pilot | NOT_DONE |
| EM-wide panel | UNKNOWN / NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Why this advances the trading research
This narrows the next test to one official, country-specific source rather than speculative global endpoint discovery. If the Brazil payload can be retrieved and validated, it can demonstrate a reproducible extraction path and schema compatibility for a pilot. It cannot by itself justify an EM aggregate or a daily trading trigger. BOP is period-based and remains macro context only.

## Next bounded action
Retrieve the exact Brazil registered XML with a raw-byte-capable transport, preserving the untouched response and manifest fields: request URL, final URL, UTC retrieval timestamp, HTTP status, content type, byte length, SHA-256. Parse the header and dataset, identify the exact DSD reference/version and all dimensions/attributes. Confirm portfolio investment transaction entries and preserve asset/liability, instrument, frequency, period, currency, multiplier, observation status and any break/vintage. If the DSD is legacy or incompatible with BOP 2.6.0, keep the pilot separate and do not force-map it.

## Hard controls
No guessed query URLs, codes, observation values, or timestamps. No synthetic data, paid API, or external contact. Do not equate BOP6(1.0) to BOP(2.6.0) without evidence. Do not treat the 2013 pilot dissemination files as current. Do not substitute IIP positions or BOP_AGG estimates for reported transactions. Keep UNKNOWN as UNKNOWN. No Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or Engines A–E changes.
