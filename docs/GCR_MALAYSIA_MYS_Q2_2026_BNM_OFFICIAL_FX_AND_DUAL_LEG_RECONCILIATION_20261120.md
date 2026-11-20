# Malaysia MYS Q2-2026 — official BNM 1200-middle FX capture and IMF dual-leg diagnostic
Date: 2026-11-20 (Asia/Kolkata)
Decision: **BNM daily/monthly FX capture and monthly-vs-daily cross-check PASS; Q2 daily mean PASS; both separate IMF↔BNM leg comparisons PASS at BNM published rounding under the already empirically supported Data Portal OBS_VALUE/10^6 derived-display convention; same-vintage alignment NOT_ESTABLISHED; MYS full national validation PARTIAL / NOT PASS; EMDE aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight and rejected repeat work
- Fetched the current Master Continuity & Acceptance Ledger from `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md` (pre-task blob SHA `86f6b5bda9ff6ab2bc91e30cf16677543dd2eecc`); also fetched the historical ledger snapshot SHA `ce94bbcfcfd080685e21c483260a93d6d2d60434`.
- Reopened the GCR priority queue, MYS BNM/IMF national crosswalk, MYS exact IMF-row extraction, and IMF scale semantics / cross-country validation reports.
- Reused the fixed 63-country Q2-2026 dual-leg cohort, existing IMF exact MYS rows, BNM Q3-2026 Annex Table 3 and previous national sign-note capture. No new IMF request, no cohort rebuild, no repeated BNM national table extraction.
- Excluded already-PASS IMF DSD/codelist capture, 154-member WEO roster, 9,299-row panel structural QA, fixed cohort construction, Brazil/India/Mexico/Chile historical scale benchmarks and the previous BNM national row capture.
- Important scale discipline: IMF `SCALE=6` means Millions in metadata, but raw Data Portal observations are preserved unchanged. Existing cross-country evidence empirically supports a derived comparison field `OBS_VALUE / 1,000,000` for 118/118 historical benchmark comparisons; the India current-vintage extension further validates Q2-2026. This is a derived USD-million presentation/comparison only, not an overwrite or a second application of the unit multiplier. Do not generalize to all 154 countries.

## 2. Official sources and method
### Daily BNM 1200 dataset
- Dataset ID: `exchangerates_daily_1200`
- Landing page: https://data.gov.my/data-catalogue/exchangerates_daily_1200
- Raw CSV: https://storage.data.gov.my/finsector/exr/daily_1200.csv
- Source: Bank Negara Malaysia; official 1200 mid-day reference.
- `rate_type=middle` is the midpoint between buying and selling; USD column is MYR per USD.
### Monthly BNM 1200 dataset
- Dataset ID: `exchangerates`
- Landing page: https://data.gov.my/data-catalogue/exchangerates
- Raw CSV: https://storage.data.gov.my/finsector/exr/monthly.csv
- The official metadata states the monthly dataset is derived from 1200 middle rates. `indicator=avg` is the average across trading days in the month.
- Both resources carry CC BY 4.0.
### Calculation
- Filter daily raw file to Q2 2026, `rate_type=middle`, USD column; do not forward-fill weekends/holidays.
- Filter monthly raw file to April–June 2026, `indicator=avg`, USD column.
- Compute Q2 daily arithmetic mean across the actual 60 observed trading-day rows. Independently compute the daily-count-weighted mean from the three official monthly average rows; compare them.
- All raw source bytes, response headers, retrieval timestamp, source SHA-256, filtered subsets, monthly cross-check and Q2 mean are recorded in the workflow artifact manifest.

## 3. Raw capture and reproducibility
- Workflow: `.github/workflows/gcr_mys_q2_bnm_fx_capture.yml`
- Script: `scripts/research/capture_mys_q2_bnm_fx.py`
- NSE collector guard commit: `2f62ec6ed1d66d65ba4d16cf6b739c54766a6d11` (added the new research-only paths to `paths-ignore` before the capture workflow was created; no full NSE collector run).
- Capture script commit: `9e43c42130a4adc8518841280644de77f35970e8`
- Workflow commit: `fe6244ba676c23ee516e81fccae3e12f9bc90201`
- Run: [44688788754](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44688788754), run number 1; conclusion SUCCESS; job ID `136129345981`; capture and artifact upload steps SUCCESS.
- Artifact ID: `14607900969`; name `gcr-mys-q2-2026-bnm-fx-44688788754`; size 1,261,845 bytes; ZIP SHA-256 `aeeb723a0b8a6e8b8bf1472b1ba7c720074c2e4d5cf604e30ba1d2e162e8c07b`; retained until 2027-02-18 (90-day artifact retention).
- Retrieval UTC: `2026-11-20T06:34:49.542146+00:00`.
- Daily raw CSV: HTTP 200; 3,870,195 bytes; SHA-256 `4b0c6cf00752753bbb070791468c7a50d39d8b8556129b5399cce94a264101be`; Last-Modified `Fri, 20 Nov 2026 04:30:09 GMT`; ETag `"11aab1ce606ae347be70c469b05b1330"`.
- Monthly raw CSV: HTTP 200; 347,365 bytes; SHA-256 `705f81be36b180d8ac4d29ef13df741a97e996ce373567a03188924b980ec71c`; Last-Modified `Sat, 31 Oct 2026 18:30:06 GMT`; ETag `"e03763e622ceb97ce73338cfaca21d0b"`.
- Q2 daily subset permanently archived at `docs/evidence/gcr_mys_q2_2026_bnm_fx/mys_q2_2026_daily_1200_middle_usd.csv`; SHA-256 `836fa4241d257dacd9477cd4cac5dd904872190657279bc96132dd59385c48bb`.
- Q2 monthly subset permanently archived at `docs/evidence/gcr_mys_q2_2026_bnm_fx/mys_q2_2026_monthly_avg_usd.csv`; SHA-256 `de9025e701389adcae917065cce1f273f2f6d3d7f9daeb33b73bf3327ba6974b`.
- The full raw CSVs are retained in the 90-day immutable workflow artifact; the Q2 filtered subsets and their hashes are also committed in GitHub.

## 4. FX quality checks — PASS
| Month | Daily middle observations | Daily mean (MYR/USD) | Official monthly avg (MYR/USD) | Absolute difference | Status |
|---|---:|---:|---:|---:|---|
| Apr-2026 | 22 | 3.9783636364 | 3.9784 | 0.0000363636 | PASS |
| May-2026 | 19 | 3.9525789474 | 3.9526 | 0.0000210526 | PASS |
| Jun-2026 | 19 | 4.0778157895 | 4.0778 | 0.0000157895 | PASS |
- Daily rows: 60; monthly avg rows: 3; dates unique; all three months covered; no imputation/forward-fill.
- Q2 arithmetic mean from the 60 daily 1200-middle USD observations: **4.001691666666666666666666667 MYR per USD**.
- Independently weighted mean of official monthly averages using daily observation counts 22/19/19: **4.001706666666666666666666667**.
- Difference: **0.000015 MYR/USD**, consistent with the monthly dataset's four-decimal rounding.
- Previous BNM Exchange Rates page candidate mean `3.9992166667` is **NOT_ADMITTED / SUPERSEDED**: exact session/rate-type was not proven and its displayed values do not reconcile to the official 1200-middle daily/monthly pair. Do not reuse it.

## 5. MYS national ↔ IMF separate-leg diagnostic
### Inputs
- BNM Quarterly Bulletin Q3 2026, Annex Table 3, BPM6, Q2-2026 preliminary, unit RM billion: portfolio net `-35.2`, assets `-33.3`, liabilities `-1.8`. Official source: https://www.bnm.gov.my/documents/20124/23688793/qb26q3_en_annex.pdf
- BNM source sign notes already captured in `docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_IMF_PORTFOLIO_SOURCE_CROSSWALK_20261120.md`: negative asset value denotes outflow from residents' acquisition of assets abroad; positive liability value denotes inflow from incurrence of foreign liabilities.
- IMF exact archived rows, IMF.STA:BOP(21.0.0), P_F, UNIT=USD, FREQUENCY=Q, TIME_PERIOD=2026-Q2, `SCALE=6`, raw values unchanged:
  - `A_NFA_T`: `8328720912.826584` USD; derived USDm comparison field `8328.720912826584`.
  - `L_NIL_T`: `-453604929.8946682` USD; derived USDm comparison field `-453.6049298946682`.
- IMF raw archive/row provenance remains in `docs/GCR_MALAYSIA_MYS_Q2_2026_IMF_RAW_ROW_EXTRACTION_20261120.md`; raw IMF values and SCALE attributes are not modified.
### Separate legs
- Asset direction: BNM's negative asset row denotes resident acquisition of foreign assets/outflow; IMF A_NFA_T positive denotes net acquisition of financial assets. For like-for-like direction, compare the reversed BNM sign: `(+33.3 RMbn / 4.0016916666666667) × 1000 = +8321.480707 USDm`.
- Asset absolute residual: `|8328.720913 - 8321.480707| = 7.240206 USDm`.
- Liability direction: BNM negative liability row denotes outflow/reduction in liabilities; IMF L_NIL_T is negative. Retain sign: `(-1.8 RMbn / 4.0016916666666667) × 1000 = -449.809768 USDm`.
- Liability absolute residual: `|-453.604930 - (-449.809768)| = 3.795162 USDm`.
- BNM's displayed one-decimal RMbn implies a half-unit rounding bound of ±0.05 RMbn. Converted at the accepted Q2 daily FX mean, this is **±12.494716 USDm**. Both leg residuals are inside this bound; each numeric leg comparison is **PASS at published display precision** under the country-specific sign mapping above.
- Do not net the two legs. BNM rounded component arithmetic remains `-33.3 + (-1.8) = -35.1 RMbn` versus published net `-35.2 RMbn`; retain REVIEW (0.1 RMbn rounding difference) and do not force identity.

## 6. Acceptance matrix
| Gate | Status |
|---|---|
| Official BNM 1200 daily dataset and rate-type identity | PASS |
| Official BNM monthly avg dataset and 1200-middle methodology | PASS |
| Full daily and monthly raw bytes captured; SHA-256 verified | PASS |
| Q2 60-row daily subset and 3 monthly rows | PASS |
| Monthly averages vs daily means | 3/3 PASS |
| Q2 daily arithmetic FX mean | PASS |
| MYS IMF raw rows and attributes | PASS (reused) |
| Country-specific asset/liability directional mapping | PASS as source-concept crosswalk |
| Asset numeric leg at BNM display rounding | PASS |
| Liability numeric leg at BNM display rounding | PASS |
| BNM rounded net identity | REVIEW; 0.1 RMbn difference |
| Same-vintage BNM preliminary ↔ IMF panel alignment | NOT_ESTABLISHED |
| MYS full dual-leg national validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 7. Interpretation and remaining dependency
- This task closes the previously open official FX-series identity, raw acquisition, SHA-256, daily/monthly arithmetic cross-check and two independent numeric leg comparisons at BNM's published rounding.
- The Q3-2026 BNM bulletin exposes Q2 as preliminary and was published 18-Nov-2026; the IMF panel exact-row archive was retrieved 19-Nov-2026. Temporal proximity does not prove same-vintage alignment or identical revision cut-off. Keep the full MYS country validation PARTIAL until that vintage bridge is documented.
- The numeric diagnostic is country-specific. It does not authorize a universal sign transform, universal scale transform, or the 63-country aggregate.
- Next exact action: obtain an explicit BNM/DOSM vintage/revision note or source publication metadata that establishes the Q2 preliminary cut-off relative to the IMF panel; if no such bridge exists, retain NOT_ESTABLISHED and proceed to the next eligible cohort country. Do not repeat the FX download or the 60-row reconciliation absent a source revision.

## 8. Protected invariants
No production code, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights or trade gates changed. No paid API, synthetic data, fabricated timestamp, silent raw-value rescaling, forward-fill, imputation, netting or aggregate authorization. UNKNOWN is never PASS.

## 9. Official references
- BNM/Data.gov daily 1200 metadata and CC BY 4.0: https://data.gov.my/data-catalogue/exchangerates_daily_1200
- BNM/Data.gov monthly metadata, avg definition and CC BY 4.0: https://data.gov.my/data-catalogue/exchangerates
- Malaysia API filter/response docs: https://developer.data.gov.my/request-query
- IMF scale semantics: `docs/GCR_IMF_BOP_SCALE_SEMANTICS_20261119.md`
- Cross-country empirical scale/sign evidence: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_CROSS_COUNTRY_PART3_20261119.md` and `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_CURRENT_VINTAGE_SUPPLEMENT_20261119.md`
