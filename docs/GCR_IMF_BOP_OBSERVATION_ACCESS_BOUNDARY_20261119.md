# Global Capital Rotation — IMF BOP Observation Access Boundary
Date: 2026-11-19
Scope: official public-route verification only; no guessed SDMX observation key, no credentials, no synthetic data.

## What is confirmed
1. IMF dataset page identifies the public Balance of Payments dataset as `IMF.STA:BOP`, annual and quarterly, and shows an API link.
   - Dataset: https://data.imf.org/en/datasets/IMF.STA:BOP
   - Public page API link resolves to the IMF Azure API Management developer portal sign-in page (https://portal.api.imf.org/signin?returnUrl=/apis) when followed without an authenticated session.
2. IMF API documentation states that IMF data are available through SDMX 2.1 and SDMX 3.0 APIs; the Swagger explorer requires a beta portal account sign-in.
   - https://data.imf.org/en/Resource-Pages/IMF-API
3. IMF SDMX Central Web Services Guide (last updated May 2025) documents a public structure query service at `https://sdmxcentral.imf.org/sdmx/v2/` for Dataflows, Codelists, Concepts and DSDs. It documents public POST validation/transform endpoints under `/ws/public/data`, and a private registration submission endpoint. It does not specify an anonymous public BOP observation query endpoint in this guide.
   - https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
4. The SDMX Central structure UI and API can retrieve the BOP DSD/Dataflow metadata; metadata availability is not observation access.

## Decision
- IMF BOP DSD/codelists: metadata route is public and can be archived.
- IMF BOP country observations via the documented API: BLOCKED pending a verified public observation route or a public downloadable dataset response. The current API link's sign-in redirect is evidence of an access boundary, not evidence that the data themselves are restricted.
- No guessed API endpoint, SDMX key, credentials, session cookie or fabricated observation will be used.
- CPIS/PIP positions cannot substitute for BOP portfolio transaction flows.

## Next allowed work
1. Inspect the dataset page's public Download/View Data route for a direct file or browser-export URL, without signing in or using credentials.
2. If the download is public, capture raw bytes, URL, UTC retrieval time, HTTP status, content type, size and SHA-256, then derive a DSD-validated country observation panel.
3. If it requires sign-in, keep IMF BOP observations BLOCKED and use only independently verified public national central bank/NSDP sources with country-by-country coverage and no synthetic EM aggregate.
4. Maintain a versioned EM country membership edition, currency conversion method, period alignment, units, revision/vintage and missingness policy before aggregation.

## Invariants
₹0; free official sources only. No synthetic observations, no guessed SDMX keys, no invented timestamps. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. UNKNOWN is not PASS.
