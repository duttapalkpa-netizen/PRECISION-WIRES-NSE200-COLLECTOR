# CDSL FPI Derivatives — 12-Nov-2026 Extraction and OI Delta QA

## Source and observation identity
- Official source: https://www.cdslindia.com/eservices/publications/fiidaily
- CDSL page displayed report date: 12-NOV-2026.
- Derivatives data note says it is compiled from reports submitted by NSE, BSE, MSEI, NCDEX and MCX on 12-NOV-2026 and represents FPI trading/positions of the previous trading day.
- This is a separate derivatives positioning dataset; do not merge with cash-market FPI investment totals.
- Rendered official HTML table inspected. No raw archive bytes acquired; no SHA-256 claimed.

## 12-Nov-2026 derivatives table
Amounts in INR crore; contract counts as reported by CDSL.
| Product | Buy contracts | Buy amount | Sell contracts | Sell amount | End OI contracts | End OI amount |
|---|---:|---:|---:|---:|---:|---:|
| INDEX_FUTURES | 46,926 | 7,947.67 | 26,621 | 4,614.95 | 184,954 | 31,349.07 |
| INDEX_OPTIONS | 14,517,699 | 2,397,478.52 | 14,566,762 | 2,404,333.50 | 4,317,978 | 720,848.91 |
| STOCK_FUTURES | 340,168 | 23,625.43 | 339,541 | 23,901.06 | 6,115,686 | 410,110.74 |
| STOCK_OPTIONS | 419,990 | 30,494.35 | 432,056 | 31,475.38 | 1,494,678 | 103,262.88 |
| INTEREST_RATE_FUTURES | 0 | 0.00 | 0 | 0.00 | 3,800 | 73.63 |
| CURRENCY_FUTURES | 39,706 | 373.30 | 40,168 | 377.43 | 295,656 | 2.78 |
| CURRENCY_OPTIONS | 0 | 0.00 | 0 | 0.00 | 0 | 0.00 |
| COMMODITY_FUTURES | 31,129 | 967.87 | 31,951 | 1,000.72 | 75,722 | 1,900.55 |
| COMMODITY_OPTIONS | 976,181 | 24,327.39 | 1,024,879 | 25,311.32 | 396,422 | 13,303.08 |

## Adjacent-day end-OI change: 11-Nov to 12-Nov 2026
Delta = 12-Nov displayed end OI minus 11-Nov displayed end OI. These are absolute changes, not percentage changes.
| Product | OI contract delta | OI amount delta (INR Cr) |
|---|---:|---:|
| INDEX_FUTURES | -10,619 | -1,312.92 |
| INDEX_OPTIONS | +1,043,994 | +177,444.17 |
| STOCK_FUTURES | -11,043 | +1,831.37 |
| STOCK_OPTIONS | +72,768 | +6,150.13 |
| INTEREST_RATE_FUTURES | 0 | -0.11 |
| CURRENCY_FUTURES | -584 | -0.01 |
| CURRENCY_OPTIONS | 0 | 0.00 |
| COMMODITY_FUTURES | -75,131 | -1,941.14 |
| COMMODITY_OPTIONS | -522,313 | -13,474.29 |

## QA and interpretation
- PASS: all nine derivative product rows and all six reported fields per row transcribed from CDSL rendered HTML.
- PASS: adjacent-day OI deltas recomputed arithmetically from the 11-Nov and 12-Nov CDSL displayed OI values.
- OI contract count and OI amount can move in different directions (e.g. STOCK_FUTURES); do not treat contract delta as a notional delta or infer bullish/bearish direction from OI alone.
- Options rows combine buy/sell contracts and amounts as presented; this table does not provide call/put split, strike, expiry, or long/short investor-side classification. Avoid directional conclusions.
- 12-Nov derivatives report represents previous trading day(s), per CDSL note; the report date is not a claim that all underlying trades occurred on 12-Nov.
- Keep derivatives data separate from confirmed cash FPI flows and NSE provisional T-day flows.
- No synthetic data, no inferred missing records, no paid source, no spend, no external contact.
- Research-only; no production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or Hard Gate changed; no PR/merge.

## Next step
Accumulate adjacent official daily derivatives rows only when published, preserving the report date and source note, then test coverage and OI continuity across dates. Do not extrapolate or impute missing days.
