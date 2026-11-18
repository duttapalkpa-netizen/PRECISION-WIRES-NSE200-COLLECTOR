# IMF Brazil Parser QA — Fixture Repair and CI Verification (Part 22)
Date: 2026-11-18

## Outcome
PASS — GitHub Actions Run #21 executed the offline parser suite successfully: 16 tests, 0 failures, 0 errors. This is fixture/test-suite validation only; it is not formal XSD validation and does not establish real Brazil registration chronology.

## Root cause established from Run #19 logs
The test helper generated malformed XML by prepending an extra '<' before the supplied body. Registration fixtures also failed to model the SDMX 2.1 message/registry namespace split. Run #19 showed 3 failures and 2 errors; Run #20 after partial repair showed 1 remaining failure.

## Correction
- Fixed doc() to insert the complete body directly after Header.
- Rebuilt registration fixtures with SubmitRegistrationsRequest in the SDMX message namespace and RegistrationRequest/Registration/ProvisionAgreement/Datasource descendants in the SDMX registry namespace.
- Corrected exact PA/BCB URL fixtures to use registry-namespace elements.
- Preserved negative controls for wrong-namespace lookalikes, narrative text, nested fake payloads, and Header cardinality/order.
- Kept parser conservative: Brazil candidate remains manual-review-only; no candidate is auto-promoted to PASS.

## Git evidence
- Test correction commit: `b83eab54be1cb73dd0a227e05cedb50cb8e3587c`.
- Follow-up assertion correction commit: `36653b0e1ebd718693a79b07da5f9f665e2a8ae1`.
- Final test file blob: `16ba53cc872aa99456fe75982269e9dc7b7e7b10` (Git blob SHA, not SHA-256).
- GitHub Actions Run #21: `44329119370`.
- Workflow: IMF Brazil Event Parser QA (Offline); job parser-qa; conclusion SUCCESS.
- Exact command: `python -m unittest discover -s tests -p 'test_imf_brazil_event_parser.py' -v`.
- Result: `Ran 16 tests ... OK`.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44329119370
- PR #39 remains open, draft, unmerged.

## Scope limits / unresolved items
- Full 58-file XSD archive, complete transitive dependency closure, raw-byte SHA-256 manifest and formal offline XSD validation: NOT_DONE.
- Actual Brazil/BR1 registration transaction timestamps and PA revision/changelog chronology: NOT_DONE / UNKNOWN.
- IMF registration-listing Dataflow BOP6 vs BCB XML payload Dataflow BOP_BPM6 mismatch: CONFIRMED / UNRESOLVED.
- Brazil/EM admission remains BLOCKED. No trading use.

## Safety and invariants
No production selector, scoring, market-data, macro-weight, or trading-admission changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), and Engines A–E remain unchanged. No paid API or subscription. UNKNOWN is not PASS.
