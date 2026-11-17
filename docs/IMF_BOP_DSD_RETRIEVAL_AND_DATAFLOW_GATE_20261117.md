# IMF BOP DSD Retrieval and Dataflow Gate — 2026-11-17

## Purpose
Advance the Global Capital Rotation & Relative-Attraction Overlay toward a validated country-level portfolio-investment transaction input. This audit intentionally avoids repeating the previously committed DSD component cross-check and IMF observation-access gate.

## New findings
1. SDMx Global Registry's BOP package page links the exact BOP V2.6.0 SDMX-ML 2.1 artefact at:
   https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1
   The same page says registry access is unauthenticated and lists the BOP DSD maintenance agency as IMF.
2. The web retrieval layer rejected the XML response as unsupported application/xml (HTTP/application status details were not exposed by that viewer). A direct container download attempt and a second direct HTTPS request attempt failed at DNS resolution in this execution environment. Therefore no raw XML bytes, HTTP response metadata, byte length, or SHA-256 were obtained. This is an environment retrieval failure, not evidence that the official registry endpoint is unavailable.
3. IMF SDMX Central's data structure catalogue independently lists IMF:BOP version 2.6.0. Its public web-service schema page identifies the service base URL https://sdmxcentral.imf.org/sdmx/v2/ and supports structure queries, including data structures and dataflows.
4. The visible IMF SDMX Central dataflow catalogue shows 216 total entries and, in the rendered page excerpt, displays CBSL and ESTAT examples including ESTAT BPM6_BOP_M and BPM6_BOP_Q. This excerpt is paginated and does not expose the full IMF agency-filtered dataflow inventory. Therefore it is NOT evidence that no IMF BOP dataflow exists.
5. The registrations catalogue lists provider-specific SDDS/NSDP registrations under dataflows such as IMF:BOP6 and IMF:BOP_BPM6, including IMF:IMF sample compact registrations and national statistical providers. These are registration/provider records and must not be mistaken for a global IMF BOP country-observation panel. They may provide a bounded official-country pilot route only after the exact dataflow/DSD compatibility and payload contents are verified.

## Evidence URLs
- SDMx BOP package and exact XML link: https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/
- Exact BOP DSD 2.1 URL: https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1
- IMF SDMX Central DSD catalogue: https://sdmxcentral.imf.org/data/datastructure.html
- IMF SDMX Central web-service schema/query builder: https://sdmxcentral.imf.org/webservice/schema.html
- IMF SDMX Central dataflow catalogue: https://sdmxcentral.imf.org/data/overview.html
- IMF SDMX Central registrations catalogue: https://sdmxcentral.imf.org/data/registrations.html

## Gate outcome
| Check | Status |
|---|---|
| Official BOP DSD 2.6.0 identity and exact structure URL | VERIFIED_OFFICIAL |
| Registry unauthenticated structure-access policy (documented) | VERIFIED_OFFICIAL |
| Raw DSD XML bytes downloaded and archived | NOT_DONE — execution environment DNS/download failure |
| Raw DSD byte length and SHA-256 | NOT_DONE |
| Parsed IMF DSD/codelist exact code values | UNKNOWN |
| Exact IMF global BOP portfolio-flow dataflow and constraints | UNKNOWN |
| Country-provider registration identified as a potential pilot route | PARTIAL — candidate route only |
| Observation query/payload captured and validated | NOT_DONE |
| EM country portfolio-flow panel | UNKNOWN / NOT_DONE |
| Production overlay integration | NOT_AUTHORIZED |

## Research relevance decision
Do not spend effort building a synthetic or inferred EM portfolio-flow proxy from this metadata. The overlay's research objective requires real, dated, source-verifiable cross-border capital-flow evidence. BOP portfolio investment is period-based and should be a slow-moving macro/context feature, not a fabricated daily trigger for 1–3 day trades. A pilot must preserve assets/liabilities, instrument, transaction/position distinction, currency, multiplier, frequency, period, status and vintage.

## Next bounded action
When network retrieval is available, fetch the exact registry XML URL above with an SDMX-ML 2.1 Accept header, save untouched response bytes, and create a manifest with exact request/final URL, HTTP status, content type, UTC retrieval time, byte length and SHA-256. Parse referenced codelists and inspect IMF agency-filtered dataflows/constraints through the documented IMF SDMX Central service. Then choose one provider registration only if it is explicitly compatible with the IMF BOP DSD and yields a real bounded country-period transaction payload. Do not infer the dataflow from the DSD name.

## Hard controls
- No guessed codes, keys, query URLs, observations or timestamps.
- No synthetic data, paid APIs, or external contact.
- Do not treat country-provider registrations as a global IMF panel.
- Do not substitute BOP_AGG estimates for observed country transactions.
- Do not convert IIP positions into BOP flows.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A–E changes.
- UNKNOWN remains UNKNOWN; this audit is not an observation-extraction PASS.
