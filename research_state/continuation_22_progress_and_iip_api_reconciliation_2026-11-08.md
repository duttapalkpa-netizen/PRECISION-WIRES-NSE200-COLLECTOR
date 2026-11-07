# PRECISION-WIRES V11.3 — Continuation 22
Date: 2026-11-08
Page: গবেষণা যাচাই অব্যাহত 22
Branch: fix/iip-41-vintage-audit-clean

## User's key concern: why did overall progress remain 36%?
The 36% value was repeated as though it were current, but it was only the last historical baseline. Continuation 20 explicitly required not inventing an overall percentage because no complete denominator had been reconciled. Later summaries failed to preserve that distinction. This is corrected in PROJECT_PROGRESS_ACCOUNTING_RECONCILIATION_2026-11-08.md.
- Historical baseline: 36% (not current / not re-certified).
- Current global percentage: NOT CALCULABLE until a canonical weighted acceptance register is frozen and reconciled.
- This does not mean work stopped; workstream-specific completed tasks below are evidence-backed.

## Newly reconciled pre-existing API evidence — do not repeat
Repository inspection found that the April 2026 official MoSPI API had already been fully acquired and compared, despite recent continuation summaries focusing on the smaller PIB 37-row transcription.
- OpenAPI YAML: HTTP 200, 11,226 bytes, SHA-256 bed83ff75c1b361368019a55473ed29c9fcd7242651706cffea04debb65211e0.
- API contract: GET https://api.mospi.gov.in/api/iip/getIIPData; documented base_year 2022-23, monthly year/month_code/type/viz_req parameters. Full schema audit in run 42367705456 artifact.
- April 2026 API request: HTTP 200, 43 rows (1 General, 36 Sectoral, 6 Use-based), 8,129 bytes; raw SHA-256 ba0ee42f7fb7809483a86dcbfe53057d401c51af67e28638c6603fcedcdca71a.
- April API CSV: data/macro/iip_apr2026_mospi_api_records.csv, 43 rows, SHA-256 192267b76af8cc0bc524d33a86461d0d70906a96a34eadfdccea12b2245a82ee; commit 198ad7bccf5d6f634e0f0af6a5868119369f1921.
- April validation JSON: data/macro/iip_apr2026_mospi_api_validation.json; commit 6b0bd934152fb83fb258fc6a3ffce29f4dce4f86.
- Latest official benchmark: PIB PRID 2329475, 2026-10-28, https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2329475. It states base 2022-23=100 (lines 70–79 and 104–105); April sectoral values Statement I line 109, use-based values Statement III line 197, NIC-2025 April column Statement IV lines 219–260.
- Final dual-month audit Run 42381121341 (#12), commit 5f079524dfa7e1210005e46020fd9b6e109401e2, job conclusion SUCCESS; Artifact ID 13577128037; ZIP SHA-256 2337b9ed18d0057cac3a4c503a6d0657f0750df720f5a50878f14b3fc67d5059. Re-downloaded and independently checked ZIP hash against GitHub digest.
- Artifact #12 contains April cross-check JSON: 43 expected, 43 observed, 43 matched, zero missing/mismatches/unexpected/duplicates, PASS_ALL_43_MATCH. May similarly 43/43; April+May = 86/86.
- PPI identity corroborated by PRID 2278961 (2026-06-29), which says the full 2022-23 series was revised using Output PPI and supersedes the WPI-based series. API records themselves do not carry deflator field; retain this caveat.
- API evidence resolves April 2026 data access through official API. It does NOT recover the native catalogue XLSX and does not complete the full 41-vintage audit.

## Correction / quarantine: Continuation 21 37-row PIB transcription
- Preserve original file and report for history: research/data/iip_april_2026_statement_iv_output_ppi_pib_transcription.csv and research/continuity/IIP_APRIL_2026_STATEMENT_IV_TRANSCRIPTION_QA_2026-11-08.md.
- It contains 37 Statement IV rows and omits six use-based rows; it is not the full 43-record April dataset.
- It labels base_year 2011-12=100, conflicting with the current revised April series base 2022-23 in PRID 2329475 and the API contract/query. Do not use it as current-series master input; quarantine from current-series joins. Do not overwrite or silently relabel.
- Use the 43-row API CSV for current 2022-23 April dataset, with its API/PIB validation and source caveat.

## Progress accounting correction
- Detailed scorecard: research_state/PROJECT_PROGRESS_ACCOUNTING_RECONCILIATION_2026-11-08.md; commit 4ffe3b0178abf07dc07f4ded9e82c7605f5a1e0a.
- April API contract: 100%; April API extraction 43/43 = 100%; April latest-PIB validation 43/43 = 100%; May latest-PIB validation 43/43 = 100%; April+May combined 86/86 = 100%.
- IIP monthly workbook ingestion remains 39/41 = 95.1% period ingestion only.
- Full IIP vintage audit remains BLOCKED_WITH_GAPS; native April XLSX NOT RECOVERED; 693 candidate transitions remain in audit scope with 431 unresolved; source-cell matured certification remains incomplete.
- Radar one-off output completed; daily automation remains 0% (not enabled).
- Full CORE-672 live implementation is not claimed complete; IPO-PLX remains foundation only.
- The overall 36% is now explicitly historical/stale. Current overall percentage is NOT CALCULABLE until the complete weighted master acceptance register is rebuilt. Do not fabricate a new number.

## New correction reports
1. research/continuity/IIP_APRIL_2026_API_43ROW_RECONCILIATION_AND_LEGACY_TRANSCRIPTION_CORRECTION_2026-11-08.md — commit 0139902007f03f521baeb0beac7bc2de1dc74656.
2. research_state/PROJECT_PROGRESS_ACCOUNTING_RECONCILIATION_2026-11-08.md — commit 4ffe3b0178abf07dc07f4ded9e82c7605f5a1e0a.

## Next highest-value task
Build the canonical master acceptance register from repository artifacts and the user's previously established final research-paper acceptance criteria. Freeze item weights and pass definitions before computing a new overall completion percentage. Reconcile 56×12 CORE-672, five engines, data backbone, source groups/factors, backtests, IPO-PLX, risk modifier, same-snapshot audit, and final paper. Do not alter production logic or repeat completed tasks.

## Invariants
Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 unchanged. UNKNOWN is neither PASS nor FAIL. No synthetic rows, fabricated timestamps, guessed IDs, unsupported source promotion, or Hard Gate relaxation. IIP full audit BLOCKED_WITH_GAPS; master Hard Gate BLOCKED. Research spend ₹0.
