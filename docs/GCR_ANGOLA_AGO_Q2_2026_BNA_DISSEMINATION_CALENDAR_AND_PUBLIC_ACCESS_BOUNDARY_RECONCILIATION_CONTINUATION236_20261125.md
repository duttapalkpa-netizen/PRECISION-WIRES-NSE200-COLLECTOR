# GCR — Angola (AGO) Q2-2026 BNA dissemination-calendar and public-access boundary reconciliation
Date: 2026-11-25 (Asia/Kolkata)
Continuation: 236
Decision: **One new official dissemination-planning source and a current IMF e-GDDS metadata record were reconciled against the existing C142 BNA source gate. The evidence confirms a quarterly BOP production/publication cadence and a public-web dissemination statement, but does not expose the Q2-2026 portfolio asset/liability values, an official data attachment, or a machine-readable export contract. AGO remains SOURCE_FOUND / PARTIAL / NOT PASS; national dual legs NOT_CAPTURED; aggregate NOT_AUTHORIZED.**

## 1. Continuity and duplicate-prevention preflight
- Re-read the current default-branch Master Continuity Ledger, GCR Master Priority Queue, 63-country Historical Task Registry and 63-country matrix before selection.
- Reopened C142 (AGO BNA external-statistics source-family gate) and checked current matrix row: AGO is a fixed-cohort member; both IMF Q2-2026 legs exist in the archived panel; national data capture, asset and liability gates remain NOT_CAPTURED; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Reused existing C142 source findings and archived IMF rows only. No IMF re-query, cohort rebuild, BNA SPA retry, national values extraction, or repeat of the known BNA portal route.
- Library Mother File 1–53/addenda through C57 and the latest relevant GCR source context were checked. Existing PASS tasks were excluded.

## 2. New official evidence — Angola 2026 National Statistical System Activity Plan
Official INE-hosted PDF:
https://ine.gov.ao/arquivos/geral/sen2026.pdf
Title: Plano de Actividades do Sistema Estatístico Nacional referente ao ano 2026 (PASEN 2026), dated December 2025.

Relevant source text:
- BNA statistical production activity B2119 is “Produção das Estatísticas da Balança de Pagamentos e da Posição de Investimento Internacional” using updated MBP6 methodology.
- Reference period: previous quarter (“Trim. n-1”); periodicity: quarterly; public availability target: “Trim. n+1”.
- The BNA dissemination calendar lists “Balança de Pagamentos e Posição do Investimento Internacional”, with reference period “Trimestre n-1”, periodicity “Bimensal”, and website placement “Depois de 60 dias”.
- The same calendar lists the public content family as “Balança de Pagamentos”, “Principais Indicadores Externos”, exports/imports and FDI by sector. It does not enumerate the detailed portfolio asset/liability table or name a downloadable workbook/API.

Interpretation boundary:
- This is an official production and dissemination schedule, not evidence that every detailed portfolio table is exposed in the public portal.
- The 4-Sep-2026 public announcement of the Q2-2026 External Statistics Information Note is consistent with the calendar's 60-day public-release target after 30-Jun-2026 (66 elapsed calendar days). This confirms release timing only, not availability of the underlying detailed data.

## 3. Metadata reconciliation — IMF e-GDDS
Current IMF e-GDDS metadata page:
https://dsbb.imf.org/e-gdds/dqaf-base/country/AGO/category/INR00
The current rendered metadata says external-sector quarterly data are posted on the BNA website and available to all users simultaneously. It also retains wording that the quarterly Statistical Bulletin (hard copy) and annual BOP/IIP report are distributed through a mailing list.

This is not necessarily a contradiction: the statements distinguish online quarterly external-sector data from the hard-copy bulletin and annual BOP/IIP report. It supersedes the overly broad interpretation in C142 that the quarterly BOP dissemination boundary is necessarily mailing-list-only. However, the page does not identify the exact Q2 portfolio dataset locator, table schema, attachment URL or revision vintage.

## 4. Public Q2 release boundary
Contemporaneous reports quoting the BNA Q2 External Statistics Information Note (4-Sep-2026) expose only high-level account totals in their text:
- Current-account surplus about USD 2.07–2.08bn.
- Capital-and-financial-account deficit USD 2,516.6m.
- Explanatory text refers to public external debt, positive FDI balance, trade credits/advances and deposits.
These are account-level aggregates and cannot be decomposed into portfolio investment assets and liabilities. No net-to-leg back-solving is permitted. The secondary BFA Q4-2026 report's external-indicator table likewise does not expose the required separate Q2 portfolio transaction legs.

## 5. Acceptance
| Gate | Status |
|---|---|
| C142/ledger/queue/registry/matrix duplicate-preflight | PASS |
| Official 2026 BNA quarterly BOP/IIP production schedule | PASS |
| Official 60-day / bimonthly public dissemination target | PASS |
| Current IMF e-GDDS public-web dissemination statement | PASS (metadata evidence only) |
| Q2-2026 release existence/date | PASS (release-announcement evidence) |
| Detailed Q2 portfolio asset and liability observations | NOT_CAPTURED |
| Official Q2 detailed raw attachment / response bytes / SHA-256 | NOT_CAPTURED |
| Public machine-readable API/export contract | NOT_IDENTIFIED |
| Portfolio taxonomy, national sign convention, units/scale bridge | NOT_ESTABLISHED |
| Same-vintage/revision bridge | NOT_ESTABLISHED |
| Separate-leg numerical reconciliation | NOT_DONE |
| AGO national validation | SOURCE_FOUND / PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 6. Exact next action
- Do not repeat the BNA JavaScript SPA route or infer a guessed API.
- Continue only if a supported browser/official BNA public download surface exposes the already-announced Q2-2026 External Statistics Information Note's detailed BOP table or a distinct Q2 workbook. Capture exact locator, response status/headers, raw bytes, retrieval UTC, terms, schema, units and SHA-256 before parsing.
- If no such supported route is available, keep AGO at SOURCE_FOUND and move to the next fixed-cohort member after a fresh exact route-history preflight. Do not contact BNA or any external party without explicit user approval.

## 7. Protected invariants
₹0; official/free sources only; no synthetic data, fabricated timestamps, net-to-leg back-solving, IIP stock substitution, unsupported sign/scale/FX conversion, IMF re-query or cohort rebuild. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 remain unchanged. No production integration or merge.
