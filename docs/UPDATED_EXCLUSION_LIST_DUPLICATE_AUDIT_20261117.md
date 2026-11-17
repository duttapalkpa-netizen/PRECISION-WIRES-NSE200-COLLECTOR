# Updated Exclusion List and Duplicate Audit — 2026-11-17

## Audit scope and source of truth
This audit recovered the historical V11.3 cost-aware replay artifact rather than relying on remembered tickers or a partial shortlist.

- Report: docs/V11_3_HISTORICAL_SIGNAL_COST_AWARE_BACKTEST_RESEARCH_REPORT_20261115.md
- Source workflow run: 43738312823
- Artifact ID: 14171590981
- Artifact SHA-256: c57469193b0f0fb6019202409b819118388a25897f0b698463f25a4e359a1360
- Historical processed input: 500,733 rows, 2,997 unique symbols, 200 sessions, 2026-01-21 to 2026-11-13.
- Historical scored cutoff-symbol observations: 484,985.
- Historical Top-30 signal ledger: 5,880 rows, 196 cutoffs, 2,176 unique symbols.
- Historical cost-aware trade ledger: 17,640 rows.

## Duplicate-check results (Python/pandas)
- Processed SYMBOL+DATE duplicate keys: 0.
- Top-30 signal SYMBOL+CUT_OFF duplicate keys: 0.
- Trade keys (CUT_OFF+SYMBOL+TARGET_PCT+HORIZON_SESSIONS) duplicate keys: 0.
- Missing SYMBOL/DATE keys in processed input: 0.
- All 2,176 historical Top-30 symbols are included in the 2,997-symbol analyzed universe.

## Exclusion policy
1. All 2,997 symbols in the historical processed 200-session universe are excluded from being described as never-before-analyzed NEW discoveries.
2. The 2,176 symbols that appeared in the historical Top-30 signal ledger are specifically marked as previously selected.
3. Exact previously selected SYMBOL+CUT_OFF pairs are DUPLICATE_BLOCK.
4. A previously analyzed symbol on a genuinely new cutoff is REVISIT, not NEW; it may be reported only as a clearly labelled re-evaluation with new source date and new evidence.
5. Only symbols absent from the full historical analyzed universe may be labelled NEW_CANDIDATE.
6. Normalization is conservative: trim whitespace and uppercase only. No fuzzy ticker matching, alias guessing, or symbol substitution.
7. The earlier V11.3 research profitability conclusion is not changed: the historical backtest showed negative mean net returns for +5% H+1, +10% H+3 and +20% H+5, including zero-cost sensitivity. Do not present the old signal ledger as a validated profitable list.

## Updated Exclusion List file
The attached companion workbook and CSV were generated from the exact artifact above:
- `PRECISION_WIRES_UPDATED_EXCLUSION_LIST_2026-11-17.xlsx`
- `updated_exclusion_list_2026-11-17.csv`
- Workbook tabs: Exclusion_List (all 2,997 analyzed symbols), Top30_Signal_Keys (5,880 exact signal rows), Duplicate_Audit.
- Artifact/source hash and row-level first/last processed sessions are included in the CSV.

## Duplicate guard
Added `scripts/research/duplicate_guard.py`.
It requires the historical processed universe, historical Top-30 signal ledger, and proposed candidate CSV. It fails closed on invalid historical keys or duplicate historical keys, blocks exact symbol-cutoff repeats, labels any symbol previously present in the historical 200-session universe as REVISIT, and only labels absent symbols NEW_CANDIDATE. It does not modify ranking or production logic.

## Today's new verified stock discoveries
NONE. This audit is a historical de-duplication and exclusion-list construction, not a fresh market scan. The Fed H.10 FX-basket analysis completed earlier is a non-stock macro diagnostic and is not counted as a stock discovery.

## Next-session instruction
Before any new 2%-to-20% candidate output, run duplicate_guard.py against the current candidate file. Do not emit NEW status without checking against the full historical universe and exact signal keys. If a new input dataset expands the universe, append its symbols and source hash to the exclusion ledger; do not erase history.
