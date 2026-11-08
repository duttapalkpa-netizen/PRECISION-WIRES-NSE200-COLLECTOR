# IIP Series Transition Record — 2011-12 to 2022-23

Status: EVIDENCE-BACKED SERIES BOUNDARY
Recorded: 2026-11-08
Scope: Research data lineage only; no production selector or CORE-672 changes.

## Official evidence

### Last old-base release
- Ministry: Ministry of Statistics & Programme Implementation (MoSPI), NSO.
- Release: Quick Estimate of IIP for March 2026.
- Release date: 28 April 2026.
- Base: 2011-12=100.
- Official PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1777370981972_ac151bbf-29ab-4f2c-a10e-bd727a4d3564_IIP_Press_release_March_2026.pdf
- Includes Statement IV with monthly NIC-2008 two-digit manufacturing indices and 13-month series values through March 2026.
- PIB release page: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2256241&lang=2&reg=3

### First new-base release
- Ministry: MoSPI, NSO.
- Release: First press release of All India IIP new series with base year 2022-23.
- Release date: 1 June 2026.
- Reference month: April 2026.
- Base: 2022-23=100.
- Official PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_Press_Release_IIP_2022-23f.pdf
- PIB release page: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2267531&lang=1&reg=3
- Release states MoSPI revised the IIP base year from 2011-12 to 2022-23; new series includes revised item basket, weights and sectoral coverage.

## Correct interpretation of the earlier HTTP 404
- Earlier attempted old-series April-2026 file identifier: `IIPMFY26002APR`.
- Request returned HTTP 404; response SHA-256: `811de0d1fef7c9e0efae9cac56aa62dc5ddeff228cdb572326c97e6079a87030`.
- Given the official March-2026 old-base release and official April-2026 new-base first release, an April-2026 2011-12/NIC-2008 monthly vintage is not part of the published old-series continuation.
- Status for recovering an old-series April-2026 workbook: `NOT_APPLICABLE` based on the documented series boundary, not `NOT_RECOVERED`.
- Preserve the 404 response as audit history; do not treat it as a data-quality defect or keep retrying the retired identifier unless a separate official catalogue record proves a legacy April release existed.

## Data lineage and integration rules
1. Keep old series `BASE_2011_12 / NIC_2008` ending at reference month 2026-03.
2. Keep new series `BASE_2022_23 / NIC_2008` beginning at reference month 2026-04. The official FAQ identifies NIC-2008 as the current classification, but new series base, weights, basket and coverage are revised.
3. Do not concatenate index levels across bases; do not infer conversion factors or splice monthly values.
4. Keep both series in separate tables/partitions with explicit `base_year`, `classification`, `reference_period`, `release_id`, `release_date`, `vintage_type`, `source_url`, and source hash fields.
5. For overlapping annual growth comparisons, use only official MoSPI/PIB published comparative statements and label them as official growth-rate bridges; do not reconstruct comparability from raw index levels without a validated methodology.
6. Preserve release vintages and revisions separately. Later-release snapshots are not original first-release vintages.
7. UNKNOWN remains neither PASS nor FAIL; no synthetic observations.

## Audit conclusion
The prior “April-2026 missing legacy vintage” blocker is resolved as a series-transition misunderstanding. The old series terminates at March 2026; April 2026 belongs to the new base-year release. This closes only that recovery subtask and does not clear the IIP 41-vintage gate, all other factor/P0/event-study requirements, or the project-wide Hard Gate.

## Related verified evidence
- Run #254 / workflow ID `42507902637`: SUCCESS.
- Artifact ID `13628033276`, ZIP SHA-256 `a988e47f6679def45d3fa3316e5d3207040047a847cd19410458a40db1814f3b`.
- PIB supplementary sidecar: 69 rows across Apr-2025, Sep-2025 and Feb-2026, 23 NIC codes each.
- Independent cross-check against MoSPI March-2026 Statement IV: 69/69 values matched, 0 mismatches (recorded in continuity ledger).
- No production integration, PR merge, or change to protected V11.3 invariants.
