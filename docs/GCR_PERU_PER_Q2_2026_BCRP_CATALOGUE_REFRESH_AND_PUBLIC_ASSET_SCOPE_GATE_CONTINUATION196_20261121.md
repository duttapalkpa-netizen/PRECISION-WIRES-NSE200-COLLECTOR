# Peru (PER) Q2-2026 — BCRP current-catalogue refresh and public-sector portfolio-asset scope gate
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 196
Decision: **Current official BCRP quarterly catalogue refresh PASS; full-economy national portfolio dual-leg scope remains NOT_ESTABLISHED; no Q2 numeric observations or raw bytes admitted; PER remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Mandatory continuity and duplicate-prevention preflight
- Re-fetched the current Master Continuity & Acceptance Ledger, GCR Master Priority Queue, Historical Task Registry and the complete PER source-boundary reports before selection.
- Reused the fixed 63-country Q2-2026 cohort and existing IMF raw archive; no cohort rebuild, IMF re-query, or repeat of the previously inaccessible BCRP API request.
- Prior PASS: official BCRPData catalogue/API documentation discovery and identification of private-sector portfolio series PN39278BQ (assets) and PN39285BQ (liabilities).
- Prior open gate: whether the private-sector asset series covers the full-economy national portfolio asset leg, and whether an official public-sector portfolio asset series exists.

## 2. Fresh official catalogue evidence
- Official BCRP quarterly series catalogue: https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales
- Catalogue page inspected 21-Nov-2026; its relevant rows show last update **20-Nov-2026** and latest quarter **T3-2026**.
- Private-sector financial-account group (USD millions):
  - PN39278BQ — Assets - Portfolio Investment; T1-2012 through T3-2026; updated 20-Nov-2026.
  - PN39285BQ — Liabilities - Portfolio Investment; T1-2012 through T3-2026; updated 20-Nov-2026.
- Public-sector financial-account group (USD millions; 25 series):
  - PN39402FQ — Assets (aggregate public-sector assets), T1-2012 through T3-2026.
  - PN39403FQ — Liabilities (aggregate public-sector liabilities), T1-2012 through T3-2026.
  - PN39404FQ — Liabilities - Portfolio Investment, T1-2012 through T3-2026.
  - The complete displayed 25-series public-sector group contains no row labelled public-sector portfolio-investment assets. It includes aggregate public-sector assets, but that is not a portfolio-specific asset series and cannot be substituted.
- The current catalogue therefore provides stronger scope evidence than the earlier 20-Aug snapshot: the listed private-sector portfolio legs and public-sector portfolio liability remain distinct, while a matching public-sector portfolio asset series is not listed in this catalogue group.
- Absence from this displayed catalogue is a bounded catalogue finding, not proof that no other official attachment or dataset exists.

## 3. API and data-access boundary
- BCRP's official API guide documents GET/POST and HTML/CSV/JSON/XML/XLS output formats: https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf
- The prior exact BCRP API retrieval attempts are already recorded as inaccessible in the current retrieval bridge. This continuation did not retry the same API route/surface.
- No raw Q2-2026 API payload, values, response headers, receipt timestamp, file bytes or SHA-256 were captured in this continuation.
- The catalogue's T3-2026 endpoint confirms Q2 is within the listed period range; it does not itself establish national portfolio scope or provide the Q2 observations in this report.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Current official quarterly catalogue reopened | PASS |
| Catalogue freshness / T3-2026 endpoint / 20-Nov-2026 update | PASS |
| Private-sector portfolio asset/liability series identities | PASS (reconfirmed) |
| Public-sector portfolio liability series identity PN39404FQ | PASS |
| Public-sector portfolio-specific asset series in displayed 25-series group | NOT_LISTED |
| Full-economy national portfolio asset scope | NOT_ESTABLISHED |
| Q2 separate national portfolio asset/liability values | NOT_CAPTURED |
| Raw API/export bytes, response receipt and SHA-256 | NOT_CAPTURED |
| Sign/scale and observation vintage bridge | NOT_ESTABLISHED |
| PER national validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Decision and next action
- Do not combine private-sector portfolio assets with aggregate public-sector assets; aggregate assets are not portfolio-specific.
- Do not treat the public-sector portfolio liability series as evidence of a matching public-sector asset series.
- Do not use net financial-account totals, IIP stocks, or IMF-only observations as national dual-leg validation.
- Keep PER PARTIAL / NOT PASS. Reopen only if a distinct official BCRP source provides a public-sector portfolio asset transaction series or a documented official scope statement proves PN39278BQ is the full-economy asset leg.
- Next queue candidate must be selected only after full report-history and route-fingerprint preflight; do not repeat inaccessible API requests.
- ₹0; no synthetic data; no IMF GET/cohort rebuild; no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
