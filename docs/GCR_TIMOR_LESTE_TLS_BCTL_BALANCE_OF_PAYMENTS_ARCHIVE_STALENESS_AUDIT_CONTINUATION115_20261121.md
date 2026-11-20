# Timor-Leste TLS — BCTL BOP archive staleness / vintage audit (Continuation 115)
Date: 2026-11-21 (Asia/Kolkata)
Decision: **The BCTL page's “Balance Of Payments” PDF item labelled Aug 2026 is a one-page historical table whose last observation is 2016 (quarterly I–IV 2016/p and annual 2016/P). It is not a 2026 BOP dataset. This closes the apparent Aug-2026-current-file lead as a false freshness signal. TLS Q2-2026 dual-leg national validation remains NOT_DONE / NOT PASS.**

## 1. Continuity preflight
Re-fetched current files:
- Master Ledger blob SHA d856df8391de33cfc973a6511d5cf7eab42d9b05
- GCR Priority Queue blob SHA f02863bd301215904b945f2ec3fe49f768554c80
- TLS C114 report blob SHA e698bf465389f925ea0440052775af124100148b
C114 was checked before the new action; completed PASS work skipped.

## 2. Exact BCTL archive PDF inspection
- Official page: https://www.bancocentral.tl/publication/quert_bop_iip_sts/
- Page labels the “Balance Of Payments” PDF “Aug 2026 | 272.8 KB”, download link 136.
- Exact link resolves to: https://www.bancocentral.tl/media/krep/None/430a8fb66f714649b6a7e46b53f026ad.pdf
- Opened PDF is one page. Title: “BALANÇA DE PAGAMENTO- TIMOR LESTE / BALANCE OF PAYMENTS: TIMOR-LESTE”; unit explicitly “In Thousand US Dollars”; source BCTL.
- Header chronology ends with I-2016/p, II-2016/p, III-2016/p, IV-2016/p, 2016/P. There are no 2025 or 2026 observations in this file.
- This demonstrates the page's Aug-2026 label is upload/metadata date, not the data vintage. Do not use this file for Q2-2026 or infer current coverage from page metadata.
- This file does not expose Q2-2026 portfolio asset/liability legs.

## 3. What remains valid from C114
- Official BCTL 2026 Mid-Year Economic Review reports H1 2026 portfolio investment -USD 524.9m and discusses it mainly as drawdown of external portfolio assets. This is an H1 aggregate component, not Q2 separate asset/liability legs.
- BCTL quarterly schedule page lists release dates through Q4 2025; no Q2-2026 dual-leg release was located via this archive route.
- BCTL defines BOP as period transactions and IIP as point-in-time stocks; IIP remains rejected as flow substitute.
- C114 report-level discrepancy retained: Executive Summary financial account -USD 705.9m versus detailed table/section -USD 702.9m; not silently reconciled.

## 4. Gate matrix
- BCTL archive page / official compiler identity: PASS.
- Aug-2026 file label captured: PASS.
- PDF content inspected; latest data period = 2016: PASS.
- File's actual 2026 data coverage: FAIL (none); do not treat upload date as data vintage.
- H1 2026 portfolio net component: CAPTURED, -USD 524.9m.
- Q2-2026 separate portfolio assets/liabilities: NOT_CAPTURED.
- Q2 period/sign/vintage for two legs: NOT_ESTABLISHED.
- Archived IMF comparison: NOT_DONE; no IMF query.
- TLS NOT_VALIDATED / NOT PASS; production admission NOT_AUTHORIZED.

## 5. Rejected interpretations
- “Aug 2026” PDF label is not evidence of 2026 observation coverage.
- Do not use 2016 series as Q2-2026 data.
- Do not infer separate legs from H1 net portfolio component.
- Do not subtract Q1 without same-vintage Q1 separate legs.
- Do not substitute IIP stocks or Petroleum Fund valuations for BOP flows.

## 6. Next exact action
1. Search BCTL official Economic Statistics / Balance of Payments data page and H1 2026 Mid-Year Review appendices for a current Q2 standalone table or H1 separate portfolio asset/liability legs.
2. If none exists, mark TLS national Q2 dual-leg source NOT_AVAILABLE and advance to next eligible cohort member.
3. No further use of the stale 2016 PDF; no repeat fetch of the same archive item.

## 7. Sources
- BCTL quarterly BOP/IIP archive and release schedule: https://www.bancocentral.tl/publication/quert_bop_iip_sts/
- Exact “Aug 2026” Balance of Payments PDF (one page, observations through 2016): https://www.bancocentral.tl/media/krep/None/430a8fb66f714649b6a7e46b53f026ad.pdf
- BCTL Mid-Year Economic Review 2026: https://www.bancocentral.tl/publication/krep/download/594/

## 8. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no annual-to-quarter proration or cross-vintage H1-Q1 subtraction, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
