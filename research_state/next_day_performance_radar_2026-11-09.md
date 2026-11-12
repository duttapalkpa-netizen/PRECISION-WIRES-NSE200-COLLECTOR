# PRECISION-WIRES V11.3 — Next Trading Day Performance Radar
Date prepared: 2026-11-07
Forecast cutoff: 2026-11-06 EOD
Next NSE trading session target: 2026-11-09

## Purpose and architecture boundary
The Next-Day Performance Radar is an integrated supplemental V11.3 research output, not a separate project and not a replacement selector. It does not alter production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, risk modifier, or Hard Gate.

## Source and coverage
- Existing successful NSE collector artifact: Run 42216720465, artifact 13501792734, SHA-256 66fe9d58e7e2c0c3b2dd335de3416b551b0fea1ef5fc0d3c31aa5108fe79a015. Its processed dataset had 200 sessions, 2,991 symbols, QA PASS. Its 6-Nov date was incomplete in the processed panel (only 60 symbols), so it was NOT used as the current market cutoff.
- Exact official 6-Nov-2026 NSE CM UDiFF Bhavcopy from user's Library: /BhavCopy_NSE_CM_0_0_0_20261106_F_0000.csv.zip; 208,064 bytes; ZIP SHA-256 339e3f07bb00acb27d0200ea5bfa748de71d9b3f779b956d1069f2168c8c9904. Official file yielded 3,715 rows overall and 2,746 unique EQ symbols.
- Merged official 6-Nov OHLCV with historical data through 5-Nov. Excluded delivery variables entirely because UDiFF Bhavcopy did not contain delivery quantity/percentage. This avoids carrying forward or inventing delivery data.
- 2,690 symbols had at least 20 prior sessions and received model scores; remaining 56 official EQ symbols are retained as UNKNOWN_INSUFFICIENT_HISTORY. Output has exactly 2,746 unique symbol rows.

## Model
- Separate price-volume-only logistic model, using chronological 70% fit / 15% Platt calibration / 15% untouched test validation. Current probabilities use time-split Platt calibration over 426,853 matured training rows; last training observation cutoff 2026-10-30 so T+1/T+3/T+5 labels are fully matured through 2026-11-06.
- P5_H1: probability that next session's HIGH reaches >= +5% relative to 6-Nov close.
- P10_H3: probability that any HIGH over next 3 sessions reaches >= +10%.
- P20_H5: probability that any HIGH over next 5 sessions reaches >= +20%.
- These are intrahorizon high-touch probabilities, not close-to-close returns, directional certainty, or guarantees.
- Delivery excluded from the model; model is a research-only price-volume sidecar, not the production V11.3 score.

## Independent chronological holdout (untouched final 15%)
- Test sample: 71,259 symbol-session rows; test starts 2026-09-24.
- P5_H1: Brier 0.0844485; ECE 0.0125657; test base rate 9.4739%; mean predicted probability 8.2173%.
- P10_H3: Brier 0.0575061; ECE 0.0011155; test base rate 6.1817%; mean predicted probability 6.2261%.
- P20_H5: Brier 0.0181407; ECE 0.0032928; test base rate 1.8496%; mean predicted probability 2.1789%.
- Current setup labels: 805 POSITIVE_SETUP, 233 NEGATIVE_SETUP, 1,652 NEUTRAL_OR_UNCLEAR, 56 UNKNOWN_INSUFFICIENT_HISTORY.

## Highest-ranked 15 (by calibrated P5_H1)
1. RELCHEMQ: P5_H1 20.76%, P10_H3 11.24%, P20_H5 2.62%
2. MFML: 20.12%, 11.01%, 2.60%
3. BNAGROCHEM: 19.42%, 12.05%, 2.67%
4. BANSALWIRE: 19.09%, 12.03%, 2.68%
5. ITL: 19.06%, 10.77%, 2.60%
6. PREMCO: 18.99%, 10.43%, 2.55%
7. RAMKY: 18.94%, 10.81%, 2.61%
8. TIPSFILMS: 18.86%, 10.31%, 2.53%
9. AMAL: 18.56%, 11.58%, 2.62%
10. GENESYS: 18.50%, 11.05%, 2.53%
11. MTNL: 18.45%, 10.50%, 2.57%
12. TTML: 18.38%, 10.39%, 2.55%
13. GNRL: 18.33%, 8.60%, 2.19%
14. IKIO: 18.25%, 10.51%, 2.58%
15. AIROLAM: 18.21%, 10.78%, 2.61%

## Output artifacts
- CSV: outputs/finalists/next_day_performance_radar_2026-11-09.csv
  SHA-256 54a6ca0d5e0e682a5898a80c9a9bb20d92fbd1f589189a8c748b85d188b735ab
- Summary JSON: outputs/finalists/next_day_performance_radar_summary_2026-11-09.json
  SHA-256 fe74f9654c7ca40edf01c294c8a750f7a86519b9f85917c2c10885fe146a657a
- Download package ZIP SHA-256 b126cd6310afea4eb197300d8709f0353d8334e9ed40e2b56318396c9f23ee0e

## Pipeline integration and QA
- Added supplemental pipeline entry pipeline/next_day_performance_radar.py.
- Integrated radar step after final selection in .github/workflows/nse_collector.yml; schedule moved to 19:00 IST (13:30 UTC) so it runs after cash-market close and targets next session.
- Added .github/workflows/next_day_radar_static_qa.yml.
- Static QA Run 42382848873 completed SUCCESS; Python compilation and architecture-contract assertions passed.
- Important limitation: the committed initial pipeline runner still requires a final integration check against the complete official raw Bhavcopy feed; do not claim a full scheduled end-to-end radar workflow PASS yet. The 2026-11-09 radar CSV above is independently generated from the verified 6-Nov official Bhavcopy and 200-session historical artifact, with full 2,746-symbol coverage.

## Next required action
Refactor the scheduled radar runner to consume the latest official raw NSE CM Bhavcopy in data/raw (not the partial processed panel) and use the same price-volume-only model when delivery fields are absent. Add a fail-closed completeness check and validate the next scheduled run's artifact before claiming automated daily completion.
