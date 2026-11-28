# GCR Continuation 293 — Kazakhstan NBK release-catalogue and vintage-boundary correction
Date: 2026-11-28 (Asia/Kolkata)
Task ID: GCR-C293-KAZ-NBK-RELEASE-CATALOGUE-01
Scope: Correct the classification of NBK's 30-Oct-2026 publication entry and establish what it does—and does not—prove for the existing KAZ Q2-2026 dual-leg vintage gate.

## 1. Mandatory preflight / duplicate prevention
- Re-read current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, immutable 63-country Q2-2026 matrix and relevant Library Mother File before selecting work.
- Re-opened KAZ C144/C145 and the existing national dual-leg report. Reused its official NBK N09 values and archived IMF raw rows; no repeated numeric comparison, no IMF re-query, no cohort rebuild and no repeated PDF extraction.
- KAZ remains a fixed 63-country member; current matrix gate state is DATA_CAPTURED / ASSET_PASS / LIABILITY_PASS / VINTAGE_PENDING / FULL_PASS=NO.

## 2. Official NBK release-catalogue check
Official NBK Balance of Payments page:
https://nationalbank.kz/en/news/platezhnyy-balans-vn-sektora
The current page lists two distinct entries:
1. “Balance of Payments of the Republic of Kazakhstan from 2000 to the first half of 2026” — published 30-Sep-2026; next publication 31-Dec-2026.
2. “Preliminary Estimate of the Balance of Payments of Kazakhstan for the 9 months of 2026” — published 30-Oct-2026; next publication 31-Dec-2026.
The 30-Oct entry is explicitly a **nine-month preliminary estimate**, not a second half-year/final Q2 report. C145's wording describing the 30-Oct item as an “additional half-year report” is corrected by this report. The catalogue lists the 9-month item at 26.38 KB; its direct file URL/content was not exposed in the retrieved page representation and no bytes/hash were obtained.

## 3. Official revision policy and time semantics
NBK official Balance of Payments metadata:
https://nationalbank.kz/en/news/metadannye/7253
The metadata states:
- BOP statistics use BPM6; quarterly; USD; transactions are resident/non-resident flows.
- Initial figures for a reporting quarter are preliminary; final data are published on day 90 after quarter-end.
- When final data for a quarter are released, previously published quarters may be updated for reporting clarifications, methodology or new sources.
- Revisions occur twice yearly, in October and April, covering the two years before the reporting year.
This establishes that October is an official revision window relevant to 2026 observations. It does **not** itself identify which Q2 portfolio legs changed, give an observation-specific Q2 release ID, or establish that the 19-Nov IMF archive was sourced from the exact same NBK revision payload.

## 4. Reused KAZ dual-leg evidence — unchanged
Existing C144/C145 official NBK Statistical Bulletin N09 (issue published 30-Oct-2026) reported Q2-2026 portfolio assets +USD1,545.1m and liabilities +USD4,448.9m. Existing comparison against the archived 19-Nov IMF rows passed at 0.1 USDm rounding precision:
- Assets residual NBK−IMF: +0.01930972407 USDm.
- Liabilities residual NBK−IMF: +0.02255375987 USDm.
These numeric PASS results are retained as historical evidence. They are not re-computed in C293 and do not independently establish synchronized vintage identity.

## 5. Vintage boundary decision
| Question | Result | Reason |
|---|---|---|
| Is 30-Oct NBK catalogue entry a second half-year report? | NO | Official page titles it “Preliminary Estimate … for the 9 months of 2026” |
| Is the 30-Sep 1H BOP publication distinct? | YES | Separate catalogue entry, 1H 2026 |
| Does NBK publish/revise historical quarters in October? | PASS | Official BOP metadata says twice-yearly Oct/Apr revisions over prior two years |
| Does October policy make Q2-2026 potentially revision-eligible? | YES | Q2-2026 lies within the stated two-year revision coverage |
| Does 30-Oct 9M title prove Q2 portfolio A/L revised values? | NO | Catalogue title/size/date do not expose portfolio legs |
| Is the 9M estimate's raw file/schema/rows/hash captured here? | NO | Link target/bytes not exposed in retrieved page representation |
| Is same-vintage NBK↔IMF proven? | NOT_ESTABLISHED | No exact revision payload receipt or IMF extraction-vintage metadata |
| KAZ VINTAGE_PASS / FULL_PASS | NO / NO | Retain PENDING / NOT_AUTHORIZED |

## 6. Next action and duplicate prevention
- Do not repeat C144 numeric extraction or C145 policy lookup.
- Next scheduled NBK BOP publication is 31-Dec-2026. At/after publication, inspect only the new Q3/final release and whether it republishes or revises Q2 portfolio asset and liability transaction legs separately, with release/revision metadata.
- The 30-Oct 9M preliminary estimate may be reopened only if a distinct supported official file URL or payload is surfaced; do not infer its contents from the title or file size.
- Require raw official bytes, exact URL, publication/revision date, file hash and both separate portfolio legs before any vintage promotion. Keep IMF archived receipt immutable; no re-query unless separately justified and approved.

## 7. Invariants
₹0; free official sources only; no paid APIs, external contact, synthetic data, net-to-leg back-solving, IIP-stock substitution, guessed timestamps, unsupported revision inference or aggregation. Fixed 63-country cohort unchanged. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.

Status: **TASK COMPLETE — RELEASE-CATALOGUE CLASSIFICATION CORRECTED; VINTAGE GATE REMAINS PENDING.**
