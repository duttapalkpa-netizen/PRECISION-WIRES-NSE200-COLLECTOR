# গবেষণা যাচাই অব্যাহত 36 — Part-8: IMF Brazil registration event ingestion contract
Date: 2026-11-18

## Purpose
Turn official IMF notification documentation into a deterministic, auditable acceptance contract for future event evidence. Documentation/specification only; no production pipeline or subscription is activated.

## Official source facts (IMF SDMX Central User Guide, last updated May 2025)
Source: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralUserGuide.pdf
- Section 6, pp.16–17: Registrations table includes Dataflow, Data Provider, URL, Last Updated. The Data Provider column has a dropdown filter. IMF says to contact IMF to ensure a Data Provider has been configured.
- Register URL creates a data registration event and updates Last Updated.
- Re-Register of an existing selected URL also updates Last Updated to the new registration event time. Hence Last Updated alone is not original-registration chronology.
- Section 7, pp.18–19: RSS is https://sdmxcentral.imf.org/rss.xml and updates on transactions including structure additions/modifications/deletions and data registrations/deletions. Each RSS item links to an SDMX 2.1 RegistryInterface document containing either SubmitStructureRequest or SubmitRegistrationRequest.
- Subscription UI offers All Data Events / All Structure Events, Refine Events, and an Event Filter column. Exact supported filter dimensions are not enumerated in the guide; provider-specific filtering remains NOT_DONE until interactively verified.
- Email subscriptions require a valid email and selected events; no IMF SDMX Central account is required. If not already authenticated with matching account email, a confirmation email completes the subscription. Email notifications include a ZIP with the SDMX change document. HTTP POST notifications carry a RegistryInterface document with Content-Type application/text.

## Deterministic evidence-ingestion contract (proposed; not yet implemented)
### Input provenance
For every notification, preserve immutable raw inputs:
- Original RSS item XML (or full RSS response snapshot)
- Exact linked RegistryInterface SDMX-ML 2.1 document
- For email route: original .eml including headers + original ZIP attachment bytes
- For POST route: raw request body + received headers + receiver timestamp
- Retrieval/receipt timestamp in UTC, source URL, HTTP metadata if available, and SHA-256 for each raw file
Never replace raw evidence with normalized output.

### Classification (strict)
1. Parse XML namespace-aware; do not rely on prefix strings alone.
2. Accept only a well-formed SDMX RegistryInterface 2.1 document.
3. Classify by actual root/child request element:
   - SubmitRegistrationRequest => registration-event candidate
   - SubmitStructureRequest => structure event; NOT a data-registration event
   - Anything else => UNKNOWN / quarantine, not PASS
4. Extract actual transaction action, provider, dataflow, registration URL, Provision Agreement references and identifiers only when present in the payload. Missing fields remain null/UNKNOWN; never infer from RSS headline or timestamp.
5. Preserve full XML subtree and original namespace URIs for audit.

### Brazil exact-match gate
A record is Brazil-related only if the payload itself contains a supported exact match:
- Data Provider URN IMF:BR1, and/or
- exact BCB registration URL:
  https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
Any candidate match must then be cross-checked against the actual Dataflow URN and Provision Agreement URN. A dataflow name alone, country narrative, transaction timestamp, or Chile/Brazil-like text is insufficient.
- IMF:CL_* / si3.bcentral.cl is not Brazil; preserve as explicit negative-control case.
- IMF:BOP6(1.0) and IMF:BOP_BPM6(1.0) remain distinct identifiers. Do not normalize one into the other.

### Event chronology
- Maintain separate event records for Register / Re-Register / Delete only when the transaction payload proves the action.
- Last Updated from the current registrations table is a current-state display value; it must not overwrite event chronology.
- A Delete followed by Register or Replace must be ordered by transaction event timestamps, with source document hash retained.
- If no historical create event is observed, original creation date remains UNKNOWN; do not backfill from current Last Updated.

### QA / acceptance tests
| Test | Required result |
|---|---|
| Valid SubmitRegistrationRequest with exact IMF:BR1 | Brazil registration candidate; PASS only after full field/provenance checks |
| Valid SubmitStructureRequest mentioning Brazil only in text | NOT Brazil registration; classify structure event |
| SubmitRegistrationRequest for IMF:CL2 / si3.bcentral.cl | Reject as Brazil; negative control |
| Payload contains only BOP6 but no provider/BCB URL | UNKNOWN / insufficient Brazil attribution |
| Payload contains BOP_BPM6 but provider/URL conflict | QUARANTINE / mismatch review |
| Malformed XML / unknown namespace / unexpected request type | QUARANTINE; never PASS |
| Duplicate delivery of same raw document hash | Idempotent duplicate; do not double-count event |
| Missing transaction timestamp or action | UNKNOWN; do not synthesize |
| Current Last Updated timestamp without event document | Current-state evidence only; not historical event |

## Current project disposition
- This contract is proposed documentation, not code, not deployed, not tested against a newly received Brazil transaction.
- Official guide semantics and documented notification channels: PASS.
- Exact subscription Refine Events filter dimensions: NOT_DONE.
- Owner subscription activation: NOT_DONE.
- Brazil-specific historical event payload: NOT_DONE.
- Registration chronology: UNKNOWN.
- BOP6 vs BOP_BPM6 mismatch: CONFIRMED.
- Brazil admission / EM aggregation / market use: BLOCKED / NOT_AUTHORIZED.

## Exact next action
Owner may optionally subscribe through official Subscribe to Changes -> All Data Events -> inspect Refine Events; no subscription is activated by this report. For historical recovery, owner must export a selected transaction's SDMX-XML/CSV if available. When raw event files are supplied, implement this contract as a short isolated parser/QA test workflow (no collector trigger), produce raw+parsed evidence and SHA-256, and run the negative controls above.

## Guardrails
₹0, official sources only. No synthetic data, no guessed endpoints or IDs, no fabricated chronology. No production integration, no PR merge, no Brazil/EM admission, no macro overlay weighting. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is not PASS.
