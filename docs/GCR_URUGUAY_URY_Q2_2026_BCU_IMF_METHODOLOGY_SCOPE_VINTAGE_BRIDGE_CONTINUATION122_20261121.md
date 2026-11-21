# Uruguay URY — Q2-2026 BCU/IMF methodology, scope and vintage bridge (Continuation 122)
Date: 2026-11-21 (Asia/Kolkata)

## Decision
A material part of the URY metadata gap is now closed: the BCU's country-specific methodology (updated December 2020) explicitly follows BPM6, defines portfolio investment, and documents source families for non-financial private corporations (EGESE), public-sector securities (BCU debt registers), regulated financial institutions (SSF financial statements), and pension-fund / external custody holdings. The current BCU SDDS page shows Q2/26 as the latest BOP period and portfolio investment net USD 710m; the linked BCU SDDS template explicitly reports portfolio investment in USD millions with separate P_123 and L_123 fields. The Q2 report itself marks the numbers preliminary and says components may not sum exactly because of rounding.

The IMF BOP panel receipt proves that the two broad IMF raw CSVs were retrieved on 2026-11-19 at 06:46:34Z and 06:46:35Z, with HTTP 200, exact byte counts and SHA-256 values. The normalized panel contains URY Q2-2026 A_NFA_T and L_NIL_T observations. However, the current IMF metadata dashboard landing page is dated 2026-11-18 and its country-specific interactive metadata could not be inspected through the available static page extraction. Neither the BCU Q2 PDF nor the IMF broad panel receipt establishes a matched same-vintage revision timestamp for URY. Therefore scope/methodology is substantially documented, but exact vintage equivalence remains NOT_ESTABLISHED. URY remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate rejection
- Re-fetched Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `dc83f74028794dec67293ac21f31d713e121d3b6`.
- Re-fetched GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `6491dbf4af0059d783cf981e4106f7dd5e5bbb49`.
- Re-fetched C121 report: `docs/GCR_URUGUAY_URY_Q2_2026_BCU_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_CONTINUATION121_20261121.md`, blob SHA `fe70fba8680b07994212b8f8c4a3bf0428683b95`.
- Reused IMF methodology report `docs/GCR_IMF_BOP_EMDE_PANEL_PART2_20261119.md` and independent evidence checkpoint; no IMF query, no repeat of BCU Table 9 extraction, no cohort rebuild.

## 2. BCU national methodology — direct evidence
- Official BCU methodology PDF: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Balanza%20de%20Pagos/metodologia_BPyPII.pdf
- Document cover says “Actualización MBP 6ª Edición, Diciembre 2020”; it states international accounts were harmonized with BPM6 and quarterly BOP/IIP series were disseminated from 2012 onward.
- BCU defines BOP as transactions/flows during a period and IIP as positions/stocks at a point in time; these are distinct accounting statements.
- Section II.3.2 “Inversión de cartera” (PDF text lines 788–797) defines portfolio investment as cross-border transactions in debt securities and equity holdings excluding direct investment and reserve assets.
- The BCU's stated source mapping:
  - Non-financial private-sector portfolio investment: EGESE survey. Corporate holdings abroad are captured through debt securities and equity in non-resident companies where ownership is below 10% and not related-party equity; both positions and flows are requested.
  - Non-resident holdings in Uruguay: captured through ownership in reporting companies where participation is below 10%; 10% or greater falls under direct investment.
  - Public-sector portfolio investment: BCU debt registers; electronic securities issued by BCU and Central Government, and non-resident holdings of government bonds are estimated from circulation less resident holdings; securities are market-valued and recorded on accrual basis.
  - Regulated financial institutions: SSF financial statements; stocks from balance sheets and transactions calculated from balance differences, taking account of original currency.
  - Pension-fund and external-custody portfolio assets: SSF records and external custody data from the financial system / Montevideo Stock Exchange; bank/financial institution surveys quarterly and Stock Exchange survey annually (footnote 9).
- This methodology is directly relevant to the institutional sectors shown in BCU Q2 Table 9 (public/private), but it does not expose a Q2-specific respondent coverage count, revision vintage, or a numerical source-to-IMF crosswalk.
- The methodological document is dated December 2020; it establishes compiler framework, not that every source/coverage detail remained unchanged in Q2 2026.

## 3. BCU SDDS publication metadata
- Current official SDDS page: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Documents/FMI/sddsuruguay.html
- The page states that its data correspond to the IMF DSBB-described categories, and that detailed data are linked in the last column. It gives general default caveats: final when first released unless otherwise indicated; not seasonally adjusted unless otherwise indicated.
- The current extracted SDDS table lists BOP latest period Q2/26 and Portfolio investment net USD 710m. This independently corroborates the Q2 report's published net line and latest-period label.
- The official SDDS template: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/SiteAssets/SDDSTemplate.html
- The template identifies Portfolio investment unit as “US dollars millions” and exposes distinct fields `P_123` and `L_123` (plus `PR_123` for previous period). The static search extraction does not resolve those field placeholders into exact numerical asset/liability values; do not treat them as captured observations. The Q2 report's Table 9 remains the numeric national dual-leg source used in C121.
- The BCU Q2 report explicitly marks the figures preliminary and states component sums may differ from totals due to rounding; therefore the general SDDS “final when first released unless otherwise indicated” is overridden for these marked preliminary Q2 values.

## 4. IMF source vintage and raw provenance — reused, not re-queried
- Receipt file: `docs/evidence/imf_bop_emde_20261119/source_artifact_receipt.json`, blob SHA `0dd4104c6e0765171a9e6fb5fd09608f93748e54`.
- Normalized panel: `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv`, Git blob SHA `2a8db2878cac6323bbad74ffa4035dc70e5e6b98`.
- IMF panel source receipt reports:
  - A_NFA_T broad CSV: retrieved 2026-11-19T06:46:34.357106Z; HTTP 200; 484,139 bytes; SHA-256 `677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e`.
  - L_NIL_T broad CSV: retrieved 2026-11-19T06:46:34.878465Z; HTTP 200; 451,290 bytes; SHA-256 `713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba`.
  - Dataflow IMF.STA:BOP(21.0.0), DSD IMF.STA:DSD_BOP(24.0.0), period range 2015-Q1 through 2026-Q3; indicator P_F; entries A_NFA_T and L_NIL_T; unit USD; frequency Q.
- The exact URY Q2 values are preserved in the normalized panel as raw OBS_VALUE with SCALE=6 and PRECISION=6. C121's /1,000,000 display remains a derived comparison field, not a mutation of source values or a universal conversion.
- IMF BOP country metadata dashboard: https://data.imf.org/en/dashboards/bop%20metadata%20dashboard ; publication date Nov 18, 2026. The dashboard's static landing page exposes no country-level metadata rows, and interactive URY metadata was not retrievable in this task.
- Consequently, IMF receipt time is known, but the IMF data vintage / last revised timestamp for URY's Q2 rows is NOT_CAPTURED. A retrieval timestamp is not a revision timestamp.

## 5. Vintage and scope bridge matrix
| Dimension | Evidence | Status |
|---|---|---|
| Period | BCU Q2 2026; IMF TIME_PERIOD 2026-Q2 | PASS |
| Frequency | BCU quarterly; IMF Q | PASS |
| Unit | BCU USD millions; IMF UNIT=USD, SCALE=6 preserved | PARTIAL: display bridge empirically aligns but no universal rule |
| Functional category | BCU portfolio investment; IMF P_F | PASS |
| Accounting legs | BCU Table 9 public/private asset/passive rows; IMF A_NFA_T / L_NIL_T | PASS |
| Sector scope | BCU public/private sector split and source mapping documented | PARTIAL: no row-level source/coverage bridge |
| Methodology | BCU MBP6 Dec-2020; IMF BPM6 dataflow | PASS at framework level |
| Preliminary/final status | BCU Q2 figures explicitly preliminary | PASS |
| BCU release/vintage timestamp | Not present in inspected PDF; SDDS page current but no archived vintage timestamp | NOT_CAPTURED |
| IMF Q2 row revision timestamp | Broad receipt captured 19-Nov; revision timestamp absent | NOT_CAPTURED |
| Same-vintage alignment | No matched source-vintage identifiers or revision history | NOT_ESTABLISHED |
| BCU PDF raw bytes / size / SHA-256 | Browser text extraction only; byte-preserving download attempt failed | NOT_CAPTURED |

## 6. Updated decision and next action
- C121 numeric dual-leg comparison remains PASS at published whole-million precision (all three asset, liability and net residuals within ±USD 0.5m).
- BCU methodology/source mapping and current SDDS period/unit corroboration are now documented.
- Exact same-vintage validation remains open. Do not upgrade URY to full PASS.
- Next useful action is a byte-preserving official retrieval of the BCU Q2 PDF and a direct country-level IMF metadata/vintage export (if exposed by the Nov-18 dashboard or BOP API). Capture exact URLs, timestamps, byte counts and SHA-256 before parsing. If those do not expose matched revision histories, keep same-vintage NOT_ESTABLISHED and move on without inventing an alignment.
- Do not rerun the IMF broad-panel query, re-extract BCU Table 9, or rebuild the cohort.

## 7. Protected constraints
₹0; official/free sources only. No synthetic data, no inferred scale/sign transform, no stock-as-flow, no net-to-leg back-solving, no cross-country vintage assumption, no IMF re-query, no cohort rebuild, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Sources
- BCU Q2-2026 BOP/IIP report, especially executive summary, Table 9 and preliminary/rounding notes: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Balanza%20de%20Pagos/informe_m6.pdf
- BCU BOP/IIP methodology, updated December 2020: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Balanza%20de%20Pagos/metodologia_BPyPII.pdf
- BCU current SDDS page: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Documents/FMI/sddsuruguay.html
- BCU SDDS template: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/SiteAssets/SDDSTemplate.html
- IMF BOP/IIP country metadata dashboard, published 18-Nov-2026: https://data.imf.org/en/dashboards/bop%20metadata%20dashboard
- IMF 2024 Uruguay SDDS annual observance report: https://dsbb.imf.org/Content/pdfs/AnnualReports/2024/URY_SDDS_AR2024.pdf
- Archived IMF source receipt: `docs/evidence/imf_bop_emde_20261119/source_artifact_receipt.json`.
