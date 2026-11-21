# Hungary (HUN) Q2-2026 — MNB/IMF portfolio source and methodology crosswalk
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 138
Status: Official national Q2 BOP source and separate portfolio legs captured; MNB methodology/revision policy captured; cross-currency numeric reconciliation NOT_DONE; same-vintage NOT_ESTABLISHED; HUN PARTIAL / NOT PASS.

## 1. Continuity preflight and selection
- Reopened Master Continuity Ledger (current blob SHA 3f16a4b4a72607fd722b691e6a7d62645a554ce4), current GCR Master Priority Queue (blob SHA 51aabd96e1b759a409e1157e42fdf15ee05f2a5e), immutable 63-country Q2 both-leg cohort (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e), current MEX C137 report, and the existing archived IMF raw asset/liability panels.
- HUN is a member of the fixed 63-country 2026-Q2 cohort. No dedicated HUN national portfolio Q2 dual-leg validation report was present in the repository tree during preflight.
- MEX same-vintage gate cannot be resolved before the next Banxico Q3 release scheduled for 25-Nov-2026; COL's newly documented BanRep BOP API route is not listed as supported in the current SDMX guide. HUN therefore selected as the next executable unvalidated cohort member with a current official Q2 BOP publication exposing both portfolio legs.
- No IMF re-query, no cohort rebuild, no repeated completed country comparison.

## 2. Official MNB Q2-2026 BOP source
- Official source: Magyar Nemzeti Bank (MNB), “Balance of payments and International Investment Position — 2026 Q2”, English Statistics Portal PDF.
- Publication date: 25-Sep-2026 (shown on PDF p.1 / extracted page 0).
- Official PDF URL: https://statisztika.mnb.hu/sw/static/file/bpm6-kozlemeny-2026-q2-en.pdf
- PDF p.3 / extracted page 2, “Net lending (FA) by instruments”, paragraph “By instruments” reports:
  - Portfolio investment net assets diminished by EUR 6,277 million.
  - Assets expanded by EUR 2,104 million.
  - Liabilities expanded by EUR 8,380 million.
- The same source identifies this as “Net lending (FA) by instruments”, so the values are financial-account transaction flows, not closing IIP positions. The separate asset and liability legs are explicitly stated and are not back-solved from the net line.
- Displayed rounded identity: 2,104 − 8,380 = −6,276 EURm, while the MNB narrative reports net assets −6,277 EURm. Preserve the EUR1m rounding difference; do not force equality or alter a component.
- The MNB Q2 release states that quarterly BOP and related IIP data are published for the first time in this release and that BOP data were revised retroactively from the beginning of 2022.

## 3. Official MNB methodology and revision semantics
- Official methodology: MNB, “Methodology applied in compiling balance of payments and international investment position statistics (BPM6)”, September 2024.
- URL: https://statisztika.mnb.hu/sw/static/file/bop_modszertani_megjegyzes_2024_szept_hu.pdf
- p.4 / extracted page 3, paragraphs 62–66:
  - MNB publishes external-sector statistics in HUF and EUR.
  - Currency-by-currency monthly flow data are converted to HUF using MNB official daily middle exchange rates averaged over the month.
  - Quarterly flows are calculated by summing the individual monthly data.
  - EUR-published flow data are derived from HUF data using the monthly-average HUF/EUR rate.
- p.5 / extracted page 4, paragraphs 128–134:
  - Historical observations are revised with quarterly publications.
  - March and September are the longer revision windows (four years); June and December mainly revise the open year and preceding four quarters.
  - Under normal revision cycles, BOP data are considered final only after 15 quarters following the reference year.
- p.6 / extracted page 5, paragraphs 143–153: BOP is a flow measure; IIP is a stock measure and stock changes also include valuation and other volume changes. No IIP closing-stock substitution is allowed.
- p.21 / extracted page 20, paragraphs 580–593: portfolio investment is a distinct financial-account instrument; the financial-account data are subject to the normal BOP revision policy.
- p.26 / extracted page 25, paragraphs 729–752:
  - Portfolio investment includes traded securities excluding those classified as FDI or reserve assets.
  - Assets are securities issued by non-residents; liabilities are securities issued by residents.
  - Primary data source is MNB securities statistics; transactions are calculated from position changes after removing price and exchange-rate effects.
  - Some household holdings at foreign custodians are estimated because direct observation is incomplete.
- These methodology details are relevant to concept and vintage alignment; they do not establish an exact observation-level MNB↔IMF vintage match or the precise mapping of MNB narrative values to IMF item codes.

## 4. Existing archived IMF exact HUN Q2 rows — reused
- Existing archived raw panel CSV blob SHAs:
  - Asset panel: 15449e87c9057291a1f52f2f8cd9805df55f9fb8.
  - Liability panel: 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Exact rows in the archived panel for HUN, 2026-Q2:
  - A_NFA_T, P_F, USD, Q, OBS_VALUE=2434272117.820269, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
  - L_NIL_T, P_F, USD, Q, OBS_VALUE=9813617187.260281, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
- The raw OBS_VALUE and SCALE attributes are preserved exactly as archived. No division, rescaling, sign flip or currency conversion is applied in this report.
- No exact HUN-only IMF API request was issued; the existing 154-country panel rows were reused.

## 5. Reconciliation boundary and decisions
- National-source values are published in EUR million; archived IMF observations are in USD with SCALE=6. MNB's own methodology requires monthly currency-specific HUF conversion and monthly-average HUF/EUR conversion, then quarterly aggregation. A simple quarterly ECB EUR/USD average would not reproduce this method and is not accepted as an exact bridge.
- No HUN monthly source-currency observations or matched monthly FX calculation were acquired in this bounded task. Therefore cross-currency numeric residuals are NOT_COMPUTED; no numerical pass is claimed.
- MNB Q2 publication vintage is 25-Sep-2026 and includes a retroactive revision back to 2022. The IMF panel was acquired 19-Nov-2026, but its observation-level source-submission/revision timestamp is not present in the archived raw rows. Acquisition date is not the source vintage. Same-vintage alignment remains NOT_ESTABLISHED.
- MNB portfolio source construction from security-position changes net of valuation effects is a valid BOP flow source, but detailed item-level crosswalk and any differences in coverage/estimation must be verified before full country admission.
- HUN status: official national separate-leg source PASS; MNB methodology/revision policy PASS; raw MNB PDF bytes/SHA-256 NOT_CAPTURED; exact cross-currency reconciliation NOT_DONE; exact item/concept equivalence NOT_ESTABLISHED; same-vintage NOT_ESTABLISHED; full national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## 6. Acceptance matrix
| Gate | Status |
|---|---|
| HUN membership in fixed 63-country Q2 both-leg cohort | PASS |
| Official MNB Q2-2026 BOP source retrieved/read | PASS |
| Separate portfolio asset and liability values | PASS (EUR 2,104m / EUR 8,380m) |
| Portfolio net line independently reported | PASS (EUR -6,277m) |
| Rounded component identity | REVIEW (EUR1m display difference retained) |
| MNB BOP currency conversion method | PASS |
| MNB revision calendar and Q2 vintage date | PASS |
| MNB portfolio instrument definition/data source | PASS |
| Existing IMF exact HUN Q2 raw rows | PASS (reused) |
| Exact cross-currency FX aggregation / residuals | NOT_DONE |
| Exact item-level equivalence to IMF A_NFA_T/L_NIL_T | NOT_ESTABLISHED |
| Same-vintage MNB ↔ IMF bridge | NOT_ESTABLISHED |
| HUN full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 7. Next exact actions
1. Obtain the official MNB monthly BOP flow/FX tables or an exact MNB export that exposes HUF and EUR monthly portfolio legs plus the monthly conversion series; preserve original units and publication vintage.
2. Reproduce the MNB documented monthly conversion sequence exactly; do not use a simple quarterly EUR/USD average or the unadmitted monthly candidate.
3. Resolve whether MNB “assets expanded / liabilities expanded” map item-by-item to IMF A_NFA_T / L_NIL_T and account for MNB security-statistics coverage/estimation.
4. Search for an observation-level MNB Q2 revision snapshot corresponding to the IMF panel's underlying source vintage; if no exact bridge exists, keep NOT_ESTABLISHED and advance to another fixed-cohort member.
5. No IMF re-query, no cohort rebuild.

## 8. Protected invariants
₹0; free official sources only. No synthetic data, fabricated timestamps, unapproved scale/sign conversion, stock-as-flow, net-to-leg back-solving, duplicate IMF requests, or cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.
