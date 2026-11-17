# Fed H.10 Relative Dollar Basket Pattern Scan — 2026-11-17

## Purpose
A bounded Python data-analysis pass over the already captured official Fed H.10 ZIP artifact. No new source data was generated and no additional network download was needed. This is a cross-basket FX-pressure diagnostic for the Global Capital Rotation & Relative-Attraction Overlay, not a capital-flow measure or trading signal.

## Input provenance
- Source: Federal Reserve Board H.10 official data package, captured in GitHub Actions run #8 / ID 44036104490.
- Source package Prepared: 2026-11-16T16:47:01.
- Retrieved: 2026-11-17T07:06:14.336027+00:00.
- Raw ZIP SHA-256: c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77.
- Raw archive: artifact ID 14306134441, expires 2027-02-15; this scan used the local copy of that exact artifact.
- XML series definitions were read from the package's own H10_struct.xml:
  - JRXWTFB_N.B: Nominal Broad Dollar Index.
  - JRXWTFN_N.B: Nominal Advanced Foreign Economies Dollar Index.
  - JRXWTFO_N.B: Nominal Emerging Market Economies Dollar Index.
- All three have index unit Index:_1997_Jan_100, multiplier 1.
- Status filter: only OBS_STATUS=A, finite numeric values; ND/non-available rows excluded. Each selected series has 5,231 valid observations. Dates were aligned by exact observation date; no forward fill.

## Python method
- Parsed the captured ZIP and H.10_data.xml / H10_struct.xml using Python.
- For n-observation change, used n prior valid observations plus current = n+1 observations, formula (latest/base - 1)*100.
- Windows:
  - 5 prior observations + current: 2026-11-05 to 2026-11-13.
  - 20 prior observations + current: 2026-10-15 to 2026-11-13.
  - 60 prior observations + current: 2026-08-18 to 2026-11-13.
- 2026-11-11 was ND and excluded; no imputation.
- 60-observation correlation uses aligned daily percentage changes on the 61-date endpoint window (60 return observations).

## Results
| Series | 5 prior valid obs | 20 prior valid obs | 60 prior valid obs |
|---|---:|---:|---:|
| Nominal Broad Dollar | +0.941681% | +0.889205% | +3.082118% |
| Nominal Advanced Foreign Economies | +1.951566% | +1.056856% | +3.484809% |
| Nominal Emerging Market Economies | -0.028413% | +0.726701% | +2.692781% |

### Relative-basket findings
- Over the latest 5-observation window, the advanced-economy dollar index rose +1.951566%, while the EM index was -0.028413%. The short-window dollar-strength movement was therefore much more pronounced against the advanced-economy basket than the EM basket.
- Over 20 valid observations, advanced index +1.056856% vs EM +0.726701%. The EM/advanced index ratio declined by 0.326702% over the same window.
- Over 60 valid observations, advanced +3.484809% vs EM +2.692781%.
- Correlation of aligned daily percentage changes over the latest 60 return observations:
  - Broad vs Advanced: 0.887519
  - Broad vs EM: 0.853091
  - Advanced vs EM: 0.516721

## Interpretation boundary
These are weighted U.S. dollar exchange-value indexes against different currency baskets. A higher index means the U.S. dollar strengthened against that basket. The recent data show stronger USD appreciation against the advanced-economy basket than against the EM basket. This is relative FX pressure / basket divergence only. It does NOT establish capital inflows into EM, risk-on positioning, FII flows, or equity-sector attraction. It must not be interpreted as proof of investor capital rotation.

## Research decision
- Useful research feature candidate: `fed_h10_advanced_minus_em_change_pct_5obs` / `20obs` as a separately named relative basket divergence diagnostic.
- Do not create a production feature yet; no historical PIT vintage backtest, regime stratification, predictive testing, or false-positive analysis has been completed.
- Do not map these series to ICE DXY or overwrite `dxy_change_pct_20d`.
- Do not modify Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, or existing classifier.

## Status
- Existing artifact reused: PASS.
- Python XML parsing and official series-definition extraction: PASS.
- ND filtering and exact-date alignment: PASS.
- 5/20/60 observation calculations: PASS.
- Cross-basket correlation: PASS.
- Capital-flow inference: NOT_SUPPORTED.
- Predictive validation / historical PIT vintages: NOT_DONE.
- Production integration: NOT_AUTHORIZED.
