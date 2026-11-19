# GCR IMF BOP DSD v2.6.0 Capture Verification — Continuation 64
Date: 2026-11-19 (Asia/Kolkata)
Scope: verify focused public SDMx Global Registry capture; metadata only, no observation data.

## Decision
- Official DSD v2.6.0 metadata capture: **PASS**.
- SDMX-ML 2.1 XML parse: **PASS**.
- SDMX-ML 3.0 XML parse: **PASS**.
- Legacy IMF Data Portal DSD v24.0.0 ↔ Global Registry DSD v2.6.0 crosswalk: **NOT DONE / BLOCKED**.
- GNB current-version series availability: **NOT TESTED**.
- No GCR country data repair, aggregate, or production admission is authorized by this capture.

## GitHub Actions and archive receipt
- Workflow: `.github/workflows/imf_bop_dsd_v260_capture.yml`
- Run: `44507773721`, run #2, conclusion SUCCESS; job `capture` SUCCESS.
- Trigger/head commit: `79817af059973e09038969fd401cde3afdd7f00e`.
- Artifact: `14520401775`, name `imf-bop-dsd-v260-public-metadata-44507773721`, 237,677 bytes; expires 2027-02-17T10:40:03Z.
- ZIP SHA-256: `d3948cfae4ed6df052736035e95572914200dbde0a945f3d43f86df950395a94`.
- Manifest SHA-256: `d545ae12d27caa62c48f4303f277f0df4e23d46a8b68af78cce0620f689c76ac`.
- Manifest retrieval UTC: `2026-11-19T10:40:27.382661+00:00`.

## Raw XML integrity
| Format | HTTP | Bytes | SHA-256 | XML parse |
|---|---:|---:|---|---|
| SDMX-ML 2.1 | 200 | 1,081,882 | `543c103c18b5597143969ef4fb42ba91be263b03262c257d47824fb45eb8e989` | PASS |
| SDMX-ML 3.0 | 200 | 1,076,119 | `4508050ea5fce0b0d5ac8184e1d3575bc000e22377e9fd6cb5c126eddd6eedaf` | PASS |

Both XML payloads were independently opened from the downloaded artifact ZIP and parsed locally. The manifest records 28 maintainables, 23 codelists, one concept scheme and three dataflows in each representation. It records zero constraints in the returned package.

## Structural facts extracted
- DSD identity: `IMF:BOP(2.6.0)`.
- The DSD contains 17 ordinary dimensions plus `TIME_PERIOD` (18 dimensions total). Dimensions include `FREQ`, `ADJUSTMENT`, `REF_AREA`, `COUNTERPART_AREA`, `REF_SECTOR`, `COUNTERPART_SECTOR`, `FLOW_STOCK_ENTRY`, `ACCOUNTING_ENTRY`, `INT_ACC_ITEM`, `FUNCTIONAL_CAT`, `INSTR_ASSET`, `MATURITY`, `UNIT_MEASURE`, `CURRENCY_DENOM`, `VALUATION`, `COMP_METHOD`, `TYPE_ENTITY`, and `TIME_PERIOD`.
- Three returned dataflows are maintained by ESTAT: `BPM6_BOP_M(2.6.0)`, `BPM6_BOP_Q(2.6.0)`, and `BPM6_ITS_A(2.6.0)`; each SDMX-ML 2.1 Dataflow structure reference points to `IMF:BOP(2.6.0)`.
- The captured package is a global metadata structure response, not a country-level observation extract and not proof that the IMF Data Portal's current BOP dataflow uses these keys.
- The SDMX-ML 3.0 response parsed successfully. Its namespace/layout differs from 2.1; the existing manifest's reference-extraction counter is not implemented for that serialization (unique_references=0), so do not interpret that counter as absence of references. Manual XML inspection confirms the three dataflow records and DSD object are present.

## Critical boundary — no silent crosswalk
The existing GCR panel uses IMF Data Portal dataflow `IMF.STA:BOP(21.0.0)` and DSD `IMF.STA:DSD_BOP(24.0.0)`, with five dimensions plus time in the recorded legacy mapping. The newly captured Global Registry structure is `IMF:BOP(2.6.0)`, with 17 dimensions plus time. These are different agency-qualified artefacts and different schema versions. Similar names or shared BPM6 subject matter do not establish dimension-code equivalence, series identity, unit/scale equivalence, or dataflow coverage.

The official SDMx-BOP maintenance policy states that a new DSD version does not automatically invalidate earlier versions; older versions can remain usable where the exchange template is unaffected. Therefore v2.6.0 does not by itself supersede or invalidate the existing IMF.STA v24.0.0 mapping.

## Next bounded actions
1. Capture the exact legacy `IMF.STA:DSD_BOP(24.0.0)` structure/codelists and the current `IMF.STA:BOP(21.0.0)` dataflow/constraints from the IMF Data Portal, with raw responses and hashes.
2. Build a field-by-field crosswalk only where official concepts, code lists, and semantics match; otherwise mark NOT_MAPPED/UNKNOWN.
3. Determine whether the Global Registry v2.6.0 package contains relevant IMF dataflows/constraints for the GCR series. The three dataflows in this capture are ESTAT-maintained, so they cannot be assumed to provide IMF country coverage.
4. Only after a verified dataflow/constraint/key crosswalk, issue bounded GNB exact-key probes. HTTP 200 with zero observations remains no data for that tested key, not universal absence.
5. Keep all 40-country gaps and aggregate gates unchanged until observations and both legs pass country/period/unit/scale/sign/vintage reconciliation.

## Guardrails
₹0; official/free sources only. No observation values were acquired in this workflow. No synthetic data, annual-to-quarterly interpolation, forward-fill, scale conversion, sign conversion, or gross-leg inference. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
