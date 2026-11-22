# NSDL DII Holiday Root-Cause and Remaining Gap — Continuation 259

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## 1. Continuity and completed-work exclusions
Re-fetched `research/GITHUB_MASTER_CONTINUITY_LEDGER.md`, C258 report, `pipeline/macro_geo_nsdl_flows.py`, and `qa/test_macro_geo_nsdl_flows.py` before work. C254 clipping was already end-to-end verified in Run #315's artifact; it was not repeated. Runs #388/#389 were completed CANCELLED, and Run #315 was completed FAILURE at its strict hard gate. No production branch or protected selector invariant was changed.

## 2. Artifact-level root cause of the seven NSDL DII errors
Downloaded and re-inspected artifact `14745631182` (Run #315). Its `outputs/macro_geo/nsdl_fpi_dii_collection.json` records seven DII failures:
- 2026-06-26
- 2026-07-17
- 2026-08-26
- 2026-09-14
- 2026-10-02
- 2026-10-20
- 2026-11-10

Official NSE Capital Market trading-holiday circular `NSE/CMTR/71775`, dated 2025-12-12, lists six of these dates as 2026 trading holidays:
- 2026-06-26 — Muharram
- 2026-08-26 — Id-E-Milad
- 2026-09-14 — Ganesh Chaturthi
- 2026-10-02 — Mahatma Gandhi Jayanti
- 2026-10-20 — Dussehra
- 2026-11-10 — Diwali-Balipratipada

Official source: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf

Therefore six of the seven reported “schema not recognized” failures were not parser/schema drift; they were attempts to request DII reports on official non-trading days. This classification is independently supported by the NSE circular. The remaining date, 2026-07-17, is not listed in that circular and remains an unresolved NSDL archive/schema/data gap. Do not classify it as a holiday or fabricate a DII row.

The official NSDL Archive DII form is discoverable from its Reports Listing, but the publicly rendered page only shows the date input and “Please Select Date” / “No Data Found” when no date is submitted. It does not expose the exact 2026-07-17 response in the available browser evidence. No guessed POST contract or parser variant was introduced.

## 3. Bounded code/test repair
Collector `pipeline/macro_geo_nsdl_flows.py` now contains a narrowly scoped 2026 NSE cash-market holiday map with the official circular URL as provenance. The DII date loop skips only those six declared holidays and records them under `non_trading_holidays` rather than emitting false schema errors. It does not skip 2026-07-17.
Regression test in `qa/test_macro_geo_nsdl_flows.py` asserts all six date/name mappings and explicitly asserts 2026-07-17 is not classified as a holiday.

Commits:
- Collector code: `91caabc9b11e8cd22d592f50f1121a99b3859c3a`
- Regression test: `82c0e6fe31ec9b19529f35e934b807880089f694`

Status at report creation:
- CODED: yes
- Regression test committed: yes
- CI: IN_PROGRESS/PENDING; not yet PASS
- July 17: UNKNOWN/BLOCKED
- Macro-Geo P0 gate: still BLOCKED pending USD/INR and matured event windows
- NSDL archive coverage: previous C258 artifact still showed 102 DII dates vs 103 FPI dates (99.03%); do not promote this to complete coverage.

## 4. Exclusions / guardrails
- No parser broadening, table fallback, guessed endpoint, third-party mirror, paid API, or synthetic DII value.
- No holiday inference from weekdays; only the six exact dates named by the official NSE circular are skipped.
- No change to the >=60 distinct dates / >=90 calendar-day coverage threshold.
- No production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, or Engines A–E change.
- No claim of overall Macro-Geo PASS.

## 5. Exact next actions
1. Inspect CI Runs #390 (ID `45000517346`), #391 (ID `45000520528`), and Macro-Geo Run #316 (ID `45000517341`) after completion; verify the new test step and actual collector output before marking PASS.
2. Verify the six dates appear as `non_trading_holidays` and no longer as DII parser errors in a fresh artifact.
3. Investigate only 2026-07-17 through exact official NSDL evidence; retain UNKNOWN/BLOCKED if the date response/table cannot be retrieved.
4. Keep USD/INR official archive and matured event-window blockers unchanged; rerun the strict hard gate only after material source evidence changes.
5. Preserve all evidence in this ledger; skip the already validated C254 clipping work.
