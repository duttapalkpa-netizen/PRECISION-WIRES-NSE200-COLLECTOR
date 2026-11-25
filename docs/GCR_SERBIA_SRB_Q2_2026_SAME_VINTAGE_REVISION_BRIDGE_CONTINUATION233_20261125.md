# Serbia SRB Q2-2026 — same-vintage / revision bridge route boundary
Date: 2026-11-25 (Asia/Kolkata)
Continuation: 233 / Research verification 57 Part-1
Decision: **SRB remains PARTIAL / NOT PASS. The July-vintage Table 2.3 header and May asset/liability legs remain NOT_CAPTURED; July-to-September revision comparison remains NOT_DONE. No new public byte-preserving route was found in this bounded pass. Do not repeat the known PDF timeout or infer the month from the orphan 3,932 row.**

## 1. Mandatory continuity preflight
Re-fetched current repository records:
- Master Continuity / Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, blob SHA `ecdf2c2db0684033fa1896d1a6f94a981d25b5f0`.
- GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, blob SHA `526248c79e868a5a0ddcb05f002ea12226e771ec`.
- 63-country Historical Task Registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`, blob SHA `677df6b399132efe730c1ec453b3c3660414643b`.
- Re-fetched SRB Continuations 104, 109, 110 and 111. Continuation 112 was not located as a distinct SRB report in the current repository docs or Library semantic search; no claim that C112 was independently read.
- C232 ledger handoff selects SRB next and specifically says recheck C101/C103/C104/C109/C112 only for incomplete vintage/revision elements. Existing C101/C103/C104/C109 and C110/C111 history reviewed; completed monthly arithmetic, sign/FX method, IMF semantics and September-vintage values excluded from repeat work.

## 2. Existing PASS evidence retained
- NBS September-2026 Statistical Bulletin, Table 2.3, explicit month header: May-2026 assets -EUR25m, liabilities +EUR3,932m, net -EUR3,957m.
- Arithmetic identity: -25 - 3,932 = -3,957 EURm.
- NBS BPM6 sign and transaction-date FX method: PASS (C103).
- IMF A/L accounting-entry and portfolio category semantic bridge: PASS (C104).
- Archived IMF exact dual rows: CAPTURED (C102).
These are not a same-vintage comparison and are not repeated here.

## 3. New bounded route check
- Reopened the official NBS English Statistical Bulletin archive page. It exposes September 2026 as the current issue and archive controls as Select/Input/Show; the extracted page does not expose a July-specific PDF href or a direct downloadable archive result.
- Followed the page's “Data series in XLS format” link; it leads to the general Statistics landing page, not a dated July Bulletin workbook.
- Official archive calendar confirms July 2026 issue identity/date (3-Sep-2026 English listing; Serbian archive previously records 31-Aug-2026). This is publication chronology only, not the July Table 2.3 column header.
- The already-known July PDF URL `https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf` was not retried; prior C109–C111 records exhaust this direct route as timeout.
- No supported browser DOM execution / archive-form Show / raw binary download capability is available in this execution. No guessed form parameters, POST, stale ViewState, authenticated web-service request, scraping, reverse engineering or NBS contact was attempted.
- NBS official September PDF remains accessible and indexed; it supports only the September vintage values already accepted in C109.

## 4. Gate matrix
| Gate | Status |
|---|---|
| September-vintage May month header and separate legs | PASS |
| September-vintage arithmetic | PASS |
| NBS sign / transaction-date FX method | PASS |
| IMF A/L portfolio semantics and exact rows | PASS / CAPTURED |
| July issue identity/publication chronology | PASS |
| July Table 2.3 complete header | NOT_CAPTURED |
| July-vintage May assets/liabilities/net | NOT_VERIFIED |
| July-to-September separate-leg revision comparison | NOT_DONE |
| NBS original July PDF raw bytes / SHA-256 | NOT_CAPTURED |
| National scope/timing/valuation equivalence | NOT_ESTABLISHED |
| USD/EUR transaction-weighted bridge | NOT_ESTABLISHED |
| SRB overall | PARTIAL / NOT PASS |
| Aggregate / production admission | NOT_AUTHORIZED |

## 5. Next exact action / stop condition
1. Resume only when a supported browser with DOM interaction and download support is available, or a genuinely new official NBS route exposes the July 2026 issue's original PDF/workbook bytes.
2. Capture original bytes, URL, HTTP status/headers, retrieval timestamp, byte count and SHA-256 before parsing.
3. Inspect July Table 2.3 full header; only if the 3,932 row is explicitly May, compare July-vintage May assets, liabilities and net separately against September's -25 / +3,932 / -3,957 EURm.
4. Until then, retain July-vintage and revision gates OPEN/BLOCKED. No inference from the orphan 3,932 row; no net-to-leg inference; no FX conversion.

## 6. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no paid source, no external contact, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. UNKNOWN is never PASS. Research spend ₹0.
