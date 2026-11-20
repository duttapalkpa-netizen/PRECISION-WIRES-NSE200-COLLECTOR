# Ukraine UKR — NBU Q2-2026 BOP latest-period and publication-boundary audit (Continuation 120)
Date: 2026-11-21 (Asia/Kolkata)

## Decision
The fixed 63-country cohort includes UKR. A scoped review of the currently accessible official NBU quarterly analytical BOP publication and NBU external-sector revision notice did not locate a Q2-2026 national portfolio-investment asset/liability transaction table. The NBU analytical quarterly BOP PDF currently exposes quarterly columns only through Q3 2025; the official 23-Sep-2026 external-sector revision notice describes revisions through Q1 2026, not Q2 2026. The latest inspected official national publication therefore does not establish Q2 2026 dual legs. UKR remains NOT_VALIDATED / NOT PASS; aggregate admission NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate rejection
- Re-fetched Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `214cef9b9b7e1f892d0fa2bc427242a919105d59`.
- Re-fetched GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `245eab58e11ac11958f39e894d960f4ba0a1affa`.
- Reused immutable 63-country cohort report `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`, blob SHA `1f767e22095865c8e5f87c2cfca55d9104b91e3e`; UKR appears in the fixed roster. No cohort rebuild.
- Repository search for UKR/Ukraine Q2-2026 portfolio assets/liabilities and dedicated UKR national dual-leg validation returned no dedicated prior UKR country report in the scoped search. No IMF re-query and no duplicate PASS work.

## 2. Official NBU quarterly BOP publication inspected
- Official NBU “Balance of Payments of Ukraine (according to BPM6)”, analytical presentation: https://finliteracy.bank.gov.ua/files/ES/BOP_q_en.pdf
- The publication page states “Last updated on: 19.12.2025”.
- The analytical table's quarterly header row covers I–IV 2020, I–IV 2021, I–IV 2022, I–IV 2023, I–IV 2024, then I 2025, II 2025, III 2025, and cumulative I–III 2024 / I–III 2025. It does not expose Q4 2025, Q1 2026 or Q2 2026 in this published table.
- The detailed table structure distinguishes “Portfolio investment: assets” and “Portfolio investment: liabilities” from “Portfolio investment (net)”, showing that the compiler's framework can publish separate legs. However, the current retrieved quarterly publication vintage does not contain Q2 2026.
- This old publication vintage cannot be used as a Q2 2026 national observation.

## 3. Official NBU revision notice inspected
- Official NBU external-sector changes notice: https://roundtable.bank.gov.ua/admin_uploads/article/Changes_ES.pdf
- It lists retrospective BOP revisions for 2020–2025 and Q1 2026, and says the notice was last updated 23-Sep-2026.
- It does not report Q2 2026 portfolio asset/liability transaction values.
- Official NBU methodology note states detailed BOP data are published quarterly 75–80 days after the reporting quarter and prior periods can be revised: https://bank.gov.ua/admin_uploads/article/BoP_methodological_notes.pdf
- The publication timetable is contextual metadata, not evidence that Q2 2026 values are actually present in the inspected files.

## 4. Methodology and sign boundary
- NBU external-sector methodology states NBU compiles BOP under BPM6 and compiles BOP quarterly.
- The NBU methodology explains that “net acquisition of financial assets” and “net incurrence of liabilities” are increases net of decreases, and the financial-account balance is assets minus liabilities. This is a conceptual framework only; it does not supply the missing Q2 2026 observations.
- Do not infer Q2 from Q1/Q3, annual or cumulative data; do not derive legs from a net value; do not substitute IIP stocks for BOP transactions; do not use non-official third-party datasets as national-source evidence.

## 5. Gate matrix
| Check | Status |
|---|---|
| UKR in immutable 63-country Q2 cohort | PASS |
| Scoped repository search: no dedicated prior UKR country report | PASS (scoped search only) |
| Official NBU compiler / BPM6 methodology | PASS |
| NBU analytical quarterly BOP table inspected | PASS |
| Latest quarter in inspected analytical table | Q3 2025 |
| Official revision notice latest period explicitly referenced | Q1 2026 |
| Q2 2026 national portfolio asset leg | NOT_CAPTURED |
| Q2 2026 national portfolio liability leg | NOT_CAPTURED |
| Q2 2026 national portfolio net | NOT_CAPTURED |
| Q2 2026 source vintage / period alignment | NOT_ESTABLISHED |
| Raw Q2 source bytes / byte count / SHA-256 | NOT_CAPTURED |
| National dual-leg comparison | NOT_DONE |
| UKR validation | NOT_VALIDATED / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Next exact action
- Do not repeat the same stale quarterly PDF retrieval. Revisit UKR only if a newly published NBU Q2-2026 detailed BOP release, downloadable Excel/SDMX table, or official open-data API response explicitly exposes Q2 portfolio asset and liability transaction legs.
- If such a source is found, archive exact raw bytes/response, source URL, retrieval timestamp, byte count and SHA-256 before parsing; confirm quarter basis, unit, sign and vintage; compare legs separately against the already archived IMF exact-key rows without a new IMF query.
- Otherwise retain UKR NOT_VALIDATED / NOT PASS and advance to the next eligible fixed-cohort member, Uruguay (URY), after checking the immutable roster and repository for prior URY reports. No cohort rebuild.

## 7. Protected constraints
₹0 spend; official free sources only. No synthetic values, no inferred legs, no stock-as-flow, no generic FX, no sign flip, no annual/cumulative proration, no IMF re-query, no cohort rebuild, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Sources
- NBU quarterly analytical BOP (BPM6), last updated 19-Dec-2025: https://finliteracy.bank.gov.ua/files/ES/BOP_q_en.pdf
- NBU external-sector revision notice, last updated 23-Sep-2026: https://roundtable.bank.gov.ua/admin_uploads/article/Changes_ES.pdf
- NBU BOP methodology note: https://bank.gov.ua/admin_uploads/article/BoP_methodological_notes.pdf
- NBU external-sector methodology: https://forumbeps.bank.gov.ua/admin_uploads/article/BoP_methodological_notes_en.pdf
- Immutable Q2-2026 cohort: `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`
