# September 2026 IIP — Complete NIC-2 Manufacturing Cohort QA Note
Date recorded: 2026-11-05
Reference month: 2026-09
Release: 2026-10-28 16:00 IST
Base: 2022-23=100
Estimate vintage: September Quick Estimate; August 2026 Final Revision
Official source: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2329475&lang=2&reg=48

## Work completed
Transcribed all 23 manufacturing NIC-2025 two-digit groups from official Statement II-A into `research/data/iip_2026_09_manufacturing_nic2_statement_IIA.csv`.
Each row carries NIC-2025 code, description, weight, September 2025 and September 2026 index, April-September 2025-26 and 2026-27 cumulative index, monthly YoY growth, cumulative YoY growth, estimate stage, publication timestamp, Statement II-A, and official PIB source URL.

## Independent arithmetic checks performed on the 23-row transcription
- Rows: 23; distinct NIC-2 codes: 23; expected continuous code set 10–32.
- Positive monthly growth groups: 17; negative: 6; zero: 0.
- Positive breadth derived: 17/23 = 73.9130%; this percentage is calculated, not directly published as a percentage by MoSPI.
- Sum of displayed rounded NIC-2 weights: 76.065; official Manufacturing weight: 76.062. Difference +0.003 is within expected display-rounding tolerance ±0.005; do not adjust any individual published weight to force equality.
- All 23 September YoY growth values recompute from displayed Sep-2026/Sep-2025 indices to one decimal with no mismatches.
- All 23 April-September cumulative growth values recompute from displayed cumulative indices to one decimal with no mismatches.
- Key groups: NIC 11 beverages +39.4%; NIC 27 electrical equipment +33.9%; NIC 22 rubber/plastics +19.9%; NIC 29 motor vehicles +19.0%.

## Why this is useful to the stock research
- Provides a complete one-month NIC-2 manufacturing breadth and leadership snapshot rather than only the top three groups.
- Preserve index levels, weights, monthly growth and cumulative growth separately; do not use growth rates as contributions or factor weights.
- For company joins, require documented business-segment exposure to the corresponding NIC group; broad company name/sector labels are insufficient.
- Treat IIP as a slow-moving macro/sector context feature and risk modifier, not a standalone 1–5 day price predictor. Validate any predictive effect out-of-sample and with publication-time cutoff.
- This is a point-in-time release vintage: the September Quick Estimate can be revised later. New revision rows must append; do not overwrite this vintage.

## Important publication timing
Published 28 October 2026 at 16:00 IST. This is after the regular cash-market close. Earliest feature eligibility is the next valid NSE trading session, subject to official exchange calendar. Do not backdate to the September reference month or use in a pre-close 28 October signal.

## QA automation
- Validator: `pipeline/validate_iip_2026_09_manufacturing_nic2.py`.
- Existing release QA workflow extended to run both the summary metrics validator and full 23-group NIC-2 validator.
- Workflow timeout: 5 minutes; manual dispatch only.
- Manual independent calculation in this task found zero YoY or cumulative-growth arithmetic mismatches. GitHub Actions has not been dispatched; no CI PASS/run ID is claimed.
- Raw official PDF binary SHA-256 remains pending. This dataset is official-page-transcribed, not raw-binary certified.

## Status
SEPTEMBER_2026_NIC2_ROWS: 23/23 TRANSCRIBED
CODE_COVERAGE: 10–32 COMPLETE
WEIGHT_SUM: 76.065 VS OFFICIAL 76.062; ROUNDING DIFFERENCE +0.003
MONTHLY_GROWTH_ARITHMETIC: 23/23 MATCH
CUMULATIVE_GROWTH_ARITHMETIC: 23/23 MATCH
POSITIVE_BREADTH: 17/23 = 73.9130% DERIVED
CI_EXECUTION: PENDING
RAW_PDF_SHA256: PENDING
APRIL_2023_ONWARD_FULL_MONTHLY_PANEL: NOT YET COMPLETE
MASTER_HARD_GATE: BLOCKED

## Protected invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics or V11.3(A/B/C/D/E) logic changed. No synthetic rows, fabricated timestamps, unsupported source promotion, or Hard Gate relaxation.