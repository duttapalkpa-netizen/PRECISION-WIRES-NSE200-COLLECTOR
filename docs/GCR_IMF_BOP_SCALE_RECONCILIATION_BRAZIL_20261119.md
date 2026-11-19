# IMF BOP Scale / Sign Reconciliation — Brazil
Date: 2026-11-19
Status: **PASS — Brazil assets and liabilities; 10/10 quarter checks**

## Progress Log
### Completed
- Matched IMF quarterly BOP portfolio-flow values to two official Banco Central do Brasil monthly net-flow series.
- Tested four 2015 calendar quarters plus 2026-Q3 for both assets and liabilities.
- Confirmed `IMF OBS_VALUE / 1,000,000` matches the sum of three BCB monthly observations to within the BCB source's maximum 3-month rounding bound.
- Archived raw BCB JSON, quarter-level comparison CSV/JSON and SHA-256 receipts in GitHub.

### Rejected
- No scale conversion is generalized to India or the other 152 WEO EMDE members from Brazil-only evidence.
- The BCB registered XML header identifies `BOP_BPM6(1.0)`, while the public IMF dataflow queried here is `IMF.STA:BOP(21.0.0)`; similar values do not establish Dataflow alias equivalence.
- RBI Table 196 (2019 publication) uses April–June fiscal quarters; it is not directly aligned to IMF calendar-quarter `2015-Q1`. It is not accepted as a scale validation without a period and series crosswalk.
- No production signal, aggregate or trading admission.

### Next actions
1. Establish an India national-source series crosswalk with explicit fiscal-to-calendar quarter alignment and vintage controls.
2. Repeat scale checks for at least one additional EMDE country and a different reporting vintage.
3. Only then generalize the scale normalization to the 154-member panel and produce converted values.
4. Keep BPM basis and revision/vintage differences visible.

## 1. Official BCB sources
- **SGS 22906** — “Portfolio investment - Net acquisition of financial assets - monthly - net”; unit: million US dollars; monthly. BCB identifies its Department of Economics as source. Dataset metadata: https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net
- **SGS 22924** — “Portfolio investment - Net incurrence of liabilities - monthly - net”; unit: million US dollars; monthly. Dataset metadata: https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net
- Public raw JSON endpoints:
  - https://api.bcb.gov.br/dados/serie/bcdata.sgs.22906/dados?formato=json
  - https://api.bcb.gov.br/dados/serie/bcdata.sgs.22924/dados?formato=json
- IMF panel series:
  - `BRA.A_NFA_T.P_F.USD.Q`
  - `BRA.L_NIL_T.P_F.USD.Q`

## 2. Method
For each calendar quarter:
1. Sum the three monthly BCB observations (BCB values are reported to one decimal place in USD million).
2. Divide the IMF raw quarterly `OBS_VALUE` by (10^6) to express it in USD million.
3. Compare the two results.
4. Maximum cumulative rounding bound is (3 	imes 0.05 = 0.15) million USD, because each of the three monthly BCB values is rounded to one decimal.
5. PASS only when all three monthly values exist, each is one decimal, IMF `SCALE=6`, and absolute difference is at most 0.15 million USD.

No IMF values were changed in the source panel. The normalization is a separately derived reconciliation result.

## 3. Results
<text>All amounts below are USD million.</text>

| Entry | Quarter | BCB monthly sum | IMF raw ÷ 1e6 | IMF − BCB residual | Result |
|---|---|---:|---:|---:|---|
| Assets | 2015-Q1 | -1,273.1000 | -1,273.138947 | -0.038947 | PASS |
| Assets | 2015-Q2 | 512.4000 | 512.497140 | 0.097140 | PASS |
| Assets | 2015-Q3 | -1,145.2000 | -1,145.178767 | 0.021233 | PASS |
| Assets | 2015-Q4 | -1,662.9000 | -1,662.884227 | 0.015773 | PASS |
| Assets | 2026-Q3 | 7,555.7000 | 7,555.691695 | -0.008305 | PASS |
| Liabilities | 2015-Q1 | 17,629.5000 | 17,629.558375 | 0.058375 | PASS |
| Liabilities | 2015-Q2 | 10,036.2000 | 10,036.148646 | -0.051354 | PASS |
| Liabilities | 2015-Q3 | -9,943.2000 | -9,943.234065 | -0.034065 | PASS |
| Liabilities | 2015-Q4 | -3,452.6000 | -3,452.478076 | 0.121924 | PASS |
| Liabilities | 2026-Q3 | -4,860.1000 | -4,860.140999 | -0.040999 | PASS |

- 10/10 checks PASS; 0 REVIEW; 0 missing source rows.
- Maximum absolute residual: 0.12192411 million USD, below the 0.15 million rounding bound.
- Both asset and liability signs match the official BCB monthly net-flow series.

## 4. Interpretation
For the tested Brazil IMF BOP series, the empirically validated transformation to USD million is:
`USD_million = OBS_VALUE / 10^6`.
This reconciles the raw IMF values with BCB's independently published monthly net series across 2015-Q1–Q4 and 2026-Q3. It validates the Brazil scale and sign mapping only. It does not authorize applying the transformation to all EMDE countries, nor does it resolve the BOP6/BOP_BPM6 structure identity mismatch.

## 5. Reproducibility
- Workflow run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44475693836
- Artifact ID: `14506740234`; ZIP bytes 8,004; SHA-256 `08e7702d9c5e393779d6ff635f6d532ddcfcb79be1eb2be18fd840a13f37b79b`.
- BCB 22906 raw JSON: 14,594 bytes; SHA-256 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`.
- BCB 22924 raw JSON: 14,890 bytes; SHA-256 `2064005a5dd42b83ba66aeb21de983ca4286af9662f57c23971b4b7dfe295dbb`.
- Durable evidence commit: `45d2ce937be6c2f89d1ba4ae7fe0d1ad14842266`.
- Files: `docs/evidence/imf_bop_20261119/bcb_scale_reconciliation/`.

## 6. Decision
- Brazil scale/sign mapping: PASS for the two selected BOP portfolio-flow series and five tested quarters.
- India and remaining EMDE scale mapping: NOT_DONE / UNKNOWN pending national-source crosswalk.
- 154-member EMDE aggregate: NOT_AUTHORIZED until country-level unit, period, BPM basis, vintage and missingness checks pass.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged; ₹0 spend; no synthetic data; UNKNOWN is not PASS.
