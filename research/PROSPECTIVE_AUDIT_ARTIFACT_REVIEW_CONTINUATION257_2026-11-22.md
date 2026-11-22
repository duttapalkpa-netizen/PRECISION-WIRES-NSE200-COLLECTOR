# Prospective Audit Artifact Review — Continuation 257

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## 1. Continuity check
Re-fetched Master Continuity Ledger (blob `1accb587692d9b93c92c2e30a06f9aaaa90e2d8c`), C256 report (blob `d30ee2b4d64e8d7d26209fd08442124f0f7439f3`) and C255 report (blob `7c70f2cc215df850640b00baf31f207bbed59af9`). No C254/C255 PASS work was repeated.

## 2. Run #389 result
- Run ID `44998017821`, head `71e7102acd3e647263e29b5f806e596e048096b8`, conclusion `cancelled`.
- Job `137135532614`: steps 1–15 SUCCESS, including C254 test suite (step 5), 200-session acquisition/manifest validation, legacy equity master provenance, dataset QA, quarterly/XBRL extraction and corrected-label walk-forward (step 15).
- Step 16 P0 collection was cancelled; steps 17–33 skipped. Step 34 artifact upload SUCCESS.
- Artifact `prospective-watchlist-audit`, ID `14744698608`, 31,122,264 bytes; GitHub SHA-256 `5abaa9ca0110848f1181297db69b5774ced282b39f2cd045fa67993ceeb4ad6d`. Downloaded archive SHA-256 independently matches.
- Artifact manifest: 200/200 requested sessions, 200 retained and fully provenanced entries; dates 2026-02-16 through 2026-11-20.
- Dataset QA: PASS; 200 raw files/sessions/processed dates, 2,999 symbols, delivery quantity and percentage coverage 100%, no issues.
- Acquisition manifest validation: PASS; 200/200 entries, no errors.

## 3. Walk-forward evidence (exploratory metrics; not release approval)
- 100 sessions tested, 3,000 candidate rows, Top-30 ranking.
- Precision / base rate / lift:
  - T5_H1: 32.43% / 9.17% / 3.54x.
  - T10_H3: 22.03% / 6.83% / 3.23x.
  - T15_H5: 14.10% / 4.87% / 2.89x.
  - T20_H5: 6.96% / 2.20% / 3.17x.
- Recall respectively: 4.08%, 3.62%, 3.19%, 3.49%.
- Full-universe winner-vs-nonwinner mean probability separation is weak and reversed in the supplied output: winner 0.086886 vs nonwinner 0.087184; medians 0.086960 vs 0.086914. This is a material diagnostic to investigate before interpreting the probability score as calibrated winner discrimination; it does not negate the separately reported Top-30 lift.
- Output contains no T2_H1 metric; do not infer +2% results.
- These are historical target-hit precision/lift statistics, not cost-aware profitable trade returns. No trading-cost, slippage, drawdown or net-return conclusion is supported by this artifact.
- Watchlist ledger has 310 rows and columns for T5_H1, T10_H3, T20_H5 and maturity flags. It is not evidence of a completed daily prospective evaluation or mature 50-per-state Behavioral DNA.

## 4. C254 NSDL repair validation boundary
- Run #389 artifact contains no NSDL/FPI/DII/flow files. Therefore this artifact cannot verify C254 FPI date clipping or the 2026-07-17 DII gap. C254 remains CODED; regression step SUCCESS; real NSDL output validation PENDING.
- Do not claim the artifact's 200-session manifest proves NSDL date-window integrity.

## 5. Run #315 Macro-Geo status at review
- Run ID `44998007758` remains IN_PROGRESS; step 8 P0 market/media collection and step 9 corporate disclosures SUCCESS; step 10 bounded P0 source repair IN_PROGRESS; steps 11–19 pending.
- No artifact published at inspection. No source-level Macro-Geo conclusion or hard-gate status may be upgraded from this run yet.

## 6. Exact next actions
1. Investigate why full-universe winner probability mean/median do not separate winners from nonwinners, while preserving the reported Top-30 lift. Inspect target-label joins, probability calibration, sample definitions and state/selection aggregation; do not alter Production Selector or RANKING_SCORE.
2. Obtain an audit run/artifact that actually executes the NSDL flow collector, then validate FPI clipping and missing DII date using official data.
3. Wait for Run #315; inspect source-level output, event maturity, USD/INR and strict hard gate. Keep BLOCKED until all criteria are evidenced.
4. Add no +2% or profitability claims absent target-specific and cost-aware matured evidence.

## Guardrails
Audit branch only; ₹0; official/free sources only; no synthetic data/timestamps; UNKNOWN/BLOCKED never PASS. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged.
