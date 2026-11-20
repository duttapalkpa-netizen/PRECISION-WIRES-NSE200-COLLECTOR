# Malaysia MYS Q2-2026 — FX methodology gate and official 1200-middle series specification
Date: 2026-11-20 (Asia/Kolkata)

Decision: **Official rate-series identity and BPM6 conversion methodology PASS. Exact daily raw-data capture and checksum NOT_DONE; prior 60-row candidate is NOT_ADMITTED as a final series. MYS remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## Continuity preflight and duplicate rejection
- Reopened current GCR priority queue (blob SHA `61f64b7f50711ffc48e2c637089764269e81fb5c`), MYS daily-FX candidate report (SHA `42712a95fc22b81c536f00a242988b1c7f15e5a3`), MYS archived IMF extraction report (SHA `025d58375f47eab1b66dc808e033727e9a733308`) and MYS national crosswalk (SHA `749a2bf15c5e29ef8756ca36a7cd1dede16ed510`).
- Reused prior IMF extraction, BNM component extraction, fixed cohort and candidate CSV. No new IMF request, no panel rebuild, no cohort rebuild and no repeated national extraction.
- The Master Continuity Ledger path/body was not independently resolved in this execution. The priority queue records referenced ledger blob SHA `ce94bbcfcfd080685e21c483260a93d6d2d60434`; do not claim the ledger body was reopened.

## Official series identity — PASS
Official Malaysia Open Data catalogue dataset:
- Dataset ID: `exchangerates_daily_1200`
- Landing page: https://data.gov.my/data-catalogue/exchangerates_daily_1200
- Full CSV: https://storage.data.gov.my/finsector/exr/daily_1200.csv
- Full Parquet: https://storage.data.gov.my/finsector/exr/daily_1200.parquet
- Source agency: Bank Negara Malaysia.
- Dataset description: daily MYR exchange rates at 1200, acting as mid-day reference.
- Fields: `date`, `rate_type`, and currency columns including `USD`.
- `rate_type=middle` is explicitly defined as midpoint between buying and selling rates.
- The catalogue distinguishes 0900 start-of-day, 1130 selected-bank best counter rates, 1200 mid-day reference, and 1700 end-of-day reference. 1130 has no official midpoint.
- Catalogue states full data are downloadable since 2003 and attributes source to BNM; licence CC BY 4.0.
- This resolves the prior ambiguity about which BNM dataset and rate type to use. It does NOT validate the earlier manually transcribed 60-row candidate values.

## BPM6 methodology — PASS as methodology, not data capture
Official IMF BPM6 Sixth Edition, hosted by DOSM:
https://www.dosm.gov.my/uploads/content-downloads/file_20220920111121.pdf
Chapter 3, paragraphs 3.104–3.108: transaction-time market rate is the principle; daily average exchange rates for daily transactions are a good approximation; if daily rates cannot be applied, use the shortest available period average; use midpoint between buying and selling rates to exclude spread.
Chapter 9 (exchange-rate effects) explains that daily average rates are preferable to a simple beginning/end period average where flows occur throughout the period.
Implication for this Q2 flow crosswalk: use observed BNM 1200 middle rates for each actual trading day in 2026-Q2; compute the arithmetic mean across observed trading-day rates, with no weekend/holiday forward-fill. This is an approximation under BPM6, not an assertion that all individual transaction timestamps are known.

## Exact capture status and rejected shortcuts
- Browser access to the official catalogue metadata succeeded.
- Direct binary CSV open through the web reader returned unsupported content-type; API JSON endpoint did not resolve through the available web reader; container download attempt failed. No exact daily_1200 CSV bytes or source SHA-256 captured in this execution.
- Therefore no daily_1200 raw rows, count, arithmetic mean or recalculated MYS leg comparison is claimed.
- Prior candidate CSV `docs/evidence/malaysia_mys_q2_2026_bnm_daily_usd_myr_candidate.csv` (60 rows; prior candidate mean 3.9992166667) is NOT_ADMITTED as final input until its dates and values are independently matched to the official `daily_1200.csv` with `rate_type=middle`. Do not overwrite or silently relabel it.
- The prior candidate diagnostic residuals are also not accepted as final numeric evidence.
- No monthly three-value unweighted average, no 0900/1700 substitution, no 1130 best-counter rate, no rate selected merely because it yields a close reconciliation.

## Updated acceptance matrix
| Gate | Status |
|---|---|
| IMF MYS Q2 exact raw rows | PASS (reused prior archive) |
| BNM Q2 portfolio asset/liability rows | PASS (reused prior extraction) |
| Official BNM 1200 daily dataset identified | PASS |
| Middle rate type semantics | PASS |
| BPM6 conversion methodology | PASS |
| Official daily_1200 raw bytes and SHA-256 | NOT_DONE |
| 2026-Q2 official 1200-middle rows | NOT_DONE |
| 2026-Q2 daily mean calculation | NOT_DONE |
| Separate asset/liability numeric reconciliation on admitted FX | NOT_DONE |
| Same-vintage alignment | NOT_ESTABLISHED |
| MYS full validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## Next exact action
1. Retrieve the exact official `daily_1200.csv` bytes or official OpenAPI filtered records for 2026-04-01 through 2026-06-30; retain HTTP response, retrieval timestamp, row count and SHA-256.
2. Filter `rate_type=middle`; select USD and dates; verify unique dates, no duplicates, no missing trading days against the source calendar, no weekend/holiday forward-fill.
3. Compute and report the arithmetic mean of the actual observed daily 1200-middle rates. Archive the daily rows and calculation output.
4. Independently test Malaysia-specific scale/sign mapping for A_NFA_T and L_NIL_T against the BNM BPM6 source notes and exact national publication vintage. Do not infer from Brazil/India or candidate closeness.
5. Keep each leg separate; no netting or aggregate authorization. If the official raw download remains inaccessible, preserve NOT_DONE and use a supported source-access route; do not fabricate or reconstruct the daily series from the prior candidate.

## Protected invariants
No production code, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights or trade gates changed. No paid APIs, synthetic data, fabricated timestamps, silent conversions, imputation, forward-fill, netting or aggregate authorization. UNKNOWN is never PASS.

## Reproducibility references
- Prior candidate report: `docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_DAILY_FX_CANDIDATE_RECONCILIATION_20261120.md`
- Prior candidate CSV: `docs/evidence/malaysia_mys_q2_2026_bnm_daily_usd_myr_candidate.csv`
- IMF raw extraction: `docs/GCR_MALAYSIA_MYS_Q2_2026_IMF_RAW_ROW_EXTRACTION_20261120.md`
- BNM national crosswalk: `docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_IMF_PORTFOLIO_SOURCE_CROSSWALK_20261120.md`
- Official BNM-sourced dataset: `https://data.gov.my/data-catalogue/exchangerates_daily_1200`
- Official IMF BPM6 manual: `https://www.dosm.gov.my/uploads/content-downloads/file_20220920111121.pdf`
