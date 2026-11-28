# GCR Continuation 294 — Georgia NBG Q3-2026 release-trigger pre-publication gate
Date: 28-Nov-2026 (Asia/Kolkata)
Scope: GEO only; fixed Q2-2026 63-country cohort; pre-release readiness, no premature vintage promotion.

## 1. Mandatory continuity preflight
- Re-fetched current main-branch Master Continuity Ledger (blob 7df2b12e2d9896de5241487115a1d7801d47f470), GCR Master Priority Queue (blob 87ee620a3a3559e97b8a186f2bd888074e6bc1e7), Historical Task Registry (blob a5d2d6a5f631e38a06525ddfc2f47337fdb91117), immutable 63-country matrix (blob 6daf8f9ea11d60fe94409b00fa777f39ebb5cbc6) and C293 report.
- Reopened Library Mother File: PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md. Its no-repeat protocol requires raw evidence, immutable IDs, and no promotion of UNKNOWN/BLOCKED/PARTIAL without fresh evidence.
- Reused GEO C261 calendar/revision-policy and BPM5/BPM6 conflict audit. Skipped repeat Q2 press-release scrape, stale NSDP snapshot, IMF re-query, cohort rebuild, and all accepted country numeric PASS work.

## 2. Official publication trigger re-confirmed
- NBG official Advance Release Calendar: https://nbg.gov.ge/en/statistics/data-distribution
- Under External Sector > Balance of Payments, November-2026 cell is listed as “30 Q3/2026”; this confirms the scheduled Q3-2026 BOP release trigger on 30-Nov-2026.
- As of this audit date (28-Nov-2026), the scheduled date is still in the future. No Q3 publication payload, Q2 revised portfolio A/L rows, Q2 methodology bridge, or observation-level revision identifier is claimed here.
- This is calendar verification only; absence of a release before its scheduled date is not evidence of a publication failure.

## 3. GEO acceptance boundary (unchanged)
| Gate | Result |
|---|---|
| Fixed cohort membership / archived IMF Q2 rows | Existing PASS retained |
| Official NBG release-calendar trigger | PASS — 30-Nov-2026 |
| Q3-2026 BOP payload available and captured | NOT YET DUE / NOT CAPTURED |
| Separate Q2 portfolio asset revision value | NOT_CAPTURED |
| Separate Q2 portfolio liability revision value | NOT_CAPTURED |
| BPM5/BPM6 Q2 methodology conflict | UNRESOLVED |
| Observation-specific national revision/vintage ID | UNKNOWN |
| GEO VINTAGE_PASS / FULL_PASS | NO / NO |
| Aggregate admission | NOT_AUTHORIZED |

## 4. Exact post-release action; duplicate prevention
On/after 30-Nov-2026, reopen only if the official NBG Q3 BOP release is actually published and accessible. Inspect:
1. Q2-2026 comparative/revised portfolio investment transaction assets and liabilities separately;
2. units, signs, transaction-vs-stock definitions and any BPM5/BPM6 methodology correction/crosswalk;
3. release/revision date, observation-specific version/revision identifier, and a defensible bridge to the archived IMF Q2 vintage.
Capture exact official URL, raw bytes, byte count, SHA-256 and receipt timestamp before considering any status change. If any leg or vintage bridge is absent, retain PENDING/UNKNOWN and move to the next eligible queue item. Do not use IIP stocks, net-to-leg back-solving, annual allocation, guessed timestamps, third-party mirrors or IMF re-query.

## 5. Protected invariants
₹0; free official sources only; immutable 63-country cohort; no production/selector/workflow changes; CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.

**Task result:** pre-publication trigger and exact acceptance checklist verified and recorded. The underlying GEO vintage task remains **PENDING** until the scheduled official release is available; no country gate or aggregate status is promoted.
