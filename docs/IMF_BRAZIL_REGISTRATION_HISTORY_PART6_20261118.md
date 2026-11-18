# IMF Brazil Reconstruction — Continuation Page 36 — Part 4
Date: 2026-11-18

## Purpose
A bounded re-check of the official IMF public surfaces after Part 5. This page does not claim to have retrieved Brazil historical registration events.

## Fresh official-surface observations
1. The current Registrations page exposes a current-state row for `IMF:BOP6(1.0)`, provider `IMF:BR1`, registered BCB URL, and Last Updated `2026-10-26T11:47:29.000Z`. This is current registration metadata only; it is not a dated create/replace/delete event history.
   Source: https://sdmxcentral.imf.org/data/registrations.html
2. The public Data Registrations activity page continues to expose the four views (Breakdown By Provision Agreement, Breakdown By Dataflow, Breakdown By Data Provider, Show All Data Registrations), but the accessible page extraction shows no event rows. Interactive filtering for exact `IMF:BR1` remains NOT_DONE.
   Source: https://sdmxcentral.imf.org/activity/data-log.html
3. The IMF search/export interface explicitly warns that neither Data Registrations nor Metadata Sets may be downloaded through its generic structure-export facility. This is a useful boundary for avoiding a false assumption that the structure export will supply registration history.
   Source: https://sdmxcentral.imf.org/search.html
4. The documented candidate Provision Agreement structure query was retried through the available browser retrieval interface and again returned an internal access error. This is a retrieval-tool limitation only; no HTTP status, payload, endpoint outage, or invalidity is inferred.
   Candidate URL: https://sdmxcentral.imf.org/sdmx/v2/structure/provisionagreement/IMF/all/latest?references=none

## Acceptance state
| Item | Status |
|---|---|
| Current Brazil registration row visible | PASS (current-state only) |
| Exact IMF:BR1 provider identity | PASS (prior official directory evidence) |
| Public history page and filter modes identified | PASS |
| Actual Brazil historical event rows retrieved | NOT_DONE |
| Brazil Provision Agreement URN and dated changelog | NOT_DONE |
| Create/replace/delete chronology | UNKNOWN |
| BOP6 vs BOP_BPM6 mismatch | CONFIRMED |
| Brazil admission / EM aggregation / market use | BLOCKED / NOT_AUTHORIZED |

## Decision and next action
No further public static extraction can safely advance the historical chronology. The next required action is an interactive official-GUI operation: Data Registrations -> Breakdown By Data Provider -> exact `IMF:BR1`; capture the actual dated rows and Registration Details; then open the linked Provision Agreement and capture its URN and Changelog/exports. If the UI requires an authorized session or yields no rows, preserve that exact limitation and remain UNKNOWN. No guessed identifiers, undocumented endpoints, or FMR submission interface as a read API.

## Guardrails
No repeated RSS/BCB payload downloads. No production integration, PR merge, or trading admission. Macro overlay remains deferred until Brazil Reconstruction is evidence-backed closed. ₹0 spend; free official sources only; no synthetic data or fabricated timestamps. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is not PASS.
