# GCR Cabo Verde (CPV) Q2-2026 — updated BCV BOP statistical-table locator and XLS access boundary
Date: 2026-11-26 (Asia/Kolkata)
Continuation: 256
Decision: NEW OFFICIAL BCV BOP STATISTICAL PAGE LOCATOR DISCOVERED; Q2-2026 XLS ATTACHMENT TARGET/RAW BYTES NOT RECOVERED; NO NATIONAL DUAL-LEG PROMOTION.

## 1. Mandatory preflight and selection
- Re-fetched the current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and fixed 63-country matrix from the repository default branch; recorded current blob SHAs in the continuation write/read-back record.
- Re-read the Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md` and the controlling CPV C213 methodology report. C214's matrix evidence-reference correction was checked in the registry history.
- PASS work skipped: IMF cohort/panel/receipt capture, CPV BPM6 methodology, BOP-vs-IIP scope and sign-convention work. No IMF re-query, cohort rebuild, repeat of the old failed XLS/XLSX download, or production workflow run.
- CPV was selected because its fixed-cohort matrix row remains SOURCE_FOUND with national Q2 portfolio A/L NOT_CAPTURED, and the official central-bank page now indexes a BOP statistical document covering Q1-2012 through Q2-2026.

## 2. New official source locator
- Banco de Cabo Verde official statistical page: https://www.bcv.cv/pt/Estatisticas/Quadros%20Estatisticos/Sector%20Externo/quadrosestatisticos/Paginas/BalancadePagamentos.aspx
- The page is indexed as updated 17-Nov-2026 and lists “Balança de Pagamentos (Estatísticas do 1º trimestre de 2012 a 2º trimestre de 2026)” with an XLS document affordance.
- This is a new official page-level locator for a current BOP statistical table. The search result does not expose the XLS attachment href, filename, MIME/size, sheet names or response bytes. Direct page opening through the available retrieval surface returned cache miss/timeout; no attachment click target could be resolved.
- The page also lists a separate IIP statistical table through Q2-2026. It is a stock dataset and is not admitted as a substitute for BOP transaction flows.

## 3. Prior-route and semantic boundary
- C213 remains the controlling official methodology record: BCV's June-2016 external-sector methodology explicitly adopts BPM6, distinguishes BOP transaction flows from IIP stocks, defines portfolio investment and documents BPM6 sign convention/gross financial-account reporting.
- The new page-level locator is distinct from the earlier failed workbook retrieval fingerprint recorded in C153/C213, but the underlying XLS attachment identity cannot yet be compared because its href/filename are not exposed. Therefore this continuation records discovery only, not a proven new byte-transfer capability.
- No claim is made that the XLS contains separate Q2 portfolio asset and liability observations. A generic BOP table, financial-account aggregate, net portfolio balance, IIP stock, direct investment or other investment line cannot substitute for both required portfolio legs.

## 4. Acceptance result
| Gate | Status |
|---|---|
| Fixed 63-country CPV cohort membership | PASS (reused) |
| Official BCV BPM6 external-sector methodology | PASS (reused C213) |
| Official BOP statistical page, Q1-2012 to Q2-2026 locator | DISCOVERED |
| Exact XLS attachment URL / filename / MIME / size | NOT_CAPTURED |
| Raw XLS bytes and SHA-256 | NOT_CAPTURED |
| Workbook sheets, headers, units and vintage | NOT_CAPTURED |
| Q2-2026 separate portfolio assets and liabilities | NOT_VERIFIED |
| National sign/unit mapping and numeric comparison | NOT_DONE |
| CPV national validation | SOURCE_FOUND / PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Exact next action
- Resume only with a supported browser or XLS-capable byte-transfer route that resolves the official page's actual XLS href and captures the raw response bytes with URL, retrieval timestamp, HTTP metadata, MIME, size and SHA-256.
- Inspect workbook sheet names, period labels, portfolio A/L rows, units, sign convention and revision/vintage notes. Compare separately to the already archived IMF exact-key rows only after the national source semantics are established.
- If the actual XLS href resolves to the same already failed C153 route, close it as duplicate and do not retry. If a distinct supported route yields bytes, continue row-level QA; otherwise keep CPV gates unchanged and advance to the next eligible fixed-cohort country after full preflight.

## 6. Protected invariants
₹0; official/free sources only; no IMF re-query/cohort rebuild; no synthetic data, guessed sign/unit, net-to-leg back-solving, IIP-stock-as-flow, H1/annual interpolation, fabricated timestamps or unsupported proxy promotion. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No workflow dispatch, merge or production integration.
