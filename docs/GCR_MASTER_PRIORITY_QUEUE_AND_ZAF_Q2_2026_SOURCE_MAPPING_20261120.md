# GCR Master Priority Queue & South Africa Q2-2026 Portfolio Mapping Check
Date: 2026-11-20
Purpose: enforce dependency-ordered execution; complete one bounded highest-value country-validation task.

## A. Continuity preflight — completed before selection
Master ledger fetched at blob SHA `ce94bbcfcfd080685e21c483260a93d6d2d60434`; the relevant prior reports were reopened:
- IMF BOP public observation pilot and separate Global Registry DSD 2.6.0 capture.
- 154-member WEO EMDE panel and 12-country exact-key cross-check.
- 63-country 2026-Q2 synchronous dual-leg cohort.
- Brazil/India scale-sign checks; Chile vintage review; Nigeria 6/6 national comparison.
- SARB South Africa Parts 3–5; CDSL/NSDL raw capture and CDSL sector arithmetic QA.
- BSE and NSE TRI rights gates.
- Brazil PA transaction-2 / Changelog probes and 40-event Registration lifecycle.

### PASS work rejected from repeat
- IMF BOP DSD V2.6.0 SDMX-ML 2.1/3.0 raw capture and XML parse: already PASS (run 44473409770; artifact 14505177819); do not recapture.
- IMF public BOP observation capture, WEO G200 154-member roster, 12-country exact-key comparison, and 9,299-row panel structural QA: already PASS; do not rebuild.
- Brazil Registration URN 40/40 lifecycle and BCB SGS raw captures/accounting identities: already PASS; do not repeat.
- Brazil BOP6 vs BOP_BPM6 PA/payload mismatch: already confirmed BLOCKED after identical public probes returned HTTP 500; no repeated probes. Only authorized owner-side PA history/correction can close it.
- India RBI Table 197 and Table 42 work: reuse existing; India Q1-2026 liability remains REVIEW.
- CDSL 15-Nov-2026 sector HTML capture and 192/192 component arithmetic: already PASS; grand totals remain REVIEW. Do not recapture or rerun arithmetic.
- BSE/NSE TRI rights gates: already reviewed; no repeated route or rights searches absent new terms/licence evidence.
- MoSPI IIP/CPI/GDP/PLFS audit: prior Part 3 was duplicate; excluded.

## B. Dependency-ordered master priority queue
Priority is based on (i) how many downstream tasks a gate unlocks, (ii) whether evidence can be obtained from an official free source, (iii) whether it blocks an entire workstream, and (iv) whether the next action is executable without external credentials or paid access.

| Rank | Work package | Current state | Why this order | Next action |
|---:|---|---|---|---|
| 1 | 63-country EMDE national-source scale/sign/vintage validation | PARTIAL; 124/124 matched comparisons across five countries, but not universal | Direct prerequisite for a defensible EMDE aggregate; advances the core GCR capital-flow factor | Continue one country at a time from the existing 2026-Q2 dual-leg cohort, starting with large members where official national source is available |
| 2 | Brazil PA/Dataflow identity and historical Changelog | BLOCKED / external owner dependency | Critical Brazil Reconstruction blocker, but public tx2 formats already exhausted; repeated public retries have near-zero expected value | Await authorized owner-side PA history/export or official correction/exception; no repeat endpoint probes |
| 3 | India FPI/DII daily flow lineage and NSDL/CDSL matched-date confirmation | PARTIAL / NOT_DONE | Needed to connect global flows to India market response; raw page capture exists, but archive and status semantics incomplete | Parse existing CDSL raw archive/sector file and complete a bounded NSDL Archive postback only through documented public UI controls |
| 4 | Global macro daily synchronized panel (rates, FX, USD, volatility, energy) | PARTIAL | Needed for matched-time push/pull factors after the core flow definitions are stable | Reuse archived source captures; close one source family and its timestamp/vintage QA at a time |
| 5 | Benchmark/sector TRI and taxonomy bridge | BLOCKED by source rights or mapping | Needed for sector-return transmission, but both BSE and NSE index licensing pages do not establish free database/derived-data rights | Keep excluded unless exact official licence/permission appears; do not proxy with PR indices |
| 6 | Relative-attraction formula, sector transmission, event study and rolling OOS backtest | NOT_DONE / NOT_AUTHORIZED | Depends on 1, 3, 4, 5 and synchronized matured observations | Do not start before upstream source/rights/missingness gates pass |
| 7 | Production integration / weights / trade alert changes | NOT_AUTHORIZED | Last step only after independent OOS evidence and user approval | No change without explicit approval |

**Execution rule:** finish the current ranked task to its acceptance boundary, record exact status and evidence, then move to the next rank. Do not jump between unrelated workstreams unless a higher-ranked item becomes externally blocked.

## C. Selected task — South Africa (ZAF), 2026-Q2
Why selected: ZAF is one of the existing 63 countries with both IMF panel legs present for 2026-Q2; official SARB September-2026 statistical tables are now directly accessible as a PDF even though the previously identified ZIP archive fetch timed out. This gives a free official route to validate the national labels, values, units and signs without rebuilding the cohort or re-downloading the IMF panel.

### Official SARB source
- September 2026 Quarterly Bulletin statistical tables, attachment 8: https://www.resbank.co.za/content/dam/sarb/publications/quarterly-bulletins/quarterly-bulletin-publications/2026/september/8-tables-external-economic-accounts.pdf
- Bulletin issue date: 29 September 2026.
- Table: Balance of payments, quarterly figures, page S-87 / PDF page 3.
- Unit: R millions.
- Q2-2026 is the final 2026 column in the quarterly table.

### Official code and concept mapping
- Portfolio investment, net incurrence of liabilities: code 5644K; Q2-2026 = **-9,023 R million**.
  - Equity and investment fund shares: 5756K = -34,161.
  - Debt securities: 5757K = +25,138.
  - Components sum exactly: -34,161 + 25,138 = -9,023.
- Portfolio investment, net acquisition of financial assets: code 5660K; Q2-2026 = **-68,769 R million**.
  - Equity and investment fund shares: 5758K = -42,915.
  - Debt securities: 5759K = -25,854.
  - Components sum exactly: -42,915 + -25,854 = -68,769.
- These totals correspond conceptually to IMF BOP entries L_NIL_T (liabilities) and A_NFA_T (assets), subject to the explicit portfolio-investment scope and vintage match. The four subcomponents are not substituted for the total lines.
- SARB table note 4 explicitly defines sign conventions: positive net incurrence of liabilities = capital inflow; negative = disposal/outflow. Negative net acquisition of assets = outflow. Positive net disposal of assets = inflow.
- Q2 values therefore indicate both portfolio-liability disposal/outflow and resident net acquisition of foreign assets/outflow. Do not net or combine these legs in this source gate.

### Independent corroboration and boundary
- SARB September 2026 bulletin narrative states Q2 net portfolio investment was an outflow and that the financial-account net capital flow was an inflow of R1.9bn overall. This is consistent with the negative portfolio legs, but the total financial-account net flow is not a substitute for either portfolio leg.
- The bulletin table explicitly says data for the previous four years are preliminary and subject to revision. Preserve this as the SARB publication vintage; do not imply finality.
- This report establishes official labels, codes, unit, Q2 values, subcomponent arithmetic and sign semantics. It does **not** yet complete an exact numeric comparison to the IMF panel because the IMF raw ZAF Q2 row and its API retrieval receipt were not re-opened in this bounded task. No ZAR/USD conversion was attempted.
- The Q2 cohort and source coverage matrix are reused; no IMF panel, 154-member roster, or historical dataset was rebuilt.

## D. Acceptance result
| Gate | Status |
|---|---|
| ZAF is in existing 2026-Q2 both-leg cohort | PASS |
| Official SARB Q2-2026 BOP table retrieved/read | PASS |
| Exact portfolio liability/asset labels and codes | PASS |
| Q2-2026 values and R million unit | PASS |
| Liability subcomponent sum (5756K+5757K=5644K) | PASS |
| Asset subcomponent sum (5758K+5759K=5660K) | PASS |
| Official sign convention | PASS |
| SARB vintage/revision caveat recorded | PASS |
| Exact numeric IMF↔SARB value/FX reconciliation | NOT_DONE |
| ZAF full national-source validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## E. Next exact action in rank order
1. Retrieve the exact ZAF Q2-2026 rows from the already archived IMF raw panel/exact-key artifact and independently match them to the SARB Q2 values using a documented quarterly ZAR/USD conversion series/vintage, or compare to an official SARB USD-denominated equivalent if present.
2. Preserve both original currencies and units; do not convert without an exact dated official rate and a defined quarterly convention.
3. If this reconciliation passes, mark ZAF's Q2 source-validation status accordingly and advance to the next highest-weight unvalidated member of the same 63-country cohort. Do not aggregate until each included country has both legs, aligned vintages, verified units/signs and the pre-registered coverage rule.
4. If the exact IMF raw row or compatible FX vintage cannot be recovered, keep the value comparison NOT_DONE and move to the next executable country only after documenting the blocker.

## F. Protected invariants
No production code, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, model weights or trade gates changed. No paid API, synthetic data, fabricated timestamp, silent FX conversion, access-control bypass, or repeated completed audit. UNKNOWN is never PASS.


## G. ZAF Q2-2026 numeric reconciliation update (2026-11-20)
- New detail report: `docs/GCR_ZAF_Q2_2026_IMF_SARB_OECD_FX_RECONCILIATION_20261120.md`.
- Existing exact-key IMF receipt reused: run 44474458684 / artifact 14505009889 / ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`.
- ZAF A_NFA_T Q2-2026 = +4,174,854,099.360882 USD; L_NIL_T = -547,771,649.1229077 USD. Exact raw file hashes and timestamps are recorded in the detail report.
- SARB Q2 values: assets -R68,769m; liabilities -R9,023m. Official quarterly FX comparator: OECD Main Economic Indicators, Q2-2026 average daily rate 16.4719712481963 ZAR/USD; 2026-08-17 release vintage (FRED/ALFRED mirror, source OECD).
- Liability leg: SARB converted -547.779003742 USDm vs IMF -547.771649123 USDm; residual +0.007354619 USDm; PASS within strict SARB integer-R-million half-unit bound (~0.0304 USDm).
- Asset leg: after the explicit sign reversal required by SARB note 4, SARB +4,174.910152756 USDm vs IMF +4,174.854099361 USDm; residual -0.056053395 USDm, outside the strict ~0.0304 USDm bound; REVIEW, not PASS.
- ZAF national dual-leg comparison remains PARTIAL / NOT PASS. 63-country aggregate remains NOT_AUTHORIZED. Do not widen tolerance, net the legs, or infer a cause for the asset residual.
- Rank-1 country validation package remains open. Next country must be selected from the existing 63-country Q2 both-leg cohort by GDP/market relevance and official source accessibility; do not rebuild cohort. Investigate ZAF residual only if a more exact official FX/conversion convention is identified.


## H. Next country validation — China (CHN), Q2-2026 (2026-11-20)
- CHN selected from the existing 63-country Q2 both-leg cohort: large EMDE market, both IMF entries present through 2026-Q2, official SAFE USD BOP release available. Existing 12-country exact-key receipt reused; no cohort/panel rebuild.
- SAFE official Q2 release 29-Sep-2026 (index 000014453-2026-0068), USD 100m units: portfolio assets -488 (= -USD48.8bn), liabilities +433 (= +USD43.3bn), total portfolio investment -55 (= -USD5.5bn); -488 + 433 = -55.
- IMF exact Q2 raw values: A_NFA_T +USD48.794459bn; L_NIL_T +USD43.286601bn. Absolute residuals are USD5.540896m (assets) and USD13.399286m (liabilities), both within SAFE's ±USD50m half-unit display-rounding bound.
- Liability signed/magnitude comparison is consistent at rounded precision. Asset magnitude corroborates but sign differs (SAFE negative, IMF positive); no sign reversal is authorized without an exact source concept/sign crosswalk. CHN remains PARTIAL / NOT PASS.
- Detail report: `docs/GCR_CHINA_CHN_Q2_2026_SAFE_IMF_BOP_COMPARISON_20261120.md`.
- Next exact action: official SAFE detailed time-series BOP download and metadata/version for asset sign; do not substitute IIP stock values for BOP flow. If inaccessible, preserve PARTIAL and advance within the same fixed cohort.


## I. CHN SAFE detailed workbook access boundary (2026-11-20)
- Official SAFE navigation path found: Data and Statistics → Balance of Payments → dated “The time-series data of Balance of Payments of China” (dispatch 2026-09-29, index 000014453-2019-0016).
- Exact XLSX locator: https://www.safe.gov.cn/en/file/file/20260929/20c1e5e45d704a77b302ba234211a75b.xlsx. Browser content extraction rejected the XLSX MIME type; direct byte download failed in this environment. No workbook hash/content/row mapping is claimed.
- CHN sign-mapping blocker is now specifically narrowed to XLSX byte retrieval and inspection, not absence of an official source. Detailed audit: `docs/GCR_CHINA_CHN_SAFE_DETAILED_BOP_TIME_SERIES_ACCESS_AUDIT_20261120.md`.
- CHN remains PARTIAL / NOT PASS; no silent sign flip. Resume only by retrieving/hash/inspecting this exact workbook via a supported owner-side browser/workflow route, then compare detailed Q2 portfolio transactions to existing IMF raw exact rows. Do not substitute IIP stocks or cumulative Q3 data.


## J. Next cohort country validation — Indonesia IDN Q2-2026 (2026-11-20)
- IDN selected from the existing 63-country Q2 both-leg cohort; reused the existing 12-country exact-key receipt (run 44474458684 / artifact 14505009889); no new IMF request or panel rebuild.
- Bank Indonesia SEKI Table V.7, Q2** 2026 (Very Temporary Data), USDm: portfolio assets -1,488; liabilities +11,440; total +9,953.
- IMF raw Q2 values (SCALE=6): A_NFA_T +1,487.605237 USDm; L_NIL_T +11,440.221642 USDm. Both absolute residuals fall within ±0.5 USDm BI whole-million rounding.
- Liability signed/magnitude comparison PASS (IMF−BI +0.221642 USDm). Asset magnitude residual 0.394763 USDm is within rounding but sign conflicts (BI negative, IMF positive); no sign reversal authorized. IDN remains PARTIAL / NOT PASS.
- Detail report: `docs/GCR_INDONESIA_IDN_Q2_2026_IMF_BANK_INDONESIA_BOP_RECONCILIATION_20261120.md`.
- Next exact action: source an official BI concept/sign methodology and revision-vintage bridge for the asset leg; do not infer mapping from total financial account or IIP stocks. If unresolved, advance to next eligible cohort member while preserving IDN PARTIAL.


## K. IDN BI official asset-sign crosswalk and Q2-2026 numerical recheck (2026-11-20)
- Official BI BPM6 implementation note confirms the BPM5 +/- convention was retained; footnote 4 states financial inflow (asset reduction/liability increase) is positive and outflow (asset increase/liability reduction) negative. BI BOP metadata defines portfolio assets as resident acquisition of nonresident securities and liabilities as nonresident acquisition of resident securities, and explicitly says BI capital/financial asset/liability entries are shown as net inflow/outflow (+ inflow/credit, − outflow/debit).
- Thus BI portfolio asset sign must be inverted for comparison with IMF A_NFA_T net acquisition; liability sign is retained for L_NIL_T. This is an official BI methodology-based country-specific mapping, not a fitted sign flip.
- BI Q2** 2026 table values USDm: assets -1,488 → mapped +1,488; liabilities +11,440 → retained +11,440. IMF exact values USDm: A_NFA_T +1,487.605237; L_NIL_T +11,440.221642. Residuals -0.394763 and +0.221642 USDm respectively; both PASS within ±0.5 USDm whole-million display rounding.
- BI Q2 report publication 2026-08-21, page update 2026-09-17; Q2 is marked ** Very Temporary Data. Exact BI↔IMF same-vintage alignment remains REVIEW / NOT_ESTABLISHED. Therefore IDN sign mapping + rounded numeric checks PASS, but full country validation remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: `docs/GCR_INDONESIA_IDN_BPM5_SIGN_CONVENTION_CROSSWALK_AND_Q2_2026_RECHECK_20261120.md`. Next action: locate dated BI Q2 revision snapshot/vintage bridge; if unavailable, preserve limitation and move to next eligible cohort member.


## L. Next cohort country validation — Saudi Arabia SAU Q2-2026 (2026-11-20)
- SAU selected from the fixed 63-country Q2 both-leg cohort after IDN sign crosswalk was resolved but exact BI↔IMF vintage alignment remained REVIEW. Reused existing IMF 12-country exact-key artifact 14505009889; no new IMF GET or cohort rebuild.
- SAMA September 2026 Monthly Statistical Bulletin, Table 1 BOP, Contd.6, PDF/printed p.131, USDm, Q2-2026 marked e (Estimated): portfolio asset net acquisition +9,664; portfolio liability net incurrence +6,381; portfolio balance +3,283 (9,664−6,381).
- IMF raw Q2 values (SCALE=6): A_NFA_T +9,663.782086 USDm; L_NIL_T +6,381.234539 USDm. Residuals -0.217914 and +0.234539 USDm; both within ±0.5 USDm whole-million display rounding. Concept labels and signs match; both numerical legs PASS without sign transform.
- SAMA's Q2 values are explicitly estimated (e). IMF receipt retrieved 2026-11-19; exact source-vintage identity is not established. SAU full national validation remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: `docs/GCR_SAUDI_ARABIA_SAU_Q2_2026_SAMA_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md` (identity notation corrected in commit a32bf6e06ef15f2973128582b151f66f9f9b4d42).
- Next exact action: seek dated SAMA Q2 estimate revision archive or subsequent revised observation; if no public versioned source exists, retain SAU PARTIAL and advance within fixed cohort.


## M. SAU Q2-2026 source-vintage follow-up (2026-11-20)
- SAMA calendar lists the October 2026 bulletin for 29-Oct-2026 and November 2026 bulletin for 29-Nov-2026. The latest available September 2026 bulletin still marks Q2-2026 portfolio rows as e = Estimate.
- IMF DSBB metadata gives a general BOP revision practice of usually three months after reference quarter; it does not prove that the specific Q2-2026 portfolio legs have been revised. No dated public revised Q2 asset/liability observation or same-vintage bridge was found in the official material inspected.
- Preserve existing numeric asset/liability PASS at published rounding, but same-vintage NOT_ESTABLISHED; SAU remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_SAUDI_ARABIA_SAU_Q2_2026_SOURCE_VINTAGE_FOLLOWUP_AUDIT_20261120.md.
- Next: advance to the next eligible country in the fixed 63-country cohort using existing exact-key IMF receipt. Do not repeat SAU extraction, issue duplicate IMF GETs or rebuild the cohort.


## N. Next cohort source gate — Poland POL Q2-2026 (2026-11-20)
- POL selected from existing IMF 12-country exact-key sample; no new IMF GET or cohort rebuild. Existing artifact 14505009889 reused.
- IMF Q2-2026 exact values: A_NFA_T +USD6,602m; L_NIL_T +USD19,391m. Raw CSV SHA-256 values recorded in detail report.
- NBP official quarterly workbook bop_q.xlsx is linked from its BOP PDF, but workbook retrieval/content inspection/hash remain BLOCKED. The linked PDF's narrative front matter (March 2026, 15-May-2026, April release 12-Jun-2026) conflicts with later table columns showing Q2/Q3 2026. Candidate table values are quarantined, not used.
- POL national comparisons NOT_DONE; full dual-leg validation BLOCKED; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_POLAND_POL_Q2_2026_NBP_IMF_SOURCE_GATE_AUDIT_20261120.md.
- Next: retrieve and inspect exact NBP workbook via supported route; otherwise advance to next eligible country in fixed cohort. No duplicate IMF query or cohort rebuild.
