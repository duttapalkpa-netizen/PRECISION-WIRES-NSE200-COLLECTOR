# Fed H.10 Broad Dollar — 20 Valid Observation Derived Result (2026-11-17)

## Acceptance status
- Official H.10 raw capture: PASS
- ND / non-available status exclusion: PASS
- Existing overlay parser admission: PASS, 5,231 valid observations
- 20-prior-valid-observation calculation: PASS, research-only
- Independent second-vintage cross-check: NOT_DONE
- Historical PIT replay: NOT_DONE
- Classifier / production integration: NOT_AUTHORIZED

## Corrected raw observation accounting
The H.10 XML has 5,445 source observation records for JRXWTFB_N.B. Their statuses are:
- A (available): 5,231
- ND (not available): 214

The ND records carry numeric sentinel values (including -9999.0), not the literal string "ND". The first parser-admission run incorrectly treated these as numeric because it only checked value text. That earlier 5,445 count is superseded. The corrected collector filters on OBS_STATUS == "A", validates date and finite numeric value, and only then writes parser input. The corrected parser admission count is 5,231; all 214 ND records are excluded.

## Actual 20-observation calculation
- Input series: JRXWTFB_N.B / fed_h10_nominal_broad_dollar_index
- Window semantics: 20 prior valid H.10 observation dates plus current date = 21 valid observations
- Window start / base date: 2026-10-15
- Base value: 121.5693
- Window end / latest date: 2026-11-13
- Latest value: 122.6503
- Missing / ND date inside the otherwise recent period: 2026-11-11 (excluded; no fill)
- Formula: (122.6503 / 121.5693 - 1) × 100
- Result: +0.8892047581%
- Rounded display: +0.8892%
- Calendar: H.10 valid observation dates, not 20 Indian trading sessions.
- Output indicator: fed_h10_nominal_broad_dollar_change_pct_20obs.
- This is not ICE DXY and must not be relabelled or inserted into dxy_change_pct_20d.

## Corrected evidence capture
- Workflow #8 / ID 44036104490: SUCCESS.
- Commit: 4e3da948ff04e1d8efe50ee3782a16c4814e8965
- Run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44036104490
- Artifact ID: 14306134441
- Artifact name: fed-h10-official-evidence-44036104490
- Artifact archive SHA-256: 2d9a4808cd9e48ac21175b8a79ccf42173f57f2370086e24832e4d460afbe4ba
- Artifact expiry: 2027-02-15T07:06:07Z
- Raw payload byte length: 2,088,268
- Raw payload SHA-256: c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77
- HTTP 200, application/x-zip-compressed; retrieved 2026-11-17T07:06:14.336027Z.
- Parser result JSON: status PASS, admitted 5,231, source count 5,445, excluded non-available 214, latest 2026-11-13 = 122.6503.

## Regression QA
- Workflow #232 / ID 44036012995: SUCCESS; 72 tests in 0.056s.
- Includes dedicated tests for ND status with numeric -9999 sentinel, unknown statuses, and non-finite values, in addition to the six 20-observation/PIT tests.
- The capture workflow also executed the existing `load_observations` parser against the corrected CSV and verified exact count equality (5,231).

## Remaining limitations
- The calculation is a single current package vintage with Prepared timestamp 2026-11-16T16:47:01. It does not prove what was known on earlier dates.
- No second independent publication vintage has been archived or reconciled.
- GitHub artifact retention is 90 days; durable long-term raw archive remains NOT_DONE.
- This result is research-only and is not integrated into classifier or production ranking.
