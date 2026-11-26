# GCR SRB Serbia Q2-2026 — NBS transaction-date FX / sign methodology and revision-vintage boundary
Continuation: 265
Date: 2026-11-26
Scope: official NBS methodology and post-Q2 release boundary check for C263 Serbia national dual-leg capture. Research-only.

## 1. Preflight and duplicate prevention
- Re-read current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, fixed 63-country Q2 matrix and Library Mother File 1–53.
- Re-read C263 NBS September 2026 Table 2.3 report. C263 national monthly values and arithmetic are reused; no repeated extraction.
- Skipped accepted monthly dual-leg sums and all prior PASS work. No IMF re-query, cohort rebuild, workflow dispatch, code change or production integration.
- C263 already occupies Continuation 263 for SRB; C264 occupies CHN. This report is correctly numbered C265.

## 2. New official methodology evidence
Official NBS Explanatory Notes:
https://www.nbs.rs/export/sites/NBS_site/documents-eng/statistika/mo/II-EOI-PB-e.pdf
- BPM6 BOP data are disseminated monthly and annually in EUR million and USD million.
- Transactions are recalculated from original currencies into reporting currency using the official middle exchange rates of NBS on the transaction date.
- Financial-account items use the assets-liabilities approach: increases in assets/liabilities are positive; decreases are negative.
- Net value is assets minus liabilities.
- Portfolio investments include equity securities below 10% ownership and debt securities; compilation sources include ITRS through banks and NBS and the Central Securities Depository and Clearing House.
- These statements establish the national methodology and sign semantics. They do not supply the transaction-level original-currency observations or the transaction-date rate-weighted conversion needed to independently convert the C263 aggregate EUR values into USD.

## 3. Current official data-route check
NBS official Balance of Payments page:
https://www.nbs.rs/en/drugi-nivo-navigacije/statistika/platni_bilans/index.html
- Current page lists September 2026 monthly BPM6 BOP and a separate detailed monthly BPM6 dataset; it also lists 2007–2025 history and explanatory notes.
- The official monthly XLS URL exposed by the page is:
  https://www.nbs.rs/export/sites/NBS_site/documents-eng/statistika/ino_ekonomski_odnosi/platni_bilans/balance_of_payments_26.xls
- The official detailed monthly XLS URL exposed by the page is:
  https://www.nbs.rs/export/sites/NBS_site/documents-eng/statistika/ino_ekonomski_odnosi/platni_bilans/balance_of_payments_detailed_26.xls
- Current retrieval surface returned HTTP 400 unsupported application/vnd.ms-excel for both links. This is a reader/content-type limitation; it is not evidence that the files are absent. No raw bytes, workbook sheets, USD Q2 A/L observations, byte count or SHA-256 were captured.
- NBS September 2026 BOP developments report (18-Nov-2026):
  https://www.nbs.rs/export/sites/NBS_site/documents-eng/statistika/ino_ekonomski_odnosi/platni_bilans/saopstenja/BOP_e_09_26.pdf
  It reports Jan–Sep 2026 cumulative portfolio net inflow EUR 4.4bn, driven by resident bond issuance abroad. This is cumulative/net context only; it does not expose a revised Q2 separate portfolio A/L pair and is not used to back-solve Q2.

## 4. Reused C263 Q2 evidence and conversion boundary
C263 Table 2.3 monthly national transaction legs (EURm), retained unchanged:
- Assets Apr/May/Jun: +149 / −25 / +124; Q2 sum +248.
- Liabilities Apr/May/Jun: −19 / +3,932 / +199; Q2 sum +4,112.
- Net Apr/May/Jun: +168 / −3,957 / −75; Q2 sum −3,864.
- Internal identity +248 − 4,112 = −3,864 remains PASS.
- Archived IMF Q2 raw values remain exactly as C263: asset OBS_VALUE 288993091.8400176 USD, SCALE=6; liability OBS_VALUE 4782903852.31975 USD, SCALE=6. No new query.
- Because NBS methodology specifies transaction-date FX, a single quarter-average rate applied to quarterly EUR aggregates would not reproduce the stated official conversion method. Without transaction-level original-currency amounts and transaction dates, do not calculate an estimated USD comparison from the EUR totals.
- The fact that NBS disseminates a USD series is a valid official route lead, but the XLS files were not readable in this retrieval channel; no USD Q2 pair is captured here.

## 5. Vintage / revision boundary
- C263 September Statistical Bulletin Table 2.3 states the table is preliminary and data were available until 17-Sep-2026.
- The NBS September 2026 BOP developments report is dated 18-Nov-2026 and covers January–September cumulative data. Its published portfolio statement is net and cumulative, not a Q2-specific separate A/L revision record.
- No Q2 observation-specific revision ID, revision timestamp, archived-vintage identifier or directly comparable later Q2 portfolio A/L pair was exposed in these sources.
- Therefore same-vintage identity remains PENDING / NOT_ESTABLISHED. Later issue date alone is not a vintage bridge.

## 6. Acceptance update
- NBS official transaction-date conversion methodology: PASS (methodology scope).
- NBS BPM6 asset/liability sign and net semantics: PASS (methodology scope).
- C263 quarterly arithmetic: PASS retained.
- Q2 EUR national legs: DATA_CAPTURED retained.
- USD Q2 separate A/L capture: NOT_CAPTURED.
- National-versus-IMF USD numeric comparison: REVIEW / NOT_PERFORMED.
- Same-vintage/revision bridge: PENDING / UNKNOWN.
- SRB remains DATA_CAPTURED / PARTIAL / NOT PASS; asset REVIEW; liability REVIEW; vintage PENDING; FULL_PASS=NO; aggregate NOT_AUTHORIZED.

## 7. Exact reopen condition
Reopen only if the official NBS monthly/detailed XLS is obtained through a supported byte-transfer route and exposes Q2-2026 USD portfolio assets/liabilities with workbook provenance, or if transaction-level data plus official transaction-date rates are available to reproduce conversion. Separately require observation-specific Q2 revision/vintage metadata before any vintage PASS. Do not use quarterly-average FX, net-only cumulative values, or inferred revisions.

## 8. Invariants
₹0 spend; official/free sources only; immutable 63-country cohort; no IMF re-query/cohort rebuild; no synthetic rows, unsupported FX conversion, fabricated hashes/timestamps, or annual/H1/net/IIP substitution; UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No workflow dispatch, merge or production integration.
