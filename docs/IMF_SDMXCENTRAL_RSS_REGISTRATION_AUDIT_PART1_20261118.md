# IMF SDMX Central RSS & Registration Audit — Part 1
Audit date: 2026-11-18 (Asia/Kolkata)
Continuation: গবেষণা যাচাই অব্যাহত 36
Scope: official-source discovery and registration-page cross-check only; research branch; no production integration.

## 1. Prior-state carry-forward
The user-provided Part-14 screenshot records:
- IMF RSS retrieval: NOT_RETRIEVED.
- IMF Registration History / RSS work: incomplete.
- BCB XML header shown as BOP_BPM6; Dataflow mismatch marked CONFIRMED in the prior screen.
- Brazil flow / Global EM / Trading admission: NOT_AUTHORIZED.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E must remain unchanged.

No previous PASS is re-run or promoted by this note.

## 2. Official RSS route — source discovery
The IMF SDMX Central User Guide documents the RSS URL exactly:
https://sdmxcentral.imf.org/rss.xml
It states the feed is updated when a transaction occurs, including structure additions/modifications/deletions and data registrations/deletions. Each transaction links to an underlying SDMX-ML 2.1 RegistryInterface document containing either SubmitStructureRequest or SubmitRegistrationRequest.
Official guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralUserGuide.pdf
Official RSS URL: https://sdmxcentral.imf.org/rss.xml

Status: PASS — official endpoint route and documented payload semantics located.
Status: NOT_RETRIEVED — no successful HTTP response, raw RSS bytes, response headers, item count, retrieval timestamp, or SHA-256 captured in this Part 1. A browser retrieval attempt from the research environment returned an access/internal error; this is not evidence that the IMF endpoint itself is down.
Therefore RSS ingestion, XML parsing, event extraction, and RSS-to-registration reconciliation remain UNKNOWN / NOT DONE.

## 3. Live Registration page — independent source cross-check
Official registration page:
https://sdmxcentral.imf.org/data/registrations.html

The publicly rendered page currently exposes columns:
Dataflow | Data Provider | URL | Last Updated.

A visible Brazil provider row is:
- Dataflow: IMF:BOP6(1.0)
- Data Provider: IMF:BR1
- URL: https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
- Last Updated: 2026-10-26T11:47:29.000Z

This is evidence that a Brazil registration row is visible in the live registrations listing. It is NOT evidence that the RSS feed was retrieved, that a historical registration event was reconstructed, that the XML payload passed schema/dataflow validation, or that any EM/trading admission was authorized.

## 4. Exact discrepancy to resolve — do not silently normalize
The prior screenshot records a BCB XML header/dataflow value of BOP_BPM6 and a confirmed mismatch. The current IMF registration listing displays the registry dataflow identifier IMF:BOP6(1.0), while its registered URL filename contains BOP_BPM6.
These strings belong to different semantic fields (registry dataflow identifier vs URL filename / XML header claim). The registration row alone cannot establish whether the XML header's DataflowRef is compatible. The raw BCB XML must be retrieved and parsed; preserve exact case and identifier strings. Do not rename BOP_BPM6 to BOP6 or infer equivalence.

## 5. IMF service boundary
The IMF SDMX Central Web Services Guide documents the structure service entry point:
https://sdmxcentral.imf.org/sdmx/v2/
It also states there is no official REST API for data processing services such as validation, conversion, or registration; FMR uses its own entry point:
https://sdmxcentral.imf.org/ws/public/data
Official guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf

Do not confuse the public structure REST API with the RSS transaction feed or the registry's registration records. Each requires its own request and evidence.

## 6. Part-1 acceptance matrix
| Check | Result | Evidence / reason |
|---|---|---|
| Official RSS endpoint identified | PASS | IMF SDMX Central User Guide |
| RSS transaction semantics identified | PASS | SubmitStructureRequest / SubmitRegistrationRequest documented |
| Live registration listing reachable/indexed | PASS | Official registrations page |
| Brazil registration row visible | PASS | IMF:BOP6(1.0), IMF:BR1, URL and last-updated field |
| RSS HTTP response captured | NOT_RETRIEVED | No successful response evidence |
| Raw RSS XML archived + SHA-256 | NOT_DONE | No bytes captured |
| RSS XML parsed and events normalized | NOT_DONE | Dependent on raw retrieval |
| Brazil BCB XML raw bytes + SHA-256 | NOT_DONE | Registration listing is not the payload |
| BCB XML DataflowRef validated against registry | UNKNOWN | Exact header/payload must be parsed |
| Historical registration event reconstructed | UNKNOWN | Requires RSS item + linked RegistryInterface payload |
| Brazil flow / Global EM / Trading admission | NOT_AUTHORIZED | No approval or validated data panel |

## 7. Next bounded action — Part 2
1. Execute a short, isolated HTTP retrieval of https://sdmxcentral.imf.org/rss.xml from the repository CI runner with redirects enabled; capture status, final URL, Content-Type, retrieved_at_utc, byte count, raw bytes and SHA-256.
2. Accept only HTTP 200 + XML content + namespace-aware parse + valid RSS structure. Save malformed/HTML/error responses as failed evidence, not PASS.
3. Extract item title, link, guid, pubDate and linked RegistryInterface URL without inventing timestamps.
4. Fetch only the linked Brazil registration event payload if an actual RSS item exists; preserve raw bytes and hash.
5. Separately retrieve the currently registered BCB XML URL; compare XML Header/DataflowRef and ProviderRef with registry row IMF:BOP6(1.0) / IMF:BR1. Report exact mismatch, if any.
6. Keep the CI job under 10 minutes, preferably a small isolated job. No synthetic data and no production integration.

## 8. Protected invariants and exclusions
- Production Selector unchanged.
- RANKING_SCORE unchanged.
- +1 PRESSURE_FADE unchanged.
- CORE-672 unchanged (56 Steps × 12 Filters).
- Engines A-E unchanged.
- UNKNOWN is not PASS.
- No fabricated timestamps, RSS events, XML identifiers, observations or EM aggregates.
- Free official sources only; research spend ₹0.
- No PR merge or production integration without explicit user approval.

## 9. Provenance and limitations
This Part-1 note distinguishes source-documentation verification and a live registration-page listing from raw RSS retrieval. Search/index access to a rendered official page is not a substitute for archiving raw response bytes. No HTTP success, retrieval time, RSS item count, artifact ID, workflow run ID, or SHA-256 is claimed here.
