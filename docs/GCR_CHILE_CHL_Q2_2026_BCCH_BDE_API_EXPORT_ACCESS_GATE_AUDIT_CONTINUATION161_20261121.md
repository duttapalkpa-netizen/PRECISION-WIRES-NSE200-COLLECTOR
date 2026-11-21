# GCR Q2-2026 — Chile (CHL) BCCh BDE raw-export/API access gate audit
Date: 2026-11-21
Chapter: গবেষণা যাচাই অব্যাহত 47
Part: 9
Continuation sequence: 161
Status: DOCUMENTED OFFICIAL API/EXPORT ROUTES VERIFIED; API REQUIRES USER ACCOUNT + ENABLED TOKEN; PUBLIC BASKET EXPORT CONTROL DOCUMENTED BUT NOT EXECUTED; RAW BYTES/SHA-256 NOT_CAPTURED; CHL PARTIAL / NOT PASS.

## 1. Continuity preflight
- Re-fetched Master Continuity Ledger, GCR Priority Queue and the exact CHL Continuation 160 report before acting. CHL's two official BCCh BDE monthly flow series and Q2 arithmetic were not repeated.
- Scope is only the unresolved raw-byte/vintage capture gate for series F068.G2.FLU.Z.0.S.A.Z.T.Z.Z.6.0.M (assets) and F068.G2.FLU.Z.0.S.P.Z.T.Z.Z.6.0.M (liabilities).
- No IMF re-query, no cohort rebuild, no paid source, no production changes.

## 2. Official API route — exact access gate
Official BCCh API overview states the BDE API is free, but requires a BDE account and activation of API access. Official access instructions require login, acceptance of terms, activation, then a personal API Key Token valid for one year. The REST GetSeries method returns JSON observations and metadata and requires that token in the request URL. Official documentation also describes Python bcchapi and SOAP options.
Sources:
- https://si3.bcentral.cl/estadisticas/Principal1/Web_Services/index_API_sec1_es.htm
- https://si3.bcentral.cl/estadisticas/Principal1/Web_Services/acceso_api.html
- https://si3.bcentral.cl/estadisticas/Principal1/Web_Services/documentacion.html
- https://si3.bcentral.cl/estadisticas/Principal1/Web_Services/ayuda_soporte.html
Decision: this is a documented, free, technically valid raw-response route, but it is credential-gated. No BDE account/token or user-supplied credentials are available in the research context. Do not invent a token, use another person's credentials, or expose credentials in repository files. Therefore API request NOT_EXECUTED.

## 3. Official BDE basket export route
Official BDE Canasta pages expose an “Exportar a Excel” control with horizontal/vertical layout and “Año seleccionado” / “Todos los años” options. The official basket UI is an alternative interactive export route. However, current browser search/index access only confirms the control's existence; it does not execute the UI's “Aceptar” action or yield the resulting workbook bytes. No downloadable file, export receipt, retrieval timestamp, workbook hash or fresh Q2 series payload was captured.
Source examples:
- https://si3.bcentral.cl/siete/ES/Siete/Canasta?idCanasta=T7KXJ2131
- https://si3.bcentral.cl/siete/ES/Siete/Canasta?idCanasta=T0KVH2135
Status: export UI documented; export action NOT_EXECUTED; workbook bytes NOT_CAPTURED.

## 4. What is and is not established
- Prior Part-8 observations remain source-page observations only: Q2 asset sum USD 5,098.91m; liability sum USD 5,397.51m; difference USD 298.60m, rounding to official Q2 net USD 299m. No change to these numbers.
- Prior archived IMF raw rows remain exactly as recorded in Part 8; no conversion or re-query.
- No exact BDE raw response bytes, JSON/XLSX payload, SHA-256, API updatedAt/createdAt metadata snapshot, publication/revision vintage receipt or same-vintage cut-off alignment obtained in Part 9.
- No exact sign bridge admission or numeric PASS. Existing near-match remains diagnostic only.

## 5. Acceptance matrix
| Gate | Result |
|---|---|
| Previous official Q2 dual-leg monthly observations | PASS — source-page evidence from Part 8 |
| Official BDE API documented and free | PASS |
| API credential gate documented | PASS |
| API account/token available in this research context | NO |
| API request executed | NOT_EXECUTED |
| Official BDE Excel export UI identified | PASS |
| Export action executed / workbook bytes | NOT_EXECUTED / NOT_CAPTURED |
| Raw payload SHA-256 and retrieval receipt | NOT_CAPTURED |
| Same-vintage revision metadata | NOT_ESTABLISHED |
| Exact item/sign/scale bridge | PARTIAL |
| CHL national validation | PARTIAL / NOT PASS |
| Cross-country aggregate | NOT_AUTHORIZED |

## 6. Decision and next bounded action
- The blocker is no longer an unknown API design: BCCh's official API is free but explicitly account/token gated. The basket offers a visible Excel export control, but a live export action is still needed to preserve raw bytes.
- Next action, without asking for or storing secrets: use an authorized BDE session to activate the free API or use the public basket's Excel export, download the two series, then archive exact response/workbook bytes, URL, retrieval timestamp, series IDs, metadata update time and SHA-256. If no authorized session/export action is available, retain CHL PARTIAL and advance to next eligible cohort member.
- ₹0 spend. No synthetic data, no net-to-leg back-solving, no IIP substitution, no annual/H1 allocation, no IMF re-query/cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
