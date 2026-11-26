# GCR Continuation 270 — Mexico Q2-2026 Banxico Q3-release revision / vintage recheck
Date: 2026-11-26 (Asia/Kolkata)
Country: MEX — Mexico
Period: 2026-Q2
Decision: A NEW OFFICIAL BANXICO RELEASE SHOWS A DIFFERENT Q2 PORTFOLIO-ASSET VALUE THAN THE AUGUST Q2 RELEASE. LIABILITY VALUE IS UNCHANGED. THE IMF RECEIPT PREDATES THIS NOVEMBER RELEASE; SAME-VINTAGE ALIGNMENT IS NOT ESTABLISHED. KEEP MEX PARTIAL / NOT PASS.

## 1. Continuity preflight and duplicate prevention
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and fixed 63-country Q2-2026 matrix; re-read Library Mother File and prior MEX report.
- Reused the existing IMF exact-key receipt from run 44474458684 / artifact 14505009889; no IMF GET, cohort rebuild or panel rebuild.
- C251/C252 prior work retained: 25-Aug-2026 Banxico Q2 release reported portfolio assets +USD8,937m and liabilities +USD10,561m; exact archived IMF Q2 values were +USD8,937.255098m and +USD10,561.285114m; both previously passed at whole-USDm rounding. Exact same-vintage identity was NOT_ESTABLISHED.
- New distinct official evidence inspected: Banxico Q3-2026 BOP PDF published 25-Nov-2026:
  https://www.banxico.org.mx/publicaciones-y-prensa/balanza-de-pagos/%7BFE2A999A-C9E0-98B0-F65D-01340BA453AC%7D.pdf
  Source page: https://www.banxico.org.mx/publicaciones-y-prensa/balanza-de-pagos/balanza-pagos-comercio-invers.html

## 2. Q2 values in the new Q3 publication
Banxico Q3 release, Cuadro 3, PDF page 6 / printed page 6, unit: USD millions; Q2 2026 column:
- Portfolio investment, net acquisition of financial assets: +9,480.
- Portfolio investment, net incurrence of liabilities: +10,561.
- Portfolio investment balance (A-B): -1,082.
- Internal arithmetic: 9,480 - 10,561 = -1,081; published balance is -1,082, a USD1m whole-number rounding difference. The report itself warns component sums may not equal totals because of rounding.
- Q2 asset changed by +543m compared with the 25-Aug-2026 Q2 release value +8,937m.
- Q2 liability is unchanged at +10,561m compared with the 25-Aug-2026 Q2 release.

## 3. Comparison to the existing IMF receipt
Existing IMF exact Q2 values (unchanged; receipt timestamp 19-Nov-2026):
- A_NFA_T: +USD8,937.255098m.
- L_NIL_T: +USD10,561.285114m.

New Banxico Q3-release Q2 rows versus archived IMF:
| Leg | Banxico Q3-release Q2 (USDm) | IMF existing Q2 (USDm) | IMF minus Banxico (USDm) | Result |
|---|---:|---:|---:|---|
| Portfolio assets / A_NFA_T | +9,480 | +8,937.255098 | -542.744902 | REVIEW / NOT MATCHED |
| Portfolio liabilities / L_NIL_T | +10,561 | +10,561.285114 | +0.285114 | PASS at ±0.5 whole-USDm display rounding |

The asset residual is far outside the ±0.5 USDm rounding bound. Do not widen tolerance or silently replace the IMF value. The IMF receipt date (19-Nov) precedes the new Banxico Q3 release (25-Nov), so the two are not a same-publication-vintage pair.

## 4. Revision / vintage interpretation
- The new Q3 release explicitly says it incorporates revisions to some BOP items from continuous additional information; it names profits/dividends, direct investment and services as the principal revisions this time. It also says components may be revised in future releases.
- Despite that general note, the actual Q2 portfolio asset row in this release is +9,480m, compared with +8,937m in the August Q2 release. The inspected text does not explain the portfolio-asset revision or identify an observation-specific revision record.
- Therefore a Q2 asset value change is OBSERVED; its specific cause and revision lineage are NOT_ESTABLISHED. Do not claim the PDF explicitly attributes this asset change to the stated principal revision categories.
- The IMF receipt is timestamped 19-Nov-2026 in the earlier C252 report, before the 25-Nov Banxico release. It cannot be asserted to reflect this newer Banxico Q2 value.

## 5. Acceptance result
- New official Banxico Q3 release publication date and Q2 table inspected: PASS.
- New Q2 portfolio A/L rows captured from official table: PASS (published whole-USDm values only).
- Q2 asset revision versus August release detected: PASS (change +USD543m).
- Q2 liability unchanged versus August release: PASS.
- Asset numeric comparison against existing IMF receipt: REVIEW / NOT MATCHED; residual -USD542.744902m.
- Liability numeric comparison against existing IMF receipt: PASS at ±USD0.5m.
- Observation-specific revision cause / revision ID: NOT_ESTABLISHED.
- Same-vintage Banxico↔IMF bridge: NOT_ESTABLISHED.
- MEX full national validation: PARTIAL / NOT PASS.
- Aggregate admission: NOT_AUTHORIZED.

## 6. Next exact action
Seek only an official Banxico observation-level revision history/version record or a subsequent dated source that explains the Q2 portfolio-asset value change and allows a matching IMF observation vintage. If no public versioned record exists, preserve the mismatch as a vintage-sensitive REVIEW and advance to the next eligible cohort member. Do not repeat the 25-Aug extraction, query IMF again, rebuild the cohort, or substitute IIP stocks.

## 7. Protected invariants
₹0 spend; free official sources only; no paid APIs/licences/subscriptions; no synthetic data, fabricated timestamps or hashes; no tolerance widening; no netting or imputation; UNKNOWN is neither PASS nor FAIL. CORE-672 (56×12), Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, Engines A–E and IPO-PLX V2.0 unchanged. No workflow dispatch, merge or production integration.
