# Chile BOP Revision-Vintage Provenance Audit — Continuation 39 Part-4
Date: 2026-11-19 (Asia/Kolkata)
Scope: official Banco Central de Chile revision policy and Q3-2026 release, specifically to explain the previously observed 2026-Q1/Q2 IMF-vs-current-BDE comparison differences. Research-only; no production changes.

## Executive decision
The prior Chile current-vintage comparison showed 2026-Q1/Q2 differences between the current Banco Central de Chile BDE series pages (updated 18-Nov-2026) and the IMF BOP panel. A new official BCB release and revision calendar establish that Q1/Q2 2026 Balance of Payments figures were scheduled for and actually underwent quarterly revision on 18-Nov-2026, at the Q3 release. The BCB release states that financial-account revisions reflected updated CNCI asset/liability information and newly incorporated financial-statement information.

This is a strong official explanation for why an earlier 07-Sep-2026 snapshot and a later 18-Nov-2026 snapshot can differ. It does NOT yet prove that every previously compared portfolio-investment BDE series value was revised by exactly the same component or amount. The portfolio-specific row-level reconciliation remains open.

## Official source 1 — BCB publication and revision policy
Source: https://www.bcentral.cl/documents/d/banco-central/calendario_cnn_bp?download=true
- Quarterly Balance of Payments first estimates are published on the 18th of the second month after the reference quarter ends (Q4 follows the annual preliminary close).
- Along with a new quarter estimate, previously published quarters for the current year are revised.
- Annual revisions are also applied to the quarters in the corresponding year.
- Exceptional revisions may occur for source/method changes and their reasons are to be explained to users.
- The 2026 calendar explicitly lists:
  - Q1 first version: 18-May-2026; quarterly revision 1: 18-Aug-2026; quarterly revision 2: 18-Nov-2026.
  - Q2 first version: 18-Aug-2026; quarterly revision 1: 18-Nov-2026.
  - Q3 first version: 18-Nov-2026.
This schedule aligns with the observed earlier BDE snapshot updated 07-Sep-2026 and the later current BDE snapshot updated 18-Nov-2026.

## Official source 2 — BCB Q3 2026 Balance of Payments release
Source: https://www.bcentral.cl/documents/33528/8798046/Balanza%2Bde%2BPagos%2BTercer%2BTrimestre%2B2026.pdf/cc1162a1-cca3-bc75-b697-3df5b826cb04?t=1794947628782
Report: “Balanza de Pagos, Posición de Inversión Internacional y Deuda Externa — Resultados al tercer trimestre de 2026”.
- The release states that Q1 and Q2 2026 figures were revised in line with the publication/revision policy.
- It states that financial-account revisions were explained by updated asset/liability information from the Compendio de Normas de Cambios Internacionales (CNCI) and inclusion of additional financial-statement information.
- Table 3 provides previous and revised Q1/Q2 2026 financial-account values and Q3 2026 first/revised publication values. Exact rows copied below are aggregate assets/liabilities and institutional sectors, not the functional-category portfolio series.

### Table 3 selected official values (USD million)
| Measure | Q1 previous | Q1 revised | Q1 difference | Q2 previous | Q2 revised | Q2 difference | Q3 first/current |
|---|---:|---:|---:|---:|---:|---:|---:|
| Financial account | 304 | 1,522 | 1,218 | -3,422 | -3,067 | 354 | -3,503 |
| Financial-account assets | 7,473 | 7,958 | 486 | 1,114 | 2,051 | 936 | 10,998 |
| Financial-account liabilities | 7,169 | 6,437 | -732 | 4,536 | 5,118 | 582 | 14,502 |
| Financial-account liabilities — banks | -2,024 | -2,354 | -331 | -1,798 | -2,040 | -241 | 6 |
| Financial-account liabilities — nonfinancial companies and households | 4,566 | 4,388 | -178 | 3,832 | 4,931 | 1,099 | 5,809 |

Note: the source table presents institutional-sector assets/liabilities and the total financial account. It does not provide the exact portfolio-assets and portfolio-liabilities BDE series crosswalk in this table. The values above must not be used as direct replacements for IMF P_F asset/liability observations.

## Reconciliation with the prior Chile vintage anomaly
Prior cross-country audit (Part 3) recorded:
- Official BDE older page snapshot, updated 07-Sep-2026: Chile portfolio assets/liabilities comparisons for 2025-Q4 through 2026-Q2 matched IMF panel 6/6.
- Current BDE pages updated 18-Nov-2026: 2025-Q4 remained 2/2 PASS; 2026-Q1/Q2 produced 4 REVIEW; 2026-Q3 had national observations but no corresponding IMF panel rows.
- BCB's official calendar and Q3 report now prove that Q1/Q2 revision at the 18-Nov publication was scheduled and that financial-account inputs were updated. Thus vintage mismatch is an established explanation class, not a scale conversion failure.
- Still NOT_DONE: capture a byte-level archived 07-Sep vintage of the exact portfolio assets/liabilities series and perform exact old-vs-new row-level reconciliation; map each BDE series code to the IMF P_F dimensions/instruments; determine whether the previously observed differences are entirely revision effects or include definition/sign/coverage differences.
- The earlier 07-Sep evidence was a rendered official page snapshot, not a raw-byte archived source. Keep its evidentiary grade lower until a reproducible archived file is available.

## GCR model / acceptance decision
1. Add mandatory `source_vintage_date`, `source_updated_at`, `observation_period`, `publication_date`, and `retrieval_timestamp_utc` to every national-source comparator.
2. Compare an IMF observation only with national data from a matched vintage or a documented revision bridge. Do not compare current national data with a stale IMF panel and call it a scale/sign failure.
3. Preserve old and revised values as separate immutable vintages; never overwrite the old snapshot.
4. Treat current Chile Q1/Q2 2026 comparisons as `REVIEW_VINTAGE_MISMATCH`, not PASS and not a confirmed scale failure, until exact portfolio-series reconciliation is complete.
5. Keep 2026-Q3 national observations as `IMF_PANEL_MISSING`; no forward fill or synthetic row.
6. Do not change GCR score weights, EMDE aggregation, production selector, ranking score, pressure fade, CORE-672 or Engines A-E.

## Acceptance update
| Gate | Status | Reason |
|---|---|---|
| Chile quarterly revision policy source | PASS | Official BCB policy states current-year quarters revised with new-quarter release |
| 18-Nov-2026 Q1/Q2 revision event | PASS | BCB Q3 report explicitly confirms Q1/Q2 revisions |
| Financial-account revision rationale | PASS | CNCI updated assets/liabilities and financial-statement data cited |
| Exact portfolio-series old-vs-new bridge | NOT_DONE | Table 3 is not the exact portfolio functional-category series |
| Chile 2026-Q1/Q2 IMF-vs-current-BDE | REVIEW_VINTAGE_MISMATCH | Revision timing now explained, exact series bridge still absent |
| Chile 2026-Q3 IMF panel row | BLOCKED / MISSING | National observation exists; IMF selected panel lacks rows |
| EMDE aggregate admission | BLOCKED | 40 countries no data; 83 country-entry cells empty; gaps/vintage/basis unresolved |

## Next highest-value actions
1. Obtain a byte-level dated snapshot/export of the exact Chile BDE portfolio assets and liabilities series as at 07-Sep-2026 (or another official archived vintage), with URL, retrieval UTC, headers, bytes and SHA-256.
2. Compare the archived vintage, 18-Nov current BDE series and IMF P_F panel row by row for Q4-2025 through Q3-2026; preserve all three values and vintage timestamps.
3. Map exact BDE series dimensions to IMF `A_NFA_T` / `L_NIL_T` and P_F only after confirming instrument coverage, sign and valuation basis.
4. Keep Brazil's PA revision/changelog and BOP6/BOP_BPM6 identity blockers unchanged; they still require exact owner/provider-side PA revision export or authoritative Brazil-specific mapping. Do not repeat the known failing transaction-ID-2 serializations.

## Evidence limitations and hard invariants
This audit uses official BCB PDF and policy-page text inspected from public web sources. The original PDF/policy bytes, response headers and SHA-256 were not captured in this turn; this is source-cited research evidence, not an immutable raw-file PASS. ₹0; official/free sources only. No synthetic data, guessed timestamps/hashes, interpolation, unapproved crosswalk, or aliases. UNKNOWN is not PASS. No production integration or macro weights.
