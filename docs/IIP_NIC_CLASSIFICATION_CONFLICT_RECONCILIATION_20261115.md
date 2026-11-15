# IIP NIC Classification Conflict Reconciliation — 2026-11-15

Status: SUBSTANTIVE SERIES CLASSIFICATION RESOLVED; OFFICIAL HTML FAQ PAGE CONFLICT RETAINED AS DOCUMENTATION DEFECT
Scope: Current IIP series with base 2022-23=100. This is a source-reconciliation decision only; it is not an IIP item-group/weight concordance or production approval.

## Question
Does the current 2022-23 IIP series disseminate manufacturing industry groups using NIC-2008 or NIC-2025?

## Evidence inspected

1. **MoSPI FAQ PDF — new IIP series, base year 2022-23**
   - Official document: https://mospi.gov.in/uploads/latestReleases/latest_release_1779857844835_f8e09093-f2ef-4fb3-9890-6149d4162032_FAQ_for_new_IIP_series_with_base_year_2022-23.pdf
   - The document identifies itself as “Frequently Asked Questions (FAQs) — Index of Industrial Production - New Series with Base year 2022-23”.
   - Question 28 explicitly asks: “Which NIC classification will be used in dissemination of the Index at NIC 2-digit level?”
   - Answer: “The latest version of NIC i.e. NIC 2025 will be used to disseminate the Index in the new series of IIP.”
   - This is the most directly scoped FAQ answer: it names the new IIP series and its NIC 2-digit dissemination.

2. **MoSPI / TAC-IIP official report-release press note, 25 May 2026**
   - Official document: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1779706122249_3b3add9b-577c-4a1e-a9be-0e2b1c3d6e2c_Press_Note_on_release_of_TAC-IIP_Report_on_base_revision_of_IIP_with_base_2022-23__25052026.pdf
   - The press note says the updated IIP series is aligned with NIC-2025.
   - It further specifies that manufacturing-sector indices at the 2-digit level of NIC-2025 were scheduled for the new-series release.
   - This is a direct new-series design statement from the Technical Advisory Committee report announcement.

3. **MoSPI / PIB September 2026 IIP release, published 28 October 2026**
   - PIB PRID: 2329475.
   - Official release: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475&lang=2&reg=48
   - Paragraph 5 explicitly says the September 2026 new-base release provides 2-digit NIC-2025 manufacturing detail.
   - Statement II-A is headed “Manufacturing at NIC 2 digit”; its first classification column is labelled “NIC 2025”.
   - The release states the 2022-23 base and gives the September 2026 quick-estimate vintage. This is operational dissemination evidence, not merely a proposal.
   - Preserve its vintage metadata: September 2026 is a quick estimate; weighted response rate 86.5%; August 2026 final revision response rate 92.0%.

4. **Conflicting MoSPI HTML FAQ landing page**
   - URL: https://mospi.gov.in/faq
   - The currently indexed “FAQs on Index of Industrial Production (IIP)” answer says the current base is 2022-23=100 but says the current series uses NIC-2008.
   - This conflicts with the more specifically scoped new-series FAQ PDF (Question 28), TAC-IIP new-series statement, and September 2026 operational release.
   - The HTML FAQ answer has no visible version/date context in the captured result establishing that it supersedes the detailed new-series FAQ PDF. Treat it as a live official-page content inconsistency / likely stale or erroneous answer, not as authority to relabel the operational 2022-23 series NIC-2008.
   - Do not silently delete or suppress this conflicting official page. Preserve it in the source register and raise for official clarification/correction if a formal external confirmation is later required.

## Reconciled decision

- Legacy IIP series, base 2011-12: NIC-2008 (preserve as its own series).
- Current IIP series, base 2022-23, effective from the new-series release beginning April 2026: NIC-2025 for manufacturing NIC 2-digit dissemination.
- The 2022-23 series classification decision is now **NIC-2025 — evidence-backed PASS**.
- The generic/current MoSPI HTML FAQ page remains **SOURCE_CONFLICT / DOCUMENTATION_DEFECT** because it states NIC-2008 for the same current base-year label.
- Do not treat NIC-2008 as the current 2022-23 manufacturing classification merely because the HTML FAQ page says so.
- Do not infer an item-group or weight bridge from the classification label. NIC-2025/NIC-2008 concordance remains a separate 4-digit class mapping; it does not by itself provide a valid 463-item-group IIP bridge or authorize aggregation.

## Impact on prior checkpoint and next work

- The 15 November “IIP classification applicability contradiction” UNKNOWN decision is superseded only for the narrow question “which classification is used for the current 2022-23 IIP NIC 2-digit manufacturing dissemination?” It is now resolved to NIC-2025 based on the three direct new-series sources above.
- Retain the old HTML FAQ contradiction as a recorded source defect; do not erase the prior audit commit or evidence.
- Reopen the NIC concordance extraction work only as a standalone research task if needed; keep production mapping and any IIP item-group/weight bridge blocked until exact source tables and mapping semantics are independently validated.
- No prefix-based roll-up, no synthetic mappings, no assumed one-to-one mapping, and no index-level splicing.
- The NIC-2025 4-digit concordance remains separate from IIP's NIC-2-digit published classification. Its full machine-readable extraction and QA must preserve partial mappings, aggregations, split continuation rows and forward/reverse multiplicities.
- No raw PDF bytes were downloaded or hashed in this reconciliation; no SHA-256 is claimed.

## Progress and acceptance

- Exact source comparison (new-series FAQ PDF, TAC-IIP press note, September release/table header, HTML FAQ): 100% — COMPLETE.
- Current 2022-23 IIP NIC 2-digit classification decision: 100% — PASS (NIC-2025).
- HTML FAQ inconsistency recording: 100% — COMPLETE as a documented discrepancy; official correction/clarification: NOT_DONE.
- Full NIC concordance binary archival / SHA-256: 0% — NOT_DONE.
- Full machine-readable NIC concordance extraction and parser QA: 0% — NOT_DONE.
- IIP-specific 463 item-group / weight bridge: UNKNOWN / BLOCKED.
- Project-wide IIP vintage gate and PRECISION-WIRES Hard Gate: unchanged; not passed by this document.

## Protected invariants

No synthetic data, fabricated timestamps, paid API, spend, external contact, production selector change, RANKING_SCORE change, +1 PRESSURE_FADE change, CORE-672 diagnostic change, workflow rerun, PR creation or PR merge. Existing PASS artifacts, run IDs, hashes and source vintages remain untouched.
