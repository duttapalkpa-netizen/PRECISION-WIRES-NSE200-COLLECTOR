# IMF BOP SCALE metadata resolution — 2026-11-19

## Verified metadata
- DSD: `IMF.STA:DSD_BOP(24.0.0)`; optional attribute `SCALE` is present and its ConceptIdentity points to `IMF:CS_MASTER_SYSTEM(1.0.2).SCALE`.
- Exact `SCALE` concept enumerates `IMF:CL_UNIT_MULT(1.0+.0)`; latest public codelist `CL_UNIT_MULT(1.0.2)` has code `6` labelled **Millions**, description `10^6`.
- SDMX glossary defines unit multiplier as the base-10 exponent used to calculate the actual value in the unit of measure; `6` denotes observations in millions. This establishes the metadata code meaning, not whether the IMF Data Portal CSV response has already normalized numeric values.

## Numeric application remains blocked
- All 9,299 panel observations carry `UNIT=USD` and `SCALE=6`; preserve both exactly.
- Raw observation values are already large in absolute USD magnitude. Mechanically multiplying them by 10^6 produces implausible values for some countries. Do not assume the CSV response requires a second multiplier.
- Need direct comparison between IMF portal display, raw SDMX response and official national-source published values for selected observations (Brazil and India), including any server-side scale normalization.
- Decision: **SCALE code meaning PASS; numeric transformation BLOCKED.** No multiply/divide, rescaling, FX conversion, netting or aggregate is authorized. Raw `OBS_VALUE` remains unchanged.

## Reproducible capture
- Run 44475051442; artifact 14505852262; ZIP SHA-256 `391981ce19d89d8ccc6377580e33345a9d75adffdc3f4197c4e4c743a66e3cf3`.
- DSD XML SHA-256 `5953ac8b3a52fae9cd7c5821621446d046969bcef0e88540ef17520c2d39b098`.
- Master concept scheme SHA-256 `e753812c45b8159c77e191f091c63d5364375f57daca179da9799040de48e568`.
- CL_UNIT_MULT SHA-256 `40a911ecceb0b96ff0ee2a166af3c2512f19fbbfca50e71b2e47936cad3bac78`.

No production changes; no paid sources; no synthetic data; UNKNOWN is not PASS.
