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
