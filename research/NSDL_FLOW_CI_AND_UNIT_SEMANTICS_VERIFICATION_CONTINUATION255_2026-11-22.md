# NSDL Flow CI and Unit Semantics Verification — Continuation 255

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## 1. Continuity and CI status
- Re-read Master Continuity Ledger blob `ebca87b258af87f7929f2acc5b5ffa71bf774136` and C254 report blob `58e4d610943ccf3936df87fe590a949c50b2df09`.
- Run #388 / ID `44998007760`, head `77ffe26afcc9afd3ede9fab0aea07816868abb6c`: job `prospective-audit` ID `137133127591` remains IN_PROGRESS. Steps 1–14 completed successfully; step 15 corrected-label walk-forward is IN_PROGRESS; steps 16 onward are pending.
- Run #389 / ID `44998017821`, head `71e7102acd3e647263e29b5f806e596e048096b8`: still PENDING with no job available at inspection time.
- No code changes were made while Run #388 was active.

## 2. Official NSDL unit semantics
- Official NSDL DII report page: https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=L
- The official page labels separate fields `Net Investment (Rs. Crore)` and `Net Investment US ($) million`, with a USD/INR conversion field. This confirms that the official DII table distinguishes INR crore from USD million.
- The collector parser selects a `net investment` column while excluding `usd`, `million`, and `us mn`; this is consistent with selecting the INR-crore field when the official page uses those exact labels.
- This does not yet prove every historical page uses identical headers. Add a strict row-level schema assertion only after inspecting the exact fetched HTML for the relevant NSDL pages.
- The page distinguishes provisional exchange data based on trading-member information on T day from confirmed DII trades compiled from custodian reports to depositories for trades conducted on and up to previous trading days. Preserve this temporal distinction downstream.

## 3. Remaining evidence gaps
- The exact 2026-07-17 DII page/table schema has not been inspected; this remains an unresolved archive retrieval/schema gap.
- C254's measured 102/103 DII-vs-FPI date alignment remains the baseline; no missing value has been inferred.
- `OBSERVED_AT_UTC` is retrieval time, not the trading/reporting date.
- USD/INR and the Macro-Geo P0 hard gate remain BLOCKED.

## 4. Status
- Official NSDL DII unit semantics: VERIFIED at public report-page level (INR crore and USD million are separate).
- Collector row-level mapping across all historical pages: NOT YET VERIFIED.
- C254 FPI date clipping: CODED; CI PENDING.
- C254 tests: COMMITTED; Run #389 PENDING.
- Run #388 steps 1–14: step-level SUCCESS only; step 15 remains IN_PROGRESS.
- No claim of full workflow PASS or release approval.

## 5. Next exact actions
1. Wait for Runs #388 and #389; inspect the relevant test step, later audit steps, and artifacts.
2. Inspect the exact NSDL DII page for 2026-07-17 via the official form/archive; do not assume it was a holiday or fabricate a row.
3. Add strict parser assertions only if observed official HTML supports a stable, unambiguous mapping.
4. Verify a fresh artifact's FPI dates all fall within 2026-06-23..2026-11-20 and preserve the 2026-07-17 DII gap if still unresolved.
5. Keep the overall Macro-Geo hard gate blocked until all required independent gates pass.

## Guardrails
Audit branch only; ₹0 spend; official/free sources only; no synthetic rows, inferred dates, mirrors, paid APIs, or gate relaxation. UNKNOWN/BLOCKED never PASS. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, and Engines A–E unchanged.