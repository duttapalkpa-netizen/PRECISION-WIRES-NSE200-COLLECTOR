# IMF BOP Observation Access Gate — 2026-11-17

## Decision
- IMF BOP dataset identity and statistical scope: VERIFIED_OFFICIAL.
- IMF SDMX 2.1 / 3.0 API availability: VERIFIED_OFFICIAL at the product-documentation level.
- Public, unauthenticated BOP observation query URL + response bytes + retrieval metadata: NOT_VERIFIED in this audit.
- Country-level portfolio-investment transaction panel: UNKNOWN / NOT_DONE.
- BOP_AGG annual world/country-group panel as an observed-only global flow: NOT_ADMISSIBLE without component-level actual/estimate separation.
- Trading-trigger suitability for 1–3 day horizon: NOT_SUPPORTED by the documented frequency.

## Official source inspection
1. IMF Data API page: https://data.imf.org/en/Resource-Pages/IMF-API
   - Inspected 2026-11-17.
   - Official page states IMF data are available through SDMX 2.1 and SDMX 3.0 APIs.
   - The API exploration / Swagger link instructs users to sign in with a beta portal account.
   - This does not prove that every dataset query requires authentication; it does mean this audit has not established an unauthenticated data-query route from the portal documentation alone.
2. IMF BOP dataset page: https://data.imf.org/Datasets/BOP
   - Inspected 2026-11-17.
   - Describes BOP as transactions between residents and nonresidents, comprising current, capital and financial-account components.
   - Dataset page provides API / View Data / Download navigation.
   - No observation payload, exact data query URL, HTTP response, byte length, publication vintage, or SHA-256 was captured in this audit.
3. IMF BOP_AGG dataset page: https://data.imf.org/en/datasets/IMF.STA:BOP_AGG
   - Inspected 2026-11-17.
   - Describes an annual November publication.
   - Country-level information is based on reported data / NSDP except specified Fund-account substitutions.
   - World and country-group aggregates combine reported country data with estimates for nonreporting economies, including WEO and External Wealth of Nations sources (Euro Area treatment differs).
   - Therefore BOP_AGG cannot be treated as a purely observed-only aggregate unless actual and estimated components are explicitly separated and documented.
4. SDMX Global Registry BOP DSD V2.6.0 reference: https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/
   - Official SDMX page states BOP DSD V2.6.0 is maintained by IMF and registry artefacts can be accessed without authentication.
   - Public access to structure metadata is not evidence that BOP observation data were downloaded.

## Why this is the next gate
The overlay's global EM portfolio-flow input is a material classification input, but it must remain UNKNOWN until a country-level transaction panel is actually extracted and validated. Metadata availability or a successful structure query cannot be promoted to observed transaction coverage.

## Required next acceptance sequence
1. Identify the exact IMF BOP dataflow/version, provider, dimensions, and portfolio-investment transaction series from the official DSD/codelists.
2. Verify a concrete public data query (or document the precise authentication requirement) without inventing URLs.
3. Capture one bounded country/period test response, recording exact request URL, HTTP status, content type, retrieved UTC timestamp, publication/as-of metadata, byte length, SHA-256, and raw bytes.
4. Parse and validate measure, accounting entry, unit, multiplier, currency, frequency, time period, reporting economy, and data attributes. Distinguish assets/liabilities and net incurrence/acquisition directions correctly.
5. Verify actual-vs-estimate status; exclude estimates from an observed-only panel unless separately labelled.
6. Only after a bounded pilot passes, decide whether a complete panel is feasible. Do not assume daily frequency: IMF BOP data is period-based; the IMF BOP_AGG publication is annual.
7. Keep the 1–3 day scanner independent of quarterly/annual macro observations; such data may be slow-moving context only after freshness and PIT rules are established.

## Hard controls
- No synthetic observations, no inferred timestamps, no guessed query URLs, no paid API, no external contact.
- No substitution of BOP_AGG estimates for observed country transactions.
- No conversion of IIP positions (stocks) into BOP transaction flows.
- No production classifier or ranking changes.
- UNKNOWN remains UNKNOWN until raw observation bytes and all validation evidence exist.

## Prior work reused (not repeated)
- Existing metadata-first contract: docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md.
- Existing official-source register and known BOP_AGG estimation caveats: docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md.
- This note adds current IMF portal/API access-gate findings only; it does not claim observation extraction or solve the outstanding country-level panel.

## Status
- Official source documentation review: PASS.
- Public observation data route verification: NOT_DONE.
- Raw BOP observation payload capture: NOT_DONE.
- Country-level portfolio-flow panel: UNKNOWN / NOT_DONE.
- BOP_AGG actual/estimate decomposition: NOT_DONE.
- Production integration: NOT_AUTHORIZED.
