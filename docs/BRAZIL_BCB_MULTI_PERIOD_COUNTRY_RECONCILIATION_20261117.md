# Brazil BCB Multi-Period Domestic Portfolio Country Reconciliation — 2026-11-17

## Purpose and boundary
Extend the existing September-2026 one-period country validation without repeating source discovery or raw capture. This audit compares already archived latest-vintage SGS observations for domestic-market equity/fund and debt components with the exact monthly amounts stated in BCB's official monthly External Sector Statistics releases.

It is a **cross-vintage comparison**: the archived SGS CSVs were captured on 2026-11-17, while the cited monthly press releases were published earlier. A mismatch is not automatically a source error; it may reflect BCB's subsequent revisions. No historical press-release vintage raw dataset was available for these periods in this bounded audit.

## Inputs reused (no re-download)
- SGS 22930, domestic-market equity liabilities net: `bcb_domestic_market_crosscheck_202609/sgs_22930.csv`, blob `f7626bbc6b62630b6518451c472f718de3370175`.
- SGS 22936, investment-fund liabilities net: `data/raw/bcb/instrument_net_capture_20261117/sgs_22936.csv`, blob `3865fe689081cea11dff15227d01da4bb75925e0`.
- SGS 22942, debt securities issued in domestic market net: `data/raw/bcb/instrument_net_capture_20261117/sgs_22942.csv`, blob `3da8dc2b03da91e0dc9ff0861024c1ff17cce400`.
- All three files are preserved raw UTF-8 CSV with semicolon delimiter, decimal comma, USD million units; source rows run monthly through 2026-09. No data were re-fetched, transformed in-place, or overwritten.

## Sign and aggregation
The archived SGS series store liability net values with positive values representing net inflows and negative values representing net outflows for these selected series. For each reference month:
- Equity + investment funds = SGS 22930 + SGS 22936.
- Domestic debt securities = SGS 22942.
- Total domestic-market portfolio = (22930 + 22936 + 22942).
- Convert USD million to USD billion by dividing by 1,000.
- Compare independently rounded values to BCB's published one-decimal USD-billion figures. This is a comparison at the press release's stated display precision, not a general-purpose tolerance for series identities.

## Results
| Reference month | Equity + funds: SGS latest | BCB release | Match | Debt: SGS latest | BCB release | Match | Total: SGS latest | BCB release | Match |
|---|---:|---:|---|---:|---:|---|---:|---:|---|
| 2025-12 | -1.1 | -1.4 | NO | +5.3 | +5.3 | YES | +4.2 | +3.9 | NO |
| 2026-01 | +1.9 | +1.9 | YES | +6.9 | +6.9 | YES | +8.9 | +8.9 | YES |
| 2026-02 | +2.8 | +2.8 | YES | +2.8 | +2.6 | NO | +5.6 | +5.4 | NO |
| 2026-03 | -0.4 | -0.4 | YES | -2.5 | -2.5 | YES | -2.9 | -2.9 | YES |
| 2026-04 | +1.1 | +1.1 | YES | -0.5 | -0.5 | YES | +0.6 | +0.6 | YES |
| 2026-06 | -2.2 | -2.2 | YES | +1.6 | +1.6 | YES | -0.6 | -0.6 | YES |
| 2026-07 | +1.9 | +1.9 | YES | -0.7 | -0.7 | YES | +1.1 | +1.1 | YES |
| 2026-08 | -6.5 | -6.5 | YES | +1.3 | +1.3 | YES | -5.2 | -5.2 | YES |
| 2026-09 | -1.7 | -1.7 | YES | -0.4 | -0.4 | YES | -2.1 | -2.1 | YES |

Values are USD billions; positive = net inflow, negative = net outflow. The table shows independently rounded SGS calculations and BCB release values.

### Match summary
- 9 reference months checked.
- 7/9 months match all three release figures (Jan, Mar, Apr, Jun, Jul, Aug, Sep 2026).
- 23/27 component/total comparisons match at the release's one-decimal precision.
- Two reference months are vintage-sensitive exceptions:
  - Dec-2025: current SGS equity+funds is -USD 1.1bn vs release -USD 1.4bn; debt matches +USD 5.3bn; total is +USD 4.2bn vs release +USD 3.9bn.
  - Feb-2026: current SGS equity+funds matches +USD 2.8bn; debt is +USD 2.8bn vs release +USD 2.6bn; total is +USD 5.6bn vs release +USD 5.4bn.
- These are not silently accepted and not labelled data errors. They remain **VINTAGE_DIFFERENCE_UNRESOLVED** pending same-vintage data/revision bridge.

## Exact current-SGS values for the two exceptions

| Reference month | Equity + funds (USD mn) | Domestic debt (USD mn) | Total (USD mn) |
|---|---:|---:|---:|
| 2025-12 | -1,082.9 | +5,321.6 | +4,238.7 |
| 2026-02 | +2,786.2 | +2,783.2 | +5,569.4 |

The release values are published only to one decimal USD billion; the exact values above are the captured current SGS CSV values, not reconstructed historical release-vintage observations.

## Revision context
BCB's September-2026 External Sector Statistics release states that the revision covers definitive statistics for 2025 and revised estimates for 2026 (official release: https://bcb.gov.br/estatisticas/estatisticassetorexterno?kclid=KywNUB4ZA5A0GUTk). This is consistent with the possibility that a November-2026 SGS snapshot differs from earlier monthly press releases for December-2025 and February-2026. The specific numerical deltas have not yet been attributed to a documented series-by-series revision notice; therefore causation remains UNKNOWN.

## Acceptance
| Gate | Status |
|---|---|
| Reuse and integrity of three archived raw SGS files | PASS (existing archive hashes/commits retained) |
| Exact series identities and domestic-market scope | PASS (official BCB dataset metadata) |
| Nine-period latest-vintage comparison | PASS as executed |
| Full three-measure agreement across all nine periods | PARTIAL (7/9 periods) |
| Same-vintage press-release vs SGS comparison | NOT_DONE |
| Dec-2025 / Feb-2026 revision attribution | UNKNOWN / NOT_DONE |
| General all-period country equivalence | NOT_DONE |
| Brazil pilot acceptance | NOT_ACCEPTED |
| EM-wide panel | NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Next bounded action
Capture a matched-vintage bridge for the two exceptions only. Prefer official archived BCB release tables/XLS or the BCB historical-vintage dataset with a documented as-of date. Compare Dec-2025 and Feb-2026 values at the same publication vintage as the cited releases, then inspect the September-2026 revision's impact. Do not re-download the three current SGS files, re-run the September-only check, infer a blanket tolerance, or alter raw values.

## Safety and invariants
Research-only; ₹0 spend; official free BCB sources only. No synthetic data, no forward-fill, no invented timestamp/hash, no inferred revision cause. Keep BOP transactions distinct from IIP/CPIS positions. Do not modify Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, seed observations, parser admission, or production workflows.

## 2026-11-17 correction — authoritative hierarchy and scope qualification
A re-check against the current official BCB “Temas” catalogue found that the separate hierarchy map had mislabelled the debt codes. The authoritative catalogue states:
- 22942–22944 = debt-security liabilities negotiated in the **domestic market** (net / inflow / outflow).
- 22945–22947 = debt-security liabilities negotiated in the **foreign market** (net / inflow / outflow).
- 22948–22950 = foreign-market short-term debt; 22951–22953 = foreign-market long-term debt.
Therefore 22942 is **not** a short-term-only series. The previously archived 22942 raw CSV is the correct domestic-market debt net series. The hierarchy map was corrected in a separate commit; no raw data changed.

A second scope qualification remains: BCB's official topic catalogue labels 22930 as domestic-market equity liabilities, but labels 22936 only as investment-fund liabilities, without a domestic/foreign-market qualifier in the catalogue entry. Accordingly:
- Debt comparison (22942 against the release's domestic-market debt component): scope confirmed.
- Equity comparison (22930 against domestic-market equity): scope confirmed.
- Investment-fund component (22936 against domestic-market fund shares): market perimeter UNKNOWN until an authoritative BCB definition establishes the match.
- The arithmetic 23/27 numerical comparison result is reproducible, but it is **not** a full country-perimeter validation. The 7/9 three-number matches must not be interpreted as Brazil domestic portfolio country validation PASS.

### Revised acceptance
| Gate | Revised status |
|---|---|
| Correct domestic-market debt series mapping (22942) | PASS |
| Correct domestic-market equity series mapping (22930) | PASS |
| Investment-fund market perimeter (22936) | UNKNOWN |
| Nine-period numeric reproduction | PASS |
| Debt component comparison at release precision | 8/9 numeric matches; Feb-2026 unresolved |
| Equity+funds composite perimeter | PARTIAL / UNKNOWN |
| Total domestic-market portfolio perimeter | PARTIAL / NOT_ACCEPTED |
| Dec-2025 and Feb-2026 same-vintage revision bridge | NOT_DONE |
| Brazil pilot acceptance | NOT_ACCEPTED |
| EM-wide panel | NOT_DONE |
| Production integration | NOT_AUTHORIZED |

Authority: BCB official topic catalogue https://dadosabertos.bcb.gov.br/pages/temas; official dataset page for SGS 22942 https://dadosabertos.bcb.gov.br/dataset/22942-investimentos-em-carteira---titulos-de-renda-fixa---passivos---negociados-no-mercado-domestic; official dataset page for SGS 22936 https://dadosabertos.bcb.gov.br/dataset/22936-sgs.

Next: obtain an authoritative BCB definition for the market perimeter of 22936, then obtain same-vintage evidence for the Dec-2025 and Feb-2026 debt/equity/fund values. No inference from numerical coincidence, no blanket revision attribution, no raw overwrite.

## 2026-11-17 — Exact BCB Table 10 component and current-SGS comparison
A bounded extraction was added for the official BCB XLSX workbooks served under publication periods 202601, 202603 and 202610. All workbooks passed ZIP integrity and all three Table 10 accounting identities:
1. domestic-market equity (row 14) + investment-fund liabilities (row 20) = equity/funds subtotal (row 41);
2. domestic-market debt (row 24) = debt subtotal (row 42);
3. equity/funds subtotal + debt subtotal = domestic-market portfolio total (row 40).

### Market-perimeter crosswalk
- SGS 22930 maps to Table 10 row 14, domestic-market equity.
- SGS 22936 maps to Table 10 row 20, investment-fund liabilities. Footnote 1 states that the transactions concern a nonresident quota holder owning less than 10% of the net asset value of an investment fund in Brazil. In the same Table 10, row 41 combines domestic-market equity and funds, and row 40 totals the domestic-market portfolio. This supports the 22936 domestic-fund component mapping; the shorter catalogue label alone does not show the market qualifier.
- SGS 22942 maps to Table 10 row 24, domestic-market debt securities. Official topic catalogue confirms 22942–22944 domestic-market debt and 22945–22947 foreign-market debt. It is not a short-term-only series.

### Exact values: latest archived SGS minus BCB Table 10 values (USD million)
| Reference month | SGS 22930 vs row 14 | SGS 22936 vs row 20 | SGS 22942 vs row 24 | Equity/funds composite delta | Domestic total delta |
|---|---:|---:|---:|---:|---:|
| 2025-12 | +116.1748 | +211.6830 | +39.3771 | +327.8578 | +367.2349 |
| 2026-02 | -0.0374 | +0.0395 | +203.7078 | +0.0020 | +203.7098 |
| 2026-09 | -0.0023 | -0.0085 | -0.0462 | -0.0108 | -0.0570 |

The 2026-09 current BCB table (publication file 202610) matches the latest archived SGS values to within USD 0.1 million for each component. This independently supports the crosswalk and latest-SGS parser.

### Historical publication precision and file-vintage limitation
- January-2026 BCB press release (published 26-Jan-2026) reports Dec-2025 domestic-market portfolio total USD 3.9bn, comprising equity/funds -USD 1.4bn and debt +USD 5.3bn.
- March-2026 BCB press release (published 27-Mar-2026) reports Feb-2026 total +USD 5.4bn, comprising equity/funds +USD 2.8bn and debt +USD 2.6bn.
- Current SGS snapshot rounds to Dec-2025 -1.1bn equity/funds, +5.3bn debt, +4.2bn total; Feb-2026 +2.8bn equity/funds, +2.8bn debt, +5.6bn total. Thus the previously observed mismatches are real at the BCB press-release display precision.
- Important limitation: HTTP Last-Modified for the period-indexed 202601 and 202603 XLSX files served on 2026-11-17 is 19-Oct-2026 and 18-Oct-2026 respectively. These XLSX files are official historical tables but are not proven to be immutable original as-of-publication snapshots. The contemporaneous PDFs preserve the rounded published figures; the precise XLSX cell values are recorded as the BCB historical table files served in November 2026, not asserted as original-vintage exact values.
- 202610 XLSX Last-Modified is 26-Oct-2026 and its Sep-2026 Table 10 values agree with latest SGS to < USD 0.1m.

### Evidence files
- Raw XLSX and HTTP headers: data/raw/bcb/release_tables_202601/, data/raw/bcb/release_tables_202603/, data/raw/bcb/release_tables_202610/.
- Manifest: data/raw/bcb/BCB_HISTORICAL_RELEASE_TABLES_VINTAGE_MANIFEST_20261117.json.
- Exact extraction and component deltas: data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json.
- Reproducer: scripts/research/extract_bcb_domestic_portfolio_release_vintage.py.
- Capture Run #2 / ID 44090062072 (202601/202603) SUCCESS; capture Run #3 / ID 44090618010 (adds 202610) SUCCESS.
- Extraction Run #4 / ID 44090856672 SUCCESS; head 6b8cfc3daf489a04bd22db882343dc58342318b5; artifact ID 14330724185; artifact digest 9c6c2c2733c75a2b098c4180d556bf5208cd6cea06dccf85a86f32d86f42e8f1.

### Revised acceptance
| Gate | Status |
|---|---|
| BCB debt/equity/fund component crosswalk | PASS (Table 10 rows + footnote + Sep-2026 match) |
| Release Table 10 internal identities | PASS (all three workbooks) |
| Latest SGS vs 2026-10 BCB Table 10 Sep-2026 comparison | PASS (all components within USD 0.1m) |
| Dec-2025 current SGS vs historical release | VINTAGE_DIFFERENCE_CONFIRMED at published 0.1bn precision |
| Feb-2026 current SGS vs historical release | VINTAGE_DIFFERENCE_CONFIRMED at published 0.1bn precision |
| Exact original-vintage XLSX preservation | UNKNOWN (historical XLSX Last-Modified dates are Oct-2026) |
| Specific revision event/cause for Dec-2025 and Feb-2026 deltas | UNKNOWN / NOT_DONE |
| Brazil pilot acceptance | NOT_ACCEPTED pending documented revision bridge and full matured validation |
| EM-wide panel | NOT_DONE |
| Production integration | NOT_AUTHORIZED |

BCB/IMF metadata indicates published data may be revised when source information is revised; this general policy does not identify the cause of these specific deltas. Do not infer a specific revision event or date without evidence.

## Next bounded action
Retrieve any documented BCB revision notice or preserved as-of-publication data for Dec-2025 and Feb-2026, then reconcile against the 2026-10/2026-11 latest series. If no immutable original vintage is available, keep the exact revision attribution UNKNOWN and retain both published PDF values and latest SGS values as separate vintages. No synthetic values, no tolerance relaxation, no production integration.

## 2026-11-17 — 2025 annual revision bridge confirmed at published precision
The BCB September 28, 2026 official release explicitly states:
- The 2025 annual ordinary revision changed net portfolio-investment liabilities from USD 15.1bn to USD 17.6bn.
- It identifies reclassifications between direct investment and portfolio investment under the 10% ownership criterion for nonresident investors; the relevant ownership information was not available in foreign-exchange contracts.
- The September revision cycle covers definitive 2025 statistics and revised estimates for 2026.

A reproducible annual bridge was computed from the January-2026 Table 10 (2025 annual column) and the 12 monthly values in the current archived SGS snapshot:
| Measure | Jan-2026 Table 10 / prior value (USD mn) | Latest SGS 2025 sum (USD mn) | Latest minus prior (USD mn) |
|---|---:|---:|---:|
| Portfolio liabilities parent 22924 vs Table 10 total | 15,139.9821 | 17,569.2 | +2,429.2179 |
| Domestic equity 22930 vs Table 10 row 14 | -4,642.0254 | -4,525.9 | +116.1254 |
| Fund liabilities 22936 vs Table 10 row 20 | -302.7145 | +1,628.4 | +1,931.1145 |
| Domestic debt 22942 vs Table 10 row 24 | 20,229.1186 | 20,468.7 | +239.5814 |
| Domestic-market total vs Table 10 row 40 | 15,284.3787 | 17,571.2 | +2,286.8213 |

The current SGS 22924 2025 sum of USD 17,569.2m rounds to USD 17.6bn, matching the BCB September-2026 revised portfolio-liabilities figure at its published precision. This independently supports that the latest archived parent series reflects the 2025 annual revision. The largest domestic component movement is the fund-liability series 22936 (+USD 1.931bn year-on-year versus the January-2026 Table 10 vintage), consistent with the BCB-described direct/portfolio reclassification mechanism. This does **not** prove that every monthly Dec-2025 difference is caused by that mechanism; monthly allocation remains NOT_ATTRIBUTED.

For Feb-2026, the latest 22942 domestic-debt series exceeds the March-2026 historical Table 10 value by USD 203.708m. BCB's September release says 2026 estimates were revised, but the published text does not identify this specific Feb-2026 debt-series change. Its cause remains UNKNOWN / NOT_ATTRIBUTED.

### Revision evidence archive
- Official BCB release PDF: data/raw/bcb/revision_release_202609/202609_External_sector_statistics_text.pdf
- PDF bytes: 852,292; SHA-256: 2120db15085716f0c2a76270149cfbd2b40e8b9d57eb69d611b05bae8e72625e; HTTP 200; Last-Modified 05-Oct-2026.
- Reproducible bridge: scripts/research/audit_bcb_2025_annual_revision_bridge.py
- Machine-readable output: data/qa/BRAZIL_BCB_2025_ANNUAL_REVISION_BRIDGE_20261117.json
- Run #1 / ID 44091390515 SUCCESS; artifact ID 14330869727; archive digest 15d99f469b7cb9d461c47125dc9d1dec513e2edaa3deb744b7900c92e0ada971.
- Parent SGS 22924 raw file SHA-256: f3769425aed38b4ab6ddfce555f10d886d875d21e7c3e46338b7d9bc131524b2.

### Revised status
- 2025 annual parent-level revision bridge: PASS at published 0.1bn precision.
- 2025 annual component-level changes: quantified; fund liabilities carry the largest observed component delta.
- Dec-2025 monthly component revision attribution: PARTIAL / NOT_ATTRIBUTED.
- Feb-2026 debt revision attribution: UNKNOWN / NOT_ATTRIBUTED.
- Original immutable 202601/202603 XLSX as-of-publication snapshots: UNKNOWN; served files have Oct-2026 Last-Modified dates.
- Brazil pilot: NOT_ACCEPTED; EM-wide panel NOT_DONE; production integration NOT_AUTHORIZED.

## 2026-11-17 — February-2026 debt discrepancy isolated to February, not January
The March-2026 BCB Table 10 provides both February monthly values and Jan-Feb cumulative values. Subtracting the February monthly row from the Jan-Feb cumulative row yields an independently inferred January value. This allows the current SGS January value to be checked without inventing a separate vintage.

| Component | BCB-implied Jan-2026 | Latest SGS Jan-2026 | Latest minus BCB-implied (USD mn) |
|---|---:|---:|---:|
| Domestic equity 22930 | 3,752.9371 | 3,752.9 | -0.0371 |
| Investment funds 22936 | -1,824.4965 | -1,824.5 | -0.0035 |
| Domestic debt 22942 | 6,938.6408 | 6,938.6 | -0.0408 |
| Equity/funds composite | 1,928.4407 | 1,928.4 | -0.0407 |
| Domestic portfolio total | 8,867.0814 | 8,867.0 | -0.0814 |

All January components match within USD 0.1 million. The February 22942 debt difference remains +USD 203.7078 million, while February equity and funds match within USD 0.04 million each. Therefore the Jan-Feb cumulative debt discrepancy is isolated to February 2026; it is not a January carry-over or an equity/fund perimeter mismatch. The specific February revision event/cause remains UNKNOWN.

Reproducible extraction now records the Jan-Feb cumulative rows, inferred January values, identities and deltas in data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json. Updated extraction Run #5 / ID 44091831003 SUCCESS; artifact ID 14332500865; digest ee222deb9a1eabe10b0357ab1b1907f7696b764f5dfcfa2924166cb809f0cbfd.

### Revised next action
Investigate only the February-2026 SGS 22942 historical revision, using official BCB monthly revision notices or preserved series vintages. January 2026 is now closed at component level (within USD 0.1m). Do not repeat January, September-2026, or the 2025 annual revision bridge.
