# PRECISION-WIRES V11.3 — Continuation 21
Date: 2026-11-08
Page: গবেষণা যাচাই অব্যাহত 21

## Immutable project invariants and working rules
- Production selector unchanged; RANKING_SCORE unchanged; +1 PRESSURE_FADE unchanged; CORE-672 unchanged (56 steps × 12 filters); V11.3(A/B/C/D/E) production architecture unchanged.
- UNKNOWN is neither PASS nor FAIL. Never synthesize observations, fabricate timestamps, infer catalogue IDs, promote unsupported source types, or relax Hard Gate.
- ₹0 research spend; free official sources only. No paid API/licence/subscription or external contact without explicit approval.
- Preserve prior PASS/FAIL/BLOCKED artifacts, Run IDs, Artifact IDs, hashes, commits, error causes and corrections. Inspect checkpoint/manifest before selecting next task; do not repeat completed work.
- Keep tasks bounded, ideally <=10 minutes. Branch-scoped research only; never merge to main or enable main automation without explicit approval.
- GitHub Actions SUCCESS is not equivalent to audit PASS. State precise source limitations.
- User requests complete durable memory. GitHub continuation checkpoints are the durable audit trail; do not promise that ChatGPT Memory can permanently hold every raw artifact/history.
- Overall progress baseline last defensible 36%; do not inflate without global denominator reconciliation.

## Latest completed task — April 2026 Statement IV full-column transcription and QA
- Official primary publication: PIB / MoSPI PRID 2278961, 29-Jun-2026 16:00 IST: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3
- Re-opened source; Statement IV source-rendered lines 157–199. Header explicitly says Base 2011-12=100, NIC 2025, monthwise columns May-25 to May-26. April-26 is explicitly present.
- Lines 21–25 and 40–41 establish Output-PPI deflator and that 29-Jun release supersedes 1-Jun WPI-based 2022-23 series. Do not confuse the WPI release with the PPI superseding release.
- Extracted 37 rows for April 2026: 23 NIC-2 manufacturing classes, manufacturing aggregate, 4 mining rows, 5 electricity/gas rows, 3 water/waste rows, General Index.
- Ledger: research/data/iip_april_2026_statement_iv_output_ppi_pib_transcription.csv; commit 65b1ed4304a7decc26fc39327e3211b5c3fe217f; read-back SHA/blob 0a3364f4b235ff14eb3263ea79cd283e571ce024; 38 lines incl header.
- QA report: research/continuity/IIP_APRIL_2026_STATEMENT_IV_TRANSCRIPTION_QA_2026-11-08.md; commit 4461bad6db2666024cda6e92b4c83bfdceed5ac8; read-back SHA/blob 9c03eb03a9ffef9985c131b608b99ea9c0a097f4.
- QA: 37 rows; no duplicate NIC-code keys; 37/37 numeric positive April index values. Manufacturing weights 76.065 vs published 76.062 (+0.003 displayed rounding); weighted April index 118.6934 rounds to 118.7. Mining 106.0877 -> 106.1; Electricity generation 122.9177 -> 122.9; Electricity+Gas 121.7285 -> 121.7; Water 146.0667 -> 146.1. Published aggregates reconciled after rounding.
- Status: PASS_TRANSCRIPTION_AND_WEIGHTED_AGGREGATE_QA_WITH_SOURCE_TYPE_LIMITATION.
- Important limitation: this is PIB HTML transcription, NOT native MoSPI XLSX or e-Sankhyiki API. Statement IV base label 2011-12=100 retained exactly; Output-PPI superseding-release context separately recorded. No guessed ID or synthetic row.
- Continuation-20 checkpoint append commit: 7bc23ffe858bd8d900c1bd4516251c8c291f12ee.

## Previous April source-recovery task — do not repeat
- Official PIB PRID 2278961 confirms Output-PPI supersedes WPI series and includes April 2026 in monthwise Statement IV.
- Report commit bb637c0051a29bd87df5992cb4d67fa64922e694; continuation-19 append commit c409a2e2979ec7faaa839993cfb00327004d2af8.

## January 2026 official release reconciliation — do not repeat
- Official PIB PRID 2234512 confirms January 2026 Quick Estimate; base 2011-12, NIC-2008; General IIP 169.4, YoY +4.8%.
- January absent from XLSX manifest does not mean no official release. Native catalogue table/XLSX not recovered; no ID inferred.
- Report commit 3a86a7a71683fc20bf61c7ed484b67021c80860b.

## 41-month XLSX catalogue coverage reconciliation — do not repeat
- Apr-2023 to Aug-2026 = 41 months; manifest 40 unique catalogue records; 39 parsed XLSX vintages.
- January 2026 absent from manifest; April 2026 old catalogue ID IIPMFY26002APR HTTP 404.
- Legacy parsed 35 vintages Apr-2023–Mar-2026 (base 2011-12/NIC-2008); new parsed four May–Aug 2026 (base 2022-23/NIC-2025).
- Report commit f58c76a22d0db436534fbc71b2447d75a45a1430; ledger commit afbaa057279df6b30466655e6c7ba281b3ea4a12.
- Original source Run 41640521553, Artifact ID 13232127900, ZIP SHA-256 e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c.

## Other completed evidence to preserve
- September 2026 release metrics QA + NIC-2 Statement II-A QA: Run 42400271361 SUCCESS; Artifact ID 13584194796; ZIP SHA-256 6a97828061391dece1825a1b26c1daea65ad1705c6edef92468e5510cf54956b. QA scope limited; raw PIB PDF binary hash NOT_ACQUIRED.
- Radar 2026-11-09 one-off independently reconciled 20/20; Run 42385524572 SUCCESS; Artifact ID 13579421445; ZIP SHA-256 08a114830871fb87267fb4a476ee581c811e5776a69102d6fd961b980a8a9017. Static QA Run 42385628048 SUCCESS; no main automation enabled.
- IIP Run 41640521553 job-level PASS but audit BLOCKED_WITH_GAPS.
- Earlier evidence: 40/40 unique PIB catalogue IDs verified; 1,124 revision differences joined; 693 candidate transitions uncertified; 431 historical/out-of-window unresolved; certified source-cell revisions 0.

## Next highest-value bounded actions
1. Obtain and verify official PIB raw PDF/attachment bytes for PRID 2278961 if an official direct file link is exposed; preserve raw file, retrieval timestamp, byte size, SHA-256, and compare table rendering. Do not claim PDF hash until downloaded and verified.
2. Separately verify native MoSPI/e-Sankhyiki catalogue/API equivalent for April 2026; official API schema and exact filter parameters must be read, not guessed. The old ID IIPMFY26002APR remains 404.
3. Audit the full 37-row ledger against the raw PDF/table if available; maintain source-type limitation until native equivalence is proven.
4. Then continue January native catalogue/API gap separately. Never overwrite the immutable XLSX ledger.
5. Record each artifact hash, commit, QA, and task-specific progress. Overall remains 36% until global denominator reconciliation.

## Status
- April PIB Statement IV transcription/weighted aggregate QA: PASS_WITH_SOURCE_TYPE_LIMITATION.
- Native catalogue XLSX/API reconciliation: open.
- IIP full audit: BLOCKED_WITH_GAPS.
- Master Hard Gate: BLOCKED.
- Overall research progress: last defensible 36%.
- ₹0; production invariants unchanged.
