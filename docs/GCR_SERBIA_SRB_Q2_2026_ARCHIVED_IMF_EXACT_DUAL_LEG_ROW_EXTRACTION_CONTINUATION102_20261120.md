# Serbia SRB Q2-2026 — archived IMF exact dual-leg row extraction
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44 / Continuation 102
Decision: **Archived IMF SRB Q2-2026 A_NFA_T and L_NIL_T exact rows successfully extracted from the pre-existing normalized panel via Git blob SHA; scale conversion recorded; no new IMF query/cohort rebuild; NBS May liability value confirmed as printed in the same official September 2026 bulletin, but not independently re-vintaged; EUR↔USD transaction conversion and exact vintage match remain NOT_ESTABLISHED; SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight / PASS work excluded
- Re-fetched Master Continuity Ledger (blob SHA c57d93a381c4a6cee039c0d2bd58f64410c33aae), GCR Priority Queue (blob SHA 4281684d9c879c1ce62ca8a8ececebf3ac365c6b), SRB Continuation 101 (blob SHA ca0eb8844ab9d14a378f4278506f363fdf776c65), and immutable cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8).
- Continuation 101 already verified NBS monthly Q2 values and arithmetic. Do not repeat its source-family or arithmetic work.
- The previous large-file contents route returned empty, but the existing archived panel blob is addressable by its known Git blob SHA. Used the blob retrieval route; no IMF endpoint call, no new query and no cohort rebuild.

## 2. Exact archived IMF observations
Repository file: `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv`
Archived Git blob SHA: `2a8db2878cac6323bbad74ffa4035dc70e5e6b98`
Retrieved content length: 1,849,027 characters (UTF-8 text returned by repository blob retrieval).

Exact Q2-2026 rows (preserved verbatim):
```csv
dataflow,IMF.STA:BOP(21.0.0),R,SRB,A_NFA_T,P_F,USD,Q,2026-Q2,288993091.8400176,6,6,,,,,,,,,,,,O,,,,true,,,EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv,677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e
dataflow,IMF.STA:BOP(21.0.0),R,SRB,L_NIL_T,P_F,USD,Q,2026-Q2,4782903852.31975,6,6,,,,,,,,,,,,O,,,,,,,EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv,713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba
```

- Asset raw OBS_VALUE: 288,993,091.8400176; SCALE=6; UNIT=USD; normalized value = **USD 288.9930918400176 million**.
- Liability raw OBS_VALUE: 4,782,903,852.31975; SCALE=6; UNIT=USD; normalized value = **USD 4,782.90385231975 million**.
- Both rows are quarterly (FREQUENCY=Q), period 2026-Q2, country SRB, indicator P_F.
- Asset source-file SHA256 recorded in row: 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e.
- Liability source-file SHA256 recorded in row: 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba.
- These are source-file SHA-256 values embedded in the archived rows; they are not a newly computed hash of the whole panel blob.

## 3. Reconciliation boundary against NBS
- Continuation 101 NBS Q2 values remain: assets +248 EURm; liabilities +4,112 EURm; net -3,864 EURm.
- NBS September 2026 official Statistical Bulletin Table 2.3 itself prints May-2026 portfolio liabilities +3,932 EURm and May net -3,957 EURm; this confirms the earlier transcription against the same source document, not an independent later-vintage confirmation.
- IMF and NBS use different currencies (USD vs EUR). No direct numeric residual is valid until an official transaction-conversion basis / period FX method and vintage bridge are established.
- The NBS source states net = assets − liabilities; IMF indicator definitions and national mapping must still be tied to official methodology before sign/definition admission.
- Exact IMF rows are now CAPTURED; NBS PDF raw bytes, byte count and SHA-256 remain NOT_CAPTURED.
- NBS-to-IMF transaction FX conversion: NOT_ESTABLISHED.
- Same-vintage alignment: NOT_ESTABLISHED.
- May 2026 value: confirmed in the same September bulletin only; independent source-series or subsequent-vintage check NOT_DONE.
- Separate asset and liability numeric comparison: NOT_DONE.
- SRB remains PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 4. Next exact actions
1. Retrieve NBS downloadable source series or a subsequent bulletin vintage and independently verify May-2026 liability +3,932 EURm; retain vintage distinctions.
2. Capture NBS September PDF raw bytes through a supported byte-preserving route and record status/headers, byte count, retrieval timestamp and SHA-256.
3. Locate official NBS/IMF metadata for the transaction FX conversion basis and sign/concept mapping; do not use an arbitrary monthly average or quarter-end rate.
4. Only after the official bridge exists, compare each leg independently. No net-to-leg inference.

## 5. Official source
- NBS Statistical Bulletin — September 2026, Table 2.3: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_09_26.pdf
- NBS Balance of Payments page: https://www.nbs.rs/en/drugi-nivo-navigacije/statistika/platni_bilans/

## 6. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic observations, no inferred FX, no net-to-leg inference, no sign flip, no stock-as-flow, no annual proration, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
