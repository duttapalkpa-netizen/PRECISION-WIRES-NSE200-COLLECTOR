# Batch 014 — official source binary acquisition checkpoint

Date: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean
Scope priority: 40% Macro/Geo provenance gate — required source evidence, not a predictive-factor contribution.

## Official release payloads located
The exact official MoSPI PDF URLs have now been independently located in MoSPI's indexed publication records:

1. March 2024 Quick Estimates, PIB PRID 2020239, 10 May 2024:
   https://www.mospi.gov.in/sites/default/files/press_release/IIP_PR_10may24.pdf
   Search-indexed official PDF source: https://www.mospi.gov.in/sites/default/files/iip/IIP_PR_10may24.pdf

2. March 2024 First Revision, included in April 2024 Quick Estimates release, PIB PRID 2024748, 12 June 2024:
   https://mospi.gov.in/sites/default/files/iip/IIP_PR_12jun24.pdf
   Alternate official path:
   https://mospi.gov.in/sites/default/files/press_release/IIP_PR_12jun24.pdf

The official PIB page confirms the 12 June release contains March 2024 First Revision and reports a weighted response rate of 96% for that revision. Official page:
https://www.pib.gov.in/PressReleasePage.aspx?PRID=2024748&lang=2&reg=48

The official 10 May PIB page identifies the March 2024 Quick Estimates release:
https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2020239&lang=2&reg=3

## Binary acquisition attempt and result
Attempted to retrieve both exact MoSPI PDF payloads through the available execution environment, including the canonical and alternate official paths. The runtime could not resolve the MoSPI host (DNS/network connection failure). No PDF bytes were obtained, so no raw PDF SHA-256 has been calculated. This is an acquisition-environment blocker, not evidence that the official files are missing or invalid.

The two source workbook files declared in the candidate ledger remain:
- Quick: IndicesIIP2011-12Monthly_annual_mar24_NIC 2d_sectoralmonthly.xlsx
  Declared SHA-256: 5c1fa4bfec7bec39a5a109660860924084069a46849af4042d12e554323844f7
- First Revision: IndicesIIP2011-12Monthly_annual_apr24_NIC 2d_sectoralmonthly.xlsx
  Declared SHA-256: db05a095e3b86cf4333ebae2fc2733931447dde7bd0fcde18c4122ca3c390963

Exact-name Library searches and repository file search did not return either workbook binary. No replacement or reconstructed workbook was generated. These declared hashes must not be treated as independently verified until the exact bytes are acquired and hashed.

## Verified vs pending
- Official PIB release identities and dates: VERIFIED.
- Official MoSPI PDF direct URLs: LOCATED / URL-VERIFIED.
- PDF payload bytes: NOT ACQUIRED.
- Raw PDF SHA-256: PENDING.
- Quick and First Revision XLSX bytes: NOT LOCATED.
- Workbook SHA-256 revalidation: PENDING.
- Prior 19/19 two-sided PIB HTML cell crosswalk: remains PASS, unchanged.
- Full NIC-2 cohort coverage: UNKNOWN / outside the 19-row policy-aligned cohort.
- Batch 014 full source-provenance certification: BLOCKED.
- Master Hard Gate: BLOCKED.

## Next execution target
Acquire the two exact official PDF payloads and both original XLSX workbooks through a reachable official source path or an existing retained artifact. Immediately compute SHA-256 over raw bytes, compare to the declared workbook hashes, preserve the original binaries, and append a hash manifest. If bytes remain inaccessible, retain the explicit blocker; do not promote a page-text match into binary provenance certification.

Controls unchanged: immutable historical ledger and PASS artifacts retained; no synthetic rows, fabricated timestamps, unsupported source promotion, or gate relaxation. UNKNOWN is neither PASS nor FAIL. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, and A/B/C/D/E production logic remain unchanged.
