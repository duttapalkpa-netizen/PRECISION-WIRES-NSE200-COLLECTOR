# IMF Brazil Parser Registry Namespace Correction — Part 19
Date: 2026-11-18
Scope: QA-only parser correctness fix based on the pinned official SDMX-ML 2.1 XSD source. No production changes.

## Critical defect found
Review of the pinned official SDMX-ML v2.1 schemas showed a namespace boundary that the Part-16 parser and its fixtures had modelled incorrectly:
- `RegistryInterface` and its direct `SubmitRegistrationsRequest` / `SubmitStructureRequest` payload elements are in the SDMX message namespace `http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message`.
- The payload's typed content `RegistrationRequest`, `Registration`, `ProvisionAgreement`, and `Datasource` are defined in the SDMX registry namespace `http://www.sdmx.org/resources/sdmxml/schemas/v2_1/registry`.
- The old helper used the message namespace for all nested children and the synthetic fixtures inherited the same namespace throughout. This meant tests could pass while real namespace-correct registry children were not recognized by the parser.

Official source files inspected at pinned tag `sdmx-twg/sdmx-ml@v2.1`:
- `schemas/SDMXMessage.xsd`: declares RegistryInterface and direct SubmitRegistrationsRequest as message-namespace elements whose type is `registry:SubmitRegistrationsRequestType`.
- `schemas/SDMXRegistryRegistration.xsd`: defines RegistrationRequest under the registry target namespace.
- `schemas/SDMXRegistryBase.xsd`: defines Registration, ProvisionAgreement, and Datasource under the registry target namespace.
Pinned tag target commit: `bc28a2255966a3b8d33ec8f61e19f42e6e193284`.

## Correction
- Added `REG_NS` constant to `scripts/research/imf_brazil_event_parser.py`.
- Updated `children_named()` to match registry namespace children, while retaining message-namespace checks for the root and direct payload.
- Reworked fixtures so registry payload children use an explicit `r:` namespace binding.
- Rewrote narrative negative controls so they exercise actual nested registry elements, rather than accidentally becoming malformed XML or nested fake payloads.
- Added a negative test ensuring message-namespace lookalikes are quarantined instead of being mistaken for registry elements.

## Git evidence
- Parser commit: `bfb8aa61a1f2776642523eaa6535c370807b90a8`; blob `6b55c553870a0164da315975107c760394fbc044`.
- Test commit: `bf839e2a6a764674c07edb732e59cb3f79beac8c`; blob `afc6da903771697f98a2d8e84407cf79f188e3f1`.
- Branch: `qa/imf-brazil-parser-schema-path-hardening`.
- PR #39 remains open, draft, unmerged.
- PR-triggered Actions lookup for the latest head returned an empty list; GitHub Actions remains NOT_VERIFIED.

## Local verification
A local isolated replay of the fetched parser logic and all 13 fixture scenarios was run after the namespace correction:
- Result: **13 passed, 0 failed**.
- This replay was executed in a local Python test harness using the fetched source/test logic; it is not a GitHub Actions run and not formal XSD validation.
- A targeted XML structure probe independently confirmed: direct payload namespace = message; RegistrationRequest/Registration/ProvisionAgreement/Datasource namespace = registry; exact PA URN and BCB URL were discoverable in their respective subtrees.

## Acceptance
- Registry namespace handling corrected: PASS (QA branch).
- Fixtures use explicit registry namespace: PASS.
- 13 isolated local test scenarios: PASS.
- GitHub Actions: NOT_VERIFIED.
- Formal XSD validation: NOT_DONE.
- Full 58-file XSD archive and SHA-256 manifest: NOT_DONE.
- Genuine Brazil registration event fixture and historical chronology: NOT_DONE / UNKNOWN.
- BOP6 vs BOP_BPM6 mismatch: CONFIRMED / UNRESOLVED.
- Brazil/EM admission: BLOCKED / NOT_AUTHORIZED.

No merge, production integration, workflow dispatch, paid API, full NSE collector, market data modification, macro weights or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
