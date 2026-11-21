# GCR India (IND) Q1-2026 — RBI Table 42 release-persistence audit (Continuation 187)
Date: 2026-11-21 (Asia/Kolkata)
Decision: **RBI'S Q1-2026 PORTFOLIO-LIABILITY NET VALUE IS IDENTICAL IN THE OFFICIAL 22-JUN, 22-JUL AND 25-AUG 2026 TABLE 42 RELEASES; NO REVISION IN THAT PUBLISHED NET FIGURE IS EVIDENCED ACROSS THESE THREE VINTAGES. THE IMF Q1-2026 LIABILITY VALUE REMAINS USD 1,512.508347m AWAY FROM RBI. CAUSE / SAME-VINTAGE BRIDGE NOT_ESTABLISHED; INDIA Q1 LIABILITY REVIEW; NATIONAL VALIDATION PARTIAL.**

## 1. Continuity preflight and task selection
- Re-fetched Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, India Q1 Continuation 41, India current-vintage supplement, Nigeria benchmark, and exact archived India IMF rows before action.
- Excluded completed PASS work: India 2024-Q2–2025-Q3 RBI Table 197 baseline (12/12); 2026-Q1 asset comparison; 2026-Q2 asset/liability/net comparisons; India sign and scale mapping. No new IMF request or panel/cohort rebuild.
- The exact open dependency in Continuation 41 was recover the official RBI Q1-2026 Table 42 release/vintage row and compare it to the existing IMF row. This audit tests persistence of the RBI published Q1 value across successive official releases; it does not infer an underlying IMF revision date.

## 2. Official RBI Table 42 release sequence
All three sources are official RBI Bulletin pages for “Standard Presentation of BoP in India as per BPM6 (US$ Million)”, with Jan–Mar 2026 marked preliminary (P):
1. 22-Jun-2026, Table 43 in ₹ crore: https://www.rbi.org.in/scripts/BS_ViewBulletin.aspx?Id=24289
2. 22-Jul-2026, Table 42 in US$ million: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24352
3. 25-Aug-2026, Table 42 in US$ million: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24424

The June table is in ₹ crore and is used only to verify the source's own reported rupee values; it is not converted here. The July and August tables are directly in US$ million and provide the comparison basis. Across all three releases, the Q1 2026 rows are unchanged:
- Portfolio Investment in India (liability comparator): net **-12,121 USDm** in July and August; June Table 43 reports the same underlying Q1 value as **-110,826 ₹ crore**.
- Portfolio Investment by India (asset comparator): net **+74 USDm** in July and August; June Table 43 reports **+677 ₹ crore**.
- Total portfolio investment net: **-12,047 USDm** in July and August; June Table 43 reports **-110,149 ₹ crore**.
- The published Q1 observations are marked preliminary (P) in the US-dollar tables.
- The RBI October-2026 Table 42 source captured in the existing supplement is the Apr–Jun table (Q2 2026), not a newer Q1 release. It therefore does not provide a fourth Q1 observation to compare.

This is a publication-persistence check, not a complete RBI revision history. It establishes that the specific published Q1 net values did not change across the inspected June, July and August release pages; it does not prove that no underlying source data were revised elsewhere or that the IMF snapshot uses the same national vintage.

## 3. Reused IMF exact-key observations — no new request
From existing exact-sample files in the immutable archive:
- IND A_NFA_T, 2026-Q1 raw OBS_VALUE = -74,050,352.86783295 USD; UNIT=USD; SCALE=6; derived = -74.050352868 USDm.
- IND L_NIL_T, 2026-Q1 raw OBS_VALUE = -13,633,508,347.33219 USD; UNIT=USD; SCALE=6; derived = -13,633.508347332 USDm.
- Existing archived comparison CSV: `docs/evidence/imf_bop_20261119/india_scale_reconciliation_current_vintage/india_bop_scale_sign_crosswalk.csv`.
- Exact raw values were reused as stored; no re-query, overwrite, or new timestamp was created.

## 4. Current RBI↔IMF comparison (USDm)
Previously established country-specific mapping is retained:
- RBI “Portfolio Investment in India” net ↔ IMF L_NIL_T, same sign.
- RBI “Portfolio Investment by India” net ↔ negative IMF A_NFA_T.
- RBI Table 42 publishes integer USD million; tolerance ±0.5 USDm.

| Q1-2026 leg | RBI latest inspected value | IMF archived value | Residual (IMF − RBI comparator) | Bound | Result |
|---|---:|---:|---:|---:|---|
| Assets | RBI by-India +74; IMF A_NFA_T −74.050353, mapped comparator +74.050353 | +74.050353 vs +74 | +0.050353 | ±0.5 | PASS |
| Liabilities | RBI in-India −12,121 | −13,633.508347 | −1,512.508347 | ±0.5 | REVIEW |
| Combined net | RBI −12,047 | IMF L_NIL_T − A_NFA_T = −13,559.457994 | −1,512.457994 | ±0.5 | REVIEW |

- The asset row remains within integer-million rounding.
- The liability discrepancy is unchanged in the RBI Q1 release sequence because the published RBI Q1 value remains -12,121 across the three inspected releases.
- The unchanged RBI value does not explain why the archived IMF value differs. No cause is inferred.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| Master Ledger / queue / registry / prior report preflight | PASS |
| Fixed 63-country cohort unchanged | PASS (reused) |
| Existing exact IMF Q1 rows reused | PASS; no new GET |
| RBI official June/July/August Q1 release pages | PASS |
| RBI Q1 portfolio liability net persistence across three releases | PASS — identical published net value |
| RBI Q1 portfolio asset net persistence across three releases | PASS — identical published net value |
| RBI/IMF Q1 asset comparison | PASS |
| RBI/IMF Q1 liability comparison | REVIEW — residual 1,512.508347 USDm |
| RBI/IMF Q1 combined net comparison | REVIEW — residual 1,512.457994 USDm |
| Exact same-vintage identity / underlying revision cause | NOT_ESTABLISHED |
| India Q1 full dual-leg validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Next exact action and closure boundary
- Do not repeat the same three RBI release-page extractions or re-query IMF.
- The inspected release sequence provides no RBI Q1 value revision that explains the residual. The next useful evidence would be a genuinely distinct official RBI source that carries a Q1-2026 revision/vintage history or the exact underlying portfolio liability transaction series, or an already archived IMF snapshot with explicit observation revision metadata that can be matched to the RBI release.
- If neither is available, preserve India Q1 liability as REVIEW and move to the next eligible country/work package after fresh full preflight. Do not adjust the RBI value, alter signs, or infer an IMF vintage.

## 7. Rejected shortcuts and invariants
- No assumption that “subject to revision” means the Q1 value was revised.
- No inference from unchanged published values that the IMF series is wrong.
- No conversion of June ₹ crore into USD for this comparison; July/August direct USD-million pages are used.
- No net-to-leg back-solving, stock-as-flow substitution, synthetic data, fabricated timestamps, IMF re-query, or cohort rebuild.
- ₹0; official/free sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN never PASS.
