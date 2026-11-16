# FII/DII Two-Scope CSV Byte and Arithmetic Reconciliation

Date: 2026-11-16 (Asia/Kolkata)  
Status: **BYTE HASH + INTERNAL ARITHMETIC PASS; OFFICIAL DOWNLOAD PROVENANCE / SCOPE AUTHENTICATION UNKNOWN**  
Scope: Research-only analysis of the two latest CSV files already saved in the user's ChatGPT Library. No production code or mapping policy is changed.

## 1. Exact source files inspected

| Library filename | Library file ID | Library created (UTC) | Bytes | SHA-256 |
|---|---|---:|---:|---|
| `fii-dii-nse-latest.csv` | `file_00000000acf88211b0c893f07f75c306` | 2026-11-16 10:25:25 | 218 | `b733444b5a846abb672226bc96448bc0baea2da0ad15fe810207fbe93aad7f18` |
| `fii-dii-combined-latest.csv` | `file_0000000081b48211ad1ab54222986804` | 2026-11-16 10:25:25 | 218 | `2697546fa012f4c08449b37a3eb7d0f8298f296c25fd8ce4b7ca134c37999eb2` |

Both exact raw CSV byte streams were materialized from Library and SHA-256 hashed. They are distinct byte streams (different SHA-256), despite identical byte lengths.

## 2. Row-level arithmetic validation

Observation date in both files: `13-Nov-2026`. Currency/unit: ₹ crore.

| File label | Category | Buy | Sell | Reported net | Buy − Sell | Arithmetic |
|---|---|---:|---:|---:|---:|---|
| NSE | DII | 10,561.32 | 12,532.05 | -1,970.73 | -1,970.73 | PASS |
| NSE | FII/FPI | 17,376.50 | 12,122.52 | 5,253.98 | 5,253.98 | PASS |
| Combined | DII | 11,745.95 | 13,999.53 | -2,253.58 | -2,253.58 | PASS |
| Combined | FII/FPI | 18,339.57 | 12,603.02 | 5,736.55 | 5,736.55 | PASS |

All four rows satisfy BUY − SELL = NET to the reported two decimal places. Categories and date are present. Each file has exactly one DII and one FII/FPI row for the same date.

## 3. Combined minus NSE-only differences

| Category | Buy difference | Sell difference | Net difference |
|---|---:|---:|---:|
| DII | +1,184.63 | +1,467.48 | -282.85 |
| FII/FPI | +963.07 | +480.50 | +482.57 |

The two datasets are not interchangeable. The combined-minus-NSE-only differences are material and category-dependent. Do not substitute one scope for the other, add them together, or choose one as canonical without an explicit source-scope policy.

## 4. Official page context

The official NSE FII/FPI & DII report page displays two separate report sections:
- “FII/FPI & DII trading activity on NSE in Capital Market Segment”
- “FII/FPI & DII trading activity on NSE, BSE and MSEI in Capital Market Segment”

Each section has its own CSV download control. This confirms that NSE publishes two distinct scopes. The page text extraction available during this audit did not expose the actual underlying download URLs or response headers for these two controls.

Official page: https://www.nseindia.com/reports/fii-dii

## 5. Evidence boundaries / acceptance

- Exact Library bytes and SHA-256: **PASS**.
- CSV schema/date/category presence: **PASS** for these two one-day files.
- BUY − SELL = NET arithmetic: **PASS**, 4/4 rows.
- Same-date scope comparison: **PASS** as a descriptive comparison only.
- Authentication that each file was downloaded from the correspondingly named NSE control: **UNKNOWN** (no preserved exact request URL, response headers, or contemporaneous capture manifest attached to these Library files).
- Historical/rolling coverage: **NOT_AVAILABLE** from these two one-day files.
- Twenty-session maturity: **UNKNOWN / NOT_MATURE**; one distinct observation date only.
- CORE-672 mapping/aggregation policy: **NOT_AUTHORIZED / NOT_DONE**.
- Live raw API response and same-session API-to-both-CSV reconciliation: **NOT_RUN**.

The file names and values are consistent with the two official NSE report scopes, but names alone do not authenticate the download source. Do not promote the file scope to authenticated provenance.

## 6. Next bounded action

Run the isolated live-capture utility in a network-enabled research environment against the official NSE page, preserve exact raw API bytes and both CSV responses with query-redacted URL provenance, HTTP metadata and SHA-256. If the site does not expose stable distinct CSV URLs to the utility, retain ACCESS_BLOCKED and require the exact URLs copied from the two official controls. Then compare the API row values against both CSVs for the same observation date. No production mapping change until this gate passes and the minimum matured-session requirement is separately met.

## 7. Protected invariants

No change to Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 56×12, Engines A–E, collector production workflows, or any production mapping. No synthetic data, no invented timestamps, no inferred canonical scope, no PR merge.
