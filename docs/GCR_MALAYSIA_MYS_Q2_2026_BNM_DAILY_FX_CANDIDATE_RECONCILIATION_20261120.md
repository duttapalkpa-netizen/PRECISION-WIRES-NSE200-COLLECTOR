# Malaysia MYS Q2-2026 — BNM daily USD/MYR rate candidate and independent leg check
Date: 2026-11-20 (Asia/Kolkata)

Decision: **Official daily-rate observations located and 60 Q2 rows transcribed; candidate arithmetic completed. Exact rate-selection convention remains NOT_ESTABLISHED, so the FX/sign numerical comparison is REVIEW only. MYS full validation remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## Continuity preflight and duplicate rejection
- Reopened the current GCR priority queue, Malaysia national-source crosswalk, and Malaysia archived IMF exact-row extraction report.
- Reused IMF artifact 14505862034 and existing BNM Q3-2026 Annex Table 3 capture. No new IMF request, cohort rebuild, repeat national extraction or duplicate IMF panel QA.
- The exact Master Continuity Ledger blob SHA referenced in the priority queue is ce94bbcfcfd080685e21c483260a93d6d2d60434. Its path was not returned by repository file search in this execution; the priority queue and country reports were directly reopened.

## New official source discovery
- Bank Negara Malaysia official Exchange Rates page: https://www.bnm.gov.my/exchange-rates
- BNM Data Download catalogue describes the Exchange Rates dataset as daily noon middle rates for selected currencies (1997-present).
- The live Exchange Rates page itself describes rates from the Kuala Lumpur interbank market at 0900, 1200 and 1700 and exposes session/rate-type controls. The text extraction available for this task did not conclusively preserve which session/rate-type selection generated the displayed USD column. Therefore the displayed daily observations are archived as a candidate series, not yet admitted as the definitive Q2 conversion series.
- Source page references: BNM Data Download and Exchange Rates page (see report citations in the conversation).
- Q2 dates with visible USD observations: 60 business-day rows (April 22, May 19, June 19). No weekends/holidays were filled.

## Daily candidate series and arithmetic
- CSV: docs/evidence/malaysia_mys_q2_2026_bnm_daily_usd_myr_candidate.csv
- Rows: 60, dates 2026-04-01 through 2026-06-30 (observed business dates only).
- Candidate arithmetic mean: 3.9992166667 RM per USD.
- April: 22 observations, mean 3.9766590909.
- May: 19 observations, mean 3.9498157895.
- June: 19 observations, mean 4.0747368421.
- CSV SHA-256: 9ab6470fe7117165343b9914cdf4d7dbf75ece89dbe27537b7d63b4811e03ced.
- This is an arithmetic mean of the 60 displayed daily observations; it is not described as an official BNM-published quarterly average. It must not be treated as final until session/rate-type and conversion methodology are verified.

## Candidate numerical diagnostic — NOT an acceptance PASS
Inputs reused:
- BNM Q2 2026 preliminary portfolio assets = -RM33.3bn; liabilities = -RM1.8bn; net = -RM35.2bn.
- BNM note: negative assets denote outflows due to residents' acquisition of foreign assets; positive liabilities denote inflows due to incurrence of foreign liabilities. Source warns figures may not add due to rounding.
- IMF archived exact Q2 raw rows: A_NFA_T = 8,328,720,912.826584 USD; L_NIL_T = -453,604,929.8946682 USD; SCALE=6, PRECISION=6. The prior Malaysia extraction report preserves artifact and raw-file hashes.

Using the candidate 3.9992166667 RM/USD mean, and a provisional country-specific transform of IMF OBS_VALUE / 1,000,000 for USD-million comparison:
- BNM asset magnitude: 33,300 / 3.9992166667 = 8,326.630632 USDm. Candidate sign mapping reverses the BNM asset sign; IMF A_NFA_T = +8,328.720913 USDm. Absolute residual = 2.090281 USDm.
- BNM liability: -1,800 / 3.9992166667 = -450.088142 USDm. Candidate mapping retains the BNM liability sign; IMF L_NIL_T = -453.604930 USDm. Absolute residual = 3.516788 USDm.
- A one-decimal RMbn display half-unit is ±RM0.05bn, equivalent to about ±USD12.502448m at this candidate rate. Both separate-leg residuals are inside that display-rounding bound.
- This is only a diagnostic because the daily rate selection is not conclusively identified and the USD-million transform is being tested for Malaysia, not globally authorized. The leg checks are NOT marked PASS.
- Net diagnostic: BNM published net -RM35.2bn; reversing the displayed net direction gives +USD8,801.723671m at candidate FX. IMF A_NFA_T - L_NIL_T = +USD8,782.325843m; residual = USD19.397828m. This exceeds a standalone ±RM0.05bn net-row half-unit bound (~USD12.502448m). Source component sum -33.3 + (-1.8) = -35.1 RMbn differs from reported net -35.2 RMbn; BNM explicitly permits rounding differences. Net remains REVIEW; no tolerance widening or forced identity.

## Acceptance matrix
| Gate | Status |
|---|---|
| Existing IMF raw MYS Q2 rows | PASS (previous report; reused) |
| Existing BNM national asset/liability rows | PASS (previous report; reused) |
| Official BNM daily USD/MYR source located | PASS |
| 60 Q2 displayed daily observations transcribed | PASS (candidate archive) |
| Exact session/rate-type of displayed series | NOT_ESTABLISHED |
| Official BNM quarterly-average methodology | NOT_ESTABLISHED |
| Candidate FX arithmetic | PASS as arithmetic only |
| Candidate separate-leg numeric residuals | REVIEW, not PASS |
| Candidate country-specific asset sign reversal | REVIEW pending full sign/methodology and FX gate |
| Candidate liability sign retention | REVIEW pending FX gate |
| Net identity / net comparison | REVIEW |
| Same-vintage alignment | NOT_ESTABLISHED |
| MYS full dual-leg validation | PARTIAL / NOT PASS |
| EMDE aggregate | NOT_AUTHORIZED |

## Next exact action
1. Capture the BNM Exchange Rates control selection (session, rate type, quotation and currency direction) with a source-preserving export or official OpenAPI dataset metadata.
2. Establish the official conversion convention for quarterly BOP transaction flows (daily observation average, monthly published average, or other explicit BNM/DOSM methodology); do not select a convention solely because it produces a close match.
3. Verify the asset sign mapping and liability sign mapping independently against official BNM BPM6 methodology. Do not net legs.
4. If those gates pass, repeat each numeric comparison using the accepted rate and pre-registered display-rounding tolerance. Preserve the preliminary BNM vintage and IMF retrieval vintage separately.
5. If exact rate selection or conversion convention cannot be evidenced, retain REVIEW/PARTIAL and move to the next eligible country only after documenting the blocker.

## Protected invariants
No production code, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights or trade gates changed. No paid APIs, synthetic data, fabricated timestamps, silent conversion, forward-fill, netting or aggregate authorization. UNKNOWN is never PASS.

## Reproducibility
- Existing IMF extraction report: docs/GCR_MALAYSIA_MYS_Q2_2026_IMF_RAW_ROW_EXTRACTION_20261120.md
- Existing national crosswalk: docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_IMF_PORTFOLIO_SOURCE_CROSSWALK_20261120.md
- Candidate FX observations CSV: docs/evidence/malaysia_mys_q2_2026_bnm_daily_usd_myr_candidate.csv
