# Global Capital Rotation — IMF BOP Observation Access Boundary (Superseded 2026-11-19)

**Status:** Public SDMX 3.0 observation access is now verified. The earlier BLOCKED conclusion based only on the API portal/Swagger sign-in page is superseded by direct endpoint testing.

## Official source context
- IMF API documentation: https://data.imf.org/en/Resource-Pages/IMF-API — IMF says data are available through SDMX 2.1 and SDMX 3.0 APIs; Swagger explorer sign-in is a separate UI requirement.
- IMF BOP dataset: https://data.imf.org/en/datasets/IMF.STA%3ABOP — annual and quarterly frequency; public dataset metadata.
- The exact tested public endpoints are:
  - Dataflow: `https://api.imf.org/external/sdmx/3.0/structure/dataflow/IMF.STA/BOP/21.0.0?references=all`
  - DSD: `https://api.imf.org/external/sdmx/3.0/structure/datastructure/IMF.STA/DSD_BOP/24.0.0?references=all`
  - Observations: `https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0/{key}`
- These metadata and observation endpoints returned HTTP 200 from GitHub Actions without an API key, cookie or sign-in.

## DSD and exact series definition
- Dataflow: `IMF.STA:BOP(21.0.0)`
- DSD: `IMF.STA:DSD_BOP(24.0.0)`
- DSD SHA-256: `1541c0e65af5801acb86767a183a124537aa4b6a04d2a4e528c23d73d4b2019b`
- Dimensions: `COUNTRY.BOP_ACCOUNTING_ENTRY.INDICATOR.UNIT.FREQUENCY`
- Codelists: `CL_BOP_COUNTRY(1.0.0)`, `CL_BOP_ACCOUNTING_ENTRY(3.3.0)`, `CL_BOP_INDICATOR(10.0.0)`, `CL_UNIT(2.13.0)`, `CL_FREQ(1.2.0)`.
- Populated indicator: `P_F` — Portfolio investment, Total financial assets/liabilities.
- Accounting entries retained separately: `A_NFA_T` — Assets, Net acquisition of financial assets; `L_NIL_T` — Liabilities, Net incurrence of liabilities.
- Unit `USD`, frequency `Q`.
- The initial `P_MV` exact-key probe returned HTTP 200 but no observations for the tested BRA/IND keys; it was rejected. Broad country captures showed `P_F` as populated and exact-key queries then succeeded.

## Verified pilot panel
- Countries: Brazil (BRA), India (IND); not a defined EM universe.
- Window: 2015-Q1 to 2026-Q3.
- BRA A_NFA_T: 47 observations, 2015-Q1–2026-Q3.
- BRA L_NIL_T: 47 observations, 2015-Q1–2026-Q3.
- IND A_NFA_T: 46 observations, 2015-Q1–2026-Q2.
- IND L_NIL_T: 46 observations, 2015-Q1–2026-Q2.
- Total: 186 non-empty observations.

## Independent validation
- Run 44472944620; artifact 14504732476; ZIP SHA-256 `2e00a175837e1ad5e98346b114c4ec5a9d55ddf38833938711e9a3106a331d6c`.
- 4/4 exact queries HTTP 200 and CSV parse PASS.
- 186/186 exact query values match the independent broad raw country captures.
- 186/186 raw-to-normalized source attribute comparisons match; 32 source columns preserved.
- 0 duplicate keys; 0 missing or mismatched values; all quarters contiguous within each observed series.
- India 2026-Q3 was not returned and remains missing; no forward-fill or synthetic observations.

## Remaining limitations
1. `SCALE=6` maps to `CL_UNIT_MULT` code 6 = Millions. Brazil source-to-source validation across 47 quarters for each portfolio flow entry proves IMF API `OBS_VALUE` is already USD: BCB monthly USD-million values sum by quarter, and `IMF OBS_VALUE / 1,000,000` matches the BCB quarterly sum in all 94/94 checks (tolerance 0.15 USD million; maximum residual 0.12192411). Do not multiply IMF API values by 10^6 again. India still needs independent country-source validation.
2. The pilot is quarterly BOP transactions, not daily SEBI FPI/FII flows.
3. Brazil and India are only a pilot pair, not an approved emerging-market membership universe.
4. BOP_AGG is a separate annual group aggregate dataset. IMF says group totals include estimates for non-reporting economies; assess it separately and do not substitute it silently for country-reported observations.
5. Do not net assets and liabilities, infer sign conventions, or promote this pilot to a production factor until methodology, vintages, country coverage and transformations are validated.

## SCALE operational validation — Brazil 94/94 PASS\n- Official BCB SGS 22906: net acquisition of financial assets, monthly, million USD.\n- Official BCB SGS 22924: net incurrence of liabilities, monthly, million USD.\n- 47 quarters × 2 series = 94/94 PASS, 0 review, 0 blocked.\n- Reported in `docs/evidence/imf_bop_20261119/bcb_scale_reconciliation/summary.json` and `quarter_reconciliation.csv`; raw source JSONs are retained in the same folder.\n- BCB series metadata: https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net and https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net.\n\n## Durable evidence
- Report: `docs/GCR_IMF_BOP_PUBLIC_OBSERVATION_ACCESS_PART1_20261119.md`
- Machine summary: `docs/evidence/IMF_BOP_PORTFOLIO_PILOT_BRA_IND_2015Q1_2026Q3.json`
- Compressed normalized panel and four raw series: `docs/evidence/IMF_BOP_PORTFOLIO_*.csv.gz`


## Status update — 2026-11-19 (supersedes earlier access BLOCKED conclusion)
- The public observation route is now verified for `IMF.STA:BOP(21.0.0)` via anonymous SDMX 3.0 GET:
  `https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0/{series-key}?c[TIME_PERIOD]=ge:2015-Q1&c[TIME_PERIOD]=le:2026-Q3&format=csvdata`
- No API key, cookie, login or paid service used.
- A 154-member WEO October-2026 G200 EMDE panel has been retrieved (9,299 unique rows); 154/154 membership codes map to the BOP country codelist. Exact-key sample check: 24/24 requests PASS, 1,106/1,106 exact-to-broad observation/attribute matches.
- Durable report: `docs/GCR_IMF_BOP_EMDE_PORTFOLIO_PANEL_20261119.md`; evidence folder: `docs/evidence/imf_bop_emde_20261119/`.
- The prior sign-in redirect only applies to the Swagger/API explorer link; it does not prevent the tested public SDMX 3.0 observation GET route.
- Remaining blockers are not access: coverage gaps (40/154 members with no observations for the selected entries; 83/308 country-entry pairs empty), `SCALE=6` unit interpretation mismatch requiring national-source reconciliation, revision/vintage and BPM basis controls, and no EMDE aggregate yet. Preserve all missingness; no scale conversion or aggregation until cleared.


## Scale/sign status refinement — Brazil (2026-11-19)
- The `SCALE=6` code label is “Millions” in the DSD-referenced unit-multiplier codelist.
- Brazil's two BOP P_F legs have now been independently reconciled against BCB SGS monthly series 22906 (assets) and 22924 (liabilities): five quarters × two legs = 10/10 PASS using `IMF OBS_VALUE / 10^6` in USD million. Maximum absolute residual 0.12192411 million, below the 0.15 million bound from three monthly values rounded to 0.1 million.
- This resolves the Brazil scale/sign mapping for the tested series only. It does not generalize to India or other EMDE members; no EMDE-wide conversion/aggregate is authorized.
- Evidence report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_20261119.md`; durable raw BCB receipts: `docs/evidence/imf_bop_20261119/bcb_scale_reconciliation/`.


## Scale/sign status refinement — Brazil + India (2026-11-19)
- Brazil BCB SGS 22906/22924: 10/10 checks across 2015-Q1–Q4 and 2026-Q3 pass for `OBS_VALUE/1e6`.
- India RBI Table197 BPM6 quarterly USD-million table: 12/12 checks across 2024-Q2–2025-Q3 pass; assets require sign reversal from RBI credit-minus-debit, liabilities map directly.
- The scale/sign normalization is independently supported for both pilot countries, not yet for the other 152 WEO EMDE members. Do not apply it to the full panel or publish an EMDE aggregate until more national-source checks, vintages and BPM basis are closed.
- Evidence reports: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_20261119.md` and `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md`.
