# গবেষণা যাচাই অব্যাহত 36 — Part-11: Brazil Reconstruction acceptance gap matrix
Date: 2026-11-18 (Asia/Kolkata)
Scope: evidence-backed closure assessment of Brazil historical IMF registration reconstruction. This is a reconciliation checkpoint, not a claim that reconstruction is complete.

## Executive decision
**BRAZIL RECONSTRUCTION: INCOMPLETE / BLOCKED.**
The repository has established a real current-state registration/payload Dataflow mismatch and built/tested a conservative offline parser. It has not recovered the Brazil-specific historical registration event rows, the governing Provision Agreement identity/change history, or a verified create/replace/delete/re-register chronology. No Brazil historical reconstruction can be accepted until those primary records are obtained and reconciled.

## Reconciled evidence already established
1. Current IMF registration listing shows Dataflow `IMF:BOP6(1.0)`, Provider `IMF:BR1`, registered BCB XML URL, Last Updated `2026-10-26T11:47:29.000Z`. This is current-state metadata only; Last Updated is not proven to be the original registration timestamp.
2. The registered BCB XML payload declares `IMF:BOP_BPM6(1.0)`. Exact Dataflow identifiers differ; same DSD does not make them equivalent.
3. Constraint compatibility is 234/237 (98.7342%) for BOP6 and 27/237 (11.3924%) for BOP_BPM6. Mismatch remains CONFIRMED; do not normalize one identifier into the other.
4. The archived 33-item IMF RSS transaction window was retrieved/resolved; all 33 transaction URLs returned HTTP 200 and well-formed successful QueryRegistrationResponse documents. No Brazil marker was found in that bounded window. This does not establish absence outside the sampled window.
5. The official IMF historical activity UI exposes the relevant registration fields (Date, Data URL, Action, Provision URN, Dataflow URN, Data Provider URN, User), but static extraction did not yield Brazil-specific rows. The public Transactions UI sample is not exhaustive and does not identify Brazil.
6. The IMF documentation reviewed describes RSS/notification and FMR activity mechanisms; no official public REST registration-history read API has been established. Undocumented endpoints and guessed transaction IDs are excluded.
7. Offline parser current default-branch source and nine unit tests were re-fetched; local unit suite passed 9/9. It is a conservative candidate parser, not a complete SDMX semantic validator and not proof of a real Brazil event. GitHub Actions runtime remains NOT_YET_VERIFIED.

## Acceptance matrix
| Required reconstruction component | Status | What is still missing |
|---|---|---|
| Current registry row identity | PASS (current-state only) | Historical meaning not inferred |
| BCB payload identity and hash | PASS (archived prior evidence) | No new fetch required absent source change |
| Registry-vs-payload Dataflow mismatch | CONFIRMED | Authoritative IMF resolution/correction |
| Recent RSS sample inspection | PASS (bounded 33-item window) | No inference outside sample |
| Historical Brazil event rows | NOT_DONE | Actual IMF:BR1-specific dated registration transactions |
| Create / Replace / Delete / Re-Register chronology | UNKNOWN | Original transaction event payloads and timestamps |
| Provision Agreement URN and changelog | NOT_DONE | Exact Brazil PA record and dated revision/change history |
| Event-to-current-row reconciliation | BLOCKED | Need event action, provider, Dataflow, URL and PA identity |
| Parser regression suite | PASS (local 9/9) | Real transaction fixture validation |
| GitHub Actions runtime | NOT_YET_VERIFIED | Exact run ID, conclusion and job log |
| Brazil data admission / EM aggregation / market use | BLOCKED / NOT_AUTHORIZED | Complete authoritative reconciliation and explicit acceptance |

## Exact closure requirements
A future closure package must contain, for each actual Brazil registration event:
- immutable original SDMX-XML or official CSV export; raw byte count and SHA-256;
- official source URL, retrieval timestamp, response metadata where available;
- event timestamp and action exactly as represented by the source;
- exact Data URL, Provision Agreement URN, Dataflow URN and Data Provider URN;
- parser output linked to the original file hash;
- independent manual review of the event semantics and duplicate/re-registration handling;
- a reconciled timeline explaining whether the mismatch is caused by create/replace/delete/re-register, stale URL, provider reassignment, or an authoritative IMF explanation;
- final decision supported by the IMF record, not by assumption.

## Immediate next action / dependency
The remaining high-value step is **interactive retrieval of the actual historical registration evidence from the official IMF SDMX Central GUI**:
1. Data Registrations -> Breakdown By Data Provider -> exact `IMF:BR1` filter (if available).
2. Capture all relevant dated rows and Registration Details.
3. Open each linked Provision Agreement and capture exact URN plus Changelog/exports.
4. For any required transaction, use the official transaction Download/View Details control to export the SDMX-XML/CSV.
5. If the GUI requires authenticated access or the filter/export cannot be completed anonymously, the repository owner must export the official records and provide the raw files. No credentials are requested here.

Until these primary records exist, do not attempt to infer chronology from RSS item order, Last Updated, generic structure events, or the 33-item sample. Do not repeat the already completed RSS/BCB downloads merely to create activity.

## Status and guardrails
- Brazil Reconstruction: **INCOMPLETE / BLOCKED** (no percentage assigned; required primary evidence is missing).
- Parser module: local regression QA **9/9 PASS**; GitHub Actions runtime **NOT_YET_VERIFIED**.
- BOP6 vs BOP_BPM6 mismatch: **CONFIRMED**.
- Historical chronology: **UNKNOWN**.
- ₹0 spend; official/free sources only. No synthetic records, guessed IDs, undocumented endpoints, fabricated timestamps, production integration, PR merge, or trading admission.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
