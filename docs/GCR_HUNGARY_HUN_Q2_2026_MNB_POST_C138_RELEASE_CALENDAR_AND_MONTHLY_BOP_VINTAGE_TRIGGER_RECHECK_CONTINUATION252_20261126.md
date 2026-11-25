# GCR Continuation 252 — Hungary (HUN) MNB post-C138 release-calendar / monthly-BOP vintage trigger check
Date: 2026-11-26 (Asia/Kolkata)
Decision: A fresh official MNB release-calendar and statistics-homepage check confirms that the latest country-specific BOP/IIP release remains Q2-2026 dated 25-Sep-2026. MNB's 13-Nov-2026 monthly balance-of-payments time-series release covers September 2026, but the available official calendar/homepage does not expose portfolio-investment monthly asset/liability rows or a Q2-2026 revision vintage identifier. C138's monthly-portfolio-flow unavailability boundary remains intact; no monthly portfolio values or FX aggregation were invented. HUN remains PARTIAL / NOT PASS; asset/liability comparison NOT_DONE; same-vintage NOT_ESTABLISHED; aggregate NOT_AUTHORIZED.

## 1. Mandatory continuity and selection preflight
- Re-fetched current default-branch Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, fixed 63-country matrix and C251 report.
- Re-read Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md` (curated continuity record, not verbatim transcript).
- Reopened HUN C138 report in full, including C139 addendum. Reused the accepted national Q2 separate legs, methodology and revision-policy findings; did not repeat PDF extraction, IMF panel reads, monthly-data page test, or monthly portfolio route already closed in C139.
- HUN remains a useful PARTIAL task because C138 named an exact unmet gate: monthly currency-specific portfolio transaction inputs and same-vintage evidence. This continuation checks only for genuinely new official releases since C138.

## 2. New official MNB release-calendar evidence
- Official MNB statistics release calendar: https://statisztika.mnb.hu/en/publication-calendar
- Calendar states statistical press releases and time series are published/updated at 08:30 on release day.
- The current indexed 2026 calendar lists `Monthly balance of payments` on 13-Nov-2026 for reference period September 2026.
- The same calendar's currently indexed items include November/December releases, but no Q3-2026 quarterly BOP/IIP publication was identified in the retrieved calendar content during this bounded check. This is a retrieval-boundary statement, not proof that no later update could occur.

## 3. Official MNB statistics homepage status
- Official MNB Statistics homepage: https://statisztika.mnb.hu/en
- Homepage shows Balance of payments and related statistics last updated 25-Sep-2026, reference period Q2 2026.
- Homepage separately lists the 13-Nov-2026 monthly balance-of-payments time-series release for September 2026.
- The visible homepage/calendar data do not expose monthly portfolio investment asset and liability transaction observations, Q2-specific retroactive portfolio revisions, or a vintage identifier linking MNB observations to the archived IMF 19-Nov-2026 panel.
- This does not contradict the C138/C139 finding that the MNB monthly-data publication does not publish monthly portfolio transaction time series. A calendar entry labelled monthly BOP is not evidence that portfolio subcomponents are present.

## 4. Reused national evidence and acceptance
| Gate | Status |
|---|---|
| MNB Q2-2026 national portfolio assets | EUR +2,104m (C138; reuse) |
| MNB Q2-2026 national portfolio liabilities | EUR +8,380m (C138; reuse) |
| MNB reported portfolio net line | EUR -6,277m (C138; preserve EUR1m displayed rounding difference) |
| MNB methodology / monthly currency conversion sequence | PASS (C138; general rule) |
| MNB revision policy / release vintage date | PASS (C138; general policy) |
| New official 13-Nov monthly BOP release | FOUND (September 2026 calendar entry) |
| Monthly portfolio asset/liability values from new release | NOT_EXPOSED / NOT_CAPTURED |
| Q2-specific monthly HUF portfolio legs needed for MNB conversion sequence | NOT_AVAILABLE in inspected official monthly publication route (C139) |
| Q2 MNB observation-specific revision ID / IMF 19-Nov source-vintage match | NOT_ESTABLISHED |
| Cross-currency reconciliation | NOT_DONE |
| HUN national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Duplicate prevention and next trigger
- Do not repeat C138's quarterly PDF extraction, methodology parsing, archived IMF row extraction, or C139 monthly-data page check.
- Do not treat the 13-Nov monthly BOP calendar label as proof of monthly portfolio dual-leg publication; no such values were exposed in this check.
- Reopen HUN only when MNB publishes a distinct monthly portfolio A/L transaction dataset, a new Q2 revision/vintage artifact, or a Q3-2026 quarterly BOP/IIP report with portfolio A/L and revision metadata. On release, preserve the exact source artifact, publication time, revision label and any monthly inputs before recalculating.
- Until then retain HUN PARTIAL / NOT PASS and advance to another fixed-cohort member after complete report-history preflight. No IMF re-query, no cohort rebuild, no quarterly FX shortcut.

## 6. Protected invariants
₹0; official/free sources only; no external contact; no IMF re-query; no cohort rebuild; no synthetic monthly splits; no quarterly FX shortcut; no net-to-leg back-solving; no stock-as-flow; no unsupported FX/sign/scale conversion; UNKNOWN never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No merge, workflow dispatch or production integration.