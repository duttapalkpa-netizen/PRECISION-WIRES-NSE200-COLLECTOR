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


## O. Next cohort validation — Türkiye TUR Q2-2026 (2026-11-20)
- Reused existing IMF exact-key receipt; no new IMF GET or cohort rebuild. TUR Q2 IMF: A_NFA_T +USD5,749m; L_NIL_T +USD9,270m. Both exact series 46/46 broad-key matched.
- TCMB September 2026 monthly detailed BOP table aggregated Apr–Jun: portfolio assets 2,368+1,266+2,115 = USD5,749m; liabilities 6,334−1,802+4,651 = USD9,183m. Asset leg matches at displayed precision; liability residual +USD87m (IMF−TCMB), beyond rounding.
- TCMB's revision policy allows current and previous year monthly data to be revised with monthly releases. Exact September ZIP bytes/hash/revision metadata not inspected; same-vintage link unestablished. Do not attribute residual to revision without exact vintage evidence.
- TUR remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_TURKIYE_TUR_Q2_2026_TCMB_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md.
- Next: retrieve/hash/inspect TCMB September 2026 ZIP and revision metadata via supported route; no new IMF query/cohort rebuild.


## P. TUR TCMB August–September PDF vintage cross-check (2026-11-20)
- Official TCMB August 2026 and September 2026 PDFs independently show identical Q2 monthly portfolio assets 2,368 / 1,266 / 2,115 USDm and liabilities 6,334 / -1,802 / 4,651 USDm.
- Both snapshots sum to Q2 assets 5,749 USDm and liabilities 9,183 USDm. Existing IMF Q2 values are 5,749 and 9,270 USDm; asset residual 0, liability residual +87 USDm. No Q2 liability revision is observed between these two PDF snapshots.
- Limited two-snapshot comparison only; not a full revision history or same-vintage proof. September ZIP raw bytes/hash/revision metadata remain NOT_INSPECTED. TUR remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_TURKIYE_TUR_Q2_2026_TCMB_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md.
- Next: retrieve and inspect official TCMB September ZIP; otherwise preserve blocker and advance cohort.


## Q. Next cohort validation — Mexico MEX Q2-2026 (2026-11-20)
- Reused existing IMF exact-key sample/artifact 14505009889; no new IMF request or cohort rebuild. MEX Q2 IMF: A_NFA_T +USD8,937.255098m; L_NIL_T +USD10,561.285114m. Raw CSV SHA-256 values in detail report.
- Official Banxico Q2 report dated 25-Aug-2026, Cuadro 3 (USDm): portfolio asset net acquisition +8,937; liability net incurrence +10,561; net portfolio investment -1,624. Residuals vs IMF: +0.255098 and +0.285114 USDm; both within ±0.5 USDm whole-million rounding.
- Banxico states BOP components may be revised in future releases. Exact same-vintage Banxico↔IMF bridge not established. MEX numeric legs PASS; full national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md. Next: seek versioned Q2 vintage/revision evidence; otherwise preserve PARTIAL and advance cohort.


## R. MEX Banxico live SIE CE174 cross-check (2026-11-20)
- Official Banxico SIE CE174 current quarterly BPM6 table, USDm, latest period Apr–Jun 2026, reports portfolio balance -1,624, asset net acquisition +8,937 and liability net incurrence +10,561. The table is explicitly preliminary and subject to revisions.
- Current live SIE values match the 25-Aug-2026 Q2 release at whole-million precision. This is a second official publication surface, not a historical vintage log; exact IMF↔Banxico vintage identity remains NOT_ESTABLISHED.
- MEX numeric legs PASS; full validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md.


## S. Argentina ARG Q2-2026 INDEC validation (2026-11-20)
- Selected ARG from existing 12-country IMF exact-key archive after preflight; no new IMF request/panel rebuild. Reused run 44474458684, artifact 14505009889, ZIP SHA-256 588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7.
- Official INDEC Q2 report dated 29-Sep-2026, Table I.13: ANAF (financial asset net acquisition) +2,230 USDm; ENP (liability net issuance) +7,041 USDm; portfolio balance -4,811 USDm. Existing IMF exact values +2,230.206322 and +7,041.052824 USDm; residuals +0.206322 and +0.052824, both within ±0.5 USDm.
- INDEC says Q2 provisional/revisable; release-comparison annex covers only through Q1 2026, not Q2 vintage. Same-vintage NOT_ESTABLISHED; ARG PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_ARGENTINA_ARG_Q2_2026_INDEC_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md. Next: locate versioned INDEC Q2 source vintage or advance cohort.


## T. Bangladesh BGD Q2-2026 national portfolio source gate (2026-11-20)
- Reused existing IMF exact-key receipt; no new IMF query/rebuild. IMF Q2 A_NFA_T=0 USD; L_NIL_T=-113.334678 USDm.
- Bangladesh Bank Quarterly Vol XXIII No.4 Table V.1 gives FY26 Q4 (Apr-Jun 2026) portfolio investment net -109 USDm. It does not split portfolio asset net acquisition and liability net incurrence; no national sign/concept bridge or vintage identity established.
- BGD dual-leg validation BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md.


## U. Bangladesh Bank NSDP BOP SDMX route discovery (2026-11-20)
- Official NSDP page confirms BOP Browse Data, SDMX download and DSBB metadata routes. Direct links: `https://www.bb.org.bd/econdata/nsdp/browsefile/bpm6_bgd.xls`, `https://www.bb.org.bd/econdata/nsdp/xml/bgd/bop6_bgd.xml`, alternate `https://www.bb.org.bd/econdata/nsdp/xml/bgd/bopanltcl_bgd.xml`.
- MIME handling blocked raw XLS/XML inspection; no hashes, observations, series keys or vintage attributes. Route discovery PASS; actual capture NOT_DONE. BGD remains BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md. Next: supported byte-preserving retrieval then inspect structure before extracting values.


## V. Bangladesh historical portfolio component/sign crosswalk (2026-11-20)
- Official Bangladesh Bank Annual 2024–25 BOP & IIP, Table 11 (million BDT), separately reports portfolio net/assets/liabilities by quarter. FY25 Q4: net +3,996; assets 0; liabilities -3,996; accounting identity net = assets − liabilities. FY25 annual: net +16,765; assets 0; liabilities -16,765.
- Methodology describes credit/debit treatment and supports historical country sign crosswalk. This is FY25 historical evidence, not the FY26 Q4 observation. No value carried forward.
- Historical component/sign mapping PASS; FY26 Q4 national legs NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; BGD remains BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md. Next: official FY26 Q4 detailed table with separate legs and vintage metadata.


## W. BGD FY26 Q4 net-only confirmation and opposite-sign diagnostic (2026-11-20)
- Official Bangladesh Bank Quarterly Apr–Jun 2026 Vol XXIII No.4 Table V.1 confirms FY26 Q4 portfolio net -109 USDm; FY26 Q4 is provisional. Calendar 2026-Q2 = FY26 Q4.
- Reused IMF exact-key sample (A=0; L=-113.334678 USDm). Historical Bangladesh identity net=A−L would imply +113.334678 USDm, opposite to national net -109 (absolute difference 222.334678 USDm). Mark diagnostic REVIEW / FAIL_DIAGNOSTIC; no inferred sign flip or back-solving.
- Separate national legs and same-vintage evidence remain unavailable; BGD dual-leg BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md. Next: official FY26 detailed SDMX/XLS or dated revision/vintage source exposing both portfolio legs and resolving sign identity.


## X. BGD primary PDF reinspection / FY26 provisional portfolio series (2026-11-20)
- Official Bangladesh Bank Quarterly Apr–Jun 2026 Vol XXIII No.4 Table V.1 (PDF p.74, USDm) reports portfolio net: FY25 -138; FY26P -223; FY26 Q1/Q2/Q3/Q4 -45/-59/-10/-109. Calendar 2026-Q2 = FY26 Q4 = -109. Official publication index date 2026-11-15; P=Provisional, R=Revised.
- Table has no separate portfolio assets/liabilities; other DMB/NBDC and reserve rows are not portfolio components. Prior +113.334678 IMF conditional arithmetic remains diagnostic only, not a verified FY26 sign mapping.
- BGD net-only PASS; legs NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; dual-leg BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md.


## Y. BGD PI survey alternative-source scope closed (2026-11-20)
- Bangladesh Bank Survey Forms page defines PI assets/liabilities conceptually but explicitly sets calendar-year reporting. Official July–December 2025 PI publication methodology describes annual data 2010–2025 and PI-1 returns; public tables report annual stocks and transaction/NITA summaries, not FY26 Q4 quarterly BOP dual legs.
- Exclude annual survey stock/transactions and NITA flows from Q2 2026 dual-leg flow reconciliation. Official annual BOP page confirms FY26P net PI -223 only; DMB/NBDC assets/liabilities are not portfolio legs.
- Concept definitions PASS; survey as FY26 Q2 dual-leg flow source NOT_ELIGIBLE; FY26 Q2 national PI legs NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; BGD BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md. Next: supported raw-byte capture of official NSDP/BPM6 data; otherwise preserve blocker and move to next eligible country.


## Z. BGD Open Data / monthly BOP alternate route bounded (2026-11-20)
- Bangladesh Bank Open Data Initiative advertises free monthly BOP Excel and historical workbook; XLSX MIME blocked and direct byte capture failed. No raw bytes/hash claimed.
- Official monthly BOP public table displays portfolio investment as net only; DMB/NBDC and reserve asset/liability lines are not portfolio legs. IIP workbook is stock/position, not quarterly transaction flow. Exclude as substitute.
- BGD Q2 FY26 portfolio legs remain NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; dual-leg BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md.
- Next: stop repeating inaccessible Bangladesh workbook/XML routes and advance to next country in the existing 63-country dual-leg cohort with a distinct official national-source path.


## AA. Next cohort validation — Malaysia MYS Q2-2026 national-source component capture (2026-11-20)
- MYS is in the fixed 63-country Q2-2026 dual-leg cohort; both IMF entries present through Q2 (46/47 periods each). No cohort rebuild.
- Official BNM Quarterly Bulletin Q3 2026 Annex Table 3, BPM6, RMbn, Q2 provisional: portfolio net -35.2; assets -33.3; liabilities -1.8. Sign notes: negative asset = resident acquisition/outflow; positive liability = inflow from incurrence. DOSM Q2 release 14-Aug also confirms net -35.2; Q3 bulletin 18-Nov provides component split.
- Rounded components sum -35.1 vs net -35.2; source permits rounding. National rows and sign-note capture PASS; no FX conversion. IMF exact MYS Q2 values not extracted from archived large CSV; no new IMF query. Full crosswalk NOT_DONE; MYS PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_IMF_PORTFOLIO_SOURCE_CROSSWALK_20261120.md. Next: extract MYS Q2 rows from archived IMF panel without re-query, then complete scale/sign/vintage comparison.


## AB. Malaysia MYS archived IMF exact-row extraction (2026-11-20)
- Reused the existing IMF EMDE panel artifact 14505862034 (run 44474218174); ZIP SHA-256 `1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f` verified after download.
- Extracted MYS 2026-Q2 rows from the archived normalized panel without a new IMF request: A_NFA_T = 8,328,720,912.826584 USD; L_NIL_T = -453,604,929.8946682 USD. Both UNIT=USD, SCALE=6, PRECISION=6, DERIVATION_TYPE=O; raw attributes preserved.
- Normalized panel SHA-256: `e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a`. Original asset/liability CSV hashes remain recorded in the detail report.
- Official DOSM June 2026 Monthly Statistical Bulletin Table 8.8 (source BNM) records monthly “Average for Period” RM/USD: Apr 3.9784, May 3.9526, Jun 4.0778. No unweighted quarterly average was manufactured; exact Q2 rate aggregation convention remains NOT_DONE.
- MYS detail: `docs/GCR_MALAYSIA_MYS_Q2_2026_IMF_RAW_ROW_EXTRACTION_20261120.md`.
- Status: IMF raw-row extraction PASS; BNM national rows/sign-note capture PASS (reused); FX convention and separate country sign crosswalk NOT_DONE; same-vintage NOT_ESTABLISHED; MYS PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next exact action: establish official Q2 daily/quarterly RM/USD averaging convention, then reconcile asset and liability signs independently. No production changes, no new IMF query, no cohort rebuild.


## AC. Malaysia MYS Q2-2026 — official BNM daily FX candidate and leg diagnostic (2026-11-20)
- Continuity preflight reopened the current priority queue, MYS BNM national-source crosswalk and MYS archived IMF exact-row extraction report. The priority queue references Master Continuity Ledger blob SHA `ce94bbcfcfd080685e21c483260a93d6d2d60434`; its path was not surfaced by repository search in this execution, so no claim is made that the ledger body was reopened.
- Reused all existing IMF and BNM source extraction evidence; no new IMF query, cohort rebuild, national table recapture or repeated completed QA.
- Located BNM official daily USD/MYR Exchange Rates page and extracted 60 displayed business-day values for Q2 2026 (Apr 22, May 19, Jun 19). Candidate mean = 3.9992166667 RM/USD. Candidate CSV: `docs/evidence/malaysia_mys_q2_2026_bnm_daily_usd_myr_candidate.csv`, SHA-256 `9ab6470fe7117165343b9914cdf4d7dbf75ece89dbe27537b7d63b4811e03ced`.
- BNM Data Download catalogue describes daily noon middle rates, while the Exchange Rates page itself describes 0900/1200/1700 sessions and exposes session/rate-type controls. The exact selection behind the extracted table values was not conclusively preserved; therefore the 60-row series is a candidate, not an accepted conversion series.
- Candidate leg diagnostic at 3.9992166667 RM/USD: BNM asset magnitude 8,326.630632 USDm vs IMF A_NFA_T +8,328.720913 (absolute residual 2.090281); BNM liability -450.088142 USDm vs IMF L_NIL_T -453.604930 (residual 3.516788). Both are inside the candidate ±12.502448 USDm half-unit display bound, but remain REVIEW because FX session/convention and the Malaysia-specific scale/sign transformation are not fully admitted.
- Net diagnostic residual is 19.397828 USDm, above the standalone half-unit net-row bound; source component sum differs from published net by 0.1 RMbn and source warns of rounding. Net remains REVIEW; no forced identity.
- Detail report: `docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_DAILY_FX_CANDIDATE_RECONCILIATION_20261120.md`; CSV archived separately.
- Status: official daily-rate source discovery and 60-row candidate transcription PASS; FX selection/conversion convention NOT_ESTABLISHED; separate-leg comparison REVIEW; same-vintage NOT_ESTABLISHED; MYS PARTIAL / NOT PASS; EMDE aggregate NOT_AUTHORIZED.
- Next exact action: preserve BNM session/rate-type controls or official OpenAPI metadata; establish quarterly BOP transaction conversion convention; independently verify asset sign reversal and liability sign retention; then repeat comparison. No production changes, no new IMF query, no cohort rebuild.


## AD. Malaysia MYS Q2-2026 — BNM 1200-middle series and BPM6 FX methodology gate (2026-11-20)
- Reopened priority queue SHA `61f64b7f50711ffc48e2c637089764269e81fb5c`, MYS FX candidate report SHA `42712a95fc22b81c536f00a242988b1c7f15e5a3`, IMF extraction report SHA `025d58375f47eab1b66dc808e033727e9a733308`, and national crosswalk SHA `749a2bf15c5e29ef8756ca36a7cd1dede16ed510`. The referenced Master Continuity Ledger blob SHA `ce94bbcfcfd080685e21c483260a93d6d2d60434` is recorded, but its body/path did not resolve in this execution; no false claim of reopening it.
- Official dataset identity PASS: data.gov.my dataset `exchangerates_daily_1200`, source BNM, 12:00 mid-day reference, fields date/rate_type/USD, `rate_type=middle` explicitly means midpoint between buying and selling. Official landing page: https://data.gov.my/data-catalogue/exchangerates_daily_1200 ; CSV: https://storage.data.gov.my/finsector/exr/daily_1200.csv ; Parquet: https://storage.data.gov.my/finsector/exr/daily_1200.parquet .
- BPM6 methodology PASS: official IMF BPM6 manual hosted by DOSM states transaction-time market rate is the principle; daily average is a good approximation for daily transactions; if unavailable, use shortest-period average; use midpoint to exclude spread. For this Q2 flow crosswalk the selected method is arithmetic mean of actual observed BNM 1200-middle trading-day rates, without weekend/holiday fill.
- Raw capture blocker: browser reader rejected CSV binary content type; official API query did not resolve via web reader; container download failed. No daily_1200 raw bytes/hash, Q2 row count, mean or refreshed comparison is claimed.
- Prior 60-row candidate CSV and candidate FX residuals are explicitly NOT_ADMITTED as final evidence until independently matched to official daily_1200.csv and `rate_type=middle`; no silent relabel or overwrite.
- Detail report: `docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_1200_MIDDLE_FX_METHODOLOGY_GATE_20261120.md`.
- Status: official dataset identity PASS; rate type PASS; BPM6 conversion method PASS; raw daily series and SHA-256 NOT_DONE; Q2 daily mean NOT_DONE; separate-leg admitted-FX reconciliation NOT_DONE; same-vintage NOT_ESTABLISHED; MYS PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next exact action: obtain exact official daily_1200 CSV bytes or filtered OpenAPI records; preserve retrieval receipt and SHA-256; verify date completeness; calculate mean; then independently verify each leg sign/scale and publication vintage. No production changes, no IMF query, no cohort rebuild.


## AE. Malaysia MYS Q2-2026 — official BNM FX raw capture and separate-leg numeric validation (2026-11-20)
- Reopened current Master Continuity Ledger `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md` (pre-task blob SHA `86f6b5bda9ff6ab2bc91e30cf16677543dd2eecc`), plus MYS source crosswalk, exact IMF row extraction and IMF scale semantics/cross-country benchmark reports. No IMF re-query, no cohort rebuild and no repeated BNM national table extraction.
- Added research-only capture script `scripts/research/capture_mys_q2_bnm_fx.py` (commit `9e43c42130a4adc8518841280644de77f35970e8`) and 5-minute workflow `.github/workflows/gcr_mys_q2_bnm_fx_capture.yml` (commit `fe6244ba676c23ee516e81fccae3e12f9bc90201`). First guarded `nse_collector.yml` with paths-ignore (commit `2f62ec6ed1d66d65ba4d16cf6b739c54766a6d11`) to prevent an accidental full NSE run.
- GitHub Actions run `44688788754` SUCCESS; job `136129345981`; artifact `14607900969`, 1,261,845 bytes, ZIP SHA-256 `aeeb723a0b8a6e8b8bf1472b1ba7c720074c2e4d5cf604e30ba1d2e162e8c07b`, 90-day retention.
- Official raw daily BNM 1200 CSV: 3,870,195 bytes, SHA-256 `4b0c6cf00752753bbb070791468c7a50d39d8b8556129b5399cce94a264101be`; monthly CSV: 347,365 bytes, SHA-256 `705f81be36b180d8ac4d29ef13df741a97e996ce373567a03188924b980ec71c`. Both HTTP 200. Retrieval UTC `2026-11-20T06:34:49.542146Z`.
- Q2 daily 1200-middle rows: 60 (Apr 22, May 19, Jun 19); monthly `indicator=avg` rows: 3. All dates unique, three months complete. Monthly average vs actual daily mean: 3/3 PASS within four-decimal rounding. Q2 daily arithmetic mean = `4.001691666666666666666666667` MYR/USD; daily-count-weighted monthly mean = `4.001706666666666666666666667`; difference 0.000015.
- Permanent Q2 subset CSVs: `docs/evidence/gcr_mys_q2_2026_bnm_fx/mys_q2_2026_daily_1200_middle_usd.csv` SHA-256 `836fa4241d257dacd9477cd4cac5dd904872190657279bc96132dd59385c48bb`; monthly subset `mys_q2_2026_monthly_avg_usd.csv` SHA-256 `de9025e701389adcae917065cce1f273f2f6d3d7f9daeb33b73bf3327ba6974b`.
- Reconciled each MYS leg using the empirically supported Data Portal derived USD-million presentation `OBS_VALUE/10^6` (raw IMF values, UNIT and SCALE remain unchanged). Asset: BNM -33.3 RMbn sign-reversed to match resident acquisition/outflow direction, converted +8,321.480707 USDm vs IMF +8,328.720913; residual 7.240206 USDm. Liability: BNM -1.8 RMbn retained sign, converted -449.809768 USDm vs IMF -453.604930; residual 3.795162 USDm. BNM one-decimal RMbn half-unit rounding bound = ±12.494716 USDm; both separate-leg comparisons PASS at published display precision. No netting.
- BNM component arithmetic remains REVIEW: -33.3 + -1.8 = -35.1 vs reported -35.2 RMbn; source permits rounding.
- Previous 60-row page-derived candidate mean 3.9992166667 is NOT_ADMITTED / SUPERSEDED because exact session/rate type was unproven and it did not reconcile to the official 1200-middle daily/monthly pair.
- Full MYS validation remains PARTIAL / NOT PASS because exact same-vintage BNM preliminary (Q3 bulletin published 18-Nov) ↔ IMF panel revision cut-off alignment is NOT_ESTABLISHED. No 63-country aggregate authorization.
- Detail report: `docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_OFFICIAL_FX_AND_DUAL_LEG_RECONCILIATION_20261120.md` (commit `34beb34aeca06c074a90b758655789b7e610e4ae`).
- Next exact action: source-specific vintage/revision cut-off bridge for BNM preliminary Q2 vs IMF panel; if no explicit bridge is published, retain NOT_ESTABLISHED and advance to the next eligible cohort member. Do not repeat FX capture or monthly/daily reconciliation absent a source revision.
- Protected invariants unchanged; no production code, selector, ranking, pressure fade, CORE-672, Engines A–E, weights or trade gates changed. No paid source, synthetic data, fabricated timestamp, forward-fill, imputation, netting or aggregate authorization.


## AF. MYS publication-vintage gate bounded; next eligible cohort member THA selected (2026-11-20)
- Reopened current ledger, queue, MYS source crosswalk, MYS exact IMF rows, and official FX/dual-leg report; no repeated FX download or IMF request.
- Official DOSM Q2 BOP release: 14-Aug-2026; it gives portfolio net only at rounded RM35.2bn outflow. BNM Quarterly Bulletin 3Q 2026 issued 18-Nov-2026 marks Q2-2026 as preliminary and publishes separate portfolio net -35.2 RMbn, assets -33.3, liabilities -1.8. OpenDOSM dashboard last updated 18-Nov-2026 13:00 (data as of Q3) shows Q2 portfolio net -RM35,155m; it is a net-only current-vintage cross-check.
- IMF BOP dataset public page does not expose observation-level source submission/revision timestamp. Its separate metadata dashboard's 18-Nov publication date is country metadata, not MYS Q2 BOP observation vintage. Existing IMF panel archive retrieval 19-Nov is acquisition time, not source vintage.
- MYS official chronology gate PASS; IMF observation-vintage evidence NOT_AVAILABLE; exact BNM↔IMF same-vintage cut-off bridge NOT_ESTABLISHED. MYS numeric legs remain 2/2 PASS at BNM published precision; MYS full validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: `docs/GCR_MALAYSIA_MYS_Q2_2026_PUBLICATION_VINTAGE_GATE_20261120.md` (commit `6c2d6d65c426b3ac3d3d9c9e4bf9e88375324460`).
- No further repeat of MYS FX capture, daily/monthly QA or the same public IMF landing-page search absent a new historical snapshot/revision log.

## AG. Thailand THA Q2-2026 — BOT official USD table and IMF dual-leg numeric check (2026-11-20)
- Selected THA from the existing fixed 63-country Q2-2026 cohort after MYS's same-vintage gate remained NOT_ESTABLISHED; THA both IMF legs are present in the existing panel. No cohort rebuild and no new IMF request.
- BOT official EC_XT_049_S2 Balance of Payments (US$), quarterly, USD million, page last updated 30-Sep-2026 14:33; Q2/2026 marked preliminary. Its official sign note states positive increases net financial assets/liabilities and negative decreases; net financial account is assets minus liabilities.
- BOT Q2 portfolio assets +4,679.07 USDm, liabilities -238.36 USDm, total 4,917.43 USDm; identity 4,679.07 - (-238.36) = 4,917.43 exact at displayed precision.
- Reused archived IMF normalized panel SHA-256 `e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a`; THA Q2 raw A_NFA_T +4,679,073,421.50334 USD, L_NIL_T -238,358,188.710181 USD, SCALE=6, UNIT=USD, PRECISION=6, DERIVATION_TYPE=O. Derived USDm comparisons: +4,679.07342150334 and -238.358188710181.
- Residuals: asset +0.00342150334 USDm; liability +0.001811289819 USDm; both inside ±0.005 USDm BOT two-decimal display precision. Numeric leg comparisons 2/2 PASS; no sign transform, no raw overwrite, no netting.
- Research script `scripts/research/reconcile_tha_q2_2026_bot_imf.py` commit `6a618eb337a6782cb3b87c28a87efcafd958938f`; workflow `.github/workflows/gcr_tha_q2_2026_bot_imf.yml` commit `768221a7a53842ebc712df57030c19d7bca4b5c9`; NSE collector paths-ignore guard commit `b983bf461ab852d295b1eea0d17553c322d53953`.
- Run `44689541630` SUCCESS; job `136131786969`; artifact `14607329438`, 39,093 bytes, ZIP SHA-256 `70328900a9e0058385c6ac7efa5384f86d10508a5056f8f16e40c3afd5b24aec`; raw BOT HTML 551,847 bytes, SHA-256 `b4a42305fe18668c91e1feadd70ada0537f6e2f8c5b13ef59dd1fdcbd4d00f80`; retrieved 2026-11-20T06:41:16.952209Z.
- BOT source is Q2 preliminary with last update 30-Sep-2026 14:33; IMF panel archive retrieved 19-Nov but no observation-level source submission/revision date. Same-vintage NOT_ESTABLISHED; THA full national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: `docs/GCR_THAILAND_THA_Q2_2026_BOT_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120.md` (commit `523016a438a79080ed1c08c033f11f7972ba4994`).
- Next exact action: seek BOT public revision history/archived Q2 snapshot and IMF observation-level source vintage. If unavailable, preserve NOT_ESTABLISHED and advance to next eligible country after preflight. Do not repeat the same BOT table fetch.
- Invariants unchanged; no production, selector, ranking, pressure fade, CORE-672, Engines A–E, IPO-PLX V2, weights or trading gates changed. No paid data, synthetic data, inferred vintage, FX conversion, netting or aggregate authorization.


## AH. Philippines PHL Q2-2026 — BSP dedicated portfolio table cross-check (2026-11-20)
- Selected PHL from the fixed 63-country cohort after THA; no cohort rebuild and no new IMF GET.
- Official BSP dedicated Table 1.7 and dated Q2 BOP release (11-Sep-2026) show Q2 2026 portfolio net -468 USDm, asset leg (Net Acquisition of Financial Assets) +1,331 USDm, liability leg (Net Incurrence of Liabilities) +1,798 USDm.
- Existing IMF panel raw Q2 values: A_NFA_T +1,330,642,951.05526 USD (SCALE=6, UNIT=USD, PRECISION=6, DERIVATION_TYPE=O); L_NIL_T +1,798,282,616.26536 USD (same metadata). Comparison-only USDm values +1,330.64295105526 and +1,798.28261626536. Residuals vs BSP: -0.35704894474 and +0.28261626536 USDm, both within ±0.5 USDm whole-million display rounding. Numeric legs 2/2 PASS at published precision; no raw overwrite, netting, FX or sign transform.
- Rounded identity: 1,331 - 1,798 = -467 vs reported -468; 1 USDm difference is within combined whole-million display rounding. Do not force arithmetic equality.
- Same-vintage remains NOT_ESTABLISHED: BSP Q2 publication 11-Sep and preliminary status; IMF panel retrieval 19-Nov is acquisition time, with no observation-level source vintage. PHL full validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Automated parser/capture remains NOT_PASS. Runs 44690030449 and 44690124941 exposed a generic all-BOP table parser incorrectly selecting Other Investment; those wrong rows are NOT_ADMITTED. Dedicated Table 1.7 run 44690374864 failed closed because HTMLParser did not handle Excel-HTML sparse cells. Official BSP page text independently supports the values; no successful structured capture artifact is claimed.
- Report: docs/GCR_PHILIPPINES_PHL_Q2_2026_BSP_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120.md (commit 10b25708ac9df0ad7010a952c84941b6ef1b21a9).
- Operational correction: accidental NSE runs 44690020188, 44690030398, 44690124814 and 44690374904 were cancelled; no outputs admitted.
- Exact next: repair Table 1.7 Excel-HTML sparse-cell parser (including ss:Index), capture successful raw+parsed artifact and verify against release, then seek IMF observation-vintage evidence. No IMF requery, cohort rebuild, or production changes.


## AI. PHL Q2-2026 parser/capture acceptance PASS; same-vintage remains unresolved (2026-11-20)
- Fixed two parser defects: (1) ignored one-cell merged section headings in BSP Excel-HTML and validated Q2 group + 2026p subheader before reading the Q2-2026 column; (2) anchored press-release row extraction to the Portfolio Investment section only, preventing later Other Investment rows with identical labels from overwriting values. Preliminary flag is derived from verified Q2 header cell.
- Successful run 44705225122 / job 136183035008; artifact 14614766459, ZIP SHA-256 7e0d57f7d50f6f0a6622183d81f2bb8bbe04ee297f489f20dd982465d3b46b5c (15,415 bytes).
- Raw BSP Table 1.7: 156,110 bytes, SHA-256 b267ceab83794b86cd6c6a3ce703d878c2185091670e0c528b10df1644774569. BSP Q2 release raw: 148,165 bytes, SHA-256 272890a3a383bbef2eebfb274746e3835f2c3e7d3ab084f303f317f6813b5707. CSV SHA-256 8bc1a27fc66c40f99ad7d66789884a90c0f1d1cb91b4c64065fdec4e769d2939; summary SHA-256 376894e48319d0a0a2c0d4e8322f4de0fc578fd8b1b70a4f361e425b0f0dd166.
- BSP Q2 preliminary TRUE; Table 1.7 and dated release match exactly: portfolio net -468 USDm, assets +1,331, liabilities +1,798. IMF comparison residuals -0.35704894474 and +0.28261626536 USDm, both inside ±0.5; numeric legs 2/2 PASS. Rounded asset-minus-liability identity is -467 vs published -468, a 1 USDm difference retained as rounding.
- Same-vintage NOT_ESTABLISHED. Current BSP Last-Modified response header is not a historical revision chain. IMF public BOP dataset page exposes API/download but no observation-level source submission/revision timestamp. BSP FDI revision notice is not applicable to portfolio investment and is excluded.
- PHL national acceptance remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Failed diagnostic runs and wrong-category rows remain excluded.
- Paths-ignore guard added for PHL and cancellation paths in commit fbaa2617f8e996b996f299652194974141cd0921. Accidental NSE runs 44704973029 and 44704985742 confirmed cancelled; no outputs admitted.
- Detailed report updated: docs/GCR_PHILIPPINES_PHL_Q2_2026_BSP_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120.md (update commit d3808035b3c7ad8372b21ded3f1eeb9f9700deea).
- Next: bounded official vintage search only; if no specific BSP portfolio revision archive or IMF observation-level vintage attribute is public, retain NOT_ESTABLISHED and advance to next eligible cohort member after preflight. No repeat parser work, IMF requery or cohort rebuild.


## AJ. PHL official revision-policy gate closed as NOT_ESTABLISHED (2026-11-20)
- BSP official Revision Policies page states BOP/IIP data released during the reference quarter are preliminary and may be revised in any quarter of the reference year; prior-year revisions can occur with Q2 September and Q4 March reports.
- BSP 2024 BPM6 revision technical note documents historical portfolio-specific revisions to both asset and liability legs, including CPIS and BSP transaction-report updates. This demonstrates revision risk but does not establish a revision to PHL Q2-2026 values.
- BSP's FDI in-kind revision notice remains excluded; it concerns FDI, not portfolio investment.
- IMF BOP public dataset/API landing page and 18-Nov-2026 BOP/IIP metadata dashboard do not expose PHL Q2 observation-specific source submission/revision timestamp. Metadata dashboard date is not the observation vintage.
- No public PHL Q2-2026 portfolio revision chain or IMF observation-level vintage field located. Same-vintage NOT_ESTABLISHED; numeric 2/2 PASS and raw+parsed capture PASS; full national acceptance PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report update commit 395e5aca2ebf55994dbf36a8c6114b31b97f309a.
- Close bounded PHL vintage search; do not repeat generic IMF landing-page or BSP policy searches absent a new release. Next action: preflight the existing 63-country queue and choose the next eligible country without rebuilding the cohort.


## AK. Colombia COL Q2-2026 — official-source boundary gate (2026-11-20)
- Selected COL from the existing fixed 63-country Q2 both-leg cohort after repository preflight; GitHub search found no prior COL national-source reconciliation report. Existing coverage matrix confirms 46 observations in each of A_NFA_T and L_NIL_T, both ending 2026-Q2. This is availability only.
- Official BanRep Q2 report published 1-Sep-2026: Q2 financial-account net capital inflows USD3,719m; summary includes net liquidation of external assets USD6,149m, derivative gains USD804m, decreases in external liabilities USD2,683m and reserve transactions USD550m. It says net portfolio-instrument liquidations partially offset the result but does not provide separate portfolio asset/liability transaction amounts in the inspected report/PDF.
- BanRep SDDS page last updated 13-Nov-2026 displays Q2 portfolio IIP asset stock USD125,046.1m and liability stock USD118,800.9m (with equity/debt stock components). These are end-period stocks, not Q2 BOP flows; explicitly NOT_ADMITTED to the flow comparison.
- General BPM6 financial-account sign note is not enough to map portfolio component signs. No raw COL IMF values were copied; no IMF query or cohort rebuild. BanRep statistics portal series route timed out in the web reader; no export/raw bytes acquired.
- COL portfolio transaction legs NOT_EXTRACTED; sign mapping NOT_ESTABLISHED; same-vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; COL PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_COLOMBIA_COL_Q2_2026_BANREP_OFFICIAL_SOURCE_BOUNDARY_AUDIT_20261120.md.
- Next exact action: identify public BanRep export/series metadata for separate Q2 portfolio transaction assets and liabilities, with units/signs/revision metadata. If unavailable, retain blocker and advance. No stock-flow substitution or repeated IMF request.
- Invariants unchanged; no production code or protected selector/scoring/diagnostic/engine changes.


## AL. Colombia COL — BanRep exact portfolio-series catalogue identified; export remains blocked (2026-11-20)
- Continued the official-source boundary work without IMF re-query or cohort rebuild. BanRep's BOP datawarehouse page confirms BPM6 quarterly series from 2000 onward and a dedicated Portfolio Investment annex. Its financial-account sign statement is general, not yet the exact two-series crosswalk.
- Official SUAMECA multiple-download catalogue search exposes three separate quarterly portfolio series in current USD millions, 2000-Q1 through 2026-Q2, last updated 2026-09-01: portfolio total; portfolio net acquisition of financial assets; portfolio net incurrence of liabilities. The latter two are the required national components corresponding conceptually to A_NFA_T and L_NIL_T.
- SUAMECA download page timed out when opened; no series IDs, export bytes, Q2 values, exact metadata or hashes obtained. Therefore discovery PASS; raw capture NOT_DONE; numeric validation NOT_DONE; sign mapping NOT_ESTABLISHED; same-vintage NOT_ESTABLISHED; COL PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Updated detail: docs/GCR_COLOMBIA_COL_Q2_2026_BANREP_OFFICIAL_SOURCE_BOUNDARY_AUDIT_20261120.md (update commit 40722e580d98c49ac57328f7d8974115529b4e51; blob 33ff9eed00159f7c8c0798a061be785440a81f94).
- Next: access exact SUAMECA series entries via supported browser route; capture series IDs and raw quarterly exports with receipts/hash; inspect Q2 values and series sign metadata. No IMF re-query or cohort rebuild.


## AM. Colombia COL — official SDMX route ruled out for BOP; export blocker retained (2026-11-20)
- Reopened COL report, master ledger, priority queue and fixed cohort before this bounded follow-up. No duplicate COL source report, IMF re-query or cohort rebuild.
- Inspected BanRep official SDMX guide v4.0 (Oct-2026). Its documented public SDMX flow inventory covers IBR, DTF, TRM, TPM, TIB, COLCAP, monetary aggregates, UVR and TES; BOP/portfolio investment is not among the published topics. The generic SDMX REST pattern is therefore not sufficient to construct a BOP query. No guessed flow ID or query made.
- SUAMECA multiple-download catalogue independently confirms the two required portfolio component series exist, quarterly in current USD millions through 2026-Q2 and last published 2026-09-01. However no series IDs, raw export, Q2 values, sign/vintage metadata or SHA-256 are available from the captured catalogue response; the series page route returned 502.
- COL remains discovery PASS; raw capture NOT_DONE; numeric validation NOT_DONE; sign mapping NOT_ESTABLISHED; same-vintage NOT_ESTABLISHED; PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Official guide/catalogue sources: https://suameca.banrep.gov.co/archivos/webservices/sdmx_v_3_1/GUIA_CONSUMO_SDMX_V_3_1.pdf and https://suameca.banrep.gov.co/descarga-multiple-de-datos/ .
- Next rank-1 action: move to the next unvalidated member of the fixed 63-country cohort after exact repository preflight; retain COL as a blocked country case and resume only if a distinct supported export route becomes available. No production changes or protected-invariant changes.


## AN. Peru PER Q2-2026 — BCRP portfolio series identified; national scope remains unresolved (2026-11-20)
- Selected PER from the existing fixed 63-country Q2 dual-leg cohort after COL's official SDMX route was ruled out. Repository search found no prior PER Q2-2026 national portfolio-flow audit. No cohort rebuild or IMF re-query.
- BCRPData official quarterly catalogue identifies private-sector portfolio assets PN39278BQ and private-sector portfolio liabilities PN39285BQ, both quarterly through T2-2026 and last updated 2026-08-20; it separately lists public-sector portfolio liabilities PN39404FQ through T2-2026.
- Scope boundary: PN39278BQ is explicitly private-sector assets, not yet proven to cover full-economy portfolio asset acquisition. Public-sector portfolio liability is separately listed. No full national asset/liability crosswalk or public-sector asset treatment established; do not add sector fragments or assume completeness.
- BCRP official API guide documents GET/POST and CSV/JSON/XML/XLS; bounded documented-pattern requests for Q2 2026 series PN39278BQ and PN39285BQ did not return content in the web reader. No Q2 values/raw bytes/receipt/hash obtained.
- PER exact series discovery PASS for listed subseries; full national scope NOT_ESTABLISHED; API raw capture NOT_DONE; Q2 values NOT_EXTRACTED; sign mapping and same-vintage NOT_ESTABLISHED; numeric validation NOT_DONE; PER PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_PERU_PER_Q2_2026_BCRP_PORTFOLIO_SERIES_SOURCE_BOUNDARY_AUDIT_20261120.md (commit 55d03cc785edf7ce853366a41565708b0dec6a91).
- Next exact action: obtain raw BCRP API output through supported byte-preserving route and resolve full-economy portfolio asset scope/public-sector treatment before any comparison. No IIP stock or broad sector aggregate substitution; no IMF re-query/cohort rebuild.


## Continuation 50 — Pakistan PAK Q2-2026 SBP source-boundary audit (2026-11-20)
- Preflight reopened current master ledger, priority queue, fixed cohort and PER report. Repository search found no prior dedicated PAK Q2-2026 national portfolio-flow validation report; selected PAK from the fixed 63-country cohort. No cohort rebuild and no IMF re-query.
- Official SBP Economic Data catalogue lists quarterly “Summary Balance of Payments as per BPM6” through Jun-2026 and separately lists “Core Set of Portfolio Investment Assets data” as half-yearly. EasyData listing gives quarterly BOP coverage Sep-2002 to Jun-2026, last release 18-Aug-2026. These are catalogue-level discovery facts, not proof of Q2 portfolio transaction values.
- SBP September-2026 BPM6 PDF presents FY26 Jul-Jun cumulative and monthly Sep values plus Jul-Sep aggregates; it does not isolate Apr-Jun 2026. Portfolio Investment Abroad and Portfolio Investment in Pakistan appear as separate categories, but no Q2-specific transaction legs were extracted from this table.
- SBP Core Set of Portfolio Investment Assets PDF is an End-June-2025 position snapshot in PKR, not transaction flows and not Q2-2026; it has no corresponding liability leg. Explicitly excluded from A_NFA_T/L_NIL_T comparison.
- SBP archive lists a separate quarterly calendar-year BOP Excel dataset, but raw workbook and its Q2 portfolio observations/definitions were not inspected. Do not assume it is interchangeable with BPM6 quarterly dataset.
- PAK status: official quarterly BPM6 dataset discovery PASS (catalogue only); Q2 asset/liability values NOT_EXTRACTED; calendar-vs-fiscal period mapping NOT_ESTABLISHED; sign and same-vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; national validation PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_PAKISTAN_PAK_Q2_2026_SBP_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md.
- Official sources: https://www.sbp.org.pk/economic-data ; https://easydata.sbp.org.pk/apex/f?p=10:210:8439371819372: ; https://www.sbp.org.pk/assets/document/Balancepayment_BPM6.pdf ; https://www.sbp.org.pk/ecodata/CPIS-Sdds-Assets-Data.pdf ; https://archive.sbp.org.pk/ecodata/index2.asp .
- Next exact action: retrieve the official SBP quarterly BPM6 EasyData export or calendar-year archive workbook, establish calendar/fiscal period mapping, and capture separate Q2-2026 portfolio asset/liability transaction rows with raw bytes, units, revision flags and hashes. If unavailable, preserve blocker and advance; do not substitute CPIS stocks, net-only flows or FY cumulative values.
- Protected invariants unchanged; no production code, selector, ranking, pressure fade, CORE-672, Engines A-E, IPO-PLX V2, weights, gates or trade alerts changed.


## Continuation 51 — PAK Q2-2026 SBP revised quarterly values extracted (2026-11-20)
- New official SBP quarterly calendar-year BPM6 table located: https://www.sbp.org.pk/assets/document/BPM6_c.pdf . Header identifies CY26 Q2 as revised (R), units million USD.
- Exact CY26 Q2(R) values: Portfolio investment abroad = -2 USDm; Portfolio investment in Pakistan = -243 USDm. These are separately published portfolio components, not derived from cumulative/monthly figures. This corrects the prior PAK audit's NOT_EXTRACTED state for source values.
- Source-value extraction PASS only. Sign/definition crosswalk to IMF A_NFA_T/L_NIL_T NOT_ESTABLISHED; exact IMF PAK Q2 row retrieval from existing archive NOT_DONE; same-vintage/revision timestamp NOT_ESTABLISHED; dual-leg numeric comparison NOT_DONE; PAK PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report updated: docs/GCR_PAKISTAN_PAK_Q2_2026_SBP_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md. No IMF re-query or cohort rebuild. Next: retrieve exact archived IMF PAK Q2 rows, verify official BPM6 sign definitions, compare legs separately at USDm display precision, then investigate SBP revision timestamp. No netting or assumed sign transform.


## Continuation 52 — PAK Q2-2026 dual-leg archive reconciliation
- Existing IMF raw archive reused; no IMF query or cohort rebuild. Raw Git blob SHAs: asset `15449e87c9057291a1f52f2f8cd9805df55f9fb8`; liability `15f379dc42e2760eb5f2384618e48f5ddc3177f1`.
- Exact PAK rows: `A_NFA_T`, P_F, USD, Q, 2026-Q2, OBS_VALUE -2000000, SCALE 6, ACTION R; and `L_NIL_T`, P_F, USD, Q, 2026-Q2, OBS_VALUE -243000000, SCALE 6, ACTION R.
- SBP official BPM6 revision notice states financial-account increases in assets and liabilities are positive and decreases negative; SBP FY23 BPM6 introduction defines NAFA/NIL and confirms negative changes indicate decreases. Sources: https://www.sbp.org.pk/departments/stats/Notice/BPM6-Revision-16-Aug-13.pdf ; https://www.sbp.org.pk/publications/bop/BOPFY23/Intro.pdf .
- Separate USDm comparison: abroad/asset SBP -2 vs IMF A_NFA_T -2 (difference 0); in-Pakistan/liability SBP -243 vs IMF L_NIL_T -243 (difference 0). Numeric dual-leg comparison 2/2 PASS at published precision; conceptual sign/framework crosswalk SUPPORTED. No netting.
- SBP CY26 Q2 is marked revised (R), and IMF rows carry ACTION=R; exact observation-specific revision timestamp and same-vintage bridge remain NOT_ESTABLISHED. PAK national validation PARTIAL, not PASS; aggregate NOT_AUTHORIZED.
- No SBP raw PDF SHA-256 captured; no IMF re-query, no cohort rebuild, no production changes. Detail: docs/GCR_PAKISTAN_PAK_Q2_2026_SBP_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md.
- Next: inspect official SBP Data Revision Policy for dated Q2 portfolio revision history; if unavailable, retain UNKNOWN and proceed to next unvalidated cohort country.


### Continuation 52 — SBP Data Revision Policy check
- Official SBP Data Revision Policy (last updated 11-Sep-2019): https://www.sbp.org.pk/departments/stats/Data-Revision-Policy.pdf . It defines revisions and states that provisional observations are marked P and revised observations R; revisions may reflect better source data, routine recalculation, methodology changes or correction of errors. It says reasons/sources are explained when revised series are released (policy PDF lines 21-29, 53-74, 91-111).
- This supports interpreting SBP's Q2 CY26 (R) label as revised status, but the policy is generic and does not identify the Q2-2026 portfolio rows' specific revision date, prior value, reason, or revision event. Thus it does not close the same-vintage gate. IMF ACTION=R is likewise status-only without matching timestamp evidence.
- Same-vintage remains NOT_ESTABLISHED / UNKNOWN; PAK remains PARTIAL, not PASS; aggregate NOT_AUTHORIZED. Next best action: proceed to next unvalidated fixed-cohort country while retaining this PAK vintage blocker unless a dated observation-specific SBP revision record becomes publicly available.


## Continuation 53 — Peru (PER) Q2-2026 BCRP national-source boundary audit (2026-11-20)
- PER selected from fixed 63-country cohort after fresh repository search found no dedicated PER national portfolio reconciliation report. Reused exact IMF archive; no IMF query or cohort rebuild.
- Existing IMF raw rows: A_NFA_T = 1,999,155,686.69433 USD; L_NIL_T = 1,699,664,071.47559 USD; both Q, USD, 2026-Q2, ACTION=R, SCALE=6, PRECISION=6. Raw file Git blob SHAs: asset 15449e87c9057291a1f52f2f8cd9805df55f9fb8; liability 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Official BCRP quarterly indicators PDF inspected: https://www.bcrp.gob.pe/docs/Estadisticas/indicadores-trimestrales.pdf ; the accessible version covers through 2025-Q4, so it cannot validate Q2-2026. Candidate BCRP Note of Studies No. 59 Q2-2026 URL returned only iframe shell, not PDF content. Third-party report snippets were excluded from numeric admission.
- PER gates: IMF exact rows PASS; official BCRP source family discovery PASS; official national Q2 portfolio legs NOT_EXTRACTED; source bytes/hash NOT_CAPTURED; sign/definition/vintage NOT_ESTABLISHED; dual-leg comparison NOT_DONE; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_PERU_PER_Q2_2026_BCRP_IMF_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md. Next: retrieve official BCRP Q2-2026 report/PDF through supported official path, archive bytes+metadata+SHA-256, and inspect exact separate portfolio legs; if blocked, keep blocked and advance.


## Continuation 54 — PER BCRPData quarterly portfolio series discovery (2026-11-20)
- Reopened current Ledger, Queue, cohort and PER audit. Found official BCRPData Financial Account quarterly page: https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/cuenta-financiera . It lists private/public sector series through T2-2026, last updated 20-Aug-2026.
- Official Q2-2026 values (USDm): private portfolio assets PN39278BQ = 1,749; private portfolio liabilities PN39285BQ = 279; public portfolio liabilities PN39404FQ = 1,421. Official result pages: https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/resultados/PN39278BQ/html ; https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/resultados/PN39285BQ/html ; https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/resultados/PN39404FQ/html .
- Liability reconstruction: 279 + 1,421 = 1,700 USDm vs archived IMF L_NIL_T 1,699.66407147559 USDm; +0.336 USDm residual, within whole-USDm BCRP display precision. Liability numeric comparison PASS subject to definitions/vintage.
- Asset remains incomplete: private-sector portfolio assets 1,749 USDm only. Catalogue has public-sector asset aggregate PN39402FQ but no public-sector portfolio-asset subseries among listed 25 series. IMF A_NFA_T is 1,999.15568669433 USDm; private-only residual is not a valid full-scope comparison. Do not substitute total public assets.
- PER state: BCRP source extraction PASS for 3 series; liability numeric PASS; asset full-scope PARTIAL/NOT_DONE; sign/definition and same-vintage NOT_ESTABLISHED; full national dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. BCRP series metadata last updated 20-Aug-2026; IMF ACTION=R lacks matched timestamp.
- Detail report updated: docs/GCR_PERU_PER_Q2_2026_BCRP_IMF_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md. Next: inspect BCRP API/docs and public asset metadata for a separate public-sector portfolio-asset series; otherwise preserve asset UNKNOWN and advance.


### Continuation 54 — BCRP API contract check
- Official BCRPData API developer guide: https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf . It documents GET series queries, up to 10 same-frequency series, output formats including JSON/CSV, and exact series-code/date-range URL structure (guide pp.2-5; updated 24-May-2022).
- Constructed one documented, single-period JSON GET for PN39278BQ-PN39285BQ-PN39404FQ, 2026-2/2026-2/ing. The web retrieval returned an internal access error; no raw API payload/receipt was acquired. Do not claim API download or raw-file hash. Previously inspected official HTML series pages remain the evidence for the three displayed values.
- API path remains an available documented retrieval contract but the exact endpoint access in this session is BLOCKED; do not repeatedly retry the same URL. Continue with HTML display evidence only, and keep the raw-byte archival gate open.


## Continuation 55 — PER catalogue closure; NPL selected (2026-11-20)
- Full official BCRP quarterly Financial Account catalogue inspected (58 series). Public sector list contains aggregate assets PN39402FQ and aggregate liabilities PN39403FQ, then portfolio-liability components PN39404FQ onward; no public-sector portfolio-asset subseries appears in the full listed public-sector 25-series catalogue. Aggregate assets rejected as portfolio proxy. PER full asset remains PARTIAL/NOT_DONE; liability numeric PASS at published rounding; full dual-leg PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- PER report addendum records the catalogue boundary and exact citations/URLs. BCRP API GET retrieval remains blocked; no raw payload/hash claimed.
- Next country NPL selected from fixed 63-country cohort after repo search found no dedicated Q2-2026 national reconciliation report. NRB official external-sector page lists monthly BPM6/BPM5 and annual BPM6/BPM5 datasets: https://www.nrb.org.np/database-on-nepalese-economy/external-sector/ . Linked BPM6 XLSX: https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx . XLSX MIME retrieval failed (400 unsupported content-type); workbook not inspected, no values admitted.
- Next exact action: inspect NRB BPM6 workbook via XLSX-capable route; extract Apr-Jun 2026 separate portfolio asset/liability flows only if published as monthly/quarterly comparable observations; confirm sign, units, cumulative/monthly basis, vintage. Reuse archived IMF rows; no IMF query/cohort rebuild.


## Continuation 56 — Nepal NRB Q2-2026 source-boundary audit (2026-11-20)
- NRB official External Sector portal confirms monthly Balance of Payments BPM6/BPM5 datasets. NRB NSDP lists BOP Browse Data and SDMX download; currently linked XML is NEPAL_BOP_2024_Q1.xml, stale for Q2-2026 and excluded.
- NRB Monthly Statistics archive lists monthly XLSX for 2082-12 (mid-Apr 2026), 2083-01 (mid-May 2026), 2083-02 (mid-Jun 2026), and 2083-03 (mid-Jul 2026). Relevant Chaitra/Baisakh/Jestha XLSX links discovered. XLSX retrieval attempts failed (unsupported MIME / timeout); no workbook bytes, sheets, rows, values, or hashes claimed.
- NRB July 2026 macro report chart gives monthly overall BOP only; aggregate cannot replace separate portfolio legs. NRB balance-sheet foreign securities are stocks, excluded. No third-party values accepted.
- NPL gates: official BPM6 source discovery PASS; monthly XLSX links PASS; workbook/raw bytes NOT_CAPTURED; monthly-vs-cumulative period basis NOT_ESTABLISHED; separate asset/liability legs NOT_EXTRACTED; sign/unit/concept/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_NEPAL_NPL_Q2_2026_NRB_BPM6_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md. Next: retrieve official NRB XLSX through XLSX-capable path; inspect sheets and separate portfolio flow rows, establish calendar Q2 mapping and cumulative/monthly basis before any arithmetic. Reuse existing IMF archive only.


## Continuation 57 — NPL wrong-document-family correction (2026-11-20)
- Critical correction: opened NRB monthly archive PDF entries for Chaitra 2082, Baisakh 2083 and Jestha 2083. They are Banking & Financial Statistics (Monthly) (Provisional), not External Sector Balance of Payments. Full PDF search: no “portfolio” or “Balance of Payments” in April; no “Balance of Payments” in May/June. Their linked XLSX must be rejected as BOP source. Prior Continuation 56 suggestion that these monthly archive XLSX might contain portfolio rows is withdrawn.
- Correct official source remains External Sector monthly Balance of Payments (BPM6): https://www.nrb.org.np/database-on-nepalese-economy/external-sector/ ; linked official workbook https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx returns unsupported XLSX MIME; no bytes inspected.
- NSDP BOP browse timed out; SDMX download points to stale 2024-Q1 XML and XML MIME unsupported. NPL actual BOP rows not extracted; separate portfolio legs NOT_EXTRACTED; validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report correction appended. Next: seek an XLSX-capable route for the one BPM6 workbook or official NRB API/export; if blocked, stop retries and advance. No stock substitution, no IMF query, no cohort rebuild.


## Continuation 58 — NPL official BPM6 retrieval-route audit (2026-11-20)
- Reopened the official NRB External Sector page and verified it explicitly lists Monthly Balance of Payments (BPM 6). Exact workbook locator confirmed: https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx .
- Reopened NRB NSDP: Balance of Payments has Browse Data and Download in SDMX; current SDMX target is NEPAL_BOP_2024_Q1.xml, stale for Q2-2026 and not admitted. Browse route did not provide a usable Q2 portfolio export in this bounded check.
- Repeated unsupported XLSX MIME was not retried. A separate direct byte-download attempt against the exact workbook URL also failed. No bytes, workbook sheets/rows, values, or SHA-256 obtained. Discovery PASS; byte retrieval BLOCKED; separate assets/liabilities NOT_EXTRACTED; period/sign/unit/vintage NOT_ESTABLISHED; NPL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- New report: docs/GCR_NEPAL_NPL_Q2_2026_NRB_BPM6_RETRIEVAL_ROUTE_AUDIT_CONTINUATION58_20261120.md (commit `7dd358b7256f01e75e813f489c5d6591e21ae326`).
- Next: wait for a distinct supported XLSX-capable or official API/export route; then hash and inspect the exact workbook before extracting Q2 portfolio legs. If unavailable, preserve NPL PARTIAL and move to next eligible fixed-cohort country. No IMF re-query/cohort rebuild, no wrong-family monthly XLSX, no stock substitution, no production change.



## Continuation 59 — Vietnam (VNM) Q2-2026 SBV portfolio source-boundary audit (2026-11-20)
- VNM selected from the existing fixed 63-country Q2-2026 both-leg cohort after repository search found no dedicated VNM national portfolio validation report. MEX already has Banxico dual-leg work, ARG has INDEC dual-leg work, and THA has an existing reconciliation script; duplicate work was rejected.
- Official SBV Annual Report 2023 Appendix 4 (USD million) explicitly lists “Portfolio Investment Abroad: Assets” and “Portfolio Investment in Viet Nam: Liabilities”, but the latest displayed annual observations are 2022 and 2023, not Q2-2026. SBV Annual Report 2021 uses the same concepts but is older.
- Official NSO H1/Q2 and Q3/9M 2026 releases were inspected; they provide FDI, securities-market, trade and investment aggregates, but no separate Q2 BOP portfolio asset/liability transaction legs in the inspected content. These aggregates are not substitutes.
- No official Q2-2026 quarterly SBV portfolio transaction values, quarterly export/API route, raw bytes, SHA-256, sign crosswalk or same-vintage evidence were obtained. No annual-to-quarter allocation, no stock/FDI/securities aggregate substitution, no sign flip.
- VNM status: official source-family/labels PASS; Q2 asset/liability NOT_EXTRACTED; quarterly route NOT_ESTABLISHED; sign and vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_VIETNAM_VNM_Q2_2026_SBV_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_CONTINUATION59_20261120.md (commit 8035d1724461c19577ae5f03aa55fcf76acdc3b0).
- Next: search only for a distinct official SBV quarterly BOP release/data export exposing separate Q2-2026 portfolio legs; if absent, preserve VNM PARTIAL and advance to the next unvalidated fixed-cohort country. No IMF re-query/cohort rebuild or production changes.


## Continuation 60 — Paraguay (PRY) Q2-2026 BCP BOP/IIP source-boundary audit (2026-11-20)
- PHL was preflighted and excluded from repeat work: existing BSP report already has raw+parsed capture PASS, release parity PASS, separate asset/liability numeric 2/2 PASS, and bounded vintage review closed as NOT_ESTABLISHED.
- PRY selected from the existing fixed 63-country Q2-2026 dual-leg cohort after repository search found no dedicated PRY national portfolio validation report. No IMF re-query, cohort rebuild or panel rebuild.
- Official BCP BOP/IIP page confirms quarterly and annual dissemination with a three-month lag and exposes the Q2-2026 BOP/IIP XLSX download locator. Exact workbook URL recorded in detail report.
- Web retrieval returned HTTP 400 unsupported XLSX MIME; independent direct byte-download attempt failed. No workbook bytes, sheets, rows, values or SHA-256 captured. No numeric admission, no annual-to-quarter allocation and no net-only substitution.
- PRY status: official quarterly source discovery PASS; exact workbook locator PASS; XLSX bytes BLOCKED; asset/liability NOT_EXTRACTED; sign/units/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_PARAGUAY_PRY_Q2_2026_BCP_BOP_IIP_SOURCE_BOUNDARY_AUDIT_CONTINUATION60_20261120.md (commit 68485ed197f90ba823bea0da5d21bb2df2a16179).
- Next: pursue only a distinct supported XLSX-capable or official BCP API/export route; if unavailable, preserve PRY PARTIAL and advance to the next unvalidated fixed-cohort country. No repeat same-endpoint retries, IMF re-query, cohort rebuild or production changes.


## India Benchmark Panel — Official Source Contract Part 1 (2026-11-20)
- Reopened the India Market Transmission Country Priority Layer and GCR master queue; followed its first dependency: establish the India benchmark/outcome panel before country-specific Tier-0 event capture.
- Official source locator audit completed for NSE NIFTY 50 historical index CSV, NSE sector-index history selector, India VIX history, RBI/FBIL USD-INR reference-rate methodology, RBI 10Y G-Sec Par Yield (FBIL), NSE provisional FPI/DII, NSDL final FPI report families, PPAC Indian Basket crude, Cboe VIX daily history, Federal Reserve broad USD index via FRED (proxy, not DXY), U.S. Treasury daily 2Y/10Y CMT, FOMC event statements, and World Bank monthly commodity Pink Sheet.
- Important limitations: BSE SENSEX EOD/index history is licensed; zero-cost automatic archive rights not established. CCIL indicative yields carry a commercial-use restriction. NSE FPI/DII data are provisional; NSDL latest freshness not verified (inspected example dated 30-Oct-2025). FBIL daily raw export, PPAC report granularity, and all raw-byte/hash capture remain open.
- DEXINUS is a Federal Reserve H.10 New York noon buying rate, weekly-updated, and only a cross-check—not an FBIL replacement. Fed broad trade-weighted USD is not ICE DXY. U.S. Treasury CMTs use indicative bid-side quotes around 3:30 PM ET; record timezone and do not calendar-date-align blindly. World Bank Pink Sheet is monthly, not an H+1 trigger.
- Detail: docs/INDIA_BENCHMARK_PANEL_OFFICIAL_SOURCE_CONTRACT_PART1_20261120.md (initial commit f6bf86267e32acb9d81b654ac4366b1c28dc5589; date correction commit 4cc47fb9e7d3347b9ce92f7282ba0d2c64b96e34).
- Acceptance: source locators mostly PASS with explicit rights/freshness limitations; raw archive/SHA-256 NOT_DONE; synchronized benchmark panel NOT_DONE; causal event study NOT_DONE; production NOT_AUTHORIZED.
- Next exact action: isolated raw capture of NSE NIFTY 50, selected NSE sector indices and India VIX CSV; separately capture U.S. Treasury 2Y/10Y, FRED broad USD and DEXINUS, Cboe VIX, and World Bank monthly Pink Sheet with native timestamps, raw bytes and SHA-256. Keep FBIL/PPAC/FPI freshness and rights gates separate. No production changes.


## India Benchmark Panel — NSE preview fixture / duplicate-row boundary audit Part 2 (2026-11-20)
- Reopened the Part-1 India Benchmark Panel source contract and current GCR queue; inspected official NSE All Reports and NSE Indices Historical Data/FAQ surfaces.
- Official NSE All Reports exposes Historical Index Data and India VIX date-filter controls/download; NSE Indices Historical Data exposes index selectors, date range, CSV output and separate TRI/NTRI data. NSE Indices FAQ states NIFTY 50 historical data available from 03-Jul-1990.
- Critical boundary: embedded page examples are not raw payloads. NIFTY 2019 preview repeats 01-Jan-2019 twice; India VIX preview heading says 01–05 Jan 2019 but displayed observation is 03-Sep-2018 twice; TRI preview repeats 01-Jan-2019. These are page-extraction/preview anomalies, not evidence of duplicate rows in downloadable source CSV. All embedded sample values rejected as ingestion evidence.
- No actual CSV/XLSX/ZIP bytes captured; no SHA-256, raw-payload duplicate test, session coverage test or benchmark panel created. Actual payload status NOT_CAPTURED/NOT_TESTED.
- Detail report: docs/INDIA_NSE_HISTORICAL_PREVIEW_FIXTURE_AND_DUPLICATE_ROW_BOUNDARY_AUDIT_PART2_20261120.md (commit c3fab39f2037f6324cdc147b661dfbf2b4c2c900).
- Next: small isolated capture of actual date-filtered NIFTY 50, broad-market companion and India VIX downloadable payloads; hash before parsing; validate interval, exact/conflicting duplicates, sessions/holidays, schema, OHLC and price-index/TRI identity. If automated route returns HTML/blocks, stop retries and use official manual download route. No silent deduplication or production changes.


## India Benchmark Panel — NSE actual raw-capture feasibility gate Part 3 (2026-11-20)
- Re-fetched the current continuity ledger, GCR queue, and India Benchmark Panel Parts 1–2 before work; reused existing source/preview findings and did not repeat completed locator or fixture audits.
- Reconfirmed official NSE All Reports, Historical Reports directory and NSE Indices Historical Data surfaces. The pages expose date controls and download UI, but the available read-only retrieval interface does not operate the controls or return the selected file bytes.
- No official direct-download/API contract was established from the inspected official pages; third-party endpoint descriptions were not treated as authorization. No undocumented API probe or access-control bypass.
- Actual NIFTY 50, broad-market companion and India VIX raw bytes remain NOT_CAPTURED; headers/MIME/length, file hash, parsed rows and duplicate/session QA NOT_DONE. This is a session execution-bridge limitation, not proof NSE blocks downloads.
- Detail report: docs/INDIA_NSE_ACTUAL_RAW_CAPTURE_FEASIBILITY_GATE_PART3_20261120.md.
- Next exact action: use a supported interactive browser/download route on the official NSE controls, or have the user attach the exact official downloads; hash unchanged bytes before parsing. Keep TRI/NTRI separate. No sample values, no silent deduplication, no production changes.

## India FPI — NSDL Archive public form contract audit (Continuation 76, 2026-11-20)
- Reused existing verified artifact 14524707532 (run 44515445620); downloaded ZIP size 184,876 bytes and independently recomputed SHA-256 29530f3d0913f3eed93afbeb0759ecb8131b4192c71e5928d79961df77c24c69, matching recorded digest.
- Inspected the exact archived NSDL Archive HTML. Identified ASP.NET POST form frmMonthly action ./Archive.aspx; state fields __VIEWSTATE, __VIEWSTATEGENERATOR, __EVENTVALIDATION; date fields txtDate (disabled initial text input) and hdnDate; calendar format %d-%b-%Y; hidden validation/export fields hdnFlag, HdnValexceldata; public postback targets btnSubmit1 (View Report) and btnExcel (Export to Excel).
- Initial GET contains no archive investment rows. Client script reveals the public control flow but not server-side period semantics or output schema. No POST was sent, no stale ViewState replayed, and no archive output or rows claimed.
- Detail report: docs/GCR_NSDL_ARCHIVE_PUBLIC_FORM_CONTRACT_AUDIT_CONTINUATION76_20261120.md.
- Next exact action: with a supported interactive browser, load fresh page state, select one explicit date via calendar, invoke View Report once, capture response bytes/headers/UTC/hash and inspect returned rows. If browser interaction is unavailable, keep archive NOT_DONE and do not guess a POST body. Do not repeat already-PASS capture/digest or 192/192 sector subtotal arithmetic.

## Continuation 77 — CDSL daily 18-Nov-2026 full-table arithmetic QA (2026-11-20)
- Reused existing verified artifact 14527092174 / run 44519322726; ZIP SHA-256 `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd` independently matched.
- Parsed archived official CDSL eServices daily HTML. Detailed cash route/scheme INR arithmetic 17/17 PASS; seven category subtotal identities 7/7 PASS; seven subtotal sums reproduce the published INR gross purchases/sales/net total exactly. USD component aggregation residual +0.0003 USDm is retained as display-rounding residual; published total unchanged.
- CDSL 18-Nov custodian/depository reporting semantics are not aligned to NSDL Latest 19-Nov mixed provisional-T-day/custodian-prior-day presentation. Matched-date provider variance remains NOT_COMPUTABLE.
- Detail report: docs/GCR_CDSL_DAILY_18NOV2026_FULL_TABLE_ARITHMETIC_QA_CONTINUATION77_20261120.md (blob SHA `181e041bc872d96586ead475092432b7bf8f187a`).
- Next: bounded CDSL archive/date-control contract audit using existing raw HTML only; no guessed postback. If unsupported, retain NOT_DONE and move to another independent official source task. Production, CORE-672, Engines A–E, selector/score and fixed 63-country cohort unchanged.


## Continuation 78 — CDSL daily archive static snapshot/freshness audit (2026-11-20)
- Reused verified artifact 14527092174 / run 44519322726; ZIP SHA-256 `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd` matched. Exact archived member `cdsl_daily_archive.html`: 73,784 bytes, SHA-256 `aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df`.
- Manifest proves official GET to `https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx`, HTTP 200, retrieved 2026-11-19T11:57:09.076562Z. Captured HTML contains no forms, inputs, selects, buttons or date/calendar controls.
- Static cash/derivatives headings both end 02-Mar-2026. Cash report contains one daily date plus March, 2026 YTD and cumulative aggregates; not a multi-date daily series. CDSL Latest in same ZIP reports 18-Nov-2026, a 261-calendar-day cutoff gap. Keep derivatives separate.
- Decision: static stale snapshot, no date-control contract in captured HTML; historical daily coverage UNKNOWN/NOT_ESTABLISHED. No hidden endpoint, guessed parameters, challenge bypass or repeat request. Detail report `docs/GCR_CDSL_DAILY_ARCHIVE_STATIC_SNAPSHOT_FRESHNESS_AUDIT_CONTINUATION78_20261120.md` (blob SHA `69597e2fbe40d859bfbccb4af165b6c10959c4a8`).
- Next: if supported interactive browser exists, inspect visible official UI only; otherwise advance to another unfinished official source. CDSL archive daily series excluded; matched-date NSDL/CDSL NOT_DONE; production NOT_AUTHORIZED.


## AO. Japan (JPN) Q2-2026 BOJ/MOF portfolio-flow source contract audit (2026-11-20)
- Selected as an independent India-transmission Tier-0 source-family task, not as a member or replacement of the fixed 63-country IMF EMDE cohort.
- Official BOJ BPM6 page confirms monthly portfolio asset/liability flows, separate asset/liability semantics, quarterly Regional BOP, and portfolio partner-economy coverage described for 45 economies. MOF schedule lists Q2-2026 Regional BOP release on 10-Nov-2026.
- BOJ public API/CSV/JSON capability and date-frequency conventions verified from official manuals. Exact portfolio series IDs, Q2 partner-country values, India row availability, raw bytes/hash and same-vintage status were not retrieved.
- Detail: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md (commit 869e0fe8b91bb48b1f14fed170706e4b834bd76c).
- Status: source-family/contract PASS; exact bilateral extraction NOT_DONE; Japan→India transmission PARTIAL / NOT PASS; production NOT_AUTHORIZED.
- Next: inspect the official 10-Nov-2026 Q2 Regional BOP attachment or BOJ portfolio-by-counterparty series; capture/hash bytes, verify India partner coverage and separate asset/liability legs, and preserve vintage. No guessed API series code or aggregate substitution.


## AP. Japan JPN Q2-2026 — official Regional BOP India-row inspection (2026-11-20)
- Reopened current ledger, queue and Japan source-contract report. Followed the MOF official 10-Nov-2026 Q2 Regional BOP link to the 14-page MOF/BOJ PDF.
- Page 8 Assets and page 9 Liabilities have separate Portfolio Investment columns and an India row; unit is 100 million yen.
- India Q2-2026 asset cell is an em dash (—), not numeric zero; liability cell is 7,526 (100 million yen). No currency conversion.
- Official PDF retrieval/page inspection PASS; raw bytes/hash NOT_DONE because direct byte download failed in this execution environment.
- Japan national dual-leg validation remains PARTIAL / NOT PASS; asset NOT_REPORTED_IN_THIS_TABLE; production NOT_AUTHORIZED.
- Detail report updated: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md.
- Next: inspect BOJ's official 45-economy Portfolio Investment Assets and Liabilities country-breakdown series for India Q2-2026; use exact metadata/series IDs, capture/hash original bytes, and preserve publication vintage. Do not treat dash as zero or infer from aggregate BOP.


## AQ. Japan JPN — BOJ 45-economy monthly portfolio country-breakdown, June 2026 (2026-11-20)
- Reopened current ledger, queue and Japan report; no repetition of Continuation 80's Q2 regional PDF inspection.
- BOJ official documentation: Portfolio Investment Assets Country Breakdown is by issuer economy; Liabilities Country Breakdown by transactor economy; both monthly and cover 45 economies.
- Official MOF June 2026 preliminary Portfolio Investment PDF (bppi202606.pdf), pp.4-5, has India rows in both country-breakdown tables; unit 100 million yen.
- India June Assets: total A 1,379 / D 2,056 / net -677; equity net -691; long-term debt net +14; short-term fields dashes.
- India June Liabilities: total A 1,187 / D 2,773 / net -1,586; equity 0/0/0; long-term debt A dash, D 920, net -920; short-term A 1,187 / D 1,852 / net -665. Components show net -1,585 vs published -1,586; retain published total and flag 1 unit residual. No dash-to-zero promotion.
- Assets component arithmetic matches displayed total. June is preliminary monthly, not Q2; Q2 aggregation and vintage bridge NOT_DONE. PDF bytes/hash not captured.
- Detail report updated in Continuation 81. Next: inspect April/May 2026 monthly portfolio PDFs and vintage, then compare monthly series with 10-Nov-2026 Q2 regional release.
- Production NOT_AUTHORIZED; fixed cohort and production invariants unchanged.


## AR. Japan JPN — April/May 2026 India monthly portfolio asset/liability rows (Continuation 82)
- Official MOF April and May preliminary portfolio PDFs inspected via release-date links. India rows present in both Assets Country Breakdown and Liabilities Country Breakdown for both months; unit 100 million yen.
- April Assets A/D/net 739/1,487/-747; Liabilities 2,070/2,601/-531.
- May Assets 789/1,434/-645; Liabilities 64/1,371/-1,307.
- Combined with June Continuation 81, visible India rows exist for both legs across Apr-Jun. The unadjusted three-month monthly net sums (-2,069 assets; -3,424 liabilities) are not accepted as Q2 totals: preliminary vintage, sign/definition and quarterly bridge are NOT_ESTABLISHED. Q2 Regional BOP asset dash and liability 7,526 remain separately reported; no reconciliation inferred.
- No PDF raw bytes/hash captured. Production NOT_AUTHORIZED; fixed 63-country cohort and production invariants unchanged.
- Detail: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md, Continuation 82.
- Next: official historical/revised-vintage and definition bridge; if absent, keep monthly and quarterly series separate.


## AS. Japan JPN — official revision-vintage and partner-classification boundary (Continuation 83)
- MOF: Preliminary/Second Preliminary monthly PDFs are temporary; latest values are in Historical Data; annual BOP revision each April.
- BOJ: monthly portfolio assets classified by issuer economy; liabilities by transactor economy (45 economies each). Monthly preliminary release lag two months; Regional BOP quarterly release lag five months. Monthly portfolio annual revision in April of following two years; Regional BOP annual revision in May of following two years.
- Q2-2026 Regional BOP released 10-Nov-2026; no assumption of same-vintage with April/May/June monthly preliminary PDFs. Liability counterparty may reflect foreign transactor/custodian, not ultimate investor residence.
- Monthly arithmetic sums (-2,069 assets; -3,424 liabilities) not validated Q2 values. Quarterly asset dash is not zero; liability 7,526 remains separately recorded.
- BOJ monthly/quarterly ZIP flat-file links identified but ZIP retrieval failed in current environment; raw bytes/hash and exact India series IDs remain NOT_DONE.
- Detail report: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md, Continuation 83.
- Status: policy/definition boundary PASS; same-vintage reconciliation NOT_ESTABLISHED; raw capture and exact codes NOT_DONE; production NOT_AUTHORIZED.
- Next: supported ZIP-capable retrieval of BOJ flat files + code/specification list; verify India series codes/values before any join.


## AT. Japan JPN — BOJ BP01 API/flat-file retrieval bridge (Continuation 84)
- Official BOJ API manual specifies BP01 metadata `getMetadata` and exact series `getDataCode` endpoints; CSV/JSON; daily-updated metadata; request limits 250 series and 60,000 points.
- Official series-code XLSX URL identified: https://www.boj.or.jp/en/statistics/br/bop_06/data/exbpsm6a.xlsx . Official flat-file ZIPs identified: https://www.stat-search.boj.or.jp/info/bp_m_en.zip and https://www.stat-search.boj.or.jp/info/regbp_q_en.zip .
- Official statistics taxonomy confirms monthly portfolio asset/liability country-breakdown totals and instrument subseries; quarterly Regional BOP includes India. This is not exact code/value proof.
- XLSX/ZIP retrieval rejected by current web/container bridge; API metadata endpoint inaccessible through current bridge; no raw bytes/hash, exact India series codes or values captured. No guessed codes.
- Detail: Japan report Continuation 84. Status: API contract/taxonomy PASS; exact series codes/data NOT_DONE; same-vintage reconciliation NOT_ESTABLISHED; production NOT_AUTHORIZED.
- Next: supported API/HTTP client or user-provided official BOJ files; fetch metadata, identify exact India codes, retrieve and hash exact observations before parsing.


## AU. Japan JPN — BOJ monthly 45-economy vs quarterly 33-economy partner universe (Continuation 85)
- Official BOJ confirms monthly portfolio asset/liability country breakdown covers 45 economies; quarterly Regional BOP covers 33. India is included in both, but universes are distinct.
- Monthly asset country attribution = issuer economy; monthly liability = transactor economy; quarterly Regional BOP remains a separate partner-economy product.
- BP01 metadata API call via current retrieval bridge returned inaccessible/no body. Public main time-series table is only broad account net balances, not portfolio country breakdown. No guessed codes.
- Status: universe distinction PASS; exact India series IDs/data/raw hash NOT_DONE; cross-product equivalence NOT_ESTABLISHED; production NOT_AUTHORIZED.
- Detail report Continuation 85. Next: supported HTTP/API client or official metadata CSV upload; hash raw metadata, identify exact codes and query separate monthly/quarterly observations.


## AV. Moldova MDA — BNM Q2-2026 detailed BPM6 BOP source gate (Continuation 86)
- MDA confirmed in existing fixed 63-country Q2-2026 both-leg cohort; no rebuild/IMF re-query. No dedicated MDA dual-leg report found in repository.
- Official BNM Q2 release (30-Sep-2026) shows portfolio investment only as net EUR -24.9m; separate asset/liability legs are not in the release graphic.
- BNM official detailed BPM6 interactive report generator has quarter/year/currency selectors, Generate/Export controls, Statistical Series and Metadata tabs. Current read-only extraction cannot execute controls or return generated export bytes.
- Q2 XLSX locator found, but raw bytes/hash and exact series not captured. MDA remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_MOLDOVA_MDA_Q2_2026_BNM_DETAILED_BOP_SOURCE_GATE_CONTINUATION86_20261120.md.
- Next: supported interactive browser export or user-supplied official BNM Q2 workbook; capture/hash untouched bytes, extract separate asset/liability series and definitions. Do not infer legs from net -24.9m.


## AW. Morocco MAR — Office des Changes Q2-2026 dual-leg extraction and IMF exact-row diagnostic (Continuation 87)
- MAR selected from existing fixed 63-country Q2-2026 both-leg cohort after preflight; no prior MAR dedicated report found. MDA Continuation 86 was not repeated; its interactive-export blocker remains recorded.
- Official Office des Changes Q2-2026 preliminary BOP PDF, million MAD, explicitly reports net acquisition of assets +4,848, net incurrence of liabilities +36,933 and balance -32,085. Component arithmetic and balance identity all exact at published precision.
- Ministry DSBB summary separately shows assets +4,848 and liabilities -36,933; the latter is an alternate signed presentation, not a second observation.
- Existing IMF panel artifact reused (run 44474218174 / artifact 14505862034; ZIP SHA 1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f). Correct MAR Q2 raw rows (verified by exact COUNTRY=MAR filter): A_NFA_T +523,948,820.8007525 USD; L_NIL_T +3,991,543,275.295832 USD, both ACTION=R, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
- Correct MAR asset/liability directions agree with Office des Changes explicit net acquisition/net incurrence signs. Earlier MDA rows copied into MAR and asset-sign-conflict statement are withdrawn; see Continuation 88 correction.
- MAD/USD Q2 conversion convention and observation-vintage bridge not established; no numeric FX comparison. National PDF raw bytes/hash not captured.
- MAR national dual-leg extraction/arithmetic PASS; IMF exact-row recovery/country-key correction PASS; directional agreement PASS; FX comparison NOT_DONE; same-vintage NOT_ESTABLISHED; MAR PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_MOROCCO_MAR_Q2_2026_OFFICE_DES_CHANGES_IMF_DUAL_LEG_SOURCE_RECONCILIATION_CONTINUATION87_20261120.md.
- Next: official MAD/USD Q2 convention and Office des Changes BPM6 sign methodology, then numeric separate-leg comparison and vintage bridge. No re-query or cohort rebuild.


## AX. Morocco MAR — Continuation 88 country-key correction and independent QA
- Critical correction: Continuation 87 mistakenly copied exact IMF MDA values into MAR section. Reopened existing hash-verified artifact and filtered exact COUNTRY=MAR, TIME_PERIOD=2026-Q2, BOP_ACCOUNTING_ENTRY.
- Correct MAR rows: A_NFA_T +523,948,820.8007525 USD; L_NIL_T +3,991,543,275.295832 USD; both ACTION=R, SCALE=6, PRECISION=6, DERIVATION_TYPE=O. ZIP and panel SHA independently recomputed and matched.
- Correct MAR IMF asset/liability directions are positive and directionally agree with Office des Changes +4,848/+36,933 million MAD. Previous asset sign-conflict claim withdrawn. No numeric MAD/USD comparison absent official conversion convention/vintage.
- Detail report corrected in place with Continuation 88 correction note. MAR remains PARTIAL / NOT PASS; FX comparison NOT_DONE; same-vintage NOT_ESTABLISHED; aggregate NOT_AUTHORIZED.
- Lesson: exact country + period + accounting-entry assertions before copying archived rows into a country report.


## AY. V11.4 — Forward-Label V2 research-only acceptance specification (Continuation 89)
- Added docs/V11_4_FORWARD_LABEL_V2_RESEARCH_ONLY_ACCEPTANCE_SPEC_CONTINUATION89_20261120.md (commit 099bc6ec6edc51af0897a985b4226b703781628f).
- Defines exact T+1..T+h exchange-session joins, full-window maturity, explicit incomplete/quarantine states, point-in-time identity and feature/vintage leakage gates, corporate-action/duplicate handling, denominator conservation, canonical row-ledger serialization, exact JSON/CSV count parity and independent metric recomputation.
- Makes prior H+5 JSON/CSV 613-vs-616 count mismatch a mandatory gate; preserves H+3 >=50 fully matured observations per State; DATA_CONTAMINATED remains UNKNOWN/quarantined.
- Test-only fixtures cannot enter market metric denominators. Jobs <10 minutes. No new data collection or workflow dispatch.
- Specification only; implementation and production admission remain NOT_AUTHORIZED pending explicit user approval and all acceptance gates. Existing V11.4 remains BLOCKED / NOT_ADMISSIBLE; V11.3 and GCR remain closed under their own gates.


## AZ. V11.4 — Forward-Label V2 specification independent review (Continuation 90)
- Added docs/V11_4_FORWARD_LABEL_V2_SPECIFICATION_INDEPENDENT_REVIEW_CONTINUATION90_20261120.md (commit 6e8681739faf02ae06716a7b52c9521ff41c6c61).
- Independent document-level review against the general rolling-backtest acceptance contract: 12/12 checklist items PASS (source provenance, session spine/identity, maturity, leakage, real-row hand-check, denominator, JSON/CSV parity, independent recomputation, H+3 >=50 per-State, runtime, v1/v2 isolation, approval boundary).
- Document review only; no implementation/test/data/metrics verification. H+5 613-vs-616 mismatch remains unresolved.
- Implementation NOT_AUTHORIZED pending explicit user approval; V11.4 remains BLOCKED / NOT_ADMISSIBLE; production NOT_AUTHORIZED.


## BA. Morocco MAR — official FX and BPM6 sign methodology (Continuation 91)
- Added docs/GCR_MOROCCO_MAD_USD_FX_AND_BPM6_SIGN_METHODOLOGY_AUDIT_CONTINUATION91_20261120.md (commit a8ecc9189d2f589cfce5d6fa57eebf248c80dac1).
- IMF SDDS Morocco metadata and Office des Changes 2019 methodology confirm BPM6 financial-account columns are net acquisition of assets / net incurrence of liabilities and transactions are recorded net, primarily at settlement. IMF BPM6 confirms increases in assets/liabilities positive, decreases negative; financial-account balance assets minus liabilities.
- BAM 2024 official USD/MAD reference methodology: volume-weighted interbank trade average 08:30–15:30 when thresholds met; otherwise 5-minute median bid/ask midpoint averages; daily publication at 16:15; possible same-day republication. Crucially BAM states reference rates are mainly for revaluation and not intended as FX transaction reference.
- BAM API portal lists Cours de change V1, but no historical Q2 raw series/revision metadata or Office des Changes flow conversion convention established. No unsupported quarterly conversion made.
- MAR national and corrected IMF asset/liability directions agree under BPM6 increase-positive semantics. Magnitude comparison NOT_DONE; same-vintage NOT_ESTABLISHED; MAR PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: find explicit Office des Changes transaction FX conversion rule; if unavailable, advance to next cohort member without inferred conversion.


## BB. Morocco MAR — BOP vs settlement FX conversion scope (Continuation 92)
- Added docs/GCR_MOROCCO_Q2_2026_TRANSACTION_FX_CONVERSION_SCOPE_AUDIT_CONTINUATION92_20261120.md (commit bf6af30f4a4623f9a590405b3d31e51a0d8d6748).
- Official settlement-balance methodology records MAD countervalue using rate applied at payment execution, but explicitly distinguishes actual settlements from BOP transactions whether settled or deferred. This rule cannot be applied wholesale to portfolio BOP flows.
- Current Office des Changes BPM6 report says bank settlement data are principal financial-account source, but no portfolio-specific foreign-currency conversion rule found in inspected methodology. BAM daily reference rate is not accepted as proxy.
- No conversion computed; MAR remains PARTIAL / NOT PASS; numeric comparison NOT_DONE; same-vintage NOT_ESTABLISHED; aggregate/production NOT_AUTHORIZED.
- Next: portfolio-investment metadata/technical fiche; if it does not specify the rate rule, close MAR conversion as NOT_ESTABLISHED and move to next fixed cohort member.


## BC. Morocco MAR — portfolio metadata and current BOP presentation (Continuation 93)
- Official 2013 “Compte d’opérations financières” metadata records a historical gross credit/debit national-application statement despite BPM6 net-flow recommendation; its date is 14-Oct-2013.
- Current Office des Changes 2024 annual report p.59 states financial account net assets/liabilities presentation; p.60 defines portfolio as negotiable equity/debt securities; p.36 reports net portfolio assets +4,864 MDH, liabilities +3,886 MDH, balance +978 MDH. Current evidence supports net presentation. Preserve old fiche as historical/version conflict.
- Related portfolio-specific metadata fiche link (details/87) timed out; no currency/valuation/FX conversion convention obtained. Official flow-chronology metadata says national recording at settlement, accrual when available; not an FX rule.
- No MAD/USD conversion, no BAM proxy, no arithmetic mean or quarter-end rate. MAR remains PARTIAL / NOT PASS; FX convention NOT_ESTABLISHED; numeric comparison NOT_DONE; same-vintage NOT_ESTABLISHED; aggregate/production NOT_AUTHORIZED.
- Report create response commit c86b71dd38d21ce9312be470cf1c41f251ceb7b2, but subsequent path fetch 404 and retry 422 requiring sha; report artifact not independently verified. Findings and limitations are preserved here.
- Decision: close this public metadata route as NOT_ESTABLISHED and advance fixed cohort. Revisit only on a new current versioned official portfolio fiche/FX methodology.


## BD. Nepal NPL — NRB BPM6 byte-route closure (Continuation 94)
- Added docs/GCR_NEPAL_NPL_Q2_2026_NRB_BPM6_BYTE_ROUTE_CLOSURE_CONTINUATION94_20261120.md (commit 3d578a8d292a8373f40403094752e297c031b2b5).
- NRB External Sector BPM6 workbook locator remains official, but web XLSX retrieval and separate byte-download route both blocked. No workbook bytes/hash/sheets/values. NSDP XML is stale 2024-Q1; Monthly Banking & Financial Statistics is wrong source family and remains rejected.
- NPL remains PARTIAL / NOT PASS; Q2 legs not extracted; period basis/sign/unit/vintage NOT_ESTABLISHED; aggregate/production NOT_AUTHORIZED.
- Exact URL route closed; do not repeat without a new supported mechanism. Advance fixed cohort to next eligible member after preflight. No IMF query or cohort rebuild.


## BE. Romania ROU — BNR/ECB Q2-2026 portfolio source gate (Continuation 95)
- ROU is present in the immutable 63-country Q2-2026 both-leg cohort; repository search found no dedicated ROU national dual-leg report. Selected after NPL Continuation 94 closed the exact NRB XLSX route.
- IMF SDDS/DQAF confirms BNR as compiler, BPM6, separate net asset/liability dissemination, quarterly release timing and ongoing revisions. ECB BPS catalogue exposes Romania monthly portfolio-liability transaction series with National Bank of Romania as source; monthly collection indicator says “summed through period”. Inspected quarterly transaction listing was last updated 17-Apr-2026, before Q2.
- Exact ECB SDW API asset/liability CSV requests for Apr-Jun 2026 both inaccessible via current bridge. No bytes, values or hashes; no Q2 national observations admitted. ROU PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_ROMANIA_ROU_Q2_2026_BNR_ECB_PORTFOLIO_SOURCE_GATE_CONTINUATION95_20261120.md (commit 4157f08081d19e8876ad1561e4f8f293157230e7; verified blob SHA 37f744511aeab33539d1fca15be0bce08536cd90).
- Next: supported official BNR/ECB retrieval of both separate Q2 legs with raw-byte hash and vintage; do not sum monthly rows without confirmed flow semantics. Reuse archived IMF rows; no IMF query/cohort rebuild.


## BF. Romania ROU — ECB/BNR methodology and retrieval boundary (Continuation 96)
- New official IMF DSBB metadata confirms BNR portfolio coverage is partial due incomplete external-custodian information.
- ECB 2025 BOP/IIP e-book §7.3 states Romania uses monthly security-by-security stocks and derives monthly portfolio flows from stock changes, with price, FX and other changes separately compiled; assets use CSDB reference data; external-custodian-held Romanian debt securities are not covered; liabilities use residual approach and SHSDB inputs.
- Exact ECB API asset/liability retrieval for Q2-2026 remains blocked; asset portal metadata only and liability page 503; no raw bytes/hash/values. ROU PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_ROMANIA_ROU_Q2_2026_ECB_BNR_METHODOLOGY_RETRIEVAL_BOUNDARY_CONTINUATION96_20261120.md (commit ba48066871b9fc5c0cb279b933abc25232d1f175; verified blob SHA 6f3c046255ada664589286bdae276606588cc9a4).
- Close current identical ECB API route. Revisit only on a new supported BNR interactive/data-set or byte-preserving ECB route. Continue fixed cohort only after next-country preflight; no IMF re-query or cohort rebuild.


## BG. Rwanda RWA — BNR Q2-2026 portfolio source gate (Continuation 97)
- RWA selected as next country after ROU from immutable 63-country Q2-2026 cohort. Preflight checked current Master Ledger, GCR queue, cohort and ROU 95/96 reports; no dedicated RWA report existed. No cohort rebuild or IMF re-query.
- BNR External Sector Statistics page says BOP/IIP is BPM6 and lists a Balance of Payment item dated 30-Jun-2026; JavaScript portal prevented exact file URL/bytes resolution.
- BNR Annual Report 2024-2025 Appendix 14 has fiscal-year separate portfolio assets/liabilities in USDm; FY2024/25 12.1 / 6.3, net 5.8; FY2022/23 50.2 / -58.4, net 108.6. Historical arithmetic diagnostic only; not Q2 data and not a proven IMF key bridge.
- BNR October 2026 MPFSS Table 12 has 2026H1 net-only portfolio +14 USDm; no separate legs or Q2. Direct annual PDF byte download failed; no raw-file SHA/receipt.
- RWA Q2 national asset/liability observations NOT_CAPTURED; comparison NOT_DONE; PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_RWANDA_RWA_Q2_2026_BNR_PORTFOLIO_SOURCE_GATE_CONTINUATION97_20261120.md (commit ef71745ec25c570886974883bbe9cd194cba2547; verified blob SHA af725eba157789e16e65a783e886d96f66fdc727).
- Next: supported retrieval of BNR 30-Jun-2026 BOP dataset, raw-byte archival and separate leg inspection. No FY proration, net inference, IMF re-query or cohort rebuild.


## BH. Rwanda RWA — official source-family rejection / quarter-boundary audit (Continuation 98)
- New NISR official Q2-2026 external goods trade report found (exports 548.98, imports 1,606.39, re-exports 179.59, trade balance -877.81 USDm). Rejected for portfolio BOP legs: goods trade is the wrong source family.
- BNR August MPFSS is Q1 summary without portfolio legs; October MPFSS is H1 net-only +14 USDm; both rejected for Q2 dual-leg comparison. BNR 30-Jun-2026 BOP portal item remains JS-only; exact locator/bytes unresolved.
- RWA remains PARTIAL / NOT PASS; Q2 A_NFA_T/L_NIL_T NOT_CAPTURED; comparison NOT_DONE; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_RWANDA_RWA_Q2_2026_OFFICIAL_SOURCE_FAMILY_REJECTION_CONTINUATION98_20261120.md (commit 1f8997f5c491f62c494fb77494ce1a43537fedcf; verified blob SHA 001cc1fc2d6f698566206a7e746871d9eba1ee90).
- Close identical JS-only route; advance only after fixed-cohort preflight if no new supported BNR direct dataset/API. No IMF re-query or cohort rebuild.


## BI. Solomon Islands SLB — CBSI Q2-2026 portfolio source/sign-conflict audit (Continuation 99)
- SLB is next after RWA in fixed 63-country Q2 cohort; both IMF legs present. Preflight checked current Master Ledger, GCR queue, RWA Continuation 98, cohort and existing SAU report; no duplicate SLB report. No cohort rebuild/IMF re-query.
- CBSI official BOP page states BPM6 and quarterly/annual BOP; latest 2026-Q2. June 2026 Quarterly Review Table 1.17 (SBDm) reports Q2 portfolio financial assets +38 and liabilities dash/nil.
- Chapter IV narrative instead describes portfolio investment as deficit SBD 38m. Unresolved internal sign/presentation conflict; do not flip sign or infer IMF leg mapping. Table 1.14 portfolio IIP assets 373 SBDm is a stock and not a flow.
- Archived IMF panel fetch for large file returned empty content (blob SHA 2a8db2878cac6323bbad74ffa4035dc70e5e6b98); no exact SLB IMF rows captured and no new IMF query. CBSI PDF byte download failed; no SHA. FX/vintage bridge not established.
- Report: docs/GCR_SOLOMON_ISLANDS_SLB_Q2_2026_CBSI_PORTFOLIO_SOURCE_SIGN_CONFLICT_CONTINUATION99_20261120.md (commit 0552b4e1f7aa429c1e0c213235b7d5f25fa007e7; verified blob SHA 7a696af5f0562941f59363d10bb6b58199319049).
- SLB PARTIAL / NOT PASS; comparison NOT_DONE; aggregate NOT_AUTHORIZED. Next: official CBSI sign-methodology note, exact archived IMF row retrieval without re-query, transaction FX/vintage bridge, raw PDF archival. Do not admit until conflict resolved.


## BJ. El Salvador SLV — BCR Q2-2026 portfolio source-family gate (Continuation 100)
- SLV is next after SLB in immutable 63-country Q2 cohort; both IMF legs present. Preflight checked current Master Ledger, GCR queue, SLB report, exact-sample receipt and cohort; no dedicated SLV report found. No cohort rebuild/IMF re-query.
- BCR June-2026 financial statement has USD-thousand “Inversiones en el Exterior (Neto)” balance-sheet stocks (Mar 3,834,678.3; Jun 4,233,089.5). Rejected as BOP transactions; stock difference is not a transaction.
- IMF staff 2025 EFF/Article IV annual BPM6 BOP table includes separate portfolio assets/liabilities but is annual and partly staff-estimated; context only, not Q2 national data.
- Existing exact sample excludes SLV; large panel fetch empty; exact IMF rows NOT_CAPTURED. Q2 national asset/liability NOT_CAPTURED; SLV PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_EL_SALVADOR_SLV_Q2_2026_BCR_PORTFOLIO_SOURCE_FAMILY_GATE_CONTINUATION100_20261120.md (commit 94cec1b68b19e8fef099bc4ccbf2083cfaa7a286; verified blob SHA 658b83d795529e9eecd99879039e6e8bcdb6a8c3).
- Next: BCR official Q2 BOP dual-leg table; raw bytes/vintage/SHA-256; retrieve archived IMF exact rows without re-query. No stock-as-flow or annual proration.


## BK. Serbia SRB — NBS BPM6 Q2-2026 portfolio dual-leg source gate (Continuation 101)
- SRB is the next member after SLV in the immutable 63-country Q2-2026 both-leg cohort; no dedicated SRB national dual-leg report found in preflight. Re-fetched Master Ledger, GCR queue, SLV Continuation 100 and cohort; no cohort rebuild or IMF re-query.
- NBS Statistical Bulletin September 2026, Table 2.3, page 105, is an official BPM6 monthly BOP table in EURm with separate portfolio asset and liability transaction rows; data are preliminary and subject to revision.
- Q2 sums from monthly rows: assets Apr +149, May -25, Jun +124 = **+248 EURm**; liabilities Apr -19, May +3,932, Jun +199 = **+4,112 EURm**; net row Apr +168, May -3,957, Jun -75 = **-3,864 EURm**. Identity 248−4,112=-3,864 and monthly net sum agree.
- The unusual May liability +3,932 EURm is retained exactly as published and requires independent verification against the NBS downloadable series/subsequent vintage. No silent correction, net-to-leg inference or sign transform.
- Exact IMF archived SRB rows NOT_CAPTURED; raw PDF bytes/byte count/SHA-256 NOT_CAPTURED; IMF concept/sign bridge and same-vintage alignment NOT_ESTABLISHED; two-leg comparison NOT_DONE. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_SERBIA_SRB_Q2_2026_NBS_BPM6_PORTFOLIO_DUAL_LEG_SOURCE_GATE_CONTINUATION101_20261120.md (create commit a2ae592c6416ee54786be29c684f8bf753056312).
- Next: raw-byte archive/hash official NBS PDF; independently verify May liability value and any subsequent revision; retrieve exact archived IMF SRB rows without new query; establish official sign/concept/vintage bridge and compare legs separately.
- ₹0; no cohort rebuild, IMF re-query, stock-as-flow, net-to-leg inference, FX inference, sign flip or production changes. UNKNOWN is never PASS.


## BL. Serbia SRB — archived IMF exact Q2-2026 dual-leg extraction (Continuation 102)
- Preflight re-fetched Master Ledger (blob SHA c57d93a381c4a6cee039c0d2bd58f64410c33aae), GCR queue (blob SHA 4281684d9c879c1ce62ca8a8ececebf3ac365c6b), SRB Continuation 101 (blob SHA ca0eb8844ab9d14a378f4278506f363fdf776c65), and immutable cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8). NBS Q2 extraction/arithmetic already complete; no repeat.
- Previous large-file fetch returned empty, but the existing archived IMF normalized panel blob SHA `2a8db2878cac6323bbad74ffa4035dc70e5e6b98` was retrieved successfully via Git blob SHA (1,849,027 characters). No IMF query, no cohort rebuild.
- Exact SRB 2026-Q2 rows captured: A_NFA_T raw 288,993,091.8400176 USD, SCALE=6 => USD 288.9930918400176m; L_NIL_T raw 4,782,903,852.31975 USD, SCALE=6 => USD 4,782.90385231975m. Both Q/P_F. Embedded source file SHA256s: asset 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e; liability 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba.
- NBS Q2 EURm remains +248 assets / +4,112 liabilities / -3,864 net. September bulletin itself confirms May liabilities +3,932 EURm; this is same-document confirmation only, not independent later-vintage verification.
- USD↔EUR transaction conversion basis, sign/concept mapping and same-vintage alignment remain NOT_ESTABLISHED; separate-leg comparison NOT_DONE. NBS raw PDF bytes/hash NOT_CAPTURED. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_SERBIA_SRB_Q2_2026_ARCHIVED_IMF_EXACT_DUAL_LEG_ROW_EXTRACTION_CONTINUATION102_20261120.md (create commit daed219c211da0290f74c1c5c27af11723adbeb3).
- Next: independent NBS May observation/vintage check; capture PDF bytes/hash; establish official transaction FX/sign/concept bridge; then compare legs separately.
- ₹0; no IMF re-query, no cohort rebuild, no inferred FX, no sign flip, no net-to-leg inference, no production changes. UNKNOWN is never PASS.


## BM. Serbia SRB — NBS BPM6 sign / transaction-FX methodology and later-vintage route (Continuation 103)
- Preflight re-fetched Master Ledger (blob SHA bd4259ad6176cbbcd0d481c12c012efff63f7493), GCR queue (blob SHA 250e3cce04832837cf942b6cd285c62db825b7a2), SRB Continuation 102 (blob SHA 874f1908814137b67c0d4032752b73dd3a29e207), and Continuation 101 (blob SHA ca0eb8844ab9d14a378f4278506f363fdf776c65). Excluded all completed cohort, NBS Q2 extraction/arithmetic and IMF row retrieval work.
- Official NBS BPM6 Explanatory Notes state original-currency transactions are converted to reporting currency using the official NBS middle exchange rate on the transaction date; increases in assets/liabilities are positive, decreases negative; net=assets−liabilities; portfolio includes <10% equity and debt securities.
- NBS-side sign convention PASS; NBS transaction-date FX methodology PASS. This does not produce an exact conversion of aggregate quarterly EUR totals to IMF USD totals; no transaction-level amounts/dates in the monthly aggregate table, so no generic monthly/quarterly FX substitution.
- NBS official BOP page lists September 2026 monthly BPM6 XLS and detailed XLS; 18-Nov-2026 September developments also listed. This is a later vintage candidate for May 2026 revision check. Current retrieval bridge rejected XLS content type (400 unsupported); no workbook bytes/sheets/values/hash. May revision NOT_DONE.
- IMF A_NFA_T/L_NIL_T mapping and same-vintage alignment remain NOT_ESTABLISHED; exact IMF rows remain CAPTURED in Continuation 102. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_SERBIA_SRB_Q2_2026_NBS_BPM6_SIGN_FX_METHODOLOGY_AND_REVISION_ROUTE_CONTINUATION103_20261120.md (create commit 97226fa883b88f0546b4b72e92ae10fa602c731f).
- Next: obtain NBS September 2026 XLS and detailed XLS via byte-preserving route; verify May 2026 revised observations; retrieve IMF metadata for exact sign/concept mapping; do not FX-convert EUR aggregates with a generic rate.
- ₹0; no IMF query, cohort rebuild, synthetic data, inferred FX, sign flip or production changes. UNKNOWN is never PASS.


## BN. Serbia SRB — IMF BPM6 A/L + portfolio code bridge; NBS Sep-2026 vintage evidence limit (Continuation 104)
- Preflight re-fetched Master Ledger (blob SHA e0a7e5641a17363311ce4372f75fba5369be6f73), GCR queue (blob SHA 0888f0895bfd817cbda671d4e9831ed09d5af032), SRB Continuation 103 (blob SHA a6a19a1521d8c405c25cd1e8129912fdc2c80d61), Continuation 102 (blob SHA 874f1908814137b67c0d4032752b73dd3a29e207), and Continuation 101 (blob SHA ca0eb8844ab9d14a378f4278506f363fdf776c65). Excluded completed NBS sign/FX method, Q2 aggregation and IMF exact row extraction.
- Official IMF BPM6 Compilation Guide Appendix 7 A7.7 states accounting-entry codes N=net, A=assets, L=liabilities; Table A7.2 identifies 3B=Portfolio investment. IMF BPM6 Manual 6.54 defines portfolio investment as cross-border debt/equity securities other than direct investment/reserve assets. This supports standards-level semantic mapping of archived A_NFA_T/L_NIL_T with P_F to NBS separate portfolio assets/liabilities; national scope/timing/valuation equivalence remains NOT_ESTABLISHED.
- Official NBS September developments PDF (dated 18-Nov-2026, 7 pages) inspected; reports Jan-Sep 2026 net portfolio inflow EUR 4.4bn. Context only; no separate May monthly legs or revision values. No net-to-leg inference.
- NBS monthly and detailed XLS links still return 400 unsupported content-type application/vnd.ms-excel; no workbook bytes/sheets/values/hash. May revision NOT_DONE.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_IMF_BPM6_CODE_BRIDGE_AND_LATER_VINTAGE_LIMIT_CONTINUATION104_20261120.md (create commit 43cbf03ef895535ad10d05cd56673012d3b86a9d).
- Updated gate: standards-level IMF/NBS semantic bridge PASS; national coverage/timing/valuation equivalence NOT_ESTABLISHED; exact IMF rows CAPTURED; May later-vintage legs NOT_CAPTURED; USD/EUR transaction-weighted bridge NOT_ESTABLISHED; dual-leg comparison NOT_DONE; SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: byte-preserving official XLS/CSV retrieval; May revision check; transaction-weighted FX or official USD presentation; then separate leg comparison.
- ₹0; no IMF query, cohort rebuild, generic FX, net inference or production changes. UNKNOWN is never PASS.


## BO. Serbia SRB — NBS alternate public data-route audit / next vintage gate (Continuation 105)
- Preflight re-fetched Master Ledger (blob SHA 554fa175e22b21db928da579a05ffc63d267fda0), GCR queue (blob SHA ca9822d94a496ec27b5665d2c223c548b800a7fa), Continuation 104 (blob SHA fd1253e3c6f9b2681a825a756c4a88252f83ee80). PASS work skipped.
- NBS BOP page exposes September 2026 monthly and detailed BPM6 XLS workbooks; both XLS routes still fail web retrieval with HTTP/tool-side 400 unsupported content type. No workbook bytes/sheets/values/hash captured.
- NBS Statistical Bulletin “Data series in XLS format” link resolves to generic Statistics landing page; no separately exposed CSV/HTML monthly BOP flow series or official USD separate-leg series found in inspected public page/search results. This is a scoped NOT_FOUND, not proof that no archive endpoint exists.
- Official release calendar lists 3-Dec-2026 for October 2026 Statistical Bulletin; future vintage only, not current evidence.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_NBS_ALTERNATE_DATA_ROUTE_AND_NEXT_VINTAGE_GATE_CONTINUATION105_20261120.md (create commit d82302447ca36e0700af3de96d5c0f8561d0340d).
- May 2026 later-vintage separate legs NOT_CAPTURED; USD bridge NOT_ESTABLISHED; national scope/timing/valuation equivalence NOT_ESTABLISHED; SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: inspect NBS archive form's underlying endpoint via approved byte-preserving route; re-check October 2026 bulletin after scheduled 3-Dec-2026 release; no currency assumption or generic FX.
- ₹0; no IMF re-query, cohort rebuild, synthetic data, generic FX, net-to-leg inference or production changes. UNKNOWN is never PASS.


## BP. Serbia SRB — NBS archive form schema / authenticated web-service gate (Continuation 106)
- Preflight re-fetched Master Ledger (blob SHA b3d818fa8ad5d5ea3a2c5c2efad82cdd7c222edc), GCR queue (blob SHA aa260f77f4a282db6246ebdd6ecc147a1b2489eb), Continuation 105 (blob SHA 916a9d07c1e15f36a24bfe3d28b11c7958e6c90a). PASS work excluded.
- Official NBS BOP page confirms two archive UI forms (monthly BPM6 and detailed BPM6), each shown as Select + five Input controls + Show. Web text extraction does not expose DOM field names, option values, form action, query params or generated download URL. No endpoint guessed.
- Official NBS web-service system requires completed/certified application; NBS issues username/password/licence code after account creation. This is an authenticated route, not used; no application/contact made. Whether the archive UI requires those credentials remains UNKNOWN.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_NBS_ARCHIVE_FORM_AND_WEBSERVICE_ACCESS_GATE_CONTINUATION106_20261120.md (create commit b7309fd69b0783ca4bdc6a4bea9c2de34b6bec40).
- XLS bytes/sheets/values/hash and May later-vintage separate legs NOT_CAPTURED; USD series NOT_LOCATED; transaction FX bridge NOT_ESTABLISHED. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: inspect live archive form DOM and submission with actual browser capability; capture XLS bytes before parsing; do not apply for authenticated service absent explicit authorization.
- ₹0; no IMF re-query, cohort rebuild, synthetic data, generic FX, net inference or production changes. UNKNOWN is never PASS.


## BQ. Serbia SRB — NBS July-2026 Statistical Bulletin prior-vintage candidate (Continuation 107)
- Preflight re-fetched Master Ledger (blob SHA 761c100c418e2c7c003df0e46952deeebac34bba), GCR queue (blob SHA dbec3cfe50a6c13022252c0cf687d15620884368), Continuation 106 (blob SHA e5994fc9b1318aaa5b4cc4c4db8aaa1f91106b30). PASS work excluded.
- New official NBS July-2026 Statistical Bulletin PDF located: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf; 156 pages; Table 2.3 printed p.105. PDF text extraction returns portfolio asset/liability rows, including a 3,932 value in one extracted liability row.
- Exact month/header alignment could not be re-opened because PDF header/page screenshot fetch timed out. Therefore whether 3,932 in July vintage is May 2026 is NOT_VERIFIED; no cross-vintage PASS. September 2026 Table 2.3 May +3,932 EURm remains existing evidence.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_NBS_JULY_BULLETIN_PRIOR_VINTAGE_CROSSCHECK_CONTINUATION107_20261120.md (create commit e952b837e44f686b76218504214da85de2b4022e).
- Next: recover July Table 2.3 header row/page image, verify month for 3,932; compare July and September vintages separately. XLS raw capture and USD/EUR bridge remain open.
- ₹0; no IMF query/cohort rebuild, synthetic data, generic FX, net-to-leg inference or production changes. UNKNOWN is never PASS.


## BR. Serbia SRB — July Bulletin Table 2.3 header recovery gate (Continuation 108)
- Preflight re-fetched Master Ledger (blob SHA 698a63e3efe4d1a77aa60f097e38d7f594e62a6f), GCR queue (blob SHA 7c6bc3b48199d8523c040edb9513a58c48afba83), Continuation 107 (blob SHA d7c063d63b2b8a19ff94c6b4fd31a82de98e7729). Completed PASS work skipped.
- July 2026 NBS Statistical Bulletin official PDF direct open timed out; binary download failed; indexed search did not return the Table 2.3 header. NBS index/news archive independently confirm July Bulletin publication date 03-Sep-2026, but that does not establish the extracted row's month column.
- Continuation 107 extracted Table 2.3 rows including a 3,932 liability value; month alignment NOT_VERIFIED. July-vintage May liability +3,932 NOT_VERIFIED; cross-vintage May comparison NOT_DONE. September 2026 bulletin May values remain captured separately.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_JULY_BULLETIN_HEADER_RECOVERY_AND_VINTAGE_GATE_CONTINUATION108_20261121.md (create commit f88dce5962c98f799d494dce9700edd891cfe19b).
- Next: obtain July PDF bytes through browser/alternate official NBS-hosted route; inspect Table 2.3 header and row; compare May legs across July/September vintages only after alignment.
- ₹0; no IMF query/cohort rebuild, synthetic data, generic FX, net-to-leg inference or production changes. UNKNOWN is never PASS.


## BS. Serbia SRB — September-vintage exact month-header verification; July vintage still open (Continuation 109)
- Preflight re-fetched Master Ledger (blob SHA ccdda277aa8ee8cfa91a8d98c459e1dd24980509), GCR queue (blob SHA 545794c9590ebf5649b2d01a8dda0ad391e4a34a), Continuation 108 (blob SHA bac151f983b989d7bf5dae0d981b8bcbc6ab4d7d). PASS work skipped.
- Opened official NBS September-2026 Statistical Bulletin PDF Table 2.3, printed p.105, lines 8102–8184. Full header explicitly maps 2026 May to the 10th data column after ITEM (header at lines 8110–8111).
- September-vintage May values independently verified: portfolio assets -25 EURm (line 8146), liabilities +3,932 EURm (line 8147), net -3,957 EURm (line 8145). Identity -25 - 3,932 = -3,957 PASS. NBS notes data available until 17-Sep-2026 and subject to corrections (lines 8178–8180).
- This resolves September-vintage month alignment only. July 2026 PDF still timed out; Continuation 107's 3,932 row lacks header. July-vintage month mapping NOT_VERIFIED; July-to-September revision NOT_DONE.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_SEPTEMBER_VINTAGE_EXACT_MONTH_HEADER_VERIFICATION_AND_JULY_LIMIT_CONTINUATION109_20261121.md (create commit 4c8e006e31eeb8878f14846d762e8dd08cb122d1).
- USD/EUR transaction-weighted bridge and national scope/timing/valuation equivalence remain NOT_ESTABLISHED. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: obtain July PDF bytes through browser/alternate official route; inspect header; compare July-vintage May legs with September values only after exact alignment.
- ₹0; no IMF query/cohort rebuild, synthetic data, generic FX, net-to-leg inference or production changes. UNKNOWN is never PASS.


## BT. Serbia SRB — NBS July Bulletin Serbian archive route audit (Continuation 110)
- Preflight re-fetched Master Ledger (blob SHA 856d68b455fd5f80cf5d19aae5fb82717f447ef2), GCR queue (blob SHA 6460923fd2db5f709708b3c6d1e1b74f202d6a36), Continuation 109 (blob SHA e3217fd96e3fbc3dd1593e787029e3cafd929100). PASS work skipped.
- Official Serbian NBS Statistical Bulletin archive confirms July issue dated 31-Aug-2026; Serbian news archive lists “Statistički bilten - jul 2026. godine” dated 31.08.2026. English news archive lists July bulletin dated 03-Sep-2026. Publication date only; not a Table 2.3 header.
- Serbian archive page text exposes interactive Select/Input form only; no July-specific PDF href. Direct English July PDF URL still times out. No PDF bytes/header recovered.
- September-vintage May values remain verified in C109: assets -25, liabilities +3,932, net -3,957 EURm; arithmetic identity PASS. July row 3,932 month mapping NOT_VERIFIED; cross-vintage comparison NOT_DONE.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_JULY_BULLETIN_SERBIAN_ARCHIVE_ROUTE_AND_REVISION_STATUS_CONTINUATION110_20261121.md (create commit 1e38f608fdb6c8d188b7ceaa57f6182696ada7db).
- Next: inspect Serbian archive form DOM/Show action in real browser; capture July PDF bytes; verify Table 2.3 header and compare May legs. Stop if authenticated access required absent approval.
- ₹0; no IMF query/cohort rebuild, synthetic data, generic FX, net inference or production changes. UNKNOWN is never PASS.


## BU. Serbia SRB — July Bulletin retrieval route exhaustion (Continuation 111)
- Preflight re-fetched Master Ledger (blob SHA eeef11fd8bfd0ed321e5e5ba35ccf3a6c52f79c9), GCR queue (blob SHA 831c53b4843e9afcac1402a54d75184f98ea24fb), Continuation 110 (blob SHA 13eab75efb08b133c36fe8cd4dcfc989df7832f4). PASS work excluded.
- Fresh official NBS Serbian/English Bulletin archive checks confirm July 2026 issue (31-Aug / 03-Sep publication-date difference between language archives); both expose archive form only as Select/Input/Show in extracted HTML.
- Direct July PDF fetch again times out; exact search for PDF/Table 2.3/3,932 returns no indexed header. NBS BOP page lists September current monthly XLS only. No alternate public July PDF/data endpoint found.
- C107 extracted 3,932 row remains month-unattributed. July header and May legs NOT_VERIFIED; July-to-September revision NOT_DONE. September-vintage May assets -25, liabilities +3,932, net -3,957 EURm remains PASS in C109.
- Report: docs/GCR_SERBIA_SRB_JULY_BULLETIN_RETRIEVAL_ROUTE_EXHAUSTION_AND_NEXT_GATE_CONTINUATION111_20261121.md (create commit fe431027dfeefe41092fae5d4418c4c1fa158b27).
- Next route requires actual browser DOM inspection + archive Show action + binary capture. Do not repeat failed direct fetch, guess parameters or apply for gated web service absent explicit approval. If no browser capability, keep gate OPEN/BLOCKED and move to another valuable unfinished task.
- ₹0; no IMF query/cohort rebuild, synthetic data, generic FX, net-to-leg inference or production changes. UNKNOWN is never PASS.


## BV. Tajikistan TJK — official NBT Q2-2026 publication source gate (Continuation 112)
- Preflight current Master Ledger blob SHA 8ff41c04dc598dafbdde6dadcd35f2449f606b4a; GCR Queue blob SHA 92ffaf39d65737d71feb54ece02ccd42cf254f91. Serbia July PDF route remains OPEN/BLOCKED; no identical retry. THA dual-leg numeric comparison 2/2 PASS, vintage unresolved.
- Existing fixed 63-country cohort contains TJK; repository search found no dedicated TJK national Q2-2026 portfolio dual-leg report. No cohort rebuild or IMF re-query.
- Official NBT BOP page states NBT compiles BOP under IMF BPM5/BPM6 methodology. Official external-sector publication page exposes 2026 “FOR THE 2 QUARTER” issue link. Exact Q2 PDF URL resolved, but PDF fetch timed out; no bytes/contents/hash.
- NBT IIP 9-month 2025 report is position reconciliation (operations/revaluation/other changes), rejected as Q2-2026 BOP transaction-leg evidence. IMF CR 26/001 annual staff estimates also rejected as quarterly national source.
- Report: docs/GCR_TAJIKISTAN_TJK_Q2_2026_NBT_OFFICIAL_PUBLICATION_SOURCE_GATE_CONTINUATION112_20261121.md (create commit c5b47be1e1cb76e95c6bcbee98503e8054c5b8bf).
- TJK official Q2 locator PASS; PDF content/bytes NOT_CAPTURED; Q2 portfolio assets/liabilities NOT_CAPTURED; sign/unit/vintage NOT_ESTABLISHED; comparison NOT_DONE; TJK NOT_VALIDATED / NOT PASS.
- Next: retrieve exact official PDF with byte-preserving route; inspect whether it contains separate Q2 legs vs H1 cumulative; establish units/sign/vintage; then compare archived IMF rows. No H1-Q1 subtraction without aligned vintages.
- ₹0; no IMF query/cohort rebuild, synthetic data, generic FX, net inference, IIP stock substitution, annual-to-quarter proration or production changes. UNKNOWN is never PASS.


## BW. Tajikistan TJK — NBT archive label vs H1 filename period-basis gate (Continuation 113)
- Preflight re-fetched Master Ledger (blob SHA e7222e8e08233bb2f94decb543f7213a553465e8), GCR queue (blob SHA 5ca1d0c7fbbc24e8686b9577ffe12c96d7f28195), Continuation 112 (blob SHA dbc7ff164bf05d54e7898365ff6f2359f6bed03d). PASS work skipped.
- Official NBT archive labels 2026 link “FOR THE 2 QUARTER”; resolved PDF filename is “ПБ-нимсолаи 1 с.2026.pdf” (half-year 1). Exact PDF retrieval times out, so internal cover/table cannot be inspected. Period basis AMBIGUOUS / likely H1 clue, not confirmed standalone Q2.
- Standard representation page opens but exposes no extracted data table. No separate portfolio legs, units/sign/vintage established. No H1-Q1 subtraction, no IIP/annual substitute.
- Report: docs/GCR_TAJIKISTAN_TJK_Q2_2026_NBT_PUBLICATION_PERIOD_BASIS_AND_H1_Q2_AMBIGUITY_CONTINUATION113_20261121.md (create commit 85070d16f9998a480df516733eb1d66df417431a).
- TJK remains NOT_VALIDATED / NOT PASS. Next: byte-preserving PDF capture; inspect reporting period and separate legs. If H1, require same-vintage Q1 legs before any H1−Q1 derivation; else mark unavailable and advance.
- ₹0; no IMF query/cohort rebuild, synthetic data, FX inference or production changes. UNKNOWN is never PASS.


## BX. Timor-Leste TLS — BCTL H1 portfolio source and Q2 dual-leg gate (Continuation 114)
- Preflight re-fetched current Master Ledger (blob SHA 163b5cfc1653ba7362db3d7394a134876bb7989b), GCR queue (blob SHA 24b73fabe206fa3e28bd15181c47d2ced9031cf4), TJK C113 report (blob SHA f27988d966cc9dfb32a3b597ff5d5358f02584cd); GitHub search found no prior TLS Q2 dual-leg report. PASS work skipped.
- Official BCTL Mid-Year Economic Review reports H1 2026 portfolio investment -USD 524.9m and explains this negative component mainly as drawdown of external portfolio assets/Petroleum Fund assets. This is H1 aggregate component, not separate portfolio asset/liability legs.
- BCTL Quarterly BOP page release schedule lists Q1 2025 through Q4 2025 only; Q2 2026 standalone dual-leg table NOT_LOCATED through this route. BOP flows vs IIP stocks kept distinct.
- Report-level discrepancy retained: Executive Summary says financial account -USD 705.9m, while detailed table/section says -USD 702.9m; not silently reconciled.
- Report: docs/GCR_TIMOR_LESTE_TLS_Q2_2026_BCTL_H1_PORTFOLIO_SOURCE_GATE_CONTINUATION114_20261121.md (create commit c9b29c63569df74cad17cd1ac1105a70dc3e0dca).
- TLS H1 portfolio net component CAPTURED; Q2 separate assets/liabilities NOT_CAPTURED; Q2 period/sign/vintage alignment NOT_ESTABLISHED; IMF comparison NOT_DONE; TLS NOT_VALIDATED / NOT PASS.
- Next: locate official Q2 2026 BOP dual-leg release or H1 dual-leg table; absent same-vintage Q1 dual legs, do not derive Q2. If unavailable, advance next cohort country.
- ₹0; no IMF query/cohort rebuild, net-to-leg inference, IIP substitution or production changes. UNKNOWN is never PASS.


## BY. Timor-Leste TLS — BCTL BOP archive staleness audit (Continuation 115)
- Preflight current Master Ledger blob SHA d856df8391de33cfc973a6511d5cf7eab42d9b05, GCR queue blob SHA f02863bd301215904b945f2ec3fe49f768554c80, TLS C114 report blob SHA e698bf465389f925ea0440052775af124100148b.
- New finding: BCTL archive item labelled “Balance Of Payments | Aug 2026” resolves to a one-page PDF whose header ends at quarterly I–IV 2016/p and annual 2016/P; unit is thousand USD. Aug 2026 is file upload/metadata date, not observation vintage. It has no 2025/2026 rows and cannot support Q2-2026.
- H1 2026 portfolio component -USD 524.9m remains aggregate only; Q2 separate asset/liability legs NOT_CAPTURED. No net-to-leg inference, no IIP substitution, no H1-Q1 subtraction, no IMF query.
- Report: docs/GCR_TIMOR_LESTE_TLS_BCTL_BALANCE_OF_PAYMENTS_ARCHIVE_STALENESS_AUDIT_CONTINUATION115_20261121.md (create commit c226bf514c84b281dc36688938fdf6b65229ad78).
- TLS NOT_VALIDATED / NOT PASS. Next: inspect official Economic Statistics/BOP page and H1 review appendices for current Q2 or H1 dual legs; if unavailable, mark NOT_AVAILABLE and advance.
- ₹0; no cohort rebuild or production changes. UNKNOWN is never PASS.
