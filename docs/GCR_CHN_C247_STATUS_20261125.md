# CHN C247
SAFE Q2 release inspected; archived IMF Q2 rows reused; asset sign mapping REVIEW; liability PASS retained only from prior matrix; vintage PENDING; full NO; aggregate NOT_AUTHORIZED. Detailed XLSX bytes not captured. No IMF re-query, no cohort rebuild, production unchanged.

## Evidence details
SAFE official Q2 release (index 000014453-2026-0068; 29-Sep-2026): https://www.safe.gov.cn/en/2026/0929/2458.html
Portfolio Investment Q2 table unit USD100m: balance -55; assets -488; liabilities +433. SAFE says BPM6; credit positive/debit negative; table values rounded; BOP data revised regularly.
Existing IMF archive (no re-query):
- CHN A_NFA_T Q2 +USD48,794,459,103.55; file blob 0b73c5c0da92a58421d7e0a783c21cab410faf45.
- CHN L_NIL_T Q2 +USD43,286,600,714.23; file blob de6db80eb1c00d09d2ed3c880dc828fb7aaaaaf9.
SAFE displayed magnitudes are USD48,800m and USD43,300m. Residuals vs IMF are USD5.540896m and USD13.399286m; SAFE display precision is USD100m, so ±USD0.5m cannot be tested from this abridged table. SAFE asset sign is negative while IMF A_NFA_T is positive; SAFE credit/debit footnote does not prove field-level sign mapping. Asset remains REVIEW. Existing liability PASS retained only as prior accepted matrix status, not re-proven from rounded table.
SAFE preliminary Q3 release (13-Nov): https://www.safe.gov.cn/en/2026/1113/2466.html. Q3 standalone table omits portfolio investment; first-three-quarters table is cumulative. No subtraction/back-solving.
Detailed SAFE time-series XLSX locator is known (index 000014453-2019-0016; 29-Sep-2026) but bytes, sheets, headers, hash and revision bridge remain NOT_CAPTURED.
Next: distinct supported official transfer route only; inspect exact workbook schema, separate Q2 legs, units/sign/revision metadata and hash. Do not repeat failed download or query IMF.
