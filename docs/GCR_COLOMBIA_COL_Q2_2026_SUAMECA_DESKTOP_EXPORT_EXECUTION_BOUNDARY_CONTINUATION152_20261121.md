# Continuation 152 — Colombia COL Q2-2026 SUAMECA desktop export execution boundary
Date: 2026-11-21 (Asia/Kolkata)
Status: OFFICIAL EXPORT PROCEDURE VERIFIED; DESKTOP EXPORT NOT EXECUTED IN THIS SESSION; RAW VALUES / BYTES / SHA-256 NOT_CAPTURED. COL remains PARTIAL / BLOCKED, NOT PASS.

## 1. Continuity preflight and duplicate rejection
- Reopened current Master Continuity & Acceptance Ledger, GCR Master Priority Queue, immutable 63-country Q2-2026 cohort, COL source-boundary audit and Continuation 151.
- Reused the existing 63-country cohort and archived IMF panel receipt. No IMF re-query, cohort rebuild, repeat BanRep 502 attempt, or repeat source-label discovery.
- Continuation 151 already establishes the two official quarterly series families, USDm unit, Q2-2026 coverage and 2026-09-01 catalogue disclosure date. Exact series IDs and observations remain unexposed in the indexed catalogue result.

## 2. New official BanRep procedure evidence
- Reopened BanRep's official user guide: https://www.banrep.gov.co/es/preguntas-frecuentes/como-usar-nuevo-portal-estadisticas-economicas
- The guide's “Descarga múltiple de datos” instructions specify:
  1. Open the Economic Statistics Portal and select “Descarga múltiple de datos”.
  2. Add the required series using each series' shopping-cart control (both portfolio net acquisition of financial assets and portfolio net incurrence of liabilities).
  3. Select “Ver datos de series” to confirm the selected variables.
  4. Set the required period/range for each series (Q2-2026 only) and select “Ver datos de series” again.
  5. Use the data-view controls to edit the range/apply filters; select “Exportar a Excel” to generate the export file.
- The same guide explicitly states that the export function for prebuilt tables is available only in the desktop version of the portal. It does not state that a separate API is available for the multiple-download service.
- Current official catalogue page remains indexed with both separate portfolio series, current USD millions, quarterly frequency, availability 2000-Q1 through 2026-Q2 and disclosure date 2026-09-01. The page's live fetch still returned HTTP 502 in this session.
- Execution boundary: this session has no interactive desktop browser/control surface for the BanRep portal. Therefore the documented desktop workflow could be verified but not clicked/executed. No series IDs, exact Q2 values, export bytes, retrieval receipt/timestamp, SHA-256 or observation-specific revision metadata were obtained. This is an execution limitation, not evidence that the data are absent.

## 3. Acceptance matrix
| Gate | Status |
|---|---|
| Fixed 63-country cohort membership | PASS (reused) |
| Official separate quarterly portfolio series identity | PASS (Continuation 151) |
| Unit USDm / quarterly / coverage through Q2-2026 | PASS (Continuation 151) |
| Official desktop export procedure documented | PASS |
| Desktop export actually executed | NOT_EXECUTED |
| Exact series IDs and Q2 asset/liability values | NOT_CAPTURED |
| Raw export bytes + SHA-256 + retrieval receipt | NOT_CAPTURED |
| Sign definition / observation vintage bridge | NOT_ESTABLISHED |
| IMF-national separate-leg numeric comparison | NOT_DONE |
| COL full national validation | PARTIAL / BLOCKED; NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 4. Exact handoff / next action
A desktop session must:
- Open https://suameca.banrep.gov.co/descarga-multiple-de-datos/
- Add exactly these two quarterly series: (a) “Balanza de pagos - Cuenta financiera - inversión de cartera - adquisición neta de activos financieros - trimestral”; (b) “Balanza de pagos - Cuenta financiera - inversión de cartera - pasivos netos incurridos - trimestral”.
- Set the period to 2026-Q2 only, export both series together, and preserve the untouched original export.
- Supply the exported file here. Then record its exact bytes, SHA-256, series IDs/labels, Q2 values, units, sign/methodology notes and publication/revision metadata; compare each leg separately with the already archived IMF Q2 raw rows.
- Until that raw export exists, keep COL PARTIAL / BLOCKED and aggregate NOT_AUTHORIZED. Do not use IIP stocks, qualitative narrative, portfolio net total, or other financial-account totals as substitutes.

## 5. Protected invariants
₹0; official/free sources only. No synthetic data, fabricated timestamps, inferred values, net-to-leg back-solving, unsupported sign/scale transformations, IMF re-query, cohort rebuild, aggregate admission or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
