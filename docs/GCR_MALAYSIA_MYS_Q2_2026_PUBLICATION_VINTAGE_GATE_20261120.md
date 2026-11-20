# Malaysia MYS Q2-2026 — publication-vintage / revision-cutoff gate
Date: 2026-11-20 (Asia/Kolkata)
Decision: **Official publication chronology captured; same-vintage BNM↔IMF alignment NOT_ESTABLISHED; MYS remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## Continuity preflight
- Reopened the current master continuity ledger (blob SHA `396152cfd62e2c7888e4f40947b019cca7e875b8`), current GCR priority queue (blob SHA `9c49ce9064f207ce18de6a0e8c80ba8b11e126d9`), MYS national crosswalk, exact IMF row extraction and completed BNM FX/dual-leg report.
- Reused the existing MYS BNM raw daily/monthly capture, 60-row calculation, exact IMF rows and national portfolio table. No repeated FX download, IMF query, cohort rebuild, or national component re-extraction.

## 1. Official national publication chronology
### DOSM Q2 2026 release
- Official release page: https://www.dosm.gov.my/portal-main/release-content/quarterly-balance-of-payments-q22026
- Latest Release: 14 August 2026.
- The Q2 press release reports the financial account and portfolio investment net outflow (RM35.2bn); it is not the source used for the detailed asset/liability component values in this audit.
### BNM Quarterly Bulletin 3Q 2026
- Official bulletin page: https://www.bnm.gov.my/-/quarterly-bulletin-3q-2026
- BNM issue date: 18 November 2026.
- Official Annex Table 3 PDF: https://www.bnm.gov.my/documents/20124/23688793/qb26q3_en_annex.pdf
- Table 3 is BPM6, unit RM billion. It presents 2026 Q2 portfolio investment net -35.2, assets -33.3, liabilities -1.8.
- The column header explicitly marks 2026 as preliminary (p); table note defines negative asset as resident acquisition/outflow and positive liability as inflow from incurrence of foreign liabilities. It also warns values may not add due to rounding.
- The current Q3 bulletin therefore provides a dated 18-Nov-2026 national-source snapshot for Q2, but its Q2 values remain preliminary. It does not expose the date on which each underlying portfolio component was last revised or the date of the national data freeze.
### OpenDOSM BOP dashboard
- Official page: https://open.dosm.gov.my/dashboard/balance-of-payments
- Current page states “Last updated: 18 Nov 2026, 13:00” and “Data as of 3Q 2026”.
- Its displayed Q2 portfolio net is RM -35,155 million (equivalent to -35.155 RMbn), while BNM Annex Table 3 rounds net to -35.2 RMbn. This is a current-vintage net cross-check only; the dashboard table does not provide the separate portfolio asset/liability component rows needed to establish a same-vintage dual-leg bridge.
- The Q2 release page's rounded net (-35.2 RMbn) and the 18-Nov dashboard net (-35.155 RMbn) are compatible at one decimal RMbn. They do not prove whether the underlying Q2 net changed, because the 14-Aug release page exposes only rounded net and not the exact component values needed for an old/new row-level comparison.

## 2. IMF source-vintage boundary
- IMF BOP dataset page: https://data.imf.org/Datasets/BOP
- The public page confirms the BOP dataset and provides API / View Data / Download entry points, but its visible public page has no dataset-level last-updated timestamp and no per-observation submission/revision timestamp.
- The separate IMF BOP/IIP Country Metadata dashboard has a publication date of 18-Nov-2026, but it is a country metadata dashboard, not the Q2 MYS observation vintage. It must not be misused as the publication date or vintage date of the BOP observation.
- Existing MYS panel exact rows are from IMF.STA:BOP(21.0.0), P_F, Q2 2026, raw archived observation values with UNIT=USD, SCALE=6, PRECISION=6, DERIVATION_TYPE=O. The existing archive receipt was acquired 19-Nov-2026. Acquisition time is not evidence of the IMF's source submission date or vintage cut-off.
- No public per-row source-submission date, revision sequence, or historical IMF panel snapshot corresponding to the BNM 18-Nov preliminary table was located in this bounded review.

## 3. Cross-source chronology matrix
| Evidence | Public date / timestamp | Q2 status | What it proves |
|---|---|---|---|
| DOSM Q2 release | 14-Aug-2026 | Q2 release; portfolio net rounded | National release chronology; net only |
| BNM Q3 bulletin Annex Table 3 | 18-Nov-2026 issue | Q2 explicitly preliminary | Dated Q2 asset/liability snapshot and sign notes |
| OpenDOSM BOP dashboard | Updated 18-Nov-2026 13:00; data as of Q3 | Q2 current dashboard net | Current Q2 net RM -35,155m; no separate portfolio legs |
| IMF BOP dataset landing page | No visible last-updated date | Dataset-level page only | Dataset identity; no Q2 MYS observation vintage |
| IMF MYS panel archive | Retrieved 19-Nov-2026 | Q2 exact rows | Retrieval time and raw values, not source vintage |

## 4. Gate decision
- Official national publication chronology: PASS.
- BNM Q2 preliminary status and component sign definitions: PASS (reused).
- OpenDOSM 18-Nov current-vintage net cross-check: PASS as a net-only current display.
- IMF observation-specific source submission/revision date: NOT_AVAILABLE from public landing page.
- Exact BNM–IMF same-vintage cut-off bridge: NOT_ESTABLISHED.
- MYS two separate numeric leg checks at BNM published display rounding: PASS (previous report; not repeated).
- MYS full national dual-leg validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## 5. Interpretation and next action
- The available official evidence cannot establish that the IMF panel's MYS Q2 values and BNM's 18-Nov Q2 preliminary component rows represent the same source-vintage cut-off. The fact that the panel was retrieved on 19-Nov is not sufficient.
- No silent revision inference, vintage assumption, re-signing, tolerance widening, netting or aggregate is authorized.
- MYS vintage gate is now **bounded / no public observation-level vintage bridge located**. Do not repeat the same public landing-page search or FX download absent a new official historical snapshot, revision log, or source metadata.
- Advance to the next eligible country in the existing fixed 63-country cohort with a direct official USD-denominated dual-leg source. Thailand (THA) is selected for the next bounded check because the Bank of Thailand publishes a quarterly USD BOP table with explicit portfolio asset/liability rows and a dated “Last Updated” field; it remains a new validation, not an assumed PASS.

## Invariants
No cohort rebuild, no new IMF request for MYS, no production change, no paid data, no synthetic observation, no inferred timestamp, no FX recapture, no aggregation. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
