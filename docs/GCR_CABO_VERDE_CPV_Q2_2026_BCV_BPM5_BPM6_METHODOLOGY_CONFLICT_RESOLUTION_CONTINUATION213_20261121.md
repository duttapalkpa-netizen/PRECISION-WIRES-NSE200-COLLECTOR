# Cabo Verde (CPV) Q2-2026 — BCV BPM5/BPM6 methodology conflict resolution
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 213
Decision: OFFICIAL BCV BPM6 EXTERNAL-SECTOR METHODOLOGY CONFIRMED AS THE DOCUMENTED FRAMEWORK; IMF e-GDDS BPM5 ENTRY IS LEGACY/CONFLICTING METADATA, NOT CURRENT PROOF. CPV WORKBOOK BYTES/DUAL LEGS/VINTAGE REMAIN NOT_CAPTURED; NATIONAL STATUS PARTIAL/BLOCKED; AGGREGATE NOT_AUTHORIZED.

## 1. Preflight and duplicate prevention
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, 63-country matrix and the controlling CPV C153 report before selection.
- Excluded repeated BCV XLS retrieval: C153 documents the exact official workbook locator and failed retrieval paths; no identical download attempt was repeated.
- Selected the unresolved methodology conflict only. No IMF re-query, cohort rebuild or panel change.

## 2. Official BCV methodology evidence
- BCV official document: "Nota Metodológica BPM6 — Estatísticas Sector Externo", dated June 2016:
  https://www.bcv.cv/pt/Estatisticas/Quadros%20Estatisticos/Sector%20Externo/metadados/Documents/Nota%20Metodol%C3%B3gica%206MBP_Estat%C3%ADsticas%20do%20Setor%20Externo.pdf
- The document explicitly labels itself adoption of the Sixth Edition (BPM6), states that external-sector statistics had previously used BPM5 since January 1999, and describes the transition to BPM6 (document pp.1–2).
- It defines BOP as transaction flows and IIP as period-end stocks (p.2); distinguishes portfolio investment as a functional category and identifies equity/debt securities (p.4).
- The methodology states BPM6 positive signs represent increases in assets and liabilities and negative signs represent reductions (p.6). It also states BCV reports gross financial-account item transactions separately, including transactions that increase and decrease assets/liabilities (p.6). This is useful sign/structure guidance, not proof that the Q2 workbook contains the required separate portfolio rows.
- BCV's 12-Nov-2026 official notice describes a 2026 IMF-supported methodology update for monetary and financial statistics, specifically monetary balance-sheet/monetary-survey analytical tables. It does not state that BOP/IIP compilation reverted to BPM5 or superseded the external-sector BPM6 note:
  https://www.bcv.cv/pt/O%20Banco/Sala%20de%20Imprensa/Arquivo/Paginas/Comunicado-12-novembro-2026.aspx
- Therefore the BPM5 label on the IMF e-GDDS CPV metadata page is treated as a legacy or stale metadata conflict. BPM6 is the best-supported documented BCV external-sector framework. This is not a claim that every Q2-2026 workbook cell has been verified as BPM6.

## 3. What this resolves / does not resolve
| Gate | Result |
|---|---|
| Official BCV external-sector BPM6 adoption note | PASS |
| BPM6 transaction-flow vs IIP-stock distinction | PASS |
| BPM6 portfolio category definition | PASS |
| BPM6 financial-account sign convention | PASS |
| BCV gross reporting statement for financial-account items | PASS |
| IMF e-GDDS BPM5 metadata conflict | Explained as likely legacy; current dataset-level vintage still not independently stamped |
| Q2-2026 BCV workbook bytes/sheet/cell values | NOT_CAPTURED |
| Separate Q2 portfolio asset/liability observations | NOT_VERIFIED |
| National unit and row-level sign mapping | NOT_ESTABLISHED |
| Q2 workbook revision vintage | NOT_ESTABLISHED |
| IMF-national numeric comparison | NOT_DONE |
| CPV national validation | PARTIAL / BLOCKED; NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 4. Matrix treatment
- Update only CPV descriptive note to record that BCV's official external-sector BPM6 note is verified and the IMF e-GDDS BPM5 label is treated as likely legacy metadata.
- Keep CPV stage SOURCE_FOUND, national source present YES, asset/liability NOT_CAPTURED, vintage UNKNOWN, FULL_PASS NO, aggregate NOT_AUTHORIZED.
- Do not infer dual-leg capture from the methodological gross-reporting statement.

## 5. Next action
Reopen only when a genuinely different supported official BCV XLS/API/browser-byte route yields the Q2 workbook, or a new dated BCV external-sector methodology/revision notice supersedes the June-2016 BPM6 note. Then inspect exact Q2 portfolio asset/liability rows and raw bytes/hash before any numeric comparison. Do not repeat the identical failed XLS route.

## 6. Protected invariants
₹0; official/free sources only; no IMF re-query/cohort rebuild, synthetic data, H1/annual interpolation, net-to-leg back-solving, IIP-stock-as-flow, guessed signs/units, aggregate admission or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
