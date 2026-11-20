# Serbia SRB Q2-2026 — IMF BPM6 code bridge and NBS later-vintage limit
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44 / Continuation 104
Decision: **Official IMF BPM6 coding/manual evidence now supports the A_NFA_T / L_NIL_T accounting-entry semantics and portfolio functional category; this closes the standards-level concept/sign bridge (PASS, standards mapping only). NBS September 2026 later-vintage release is captured as PDF text and confirms a Jan–Sep portfolio net inflow context, but it does not publish the needed May monthly portfolio asset/liability revision values in the inspected text; revision check remains NOT_DONE. NBS XLS workbooks remain binary-content inaccessible. Cross-currency quantitative comparison NOT_DONE; SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight / PASS work excluded
- Re-fetched Master Ledger (blob SHA e0a7e5641a17363311ce4372f75fba5369be6f73), GCR Priority Queue (blob SHA 0888f0895bfd817cbda671d4e9831ed09d5af032), SRB Continuation 103 (blob SHA a6a19a1521d8c405c25cd1e8129912fdc2c80d61), Continuation 102 (blob SHA 874f1908814137b67c0d4032752b73dd3a29e207), and Continuation 101 (blob SHA ca0eb8844ab9d14a378f4278506f363fdf776c65).
- Excluded completed work: NBS-side BPM6 sign and transaction-date FX method, NBS Q2 monthly aggregation, exact IMF SRB rows. No new IMF query or cohort rebuild.

## 2. IMF official coding bridge
Official IMF BPM6 Compilation Guide, Appendix 7, “Balance of Payments Coding System”:
- A7.7 (PDF pp. 446–447) explicitly defines accounting-entry codes: N=net, A=assets, L=liabilities.
- Table A7.2 (PDF p. 447) identifies aggregate 3B as Portfolio investment within the financial account.
- A7.4–A7.7 describe the code structure: financial-account aggregate, BOP item, accounting entry, resident sector, maturity.
Official IMF BPM6 Manual:
- Paragraph 6.54 defines portfolio investment as cross-border transactions/positions involving debt or equity securities, excluding direct investment and reserve assets.
- Paragraph 8.27 ties financial-account portfolio investment to the Chapter 6 definition.
- BPM6 financial-account principles record net acquisition of financial assets and net incurrence of liabilities separately; positive values denote increases and negative values decreases (also confirmed by Appendix 7 A7.31 and NBS own explanatory notes).
Application to archived panel:
- Archived SRB rows are keyed A_NFA_T and L_NIL_T, functional category P_F, frequency Q, period 2026-Q2.
- The A/L accounting-entry distinction and portfolio functional-category concept align with NBS Table 2.3 separate “Portfolio investment — Assets” and “Portfolio investment — Liabilities” rows at the BPM6 standards level.
- This is a standards-level semantic mapping, not proof of identical national compilation scope, coverage, timing, valuation or vintage. Those require source-level metadata and remain open.

## 3. NBS September 2026 later-vintage evidence inspected
- Official NBS BOP page lists “Balance of payments - monthly, September 2026 (BPM6)” and “details (BPM6)”; page also lists “Balance of payments developments in September 2026”, dated 18-Nov-2026.
- The September developments PDF was successfully inspected as official PDF text: `BOP_e_09_26.pdf`, 7 pages, covering January–September 2026.
- It reports a net portfolio investment inflow of EUR 4.4bn in the first nine months of 2026, driven by bond issuances by residents in international markets (PDF page 6 / extracted lines 428–430).
- This cumulative net figure is contextual only. It does not expose the May-2026 monthly separate asset/liability observations or a revision comparison; no back-calculation or net-to-leg inference was performed.
- The official monthly and detailed XLS locators were opened via the NBS page, but both return HTTP/tool-side 400 unsupported content type (application/vnd.ms-excel). Workbook bytes, sheet names, May values, byte counts and hashes remain NOT_CAPTURED.
- The PDF text source confirms release date 18-Nov-2026 from the official page; original PDF raw bytes and SHA-256 were not captured.

## 4. Updated gate matrix
- NBS BPM6 sign convention and transaction-date FX method: PASS (Continuation 103).
- IMF A/L accounting-entry semantics and 3B portfolio functional category: PASS (official BPM6 standards-level mapping).
- National exact row scope equivalence / coverage / valuation / recording-time equivalence: NOT_ESTABLISHED.
- NBS September 2026 official release identified and inspected: PASS.
- May 2026 later-vintage monthly asset/liability observations: NOT_CAPTURED; revision check NOT_DONE.
- NBS XLS raw bytes/sheets/values/hash: NOT_CAPTURED (unsupported content type).
- NBS PDF raw bytes/hash: NOT_CAPTURED.
- Exact IMF SRB Q2-2026 rows: CAPTURED in Continuation 102.
- USD/EUR exact transaction-weighted bridge: NOT_ESTABLISHED.
- Same-vintage independent dual-leg comparison: NOT_DONE.
- SRB: PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 5. Next exact actions
1. Obtain NBS September 2026 XLS/detailed XLS via an approved byte-preserving workbook route, or a separately published official CSV/HTML series; preserve bytes, sheets, timestamps and SHA-256.
2. Compare May-2026 monthly portfolio asset/liability values against the September vintage; preserve any revisions as a separate vintage.
3. Obtain transaction-level FX weights or an official NBS USD presentation with metadata; do not apply a generic month/quarter rate to quarterly EUR aggregates.
4. Complete national scope/timing/valuation mapping; only then perform separate asset and liability comparison. No net-to-leg inference.

## 6. Official sources
- IMF BPM6 Compilation Guide, Appendix 7: https://www.imf.org/external/pubs/ft/bop/2014/pdf/BPM6_A7F.pdf
- IMF BPM6 Manual: https://data.imf.org/-/media/iData/External-Storage/Documents/73FBCD5B6CDE4D289C60B9B0CAA40622/en/2-bpm6.pdf
- NBS BOP page: https://www.nbs.rs/en/drugi-nivo-navigacije/statistika/platni_bilans/index.html
- NBS September 2026 developments (18-Nov-2026): https://www.nbs.rs/export/sites/NBS_site/documents-eng/statistika/ino_ekonomski_odnosi/platni_bilans/saopstenja/BOP_e_09_26.pdf

## 7. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
