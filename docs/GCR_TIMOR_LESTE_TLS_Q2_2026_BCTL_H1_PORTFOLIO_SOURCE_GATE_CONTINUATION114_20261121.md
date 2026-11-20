# Timor-Leste TLS Q2-2026 — BCTL official H1 portfolio source gate (Continuation 114)
Date: 2026-11-21 (Asia/Kolkata)
Decision: **Official BCTL material confirms H1 2026 portfolio investment net component of -USD 524.9m, interpreted by BCTL primarily as drawdown of external portfolio assets. This is H1 aggregate/net component, not separate Q2 portfolio asset and liability legs. BCTL's quarterly BOP publication schedule page lists releases only through Q4 2025. TLS Q2 dual-leg validation is NOT_DONE / NOT PASS.**

## 1. Continuity preflight
Re-fetched:
- Master Ledger blob SHA 163b5cfc1653ba7362db3d7394a134876bb7989b
- GCR Priority Queue blob SHA 24b73fabe206fa3e28bd15181c47d2ced9031cf4
- TJK Continuation 113 blob SHA f27988d966cc9dfb32a3b597ff5d5358f02584cd
GitHub search for existing TLS/Timor-Leste Q2-2026 dual-leg reports and source mapping returned no matches. Completed PASS work skipped.

## 2. Official BCTL H1 evidence
Source: BCTL 2026 Mid-Year Economic Review, official PDF:
https://www.bancocentral.tl/publication/krep/download/594/
- Cover identifies Banco Central de Timor-Leste, “Timor-Leste 2026 Mid-Year Economic Review” (PDF extracted lines 0–6).
- Summary table (PDF p.39; extracted lines 1337–1348) reports SEM1 2026 portfolio investment = -USD 524.9m; SEM1 2025 = -USD 235.6m; +123% change in magnitude.
- Detailed Financial Account discussion (PDF pp.39–40; extracted lines 1684–1701) says the negative portfolio investment balance primarily reflects reduction/drawdown of Timor-Leste external portfolio assets, including Petroleum Fund withdrawals. It explicitly cautions that the negative financial account components should not be interpreted uniformly as conventional capital outflows.
- BCTL table reports H1 aggregate financial account -USD 702.9m, direct investment -USD 113.5m, portfolio investment -USD 524.9m, other investment -USD 106.5m (latter stated in narrative). This is not a two-leg split.
- Internal consistency flag: Executive Summary line 90 says financial account net outflow USD 705.9m, while the detailed summary table and financial account section say USD 702.9m (lines 1346, 1686–1687). Do not silently reconcile; preserve as report-level discrepancy. It does not change portfolio component -524.9m.

## 3. Official quarterly BOP publication schedule gate
BCTL “Quarterly BOP and IIP Statistics” page:
https://www.bancocentral.tl/publication/quert_bop_iip_sts/
- Page lines 269–278 describes quarterly publication and lists Q1 2025 (30 May 2025), Q2 2025 (29 Aug 2025), Q3 2025 (1 Dec 2025), Q4 2025 (2 Mar 2026).
- Page's downloadable “Balance Of Payments” and “International Investment Positions” items are dated Aug 2026 (lines 331–340), but page does not expose a Q2 2026 dual-leg table in extracted content.
- The page describes BOP as period transaction statistics and IIP as point-in-time external asset/liability stocks (lines 292–299). Do not substitute IIP stocks for BOP flows.
- Schedule page only evidences releases through Q4 2025; it does not prove no later release exists elsewhere. Q2 2026 official standalone BOP dual-leg publication NOT_LOCATED through this route.

## 4. Gate matrix
- TLS cohort member: PASS (fixed cohort reused; no rebuild).
- Official BCTL compiler and quarterly BOP role: PASS.
- H1 2026 portfolio net component: CAPTURED, -USD 524.9m.
- H1 interpretation as mainly external portfolio asset drawdown: CAPTURED (BCTL narrative).
- Q2 standalone portfolio assets: NOT_CAPTURED.
- Q2 standalone portfolio liabilities: NOT_CAPTURED.
- H1 separate portfolio assets/liabilities: NOT_CAPTURED.
- Unit: USD million for H1 report table.
- Q2 period, dual legs, sign convention at two-leg level, source vintage/revision alignment: NOT_ESTABLISHED.
- Archived IMF row comparison: NOT_DONE; no IMF query issued.
- TLS NOT_VALIDATED / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 5. Rejections and restrictions
- Do not convert H1 -524.9m into Q2 using an assumed Q1 value or a different-vintage subtraction.
- Do not infer portfolio liabilities as zero or infer legs from the net component.
- Do not treat Petroleum Fund quarterly investment return/market valuation as BOP transaction legs.
- Do not substitute IIP position stocks for BOP transactions.
- Do not treat BCTL mid-year aggregate as a quarterly dual-leg report.
- No synthetic data, generic FX, sign flips, IMF re-query, cohort rebuild or production changes.

## 6. Next exact action
1. Search the BCTL official publication/download archive for a Q2-2026 standalone BOP release or H1 BOP table with separate portfolio asset and liability legs and a dated vintage.
2. If only H1 net portfolio component is published, do not derive Q2 absent same-vintage Q1 dual legs; mark TLS national dual-leg source unavailable and advance to next eligible country.
3. If separate legs are located, capture source bytes/URL/retrieval time/hash before parsing, verify sign/unit/period/vintage, then compare only with existing archived IMF panel rows.

## 7. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no annual-to-quarter proration or cross-vintage H1-Q1 subtraction, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
