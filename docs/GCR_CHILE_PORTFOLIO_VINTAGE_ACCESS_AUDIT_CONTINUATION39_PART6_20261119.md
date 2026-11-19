# Chile Portfolio-Series Vintage Reconciliation Feasibility Audit — Continuation 39 Part-6
Date: 2026-11-19 (Asia/Kolkata)
Scope: determine whether exact Chile BDE portfolio-flow series and a reproducible 07-Sep-2026 vintage can be obtained from public official sources without credentials. Research only; no production changes.

## Executive decision
**Current-vintage portfolio series discovery: PARTIAL PASS. Historical 07-Sep vintage retrieval: BLOCKED / NOT AVAILABLE IN PUBLIC EVIDENCE REVIEWED. Exact old-vs-new bridge: NOT_DONE.**

The official Banco Central de Chile BDE table exposes quarterly observations through III-2026 and identifies detailed portfolio-liability rows. The official BDE API documentation states that REST `SearchSeries` and `GetSeries` require a personal API Key Token. The public rendered table is useful for current-vintage discovery but is not a byte-level archived 07-Sep snapshot and cannot establish the historical values as of that date. No token, credentials, private API access, or unverified archive URL was used.

## Official sources inspected
1. BDE public current table, SDMX_BOP6: https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_BDP/MN_BDP42/SDMX_BOP6/638180320365121793
2. Official BDE API documentation: https://si3.bcentral.cl/estadisticas/Principal1/Web_Services/documentacion_en.html
3. Official BOP / IIP statistics landing page: https://www.bcentral.cl/es/web/banco-central/areas/estadisticas/balanza-de-pagos-y-posicion-de-inversion-internacional
4. Official 2026 quarterly revision calendar: https://www.bcentral.cl/documents/d/banco-central/calendario_cnn_bp?download=true

## New source-access finding
The BDE documentation describes:
- `SearchSeries` for catalog search and series metadata.
- `GetSeries` for observations.
- REST endpoint `https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx`.
- Both REST functions require a valid personal API Key Token in each request.
- Metadata fields include series ID, frequency, first/last observation, createdAt and updatedAt.
- The API output can expose observation values and status codes.
The documentation's authentication requirement is a hard access dependency for reproducible programmatic extraction; no token was available in the inspected public source material. This does not prove that all public exports are impossible; it means the documented API route cannot be called anonymously.

## Current-vintage table discovery (not an archived-vintage PASS)
The public SDMX_BOP6 table exposes 2003-Q1 through 2026-Q3 columns. Its current table includes:
- Row label `Inversión de cartera pasivos, títulos de deuda (BP)` (portfolio investment liabilities, debt securities), with visible values through 2026-Q3.
- Additional breakdown rows by central bank, banks, general government and other sectors.
- A separate row `Cuenta financiera, pasivos, otros sectores, inversión de cartera, títulos de participación de capital` (portfolio liabilities, equity securities).
The table also shows a current-vintage update context from 18-Nov-2026 in related BDE metadata. The visible values are current table values only. They must not be substituted for the exact series codes/dimensions used in the earlier IMF P_F comparison until code-level metadata and instrument/sign/valuation mapping are captured.

## What this resolves / what it does not
- Resolves: the official public BDE table has relevant detailed portfolio-liability breakdowns and quarterly observations through 2026-Q3.
- Does not resolve: exact BDE series IDs for both portfolio assets and liabilities; the 07-Sep-2026 archived values; raw bytes/headers/hash for that older vintage; exact row-level reconciliation against 18-Nov and IMF P_F dimensions.
- The earlier revision-policy evidence remains valid: the 2026 calendar schedules Q1 second revision and Q2 first revision on 18-Nov-2026, with Q3 first release that day. This is a plausible and officially documented reason for changed Q1/Q2 values, but not a numerical portfolio-series bridge.
- No inference from the rendered page's current values to the earlier vintage. No values reverse-engineered from charts or assumed unchanged.

## Acceptance matrix
| Gate | Status | Reason |
|---|---|---|
| Public BDE current table accessible | PASS | Official table inspected |
| Portfolio-liability categories visible | PASS | Debt/equity categories and sector breakdowns visible |
| Exact portfolio assets/liabilities series IDs | NOT_DONE | Need metadata/catalog capture |
| BDE API access contract | PASS | Official documentation reviewed |
| Anonymous API extraction | BLOCKED | Token required by documented REST API |
| 07-Sep-2026 archived vintage raw bytes | BLOCKED / NOT_FOUND | No official dated archived export identified in reviewed public sources |
| 18-Nov current-vintage exact raw capture | NOT_DONE | Rendered HTML reviewed; raw response bytes not archived in this task |
| Old-vintage/current-vintage/IMF row bridge | NOT_DONE | Missing old vintage and exact series metadata |
| Chile Q1/Q2 2026 status | REVIEW_VINTAGE_MISMATCH | Revision timing known; exact values bridge missing |

## Highest-value next action
1. Obtain from the BDE API Access route an official free/eligible token if available, without purchasing any subscription or sharing credentials in chat; otherwise request a public official downloadable historical vintage/export.
2. With authorized access, run `SearchSeries` for cartera / portfolio investment assets and liabilities, preserve metadata and update timestamps, then `GetSeries` for the exact quarterly series.
3. Capture the 18-Nov-2026 response as immutable raw bytes with retrieval UTC, status/headers, byte count and SHA-256.
4. Locate an official 07-Sep vintage archive or prior immutable artifact; if none exists, preserve the vintage gap as BLOCKED rather than fabricate a bridge.
5. Map exact BDE series dimensions to IMF `A_NFA_T` / `L_NIL_T` and P_F only after verifying instruments, signs, valuation basis and reporting coverage.

## Brazil and GCR status carried forward
Brazil PA remains `IMF:BR_BOP_BP6(1.0)` -> `IMF:BOP6(1.0)`, provider `IMF:BR1`; BCB payload declares `IMF:BOP_BPM6(1.0)`. Public structure comparison PASS; equivalence/alias NOT_PROVEN; PA Changelog and provider-side revision chronology BLOCKED. Do not repeat transaction-ID-2 HTTP 500 probes.
GCR synchronized country panel and relative-attraction score remain BLOCKED / NOT_READY. Preserve separate bank credit, portfolio, FDI, official/reserve, FX and rates layers.

## Invariants
₹0; free official sources only; no credentials/cookies in chat; no synthetic values, interpolation, guessed series IDs, fabricated timestamps or hashes, unapproved aliases/crosswalks. UNKNOWN is never PASS. No production integration, macro weights, EMDE aggregate, selector/ranking/pressure-fade/CORE-672/Engines A-E changes.
