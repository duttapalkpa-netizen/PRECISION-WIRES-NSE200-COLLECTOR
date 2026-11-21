# GCR — Kazakhstan (KAZ) Q2-2026 NBK portfolio dual-leg numeric reconciliation
Date: 2026-11-21 (Asia/Kolkata)
Status: NATIONAL DUAL-LEG NUMERIC COMPARISON PASS (publication-rounding level); SAME-VINTAGE NOT_ESTABLISHED; full vintage acceptance PARTIAL.

## Progress Log / continuity preflight
- Reopened Master Priority Queue, Master Continuity Ledger and immutable 63-country Q2 dual-leg cohort before selection. KAZ is a fixed-cohort member. Repository search for KAZ Q2-2026 portfolio reports returned no dedicated national dual-leg report. No duplicate country audit; no IMF re-query/cohort rebuild.
- Selected KAZ because NBK publishes a Q2-2026 quarterly BOP table with separate Portfolio Investment / Net acquisition of financial assets and Net incurrence of liabilities, in USD millions.

## Official national source and values
- National Bank of Kazakhstan, Statistical Bulletin N09 (382), September 2026, table 1.3, Balance of Payments of the Republic of Kazakhstan, pages 9–10. Official PDF: https://nationalbank.kz/file/download/138795
- Table unit: million USD. Q2 2026 column is labelled 2026 II.
- Portfolio investment — net acquisition of financial assets: +1,545.1 USD million.
- Portfolio investment — net incurrence of liabilities: +4,448.9 USD million.
- NBK's earlier official methodology commentary states that in its financial-account presentation minus indicates capital inflow and plus indicates capital outflow. The table separately labels asset acquisition and liability incurrence; do not net the two or conflate either with income or IIP stocks.
- The NBK BOP page identifies direct, portfolio and other investment as BOP components and says the data report transactions over a period. BNS metadata says financial account reflects net acquisition of financial assets and net incurrence of liabilities; data are generated in USD and published quarterly.

## Archived IMF raw panel — reused, exact rows only
- Asset panel blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
- Liability panel blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
- KAZ Q2-2026 A_NFA_T raw OBS_VALUE=1545080690.27593; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- KAZ Q2-2026 L_NIL_T raw OBS_VALUE=4448877446.24013; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- Scale-6 presentation is used only to express the archived USD values in USD millions for comparison: assets 1,545.08069027593 USDm; liabilities 4,448.87744624013 USDm. No sign inversion or other transformation applied.

## Numeric reconciliation (rounding to national publication precision: 0.1 USDm)
| Leg | NBK Q2-2026 (USDm) | Archived IMF raw / 1e6 (USDm) | Difference (NBK−IMF) | Result |
|---|---:|---:|---:|---|
| Portfolio assets / net acquisition | +1,545.1 | +1,545.08069027593 | +0.01930972407 | PASS — rounds to same 0.1 |
| Portfolio liabilities / net incurrence | +4,448.9 | +4,448.87744624013 | +0.02255375987 | PASS — rounds to same 0.1 |
- Both independent legs match at the national table's displayed precision. This is a numeric comparison, not proof of identical data vintage.

## Vintage and raw-evidence boundary
- NBK's September 2026 Statistical Bulletin identifies itself as an official monthly bulletin and states that amendments/reclassifications/methodological clarifications may revise previously published indicators; December data are also updated annually after final turnover.
- NBK external-sector publication page lists the half-year 2026 BOP publication on 30-Sep-2026 and additional half-year report publication on 30-Oct-2026. The comparison source is the September statistical bulletin, and the archived IMF panel is from the 19-Nov-2026 archive. Exact matched-vintage extraction/revision timestamp for both series has not been established.
- Exact source URL and page/table coordinates are preserved, but the PDF binary was not saved into the repository during this task; national PDF SHA-256 and retrieval-time metadata NOT_CAPTURED. Do not claim raw-file hash verification.
- National sign convention is supported by NBK commentary; full series-specific bridge and identical vintage NOT_ESTABLISHED.

## Acceptance
| Gate | Status |
|---|---|
| Fixed cohort membership / archived IMF Q2 both legs | PASS (roster only) |
| Official NBK Q2-2026 BOP source | PASS |
| Separate national portfolio asset and liability values | PASS |
| National publication unit (USDm) | PASS |
| Archived IMF exact Q2 rows / blob provenance | PASS |
| Asset numeric comparison at 0.1 USDm | PASS |
| Liability numeric comparison at 0.1 USDm | PASS |
| Sign convention evidence | PASS (NBK published convention) |
| National PDF bytes / SHA-256 | NOT_CAPTURED |
| Exact same-vintage bridge | NOT_ESTABLISHED |
| KAZ country numeric gate | PASS at displayed precision; vintage qualification remains PARTIAL |
| Cross-country aggregate admission | NOT_AUTHORIZED |

## Next exact actions
1. Preserve the official NBK PDF binary with retrieval timestamp and SHA-256 in the evidence archive; retain exact source page/table metadata.
2. Obtain the matching NBK standard BOP workbook/report version used for the archived IMF vintage or a revision-history bridge, then establish same-vintage status.
3. Keep the two-leg numeric match as PASS at 0.1 USDm; do not elevate vintage gate or aggregate authorization until evidence is captured.
4. Advance to the next highest-value uncovered fixed-cohort country; do not repeat KAZ numeric extraction.

## Protected invariants
₹0; official/free sources only; no synthetic data; no IIP stock as BOP flow; no netting/back-solving; no unapproved sign/scale conversion; no IMF re-query; no cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.