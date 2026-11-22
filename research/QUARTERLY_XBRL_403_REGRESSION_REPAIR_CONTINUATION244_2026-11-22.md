# Quarterly XBRL 403 Regression Repair — Continuation 244

Date: 2026-11-22
Branch: audit/prospective-selector-tracking

## Continuity check
Reviewed C243 and the failed targeted CI runs before changing code. No successful prior test was repeated as a new claim; the failed C243 regression was isolated and repaired.

## Failure evidence and repair
- Run #132 (44992146500), commit ac3f93da1f6546b820620d5567ff8196f277339d: Python module import succeeded, but the new dual-host 403 test failed because its mocked responses did not raise HTTPError from raise_for_status().
- Updated the test fixture to make both mocked 403 responses raise requests.HTTPError, matching the requests API.
- Test fixture commit: fe5f9dff9d1ab0affcda8a93cc58db4da6a5044c.

## Verification
Run #133 (44992195724), exact head SHA fe5f9dff9d1ab0affcda8a93cc58db4da6a5044c:
- "Run only quarterly disclosure and Run 121 regression tests": completed / success.
- Official NSE security-master refresh: completed / success.
- Bounded live quarterly endpoint/schema audit: completed / success.
- Bounded source-linked XBRL metric extraction: still in progress at report creation.
- Feature rebuild and diagnostic artifact upload: not yet reached.

Thus the targeted regression suite including the new dual-host 403 test is PASS. The full workflow and attachment coverage are not yet PASS.

## Next actions
1. Observe Run #133 extraction result and capture its per-host diagnostic artifact.
2. If the extraction succeeds, inspect report counts and ensure truncation/blockers are explicit.
3. If it fails, use the recorded failure evidence to fix only the demonstrated defect.
4. Do not infer 403 remediation merely because the regression test passes.

## Invariants
Audit branch only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E and production workflow unchanged. ₹0 research spend. No paid APIs, synthetic financial values, fabricated timestamps, unofficial mirrors, or access-control bypass. UNKNOWN/BLOCKED never becomes PASS.
