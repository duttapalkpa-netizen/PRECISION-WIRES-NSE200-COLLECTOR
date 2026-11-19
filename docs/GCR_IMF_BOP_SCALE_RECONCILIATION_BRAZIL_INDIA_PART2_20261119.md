# GCR — IMF BOP SCALE / SIGN validation: Brazil + India
Date: 2026-11-19
Decision: **TWO-COUNTRY BENCHMARK PASS (18/18); 154-country admission remains pending**

## Progress Log
### Completed
- October 2026 WEO EMDE membership: 154/154 Appendix names cross-checked to 154 unique workbook G200 ISO3 codes; 154/154 exact code-presence checks against IMF BOP COUNTRY(1.0.0).
- Quarterly IMF BOP Data Portal panel acquired for 154 WEO EMDE members, 2 accounting entries, 2015-Q1 to 2026-Q3: 9,299 non-empty observations; 9,299 unique keys; no duplicates; 12-country exact-key validation 1,106/1,106.
- IMF DSD_BOP(24.0.0) maps optional series attribute SCALE to IMF CL_UNIT_MULT(1.0.2); code 6 is labelled “Millions (10^6)”.
- Independent national-source scale/sign tests now pass for Brazil and India:
  - Brazil: 10/10 quarterly comparisons against BCB SGS 22906/22924, tolerance ±0.15 million USD.
  - India: 8/8 quarterly comparisons against RBI Table 197, tolerance ±0.5 million USD (integer-million display rounding).
  - Combined: 18/18 comparisons pass; no failed comparisons.
- Empirical transform for these tested Data Portal payloads: `OBS_VALUE / 1,000,000` gives the national-source US$ million amount. Do not multiply the raw API payload by 10^6 a second time.

### Rejected / not authorized
- No second multiplication by 10^6.
- No forward fill, synthetic zero, or missing-country imputation.
- No aggregation of the 154-country panel yet.
- Do not conflate the IMF Data Portal BOP series with the older BCB-registered SDMX BOP_BPM6 XML series. A separate old XML-versus-SGS reconciliation still has 201/381 monthly mismatches from 2010-01; that historical source-vintage discrepancy remains open.
- No production factor weights, trading signals or production admission.

## 1. Brazil benchmark — official BCB monthly data
BCB Open Data Portal identifies:
- SGS 22906: “Portfolio investment — Net acquisition of financial assets — monthly — net”, unit: Million US dollars, source BCB/DEPEC. <https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net>
- SGS 22924: “Portfolio investment — Net incurrence of liabilities — monthly — net”, unit: Million US dollars, source BCB/DEPEC. <https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net>

For each selected quarter, three monthly BCB values were summed in US$ million and compared with IMF Data Portal quarterly `OBS_VALUE / 1,000,000`.
- Quarters: 2015-Q1, 2015-Q2, 2015-Q3, 2015-Q4 and 2026-Q3.
- Entries: `A_NFA_T` ↔ BCB 22906; `L_NIL_T` ↔ BCB 22924.
- 10/10 pass; maximum absolute residual 0.121925 million USD; tolerance 0.15 million USD (three BCB monthly values each rounded to 0.1 million).
- BCB raw source SHA-256: SGS 22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30` (14,594 bytes); SGS 22924 `2064005a5dd42b83ba66aeb21de983ca4286af9662f57c23971b4b7dfe295dbb` (14,890 bytes).
- Independent reconstruction from archived BCB monthly JSON and the WEO/EMDE IMF quarterly panel reproduced all ten comparisons as PASS.
- Brazil reconciliation script: `scripts/research/reconcile_imf_bop_scale_brazil_bcb.py`. The workflow's data-validation steps succeeded, but its final automatic Git push failed because another commit moved `main` concurrently; this report and CSV preserve the independently reconstructed results.

## 2. India benchmark — official RBI BPM6 Table 197
RBI Table 197 is “Standard Presentation of India’s Balance of Payments as per BPM6 — Quarterly — US Dollar”, in US$ million. It presents “Portfolio Investment in India” and “Portfolio Investment by India” credit/debit/net. Source: https://rbi.org.in/SCRIPTs/PublicationsView.aspx?id=24022 (31 July 2026).

Four quarters (2024-Q2 to 2025-Q1):
- `L_NIL_T) divided by 1e6 matches RBI “Portfolio Investment in India” net.
- `A_NFA_T) divided by 1e6, with sign reversed, matches RBI “Portfolio Investment by India” net.
- 8/8 comparisons within ±0.5 million USD; maximum absolute difference 0.490 million USD.
- Detailed rows: `docs/evidence/IMF_BOP_IND_SCALE_RECONCILIATION_2024Q2_2025Q1.csv`.

## 3. Consolidated scale/sign decision
For the tested IMF Data Portal `IMF.STA:BOP(21.0.0)` / `IMF.STA:DSD_BOP(24.0.0)` portfolio flow payloads:
- Keep raw `OBS_VALUE` unchanged in the archive.
- For comparison/output in US$ million, divide the raw API `OBS_VALUE` by 1,000,000.
- Preserve `SCALE=6` as source metadata. It describes the “Millions” scale code, but the API payload is empirically already expanded to base USD in the tested Brazil and India series; do not apply the scale a second time.
- `A_NFA_T` and `L_NIL_T` remain separate measures; sign comparisons depend on the national table's presentation convention. No netting of the two entries was performed.
- Brazil SGS and India RBI are independent national sources, covering two countries and both accounting entries. This is sufficient for a two-country benchmark gate, not for an unconditional all-154-country admission.

## 4. Evidence provenance
- EMDE panel artifact: run 44474620936 / artifact 14505452613 / ZIP SHA-256 `b23854fa433b46b29bb2d8094ec9bc14d2cd6c58fdc1771fa9428ca6ae3aed17`.
- Brazil/India exact-key pilot run 44475474198. Data capture, scale/sign reconciliation and independent panel validation steps passed; final commit step failed on a concurrent `main` ref update. Exact panel SHA-256 `8ef39ecdefc4dd042d6e7a74e84aaf95aa9c66162de36164667d2bc6ad74e778`, 186 rows, 186 unique keys, 0 duplicates; all 186 exact values matched the broad raw observations and all source attributes matched.
- Brazil BCB SGS raw source hashes listed above; official BCB dataset pages are linked in Section 1.
- India comparison CSV: `docs/evidence/IMF_BOP_IND_SCALE_RECONCILIATION_2024Q2_2025Q1.csv`.
- Brazil comparison CSV: `docs/evidence/IMF_BOP_BRA_SCALE_RECONCILIATION_2015Q1_2026Q3.csv`.

## 5. Remaining gates
1. Keep all 154 WEO EMDE members and 40 no-observation countries in the completeness matrix; no imputation.
2. Verify scale/sign behavior on additional country sources before treating the transform as fully universal across all members.
3. Resolve BPM6/BPM7 basis, revision/vintage alignment and the legacy BCB registered XML-versus-SGS structural break.
4. Only then evaluate country coverage thresholds and any EMDE aggregate. No aggregate or trading signal is approved.

## Invariants
₹0 spend; free official sources only. No synthetic observations or fabricated timestamps. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged. UNKNOWN is not PASS.
