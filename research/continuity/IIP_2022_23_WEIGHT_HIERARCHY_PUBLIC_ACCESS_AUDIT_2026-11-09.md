# IIP 2022-23 Weight Hierarchy and Public-Access Audit
Date: 2026-11-09
Branch: research/iip-item-weight-public-access-audit
Scope: public Category-A weight reconciliation and official access-path verification; research-only.

## Decision
Public NIC-2025 manufacturing 2-digit weights reconcile at 23/23 codes. Exact item-group weights remain UNKNOWN / NOT ACQUIRED because MoSPI places item-level IIP data in Category B registered access. Non-commercial research access is free after registration, application and Data Access Agreement/Undertaking; no registration or request was submitted. The IIP master Hard Gate remains BLOCKED.

## Official weight hierarchy
MoSPI's new-series FAQ states:
1. Sector weights derive from FY2022-23 current-price GVA shares in NAS.
2. Manufacturing NIC-2 weights derive from ASI 2022-23 GVA shares.
3. NIC-2 weights distribute to NIC-3, then NIC-3 to NIC-4, using ASI 2022-23 GVA shares.
4. NIC-4 weights distribute to selected items by GVO contribution within the respective 4-digit industry.
5. Products are grouped by similarity within industry groups.
Source: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1779857844835_f8e09093-f2ef-4fb3-9890-6149d4162032_FAQ_for_new_IIP_series_with_base_year_2022-23.pdf

## Public weight arithmetic
Input: retained September 2026 official NIC-2025 manufacturing Statement II-A transcription, base 2022-23, release 2026-10-28 16:00 IST, 23 codes 10–32.
- Rows: 23; unique codes: 23; coverage: 10–32 complete.
- Displayed NIC-2 weights sum: 76.065.
- Official Manufacturing sector weight: 76.062.
- Difference: +0.003 percentage points, within ±0.005 rounding tolerance. No published value was altered or rescaled.
- Sector weights: Mining 11.053; Manufacturing 76.062; Electricity & Gas 10.865; Water/Sewerage/Waste 2.020; total 100.000.
- Source CSV SHA-256: 102bef6c87b95c1478686935d9a6f5fcacda90dce07ea48f36d09e340fc29b7f.

## Basket discontinuity
MoSPI FAQ states:
- Manufacturing groups: 405 (2011-12) → 455 (2022-23).
- Total groups: 407 → 463.
- Products: 839 → 1,042.
- 120 new groups added; 64 dropped.
No one-to-one item crosswalk or overlap count is inferred from these aggregate counts.

## Public source boundary
- Sector and NIC-2 weights: Category A/open access; reconciled above.
- ASI Volume I: public; publishes all-India 4-digit NIC-2008 industry estimates, including GVA. This is not itself a certified NIC-2025 IIP weight table. URL: https://mospi.gov.in/sites/default/files/asi_results/ASI%202022-23%20Volume%20I-compressed.pdf
- ASI Volume II: MoSPI says it contains product/by-product output at 3-digit industry level and is available as a CD-ROM publication; no binary acquired. URL: https://www.mospi.gov.in/sites/default/files/press_release/PR_ASI_30102024.pdf
- Item-level IIP production/indices are delivered through the microdata catalogue to registered users. GSDD 2026 classifies item-level IIP as Category B; non-commercial research access is free after registration, application and Data Access Agreement/Undertaking. URL: https://mospi.gov.in/faq
- No account created, no agreement submitted, no Category-B data requested/downloaded.

## NIC concordance safety
The 463-row NIC-2025↔NIC-2008 concordance is a classification crosswalk, not an IIP weight bridge. Partial and aggregated relationships prohibit direct weight transfer. Do not map by prefix, same-number code, or simple summation.

## Result
- Public NIC-2 weight reconciliation: PASS at stated scope.
- Sector total arithmetic: PASS.
- NIC-3/NIC-4 new-series weight bridge: NOT CERTIFIED.
- Item-level weights: UNKNOWN / NOT ACQUIRED (Category-B access).
- Old/new item-level crosswalk: UNKNOWN.
- Production integration: NOT APPROVED.
- Hard Gate: BLOCKED.

## Protected invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics or V11.3 engines changed. No synthetic rows, fabricated timestamps, inferred item weights, paid data or Hard Gate relaxation. Research spend ₹0.
