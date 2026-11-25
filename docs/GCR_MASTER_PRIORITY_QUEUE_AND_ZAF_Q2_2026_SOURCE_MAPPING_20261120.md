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


## BZ. Timor-Leste TLS — BCTL live BOP dashboard / Excel export route (Continuation 116)
- Preflight re-fetched Master Ledger blob SHA 5b90932ad15477ba22f74d44b705095f9f29cce6, GCR queue blob SHA 86f1ca7b64a70d77ed94f342349faac7fef1d8d9, TLS C115 report blob SHA 9f243d8b564204e21002b9fe77dec301029f9c0f.
- New official BCTL route: https://www.bancocentral.tl/stats/balance_pay/ embeds Power BI “BoP_V1”, exposes “Download the full Balance of Payments report” and “+ Export Excel”. Exact XLSX endpoint: https://www.bancocentral.tl/stats/bopdoc/download/c81e728d9d4c2f636f067f89cc14862c/
- XLSX endpoint MIME recognized as application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; web fetch unsupported MIME and direct container download failed. No bytes/sheets/periods/hash captured. Power BI embed also yielded no extracted rows.
- This is a newly discovered official data route, not validation. H1 2026 -USD 524.9m remains aggregate; Q2 separate portfolio assets/liabilities NOT_CAPTURED. Old Aug-2026 PDF remains stale through 2016.
- Report: docs/GCR_TIMOR_LESTE_TLS_BCTL_LIVE_BOP_DASHBOARD_AND_EXCEL_EXPORT_ROUTE_AUDIT_CONTINUATION116_20261121.md (create commit 283427dd67f29be0d6622b492ae698b6ffe6be9d).
- TLS NOT_VALIDATED / NOT PASS; unit/sign/period/vintage and IMF comparison NOT_ESTABLISHED/NOT_DONE.
- Next: actual browser/Computer Use export of XLSX or Power BI Export data; capture bytes/hash and inspect dual legs, then compare only with archived IMF rows. If blocked/no legs, record blocker and advance.
- ₹0; no IMF query/cohort rebuild, synthetic data, net-to-leg inference, IIP substitution or production changes. UNKNOWN is never PASS.


## CA. Timor-Leste TLS — BCTL live BOP latest period / export vintage (Continuation 117)
- Preflight re-fetched Master Ledger blob SHA d5c6ff4eaae89d0a57cb480ed0f149a28767fa6e, GCR queue blob SHA ffc0cefec854638081117e1904253891690f21d0, TLS C116 report blob SHA 282807d8df8ffe3c91e96c14aa2f66f5f7234d69.
- Official BCTL live BOP chart title/unit “Balance of Payments (Thousand USD)” exposes quarter labels from Jan-Mar-2020 through Jan-Mar-2025 only; latest exposed row is Q1 2025. Three numeric keys y/y2/y3 have no extracted legend; no portfolio mapping assumed.
- “Export Excel” exact target is https://bancocentral.tl/uploads/portfolio/ficheiros/1764122263_8744_BoP_2025Q3.xlsx (filename vintage Q3-2025). Web click redirected to home and direct container download failed; workbook bytes/sheets/hash NOT_CAPTURED. Q3-2025 filename is not Q2-2026 evidence.
- BCTL methodology confirms BPM6 broadly, quarterly frequency, USD unit, portfolio asset transactions from Petroleum Fund and commercial bank balance sheets, market value including accrued coupon, excluding non-transaction revaluation. It does not expose Q2-2026 dual legs.
- H1 2026 -USD 524.9m remains aggregate only. TLS Q2 separate portfolio assets/liabilities NOT_CAPTURED; TLS NOT_VALIDATED / NOT PASS; IMF comparison NOT_DONE.
- Report: docs/GCR_TIMOR_LESTE_TLS_BCTL_BOP_LIVE_SERIES_LATEST_PERIOD_AND_EXPORT_VINTAGE_AUDIT_CONTINUATION117_20261121.md (create commit e2e55fcca37495e560397e06e004fed59a74d33c).
- Next: actual browser export and inspect Q3-2025 workbook; if vintage stops at Q3-2025, mark public route stale and advance next cohort member. No IMF query/cohort rebuild.
- ₹0; no net-to-leg inference, IIP substitution or production changes. UNKNOWN is never PASS.


## CA. Türkiye TUR — TCMB September-2026 ZIP exact-endpoint access gate (Continuation 118, 2026-11-21)
- Preflight re-fetched current Master Ledger and queue, then reviewed existing TUR sections O/P and country report. Existing PDF Q2 aggregation and August/September cross-check were not repeated; no IMF query or cohort rebuild.
- Official TCMB BOP page exposes “Data - September 2026” ZIP. Exact URL resolved: https://tcmb.gov.tr/wps/wcm/connect/08454646-62d8-4188-bfbe-1c8c01d83fc4/bop.zip?CACHEID=ROOTWORKSPACE-08454646-62d8-4188-bfbe-1c8c01d83fc4-q7jJcOm&MOD=AJPERES. Web retrieval timed out; raw ZIP bytes, members, workbook sheets, byte count, SHA-256 and revision metadata NOT_CAPTURED.
- Existing Q2 national values remain assets USD 5,749m and liabilities USD 9,183m; IMF exact values USD 5,749m / USD 9,270m. Asset published-precision match; liability residual +USD 87m remains unexplained. No claim that revisions caused it.
- Report: docs/GCR_TURKIYE_TUR_Q2_2026_TCMB_SEPTEMBER_ZIP_EXACT_ENDPOINT_ACCESS_GATE_CONTINUATION118_20261121.md (commit 45ca5bcebb0a28cce43458fc3f936e5db9ef3a2a).
- TUR PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Next: supported actual browser/Computer Use or byte-preserving official route; do not repeat the same timed-out fetch. If unavailable, preflight immutable roster and prior reports, then advance next eligible member. ₹0; no production changes; UNKNOWN is never PASS.


## CB. Tanzania TZA — Bank of Tanzania Q2-2026 portfolio net-only source boundary (Continuation 119, 2026-11-21)
- Re-fetched current Master Ledger and GCR queue; checked immutable 63-country cohort order and searched repository for prior TZA Q2 national validation. TZA follows TUR; no prior dedicated TZA report found. No cohort rebuild or IMF re-query.
- Official Bank of Tanzania Statistical Bulletin, quarter ending September 2026, Vol IV No.3, Table 6.1 (Quarterly Balance of Payments), USDm: Jun-26 Q2 portfolio investment net = -14.0. Portfolio investment is presented as a single net row; separate portfolio assets and liabilities are not published in this inspected table. Do not infer from other-investment asset/liability rows.
- Report: docs/GCR_TANZANIA_TZA_Q2_2026_BOT_QUARTERLY_BOP_NET_ONLY_SOURCE_BOUNDARY_AUDIT_CONTINUATION119_20261121.md (commit 08e75278237bbd02628205825f00069b6cc0c440).
- TZA remains PARTIAL / NOT PASS; net observation captured, dual legs and national-to-IMF comparison NOT_DONE; aggregate NOT_AUTHORIZED. Raw PDF bytes/hash NOT_CAPTURED.
- Next: inspect only a newly identified official detailed BoT/NSDP source if it explicitly publishes portfolio asset/liability transaction legs; otherwise advance to UKR after prior-report/cohort preflight. No IMF re-query, cohort rebuild, net-to-leg inference, IIP substitution or production changes. ₹0; UNKNOWN is never PASS.


## CC. Ukraine UKR — NBU Q2-2026 BOP latest-period / publication-boundary audit (Continuation 120, 2026-11-21)
- Re-fetched current Master Ledger, GCR queue and immutable 63-country cohort; UKR confirmed as a fixed-cohort member. Scoped repository search found no prior dedicated UKR Q2-2026 national dual-leg report. No cohort rebuild or IMF re-query.
- Official NBU BPM6 quarterly analytical BOP PDF is last updated 19-Dec-2025; visible quarterly headers end Q3 2025. It has separate portfolio asset/liability row structure but no Q2-2026 data. NBU external-sector revision notice last updated 23-Sep-2026 describes revisions through Q1 2026, not Q2.
- Report: docs/GCR_UKRAINE_UKR_Q2_2026_NBU_BOP_LATEST_PERIOD_AND_PUBLICATION_BOUNDARY_AUDIT_CONTINUATION120_20261121.md (commit 2c353947a40469e2d48631cf5ebe37892b0811ec).
- UKR NOT_VALIDATED / NOT PASS; Q2-2026 national portfolio assets/liabilities/net NOT_CAPTURED; comparison NOT_DONE; aggregate NOT_AUTHORIZED.
- Next: use only a newly published official NBU Q2-2026 detailed BOP/Excel/SDMX/API source with explicit separate portfolio legs; else advance to URY after preflight. No stale PDF retry, no inferred legs, stock-as-flow, IMF re-query, cohort rebuild or production changes. ₹0; UNKNOWN is never PASS.


## CD. Uruguay URY — BCU Q2-2026 portfolio dual-leg / archived IMF numeric comparison (Continuation 121, 2026-11-21)
- Reused fixed 63-country cohort; URY follows UKR. Current Master Ledger and queue were preflighted; scoped repository search found no prior dedicated URY report. No IMF re-query or cohort rebuild.
- Official BCU Q2-2026 BOP report Table 9: public/private portfolio assets -47/+566 = +519 USDm; liabilities -204/+12 = -192 USDm; published portfolio net +710 USDm. Leg identity yields +711m, +1m published rounding difference. Source labels figures preliminary.
- Reused archived IMF normalized panel Git blob SHA 2a8db2878cac6323bbad74ffa4035dc70e5e6b98. Exact URY Q2 rows: A_NFA_T 518514442.91881 SCALE=6; L_NIL_T -191945243.218418 SCALE=6. Raw rows preserved; no new IMF query.
- Bounded derived display /1,000,000 gives assets +518.5144429m, liabilities -191.9452432m; BCU−IMF residuals +0.4855571m and -0.0547568m. Derived net 710.4596861m vs BCU 710m, residual -0.4596861m. All within ±0.5 USDm: numeric dual-leg/net comparison PASS at published precision. Do not generalize this derived display as a universal scale conversion.
- Same-vintage and full scope/definition equivalence NOT_ESTABLISHED; BCU raw PDF byte count/hash NOT_CAPTURED. URY numeric comparison PASS; full validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_URUGUAY_URY_Q2_2026_BCU_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_CONTINUATION121_20261121.md (final corrected commit b2be36e37766f3799ed0cd46d736ddbcc62200a6).
- Next: BCU/IMF metadata and vintage bridge, then raw PDF archival/revision comparison; no duplicate extraction, IMF re-query, cohort rebuild or production changes. ₹0; UNKNOWN is never PASS.


## CE. Uruguay URY — BCU/IMF methodology, scope and vintage bridge (Continuation 122, 2026-11-21)
- Re-fetched current Master Ledger, GCR queue, C121 report and prior IMF panel/methodology evidence; PASS work excluded; no repeat of Table 9 extraction, IMF query or cohort rebuild.
- Official BCU methodology (MBP6 update Dec-2020) maps portfolio data sources: EGESE for non-financial private sector; BCU debt registers for public securities (market valuation/accrual); SSF statements for regulated financial institutions with transaction changes calculated by original currency; SSF/pension-fund/external-custody records and quarterly/annual surveys for related holdings.
- Current BCU SDDS page shows Q2/26 BOP latest and portfolio net USD710m. SDDS template states portfolio investment unit USD millions and separate P_123/L_123 fields; extracted placeholders not numeric observations. Q2 report explicitly says preliminary and notes rounding.
- Existing IMF raw broad CSV receipts reused: A_NFA_T captured 2026-11-19T06:46:34.357106Z, 484139 bytes, SHA256 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e; L_NIL_T captured 2026-11-19T06:46:34.878465Z, 451290 bytes, SHA256 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba. Retrieval timestamps do not establish last revision timestamp.
- IMF BOP/IIP metadata dashboard landing published 18-Nov-2026 but country-level URY interactive data not retrieved. BCU raw PDF bytes/size/SHA256 NOT_CAPTURED after byte-preserving download attempt failed. Same-vintage/revision alignment NOT_ESTABLISHED.
- Report: docs/GCR_URUGUAY_URY_Q2_2026_BCU_IMF_METHODOLOGY_SCOPE_VINTAGE_BRIDGE_CONTINUATION122_20261121.md (commit c5b9daf0208e75d9610f34b0a1740f53edc62e7c).
- C121 numeric dual-leg comparison PASS remains unchanged; full URY PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Next: only supported byte-preserving BCU PDF capture and country-specific IMF vintage export; otherwise preserve blocker and advance fixed cohort. ₹0; no production changes; UNKNOWN is never PASS.


## CF. Uzbekistan UZB — CBU Q2-2026 portfolio dual-leg / archived IMF numeric comparison (Continuation 123, 2026-11-21)
- Re-fetched Master Ledger, GCR queue and immutable 63-country cohort; UZB follows URY. Scoped repo search found no prior dedicated UZB report. No IMF re-query/cohort rebuild.
- Official CBU quarterly BOP dataset page update 29-Sep-2026 11:21, periods 2005-Q1 through 2026-Q2, separate portfolio asset/liability rows. Q2 preview values: assets USD0.01m; liabilities USD1,960.49m; literal unit note “million USD, end of period”. XLSX raw bytes/hash not captured.
- Official CBU GDDS-DQAF BOP metadata states BPM6, quarterly compilation/publication, accrual basis with adjustments, no known coverage exceptions, and quarterly revision policy.
- Reused IMF archived normalized panel Git blob SHA 2a8db2878cac6323bbad74ffa4035dc70e5e6b98; exact UZB Q2 raw observations A_NFA_T 9793.61706018728 SCALE=6 and L_NIL_T 1960492267.78624 SCALE=6. No IMF re-query.
- Bounded display /1e6 yields assets 0.009793617m, liabilities 1960.492267786m; residuals +0.000206383m and -0.002267786m within ±0.005m. Numeric dual-leg comparison PASS at displayed precision.
- Time-basis caveat: “end of period” needs workbook header clarification for BOP transaction rows. BCU update 29-Sep-2026 and IMF retrieval 19-Nov-2026 are not same-vintage evidence. Full UZB validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_UZBEKISTAN_UZB_Q2_2026_CBU_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_CONTINUATION123_20261121.md (commit bbce4b2aeefb6786eb706d8a32dd9f38c4fd12eb).
- Next: byte-preserving CBU XLSX retrieval and unit/time-basis/vintage inspection; if unsupported, preserve UZB blocker and advance VNM after preflight. ₹0; no production changes; UNKNOWN is never PASS.


## CG. Vietnam VNM — official quarterly Q2-2026 portfolio source closure (Continuation 124, 2026-11-21)
- Re-fetched Master Ledger, GCR queue, fixed 63-country cohort and prior VNM C59 report; completed C59's exact next action to search for a distinct official SBV quarterly Q2-2026 BOP dual-leg publication/API/export.
- No qualifying Q2 national portfolio assets/liabilities rows located. SBV annual reports show separate asset/liability labels through annual 2023 only. NSO official Q2/H1 and Q3/9M 2026 releases do not provide BOP portfolio legs; FDI/securities/trade aggregates rejected as proxies.
- IMF e-GDDS DQAF BOP metadata search-indexed text states no portfolio asset/liability data currently available, but page's update date not visible; treat as corroborative/possibly legacy, not definitive current 2026 publication evidence.
- No raw national Q2 file/hash; no annual-to-quarter allocation, sign inference, IMF re-query or cohort rebuild. VNM remains PARTIAL / NOT PASS; dual-leg NOT_DONE; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_VIETNAM_VNM_Q2_2026_SBV_OFFICIAL_QUARTERLY_SOURCE_CLOSURE_CONTINUATION124_20261121.md (commit 4e56a8919fb4478997dd624c8c0605df4bd70db8).
- Next fixed cohort member WSM (Samoa), subject to preflight. ₹0; no production changes; UNKNOWN is never PASS.


## CH. Samoa WSM — CBS Q2-2026 quarterly BOP portfolio source-boundary audit (Continuation 125, 2026-11-21)
- Re-fetched Master Ledger, GCR queue, immutable 63-country cohort; WSM follows VNM; scoped repo search found no dedicated WSM Q2 national report.
- Official CBS quarterly bulletin index says releases cover quarter-end data and are published with three-month delay. Latest listed June-2026 bulletin, but its contents/narrative explicitly cover March 2026 / Q1; Table B-1 columns stop at 2026-I. Table B-1 (Tala million) contains separate portfolio net/assets/liabilities and BPM6 note.
- Q2-2026 national legs NOT_CAPTURED; numeric comparison NOT_DONE; WSM PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Annual forecasts, IMF Article IV estimates and IIP stocks rejected as substitutes.
- Report: docs/GCR_SAMOA_WSM_Q2_2026_CBS_QUARTERLY_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION125_20261121.md (commit 92260e1155d537f6fe2f2cdc2d35fb50a35d79c9).
- Next: locate a later CBS bulletin that actually reports June-2026 Q2; archive raw bytes/URL/time/size/SHA256 and extract Q2-II legs. If unavailable, preserve blocker and advance after preflight. ₹0; production unchanged; UNKNOWN is never PASS.


## CH. Samoa WSM — Q2-2026 CBS release-status recheck (Continuation 126, 2026-11-21)
- Re-fetched current Master Ledger, queue, fixed 63-country cohort, and prior WSM Continuation 125 report. Fixed order after WSM is ZAF (South Africa).
- Direct CBS index https://cbs.gov.ws/quarterly-bulletin lists June 2026 as latest and footer last updated 18 Aug 2026; September 2026 is not listed. Conflicting search snippet treated as stale/unverified.
- June-2026 PDF internal contents/title identify March 2026 / Q1; Table B-1 has distinct portfolio net/assets/liabilities, Tala million, BPM6, but latest quarter 2026-I only.
- Q2-2026 WSM legs NOT_CAPTURED; numeric comparison NOT_DONE; WSM PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. No raw Q2 archive/hash.
- Report: docs/GCR_SAMOA_WSM_Q2_2026_CBS_RELEASE_STATUS_RECHECK_CONTINUATION126_20261121.md (commit 0b7d5d9bd57def55020f8b4139f7445605a57d6f).
- Next: after preflight, move to ZAF South Africa. Recheck CBS only when a later bulletin is officially listed. ₹0; production unchanged; UNKNOWN is never PASS.


## Continuation 127 — ZAF Q2-2026 FX conversion methodology boundary (2026-11-21)
- Reopened current Master Ledger, queue, fixed cohort and ZAF Parts 3/4 + 20-Nov numeric reconciliation. Existing SARB/IMF values retained; no re-extraction or IMF query.
- Prior ZAF liabilities residual +0.007354619 USDm remains prior PASS; asset residual -0.056053395 USDm remains REVIEW, outside prior 0.0304 USDm rounding bound.
- IMF BPM6 §§3.104–3.106 and draft BPM7 §§4.258–4.259 require transaction-date rates or shortest-period averages in principle; the OECD quarterly average used in the prior comparison is not proven to be SARB's compilation conversion method. ZAF DQAF page fetch returned generic shell only. Quarter-average equivalence NOT_ESTABLISHED.
- ZAF full validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Report: docs/GCR_ZAF_Q2_2026_FX_CONVERSION_METHODOLOGY_BOUNDARY_CONTINUATION127_20261121.md (commit b008571b86b3ebe8855b1c7170ee64a722e20f50).
- Next rank-1 task: CHN official SAFE detailed Q2-2026 BOP XLSX byte retrieval/workbook inspection. Existing CHN audit says URL located but bytes not retrieved; retry only via a genuinely different supported transfer route, otherwise preserve BLOCKED and move on. ₹0; no production changes; UNKNOWN is never PASS.


## Batch 1 — 10-country national Q2-2026 dual-leg validation (Continuation 128, 2026-11-21)
- User asked to work in batches of 10/15/20 rather than one country per prompt. Fixed batch size 10 adopted for this cycle; no need for user to reselect between countries.
- Preflighted latest Master Ledger, GCR queue, fixed cohort, and ten prior reports. PASS work excluded.
- Batch order: CHN, COL, POL, TUR, PER, ROU, NPL, RWA, SLV, SLB.
- CHN new distinct browser link route to official SAFE XLSX still returned 400 unsupported XLSX MIME; no bytes/hash; PARTIAL/BLOCKED.
- COL new official BanRep SUAMECA multiple-download catalogue result lists separate quarterly portfolio net acquisition of assets and net incurrence of liabilities through Q2-2026 in USDm, update 2026-09-01. Page open returned 502; no raw export, series IDs or numeric values; PARTIAL/BLOCKED.
- Full per-country next actions and evidence boundary are in docs/GCR_Q2_2026_NATIONAL_DUAL_LEG_VALIDATION_BATCH10_CONTINUATION128_20261121.md (commit 5a1952a9b3b89db59e4d9dbdc53760aa509aab02).
- Next batch item: POL official NBP XLSX retrieval through a genuinely supported file route; if unavailable, record once and proceed to TUR. No IMF re-query/cohort rebuild. ₹0; production unchanged; UNKNOWN never PASS.


## Batch 1 execution update — POL/TUR/PER/ROU (Continuation 129, 2026-11-21)
- POL: direct official NBP XLSX browser fetch returned 400 unsupported content type; separate container download failed. BLOCKED; no raw bytes/hash.
- TUR: direct official TCMB ZIP route inaccessible. BLOCKED for ZIP; existing asset numeric match remains displayed PASS; liability +87 USDm REVIEW; full validation PARTIAL.
- PER: official BCRPData quarterly catalogue and three result pages re-opened. Q2-2026 private portfolio assets +1,749 USDm; private liabilities +279; public liabilities +1,421. Combined liabilities +1,700 vs IMF +1,699.664071, residual +0.335929 within ±0.5 = numeric PASS. Public portfolio asset-specific series absent from listed 25-series public block; full asset coverage PARTIAL. No raw API bytes/hash.
- ROU: official BNR methodology confirms portfolio investment uses title-by-title monthly compilation at market value/accrual and distinguishes IIP stocks from BOP flows. No Q2 transaction-leg extract/raw bytes; PARTIAL.
- Updated batch report: docs/GCR_Q2_2026_NATIONAL_DUAL_LEG_VALIDATION_BATCH10_CONTINUATION128_20261121.md, update commit d255c5bbeb286087a9a9ff185162f6372bcbe7ff.
- Next: NPL NRB alternate API/export route; then RWA, SLV, SLB. No IMF query/cohort rebuild. ₹0; production unchanged; UNKNOWN never PASS.


## Batch 1 execution update — NPL / RWA (Continuation 130, 2026-11-21)
- NPL: official NRB External Sector BPM6 workbook confirmed as correct source family but current XLSX retrieval remains unsupported. Distinct NSDP route checked: Browse Data maps to general macro-report archive, SDMX Download is stale 2024-Q1 XML. No alternate Q2-2026 official export/API found. NPL separate national portfolio legs NOT_EXTRACTED; PARTIAL/BLOCKED. Stop repeating identical routes.
- RWA: BNR External Sector portal search result lists 30-Jun-2026 “Balance of Payment” and BPM6 compilation, but direct portal is JS-only and exact downloadable locator unresolved. August-2026 BNR summary BOP table is Q1 and omits portfolio legs; 2026H1 net-only and annual FY separate legs are not Q2 substitutes. RWA remains PARTIAL/NOT PASS.
- Next: resolve BNR June-30 item through a supported document/API route; if unavailable, advance to SLV. ₹0; no IMF re-query/cohort rebuild; no production changes; UNKNOWN never PASS.


## Batch 1 execution update — SLV (Continuation 131, 2026-11-21)
- Official BCR Revista Trimestral Abril–Junio 2026 publication calendar schedules Q2-2026 BOP for 30-Sep-2026; PDF Table II.2 still has Q1-2026 as latest displayed quarter. Q1 portfolio asset +282.76 USDm / liability -56.61 USDm values are explicitly not Q2.
- Distinct BCR SDDS Quarterly BOP Data Base route (cdr=130) timed out; NSDP last updated 2022-12-23. Exact Q2 values, raw bytes/hash and vintage not captured. SLV PARTIAL/BLOCKED; aggregate NOT_AUTHORIZED.
- Next: SLB Solomon Islands primary-methodology resolution of CBSI Table 1.17 sign conflict, reusing archived IMF rows. ₹0; no IMF re-query/cohort rebuild; UNKNOWN never PASS.


## Batch 1 execution update — SLB (Continuation 132, 2026-11-21)
- CBSI June-2026 Table 1.17: Q2 portfolio assets +38 SBDm, liabilities nil. Chapter IV narrative “deficit 38” is conceptually consistent as the reverse net-inflow perspective; under BPM6 +38 asset acquisition contributes positive net lending. Do not flip sign. CBSI does not explicitly define narrative deficit convention.
- Extracted exact archived IMF SLB Q2 rows without a new query: A_NFA_T OBS_VALUE 4675384.136569459 SCALE=6; L_NIL_T OBS_VALUE 0 SCALE=6. Raw CSV blob SHAs 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Provisional arithmetic only using Q2 average 8.08 SBD/USD: 38/8.08=4.702970297 USDm vs IMF candidate OBS_VALUE/1e6=4.675384137 USDm; residual -0.027586160, within ±0.061881188 USDm SBD table-rounding bound. Liability zero vs nil. Not PASS: SLB-specific SCALE/display and CBSI BOP transaction FX method not proven; PDF original bytes/hash unavailable.
- SLB remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Next: explicit CBSI transaction FX method or advance to next eligible fixed cohort member. ₹0; no IMF re-query/cohort rebuild; UNKNOWN never PASS.


## Sequential cohort continuation — TJK/TLS/TZA screened; UKR progressed (Continuations 133–134, 2026-11-21)
- TJK: NBT 2026 archive label “FOR THE 2 QUARTER” conflicts with filename “нимсолаи 1” (H1); PDF bytes inaccessible; no same-vintage Q1 separate legs. H1−Q1 prohibited. TJK Q2 national legs NOT_CAPTURED; PARTIAL/BLOCKED.
- TLS: official BCTL live chart ends Q1-2025; export workbook filename Q3-2025; H1-2026 report net-only; archive PDF upload label Aug-2026 actually contains data only through 2016. No Q2-2026 dual legs in inspected official public routes; NOT_VALIDATED / NOT PASS.
- TZA: BoT Q2-2026 Table 6.1 has only portfolio net -USD14.0m; separate legs absent. BoT quarterly “Balance of Payments in USD” archive entry is dated 25-Aug-2020, not current. No back-solving; PARTIAL / NOT PASS.
- UKR: NBU Q2-2026 IIP report explicitly separates transaction changes from opening/closing stocks. Portfolio transaction changes: assets +159 USDm, liabilities +34 USDm. Existing IMF raw Q2 UKR rows: A_NFA_T OBS_VALUE 159000000 SCALE=6; L_NIL_T OBS_VALUE 34000000 SCALE=6. Country-specific /1e6 display matches 159/34 exactly at whole-million precision; both leg residuals zero. This is a transaction-column cross-check, not a stock substitution. NBU IIP report updated 23-Sep-2026; standalone BOP PDF is stale (last update 18-Sep-2025); formal IIP-transaction ↔ BOP P_F equivalence and same-vintage Q2 revision alignment remain open. UKR PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- UKR detailed report: docs/GCR_UKRAINE_UKR_Q2_2026_NBU_IIP_TRANSACTION_BRIDGE_AND_IMF_DUAL_LEG_CHECK_CONTINUATION134_20261121.md. Next exact action: obtain current NBU Q2-2026 BOP standard/analytical source or documented crosswalk, then verify same-vintage revision alignment. No IMF query/cohort rebuild; ₹0; production unchanged; UNKNOWN never PASS.

## Continuation 135 — UKR BOP vintage gate and CHN SAFE file-route boundary (2026-11-21)
- UKR C135 rechecked official NBU current IIP Q2 transaction columns (+159 assets, +34 liabilities) but found no current Q2-2026 BOP analytical/standard PDF or accessible API. The p4 BOP PDF last updated 21-Mar-2025; the finliteracy mirror last updated 19-Dec-2025 and ends at Q3-2025 / I-III 2025. NBU methodology confirms quarterly BOP publication/revisions and separate IIP revision policy. UKR transaction-column numeric cross-check remains PASS; formal IIP-to-BOP P_F and same-vintage bridge NOT_ESTABLISHED; PARTIAL / NOT PASS.
- CHN C135 followed the official SAFE English detail-page attachment. It resolves to the same XLSX endpoint already tested; web retrieval returns unsupported XLSX MIME. No alternate file bytes or workbook hash. Stop repeating the endpoint; CHN remains PARTIAL / NOT PASS.
- Reports: docs/GCR_UKRAINE_UKR_Q2_2026_NBU_IIP_TRANSACTION_BRIDGE_AND_IMF_DUAL_LEG_CHECK_CONTINUATION134_20261121.md; docs/GCR_CHINA_CHN_SAFE_DETAILED_BOP_TIME_SERIES_ACCESS_AUDIT_20261120.md. Next action: choose the next executable high-weight unvalidated country from fixed cohort after checking current priority queue; do not rebuild cohort or re-query IMF. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 136 — CHN SAFE Chinese attachment and COL BanRep series discovery (2026-11-21)
- CHN: found the distinct official Chinese-language SAFE record (index 000014453-2019-00427; dispatch 2026-09-29) and a different XLSX attachment URL: https://www.safe.gov.cn/safe/file/file/20260929/6674650e17de4f20a45c64610118a96f.xlsx. Browser retrieval returned 400 unsupported XLSX MIME; direct container download also failed. No bytes/hash/workbook content. Stop both known endpoint retries. CHN remains PARTIAL / NOT PASS.
- COL: official BanRep SUAMECA catalogue confirms separate quarterly portfolio net-acquisition-of-assets and net-incurrence-of-liabilities BOP series, both current USDm, 2000-Q1 through 2026-Q2, disclosed 2026-09-01. Catalogue/series pages returned 502/timeout in this retrieval bridge; no series IDs, exact Q2 values, raw bytes or hash. Series discovery PASS; values and national sign/vintage validation NOT_DONE; COL PARTIAL/BLOCKED.
- Detail: docs/GCR_CHN_SAFE_CHINESE_ATTACHMENT_AND_COL_BANREP_SERIES_DISCOVERY_CONTINUATION136_20261121.md.
- Next: retrieve the two already identified COL series through a genuinely different supported export/API route; compare separately to existing archived IMF rows. No IMF re-query/cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 137 — Banxico MEX Q2-2026 dual-leg check; COL API migration root-cause (2026-11-21)
- COL: official BanRep notice states the SDMX API was updated from 26-Oct-2026 and the previous API version retired after 15-Nov-2026. New October-2026 v4.0 guide documents REST endpoint https://totoro.banrep.gov.co/sdmx/rest/, agency BANREP.CIE and XML/JSON/CSV. Its listed DataFlows do not include BOP; do not invent a BOP Flow ID. Official multiple-download catalogue still lists separate quarterly portfolio asset/liability BOP series through Q2-2026 in current USDm, disclosed 01-Sep-2026, but exact export remains inaccessible. COL stays PARTIAL/BLOCKED; stop old REST retries.
- MEX: used existing IMF 12-country exact-key receipt only; no IMF re-query/cohort rebuild. Official Banxico Q2-2026 BOP report (25-Aug-2026), Cuadro 3, reports portfolio asset net acquisition +USD8,937m, liability net incurrence +USD10,561m, A-B=-USD1,624m. Archived IMF exact rows: asset OBS_VALUE 8,937,255,098 SCALE=6; liability OBS_VALUE 10,561,285,114 SCALE=6. USDm residuals vs Banxico whole-million values: -0.255098m assets and -0.285114m liabilities, both inside ±0.5m rounding. Separate-leg numeric comparison and sign/period checks PASS at published rounding; same-vintage/revision bridge NOT_ESTABLISHED. MEX PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_IMF_DUAL_LEG_VALIDATION_CONTINUATION137_20261121.md.
- Next: seek dated Banxico Q2 revision/vintage bridge for MEX; for COL wait for a supported BOP data export or move to the next fixed-cohort member. No IMF re-query/cohort rebuild. ₹0; protected production invariants unchanged; UNKNOWN never PASS.


## Continuation 138 — Hungary HUN Q2-2026 MNB separate portfolio legs and methodology gate (2026-11-21)
- Preflight reopened Master Continuity Ledger, GCR Master Priority Queue, fixed 63-country cohort, MEX C137 and existing archived IMF raw asset/liability panels. HUN is a fixed-cohort member with no dedicated national Q2 portfolio dual-leg report in the repository tree; no IMF re-query or cohort rebuild.
- Official MNB Statistics Portal Q2-2026 BOP/IIP release, published 25-Sep-2026, reports portfolio net assets -EUR6,277m, assets expanded +EUR2,104m and liabilities expanded +EUR8,380m in the “Net lending (FA) by instruments” section. These are separate financial-account flow legs, not IIP closing stocks. Rounded component arithmetic differs by EUR1m (2,104−8,380=-6,276 vs reported -6,277); retained as a rounding REVIEW, not forced.
- Official MNB BPM6 methodology (Sep-2024) establishes currency-by-currency monthly flows converted to HUF using MNB daily middle-rate monthly averages; quarterly flows sum monthly; EUR presentation derives from HUF via monthly-average HUF/EUR. March/September are longer 4-year revision windows; Q2 2026 publication revised BOP back to 2022. Portfolio transactions derive from security-position changes adjusted for price/FX effects; some household foreign-custody holdings are estimated.
- Reused existing archived IMF HUN Q2 rows without new query: A_NFA_T OBS_VALUE=2,434,272,117.820269 USD, SCALE=6; L_NIL_T=9,813,617,187.260281 USD, SCALE=6. Original values/attributes preserved.
- MNB national separate-leg source and methodology PASS; exact cross-currency reconciliation NOT_DONE because MNB's prescribed monthly conversion method cannot be reproduced by a simple quarterly EUR/USD average; item-level IMF equivalence and same-vintage bridge NOT_ESTABLISHED. HUN PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_HUNGARY_HUN_Q2_2026_MNB_IMF_PORTFOLIO_SOURCE_AND_METHOD_CROSSWALK_CONTINUATION138_20261121.md.
- Next: obtain MNB monthly BOP and exact monthly conversion series; reproduce the MNB method; verify item-level mapping and same-vintage. No IMF re-query/cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 139 — HUN monthly portfolio route closed; ALB Bank of Albania Q2 source gate opened (2026-11-21)
- HUN official MNB monthly-data route bounded: index lists HUF/EUR monthly BOP categories updated 13-Nov-2026, but the dedicated monthly publication page explicitly states only selected estimates are published for the open quarter and monthly time series are not published. No continuous monthly portfolio asset/liability rows for Apr–Jun 2026 are available on that route. HUN remains PARTIAL / NOT PASS; no monthly synthetic split or quarterly FX shortcut. HUN C138 report addendum records closure.
- Selected ALB from the existing immutable 63-country Q2 cohort after preflight; no dedicated ALB Q2 national portfolio report found. Official Bank of Albania Statistics Calendar schedules Q2-2026 BOP for 10-Sep-2026. Official quarterly BOP table, updated 10-Sep-2026, is in EUR millions and explicitly exposes portfolio asset parent C.2.A and liability parent C.2.L, each with equity and debt subcomponents.
- ALB national numeric Q2 rows and raw export were not captured; taxonomy/source route PASS only. No unsupported value inference. Reused archived IMF Q2 rows without new request: A_NFA_T OBS_VALUE=181700604.8387097 USD, SCALE=6; L_NIL_T=145011618.7096774 USD, SCALE=6. Numeric comparison NOT_DONE; sign/item mapping and same-vintage NOT_ESTABLISHED; ALB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_BOP_PORTFOLIO_SOURCE_GATE_CONTINUATION139_20261121.md. HUN addendum is in docs/GCR_HUNGARY_HUN_Q2_2026_MNB_IMF_PORTFOLIO_SOURCE_AND_METHOD_CROSSWALK_CONTINUATION138_20261121.md.
- Next: capture Bank of Albania's official Q2 machine-readable BOP table export/raw bytes and exact C.2.A/C.2.L values; verify sign, aggregation, scale and vintage. No IMF re-query/cohort rebuild. ₹0; protected production invariants unchanged; UNKNOWN never PASS.


## Continuation 140 — ALB official BPM6 sign/methodology verified; exact interactive Q2 export remains unextracted (2026-11-21)
- Official Bank of Albania confirms BPM6 BOP compilation and distinguishes BOP transaction flows from IIP stocks. Official 2014 BPM6 transition commentary: financial-account increases in assets/liabilities positive, decreases negative; balance = assets minus liabilities. IMF GDDS/DQAF ALB BOP metadata: EURm publication, non-EUR transactions converted to ALL using monthly transaction-time rates, financial transactions accrual basis, revision policy fixed in methodological notes; detailed time-series downloadable in Excel and dynamic HTML copyable to Excel.
- Reopened official Bank of Albania Main data page cregtab_id=645: Q2 BOP dataset, quarterly, EURm, update 10-Sep-2026; C.2.A and C.2.L with equity/debt children confirmed. Current web retrieval surface returns index/interactive controls only, not selected observation cells or workbook bytes. This is a retrieval-channel boundary, not source absence. No numeric national values or SHA-256 claimed.
- ALB sign/methodology PASS; exact Q2 asset/liability values NOT_CAPTURED; raw export/hash NOT_CAPTURED; numeric comparison NOT_DONE; vintage NOT_ESTABLISHED; ALB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Archived IMF exact rows retained; no new IMF request.
- Detail: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_BOP_PORTFOLIO_SOURCE_GATE_CONTINUATION139_20261121.md (Continuation 140 addendum).
- Next: obtain official interactive Excel/HTML export through supported browser route; preserve raw bytes and SHA-256, extract parent/child portfolio legs, compare separately to archived IMF rows. If unavailable, retain PARTIAL and advance fixed cohort. No guessed API, IMF re-query or cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 141 — ALB Main-data period ceiling confirmed (2026-11-21)
- Reopened official Bank of Albania Main data page: quarterly, EURm, C.2.A/C.2.L taxonomy visible, but browser-readable period picker ends Q3-2025 and methodology note references 2017 vintage. It cannot serve as Q2-2026 numeric evidence. The statistics index separately advertises the quarterly BOP dataset updated 10-Sep-2026; that index does not expose selected Q2-2026 observations. Direct interactive detail URL retrieval also returned inaccessible. No guessed API/export request and no invented numeric data.
- Official 2014 BPM6 commentary confirms financial-account asset/liability increases positive, decreases negative; financial-account balance is asset change minus liability change; BOP flows published in EUR with average exchange rate for flows (end-period rate for stocks). Exact 2026 transaction FX and vintage bridge remain unestablished.
- ALB remains PARTIAL / NOT PASS; Q2 national legs NOT_CAPTURED, raw export/hash NOT_CAPTURED, dual-leg numeric comparison NOT_DONE, vintage NOT_ESTABLISHED; aggregate NOT_AUTHORIZED. Stop retrying this legacy Main-data view. Next: Q2-specific supported export or advance to another fixed-cohort member. No IMF re-query/cohort rebuild; ₹0; no production changes; UNKNOWN never PASS.


## Continuation 142 — Angola AGO Q2-2026 BNA source-family gate opened (2026-11-21)
- Reopened Master Ledger, Priority Queue and fixed 63-country cohort; AGO is an eligible fixed-cohort member and no dedicated AGO Q2-2026 national portfolio dual-leg validation report existed in repository inventory. Selected as a high-priority oil-exporting EMDE. No IMF re-query/cohort rebuild.
- BNA official portal identifies External Statistics and BOP/IIP report publication family, but current browser-readable SPA route exposes no extractable content or report bytes. BNA Q2-2026 External Statistics Information Note was publicly announced 4-Sep-2026; contemporaneous reporting quotes current-account surplus ~USD2.07–2.08bn and capital-and-financial-account deficit USD2,516.6m. These are broad account-level totals only, not portfolio asset/liability legs. IMF GDDS metadata describes historic annual BOP/IIP dissemination and quarterly bulletin mailing-list distribution; plausible access boundary, not proof of missing detailed data.
- Reused exact archived IMF rows: AGO A_NFA_T OBS_VALUE=23014088.470948 USD SCALE=6; L_NIL_T=1500000000 USD SCALE=6. Asset/liability raw panel blob SHAs remain 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion, netting, or IMF re-query.
- National Q2 portfolio legs/raw bytes/hash NOT_CAPTURED; taxonomy/sign/FX bridge NOT_ESTABLISHED; same-vintage NOT_ESTABLISHED; dual-leg reconciliation NOT_DONE; AGO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Do not infer legs from the reported capital-and-financial-account net deficit.
- Detail: docs/GCR_ANGOLA_AGO_Q2_2026_BNA_EXTERNAL_STATISTICS_PORTFOLIO_SOURCE_GATE_CONTINUATION142_20261121.md.
- Next: obtain Q2 BNA note/report attachment or official quarterly-bulletin source via supported official route; preserve bytes/metadata/SHA-256; extract separate portfolio legs and verify sign/FX/scale/vintage. If unavailable, retain PARTIAL and advance. No repeated SPA retry, IMF re-query or cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.

## Continuation 143 — Armenia ARM Q2-2026 CBA BOP XLS route identified; stock/flow boundary enforced (2026-11-21)
- Reopened Master Ledger, Priority Queue and immutable 63-country cohort; ARM is a cohort member with no dedicated ARM Q2-2026 national portfolio flow dual-leg report in repository inventory. No IMF re-query/cohort rebuild.
- Official CBA legacy External Sector Statistics page exposes direct BPM6 BOP workbook: https://old.cba.am/stat/stat_data_eng/BOP_eng_for_site_BPM6_rev.xls. Browser fetch failed with 400 Unsupported content-type application/vnd.ms-excel; direct container download also failed. Exact workbook bytes/sheets/hash not captured.
- CBA BOP metadata: USD millions, quarterly/annual, BPM6, residency/accrual/double-entry, annual revisions generally end-June. CBA methodology note records 2026 revisions to 2022–2025 goods/imports, insurance/freight, telecom/computer/information services and 2024–2025 compensation/personal transfers; no portfolio unchanged assumption.
- Armstat NSDP Q2/26 BOP flows (USDm) visible: current account -749.7; capital +13.2; financial account -421.4; direct investment -287.5; derivatives +2.6; other investment -235.0; reserves +357.0. Portfolio flow not shown in visible summary; this is not zero. Same page shows IIP END-OF-PERIOD portfolio asset stock 2,131.2 USDm and liability stock 2,526.7 USDm; strictly excluded from BOP flow test. IMF DSBB metadata confirms national BOP FA classification includes portfolio investments.
- Reused archived IMF exact rows: ARM A_NFA_T OBS_VALUE=-206248729.725102 USD SCALE=6; L_NIL_T=52279059.5905749 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- National portfolio flow legs NOT_CAPTURED; workbook bytes/hash NOT_CAPTURED; sign/scale/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; ARM PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. IIP stocks are not substitutes.
- Detail: docs/GCR_ARMENIA_ARM_Q2_2026_CBA_BOP_XLS_SOURCE_AND_STOCK_FLOW_BOUNDARY_CONTINUATION143_20261121.md.
- Next: recover exact official XLS via supported spreadsheet/browser or owner-side save, preserve raw bytes/hash, extract Q2 portfolio legs and verify vintage/sign/scale. If inaccessible, retain PARTIAL and advance. No repeated identical XLS fetch, IMF re-query, cohort rebuild; ₹0; no production changes; UNKNOWN never PASS.
## Continuation 144 — Kazakhstan KAZ Q2-2026 NBK portfolio dual-leg numeric reconciliation (2026-11-21)
- Reopened Master Ledger, Priority Queue and immutable 63-country cohort; KAZ is a cohort member and repo search found no dedicated KAZ Q2-2026 national dual-leg report. No IMF re-query/cohort rebuild.
- Official NBK Statistical Bulletin N09 (382), September 2026, table 1.3, pp.9–10, https://nationalbank.kz/file/download/138795, provides Q2-2026 portfolio legs in USDm: net acquisition of financial assets +1,545.1; net incurrence of liabilities +4,448.9.
- Reused archived IMF exact rows: A_NFA_T OBS_VALUE=1545080690.27593 USD SCALE=6; L_NIL_T=4448877446.24013 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Expressing archived USD raw values in USDm using declared SCALE=6: assets 1,545.08069027593 vs NBK 1,545.1 (difference +0.01930972407); liabilities 4,448.87744624013 vs NBK 4,448.9 (difference +0.02255375987). Both PASS at national displayed precision 0.1 USDm. No sign inversion/netting.
- NBK published financial-account sign commentary: minus indicates inflow and plus outflow. National unit USDm and quarterly frequency supported by NBK/BNS metadata. Same-vintage remains NOT_ESTABLISHED: archived IMF 19-Nov panel vs NBK bulletin/revision history not bridged. PDF binary/hash NOT_CAPTURED.
- KAZ dual-leg numeric gate PASS at publication rounding; full vintage acceptance PARTIAL; aggregate NOT_AUTHORIZED. Do not claim same vintage or aggregate eligibility.
- Detail: docs/GCR_KAZAKHSTAN_KAZ_Q2_2026_NBK_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION144_20261121.md.
- Next: archive NBK PDF bytes/hash and secure exact vintage bridge; retain dual-leg numeric PASS; then advance cohort. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 145 — KAZ N09 publication-date and revision-window correction (2026-11-21)
- Correction to Continuation 144 wording: the cited NBK Statistical Bulletin N09 (382) is the issue labelled N09, but NBK's official bulletin index explicitly lists its publication date as 30-Oct-2026. The 30-Sep-2026 issue is N08. Do not call N09 the September 2026 bulletin. Official index: https://nationalbank.kz/en/news/statisticheskiy-byulleten/rubrics/2596.
- The official NBK Q2-2026 table values remain +1,545.1 USDm portfolio asset net acquisition and +4,448.9 USDm liability net incurrence; the linked official N09 table source remains https://nationalbank.kz/file/download/138795. Numeric comparison against archived 19-Nov IMF raw panel remains PASS at 0.1 USDm publication precision.
- Crucial vintage evidence: NBK BOP metadata states final quarterly data are published 90 days after quarter-end; earlier quarters are updated when final data are released; revisions occur twice yearly, in October and April, covering two years before the reporting year. Source: https://nationalbank.kz/en/news/metadannye/7253. Thus Q2-2026 falls inside the October revision window; N09 published 30-Oct is an October-vintage publication, not a September vintage.
- The IMF archive snapshot date is 19-Nov-2026, later than N09. However, no NBK revision ledger / exact release payload timestamp tied to the two portfolio rows and no IMF extraction-vintage metadata proving same synchronized vintage has been captured. Therefore same-vintage remains NOT_ESTABLISHED; do not infer same vintage merely from dates or rounded numeric equality.
- Official index distinguishes N09 (30-Oct-2026) from N08 (30-Sep-2026). Earlier text in Continuation 144 saying 'September 2026 Statistical Bulletin' is corrected by this addendum; the table values and separate-leg numeric calculations are unchanged.
- Current acceptance: national dual-leg numeric comparison PASS at 0.1 USDm; source issue date corrected to 30-Oct-2026; vintage alignment NOT_ESTABLISHED; PDF bytes/SHA256 NOT_CAPTURED; aggregate NOT_AUTHORIZED.
- Next: only promote vintage gate if an exact archived October NBK payload/revision history and IMF series-vintage provenance are obtained. Otherwise retain PARTIAL and advance to next eligible cohort member. No repeat numeric extraction, IMF re-query or cohort rebuild.
## Continuation 146 — Azerbaijan AZE Q2-2026 CBAR portfolio-only source scope gate (2026-11-21)
- Reopened Master Ledger, Priority Queue and immutable 63-country cohort. AZE is an eligible member; no dedicated Q2-2026 national portfolio-only dual-leg validation report found. No IMF re-query/cohort rebuild.
- Official CBAR Statistical Bulletin 09/2026, Table 1.4, USDm, QII 2026: https://uploads.cbar.az/assets/34f2e92e50d556d098dd5b36f.pdf. It publishes top-level net acquisition of financial assets and net incurrence of liabilities, but both subcategory rows combine 'portfolio and other investments'; no separate Q2 portfolio-only values are exposed. Combined category is not a valid portfolio-only proxy.
- CBAR 15-Sep-2026 H1 briefing as reported by APA gives six-month portfolio component figures (assets -USD0.3bn, liabilities -USD2.0bn). These are H1 cumulative, not Q2-only, and cannot substitute for Q2 or be differenced absent Q1 same-vintage portfolio-only rows.
- Reused archived IMF exact rows: AZE A_NFA_T OBS_VALUE=-333337000 USD SCALE=6; L_NIL_T=-8044000.0000001 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion, netting, residual inference or IMF re-query.
- National Q2 portfolio-only asset/liability legs NOT_CAPTURED; Q2 combined portfolio+other rows explicitly excluded; national sign/scale/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; AZE PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_AZERBAIJAN_AZE_Q2_2026_CBAR_PORTFOLIO_SOURCE_SCOPE_GATE_CONTINUATION146_20261121.md.
- Next: obtain official detailed Q2 BOP annex/workbook with portfolio separated from other investment, preserve bytes/hash, compare two legs and vintage. If unavailable, retain PARTIAL and advance; do not derive Q2 from H1 or combined rows. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 147 — Ecuador ECU Q2-2026 BCE portfolio dual-leg numeric reconciliation (2026-11-21)
- Reopened Master Priority Queue, Master Continuity Ledger and immutable 63-country Q2 cohort; ECU is eligible and no dedicated ECU Q2-2026 dual-leg report was found. No IMF re-query/cohort rebuild.
- Official BCE SDDS/NEDD English external-sector page, last updated 10-Nov-2026, publishes Q2/26 BOP USDm with separate portfolio rows: asset net acquisition -595.2; liability net incurrence +1,000.3. Page says unless otherwise indicated data are final and BOP/IIP follow IMF BPM6. BCE Q2 press release dated 1-Oct-2026 independently confirms portfolio assets decreased USD595.2m and total liabilities incurred USD1,519.3m.
- Reused archived IMF rows: ECU A_NFA_T OBS_VALUE=-595164167.96001 USD SCALE=6; L_NIL_T=1000348809 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Declared SCALE=6 display conversion only: assets -595.16416796001 USDm vs BCE -595.2 (difference -0.03583203999); liabilities +1,000.348809 USDm vs BCE +1,000.3 (difference -0.048809). Both PASS at national 0.1 USDm precision; no sign inversion or netting.
- National separate-leg/period/unit/BPM6 scope PASS; archived IMF raw row provenance PASS. Same-vintage NOT_ESTABLISHED (BCE NEDD update 10-Nov; IMF archive 19-Nov but no exact synchronized release/extraction vintage). National raw HTML/PDF SHA256 NOT_CAPTURED. ECU numeric dual-leg gate PASS at publication precision; full acceptance PARTIAL; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_ECUADOR_ECU_Q2_2026_BCE_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION147_20261121.md.
- Next: archive exact national page/report bytes and SHA256, obtain same-vintage metadata, then advance cohort. No repeated numeric extraction, IMF re-query or cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 148 — Costa Rica CRI Q2-2026 SECMCA/BCCR portfolio dual-leg numeric comparison (2026-11-21)
- Reopened Master Priority Queue, Master Continuity Ledger and fixed 63-country cohort; CRI is a cohort member and no dedicated CRI Q2-2026 portfolio dual-leg report found. No IMF re-query/cohort rebuild.
- SECMCA ESEA analytical BOP page for Costa Rica displays separate Q2-2026 portfolio investment asset and liability flows in USDm: assets +1,275.5; liabilities +1,167.5. Q2 is the second-quarter column (not H1). It further splits assets into equity/fund shares 998.7 and debt 276.7; liabilities into equity/fund shares 16.0 and debt 1,151.5. SECMCA describes BOP as transactions over a period and units USDm.
- BCCR NEDD page independently shows Q2/26 and DSBB standards/final-data statement, but its visible summary only gives total financial account -2,474.6 USDm; separate IIP portfolio rows are stocks and excluded from flow test. Thus detailed flow legs are from SECMCA regional statistical portal, not yet captured from BCCR primary export.
- Reused IMF raw rows: CRI A_NFA_T OBS_VALUE=1275459662.03478 USD SCALE=6; L_NIL_T=1167506330.15469 USD SCALE=6. Panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Display conversion only via SCALE=6: assets +1,275.45966203478 vs SECMCA +1,275.5 (difference +0.04033796522); liabilities +1,167.50633015469 vs SECMCA +1,167.5 (difference -0.00633015469). Both PASS at 0.1 USDm precision; no sign inversion/netting.
- National primary BCCR raw export/series IDs and SHA256 NOT_CAPTURED; exact same-vintage NOT_ESTABLISHED (SECMCA row-specific revision vintage and IMF extraction-vintage not linked). Numeric dual-leg gate PASS at portal precision; full acceptance PARTIAL; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_COSTA_RICA_CRI_Q2_2026_SECMCA_BCCR_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION148_20261121.md.
- Next: capture SECMCA export and metadata, map to BCCR primary series, verify revision/vintage; then advance cohort. No repeated numeric extraction, IMF re-query or cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 149 — Dominican Republic DOM Q2-2026 BCRD quarterly BOP source gate (2026-11-21)
- Reopened Master Priority Queue, Master Continuity Ledger and fixed 63-country cohort; DOM is a member, no dedicated Q2-2026 national portfolio dual-leg report found. No IMF re-query/cohort rebuild.
- BCRD official Sector Externo page lists quarterly BPM6 BOP dataset 2010–2026 and direct XLSX: https://cdn.bancentral.gov.do/documents/estadisticas/sector-externo/documents/bpagos_trim_6.xlsx. Browser fetch failed with unsupported content-type application/octet-stream; direct download failed; workbook bytes/sheets/hash not captured.
- BCRD Informe Enero-Junio 2026 (Sept 2026), pp.41–42 / Anexo 3 pp.80–81 provides H1 cumulative portfolio legs: assets +305.2 USDm; liabilities +2,366.5 USDm. Explicitly not Q2-only. BCRD preliminary Jan-Sep 2026 report gives 9M cumulative legs: assets +136.3 USDm; liabilities +2,473.9 USDm. Explicitly not Q2-only. No H1/9M-to-Q2 inference or netting.
- H1 table's sign note: negative = Dominican net borrowing from rest of world; positive = net lending. Do not infer exact Q2 signs from cumulative rows.
- Reused IMF raw rows: DOM A_NFA_T OBS_VALUE=340200000 USD SCALE=6; L_NIL_T=-184000000 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No transformation or IMF re-query.
- Q2 national portfolio asset/liability legs NOT_CAPTURED; H1/9M separate legs captured but wrong period; sign/scale/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; DOM PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_DOMINICAN_REPUBLIC_DOM_Q2_2026_BCRD_QUARTERLY_BOP_XLS_SOURCE_GATE_CONTINUATION149_20261121.md.
- Next: recover exact BCRD quarterly XLSX, preserve bytes/hash and inspect Q2-only portfolio legs, then compare and establish vintage. If inaccessible, retain PARTIAL and advance. Do not repeat same unsupported fetch, use H1/9M as Q2, or infer residuals. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 150 — Panama PAN Q2-2026 INEC MBP6 Excel access and period gate (2026-11-21)
- Reopened Master Priority Queue, Master Continuity Ledger and fixed 63-country cohort. PAN is a cohort member; no dedicated Q2-2026 national portfolio dual-leg report found. No IMF re-query/cohort rebuild.
- INEC official BOP publication dated 25-Sep-2026 is explicitly January–June 2026 (H1), uses BPM6 tables and public/private aggregate sector. Official page exposes MBP6 Table 1 Excel: https://www.inec.gob.pa/archivos/P0774740120260925095521Cuadro%201.%20Componentes%20Normalizados%20-%20MBP6.xlsx. Browser retrieval failed with 400 Unsupported content-type application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; workbook bytes/sheets/hash not captured.
- Current INEC publication index lists the H1-2026 release and prior Q1-2026 release dated 26-Jun-2026, but no Q2-only 2026 BOP release. H1 must not be treated as Q2 or differenced with Q1 without exact same-vintage portfolio-only rows.
- Reused exact IMF rows: PAN A_NFA_T OBS_VALUE=3328699298.09 USD SCALE=6; L_NIL_T=450738775.03 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion, netting or IMF re-query.
- National Q2 portfolio legs NOT_CAPTURED; Q2-only publication NOT_ESTABLISHED; H1 substitute prohibited; national sign/scale/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; PAN PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_PANAMA_PAN_Q2_2026_INEC_BOP_MB6_EXCEL_ACCESS_AND_PERIOD_GATE_CONTINUATION150_20261121.md.
- Next: recover official workbook and await/locate Q2-only release; preserve bytes/hash, extract separate Q2 legs, compare only after period and vintage proof. If absent, retain PARTIAL and advance. ₹0; no production changes; UNKNOWN never PASS.

## Continuation 151 — Colombia COL Q2-2026 BanRep quarterly source confirmation (2026-11-21)
- Reopened Master Ledger, Priority Queue, immutable 63-country cohort, prior COL source-boundary report and batch-10 queue. Reused archived IMF rows; no IMF re-query or cohort rebuild.
- New official BanRep Q2-2026 BOP/IIP report (published 1-Sep-2026) explicitly says Q2 net portfolio-instrument liquidations partially offset net capital inflows, but the accessible narrative does not publish separate numerical asset/liability transaction legs. End-June IIP portfolio positions are stocks and excluded.
- Official SUAMECA multiple-download catalogue independently lists separate quarterly portfolio asset net-acquisition and liability net-incurrence series, each in current USDm, from 31-Mar-2000 through 30-Jun-2026, last updated 1-Sep-2026. This confirms the correct official series families and Q2 coverage; exact series IDs and Q2 values were not exposed in the captured catalogue response.
- BanRep's official user guide confirms the multiple-download service is designed to select historical variables and generate tables; the documented export control is desktop-only. The previously tested direct portal page returned 502. No raw export, response bytes, retrieval timestamp, SHA-256, or exact vintage metadata captured.
- Detail: docs/GCR_COLOMBIA_COL_Q2_2026_BANREP_SUAMECA_OFFICIAL_QUARTERLY_SOURCE_CONFIRMATION_CONTINUATION151_20261121.md (commit c3ddbbbfedc47208aeee8460d59dabbc7e4e099d).
- Acceptance: cohort PASS; official separate series identity/quarterly frequency/USDm/Q2 coverage PASS; exact values/IDs/raw export/hash NOT_CAPTURED; sign/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; COL PARTIAL / BLOCKED, NOT PASS; aggregate NOT_AUTHORIZED.
- Next: use documented desktop SUAMECA export or a genuinely different supported official export route for both legs together; if inaccessible, stop repeating the same 502 route and advance. Do not use IIP stocks, narrative, or net flow as substitutes. ₹0; no production changes; UNKNOWN never PASS.


## CPV — Cabo Verde Q2-2026 BCV official BOP source gate (Continuation 153, 2026-11-21)
- Selected from the immutable 63-country Q2-2026 dual-leg cohort after Continuation 152 retained COL PARTIAL/BLOCKED and the prior queue preflight found no CPV country report. No cohort rebuild or IMF re-query.
- BCV official BOP catalogue (page rendering 17-Nov-2026) lists XLS “Balança de Pagamentos” covering 2012-Q1 through 2026-Q2. Exact workbook URL was followed via web and attempted via separate direct byte-download route; both failed (timeout/download failure). No workbook bytes, sheet structure, Q2 values, raw receipt or SHA-256. Catalogue coverage is not proof of separate portfolio legs.
- BCV Q1 bulletin shows a net portfolio line only and is not a Q2 substitute. BCV statistical overview distinguishes quarterly BOP transactions from quarter-end IIP stocks.
- Methodology conflict: IMF e-GDDS metadata describes BPM5/CVE and average monthly FX; BCV March-2026 bulletin footnote says BPM6. Metadata freshness not established; do not silently choose a standard.
- Reused exact archived IMF Q2 rows: CPV A_NFA_T OBS_VALUE=364678.4706264281 USD SCALE=6; L_NIL_T OBS_VALUE=0 USD SCALE=6. Raw panel Git blob SHAs 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion or comparison admitted.
- CPV cohort/IMF row presence PASS; official workbook locator and period coverage PASS; national dual-leg layout NOT_VERIFIED; current BPM version CONFLICT; national values/raw bytes/hash NOT_CAPTURED; sign/scale/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; CPV PARTIAL/BLOCKED, NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_CABO_VERDE_CPV_Q2_2026_BCV_OFFICIAL_BOP_SOURCE_GATE_CONTINUATION153_20261121.md (commit c5199494261675cc599bd5f82e3862ba9cf41c9d). Next: genuinely different supported BCV export route and current methodology evidence; otherwise advance. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 154 — Georgia GEO Q2-2026 NBG official BOP source-boundary audit (2026-11-21)
- Re-fetched current ledger (pre-task blob SHA c6a953ff88dcae619023bfd11235a1e7936ad12a), GCR queue (0e5fb9304e5af696042aa1919f2f1fa49f651850), immutable 63-country cohort (31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8) and CPV Continuation 153. GEO is in fixed cohort with both IMF panel legs present; no prior dedicated GEO Q2 national dual-leg report found. No IMF query or cohort rebuild.
- Official NBG “Balance of Payments of Georgia (II Quarter 2026)” release, 30-Sep-2026, confirms Q2 and explicitly states BPM5. Accessible release text does not publish separate Q2 portfolio-asset/liability transaction amounts. Official NBG NSDP labels separate “Portfolio investment: Assets” and “Portfolio investment: Liabilities” in USDm, but the visible data period is Q3/21, stale for Q2-2026. NBG BOP publication page says data are regularly revised and revisions may apply to any period.
- Official NBG Q2 IIP release reports quarter-end stock positions; excluded from BOP transaction-flow validation. No current Q2 separate-leg dataset/API response, national raw bytes, receipt, timestamp or SHA-256 captured.
- Reused archived IMF raw rows: GEO A_NFA_T OBS_VALUE=325871168.2 USD SCALE=6; L_NIL_T OBS_VALUE=416264206.49 USD SCALE=6. Existing raw panel blob SHAs 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion or numeric comparison.
- Acceptance: cohort/IMF row presence PASS; official Q2 BOP release and BPM5 statement PASS; separate Q2 national transaction legs NOT_CAPTURED; visible NSDP labels PASS for taxonomy only but period stale; item/sign/scale/vintage equivalence NOT_ESTABLISHED; national raw bytes/hash NOT_CAPTURED; numeric comparison NOT_DONE; GEO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_GEORGIA_GEO_Q2_2026_NBG_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION154_20261121.md (commit 3af8633ad131bf2aa95da82a48b4e4c8aff9c8f9).
- Next: investigate a genuinely different NBG current statistics export/API for Q2 separate portfolio transaction legs and dated revision metadata; do not retry same release page, use stale NSDP values or substitute IIP stocks. If unavailable, retain GEO PARTIAL and advance. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 155 — BDI Burundi Q2-2026 official BRB source boundary (2026-11-21)
- Rank-1 country validation continues from GEO. BDI is confirmed in the immutable 63-country cohort with both archived IMF Q2 rows present; no prior dedicated BDI Q2 national dual-leg report.
- BRB Q4-2025 Monetary Policy Report (published 26-Feb-2026) Table 9 supplies historical separate portfolio asset/liability legs in MBIF, but not target Q2-2026. Current BRB “Autres Documents” index shows Q4-2025/Q3-2025 reports; no Q2-2026 BOP table captured.
- Reused IMF Q2 raw rows: A_NFA_T=130723.2699945969 USD SCALE=6; L_NIL_T=0 USD SCALE=6. Raw panel blobs unchanged. No conversion or numeric comparison.
- BDI Q2 national legs NOT_CAPTURED; unit/sign/BPM/vintage bridge NOT_ESTABLISHED; BDI PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail report: docs/GCR_BURUNDI_BDI_Q2_2026_BRB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION155_20261121.md.
- GEO source-route addendum: official NBG NSDP advertises BOP Browse Data / Download in SDMX, but exact download URL/current Q2 data not captured. NBG Q2-2026 release's BPM5 statement conflicts with NBG's own official notice that BPM6 applies from 2015 onward; GEO remains PARTIAL pending resolution.
- Next: continue rank-1 validation with the next eligible immutable-cohort member after duplicate-report and official-source feasibility checks. No IMF re-query/cohort rebuild, stock-as-flow, annual-to-quarter allocation, net-to-leg back-solving or production change. ₹0; UNKNOWN never PASS.


## Continuation 156 — BIH Bosnia and Herzegovina Q2-2026 CBBH source boundary (2026-11-21)
- Selected after BDI from immutable 63-country cohort; duplicate search found no dedicated BIH Q2 national dual-leg report. BGD skipped as its national net-only and annual-survey routes were already exhausted.
- CBBH release calendar schedules Q2-2026 BOP by 30-Sep-2026. Bulletin 2 2026 T15 contains BPM6 KM-million BOP and separate portfolio asset/liability legs only through Q1 2026 (Q1 asset=-101 KMm, liability=0 KMm; not Q2). CBBH official portal guide documents anonymous access and Excel/PDF export; dynamic Panorama Necto portal was inaccessible in this browser session, so Q2 export NOT_EXECUTED.
- IMF e-GDDS confirms quarterly CBBH BOP, KM million and revision practices. Reused exact archived IMF Q2 rows: BIH A_NFA_T=61489941.04204912 USD SCALE=6; L_NIL_T=1324417089.731674 USD SCALE=6. Raw panel blobs unchanged. No conversion/comparison.
- Q2 national legs/raw bytes/hash NOT_CAPTURED; portal execution NOT_EXECUTED; sign/scale/vintage bridge NOT_ESTABLISHED; BIH PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail report: docs/GCR_BOSNIA_HERZEGOVINA_BIH_Q2_2026_CBBH_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION156_20261121.md.
- Next: attempt exact anonymous CBBH portal Q2 export only through supported interactive access; if unavailable, retain BIH PARTIAL and advance to next eligible cohort member. No Q1/IIP/BIS/projection substitute, net-to-leg inference, IMF re-query, cohort rebuild or production changes. ₹0; UNKNOWN never PASS.


## Continuation 157 — BLZ Belize Q2-2026 CBB official BOP source boundary (2026-11-21)
- Selected after BIH from fixed cohort; no prior dedicated BLZ Q2 national dual-leg report. BIH CBBH dynamic portal remains NOT_EXECUTED; no repeat.
- Official CBB June-2026 Quarterly Review Table A.22 (page 51, $mn) publishes separate portfolio asset=0.0 and liability=0.0 for Jan–June 2026, H1 cumulative only. 2026 figures provisional. Table A.21 net-only and IIP Table A.31 not substitutes.
- Official BOP page exposes full XLSX locator; browser fetch returned HTTP 400 unsupported XLSX MIME, so no workbook bytes/sheets/Q2 values/hash. IMF e-GDDS describes quarterly BOP and separate portfolio legs.
- Reused IMF Q2 raw rows: BLZ A_NFA_T=142.2106890070215 USD SCALE=6; L_NIL_T=0 USD SCALE=6. Raw panel blobs unchanged. No conversion/comparison. BLZ Q2-only national legs NOT_CAPTURED; BLZ PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail report: docs/GCR_BELIZE_BLZ_Q2_2026_CBB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION157_20261121.md.
- Next: supported raw-byte/export retrieval of CBB official XLSX; inspect exact Q2 dual legs. If inaccessible, retain BLZ PARTIAL and advance. No H1-to-Q2 inference, IIP substitution, net-to-leg inference, IMF query, cohort rebuild or production changes. ₹0; UNKNOWN never PASS.


## Continuation 158 — BOL (Bolivia) Q2-2026 source-gate result
- BOL was selected from the immutable 63-country cohort after checking the latest ledger/queue and confirming no prior dedicated BOL Q2 national dual-leg report. Both archived IMF Q2 rows are present; no re-query or cohort rebuild.
- BCB's official VI Manual page lists two quarter-specific files: “Balanza de Pagos” XLSX and “Series de tiempo: Balanza de Pagos” XLSX for SEGUNDO TRIMESTRE 2026. Both XLSX retrieval attempts failed at the supported web route (HTTP 400 unsupported XLSX MIME) and separate byte-download attempt did not yield bytes. The H1-2026 publication is not a Q2 substitute.
- IMF raw values reused exactly: A_NFA_T OBS_VALUE=-154107393.924487, SCALE=6; L_NIL_T OBS_VALUE=974071938.904098, SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 / 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Status: official Q2 locators PASS; national values/bytes/layout NOT_CAPTURED; Q2 methodology/sign/unit/scale/vintage NOT_ESTABLISHED; comparison NOT_DONE; BOL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BOLIVIA_BOL_Q2_2026_BCB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION158_20261121.md (commit 88a2d13a353f73a2af386fc1f31deaa4ab7879be).
- Next rank-1 bounded item: BLR Belarus source feasibility, after duplicate-report check; retain BOL PARTIAL and revisit only with a genuinely supported official BCB byte/export route. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 159 — BLR (Belarus) Q2-2026 source-gate result — Chapter 47 Part 7
- Selected after BOL from the immutable 63-country cohort; no duplicate dedicated BLR Q2 national dual-leg audit. Both archived IMF Q2 raw rows present; no IMF re-query/cohort rebuild.
- NBRB official BPM6 methodology and metadata confirm quarterly BOP, standard/analytic presentations, separate net asset acquisition/liability incurrence by functional category, portfolio investment classification, USD/BYN, and preliminary/revision policy. Live data page timed out/inaccessible; Q2-2026 national asset/liability values and raw bytes NOT_CAPTURED.
- Exact archived IMF values reused: A_NFA_T OBS_VALUE=6414501.08999999, SCALE=6; L_NIL_T OBS_VALUE=-325487157.39, SCALE=6. Raw panel Git blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 / 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Status: cohort/IMF row presence PASS; official BPM6/quarterly methodology PASS; national Q2 dual legs/raw bytes NOT_CAPTURED; Q2 vintage/item/sign/scale bridge NOT_ESTABLISHED; comparison NOT_DONE; BLR PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BELARUS_BLR_Q2_2026_NBRB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION159_20261121.md (commit 47c7d96056c770943d12cd7040b5cf95d726f2d2).
- Next rank-1 bounded action: supported NBRB Q2-2026 bulletin/data-export raw-byte retrieval; if inaccessible, retain BLR PARTIAL and advance. No IIP/annual/adjacent-quarter/net-total substitute, no production changes; ₹0; UNKNOWN never PASS.


## Continuation 160 — Chapter 47 Part 8 update (2026-11-21)
- BLR follow-up: NBRB official latest 2026 publication locator is Jan–June; exact PDF timeout/direct download failure; Q2 national legs remain uncaptured. Keep BLR PARTIAL; no H1 substitution.
- CHL selected after cohort/duplicate preflight. Official BCCh Q2 BOP publication + official BDE monthly source independently expose both portfolio transaction legs. Q2 BDE sums: assets USD 5,098.91m; liabilities USD 5,397.51m; net difference USD 298.60m, rounding to Q2 report's USD 299m net. No net-to-leg back-solving.
- IMF archived CHL Q2 values: asset 5,098,898,918.11 USD SCALE=6; liability 5,397,501,758.8 USD SCALE=6. Diagnostic /1e6 is near BDE sums but not admitted as PASS; exact same-vintage cut-off and source raw bytes/SHA-256 remain missing. CHL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detailed report: docs/GCR_CHILE_CHL_Q2_2026_BCCH_BDE_MONTHLY_DUAL_LEG_VINTAGE_AUDIT_CONTINUATION160_20261121.md (commit df6d0252ef70c345308a1da44574671050f8141e).
- Next: documented raw export/API capture for the two BCCh BDE series, with response bytes, timestamp, series codes, vintage metadata and SHA-256; then exact sign/scale/vintage reconciliation. If unavailable, retain PARTIAL and advance. No IMF re-query/cohort rebuild or production changes; ₹0; UNKNOWN never PASS.


## Continuation 161 — Chapter 47 Part 9 priority update (2026-11-21)
- CHL Part 8 established separate official monthly BDE portfolio asset/liability flows and Q2 arithmetic, but not immutable raw bytes. Part 9 confirms the official free REST API is account/token-gated; no authorized BDE token in context, so no API request was made. The public Canasta UI advertises Excel export, but export action and bytes remain NOT_EXECUTED/NOT_CAPTURED.
- CHL stays PARTIAL / NOT PASS; raw SHA-256 and same-vintage metadata unresolved; aggregate NOT_AUTHORIZED.
- Rank-1 next: authorized BDE API or Canasta Excel export capture if available; otherwise stop retrying credential-gated endpoint and advance to next eligible immutable-cohort country. Do not request/store secrets or change production. ₹0; UNKNOWN never PASS.


## Continuation 162 — Chapter 47 Part 10 priority update (2026-11-21)
- COL remains PARTIAL/BLOCKED: official BanRep catalogue exposes separate quarterly portfolio asset/liability series through Q2-2026, but SUAMECA multiple-download returned 502 and prebuilt dashboard timed out; no exact Q2 observations/raw export captured. Do not substitute IIP stocks or financial-account net totals.
- Next eligible queue item: POL (Poland) per existing batch priority, after avoiding further identical COL 502/timeout/SDMX probes. For POL, use only a genuinely new XLSX-capable raw-byte route; prior exact NBP workbook endpoint already failed, so no identical retries. Preserve status until source bytes/legs/vintage/sign are evidenced. ₹0; UNKNOWN never PASS.


## Continuation 163 — Chapter 47 Part 11 priority update (2026-11-21)
- POL Q2 blocker partially resolved: distinct official NBP Q2 release (30-Sep-2026) Appendix 1 publishes separate portfolio assets 24,144 mn PLN and liabilities 70,910 mn PLN, with equity/debt components summing exactly to each leg. Prior bopa_en.pdf date mismatch does not apply to this separate Q2 PDF.
- Existing IMF exact values reused: +USD6,602m assets and +USD19,391m liabilities. NBP PDF raw-byte SHA-256 not captured; transaction USD/PLN conversion method and same-vintage bridge not established. No cross-currency comparison; POL remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Rank-1 next: obtain NBP PDF raw bytes/hash and authoritative transaction FX/vintage bridge or matched USD legs. If no route, preserve captured PLN legs and advance to next eligible country. Do not retry known NBP XLSX unsupported route. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 164 — Chapter 47 Part 12 priority update (2026-11-21)
- POL NBP methodology gate: official Sep-2023 methodological notes establish quarterly publication timing, September Q2 revision cycle (up to nine quarters), security-by-security source and portfolio transaction valuation, but do not specify exact Q2 portfolio transaction FX conversion rule. NBP Q2 release is Sep-30 vintage; IMF raw archive Nov-19; vintage equivalence NOT_ESTABLISHED.
- Raw Q2 PDF download via new container route failed; raw SHA-256 not captured. POL retains PARTIAL / NOT PASS. Next: seek explicit official reporting-form FX conversion spec or matched-vintage USD dual-leg table; otherwise advance, no repeated PDF attempts or ad-hoc FX. ₹0; UNKNOWN never PASS.


## Continuation 165 — Chapter 47 Part 13 priority update (2026-11-21)
- POL: Official NBP reporting notes v1.8 establish transaction FX rule for portfolio securities: actual exchange rate on transaction date (or §6 fallback actual rate / NBP average rate on preceding day); quarter-end average rate applies to end-period balances, not flows. PW-AIN and PW-RIN examples demonstrate trade-date rate distinctly from end-period rate.
- This closes the methodology-rule discovery gap, but does not permit converting national Q2 PLN aggregate totals to USD without transaction-level currency/date weights or an official matched USD Q2 dual-leg aggregate. NBP PDF SHA-256 and Sep-30 NBP vs Nov-19 IMF same-vintage bridge remain open. POL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: seek official NBP Q2 USD dual-leg aggregate/series and vintage metadata; if unavailable, preserve PLN values and advance. No quarter-average/quarter-end/implied-rate aggregate conversion. ₹0; UNKNOWN never PASS.


## Continuation 166 — Chapter 47 Part 14 priority update (2026-11-21)
- POL: no official matched Q2-2026 USD portfolio asset/liability table found in bounded NBP official-domain search. Retain NBP Q2 legs in PLN (assets 24,144m; liabilities 70,910m); do not infer USD using aggregate FX. POL PARTIAL / NOT PASS.
- TUR: TCMB official page confirms monthly BPM6/EVDS and separate USD portfolio assets/liabilities. September summary table is Sep monthly + Jan-Sep cumulative + 12-month, not Q2-only. Existing Q2 PDF sums remain assets 5,749 vs IMF 5,749; liabilities 9,183 vs IMF 9,270 (87m unexplained). Exact official ZIP endpoint previously timed out; no new byte-preserving route, do not repeat. TUR PARTIAL / NOT PASS.
- Next eligible cohort member NPL: avoid previously failed NRB XLSX and stale NSDP/SDMX routes; use only a genuinely new official supported API/export. If unavailable, close once and advance to RWA. ₹0; no IMF re-query/cohort rebuild; aggregate NOT_AUTHORIZED; UNKNOWN never PASS.


## 2026-11-21 — Duplicate-prevention handoff correction
- Mandatory GCR historical task registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`.
- Correction to stale Continuation 166 handoff: NPL is NOT a fresh next task. Its NRB BPM6 XLSX, stale NSDP XML and wrong-family archive routes were already audited/closed across Continuations 55/56/58/94/128/130. Do not repeat absent a genuinely new supported official route.
- RWA is also NOT a fresh task: BNR portal source gate Continuation 97 and portal recheck Continuation 130 already exist; exact JS-only portal route remains unresolved. Do not repeat absent a new exact download/API/export route.
- SLV has Continuation 100 history and is not a new-country candidate. Reconcile the complete queue and report inventory before selecting any next country; stale rank snippets cannot override prior work.
- Enforce route fingerprints, PASS skip, named unmet gate for PARTIAL, no retry of closed BLOCKED routes without new evidence, and final re-fetch verification of report/ledger/queue. Aggregate remains NOT_AUTHORIZED; no production changes; ₹0; UNKNOWN never PASS.


## Continuation 167 — Honduras HND BCH Q2-2026 source gate (2026-11-21)
- Selected HND from the immutable 63-country cohort after preflight; no dedicated HND Q2 national dual-leg report found. Reused existing cohort; no IMF re-query/cohort rebuild.
- BCH official dynamic BOP page confirms quarterly/annual frequency and provides an XLSX locator. Official calendar specifies quarterly BOP reporting and a 90-day release schedule; SDDS page lists BOP Browse Data/SDMX.
- XLSX locator redirects to SharePoint WOPI app shell; container byte-download failed. Official SDMX XML route returned HTTP 400 unsupported text/xml. No raw bytes, sheets, observations, Q2 portfolio legs or SHA-256 captured. Q3-2025 chart is not Q2 evidence.
- HND PARTIAL / NOT PASS; Q2 portfolio assets/liabilities NOT_CAPTURED; sign/unit/vintage NOT_ESTABLISHED; comparison NOT_DONE; aggregate NOT_AUTHORIZED. Detail: `docs/GCR_HONDURAS_HND_Q2_2026_BCH_OFFICIAL_BOP_SOURCE_AND_XLSX_ACCESS_GATE_CONTINUATION167_20261121.md` (commit `bb1df78f301d016ab90b13c0d6fcbd2f342a0335`).
- Do not repeat identical XLSX/WOPI/XML routes. Reopen only with a new supported official API/export/byte route. Next selection must follow complete report-history preflight. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 168 — Chapter 47 Part 16: Kosovo KOS BQK Q2-2026 ROW transaction-matrix source gate (2026-11-21)
- Re-fetched current ledger, GCR queue, duplicate registry and immutable 63-country cohort before selection. KOS is in the fixed Q2-2026 both-leg cohort (A_NFA_T and L_NIL_T PRESENT); no dedicated prior KOS national dual-leg report found in scoped repository search. No IMF re-query/cohort rebuild.
- New official BQK route identified: External Sector Statistics → Financial Accounts Statistics → REST OF THE WORLD (S.2) → ROW Matrix — Transactions, period Q2 2026. Exact XLS locator: https://bqk-kos.org/wp-content/uploads/2024/09/ROW%20Matrix%20%E2%80%93%20Transactions.xls . BQK methodology states financial-account statistics record transaction flows by financial instrument and assets/liabilities for relations with non-residents; methodology aligned with ESA 2010/SNA 2008 and BPM6.
- Browser XLS fetch returned HTTP 403 Forbidden; no workbook bytes/sheets/rows/portfolio leg values/hash. Separate BQK monthly Financial account XLS route returned HTTP 400 unsupported Excel MIME; container download failed. These identical routes are closed absent a new supported transfer capability.
- Q2 IIP International Investment Portfolio is a stock product and is NOT_ADMITTED as a transaction-flow substitute. Do not use financial-account net totals or net-to-leg back-solving.
- Status: cohort membership PASS; official ROW transaction-matrix locator/methodology PASS; actual workbook bytes NOT_CAPTURED; portfolio leg exposure NOT_VERIFIED; Q2 national asset/liability legs NOT_CAPTURED; sign/unit/vintage NOT_ESTABLISHED; KOS PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_KOSOVO_KOS_Q2_2026_BQK_ROW_TRANSACTION_MATRIX_SOURCE_GATE_CONTINUATION168_20261121.md (commit 8bdb4ee396a68591f46fdcd56f75a365ea48c501).
- Next exact action: only retrieve the exact ROW transaction XLS through a genuinely new supported official byte-transfer/export route; inspect S.2 transactions, instrument labels, Q2 header and separate portfolio asset/liability legs. Then reuse archived IMF rows for separate-leg sign/unit/vintage comparison. No repeated failed XLS requests, no production changes; ₹0; UNKNOWN never PASS.


## Continuation 169 — Chapter 47 Part 17: The Gambia GMB CBG Q2-2026 BOP source-feasibility gate (2026-11-21)
- Re-fetched current Master Ledger, GCR Priority Queue, Historical Task Registry and immutable 63-country Q2 both-leg cohort. GMB is present with A_NFA_T_PRESENT and L_NIL_T_PRESENT; scoped repository search found no prior dedicated GMB national portfolio dual-leg report. No IMF re-query/cohort rebuild.
- Official CBG Monetary Policy Report August 2026 inspected. It confirms preliminary Q2-2026 BOP; current account deficit USD34.6m, capital account surplus USD26.2m, financial-account net inflow USD95.4m. Narrative names FDI inflows USD83.3m, other investment net inflows USD24.1m and reserve-asset net acquisition USD12.0m. Appendix Table 2 reports Q2 financial-account net -95.4; Table 5 only current account/capital account/net lending-borrowing. No portfolio investment row found in report; national Q2 portfolio asset/liability legs NOT_CAPTURED. Absence does not imply zero.
- CBG Statistics page points to its Macroeconomic Data Warehouse; linked URL redirects to an interactive app shell with generic editor/CSV-upload instructions and no visible BOP catalogue, series IDs, export payload or API. CBG quarterly-bulletin page rendering lists files through 2018 only. Historical 2017/18 portfolio-net rows are not Q2-2026 evidence.
- IMF DSBB metadata search result states CBG compiles BOP quarterly using BPM5. This confirms frequency/methodology metadata only, not BPM6 comparability or national Q2 dual legs.
- Status: fixed cohort membership PASS; official Q2 report inspected PASS; quarterly compilation metadata PASS; Q2 national portfolio asset/liability legs NOT_CAPTURED; data warehouse payload NOT_EXTRACTED; sign/unit/classification/vintage NOT_ESTABLISHED; GMB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_GAMBIA_GMB_Q2_2026_CBG_BOP_QUARTERLY_REPORT_AND_DATAWAREHOUSE_SOURCE_GATE_CONTINUATION169_20261121.md (commit ac53489c52ff5bcc4389cdb1a4969c6ecfe13023).
- Next: seek only a distinct public CBG Q2 BOP table or documented data-warehouse API/export payload with separate portfolio asset/liability transaction legs and metadata. If unavailable, close this route and advance after full preflight. No net-to-leg back-solving, no zero inference, no old-quarter substitute, no production changes; ₹0; UNKNOWN never PASS.


## Continuation 170 — Chapter 47 Part 18: Guinea GIN BCRG Q2-2026 BOP source-boundary audit (2026-11-21)
- Re-fetched current Master Ledger, GCR Priority Queue, Historical Task Registry, immutable 63-country cohort, and previous GMB Continuation 169 report. GIN is in the fixed cohort with both IMF rows present; scoped repository searches found no prior dedicated GIN Q2 national dual-leg report. GMB remains PARTIAL and its same route was not repeated. No cohort rebuild or IMF re-query.
- Official BCRG 2026 index and 22nd MPC page (22-Sep-2026 listing; meeting document download label) located. The rendered MPC page did not expose a retrievable document URL. Official BCRG BOP statistics index and Balance des paiements page located; rendered BOP page exposes title but no visible dataset, series IDs, download or API payload.
- Inspected official BCRG June-2025 Q1 monetary policy report. Its Table 11 and Appendix Table 17 show portfolio investment as a single net functional-category row only, not separate asset/liability transaction legs. Historical 2024–Q1 2025 net values are explicitly not used for Q2-2026 and do not prove 2026 detailed data lack a split.
- Current Q2-2026 national portfolio assets/liabilities NOT_CAPTURED; September 2026 MPC raw bytes/hash NOT_CAPTURED; BOP statistics API/export NOT_EXTRACTED; sign/unit/classification/vintage NOT_ESTABLISHED; comparison NOT_DONE; GIN PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_GUINEA_GIN_Q2_2026_BCRG_OFFICIAL_BOP_SOURCE_BOUNDARY_AND_REPORTING_ROUTE_CONTINUATION170_20261121.md (commit f524e985d943eb180db883adcc047567005393d4).
- Next: find the actual document URL behind the official September 2026 MPC download control or a distinct public BCRG BOP export/API. Preserve raw bytes/hash and metadata before inspecting Q2 separate portfolio legs. If no new locator exists, retain PARTIAL and advance after full preflight. No historical net-to-leg back-solving, no production changes; ₹0; UNKNOWN never PASS.


## Continuation 171 — Chapter 47 Part 19: Lao PDR LAO BOL Q2-2026 BOP dual-leg source-boundary audit (2026-11-21)
- Re-fetched Master Ledger, GCR Priority Queue, Historical Task Registry, immutable 63-country Q2 cohort and GIN Continuation 170 report. LAO exact cohort row has A_NFA_T_PRESENT and L_NIL_T_PRESENT; scoped repository search found no dedicated LAO national Q2 dual-leg report. GIN remains PARTIAL and no BCRG page retries. No IMF re-query/cohort rebuild.
- Official BOL External Sector Statistics page located: https://www.bol.gov.la/en/External_Sectors. It lists Balance of Payments, Official Reserve Assets, Exchange Rate and FDI netflow, with Download Excel/Metadata columns; indexed rendering shows no populated download link for BOP. Direct open returned HTTP 502. Annual Reports index lists 2025 report last updated 19-Aug-2026; no Q2-2026 file locator or bytes captured.
- Official BOL Annual Economic Report 2023 Table 13 demonstrates historical reporting can split Portfolio investment into net total, assets and liabilities (assets further by equity/fund shares and debt securities), in million USD. Historical values are schema-only and not Q2-2026. Official BOL historical Q4/2016 report used a net-only portfolio row, showing layout varied by vintage; current layout cannot be presumed.
- AMRO 2024 Lao PDR consultation assessment says BOL BOP is quarterly, BPM6, with 1–2 quarter publication lag. Official BOL legal PDF dated 18-Dec-2025 says BOL compiles BOP quarterly and annually, including portfolio investment among transaction types. This is methodology/compilation context, not proof Q2-2026 legs are public.
- Q2-2026 national portfolio asset/liability values NOT_CAPTURED; current Excel/metadata URL NOT_EXPOSED; raw bytes/hash NOT_CAPTURED; sign/unit/classification/vintage NOT_ESTABLISHED; comparison NOT_DONE; LAO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_LAO_PDR_LAO_Q2_2026_BOL_OFFICIAL_BOP_DUAL_LEG_SOURCE_BOUNDARY_CONTINUATION171_20261121.md (commit ed3ca079ce3e347e64e1ee46bf57b7ba2fda98cb).
- Next: resolve actual Download Excel/Metadata URLs behind BOL External Sector Statistics via a distinct supported route; capture Q2-2026 workbook bytes/hash and inspect separate portfolio asset/liability rows, sign/unit/BPM6/vintage. If unavailable/not released, retain PARTIAL and advance after full preflight. No historical/annual/H1 substitute, net-to-leg back-solving or production changes; ₹0; UNKNOWN never PASS.


## Continuation 172 — Chapter 47 Part 20: LAO official NSDP BOP XLSX/SDMX locator discovery (2026-11-21)
- Re-fetched Master Ledger, GCR Priority Queue, Historical Task Registry, Continuation 171 LAO report and immutable Q2 cohort. LAO is in fixed cohort with both IMF legs; no cohort rebuild or IMF re-query.
- New official source discovered: Lao Statistics Bureau National Summary Data Page https://www.lsb.gov.la/lsb-en.htm . Its Balance of Payments row explicitly links Browse Data, Download in SDMX and DSBB Metadata.
- Exact BOL XLSX locator resolved from Browse Data: https://www.bol.gov.la/statistics/BOP6_Lao%20PDR.xlsx . Exact BOL SDMX XML locator resolved from Download in SDMX: https://www.bol.gov.la/statistics2/BOP6_Lao%20PDR.xml . Official IMF DSBB metadata locator: https://dsbb.imf.org/egdds/dqaf-base/country/LAO/category/BOP00 . These exact links are new discoveries and close Continuation 171's locator-identification gap.
- Both BOL downloads were followed from official NSDP page but retrieval returned HTTP 400 Timeout fetching; no bytes, headers, length, XML keys, workbook sheets, observations or SHA-256. A separate container request failed DNS resolution (no HTTP response). DSBB page opened to a general shell; country-specific extracted fields not visible. Do not infer absence/zero or claim data absent.
- Q2-2026 presence, separate portfolio asset/liability legs, sign, units, BPM6 and revision vintage remain NOT_VERIFIED / NOT_ESTABLISHED. LAO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_LAO_PDR_LAO_Q2_2026_BOL_NSDP_SDMX_EXPORT_LOCATOR_DISCOVERY_CONTINUATION172_20261121.md (commit 0628b1ba96b4e3ab31e4530373c7bdb8f5070826).
- Next: retrieve exact XLSX or XML through a genuinely different supported byte-transfer route; record URL/time/status/content type/byte count/SHA-256; inspect Q2-2026 portfolio assets and liabilities separately, signs/units/vintage; only then reconcile archived IMF rows. Do not repeat same timed-out fetch path. No production changes, ₹0, UNKNOWN never PASS.


## Continuation 173 — Chapter 47 Part 21: LAO BOL SDMX Central / DSBB metadata cross-check (2026-11-21)
- Re-fetched Master Ledger, Priority Queue, Historical Registry, Continuation 172 and 171 before work. LAO fixed cohort and both IMF rows remain as previously established; no IMF re-query/cohort rebuild.
- Live official NSDP page https://www.lsb.gov.la/lsb-en.htm reconfirmed BOP Browse Data, Download in SDMX and DSBB Metadata links. Clicking BOL XLSX https://www.bol.gov.la/statistics/BOP6_Lao%20PDR.xlsx and XML https://www.bol.gov.la/statistics2/BOP6_Lao%20PDR.xml now returns HTTP 502 Bad Gateway (C172 recorded HTTP 400 timeout; retain both outcomes as separate attempts). No bytes/headers/length/sheets/series/observations/hash.
- DSBB URL https://dsbb.imf.org/egdds/dqaf-base/country/LAO/category/BOP00 resolves but extracted view is a generic dynamic shell with {{country.CountryName}} and no LAO-specific BOP periodicity/timeliness/methodology/revision fields. Only locator PASS.
- Public IMF SDMX Central registrations page https://sdmxcentral.imf.org/data/registrations.html inspected; find exact “LAO” returned no match. This is scoped absence in that registry page only, not proof no feed exists. No alternate registered mirror identified.
- Q2-2026 period, portfolio asset/liability legs, signs, units, BPM6 and vintage NOT_VERIFIED/NOT_ESTABLISHED; raw data/hash NOT_CAPTURED; LAO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_LAO_PDR_LAO_Q2_2026_BOL_SDMX_CENTRAL_REGISTRY_AND_DSBB_METADATA_CROSSCHECK_CONTINUATION173_20261121.md (commit 39fd1886b182f813a3101905a2bee93bd26f61b8).
- Next: only a distinct official BOL mirror/export, public NSDP data-service endpoint, or genuinely new supported byte-transfer capability; preserve bytes/hash and inspect two Q2 portfolio legs. If unavailable, keep PARTIAL and advance after full preflight. No historical/IMF-only substitutes, production changes; ₹0; UNKNOWN never PASS.


## Continuation 174 — Chapter 47 Part 22: Sri Lanka LKA Q2-2026 CBSL/Treasury portfolio dual-leg reconciliation (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Registry, LAO C173 and fixed 63-country cohort. LKA row: A_NFA_T_PRESENT and L_NIL_T_PRESENT; scoped repo search found no prior dedicated LKA national dual-leg reconciliation. No IMF re-query/cohort rebuild; LAO failed route not repeated.
- Official Ministry of Finance, Planning and Economic Development Sri Lanka, Budget Economic and Fiscal Position Report–2027, issued 12-Nov-2026, official PDF https://treasury.gov.lk/api/file/04b45c52-3ded-4621-86c7-b8c67455c9d8 , Table 7 page 102, BOP 2026, USD million, source explicitly CBSL. Separate provisional Q2-2026 Portfolio Investment Assets +26 and Liabilities -351.
- Reused archived IMF raw rows, asset file blob SHA 15449e87c9057291a1f52f2f8cd9805df55f9fb8 exact Q2 value USD +25,676,196.5415909; liability file blob SHA 15f379dc42e2760eb5f2384618e48f5ddc3177f1 exact Q2 value USD -350,932,889.850796. In USD mn: +25.6761965 rounds to +26; -350.9328899 rounds to -351. Both legs independently agree with national published rounded values. No net-to-leg back-solving.
- National values are provisional. CBSL primary statistical tables page direct access returned HTTP 403; no original CBSL workbook or Ministry PDF raw bytes/hash captured. IMF row's revision date unavailable, so exact same-vintage bridge NOT_ESTABLISHED. Classification: strong dual-leg reconciliation / provisional; final same-vintage pass pending. Aggregate remains NOT_AUTHORIZED.
- Detail report: docs/GCR_SRI_LANKA_LKA_Q2_2026_CBSL_TREASURY_BOP_PORTFOLIO_DUAL_LEG_RECONCILIATION_CONTINUATION174_20261121.md (commit 8b9f7f96657d6974a456672b65dfa2dc9180393b).
- Next: obtain underlying CBSL Table 2.10 BPM6 quarterly export + metadata and SHA-256; establish IMF observation revision date vs 12-Nov-2026 national vintage. Upgrade only if bridge is confirmed. No production changes, ₹0; UNKNOWN never PASS.


## Continuation 175 — Chapter 47 Part 23: LKA CBSL Table 2.10 release-vintage / raw-export access gate (2026-11-21)
- Preflight re-fetched Master Ledger, GCR Priority Queue, Historical Registry, C174 and fixed cohort. LKA remains in immutable 63-country Q2-2026 cohort; no IMF re-query/cohort rebuild; no repeat Treasury Table 7 extraction.
- Official CBSL External Sector landing page identifies “Balance of Payments (BPM6 Basis) - Quarterly (2012 1Q to Latest)”. Direct page open HTTP 403. Official source: https://www.cbsl.gov.lk/en/statistics/statistical-tables/external-sector.
- Distinct exact versioned CBSL Table 2.10 XLSX locator found via secondary source catalogue: https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/statistics/sheets/table2.10_20260930_e.xlsx ; filename date 2026-09-30; reported Last-Modified Wed, 30 Sep 2026 15:06:48 GMT; third-party-reported SHA-256 2d6e3ebd5c4305028a3693d9e1c25a0c64c606616f0b24cf334695e1ad3d62f6. Exact workbook sheet described as “BPM6-Financial AC - Quarterly”, through 2026Q2, with separate quarterly asset/liability column pairs. This SHA is NOT independently verified; no bytes or hash captured.
- Direct web open of exact XLSX HTTP 403; container download failed. No bytes, headers, length, sheet inspection or local SHA. Do not mark raw file PASS.
- CBSL-authored article states full BOP including financial account generally published quarterly with 3-month lag, compiled under BPM6, and monthly data revisions occur with regular quarterly BOP releases; full two-year revision with annual publication. Source article: https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/statistics/otherpub/information_series_note_20250310_a_key_milestone_in_external_sector_statistics_current_account_statistics_on_a_monthly_e.pdf . Exact Q2 observation revision vintage remains unavailable.
- The reported 30-Sep-2026 workbook marker and Treasury report issue date 12-Nov-2026 are different markers; no evidence yet that they are the same revision snapshot. LKA remains STRONG DUAL-LEG RECONCILIATION / PROVISIONAL, NOT FINAL SAME-VINTAGE PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_SRI_LANKA_LKA_Q2_2026_CBSL_TABLE210_RELEASE_VINTAGE_AND_RAW_EXPORT_ACCESS_CONTINUATION175_20261121.md (commit 47e35b88c497177e593a8b587ac2371debbd42a9).
- Next: obtain official XLSX via a genuinely distinct supported byte-transfer route; verify reported SHA-256 against bytes; inspect Q2 asset/liability cells; identify exact revision/vintage identifier. If no new route, close this route and advance after preflight. No production changes, ₹0; UNKNOWN never PASS.


## Continuation 176 — Chapter 47 Part 24: LKA Table 2.10 series cross-check and revision-risk gate (2026-11-21)
- Preflight re-fetched Master Ledger, Priority Queue, Historical Registry, C175, C174 and fixed cohort. No cohort rebuild/IMF re-query; no repeat of blocked direct CBSL XLSX route.
- Secondary Macro Lab pages explicitly identify CBSL as source, BPM6 quarterly Table 2.10, and 30-Sep-2026 release: Portfolio Investment Assets Q2 +25.68 USD mn; Liabilities Q2 -350.9 USD mn; liabilities equity/fund shares -38.90; liabilities debt securities -312.0; assets debt securities +25.68. Liabilities components sum to -350.90 at displayed precision. These are secondary corroboration only; Macro Lab states it is independent and not affiliated with CBSL/government.
- Pages expose CSV/JSON affordances; clicking JSON resolved back to HTML, so no raw machine-readable export bytes/hash. Secondary source also reports 2021 Table 2.10 vs older BOP mirror discrepancies: Q1 -742.213 vs -92.73 (diff -649.483); Q2 2.025 vs 3.24 (diff -1.215); Q3 -794.206 vs -1,156.54 (diff +362.334), attributed by catalogue to CBSL revision year. This is secondary QA evidence, not official revision log. Older mirror is rejected as substitute.
- C174 national Treasury values remain provisional +26/-351 USD mn; C175 same-vintage bridge still NOT_ESTABLISHED. Primary CBSL workbook bytes/hash NOT_CAPTURED; LKA remains strong dual-leg reconciliation / provisional, not final PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_SRI_LANKA_LKA_Q2_2026_TABLE210_SERIES_CROSSCHECK_AND_REVISION_RISK_CONTINUATION176_20261121.md (commit 1df18af6c399d01d92962180bf1502fc8fe4e24b).
- Next: seek genuinely different official CBSL/SDDS raw export and exact release-vintage metadata; if none, close LKA retrieval as PARTIAL and advance after preflight. No production changes, ₹0; UNKNOWN never PASS.


## Continuation 177 — Chapter 47 Part 25: LKA official SDDS alternate BOP workbook route (2026-11-21)
- Re-fetched Master Ledger, Priority Queue, Historical Registry, C174–C176 and fixed cohort before work. LKA remains cohort member; no IMF re-query/cohort rebuild. Prior Table 2.10 XLSX and Macro Lab HTML routes not repeated.
- CBSL official SDDS/NSDP page https://www.cbsl.gov.lk/en/node/1809 was reopened. It explicitly says “Last Updated On: 11th November 2017”; its BOP rows display Q2/17 observations. The BOP “More Data” link 191 resolves to distinct official file https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/statistics/sdds/BOP.xlsx.
- The click returned HTTP 400 unsupported content-type for XLSX; container download failed. No bytes, headers, workbook sheets, Q2-2026 rows or SHA-256. The separate erd.cbsl.gov.lk SDDS portal click timed out HTTP 400.
- Important: BOP.xlsx is a valid official alternate locator, but the linked NSDP page is stale 2017; no evidence the workbook contains Q2-2026. Route discovery PASS only; currentness/data NOT_VERIFIED. LKA remains strong provisional reconciliation, not final PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_SRI_LANKA_LKA_Q2_2026_SDDS_BOP_OFFICIAL_ALTERNATE_WORKBOOK_ROUTE_CONTINUATION177_20261121.md (commit 392722448bcea6ed8697efad140dc8b986508b9e).
- Next: inspect workbook only if a genuinely new supported byte-transfer route becomes available; otherwise close stale legacy route and advance to next fixed-cohort member after full preflight. No production changes, ₹0; UNKNOWN never PASS.


## Continuation 178 — Lesotho (LSO) CBL BPM6 portfolio source boundary (2026-11-21)
- LSO is in the immutable 63-country 2026-Q2 dual-leg cohort; no dedicated LSO national portfolio dual-leg report found in scoped repository search. No cohort rebuild/IMF re-query.
- Official CBL Statistical Research Portal BOP6 catalogue lists `BPI_BPM6_XDC` Portfolio investment in Million Maloti as a single aggregate series; no separate portfolio assets/liabilities series or equity/debt children are exposed in that category.
- CBL Quarterly Economic Review September-2025 Table 19 reports Portfolio Investments net only and ends Q3-2025. It is not Q2-2026 evidence.
- Net-only BPI and government-finance foreign asset/liability balance-sheet series rejected as dual-leg substitutes. No back-solving or unsupported conversion.
- LSO PARTIAL / NOT PASS; national Q2-2026 dual legs NOT_CAPTURED; aggregate NOT_AUTHORIZED.
- Detail report: `docs/GCR_LESOTHO_LSO_Q2_2026_CBL_BPM6_PORTAL_PORTFOLIO_DUAL_LEG_SOURCE_BOUNDARY_CONTINUATION178_20261121.md` (commit `683d34767c3a8ec8b75b470ca8c704469582d418`).
- Next: only reopen LSO on a genuinely new official detailed Q2 dual-leg route; otherwise select next cohort member after full duplicate-prevention preflight.


## Continuation 179 — Mongolia (MNG) NSO PxWeb quarterly BOP source/API gate (2026-11-21)
- MNG fixed-cohort membership PASS; no dedicated prior MNG Q2-2026 national dual-leg report found. No cohort rebuild or IMF re-query.
- Official NSO quarterly BOP PxWeb table `DT_NSO_0100_001V10_quarter` located; source metadata = Bank of Mongolia, unit million USD, frequency quarterly, period includes `2026-2`; 69 indicator values.
- The web-readable page did not expose indicator labels or observations. Documented PxWeb API base found in public client references, but actual API metadata retrieval was inaccessible (web layer) and DNS failed in container. No raw API response/hash, no separate portfolio legs.
- MNG PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Do not use net-only/annual/H1/IIP substitutes.
- Detail: `docs/GCR_MONGOLIA_MNG_Q2_2026_NSO_PXWEB_BOP_QUARTERLY_SOURCE_AND_API_GATE_CONTINUATION179_20261121.md` (commit `6b01b968365b9f2b8e636518f8458079e2ab090b`).
- Next: obtain official PxWeb codebook and exact JSON-stat2 data query through a supported API/export path; otherwise request official export attachment and move to next eligible cohort member.


## Continuation 180 — Montenegro (MNE) CBCG / NSDP SDMX source boundary (2026-11-21)
- MNE selected after current continuity preflight and no dedicated prior country dual-leg report in scoped repository search. MNG C179 inaccessible PxWeb API route not repeated.
- Official CBCG BOP page: BPM6 2010–2026, quarterly EUR, financial account displayed as net acquisition of assets / net incurrence of liabilities; page updated 19-Nov-2026.
- Official CBCG ZIP archive locator found but download blocked HTTP 400 application/zip; no bytes/hash.
- Official MONSTAT NSDP BOP Browse Data endpoint on legacy CBCG domain timed out; SDMX download resolves to official DSBB XML `https://dsbb.imf.org/xml/MNE/BOP6_Montenegro.xml`, but XML retrieval blocked HTTP 400 text/xml. These are locator-only, not content validation.
- Official Q2-2026 release date 19-Aug-2026. MONSTAT metadata confirms quarterly BPM6 BOP and portfolio investment coverage; metadata unit EUR thousands.
- No Q2-2026 separate portfolio legs captured; MNE PARTIAL / NOT PASS; exact cohort-row membership not re-extracted; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BOP6_NSDP_SDMX_SOURCE_BOUNDARY_CONTINUATION180_20261121.md` (commit `04fc8bbbf529eed183eaa9453496de2df12bc3f0`).
- Next: new supported transfer for ZIP/XML + exact MNE cohort-row check; no retry of same blocked routes.


## Continuation 181 — Poland (POL) NBP USD publication gate closure (2026-11-21)
- Current NBP public BOP PDF remains PLN-million; no current Q2-2026 official USD portfolio assets/liabilities table surfaced in the bounded public publication search. NBP Web API documentation concerns currency quotations and does not supply transaction-level weights.
- Prior national PLN legs and transaction-date FX principle are retained; no guessed conversion or quarter-end FX.
- POL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_POLAND_POL_Q2_2026_NBP_USD_DUAL_LEG_PUBLICATION_SEARCH_CLOSURE_CONTINUATION181_20261121.md (commit 5ab4cf466d2caab451674faa0d65666426ae5084).
- Next: next unexhausted fixed-cohort country after repository/registry duplicate-prevention preflight.


## Continuation 182 — MNE Montenegro CBCG Bulletin 9/2026 export locator (2026-11-21)
- Exact fixed-cohort row verified against immutable cohort SHA-256 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8: MNE has both IMF panel legs present, national validation pending, aggregate NOT_AUTHORIZED.
- Distinct official CBCG Bulletin 9/2026 PDF route identified; BOP section points to Tables 5.1–5.4 download tables. Quarterly EUR BPM6 methodology, FX treatment and preliminary/revision warning verified.
- The PDF contains no Q2-2026 portfolio asset/liability values; table export payload not retrieved. MNE PARTIAL / NOT PASS.
- Detail: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_9_2026_TABLE_EXPORT_LOCATOR_CONTINUATION182_20261121.md (commit 6ec0f976e2a5fdb26c704b0991b5cd0e5f3fa888).
- Next: resolve the linked official Tables 5.1–5.4 export, or move on without repeating blocked C180 transfer paths.


## Continuation 183 — MNE PDF table-export annotation access boundary (2026-11-21)
- Reopened official CBCG Bulletin 9/2026 PDF and confirmed the BOP Tables 5.1–5.4 download affordance, quarterly EUR/BPM6 methodology, FX methodology, and preliminary/revision caveat.
- Available PDF extraction exposed the affordance text but not the annotation target URL; direct PDF byte download failed. No table bytes, MIME, timestamp, hash, or Q2 portfolio legs were captured. This is an access boundary, not evidence of data absence.
- MNE remains PARTIAL / NOT PASS; fixed cohort and IMF archive unchanged; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_PDF_ANNOTATION_ACCESS_AUDIT_CONTINUATION183_20261121.md` (commit 54e8d2efe633049b7aef672ff84339d8ee18a741).
- Next: do not repeat the same PDF extraction/download route. Select the next eligible fixed-cohort country only after complete historical/queue preflight; reopen MNE only on a genuinely new official export locator or supported annotation-download capability.


## Continuation 184 — North Macedonia (MKD) Q2-2026 official source-boundary audit (2026-11-21)
- Fresh continuity preflight and duplicate check completed; MKD had no prior dedicated national-validation report in the repository inventory. Exact MKD row confirmed in the immutable 63-country cohort; both IMF Q2 legs present; no cohort rebuild or IMF re-query.
- Official NBRNM PxWeb quarterly financial-account table located (matrix ES-001; source NBRNM; created 23-Sep-2026; units million EUR/USD; 210 item values; 114 quarters). Full codebook and selected observation payload were not exposed by the available page rendering; raw API/export bytes/hash not captured.
- Official SSO Bulletin 10/2026 reports Q2-2026 portfolio investment net +USD227.7m only. Its +USD144.9m net acquisition of financial assets and +USD431.0m net incurrence of liabilities are financial-account-wide totals, not portfolio-specific legs. 2025/2026 data are marked provisional.
- NBRNM methodology and revision PDFs linked from PxWeb returned 403 via the available retrieval path. MKD remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_NORTH_MACEDONIA_MKD_Q2_2026_NBRNM_PXWEB_AND_SSO_PORTFOLIO_SOURCE_BOUNDARY_CONTINUATION184_20261121.md` (commit 049aa09b4dd0df397364cd16fc76f5160eefd00c).
- Next: retrieve NBRNM full table metadata/codebook and Q2-2026 portfolio asset/liability observations through a supported official export/API path; preserve bytes, MIME, UTC timestamp, hash and vintage. If unavailable, retain PARTIAL and move to next eligible cohort member after full preflight.


## Continuation 185 — Indonesia (IDN) BI BPM5-to-IMF BPM6 sign crosswalk (2026-11-21)
- Selected the open actionable dependency in the existing IDN report after fresh Master Ledger / Priority Queue / Historical Registry / cohort / exact-key receipt preflight. No later IDN follow-up report was found. Reused archived IMF exact-key rows; no IMF re-query or cohort rebuild.
- Bank Indonesia's official BOP metadata explicitly says data are compiled using BPM6 concepts but published financial-account asset/liability sides remain presented under BPM5 as net inflow/outflow (positive inflow/credit, negative outflow/debit). IMF BPM6 Compilation Guide Table 8.10 supplies the exact sign conversion: BPM5 asset increases negative vs BPM6 asset increases positive; liability increases positive in both.
- Therefore reverse BI's asset sign only and retain BI's liability sign. Mapped BI assets +1,488 USDm vs IMF +1,487.605237 (absolute residual 0.394763); liabilities +11,440 vs IMF +11,440.221642 (residual 0.221642). Both within ±0.5 USDm BI whole-million rounding. No net-to-leg back-solving.
- Sign bridge and both numeric checks PASS. BI Q2 2026 is explicitly **Very Temporary**; same-vintage/revision identity remains NOT_ESTABLISHED. IDN overall PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_INDONESIA_IDN_Q2_2026_BI_BPM5_TO_IMF_BPM6_SIGN_CROSSWALK_CONTINUATION185_20261121.md` (commit d7c62b821f7b7cb439c46cbc691eb674924b7099).
- Next: inspect subsequent official BI SEKI V.7 Q2-2026 vintages/revision markers and establish same-vintage match; retain overall PARTIAL until evidenced.


## Continuation 186 — Indonesia (IDN) latest BI Q2 revision vs archived IMF vintage (2026-11-21)
- Selected the exact open C185 next action after fresh Ledger/Priority Queue/Registry/C185/IDN prior-report/IMF receipt preflight. No duplicate BI Table V.7 extraction, IMF re-query or cohort rebuild.
- New official BI Q3-2026 BOP report, published 20-Nov-2026, provides Table 7 (PDF p.37): Q2-2026 provisional portfolio assets -1,466 USDm, liabilities +11,399 USDm, total +9,934. Box 1 (PDF p.28) explicitly states Q1–Q2 2026 portfolio-investment data were updated due to updated LLD and ULN data. This supersedes the older 21-Aug Q2** values -1,488 / +11,440 / +9,953.
- Retained official BI BPM5→IMF BPM6 sign mapping: reverse asset sign only; retain liability sign. Reused archived IMF snapshot retrieved 19-Nov: A_NFA_T +1,487.605237 USDm; L_NIL_T +11,440.221642 USDm. Residuals against latest BI mapped values: asset +21.605237; liability +41.221642 USDm, both > ±0.5 rounding.
- Current sign mapping PASS; latest national revision evidence PASS; numeric match to archived IMF snapshot FAIL/REVIEW; exact same-vintage bridge NOT_ESTABLISHED; IDN PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_INDONESIA_IDN_Q2_2026_BI_NOV2026_REVISION_VINTAGE_RECHECK_CONTINUATION186_20261121.md` (commit 51ba355709893c89a718d0eb94d87c98ad22e277).
- Next: inspect only a later IMF snapshot already in the archive with explicit retrieval/revision metadata. If none exists, do not re-query IMF; retain mismatch and advance to next eligible cohort country after preflight.


## Continuation 187 — India (IND) Q1-2026 RBI published-value persistence (2026-11-21)
- Selected exact open Continuation 41 item after fresh preflight of Ledger, Queue, Registry, India prior reports and existing IMF exact rows. No new IMF request/cohort rebuild.
- Official RBI Table 43/42 pages dated 22-Jun, 22-Jul and 25-Aug 2026 show Q1-2026 portfolio investment in India net -12,121 USDm (July/August), portfolio investment by India net +74 USDm, total net -12,047 USDm; same Q1 values persisted across the inspected releases. October Table42 captured in prior work is Q2-only, not a newer Q1 release.
- Existing IMF Q1 values: A_NFA_T -74.050352868 USDm; L_NIL_T -13,633.508347332 USDm. Asset comparison remains PASS (+0.050353 residual); liability remains REVIEW (-1,512.508347 residual); combined net REVIEW (-1,512.457994). RBI published-value revision does not explain discrepancy on evidence inspected; underlying cause/vintage NOT_ESTABLISHED.
- India remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: `docs/GCR_INDIA_IND_Q1_2026_RBI_TABLE42_RELEASE_PERSISTENCE_AUDIT_CONTINUATION187_20261121.md` (commit c4f73d755090a71c0312f9f82ac7afecd7b226ab).
- Next: genuinely distinct official RBI Q1 revision-history/transaction-level data or already archived IMF vintage metadata; otherwise retain REVIEW and advance. Do not repeat known releases or issue new IMF GET.


## Continuation 188 — LKA CBSL official page freshness gate (2026-11-21)
- Reused LKA C174–C177 and fixed cohort; no IMF re-query/cohort rebuild. Treasury Table 7 Q2 assets +26 and liabilities -351 USDm remain provisional and numerically corroborated at published rounding.
- New CBSL official search-indexed External Sector page metadata: page content updated 01-Oct-2026 11:30; describes BPM6 quarterly BOP 2012Q1–Latest. Direct page open 403; no current workbook/export URL, raw bytes/hash, or statistical revision identifier exposed.
- This is page freshness only, not data vintage. It does not bridge C175's 30-Sep-2026 workbook filename marker to the 12-Nov-2026 Treasury report. LKA remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- C188 detail: `docs/GCR_SRI_LANKA_LKA_Q2_2026_CBSL_EXTERNAL_SECTOR_PAGE_FRESHNESS_AND_EXPORT_GATE_CONTINUATION188_20261121.md` (commit 2971a494803edc77b51290e607c8aa2af763a44b).
- Close repeat C175–C177 route attempts. Reopen only on distinct official export/API locator or actual current Table 2.10 revision identifier.


## Continuation 189 — GIN BCRG official MPC download-affordance boundary (2026-11-21)
- Selected GIN after C188 and fresh preflight of Ledger/Queue/Registry/C170/C188/fixed cohort. No IMF re-query or cohort rebuild.
- Official 22nd MPC page directly opens and shows “Télécharger”, but the extracted page link inventory exposes no attachment href/document URL. No URL guessed; no bytes/hash or Q2 portfolio observations captured.
- GIN remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: `docs/GCR_GUINEA_GIN_Q2_2026_BCRG_MPC_DOWNLOAD_AFFORDANCE_AND_LINK_TARGET_ACCESS_GATE_CONTINUATION189_20261121.md` (commit 9bebc3da4f89d745c4599d0d0e4da39339c0f7ab).
- Reopen only on a distinct official BCRG attachment/API export target; do not repeat static page inspection.


## Continuation 190 — MNG NSO PxWeb API metadata-route recheck (2026-11-21)
- Selected MNG's open C179 dependency after fresh preflight of Ledger/Queue/Registry/C189/MNG report/fixed cohort.
- Official table metadata confirms quarterly BOP flow scope, Bank of Mongolia source, million USD, and Q2-2026 period example. Direct PxWeb v1 metadata URL tested but retrieval surface returned “URL not accessible”; no HTTP response/body/bytes/hash or indicator labels captured.
- MNG remains PARTIAL / NOT PASS; national portfolio A/L NOT_CAPTURED; aggregate NOT_AUTHORIZED. Detail: `docs/GCR_MONGOLIA_MNG_Q2_2026_NSO_PXWEB_API_METADATA_ROUTE_RECHECK_CONTINUATION190_20261121.md` (commit b34c392e7cac13b24e260ee2bd5e3011004a5e13).
- Do not repeat the same API URL through the same retrieval surface. Reopen only on a genuinely different official export/attachment capability.


## Continuation 191 — MNG corrected PxWeb metadata endpoint and page update check (2026-11-21)
- C190 endpoint audit found its metadata URL omitted the table filename suffix `.px`; corrected the endpoint using the public PxWeb client construction. The corrected URL was tested but remains inaccessible through the current retrieval bridge; no raw JSON/HTTP response captured.
- Official NSO table now displays update marker 09-Nov-2026 and Q2-2026 among periods; quarterly, million USD, Bank of Mongolia source. Page metadata only; not observation vintage. Indicator codebook and separate portfolio legs still NOT_CAPTURED.
- MNG PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: `docs/GCR_MONGOLIA_MNG_Q2_2026_NSO_PXWEB_CORRECTED_METADATA_ENDPOINT_AND_ACCESS_GATE_CONTINUATION191_20261121.md` (commit 3dddaefe0093bd366a7c755e5407a088f498517e).
- Do not retry same blocked API surface; reopen only with a distinct supported official export/attachment capability.


## Continuation 192 — ALB Q2 release calendar vs legacy Main-data ceiling (2026-11-21)
- Official Bank of Albania calendar confirms Q2-2026 BOP release date 10-Sep-2026; official time-series landing page shows the same page update marker.
- Click-through legacy quarterly table has EURm and C.2.A/C.2.L taxonomy but its displayed methodology cites the 11-Sep-2017 publication/revision and exposes no Q2-2026 observation cells or export bytes. Same route family as C140/C141; closed for repeat.
- ALB remains PARTIAL / NOT PASS; Q2-specific export and values NOT_CAPTURED; aggregate NOT_AUTHORIZED. Detail: `docs/GCR_ALBANIA_ALB_Q2_2026_BOA_Q2_RELEASE_CALENDAR_VS_LEGACY_TABLE_CEILING_CONTINUATION192_20261121.md` (commit 46725db533106245fa306ad2387720b59a9392f9).
- Reopen only on distinct Q2-specific official export/API/workbook locator; otherwise advance to next eligible fixed-cohort member.


## Continuation 193 — IDN archived IMF vintage inventory closure (2026-11-21)
- Current repository tree and IMF exact-sample/coverage manifests were inspected after re-fetching Ledger, Queue, Registry and IDN C185/C186 reports. Only the 19-Nov-2026 exact-key IMF transport snapshot is archived for IDN; no later snapshot or observation-level revision metadata found.
- The coverage QA manifest explicitly describes a current retrieval snapshot with no point-in-time historical vintages. BI's 20-Nov revised Q2 legs remain discrepant against the 19-Nov IMF snapshot by +21.605237 USDm assets and +41.221642 USDm liabilities; same-vintage NOT_ESTABLISHED.
- C186 archive-follow-up branch closed NOT_AVAILABLE. IDN remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. No new IMF GET, BI extraction or cohort rebuild.
- Detail: docs/GCR_INDONESIA_IDN_Q2_2026_IMF_ARCHIVED_VINTAGE_INVENTORY_AND_MATCH_GATE_CONTINUATION193_20261121.md (commit d1319128935b78064c01edc66e0458759de19ca7).
- Next: choose the next eligible fixed-cohort country only after full history and route-fingerprint preflight.


## Continuation 194 — CHN SAFE detailed time-series workbook locator (2026-11-21)
- After C193, CHN's open prior-report next action was selected: inspect the official SAFE detailed BOP time-series attachment, not IIP stocks. Ledger/Queue/Registry and CHN report were re-fetched; cohort and IMF receipt reused.
- SAFE time-series page exposes exact linked XLSX target `https://www.safe.gov.cn/en/file/file/20260929/20c1e5e45d704a77b302ba234211a75b.xlsx`. Official locator recovered; web surface rejected XLSX MIME and direct container download failed. No raw bytes/hash/workbook cells.
- CHN remains PARTIAL / NOT PASS; asset sign unresolved; aggregate NOT_AUTHORIZED. No IMF GET/cohort rebuild.
- Detail: `docs/GCR_CHINA_CHN_Q2_2026_SAFE_OFFICIAL_TIMESERIES_WORKBOOK_LOCATOR_AND_RAW_ACCESS_GATE_CONTINUATION194_20261121.md` (commit 265712fed07a20bed233e29c9ab77cdd7ea742ea).
- Next: retrieve this exact official workbook via supported browser/file workflow; otherwise wait for a distinct official machine-readable export. Do not repeat identical unsupported fetch.


## C194 correction — CHN duplicate route; restore COL next action (2026-11-21)
- C194's SAFE English XLSX URL was not a new route. C135 already established English and Chinese links resolve to the same XLSX and ordered no same-endpoint retries; C136 explicitly prohibited retrying either known XLSX URL through the same unsupported retrieval paths.
- Retract C194's “newly recovered locator” characterization. Mark C194 DUPLICATE / NO PROGRESS. CHN remains PARTIAL / NOT PASS; do not repeat either known XLSX route on the same access surfaces.
- Restore C136's next actionable item: COL — retrieve the already identified separate BanRep/SUAMECA quarterly portfolio asset and liability transaction series through a genuinely different supported route. Recheck current COL reports and route fingerprints first; do not repeat same 502/timeout catalogue route. No IMF GET/cohort rebuild.
- All future selections must pass full Ledger/Queue/Registry + prior report + URL/API/file fingerprint preflight; skip PASS and exhausted routes before selecting the highest-value unfinished task.


## Continuation 195 — MKD NBRNM PxWeb API metadata route boundary (2026-11-21)
- Re-fetched Ledger/Queue/Registry and full MKD history; C184 was the only dedicated MKD report. Selected its open official ES-001 codebook/dual-leg extraction dependency; reused fixed cohort and archived IMF panel.
- Tested a distinct PxWeb v1 metadata API path constructed from the exact official `.px` table URL. Retrieval surface returned inaccessible; no JSON/body/headers/bytes/hash. Do not repeat same route/surface.
- MKD remains PARTIAL / NOT PASS; separate portfolio A/L cells and vintage bridge NOT_CAPTURED; aggregate NOT_AUTHORIZED. No IMF GET/cohort rebuild.
- Detail: `docs/GCR_NORTH_MACEDONIA_MKD_Q2_2026_NBRNM_PXWEB_API_METADATA_ROUTE_ACCESS_GATE_CONTINUATION195_20261121.md` (commit c85f91b43b4fae8941613b1f29b42e7ac20b7b5d).
- Next: select next eligible fixed-cohort member after full prior-report and route-fingerprint preflight.


## Continuation 196 — Peru PER BCRP current-catalogue scope refresh (2026-11-21)
- Fresh official BCRP quarterly catalogue (inspected 21-Nov; rows last updated 20-Nov) reconfirms PN39278BQ private-sector portfolio assets and PN39285BQ private-sector portfolio liabilities through T3-2026. Public-sector list includes PN39402FQ aggregate assets, PN39403FQ aggregate liabilities and PN39404FQ portfolio liabilities, but no public-sector portfolio-specific asset series in the displayed 25-series group.
- No API retry: prior exact route is inaccessible through current retrieval bridge. No Q2 observations/raw bytes/hash captured. Do not add aggregate public assets to private portfolio assets or treat IIP stocks/net totals as substitutes.
- PER remains PARTIAL / NOT PASS; full national asset scope NOT_ESTABLISHED; aggregate NOT_AUTHORIZED. Detail: docs/GCR_PERU_PER_Q2_2026_BCRP_CATALOGUE_REFRESH_AND_PUBLIC_ASSET_SCOPE_GATE_CONTINUATION196_20261121.md.
- Reopen only on a distinct official public-sector portfolio-asset transaction series or explicit full-economy scope statement; otherwise advance after full history/route preflight.


## Continuation 197 — ROU BNR Interactive Database route discovery (2026-11-21)
- C95/C96 and full route history rechecked; same ECB SDW API endpoints remain closed and were not retried. New distinct official route: BNR Interactive Database https://www.bnr.ro/en/2550-interactive-database. IMF DSBB metadata confirms detailed BOP data are disseminated through Statistics → Interactive Database and Statistics → Data Sets.
- The BNR landing page is a JS shell in this text retrieval; no table locator, Q2 portfolio A/L observations, export bytes, receipt or SHA-256 captured. Route-discovery PASS only; ROU remains PARTIAL / NOT PASS; external-custodian portfolio coverage caveat remains.
- Detail: docs/GCR_ROMANIA_ROU_Q2_2026_BNR_INTERACTIVE_DATABASE_OFFICIAL_ROUTE_DISCOVERY_CONTINUATION197_20261121.md. Next: use JS-capable interactive browser to export exact Q2 separate portfolio A/L rows and preserve native bytes/metadata/hash; if unavailable, advance without retrying ECB endpoints.


## Continuation 198 — Interactive portal execution-mode gate (2026-11-21)
- C197 ROU BNR Interactive Database remains a valid official locator but is not executable in the current session: BNR page is a JS shell and no JS-capable browser / Computer Use action is exposed. No query/export/bytes; ROU PARTIAL / NOT PASS.
- Cross-check: NBG NSDP shows BOP “Download in SDMX” label without an exposed BOP href/target; Statistics Data page is a JS search shell. CBBH C156 and BNM C86 also have documented UI export controls but no executed workboards.
- Process improvement PASS: new Execution-Mode Gate requires route classification (static/API/UI) before selection. Select UI routes only when a JS-capable browser is actually available; otherwise mark NOT_EXECUTED — UI CAPABILITY UNAVAILABLE and advance to a retrievable static official route. Never count page-shell inspection as export/data PASS.
- Detail: `docs/GCR_INTERACTIVE_OFFICIAL_PORTAL_EXECUTION_CAPABILITY_GATE_CONTINUATION198_20261121.md`. No country validation progress; ROU/GEO/BIH/MDA remain PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. No IMF re-query/cohort rebuild; all protected invariants unchanged.


## Continuation 199 — Armenia ARM current CBA Financial Account export route (2026-11-21)
- Reused fixed 63-country cohort and archived ARM IMF rows; no IMF request/cohort rebuild. Full C143 reviewed; its legacy XLS URL remains closed and was not retried.
- Distinct current official route: CBA Financial Account page https://www.cba.am/en/statistics/financial-account/275 exposes XLSX/XML/JSON export controls. Exact export-all target https://www.cba.am/en/statistics/financial-account/275/export-all/ timed out once; no body/bytes/hash or Q2 portfolio series captured.
- CBA metadata: BPM6, USD millions, quarterly/annual BOP, annual revision practice. Armstat NSDP's Q2 financial-account aggregate omits portfolio flow line; not zero. IIP portfolio positions excluded as stocks.
- ARM remains PARTIAL / NOT PASS; no numeric validation or aggregate admission. Detail: docs/GCR_ARMENIA_ARM_Q2_2026_CBA_CURRENT_FINANCIAL_ACCOUNT_EXPORT_ROUTE_GATE_CONTINUATION199_20261121.md. No repeat of either C143 legacy XLS or C199 same-surface export timeout. Next: move to another eligible fixed-cohort member with a retrievable static official source under C198 Execution-Mode Gate.


## Continuation 200 — 63-country national validation master matrix
- Matrix report: `docs/GCR_63_COUNTRY_Q2_2026_NATIONAL_VALIDATION_MASTER_MATRIX_CONTINUATION200_20261121.md`.
- CSV: `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`.
- Fixed cohort SHA-1 `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`; exactly 63 rows. All 63 have IMF A_NFA_T and L_NIL_T entries present; national validation is a separate gate.
- Snapshot stage counts: SOURCE_FOUND 20; DATA_CAPTURED 23; BLOCKED 19; NOT_STARTED 1; FULL_PASS 0. Therefore 63/63 remain outside full national validation; aggregate NOT_AUTHORIZED.
- Asset gate: PASS 15 / REVIEW 7 / NOT_CAPTURED 41. Liability gate: PASS 15 / REVIEW 8 / NOT_CAPTURED 40. Vintage: PENDING 23 / UNKNOWN 40.
- This is a first consolidated inventory, not a complete re-audit of every historical report. Continue from latest country-specific report; do not repeat PASS work or closed routes. Update a country only with new primary evidence and read-back verification.


## Continuation 200 — 63-country Q2-2026 master status matrix (2026-11-21)
- Added `docs/GCR_2026Q2_63_COUNTRY_MASTER_STATUS_MATRIX_CONTINUATION200_20261121.md` and machine-readable companion `docs/evidence/gcr_2026q2_country_master_status_matrix.csv`.
- Immutable cohort input reused unchanged: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`; 63 rows, both IMF Q2 legs present for each. No cohort rebuild or IMF re-query.
- Bounded inventory snapshot: SOURCE_FOUND or later 58/63; DATA_CAPTURED 12; ASSET_PASS 6; LIABILITY_PASS 6; VINTAGE_PASS 0; FULL_PASS 0; BLOCKED 24; NOT_STARTED 4. All aggregate_admission remain NOT_AUTHORIZED.
- Important limitation: matrix is a first conservative inventory, not exhaustive 63-country report-history re-audit. NOT_STARTED means no evidence surfaced in bounded inventory, not proof of no prior work. The per-country notes and gates are explicit in the matrix; statuses must be refined only after exact report inspection.
- Next: complete exhaustive 63-country report-history audit, then reconcile leg-specific and vintage statuses. Never promote a country to FULL_PASS without both separate national legs, scope/sign/scale, same-vintage and provenance gates.


## Continuation 201 — 63-country Q2-2026 national validation matrix reconciled (2026-11-21)
- Immutable cohort CSV SHA-1: `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`; exactly 63 unique members.
- Matrix CSV: `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`; explicit YES/NO flags added for NOT_STARTED, SOURCE_FOUND, DATA_CAPTURED, ASSET_PASS, LIABILITY_PASS, VINTAGE_PASS, FULL_PASS and BLOCKED.
- Exact cohort-to-matrix reconciliation: 63/63; missing 0; extra 0; duplicate 0.
- Current stages: NOT_STARTED 1; SOURCE_FOUND 20; DATA_CAPTURED 23; BLOCKED 19. Therefore 40 countries remain below DATA_CAPTURED (20+19+1); 23 have captured national values, not necessarily accepted.
- Independent gates: ASSET_PASS 15; LIABILITY_PASS 15; VINTAGE_PASS 0; FULL_PASS 0. These gate counts overlap; do not sum them.
- No country has FULL_PASS; aggregate remains NOT_AUTHORIZED. Matrix is a status inventory, not a complete line-by-line re-audit of every historical report; latest country continuations control promotions.
- Detail: `docs/GCR_63_COUNTRY_Q2_2026_NATIONAL_VALIDATION_MASTER_MATRIX_RECONCILIATION_CONTINUATION201_20261121.md`.
- CSV update commit: `f596dc889642e3a9262f2fd7b7dc9b02a6a57a0a`; CSV blob SHA-1: `45e466c72c034d460dfccf57474b07bfb6d12ea9`.
- Preserve immutable cohort, no IMF re-query/rebuild, no unsupported inference, ₹0, and all V11.3 production invariants.


## GCR Continuation 200 — country master matrix baseline (2026-11-21)
- Matrix `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`: 63/63 fixed cohort rows matched; 0 key/period/leg mismatches.
- Overall stages: SOURCE_FOUND 20; DATA_CAPTURED 23; BLOCKED 19; NOT_STARTED 1; FULL_PASS 0.
- Continue one country at a time. Resolve captured-but-REVIEW/PENDING gates and prioritize executable official sources among SOURCE_FOUND. Do not retry BLOCKED routes without genuinely new official route or supported retrieval capability.
- Check underlying country reports and raw evidence before status promotion. Matrix is a baseline, not a substitute for source reports. Aggregate NOT_AUTHORIZED; no cohort rebuild, IMF re-query, production changes or paid data.


### C201 read-back correction — final matrix snapshot
- Final read-back matrix CSV blob SHA-1: `64bb4a85cb2f004b5faa906b6353a6f71ecb9ad2`. The CSV currently has 63 data rows and 30 columns, including the eight requested YES/NO status flags plus detailed source/data/asset/liability/vintage/overall status and evidence_ref fields.
- The earlier C201 CSV commit blob SHA `45e466c72c034d460dfccf57474b07bfb6d12ea9` is a prior intermediate snapshot; use the final read-back blob SHA above.
- Recomputed from the final CSV: NOT_STARTED 1; SOURCE_FOUND 20; DATA_CAPTURED 23; BLOCKED 19; ASSET_PASS 15; LIABILITY_PASS 15; VINTAGE_PASS 0; FULL_PASS 0. Cohort membership remains exact 63/63.
- Interpretation unchanged: 40 are below DATA_CAPTURED; 23 have national data recorded but remain short of FULL_PASS; all 63 remain not fully accepted; aggregate NOT_AUTHORIZED.


## Continuation 202 — Nigeria NGA historical evidence reconciliation (2026-11-21)
- Existing report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_NIGERIA_20261119.md` was inspected; CBN Q2-2026 BOP Highlights national source and both portfolio legs are already captured. Six comparisons (assets/liabilities across Q2-2025, Q1-2026, Q2-2026) PASS within the report's ±USD 5m rounding tolerance. Q2-2026 is provisional; same-vintage bridge remains pending.
- Corrected stale NGA row in `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`: DATA_CAPTURED; ASSET_PASS; LIABILITY_PASS; VINTAGE_PENDING; FULL_PASS=NO; aggregate NOT_AUTHORIZED. evidence_ref now points to the Nigeria report.
- Final matrix blob SHA-1 read-back verified: `f9d68b4a24d92c41e6c72db776d89254a8f6d7de` (63 rows, 30 columns; NGA row verified).
- Detail: `docs/GCR_NIGERIA_NGA_Q2_2026_HISTORICAL_EVIDENCE_MATRIX_RECONCILIATION_CONTINUATION202_20261121.md`.
- Recomputed stages after this single-country correction: SOURCE_FOUND 19; DATA_CAPTURED 24; BLOCKED 19; NOT_STARTED 1; ASSET_PASS 16; LIABILITY_PASS 16; VINTAGE_PASS 0; FULL_PASS 0. Below DATA_CAPTURED: 39. Counts are not additive across independent gates.
- No IMF re-query/cohort rebuild; aggregate remains NOT_AUTHORIZED; ₹0; all production invariants unchanged; UNKNOWN never PASS.


## Continuation 203 — Pakistan PAK matrix evidence reconciliation (2026-11-21)
- PAK C51–C52 already captured official SBP CY26 Q2(R) portfolio asset/liability values (-2 / -243 USDm), reused exact archived IMF rows, documented SBP BPM6 sign framework, and passed separate numeric comparisons 2/2 at published USDm precision.
- Rejected repeat source fetch, IMF extraction, sign crosswalk and numeric comparison. Selected the actionable stale-matrix correction only: PAK was still SOURCE_FOUND despite the accepted C51–C52 evidence.
- Matrix row corrected to DATA_CAPTURED; ASSET_PASS; LIABILITY_PASS; VINTAGE_PENDING; FULL_PASS=NO; aggregate NOT_AUTHORIZED. Read-back: 63 rows / 30 columns; CSV blob SHA-1 `2e9b5a9246cebc249acc2e615cae5e43d4d8f4ac`.
- Counts after PAK correction: SOURCE_FOUND 18; DATA_CAPTURED 25; BLOCKED 19; NOT_STARTED 1; ASSET_PASS 17; LIABILITY_PASS 17; VINTAGE_PASS 0; FULL_PASS 0. Independent gate counts overlap.
- PAK exact SBP revision timestamp / IMF same-vintage bridge remains NOT_ESTABLISHED; do not promote to FULL_PASS. Detail: `docs/GCR_PAKISTAN_PAK_Q2_2026_HISTORICAL_EVIDENCE_MATRIX_RECONCILIATION_CONTINUATION203_20261121.md`. Next: continue the same fixed-cohort historical evidence reconciliation with another demonstrably stale matrix row; inspect its latest country report first and do not re-run completed PASS work or closed routes. No IMF re-query/cohort rebuild; aggregate NOT_AUTHORIZED; production invariants unchanged.


## Continuation 204 — BOL Bolivia matrix status reconciliation (2026-11-21)
- Reused C158 official BCB Q2 locator report; no repeated XLSX route, no IMF request, no cohort rebuild.
- Corrected the stale 63-country matrix row from NOT_STARTED/NOT_FOUND to BLOCKED / SOURCE_FOUND, because official Q2 locators exist but both XLSX retrievals returned HTTP 400 and no national bytes/legs were captured.
- Read-back matrix: 63 rows; NOT_STARTED 0; SOURCE_FOUND 18; DATA_CAPTURED 25; BLOCKED 20; ASSET_PASS 17; LIABILITY_PASS 17; VINTAGE_PASS 0; FULL_PASS 0. Aggregate remains NOT_AUTHORIZED.
- Detail: `docs/GCR_BOLIVIA_BOL_Q2_2026_HISTORICAL_EVIDENCE_MATRIX_RECONCILIATION_CONTINUATION204_20261121.md`.
- Next: select the next demonstrably stale matrix row only after checking current Ledger, Registry, full country report history and route fingerprint. Prefer an executable new official static/API route; do not retry closed routes or treat a status correction as country validation. ₹0; protected production invariants unchanged.


## Continuation 205 — India IND Q2-2026 matrix evidence correction (2026-11-21)
- Reused existing RBI Table 42 Apr-Jun 2026 release (23-Oct-2026), current-vintage supplement, archived exact IMF observations and comparison CSV; no re-fetch/re-query.
- The prior IND matrix row was stale at SOURCE_FOUND despite 3/3 Q2 asset/liability/combined-net comparisons PASS within ±USD0.5m. Corrected IND to DATA_CAPTURED, asset PASS, liability PASS, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED.
- Q2 residuals: assets -0.489413221 USDm; liabilities +0.240053743 USDm; combined net -0.270533037 USDm. RBI source raw HTML SHA-256 075c28122d588e5bce0ff45c8c8d5d8b453c53dc5b9a20f79d5cd3a6e54f5396; comparison CSV SHA 8ff2534dc730c822b20351530b9379fb86369cb2.
- C187 India Q1 liability REVIEW (-1,512.508347 USDm residual) remains open; no all-period FULL_PASS. BOJ API C84-C85 is closed for repeated same-route probes.
- Detail: docs/GCR_INDIA_IND_Q2_2026_HISTORICAL_EVIDENCE_MATRIX_RECONCILIATION_CONTINUATION205_20261121.md.
- Next: only seek new primary same-vintage/revision evidence for the open Q1 liability or vintage bridge; do not repeat completed Q2 comparison or BOJ inaccessible API route. ₹0; protected production invariants unchanged; UNKNOWN never PASS.


## Continuation 206 — Argentina ARG matrix evidence-link reconciliation (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Task Registry, 63-country matrix and ARG INDEC–IMF report before selection. Completed PASS work and closed INDEC vintage routes were not repeated.
- Existing report `docs/GCR_ARGENTINA_ARG_Q2_2026_INDEC_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md` already records Q2-2026 assets/liabilities numeric PASS at ±USD0.5m; residuals +0.206322m / +0.052824m. Same-vintage remains NOT_ESTABLISHED.
- Defect: ARG matrix row had evidence_ref=NO_DEDICATED_REPORT_REF_IN_BASELINE despite the dedicated report. Corrected only evidence_ref to `GCR_ARGENTINA_ARG_Q2_2026_INDEC_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120`; no stage or gate promotion.
- Matrix commit `c8b346302cea6197b0de577ef26045fd7dc0eb70`; blob SHA-1 `1fa8a1e7c57b064ad58f51e6ae18ebe8c3336daf`. Detail: `docs/GCR_ARGENTINA_ARG_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION206_20261121.md`.
- ARG remains DATA_CAPTURED; asset/liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED. No IMF re-query/cohort rebuild, no new national data, no production change; ₹0; UNKNOWN never PASS.
 

## Continuation 207 — Burundi BDI matrix evidence-link reconciliation (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Registry, 63-country matrix and BDI C155 report before selection.
- Existing C155 report `docs/GCR_BURUNDI_BDI_Q2_2026_BRB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION155_20261121.md` documents BRB Q4/Q3-2025 historical dual-leg table only; Q2-2026 national legs remain NOT_CAPTURED. No BRB or IMF retrieval repeated.
- Corrected only BDI matrix evidence_ref from `NO_DEDICATED_REPORT_REF_IN_BASELINE` to the C155 report basename. No stage/gate promotion; BDI remains SOURCE_FOUND, Q2 national legs NOT_CAPTURED, vintage UNKNOWN, aggregate NOT_AUTHORIZED.
- Matrix commit `641e119f6a7dd13a2fd4893bf3549592152acb62`; blob SHA-1 `7a27ec249675fb40721340f3ed065ca9a2c5bb5c`. Detail: `docs/GCR_BURUNDI_BDI_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION207_20261121.md`.
- Do not substitute historical quarters or annual estimates; reopen only on new official Q2-2026 dual-leg evidence. No IMF re-query/cohort rebuild; ₹0; protected invariants unchanged; UNKNOWN never PASS.


## Continuation 208 — Mexico MEX matrix evidence-link reconciliation (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Registry, 63-country matrix and MEX Banxico reconciliation before selection.
- Existing MEX report records Q2-2026 Banxico–IMF asset residual +0.255098 USDm and liability residual +0.285114 USDm; both PASS within ±0.5 USDm. Exact same-vintage identity remains NOT_ESTABLISHED because Banxico values are revisable and no dated bridge is preserved.
- Corrected only MEX matrix evidence_ref from `NO_DEDICATED_REPORT_REF_IN_BASELINE` to `GCR_MEXICO_MEX_Q2_2026_BANXICO_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120`. No stage/gate promotion; MEX remains DATA_CAPTURED, asset/liability PASS, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED.
- Matrix commit `f9094b380ff959e13d59a9d68713cb35fe82e42c`; blob SHA-1 `efcc44b085abd2ff250a82c988b9a4fa2dc69c23`. Detail: `docs/GCR_MEXICO_MEX_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION208_20261121.md`.
- No Banxico/IMF re-fetch or cohort rebuild; ₹0; protected invariants unchanged; UNKNOWN never PASS.


## Continuation 209 — Thailand THA Q2-2026 matrix evidence-link correction (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Registry, 63-country matrix and dedicated BOT–IMF report before selection. Rejected repeat numeric PASS and same-page source retrieval.
- Existing BOT report records Q2 assets +4,679.07 USDm and liabilities -238.36 USDm; archived IMF residuals +0.00342150334 / +0.001811289819 USDm, both PASS at ±0.005 USDm. BOT source remains preliminary; same-vintage NOT_ESTABLISHED.
- Corrected only THA matrix evidence_ref from NO_DEDICATED_REPORT_REF_IN_BASELINE to GCR_THAILAND_THA_Q2_2026_BOT_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120. THA remains DATA_CAPTURED; asset/liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_THAILAND_THA_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION209_20261121.md`. Matrix commit `0c3e3c46b5d56678295e2e02dfe0f4637ccc9b78`; matrix blob SHA `a9162af9a86514eaf78f741ba5e8c5927da50a7d`. Detail report commit `0be627c2d5aed9f94e017e4752602f71ad406209`.
- No BOT/IMF re-fetch, cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 210 — Costa Rica CRI Q2-2026 matrix evidence-link correction (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Registry, 63-country matrix and dedicated SECMCA/BCCR report before selection; no repeat numeric work or source retrieval.
- Existing report records Q2 portfolio assets +1,275.5 USDm and liabilities +1,167.5 USDm; residuals +0.04033796522 / -0.00633015469 USDm, both PASS at 0.1 USDm display precision. Direct BCCR raw-file SHA-256 and exact same-vintage bridge remain NOT_ESTABLISHED.
- Corrected only CRI matrix evidence_ref from NO_DEDICATED_REPORT_REF_IN_BASELINE to GCR_COSTA_RICA_CRI_Q2_2026_SECMCA_BCCR_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION148_20261121. CRI remains DATA_CAPTURED; asset/liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_COSTA_RICA_CRI_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION210_20261121.md`. Matrix commit `a442364f24dc3bfae527e2a6d3965613da9d1138`; matrix blob SHA `027d23b1a5ba868dad697d92061425d6c7915c37`; detail report commit `f42b0369004e20c3bc1034c64885683b4d64cc85`.
- No SECMCA/BCCR re-fetch, IMF re-query/cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 211 — Ecuador ECU Q2-2026 matrix evidence-link reconciliation (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Task Registry, 63-country matrix and dedicated BCE report before selection. Rejected repeat numeric comparison and source retrieval.
- Existing BCE report records Q2 assets -595.2 USDm and liabilities +1,000.3 USDm; residuals -0.03583203999 / -0.048809 USDm, both PASS at 0.1 USDm publication precision. National raw-file SHA-256 NOT_CAPTURED; same-vintage NOT_ESTABLISHED.
- Corrected only ECU matrix evidence_ref from NO_DEDICATED_REPORT_REF_IN_BASELINE to GCR_ECUADOR_ECU_Q2_2026_BCE_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION147_20261121. ECU remains DATA_CAPTURED; asset/liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_ECUADOR_ECU_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION211_20261121.md`; matrix commit `7ab32d8bb18a77b6c4ed8837a71fc4de2d8b444d`; matrix blob SHA-1 `15b89466d49e1f38c2d9c01a9dd3041f7971126b`; detail report commit `b48a52c2b92ad0a61e8df2a4f7920218b27568de`.
- No BCE/IMF re-fetch, cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 212 — Philippines PHL Q2-2026 matrix evidence-link reconciliation (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Task Registry, 63-country matrix and controlling BSP–IMF report before selection. Completed parser/capture/numeric work and closed generic vintage-search routes were not repeated.
- Existing report records BSP Q2 assets +1,331 USDm and liabilities +1,798 USDm; IMF differences -0.35704894474 / +0.28261626536 USDm, both within ±0.5 USDm. Successful raw/parsed artifact and release parity are documented; same-vintage remains NOT_ESTABLISHED.
- Corrected only PHL matrix evidence_ref from NO_DEDICATED_REPORT_REF_IN_BASELINE to GCR_PHILIPPINES_PHL_Q2_2026_BSP_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120. Preserved DATA_CAPTURED, asset REVIEW, liability REVIEW, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED; no gate promotion.
- Detail: `docs/GCR_PHILIPPINES_PHL_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION212_20261121.md`; matrix commit `4de3e0c125678ba9dfbe75b8358ae29478f9cdb8`, blob SHA-1 `a1a49e1d9517f09afcf584286d698aac637307a4`; report commit `270f5714db041305fd8839639804e2a4cb5c6c9e`.
- No BSP/IMF re-fetch, cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 213 — Cabo Verde CPV Q2-2026 BPM6 methodology conflict resolution (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Task Registry, 63-country matrix and C153 BCV source-gate report. Excluded repeated failed XLS retrieval; selected the distinct open BPM5/BPM6 methodology conflict.
- Official BCV June-2016 external-sector methodology explicitly documents BPM6 adoption, distinguishes BOP flows from IIP stocks, defines portfolio investment, and states BPM6 sign convention/gross reporting. The IMF e-GDDS BPM5 entry is therefore treated as likely legacy metadata, not current proof. The 12-Nov-2026 BCV methodology notice concerns monetary/financial statistics and does not supersede the external-sector note.
- Updated only CPV matrix descriptive note; retained SOURCE_FOUND, NOT_CAPTURED legs, UNKNOWN vintage, FULL_PASS NO and aggregate NOT_AUTHORIZED. No numeric gate promotion.
- Detail: `docs/GCR_CABO_VERDE_CPV_Q2_2026_BCV_BPM5_BPM6_METHODOLOGY_CONFLICT_RESOLUTION_CONTINUATION213_20261121.md`; matrix commit `d5c778f5ad1063a3d39ade392d2224bb6c04b1ce`, blob SHA-1 `1569f1eb77b5ad3eaddea881f72e5ca23ab5522e`; report commit `79d2ff1f143d1e17ce3b1d6013a101846978fd72`.
- No BCV XLS retry, IMF re-query, cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 214 — CPV C213 matrix evidence-reference read-back correction (2026-11-21)
- Preflighted the current Master Ledger, Priority Queue, Historical Task Registry and 63-country matrix; reopened C213. Found C213 had updated the CPV descriptive note but left evidence_ref at older C153.
- Corrected only CPV evidence_ref to `GCR_CABO_VERDE_CPV_Q2_2026_BCV_BPM5_BPM6_METHODOLOGY_CONFLICT_RESOLUTION_CONTINUATION213_20261121`. Matrix commit `e794becb96cf8342c3a285f156138b444f29731e`; blob SHA-1 `c14f4f8799e2c25cf054fbac4366c5840cf3c66e`.
- Preserved SOURCE_FOUND; data_capture NO; asset/liability NOT_CAPTURED; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED. No numeric or country gate promotion.
- Detail: `docs/GCR_CABO_VERDE_CPV_Q2_2026_MATRIX_EVIDENCE_REFERENCE_READBACK_CORRECTION_CONTINUATION214_20261121.md`; report commit `f0483d5696df1122b98195e273de5b0363d58cdf`.
- No BCV XLS retry, IMF re-query, cohort rebuild, synthetic data or production changes; ₹0; protected invariants unchanged; UNKNOWN never PASS.


## Continuation 215 — ZAF official SARB daily FX API route discovery (2026-11-21)
- Preflighted current Master Ledger, Priority Queue, Historical Task Registry and 63-country matrix; reopened controlling ZAF reconciliation and C127 FX boundary. Existing liability PASS and asset REVIEW were not recalculated.
- Discovered official SARB OpenAPI contract: `GET /WebIndicators/HistoricalExchangeRatesDaily`; live snapshot identifies “Rand per US Dollar”, series `EXCX135D`, latest observation 2026-11-20 = 17.4429. OpenAPI also documents date-bounded `GetTimeseriesObservations/{timeseriesCode}/{startDate}/{endDate}`.
- Attempted Q2 2026 date-bounded endpoint; current retrieval channel returned inaccessible/internal error. No Q2 rows, raw bytes/hash or response metadata captured. This is a retrieval-channel boundary, not proof SARB lacks the data. BOP transaction FX convention remains NOT_ESTABLISHED; ZAF asset REVIEW / NOT PASS; aggregate NOT_AUTHORIZED.
- Updated only ZAF matrix descriptive note; all stage/gate fields preserved. Matrix commit `95540297274a9a6f001e7b0f49dd47050f5acce2`; blob SHA-1 `3758ed7d60f65fffeffbd43d7228ffeb92bbc3f6`.
- Detail: `docs/GCR_ZAF_Q2_2026_SARB_OFFICIAL_DAILY_FX_API_ROUTE_DISCOVERY_CONTINUATION215_20261121.md`; report commit `51b16cb4e839ca32337be1c6e1becfa4739f4a7f`.
- Next: obtain the documented historical payload through a supported HTTP/API-capable route; validate dates/coverage and only use a daily mean if SARB's BOP conversion convention supports it. No IMF re-query/cohort rebuild, synthetic data, tolerance widening or production change; ₹0; UNKNOWN never PASS.


### C215A — ZAF matrix gate-orientation correction (2026-11-21)
- Independent read-back found the ZAF matrix asset/liability gates inverted relative to the controlling reconciliation: matrix had asset PASS / liability REVIEW, while the report has asset REVIEW / liability PASS.
- Corrected matrix to asset_gate REVIEW, liability_gate PASS; status_ASSET_PASS NO, status_LIABILITY_PASS YES; asset_status DATA_CAPTURED, liability_status LIABILITY_PASS. Stage DATA_CAPTURED, vintage PENDING, FULL_PASS NO and aggregate NOT_AUTHORIZED preserved.
- Matrix correction commit `86dfe96ae4b3a71a78a0eebbabd4fd36bd4ac4e3`; blob `a4ed9fcf8732dd81a1d1563aaf5388ed6c2bbd0a`. C215 report addendum commit `96cf932d5345859c01b7fb92ade0986f992b0ec5`.
- New SARB API Q2 historical payload remains NOT_CAPTURED; asset FX REVIEW remains open. No gate promotion, IMF re-query, cohort rebuild, tolerance widening or production change; UNKNOWN never PASS.

## Continuation 217 — South Africa ZAF SARB alternate export-family boundary (2026-11-21)
- Official SARB Online Statistical Query workflow verified: KBP code/keyword, version, frequency/date-range selection and Excel/CSV/PDF/DOC export for Quarterly Bulletin series.
- It is not proven to expose EXCX135D; do not treat KBP exports as the daily ZAR/USD target or infer a code mapping. No payload/hash captured.
- ZAF asset REVIEW, liability PASS, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED unchanged.
- Detail: docs/GCR_ZAF_Q2_2026_SARB_ONLINE_STATISTICAL_QUERY_EXPORT_FAMILY_BOUNDARY_CONTINUATION217_20261121.md. Next C218: prove or reject an official KBP daily USD/ZAR series and inspect the Selected Historical Rates export request via supported HTTP route.
## Continuation 218 — South Africa ZAF SARB KBP5339M monthly USD/ZAR cross-check (2026-11-21)
- Verified official SARB September 2026 Quarterly Bulletin p. S-114 series `(5339M)` (USA Dollar; monthly average; middle rates in SA cents per USD) and 10:30 weighted-average footnote.
- Q2 values: Apr 1,653.90 cents/R16.5390; May 1,648.06/R16.4806; Jun 1,639.70/R16.3970. No quarter aggregation.
- Monthly series is not daily EXCX135D; BOP transaction conversion convention remains NOT_ESTABLISHED. ZAF asset REVIEW, liability PASS, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED unchanged.
- Detail: docs/GCR_ZAF_Q2_2026_SARB_KBP5339M_OFFICIAL_MONTHLY_USD_ZAR_SERIES_VERIFICATION_CONTINUATION218_20261121.md. Next C219: daily series and BOP FX methodology.
## Continuation 219 — ZAF SARB B03/B31 reporting-currency methodology boundary and CHN handoff (2026-11-21)
- New official SARB B03 (May 2021) and B31 (June 2021) guides reviewed. B03/B31 report monetary amounts in ZAR thousands; B03 specifies accrual/transaction-time and market-price valuation for traded equity/debt; B31 covers institutional-investor foreign-asset acquisitions/disposals and transaction-value/time reporting.
- Neither guide discloses the compiler-side FX rate source/method for conversion into published BOP USD series. BPM6 3.104–3.106 gives the general benchmark but not proof of SARB's actual implementation. Prior ZAF liability arithmetic PASS and asset REVIEW preserved; method equivalence NOT_ESTABLISHED; ZAF remains PARTIAL; aggregate NOT_AUTHORIZED.
- ZAF guide search is bounded; do not repeat absent a new official source/revision. Next rank-1 cohort task returns to CHN detailed SAFE workbook access audit per C127; no IMF re-query/cohort rebuild.
- Detail: docs/GCR_ZAF_Q2_2026_SARB_B03_B31_REPORTING_CURRENCY_FX_METHODOLOGY_BOUNDARY_CONTINUATION219_20261121.md.
## Continuation 220 — Montenegro MNE CBCG Bulletin alternate-host route; next MNG candidate (2026-11-21)
- New distinct official `www.cbcg.me` host renders Bulletin 9/2026 (65 pages); the Tables 5.1–5.4 download affordance is visually confirmed on page 54.
- Raw PDF download failed; link annotation target and table-export URL remain unresolved; no workbook bytes/hash or Q2 dual-leg observations captured. MNE remains PARTIAL / NOT PASS.
- Next candidate MNG NSO PxWeb BOP table: official table page is accessible; public JSON/XML API is stated in NSO terms, but do not guess API route/request/indicator codes. Require official endpoint and method evidence before query.
- Detail: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_9_2026_ALTERNATE_HOST_AND_TABLE_LINK_ACCESS_CONTINUATION220_20261121.md. No IMF re-query/cohort rebuild; aggregate NOT_AUTHORIZED.
## Continuation 221 — Mongolia MNG NSO official API contract boundary (2026-11-21)
- Official NSO terms confirm JSON/XML open-data API, CC BY 4.0 and one-request-per-second/IP limit; live BOP table confirms Bank of Mongolia source, quarterly frequency, million USD, 69 indicators, 71 quarters and Q2 `2026-2`.
- Exact API root/path, HTTP method, query schema and indicator codes are not stated in inspected official docs. C179's failed API base was not retried; no guessed third-party client route used. No data bytes or hash captured.
- MNG remains PARTIAL / NOT PASS; next action requires an official API manual/OpenAPI contract or official Q2 export. Detail: docs/GCR_MONGOLIA_MNG_Q2_2026_NSO_PXWEB_OFFICIAL_API_CONTRACT_BOUNDARY_CONTINUATION221_20261121.md. No IMF re-query/cohort rebuild; aggregate NOT_AUTHORIZED.

## Continuation 222 — MNG matrix evidence-reference/read-back correction (2026-11-21)
- Reused C221 official NSO API-contract boundary; did not retry API or repeat source research.
- Corrected only the MNG national validation matrix evidence_ref to C221 and clarified its metadata/API boundary note. Preserved BLOCKED, both national legs NOT_CAPTURED, vintage UNKNOWN, FULL_PASS NO and aggregate NOT_AUTHORIZED.
- Final matrix commit `2074feae218e6890088d95412fbf7a1013c71bbf`; blob `b91df09667dc67b6b6fd595824606d324367b24f`. C222 report commit `7eea1f9e2341be21351a7e5201e95aa3c49a283b`.
- Next: MNG remains closed absent official API manual/OpenAPI or official Q2 export. Select another eligible fixed-cohort member only after exact report/route preflight. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 223 — GEO NBG statistics-data route boundary and matrix evidence correction (2026-11-21)
- New official NBG Statistics Data discovery surface confirms static Excel/interactive dashboards and title/code search; no accessible Q2 BOP table locator/API schema/payload found. C154's Q2 BPM5 release boundary and stale NSDP snapshot reused, not repeated.
- Corrected GEO matrix evidence_ref to C154 and clarified unresolved national Q2 dual-leg capture; all gates preserved (SOURCE_FOUND, national data NO, A/L NOT_CAPTURED, vintage UNKNOWN, FULL_PASS NO, aggregate NOT_AUTHORIZED).
- Matrix commit `9655247cb907dee8e4846bd9dd33e6b5d91f67c0`; blob `de7b182d3a3debee674c35c1e9fd980e99ab83b3`; C223 report commit `e279d4262f50e73311d1e306c812efb7909fdf67`.
- Next: GEO remains PARTIAL; reopen only on an exact official Q2 BOP export/API locator and raw data. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 224 — GIN BCRG MPC attachment resolution boundary (2026-11-21)
- Reused C170 BCRG source audit. Official 2026 archive links to the 22nd MPC article (22-Sep-2026); article exposes “Télécharger” text but no file target/attachment URL in the inspected page representation. No guessed media path or API; no raw bytes or Q2 portfolio legs.
- Corrected GIN matrix evidence_ref to C170 and clarified that the attachment target remains unresolved. GIN remains BLOCKED; A/L NOT_CAPTURED; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Matrix commit `0c4f29eebc6b508e7f17473a26f0c28f6bbd90be`; blob `d6b1986f1c029f0ea4b69dd77549e0b6cbd596b3`; C224 report commit `9415534d63c43c5d3d64acf3b225ad8fb0e7eb23`.
- Do not repeat the same article/archive extraction. Reopen only if BCRG exposes a distinct downloadable file target or documented data export/API.


## Continuation 225 — AZE CBAR external-sector index / combined-category boundary
- Distinct official CBAR External Sector Statistics index and Interactive Statistic Database navigation inspected. Database shell returned no data text; 2026 attachment controls did not expose a distinct Q2 raw export locator.
- CBAR Statistical Bulletin 09/2026 Table 1.4 confirms Q2-2026 asset/liability totals but only groups “portfolio and other investments” under each leg (-302 / +2,466 USDm). These combined figures are not portfolio-only and cannot validate IMF portfolio rows.
- AZE matrix note/evidence_ref updated to C225; country gates preserved: national A/L NOT_CAPTURED, vintage UNKNOWN, FULL_PASS NO, aggregate NOT_AUTHORIZED. No IMF re-query/cohort rebuild.
- Matrix commit `b85f7d9cfc927b7301bf91591ae0b004d54a0282`; blob `9b1b7a82cf43455eaba82cd0a054e3976e734f5d`; report commit `af4425511747a7dc3c91b68508e63023fe44d3f7`.
- Reopen only on a distinct detailed Q2 export/API with portfolio separated from other investment for both legs.


## Continuation 226 — BDI BRB June-2026 monthly indicators non-BOP boundary (2026-11-21)
- Fresh preflight reused C155/C207 and excluded completed historical-table audit/evidence-link correction. Inspected a distinct official BRB June-2026 “Indicateurs de conjoncture” PDF (18 pages) from the official index.
- PDF contents cover production, CPI, trade, FX, public finance, monetary/banking indicators; no BOP section. Full-text search for “Balance des paiements” returned no match. Trade and FX data are not portfolio transaction legs.
- No Q2-2026 portfolio asset/liability values, BOP raw bytes, revision metadata or SHA-256 captured. BDI remains PARTIAL / NOT PASS; national legs NOT_CAPTURED; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- No matrix change because this is a source-family exclusion only; no IMF re-query/cohort rebuild or production change. Detail: `docs/GCR_BURUNDI_BDI_Q2_2026_BRB_JUNE_2026_INDICATEURS_NON_BOP_SOURCE_BOUNDARY_CONTINUATION226_20261121.md`. Reopen BDI only on a distinct official Q2 BOP dual-leg export with dated revision metadata. ₹0; UNKNOWN never PASS.


## Continuation 227 — Malaysia MYS Q2-2026 matrix evidence-reference correction (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Task Registry, fixed 63-country matrix and controlling MYS BNM reconciliation report before selection.
- Existing BNM official 1200-middle raw capture, FX QA and separate-leg comparisons were already complete; no BNM re-fetch, IMF re-query, cohort rebuild or numeric recalculation.
- Corrected only MYS matrix `evidence_ref` from `NO_DEDICATED_REPORT_REF_IN_BASELINE` to `GCR_MALAYSIA_MYS_Q2_2026_BNM_OFFICIAL_FX_AND_DUAL_LEG_RECONCILIATION_20261120`. Preserved DATA_CAPTURED, asset/liability PASS, vintage PENDING, FULL_PASS NO and aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_MALAYSIA_MYS_Q2_2026_MATRIX_EVIDENCE_REFERENCE_READBACK_CORRECTION_CONTINUATION227_20261121.md`. Matrix commit `7e544e73de2aac8c8f12d1e6e43391ae00ec3f05`, blob SHA `4a81b4216e37013e0dc1a60a3c00e9a682f6f059`.
- MYS remains PARTIAL / NOT PASS because same-vintage BNM preliminary ↔ IMF alignment is NOT_ESTABLISHED. Do not repeat FX capture or promote aggregate; ₹0; UNKNOWN never PASS.


## Continuation 228 — NSE Run #339 raw-source artifact packaging root cause and retention correction (2026-11-21)
- Inspected Run #339 job log and downloaded artifact 14660032260. ZIP SHA-256 `23e74e7f9ef2e32bf5b6bbc5a931814c06fe065835b8bdda74f3c00dbdafd213`; 17 entries, no NSE raw bhavcopy/delivery CSV, sessions file, acquisition diagnostics, security master or raw manifest. Job log/QA nevertheless records 200 successful full-delivery files / raw_files=200.
- Compared Run #416 artifact 14632139339 (SHA-256 `b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082`): normalized 200-session data and security master retained, but original raw files/manifest absent.
- Direct workflow inspection confirmed upload-artifact allowlist omitted `data/raw/sec_bhavdata_full_*.csv`, sessions, acquisition diagnostics and security master. Corrected the allowlist on isolated branch `audit/prospective-selector-tracking` only; commit `46f4a359f21da676cb0c92e874fb08f14ee20d90`.
- Future artifact-retention correction PASS by commit; future-run proof PENDING. Historical Run #339 raw bytes remain BLOCKED; per-file provenance manifest NOT_DONE. Do not redownload or infer old URL/timestamps.
- Detail: `docs/NSE_RUN339_RAW_SOURCE_ARTIFACT_PACKAGING_ROOT_CAUSE_AND_RETENTION_FIX_CONTINUATION228_20261121.md`. No production code/selector/ranking/CORE-672 changes; ₹0; UNKNOWN never PASS.

## Continuation 229 — CDSL daily archive raw freshness and arithmetic QA (2026-11-25)
- Reused existing verified artifact 14527092174 / run 44519322726; ZIP SHA-256 rechecked as 83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd. No new source request.
- CDSL archive raw page capture: 19-Nov-2026 11:57:09.076562 UTC, HTTP 200, 73,784 bytes, SHA-256 aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df; displayed investment/derivatives cutoff 02-Mar-2026.
- Scoped arithmetic QA: 75/75 daily/March/YTD numeric rows and 8/8 cumulative rows satisfy purchases-sales=net; INR subtotals 3/3 exact; USD daily and March subtotal sums each differ from published total by -0.01 USDm, retained as REVIEW; YTD USD sum exact.
- This artifact-specific 02-Mar snapshot conflicts with C39's 30-Sep and C68's 31-Oct rendered archive snapshots for the same URL. Preserve each raw capture; do not claim archive completeness or choose a canonical response. CDSL daily 18-Nov eServices and 15-Nov fortnightly sector results remain separate accepted evidence; no repeat.
- CDSL archive parsing/arithmetic subtask: PASS. Archive freshness/completeness: NOT PASS / UNKNOWN. NSDL Archive postback and matched-date reconciliation remain NOT_DONE.
- Detail: docs/GCR_CDSL_DAILY_ARCHIVE_RAW_FRESHNESS_AND_ARITHMETIC_QA_CONTINUATION229_20261125.md; report commit undefined.
- Next exact action: one fresh-state NSDL Archive public date selection + View Report using supported interactive browser; if unavailable, preserve NOT_DONE and do not guess POST/ViewState. No stale-state replay.

## Continuation 230 — NSDL archival permission gate reconciliation (2026-11-25)
- Re-read current ledger, queue, registry, C76 form-contract audit and C229 CDSL raw archive QA. C76/C229 suggest a fresh-state NSDL View Report postback, but the controlling Continuity Ledger explicitly marks NSDL FPI/DII archival BLOCKED pending written permission. No written permission evidence is present.
- Decision: NSDL postback NOT_AUTHORIZED; no postback, guessed POST, stale ViewState replay, scraping or reverse engineering. NSDL rows remain NOT_CAPTURED; matched-date reconciliation NOT_DONE. CDSL C229 arithmetic PASS retained; freshness/completeness remains NOT_PASS / UNKNOWN.
- CHN known XLSX routes and COL desktop-only/502 routes remain blocked; POL same-vintage USD bridge remains unresolved. Next cohort candidate may be reopened only on a genuinely new official route; TUR's known ZIP timeout is closed absent a distinct official route/source revision. No IMF re-query/cohort rebuild.
- Detail: docs/GCR_NSDL_ARCHIVAL_PERMISSION_GATE_RECONCILIATION_CONTINUATION230_20261125.md. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 231 — Rwanda RWA BNR WebDash alternate-route boundary (2026-11-25)
- Preflight: re-read current Master Ledger, GCR queue, 63-country registry, RWA C97/C130, NPL C58/C94/C130, SLV C100/C131, and Library Mother File 1–53 + GCR Gap Matrix. PASS work skipped.
- NPL: current NRB External Sector page still points to the known BPM6 XLSX; current NSDP BOP Download in SDMX resolves to the already known stale NEPAL_BOP_2024_Q1.xml (unsupported XML). No genuinely new official Q2 API/export route; NPL stays PARTIAL/BLOCKED. No repeated XLSX fetch.
- RWA: distinct official https://webdash.bnr.rw/ identified. Its indexed BOP table exposes annual USDm data 2019–2023 with a combined portfolio investment row, but no Q2-2026, separate asset/liability legs, API/export contract, or raw payload. BNR June-30-2026 portal item remains JS shell / exact file unresolved. October-2026 MPFSS Table 12 remains H1 net-only +USD14m, not Q2 or dual-leg. RWA remains PARTIAL/NOT PASS; both Q2 legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED.
- Matrix RWA evidence_ref/note updated only; no gate promotion. Report: docs/GCR_RWANDA_RWA_Q2_2026_BNR_WEB_DASH_ALTERNATE_ROUTE_BOUNDARY_CONTINUATION231_20261125.md (commit 719b1482b5b1216d0a3a6cb5ea73c6a002f81025).
- Next fixed-cohort follow-up: SLB official transaction-FX conversion-method boundary from C132, after exact route-history preflight. No generic quarterly FX conversion or inferred sign/scale. ₹0; no IMF re-query/cohort rebuild; production unchanged; UNKNOWN never PASS.


## Continuation 232 — Solomon Islands SLB CBSI official Q2 dataset locator / FX method boundary (2026-11-25)
- Mandatory preflight re-read current ledger, GCR queue, 63-country registry/matrix, SLB C99/C132 evidence, C128 batch handoff, C231 and Library Mother File 1–53 + GCR Gap Matrix. Existing PASS arithmetic and IMF archive rows were reused, not repeated.
- New official CBSI BOP page: https://www.cbsi.com.sb/data-statistics/economic-statistics/balance-payments explicitly states BPM6, quarterly/annual series, SB$ million presentation and latest Q2-2026. Its Download link resolves to https://www.cbsi.com.sb/sites/default/files/2026-09/Balance-of-Payment-Statistics-2006-2026-Q2.xlsx. Web retrieval returned HTTP 400 unsupported XLSX MIME; direct byte download also failed. No raw workbook/hash claimed.
- CBSI June-2026 Quarterly Review gives Q2 quarterly-average SBD/USD 8.08 and Table 1.17 portfolio assets +38 SBDm / liabilities nil. It does not say this quarterly average is the BOP compiler's transaction conversion rate. Official daily exchange-rate page describes daily SBD/USD rate publication, but does not link it to BOP conversion. Therefore transaction FX method and SLB-specific IMF SCALE/display bridge remain NOT_ESTABLISHED; 8.08 is context only, not a numeric PASS.
- SLB remains PARTIAL / NOT PASS; asset/liability numeric comparison REVIEW, vintage PENDING, aggregate NOT_AUTHORIZED. Matrix evidence_ref/note updated only; no gate promotion. Detail: docs/GCR_SOLOMON_ISLANDS_SLB_Q2_2026_CBSI_OFFICIAL_DATASET_AND_TRANSACTION_FX_METHOD_BOUNDARY_CONTINUATION232_20261125.md; report commit a5c7ecc52b89d8fff0d81bec0b00b785f123abf2.
- Next fixed-cohort unresolved item: SRB same-vintage/revision bridge, after re-reading C101/C103/C104/C109/C112 and current matrix/queue. Do not repeat its accepted monthly arithmetic or sign/FX method work. ₹0; no IMF re-query/cohort rebuild; no production change; UNKNOWN never PASS.


## Continuation 233 — Serbia SRB same-vintage / revision bridge route boundary (2026-11-25)
- Re-read current ledger, queue, 63-country registry and SRB C104/C109/C110/C111; C112 not found as a distinct SRB report in current repo docs or Library search. September-vintage May legs/arithmetic and NBS/IMF method semantics remain PASS; not repeated.
- Official NBS Bulletin archive only exposes generic Select/Input/Show controls; XLS link leads to general Statistics landing page. July issue chronology is confirmed but no July Table 2.3 header/May leg capture. Known July PDF direct URL remains closed after C109–C111 timeout; no duplicate fetch.
- SRB July-vintage May legs NOT_VERIFIED; July-to-September revision NOT_DONE; raw bytes/hash NOT_CAPTURED; national scope and USD/EUR bridge NOT_ESTABLISHED. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: ${reportPath}; report commit ${created.result.commit_sha}. Resume only with supported browser DOM/download or a genuinely new official byte route. ₹0; no IMF re-query/cohort rebuild; no production changes; UNKNOWN never PASS.


## Continuation 234 — Mongolia MNG official Open Data API contract advance (2026-11-25)
- After C233 SRB route remained blocked, selected MNG from the fixed cohort after exact preflight C179/C190/C221/C222. PASS work and known failed endpoint attempts were not repeated.
- New official NSO Open Data documentation publishes GET route example, table metadata response fields (title, variables/code/text/values/valueTexts) and JSON/XML output. NSO terms include <=1 request/second/IP, <=100,000 responses/request and CC BY 4.0.
- Official MNG BOP table page confirms quarterly, million USD, Bank of Mongolia source, 69 Indicator and 71 Quarter values incl. 2026-2; no separate portfolio indicators yet captured. Candidate table-specific API route remains inaccessible through current retrieval surface; no HTTP response/body/hash or query claimed.
- MNG remains BLOCKED / PARTIAL / NOT PASS; national A/L NOT_CAPTURED; aggregate NOT_AUTHORIZED. Detail: docs/GCR_MONGOLIA_MNG_Q2_2026_OFFICIAL_OPEN_DATA_API_DOCUMENTATION_AND_TABLE_ROUTE_BOUNDARY_CONTINUATION234_20261125.md; report commit fc9d3bfb4503c75e30341f90277823977a417d52.
- Next: exact table metadata GET via supported client, then real indicator-code identification and Q2-only capture. No guessed query, IMF re-query/cohort rebuild, paid source or production change; ₹0; UNKNOWN never PASS.

## Continuation 235 — MNG documented GET .px metadata route test (2026-11-25)
- Fresh preflight: current ledger/queue/registry, MNG C179/C190/C221/C222/C234, matrix, C233 handoff and Library Mother File/Gap context. Reused C234's new official NSO Open Data GET/schema documentation.
- One distinct .px-suffix table metadata GET attempt for MNG returned “URL not accessible” from the current retrieval surface. No HTTP status/headers/body/bytes/hash; no indicator metadata or Q2 A/L values. Do not mislabel as HTTP 4xx/5xx.
- Close this exact URL variant for repeat through the same reader. MNG remains BLOCKED/PARTIAL/NOT PASS; A/L NOT_CAPTURED; aggregate NOT_AUTHORIZED. Detail: docs/GCR_MONGOLIA_MNG_Q2_2026_DOCUMENTED_GET_METADATA_ENDPOINT_SUFFIX_TEST_CONTINUATION235_20261125.md; report commit 08c32ffc9d205e7141118a98c71c9637bcee1ee0.
- Next: genuinely different supported GET-capable client/browser or official Q2 export; if unavailable, move to next eligible cohort member after fresh route-history preflight. No IMF re-query/cohort rebuild; ₹0; production unchanged; UNKNOWN never PASS.



## Continuation 236 — Angola AGO BNA dissemination schedule / public access boundary (2026-11-25)
- Preflight: current ledger/queue/registry/matrix, C142 and Library Mother File/GCR context re-read. Existing PASS and the previously attempted BNA SPA route were skipped.
- New official INE PASEN 2026 schedule: BNA BOP/IIP production is quarterly under MBP6; public availability is quarter n+1. BNA dissemination calendar specifies previous-quarter BOP/IIP, bimonthly, website placement after 60 days. Current IMF e-GDDS metadata says quarterly external-sector data are publicly posted on the BNA website simultaneously; hard-copy quarterly bulletin and annual BOP/IIP mailing-list language is separate.
- The 4-Sep-2026 Q2 release announcement is timing-consistent, but public text has only account-level current-account and capital/financial totals; no portfolio A/L rows or detailed raw attachment locator/API/schema identified. This corrects the overly broad mailing-list-only reading in C142 but does not validate national values.
- AGO remains SOURCE_FOUND / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED. Matrix gate unchanged; evidence_ref points to C236.
- Report: docs/GCR_ANGOLA_AGO_Q2_2026_BNA_DISSEMINATION_CALENDAR_AND_PUBLIC_ACCESS_BOUNDARY_RECONCILIATION_CONTINUATION236_20261125.md (commit 7aec846aef1f3a1079ad503215fba3579f72eeae).
- Next: supported official BNA public download/browser route for detailed Q2 portfolio A/L, otherwise advance to next fixed-cohort country after fresh route-history preflight. No guessed API, no BNA SPA repeat, no IMF re-query/cohort rebuild; ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 237 — Albania ALB official Q2-2026 portfolio dual-leg capture (2026-11-25)
- Preflight: current ledger/queue/registry/matrix, Library Mother File/GCR context, ALB C139–C141/C192 reread. Existing PASS sign/taxonomy and IMF rows reused; legacy Main-data route closed and not repeated.
- New distinct official BoA Monthly Statistical Report 08/2026 PDF https://www.bankofalbania.org/rc/doc/RSM_gusht_2026_anglisht_35170.pdf; Table 2-1 is quarterly BOP in EURm and separately reports Q2 assets +156.25, liabilities +124.70, net +31.55. Published net identity exact.
- Official PDF text captured through document reader; raw bytes/headers/hash not captured (direct download failed). Archived IMF rows reused: A=181700604.8387097 USD, L=145011618.7096774 USD (SCALE=6). No FX conversion or IMF re-query; implied ratios not admitted.
- ALB current_stage DATA_CAPTURED; asset/liability gates REVIEW pending approved EUR/USD flow conversion; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_MONTHLY_STATISTICAL_REPORT_OFFICIAL_DUAL_LEG_CAPTURE_CONTINUATION237_20261125.md (commit 214a86283beb2ecc1cca5dfabf7d39201ac748cd).
- Next: independent official Q2 transaction-FX conversion methodology and revision cutoff. Do not repeat legacy Main-data route or re-query IMF. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 238 — Albania ALB official FX convention / revision boundary (2026-11-25)
- New official BoA June-2014 BPM6 commentary confirms EUR BOP presentation and user conversion convention: average FX for flows, end-period FX for stocks. BoA monthly average rates to ALL are simple averages of daily official rates. IMF BPM6 §§3.105–3.106 clarify transaction/shortest-period conversion and converting underlying flows before deriving net.
- Exact Q2-2026 portfolio-specific USD aggregation and same-vintage/revision cutoff remain NOT_ESTABLISHED. No inferred cross-rate or unweighted quarterly mean used; no conversion applied. ALB numeric gates REVIEW, vintage UNKNOWN, aggregate NOT_AUTHORIZED.
- Report: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_OFFICIAL_FLOW_FX_RULE_AND_REVISION_BOUNDARY_CONTINUATION238_20261125.md (commit 01d226cb0c6d751643e988ff6f5377600e87adc7). Next: distinct dated Q2 revision/methodology/transaction-rate evidence only; else advance fixed cohort. No legacy-route repeat, IMF re-query or cohort rebuild.


## Continuation 239 — BGD Bangladesh Q2-2026 official publication boundary (2026-11-25)
- Selected after C238 Albania boundary and exact current matrix/registry preflight. New official Bangladesh Bank Quarterly Vol XXIII No.4 covers April-June 2026; Table V.1 is USDm and maps calendar Q2-2026 to FY26 Q4.
- Portfolio investment is net-only in Table V.1; separate portfolio asset/liability legs are not exposed. Other-investment and reserve-asset leg rows are not portfolio substitutes. FY26 values provisional; no observation-specific vintage bridge.
- BGD remains SOURCE_FOUND / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED. Report docs/GCR_BANGLADESH_BGD_Q2_2026_BB_Q4FY26_NET_ONLY_SOURCE_BOUNDARY_CONTINUATION239_20261125.md (commit 68b6eb13da5ca33ba26f4f8d0ec5734f041642f3).
- Reopen only on distinct official Q2 dual-leg data with revision metadata. No net-to-leg backsolve, IMF re-query, cohort rebuild or production change.


## Continuation 240 — TJK Tajikistan official NBT workbook route fingerprint (2026-11-25)
| Country | New official route | C240 finding | Status | Duplicate prevention / reopen condition |
|---|---|---|---|---|
| TJK Tajikistan | NBT BOP page https://www.nbt.tj/en/payments_balance/; Standard 2026 XLSX https://www.nbt.tj/upload/iblock/d9d/6x5djzg70lrzfq0t9f3pibhv3vmkb71x/st_pr_2026_2.xlsx; Analytical 2026 XLSX https://www.nbt.tj/upload/iblock/1fd/gt06fcxjn5ilv466tnxmf28usqj9vnc5/an_pr_2026_2.xlsx | Official BOP source and exact 2026 workbook locators confirmed; reader rejects XLSX MIME (400), direct standard-workbook byte download failed. No raw bytes/schema/Q2 A/L/vintage/hash. | SOURCE_FOUND / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED | Do not repeat same reader click/direct download. Reopen only through genuinely different supported XLSX-capable byte route or distinct official NBT export with revision metadata. |
- Detail: docs/GCR_TAJIKISTAN_TJK_Q2_2026_NBT_OFFICIAL_STANDARD_BOP_XLSX_LOCATOR_AND_BYTE_ACCESS_BOUNDARY_CONTINUATION240_20261125.md; report commit 35f0059e6d7a884db9f606d288c4d5919d0d1e85. No IMF re-query/cohort rebuild or production change. ₹0; UNKNOWN never PASS.


## Continuation 241 — Montenegro MNE CBCG Bulletin 9/2026 table-annotation boundary (2026-11-25)
- Re-read current Master Ledger/Queue/Registry/matrix and Library Mother File/GCR context; controlling MNE C182 report inspected. C237–C240 work skipped; no IMF re-query/cohort rebuild.
- Official CBCG Bulletin 9/2026 re-opened. PDF text reader exposes “Tables 5.1–5.4 - download tables” but not the annotation target/direct payload URL. Same PDF byte-preserving download failed in current runtime. No raw bytes, headers, SHA-256, table workbook or Q2 portfolio A/L values captured.
- Reconfirmed official methodology text: BPM6, quarterly EUR, transaction-day and average FX conventions; bulletin data preliminary/revisable. No conversion or stock/flow substitution.
- MNE remains PARTIAL / NOT PASS; both Q2 legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED. Do not repeat same PDF text extraction/download, C180 ZIP or NSDP XML/Browse routes. Reopen only with supported annotation/link extraction or distinct official export endpoint.
- Detail: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_9_2026_TABLE_ANNOTATION_ACCESS_BOUNDARY_CONTINUATION241_20261125.md (commit c7eb31705caef3183f90a848a08551210026402a). ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 242 — Paraguay PRY BCP Statistical Annex alternate export boundary (2026-11-25)
- Re-read current Ledger/Queue/Registry/matrix, Library Mother File/GCR context and PRY C60 report. C237–C241 and PASS work skipped; no IMF re-query/cohort rebuild.
- Distinct official BCP Statistical Annex page states the periodically updated file includes balance-of-payments statistics. Current XLSX locator: https://www.bcp.gov.py/documents/20117/213069/Anexo_Estad%C3%ADstico_del_Informe_Econ%C3%B3mico_23_11_2026.xlsx/1fc7fda2-74cf-e07c-be5b-535f02a89ba3?t=1795456089070 . Reader click returned HTTP 400 unsupported XLSX MIME and separate byte download failed.
- This is not the C60 Q2-specific BOP/IIP workbook URL. However, no annex bytes/sheets/Q2 coverage or portfolio A/L values were obtained. BCP BOP page confirms quarterly/annual dissemination with 3-month lag; next quarterly calendar date is 30-Dec-2026.
- PRY remains PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED. No repeat of C60 workbook URL or this same annex reader/download path. Detail: docs/GCR_PARAGUAY_PRY_Q2_2026_BCP_STATISTICAL_ANNEX_ALTERNATE_EXPORT_ACCESS_BOUNDARY_CONTINUATION242_20261125.md (commit ec6e16fb0507a278cf1cc23e6c98548596cc81a5). ₹0; production unchanged.


## Continuation 243 — WSM Samoa release-status recheck (2026-11-25)
- Direct official CBS index recheck did not confirm the search-index “September 2026” snippet: the opened page's Latest list still begins with June 2026 and footer says 18-Aug-2026. C125/C126 June bulletin Q1 finding reused; no repeated PDF extraction.
- WSM Q2-II portfolio A/L remain NOT_CAPTURED; SOURCE_FOUND / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Do not treat the search snippet as release evidence.
- Next WSM action: wait for a later issue to appear on the direct CBS index; verify internal reporting period and Table B-1 before capture. Otherwise continue the next eligible fixed-cohort task after exact route-history preflight. Report: docs/GCR_SAMOA_WSM_Q2_2026_CBS_OFFICIAL_INDEX_RELEASE_STATUS_RECHECK_CONTINUATION243_20261125.md.


## Continuation 244 — MEX Banxico Q3 schedule / Q2 vintage precheck (2026-11-25)
- Re-read current Ledger, Priority Queue, Historical Registry, fixed 63-country matrix, Library Mother File GCR context, and controlling MEX C137/C208 reports. Existing Q2 dual-leg numeric PASS was reused; no repeat PDF/SIE extraction, no IMF re-query, no cohort rebuild.
- Official Banxico BOP page schedules quarterly releases on 25-May/August/November at 09:00 and still lists Q2 (25-Aug-2026) as latest. Indexed November calendar lists Q3-2026 BOP for 25-Nov-2026. At 19:10 IST (07:40 Mexico City), the scheduled 09:00 Mexico City publication was 80 minutes away; no Q3 release/Q2 revision was captured.
- MEX existing numeric legs remain PASS at ±USD0.5m; same-vintage remains NOT_ESTABLISHED; MEX PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Exact post-release action: after 20:30 IST, inspect official Banxico page; if Q3 release appears, capture bytes/metadata/hash and inspect only its Q2 revised legs and explicit vintage/version bridge. Release date alone is not same-vintage proof. If absent, stop; no inferred publication.
- Report: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_Q3_RELEASE_SCHEDULE_AND_VINTAGE_GATE_PRECHECK_CONTINUATION244_20261125.md; commit 86196e69abcd73f494e19e3ec2519e112f50e0d7. ₹0; invariants unchanged; UNKNOWN never PASS.


## Continuation 245 — Uzbekistan UZB CBU Q2 latest-vintage / release-calendar boundary (2026-11-25)
- Preflight: current Ledger/Queue/Registry/63-country matrix, Library Mother File GCR context and UZB C123 report re-read. Existing numeric comparison PASS reused; no IMF re-query/cohort rebuild or repeated prior XLSX-byte attempt.
- New official source audit: CBU standard BOP dataset page indexed update 29-Sep-2026, Q2/2026 latest; e-GDDS calendar schedules Q2 BOP 30-Sep and Q3 BOP 31-Dec. Official H1-2026 review (29-Sep) reports net portfolio investment inflows around USD2bn only; not separate Q2 A/L. H1 statistical bulletin XLSX appears in 24-Nov statistics-page search index, but current dynamic page surface was stale and workbook bytes/headers were not exposed.
- “million USD, end of period” remains ambiguous for BOP transaction rows without workbook headers. Same-vintage/revision bridge not established. UZB DATA_CAPTURED; existing asset/liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_UZBEKISTAN_UZB_Q2_2026_CBU_LATEST_VINTAGE_AND_RELEASE_CALENDAR_BOUNDARY_CONTINUATION245_20261125.md (commit 5a4efbb7d5608682b482419d48e18070826ca6e9).
- Next: distinct supported byte-preserving CBU H1-2026 XLSX/Q2 workbook route and explicit time-basis/revision metadata only. No IMF re-query/cohort rebuild; ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 245 — Uruguay URY BCU Q2 preliminary-status / Q3 release vintage gate (2026-11-25)
- Selected URY after C244 based on fixed-cohort matrix: prior numeric dual-leg PASS already exists; same-vintage gate remains open. Existing arithmetic and IMF rows reused, not repeated.
- New official BCU Q2 report remains explicitly preliminary; Table 9 sector-level portfolio flow table is confirmed. BCU official calendar lists Q3-2026 “Cuentas Internacionales” for 30-Dec-2026. No Q2 revision identifier or observation-specific BCU↔IMF vintage bridge found.
- URY remains DATA_CAPTURED; asset/liability numeric PASS reused; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED. Matrix unchanged.
- Report: docs/GCR_URUGUAY_URY_Q2_2026_BCU_PRELIMINARY_STATUS_AND_Q3_RELEASE_VINTAGE_GATE_CONTINUATION245_20261125.md. Next: inspect Q3 publication after 30-Dec-2026 for Q2 revisions and explicit vintage bridge. No IMF re-query/cohort rebuild, ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 246 — Mexico MEX Q3 release post-publication vintage recheck (2026-11-25)
- C244's scheduled 25-Nov post-release check was completed. Official Banxico Q3-2026 BOP PDF dated 25-Nov is now listed and inspected.
- Its Q2 portfolio rows show assets USD 9,480m and liabilities USD 10,561m (net balance -1,082m). Previously accepted numeric dual-leg comparison is reused; no recalculation or IMF re-query.
- The footnote identifies principal revisions in profits/dividends, direct investment and services, but does not identify whether Q2 portfolio asset/liability observations changed. No observation-specific revision timestamp/version bridge; MEX vintage remains PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED.
- Report: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_Q3_RELEASE_POSTPUBLICATION_VINTAGE_RECHECK_CONTINUATION246_20261125.md (commit 2a4e47d5d82933ffe11bedcc2a0738d4b8994458). Next: compare Q2 portfolio pair against the 25-Aug first-release table and capture explicit revision metadata; otherwise retain UNKNOWN and advance. ₹0; cohort immutable; production unchanged.


## Continuation 247 — CHN China SAFE Q2 official A/L and sign-crosswalk audit (2026-11-25)
- SAFE official Q2 table (29-Sep) shows portfolio assets -488 and liabilities +433 in USD100m rounded units. Archived IMF rows (19-Nov, no new query): asset +48.794459bn; liability +43.286601bn.
- Rounded display precision cannot test ±USD0.5m; asset sign crosswalk remains REVIEW. Liability PASS is prior accepted status only, not re-proven by rounded abridged display. SAFE 13-Nov Q3 release lacks standalone portfolio legs; no 9M subtraction/back-solving. Detailed XLSX bytes/schema/hash/revision bridge unavailable.
- CHN status: asset REVIEW; liability PASS retained; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED. Report docs/GCR_CHN_C247_STATUS_20261125.md; matrix updated. Next distinct supported official XLSX transfer route only; no IMF re-query.


## C246 authoritative correction note (carried forward in C247)
The earlier C246 prose saying both MEX legs PASS is superseded by direct comparison: 25-Aug Banxico Q2 asset USD8,937m vs 25-Nov Q3-release Q2 asset USD9,480m (+USD543m); liabilities USD10,561m unchanged. Archived IMF asset USD8,937.255098m now differs by USD542.744902m; liability USD10,561.285114m differs by -USD0.285114m. Correct MEX gate: asset REVIEW, liability PASS, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED. Matrix row synchronized. Do not rely on earlier C246 both-leg PASS sentence.


## Continuation 248 — Colombia COL Q2-2026 official portfolio series scope / alternate-route audit (2026-11-26)
- Preflight re-read current Master Ledger, Priority Queue, Historical Registry, 63-country matrix, Library Mother File and COL C151/C152/C162 reports. Reused existing cohort/IMF panel; skipped C247 CHN, C246 MEX and all PASS work.
- Confirmed official catalogue metadata for two quarterly BOP portfolio legs through Q2-2026 in current USDm. Also identified a separate monthly local-market foreign portfolio flow series; it is not the national BOP A/L dual-leg dataset and is NOT_ADMITTED as a substitute.
- Q2 IIP portfolio positions are stocks, and the Q2 financial-account net total includes derivatives/reserves/other components; both are excluded as substitutes.
- Same SUAMECA 502/dashboard and documented desktop-export paths were not retried. No raw Q2 A/L observations, exact series IDs, export bytes, SHA-256, sign bridge or vintage evidence obtained.
- COL remains BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Matrix row updated only with C248 evidence pointer and explanatory note; all gate states unchanged.
- Report: docs/GCR_COLOMBIA_COL_Q2_2026_OFFICIAL_PORTFOLIO_SERIES_SCOPE_AND_ALTERNATE_ROUTE_AUDIT_CONTINUATION248_20261126.md (commit a1206349a0ae0285e97b5e406fdbfc05651296b2).
- Next eligible country task: POL (Poland), after fresh preflight; no unsupported PLN→USD conversion. ₹0; no IMF re-query/cohort rebuild; no production changes; UNKNOWN never PASS.


## Continuation 249 — POL Poland NBP version-2.1 publication / latest vintage boundary (2026-11-26)
- Re-read current Ledger, Queue, Registry, matrix, Library Mother File 1–53 and POL C163/C164/C165/C181. Prior PLN dual legs and transaction-date FX rule reused; no repeat extraction, NBP byte retry, IMF re-query or cohort rebuild.
- NBP public reporting list shows explanatory-notes v2.1 dated 13-Jul-2026, but its attachment URL/bytes/text are not exposed in the inspected page. Retrievable v2.0 notes specify actual transaction-date/prior-day rate for other data and four-decimal reporting FX precision; this does not supply underlying Q2 currency/date weights.
- NBP latest indexed 13-Nov monthly BOP is September and preliminary/revisable; no matched Q2 USD portfolio dual-leg or NBP–IMF same-vintage bridge found. POL remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_POLAND_POL_Q2_2026_NBP_VERSION21_PUBLICATION_AND_LATEST_VINTAGE_BOUNDARY_RECHECK_CONTINUATION249_20261126.md (commit 37573606aa47bb1fa65a14ddbf66032088e98e42). Matrix note/evidence_ref updated without gate promotion.
- Next candidate MNE; reopen only via supported CBCG table annotation extraction or distinct official export route. Do not repeat C241 failed routes. ₹0; production unchanged; UNKNOWN never PASS.

## Continuation 250 — MNE Montenegro CBCG official BPM6 download route fingerprint (2026-11-26)
- Re-read current Ledger, Queue, Registry, fixed 63-country matrix, Library Mother File 1–53 and C241. Skip PASS work; do not repeat CBCG Bulletin PDF reader/byte route, old CBCG ZIP, MONSTAT NSDP SDMX/XML/Browse, IMF re-query or cohort rebuild.
- New official CBCG BOP statistics page: https://www.cbcg.me/me/statistika/statisticki-podaci/ekonomski-odnosi-sa-inostranstvom/platni-bilans; BPM6 quarterly EUR data, page updated 19-Nov-2026. BPM6 (2010–2026) official download link resolves to https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/statistika/bop_sep_2026.zip.
- Web reader rejects application/zip; direct byte-download failed. No ZIP bytes/hash or Q2 portfolio asset/liability legs captured. Filename is not proof of coverage. MNE remains BLOCKED / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_OFFICIAL_BPM6_DOWNLOAD_ROUTE_FINGERPRINT_CONTINUATION250_20261126.md (commit 0026acf7352ff6711b31b292fe2ab41963aad04c). Matrix note/evidence_ref updated, no gate promotion. Reopen only with supported official byte retrieval or distinct CBCG endpoint.

## Continuation 251 — ALB Albania official legacy USD archive Q2 eligibility adjudication (2026-11-26)
- Re-read current Ledger, Queue, Registry, matrix, Library Mother File 1–53, C250 and ALB C139/C237/C238. Skipped PASS work, repeated EUR extraction, legacy Main-data route, C238 methodology PDF, IMF query and cohort rebuild.
- New BoA official archive navigation lists USD quarterly BOP and Financial Account series. The legacy USD BOP selector ends Q4-2013; its 11-Sep-2017 note is a historical 2013 revision, not Q2-2026. New-format USD Financial Account page shows portfolio A/L taxonomy but no Q2-2026 values and same 2017 revision note. Not an eligible Q2 bridge.
- Reuse C237 EURm legs +156.25 / +124.70. General flow average-rate convention PASS only; Q2-specific USD aggregation and same-vintage unresolved. ALB remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_LEGACY_USD_ARCHIVE_Q2_ELIGIBILITY_AND_VINTAGE_BOUNDARY_CONTINUATION251_20261126.md (commit 9835344450ed796d63bbaedbf633fb3bcc531296). Matrix note/evidence_ref updated without gate promotion.