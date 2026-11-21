# GCR — Ecuador (ECU) Q2-2026 historical matrix evidence-link reconciliation
Date: 2026-11-21 (Asia/Kolkata)

## Preflight and selection
- Re-fetched the current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, 63-country national validation matrix and dedicated ECU Q2-2026 BCE report before selecting this task.
- Controlling national report: `docs/GCR_ECUADOR_ECU_Q2_2026_BCE_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION147_20261121.md`, blob SHA-1 `90b53d62bd0044c5c3f0a4e45aa91f2042acf50d`.
- ECU already has separate national portfolio asset/liability observations and numeric comparisons at 0.1 USDm publication precision. Repeated extraction/comparison was excluded.
- Defect: ECU matrix row had `evidence_ref=NO_DEDICATED_REPORT_REF_IN_BASELINE` despite the dedicated C147 report. Selected this narrow metadata correction; no source retrieval or numeric recalculation.

## Existing evidence retained — no new PASS claim
- BCE Q2/26 portfolio asset net acquisition: -595.2 USDm; archived IMF exact row converted using declared SCALE=6: -595.16416796001 USDm; difference -0.03583203999 USDm; existing report records PASS at 0.1 USDm precision.
- BCE Q2/26 portfolio liability net incurrence: +1,000.3 USDm; archived IMF exact row converted using declared SCALE=6: +1,000.348809 USDm; difference -0.048809 USDm; existing report records PASS at 0.1 USDm precision.
- These are numeric comparisons only. BCE national raw HTML/PDF SHA-256 is NOT_CAPTURED; exact BCE–IMF same-vintage bridge is NOT_ESTABLISHED.
- BCE NEDD page last-updated date and IMF archive date do not by themselves prove synchronized vintage.

## Matrix change
- Changed only ECU `evidence_ref` from `NO_DEDICATED_REPORT_REF_IN_BASELINE` to `GCR_ECUADOR_ECU_Q2_2026_BCE_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION147_20261121`.
- Retained ECU stage `DATA_CAPTURED`, asset gate `PASS`, liability gate `PASS`, vintage `PENDING`, FULL_PASS `NO`, aggregate admission `NOT_AUTHORIZED`.
- No other country row or ECU field changed.

## Exact remaining blockers
1. Preserve the BCE NEDD page or official Q2 bulletin as raw evidence with retrieval timestamp and SHA-256.
2. Obtain exact BCE revision/release vintage and IMF series extraction-vintage evidence before considering the vintage gate.
3. Until both are independently established, ECU remains PARTIAL; no FULL_PASS or aggregate admission.

## Protected invariants
₹0; official/free sources only; no synthetic data; no IMF re-query or cohort rebuild; no sign inversion, netting, back-solving or stock/flow substitution. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
