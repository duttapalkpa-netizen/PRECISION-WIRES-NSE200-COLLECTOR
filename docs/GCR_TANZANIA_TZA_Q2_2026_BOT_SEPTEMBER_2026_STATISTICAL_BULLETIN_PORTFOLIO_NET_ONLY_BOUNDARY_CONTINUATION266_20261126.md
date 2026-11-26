# GCR Continuation 266 — Tanzania (TZA) Q2-2026 Bank of Tanzania September Statistical Bulletin: portfolio net-only boundary
Date: 2026-11-26

## Preflight and selection
- Re-read the current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry and immutable 63-country national-validation matrix; reviewed the Library Mother File continuation summary and the TZA source-boundary row.
- Skipped prior PASS work and closed routes. TZA was selected as an unfinished rank-1 national validation member with archived IMF Q2 asset/liability rows present, but no separate national portfolio legs admitted in the matrix.
- No IMF query, cohort rebuild, workflow dispatch, paid service, or production change.

## Official source inspected
- Bank of Tanzania, Statistical Bulletin for the quarter ending September 2026, Vol. IV No. 3:
  https://www.bot.go.tz/Publications/Regular/Quarterly%20statistical%20Bulletin/en/2026110418292086.pdf
- The bulletin cover identifies the issuing authority and reporting issue (PDF text lines 0–8); Table 6.1 is titled Quarterly Balance of Payments, in USD millions, with quarterly columns Dec-2024 through Sep-2026 (lines 1771–1778).
- In Table 6.1 the Q2-2026 (Jun-26) Portfolio investment entry is -14.0 USD million. The table gives this as one net portfolio-investment line only (lines 1822–1827). It does not split portfolio investment into net acquisition of financial assets and net incurrence of liabilities. The adjacent Assets/Liabilities subrows at lines 1828 and 1835 are nested under Other investment, not Portfolio investment; they must not be re-labelled as portfolio legs.
- Therefore the -14.0 USDm value is a national-source net-only observation, not either of the required dual legs. No asset/liability inference or back-solving is valid.

## Acceptance
- Official Q2 portfolio net-only value: CAPTURED from Table 6.1, -USD14.0m.
- Separate portfolio asset leg: NOT_CAPTURED.
- Separate portfolio liability leg: NOT_CAPTURED.
- National-vs-IMF asset/liability numeric comparison: NOT_PERFORMED.
- Unit and period: USD million; quarter ending June 2026.
- Source issue: September 2026 Statistical Bulletin, Vol. IV No.3. The opened source does not provide a Q2-specific portfolio-leg vintage/revision identifier; vintage remains UNKNOWN.
- TZA remains SOURCE_FOUND / PARTIAL / NOT PASS; full_pass=NO; aggregate_admission=NOT_AUTHORIZED. No gate promotion.
- Do not substitute the net value for either leg; do not use the Other Investment Assets/Liabilities subrows as Portfolio Investment legs.

## Reopen condition / next action
Reopen TZA only if a distinct official Bank of Tanzania detailed BOP table/export provides Q2-2026 portfolio net acquisition of financial assets and net incurrence of liabilities separately, with source-period, unit, sign and revision/vintage metadata. Preserve the current net-only capture as contextual evidence; do not repeat this bulletin extraction.

## Invariants
₹0; free official sources only; no IMF re-query/cohort rebuild; no annual/H1/net/IIP substitution for missing transaction legs; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; no merge or production integration without explicit approval.
