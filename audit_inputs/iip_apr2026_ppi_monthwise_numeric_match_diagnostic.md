# April 2026 NIC-2025 PPI-series value reconciliation: May release diagnostic

Status: NUMERIC MATCH 23/23; BASE-YEAR LABEL CONFLICT; NOT ACCEPTED AS COMPARABLE VINTAGE

## Scope

Compared the 23 April 2026 NIC-10 through NIC-32 index values in the existing first-release ledger's later-vintage field against the April-2026 column in MoSPI's 29 June 2026 May-IIP press release, Statement "INDEX OF INDUSTRIAL PRODUCTION - MONTHWISE".

Official source:
https://www.pib.gov.in/newsite/archiveContent.aspx?lang=2&reg=48&relid=290616

Relevant source lines:
- Lines 8-10 and 27-28: MoSPI says Output PPI replaces WPI and the revised PPI-based IIP series supersedes the 1 June 2026 WPI-based series.
- Lines 144-146: monthwise table title; explicitly labels its base as 2011-12=100 and column labels NIC 2025, April 2026.
- Lines 147-169: NIC 10-32 monthly observations, including April 2026.
- Lines 55 and 222-224: detailed data available through e-Sankhyiki IIP portal.

## Result

- Ledger rows: 23 (NIC 10-32).
- Official release April-2026 monthwise rows: 23 (NIC 10-32).
- Exact numeric matches against the ledger's first later-vintage value: 23/23.
- Numeric mismatches: 0.
- Important qualification: the source table explicitly labels the series "Base: 2011-12=100", whereas the target ledger is labelled base_year=2022-23. Despite exact numeric equality, this is a base-year/series-label conflict. No conversion methodology or explicit statement in this source was found that authorizes treating those values as the 2022-23=100 series.
- Therefore this is recorded as a diagnostic corroboration only. It does NOT satisfy the same-base-year comparable vintage acceptance criterion and must NOT clear LATER_VINTAGE_SOURCE_CROSSCHECK_PENDING.
- Do not overwrite the historical first-release values, later vintage values, or revision deltas.
- Do not infer that equality proves series equivalence.
- Keep raw PDF SHA-256 pending; this source was inspected as a PIB HTML release page, not as downloaded raw PDF bytes.

## Disposition

NUMERIC_MATCH_23_OF_23; BASE_YEAR_LABEL_CONFLICT_2011_12_VS_2022_23; COMPARABILITY_NOT_ESTABLISHED; LATER_VINTAGE_SOURCE_CROSSCHECK_PENDING; RAW_PDF_SHA256_PENDING.

No production selector, score, diagnostic, source row, or hard-gate status changed.
