# Fed H.10 Nominal Broad Dollar Index — 20 Valid Observation Change Specification

## Status and scope
- Specification: DEFINED
- Pure research helper: IMPLEMENTED
- QA: PASS (6 dedicated cases; full workflow ran 70 tests)
- Live derived value: NOT_COMPUTED in this work item
- Historical point-in-time vintage coverage: NOT_DONE
- Classifier / production integration: NOT_AUTHORIZED

## Indicator identity
- Output name: `fed_h10_nominal_broad_dollar_change_pct_20obs`
- Input series: `fed_h10_nominal_broad_dollar_index`
- Federal Reserve H.10 series: `JRXWTFB_N.B`
- Unit: percent
- Explicit non-equivalence: this is the Fed nominal broad dollar index, not ICE DXY and not `dxy_change_pct_20d`.

## Window definition
- The phrase “20-observation change” means 20 prior valid H.10 observations plus the current valid observation: 21 values total.
- Formula: `(latest_value / value_20_valid_observations_earlier - 1) * 100`.
- The 20-count is the count of prior valid Federal Reserve H.10 observation records, not 20 calendar days and not 20 Indian exchange sessions.
- Sort by actual H.10 observation date. No synthetic calendar, no forward-fill, no interpolation, and no replacing missing/ND observations.
- If fewer than 21 eligible valid observations exist, return `None` (downstream state must remain UNKNOWN / unavailable).
- Base value must be non-zero; otherwise fail closed.

## Point-in-time / vintage rules
- `decision_at` is mandatory and normalized to UTC.
- Eligible rows must have `published_at <= decision_at`, `date <= UTC decision date`, and `as_of_date <= UTC decision date`.
- For a given observation date, use the latest publication vintage available by `decision_at`.
- If two values conflict for the same observation date and same publication vintage, raise an error.
- The H.10 XML Header `Prepared` timestamp is the package publication vintage. A single current package can support a decision only at/after its Prepared timestamp; it cannot reconstruct what was known at earlier historical decision times.
- A full PIT backtest requires archived historical H.10 package vintages. That archive is not yet available, so historical PIT acceptance remains NOT_DONE.

## Output metadata
The helper returns indicator name, percentage value, unit, window count (21), prior count (20), start/end observation dates, base/latest values, UTC decision cutoff, calendar semantics, trusted quality label, `production_eligible=false`, and the explicit non-equivalence warning.

## QA coverage
1. 21 values produce a 20-prior-observation result with the expected percentage.
2. 20 values return no result.
3. A missing observation is not forward-filled; fewer than 21 actual records returns no result.
4. Publication vintage later than the decision cutoff is excluded.
5. A later revision for an observation date is used only after that revision is published.
6. Conflicting values within the same publication vintage are rejected.

## Evidence and CI
- Implementation commit: `f7af7e6acaa12d2a22f01457fd96bbf2787dd970`
- QA commit: `83d2e1f4c6d2056e83d7249c2158a7e87817f85d`
- GitHub Actions workflow run #229 / ID 44035746086: SUCCESS.
- Full test result: 70 tests in 0.055s; OK.
- This run validates helper behavior and regression compatibility. It does not calculate or authorize a production signal from the live H.10 dataset.

## Acceptance boundary / next work
- 20-valid-observation formula and calendar semantics: DEFINED.
- No-forward-fill behavior: TESTED.
- PIT cutoff and vintage selection: TESTED at unit level.
- Actual live derived observation: NOT_COMPUTED here.
- Multi-vintage historical replay: NOT_DONE.
- Long-term raw payload archive: NOT_DONE.
- Classifier integration / trading use: NOT_AUTHORIZED.
- Next task: produce a separate research-only derived output from the captured raw H.10 archive, verify the 21 actual valid observations and their vintage, then test the result against a second independently downloaded official package. Do not modify existing `dxy_change_pct_20d` or any production scoring path.
