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

## Official-release gap crosswalk
- Added `research/continuity/IIP_OFFICIAL_RELEASE_GAP_CROSSWALK_2026-11-03.md`.
- January 2026: no dedicated catalogue workbook row, but January observation data exists in six later parsed vintages. Official Quick release is 2 Mar 2026 (PIB PRID 2234512); 30 Mar 2026 release (PRID 2246871) identifies January as Final. This is a catalogue-row gap, not missing observation values.
- April 2026: catalogue XLSX IIPMFY26002APR returned 404. Official 1 Jun 2026 release (PIB PRID 2267531) contains April Quick estimates in new 2022-23/NIC-2025 series. The 29 Jun 2026 May release (PIB archive relid 290616) states that its Output-PPI-based full series supersedes the earlier WPI-based series from 1 Jun. The May workbook includes April values, but is a later revised vintage and does not replace the failed April XLSX.
- Official revision schedule changed on 17 Apr 2025: from Quick + first revision + final to Quick followed by one Final estimate.

## Policy-derived stage-join sidecar — locally executed and independently hash-checked
- Reproducible builder committed: `pipeline/build_iip_revision_stage_ledger.py`.
- Machine-readable summary committed: `research/continuity/iip_revision_stage_ledger_summary_2026-11-03.json`.
- Joined all 125,220 parsed observations across 39 successful workbook vintages; zero unknown stage rows and zero unjoined revision-difference rows.
- Stage counts: 917 Quick; 529 First Revision; 894 Final; 69 Final Transition Backlog; 122,811 historical-panel rows.
- All 1,124 value-difference rows joined to previous/current vintage stage metadata and source hashes.
- 693 differences are policy-stage-aligned candidates (389 Quick→First Revision; 271 Quick→Final; 20 Quick→Final Transition Backlog; 13 First Revision→Final Transition Backlog). They are NOT certified revisions until each official release statement and method vintage is verified.
- 431 differences remain unresolved because one side is a historical-panel/out-of-window value (397 Historical Panel→Final; 15 Historical Panel→Final Transition Backlog; 19 Quick→Historical Panel).
- Methodology split: 1,056 legacy-base series comparisons; 68 Output-PPI superseding series comparisons. No cross-base-year comparisons.
- Local derived-file SHA-256: stage join CSV `4c97f1e1ba949d633b98d2cfb4894be0de44333661ec82a7c4f1ce756e933d1d`; observation-stage ledger CSV `bac0330f82e568065369692fbc6e86f3c57e864f6096c8043ad8ca7afa71e062`; summary JSON `1a7400df71aa2b5c0da1184a4416967ae3b3fb56e316d32382f3ddcf79fc7208`.
- This sidecar is a policy-derived classification, not an official source document. It does not change the source audit status or Hard Gate.

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
- Run the committed stage-ledger builder against the exact Run #41640521553 artifact in a reproducible GitHub Actions job and retain the resulting CSV/JSON artifact with SHA-256.
- Independently verify source-release publication timestamps and statement-level values for all candidate transitions; do not promote the 693 policy-aligned candidates to certified revisions before that join.
- Resolve the April 2026 catalogue XLSX 404 only from an independently verified official source; otherwise keep it explicitly unresolved and retain the official June 1 PDF / June 29 PPI-based workbook as separate alternate evidence.
- Correct the audit summary so missing catalogue periods and missing observation periods are reported separately.
- Preserve Hard Gate BLOCKED until raw-vintage coverage, release-stage provenance, same-snapshot evidence and all other required factors are verified.
