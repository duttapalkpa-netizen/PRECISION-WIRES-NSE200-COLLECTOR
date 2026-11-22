# Security Master Fresh-Acquisition Stale-Artifact Guard — Continuation 236

Date: 2026-11-22 (Asia/Kolkata)
Branch: audit/prospective-selector-tracking
Status: CODE COMMITTED; REGRESSION TEST ADDED; TEST EXECUTION / CI NOT VERIFIED

## 1. Continuity preflight
- Re-read the latest available C235 report and the collector, validator, regression tests, and prospective workflow on the audit branch.
- C235 already established the legacy-source boundary and validation checks. Its six offline tests were explicitly pending execution.
- Selected one narrowly scoped residual defect: a failed fresh acquisition could leave an older master/manifest pair in the workspace. Because the validator accepts provenance up to seven days old, that old pair could still pass validation after a new network failure.
- No prior PASS item was repeated; no daily MII URL or schema was inferred.

## 2. Changes committed
1. `collector/security_master.py` now removes the previous normalized master and provenance manifest immediately before attempting a fresh acquisition. If both configured official legacy endpoints fail, there is no prior-run pair left for the subsequent validator to accept.
2. `qa/test_security_master_validation.py` adds a regression test that seeds an old master/manifest pair, simulates network failure for both endpoint attempts, and asserts that neither stale file remains.

Commit trail:
- Fresh-acquisition cleanup: `6f8a655826f829bcf8acd8df2ef3bd498a806721`
- Regression test: `dcab18abbc5e8a8d1a70487cb372fe5341d8c9b7`

## 3. Verification status
| Check | Status |
|---|---|
| Collector cleanup logic committed | CODED |
| Regression test added | CODED |
| Offline test execution | NOT VERIFIED |
| GitHub Actions run linked by commit lookup | NONE RETURNED |
| Live NSE legacy endpoint acquisition | NOT VERIFIED |
| Daily CM-MII feed equivalence | UNKNOWN / NOT ESTABLISHED |

The GitHub commit-workflow lookup returned no associated runs for either commit. This does not establish a successful CI result. The full prospective workflow was not manually dispatched.

## 4. Acceptance boundary
This closes the identified stale-artifact reuse path for executions that run `collector/security_master.py` before `qa/validate_security_master.py`. It does not prove NSE reachability or daily MII equivalence. The source remains explicitly `LEGACY_EQUITY_L_CSV`, not the daily CM-MII security file.

## 5. Protected invariants
Audit-only branch. No production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, or production workflow changes. ₹0; no paid APIs, synthetic data, guessed source URLs, or fabricated timestamps. UNKNOWN never PASS.
