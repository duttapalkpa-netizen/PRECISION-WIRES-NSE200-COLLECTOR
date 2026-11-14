# Six-country official BPM6 reporting-basis and SDMX constraint cross-check

Audit date: 2026-11-15
Scope: CAF, ERI, GNQ, SOM, TCD, TKM — six countries with no non-empty annual P_F/USD assets/liabilities observations in the archived IMF.STA:BOP(21.0.0) response.

## 1. Official IMF reporting-basis evidence

The IMF's public document titled "Availability of Official BPM6 Basis Balance of Payments and International Investment Position Data", dated April 2025, provides country names/codes and separate BOP BPM6-basis start dates and IIP BPM6-basis start dates. The document states that official BPM6-basis availability reflects the economy's own reported BPM6-basis data included in that publication; earlier periods and economies not yet providing official BPM6-basis estimates are IMF-converted BPM5-basis estimates.

Source PDF:
`https://data.imf.org/-/media/iData/External-Storage/Documents/FCB3A324C1E04091A38C82B5C936614D/en/4-Economies-Reporting-on-BPM6-Basis-April-2025.pdf`

Review of the complete two-page table (including the continuation page) found no entries for the six target countries/codes:
- CAF — Central African Republic
- ERI — Eritrea
- GNQ — Equatorial Guinea
- SOM — Somalia
- TCD — Chad
- TKM — Turkmenistan

**Interpretation strictly limited to this document:** none of these six appears in the April 2025 table of economies for which the publication lists an official own-reported BPM6-basis BOP start date. This is evidence about the publication's BPM6-basis reporting inventory as of April 2025 only. It does not prove IMF membership status, formal reporting obligations, ineligibility, absence of BPM5 data, or that no later BPM6 submission occurred. The document's publication cutoff is older than this audit date.

The IMF BOP dataset page also lists a later document "Economies Reporting on BPM6 Basis October 2025" with publication date 14 May 2026. Search-index metadata confirms its existence, but its PDF body was not retrieved and inspected in this audit. Therefore no claim is made that the six countries are absent from that later edition. It is the next version to inspect before upgrading this finding.

## 2. SDMX reporting-constraint registry cross-check

The public IMF SDMX Central Reporting Constraints page was inspected. Its visible registry lists, among many other entries:
- `IMF:BOP6_CONSTRAINT` — target structure type Dataflow; constrained structure `BOP6[1.0]`; type Cube Region Constraint.
- `IMF:BOP_BP6_CONSTRAINT` — target structure type Dataflow; constrained structure `BOP_BPM6[1.0]`; type Cube Region Constraint.

The registry page's visible list does **not** show a constraint explicitly attached to `IMF.STA:BOP(21.0.0)` or `IMF.STA:DSD_BOP(24.0.0)`. These similarly named legacy/global BOP6 flows are not proven to be the same maintainable artefact as the IMF.STA BOP dataflow audited in this project. Do not transfer their cube regions to the DSD_BOP series.

IMF SDMX Central's own overview explains that constraints can be applied at DSD, Dataflow, Provision Agreement, and Data Provider levels, and that constraints can define allowed/restricted series or partial series. Thus a complete eligibility check requires matching the exact dataflow and any applicable provision-agreement/provider constraints; a generic registry listing is not sufficient.

Sources:
- `https://sdmxcentral.imf.org/data/constraints.html`
- `https://sdmxcentral.imf.org/overview.html`

## 3. Evidence classification for the six countries

| Country | No non-empty annual series in archived P_F/USD exact keys | Listed in April 2025 official BPM6 BOP-start table | Formal eligibility conclusion |
|---|---|---|---|
| CAF | Yes | No | UNKNOWN |
| ERI | Yes | No | UNKNOWN |
| GNQ | Yes | No | UNKNOWN |
| SOM | Yes | No | UNKNOWN |
| TCD | Yes | No | UNKNOWN |
| TKM | Yes | No | UNKNOWN |

"Not listed" is not coded as FAIL. The April 2025 source is a historical publication inventory, not a formal eligibility/obligation register for the exact P_F/USD/A series.

## 4. Gate decision

- Historical official BPM6 reporting-basis cross-check: PASS as a source review.
- Six-country absence from April 2025 table: PASS as a table-level finding only.
- Latest October 2025 BPM6 reporting table: NOT_RETRIEVED; requires inspection.
- Exact IMF.STA:BOP(21.0.0) applicable reporter constraints: UNKNOWN.
- Formal reporter eligibility for all six: UNKNOWN.
- Quarterly coverage acceptance: NOT PASS.
- EMDE aggregation: BLOCKED.

## 5. Next action

Retrieve and inspect the IMF document "Economies Reporting on BPM6 Basis October 2025" (published 14 May 2026) and reconcile these six countries against its BOP start-date column. Separately resolve exact IMF.STA BOP dataflow, provision agreement, and provider-level constraint references. Until both are inspected, retain UNKNOWN. Do not infer ineligibility from missing observations or a country absent from an older publication list.

## 6. Protected invariants

₹0 spend; official public IMF sources only; no external contact, paid API, credentials, synthetic data, aggregation, annual-to-quarterly conversion, PR merge, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E, and Hard Gate unchanged.
