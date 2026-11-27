# PRECISION-WIRES V11.3 — Failure & Lessons Learned
## ২৭ নভেম্বর ২০২৬ — Run #412 evidence addendum

**Scope:** Morning pre-market review, 26-Nov-2026 cutoff → 27-Nov-2026 next session. Observation-only; ₹0; no production change.

## 1. Evidence provenance

- Run #412: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45890145641
- Job 140150511665: SUCCESS; 7m38s.
- Artifact 15151761186: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45890145641/artifacts/15151761186
- Independently downloaded ZIP SHA-256 = GitHub artifact digest:
  `a5cd5ed868a3f66d9ea0cd43ca03b7fea2e5cd4ebc3b5f83e3c28fc6fdd3ca5a`.
- Artifact contains 17 files; watchlist_ledger.csv = 350 rows / 17 columns; latest_picks.csv = 10 signal rows / 7 unique symbols for 26-Nov cutoff.
- QA summary says 200 raw files / 200 dates / 3,009 symbols / 100% delivery; raw per-file source manifest, requested DATE ↔ internal DATE1 parity and point-in-time universe decision ledger are absent. 200 valid distinct sessions remain NOT_ACCEPTED.
- Retrospective reproducibility check is byte-for-byte PASS for the repeated outputs, not label/session correctness.

## 2. Existing immutable lesson PW-LSN-20261125-001 — calendar-aware maturity / OUTCOME_LAST_DATE

**New evidence (27-Nov review):**
- 23-Nov cutoff: 10 signal rows / 7 unique symbols. Run #412 marked T1 mature on 10 rows and T3 mature on 9 rows while OUTCOME_LAST_DATE remained blank. Official calendar says H+1=25-Nov and H+3=27-Nov; artifact created on 26-Nov, so T3 maturity was premature.
- 24-Nov cutoff: 10 rows / 9 unique symbols despite 24-Nov being an official NSE equity holiday. This cohort is invalid and must not enter maturity/denominator calculations.
- 25-Nov cutoff: 10 rows / 7 unique symbols; T1 marked mature on all 10 rows, but OUTCOME_LAST_DATE blank. H+1=26-Nov; without exact raw row/date linkage the result remains PENDING / NOT_VERIFIED.
- 26-Nov cutoff: 10 rows / 7 unique symbols; T1/T3/T5 immature. Expected H+1=27-Nov close, H+3=01-Dec, H+5=03-Dec.

**Root cause:** VERIFIED at tracker/contract level in prior audit: maturity derives from the next sorted row rather than the official exchange-session spine, and horizon end date is not persisted. Individual return impact remains UNKNOWN.

**Why not caught:** maturity flags are accepted without checking exact official session date and OUTCOME_LAST_DATE; QA checks schema/counts but not exchange calendar semantics.

**Research question:** Does every matured signal resolve to the exact H+1/H+3/H+5 official trading session and an independently verified source row?

**Bounded free-official-source test:** Offline test retained artifacts only; compare each cutoff with NSE official calendar, require exact expected horizon date and non-empty OUTCOME_LAST_DATE, reject holiday, duplicate, missing, forward-filled or non-session rows. No new NSE bulk acquisition.

**Leakage-safe validation:** Test all retained holiday-adjacent and missing-session examples before any future holdout; minimum 50 fully matured observations per State remains unchanged.

**Acceptance:** zero holiday-as-session labels; exact end-date parity for all matured rows; no premature T3/H5 maturity; separate high-touch, close-to-close and executable outcomes. Expected artifact: `calendar_aware_tracker_regression.json`.

**Confidence:** tracker defect HIGH; stock-level impact UNKNOWN. **Status:** OPEN. Carry forward to morning and nightly checks.

## 3. Existing immutable lesson PW-LSN-20261126-001 — raw percentile is not risk-qualified admission

**New evidence (27-Nov review):**
- Run #412 latest_picks.csv: 10 selector rows / 7 unique symbols: SHALPAINTS, SAKUMA, EBIX, NGIL, ARIS, ONIXSOLAR, AIROLAM.
- Scores are percentile ranks, not calibrated probabilities. latest_picks.csv has no current official close/time, official catalyst timestamp, sector/relative-strength, liquidity, ASM/GSM/price-band/margin or final admission evidence.
- Official NSE ASM page lists AIROLAM as STASM-I and ONIXSOLAR as LTASM-I.
- Official NSE SAKUMA board-outcome filing dated 25-Nov-2026 reports withdrawal/cancellation of proposed 65-crore-share preferential issue because proposed allottees were unwilling/unable to subscribe; the 28-Nov adjourned EGM was cancelled.
- Official NSE SHALPAINTS quote page's latest accessible indexed quote remained 20-Nov close ₹97.42; no fresh 26-Nov official price/time was captured in this audit.

**Root cause:** VERIFIED at code/schema level in the prior audit: raw model output does not join the required current official risk and freshness fields. Predictive impact UNKNOWN.

**Why not caught:** percentile ranking can be mistaken for final candidate rank if the independent admission gate is skipped.

**Research question:** Can every raw lead be independently reconciled against official identity, fresh quote, price-volume/RS, sector, liquidity, catalyst timestamp and surveillance before admission?

**Bounded test:** Reuse Run #412 latest_picks; join official NSE security identity, quote, ASM/GSM/price-band/margin, and dated filing references at the original cutoff. Missing/stale fields remain UNKNOWN and do not fill a candidate slot.

**Leakage-safe validation:** cutoff-only source timestamps; no post-cutoff price/news; no single-event production inference; minimum 50 matured observations per State unchanged.

**Acceptance:** 100% identity/current-price/risk-field reconciliation; percentile never labelled probability; no production code, threshold, ranking or admission change. Expected artifact: `prospective_risk_gate_admission_audit.json`.

**Confidence:** code/schema gap HIGH; predictive impact UNKNOWN. **Status:** OPEN. Carry forward.

## 4. Full-universe missed-winner audit — blocked

- Exact missing data: 26-Nov cutoff's full eligible NSE equity universe point-in-time inclusion/exclusion ledger, per-symbol filter trace, and accepted official EOD high/close/corporate-action rows for subsequent H+1/H+3/H+5 sessions.
- Current 26-Nov cohort is not mature at 27-Nov pre-market. Previous cohorts have blank outcome-end dates or calendar-invalid maturity flags.
- Do not report zero missed winners; missed-winner count, root cause and CORE-672 filter attribution remain UNKNOWN/BLOCKED.

Expected bounded artifacts:
1. `point_in_time_decision_ledger_audit.json`
2. `universe_missed_winner_reconciliation.json`
3. `missed_winner_root_cause_audit.json`

Each job ≤10 minutes; reuse retained evidence. Decision trace absent → filter attribution UNKNOWN.

## 5. Next-day carry-forward checklist

1. Calendar-aware maturity regression; exact H+1/H+3/H+5 dates and OUTCOME_LAST_DATE.
2. Full-universe decision ledger and unique-symbol/signal-row parity.
3. Official raw EOD provenance, DATE1/requested-date parity and corporate-action validation.
4. Prospective risk-gate admission audit for all 26-Nov raw leads.
5. Keep target-wise Best-3 UNKNOWN until independently verified stock-level matured outcomes and sufficient sample/consistency exist.
6. Keep A exploratory, B UNKNOWN/NOT_AUTHORIZED, C UNKNOWN/BLOCKED.
7. No production/selector/ranking/threshold change without repeated leakage-safe out-of-sample evidence and separate user approval.

## 6. আজকের শিক্ষা → গবেষণায় সংযোজন → পরবর্তী যাচাই

**আজকের শিক্ষা:** premature maturity flags and raw percentile leads remain unsafe for accepted forecast/admission decisions.

**গবেষণায় সংযোজন:** append Run #412 evidence to PW-LSN-20261125-001 and PW-LSN-20261126-001; no duplicate lesson ID and no new predictive lesson.

**পরবর্তী যাচাই:** calendar-aware tracker regression → point-in-time decision ledger → full-universe reconciliation → prospective risk-gate admission audit.
