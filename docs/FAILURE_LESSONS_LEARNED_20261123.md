# Failure & Lessons Learned Research Log — 2026-11-23
## PRECISION-WIRES V11.3 | Observation-only, pre-market

**Data cutoff:** NSE 20-Nov-2026 EOD.  
**Review time:** 23-Nov-2026 08:45 IST.  
**Market state:** pre-open; 23-Nov session outcome not yet available. NSE capital-market trading is closed on 24-Nov-2026, so 23-Nov cohort H+1 is evaluated after 23-Nov close; H+3 after 25-Nov close; H+5 after 27-Nov close.

## 1. Cohort and outcome state
- Previous shadow cohort from 20-Nov cutoff: 8 unique symbols / 10 selector rows — NRL, V2RETAIL, SIGACHI, RSDFIN, KDDL, YATRA, KMCSHIL, HINDOILEXP.
- 23-Nov 08:45: all eight remain **PENDING** for 23-Nov H+1. No false positive, success or failure can be assigned before the 23-Nov close and source-data maturity.
- Target-wise missed winners after the 20-Nov cutoff: **UNKNOWN / PENDING**; eligible-universe row-level predictions and future outcomes are not yet available.
- Current 23-Nov research watchlist: one observation-only candidate, WELSPUNLIV; not a production selector promotion.

## 2. Existing immutable lessons carried forward
- `PW-LSN-20261121-001` — exact forward-session label defect: keep historical metrics blocked until exact exchange-session windows and full-horizon maturity are proven.
- `PW-LSN-20261121-002` — H+5 JSON/CSV count mismatch: canonical row-ledger parity still open.
- `PW-LSN-20261121-003` — raw NSE artifact allowlist omission: Run #398 improves byte retention, but now exposes a distinct session-calendar defect below.
- `PW-LSN-20261122-001` — Macro-Geo archive report schema mismatch: source collection / downstream hard gate remains blocked.
- `PW-LSN-20261122-002` — archive report consumer key mismatch: code patch committed, regression execution/end-to-end Macro-Geo acceptance still pending.

## 3. New verified lessons

### PW-LSN-20261123-001 — Holiday dates counted as trading sessions
**Evidence**
- Run ID `45027842316`, artifact ID `14757294944`, source head `7360870b768a6ed746451afa96ea918a3bffae07`.
- ZIP SHA-256 `212a84103f2a9f47681865c7e165fe0247001b02d9563a5cef578636fb0b1898` independently matches GitHub artifact digest.
- Raw-file byte/hash integrity: 200/200 PASS. Manifest has 200 unique requested dates.
- Internal CSV DATE1 audit: only 188 unique observed trading dates; 12 requested dates are exact duplicate files for the previous session and are official NSE holidays: 03-Mar, 26-Mar, 31-Mar, 03-Apr, 14-Apr, 01-May, 28-May, 26-Jun, 14-Sep, 02-Oct, 20-Oct, 10-Nov.
- NSE `data/qa/qa_report.json` reports 200 sessions/processed dates because it counts requested slots, not unique internal DATE1 values. The holiday list is independently supported by NSE Circular NSE/CMTR/71775 and the official NSE holiday page.
- Detailed evidence: `docs/NSE_200_SESSION_ARCHIVE_SEMANTIC_DATE_AUDIT_20261123.md`.

**Root cause:** VERIFIED — holiday calendar/session generation included 12 NSE holidays; the archive endpoint returned the prior valid session's same CSV for those requested dates. QA checked bytes and hashes but did not assert internal DATE1 equals manifest trade_date or reconcile official holidays.

**Why research missed it:** duplicate holiday rows can distort EMA/RSI/volume windows and compress H+1/H+3/H+5 exchange-session labels. The existing QA's 200 count was request-count semantics, not 200 distinct exchange sessions.

**Corrective research/test**
1. Parse official NSE holiday calendar and build a unique valid trading-session spine.
2. Test every retained CSV: internal DATE1 == manifest trade_date; no official holiday; distinct observed dates == expected sessions.
3. Preserve the 188 valid existing sessions; add 12 earlier valid sessions to reach 200 unique trading sessions; do not redownload already verified valid files.
4. Re-run the label-v2/walk-forward audit only on the corrected date spine, with row-level prediction exports and independently reconciled denominators.

**Result/confidence:** 200/200 file hashes confirmed; 188 unique dates and 12 holiday duplicates confirmed. The 200-session coverage claim is **NOT ACCEPTED**. Run #398's target metrics cannot be accepted because row-level outputs are absent to remove duplicate cutoffs and recompute. No production selector/ranking change.

**Carry-forward:** active P0 QA backlog for the next research run. Keep all affected historical performance metrics UNKNOWN until corrected rerun.

### PW-LSN-20261123-002 — NSE filing timestamp timezone label not proven
**Evidence**
- Raw quarterly-results calendar WELSPUNLIV `an_dt`: `21-Nov-2026 19:13:50` (no timezone suffix).
- Normalized `BROADCAST_AT` / `PUBLICATION_TIMESTAMP`: `2026-11-21T19:13:50+00:00`.
- Official NSE quote page displays broadcast `21-Nov-2026 19:13:50` without UTC designation. Similar wall-clock/normalized pairs occur for APLAPOLLO, TATASTEEL and HMAAGRO.
- Official NSE quote page: https://www.nseindia.in/get-quote/equity/WELSPUNLIV/Welspun-Living-Limited

**Root cause:** discrepancy VERIFIED; exact source timezone contract remains UNKNOWN. The normalizer may be appending +00:00 to a local wall-clock value rather than converting from the source timezone; this must not be assumed without contract evidence.

**Why research missed it:** the current schema accepts a timezone-aware ISO string without proving the original source field's timezone semantics. This can shift events by 5h30 and corrupt pre-event/post-event joins or macro vintages.

**Corrective research/test**
1. Preserve raw source datetime text and a separate `source_timezone_status`.
2. Obtain official source/API timezone documentation or validate five filings against official NSE display and independently confirmed publication times.
3. Add a regression assertion that a timezone offset is only emitted after verified conversion; otherwise serialize as unzoned source text and mark UNKNOWN.
4. Until then, exclude these normalized timestamps from GCR/news point-in-time joins.

**Result/confidence:** representation mismatch confirmed; timezone contract unresolved. GCR/news event-time alignment remains UNKNOWN. No timestamp correction or production code change today.

**Carry-forward:** add to daily source-timestamp checklist; do not treat normalized +00:00 as verified UTC.

## 4. Candidate-selection post-mortem / missed-mover observations
- **NRL:** 20-Nov close ₹184.36; 5-session +140.65%, 20-session +217.42%, RSI14 86.47, but 20-Nov volume 0.76× prior-20-session average and traded value about ₹3.42 crore. Existing ISIN conflict and prior BE/5% band/100% margin flags remain unresolved. Selection risk: extreme extension, identity and liquidity risk. Outcome remains PENDING; not yet a false positive.
- **V2RETAIL:** close ₹162.06; 1-day +2.99% and volume 4.11× average, but 5-day −1.24%, 20-day −4.75%, close below EMA50, RSI14 48.73; prior promoter-sale disclosure remains a supply-risk context. Outcome PENDING.
- **SIGACHI:** close ₹30.57, below the established ₹50 base-universe floor; high volume ratio does not override the existing universe rule. Excluded by rule, not a production miss.
- **RSDFIN:** 195 shares traded, traded value about ₹0.0016 crore; illiquid. Excluded.
- **KDDL:** 5-day +10.99%, 20-day +26.21%, trend positive, but volume 0.77× average and no fresh verified catalyst; watch-only, not qualified.
- **YATRA:** close below EMA50, RSI14 about 53.3, volume 0.45× average; prior Q2 data mixed. Not qualified.
- **KMCSHIL:** 5-day +21.38%, 20-day +34.49%, RSI14 74.24, but volume only 1.05× average and no fresh official catalyst verified. Not qualified.
- **HINDOILEXP:** 5-day +12.69%, 20-day +31.64%, but volume 0.39× average and prior ST ASM-1 / high-valuation flags. Not qualified.
- **HMAAGRO (not eligible under base universe):** official NSE close ₹33.91 (<₹50 floor), +15.58% on 20-Nov, 1,129.70 lakh shares and ₹373.25 crore turnover. NSE shows board-outcome broadcast at 20-Nov 16:03:44, after the 16:00 close. The post-close filing must not be used as a predictive catalyst for the earlier same-session +15.58% move. Classify as universe exclusion plus hindsight-attribution risk, not an avoidable premarket miss.
- **APLAPOLLO / TATASTEEL:** major weekend transaction disclosure, but 20-Nov technical structure was weak (below EMA20/EMA50; RSI below 50) and NIFTY Metal closed −0.23%. Keep event-only; no qualified alert without technical confirmation.

## 5. Daily scorecard
| Measure | 23-Nov pre-market status |
|---|---|
| Previous selected unique symbols | 8 |
| Matured outcomes available at 08:45 | 0 |
| Confirmed false positives | UNKNOWN / PENDING |
| Target-wise missed winners | UNKNOWN / PENDING |
| Avoidable vs unavoidable misses | UNKNOWN |
| New confirmed data/QA failure modes | 2 (holiday-session mapping; timestamp timezone representation) |
| Production rule changes | 0 |

## 6. Today’s learning → research addition → next verification
1. **Learning:** byte-perfect files do not prove unique valid exchange sessions; a source timestamp string with `+00:00` does not prove UTC semantics.
2. **Research addition:** add holiday-aware DATE1/manifest parity and raw-timezone contract checks to the daily checklist and audit backlog; link lessons `PW-LSN-20261123-001` and `PW-LSN-20261123-002`.
3. **Next verification:** correct the session spine, add 12 earlier valid sessions, rerun a short date-semantic regression, then recompute target-specific matured metrics from row-level outputs; separately validate NSE timestamp timezone semantics.
4. **No production change:** Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is not PASS.


---

## 7. Evening update — 23-Nov-2026 Nightly Rotation Backtest

**Review report:** NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261123.md  
**Report commit:** 21ade4ee39b9693f89d4ac8ece316bab79854807  
**Report SHA-256:** 7c0210b8bb8e55279df65d2974658338f510b1342c716276c65e4f92ae7c928e  
**Evidence:** Run #420 / ID 45202379089; job 137788955150; artifact 14833925413; ZIP SHA-256 693cb2d8f68cc38a56fd9c17140f6126e11bb1617d6b0fee9ad4d2de5264686d; processed dataset SHA-256 8d6c634ddbb442bd5003ec96f20fdac8f150b5775f451efd84eeb5262bc12f57.

### Existing lessons updated with new occurrences/evidence (no duplicate IDs)

- **PW-LSN-20261121-001 — forward-label defect:** Run #420 code SHA-256 dca7363ef1c5f56a097ed66b4305935f2c90975e2387b9c5b44780c4101f83e2; future_outcomes() lines 98–105 uses shift(-1).rolling(h,min_periods=1).max(), and lines 532–534 train WIN5_H1/WIN10_H3/WIN20_H5 from those labels. Exact next-session post-hoc diagnostics differ sharply from the stored JSON (notably +10 H+3: 40.40% stored vs 15.27% corrected; +20 H+5: 20.63% vs 5.69%). Root cause VERIFIED; acceptance OPEN.
- **PW-LSN-20261121-002 — H+5 JSON/CSV reconciliation:** Run #420 metrics JSON implies 619 +20% H+5 Top-30 hits; prediction CSV contains 622 rows at/above +20% using its stored labels. Three-row mismatch persists. Root cause VERIFIED as an artifact-internal reconciliation gap; acceptance OPEN.
- **PW-LSN-20261123-001 — holiday dates counted as sessions:** Run #420 again reports 200 requested/date labels, but the 12 official holiday-labelled rows are exact copies of the previous valid session for every shared symbol; only 188 unique valid sessions remain. Code SHA-256: collector a55e6390f7e4299fc47b812baaa24047bbfae84686e397f1535e08f56c6f7e0f; builder 7190c653a829b56eaf2041a9886cf0b873de0bd2d1af1821ce0bcb80458181a1; QA 2a7590ad14522fa0440ad4609d11e12e0414f5b25f948c10d47c59c025803c19. QA's PASS is not semantic session acceptance. Root cause VERIFIED; acceptance NOT_MET.
- **PW-LSN-20261121-003 — raw manifest/provenance:** Run #420 artifact contains the processed dataset but no raw source files/per-file manifest; raw publication timestamps and per-file hashes remain unavailable. Dataset hash does not replace raw provenance. Acceptance OPEN.
- **PW-LSN-20261123-002 — source timestamp timezone:** no new timezone contract evidence; source timestamp remains unzoned/UNKNOWN. Carry forward unchanged.

### New immutable lessons

**PW-LSN-20261123-003 — H+3/H+5 maturity calendar offset**
- Cutoff 20-Nov; 23-Nov = H+1; 24-Nov holiday; 25-Nov = H+2; 26-Nov = H+3; 27-Nov = H+4; 30-Nov = H+5.
- The morning note labelled 25-Nov as H+3 and 27-Nov as H+5, one valid session early. Root cause VERIFIED (cutoff anchor vs alert-date anchor).
- Test: maturity engine must advance from cutoff over official valid exchange sessions; expected artifact cutoff_horizon_maturity_audit_20261124.json; sample = one verified cutoff/holiday sequence; acceptance OPEN.

**PW-LSN-20261123-004 — HINDOILEXP +2%/+5% H+1 missed winner**
- Expected: no qualified alert; actual: 20-Nov close ₹216.82 to 23-Nov high ₹233.10 (+7.51%), close ₹224.03 (+3.33%); adverse −2.22%.
- Cutoff evidence: 5d +12.69%, 20d +31.64%, EMA20>EMA50, RSI 72.31, RVOL 0.39×; morning note explicitly flagged low volume and prior ASM/high-valuation risk.
- Confidence SUPPORTED, not causal proof. Dataset hash 8d6c634ddbb442bd5003ec96f20fdac8f150b5775f451efd84eeb5262bc12f57; retrieval 23-Nov 15:11:40Z; source publication timestamp unavailable. Test: retain row-level decision reason and quantify low-RVOL false-negative cohort; artifact daily_missed_winner_incident_20261123.csv; acceptance OPEN.

**PW-LSN-20261123-005 — SHALPAINTS +2%/+5% H+1 missed winner**
- Actual high +19.89%, close +6.72%, adverse +5.67%; cutoff 5d +1.55%, 20d +41.09%, EMA20>EMA50, RSI 73.58, RVOL 0.08×.
- Confidence HYPOTHESIS (low-volume/liquidity gate plausible; exact selector decision row missing). Same dataset hash; source publication timestamp unavailable. Test: compare cutoff liquidity/volume gate against the complete 1,032-row decision ledger; acceptance OPEN.

**PW-LSN-20261123-006 — HITECH +2%/+5% H+1 missed winner**
- Actual high +16.36%, close +13.51%, adverse +6.04%; cutoff 5d −0.26%, 20d +14.06%, EMA20<EMA50, RSI 54.94, RVOL 0.56×.
- Confidence HYPOTHESIS (trend/volume confirmation weakness); exact exclusion reason absent. Same dataset hash; publication timestamp unavailable. Test: reconcile cutoff EMA/RSI/RVOL gates with decision export; acceptance OPEN.

**PW-LSN-20261123-007 — ITI +2%/+5% H+1 missed winner**
- Actual high +15.96%, close +12.41%, adverse +0.72%; cutoff 5d −8.34%, 20d +8.12%, EMA20<EMA50, RSI 49.16, RVOL 0.04×.
- Confidence HYPOTHESIS (weak trend/participation); exact exclusion reason absent. Same dataset hash; publication timestamp unavailable. Test: same bounded cutoff-gate reconciliation; acceptance OPEN.

**PW-LSN-20261123-008 — THOMASCOOK +2%/+5% H+1 missed winner**
- Actual high +14.68%, close +12.85%, adverse +1.17%; cutoff 5d +4.36%, 20d +21.23%, EMA20>EMA50, RSI 68.10, RVOL 0.98×.
- Confidence UNKNOWN; no row-level exclusion reason. Same dataset hash; publication timestamp unavailable. Test: recover exact candidate/exclusion decision; acceptance OPEN.

**PW-LSN-20261123-009 — AJMERA +2%/+5% H+1 missed winner**
- Actual high +13.72%, close +8.93%, adverse −2.47%; cutoff 5d +12.01%, 20d +16.94%, EMA20>EMA50, RSI 71.36, RVOL 9.81×, delivery 13.90%.
- Confidence UNKNOWN; apparently strong volume/trend but candidate decision row absent. Same dataset hash; publication timestamp unavailable. Test: decision-ledger recovery and catalyst/risk exclusion check; acceptance OPEN.

**PW-LSN-20261123-010 — full-universe candidate decision export missing**
- 1,032 base-universe symbols; +2% H+1 had 261 universe high-touch winners / 260 missed; +5% H+1 had 41 / 41 missed. Only one qualified candidate was retained; the other per-symbol decision/exclusion rows are absent.
- Root cause VERIFIED as a research evidence gap; individual causal reasons for remaining 255 +2% and 35 +5% cases stay UNKNOWN. Test: exactly 1,032 unique cutoff decisions, one status/reason per symbol, selected + excluded + missed counts reconcile to the same denominator; artifact daily_candidate_decision_20261123.csv plus denominator JSON; acceptance OPEN.

### Integration status
- Observation backlog additions: session-spine parity, exact forward-session labels, cutoff-anchored horizon maturity, and full-universe candidate decision export.
- Duplicate lessons excluded: no new IDs for the repeated holiday or forward-label defects; prior IDs updated.
- The six named missed-winner examples are incident samples, not the entire 260/41 set. Remaining cases stay UNKNOWN until the complete decision export exists.
- No threshold, selector, ranking, production code, trade assumption or admission changed.
- Next verification: offline session/date regression, approved label-v2 research test, and complete candidate decision denominator. All acceptance statuses OPEN / NOT_ACCEPTED.
