# GCR — IMF BOPS SDMX public structure-route audit
Date: 2026-11-19 (Asia/Kolkata)
Workstream: Global Capital Rotation & Relative-Attraction Overlay
Stage: Observation only
Status: STRUCTURE API DOCUMENTED; BOP DATAFLOW / INDIA SERIES NOT VERIFIED; RAW DATA NOT ACQUIRED

## 1. Purpose
Resolve the prior Continuation 43 Part-4 blocker: whether IMF SDMX Central exposes a documented public structure-discovery route that can identify the exact BOP dataflow, DSD, dimensions, codelists and India quarterly series without relying on the dataset landing-page API sign-in route.

## 2. New official-source findings
### 2.1 IMF SDMX Central Web Services Guide
Official guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- Guide last updated May 2025.
- Official structure-service entry point: https://sdmxcentral.imf.org/sdmx/v2/
- Guide explicitly says structure queries cover Dataflows, Codelists, Concepts and Data Structures.
- Supported structure resources include `dataflow`, `datastructure`, `codelist`, `conceptscheme`, and others.
- Path parameters include agencyID, structureID, version and itemID; request parameters control detail and referenced structures.
- Guide describes browser execution or external HTTP requests for GET structure queries.
- This is a public structure-discovery interface, distinct from the IMF data dissemination/data query endpoint. The guide's public validation/transform POST services do not themselves prove that BOP observations can be downloaded through the same route.

### 2.2 IMF SDMX Central registry
Official registry: https://sdmxcentral.imf.org/data/registrations.html
- Public HTML registry page is reachable and exposes Data Structures, Dataflows, Codelists and registered data-source sections.
- Search-indexed current registry listing identifies IMF agency Data Structure `BOP`, name “Balance of Payments and International Investment Position”, version `2.6.0`.
- The public registration listing includes multiple national registrations for BOP-family dataflows, demonstrating that registered national BOP XML sources exist. These registrations are not proof of the IMF global dataset's observation access or of India's registration.
- Registry HTML inspection does not expose a confirmed India-specific BOP registration in the reviewed output.

### 2.3 Legacy BOP structure identifiers in IMF documentation
The May-2025 guide contains examples using:
- Dataflow `IMF:BOP_BPM6(1.0)`
- Data Structure `IMF:ECOFIN_DSD(1.0)`
- Data domain `BOP6`
- Quarterly frequency code `Q`
- Example indicator `BCA_BP6_EUR`
These are explicitly guide examples / legacy structure identifiers, not verified current India series identifiers. They must not be copied into a production data query without checking current structure versions and codelists.

## 3. What remains unverified
- A live successful GET response from the structure API for the exact BOP dataflow and DSD was not obtained in this inspection; direct URL retrieval attempts through the browser research interface returned inaccessible/internal-error results. The API route itself is documented, but the exact query payload is not yet verified.
- No current dataflow ID/version confirmed for the IMF BOP dataset used in RBI paper's underlying replication.
- No India REF_AREA code validated against the relevant BOP codelist in the current DSD.
- No current dimension order, counterpart-area code, frequency constraint, indicator/item codes, unit multiplier, observation attributes or status codes validated.
- No IMF observation data request was successfully executed.
- No raw bytes, response headers, row counts, source vintage, retrieval timestamp, or SHA-256 for IMF India quarterly data exist.
- The previous IMF BOP dataset landing-page API link redirected to sign-in; this does not prove every SDMX structure/data route is gated, nor does the structure API documentation prove that observation retrieval is public.

## 4. Safe next acquisition protocol
1. Query the official structure service for current IMF BOP dataflows and the IMF BOP DSD, using the documented structure endpoint and explicit agency/ID/version.
2. Save raw structure responses first; capture final URL, HTTP status, content type, retrieval timestamp, byte count and SHA-256.
3. Resolve the exact DSD from the dataflow's references; extract dimension order, concept identities and referenced codelist IDs/versions.
4. Resolve India REF_AREA, quarterly FREQ, counterpart-area selection, BOP item/indicator codes, units/multipliers, sign conventions and observation attributes only from those returned structures/codelists.
5. Only after steps 1–4 pass, test a single narrow India quarterly observation query. Do not guess a full SDMX key or transplant legacy example codes.
6. Archive the exact raw response immutably; validate unique series keys, quarter chronology, missing quarters, duplicate observations, units, signs, status flags and revision/vintage metadata.
7. Compare to RBI Table 42 only as a separately labelled national cross-check; do not call it a replacement for IMF BOPS or for the original RBI paper vintage.

## 5. Acceptance matrix
| Gate | Status | Evidence / reason |
|---|---|---|
| Official IMF SDMX structure API route documented | PASS | May-2025 IMF Web Services Guide |
| Public registry HTML reachable | PASS | IMF SDMX Central registrations page |
| Current IMF BOP DSD identifier surfaced | PARTIAL | Search-indexed registry shows IMF:BOP 2.6.0; full structure payload not captured |
| Exact current BOP dataflow ID/version | UNKNOWN | Not resolved from a successful structure response |
| India REF_AREA and quarterly constraints | NOT_DONE | Relevant current codelists not captured |
| BOP item codes and sign/unit metadata | NOT_DONE | No validated current DSD/codelist extraction |
| IMF India quarterly raw observations | NOT_ACQUIRED | No successful data query |
| Vintage-preserving archive + SHA-256 | NOT_DONE | No raw observation bytes |
| Independent reproduction of RBI sudden-stop episodes | NOT_DONE | Requires exact raw quarterly series and edge-case replication |

## 6. Decisions and invariants
- Observation phase remains OPEN. Planning and Organizing remain NOT_STARTED.
- No dataflow, item code, dimension key, unit, sign conversion, or missing-value treatment is guessed.
- No synthetic observations, interpolation, fabricated timestamps or silent deduplication.
- ₹0 spend; official/free sources only.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged.
- UNKNOWN is never PASS. GCR is NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.

## 7. Next highest-value action
Execute a bounded, read-only retrieval of the exact IMF BOP Dataflow + DSD + referenced codelists from the documented SDMX structure API, archive those metadata bytes and hashes, then determine whether an India quarterly data query can be made without authentication. If the live structure response cannot be retrieved, record the precise HTTP/network failure and stop rather than guessing.
