# Timor-Leste TLS — BCTL live BOP dashboard and Excel export route audit (Continuation 116)
Date: 2026-11-21 (Asia/Kolkata)
Decision: **A new official BCTL live Balance of Payments route has been located, beyond the stale 2016 PDF archive: the BOP page embeds a Power BI report (“BoP_V1”) and exposes an “Export Excel” link. The Excel endpoint is a real XLSX resource, but automated retrieval through current web/container routes failed (web unsupported MIME; direct download failed). Therefore data contents, latest period and portfolio dual legs remain NOT_CAPTURED. This is a new source route, not a validation PASS. TLS remains NOT_VALIDATED / NOT PASS.**

## 1. Continuity preflight
Re-fetched:
- Master Ledger blob SHA 5b90932ad15477ba22f74d44b705095f9f29cce6
- GCR Priority Queue blob SHA 86f1ca7b64a70d77ed94f342349faac7fef1d8d9
- TLS C115 report blob SHA 9f243d8b564204e21002b9fe77dec301029f9c0f
Completed PASS work skipped; did not retry stale 2016 PDF.

## 2. Newly discovered official live BOP route
- BCTL Economic Statistics page has an explicit External Sector > Balance of Payments navigation entry.
- Exact BOP page: https://www.bancocentral.tl/stats/balance_pay/
- Page renders “BoP_V1” Power BI embed (link 126) and explicitly says “Download the full Balance of Payments report.”
- Page exposes “+ Export Excel” (link 127).
- Exact Excel endpoint resolved from that link:
  https://www.bancocentral.tl/stats/bopdoc/download/c81e728d9d4c2f636f067f89cc14862c/
- Web fetch rejected the response because MIME type is application/vnd.openxmlformats-officedocument.spreadsheetml.sheet (unsupported by web open route). Direct container download of this exact URL also failed. No XLSX bytes, workbook sheets, observation periods, or SHA-256 captured.
- Power BI embed resolves to:
  https://app.powerbi.com/view?r=eyJrIjoiMDU3Nzc3M2YtNDlmYy00ODEyLTgyZTAtNDNlY2ZlNGQ3NTRhIiwidCI6ImVhOGNhZTEyLWE5MjMtNDEyYi1hY2VlLWU0NmJhOTI1ZmY0ZCIsImMiOjEwfQ%3D%3D
  The report page is a live visualization route; extracted HTML provides no data rows.

## 3. Evidence interpretation
- This is a stronger and distinct official source route than the historical archive PDF. It may contain current BOP series, but its data contents and vintage are not yet inspected.
- BCTL metadata says BOP summarizes transactions over a specific period and identifies BCTL as official compiler. IIP remains a separate point-in-time stock dataset.
- The Mid-Year Economic Review remains H1 aggregate only: portfolio investment -USD 524.9m, mainly explained as drawdown of external portfolio assets. It does not establish Q2 dual legs.
- The old “Balance Of Payments | Aug 2026” PDF remains stale through 2016 and is not reused.

## 4. Gate matrix
- Official BCTL BOP live data page locator: PASS.
- Power BI embedded report locator: PASS.
- Excel export control and exact endpoint: PASS.
- XLSX response recognized as Excel MIME: PASS (endpoint response type only).
- XLSX bytes/workbook schema/observation vintage: NOT_CAPTURED.
- Q2-2026 portfolio assets and liabilities: NOT_CAPTURED.
- Unit/sign/period/vintage: NOT_ESTABLISHED.
- Archived IMF comparison: NOT_DONE; no IMF query.
- TLS NOT_VALIDATED / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 5. Next exact action
1. Use an actual browser/Computer Use session on the official BCTL BOP page to click “+ Export Excel” and save the workbook; or interact with the Power BI report's Export data control if enabled.
2. Capture raw workbook bytes, retrieval timestamp, byte count, SHA-256, sheet names and all period headers before parsing.
3. Locate portfolio investment assets and liabilities as separate BOP transaction legs; verify Q2 standalone vs cumulative, USD unit, signs and release/revision vintage.
4. Compare to existing archived IMF panel rows only after alignment; no IMF re-query.
5. If export is blocked or workbook has no dual legs, record exact blocker and advance next cohort member.

## 6. Sources
- BCTL Economic Statistics: https://www.bancocentral.tl/stats/economic/
- BCTL live Balance of Payments page: https://www.bancocentral.tl/stats/balance_pay/
- Exact BCTL Excel export endpoint: https://www.bancocentral.tl/stats/bopdoc/download/c81e728d9d4c2f636f067f89cc14862c/
- BCTL Power BI embed: https://app.powerbi.com/view?r=eyJrIjoiMDU3Nzc3M2YtNDlmYy00ODEyLTgyZTAtNDNlY2ZlNGQ3NTRhIiwidCI6ImVhOGNhZTEyLWE5MjMtNDEyYi1hY2VlLWU0NmJhOTI1ZmY0ZCIsImMiOjEwfQ%3D%3D
- BCTL 2026 Mid-Year Economic Review: https://www.bancocentral.tl/publication/krep/download/594/

## 7. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no annual-to-quarter proration or cross-vintage H1-Q1 subtraction, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
