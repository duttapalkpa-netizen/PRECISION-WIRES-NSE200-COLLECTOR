# Quarterly XBRL Extraction Runtime Guard — Continuation 241

Date: 2026-11-22 (Asia/Kolkata)
Branch: audit/prospective-selector-tracking

## 1. Continuity check and live run update
- Re-checked Run #372 (44991296424), avoiding repeat acquisition or dataset QA.
- Its XBRL metric extraction step has now completed successfully, and normalized quarterly metric validation/features step has also completed successfully.
- Run #372 is still in progress at corrected-label walk-forward audit. Macro-Geo, retrospective audits, reproducibility, hard gate, and final artifact upload remain pending.
- No artifact was available yet for Run #372.

## 2. Bounded extraction improvement
The prior XBRL extraction step had remained in progress for an extended interval while processing an unbounded-in-practice attachment queue (up to 500 disclosures by default and up to 8 attachment candidates per disclosure). To reduce CI runtime without weakening the evidence rules:
- Added reusable newest-first disclosure selection helper with explicit available/processed/truncated counts.
- Added a per-disclosure attachment-attempt cap, configurable by environment.
- The prospective audit workflow now sets a bounded CI profile: 30 newest result disclosures and at most 2 attachment candidates per disclosure.
- The extraction report now records available, processed, and truncated disclosure counts plus both caps. Truncated records are explicit; they are not silently represented as complete coverage.
- The module's default remains 500 disclosures / 8 attachments for non-CI use unless overridden.

Commits:
- Extraction runtime/coverage diagnostics: 438cc1c765d8c5fca68d5e836e86d06cc476d9fe
- Regression tests for cap/truncation: 5f392be909b0a0382ba93aac5498fdbc93e23db4
- Prospective workflow bounded profile: 3f2a8c87d301ba1163c5128f7e7973e52d1293ea

## 3. Verification state
| Item | Status |
|---|---|
| Existing Run #372 XBRL extraction | PASS |
| Existing Run #372 quarterly metric validation/features | PASS |
| New cap/truncation regression tests | CI step completed successfully in Quarterly Results Targeted Tests Run #129 |
| New bounded prospective workflow profile | CODED; Run #377 pending |
| Full new-profile end-to-end extraction | NOT YET VERIFIED |
| Run #372 corrected-label walk-forward | IN PROGRESS |
| Macro-Geo hard gate / prospective release | NOT YET REACHED |
| Completeness of all historical quarterly disclosures under 30-row CI cap | PARTIAL BY DESIGN; counts will be emitted, never implied complete |

Targeted test run:
- Run #129: 44991789531, commit 5f392be909b0a0382ba93aac5498fdbc93e23db4
- Step 5, "Run only quarterly disclosure and Run 121 regression tests": completed / success.
- Run #128 at the previous code-only commit was still in progress at last observation; no PASS claim made for it.

New prospective workflow:
- Run #377: 44991792513, commit 3f2a8c87d301ba1163c5128f7e7973e52d1293ea, pending at last observation.

## 4. Next exact actions
1. Verify Run #377's QA and bounded XBRL extraction steps against the new code.
2. Continue observing Run #372 walk-forward and downstream Macro-Geo/hard-gate steps; do not duplicate its successful steps.
3. If the bounded extraction still exceeds the job budget, tune only the audit-branch cap based on measured diagnostics; do not weaken provenance, basis, timestamp, or UNKNOWN rules.

## 5. Invariants
Audit-only branch. No production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, production workflow, or production data/model logic changed. ₹0 research spend; no paid APIs, synthetic financial data, guessed source contracts, or fabricated timestamps. UNKNOWN is never PASS.
