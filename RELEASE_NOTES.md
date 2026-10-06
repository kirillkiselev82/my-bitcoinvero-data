# v1 public onchain-only packaging revision — 2026-10-06

This revision changes packaging and documentation, not historical calculations.

- Removed all 11 price-dependent series, their joined daily table and the old
  unresolved price-derived licence notice. No raw price series is included.
- Retained the 16 original price-independent CSVs and their exact joined values.
- Retained original project evidence, Core JSON responses and checkpoint CSV
  without byte changes. Preserved unsuccessful-run context and evidence hashes.
- Applied CC BY 4.0 within the scope of LICENSE-DATA.md, with code and third-party
  rights expressly excluded; documented all excluded price-derived paths.
- Corrected daily inventory descriptions, disclosed the unconfirmed calendar
  anomaly diagnosis and potentially incomplete terminal calendar day.
- Replaced the claim that all audit phases passed with actual phase/provenance
  limitations. Preserved original historical report statements without editing.
- Recorded the r4/r5 calculator mismatch and unknown running Core daemon version
  as evidence limitations, not empty placeholders or invented values.
- Qualified the Coin Metrics provider claim and retained input hash metadata
  without redistributing observations or claiming current downloads reproduce it.
- Regenerated the public inventory and checksums after all packaging changes.

Packaging validation: all public checksums and listed sizes agree; the 16 narrow
CSVs are byte-identical to the supplied originals; the joined table exactly
matches their dates and serialized values; each series has 4 062 calendar rows;
both checkpoint reference hashes and Core count/value/block/MuHash fields agree;
the project audit aggregate values match Core at both heights. Original evidence
bytes and sidecar hashes are preserved. No recalculation, remote node query,
external audit or recovery of historical code was performed by this packaging step.

Remaining limitations: historical r4 code is unavailable, the daemon version at
RPC capture is unknown, daily boundary heights are not provided, and exact block
tracing of the November 2014 anomaly is not included. These do not disappear
when checksums pass. Do not describe this package as a fully reproducible or
externally audited software/data pipeline.
