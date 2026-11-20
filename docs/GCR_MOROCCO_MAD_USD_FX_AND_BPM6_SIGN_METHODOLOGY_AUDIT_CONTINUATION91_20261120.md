# Morocco MAR Q2-2026 — Official FX and BPM6 Sign-Methodology Audit
Date: 2026-11-20
Status: BPM6 sign/recording-method review PASS (bounded); MAD/USD flow-conversion convention NOT_ESTABLISHED; numeric comparison NOT_DONE; MAR PARTIAL / NOT PASS

## 1. Preflight and task selection
- Re-fetched Master Continuity Ledger, GCR Master Priority Queue, Morocco Continuation 87/88 report, V11.4 Continuation 89/90 reports, and nightly backtest review.
- PASS work was not repeated. V11.4 implementation remains NOT_AUTHORIZED; no implementation was started.
- Selected the open Morocco Continuation 87 task: official Q2 MAD/USD flow-conversion convention and BPM6 sign/mapping methodology.
- Reused existing IMF artifact 14505862034 / run 44474218174 and corrected MAR exact rows from Continuation 88; no new IMF request or cohort rebuild.

## 2. Official Office des Changes / IMF methodology findings
- IMF SDDS DQAF Morocco Balance of Payments metadata says the Exchange Office is responsible for compiling BOP statistics and the framework is BPM6. It explicitly states that the financial-account headings are “net acquisitions of financial assets” and “net incurrence of liabilities”, replacing credits/debits; financial-account transactions are recorded net. It also states BOP recording is primarily when settlement takes place (or customs clearance for merchandise / actual payment for other operations), and quarterly BOP is disseminated three months after reference period.
- Official Office des Changes 2019 annual BOP/IIP report's methodology section likewise says financial transactions are recorded as net flows of assets and liabilities (“Acquisition nette d’avoirs” and “Accroissement net des engagements”), not credit/debit. Its account-level discussion describes net acquisitions of assets and net increases in liabilities separately.
- IMF BPM6 Compilation Guide states financial-account increases in assets and liabilities are positive and decreases are negative; the financial-account balance is net acquisition of assets minus net incurrence of liabilities.
- Decision: the Office des Changes Q2 PDF's +4,848 MDH net acquisition of assets and +36,933 MDH net incurrence of liabilities are directionally consistent with BPM6 positive-increase semantics. The Ministry DSBB summary's negative liability display is an alternate signed summary display and must not be treated as the source's native liability-flow sign or a separate observation. Do not sign-flip either detailed source leg.

## 3. Official Bank Al-Maghrib daily USD/MAD reference-rate methodology
- Official BAM 2024 PDF “Méthodologie de calcul des cours de change de référence du Dirham” states:
  * Daily reference rates are calculated from interbank transactions by market-maker banks.
  * USD/MAD reference rate, when market thresholds are met, is a volume-weighted average of USD/MAD interbank transaction rates on the electronic trading platform between 08:30 and 15:30.
  * If those thresholds are not met, BAM samples firm interbank bid/ask quotes every five minutes from 08:30 to 15:30, calculates midpoint using median bid and median ask, then averages those midpoints.
  * Reference rates are published daily at 16:15; same-day republication may occur for calculation/publication errors.
  * Critically, the methodology states reference rates are mainly for revaluation of foreign-currency assets/liabilities and are not intended to be used directly or indirectly as a reference when executing FX transactions.
- BAM developer portal lists a “Cours de change - Version1” REST API, but this bounded read-only source inspection did not establish its historical query contract, raw daily 2026-Q2 observations, revision history, bulk export rights or a quarterly average.
- Therefore the daily BAM reference-rate methodology is a real official rate methodology, but it does NOT itself specify the exchange-rate convention used by Office des Changes to translate Q2 portfolio transaction flows into USD. A simple arithmetic mean of daily BAM rates, quarter-end rate, or an unverified third-party history would be an unsupported conversion. No conversion was calculated.

## 4. Crosswalk to existing MAR/IMF rows
- National Q2 source remains preliminary, million MAD: assets +4,848; liabilities +36,933; balance -32,085.
- Correct existing IMF MAR Q2 rows remain those independently verified in Continuation 88:
  * A_NFA_T +523,948,820.8007525 USD
  * L_NIL_T +3,991,543,275.295832 USD
  * both ACTION=R, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
- Both legs have positive direction under the native BPM6 labels. Directional consistency is supported; numerical MAD/USD comparison is NOT_DONE because no official flow-conversion convention, exact historical raw BAM Q2 series and matching observation-vintage bridge were established.
- IMF ACTION=R does not alone provide observation-specific revision timestamp. Same-vintage remains NOT_ESTABLISHED.
- Do not infer MAD/USD quarterly mean from monthly or quarter-end data; do not use a reference revaluation rate as a flow conversion rule absent explicit Office des Changes methodology.

## 5. Acceptance
| Gate | Status |
|---|---|
| Morocco BPM6 framework and financial-account labels | PASS |
| Native sign semantics (increase positive, decrease negative) | PASS |
| Office des Changes flow recording timing (settlement basis) | PASS |
| BAM official daily USD/MAD reference-rate methodology located | PASS |
| BAM historical Q2-2026 daily raw series and revision metadata captured | NOT_CAPTURED |
| Office des Changes Q2 flow FX conversion convention identified | NOT_ESTABLISHED |
| Numeric MAD→USD conversion | NOT_DONE |
| Separate-leg magnitude comparison | NOT_DONE |
| Observation-specific same-vintage bridge | NOT_ESTABLISHED |
| MAR full national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |
| Production integration | NOT_AUTHORIZED |

## 6. Next exact action
- Search the Office des Changes BOP methodology appendices / current methodological notes for explicit currency conversion rules for transactions recorded in foreign currencies (daily transaction-date rate, monthly average, quarterly average, or other documented rule).
- If the rule points to BAM daily rates, obtain the official Q2 daily USD/MAD raw series via supported public API/export and capture unchanged bytes, URL, retrieval UTC, MIME, byte count, SHA-256, revision/vintage metadata before calculation.
- If no official flow conversion rule and observation-vintage bridge can be established, retain MAR PARTIAL / NOT PASS and advance to next fixed-cohort country. Do not manufacture a quarterly average or use the BAM revaluation reference series as an unapproved flow conversion.
- No new IMF query, no cohort rebuild, no unsupported FX conversion, no netting and no production changes.

## 7. Official source register
1. IMF SDDS DQAF Morocco BOP metadata: https://dsbb.imf.org/sdds/dqaf-base/country/MAR/category/BOP00
2. Office des Changes, Rapport annuel Balance des paiements et PEG 2019, methodology section: https://www.oc.gov.ma/sites/default/files/2020-06/Rapport%20annuel%20BP%20%20PEG%202019%20-%20VO%20-.pdf
3. Bank Al-Maghrib, Méthodologie de calcul des cours de change de référence du Dirham (2024): https://www.bkam.ma/content/download/797654/8820941/M%C3%A9thodologie%20de%20calcul%20des%20cours%20de%20change%20de%20r%C3%A9f%C3%A9rence%20du%20Dirham_2024.pdf
4. Bank Al-Maghrib developer API portal (lists Cours de change Version1): https://apihelpdesk.centralbankofmorocco.ma/apis
5. IMF BPM6 Compilation Guide: https://www.imf.org/external/pubs/ft/bop/2014/pdf/guide.pdf

## 8. Protected invariants
Fixed 63-country IMF Q2-2026 cohort unchanged. No new IMF request, no production change, no synthetic data, fabricated timestamps, unsupported FX, forward-fill, guessed mapping or paid API. ₹0. UNKNOWN is never PASS.


## Continuation 91 — Final verification marker
- This is the bounded Morocco official FX and BPM6 methodology audit for Continuation 91. The report's status remains: sign/recording methodology review PASS; official BAM reference-rate method identified; Q2 flow FX conversion convention NOT_ESTABLISHED; no numeric conversion; MAR PARTIAL / NOT PASS; aggregate and production NOT_AUTHORIZED.
