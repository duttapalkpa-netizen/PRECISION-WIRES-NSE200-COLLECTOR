# NSDL Archive Date Lookup and CI Continuity — Continuation 256

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## 1. Continuity checked
Re-fetched `research/GITHUB_MASTER_CONTINUITY_LEDGER.md` (blob `bbdbb64f4e0c357ae339ceca680b8f22ba63c015`) and C255 report (blob `7c70f2cc215df850640b00baf31f207bbed59af9`). C254 date clipping and three tests are already committed; no duplicate implementation was attempted.

## 2. CI state (latest inspection)
- Run #388 / ID `44998007760`: job completed `cancelled`. Step 5 regression suite SUCCESS; step 15 corrected-label walk-forward SUCCESS. Step 16 collection was cancelled; later steps skipped. This is not a full workflow PASS.
- Run #389 / ID `44998017821`: `in_progress`; step 5 regression suite SUCCESS; step 6 NSE history acquisition IN_PROGRESS; later steps pending. No artifact-based C254 date-window validation available yet.
- Run #315 / ID `44998007758`: `in_progress`; steps 5–7 SUCCESS; step 8 P0 market/media collection IN_PROGRESS; later steps pending.
- No source edits made while either relevant workflow remained active.

## 3. Official NSDL archive lookup
- Opened official NSDL FPI reports listing: `https://pilot.fpi.nsdl.co.in/Reports/ReportsListing.aspx`.
- The page exposes an “Archive DII” navigation item, but it resolves to `https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=A`, a date-input form with “Please Select Date” / “No Data Found” when no date is submitted.
- The public inspection path did not submit the date form or expose its form POST contract. Therefore the exact 2026-07-17 DII row/schema remains NOT VERIFIED; no holiday assumption, missing-value imputation, guessed POST endpoint, or code change is justified.
- The official live DII report page (Rep=L) continues to expose distinct INR-crore and USD-million fields and explains provisional T-day exchange data versus confirmed prior-day custodian/depository data. This is page-level semantics, not proof of the missing date row.

## 4. Status and exclusions
- C254 date-window clipping: CODED; step 5 SUCCESS in #388/#389, but fresh artifact verification PENDING.
- C254 tests: step 5 SUCCESS in #388 and #389.
- 2026-07-17 DII row and row-level parser mapping: UNKNOWN / NOT VERIFIED.
- USD/INR and Macro-Geo P0 release gate: BLOCKED as recorded in C252/C255.
- Excluded: guessed NSDL POST endpoint, inferred trading holiday, synthetic DII row, third-party mirrors, paid APIs, gate relaxation.
- Protected invariants remain unchanged; production branch untouched.

## 5. Exact next actions
1. Wait for Run #389 and #315; inspect final steps, artifacts, and exact outputs. Do not edit code during active runs.
2. From #389 artifact, verify every FPI date lies in 2026-06-23..2026-11-20 and explicitly retain/report the 2026-07-17 DII gap if still absent.
3. Inspect NSDL form HTML/JavaScript or browser-visible date submission contract from official assets before any request implementation; use only a directly evidenced official route.
4. If official row is retrievable, inspect exact HTML headers and row values before asserting parser mapping; otherwise keep the date unresolved.
5. Keep USD/INR and overall Macro-Geo hard gate BLOCKED until independently satisfied.

## Guardrails
₹0 spend; official/free sources only; no fabricated data/timestamps; UNKNOWN/BLOCKED never PASS. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged.
