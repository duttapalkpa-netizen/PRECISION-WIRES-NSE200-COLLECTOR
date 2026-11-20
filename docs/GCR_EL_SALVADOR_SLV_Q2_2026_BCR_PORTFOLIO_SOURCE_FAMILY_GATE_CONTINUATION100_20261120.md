# El Salvador SLV Q2-2026 — Banco Central de Reserva official-source family gate
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44, Part-5 / Continuation 100
Decision: **SLV fixed-cohort membership PASS; country-specific BCR source-family discovery PASS; official IMF staff BPM6 annual table contains portfolio assets/liabilities only as annual estimates, not Q2 observations; BCR June 2026 balance sheet includes foreign investment stocks, not BOP transactions; Q2-2026 national portfolio A_NFA_T/L_NIL_T NOT_CAPTURED; SLV PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight / PASS work excluded
- Re-fetched Master Continuity Ledger (blob SHA `185e55b1423c6b55ac24717a4bc6c893135acb4c`), GCR Master Priority Queue (blob SHA `03e99b7cc65ef685d3857ac45ebec25cb06493b3`), SLB Continuation 99 (blob SHA `7a696af5f0562941f59363d10bb6b58199319049`), exact-sample receipt (blob SHA `053fa26e9feaab26d5bb4c35911a09fc3f71d1bd`) and immutable 63-country cohort (blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`).
- SLV is the next fixed-cohort member after SLB and is present with both IMF Q2-2026 legs. Repository search found no dedicated SLV national Q2 portfolio source gate or reconciliation report.
- Existing exact-sample receipt covers 12 countries and does not include SLV. No exact SLV row was extracted from the large normalized panel (large-file GitHub fetch route returns empty content). No new IMF query or cohort rebuild.

## 2. Official national-source discovery and source-family screening
- Central Reserve Bank of El Salvador (BCR) is the national central bank/source named in IMF staff's country BOP table. IMF 2025 Article IV / EFF report presents a BPM6-formatted annual BOP table with portfolio investment net and separate “net acquisition of financial assets” and “net incurrence of liabilities” rows, sourced from BCR and IMF staff estimates.
- The annual IMF staff table is not a BCR Q2-2026 observation and its 2026 column is an annual projection/estimate. Do not use annual estimate to infer Q2.
- Official BCR financial statement “I.1 Banco Central de Reserva de El Salvador”, balance sheet at 31-Mar-2026 and 30-Jun-2026, in USD thousands, includes “Inversiones en el Exterior (Neto)” stock: 3,834,678.3 at Mar-2026 and 4,233,089.5 at Jun-2026. These are central-bank balance-sheet stocks (and a broad net foreign investment line), not economy-wide BOP portfolio transaction legs. Explicitly reject as A_NFA_T/L_NIL_T evidence; do not difference stocks or assign portfolio classification.
- The BCR statement's Jun/Mar stock difference is not a transaction flow because it can include valuation, FX, reclassification and other changes and is not a matched economy-wide portfolio asset/liability table.
- IMF staff annual BOP table is BPM6-format, but is still annual estimates and not a current Q2 national observation. No Q2 numeric values admitted.

## 3. Evidence boundary / rejection matrix
| Candidate | Published content | Decision |
|---|---|---|
| BCR Jun-2026 balance sheet | USD-thousand balance-sheet stocks; net foreign investments | REJECT for BOP transactions; wrong instrument/account/scope |
| BCR Mar-Jun stock difference | Change in a broad net stock | REJECT; stock change is not transaction flow |
| IMF 2025 Article IV/EFF BOP table | Annual historical and projected BPM6 portfolio net/assets/liabilities; BCR + IMF staff estimates | CONTEXT ONLY; wrong period and not national Q2 observation |
| Fixed IMF cohort | Both Q2 legs present for SLV | Candidate eligibility only; no national validation |
| SLV Q2-2026 national portfolio A_NFA_T/L_NIL_T | No admitted national values | NOT_CAPTURED |

## 4. Gate matrix
- SLV in fixed 63-country Q2 both-leg cohort: PASS.
- No prior dedicated SLV national report found: PASS.
- BCR identified as national source in IMF staff BOP source note: PASS.
- BPM6 annual BOP portfolio rows exist: PASS (annual staff estimates only).
- Official BCR June 2026 financial statement retrieved by web text: PASS (balance-sheet stock only).
- Q2 national portfolio asset transaction: NOT_CAPTURED.
- Q2 national portfolio liability transaction: NOT_CAPTURED.
- BCR source table exact Q2 BOP frequency/units/signs/vintage: NOT_ESTABLISHED.
- Exact IMF SLV rows from archived evidence: NOT_CAPTURED.
- Same-vintage dual-leg comparison: NOT_DONE.
- SLV national validation: PARTIAL / NOT PASS.
- Aggregate / production admission: NOT_AUTHORIZED.

## 5. Next exact action
1. Locate BCR official quarterly BOP release or time series for 2026-Q2 with separate portfolio net acquisition of financial assets and net incurrence of liabilities, not central-bank balance-sheet stocks.
2. Capture original official workbook/PDF/CSV bytes, publication vintage, release date, unit, signs, period and source metadata; compute SHA-256 before parsing.
3. Retrieve exact archived IMF SLV rows from the pre-existing IMF panel through a supported raw-file route; no new IMF query. The existing exact-sample receipt does not include SLV.
4. Only after national source and IMF row are both available, establish exact concept/sign/scale/vintage and compare the two legs separately.
5. If the BCR public route cannot provide the actual Q2 financial-account legs, close that route and advance to the next eligible cohort member after preflight.

## 6. Official evidence
- BCR official financial statement (June 2026; balance sheet in USD thousands): https://www.bcr.gob.sv/documental/Inicio/vista/2482985c1d8a6b2f69742a62bfa1e402.pdf
- IMF El Salvador 2025 EFF / Article IV report, Table 3a (BPM6 annual BOP; BCR and IMF staff estimates): https://www.elibrary.imf.org/view/journals/002/2025/058/article-A001-en.xml
- IMF 2025 Article IV consultation Table 3a (annual BPM6 BOP): https://www.elibrary.imf.org/abstract/journals/002/2025/067/article-A001-en.xml
- BCR official portal: https://www.bcr.gob.sv/

## 7. Protected invariants
No cohort rebuild, no IMF re-query, no stock-as-flow, no stock-difference-as-transaction, no annual-to-quarter proration, no net-to-leg inference, no FX inference, no synthetic data, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
