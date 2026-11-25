# GCR Continuation 249 — Poland (POL) Q2-2026 latest NBP instruction and publication-vintage boundary recheck
Date: 2026-11-26 (Asia/Kolkata)
Decision: NEW OFFICIAL NBP PUBLICATION-LIST ENTRY CONFIRMS REPORTING-INSTRUCTIONS VERSION 2.1 WAS PUBLISHED 13-JUL-2026; THE PORTAL EXTRACTION DOES NOT EXPOSE ITS ATTACHMENT URL/BYTES. RETRIEVABLE NBP VERSION 2.0 TEXT CONFIRMS THE SAME TRANSACTION-DATE FX RULE AND SPECIFIES FOUR-DECIMAL FX PRECISION. LATEST 13-NOV-2026 MONTHLY BOP RELEASE IS PRELIMINARY AND DOES NOT PROVIDE A MATCHED Q2 PORTFOLIO USD DUAL-LEG BRIDGE. POL REMAINS PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Mandatory continuity / duplicate-prevention preflight
- Re-fetched current default-branch Master Continuity Ledger (pre-task blob SHA-1 c22bd6a03e5793f5ca678039495dc4190e7a7b5d), GCR Master Priority Queue (4988b916076828845af64e0bfff56575a16fe3ef), Historical Task Registry (c4443a4240b52e23e0ec1f59f54d7d4773bd6c21), and fixed 63-country national validation matrix (e9aec00644e95f9ea9b0c7777a7a68e30a525cf2).
- Read the Library Mother File PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md (curated through pages 1–53; not a verbatim transcript), and re-read exact POL reports C163/C164/C165/C181.
- Reused prior accepted national values and transaction-date methodology; no repeat Q2 value extraction, no NBP PDF/XLSX byte-download retry, no IMF re-query, no cohort rebuild, no daily/quarterly FX conversion.
- Skipped C248 Colombia and all unrelated PASS work.

## 2. Fresh official NBP publication-list evidence
- Re-opened the current official NBP public reporting portal publication list: https://sprawozdawczosc.nbp.pl/pages/information/publication/common-publication-list.jsf
- The live listing includes explanatory notes version 2.1, publication date 13-Jul-2026. This is a newer official version than the English version 2.0 (June 2025) and v1.8 (July 2023) examined in prior POL work.
- The page extraction exposes the title/version/publication date but does not expose a usable direct attachment URL or downloadable bytes for the v2.1 item. Therefore no claim is made about the unseen v2.1 PDF's detailed text or whether it changes the relevant portfolio reporting rule.
- The portal also lists an XML reporting instruction dated 19-Jan-2026. The visible summary does not expose any matched Q2 portfolio USD aggregate or transaction-level currency/date records.

## 3. Retrievable official methodology cross-check (version 2.0)
- The official NBP v2.0 explanatory-notes PDF (June 2025) was opened and inspected: https://nbp.pl/wp-content/uploads/2025/06/objasnienia-do-rozporzadzenia-v2.0.pdf
- General notes 4–6 (PDF text lines 79–86) say data are reported in PLN, balances of foreign-currency assets/liabilities at period-end use NBP average rates on the last business day, while other data use the actual rate applied on the transaction date or the NBP average rate from the preceding day; the document explicitly requires rates with four decimal places for reporting conversions.
- The v2.0 table of contents retains the separate PW-RIN and PW-AIN questionnaires. This supports the already accepted form-specific transaction-date principle from C165, but does not provide the national Q2 transaction-level source currency/date weights.
- The v2.1 attachment itself was not retrievable through the inspected page surface. The v2.0 evidence must not be mislabeled as a direct inspection of v2.1.

## 4. Latest NBP release/vintage check
- Re-opened NBP's latest indexed monthly BOP publication dated 13-Nov-2026, covering September 2026: https://static.nbp.pl/dane/bilans-platniczy/bilansplatniczy.pdf
- Its front page says the September monthly BOP is estimated from monthly and quarterly reports, public statistical surveys and administrative sources, and explicitly says the presented version is preliminary and may change.
- It is a September monthly publication, not a matched Q2-2026 portfolio asset/liability USD dual-leg table. It supplies no evidence in the inspected text that the NBP Q2 release values (30-Sep-2026) and the archived IMF capture (19-Nov-2026) share the same observation-specific revision cut-off.
- Current/archived NBP Table A rates are exchange-rate quotations, not the missing transaction-level amounts/currency weights. No conversion from 24,144 mn PLN / 70,910 mn PLN was calculated.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| Current Ledger / Queue / Registry / 63-country matrix preflight | PASS |
| Library Mother File reviewed | PASS (curated 1–53; scope caveat retained) |
| Prior national Q2 portfolio assets | PASS (reused; 24,144 mn PLN) |
| Prior national Q2 portfolio liabilities | PASS (reused; 70,910 mn PLN) |
| NBP transaction-date FX principle | PASS (reused; C165) |
| New NBP v2.1 publication-list entry / 13-Jul-2026 date | PASS (listing metadata only) |
| NBP v2.1 attachment bytes / exact text | NOT_CAPTURED |
| Retrievable NBP v2.0 four-decimal reporting FX precision | PASS (methodology text only) |
| New matched USD Q2 dual-leg values | NOT_FOUND in bounded official public-source review |
| Transaction-level currency/date amounts and weights | NOT_CAPTURED |
| NBP Q2 raw PDF bytes / SHA-256 | NOT_CAPTURED |
| NBP 30-Sep vs IMF 19-Nov observation-specific same-vintage bridge | NOT_ESTABLISHED |
| Cross-currency numeric comparison | NOT_DONE |
| POL national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Decision / next action
- C249 closes this bounded current-publication and methodology-version recheck. It does not close POL national validation.
- Do not infer v2.1 content from its listing title, do not substitute v2.0 for an uninspected v2.1 attachment, and do not convert the PLN national totals using a quarterly average, quarter-end rate, or aggregate-implied ratio.
- Reopen POL only if the actual v2.1 attachment becomes retrievable and contains new relevant conversion/dissemination metadata, or a distinct official matched Q2 USD dual-leg publication / transaction-level source with dates, currencies, amounts and observation-vintage metadata is found.
- Keep POL national PLN legs as captured evidence; do not downgrade them. The unresolved currency/vintage gates continue to block numeric cross-currency acceptance and aggregate admission.
- Next cohort candidate remains MNE (Montenegro), whose open exact task is official CBCG Bulletin 9/2026 Tables 5.1–5.4 export annotation resolution; C241 already closed identical PDF-reader and byte-download attempts, so do not repeat them. Reopen only with a genuinely supported annotation/link extraction or distinct official CBCG table-export route.

## 7. Protected invariants
₹0; free official sources only; no external contact; no IMF re-query; no cohort rebuild; no fabricated values/timestamps/hashes; no unsupported FX conversion; no stock/flow substitution; UNKNOWN never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No workflow dispatch, merge or production integration.