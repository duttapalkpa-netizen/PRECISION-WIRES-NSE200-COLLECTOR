# IIP 2022-23 NIC classification resolution

Status: VERIFIED FOR DISSEMINATION LABEL; ITEM-BASKET MAPPING IS A DISTINCT CONCEPT

## Finding

The April 2026 first-release ledger's `classification=NIC-2025` is correct for the published NIC 2-digit IIP dissemination table. It must not be changed to NIC-2008 merely because the Microdata catalogue also mentions NIC-2008 in its item-basket description.

## Evidence hierarchy

1. The official MoSPI FAQ for the new IIP series, Question 28, asks which NIC classification will be used for dissemination at NIC 2-digit level and answers: NIC 2025.
   Source: https://mospi.gov.in/uploads/latestReleases/latest_release_1779857844835_f8e09093-f2ef-4fb3-9890-6149d4162032_FAQ_for_new_IIP_series_with_base_year_2022-23.pdf

2. The official 1 June 2026 first press release states that the detailed April 2026 tables at NIC 2-digit level are under NIC-2025 (PDF text, lines 119-121). Statement II-A labels the 10-32 manufacturing division rows as NIC 2025 (PDF text, lines 522-523; document page 5).
   Source: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_Press_Release_IIP_2022-23f.pdf

3. The Microdata catalogue's study description says the manufacturing item basket's 80%-output selection criterion is applied within each 3-digit industry of NIC-2008 (study-description lines 96-98). This describes the underlying item-basket/source selection frame, not the NIC 2-digit dissemination classification.
   Source: https://microdata.gov.in/nada/index.php/catalog/299/study-description

## Audit disposition

- Keep the ledger's `classification=NIC-2025` for NIC 2-digit published indices.
- Do not relabel the 23 rows as NIC-2008.
- Record NIC-2008 only as a distinct item-basket selection/mapping reference where relevant.
- This resolution does not establish later-vintage value cross-checking, raw PDF SHA-256, or public-use microdata access.
- The Output-PPI revised series superseded the 1 June WPI-based first release; the first-release ledger remains a historical first-release record, not a current revised-series acceptance.
- No production selector, score, diagnostic, source value, or hard-gate status is changed.

## Remaining blockers

1. Comparable PPI-based later-vintage source rows for the same NIC-2025 codes and reference month.
2. Raw PDF bytes and independently computed SHA-256.
3. Microdata public-use file access (portal requires a free account login).
