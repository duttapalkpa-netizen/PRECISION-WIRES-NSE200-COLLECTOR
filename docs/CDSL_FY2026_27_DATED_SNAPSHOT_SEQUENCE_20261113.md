# CDSL FY2026-27 Dated Snapshot Sequence and Arithmetic Validation — 2026-11-13

## Objective
Resolve the previous two-snapshot conflict as far as possible by independently reopening the same official CDSL FY page twice in the current audit and preserving each date-marked observation separately. This does not assume page footer metadata is the dataset revision timestamp.

## Official source
https://www.cdslindia.com/eservices/Publications/FIIFinancial

## Repeated direct-open observations
| Observation | Page/report marker | FY2026-27 displayed total (₹ Cr) | Evidence |
|---|---|---:|---|
| A | 12-Nov-2026 | -30,254.53 | Earlier direct-open result `turn668516view0`, lines 32–37; repeated in current direct open `turn762323view0`, lines 32–37 |
| B | 13-Nov-2026 | -20,527.21 | Second direct open in current audit `turn924022view0`, lines 32–37 |
| C | Undated search-index extraction | -46,282.74 | Prior search-index result `turn531956search1`; no effective date marker exposed |

The two current direct-open observations carry distinct page/report markers (12-Nov and 13-Nov) and different values. This is consistent with a changing daily cumulative FY series. It does not by itself explain the undated -46,282.74 search-index snapshot; that value remains an unanchored separate observation and must not be promoted as a current value.

## 13-Nov-2026 component arithmetic (₹ Cr)
| Component | Value |
|---|---:|
| Equity | -79,733.73 |
| Debt-General Limit | +53,093.43 |
| Debt-VRR | -19,800.52 |
| Debt-FAR | +19,604.88 |
| Hybrid | -4,919.63 |
| Mutual Fund — Equity | +10,434.53 |
| Mutual Fund — Debt | -14.27 |
| Mutual Fund — Hybrid | -72.34 |
| Mutual Fund — Solution Oriented | 0.00 |
| Mutual Fund — Other | +879.65 |
| AIF | +0.79 |
| **Component sum** | **-20,527.21** |
| **Displayed total** | **-20,527.21** |
| **Difference** | **0.00** |

Arithmetic re-added independently from all 11 displayed component categories: PASS at 0.01 crore precision.

## Sequential change: 12-Nov to 13-Nov
| Measure | 12-Nov snapshot | 13-Nov snapshot | Change (13-Nov minus 12-Nov) |
|---|---:|---:|---:|
| FY2026-27 total (₹ Cr) | -30,254.53 | -20,527.21 | +9,727.32 |
| Equity | -88,632.53 | -79,733.73 | +8,898.80 |
| Debt-General | +52,396.65 | +53,093.43 | +696.78 |
| Debt-VRR | -19,726.76 | -19,800.52 | -73.76 |
| Debt-FAR | +19,397.85 | +19,604.88 | +207.03 |
| Hybrid | -4,918.26 | -4,919.63 | -1.37 |
| MF Equity | +10,434.71 | +10,434.53 | -0.18 |
| MF Debt | -14.27 | -14.27 | 0.00 |
| MF Hybrid | -72.34 | -72.34 | 0.00 |
| MF Solution | 0.00 | 0.00 | 0.00 |
| MF Other | +879.63 | +879.65 | +0.02 |
| AIF | +0.79 | +0.79 | 0.00 |

The total change of +₹9,727.32 Cr exactly equals the sum of category changes. The equity and debt category changes also match the separately observed 13-Nov vs 12-Nov daily cash movements previously captured in CDSL daily QA. This is a cross-check, not a substitute for daily raw data or proof that the annual series and daily series have identical extraction timestamps.

## Grand total row
- 12-Nov direct-open total row: ₹1,514,470.93 Cr.
- 13-Nov direct-open total row: ₹1,524,198.25 Cr.
- Difference: +₹9,727.32 Cr, equal to the FY2026-27 row change.
- This internal consistency supports the daily cumulative series interpretation.

## Corrected conclusion
1. The direct-open CDSL page returned 12-Nov FY total -₹30,254.53 Cr and then 13-Nov FY total -₹20,527.21 Cr in separately date-marked retrievals.
2. The 13-Nov component arithmetic is exact at displayed precision.
3. The one-day change is +₹9,727.32 Cr, matching the category-level change and previously captured daily CDSL cash change.
4. The earlier -₹46,282.74 search-index observation has no reliable date marker and is not suitable as a current live value. Preserve it as an undated conflicting extraction only.
5. The footer “Page last updated May 20, 2020” is stale page metadata and must not be mistaken for the report marker. The report marker under the table is 13-Nov-2026.
6. This is rendered HTML validation only. No downloadable raw source file, MIME type, byte count, or raw SHA-256 is claimed.

## Acceptance ledger
| Check | Result |
|---|---|
| 12-Nov direct-open dated snapshot preserved | PASS |
| 13-Nov direct-open dated snapshot independently retrieved | PASS |
| 13-Nov 11-component arithmetic | PASS (₹0.00 Cr difference) |
| 12→13-Nov total delta reconciliation | PASS |
| 12→13-Nov category delta reconciliation | PASS |
| Daily CDSL cash delta cross-check | PASS (rendered observations) |
| Undated -₹46,282.74 snapshot date established | UNKNOWN |
| Raw annual export acquired | NOT ACQUIRED |
| Raw SHA-256/schema QA | NOT STARTED |
| Production factor promotion | BLOCKED / NOT AUTHORIZED |

## Invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic data/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; research-only; no PR merge.
