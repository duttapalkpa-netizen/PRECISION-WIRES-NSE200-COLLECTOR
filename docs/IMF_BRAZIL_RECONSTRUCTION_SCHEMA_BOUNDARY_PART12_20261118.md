# গবেষণা যাচাই অব্যাহত 36 — Part-12: SDMX 2.1 schema boundary and final Brazil evidence handoff
Date: 2026-11-18 (Asia/Kolkata)
Scope: official SDMX schema availability check, parser capability boundary, and exact evidence required to close Brazil Reconstruction.

## Decision
**BRAZIL RECONSTRUCTION REMAINS INCOMPLETE / BLOCKED.** This checkpoint does not manufacture missing historical facts. The decisive missing inputs remain the official Brazil-specific registration event exports and the linked Provision Agreement history.

## New official-source check
- The SDMX XML Schemas publisher states that it publishes official XSD schemas for SDMX-ML, including registry operations, and lists the SDMX 2.1 schema set: https://xml.sdmx.org/2.1 (source index: https://xml.sdmx.org/).
- The SDMX 2.1 index explicitly lists `SDMXRegistry.xsd`, `SDMXRegistryBase.xsd`, `SDMXRegistryRegistration.xsd`, and related schema files. The browser retrieval of the linked XSD returned an unsupported XML content-type error; therefore the XSD body was **not inspected or locally validated** in this step.
- Official IMF Web Services Guide example documents the `SubmitRegistrationsRequest` envelope containing `RegistrationRequest action="Replace"`: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf.
- These sources support the envelope/schema reference only. They do not provide Brazil's actual registration events or PA URN/changelog.

## Parser capability boundary (re-fetched default branch)
- Parser blob: `a51dc69b28d244642736eca47e945bdd5b3d3459`.
- Test blob: `a75a68e170fb18eab8c7480b05cc22debc249d5f`.
- Parser checks XML well-formedness, RegistryInterface root namespace, supported request envelope, exact provider or exact BCB URL evidence, and emits candidate/UNKNOWN rather than PASS.
- It is **not** a complete SDMX 2.1 XSD validator or semantic validator. It does not currently prove every Registration has a valid ProvisionAgreement reference, a valid DataProvider/Dataflow reference, or that the extracted action/time/URN set is semantically complete.
- Existing local regression result remains 9/9 PASS from Part-10. This is fixture QA only, not schema validation, not GitHub Actions runtime evidence, and not real Brazil event validation.
- No parser code change is justified without the actual source transaction payload and inspected schema details. Do not weaken exact-match gates.

## Closure handoff — minimum owner export
The repository owner must provide the following official exports (no credentials):
1. Data Registrations result filtered to exact Data Provider `IMF:BR1`, including every visible matching row and all detail fields.
2. Each linked Provision Agreement record: exact URN, agency, version, valid-from/to, revisions, annotations and dated changelog/export.
3. For every relevant transaction, original Download Transaction SDMX-XML and/or View Details CSV, preserving source URL, retrieval timestamp, response metadata, raw bytes and SHA-256.
4. If the UI presents pagination/date filters, export all pages/date ranges needed to cover the earliest available record through the current row; record filter and range explicitly.
5. Do not send passwords, session cookies, API tokens or other credentials. Raw official files alone are sufficient for offline analysis.

Upon receipt, perform in a short isolated task:
- hash and inventory every raw file;
- validate XML against the official SDMX 2.1 registry XSD locally where dependencies permit, recording validator/version and exact schema hashes;
- parse actual event timestamps/actions and exact Data URL, PA URN, Dataflow URN, Data Provider URN;
- deduplicate by source transaction identity without discarding repeated Replace/Re-Register events;
- reconcile the complete event sequence to the current `IMF:BR1` row and BCB payload Dataflow;
- independently review the BOP6 vs BOP_BPM6 mismatch and document authoritative resolution or retain BLOCKED.

## Acceptance matrix update
| Component | Status |
|---|---|
| Official SDMX 2.1 XSD index located | PASS (index only) |
| XSD body inspected / local validation | NOT_DONE |
| Parser local regression fixtures | PASS (9/9; fixture-only) |
| Parser full XSD/semantic validation | NOT_DONE |
| Brazil-specific registration event rows | NOT_DONE |
| Brazil Provision Agreement URN/changelog | NOT_DONE |
| Create/Replace/Delete/Re-Register chronology | UNKNOWN |
| Event-to-current-row reconciliation | BLOCKED |
| Brazil/EM admission and market use | BLOCKED / NOT_AUTHORIZED |

## Guardrails
- No synthetic evidence, guessed transaction IDs/endpoints, inferred chronology, or fabricated timestamps.
- Do not treat Last Updated as original registration date.
- Do not repeat the completed 33-item RSS window or BCB download without new source evidence.
- ₹0 spend; official/free sources only.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. No production integration, PR merge, macro weighting or trading admission.
- UNKNOWN is not PASS.

## Exact next action
**Await the owner-exported IMF:BR1 registration-history rows + Provision Agreement changelog + original transaction XML/CSV.** Until those primary records are supplied, Brazil Reconstruction cannot truthfully be marked complete.
