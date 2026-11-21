# Quarterly Results Exploratory Event-Study Readback — Run #127 Evidence + Run #416 Price Panel

Date: 2026-11-22 (Asia/Kolkata)
Status: EXPLORATORY COMPUTATION COMPLETE; FORMAL EVENT-STUDY ACCEPTANCE BLOCKED.

## 1. Continuity preflight and task selection
- Re-read the Master Continuity Acceptance Ledger through C228, GCR Master Priority Queue through C228, Historical Task Registry through C228, the C228 Run #339 retention report, and the 2026-11-21 Nightly Rotation Backtest Research Review.
- Skipped C227 and all explicitly completed PASS work. Did not repeat the Run #339 artifact inventory/hash audit.
- Selected the unresolved quarterly-results event-study input blocker because Run #127 reported `data/processed/nse_eq_200_sessions.csv` missing from its bounded workspace.

## 2. Evidence reused (no synthetic data)
- Run #127: `44935826471`, commit `edc7f41ac81c0381b0257e1b819b8fb59e34ae79`; artifact `14719334134`, ZIP SHA-256 `9220686f33a8242252958091f9abd319d54c0030d2fb8d024b2781dbb0b8cff7`.
- Run #127 report: 500/500 result-disclosure source records valid; 2,971/2,971 calendar records valid; 476 verified metric rows; 23 superseded revisions; 1 blocked metric row; report status `COLLECTED_WITH_BLOCKERS`.
- Run #416: `44744602064`; artifact `14632139339`, ZIP SHA-256 `b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082`.
- Reused its retained normalized NSE price panel `data/processed/nse_eq_200_sessions.csv`; extracted CSV SHA-256 `d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db`. It contains 503,892 rows, 2,999 symbols and 200 sessions from 2026-02-16 through 2026-11-20.
- Reused Run #127's `quarterly_results_disclosures.csv` (500 rows) and the event-study logic in `pipeline/quarterly_results_research.py`. No fresh market-data request and no values were synthesized.

## 3. Exploratory event-study readback
The code's current rule uses the first available trading session strictly after the local disclosure date as the reaction base; D1/D3/D5 are subsequent session offsets from that base.

| Measure | Result |
|---|---:|
| Result disclosures | 500 |
| Disclosures with usable BROADCAST_AT and source URL | 463 |
| Matched symbols with a post-disclosure price session | 391 |
| Excluded for missing BROADCAST_AT / source | 37 |
| No post-disclosure price match | 72 |
| D1 matured observations | 390 |
| D3 matured observations | 381 |
| D5 matured observations | 0 |

Exploratory return distribution:
- D1: mean +0.0402%, median -0.3954%; 156 positive, 60 at/above +2%, 25 at/above +5% (n=390).
- D3: mean -1.0611%, median -1.1076%; 131 positive, 56 at/above +2%, 22 at/above +5% (n=381).
- D5: no matured observations; all 391 matched rows are immature at the Run #416 panel cutoff.

These are descriptive calculations only. They are not a trading signal, causal estimate, or proof of profitability. The event-study implementation's horizon/base convention must be reviewed against a formally approved specification before the rates are accepted as H+1/H+3 outcomes.

## 4. Remaining blockers (not promoted)
1. D5 maturity is zero because the price panel ends 2026-11-20 and the event sample extends through 2026-11-21.
2. 37 rows have missing `BROADCAST_AT`; creation/revision timestamps must not be silently substituted for original broadcast time. Revision-only records need a separate explicitly defined treatment if desired.
3. 72 symbols have no matched post-disclosure price session in the reused panel; reasons require row-level classification (symbol coverage, listing date, or timing).
4. Run #127 financial coverage remains incomplete: 476 verified rows / 500 disclosure rows; 23 superseded revisions and 1 blocked row. One blocked AGL attachment returned HTTP 404 and its iXBRL fallback did not expose the required facts/basis. Do not coerce to zero or mark PASS.
5. The reused Run #416 panel is not a Run #127 contemporaneous raw-provenance panel. This readback does not satisfy the future raw-source artifact retention proof from C228.

## 5. Acceptance
- Exploratory panel join/readback: COMPUTED.
- Formal quarterly event-study gate: BLOCKED / NOT ACCEPTED.
- Step 2 financial coverage: BLOCKED_INCOMPLETE_OR_UNVERIFIED_COVERAGE.
- Production integration: NOT AUTHORIZED.

## 6. Protected invariants
Research-only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. No paid APIs, no synthetic data, no fabricated timestamps. ₹0. UNKNOWN never PASS.
