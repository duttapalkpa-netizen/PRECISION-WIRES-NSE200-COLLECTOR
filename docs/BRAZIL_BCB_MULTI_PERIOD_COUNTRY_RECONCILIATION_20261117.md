# Brazil BCB Multi-Period Domestic Portfolio Country Reconciliation — 2026-11-17

## Purpose and boundary
Extend the existing September-2026 one-period country validation without repeating source discovery or raw capture. This audit compares already archived latest-vintage SGS observations for domestic-market equity/fund and debt components with the exact monthly amounts stated in BCB's official monthly External Sector Statistics releases.

It is a **cross-vintage comparison**: the archived SGS CSVs were captured on 2026-11-17, while the cited monthly press releases were published earlier. A mismatch is not automatically a source error; it may reflect BCB's subsequent revisions. No historical press-release vintage raw dataset was available for these periods in this bounded audit.

## Inputs reused (no re-download)
- SGS 22930, domestic-market equity liabilities net: `bcb_domestic_market_crosscheck_202609/sgs_22930.csv`, blob `f7626bbc6b62630b6518451c472f718de3370175`.
- SGS 22936, investment-fund liabilities net: `data/raw/bcb/instrument_net_capture_20261117/sgs_22936.csv`, blob `3865fe689081cea11dff15227d01da4bb75925e0`.
- SGS 22942, debt securities issued in domestic market net: `data/raw/bcb/instrument_net_capture_20261117/sgs_22942.csv`, blob `3da8dc2b03da91e0dc9ff0861024c1ff17cce400`.
- All three files are preserved raw UTF-8 CSV with semicolon delimiter, decimal comma, USD million units; source rows run monthly through 2026-09. No data were re-fetched, transformed in-place, or overwritten.

## Sign and aggregation
The archived SGS series store liability net values with positive values representing net inflows and negative values representing net outflows for these selected series. For each reference month:
- Equity + investment funds = SGS 22930 + SGS 22936.
- Domestic debt securities = SGS 22942.
- Total domestic-market portfolio = (22930 + 22936 + 22942).
- Convert USD million to USD billion by dividing by 1,000.
- Compare independently rounded values to BCB's published one-decimal USD-billion figures. This is a comparison at the press release's stated display precision, not a general-purpose tolerance for series identities.

## Results
| Reference month | Equity + funds: SGS latest | BCB release | Match | Debt: SGS latest | BCB release | Match | Total: SGS latest | BCB release | Match |
|---|---:|---:|---|---:|---:|---|---:|---:|---|
| 2025-12 | -1.1 | -1.4 | NO | +5.3 | +5.3 | YES | +4.2 | +3.9 | NO |
| 2026-01 | +1.9 | +1.9 | YES | +6.9 | +6.9 | YES | +8.9 | +8.9 | YES |
| 2026-02 | +2.8 | +2.8 | YES | +2.8 | +2.6 | NO | +5.6 | +5.4 | NO |
| 2026-03 | -0.4 | -0.4 | YES | -2.5 | -2.5 | YES | -2.9 | -2.9 | YES |
| 2026-04 | +1.1 | +1.1 | YES | -0.5 | -0.5 | YES | +0.6 | +0.6 | YES |
| 2026-06 | -2.2 | -2.2 | YES | +1.6 | +1.6 | YES | -0.6 | -0.6 | YES |
| 2026-07 | +1.9 | +1.9 | YES | -0.7 | -0.7 | YES | +1.1 | +1.1 | YES |
| 2026-08 | -6.5 | -6.5 | YES | +1.3 | +1.3 | YES | -5.2 | -5.2 | YES |
| 2026-09 | -1.7 | -1.7 | YES | -0.4 | -0.4 | YES | -2.1 | -2.1 | YES |

Values are USD billions; positive = net inflow, negative = net outflow. The table shows independently rounded SGS calculations and BCB release values.

### Match summary
- 9 reference months checked.
- 7/9 months match all three release figures (Jan, Mar, Apr, Jun, Jul, Aug, Sep 2026).
- 23/27 component/total comparisons match at the release's one-decimal precision.
- Two reference months are vintage-sensitive exceptions:
  - Dec-2025: current SGS equity+funds is -USD 1.1bn vs release -USD 1.4bn; debt matches +USD 5.3bn; total is +USD 4.2bn vs release +USD 3.9bn.
  - Feb-2026: current SGS equity+funds matches +USD 2.8bn; debt is +USD 2.8bn vs release +USD 2.6bn; total is +USD 5.6bn vs release +USD 5.4bn.
- These are not silently accepted and not labelled data errors. They remain **VINTAGE_DIFFERENCE_UNRESOLVED** pending same-vintage data/revision bridge.

## Exact current-SGS values for the two exceptions

| Reference month | Equity + funds (USD mn) | Domestic debt (USD mn) | Total (USD mn) |
|---|---:|---:|---:|
| 2025-12 | -1,082.9 | +5,321.6 | +4,238.7 |
| 2026-02 | +2,786.2 | +2,783.2 | +5,569.4 |

The release values are published only to one decimal USD billion; the exact values above are the captured current SGS CSV values, not reconstructed historical release-vintage observations.

## Revision context
BCB's September-2026 External Sector Statistics release states that the revision covers definitive statistics for 2025 and revised estimates for 2026 (official release: https://bcb.gov.br/estatisticas/estatisticassetorexterno?kclid=KywNUB4ZA5A0GUTk). This is consistent with the possibility that a November-2026 SGS snapshot differs from earlier monthly press releases for December-2025 and February-2026. The specific numerical deltas have not yet been attributed to a documented series-by-series revision notice; therefore causation remains UNKNOWN.

## Acceptance
| Gate | Status |
|---|---|
| Reuse and integrity of three archived raw SGS files | PASS (existing archive hashes/commits retained) |
| Exact series identities and domestic-market scope | PASS (official BCB dataset metadata) |
| Nine-period latest-vintage comparison | PASS as executed |
| Full three-measure agreement across all nine periods | PARTIAL (7/9 periods) |
| Same-vintage press-release vs SGS comparison | NOT_DONE |
| Dec-2025 / Feb-2026 revision attribution | UNKNOWN / NOT_DONE |
| General all-period country equivalence | NOT_DONE |
| Brazil pilot acceptance | NOT_ACCEPTED |
| EM-wide panel | NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Next bounded action
Capture a matched-vintage bridge for the two exceptions only. Prefer official archived BCB release tables/XLS or the BCB historical-vintage dataset with a documented as-of date. Compare Dec-2025 and Feb-2026 values at the same publication vintage as the cited releases, then inspect the September-2026 revision's impact. Do not re-download the three current SGS files, re-run the September-only check, infer a blanket tolerance, or alter raw values.

## Safety and invariants
Research-only; ₹0 spend; official free BCB sources only. No synthetic data, no forward-fill, no invented timestamp/hash, no inferred revision cause. Keep BOP transactions distinct from IIP/CPIS positions. Do not modify Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, seed observations, parser admission, or production workflows.
