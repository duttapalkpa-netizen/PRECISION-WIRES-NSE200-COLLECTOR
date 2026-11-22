# NSDL FPI/DII Date-Window Integrity Repair — Continuation 254

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## 1. Continuity check
- Re-read `research/GITHUB_MASTER_CONTINUITY_LEDGER.md` (blob `3dc0de26567ca4ef1fba779170849b3a4c7f96ea`) and C253 report (blob `3f70e8295a3a9443b0e6aa6f0f0324a7e983f95d`).
- Re-fetched Run #386 artifact `14743653729` (SHA-256 `20e83e668e7d089bf915b74bfc31cd47853ec77171c9d34cda52fb65aa5c690a`) and inspected the NSDL collector report and CSV directly.
- Existing quarterly and macro source-policy PASS work was not repeated.

## 2. Artifact-backed findings
- NSDL official collector report: `outputs/macro_geo/nsdl_fpi_dii_collection.json`; range declared 2026-06-23 through 2026-11-20.
- FPI archive CSV had 119 unique dates, 2026-06-01 through 2026-11-20. The first 16 FPI trading dates (2026-06-01 through 2026-06-22) were outside the declared window because monthly FPI postbacks returned the full month and were not clipped.
- Within the declared common window, FPI has 103 unique dates; DII has 102 unique dates. Both have zero duplicate (DATE,GROUP) keys and no null DATE/GROUP/NET_VALUE in the archived CSV.
- DII is present on 102/103 FPI archive dates = 99.03%; the single missing FPI archive date is 2026-07-17. This is an observed archive-date comparison, not a synthetic weekday calendar.
- The collector logged seven DII schema failures. Six dates (2026-06-26, 2026-08-26, 2026-09-14, 2026-10-02, 2026-10-20, 2026-11-10) are not present in the FPI archive date set; only 2026-07-17 is a missing date in the common FPI observation-date set. Do not assert a definitive exchange-holiday cause without an independent official calendar check.
- Source URLs are the official NSDL FPI archive `https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx` and DII archive `https://www.fpi.nsdl.co.in/web/Users/DIIGenerateReport.aspx?Rep=A`.
- The CSV's OBSERVED_AT_UTC values are retrieval timestamps, not trade/event timestamps. NET_VALUE units should not be inferred from this CSV alone; verify source table units before financial interpretation.

## 3. Proven defect and repair
- `pipeline/macro_geo_nsdl_flows.py` used month-end FPI queries and correctly parsed daily rows, but it did not clip FPI observations to the declared `start`/`end` window. This allowed out-of-window June 1–22 rows into the output.
- Code commit `77ffe26afcc9afd3ede9fab0aea07816868abb6c` adds `clip_to_window()` and clips parsed rows to the declared window before coverage counts and output.
- The same commit adds `coverage_audit()` which explicitly compares DII dates with FPI archive dates and reports exact missing dates and percentage. It does not create missing observations or change the existing minimum 60-date / 90-day acceptance threshold.
- Regression tests added in `qa/test_macro_geo_nsdl_flows.py`, commit `71e7102acd3e647263e29b5f806e596e048096b8`: FPI window clipping, exact DII gap reporting without imputation, and complete alignment reporting.

## 4. CI status at report creation
- Run #388 ID `44998007760` (code commit) was IN_PROGRESS.
- Run #389 ID `44998017821` (test commit) was PENDING.
- CI has not yet established PASS for this repair. Do not mark the code/tests PASS until the relevant run's test step and overall required acceptance are inspected.

## 5. Status
- Source identity/provenance: official NSDL archive URLs present in artifact.
- FPI date-window clipping: CODED, CI PENDING.
- DII archive-date alignment: 102/103 (99.03%) within the observed FPI archive date set; one unresolved date 2026-07-17.
- Historical-flow data: AVAILABLE under the existing >=60 dates and >=90 days threshold, but date alignment quality is AVAILABLE_WITH_GAPS, not complete.
- USD/INR remains BLOCKED; this work does not resolve the FBIL endpoint blocker.
- Macro-Geo P0 hard gate remains BLOCKED; no release eligibility inferred.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), Engines A–E unchanged.

## 6. Next actions
1. Inspect Runs #388 and #389; if either fails, repair only the exact evidenced defect.
2. After CI verifies, inspect a new NSDL artifact to confirm FPI rows are within 2026-06-23..2026-11-20 and that the 2026-07-17 DII gap remains explicit.
3. Investigate the 2026-07-17 NSDL DII report schema using only official NSDL page evidence; do not synthesize a value.
4. Confirm units and field semantics from the official NSDL table before using NET_VALUE in macro factor calculations.
5. Keep USD/INR and the overall hard gate BLOCKED until their own explicit evidence criteria pass.

## Guardrails
Audit branch only; ₹0 spend; official/free sources only; no synthetic rows, inferred dates, mirrors, paid APIs, or gate relaxation. UNKNOWN/BLOCKED never PASS.