# GCR — Mexico (MEX) Q2-2026 Banxico SIE IIP transaction cross-check and series-version API route
Date: 2026-11-27 (Asia/Kolkata)
Continuation: 271
Decision: **A distinct official Banxico SIE IIP analytical table independently displays Q2-2026 portfolio-transaction asset and liability legs equal to the latest Q3 BOP release values. Banxico's official SIE API documentation exposes a per-series versions-metadata route. This strengthens the current-value corroboration and identifies a new revision-lineage route, but the exact portfolio series IDs and observation-specific version payload have not yet been captured. MEX remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity and duplicate-prevention preflight
- Re-fetched the current Master Continuity Ledger, Priority Queue, Historical Task Registry and fixed 63-country matrix.
- Reopened the C270 MEX Q3-release recheck and its previous C252 baseline; reused the archived IMF receipt only.
- C270's key unresolved gate is exact Banxico observation-level revision/version lineage. No August release extraction, IMF re-query, cohort rebuild, or production work was repeated.
- This task tests a distinct official SIE analytical-table surface and the explicitly documented series-version API route; it does not repeat the C270 PDF table extraction.

## 2. New official Banxico SIE evidence
Official SIE analytical table CA737, “Estado Integrado de la Posición de Inversión Internacional (trimestral)”:
https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadroAnalitico&idCuadro=CA737&sector=1

The rendered Q2-2026 table states “Abr-Jun 2026”, units “Millones de Dólares”, and labels the relevant column “Transacciones de la cuenta financiera”:
- Assets → Portfolio investment → transaction: +USD9,480m.
- Liabilities → Portfolio investment → transaction: +USD10,561m.

These are the same rounded Q2-2026 values as the Banxico Q3 BOP release captured in C270. The CA737 table is an IIP reconciliation presentation; its transaction column is corroborative evidence of the reported portfolio transactions, not a separate revision timestamp or proof that the IMF receipt and Banxico data share a vintage.

Official SIE structure CE174 is labelled BPM6, quarterly, USD millions, current flows; the accessible rendered structure page currently shows data only through Q1-2026, so it is not substituted for the CA737 Q2 observations:
https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CE174&locale=en

## 3. New revision-lineage route fingerprint
Official Banxico SIE API Swagger page:
https://www.banxico.org.mx/SieAPIRest/swagger/index.html

The published API description lists:
- GET /v1/series/{idSeries}
- GET /v1/series/{idSeries}/datos
- GET /v1/series/{idSeries}/datos/oportuno
- GET /v1/series/{idSeries}/datos/{fechaInicial}/{fechaFinal}
- GET /v1/series/{idSeries}/versiones
- GET /v1/series/{idSeries}/versiones/{idVersion}/datos

The existence of a series-version metadata endpoint is a genuinely distinct route candidate for observation revision lineage. However:
- Exact SIE series IDs for the portfolio asset and liability parent rows have not yet been extracted from the CA737/CE174 table metadata.
- No API request was made; no version list, version ID, response bytes, schema, timestamp or hash was captured.
- API availability in the Swagger catalogue does not prove that every series exposes historical vintages or that a particular version maps to the 25-Aug / 25-Nov Q2 BOP releases.
- Do not guess IDs or construct unverified API requests.

## 4. Reconciliation against existing evidence
C270 archived IMF receipt (run 44474458684 / artifact 14505009889; dated 19-Nov-2026):
- IMF Q2 asset: +USD8,937.255098m.
- IMF Q2 liability: +USD10,561.285114m.
Latest Banxico Q3-release / CA737 Q2 transaction values:
- Asset: +USD9,480m; IMF minus Banxico = -USD542.744902m (REVIEW / NOT MATCHED).
- Liability: +USD10,561m; IMF minus Banxico = +USD0.285114m (PASS at ±USD0.5m).
The IMF receipt predates the 25-Nov Banxico release; same-vintage is not established. The CA737 cross-check does not close this timing gap or identify why the Q2 asset was revised by +USD543m versus the 25-Aug release.

## 5. Acceptance
| Gate | Status |
|---|---|
| Distinct official SIE CA737 Q2 IIP transaction table located | PASS |
| Q2 portfolio asset transaction value +USD9,480m corroborated | PASS (rounded table value) |
| Q2 portfolio liability transaction value +USD10,561m corroborated | PASS (rounded table value) |
| API series-version endpoint documented by Banxico | PASS (route documentation only) |
| Exact portfolio series IDs | NOT_CAPTURED |
| Version metadata / observation-level revision chain | NOT_CAPTURED |
| Raw API response bytes / retrieval receipt / SHA-256 | NOT_CAPTURED |
| Same-vintage IMF↔Banxico bridge | NOT_ESTABLISHED |
| Asset numeric match to archived IMF row | REVIEW / NOT MATCHED |
| Liability numeric match to archived IMF row | PASS (±USD0.5m) |
| MEX national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 6. Next exact action
1. Inspect the official CA737 structure's series metadata controls to obtain the exact asset and liability portfolio parent series IDs; do not infer IDs.
2. Only after exact IDs are grounded, use the documented official /versiones route to retrieve available version metadata and test whether it exposes observation-specific Q2-2026 revision lineage.
3. Capture exact URL, retrieval timestamp, HTTP status/headers, raw response bytes, schema, version identifiers and SHA-256; compare release dates and Q2 observations without conflating publication vintage and observation vintage.
4. If the official metadata does not expose the required historical lineage, preserve MEX vintage as PENDING and move to the next eligible country under Rank 1.

## 7. Protected invariants
₹0; official/free sources only; no IMF re-query, cohort rebuild, net-to-leg back-solving, unsupported conversion, synthetic data, guessed IDs, terms bypass, workflow dispatch, merge or production change. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 remain unchanged.
