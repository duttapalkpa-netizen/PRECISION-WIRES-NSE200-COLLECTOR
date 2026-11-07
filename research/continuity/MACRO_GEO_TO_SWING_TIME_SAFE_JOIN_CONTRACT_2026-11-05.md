# Macro-Geo → 2%–5% Swing Research: Time-Safe Company Join Contract
Recorded: 2026-11-05
Status: RESEARCH DESIGN + VALIDATION IMPLEMENTED; COMPANY MAPPINGS NOT YET POPULATED

## Purpose
Connect published Macro-Geo/IIP evidence to listed-company business exposure and then to the existing 2%/3%/5% forward-outcome research without look-ahead or fabricated company classifications.

## Repository inspection findings
- `config/universe.csv` currently contains only the `SYMBOL` header; it is not a populated research universe.
- `research/data/iip_2026_09_manufacturing_nic2_statement_IIA.csv` contains the 23 NIC-2025 manufacturing groups (codes 10–32), September 2026 Quick Estimate vintage, published 2026-10-28 16:00 IST.
- `pipeline/walk_forward_backtest.py` already derives stock-level price, volume, delivery and relative-strength features and forward H+1/H+3/H+5 outcomes. The repository inspection did not establish a verified join from IIP NIC-2 to company segment exposure in that pipeline.
- Therefore, this work does not claim predictive Macro-Geo integration or validated alpha.

## Company exposure mapping contract
Template: `research/data/company_nic2_exposure_mapping_template.csv`

One row represents one listed-company business segment exposure to one NIC-2025 two-digit group over an effective interval. A company may have multiple segment rows. Required evidence:
- NSE symbol and ISIN; legal company name.
- NIC-2025 two-digit code (10–32) only when supported by a documented business activity crosswalk; otherwise use UNKNOWN and do not join.
- Segment revenue share percentage; use only disclosed, source-supported share. Do not invent equal weights or infer from market sector labels.
- Effective-from/effective-to dates.
- Evidence source type, URL, publication timestamp, document ID, SHA-256 and verification note.
- VERIFIED status only after manual/source verification. UNKNOWN and REJECTED rows are retained as explicit states and excluded from joins.

A broad exchange sector, company name similarity, or NIC concordance alone is not sufficient to claim company segment exposure. Do not use NIC-2008/NIC-2025 concordance as a substitute for a company business-segment disclosure.

## Point-in-time / no-look-ahead rules
1. The IIP reference month is descriptive, not the information-availability date.
2. An IIP vintage is eligible only when its actual publication timestamp is at or before the signal decision timestamp.
3. Company mapping evidence must itself have been public by the decision timestamp.
4. The mapping effective interval must cover the decision timestamp.
5. For the 2026-09 Quick Estimate released 2026-10-28 16:00 IST (after the regular cash-market close), do not use it for a pre-close 28 October signal. The first usable exchange session must be determined from the official NSE trading calendar; this script enforces publication cutoff but deliberately does not fabricate an exchange session calendar.
6. Keep each revision vintage append-only. Never overwrite an earlier release with a later revision.
7. No interpolation, backfill, or synthetic lower-level linking factors.

## Executable validator/join
`pipeline/build_iip_company_time_safe_join.py`:
- Requires a timezone-aware decision cutoff.
- Checks required mapping and IIP columns, valid NIC codes, explicit mapping states, duplicate mapping keys, verified-source provenance, numeric segment shares and company segment-share totals.
- Excludes UNKNOWN/REJECTED mappings.
- Excludes mapping evidence and IIP vintages published after the decision cutoff.
- Enforces effective dates and writes a research-only joined CSV plus SHA-256 QA report.
- Empty template is a valid schema-only state and returns NO_VERIFIED_MAPPINGS; this is not a research PASS.

## Evaluation protocol after verified mappings and price history exist
- Baseline: existing core stock features only.
- Research arm: same baseline plus point-in-time Macro-Geo/IIP company-exposure features, initially as a risk/context modifier only.
- Chronological walk-forward splits; purge/embargo overlapping H+1/H+3/H+5 outcome windows. No random split.
- Report separately for 2%, 3%, and 5% upside: sample count, hit rate, time-to-hit, MFE/MAE, false-breakout rate, adverse excursion/stop incidence, drawdown and coverage.
- Compare baseline vs augmented arm on identical eligible observations; report absolute and relative lift with confidence intervals. Cluster uncertainty by symbol and time; control for multiple factor/threshold tests.
- Ablation by NIC group, vintage, sector and market regime. Include a no-Macro-Geo baseline and a placebo/lead-lag leakage check.
- Do not assign factor weights or production score contribution unless out-of-sample results are stable, economically meaningful and reproducible.

## Non-changes / hard boundaries
No edits to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or engines A/B/C/D/E. UNKNOWN remains neither PASS nor FAIL. No synthetic rows, fabricated timestamps, unsupported source promotion, paid data/API or hard-gate relaxation.

## Current outcome
The mapping schema and executable time-safe join are added. No company mapping rows have been fabricated; therefore no stock-level Macro-Geo joins, event-study results, predictive lift, or Hard Gate PASS are claimed. GitHub Actions execution is separate and has not been claimed by this commit.
