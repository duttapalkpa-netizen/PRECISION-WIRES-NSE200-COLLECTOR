# Philippines PHL Q2-2026 — BSP portfolio investment dual-leg cross-check against archived IMF panel
Date: 2026-11-20 (Asia/Kolkata)
Decision: **BSP dedicated portfolio table values independently verified from official publication; IMF archived values numerically reconcile within BSP whole-USD-million rounding for both legs; same-vintage NOT_ESTABLISHED; automated raw-capture parser NOT_PASS; PHL full admission PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity and cohort
- PHL is a member of the pre-existing fixed 63-country synchronous Q2-2026 cohort. No cohort rebuild and no new IMF GET.
- Reused committed IMF panel docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv, SHA-256 e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a.
- Exact PHL Q2-2026 rows:
  - A_NFA_T raw OBS_VALUE +1,330,642,951.05526 USD; UNIT=USD; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; derived +1,330.64295105526 USDm.
  - L_NIL_T raw OBS_VALUE +1,798,282,616.26536 USD; UNIT=USD; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; derived +1,798.28261626536 USDm.
- Raw IMF values and metadata remain unchanged.

## 2. Official BSP portfolio values
- Dedicated source: BSP Table 1.7, Portfolio Investment, USD million: https://www.bsp.gov.ph/Statistics/External/table1.7_data.aspx
- Dated BSP Q2-2026 BOP release (11-Sep-2026): https://www.bsp.gov.ph/Media_And_Research/Media%20Releases/2026_09/news-09112026a1.aspx
- Official release table gives Q2 2026: portfolio net -468 USDm; net acquisition of financial assets +1,331 USDm; net incurrence of liabilities +1,798 USDm.
- Dedicated Table 1.7 confirms the same Q2 values. Identically named rows elsewhere in all-BOP Table 1 were rejected because they belong to Other Investment, not Portfolio Investment.
- Display identity: 1,331 - 1,798 = -467 USDm vs published net -468 USDm; 1 USDm difference is within combined whole-million rounding of independently rounded rows. No forced identity or netting.

## 3. IMF vs BSP separate-leg numeric comparison
BSP publishes whole USD millions; ±0.5 USDm is the per-row display rounding tolerance.

| Entry | IMF raw USD | Derived IMF USDm | BSP USDm | IMF−BSP USDm | Tolerance | Result |
|---|---:|---:|---:|---:|---:|---|
| A_NFA_T | 1,330,642,951.05526 | 1,330.64295105526 | 1,331 | -0.35704894474 | ±0.5 | PASS |
| L_NIL_T | 1,798,282,616.26536 | 1,798.28261626536 | 1,798 | +0.28261626536 | ±0.5 | PASS |

Separate numeric legs 2/2 PASS at BSP displayed precision. No sign inversion, raw IMF overwrite, netting, FX conversion, or global scale/sign assumption.

## 4. Automated capture QA — explicit limitation
- Research script: scripts/research/reconcile_phl_q2_2026_bsp_imf.py.
- Workflow: .github/workflows/gcr_phl_q2_2026_bsp_imf.yml, timeout 5 minutes.
- Script commit 5668468624c7ec622c51d68a1a3799638810a0b5; workflow commit c91d341952e21100bccefceadc517fa8dc2f864b; parser correction 7dc094255f50d8486708d57b79db6799434fb2a8; dedicated Table 1.7 correction 5f322db2d783d85b9e2631d9b4b6d0b65030bf4b; Excel-HTML signature correction c62532e2a980f727d550790d47b1f608434fef70.
- Run 44690030449 failed closed after detecting the generic Table 1 parser had selected identically named Other Investment rows; erroneous parsed values NOT_ADMITTED.
- Run 44690124941 captured raw Table 1 (HTTP 200, 232,567 bytes, SHA-256 5b7279ce8c7c4c249cc3fce6b9705675b42cff3794f88e178b454411301d94cf) and the BSP release (HTTP 200), but first generic-table parsing attempt was rejected. Artifact 14607583953, ZIP SHA-256 b8b92e22f272cc19aeab4cc0549ec7046d5f6189fb3f91d0dc40084a92f96938. Diagnostic only; wrong component rows are not evidence.
- Dedicated Table 1.7 workflow run 44690374864 failed closed because Python HTMLParser did not parse BSP Excel-HTML sparse-row representation (only one label cell). No parsed Table 1.7 artifact or script-generated numeric PASS claimed.
- Official published HTML text independently confirms the values above; those values are not claimed as script-generated structured evidence.
- Parser must be repaired for Excel HTML sparse cells including ss:Index, then rerun.

## 5. Publication-vintage gate
- BSP Q2 release dated 11-Sep-2026; Table 1.7 current published table, Q2 2026 preliminary (p).
- Archived IMF panel retrieved 19-Nov-2026; public IMF BOP dataset does not expose observation-specific source submission/revision timestamp for PHL Q2.
- Retrieval time is not source vintage. BSP↔IMF same-vintage cut-off NOT_ESTABLISHED.
- PHL national validation PARTIAL / NOT PASS. 63-country aggregate NOT_AUTHORIZED.

## 6. Operational containment
- Unintended NSE collector runs 44690020188, 44690030398, 44690124814 and 44690374904 were cancelled; no outputs admitted as evidence.
- Cancellation commits: e65adc5174166379a9671fdc47f541f565f0ea5d, 88a58c2593b219e935ab0d1bfb4df17be9606545, 1c0d2d2d2a637a00f6d652c1d1cb321450ff02df, 941f454735402ecb511a473b8565592de82616d8, 3cb1ad7cbf2d78e2b6da7cbc9f8715d80cb6937e. Confirmed cancelled for 44690124814 and 44690374904; earlier runs also recorded cancelled.

## 7. Exact next action
Repair BSP Table 1.7 Excel-HTML parser with sparse-cell index handling, verify Q2 2026 extraction against dated official release, create a successful raw+parsed evidence artifact, then pursue PHL observation-level IMF vintage bridge. Do not rerun IMF acquisition or rebuild cohort.

## 8. Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights and trading gates unchanged. No paid data, synthetic values, fabricated timestamps, forward-fill, imputation, unauthorized netting, production integration or aggregate authorization. UNKNOWN is never PASS.
