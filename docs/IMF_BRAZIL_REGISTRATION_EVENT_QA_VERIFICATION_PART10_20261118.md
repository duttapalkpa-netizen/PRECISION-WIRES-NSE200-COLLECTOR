# গবেষণা যাচাই অব্যাহত 36 — Part-10: IMF Brazil parser QA verification checkpoint
Date: 2026-11-18

## Objective
Verify the already-committed Part-9 offline parser and its nine regression tests without repeating RSS/BCB acquisition, changing parser logic, or triggering the full NSE collector.

## Re-opened default-branch sources
- Parser: `scripts/research/imf_brazil_event_parser.py`, current blob SHA `a51dc69b28d244642736eca47e945bdd5b3d3459`.
- Tests: `tests/test_imf_brazil_event_parser.py`, current blob SHA `a75a68e170fb18eab8c7480b05cc22debc249d5f`.
- Workflow: `.github/workflows/imf_brazil_event_parser_qa.yml`, current blob SHA `43d9f5c77c7abe4d05ffb446d2ed1c9b0a343b9b`.
- Part-9 report: `docs/IMF_BRAZIL_REGISTRATION_EVENT_PARSER_PART9_20261118.md`, blob SHA `a7d73193f0cfe00d8d1a98fb4f1af037e05789d3`.
- Master ledger before this update: blob SHA `f165a3e4f5f8c16e0ee0c60cc6d6ebf9a65cd857`.

## QA execution performed
- Copied the exact fetched parser and test source contents into an isolated local temporary directory; no source edits were made.
- Executed: `python -m unittest discover -s tests -p 'test_imf_brazil_event_parser.py' -v`.
- Result: **9 tests passed, 0 failed**, runtime approximately 0.002 seconds.
- Covered exact provider candidate/no auto-PASS, exact BCB URL, embedded-URL negative control, RegistrationRequest action capture, structure-only event, Chile negative control, BOP6-only insufficient attribution, wrong namespace quarantine, malformed XML quarantine.
- This is an independently executed local unit-test result against the currently fetched default-branch source, not a GitHub Actions run and not a real Brazil transaction validation.

## GitHub Actions status retrieval boundary
- Attempted the available connected GitHub commit-workflow-run lookup for test commit `d3a3b9c9936fa78d7939821096f4dc2b167cbecc`; it returned an empty run list.
- The connected action explicitly filters to pull-request-triggered runs and returns only the first page. Therefore the empty response cannot establish that the push-triggered workflow did not run, nor can it establish SUCCESS.
- No general Actions run-list / workflow-dispatch operation is exposed by the connected GitHub tool set in this session. Thus GitHub Actions run ID, conclusion, job log and artifact remain **NOT_YET_VERIFIED**.
- The workflow definition is scoped to parser/test/workflow paths, Python 3.12, read-only contents, and a 3-minute timeout. This verifies configuration only, not runtime outcome.

## Acceptance matrix
| Check | Status | Evidence |
|---|---|---|
| Current parser source fetched | PASS | blob `a51dc69b28d244642736eca47e945bdd5b3d3459` |
| Current nine-test source fetched | PASS | blob `a75a68e170fb18eab8c7480b05cc22debc249d5f` |
| Workflow definition fetched | PASS | blob `43d9f5c77c7abe4d05ffb446d2ed1c9b0a343b9b` |
| Local regression suite | PASS | 9/9 tests executed successfully |
| GitHub Actions runtime | NOT_YET_VERIFIED | connected run lookup is PR-only; no run-list action |
| Real IMF Brazil event fixture | NOT_DONE | no owner-exported raw transaction supplied |
| Brazil registration chronology | UNKNOWN | no transaction timestamp evidence |
| BOP6 vs BOP_BPM6 mismatch | CONFIRMED | previously verified source/constraint mismatch |
| Brazil / EM / market admission | BLOCKED | no complete event, Dataflow and Provision Agreement reconciliation |

## Next action
If GitHub Actions confirmation is required, inspect repository **Actions → IMF Brazil Event Parser QA (Offline)** and record the exact run ID, conclusion and job log. Do not interpret a missing result from the PR-only connector as failure or success. Once a real IMF RegistryInterface transaction XML/CSV is available, hash and review it separately; synthetic fixtures remain test-only.

## Guardrails
No code change in this checkpoint. No RSS/BCB fetch, no full NSE collector, no production integration, no PR merge, no trading admission, no paid service or spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
