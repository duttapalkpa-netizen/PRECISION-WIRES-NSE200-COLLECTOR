# GCR Continuation 267 — Progress baseline reconciliation: historical 8-milestone score vs 63-country capture
Date: 2026-11-26

## Purpose
Resolve the apparent conflict between the previously reported 62.5% GCR progress and the later 46% figure. This is a measurement-definition and continuity-control task, not a claim that the full GCR is complete.

## Sources re-opened
- Current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry and 63-country matrix.
- Library conversation archive containing the historical GCR progress checkpoint and its milestone breakdown.
- Library Mother File continuation summary (pages 1–53 and addenda 55–57).

## Historical 62.5% checkpoint — confirmed
A prior GCR Overlay V1 progress record explicitly defined 62.5% as 5 of 8 equal-weight milestones. The record explicitly cautioned that this was not a weighted completion percentage for the entire research project.
The five milestone headings recorded as PASS were:
1. Overlay architecture and transmission-chain design.
2. Official source register and variable definitions.
3. CDSL India FPI evidence snapshot.
4. H.10 historical FX/dollar panel acquisition.
5. Schema, parser and categorical diagnostic tests.

At that historical checkpoint:
- Milestone 6 — Global Macro Data Ingestion: 20% documented.
- Milestone 7 — Relative Attraction + Sector–Stock Bridge: 0%.
- Milestone 8 — Historical Event Study / Backtest: 0%.
Thus 62.5% = 5/8 milestone-count score, not 62.5% of all data, gates, validation or production readiness.

## Later 63-country metric — separate denominator
The current immutable 63-country Q2-2026 matrix has 63 country rows:
- DATA_CAPTURED: 29
- SOURCE_FOUND: 14
- BLOCKED: 20
- FULL_PASS: 0
Therefore 29/63 = 46.03% is only a national-source capture-stage ratio. It is not an overall GCR completion score. It does not measure the eight milestone programme, Macro-Geo P0 completeness, Relative-Attraction/sector bridge, or historical validation.
C266's Tanzania net-only capture does not change the 29 DATA_CAPTURED count; it remains SOURCE_FOUND because separate portfolio assets/liabilities were not captured.

## Current cross-check and acceptance
- The latest Mother File addendum 55 reports Macro-Geo P0 6/8, with USD/INR NOT_CONNECTED and FPI/DII historical coverage insufficient; strict hard gate BLOCKED; candidate_release_allowed=false.
- Addenda 56–57 preserve USD/INR/FPI/DII source-route/terms blockers and no production release.
- Current 63-country matrix has 0 FULL_PASS countries and no vintage PASS country count.
- The old 62.5% checkpoint is historically valid under its original denominator. Its current-day milestone status has not been fully re-audited against a fresh eight-milestone acceptance checklist; therefore it must be labelled historical checkpoint, not current overall GCR completion.
- The prior 46% statement was incorrectly presented as overall GCR completion. It is corrected to 46.03% national-source capture-stage only.

## Reporting rule from now on
Always report three separate measures:
A. Historical Overlay V1 milestone checkpoint: 62.5% (5/8), date/context as historical; not current weighted completion.
B. Current 63-country national-source capture: 29/63 = 46.03%; denominator and status labels shown.
C. Overall GCR completion: NOT_COMPUTABLE / NOT_CERTIFIED until an auditable current status and explicit weighting/acceptance criteria for all eight milestones and dependent hard gates are reconciled. Never substitute A or B for C.

## Next genuine unfinished work
Continue Milestone 6 — Global Macro Data Ingestion only on permitted official source acquisition with exact raw bytes, source semantics, dates, vintage and SHA-256. Existing latest source-coverage evidence: 6/8 P0 groups; USD/INR disconnected; FPI/DII daily history insufficient; hard gate BLOCKED. Do not repeat closed source-route checks, do not bypass NSDL terms, do not infer missing daily rows. After permitted raw source coverage is established, update collector mappings/tests and run audit-only source coverage, event study and hard gate separately. Do not start Milestones 7–8 as if their upstream panel were accepted.

## Invariants
₹0; free official sources only; no IMF re-query/cohort rebuild; no stock/annual/H1/net substitution for transaction legs; UNKNOWN never PASS; H+3 minimum 50 matured observations per State; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; no merge, workflow dispatch or production integration without explicit approval.
