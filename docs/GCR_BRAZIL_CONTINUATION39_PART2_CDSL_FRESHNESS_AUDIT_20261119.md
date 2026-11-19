# GCR CDSL Archive Freshness and Brazil Continuation 39 Part-2 — 2026-11-19

## Scope and decision
Research-only, read-only evidence update for Global Capital Rotation & Relative-Attraction Overlay and Brazil Reconstruction. No production code, weights, selector, ranking score, pressure-fade, CORE-672, or Engines A-E changed. ₹0; official sources only. UNKNOWN is not PASS.

## Progress Log — evidence reused, not repeated
- Brazil Registration lifecycle remains 40/40 PASS (run 44465947951; artifact 14502380926; ZIP SHA-256 2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41).
- Brazil PA identity remains confirmed: IMF:BR_BOP_BP6(1.0) -> Dataflow IMF:BOP6(1.0), Provider IMF:BR1.
- BCB payload still declares IMF:BOP_BPM6(1.0); no authoritative Brazil-specific crosswalk/correction accepted.
- PA transaction ID 2 fusion-json and sdmx-json requests both returned HTTP 500; do not repeat equivalent requests.
- Continuation 76 added read-only structure GETs for PA, BOP6, BOP_BPM6 and ECOFIN_DSD. Script commit c1365fbbccbd773d7ad61dd1fdfc42138c4af98e; trigger commit 786ac4a64ea8ab412c41907c0e1afe1e46d8dcb5. Run/artifact still NOT VERIFIED.
- GCR CDSL replay run 44521501249 SUCCESS; artifact 14527843295; ZIP SHA-256 2c8952476f58637c0f346e695793d2b8c8fd170dac551386ace1e37e0e7aea99. Same archive URL yielded materially different HTTP-200 bodies in three captures; archive completeness remains BLOCKED.

## New direct official CDSL page observation
Source URL: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
Method: direct read-only page inspection; no form submission, POST, credentials, or undocumented endpoint.
Observed page heading: “Daily Trends in FII / FPI Investments upto 30-Sep-2026”.
The visible cash-investment table contains dated rows including 01-Sep-2026 onward; the page's separate derivatives table has its own dated records. The page note states the report is compiled on the basis of reports submitted to depositories by NSE, BSE, MSEI, NCDEX and MCX on 30-Sep-2026 and constitutes FII/FPI trading/position of the previous trading day.
The page notes further distinguish provisional exchange-member T-day data from confirmed custodian/depository reports for previous trading day(s). RBI reference exchange rate is used for USD conversion, with the immediately preceding working-day reference rate used when the trading day is a bank holiday. Aggregate discrepancies may arise from rounding.
This is a current page-render observation, not a historical raw-byte archive receipt: this inspection did not capture response headers, retrieval UTC timestamp, byte count or SHA-256. Do not promote it to immutable raw-source PASS.
The visible page's heading date (30-Sep-2026) is a freshness boundary for this rendered page; it does not prove archive dataset completeness or explain the previously inconsistent GET bodies.

## Acceptance update
| Workstream | Status | Reason |
|---|---|---|
| Brazil Registration lifecycle | PASS | Reused 40/40 accepted evidence |
| Brazil PA identity | PASS | PA references BOP6 and BR1 |
| Brazil PA transaction-2 Changelog | BLOCKED | Both documented JSON serializations HTTP 500 |
| Brazil BOP6 vs BOP_BPM6 payload identity | BLOCKED | No authoritative Brazil-specific crosswalk or correction |
| Brazil public structure GET comparison | PENDING / NOT_VERIFIED | Continuation 76 workflow run/artifact not independently inspected |
| GCR CDSL replay artifact integrity | PASS | Run and ZIP digest previously verified |
| GCR CDSL archive completeness | BLOCKED | Three materially different HTTP-200 bodies; page inspection does not establish selected export semantics |
| CDSL page freshness observation | OBSERVED / NOT_RAW_VERIFIED | Direct rendered page says upto 30-Sep-2026; no raw byte receipt |
| NSDL/CDSL matched-date reconciliation | NOT_DONE | No accepted matched-date, status-qualified provider pair |
| GCR synchronized global/India panel | BLOCKED | Complete aligned source panel not accepted |
| GCR predictive event study | NOT_DONE | No accepted synchronized panel |
| Production integration | BLOCKED | Source, coverage, reconciliation and event-study gates open |

## Next highest-value bounded actions
1. Inspect the actual GitHub Actions run for trigger commit 786ac4a64ea8ab412c41907c0e1afe1e46d8dcb5, then download the artifact and independently verify ZIP and per-response hashes. Until then the four-structure comparison remains NOT_VERIFIED.
2. Obtain the raw CDSL page plus page scripts/form metadata with a reproducible GET capture that records final URL, UTC retrieval time, status, headers, bytes and SHA-256. Identify only documented selector/export semantics; do not POST or guess parameters.
3. After request semantics are documented, use an isolated GET-only selected-date capture if the official site exposes one. Validate row dates, source notes, table identity, and cash-vs-derivative separation before completeness claims.
4. For Brazil, obtain owner/provider-side export of exact PA IMF:BR_BOP_BP6(1.0) revisions/changelog and registration transaction details; no credentials/cookies. Do not infer historical chronology from Last Updated.
5. Keep BOP6/BOP_BPM6 identity blocked until an authoritative Brazil-specific structure map, crosswalk or provider correction is captured.

## Hard invariants
No synthetic data, interpolation, fabricated timestamps, guessed hashes, guessed SDMX keys, unapproved FX/sign/scale conversion, or aliases. UNKNOWN is never PASS. No production integration, macro weights, trading admission, or selector/score/diagnostic/engine changes.
