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
