# CDSL FY2026-27 Conflicting Retrieval Snapshot Reconciliation — 2026-11-13

## Executive finding
The previous report treated the search-index extraction showing FY2026-27 total -₹46,282.74 Cr as the current official rendered value. A direct open of the same official CDSL financial-year URL now exposes a different table snapshot dated 12-Nov-2026, with FY2026-27 total -₹30,254.53 Cr. The direct-open snapshot exactly matches the earlier preserved observation. Therefore, the evidence does **not** establish a confirmed permanent revision of the CDSL series. It establishes conflicting retrieval snapshots / cache or publication-vintage ambiguity.

## Official URL and retrieval evidence
URL: https://www.cdslindia.com/eservices/Publications/FIIFinancial

### Observation A — search-index extraction
Web result ref: `turn531956search1`
- Extracted FY2026-27 row total: -₹46,282.74 Cr.
- Components in that extraction: Equity -103,326.25; Debt-General +51,951.00; Debt-VRR -19,553.54; Debt-FAR +18,375.04; Hybrid -4,953.12; MF Equity +10,430.92; MF Debt -14.27; MF Hybrid -73.63; MF Solution 0; MF Other +875.12; AIF +5.99.
- The component sum equals -₹46,282.74 Cr at displayed precision.
- Search result did not expose a dated source snapshot marker sufficient to establish its effective date.

### Observation B — direct-open extraction
Web result ref: `turn668516view0`, lines 32–37.
- FY2026-27 row: Equity -88,632.53; Debt-General +52,396.65; Debt-VRR -19,726.76; Debt-FAR +19,397.85; Hybrid -4,918.26; MF Equity +10,434.71; MF Debt -14.27; MF Hybrid -72.34; MF Solution 0; MF Other +879.63; AIF +0.79.
- Displayed total: -₹30,254.53 Cr.
- Page extraction displays `**12-Nov-2026` immediately below the total row (line 34); treat this as a page/report marker, not a fully documented revision timestamp.
- Component sum independently recomputed: -₹30,254.53 Cr; difference to displayed total ₹0.00 Cr.
- This exact row matches the earlier captured FY2026-27 snapshot in the prior reconciliation artifact.

## Difference between the two retrieved rows
| Measure | Search-index snapshot A | Direct-open snapshot B | A minus B |
|---|---:|---:|---:|
| FY2026-27 total (₹ Cr) | -46,282.74 | -30,254.53 | -16,028.21 |
| Equity | -103,326.25 | -88,632.53 | -14,693.72 |
| Debt-General | 51,951.00 | 52,396.65 | -445.65 |
| Debt-VRR | -19,553.54 | -19,726.76 | +173.22 |
| Debt-FAR | 18,375.04 | 19,397.85 | -1,022.81 |
| Hybrid | -4,953.12 | -4,918.26 | -34.86 |
| MF Equity | 10,430.92 | 10,434.71 | -3.79 |
| MF Debt | -14.27 | -14.27 | 0.00 |
| MF Hybrid | -73.63 | -72.34 | -1.29 |
| MF Solution | 0.00 | 0.00 | 0.00 |
| MF Other | 875.12 | 879.63 | -4.51 |
| AIF | 5.99 | 0.79 | +5.20 |

The category deltas sum to -₹16,028.21 Cr. This is a source-snapshot discrepancy, not an arithmetic residual.

## Cross-row total check
Direct-open FY total row (line 33) reports grand total ₹1,514,470.93 Cr. Search-index extraction reports grand total ₹1,498,442.72 Cr. Difference: -₹16,028.21 Cr, equal to the FY2026-27 row difference. This strongly suggests the two retrieval snapshots differ in the current FY contribution while earlier-year aggregate values are otherwise aligned; a full row-by-row grand-total recomputation is not asserted here.

## Conclusion / corrected status
- The earlier claim that -₹46,282.74 Cr is definitively the current official live value is **withdrawn**.
- The direct-open page is dated 12-Nov-2026 and reports -₹30,254.53 Cr, matching the prior preserved snapshot.
- Search-index extraction separately reports -₹46,282.74 Cr and is internally arithmetically consistent.
- Effective publication time, cache state, and reason for the discrepancy remain UNKNOWN.
- Preserve both observations as separate immutable retrieval snapshots; do not overwrite or merge them.
- Do not select either value for production or factor input until a timestamped raw export or reproducible repeated direct retrieval resolves the discrepancy.

## Acceptance ledger
| Check | Result |
|---|---|
| Direct-open official FY row captured | PASS |
| Direct-open component sum vs displayed total | PASS (₹0.00 Cr) |
| Search-index FY row captured | PASS |
| Search-index component sum vs displayed total | PASS (₹0.00 Cr) |
| Two snapshot difference quantified | PASS |
| Earlier -₹30,254.53 snapshot confirmed in direct-open result | PASS |
| -₹46,282.74 confirmed as definitive live revision | NOT ESTABLISHED |
| Effective revision / cache timestamp | UNKNOWN |
| Raw source export and SHA-256 | NOT ACQUIRED |
| Production factor promotion | BLOCKED / NOT AUTHORIZED |

## Invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic data/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; research-only; no PR merge.
