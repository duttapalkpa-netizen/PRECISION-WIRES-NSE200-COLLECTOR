# IMF Brazil Parser QA Pull-Request Trigger Enablement — Part 18
Date: 2026-11-18
Scope: CI trigger wiring only. QA branch only; no production change.

## Baseline issue
The existing workflow `.github/workflows/imf_brazil_event_parser_qa.yml` had only `workflow_dispatch` and `push: branches: [main]`. Therefore the open QA draft PR #39 did not automatically execute this offline parser test workflow on pull-request commits.

## Change
Added a `pull_request` trigger targeting `main`, with the same narrow path filters:
- `scripts/research/imf_brazil_event_parser.py`
- `tests/test_imf_brazil_event_parser.py`
- `.github/workflows/imf_brazil_event_parser_qa.yml`

Preserved:
- manual `workflow_dispatch`
- main-only push trigger
- read-only `contents: read` permission
- ubuntu-latest runner
- Python 3.12
- 3-minute job timeout
- offline unittest command only; no network or secrets.

## GitHub evidence
- Workflow update commit: `1c76b0f6241d1fdcc8be74917f2632a629438ce3`
- Workflow blob after fetchback: `e71c4e27dc336816e7b102de96d6b361da1969f6`
- Pull request #39 rechecked: open, draft=true, merged=false.
- Workflow file fetchback confirms the `pull_request` trigger.
- The available PR-triggered workflow-run lookup returned an empty list at verification time. Therefore **GitHub Actions execution is NOT_VERIFIED / no run evidence yet**. Do not report CI PASS.

## Acceptance
- PR trigger added: PASS (QA branch).
- Trigger file fetchback: PASS.
- PR #39 remains draft/unmerged: PASS.
- GitHub Actions run result: NOT_VERIFIED (empty workflow-run list).
- Local Part-16 tests remain 12/12 PASS only; this is not CI evidence.
- Formal XSD validation remains NOT_DONE; official 58-file bundle/hash manifest remains NOT_DONE.
- Real Brazil event evidence and historical chronology remain NOT_DONE/UNKNOWN.
- BOP6 vs BOP_BPM6 mismatch remains CONFIRMED / UNRESOLVED; Brazil/EM admission BLOCKED.

No workflow dispatch, merge, production integration, full NSE collector, external API, paid service, or data acquisition was performed. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
