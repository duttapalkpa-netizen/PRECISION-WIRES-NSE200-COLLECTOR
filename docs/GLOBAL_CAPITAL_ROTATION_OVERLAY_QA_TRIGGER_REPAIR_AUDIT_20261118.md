# Global Capital Rotation Overlay QA Trigger Repair & Runtime Validation — 2026-11-18

## Outcome
PASS — the isolated Overlay QA workflow now listens to both its original mainline research branch and the active continuation branch. A real push-triggered run completed successfully on the active branch.

## Root cause
Before the change, `.github/workflows/global-capital-rotation-qa.yml` had a push branch filter containing only:
- `research/global-capital-rotation-overlay-mainline-20261113`

The active branch was:
- `research/bcb-priority-metadata-audit-20261117`

Because GitHub applies branch and path filters together, a matching file path on the active branch was insufficient to trigger the workflow. GitHub's official workflow documentation confirms both filters must match when both are configured: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow

## Change
- Added `research/bcb-priority-metadata-audit-20261117` to the existing branch allowlist.
- Preserved the original branch, path filters, 5-minute timeout, Python 3.12, compile step and focused unittest command.
- No parser, registry, seed observation, production selector, ranking, pressure-fade, CORE-672, Engine A–E, Hard Gate or collector code was changed.

Workflow file:
- `.github/workflows/global-capital-rotation-qa.yml`
- Commit: `1f46bcdeb1f6a17dc4e389f9468f5bb52179d133`
- Blob SHA: `ad0efc3644047247045847c8c15f89cb23d5fe9b`

## Runtime evidence
- GitHub Actions run: `44245756372`
- Job/check ID: `134604186428`
- Head SHA: `1f46bcdeb1f6a17dc4e389f9468f5bb52179d133`
- Started: `2026-11-18T05:39:29Z`
- Completed: `2026-11-18T05:39:40Z`
- Conclusion: `success`
- All job steps completed successfully, including Python compile and focused regression suite.
- Unit tests: **72 passed**, 0 failures/errors; runtime 0.112 seconds.
- Job duration: approximately 11 seconds.

Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44245756372

## Acceptance
| Check | Result |
|---|---|
| Active branch trigger added | PASS |
| Original branch trigger preserved | PASS |
| Python compile | PASS |
| Focused Overlay regression suite | PASS — 72/72 |
| Workflow job conclusion | PASS |
| Production integration | NOT AUTHORIZED |

This closes the workflow-trigger/runtime-QA blocker only. It does **not** qualify all overlay sources or validate the overlay's live data coverage. The source registry contains only the qualified Federal Reserve H.10 nominal broad dollar index tuple; other source/indicator routes remain unqualified unless exact official endpoint, unit, frequency and raw-payload evidence are established. Existing seed rows and any unqualified indicators remain UNKNOWN and cannot drive trusted classifications.

## Next bounded work
Continue exact source-route qualification and immutable raw-payload manifest capture for the next unqualified official source group. Do not guess endpoint/series/unit mappings, and do not promote UNKNOWN rows. Avoid repeating this 72-test suite unless code or test inputs change.

## Invariants
₹0 spend; official/free sources only; no synthetic data or fabricated timestamps; no production selector/scoring changes; Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), Engines A–E and Hard Gate remain unchanged.
