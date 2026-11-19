# GCR — RBI Table 42 prior-work reuse and duplicate-task correction
Date: 2026-11-19 (Asia/Kolkata)
Scope: audit of prior GitHub research before repeating RBI DBIE/Table 42 acquisition
Decision: PRIOR WORK EXISTS; DO NOT REPEAT TABLE 42 SCALE/SIGN ACQUISITION OR VALIDATION

## 1. Why this correction is required
Continuation 44 Part-4 proposed obtaining RBI DBIE Table 42 CSV/JSON as if India BPM6 cross-check data had not previously been captured. A repository search and direct file inspection found earlier completed RBI Table 197 and Table 42 work, raw HTML archives, comparison scripts and validated results. The Part-4 “raw acquisition pending” statement was too broad and failed to distinguish a new DBIE time-series export from the already acquired RBI Bulletin Table 42 HTML snapshots.

## 2. Prior India benchmark — RBI Table 197
Source report:
`docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md`
- Status: 12/12 PASS across six quarters, 2024-Q2 to 2025-Q3.
- RBI Table 197 official BPM6 quarterly USD-million source.
- Mapping: RBI 3.2.A “Portfolio Investment in India” credit-minus-debit net ↔ IMF L_NIL_T, same sign; RBI 3.2.B “Portfolio Investment by India” ↔ negative IMF A_NFA_T.
- Comparison: IMF raw OBS_VALUE / 1,000,000 against RBI USD-million values; integer-publication tolerance ±0.5m.
- Maximum absolute residual 0.4899709189m.
- Raw RBI HTML: 146,017 bytes; SHA-256 `391c549c5b64c0b7f9204eb9634975f77d4ba2d7796542ed23932fb8d740813d`.
- Workflow run 44476434148; artifact 14506542277; ZIP 28,097 bytes; SHA-256 `eb719a38a285603ec2eff92ea7a88aadd5cbb7481393fe5b8f44188bffcacf62`.
- Report file blob SHA at audit: `83bc6de6a724f4f1ddc6a7e74556e5f596393788`.

## 3. Prior India benchmark — RBI Table 42 current-vintage supplement
Source report:
`docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_CURRENT_VINTAGE_SUPPLEMENT_20261119.md`
- Two official RBI Bulletin Table 42 pages captured anonymously:
  - Jan–Mar 2025 / Jan–Mar 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24424 (published 2026-08-25).
  - Apr–Jun 2025 / Apr–Jun 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566 (published 2026-10-23).
- Raw HTML and retrieval metadata/hashes archived under `docs/evidence/imf_bop_20261119/india_scale_reconciliation_current_vintage/`.
- Jan–Mar raw HTML SHA-256: `a92ac0f8196efbd8f503984620d7c0291c6d704405e52d64eec4f96948ddf744`.
- Apr–Jun raw HTML SHA-256: `075c28122d588e5bce0ff45c8c8d5d8b453c53dc5b9a20f79d5cd3a6e54f5396`.
- Crosswalk artifact 14505649659; ZIP SHA-256 `8db4f9536a57df1e8635855af5bb90225de0f800e6e9164bd20d99d1f355b4e2`.
- Four quarters × three comparisons (assets, liabilities, combined net) = 12 checks; 10 PASS, 2 REVIEW.
- 2025-Q1, 2025-Q2, 2026-Q2: all checks PASS. 2026-Q1 asset PASS; liability and combined net REVIEW.
- 2026-Q1 IMF liability -13,633.508347m USD vs RBI 3.2.A net -12,121m; residual -1,512.508347m. Combined-net residual -1,512.457994m. Cause not established; no adjustment permitted.
- Combined India evidence: eight unique quarters; asset/liability 15/16 PASS, 1 REVIEW. Current-vintage gate remains PARTIAL, not PASS.
- Report blob SHA at audit: `d638cf4a9bc262b55c7660585d01aca493ebf518`.

## 4. Prior reproducible code
- `scripts/research/reconcile_imf_bop_scale_india_rbi_table197.py`: fetches RBI Table 197, records retrieval timestamp/status/headers/byte count/SHA, validates source labels and values, compares six quarters against committed IMF panel. Blob SHA `c746442c2ab483d5212da908715c20f0049d69ad`.
- `scripts/research/crosscheck_india_bop_scale_sign.py`: captures two RBI Table 42 Bulletin pages, records raw HTML hashes and retrieval metadata, parses portfolio total/assets/liabilities, compares 2025-Q1/Q2 and 2026-Q1/Q2 against the IMF panel, writes CSV/JSON/manifest/report. Blob SHA `e058a7988068733b987109cc8c87759a5e8fa213`.
- The second script explicitly uses RBI Bulletin Table 42 HTML, not the DBIE time-series CSV/JSON export page. This distinction must be preserved.

## 5. What is complete and what is not
### Complete / do not repeat
- RBI Table 197 historical six-quarter India scale/sign cross-check: 12/12 PASS.
- RBI Bulletin Table 42 current-vintage four-quarter crosswalk: raw HTML acquired, metadata/hashes archived, 12 comparisons generated, 10 PASS / 2 REVIEW.
- India asset/liability sign mapping: assets sign reversed; liabilities same sign.
- Raw IMF panel unchanged; diagnostic comparison only.
- Existing source files, scripts, artifacts and manifests are already in GitHub.

### Still open
- 2026-Q1 liability/combined-net discrepancy: REVIEW; exact old/new vintage and definition bridge not established.
- RBI DBIE table page's separate CSV/JSON controls were surfaced in a later route-discovery check, but no new DBIE export bytes have been captured in this Part-4/Part-5 audit. This is a distinct optional acquisition route, not a prerequisite to repeat or invalidate the already archived RBI Bulletin Table 42 crosswalk.
- The India check validates only the matched country-periods and current source definitions; it does not authorize scale/sign generalization to all 154 EMDE members or an EMDE aggregate.
- Full GCR observation panel, other-country coverage/vintage validation, global relative-attraction calculation, sector transmission and event study remain incomplete.

## 6. Correction to Continuation 44 Part-4
Part-4 correctly identified RBI Table 42's official DBIE route and general sign convention, but its wording implied that India Table 42 source acquisition and scale/sign cross-check remained wholly unperformed. That implication is corrected here:
- Already acquired: RBI Bulletin Table 42 raw HTML for four quarters, with raw SHA-256 and crosswalk artifact.
- Already validated: 10/12 Table 42 comparisons PASS; 2/12 REVIEW.
- Not acquired: separate DBIE time-series CSV/JSON export.
The latter must not be used to restart the completed Bulletin Table 42 work. Only pursue it if it materially extends the historical coverage or resolves the 2026-Q1 vintage discrepancy.

## 7. Next highest-value action
Do not rerun Table197 or Table42 cross-check scripts unchanged. Investigate the exact 2026-Q1 RBI-vs-IMF vintage/definition discrepancy using the already archived RBI Table42 pages and IMF observations, including source release dates and row labels. Seek an older/newer official RBI vintage for the same quarter only if it is available at ₹0 and can be archived. If no exact bridge exists, keep REVIEW and move to the next independent country/coverage blocker; do not force reconciliation.

## 8. Invariants
₹0 spend; official/free sources; no synthetic rows, no interpolation, no fabricated timestamps, no silent adjustments. Preserve IMF raw observations. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. GCR remains INCOMPLETE / BLOCKED; aggregate and production admission NOT_AUTHORIZED.
