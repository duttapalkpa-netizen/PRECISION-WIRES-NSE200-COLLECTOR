# GCR 63-Country Q2-2026 Country-by-Country Master Status Matrix
Date: 2026-11-21 (Asia/Kolkata)

## Purpose and authority
This matrix is derived from the immutable 63-country Q2-2026 cohort CSV. It is a status-control artifact, not a claim that every country report has been fully re-audited. The cohort CSV proves only that both IMF panel entries (A_NFA_T and L_NIL_T) are present for 2026-Q2; it does not prove national-source validation.

- Immutable cohort: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`
- Cohort blob SHA-1: `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`
- Cohort size: 63 country rows; both IMF panel legs present on every row.
- Status rules: `NOT_STARTED` = no country-specific source evidence surfaced in the bounded inventory; `SOURCE_FOUND` = official source/locator documented; `DATA_CAPTURED` = national Q2 portfolio legs/data captured but not fully accepted; `ASSET_PASS` / `LIABILITY_PASS` = that leg passed its defined comparison gate; `VINTAGE_PASS` = both-leg same-vintage gate passed; `FULL_PASS` = all gates passed; `BLOCKED` = a named route/access/scope gate blocks further validation.
- A status is not inferred from the existence of a report filename alone. Where evidence was not strong enough, the status remains conservative.

## Snapshot counts
- Cohort members: 63
- SOURCE_FOUND or later: 58
- DATA_CAPTURED or later: 12
- Countries with an individual asset-leg PASS recorded in this matrix: 6
- Countries with an individual liability-leg PASS recorded in this matrix: 6
- VINTAGE_PASS: 0
- FULL_PASS: 0
- BLOCKED: 24
- NOT_STARTED: 4
- Aggregate admission: NOT_AUTHORIZED for all rows.

**Important:** These are conservative matrix counts from the bounded preflight inventory, not yet an exhaustive report-by-report re-audit of all 63 country histories. A country may have prior evidence not surfaced by the search inventory; do not interpret NOT_STARTED as proof no prior work exists. Likewise, a partial country report is not a FULL_PASS.

## Country matrix (machine-readable companion)
See `docs/evidence/gcr_2026q2_country_master_status_matrix.csv` for all 63 rows and per-gate statuses.

## Key known exceptions
- **ZAF:** SARB dual legs compared; liability PASS, asset REVIEW (FX residual exceeds strict rounding bound); not full.
- **CHN:** SAFE Q2 values captured; liability magnitude aligns, asset sign crosswalk unresolved; detailed XLSX blocked.
- **IDN:** BI Q2 dual legs captured; Nov-2026 revision identified; same-vintage bridge unresolved.
- **LKA:** Treasury Q2 dual legs captured and rounded values align; primary CBSL raw bytes/vintage bridge pending.
- **ARM:** CBA official source route found; export timed out; no national dual-leg values or bytes captured.
- **COL:** BanRep official series route inspected; data retrieval blocked.
- **ROU:** BNR interactive database locator found; JS-capable export not executed.
- **GEO:** NBG NSDP route inspected; no BOP payload exposed.
- **BIH:** CBBH interactive portal export not executed.
- **MDA:** BNM Reports Generator requires interactive execution.
- **NPL:** NRB XLSX route blocked; no values captured.
- **PER:** BCRP catalogue lacks confirmed public-sector asset series; scope unresolved.
- **SLB:** CBSI sign-convention conflict; scale/vintage unresolved.
- **SLV:** BCR source-family gate incomplete; no dual-leg validation.
- **BLZ:** CBB Q2 report H1-only; workbook bytes blocked.
- **BOL:** BCB Q2 XLSX routes blocked.
- **KOS:** BQK official XLS route returned 403; no values captured.
- **GMB:** CBG Q2 report has financial-account net only; no portfolio legs.
- **GIN:** BCRG report download target unresolved; net-only historic data not Q2 proof.
- **LAO:** BOL/NSDP XLSX/XML routes blocked; no bytes captured.
- **MNG:** NSO PxWeb metadata found; data endpoint inaccessible.
- **MNE:** CBCG bulletin table annotation target unresolved; dual legs not captured.
- **HND:** BCH XLSX/SDMX bytes blocked.
- **TZA:** BoT Q2 quarterly source appears net-only; no split legs.
- **PAK:** SBP Q2 BOP source does not expose separate Q2 portfolio legs; PARTIAL/BLOCKED.

## Acceptance and next steps
1. Re-audit each of the 63 country-specific report histories and update statuses only from exact report evidence.
2. For each country require national Q2-2026 portfolio net acquisition of financial assets and net incurrence of liabilities, source URL, native units, sign convention, observation vintage/revision, raw-byte receipt metadata and SHA-256 where downloadable.
3. Compare each national leg independently with the already archived IMF row. Do not net legs, infer one leg from net totals, substitute IIP stocks, or use H1/annual data as Q2.
4. Set `VINTAGE_PASS` only when both legs' observation vintage is explicitly aligned; set `FULL_PASS` only when both leg comparisons, scope, sign, scale, vintage and provenance gates pass.
5. Never sum or authorize the 63-country aggregate while any included country remains incomplete or the pre-registered coverage rule is unmet.

## Invariants
₹0; official/free sources only; no IMF re-query or cohort rebuild; no synthetic data or fabricated timestamps; UNKNOWN is never PASS; no production changes.