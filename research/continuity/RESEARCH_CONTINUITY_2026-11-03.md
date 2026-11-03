# PRECISION-WIRES V11.3 — Research continuity ledger
Updated: 2026-11-03 (UTC)

## Frozen invariants
- Production selector unchanged.
- RANKING_SCORE unchanged.
- +1 PRESSURE_FADE unchanged.
- CORE-672 / 672 diagnostics unchanged.
- UNKNOWN is neither PASS nor FAIL.
- No synthetic evidence rows, fabricated timestamps, unsupported source promotion, or hard-gate relaxation.
- Research spend remains ₹0; no paid APIs, licences, subscriptions, or external contact without explicit approval.
- Hard Gate remains BLOCKED until all evidence requirements pass.

## IIP 41-catalogue-record audit — verified facts
- Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
- PR: #17, https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/17
- Validation Run #41601065926 succeeded as a GitHub workflow, but its first artifact audit was BLOCKED_WITH_GAPS. Artifact ID 13213484457; SHA-256 a7085df03050850ff96fb2d7c5dc97e9f408f37fa72221caaf945093725983e3.
- The initial parser read both the monthly index and growth-rate sections as if they were the same measure. This generated 232,067 false/invalid comparison rows.
- Corrected index-only parser reduced the revision comparison output to 1,056 candidate differences across the legacy base-year snapshots; these still require estimate-stage/revision-policy reconciliation before promotion.
- Latest validation Run #41602595857 succeeded. Artifact ID 13215061946; SHA-256 45387e22c4718052e2bfc154bd6dcf08a0dd3d7c1413a8c913e7e4e3178c5022.
- Latest artifact audit: 41 catalogue rows; 40 unique table IDs; 40 unique reference periods; one duplicate catalogue ID IIPMFY25018AUG; 40 download successes and one HTTP 404; 35 parsed workbooks and five parse failures; 120,796 parsed observations and 1,056 candidate revision differences. Audit status remains BLOCKED_WITH_GAPS, Hard Gate BLOCKED.
- The two duplicate August-2025 catalogue entries collided on one local raw-file path in the first corrected run; separate per-record raw paths are required to prevent concurrent writes/truncated XLSX.
- Four May–August 2026 workbooks use a different format: title "Monthly Sectoral, Sub-sectoral/NIC 2 digit indices of industrial production", NIC-2025, base year 2022-23. They were not parsed by the NIC-2008/2011-12-only heading matcher.
- April-2026 catalogue record IIPMFY26002APR returned HTTP 404. Do not silently replace this with a later month's workbook. The official 1 June 2026 press release confirms April 2026 was the first IIP release with base year 2022-23, and the new series has a revised basket, weights and sectoral coverage.
- The apparent missing January-2026 catalogue reference period must not be interpreted as missing observation data without checking official Quick / First Revision / Final estimate release stages. MoSPI's published revision policy must be joined explicitly.

## Error learnings / controls
1. A successful Actions workflow means code executed and artifact uploaded; it does not mean the source audit itself passed.
2. Catalogue rows, unique table IDs, distinct release dates, raw workbooks, parsed workbooks, and monthly observations are separate counts.
3. Never combine index levels and growth rates in one series.
4. Keep 2011-12/NIC-2008 and 2022-23/NIC-2025 as separate series; do not compare or concatenate them without an explicit classification/base-year bridge.
5. Deduplicate catalogue entries for independent vintage counts, but preserve duplicate rows and provenance in the manifest.
6. Keep failed download and parser states explicit; never infer missing files or invent release timestamps.
7. Serialize XLSX parsing or otherwise protect parser state; use unique per-record raw paths to avoid concurrent writes.
8. Recompute manifest and artifact SHA-256 after every material change.

## Next bounded task
- Extend the parser to recognize both legacy NIC-2008/base-2011-12 and new NIC-2025/base-2022-23 workbook headings and preserve base_year/classification on every observation.
- Use unique per-record raw paths to eliminate duplicate-ID file collisions.
- Compare revisions only within the same base year, classification, NIC code and reference period.
- Resolve April-2026's 404 using an independently verified official source artifact; do not substitute the May-2026 workbook.
- Join official Quick / First Revision / Final stages and release timestamps before declaring revision audit complete.
- Preserve Hard Gate BLOCKED until every required evidence item is verified.
