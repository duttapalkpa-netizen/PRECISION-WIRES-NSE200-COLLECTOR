# CDSL Daily FPI Date-Alignment Ledger — 2026-11-13

## Purpose
Consolidate only previously verified CDSL daily observations into a date-aligned coverage ledger. This is a coverage/provenance control, not a fabricated continuous time series and not a raw-archive acquisition.

## Source and date semantics
- Official CDSL daily route: https://www.cdslindia.com/eservices/publications/fiidaily
- Official SEBI FPI curation index identifies CDSL's latest daily, current-month and archive routes separately: https://www.sebi.gov.in/curation/fpi.html
- CDSL states that custodian/depository-reported confirmed data reflects trades conducted on and up to previous trading day(s). Therefore, the displayed/reporting date is not to be relabelled as the underlying trade date.
- CDSL confirmed-custodian observations must remain separate from same-day exchange provisional FPI/FII observations.
- A live web-index snapshot retrieved for this audit displayed 11-NOV-2026, while an earlier direct page observation in this research batch displayed 13-NOV-2026. This is a retrieval/cache/vintage discrepancy; neither observation is silently overwritten. The latest indexed result is not proof that 12- or 13-Nov data disappeared.

## Date-aligned observation ledger

| CDSL reporting date | Cash table | Derivatives table | Evidence / interpretation | Coverage state |
|---|---|---|---|---|
| 11-Nov-2026 | Captured; arithmetic and USD/INR cross-checks recorded in prior research artifacts | 9 product rows captured; EOD OI captured | Prior artifacts: `940fff57a820afd8a5deb44059e5e72e9d8150d4` and `c47907225a59b377fe34a7c37a765c14902301a9`. Current official indexed page independently displays 11-Nov cash and derivatives tables. | CASH PASS; DERIVATIVES PASS |
| 12-Nov-2026 | Not independently evidenced in the consolidated source records available for this ledger | 9 product rows captured; EOD OI and 11→12-Nov delta audited | Prior artifact: `ed68ee12dc9c73d9cadbc7dbf7383e424ae90076`. Do not infer cash coverage from derivatives coverage. | CASH UNKNOWN; DERIVATIVES PASS |
| 13-Nov-2026 | Captured; category arithmetic and USD→INR reconciliation recorded | 9 product rows captured; 12→13-Nov EOD OI delta recorded | Prior artifacts: `5ae4d16e7febee293a1f7a8d0b1b0d46b85e2b22` and `00aad92706288707e98c863f0ccf5aa24f12da23`. Earlier direct page observation displayed report date 13-Nov-2026. | CASH PASS; DERIVATIVES PASS |

## Exact limitations
1. The three reporting dates above are observed report dates, not a claim of three consecutive trading sessions or a complete date range.
2. 12-Nov cash is UNKNOWN, not FAIL and not inferred from 11-/13-Nov cash.
3. This ledger does not establish complete daily coverage before 11-Nov or after 13-Nov.
4. The visible daily archive list on the CDSL landing page and the current Latest/Current Month route are separate surfaces. An archive-list boundary is not proof of the end of daily data.
5. No original daily archive binary was acquired in this task. No raw-file byte count, MIME type, schema validation, or SHA-256 is claimed.
6. Do not fill any gap from fortnightly, monthly, quarterly or annual CDSL totals.

## Next data action
Acquire the missing 12-Nov cash observation only through an explicitly exposed official CDSL page/report link or browser-visible official export. Record retrieval timestamp, displayed reporting date, exact source URL, MIME type, byte count and SHA-256 before parsing. If no official artifact is exposed, leave it UNKNOWN and document the access limitation; do not guess a URL or synthesize a row.

## Acceptance ledger
| Check | Result |
|---|---|
| Known daily reporting dates consolidated | PASS (3 observed dates) |
| Cash coverage by date distinguished from derivatives | PASS |
| 11-Nov cash and derivatives | PASS |
| 12-Nov derivatives | PASS |
| 12-Nov cash | UNKNOWN |
| 13-Nov cash and derivatives | PASS (prior direct-page evidence) |
| Consecutive full daily coverage established | NOT ESTABLISHED |
| Full historical daily archive acquired | NOT ACQUIRED |
| Raw-file SHA-256/schema QA | NOT STARTED |
| Daily confirmed-vs-provisional reconciliation | NOT STARTED |
| Daily factor acceptance | BLOCKED |

## Invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic rows or timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; research-only; no PR merge.
