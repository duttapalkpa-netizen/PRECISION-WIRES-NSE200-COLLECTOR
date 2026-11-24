# PRECISION-WIRES V11.3 — Nightly Rotation Backtest & Research Performance Review
**তারিখ:** ২৪ নভেম্বর ২০২৬  
**অবস্থা:** PARTIAL — archive/label validation BLOCKED; কোনো performance PASS নয়  
**Phase:** Observation only; ₹0; free official sources only

## 1. Preflight ও reused evidence
Master Continuity Ledger C69 পর্যন্ত, ২৪-Nov Daily Unified Top-5 report, ২৩-Nov Nightly Review, ২৪-Nov Lessons Register, retained archive, latest workflow runs এবং artifact hashes পড়া হয়েছে। Accepted ZIP-byte checks পুনরাবৃত্তি করা হয়নি। ২৪-Nov NSE Capital Market holiday; next equity session ২৫-Nov. Official circular: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf

- **Run #421:** GitHub Actions ID \`45422367928\`; job \`138545045702\`; workflow conclusion SUCCESS; head commit \`7cf2292e467ffebf8c95ae67981570ab4d13a2ca\`; elapsed **12m06s** (15:10:17Z–15:22:23Z), 10-minute limit exceeded.
- **Artifact:** \`14936656169\`, \`precision-wires-adaptive-421\`, 62,184,126 bytes. GitHub digest and downloaded ZIP SHA-256 independently match: \`d57374c50a8b8e2fe5710fd57660225ea59a2beffd639cb9e83b77e734499954\`.
- Artifact contains 25 processed/output files; raw NSE CSVs and per-file raw manifest are absent. ZIP integrity PASS does not establish source provenance or semantic session coverage.

## 2. Ultimate 2% / 5% / 10% / 15% / 20% Stock-Capture Alert

| Target | Horizon | Fully validated historical unique hit / miss / eligible | Capture rate | 24-Nov morning cohort |
|---|---|---|---|---|
| +2% | H+1 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 selected; denominator 0; NOT_APPLICABLE |
| +5% | H+1 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 selected; denominator 0; NOT_APPLICABLE |
| +10% | H+3 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 selected; denominator 0; NOT_APPLICABLE |
| +15% | H+5 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 selected; denominator 0; NOT_APPLICABLE |
| +20% | H+5 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 selected; denominator 0; NOT_APPLICABLE |

২৪-Nov morning report-এ qualified Top-5 candidate **০**; market holiday এবং live 1m feed HTTP 403/zero rows। তাই denominator ০-কে 0% capture বলা হয়নি। Intraday high-touch, terminal close-to-close এবং executable trade win—সব historical target-এর জন্য UNKNOWN; executable win NOT_AUTHORIZED. ২৩-Nov shadow cohort (৭ unique symbols / ১০ selector rows) H+1 ২৫-Nov close, H+3 ২৭-Nov close, H+5 ০১-Dec close পর্যন্ত IMMATURE/PENDING.

আগের 2% 4/7 observation শুধু ১৯-Nov-এর নির্দিষ্ট shadow cohort-এর dated high-touch result; verified market-wide capture নয়। পুরোনো +5/+10/+20 diagnostics NOT_VALIDATED-ই থাকবে।

## 3. Run #421 archive semantic audit — গুরুত্বপূর্ণ নতুন finding

Processed dataset \`data/processed/nse_eq_200_sessions.csv\`:
- SHA-256: \`9f4f4305221a0b901a92088d22ffc5795614daeb2d6f78c013c78c6ec4f929f1\`
- 504,610 rows; 2,999 symbols; 200 DATE labels (১৮-Feb–২৪-Nov ২০২৬)।
- 200 labels-এর মধ্যে ১৩টি official NSE equity holiday date-এ আগের trading date-এর সঙ্গে সম্পূর্ণ একই processed values পাওয়া গেছে; প্রতিটি pair-এ symbol set এবং সব non-DATE columns 100% identical। ফলে মাত্র **187 unique daily content sessions**; 200 valid sessions নয়।

| Previous session | Duplicate holiday label | NSE holiday |
|---|---|---|
| 02-Mar | 03-Mar | Holi |
| 25-Mar | 26-Mar | Shri Ram Navami |
| 30-Mar | 31-Mar | Shri Mahavir Jayanti |
| 02-Apr | 03-Apr | Good Friday |
| 13-Apr | 14-Apr | Ambedkar Jayanti |
| 30-Apr | 01-May | Maharashtra Day |
| 27-May | 28-May | Bakri Id |
| 25-Jun | 26-Jun | Muharram |
| 11-Sep | 14-Sep | Ganesh Chaturthi |
| 01-Oct | 02-Oct | Gandhi Jayanti |
| 19-Oct | 20-Oct | Dussehra |
| 09-Nov | 10-Nov | Diwali-Balipratipada |
| 23-Nov | 24-Nov | Prakash Gurpurb Sri Guru Nanak Dev |

এগুলো official NSE 2026 holiday calendar-এর সঙ্গে মিলে যায়। Run #421 QA JSON তবুও \`PASS\` বলেছে: 200 raw file/session count ও 200 processed DATE labels গণনা করেছে; unique valid dates বা internal source DATE1 বনাম requested filename date যাচাই করেনি। QA JSON SHA-256 \`48547e28ff82e978c8b63712c9fc5e4692268c3c99fba015bd1bfa3d7bd1af19\`.

Code inspection at run head commit:
- \`pipeline/walk_forward_backtest.py\`, Git blob SHA-1 \`d085f7a2d35a88b4c4eaba65144a429a06961b09\`; previously independently recorded code SHA-256 \`dca7363ef1c5f56a097ed66b4305935f2c90975e2387b9c5b44780c4101f83e2\`. \`future_outcomes()\` still uses \`shift(-1).rolling(h,min_periods=1).max()\`: H+3/H+5 trailing/partial windows, not exact T+1…T+h; \`futclose\` also takes max future close rather than terminal T+h close.
- \`collector/nse_download.py\` blob SHA-1 \`1450b0ad5f577187c426f4be42cf9e65fce1d816\`; its full-delivery validator checks required columns/ranges but not requested stamp against source DATE1.
- \`collector/build_200_sessions.py\` blob SHA-1 \`a5677a5f3d8a32f20e2e97a6593269f1127eb1d8\`; it assigns DATE from filename.
- \`qa/validate_dataset.py\` blob SHA-1 \`35bc5d1961fe726ccb005751f4de1ce4d3b20ae5\`; it checks session-list length >=200 and duplicate SYMBOL+DATE, not unique semantic sessions or official holiday parity.

Therefore Run #421's \`qa_report.json PASS\` is **NOT ACCEPTED** for 200-session semantics. Do not use its labels for validated historical performance.

## 4. Three strictly separate performance tracks

| Track | Status | Evidence-based result |
|---|---|---|
| V11.4 Historical Behavioural Selector | **BLOCKED / NOT_VALIDATED** | 100 cutoffs, 3,000 Top-30 prediction rows, 1,109 unique selected symbols; full-universe file 252,656 rows / 2,902 symbols. Labels are contaminated by the proven forward-window defect and 13 duplicate holiday sessions. Metrics JSON has no confidence intervals. No Precision/Recall/F1/capture metric is admitted. |
| V11.3 Cost-aware Trade Replay | **UNKNOWN / NOT_AUTHORIZED** | No user-approved entry/exit/stop/circuit/position-sizing/overlap assumptions and no independently reconciled executable replay. Net return, win rate, expectancy, costs, profit factor and drawdown are not reported. |
| Global Capital Rotation | **UNKNOWN / BLOCKED** | One-day FII/DII snapshot only (23-Nov); GDELT returned 30 article titles but also a read-timeout; no synchronized vintage-aligned macro/sector/stock panel, defensible crosswalk or matured outcomes. |

Run #421's stored \`walk_forward_metrics.json\` SHA-256: \`ee6624f046bd910491eac0e94d90006200abb23576990b8d5570bb3ebc36d440\`. It contains point estimates but no CI fields; stored values remain audit-only and NOT_VALIDATED. H+5 reconciliation still fails: JSON precision 0.2096667 × 3,000 = **629** hits, while prediction CSV has **632** rows at/above +20% H+5 (3-row mismatch). Predictions CSV SHA-256 \`e80410b11cfaf8834af774c7e0e3ed39901efd5ce63b0ed2623dd5fef46a6951\`; universe probabilities SHA-256 \`356dc3329f28fb38e6cf6920f1564f3febf7b04f98dbe36dc4da887ca9bd96a9\`.

H+3 State calibration remains UNKNOWN: no independently verified fully matured per-State sample count; contaminated state rows (121 and 2,879) do not count toward the minimum 50.

## 5. Morning alert outcomes, comparability and failure audit

- ২৪-Nov morning report: NSE holiday, no fresh equity session, qualified candidates 0. Run #421 final status \`PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED\`; blocker \`LIVE_INTRADAY_1M_FEED_MISSING\`. Live status: HTTP 403, rows 0, symbols 0, captured_at \`2026-11-24T15:19:27.028758Z\`; market_open_observed=false. Status JSON SHA-256 \`75c656624a8d3b08a82fe51f9facd901510db4340c4e22f21d10b88bc76ae130\`; live status SHA-256 \`99d672afef7c63420164c5234d7561c99ae4a41156eee56589288eff60a007e9\`.
- No 24-Nov selected symbol matured; no new false-positive or missed-winner attribution. The 23-Nov seven-symbol shadow cohort remains pending at the dates above.
- Prior 20-Nov 1,032-symbol base-universe audit remains PARTIAL: +2% H+1 had 261 universe high-touch winners / 260 missed; +5% H+1 had 41 / 41 missed. Full point-in-time decision export is still absent; residual individual causes UNKNOWN.
- Prior Run #420 had 200 labels / 188 unique sessions / 12 holiday duplicates. Run #421 has 200 labels / 187 unique content sessions / 13 duplicate holiday pairs. This is not an improvement. Run #421 took 12m06s vs prior 12m11s: five seconds faster but still over the 10-minute cap.
- Fixed baseline/latest rolling percentage-point comparison is **NOT_AVAILABLE**: cutoff sets and archive versions differ, and both label/session integrity gates fail. No day-over-day performance improvement claim.
- Historical Best 3 per target (+2/+5/+10/+15/+20): **UNKNOWN/BLOCKED**. No verified historical winners or prospective candidates ranked. No stock is promoted from provisional Top-N.

## 6. Proven gaps and bounded next research actions

1. **Holiday-aware session-spine QA (offline, reuse artifact #14936656169).** Acceptance: all 13 holiday labels rejected as sessions; internal source DATE1/requested date parity; unique valid session count independently reconciled; QA must fail closed. Expected artifact: \`session_spine_semantic_audit_421.json\`. Blocker: raw source files/DATE1 manifest absent from this artifact; no new NSE acquisition until a permitted official archival route is established.
2. **Exact forward-label v2 correctness pilot — approval required before implementation.** Acceptance: five fully matured cutoffs; exact T+1…T+h exchange sessions; no partial horizon; missing session prevents maturity; high-touch and terminal T+h close labels separate; hand-check rows and no look-ahead. Expected artifact: \`forward_label_v2_correctness_pilot.json\`. Blocker: separate user approval and valid session spine.
3. **Canonical row-ledger reconciliation + missed-winner denominator export.** Acceptance: one row ledger generates JSON/CSV/summary with exact integer parity; unique-symbol and signal-row counts separate; full eligible-universe decision/exclusion row per symbol; cluster-bootstrap CI only after labels pass. Expected artifacts: \`h5_reconciliation.json\`, \`candidate_decision_ledger.csv\`, \`walk_forward_cluster_ci.json\`. Blocker: current label defect and missing decision export.

No new validation run was dispatched. The 120-minute prospective workflow was not run. No additional scope beyond these proven gaps.

## 7. Selection Failure & Missed-Winner Root-Cause Audit
২৪-Nov-এ selected stock নেই; therefore today's false-positive count, missed-winner count and cause attribution are UNKNOWN/NOT_APPLICABLE, not zero-performance claims. Previous same-universe 20-Nov missed-winner audit remains PARTIAL as documented; no hindsight cause was promoted. No selector threshold, code or production change.

## 8. আজকের শিক্ষা ও গবেষণায় সংযোজন

- Existing \`PW-LSN-20261121-001\` updated, not duplicated: Run #421 source still has trailing/partial H+3/H+5 label windows; close outcome is rolling maximum, not terminal T+h close.
- Existing \`PW-LSN-20261121-002\` updated: H+5 JSON 629 vs prediction CSV 632; reconciliation OPEN.
- Existing \`PW-LSN-20261123-001\` updated: 13 exact holiday duplicate date pairs, 187 unique daily content dates; QA false PASS confirmed.
- Existing \`PW-LSN-20261124-001\` updated: Run #421 runtime 12m06s still exceeds 10-minute target.
- Existing \`PW-LSN-20261124-002\` updated: live feed HTTP 403 / zero rows; final selection remains blocked; GCR independently blocked by missing synchronized panel.
- Existing \`PW-LSN-20261124-003\` carried forward; no new matured high-touch/close divergence observation today.
- New immutable lesson **\`PW-LSN-20261124-004\`**: walk-forward metrics artifact omits confidence intervals and explicit unique-symbol/row-denominator reconciliation; root cause VERIFIED from artifact schema. Acceptance OPEN: emit cutoff-cluster CI, eligible/matured/excluded counts, unique symbols, signal rows, and canonical row-ledger parity.
- Research note added to Observation-only diagnostic backlog: metrics evidence contract for CIs and unique-symbol/row reconciliation. All acceptance tests OPEN / NOT_ACCEPTED.
- Duplicate lessons excluded: no new ID for the same holiday-spine or forward-label defect.
- Next verification: session-spine offline audit; after separate approval only, exact label pilot; then canonical H+5 parity and candidate-decision export.

## 9. Invariants and final acceptance
- Artifact ZIP hash integrity: PASS (downloaded and independently recomputed).
- 200 unique valid session claim: NOT_ACCEPTED (187 unique daily content sessions only).
- V11.4: NOT_VALIDATED; no confidence interval or verified capture score.
- V11.3 replay: UNKNOWN / NOT_AUTHORIZED.
- GCR: UNKNOWN / BLOCKED.
- Best-3: UNKNOWN/BLOCKED.
- Today's qualified candidates: 0; no matured alert outcome.
- ₹0; official/free sources only; no synthetic data, forward-fill, guessed mappings, fabricated timestamps or look-ahead.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged.
- UNKNOWN is never PASS.
