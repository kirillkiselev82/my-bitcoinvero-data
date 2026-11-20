# BitcoinVero UTXO daily metrics v2 — Bitcoin block 968,206

**Historical snapshot, not a live chain-tip feed.** This release covers Bitcoin
blocks **0–968,206** and publishes **16 BTC-price-independent daily UTXO metrics**.
The CSVs have **6,473 UTC calendar-date labels**, from **2009-01-03 through
2026-09-23**. The last block's timestamp is **2026-09-23 01:06:32 UTC**, so the
last row is a **partial UTC day**; the release does not extend to November 2026.
The whole calculation was produced by BitcoinVero's Bitcoin Core → canonical
Stage → dense UTXO State → Metrics v4.4 pipeline.

## Snapshot and validation level

| Property | Value |
|---|---|
| Final block height | `968206` |
| Final block hash, as recorded by Stage/State | `00000000000000000000014b8c7f91bbf877876ca6b709a3e167a1fa3d42362f` |
| Eligible live outputs at final checkpoint | `165204813` |
| Eligible live value at final checkpoint | `2008791675380694` sat = **20,087,916.75380694 BTC** |
| Metrics generator | BitcoinVero Metrics `4.4` (R14) |
| Generator result | `COMPUTED_WITH_LIMITED_VALIDATION`; `certified=false` |
| History-audit / current-live recertification | `NOT_PERFORMED` / `NOT_PERFORMED` |
| Independent live-set MuHash comparison with Bitcoin Core | **MATCH** at 968,206 (separate evidence; limited scope) |
| BitcoinVero H127 R6-P3 certificate | **CERTIFIED / STATE_CONSISTENCY** on 2026-11-19; not a full-history certificate |

The historical v1 release remains obtainable from GitLab tag [`v1.0.0`](https://gitlab.com/bitcoinvero/bitcoinvero-data/-/tags/v1.0.0). The current `main` tree presents v2 data; version-to-version changes are documented in `RELEASE_NOTES.md`. The v1 original audit and Core evidence files under `evidence/original/`, `evidence/context/` and `evidence/core-rpc/` remain retained as historical records; they are not renamed or relabeled as v2 evidence.

The supplied State checkpoint has valid internal checksums, and its final height,
block hash, live count and live value agree with the supplied Stage release and
Metrics manifest. All 16 original CSVs match that manifest's file hashes, sizes
and row counts. The recombined wide CSV matches their serialized values. Daily
accounting and HODL-share consistency checks also passed; see
`evidence/validation_summary.json`.

**Different scopes must not be conflated.** The original Metrics 4.4 run used `internal-checks-only`; its original manifest, unchanged in this archive, says `COMPUTED_WITH_LIMITED_VALIDATION`, `certified=false`, `independent_history_audit=NOT_PERFORMED` and `current_live_recertification=NOT_PERFORMED`. Those fields describe **that Metrics run only**, not everything subsequently checked against the same State.

Separately, the original BitcoinVero H127 R6-P3 certificate issued **2026-11-19T18:52:43 UTC** is **`CERTIFIED` at level `STATE_CONSISTENCY`**, scoped to `INTERNAL_STATE_CONSISTENCY_ONLY`. It covers the exact State after block 968,206: **P07 internal State scan and P07.26–29 state-derived fees/rewards were OK (3/3 required checks)**. In **this certified invocation**, P12 (Bitcoin Core → Stage) and P15 (Stage → UTXO) and P15.14–16 independent fees/rewards were **`NOT_EVALUATED`**. The certificate explicitly does **not** prove canonical Bitcoin history, or all prior UTXO compositions. It relies on operational assumptions that other writers did not modify the source outside existing cooperative leases; source byte immutability and atomic snapshots were not independently established. It is a **BitcoinVero-issued, SHA-256-addressed registry entry, not a digital signature or third-party attestation**.

The certificate's bounded engine prepared a selected-check report (`COMPUTED_PENDING_FINALIZATION`) with `engine_return_code=2`; **subsequent owned-process finalization completed with `return_code=0`** and a registry event. The original completion receipt, acknowledged stdout and both process-exit observations are bundled. The registry's `ack_sha256` is computed from **canonical compact JSON**, not the literal bytes of `ack.stdout` including spacing/newline.

A **separately executed native MuHash calculation** compared this UTXO State with a Bitcoin Core `coinstatsindex` reference at the **same block hash and height**, reporting **`MATCH` with no differences** for block height/hash, live output count, live value and MuHash commitment. The result and Core-reference JSON are bundled under `evidence/muhash/`. This offers a meaningful live-set cross-check, **not** a proof of every historical transition or a full release certificate. Its recorded `full_verify` was `NOT_PERFORMED` and it did not separately certify the global TXID-duplicate history.

Additional APPLY/recovery/source-lineage journals and a Stage-window list are bundled with original SHA-256 bindings. The underlying Stage parquet/window payloads, full dense State, raw chain and runnable calculator/auditor are **not** bundled, so byte-for-byte end-to-end replay is not provided. No independent external auditor is claimed.

## Contents and how to read them

| Path | Description |
|---|---|
| `data/onchain/utxo_*.csv` | 16 source metric files: columns `timestamp,value`; dates in `YYYY-MM-DD`, 6,473 rows per file |
| `data/onchain_daily.csv` | Convenience join: one `date` column and 16 metric columns; **generated for this public package** from the 16 source CSVs |
| `evidence/utxo_metrics_v4_manifest.json` | Unmodified, original Metrics v4.4 calculation manifest, including 27 private output descriptions; the other 11 CSVs are **not bundled** |
| `evidence/checkpoint.bin`, `evidence/state.meta` | 180-byte and 192-byte State metadata, not the dense UTXO data files |
| `evidence/stage_release_0_968206.json` | Original Stage release descriptor, not the underlying block data |
| `evidence/validation_summary.json` | Initial packaging checks augmented with the **separate** certificate/MuHash evidence review |
| `evidence/provenance/` | Four original pinned APPLY/recovery/source-lineage and Stage-window ledger files |
| `evidence/auditor/` | H127 R6-P3 BitcoinVero-owned STATE_CONSISTENCY registry event, bound reports and exit/ACK receipts |
| `evidence/muhash/` | Original BitcoinVero native MuHash result, Bitcoin Core reference and environment notes |
| `evidence/README.md` | Exact scope and limitations of the different types of evidence |
| `evidence/validation/2014-11-06_07/` | Reproducible, bounded investigation of the calendar-date reversal at blocks 328875/328876 |
| `evidence/original/`, `evidence/context/`, `evidence/core-rpc/`, `evidence/CODE_IDENTITY.md` | Original v1 historical evidence, retained unchanged in the GitLab repository |
| `node_checkpoints.csv` | Recorded Core comparisons at 617698, 663917 and 968206; separate reference scopes |
| `price/` | BTC/USD **input identity metadata only**, with no price observations or price-derived series |
| `MANIFEST.json` | Exact v2 public file inventory with sizes and SHA-256 digests |
| `SHA256SUMS` | Digests of every other file, including `MANIFEST.json` |
| `LICENSE-DATA.md`, `RELEASE_NOTES.md` | Licensing scope and historical differences from v1 |

The *original* Metrics manifest also records server-local paths, run diagnostics,
internal software identities and a BTC/USD input hash. Those are provenance
metadata, **not** downloadable paths and **not** a grant of rights to the absent
price data. The accompanying binary metadata are not the full underlying
hundreds-of-gigabytes UTXO State.

### Metric definitions

The calculator's **eligible output** policy is: creation height != 0 (genesis
coinbase excluded), script length at most 10,000 bytes and first script byte not
`OP_RETURN`. These are the calculator's inventory rules; they are **not** a
proof of key ownership, economic spendability, coinbase maturity or matching
Bitcoin Core's entire UTXO set.

| CSV stem (prefix `utxo_`) | Unit | Interpretation |
|---|---|---|
| `supply_btc` | BTC | Cumulative eligible live output value under calendar accounting, **not** scheduled or total bitcoin issuance |
| `live_utxo_count` | outputs | Cumulative count of eligible, not-yet-closed output records |
| `created_btc` | BTC/day | Eligible output value attributed to its creation block's UTC date |
| `closed_btc` | BTC/day | Value removed by ordinary spends **plus BIP30 overwrites**; close dates may be causality-clamped |
| `spent_btc` | BTC/day | Value removed by ordinary spends only, **excluding BIP30 overwrites** |
| `raw_inputs` | inputs/day | Number of ordinary spend inputs; BIP30 overwrites are not counted as spends |
| `cdd` | BTC·days/day | For ordinary spends, sum of spent BTC × `max(spend_block_time − creation_block_time, 0) / 86400` |
| `dormancy` | days | `cdd / spent_btc`; undefined when `spent_btc` is zero |
| `hodl_0_1d` ... `hodl_2y_plus` | share (0–1) | Share of eligible live **BTC value** in each UTC-calendar-day age cohort, not share of output count |

HODL intervals are **[0,1), [1,7), [7,30), [30,90), [90,180), [180,365),
[365,730), [730,∞) calendar days**. In the actual Metrics v4.4 implementation,
cohort age is the difference between the observation UTC **date index** and
creation UTC **date index**, not exact elapsed seconds since a transaction.
The shares sum to approximately one when live eligible value is positive.
The first six dates have no live eligible inventory, so HODL shares are blank.
`dormancy` is blank when no eligible spend value exists. Do not replace blank
values with zero.

The data are **calendar-accounted**, not UTXO snapshots at each day's last
block. Bitcoin block timestamps may be nonmonotonic. When a closure's raw UTC
block date is earlier than its output's creation date, this calculator assigns
the closure to the **creation date** for inventory/HODL purposes (1,331 such
closes in this calculation). Spent-output ages used by CDD are floored at zero.
Two historical BIP30 overwrites are tracked as inventory removals rather than
ordinary spends; total `closed_btc − spent_btc` across the release is **100 BTC**.

The decimal CSV fields are the calculator's original serialized daily values,
which may involve floating-point rounding and may display integer counts as
`123.0`. **Use the integer-satoshi State checkpoint** for the exact terminal
value. The derived wide CSV keeps each source value as a string (no numeric
reformatting); its columns are named without the `utxo_` prefix.

## Known limitations

1. **Partial final day:** September 23, 2026 ends at 01:06:32 UTC in the
   supplied Stage record. This is a dataset boundary, not a complete-day sum.
2. **No per-day block boundaries:** the release supplies only the overall
   terminal height/hash, not the last block height/hash for each UTC date.
3. **Separate assurance scopes:** the original Metrics run is still `COMPUTED_WITH_LIMITED_VALIDATION`, `certified=false`; the later H127 certificate has level `STATE_CONSISTENCY` **only**, and the separate MuHash `MATCH` is a live-set commitment comparison, not full historical certification. Do not report a full-history audit, third-party certification or daily balance validation.
4. **Incomplete reproducibility:** Stage/State provenance ledgers and selected evidence are included, but Bitcoin Core's raw chain, Stage parquet payloads, dense UTXO data files, and pinned runnable calculator/auditor implementations are not. SHA-256 establishes file identity, not unconditional correctness or full replayability.
5. **Price data and licence:** `price/` documents the distinct v2 input filename and hash but no price values. All eleven price-dependent series are withheld pending exact input acquisition/provenance and rights review. A Coin Metrics-like filename is not licence evidence.

## Integrity verification

From the repository root on GNU/Linux:

```sh
sha256sum --check SHA256SUMS
```

`MANIFEST.json` lists all payload files (excluding itself and `SHA256SUMS`);
`SHA256SUMS` hashes every other file including the manifest. All digests
are SHA-256; the certificate-registry record has **no digital signature**, and
no independent third-party attestation is claimed.

For applications, read an individual metric in the form:

```python
import csv
with open('data/onchain/utxo_supply_btc.csv', newline='', encoding='utf-8') as f:
    for observation in csv.DictReader(f):
        print(observation['timestamp'], observation['value'])
```

## Кратко по-русски

**BitcoinVero UTXO v2:** 16 метрик, не зависящих от BTC/USD, за **6 473
календарных дня** — от 3 января 2009 года до **23 сентября 2026 года**.
Расчёт заканчивается на блоке **968 206**. Последний календарный день
**неполный** (последний блок в 01:06:32 UTC). Это исторический набор, а не
обновляемая в реальном времени статистика.

**Контрольная точка:** 165 204 813 живых подходящих выходов,
2 008 791 675 380 694 сатоши. Целостность checkpoint, манифестов и файлов
проверена; 16 исходных CSV, объединённая таблица и основные инварианты
согласованы. **Отдельный сертификат H127 R6-P3 от 19.11.2026:**
`CERTIFIED / STATE_CONSISTENCY` — проверка внутренней согласованности
конкретного State, но **не всей истории Bitcoin**. P07 и проверки производных
комиссий/наград: OK; независимые P12/P15 в этом сертифицированном запуске
`NOT_EVALUATED`. **Отдельный MuHash:** `MATCH` с Bitcoin Core на блоке
968 206, расхождений нет; это сверка живого UTXO-набора, не проверка всей
истории переходов. Исходный Metrics v4.4 манифест не меняется и по-прежнему
содержит `COMPUTED_WITH_LIMITED_VALIDATION`, `certified=false`.
Сертификат выпущен BitcoinVero и обусловлен предположениями о неизменности
источника; это не цифровая подпись или независимая внешняя сертификация.

Восемь HODL-групп определены по разнице **календарных дат UTC**, а не по
точному возрасту выхода в секундах. Дневной баланс — календарный учёт
созданий и закрытий, **не** проверенный UTXO-снимок на конец суток.
Данные BTC/USD и все 11 зависящих от цены метрик
не публикуются; папка `price/` содержит только информацию об источнике BTC/USD без самих цен. Код калькулятора, файлы полного State и Stage не включены.
