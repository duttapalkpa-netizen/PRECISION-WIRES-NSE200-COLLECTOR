# 317-session workflow integration

Historical source artifacts were verified for baseline 200 sessions and backfills of 57 and 60 sessions. A separate 317-session workflow must reconstruct and validate the merged source before replacing the current 200-session portfolio workflow. No production selector, ranking score, pressure fade, CORE-672 diagnostics, or engines are changed.


## Completion record
- Implemented assembler `pipeline/verify_317_artifact_inputs.py` and isolated workflow `.github/workflows/portfolio_two_stock_rolling_audit_317.yml`.
- Successful run `41985471618`, artifact `13395692955`, artifact SHA-256 `af5d182747c9d6334bb395adec244fa0dccff9224427d69282a21c6220f5ec67`.
- Reconstructed dataset: 317 sessions, 765,887 EQ rows, 3,040 symbols, zero duplicate keys; merged CSV SHA-256 `c60afb406103be6c079cea7e3b18a50bd2f729d4424aa526b0bb51523bb17464`.
- Portfolio audit passed research-only for HINDCOPPER (317 sessions) and EPACKPEB (279 sessions), latest session 2026-11-03.
- The new cron schedule remains inactive on this feature branch until authorized merge to default branch. This run is a historical 317-session reconstruction, not a newer-session incremental append.
