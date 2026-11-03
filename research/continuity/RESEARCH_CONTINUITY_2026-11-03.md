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
- Audit code commit: 16f382aabf984eca403e85fb0c701e36a5a35370.
- Run #41640521553 completed SUCCESS; its one validation job and all steps passed. This means the audit ran and artifact uploaded, not that the source audit itself passed.
- Artifact ID 13232127900; SHA-256 e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c; 3,203,900 bytes; 43 files.
- Audit status: BLOCKED_WITH_GAPS; Hard Gate BLOCKED.
- 456 catalogue records across 46 pages; 41 qualifying catalogue rows; 40 unique table IDs / 40 unique catalogue reference periods; one duplicate catalogue row excluded from independent-vintage download count.
- 39 workbooks downloaded and parsed; one HTTP 404; parse failures 0; 125,220 observations; 1,124 within-series value differences (1,056 legacy 2011-12/NIC-2008; 68 new 2022-23/NIC-2025).
- Failed workbook: IIPMFY26002APR, catalogue code 158504, Apr 2026, HTTP 404. Preserve as failed source evidence; do not substitute a later workbook.
- Earlier false cross-series differences were eliminated by comparing only within identical base_year + classification + NIC code + reference period.

## Official release-source verification — completed bounded pass
- Added `research/continuity/IIP_OFFICIAL_RELEASE_EVIDENCE_LEDGER_2026-11-03.md` and `iip_official_release_evidence_summary_2026-11-03.json`.
- 38 of 40 unique catalogue vintage rows have an independently located official PIB release page. Two remain UNKNOWN: July 2024 (`IIPMFY24014JUL`) and May 2025 (`IIPMFY25006MAY`). No neighbouring-month inference is used.
- April 2026 Quick Estimate is confirmed by official PIB PRID 2267531 / PDF, but the catalogue XLSX still has HTTP 404.
- May 2026 Output-PPI Quick Estimate is confirmed by PIB PRID 2278961 (29 Jun 2026); it supersedes the 1 Jun WPI-based new series. Keep the methodology break distinct.
- Legacy release-stage policy is explicit in PIB PRID 1931708: current month Quick, prior month First Revision, third-prior month Final. Revised policy is explicit in PIB PRID 2122427 (17 Apr 2025): from April 2025, Quick followed by one Final estimate in the next release.
- The source ledger records source workbook SHA-256 and download state alongside PIB ID, publication date/time, and URL. Unknown pages remain UNKNOWN.
- Ledger CSV SHA-256: `b5a1818fcf29642c4c55162fa34aeb61c13939cfab1e9796b187aa74c18a37df`; summary JSON SHA-256: `16e0996d7edb24ab9d3d892897cb3a76ddf50ee2ce971c51408e6f6b2060fd33`.

## Policy-derived stage-join sidecar — not certified revision evidence
- Reproducible builder committed: `pipeline/build_iip_revision_stage_ledger.py`.
- Joined all 125,220 parsed observations across 39 successful workbook vintages; zero unknown stage rows and zero unjoined revision-difference rows.
- Stage counts: 917 Quick; 529 First Revision; 894 Final; 69 Final Transition Backlog; 122,811 historical-panel rows.
- All 1,124 value-difference rows joined to previous/current vintage stage metadata and source hashes.
- 693 differences are policy-stage-aligned candidates (389 Quick→First Revision; 271 Quick→Final; 20 Quick→Final Transition Backlog; 13 First Revision→Final Transition Backlog). They remain candidates, NOT certified revisions.
- 431 differences remain unresolved because one side is a historical-panel/out-of-window value (397 Historical Panel→Final; 15 Historical Panel→Final Transition Backlog; 19 Quick→Historical Panel).
- Methodology split: 1,056 legacy-base series comparisons; 68 Output-PPI superseding series comparisons. No cross-base-year comparisons.
- Certified cell-level revision rows: 0. A release-page stage tag alone does not prove every cell-level difference; exact source statements and matching source payloads must be tied to each changed observation pair.
- This sidecar does not change the source audit status or Hard Gate.

## Error learnings / controls
1. A successful Actions workflow means code executed and artifact uploaded; it does not mean the source audit itself passed.
2. Catalogue rows, unique table IDs, distinct release dates, raw workbooks, parsed workbooks, and monthly observations are separate counts.
3. Never combine index levels and growth rates in one series.
4. Keep 2011-12/NIC-2008 and 2022-23/NIC-2025 as separate series; do not compare or concatenate them without an explicit classification/base-year bridge.
5. Deduplicate catalogue entries for independent-vintage counts, but preserve duplicate rows and provenance in the manifest.
6. Keep failed download and parser states explicit; never infer missing files or invent release timestamps.
7. Serialize XLSX parsing or otherwise protect parser state; use unique per-record raw paths to avoid concurrent writes.
8. Recompute manifest and artifact SHA-256 after every material change.
9. Catalogue reference-period continuity is not equivalent to observation-period coverage.
10. June 29 2026 Output-PPI revision is a methodology-vintage break, not an ordinary revision; preserve the June 1 WPI vintage separately.

## Next bounded task
- Resolve the two remaining official PIB page lookups (July 2024 and May 2025) and independently capture official publication timestamps.
- Perform exact statement-cell extraction for each of the 693 candidate value transitions; tie each side to source workbook/PDF payload SHA-256 and record source page/table/cell coordinates.
- Resolve April 2026 catalogue XLSX HTTP 404 only from an independently verified official source; otherwise keep it explicitly unresolved.
- Reconcile the 431 historical-panel/out-of-window differences and separate catalogue-period continuity from observation-period coverage.
- Preserve Hard Gate BLOCKED until raw-vintage coverage, cell-level revision provenance, same-snapshot evidence and all other required factors are verified.
