# Mexico (MEX) Q2-2026 — Banxico/IMF portfolio BOP dual-leg validation; Colombia API migration boundary
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 137
Status: MEX separate-leg numerical comparison PASS at published rounding; same-vintage alignment NOT_ESTABLISHED; MEX full national validation PARTIAL / NOT PASS. COL remains PARTIAL / BLOCKED.

## 1. Continuity preflight and selection
- Reopened current GCR priority queue, fixed 63-country 2026-Q2 both-leg cohort, Continuation 136, BanRep series-discovery record, existing IMF 12-country exact-key receipt and archived raw asset/liability CSVs.
- COL was selected for the preceding step. Its official series catalogue was confirmed, but exact export remained unavailable. A newly found official BanRep SDMX API migration explains why the old API route is no longer valid. The new SDMX guide's listed dataflows do not include BOP; no BOP Flow ID was guessed.
- MEX was already in the immutable 63-country cohort and the existing 12-country exact-key sample. MEX exact asset and liability IMF rows were reused; no IMF query and no cohort rebuild.
- Completed PASS work for other countries was not repeated.

## 2. Official Banxico Q2-2026 BOP source
- Official Banco de México publication: “La Balanza de Pagos en el Segundo trimestre de 2026”.
- Publication date: 25-Aug-2026.
- Official PDF: https://www.banxico.org.mx/publicaciones-y-prensa/balanza-de-pagos/%7BE333A05C-EB45-9A4A-6F1D-591845A64896%7D.pdf
- PDF page 6 (printed page 6; extracted PDF page 5), Cuadro 3, unit “Millones de dólares”.
- Q2-2026 Portfolio Investment (II):
  - A. Net acquisition of financial assets: +USD 8,937 million.
  - B. Net incurrence of liabilities: +USD 10,561 million.
  - Portfolio investment balance (A-B): -USD 1,624 million.
- The table explicitly defines financial account as net lending (+) / net borrowing (-), and footnote says net borrowing means net incurrence of liabilities exceeds net acquisition of financial assets. No sign transform was applied.
- The publication states BOP components can be revised in future releases. Publication vintage retained as 25-Aug-2026; no claim of exact match to the later IMF observation vintage.

## 3. Existing IMF exact-key evidence — reused, no new query
- Existing exact sample: run 44474458684; artifact 14505009889; ZIP SHA-256 588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7.
- Existing exact-key receipt docs/evidence/imf_bop_emde_20261119/exact_sample_checks/summary.json confirms both MEX requests HTTP 200 and exact-to-broad match for all 46 quarterly observations per entry, 2015-Q1 to 2026-Q2.
- MEX A_NFA_T exact request: retrieved 2026-11-19T06:45:19.095563Z; 4,893 bytes; response SHA-256 a404aca5a719b9558e75b9483b925d18011fa2d9199937d275956782a84c5014.
- MEX L_NIL_T exact request: retrieved 2026-11-19T06:45:19.493209Z; 4,741 bytes; response SHA-256 1a7de8eb3d258875fbffbde987ce22db437eadbdd9c93e05acec12a4ab7785c7.
- Existing archived raw panel blob SHAs: asset 15449e87c9057291a1f52f2f8cd9805df55f9fb8; liability 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Exact MEX rows:
  - A_NFA_T, P_F, USD, Q, 2026-Q2, OBS_VALUE=8,937,255,098, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
  - L_NIL_T, P_F, USD, Q, 2026-Q2, OBS_VALUE=10,561,285,114, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
- Original OBS_VALUE and SCALE remain preserved separately. For comparison with Banxico's USD-million table, USD amounts are expressed in USD millions; no FX conversion and no sign reversal.

## 4. Separate-leg arithmetic and independent identity
- Asset: IMF 8,937.255098 USDm vs Banxico 8,937 USDm; residual (Banxico minus IMF) = -0.255098 USDm.
- Liability: IMF 10,561.285114 USDm vs Banxico 10,561 USDm; residual (Banxico minus IMF) = -0.285114 USDm.
- Both residuals are within the ±0.5 USDm half-unit display-rounding bound of Banxico's whole-million table.
- Independent identity: 8,937 - 10,561 = -1,624 USDm; exactly matches Banxico's Q2 portfolio investment A-B line.
- Separate asset and liability numeric checks: PASS at published rounding. Sign alignment: PASS. Period: PASS. Currency/unit after explicit USD-to-USDm expression: PASS.

## 5. Vintage and admission boundary
- Banxico BOP Q2 report is dated 25-Aug-2026 and explicitly notes that BOP components can be revised in future publications.
- IMF exact-key observations were retrieved 19-Nov-2026. The exact Banxico observation vintage corresponding to that later IMF receipt is not established.
- Therefore MEX national-source separate-leg numeric comparison is PASS at published rounding, but same-vintage/revision bridge remains NOT_ESTABLISHED.
- MEX full national dual-leg validation: PARTIAL / NOT PASS. 63-country aggregate: NOT_AUTHORIZED.
- Do not promote the MEX numeric result to full country validation until same-vintage/revision gate is satisfied.

## 6. COL — official API migration root-cause and stop boundary
- BanRep portal notice states that its SDMX web-service API was updated from 26-Oct-2026 to support XML, JSON and CSV; the prior version was to remain only until 15-Nov-2026.
- Official new technical guide, October 2026 v4.0: https://suameca.banrep.gov.co/archivos/webservices/sdmx_v_3_1/GUIA_CONSUMO_SDMX_V_3_1.pdf
- New REST endpoint documented as https://totoro.banrep.gov.co/sdmx/rest/; agency ID is BANREP.CIE; REST supports XML, JSON and CSV.
- The new guide's published DataFlow list names IBR, TRM, TPM, TIB, COLCAP, monetary aggregates, DTF, UVR and TES; it does not list a BOP dataflow. Do not invent a BOP Flow ID or assume the generic IBR examples apply to BOP.
- The official multiple-download catalogue still lists the separate quarterly BOP portfolio asset-acquisition and liability-incurrence series through 2026-Q2, current USD millions, disclosed 01-Sep-2026. However, the catalogue/export retrieval bridge returned 502/timeout and no series IDs or values were captured.
- The old REST route used in earlier attempts is not a valid current route after the announced retirement. This explains why repeated old-endpoint attempts would be unproductive. No old endpoint retry was made in this continuation.
- COL exact Q2 national values/raw export/hash remain NOT_CAPTURED; COL PARTIAL / BLOCKED. No IIP stock substitution or net-to-leg inference.

## 7. Acceptance matrix
| Gate | MEX | COL |
|---|---|---|
| Fixed 63-country Q2 both-leg cohort membership | PASS | PASS |
| Official national BOP source identified | PASS | PASS (catalogue series locator only) |
| Separate asset and liability values captured | PASS | NOT_DONE |
| Sign/concept alignment | PASS | NOT_ESTABLISHED |
| Unit/period alignment | PASS | Catalogue metadata PASS; exact values NOT_DONE |
| Separate-leg numerical comparison | PASS at ±0.5 USDm rounding | NOT_DONE |
| Raw national response bytes / SHA-256 | NOT_CAPTURED in this task; official PDF source inspected | NOT_CAPTURED |
| Same-vintage/revision bridge | NOT_ESTABLISHED | NOT_ESTABLISHED |
| Full country validation | PARTIAL / NOT PASS | PARTIAL / BLOCKED |
| 63-country aggregate admission | NOT_AUTHORIZED | NOT_AUTHORIZED |

## 8. Next exact actions
1. MEX: obtain a dated Banxico Q2-2026 revision/vintage record or a later official release exposing the same two portfolio transaction legs; align it to the IMF receipt vintage. Until then MEX remains PARTIAL.
2. COL: use only a supported official data export/API route if BanRep publishes a BOP Flow ID or the multiple-download service becomes retrievable; otherwise preserve BLOCKED and move to the next unvalidated fixed-cohort member. Do not repeat the retired REST endpoint.
3. Next country selection must reuse the fixed cohort and existing IMF archive; no IMF query or cohort rebuild.

## 9. Protected invariants
₹0; free official sources only. No synthetic data, fabricated timestamps, inferred sign/scale conversion, stock-as-flow, net-to-leg back-solving, duplicate IMF requests, or cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
