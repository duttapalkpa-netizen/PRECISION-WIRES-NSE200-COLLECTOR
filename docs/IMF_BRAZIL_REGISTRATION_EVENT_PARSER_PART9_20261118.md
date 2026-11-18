# গবেষণা যাচাই অব্যাহত 36 — Part-9: IMF Brazil event parser and isolated QA workflow
Date: 2026-11-18

## Progress Log
### Reused completed evidence
- Parts 1–8 and the Master Continuity Acceptance Ledger were reviewed before implementation.
- Existing archived 33 RSS transaction resolver and its bounded result were not rerun.
- Existing resolver workflow is a separate 8-minute job; the new QA workflow does not call it and does not fetch RSS/BCB data.
- Prior false positive preserved: IMF:CL_* / si3.bcentral.cl is Chile, not Brazil.
- Hard rule retained: UNKNOWN is not PASS; current Last Updated cannot establish original registration chronology.

## Deliverables added
1. `scripts/research/imf_brazil_event_parser.py`
   - Offline-only; accepts local XML paths and does not make network requests.
   - Namespace-aware validation of RegistryInterface 2.1 root namespace.
   - Strictly distinguishes SubmitRegistrationRequest from SubmitStructureRequest.
   - Exact Brazil matching only on IMF:BR1 or the full BCB URL; no substring/country-name inference.
   - Emits SHA-256, byte count, raw evidence values and conservative status.
   - Even an exact Brazil candidate is not automatically PASS; it is marked REQUIRES_MANUAL_EVIDENCE_REVIEW pending action, timestamp, Dataflow and Provision Agreement checks.
2. `tests/test_imf_brazil_event_parser.py`
   - Seven unit tests: exact provider candidate; exact BCB URL candidate; structure-only request; Chile negative control; BOP6-only insufficient attribution; wrong namespace quarantine; malformed XML quarantine.
3. `.github/workflows/imf_brazil_event_parser_qa.yml`
   - Manual + path-scoped push trigger only for parser/test/workflow files.
   - Python 3.12, offline unit tests, timeout 3 minutes, contents read-only.
   - No RSS/BCB acquisition, no full NSE collector, no production data writes.

## Change commits
- Parser: `27f26223f46f549107e55f17c7957660a00c94c2`
- Initial tests: `fa755e5be28fd473fea0b66e4af37a91daa131ff`
- Workflow: `cd15fd0aca53beb4e93b0af465c954b6ffc50006`
- Corrected malformed-XML assertion: `5dd500c3c061954eb2af1e4e77d1943dcd72620b`

## Acceptance status
| Item | Status |
|---|---|
| Parser source committed | PASS |
| Unit-test source committed | PASS |
| Isolated short workflow committed | PASS |
| Malformed XML test assertion corrected | PASS |
| GitHub Actions execution result | PENDING / not yet independently verified |
| Real IMF Brazil transaction fixture | NOT_DONE |
| Parser against a real Brazil event | NOT_DONE |
| Brazil chronology | UNKNOWN |
| BOP6 vs BOP_BPM6 mismatch | CONFIRMED |
| Brazil admission / EM aggregation / market use | BLOCKED / NOT_AUTHORIZED |

## Important limitations
- This is an offline parser for the documented request envelope, not a complete SDMX registration semantic validator.
- The parser does not infer Register/Re-Register/Delete from arbitrary XML text. It records only narrowly recognized action candidates and preserves all evidence values for review.
- A provider or URL exact match produces a candidate, never an automatic PASS. The actual transaction payload, event action/time, Dataflow URN and Provision Agreement URN still require review.
- No real event payload was available; synthetic unit fixtures validate conservative logic only and are not research observations.

## Exact next action
Check the isolated GitHub Actions run triggered by these scoped commits. If it fails, fix only the failing parser/test and rerun this short workflow. When an owner-exported actual IMF RegistryInterface XML/CSV becomes available, add a separately hashed real fixture (with sensitive email headers removed only from a working copy; preserve original privately) and test without promoting Brazil until all provenance and URN checks pass.

## Guardrails
₹0 official/free sources only. No guessed endpoints, no synthetic market data, no invented timestamps. No production integration, no PR merge, no Brazil/EM admission, no macro overlay weights. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.


## Part-9 correction — SDMX 2.1 registration envelope verified
- Official IMF Web Services Guide example uses the plural request element `SubmitRegistrationsRequest`, containing `RegistrationRequest action="Replace"`; the earlier parser initially accepted only the singular form. This was corrected to accept the documented plural form while retaining the singular compatibility form.
- Tightened the BCB URL gate: it now requires the exact full URL as a complete XML text/attribute value. A URL merely embedded in descriptive prose is not accepted.
- Expanded unit coverage from 7 to 9 tests: added exact URL whole-value negative control and RegistrationRequest action-attribute capture. Fixtures now use the documented plural envelope.
- Parser correction commits: `9004edf15e86befb841ee2c5a48761f6131b913c5` (plural envelope), `59efd1a51dac3d4390fc4530613d68c033c22cb3` (exact URL gate).
- Test correction commits: `1669ee9cd0be3a589fb1a0539169a016cd42f537` (plural fixtures), `d3a3b9c9936fa78d7939821096f4dc2b167cbecc` (two additional tests).
- This correction is grounded in the IMF Web Services Guide example, which identifies SubmitRegistrationsRequest and RegistrationRequest action. It is not a claim that a Brazil transaction was found.
- GitHub Actions execution remains NOT_YET_VERIFIED; the workflow is path-triggered by parser/test changes, but no run result has been independently fetched in this review.
