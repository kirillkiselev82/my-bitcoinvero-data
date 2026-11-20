# BitcoinVero v2 — evidence scopes

Evidence here is segregated by purpose. Original producer objects in the root of this directory have not been edited.

| Location | Provenance and significance |
|---|---|
| `checkpoint.bin`, `state.meta`, `stage_release_0_968206.json`, `utxo_metrics_v4_manifest.json` | Original producer files from the 968,206 Metrics v4.4 run. Source status remains `COMPUTED_WITH_LIMITED_VALIDATION` and `certified=false`. |
| `validation_summary.json` | Public-package checks, including separately acquired audit evidence. This is **not** a producer or third-party certificate. |
| `provenance/` | Original APPLY, recovery, source-lineage and Stage-windows ledgers whose hashes were separately verified against producer pins. |
| `auditor/certificate/registry/events/` | **Original BitcoinVero-owned certificate-registry event**. Certification level `STATE_CONSISTENCY` at height 968,206, not full history. |
| `auditor/certificate/registry/run/` | Owned-process exit and canonical-JSON stdout acknowledgment evidence. `ack_sha256` hashes canonical compact JSON, **not the literal `ack.stdout` file bytes**. |
| `auditor/certificate/audit/reports/` | Underlying engine and finalized auditor outputs, receipts and SHA-256 sidecars. The selected-check engine uses a separate intermediate return code from the final owned-process return code. |
| `muhash/` | Original BitcoinVero native MuHash result and Bitcoin Core reference (source from recorded `coinstatsindex` query) plus environment metadata. |
| `validation/2014-11-06_07/` | Targeted and reproducible offline review of 501 block header exports and nine dated outpoints; original operator outputs and SHA-256 digests retained. |
| `original/`, `context/`, `core-rpc/`, `CODE_IDENTITY.md` | Preserved historical v1 audit and Core RPC evidence. These remain unchanged, refer to v1 heights, and do not constitute v2 certification. |

## Certification boundaries

The November 19, 2026 certificate proves only the **internal consistency of the exact bound State** subject to its operational source-stability assumptions. Its P07 and derived fees/rewards checks were OK; P12/P15 independent history checks were **NOT_EVALUATED in the certified run**. The final owned-process `return_code=0`; the selected engine reports `engine_return_code=2` in the bound result, and its prepared report is not an independent full-history certificate. Do not silently conflate these layers.

The October 2026 MuHash record separately reports `MATCH` with Bitcoin Core at height 968,206 for height, block hash, live count, value and MuHash commitment, with `differences=[]`. This is not a complete transition-history audit, per-day snapshot verification, or independently signed third-party attestation. Original MuHash metadata explicitly says `NO_GLOBAL_TXID_DUPLICATE_AUDIT_OR_RELEASE_CERTIFICATION` and `full_verify=NOT_PERFORMED`.

State and Stage source files, raw blockchain data, runnable auditor and MuHash binary, as well as an immutable full runtime environment, are **not bundled**. These documents contain production-local paths for provenance, not endpoints or claims of present server access. The registry event is SHA-256-addressed but **not digitally signed**.

The separate diagnostic full-audit continuation completed P15 in November 2026 but explicitly declared `DIAGNOSTIC_NOT_CERTIFIED`; its source P07/P11/P12 outcomes were assumed from prior reports. It is not merged with the STATE_CONSISTENCY certificate to assert full certification.

## Calendar-accounting validation (2014-11-06 / 2014-11-07)

The precise 10895.38263160 BTC inter-day closing difference is explained by nine created-in-328875/spent-in-328876 outputs where UTC block dates reverse. Original RPC-derived exports and independent offline cross-check are in `validation/2014-11-06_07/`. The review did not independently re-fetch full raw blocks or output scripts. This case study does not certify all historical daily observations.
