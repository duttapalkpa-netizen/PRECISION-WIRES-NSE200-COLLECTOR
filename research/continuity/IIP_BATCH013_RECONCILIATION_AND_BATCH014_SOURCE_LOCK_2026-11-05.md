# IIP revision audit — Batch 013 reconciliation and Batch 014 source lock
Date: 2026-11-05
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: fix/iip-41-vintage-audit-clean

## Batch 013 — February 2024: corrected official release mapping
- Quick vintage: `IIPMFY23090FEB`, source workbook `IndicesIIP2011-12Monthly_annual_feb24_NIC 2d_sectoralmonthly.xlsx`, declared SHA-256 `7e053a7421646b308cb6849cb92130e8254cd26a9a9f9d76e836e6ba4c192e26`.
- Quick official release: PIB PRID `2017772`, 12 Apr 2024. Official MoSPI PDF: https://mospi.gov.in/sites/default/files/iip/IIP_PR_12apr24.pdf
- First-revision vintage: `IIPMFY23094MAR`, source workbook `IndicesIIP2011-12Monthly_annual_mar24_NIC 2d_sectoralmonthly.xlsx`, declared SHA-256 `5c1fa4bfec7bec39a5a109660860924084069a46849af4042d12e554323844f7`.
- Correct first-revision official release is PIB PRID `2020239`, published 10 May 2024 at 17:30 IST. Official PIB page: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2020239&lang=2&reg=3
- The prior ledger's `2020261` mapping for this first-revision event is incorrect and must not be used as the official PRID. Retain the old ledger/artifact unchanged; apply the correction in a new reconciliation layer.
- Official PRID 2020239 Statement IV explicitly identifies February 2024 as the first-revised period (release text also states this). NIC 27, Manufacture of electrical equipment, February 2024 = `111.6`; the official table's February 2024 column is unambiguous. The Quick February 2024 NIC 27 value in PRID 2017772 Statement IV is `111.8`; revision delta = `-0.2`.
- The earlier `111.5` reading was a transcription/reading error in the prior adjudication. The official PRID 2020239 source and the source-ledger value both support `111.6`; do not retain 111.5 as an unresolved competing official value.
- Original workbook-cell revalidation ZIP SHA-256 (reported in the prior audit): `dbd8f1b26576eb57b29c062ac36d1b2d2cdd38b19e4771a962449d50ce593284`; reported 34/34 workbook-cell matches.
- Prior adjudication ZIP SHA-256: `24685a01a0b663de94a9944ac2a472b425b4e721f6da88dfbd51c6aa666820f8`.
- **Still pending:** raw PDF binary download and independently computed SHA-256 for the Quick and First Revision official PDFs. Browser-visible official HTML/PDF text is not a substitute for raw payload hashing. Until PDF bytes and hashes are captured, Batch 013 is not fully source-provenance certified. Preserve the reported 34/34 workbook check, but do not claim the full two-sided PDF-payload gate is complete.

## Batch 014 — March 2024: official source pair locked; cell audit not yet certified
- Quick vintage: `IIPMFY23094MAR`, declared workbook SHA-256 `5c1fa4bfec7bec39a5a109660860924084069a46849af4042d12e554323844f7`; official Quick release is PIB PRID `2020239`, 10 May 2024 17:30 IST.
- First-revision vintage: `IIPMFY24002APR`, declared workbook SHA-256 `db05a095e3b86cf4333ebae2fc2733931447dde7bd0fcde18c4122ca3c390963`; official First Revision release is PIB PRID `2024748`, 12 Jun 2024 17:30 IST. Official PIB page: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2024748&lang=2&reg=48
- PRID 2024748 states that March 2024 underwent first revision. The source master ledger currently maps the March Quick release to PRID `2020261`; correct official mapping is `2020239`. Keep the old master ledger immutable and record this correction in a new overlay.
- A material NIC 27 check requires adjudication before Batch 014 can be certified: the current master ledger records March 2024 NIC 27 First Revision as `124.3`, while the PIB Statement IV result surfaced for PRID 2024748 appears to show `124.7` for Mar-24. This is a **candidate source/workbook-vintage conflict**, not yet a confirmed mismatch, because the raw official PDF payload and exact workbook cell have not been re-opened and independently hashed in this pass.
- Required next test: retrieve the exact PRID 2024748 Statement IV PDF payload; independently hash it; verify the March-24/NIC-27 cell and adjacent rows; inspect the exact `IIPMFY24002APR` workbook cell and workbook SHA-256; compare PIB page, PDF table, workbook cell and ledger. If values differ, preserve both and classify `UNRESOLVED_SOURCE_ARTIFACT_VINTAGE_CONFLICT`; never overwrite one value or infer a correction.
- Batch 014 status: `SOURCE_PAIR_LOCKED_CELL_AUDIT_PENDING`; no certification claim.

## Operating controls
- The old master ledger and all historical PASS/UNKNOWN records remain preserved; corrections are append-only overlays.
- No synthetic rows, fabricated timestamps, unsupported source promotion or Hard Gate relaxation.
- UNKNOWN is neither PASS nor FAIL.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE or CORE-672 changes.
- Hard Gate remains BLOCKED until the full evidence requirements are satisfied.
