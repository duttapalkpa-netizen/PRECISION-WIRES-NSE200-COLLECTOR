# Honduras HND Q2-2026 — BCH official BOP source and XLSX access gate
Date: 2026-11-21 (Asia/Kolkata)
Chapter: 47 / Part-15
Continuation: 167
Decision: **HND fixed-cohort membership PASS; no prior dedicated HND Q2-2026 national dual-leg report found; BCH quarterly BOP source and official XLSX locator discovery PASS; XLSX/SDMX byte retrieval BLOCKED; Q2-2026 national portfolio assets/liabilities NOT_CAPTURED; HND PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight and duplicate exclusion
- Re-fetched current Master Continuity Ledger (blob SHA `58a441fa12795dd1b7494ce0ce6d1e7497f1f5df`), GCR Master Priority Queue (blob SHA `4765bb3fc43718cdee5aae84be6c7cc2d6f202b5`), duplicate-prevention registry (blob SHA `e2db1e783d440aca9755f211ff704235b9b330b8`) and immutable 63-country Q2-2026 cohort (blob SHA `1f767e22095865c8e5f87c2cfca55d9104b91e3e`).
- Cohort explicitly includes HND — Honduras.
- Repository searches for HND/Honduras and HND Q2-2026 national portfolio dual-leg validation found no dedicated prior country report. Cohort file and generic source indexes were not treated as a country validation.
- Reused existing cohort only; no cohort rebuild and no IMF re-query.

## 2. Official BCH source-family evidence
- BCH official dynamic Balance of Payments page: https://www.bch.hn/estadisticas-y-publicaciones-economicas/reportes-dinamicos/sector-externo/balanza-pagos
  - Page states frequency is quarterly and annual.
  - Page provides “Obtener serie de Datos”.
  - Page note: positive (negative) sign for reserves and related items means a decrease (increase) in assets vis-à-vis non-residents. This sign note is explicitly scoped to reserves and related items; do not generalize it to portfolio investment.
- BCH official economic/financial dissemination calendar:
  https://www.bch.hn/estadisticos/GIE/LIBCalendario%20PDF/Calendario%20de%20Divulgaci%C3%B3n%20de%20Informaci%C3%B3n%20Econ%C3%B3mica%20y%20Financiera.pdf
  - Lists “Informe de Balanza de Pagos, Posición de Inversión Internacional y Deuda Externa” as quarterly, 90 days after quarter-end, PDF.
  - Lists “Balanza de Pagos Trimestral” as quarterly, preliminary 90 days after quarter-end and final after two years, PDF/Excel/PPTX/png.
  - Lists IIP tables separately as quarterly. Do not confuse IIP positions with BOP flows.
- BCH official SDDS/NSDP page:
  https://www.bch.hn/EN/economical-statistics/special-data-dissemination-standard/data-dissemination-system
  - Lists Balance of Payments with Browse Data, Download in SDMX and DSBB Metadata.
- Official Q3-2025 BCH report indexed in the official domain includes “Inversión de Cartera” chart with separate Activos/Pasivos, in USD millions, but it is a Q3-2025 report, not Q2-2026. It is source-family context only and cannot provide target-quarter observations:
  https://www.bch.hn/estadisticos/EME/Informe%20BOP%20PII%20y%20Deuda/Informe%20de%20Balanza%20de%20Pagos%20Posici%C3%B3n%20de%20Inversi%C3%B3n%20Internacional%20y%20Deuda%20Externa%20III%20trim_2025.pdf

## 3. Exact official export locators and retrieval boundary
- The dynamic BCH BOP page's “Obtener serie de Datos” link resolves to the official workbook locator:
  https://www.bch.hn/estadisticos/EME/Series%20pblicas/Balanza%20de%20Pagos.xlsx?d=wb684924b7bd14bdca0d4bc95686dcbab
- The resolved browser route redirects to a SharePoint WOPI frame:
  https://www.bch.hn/estadisticos/EME/_layouts/15/WopiFrame.aspx?sourcedoc=%7BB684924E-7BD1-4BDC-A0D4-BC95686DCBAB%7D&file=Balanza%20de%20Pagos.xlsx&action=default
  Browser extraction returned only an app shell/inputs, no workbook bytes or sheet content. A separate container byte-download attempt against the public XLSX locator failed; a separate attempt against the WOPI frame also failed.
- BCH official SDMX link resolves to:
  https://www.bch.hn/estadisticos/EME/Documents/SDMX/BOP5USD_Honduras.xml?csf=1&e=GHj5pZ
  Retrieval returned HTTP 400 unsupported content-type text/xml through the current route. No XML bytes, data structure, observations or SHA-256 were captured.
- No further identical XLSX/WOPI/XML retrieval retry is authorized absent a genuinely new supported transfer route or capability.
- No raw national workbook/XML bytes, headers, byte count, retrieval receipt, sheets, table coordinates, Q2 values or SHA-256 are claimed.

## 4. Gate matrix
| Gate | Status |
|---|---|
| HND in immutable 63-country cohort | PASS |
| No prior dedicated HND Q2-2026 country report found | PASS |
| Official BCH quarterly BOP source discovery | PASS |
| Official quarterly BOP Excel locator discovery | PASS |
| Official SDDS BOP download locator discovery | PASS |
| XLSX workbook bytes/sheets/values | NOT_CAPTURED / BLOCKED |
| SDMX XML bytes/observations | NOT_CAPTURED / BLOCKED |
| Q2-2026 portfolio asset transaction | NOT_CAPTURED |
| Q2-2026 portfolio liability transaction | NOT_CAPTURED |
| Portfolio sign/unit/frequency/period/vintage bridge | NOT_ESTABLISHED |
| National-vs-IMF numeric comparison | NOT_DONE |
| HND national validation | PARTIAL / NOT PASS |
| Aggregate / production admission | NOT_AUTHORIZED |

## 5. Next exact action and route closure
- Keep HND PARTIAL / NOT PASS.
- Do not infer portfolio signs from the BCH reserves sign note.
- Do not use Q3-2025 chart values, IIP stocks, reserve assets, or other BOP net totals as Q2-2026 portfolio transaction legs.
- Reopen only if a distinct supported official Excel/API/SDMX route becomes available and captures original bytes plus metadata. If a supported interactive BCH export is later available, capture the original file, sheet names, period headers, asset/liability rows, source update/vintage, retrieval timestamp, byte count and SHA-256 before parsing.
- Reuse existing IMF raw panel rows only after a supported retrieval of the already archived raw CSVs; no IMF query or cohort rebuild.
- If no new official retrieval capability appears, close this exact route and advance to the next unvalidated cohort member after the mandatory duplicate-preflight.

## 6. Immutable constraints
₹0; official/free sources only. No synthetic data, fabricated timestamps, unsupported scale/sign/FX transformations, stocks-as-flows, annual/H1-to-quarter allocation, net-to-leg back-solving, IMF re-query or cohort rebuild. Preserve Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2. UNKNOWN is never PASS. Aggregate remains NOT_AUTHORIZED.
