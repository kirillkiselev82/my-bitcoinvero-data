# BitcoinVero UTXO daily metrics v2.0.0 — block 968206

## Release content

- The existing GitLab `main` data paths are updated in place to a new **complete genesis-to-968206 calculation**; 16 original price-independent CSVs and one derived wide CSV, 6473 UTC dates from 2009-01-03 through 2026-09-23. The final UTC day is partial (01:06:32 UTC).
- Previous release v1 remains recoverable at Git tag [`v1.0.0`](https://gitlab.com/bitcoinvero/bitcoinvero-data/-/tags/v1.0.0). Its original historical `evidence/` reports remain on the same paths; they are not represented as current v2 certificates.
- The 16 narrow CSVs are byte-preserved from the operator-provided R14 v2 metrics archive; the wide CSV reproduces the original serialized values. The source Stage, Metrics and State checkpoint evidence remains unedited.
- Added original 971-entry APPLY/recovery/source lineage evidence, 970 Stage windows, BitcoinVero H127 `STATE_CONSISTENCY` registry and execution receipts, and a separate Bitcoin Core MuHash `MATCH` reference. See `evidence/README.md` for precise scopes.
- The Metrics producer run itself remains `COMPUTED_WITH_LIMITED_VALIDATION`, `certified=false`; H127 is an **internal-State-only** certificate with P12/P15 `NOT_EVALUATED` in the certified run. MuHash independently compares the *live set* and is not full-chain history certification or a third-party signature.

## Historical changes and technical findings

- This is a **full historical recomputation**, not an append-only continuation of v1. Compared with v1 through the overlapping complete UTC dates ending 2020-02-15, 13 of 16 series match by serialized values, whereas `utxo_spent_btc`, `utxo_raw_inputs` and `utxo_dormancy` differ on certain dates in 2010–2015. The causes of *these version-to-version differences* have not been fully established; no unverified explanation is asserted.
- **Resolved 2014-11-06 / 2014-11-07 calendar inversion:** Bitcoin block 328875 (2014-11-07 00:03:02 UTC) precedes block 328876 by height, but the latter has an earlier timestamp (2014-11-06 23:57:14 UTC). Nine outputs created in the former and spent in the latter total **1,089,538,263,160 sats = 10895.38263160 BTC**. Producer code, pinned by `metrics_code_sha256`, clamps close-date accounting to the creation date, explaining the exact -/+ 10895.38263160 BTC split between `closed_btc` and `spent_btc` across those days (0 sat difference). See `evidence/validation/2014-11-06_07/`. The block results are operator-captured RPC exports reviewed offline, not a fresh external raw-block audit.
- A total of 1331 causality-clamped closes and two BIP30 overwrites are recorded by the producer. `closed_btc − spent_btc` cumulatively equals 100 BTC due to BIP30. Day-level values remain calendar-accounting aggregates, not height-anchored daily UTXO snapshots.
- Added checkpoint 968206 to `node_checkpoints.csv`, sourced from separate pinned BitcoinVero native MuHash + Bitcoin Core reference evidence. Historical checkpoint rows for 617698 and 663917 are retained unchanged.
- BTC/USD identity information is disclosed in `price/` without distributing observations or any price-derived series; v2 input differs from v1 (older identity remains in the Git tag).

## Known limitations

Underlying Stage Parquet, full UTXO State, raw blockchain data and runnable producer/auditor implementations are not bundled. No full independent history certification, third-party cryptographic attestation or complete byte-exact re-execution is claimed. Current GitLab release verification requires the preserved v1 files as well as this overlay's new files; see the full-tree `MANIFEST.json` and `SHA256SUMS`.
