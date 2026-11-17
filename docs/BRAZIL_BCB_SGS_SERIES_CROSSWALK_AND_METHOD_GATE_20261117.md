# Brazil BCB SGS Portfolio-Flow Series Crosswalk & Method Gate — 2026-11-17

## Purpose
Continue the previously committed Brazil BCB pilot without repeating endpoint discovery. This bounded audit expands the exact-series map and compares it with the BCB's 26-Oct-2026 External Sector Statistics release. It does not create observations, combine series, or authorize production use.

## Official series crosswalk

| SGS code | Official dataset title | Dimension | Frequency / unit | Current qualification |
|---|---|---|---|---|
| 22907 | Portfolio investment - Net acquisition of financial assets - monthly - inflows | Asset-side inflows | Monthly / USD million | Official catalogue identity verified; payload raw archive NOT_DONE |
| 22908 | Portfolio investment - Net acquisition of financial assets - monthly - outflows | Asset-side outflows | Monthly / USD million | Official catalogue identity verified; payload not fetched in this audit |
| 22906 | Portfolio investment - Net acquisition of financial assets - monthly - net | Asset-side net acquisition | Monthly / USD million | Official catalogue identity verified; payload not fetched in this audit |
| 22926 | Portfolio investment - Net incurrence of liabilities - monthly - outflows | Liability-side outflows | Monthly / USD million | Official catalogue identity verified in prior pilot; raw payload not validated |

All four catalogue pages identify BCB/Depec as publisher/maintainer, monthly frequency, coverage from 1995-01-01, and the SGS code. The asset-side pages link distinct JSON/CSV/WSDL/HTML resources. The asset-side general concept text describes portfolio investment instruments broadly (equity/fund shares and debt securities), but the catalogue page alone does not provide enough series-specific decomposition to assert exact instrument coverage or a signed accounting identity.

Official page evidence:
- 22907: https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows
- 22908: https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows
- 22906: https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net
- 22926: https://opendata.bcb.gov.br/dataset/22926-portfolio-investment---net-incurrence-of-liabilities---monthly---outflows

## Independent official release cross-check
BCB's External Sector Statistics press release dated 2026-10-26 reports portfolio investment in the domestic market as net inflows, with a monthly series and a last-12-month series. It states that in September 2026 portfolio investment liabilities traded in the domestic market recorded net outflows of USD 2.1bn: USD 1.7bn in equities/funds and USD 0.4bn in debt securities; the trailing 12-month domestic-market portfolio investment net inflow was USD 5.1bn.

Source: https://www.bcb.gov.br/content/statistics/externalsectorstatistics_prev/202610_External_sector_statistics_text.pdf

This release provides a useful official aggregate cross-check, but it is not proof that any one SGS series (22906/22907/22908/22926) is identical in coverage, sign, or perimeter to the release's domestic-market measure. Do not backfill SGS observations from chart values or infer exact monthly values from the chart.

## Methodology route
The 22906 and 22908 dataset pages point to BCB balance-of-payments methodological notes at https://www.bcb.gov.br/estatisticas/notasmetodologicas. The current retrieval view is JavaScript-dependent and exposed no readable note content. Therefore the methodology/sign reconciliation is still NOT_DONE; no claim is made that the series arithmetic has been reconciled.

## Decision and fail-closed rules
- Keep asset acquisitions (22906/22907/22908) separate from liability incurrence (22926).
- 22906 is a published asset-side net series; it is not automatically the same as net portfolio inflows into Brazil's domestic market.
- Do not calculate 22907 minus 22908 as a substitute for 22906 until BCB's definitions, revisions, coverage and sign convention are verified.
- Do not combine asset and liability series until the BOP accounting sign convention and perimeter are documented from BCB methodology.
- The press-release USD-billion domestic-market aggregate is an independent validation target only, not a source of fabricated SGS rows.
- Monthly data are macro-context inputs, not 1–3 day trade triggers.
- No synthetic values, timestamps, hashes, or inferred observations. No production integration.

## Gate status
| Work item | Status |
|---|---|
| Official identity of 22907 | PASS |
| Official identity of 22908 | PASS |
| Official identity of 22906 | PASS |
| Prior official identity of 22926 | PASS |
| Monthly periodicity and USD-million unit for asset-side series | PASS |
| BCB 2026-10-26 release provides independent domestic-market aggregate | PASS |
| Exact scope equivalence between SGS series and release aggregate | UNKNOWN |
| BCB methodological note content inspected | BLOCKED (JS-only retrieval view) |
| Series arithmetic and sign reconciliation | NOT_DONE |
| Raw bounded API payloads, HTTP metadata, byte lengths and SHA-256 | NOT_DONE |
| Reproducible observation QA / manifest | NOT_DONE |
| Country-period pilot acceptance | NOT_ACCEPTED |
| EM-wide panel | UNKNOWN / NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Progress (this bounded crosswalk task)
- Official series crosswalk expansion: 100% (metadata identity only).
- Independent official release cross-check: 100%.
- Methodological note content retrieval: 0% (route found, content not readable).
- Raw payload capture and immutable manifest: 0%.
- Sign/perimeter reconciliation: 0%.
- Production integration: NOT_AUTHORIZED.

## Next smallest high-value action
Use the exact JSON resources for 22906, 22907, 22908 and 22926 with a raw-byte-capable transport; capture one common bounded date range and full response manifest. Then inspect the BCB methodological notes through an accessible official document route and test whether 22906 reconciles to 22907/22908 before any liability-side integration. Do not repeat the failed web-renderer/raw-byte path; use a genuinely different transport or leave the raw capture gate open.

## Invariants
Research-only. Preserve Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and collector workflows. ₹0 spend. UNKNOWN never PASS.
