# Uruguay (URY) Q2-2026 — BCU preliminary-status and Q3 release vintage gate (Continuation 245)

Date: 2026-11-25 (Asia/Kolkata)
Decision: EXISTING Q2 NUMERIC DUAL-LEG COMPARISON REUSED; NO NEW NUMERIC PASS CLAIMED. BCU OFFICIAL Q2 REPORT STILL LABELS FIGURES PRELIMINARY. OFFICIAL CALENDAR SCHEDULES “CUENTAS INTERNACIONALES 3ER TRIMESTRE 2026” FOR 30-DEC-2026. NO Q2 OBSERVATION-SPECIFIC REVISION/VINTAGE BRIDGE FOUND IN THE SOURCES CHECKED. URY REMAINS PARTIAL / NOT PASS; VINTAGE PENDING; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity and duplicate-prevention preflight
- Re-fetched current default-branch Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, 63-country matrix and C244 MEX report before continuing.
- Re-searched Library Mother File continuation 1–53 and URY historical context. Prior URY report snippets confirm existing national Q2 Table 9 comparison: official BCU portfolio assets +USD519m, liabilities −USD192m, reported net +USD710m, separate legs sum +USD711m (USD1m published rounding); existing numeric dual-leg comparison was previously recorded PASS at published precision.
- Existing accepted arithmetic and archived IMF exact rows reused; no IMF re-query, no repeat calculation, no cohort rebuild.
- The BCU Q2 PDF is used only to check its published status/revision language and the release calendar. It is not represented as a new data capture.

## 2. New official BCU publication-schedule evidence
- BCU official Q2 report: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Balanza%20de%20Pagos/informe_m6.pdf
- It is titled “Informe de Balanza de Pagos y Posición de Inversión Internacional — Segundo trimestre 2026”. Executive summary and tables label estimates as preliminary; Table 9 reports portfolio investment by institutional sector (PDF text lines 681–703).
- BCU official statistics calendar page: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Paginas/Default.aspx
- Calendar search result lists “Cuentas Internacionales — 3er Trimestre 2026” for 30-Dec-2026 as pending. This is the next scheduled international-accounts release, not evidence that Q2 has already been revised.
- No Q2 revision number, observation-specific timestamp, cutoff vintage, revision table or explicit BCU-to-IMF vintage bridge was found in the material checked.

## 3. Existing numeric evidence reused (not recalculated)
- Controlling earlier URY report: Library conversation record and prior GCR URY reconciliation; existing official BCU Table 9: assets +519 USDm; liabilities −192 USDm; reported net +710 USDm; asset/liability components sum +711 USDm due to published rounding.
- Prior archived IMF dual-leg numerical reconciliation is retained as PASS, but this alone does not prove the IMF and BCU observations are from the same vintage.
- Do not confuse portfolio transaction flows with portfolio investment positions in Table 2; the latter are stocks and are not substituted.

## 4. Acceptance boundary
| Gate | Status |
|---|---|
| Ledger / Queue / Registry / matrix preflight | PASS |
| Library Mother File and prior URY numeric report context | PASS |
| Existing separate-leg numerical comparison | PASS (reused; not recalculated) |
| BCU Q2 report status | PRELIMINARY |
| Official Q3 2026 international-accounts release schedule | FOUND — 30-Dec-2026 |
| Q2 revision identifier / observation-specific timestamp | NOT_CAPTURED |
| BCU Q2 vintage ↔ archived IMF vintage bridge | NOT_ESTABLISHED |
| URY full national validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 5. Next exact action
1. After 30-Dec-2026, inspect the official BCU “Cuentas Internacionales 3er Trimestre 2026” release.
2. If it contains revised Q2 portfolio assets and liabilities, capture only the Q2 revisions, the revision cutoff/identifier, source bytes and retrieval metadata/hash where supported.
3. Compare both Q2 legs with the already archived IMF rows; require explicit observation-vintage alignment, not merely matching values or release date.
4. If the release is absent or no Q2 vintage bridge is supplied, retain URY vintage PENDING/UNKNOWN and advance to the next eligible fixed-cohort task after fresh preflight.

## 6. Protected invariants
₹0; free official sources only. No IMF re-query, cohort rebuild, net-to-leg back-solving, synthetic values/timestamps, unsupported FX/sign/scale conversion, stock-as-flow substitution or aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 remain unchanged. UNKNOWN is never PASS.

## 7. Source references
- BCU Q2 2026 official report: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Balanza%20de%20Pagos/informe_m6.pdf
- BCU official statistics calendar: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Paginas/Default.aspx
- Web evidence: turn142592view0, turn795836view0, turn874156search0, turn874156search4.
- Prior URY numeric report remains controlling for the previously accepted dual-leg arithmetic; no new numeric validation is claimed in C245.
