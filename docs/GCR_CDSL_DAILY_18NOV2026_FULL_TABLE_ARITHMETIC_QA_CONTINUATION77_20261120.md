# GCR CDSL Daily FPI — 18-Nov-2026 Full-Table Arithmetic QA (Continuation 77)
Date: 2026-11-20 (Asia/Kolkata)
Scope: read-only independent parsing and arithmetic validation of the already archived official CDSL eServices daily HTML. No new source capture, no production ingestion, no matched-date NSDL/CDSL claim.

## Continuity preflight and excluded repeats
- Re-fetched current Continuity & Acceptance Ledger: blob SHA `ceff27c81ef9c645d9acb06aa92cf584ed882430`.
- Re-fetched current GCR Master Priority Queue: blob SHA `ac3fc12350e7e6bd911ca26a77941ea475aca7e0`.
- Reopened Continuation 76 NSDL form-contract report and CDSL sector arithmetic report; the prior sector 192/192 subtotal arithmetic was not repeated.
- Reused existing artifact 14527092174 / run 44519322726; no new workflow run, no source re-download request, no IMF query/cohort rebuild.
- BSE and NSE TRI routes are already rights-screened and NOT ADMITTED; no repeat rights review. Interactive NSDL postback remains unsupported in this session and was not guessed.

## Artifact provenance
- ZIP: `gcr-india-fpi-raw-pages-3.zip`, 1,067,099 uncompressed bytes across 10 members.
- Artifact ID: `14527092174`; workflow run: `44519322726`.
- Independently recomputed ZIP SHA-256: `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd`, exact match to recorded digest.
- Parsed member: `cdsl_daily_latest_eservices.html`; title “FII Daily Data - Eservices”.
- CDSL daily table reporting date: `18-NOV-2026`; 28 HTML rows including header, seven asset/route category subtotals, grand total and explanatory note. No modification of source bytes.

## Arithmetic results
- Detailed investment-route/scheme rows checked: 17/17 satisfy gross purchases minus gross sales equals net investment at the displayed INR-crore precision.
- Category subtotals checked: 7/7 satisfy the same identity exactly at displayed INR-crore precision:
  - Equity: 26,444.96 − 15,179.28 = 11,265.68
  - Debt-General Limit: 1,049.90 − 371.45 = 678.45
  - Debt-VRR: 0.00 − 106.34 = −106.34
  - Debt-FAR: 1,805.91 − 1,094.77 = 711.14
  - Hybrid: 40.87 − 41.89 = −1.02
  - Mutual Funds: 2.72 − 3.73 = −1.01
  - AIFs: 0.00 − 0.00 = 0.00
- Sum of the seven category subtotals exactly reproduces published totals: purchases INR 29,344.36 crore; sales INR 16,797.46 crore; net INR 12,546.90 crore.
- Grand-total identity: 29,344.36 − 16,797.46 = 12,546.90 crore; residual 0.00.
- Sum of displayed category USD-million subtotals is 1,340.9063 versus published total 1,340.906; residual +0.0003 USD million, consistent with aggregation of displayed rounded component values. Preserve the published total; do not adjust component values.
- Published conversion rate is INR 93.5703 per USD. No independent currency transformation is used to overwrite the source USD figures.

## Source semantics and comparison boundary
- CDSL page note says the data are compiled from reports submitted to depositories by custodians on 18-Nov-2026 and represent FPI trades conducted on and up to previous trading day(s). Retain this as the source's stated reporting/trade-date semantics.
- In the same archived ZIP, NSDL Latest is headed 19-Nov-2026 and explains that exchange-member provisional T-day trades differ from custodian-confirmed trades for previous trading day(s). Therefore the 19-Nov NSDL page and 18-Nov CDSL page are not a matched-date provider comparison. Provider variance remains NOT_COMPUTABLE, not zero.
- Derivatives table is a separate market dimension and was not added to cash-market totals.
- Fortnightly sector FPI remains a separate frequency/period class; no daily interpolation or daily sector allocation is made.

## Acceptance matrix
| Gate | Status |
|---|---|
| Existing ZIP digest independently verified | PASS |
| CDSL daily cash table extracted from exact archived HTML | PASS |
| Detailed route/scheme INR arithmetic | PASS (17/17) |
| Category subtotal INR arithmetic | PASS (7/7) |
| Published grand-total INR identity | PASS |
| Displayed USD subtotal aggregation | PASS with +0.0003 USDm rounding residual |
| CDSL/NSDL matched-date provider comparison | NOT_DONE |
| NSDL Archive date-specific postback/output | NOT_DONE |
| Historical daily coverage/completeness | UNKNOWN |
| Sector-flow predictive join/backtest | BLOCKED / NOT_RUN |
| Production ingestion or scoring admission | BLOCKED / NOT_AUTHORIZED |

## Next exact action
- Do not repeat the already-PASS CDSL arithmetic or raw capture.
- Next executable source task: inspect the archived CDSL fortnightly landing/archive HTML's exact date-selection controls and response freshness boundary, without guessing undocumented postback payloads; alternatively, if a supported interactive browser becomes available, execute one fresh public selection and capture the response bytes/metadata/hash.
- Keep NSDL archive rows NOT_DONE until a fresh-state public UI interaction yields an actual response. If no supported browser route exists, preserve the blocker and select a distinct official source task.
- No daily/fortnightly conflation, no AUC-stock/flow conflation, no date inference, no silent rounding adjustment, no production change.

## Protected invariants
₹0; official/free sources only; no synthetic data, no fabricated timestamps, no paid API, no external contact. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2 and fixed 63-country Q2-2026 IMF cohort unchanged. UNKNOWN is never PASS.
