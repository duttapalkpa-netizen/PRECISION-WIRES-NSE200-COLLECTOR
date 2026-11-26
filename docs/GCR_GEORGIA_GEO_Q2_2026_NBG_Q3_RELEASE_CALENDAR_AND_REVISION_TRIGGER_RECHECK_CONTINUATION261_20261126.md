# Georgia (GEO) Q2-2026 — NBG Q3 release-calendar and revision-trigger recheck
Date: 2026-11-26 (Asia/Kolkata)
Continuation: 261
Decision: The official NBG release calendar currently places the Q3-2026 Balance of Payments release on 30-Nov-2026 (November column). As of 26-Nov-2026 this is a future scheduled release, not an available Q2 revision bridge. NBG's revision policy confirms regular revision of preliminary prior-period data on release of the next period, but no Q2-specific revised portfolio A/L values or BPM5/BPM6 correction was located. GEO remains SOURCE_FOUND / PARTIAL / NOT PASS; Q2 national portfolio A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED.

## 1. Mandatory continuity / duplicate-prevention preflight
- Re-fetched the default-branch Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and immutable 63-country national validation matrix.
- Read the Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md` and the task-specific GEO C154 and C223 reports.
- Reused the fixed GEO cohort membership and existing archived IMF rows. No IMF query, cohort rebuild, duplicate Q2 press-release extraction, stale NSDP reuse, or third-party mirror use.
- CPV C260, MNE C259 and AGO C236 routes were excluded from repetition. C154/C223 already establish the original NBG Q2 release and statistics-data locator boundaries.

## 2. New official evidence — release-calendar trigger
- Official NBG Advance Release Calendar: https://nbg.gov.ge/en/statistics/data-distribution
- The currently rendered calendar is headed November-2026 through February-2027.
- Under External Sector → Balance of Payments, the November column lists `30 Q3/2026`; the next three month cells are blank in the captured table. The Q3/2026 BOP release is therefore scheduled for 30-Nov-2026.
- The current audit date is 26-Nov-2026. The scheduled release date is four calendar days ahead; this is a future trigger and cannot be treated as an already published Q3 report or Q2 revision.
- A bounded official NBG-domain search found the Q2 release (30-Sep-2026) and Q2 IIP release, but no published Q3 BOP article/table in the accessible results. This is a bounded search result, not proof of non-publication through every NBG channel.

## 3. New official evidence — revision policy
- Official NBG Data Revision Policy: https://nbg.gov.ge/en/page/data-revision-policy
- It states that regular revision occurs when data released on scheduled dates are preliminary, with revision upon release of statistics for the next period.
- It separately states that extraordinary revisions may be made retrospectively for more than a year in exceptional cases involving significant errors/omissions or methodology changes, with a corresponding public notice.
- This confirms the revision mechanism, but does not itself establish that the Q2-2026 portfolio observations have been revised, identify the values, provide a Q2-specific revision notice, or prove an observation-level vintage match.

## 4. Methodology conflict — retained, not silently resolved
- The official Q2-2026 BOP release dated 30-Sep-2026 explicitly says it is prepared under IMF BPM5: https://nbg.gov.ge/en/media/news/balance-of-payments-of-georgia-ii-quarter-2026
- C154 records NBG's 2014 methodology notice stating BPM6 compilation from Q1-2014 and presentation only in BPM6 since 2015: https://nbg.gov.ge/en/media/news/national-bank-of-georgia-started-compiling-balance-of-payments-statistics-according-to-new
- No Q2-specific NBG correction, metadata note, item crosswalk or publication-vintage explanation resolving this contradiction was found in this bounded recheck.
- Do not assume the Q2 release's BPM5 label is a typo; do not silently relabel it BPM6. Concept equivalence, sign/scale bridge and IMF item comparability remain NOT_ESTABLISHED.

## 5. Existing cohort / data boundary reused
- GEO remains a member of the immutable 63-country Q2-2026 cohort with both IMF panel entries already present.
- C154's archived raw IMF rows remain the prior evidence; no IMF re-query or rescaling was performed.
- NBG Q2 accessible release text does not provide separate portfolio-investment asset and liability transaction values. NBG's IIP aggregate assets/liabilities are stocks and cannot replace BOP transaction flows.
- No Q2 national portfolio A/L raw table/workbook, exact export URL, raw bytes, byte count, receipt timestamp, SHA-256, observation-specific revision ID, or Q2-specific methodology bridge was captured.

## 6. Acceptance
| Gate | Result |
|---|---|
| Fixed 63-country GEO cohort membership / archived IMF rows reused | PASS |
| Current official NBG release calendar retrieved | PASS |
| Q3-2026 BOP date verified as 30-Nov-2026 | PASS |
| Q3 release available as of 26-Nov-2026 | NOT YET DUE / NOT CAPTURED |
| Official NBG regular/extraordinary revision policy verified | PASS |
| Q2-2026 portfolio A/L revision values captured | NO |
| BPM5/BPM6 Q2 conflict resolved | NO |
| Q2 national portfolio A/L | NOT_CAPTURED |
| Observation-specific vintage | UNKNOWN |
| GEO full national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 7. Next exact action / no-repeat rule
- Do not retry the same Q2 press-release page, stale Q3/21 NSDP snapshot, or NBG Statistics Data shell without a newly exposed documented dataset locator.
- Reopen GEO after the scheduled 30-Nov-2026 Q3 BOP publication only if the official release is actually accessible. Inspect its Q2 comparative/revised portfolio asset and liability transaction rows, any BPM methodology statement, revision notes, unit/sign definitions and publication vintage.
- If the release does not expose Q2 separate portfolio legs or a Q2 methodology correction, keep GEO PARTIAL / UNKNOWN and move to the next eligible fixed-cohort member.
- No endpoint guessing, third-party mirror, IIP stock substitution, net-to-leg back-solving, annual-to-quarter allocation, unsupported conversion or aggregate admission.

## 8. Protected invariants
₹0; free official sources only; no IMF re-query/cohort rebuild; no fabricated data/timestamps; UNKNOWN never PASS; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; no workflow dispatch, merge or production integration.
