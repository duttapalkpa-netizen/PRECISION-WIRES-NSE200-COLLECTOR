# Peru (PER) Q2-2026 — BCRP official portfolio-series source-boundary audit
Date: 2026-11-20 (Asia/Kolkata)
Decision: official BCRP series catalogue and API documentation inspected; exact portfolio subseries identified, but complete national A_NFA_T/L_NIL_T coverage is NOT_ESTABLISHED; no Q2 transaction values admitted; numeric comparison NOT_DONE; sign mapping NOT_ESTABLISHED; same-vintage NOT_ESTABLISHED; national validation PARTIAL/BLOCKED; aggregate NOT_AUTHORIZED.

## Continuity and duplicate rejection
- Reused the fixed 63-country Q2-2026 synchronous dual-leg cohort. PER is listed in that cohort. Repository search for a prior PER Q2-2026 national portfolio-flow report returned no matching report; no cohort rebuild or IMF re-query was performed.
- Existing IMF panel/receipt is untouched. No IMF observation values were copied into this source-boundary task.

## Official BCRP evidence
1. BCRPData quarterly series catalogue:
   https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales
   The official catalogue lists:
   - Private-sector financial account, assets — portfolio investment: series **PN39278BQ**, quarterly T1-2012 through T2-2026, last updated 2026-08-20.
   - Private-sector financial account, liabilities — portfolio investment: series **PN39285BQ**, quarterly T1-2012 through T2-2026, last updated 2026-08-20.
   - Public-sector financial account, liabilities — portfolio investment: series **PN39404FQ**, quarterly T1-2012 through T2-2026, last updated 2026-08-20.
   The catalogue therefore confirms separately identifiable portfolio subseries, but it does not expose a single national total asset portfolio flow series in the inspected catalogue. The asset code is explicitly under the private-sector financial account; public-sector portfolio liabilities are separately itemized. Do not silently equate the private-sector asset series with the full-economy A_NFA_T without a documented scope bridge.
2. BCRPData official API developer guide:
   https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf
   The guide documents GET/POST retrieval, 1–10 same-frequency series codes, and CSV/JSON/XML/XLS outputs. Its documented GET pattern is:
   https://estadisticas.bcrp.gob.pe/estadisticas/series/api/[series-codes]/[format]/[start-period]/[end-period]/[language]
   A bounded Q2-2026 request was attempted using the documented pattern for PN39278BQ and PN39285BQ in JSON and CSV; the web reader could not retrieve the API response. No raw bytes, Q2 observations, response headers, receipt or SHA-256 were obtained. Do not claim values or capture.
3. BCRP Q2-2026 Macroeconomic Report Annex 1 reproduces the broader BOP table and says the financial account and its components (private sector, public sector, short-term capital) are expressed as net assets of liabilities. It reports private-sector assets and liabilities at aggregate level, not portfolio-only national total legs in that table. Source locator found: https://www.bcrp.gob.pe/docs/Publicaciones/Nota-Estudios/2026/nota-de-estudios-59-2026.pdf . This general accounting identity is not enough to infer a portfolio-specific sign mapping or fill the missing asset scope.

## Fail-closed source boundary
- Exact private-sector portfolio asset series discovery: PASS (PN39278BQ).
- Exact private-sector portfolio liability series discovery: PASS (PN39285BQ).
- Public-sector portfolio liability series discovery: PASS (PN39404FQ).
- Complete national portfolio asset scope / public-sector asset treatment: NOT_ESTABLISHED.
- API retrieval/raw-byte capture: NOT_DONE (documented endpoint request inaccessible in this session).
- Q2-2026 values: NOT_EXTRACTED.
- Portfolio sign mapping: NOT_ESTABLISHED.
- Same-vintage bridge to IMF Q2 panel: NOT_ESTABLISHED.
- Numeric dual-leg comparison: NOT_DONE.
- PER national validation: PARTIAL/BLOCKED / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.
- IIP positions/stocks and broad private-sector/public-sector financial-account totals are not substitutes for portfolio transaction flows. Do not aggregate sector fragments or infer missing public-sector asset components.

## Next exact action
Use the documented BCRP API via a supported raw-byte route to capture exact series values and metadata. Before numeric admission, resolve the scope bridge: whether PN39278BQ is the complete portfolio asset transaction series for the economy or whether additional public-sector portfolio asset flows exist elsewhere; reconcile private and public portfolio liability components without double counting; obtain BCRP portfolio-specific sign definitions and vintage/revision evidence. If scope remains incomplete, retain PER as BLOCKED and move to the next eligible fixed-cohort country. No IMF re-query or cohort rebuild.

## Invariants
No paid sources, no fabricated values/timestamps, no inferred sign flip, no stock-flow substitution, no netting, no synthetic rows, no forward-fill, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
