# CDSL FY 2026-27 Live-Series Vintage Drift and Arithmetic Recheck — 2026-11-13

## Objective
Revalidate the currently rendered official CDSL financial-year series against the previously captured FY 2026-27 observation. Detect vintage drift without overwriting the earlier snapshot.

## Official source
CDSL eServices Financial Year series:
https://www.cdslindia.com/eservices/Publications/FIIFinancial

Official source extraction retrieved 13-Nov-2026 (page crawl dated yesterday) currently renders FY 2026-27 total net investment as **-₹46,282.74 crore**. Earlier research snapshot recorded **-₹30,254.53 crore** for FY 2026-27. These are distinct observed vintages; the older value is retained as historical evidence, not silently replaced.

## Current FY 2026-27 component re-addition (₹ crore)
| Component | Current rendered value |
|---|---:|
| Equity | -103,326.25 |
| Debt-General Limit | +51,951.00 |
| Debt-VRR | -19,553.54 |
| Debt-FAR | +18,375.04 |
| Hybrid | -4,953.12 |
| Mutual Fund — Equity | +10,430.92 |
| Mutual Fund — Debt | -14.27 |
| Mutual Fund — Hybrid | -73.63 |
| Mutual Fund — Solution Oriented | 0.00 |
| Mutual Fund — Other | +875.12 |
| AIF | +5.99 |
| **Recomputed component sum** | **-46,282.74** |
| **CDSL displayed total** | **-46,282.74** |
| **Difference** | **0.00** |

Arithmetic: PASS (exact at displayed 2-decimal precision).

## Vintage comparison
| Observation | FY 2026-27 total (₹ crore) | State |
|---|---:|---|
| Earlier captured snapshot in prior audit | -30,254.53 | Historical snapshot retained |
| Current official rendered extraction | -46,282.74 | Current observation |
| Change between observations | -16,028.21 | Vintage delta; not an arithmetic error |

The prior value was independently internally consistent in its own snapshot. The current value is also internally consistent. The change is evidence of a revised/updated observation or page vintage, not proof that either snapshot is erroneous. Exact publication timestamp/revision history was not exposed in the extraction, so the reason and effective revision time remain UNKNOWN.

## Scope and safeguards
- This is rendered official HTML table revalidation, not raw downloadable-file acquisition.
- No raw file bytes, MIME type, or SHA-256 are claimed.
- FY 2026-27 is a partial financial year; do not compare it as a completed annual outcome.
- Do not mix this annual aggregate with daily CDSL confirmed-custodian series, NSE provisional exchange series, calendar-year series, or quarterly/fortnightly observations.
- Preserve the prior snapshot and its audit artifact. Do not overwrite historical values.
- No inferred daily values or synthetic rows.

## Acceptance ledger
| Check | Result |
|---|---|
| Current official FY 2026-27 row observed | PASS |
| All 11 components re-added | PASS |
| Displayed total reconciliation | PASS (₹0.00 Cr difference) |
| Prior snapshot preserved as separate vintage | PASS |
| Exact revision timestamp / cause | UNKNOWN |
| Raw annual source file acquired | NOT ACQUIRED |
| Raw SHA-256/schema QA | NOT STARTED |
| Daily factor acceptance | NOT AFFECTED / BLOCKED independently |

## Invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic data/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; research-only; no PR merge.
