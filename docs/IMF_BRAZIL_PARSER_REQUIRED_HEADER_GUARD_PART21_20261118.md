# IMF Brazil Parser Required Header Guard — Part 21
Date: 2026-11-18
Scope: QA-only SDMX 2.1 message-envelope guard; no production changes.

## Source basis
Pinned official source: `sdmx-twg/sdmx-ml@v2.1`, tag target commit `bc28a2255966a3b8d33ec8f61e19f42e6e193284`.
The pinned `schemas/SDMXMessage.xsd` defines RegistryInterfaceType as a sequence with a required `Header` of BasicHeaderType followed by an optional choice of message payload. Therefore, a schema-shaped RegistryInterface must have exactly one direct Header in first-child position. A parser that only checks for a payload can accept malformed envelopes that an XSD validator would reject.

## Change
- Parser now checks exactly one direct Header in the message namespace.
- Header must be the first direct child of RegistryInterface.
- Missing, misplaced, or duplicate Header causes QUARANTINE / FAIL before payload interpretation.
- Existing message/registry namespace separation from Part-19 remains unchanged.

## Regression tests added
- Missing required Header -> QUARANTINE.
- Header after payload -> QUARANTINE.
- Duplicate Header -> QUARANTINE.

## Git evidence
- Parser commit: `2b91d3698518b487cf980e89479223cc65632f0b`; blob `85f089d5f9c6f6f1376ab5bd5705c064334cc14c`.
- Test commit: `9247ae489fabc9cbfa383068419ff73a8731f8e2`; blob `636d171940b0b654a9185ebb97fb08f3c3af6ae9`.
- Branch: `qa/imf-brazil-parser-schema-path-hardening`.
- The new tests were added but were NOT executed in a local Python runtime in this part. GitHub Actions is also NOT_VERIFIED. Do not describe this change as test-PASS.

## Acceptance
- Required Header guard code present: PASS (fetchback verified).
- Three regression tests present: PASS (fetchback verified).
- Test execution: NOT_VERIFIED.
- Formal offline XSD validation: NOT_DONE.
- Full 58-file schema archive and raw-byte SHA-256 manifest: NOT_DONE.
- Full dependency closure: NOT_DONE.
- Real Brazil transaction evidence and chronology: NOT_DONE / UNKNOWN.
- BOP6 vs BOP_BPM6 mismatch: CONFIRMED / UNRESOLVED.
- Brazil/EM admission: BLOCKED / NOT_AUTHORIZED.

## Environment limitation
A direct network fetch from the local execution container failed with DNS resolution unavailable. GitHub connector could inspect the official pinned raw XSD text, but this did not create a local byte-exact archive. Thus no local schema validator, bundle or SHA-256 manifest was produced.

No merge, production integration, workflow dispatch, paid API, full NSE collector, market-data modification, macro weights or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
