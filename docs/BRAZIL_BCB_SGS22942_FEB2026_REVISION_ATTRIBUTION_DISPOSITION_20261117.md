# SGS 22942 February 2026 Revision Attribution — Official Evidence Disposition
Date: 2026-11-17 (Asia/Kolkata)
Status: INVESTIGATION COMPLETE; SPECIFIC REVISION CAUSE UNPROVEN

## Executive finding
The February-2026 difference in SGS 22942 is real, isolated to the February observation, and compatible with BCB's published revision framework. However, no official source inspected in this bounded investigation identifies a specific February-2026 SGS 22942 revision, its effective date, or the underlying transaction/compilation cause. The correct disposition is `REVISION_POSSIBLE_UNATTRIBUTED`, not `REVISION_CONFIRMED`.

## Exact discrepancy (USD million)
- SGS 22942 is officially titled "Portfolio investment - Debt securities - issued in the domestic market - monthly - net"; BCB Open Data Portal metadata gives monthly frequency, million USD, and temporal coverage from 1995-01.
- February-2026 contemporaneous publication Table 10 row 24: 2,579.492203640002.
- Latest archived SGS 22942 observation (raw capture 2026-11-17): 2,783.2.
- Latest minus publication table: +203.707796359998.
- The same March-2026 Table 10 provides Jan-Feb cumulative values. Subtracting February from Jan-Feb gives January 2026 6,938.640771049998; latest SGS January is 6,938.6, a difference of -0.040771049998. Therefore the mismatch is isolated to February and is not a January carry-over.
- Existing extraction identities in Table 10 (row 24 = row 42; row 41 + row 42 = row 40) pass. Existing source raw SHA-256 and workbook SHA-256 are preserved in the vintage extraction JSON and manifest.

## Official revision-policy evidence
1. BCB's published June-2023 third-edition DSTAT revision policy states that short-term ordinary revisions can occur at the same frequency as publication, may incorporate new information, revised estimates, correction of source/compilation errors and quality validation; low-impact routine revisions need not receive detailed disclosure. It also says balance-of-payments revisions may occur monthly and may reach back to January of the preceding year when necessary. This establishes that an observation can legitimately change after first publication, but it does not prove this specific 22942 change.
2. BCB's September-2026 statistics page identifies a fourth-edition DSTAT revision policy and says the annual BOP/PII revision was consolidated in September; that release covers definitive 2025 statistics and revised current-year 2026 estimates.
3. The September-2026 release explicitly reports a 2025 portfolio-liability revision from USD 15.1bn to USD 17.6bn, linked to direct/portfolio reclassification where a nonresident investor individually owns at least 10% of an investment fund. The same release's 2026 discussion identifies revisions mainly in direct-investment estimates. It does not identify a February-2026 SGS 22942 domestic debt-security revision or quantify +USD 203.708m for that month.
4. The 24-Feb-2026 release discusses table publication changes, not a February 22942 revision. The 24-Apr-2026 release documents a separate extraordinary travel-receipts revision over Oct-2023 to Feb-2026, not debt securities.
5. The March-2026 Table 10 workbook downloaded 2026-11-17 reports HTTP Last-Modified 2026-10-18. Therefore it is an official BCB historical-period workbook as served in October 2026, not proven to be an immutable original March-2026 publication-vintage workbook. The contemporaneous March PDF preserves only rounded values (+USD 2.6bn debt); it does not provide the exact original-vintage value or an audit trail.

## Evidence sources
- BCB Open Data Portal SGS 22942: https://opendata.bcb.gov.br/dataset/22942-portfolio-investment---debt-securities----issued-in-the-domestic-market---monthly---net
- BCB DSTAT revision policy (June 2023, 3rd edition): https://www.bcb.gov.br/content/estatisticas/Documents/notas_metodologicas/Politica_de_Revisoes_de_Estatisticas.pdf
- BCB external-sector statistics page, 28-Sep-2026 release (4th-edition policy / 2025 and 2026 revision description): https://www.bcb.gov.br/estatisticas/estatisticassetorexterno
- BCB Feb-2026 release (published 24-Feb-2026): https://www.bcb.gov.br/content/estatisticas/hist_estatisticassetorexterno/202602_Texto_de_estatisticas_do_setor_externo.pdf
- BCB Apr-2026 release (published 24-Apr-2026): https://www.bcb.gov.br/content/estatisticas/hist_estatisticassetorexterno/202604_Texto_de_estatisticas_do_setor_externo.pdf
- BCB Mar-2026 historical Table 10 workbook: `data/raw/bcb/release_tables_202603/bcb_external_sector_tables_202603.xlsx`, SHA-256 `3590b1bf3baded2a12c5ec747329bdd0fb7be10b26043eba99b64f8de9f75017`, Last-Modified `Sun, 18 Oct 2026 18:30:04 GMT`.
- Latest SGS 22942 raw: `data/raw/bcb/instrument_net_capture_20261117/sgs_22942.csv`, SHA-256 `4c09c850decf3317d27d1c0f4dc4aa68dc4f0b3aa2aafacfece113ff7f9c7169`, retrieved 2026-11-17T11:49:18.232400+00:00.
- Exact extracted values and Jan-Feb inference: `data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json`.

## Investigation decision
- Discrepancy existence: PASS.
- February-only isolation (January within USD 0.1m): PASS.
- Table 10 arithmetic identities: PASS.
- General BCB revision-policy compatibility: PASS.
- Specific revision event/date/cause for February 2026 SGS 22942: UNKNOWN / NOT_PROVEN.
- Original March-2026 workbook vintage immutability: NOT_PROVEN.
- February-2026 22942 reconciliation: BLOCKED pending exact same-vintage evidence.
- Brazil pilot acceptance: NOT_ACCEPTED.
- EM-wide panel: NOT_DONE.
- Production integration: NOT_AUTHORIZED.

## Next bounded action
1. Do not repeat raw capture, Table 10 extraction, January inference, or September-2026 validation.
2. Seek a BCB-issued immutable historical release version or a documented SGS revision/version log for February-2026 22942. The BCB monthly BOP ZIP already archived in this repository is dated 2019-03-22 and cannot validate 2026; do not misapply it.
3. If no historical version endpoint or official archived vintage exists, record that limitation and begin prospective monthly vintage snapshots for 22942 (and peer BOP series) with source URL, retrieval timestamp, response headers, bytes, SHA-256, and period values.
4. Keep the February value gap UNKNOWN; no plug, blanket tolerance, synthetic data, or inferred cause.

## Protected invariants
Research-only; ₹0; free official sources. No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate, parser admission, seed observations, or production workflows.
