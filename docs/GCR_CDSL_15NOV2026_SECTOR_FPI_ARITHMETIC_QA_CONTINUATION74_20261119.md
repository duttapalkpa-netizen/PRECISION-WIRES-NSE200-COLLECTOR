# GCR CDSL 15-Nov-2026 Sector FPI Report — Independent Arithmetic QA (Continuation 74)
Date: 2026-11-19 (Asia/Kolkata)
Scope: read-only validation of the already archived official CDSL sector report. No production ingestion or backtest claim.

## Source and artifact provenance
- Official dated page: https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Nov%2015%202026.html
- Prior capture workflow run: 44519322726 (SUCCESS).
- Artifact ID: 14527092174; name: gcr-india-fpi-raw-pages-3.
- ZIP bytes: 1,067,099 (archive member uncompressed total 1,067,099 bytes).
- GitHub artifact digest / independently recomputed ZIP SHA-256: 83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd (MATCH).
- Dated sector HTML: 327,522 bytes; SHA-256: 3f77f3896a95b8cff3a7728049127493814e1b503eb39dcb75b0e8fe145cf84e.
- Raw HTML is preserved unchanged in the ZIP; parsing was performed on a temporary extracted copy.

## Table structure
- Main sector table: 29 rows × 98 columns after HTML table expansion.
- Three header rows; 24 numbered sector/category rows; one published grand-total row.
- Eight 12-column blocks: (1) 31-Oct-2026 AUC INR Cr, (2) 31-Oct-2026 AUC USD Mn, (3) 16–31 Oct net investment INR Cr, (4) same USD Mn, (5) 01–15 Nov net investment INR Cr, (6) same USD Mn, (7) 15-Nov-2026 AUC INR Cr, (8) same USD Mn.
- Each 12-column block has 11 category/route components plus one published Total column. Debt, Hybrid, Mutual Fund and AIF subcategories remain separate as reported.
- Separate note table records inclusion dates for Debt VRR, Debt-FAR, Mutual Funds and AIF.
- Separate conversion table states period-specific end-of-period RBI reference rates: 95.2492 for 31-Oct AUC and 16–31 Oct net investment; 94.1997 for 15-Nov AUC and 01–15 Nov net investment. The report separately says daily RBI reference rates are used for CDSL daily conversions, while this report uses period-end reference rate.

## Independent arithmetic QA
- For each of 24 numbered sector rows, in each of 8 blocks, sum of 11 reported components was compared with that row's published Total.
- Result: 192/192 sector-row subtotal checks matched exactly at the displayed integer precision (zero mismatches).
- Grand-total row was independently compared with the sum of the 24 published sector totals. Residual = published grand total minus sum of sector totals:
  - 31-Oct AUC INR Cr: 0
  - 31-Oct AUC USD Mn: +1
  - 16–31 Oct net investment INR Cr: -1
  - 16–31 Oct net investment USD Mn: +2
  - 01–15 Nov net investment INR Cr: -2
  - 01–15 Nov net investment USD Mn: -2
  - 15-Nov AUC INR Cr: -1
  - 15-Nov AUC USD Mn: -3
- Preserve published grand totals. Small residuals are recorded as displayed-total reconciliation differences; no correction or inferred adjustment is applied.

## Interpretation limits / rejected transformations
- The 01–15 Nov figures are fortnightly net investment, not daily observations. Do not expand/interpolate them into daily flows.
- AUC is a stock/position measure, not transaction flow. Keep separate from net investment.
- The source's INR/USD columns are both retained as published. Do not recompute USD values using one common conversion rate; the page explicitly describes end-of-period rates by period and daily rates for daily data.
- Sector classification follows BSE Common Industry Classification; "Others" includes investment outside the approximately 4,800 issuers classified by BSE. Do not silently map this to NSE sector TRI labels.
- Sector flow alone does not establish sector return, causal impact, or stock beneficiary.
- No matched-date NSDL/CDSL cash reconciliation, no sector TRI join, no earnings/fundamental join and no out-of-sample GCR test were performed in this increment.

## Acceptance
- Raw artifact digest verification: PASS.
- Main table schema and period inventory: PASS.
- 24 × 8 sector subtotal arithmetic: PASS (192/192).
- Published grand-total vs sector-sum reconciliation: REVIEW (eight residuals of -3 to +2 displayed units; retain source values).
- Sector classification crosswalk to official TRI: NOT_DONE.
- Daily flow alignment / NSDL confirmation: NOT_DONE.
- GCR-to-sector/stock predictive backtest: BLOCKED / NOT_RUN.

## Next highest-value bounded action
Obtain official BSE sector total-return index (TRI) historical data with exact index identifiers, currency, observation dates, publication/retrieval metadata and raw hashes; independently establish the BSE sector-classification-to-TRI mapping before joining this fortnightly flow panel. If free official TRI history or a defensible mapping is unavailable, keep sector transmission UNKNOWN. Do not run a predictive backtest on a non-comparable join.

## Invariants
₹0 spend; official/free sources only; no synthetic data, forward-fill, daily interpolation, guessed sector crosswalk, or silent grand-total adjustment. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. Observation remains OPEN; Planning/Organizing and production admission NOT_AUTHORIZED. UNKNOWN is not PASS.
