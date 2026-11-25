# GCR Continuation 253 — Chile (CHL) Q2-2026 portfolio net revision / vintage boundary recheck
Date: 2026-11-26 (Asia/Kolkata)

## Decision
A new official Banco Central de Chile Q3-2026 BOP/IIP publication dated 18-Nov-2026 confirms that Q1 and Q2 2026 BOP figures were revised. Its Q2 portfolio-investment net balance is now USD +154m in the summary table, versus USD +299m in the earlier Q2 publication captured in C160: a published net revision of -USD145m. However, the revision table does not disaggregate Q2 portfolio investment into revised asset and liability transaction legs. Therefore the prior BDE monthly legs cannot be treated as the current Q3-release vintage; the exact revised dual-leg pair and its same-vintage comparison remain NOT_CAPTURED / NOT_ESTABLISHED. CHL remains DATA_CAPTURED / PARTIAL / NOT PASS; vintage PENDING; aggregate NOT_AUTHORIZED.

## 1. Mandatory continuity and duplicate-prevention preflight
- Re-fetched the current default-branch Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and fixed 63-country national validation matrix.
- Re-read the Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md`.
- Reopened CHL C160 (official BDE monthly dual-leg observation audit) and C161 (official BDE API/export access gate) before selection.
- Reused the C160 observed Q2 monthly sums and archived IMF raw-row references; did not repeat BDE monthly extraction, credential-gated API requests, basket export interaction, IMF query, cohort rebuild, or any prior PASS arithmetic.
- Selected only the new official Q3-release revision trigger that became available after the earlier CHL checks.

## 2. New official Q3-2026 release and publication date
- Official BCCh publication: https://www.bcentral.cl/documents/33528/8798046/Balanza%2Bde%2BPagos%2BTercer%2BTrimestre%2B2026.pdf/cc1162a1-cca3-bc75-b697-3df5b826cb04?t=1794947628782
- The Q3 report's review section states that Q1 and Q2 2026 BOP figures were revised (PDF text lines 989–992).
- The report says financial-account revisions reflect updated assets/liabilities information from the Compendio de Normas de Cambios Internacionales (CNCI) and additional financial-statement information (lines 990–992).
- The report is a new Q3 release, dated 18-Nov-2026 in the BCCh publication index.

## 3. Q2 portfolio net revision signal
- Earlier Q2 publication, as recorded in C160: portfolio-investment net = USD +299m; independently observed BDE monthly Q2 legs were assets USD +5,098.91m and liabilities USD +5,397.51m, with liabilities minus assets = USD +298.60m, rounding to +299m.
- New Q3 report Table 1 (PDF lines 170–217) shows Q2-2026 portfolio investment net = USD +154m.
- Published net difference: +154m minus +299m = -USD145m.
- This is evidence that the published Q2 portfolio net balance changed between the two releases. It is not evidence of the revised gross asset and liability legs individually.

## 4. What the revision table does and does not establish
- Table 3 (PDF lines 994–1029) reports Q2 financial-account total assets revised from USD 1,114m to USD 2,051m (+USD936m), and total liabilities from USD 4,536m to USD 5,118m (+USD582m).
- Those are total financial-account asset/liability revisions, not portfolio-investment-only asset/liability rows. The table's breakdown is by institutional sector and does not provide the required functional-category × leg cross-tabulation for portfolio investment.
- The Q2 portfolio net value in Table 1 is functional-category-level but net-only.
- Do not derive portfolio assets or liabilities from the revised net, from total financial-account legs, from IIP stocks, or from sector totals. Do not allocate the net change across legs.
- The report's revision statement and updated net value establish a new Q2 revision vintage trigger, but no Q2 portfolio A/L pair, observation-specific update timestamp, raw BDE export or BDE series update-time receipt was obtained in this bounded check.

## 5. Reused evidence and acceptance boundary
- C160 official BDE monthly series remain the earlier captured source-page evidence only: assets +5,098.91 USDm; liabilities +5,397.51 USDm; Q2 net difference +298.60 USDm. These values are not relabelled as the new Q3-release vintage.
- C160 archived IMF raw rows remain unchanged; no IMF re-query or scale conversion was performed.
- C161 established that the free BCCh BDE API requires a user account and enabled personal token; public basket Excel export was documented but not executed. This access boundary remains in force.
- Prior numeric comparisons and source-page arithmetic are preserved as historical evidence only; this report does not promote the current-vintage numeric gate.

| Gate | Status |
|---|---|
| Fixed 63-country cohort membership | PASS (reused) |
| Prior official BDE Q2 monthly asset/liability observations | CAPTURED — earlier source-page vintage |
| New official BCCh Q3-2026 release | FOUND |
| Q2 BOP revision occurrence | CONFIRMED |
| Q2 portfolio net, earlier publication | USD +299m |
| Q2 portfolio net, Q3 publication | USD +154m |
| Published Q2 portfolio net revision | -USD145m |
| Q2 revised total financial-account assets/liabilities | USD +2,051m / +5,118m; not portfolio-only |
| Q2 revised portfolio asset leg | NOT_EXPOSED |
| Q2 revised portfolio liability leg | NOT_EXPOSED |
| New-vintage BDE raw bytes / response metadata / SHA-256 | NOT_CAPTURED |
| Current-vintage dual-leg comparison | NOT_DONE |
| Same-vintage alignment to archived IMF panel | NOT_ESTABLISHED |
| CHL national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Exact next action and duplicate prevention
- Do not repeat the same credential-gated API attempt or claim the old public basket values are refreshed.
- Reopen CHL only if an authorized BDE session executes the documented public basket Excel export, or a genuinely accessible official data export provides both Q2 portfolio legs with series identifiers, update/vintage metadata and raw bytes/hash.
- Capture both legs separately, compare the revised Q2 net to +154m, preserve the old vintage, and then run exact sign/scale comparison to the archived IMF rows. If no current-vintage pair is available, retain PENDING/UNKNOWN and advance to another eligible fixed-cohort member.
- No net-to-leg back-solving, no IIP stock substitution, no use of total financial-account legs as portfolio proxies, no IMF re-query, no cohort rebuild, no paid service, no external contact.

## 7. Protected invariants
₹0; free official sources only. No synthetic data, fabricated timestamps, inferred signs, unsupported scale conversions, interpolation, net-to-leg back-solving or aggregate promotion. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 Steps × 12 Filters), Engines A–E and IPO-PLX V2.0 remain unchanged. No merge, workflow dispatch or production integration.
