# IMF Brazil Registration History — Part 5: Official UI Filter and API Boundary
Date: 2026-11-18 (Asia/Kolkata)
Continuation page: 39
Scope: narrow official-source audit after Part 4; no repeated RSS/BCB payload retrieval, no undocumented API, no production changes.

## 1. Reused prior accepted evidence
- Current registration listing: `IMF:BOP6(1.0)`, provider `IMF:BR1`, BCB registered XML URL, last updated `2026-10-26T11:47:29.000Z`.
- BCB XML payload Dataflow remains `IMF:BOP_BPM6(1.0)`; prior contract reconciliation run `44290101769`, artifact `14420378420`, digest `6435b5df856889ae1a48742681f0b127b04e1a4057c361b054c329a5049fc8aa`.
- Distinct Dataflow IDs; same DSD does not imply equivalence. Mismatch CONFIRMED; Brazil admission BLOCKED.
- Recent RSS 33-item window remains bounded and has no Brazil match; do not re-fetch.

## 2. Newly verified official UI structure
Official Data Registrations page: https://sdmxcentral.imf.org/activity/data-log.html
- The page title is "Data Registrations" and it explicitly says historical activity for provision agreements.
- It provides breakdown modes: Breakdown By Provision Agreement, Breakdown By Dataflow, Breakdown By Data Provider, and Show All Data Registrations.
- Its registration detail panel exposes Data URL, Provision URN, Dataflow URN, Data Provider URN and User; event rows include Date, Data URL, Action, Data Store and Series.
- The static public page extraction exposed the controls/field schema but no data rows. This is not evidence that no Brazil event exists; actual filtering/interaction is still NOT_DONE.
Official current registration listing: https://sdmxcentral.imf.org/data/registrations.html
- Current listing independently shows IMF:BOP6(1.0) / IMF:BR1 / BCB URL.
Official data provider directory: https://sdmxcentral.imf.org/organisations/dataproviders.html
- Provider directory identifies IMF:BR1 as Central Bank of Brazil.
Official Provision Agreements page: https://sdmxcentral.imf.org/data/provisionAgreements.html
- Provides Provision Agreement details with URN, URL, Revisions, Description, Annotations, Valid From and Valid To; includes Changelog and Export SDMX-ML 3.0 / Excel controls. Static page extraction does not reveal the selected Brazil agreement's actual history.

## 3. API contract correction and boundary
- IMF SDMX Central Web Services Guide, last updated May 2025, documents structure REST entry point `https://sdmxcentral.imf.org/sdmx/v2/` and standard structure query capability.
- The guide explicitly says there is no official REST API for registration processing services; it identifies a separate FMR entry point `https://sdmxcentral.imf.org/ws/public/data`. This is a registration submission/processing interface, not evidence of a public historical registration-query API.
- A candidate standard structure query URL for Provision Agreements was tested through the available browser retrieval interface but returned an internal access error. This does not establish endpoint outage or invalidity. No raw response, HTTP status, payload, or SHA-256 is claimed.
- No internal AJAX endpoint, inferred query parameter, POST request, or undocumented endpoint was used.
- Important distinction: standard REST structure queries can retrieve ProvisionAgreement structures; they do not by themselves reconstruct registration event chronology unless the returned structure/changelog contains actual dated revisions. The GUI history view remains the correct documented read path to pursue.

## 4. Acceptance matrix
| Item | Status |
|---|---|
| Exact Brazil current registration row | PASS (prior evidence reused) |
| IMF:BR1 provider identity | PASS (official directory) |
| Data Registrations history page + filter modes identified | PASS |
| Actual Brazil historical rows retrieved by interactive filter | NOT_DONE |
| Brazil Provision Agreement URN and changelog captured | NOT_DONE |
| Dated create/replace/delete chronology | UNKNOWN |
| BOP6 vs BOP_BPM6 mismatch | CONFIRMED |
| Brazil registration admission | BLOCKED |
| EM aggregation / market use | NOT_AUTHORIZED |

## 5. Single next action
Use the official Data Registrations GUI in "Breakdown By Data Provider" and select exact provider `IMF:BR1`; then inspect the BOP registration row and capture every displayed historical event and its Registration Details. Separately open the corresponding Provision Agreement and use its Changelog / Export controls to preserve the exact URN and dated revisions. Capture only actual returned rows/documents, with raw download bytes, source URL, retrieval timestamp and SHA-256. If the GUI returns no records or requires authorized login, preserve the exact observed limitation and keep historical chronology UNKNOWN. Do not infer a transaction ID or use FMR submission interface as a read API.

## 6. User macro priority preserved, not yet integrated
The high-impact overlay remains queued behind Brazil closure: P0 US 10Y/Fed, broad USD vs ICE DXY distinction, USD/INR, Brent/OPEC+, India FPI/DII sector flows and 200-session event study; P1 China/EM rotation, Korea/Taiwan AI/semiconductor relative returns, Japan/JPY carry stress and matched TRI ratios. Existing source discovery is not evidence of synchronized ingestion or predictive value. Each factor must demonstrate incremental, out-of-sample, cost-aware impact on Indian sector/stock outcomes before receiving weight. Low-impact/unproven factors stay deferred or rejected.

## 7. Invariants
₹0 spend; free official sources only. No synthetic data, invented timestamps, guessed IDs/endpoints, or undocumented routes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. No PR merge, production integration, or trading admission. UNKNOWN is not PASS.
