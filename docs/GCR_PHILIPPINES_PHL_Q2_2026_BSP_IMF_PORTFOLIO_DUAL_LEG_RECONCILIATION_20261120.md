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


## 9. Continuation 45 — parser repair and successful evidence artifact (2026-11-20)
- Reopened the failed Table 1.7 artifact and inspected the raw Excel-HTML. Root cause: a one-cell merged "Portfolio Investment" section heading preceded the actual 20-cell data row; the parser incorrectly treated the heading as a truncated data row. Corrected by ignoring one-cell merged headings, checking the Q2 group header and the 2026p subheader, and extracting column 11 (Q2 2026, distinct from Q2 2025 at column 10).
- Second parser defect: the dated press release contains several functional-account sections with identically named component rows. The parser had overwritten the Portfolio Investment components with later Other Investment rows. Corrected by anchoring extraction to the Portfolio Investment heading and consuming only its next two component rows; release-vs-Table-1.7 exact parity is now enforced.
- Q2 preliminary flag is now derived from the verified header cell "2026 p", not a fragile HTML regex.
- Successful workflow run 44705225122, job 136183035008, conclusion SUCCESS. Workflow head SHA 9c0c84a6b42f43980fdceb650395897dcea69b16. Artifact 14614766459, name gcr-phl-q2-2026-bsp-imf-44705225122, 15,415 bytes, ZIP SHA-256 7e0d57f7d50f6f0a6622183d81f2bb8bbe04ee297f489f20dd982465d3b46b5c, expires 2027-02-18.
- Downloaded artifact independently inspected. Files:
  - bsp_table1_7_raw.html: 156,110 bytes, SHA-256 b267ceab83794b86cd6c6a3ce703d878c2185091670e0c528b10df1644774569.
  - bsp_q2_release_raw.html: 148,165 bytes, SHA-256 272890a3a383bbef2eebfb274746e3835f2c3e7d3ab084f303f317f6813b5707.
  - phl_q2_2026_bsp_imf_reconciliation.csv: 384 bytes, SHA-256 8bc1a27fc66c40f99ad7d66789884a90c0f1d1cb91b4c64065fdec4e769d2939.
  - summary.json: 3,919 bytes, SHA-256 376894e48319d0a0a2c0d4e8322f4de0fc578fd8b1b70a4f361e425b0f0dd166.
- Exact structured result: BSP Q2 preliminary flag TRUE; net -468 USDm, assets +1,331 USDm, liabilities +1,798 USDm; release and Table 1.7 values match exactly. IMF asset residual -0.35704894474 USDm and liability residual +0.28261626536 USDm, both within ±0.5 USDm. Numeric legs 2/2 PASS. Rounded identity differs by +1 USDm and is retained as rounding, not forced to zero.
- Prior bad parser runs 44690030449, 44690124941, 44690374864 and 44704973071 remain diagnostic/failed; no erroneous rows admitted.
- Paths-ignore guard was finally verified and added in commit fbaa2617f8e996b996f299652194974141cd0921 for PHL script, PHL workflow and cancellation trigger/workflow paths. Accidental NSE runs 44704973029 and 44704985742 were both confirmed completed/cancelled; no outputs admitted.
- Remaining blocker: BSP↔IMF same-vintage NOT_ESTABLISHED. BSP Q2 data are explicitly preliminary; HTTP Last-Modified is the current server response timestamp, not a historical revision chain. Public IMF BOP dataset page lists dataset/API/download but no observation-level source submission/revision timestamp. BSP FDI page's announced January–June revision concerns FDI/in-kind transactions, not portfolio investment, so it is not used as evidence for this portfolio series.
- Final PHL state remains numeric 2/2 PASS; source capture PASS; release parity PASS; same-vintage NOT_ESTABLISHED; full national acceptance PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next action: only pursue a specific BSP portfolio-series revision archive and IMF observation-level vintage field if an official public endpoint/document exists; otherwise close this bounded vintage search as NOT_ESTABLISHED and move to the next cohort country after preflight. No repeat Table 1.7 parser work, no IMF requery, no cohort rebuild.
