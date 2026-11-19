# GCR India 2026-Q1 Vintage Persistence + Brazil PA Access Boundary
Date: 2026-11-19 (Asia/Kolkata)
Continuation: Research verification 40, Part-2
Scope: official public-source recheck; read-only. No API replay, no credentials, no production changes.

## Progress Log — reused evidence
- Reused India baseline: RBI Table197 2024-Q2–2025-Q3, 12/12 asset/liability comparisons PASS.
- Reused India current-vintage supplement: 2025-Q1/Q2 and 2026-Q1/Q2 12 comparisons; 10 PASS, 2 REVIEW. 2026-Q1 liability and combined net remain REVIEW because IMF L_NIL_T = -13,633.508347 USD million vs RBI Table42 = -12,121 USD million; residual -1,512.508347 USD million.
- Reused Brazil PA and registration identity: PA IMF:BR_BOP_BP6(1.0) -> Dataflow IMF:BOP6(1.0), provider IMF:BR1; BCB payload declares IMF:BOP_BPM6(1.0). Identity conflict remains unresolved. Prior transaction-ID-2 fusion-json and sdmx-json both HTTP 500; do not repeat.

## New official RBI publication persistence check
Sources inspected:
1. RBI Bulletin Table 42, “Standard Presentation of BoP in India as per BPM6 (US$ Million)”, 22 June 2026:
   https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24288
2. RBI Bulletin Table 42, same title, 22 July 2026:
   https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24352
3. RBI official table metadata:
   https://rbi.org.in/Scripts/PublicationsView.aspx?id=24094

Directly visible indexed/page text in both 22-June and 22-July Table 42 publications reports Jan-Mar 2026 (preliminary) portfolio investment in India net = -12,121 USD million. The same number is also present in the already-retrieved Aug-25 2026 Table 42 source record used by the previous supplement. The October-23 Table 42 release is Apr-Jun 2025/2026 and does not provide a new Jan-Mar 2026 observation in the captured table view.

RBI table metadata explicitly states: “Revision Policy — Data are subject to revision.” This establishes that revisions are possible, not that a revision explains the IMF/RBI discrepancy.

## India decision
- The -12,121 USD million RBI Q1 2026 net value is persistent across the two inspected June/July official publications; the prior supplement also records it in the Aug-25 publication.
- The IMF current panel liability remains -13,633.508347 USD million for the tested key/vintage.
- Difference remains -1,512.508347 USD million.
- No official evidence found in this bounded check that the difference is caused by a subsequent RBI revision, a period mismatch, a scale issue, or a BPM basis difference.
- Status: India 2026-Q1 liability = REVIEW / UNRESOLVED; do not adjust, blend, or overwrite either source.
- The 2024-Q2–2025-Q3 12/12 historical baseline and 2026-Q2 pass remain intact. This Part-2 does not invalidate them.

## New Brazil official GUI access-boundary check
Official pages:
- Provision Agreements: https://sdmxcentral.imf.org/data/provisionAgreements.html
- Structure Submissions: https://sdmxcentral.imf.org/activity/structure-log.html
- Registrations: https://sdmxcentral.imf.org/data/registrations.html

Public page rendering exposes Provision Agreement detail controls: References, Changelog, Export SDMX-ML 3.0, Export Excel, Compare and View Provision Agreement; metadata fields include URN, URL, Revisions, Description, Annotations, Valid From and Valid To.
Structure Submissions page exposes Structure Type, Agency, Id, Version, Modification Date, Modification Action, Modification User, Download Revision and Compare.
The static rendering does not populate the selected Brazil PA's dated revision rows or its Changelog. It also displays a confirmation/re-authentication dialog requiring username/password for an action; the static view does not establish which exact PA operation triggers it.

No interactive selection, authentication, credential entry, export, or mutation was attempted. No claim is made that Brazil's Changelog is empty or that every view action requires login.

## Brazil decision
- Current PA/dataflow/provider identity remains established from prior archived XML.
- Actual selected Brazil PA revision/changelog contents remain NOT_OBSERVED / UNKNOWN.
- The 40/40 registration lifecycle remains valid but does not substitute for the PA revision history.
- Brazil BOP6 vs BOP_BPM6 identity remains BLOCKED; no alias, header rewrite, or Brazil admission authorized.
- Exact next evidence route: an authorized interactive session selects PA URN IMF:BR_BOP_BP6(1.0), exports the actual revisions/changelog and compares selected revision(s). Preserve original files, source URLs, UTC retrieval time, byte counts and SHA-256. If owner authentication is required, the authorized owner/provider must export and supply the files; do not bypass access or request credentials in chat.

## Rejected / excluded
- Do not label the India Q1 difference as a revision without evidence.
- Do not use RBI's general revision policy as proof that a specific Q1 value was revised.
- Do not net assets/liabilities or alter sign conventions to force a match.
- Do not repeat PA transaction-ID-2 HTTP 500 endpoints.
- Do not infer Brazil PA changelog contents from the existence of UI controls.
- No synthetic data, imputation, guessed endpoints, IDs, timestamps or mappings.

## Next exact bounded actions
1. India: obtain IMF country metadata/revision information and RBI source release/series notes for India Q1 2026; compare same observation vintage and exact reporting concept before changing REVIEW status.
2. Brazil: authorized owner-side PA Changelog/Revision/Compare export for exact URN IMF:BR_BOP_BP6(1.0); only then determine whether a dated PA revision or official correction resolves BOP6/BOP_BPM6.
3. GCR: continue country/vintage validation; do not publish 154-member converted aggregate until all inclusion, missingness, BPM basis and scale gates are satisfied.

## Hard invariants
₹0, official/free sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS. No production integration, aggregate admission or trading use.
