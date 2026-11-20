# GCR ZAF Q2-2026 — IMF / SARB / OECD FX Reconciliation
Date: 2026-11-20
Status: PARTIAL — liability leg passes; asset leg remains REVIEW because the residual is outside the strict rounding bound.

## Progress log
- Reused the already archived 154-member WEO EMDE panel, 63-country Q2-2026 dual-leg cohort, ZAF exact-key sample, and SARB September-2026 BOP table. No rebuild or repeated source extraction.
- Exact IMF source receipts: run 44474458684; artifact 14505009889; ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`.
- Exact ZAF rows are archived at `docs/evidence/imf_bop_emde_20261119/exact_sample_checks/ZAF_A_NFA_T.csv` and `ZAF_L_NIL_T.csv`; source receipt is `exact_sample_checks/summary.json`.

## 1. IMF exact Q2-2026 observations
Dataflow `IMF.STA:BOP(21.0.0)`; DSD `IMF.STA:DSD_BOP(24.0.0)`; indicator `P_F`; unit USD; frequency Q.
| Entry | Exact Q2-2026 raw OBS_VALUE (USD) | Raw file SHA-256 | Exact GET |
|---|---:|---|---|
| A_NFA_T | +4,174,854,099.360882 | `6a4211d9c6475113a652474fa5463acab1a7e2c4e4341cb37352d1d80d0248bb` | HTTP 200 |
| L_NIL_T | -547,771,649.1229077 | `af1655d66cfd815b4aece4dc923ab8f6510c8f26e19cfb05ccb928803c45070f` | HTTP 200 |

Exact retrieval timestamps: assets 2026-11-19T06:45:24.259338Z; liabilities 2026-11-19T06:45:24.711771Z. Both series end at 2026-Q2. The archived source attributes carry SCALE=6 (Millions). Keep raw OBS_VALUE and SCALE separate; comparison display uses raw OBS_VALUE / 1,000,000.

## 2. SARB national source
Official South African Reserve Bank, September 2026 Quarterly Bulletin, published 29 September 2026, Statistical Tables attachment 8, Table KB502, page S-87 / PDF page 3. Unit: R millions.
- 5644K — net incurrence of portfolio liabilities: -9,023.
  - 5756K equity and investment fund shares: -34,161.
  - 5757K debt securities: +25,138.
  - Component sum: -9,023 (exact).
- 5660K — net acquisition of portfolio financial assets: -68,769.
  - 5758K equity and investment fund shares: -42,915.
  - 5759K debt securities: -25,854.
  - Component sum: -68,769 (exact).
- SARB note 4: positive net incurrence of liabilities means inflow; negative means outflow. Negative net acquisition of assets means outflow; positive disposal means inflow. Previous four years are preliminary and subject to revision.
Official PDF: https://www.resbank.co.za/content/dam/sarb/publications/quarterly-bulletins/quarterly-bulletin-publications/2026/september/8-tables-external-economic-accounts.pdf

## 3. FX source and conversion rule
OECD Main Economic Indicators, South Africa quarterly average of daily rates, national currency per USD; OECD descriptor CCUSMA02, country ZAF, quarterly, not seasonally adjusted. Q2-2026 = **16.4719712481963 ZAR per USD**. The 17 August 2026 OECD release vintage is visible in ALFRED; FRED current series also displays the rounded value 16.47197. This is an OECD-sourced quarterly average, not a SARB-published rate. No exchange rate is inferred from monthly BOP flows.
- Series: https://fred.stlouisfed.org/series/CCUSMA02ZAQ618N
- Vintage receipt: https://alfred.stlouisfed.org/release?et=&ob=pv&od=desc&pageID=3&rd=2026-08-17&rid=205&t=exchange+rate
- OECD exchange-rate definition: https://www.oecd.org/en/data/indicators/exchange-rates.html

Conversion: SARB R million / (ZAR per USD) = USD million. Apply sign mapping only where the official concept/sign definition requires it. Compare each entry separately.

## 4. Reconciliation
| Leg | SARB source value | SARB converted USDm | IMF USDm | IMF − SARB USDm | Decision |
|---|---:|---:|---:|---:|---|
| Liabilities (5644K ↔ L_NIL_T) | -9,023 Rm | -547.779003742 | -547.771649123 | +0.007354619 | PASS |
| Assets (5660K ↔ A_NFA_T) | -68,769 Rm | +4,174.910152756 after sign reversal | +4,174.854099361 | -0.056053395 | REVIEW |

Asset sign reversal is explicit: SARB note 4 describes a negative net acquisition of assets as an outflow, while IMF A_NFA_T is positive for this outflow in the archived national mapping. The reversal aligns the economic direction; it is not an arbitrary fit.

Strict rounding bound: SARB reports whole R millions. Half-unit rounding at the Q2 FX rate is 0.5 / 16.4719712481963 = approximately **0.0304 USD million**. Liability residual is within this bound. Asset residual (0.0561 USD million) is outside it. Do not enlarge tolerance to force acceptance. Possible causes such as differing underlying FX aggregation, revisions, or source compilation must remain hypotheses until verified.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| Existing Q2 cohort membership | PASS |
| IMF exact-key retrieval and raw evidence | PASS |
| SARB national table, labels, codes, unit, components and sign note | PASS |
| OECD quarterly FX series, unit, frequency and release vintage | PASS |
| Liability numerical reconciliation | PASS |
| Asset numerical reconciliation | REVIEW / OUTSIDE_ROUNDING_BOUND |
| ZAF full dual-leg national-source validation | PARTIAL / NOT PASS |
| 63-country EMDE aggregate | NOT_AUTHORIZED |

## 6. Next action
Keep ZAF in PARTIAL. Do not re-download the IMF panel or repeat SARB extraction. The next country-level validation should be selected from the existing 63-country Q2 dual-leg cohort using GDP/market relevance and availability of an official national source, with the same strict concept, sign, unit, vintage and rounding controls. In parallel, only investigate the ZAF asset residual if a more exact official quarterly FX/conversion methodology becomes available.

## Protected invariants
No aggregation, netting, imputation, synthetic observations, silent conversion, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
