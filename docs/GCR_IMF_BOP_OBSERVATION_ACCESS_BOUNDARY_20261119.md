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
1. `SCALE=6` and `PRECISION=6` are retained exactly; no scale conversion or currency conversion is applied until SCALE semantics are independently resolved.
2. The pilot is quarterly BOP transactions, not daily SEBI FPI/FII flows.
3. Brazil and India are only a pilot pair, not an approved emerging-market membership universe.
4. BOP_AGG is a separate annual group aggregate dataset. IMF says group totals include estimates for non-reporting economies; assess it separately and do not substitute it silently for country-reported observations.
5. Do not net assets and liabilities, infer sign conventions, or promote this pilot to a production factor until methodology, vintages, country coverage and transformations are validated.

## Durable evidence
- Report: `docs/GCR_IMF_BOP_PUBLIC_OBSERVATION_ACCESS_PART1_20261119.md`
- Machine summary: `docs/evidence/IMF_BOP_PORTFOLIO_PILOT_BRA_IND_2015Q1_2026Q3.json`
- Compressed normalized panel and four raw series: `docs/evidence/IMF_BOP_PORTFOLIO_*.csv.gz`
