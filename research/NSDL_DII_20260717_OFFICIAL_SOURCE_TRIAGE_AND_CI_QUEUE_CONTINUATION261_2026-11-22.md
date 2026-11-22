# NSDL DII 2026-07-17 Official Source Triage and CI Queue — C261

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## Continuity check
Re-fetched Master Continuity Ledger, C259 report, collector and tests. C254 date clipping remains PASS and was not repeated. C260 corrected Capital Market holiday scope is committed. No production files or protected selector invariants were changed.

## Official source findings
1. NSE Capital Market trading-holiday circular NSE/CMTR/71775 dated 2025-12-12 lists 2026 trading holidays but does not list 2026-07-17 or 2026-08-26. Official URL: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf
2. A distinct NSE Clearing Capital Market settlement-holiday circular NCL/CMPT/71904 dated 2025-12-22 does list 2026-08-26 (Id-E-Milad). This is a settlement holiday, not the NSE Capital Market trading-holiday circular. Official URL: https://nsearchives.nseindia.com/content/circulars/CMPT71904.pdf
3. NSE Debt Segment settlement circular NCL/DS/71918 also lists 2026-08-26, but is not the Capital Market trading calendar: https://nsearchives.nseindia.com/content/circulars/DS71918.pdf
4. NSDL official DII archive form is date-driven and, without a submitted date, renders “Please Select Date” / “No Data Found”; no public indexed result for the exact 2026-07-17 date was found. Official form: https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=A
5. NSDL's latest DII report page (example report dated 2026-04-16) explains that exchange provisional data is based on T-day trading-member information, while confirmed custodian/depository data reflects trades on and up to previous trading day(s). It shows separate INR-crore and USD-million columns. This establishes that DII report semantics are mixed/provisional-vs-confirmed; it does not prove a row exists for 2026-07-17. Official page: https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=L

Conclusion: 2026-07-17 is not a published NSE CM trading holiday in the official 2026 trading calendar. Since C258 archive has an FPI observation for that date but no DII row, this remains an unresolved NSDL archive retrieval/schema/data gap. No inference of zero investment, holiday, or missing table semantics is allowed. 2026-08-26 must also remain a DII query date: the official CM trading calendar does not list it as a trading holiday, although a separate CM settlement-holiday circular does list it. The collector must not skip it on settlement-holiday evidence alone.

## CI queue and current status
Corrected code:
- Collector correction commit `885528a076e98996455358ee236f1a2960a276ea`
- Regression-test correction commit `9fac7d42bd09f6b0a4d9a4c0742a36451816e0a4`
- C259 correction addendum commit `661f74b9b0b3a7734c1d8fac2e0e9874f5d0fc22`
- C260 ledger commit `e8d295df75f97914b4e832d1708b3355e9f7a696`

Latest workflow API inspection:
- Run #392 ID `45001040461`: CANCELLED on collector-only correction SHA.
- Run #393 ID `45001043441`: PENDING on corrected test SHA.
- Run #317 ID `45001040455`: PENDING on collector-only correction SHA.
- Older #390 / #316 remain IN_PROGRESS on the superseded C259 SHA and cannot validate C260.
Pending runs have no jobs exposed yet; do not claim test or artifact acceptance.

## Rejected assumptions
- Do not treat the CM settlement holiday or Debt Segment holiday as a CM trading holiday.
- Do not infer 2026-07-17 is a holiday or a zero-flow day.
- Do not create a DII row from FPI data or weekday calendars.
- Do not change parser schema, DII units, coverage threshold, or P0 gate without direct source evidence.
- No paid API, third-party mirror, synthetic data, or production changes.

## Exact next actions
1. Resolve queued/pending Runs #393 and #317; inspect jobs and logs once they start. If they remain pending, document the queue rather than treating them as PASS.
2. Run the corrected full Macro-Geo workflow on the corrected SHA when the current in-progress jobs finish; inspect the new artifact's `non_trading_holidays`, 2026-08-26 query outcome, and 2026-07-17 query outcome.
3. For 2026-07-17, obtain the exact NSDL date-submitted response using only the observed official form contract. If the public response remains unavailable, keep UNKNOWN/BLOCKED and record the exact limitation.
4. Preserve C254 PASS; maintain USD/INR and mature-event-window blockers; no hard-gate relaxation.
