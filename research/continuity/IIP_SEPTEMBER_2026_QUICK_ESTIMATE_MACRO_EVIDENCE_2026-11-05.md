# IIP September 2026 Quick Estimate — Source-Locked Macro Evidence Entry
Reference month: September 2026
Official release: 28 October 2026, 16:00 IST (PIB)
Base year: 2022-23
Classification: NIC-2025 for manufacturing 2-digit dissemination
Source: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2329475&lang=2&reg=48

## 1. Officially reported values captured
- All-India IIP: 6.7% year-on-year growth; index 124.3 versus 116.5 in September 2025.
- Sector growth: Mining & Quarrying -6.2%; Manufacturing +7.6%; Electricity & Gas Supply +11.2%; Water Supply, Sewerage & Waste Management +5.8%.
- Manufacturing breadth: 17 of 23 NIC-2025 two-digit groups showed positive growth.
- Three strongest named manufacturing groups in the release: Electrical equipment +33.9%; Motor vehicles, trailers and semi-trailers +19.0%; Rubber and plastics products +19.9%. These are group growth rates, not contributions to aggregate IIP unless the release explicitly identifies them as such.
- Use-based growth: Primary +4.0%; Capital +10.4%; Intermediate +12.2%; Infrastructure/Construction +7.2%; Consumer durables +6.0%; Consumer non-durables +1.4%.
- Weighted response rate: September Quick Estimate 86.5%; August Final Revision 92.0%. The response rates belong to different reference-month estimate stages and must not be interchanged.
- The same release says August 2026 underwent Final Revision. This ledger does not substitute its earlier Quick Estimate value for the final revised value.

## 2. Timing and look-ahead safety
The release was published at 16:00 IST on 28 October 2026, after the regular cash-market close. For any daily scanner/event study, this information is unavailable to a 28 October pre-close decision. The first eligible trading-session feature date is 29 October 2026, subject to the official exchange calendar. Store both reference_month=2026-09 and publication_timestamp=2026-10-28T16:00:00+05:30; never backdate the information to September.

## 3. Research use in PRECISION-WIRES
- Treat the headline IIP growth, manufacturing growth and NIC-2 group breadth as Macro-Geo / sector-demand context and risk modifiers.
- Treat use-based indices as broad demand/capex context: Capital and Intermediate Goods are stronger than Consumer Non-durables in this release.
- Join NIC-2025 two-digit IIP group data to company sector/theme tags only where a documented many-to-many mapping exists. Do not infer company-level exposure from a broad NIC label alone.
- Do not convert the 17/23 breadth or any growth percentage into a production score, factor weight, expected stock return, or direct 2%-5%-10% prediction without out-of-sample validation.
- Response rate is a source-quality / estimate-maturity attribute, not a multiplier to adjust the published index.
- Preserve the Quick Estimate vintage as released; when later revisions arrive, append new vintage records rather than overwriting this one.

## 4. Files and QA
- Structured ledger: `research/data/iip_new_series_release_2026_09_official_metrics.csv` (19 rows).
- QA script: `pipeline/validate_iip_2026_09_release_metrics.py`.
- Manual QA workflow: `.github/workflows/iip_2026_09_release_metrics_qa.yml` (5-minute timeout).
- The validator derives manufacturing positive breadth as 17/23 = 73.9130%; this is a derived statistic, not a separately published MoSPI metric.
- QA workflow was committed but not dispatched in this session. No passing run or artifact ID is claimed.
- Raw PIB PDF binary was not acquired in this task; the CSV is source-attributed to the PIB release page, but raw PDF SHA-256 and independent PDF-cell reconciliation remain pending.

## 5. Current status
SEPTEMBER_2026_RELEASE_ID_AND_DATE: VERIFIED_FROM_OFFICIAL_PIB
RELEASE_METRICS_TRANSCRIBED: SOURCE_ATTRIBUTED_LEDGER_CREATED
PUBLICATION_CUTOFF: RECORDED_16_00_IST
MANUFACTURING_NIC2_BREADTH: 17_OF_23; DERIVED_SHARE_73_9130_PERCENT
RESPONSE_RATE_STAGE_SEPARATION: RECORDED
CSV_STRUCTURE_AND_TRANSCRIPTION_QA: WORKFLOW_PENDING
RAW_PDF_BINARY_SHA256: PENDING
OFFICIAL_NEW_SERIES_MONTHLY_HISTORY_2023_04_ONWARD: PENDING
REVISION_VINTAGE_PANEL: INCOMPLETE
MASTER_HARD_GATE: BLOCKED

## 6. Protected invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics or V11.3(A/B/C/D/E) logic changed. No old PASS artifacts overwritten. No synthetic rows, fabricated timestamps, unsupported source promotion or Hard Gate relaxation.