# Argentina (ARG) Q2 2026 INDEC–IMF Portfolio BOP Reconciliation
Date: 2026-11-20
Status: PARTIAL / NOT PASS — numerical legs pass; same-vintage gate not established.

## Scope and preflight
- Preflighted the current Master Continuity Ledger, GCR priority queue, MEX detail report, TUR detail report, POL source-gate report and IMF EMDE panel report before selecting the next eligible country.
- Completed PASS items were not repeated. MEX Banxico current-series check was not repeated. Selected ARG from the existing fixed 12-country IMF exact-key sample.
- No new IMF request, sample rebuild, cohort rebuild, synthetic value, or aggregation was performed.

## Immutable IMF source receipt
- Workflow run: 44474458684.
- Artifact: 14505009889.
- ZIP SHA-256: 588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7.
- IMF dataflow: IMF.STA:BOP(21.0.0); indicator P_F; unit USD; quarterly; entries A_NFA_T and L_NIL_T.
- ARG A_NFA_T raw CSV: 5,173 bytes; SHA-256 31ed92d953089ee94eb3c46aa486e8ff32f738e2c4c5e994f40d60e5952160ab.
- ARG L_NIL_T raw CSV: 5,005 bytes; SHA-256 51e19d9729de105b99f65601155b7c721ec0b0a593e262957c09e87b6b46cfc2.
- Q2 2026 exact IMF observations: A_NFA_T = USD 2,230,206,321.95952 (+2,230.20632195952 USDm); L_NIL_T = USD 7,041,052,823.63644 (+7,041.05282363644 USDm).

## Official national evidence
- INDEC Q2 2026 Balance of Payments, International Investment Position and External Debt report:
  https://www.indec.gob.ar/uploads/informesdeprensa/bal_09_26BA83A84318.pdf
- Report date: Buenos Aires, 29 September 2026; report cover identifies September 2026. It states figures from 2024 through Q2 2026 are provisional and subject to revision (PDF p.2).
- Financial account table I.13 (PDF p.21) reports Q2 2026 portfolio investment:
  - ANAF (net acquisition of financial assets): +2,230 USDm.
  - ENP (net incurrence/issuance of liabilities): +7,041 USDm.
  - Net portfolio balance: -4,811 USDm.
- INDEC footnotes define ANAF as net acquisition of financial assets and ENP as net issuance/incurrence of liabilities. The report's BPM6 framing and direct portfolio category provide the country-level concept bridge to IMF A_NFA_T and L_NIL_T. No FX or sign transformation applied.
- The report explicitly explains portfolio assets rose USD 2,230m and external liabilities USD 7,041m; portfolio inflow balance USD 4,811m (PDF p.21).
- Revision annex compares September 2026 and June 2026 releases for earlier periods through Q1 2026; it does not provide a prior-vintage Q2 2026 portfolio asset/liability comparison. Therefore the annex does not prove Q2 vintage identity.

## Reconciliation
All amounts USDm; residual = IMF exact − INDEC displayed integer:
| Leg | IMF exact | INDEC | Residual | Rounding gate |
| A_NFA_T / ANAF | +2,230.206322 | +2,230 | +0.206322 | PASS (±0.5) |
| L_NIL_T / ENP | +7,041.052824 | +7,041 | +0.052824 | PASS (±0.5) |
- INDEC balance identity: 2,230 − 7,041 = −4,811 USDm; agrees with the published portfolio balance.
- The two values fit the whole-USDm rounding interval. This is numeric agreement, not proof of same vintage.

## Acceptance matrix
- Existing IMF exact-key raw receipt and hashes: PASS.
- Official INDEC Q2 2026 report and publication date: PASS.
- Portfolio concepts and signs: PASS.
- Asset numerical comparison: PASS at published rounding.
- Liability numerical comparison: PASS at published rounding.
- Q2 2026 same-vintage bridge: NOT_ESTABLISHED.
- ARG full national dual-leg validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Exact next action
Seek an INDEC Q2 2026 versioned SDMX-ML historical vintage or a dated source-revision snapshot for the portfolio asset and liability flows, and establish whether the IMF 2026-11-19 receipt reflects that same national vintage. INDEC publishes current MBP6 series and SDMX-ML archives, but only a versioned snapshot/change record can close this gate. If unavailable, preserve ARG as PARTIAL and advance to the next eligible cohort member. Do not infer same-vintage from small residuals.

## Protected invariants
No cross-country aggregation, netting, imputation, forward-fill, synthetic observations, silent sign transforms, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.


## 2026-11-20 — bounded official vintage-access check
- Official INDEC international accounts page lists the current BOP SDMX-ML archive (BOP.xml), but the retrieval interface rejected its text/xml content type; the official Datos Argentina MBP6 quarterly CSV resource link timed out. This does not establish that the live files contain historical vintages or revision logs. No same-vintage evidence was obtained. Preserve ARG PARTIAL / NOT PASS; do not repeatedly retry the same failed public routes.
- Next exact action remains an accessible versioned Q2 2026 archive/change record or advance to another eligible country.
