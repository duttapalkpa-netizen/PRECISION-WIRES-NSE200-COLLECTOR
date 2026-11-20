# Thailand THA Q2-2026 — Bank of Thailand vs IMF portfolio dual-leg reconciliation
Date: 2026-11-20 (Asia/Kolkata)
Decision: **BOT official USD table capture PASS; archived IMF exact-row extraction PASS; both numeric portfolio legs PASS at BOT two-decimal USD-million display precision; same-vintage status NOT_ESTABLISHED; THA full national validation PARTIAL / NOT PASS; 63-country aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight and selection
- Reopened current Master Continuity Ledger (blob SHA `396152cfd62e2c7888e4f40947b019cca7e875b8`), GCR master priority queue (blob SHA `9c49ce9064f207ce18de6a0e8c80ba8b11e126d9`), fixed 63-country Q2-2026 cohort (blob SHA `1f767e22095865c8e5f87c2cfca55d9104b91e3e`), IMF panel report and prior country-validation reports.
- MYS public vintage bridge was bounded: national Q2 components are dated 18-Nov preliminary, while IMF observation-level source revision date is unavailable. MYS remains PARTIAL; no repeated FX or IMF query.
- POL workbook retrieval remains blocked; TUR's 87 USDm liability difference remains unresolved after August/September PDF snapshots; MEX and ARG have numeric passes but their source vintages remain unaligned. The next eligible direct USD source selected was THA.
- THA is in the existing 63-country cohort with both A_NFA_T and L_NIL_T present at 2026-Q2. No cohort rebuild or new IMF query.

## 2. Official Bank of Thailand source
- Source: Bank of Thailand, EC_XT_049_S2 “Balance of Payments (US$)”.
- Official page: https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?language=ENG&reportID=1022
- Unit: millions of USD; frequency: quarterly.
- Page header: Q2/2026 p (preliminary).
- Page metadata: Last Updated 30 Sep 2026 14:33.
- Official note: for each financial-account component, positive indicates an increase in net financial assets or liabilities; negative indicates a decrease. Net financial-account balance is assets minus liabilities.
- Portfolio parent row: 4,917.43 USDm.
- Portfolio assets: +4,679.07 USDm.
- Portfolio liabilities: -238.36 USDm.
- Accounting identity: assets minus liabilities = 4,679.07 - (-238.36) = 4,917.43 USDm. This is exact at displayed precision.
- The BOT source sign convention directly aligns asset increase/decrease with IMF A_NFA_T and liability increase/decrease with IMF L_NIL_T; no country-specific sign inversion is applied.

## 3. Existing archived IMF panel — exact THA Q2 rows
- Reused committed normalized panel: `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv`.
- Panel SHA-256: `e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a`.
- Original source artifact: workflow run `44474218174`, artifact `14505862034`, ZIP SHA-256 `1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f`.
- IMF dataflow IMF.STA:BOP(21.0.0), indicator P_F, quarter 2026-Q2, country THA, unit USD, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
- Raw IMF observations remain unchanged; comparison-only derived USD-million display uses the empirically supported `OBS_VALUE / 1,000,000` convention from the existing country-validated scale benchmarks.

| Entry | IMF raw OBS_VALUE (USD) | Derived IMF USDm | BOT USDm | IMF−BOT USDm | Tolerance | Result |
|---|---:|---:|---:|---:|---:|---|
| A_NFA_T | 4,679,073,421.50334 | 4,679.07342150334 | 4,679.07 | +0.00342150334 | ±0.005 | PASS |
| L_NIL_T | -238,358,188.710181 | -238.358188710181 | -238.36 | +0.001811289819 | ±0.005 | PASS |

- Both absolute residuals are within BOT's two-decimal USD-million display rounding tolerance. No sign reversal, netting, raw rescaling or value overwrite.
- BOT portfolio identity is independently satisfied at display precision; this is not used to replace either individual leg.

## 4. Reproducible capture
- Research-only script: `scripts/research/reconcile_tha_q2_2026_bot_imf.py`.
- Workflow: `.github/workflows/gcr_tha_q2_2026_bot_imf.yml`.
- NSE collector paths-ignore guard commit: `b983bf461ab852d295b1eea0d17553c322d53953` (script/workflow excluded from full NSE collector push trigger).
- Script commit: `6a618eb337a6782cb3b87c28a87efcafd958938f`.
- Workflow commit: `768221a7a53842ebc712df57030c19d7bca4b5c9`.
- GitHub Actions run: [44689541630](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44689541630), run number 1, conclusion SUCCESS; job ID `136131786969`; duration ~13 seconds.
- Artifact: `14607329438`, name `gcr-tha-q2-2026-bot-imf-44689541630`, 39,093 bytes, ZIP SHA-256 `70328900a9e0058385c6ac7efa5384f86d10508a5056f8f16e40c3afd5b24aec`, retained until 2027-02-18.
- Raw BOT HTML: HTTP 200; 551,847 bytes; SHA-256 `b4a42305fe18668c91e1feadd70ada0537f6e2f8c5b13ef59dd1fdcbd4d00f80`; retrieved 2026-11-20T06:41:16.952209Z.
- Response headers preserved in artifact summary; cache control is no-cache/no-store. BOT source's displayed Last Updated field is 30 Sep 2026 14:33.
- Artifact contains raw BOT HTML, exact two-row reconciliation CSV and JSON summary/receipt. No raw IMF panel re-download was required.

## 5. Vintage gate
- BOT public table reports Q2/2026 as preliminary and exposes last-updated timestamp 30-Sep-2026 14:33.
- The IMF panel was retrieved 19-Nov-2026, but the public IMF BOP dataset landing page does not expose observation-specific submission/revision timestamp or historical vintage.
- Retrieval date is not source-vintage date. Do not infer that BOT's 30-Sep snapshot and IMF's 19-Nov archived panel share the same input cut-off.
- Same-vintage status: **NOT_ESTABLISHED**.
- Numeric dual-leg check: 2/2 PASS. Full THA country admission remains **PARTIAL / NOT PASS** pending a source-vintage bridge.

## 6. Acceptance matrix
| Gate | Status |
|---|---|
| THA fixed-cohort Q2 both-leg presence | PASS (reused) |
| BOT official USD BOP page retrieved and raw bytes hashed | PASS |
| BOT Q2/2026 p status and last-updated timestamp captured | PASS |
| BOT portfolio asset/liability rows parsed | PASS |
| BOT financial-account sign semantics captured | PASS |
| BOT asset-minus-liability identity | PASS |
| IMF exact THA Q2 rows extracted from archived panel | PASS |
| Asset numeric comparison | PASS |
| Liability numeric comparison | PASS |
| Same-vintage BOT ↔ IMF bridge | NOT_ESTABLISHED |
| THA full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 7. Exact next action
- Seek a public BOT revision history or archived prior-quarter snapshot for the Q2 portfolio rows, and an IMF observation-level source-submission/vintage attribute for THA Q2. If unavailable, preserve NOT_ESTABLISHED and proceed to the next eligible cohort country; do not repeat the same BOT page capture.
- Next likely source candidates remain from the fixed 63-country cohort only; no cohort rebuild. Consider Philippines or Colombia only after preflight of source accessibility and existing completed reports.

## 8. Protected invariants
No production code, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights or trade gates changed. No paid source, synthetic data, fabricated timestamps, FX conversion, imputation, forward-fill, netting or aggregate authorization. UNKNOWN is never PASS.
