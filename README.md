# BitcoinVero UTXO daily metrics, 2009-01-03 … 2020-02-16 (v1)

Historical Bitcoin UTXO metrics reconstructed by BitcoinVero from its own Bitcoin
Core node, through block **617 698**
(`000000000000000000095ad21001856998971c4951123d14276b5f13c45e83d8`).
This public package contains **16 price-independent series**, 4 062 UTC calendar
rows per series, and verification evidence. It contains no USD price series or
price-derived metric series. Known calendar and reproducibility limitations are
disclosed below; this is not a claim of a fully reproducible software release.

- Author: Kirill Kiselev / BitcoinVero.
- Websites: https://bitcoinvero.com/ · https://биткоин.москва/
- Project repository: https://gitlab.com/bitcoinvero/bitcoinvero
  (general project link, not an identified revision of the historical calculator).
- Data licence: CC BY 4.0, within the scope of `LICENSE-DATA.md`.
- Code licence: BitcoinVero Educational Use License 1.2; code is not included.

## Check against Bitcoin Core

The project audit reports and operator-provided Bitcoin Core RPC responses agree
on live output count, total value, and block hash at both checkpoints:

| Height | Live outputs, project = Core | Live value, sat, project = Core |
|---|---|---|
| 617 698 | 65 419 258 | 1 822 105 482 121 089 |
| 663 917 | 68 584 801 | 1 858 679 644 247 703 |

See `node_checkpoints.csv` for exact values, references and SHA-256 identifiers.
The 617 698 checkpoint also matches the terminal daily count and supply in this
package. The 663 917 checkpoint is a later state check: **daily metrics through
663 917 are not published here**.

**Scope:** these are comparisons of aggregates and chain anchors, not proof that
every individual output is identical. The MuHash values are Bitcoin Core's only;
a compatible MuHash from BitcoinVero state is not available in this release.
The project fingerprints in the reports are a different construction and must
not be compared directly to Core MuHash. This is internal project verification,
with operator-supplied RPC evidence, not an external independent audit.

At 617 698, scheduled issuance minus the project live value equals Core's
`total_unspendable_amount` of 182.67878911 BTC; at 663 917 the corresponding value
is 191.05752297 BTC. These are aggregate equalities, not proof of matching
individual exclusion categories or the full set of outputs.

To query a historical checkpoint, use a Bitcoin Core node with a coinstatsindex
that has indexed at least the requested height:

```sh
bitcoin-cli gettxoutsetinfo muhash 617698 true
bitcoin-cli gettxoutsetinfo muhash 663917 true
```

Adapt RPC connection/authentication options to your node. The running daemon's
version at the supplied RPC capture has not been recorded. See
`evidence/core-rpc/COMMAND.txt` for the observed client version, provenance and
commands to record the daemon version. RPC responses are evidence, not signed
attestations from Bitcoin Core developers.

## Contents

| Path | Contents |
|---|---|
| `data/onchain_daily.csv` | 16 price-independent metrics joined by date |
| `data/onchain/*.csv` | The same 16 original metric files, `timestamp,value` |
| `node_checkpoints.csv` | Two aggregate comparisons and evidence hashes |
| `evidence/original/` | Unmodified historical manifests and successful project audit reports |
| `evidence/context/` | An unsuccessful historical audit whose heavy-phase evidence was reused |
| `evidence/core-rpc/` | Complete structured RPC responses supplied by the operator and provenance notes |
| `evidence/CODE_IDENTITY.md` | Expected historical calculator identity and the unresolved mismatch |
| `price/` | Historical input identity and withholding notes; no price observations |
| `RELEASE_NOTES.md` | Packaging changes and verification results |
| `MANIFEST.json`, `SHA256SUMS` | Actual public file inventory, sizes and checksums |

The original metrics manifest describes a larger private calculation containing
27 series, including price-derived metrics. It is retained byte-for-byte as
historical evidence. **Use this release's `MANIFEST.json` for the public file
inventory**; filenames in the historical manifest do not mean those files are
included or licensed for redistribution here.

## Definitions and calendar convention

**Eligible output:** the recorded calculator policy includes outputs with
creation height other than 0, script length at most 10 000 bytes, and first script
byte other than `OP_RETURN`. The genesis coinbase is excluded. Eligibility does
not establish ownership, possession of a spending key, or immediate spendability
of an immature coinbase output.

**Calendar day:** the UTC date of the block timestamp. Block timestamps need not
increase with height. When the UTC date of a close precedes its output's creation
date, the recorded policy assigns that close to the creation date (1 169 closes
in this range). CDD uses nonnegative elapsed block time. Date grouping and this
clamp must not be confused with replaying a height-ordered state at a specified
daily checkpoint.

**Daily inventory:** `supply_btc` and `live_utxo_count` are calendar aggregates of
creations minus closes. The supply series follows the cumulative sum of daily
`created_btc - closed_btc`. They are **not certified snapshots at the last block
of each UTC day**. The final point is checked against state at height 617 698.
This package does not provide a height and block hash for every daily row.

**BIP30:** historical duplicate-coinbase overwrites remove outputs from inventory.
They contribute to `closed_btc` but are excluded from ordinary spend metrics
(`spent_btc`, CDD, dormancy and raw input count). Thus `closed_btc` and `spent_btc`
are intentionally different.

| Column in the joined CSV | Unit | Definition |
|---|---|---|
| `supply_btc` | BTC | Calendar-accounted value of eligible live outputs; not scheduled issuance |
| `live_utxo_count` | outputs | Calendar-accounted count of eligible live outputs |
| `created_btc` | BTC | Eligible output value assigned to a creation date |
| `closed_btc` | BTC | Output value removed, including normal spends and BIP30 overwrites |
| `spent_btc` | BTC | Value removed by normal spends only |
| `raw_inputs` | inputs | Normal spends assigned to a close date |
| `cdd` | BTC·days | Sum of spent value × max(spend block time − creation block time, 0) / 86 400 |
| `dormancy` | days | `cdd / spent_btc`, undefined when the denominator is zero |
| `hodl_<band>` | share, 0…1 | Calendar-cohort share of live value by age band |

HODL bands are 0–1, 1–7, 7–30, 30–90, 90–180, 180–365, 365–730 and 730+ days.
The finite intervals use an inclusive lower boundary and an exclusive upper
boundary. Shares sum to approximately 1 when inventory is positive, subject to
floating-point rounding; they are undefined for zero inventory. These are
calendar-cohort calculations, not a per-output age proof at a daily block height.

The original files use UTC midnight timestamps as day labels. The joined file
uses ISO dates and retains the original values without converting their numeric
representations. Empty cells mean undefined values; do not silently replace them
with zero. Counts may be serialized with `.0` despite being integer-valued.
Amounts are BTC decimal strings; parse with decimal arithmetic for monetary
comparisons. Their serialization does not guarantee exact satoshi recovery for
every daily floating-point value. Checkpoint totals are separate integer-satoshi
fields.

## Known limitations

1. **Calendar anomaly, 2014-11-06 / 2014-11-07.** Published daily supply rises by
   approximately 14 745.38263159 BTC, then falls by 7 145.38263160 BTC. This is the
   only negative daily difference in this range. Nonmonotonic block timestamps
   and calendar accounting are a possible explanation; the affected blocks and
   outputs have not been individually traced in the supplied evidence. The
   explanation is not presented as a confirmed diagnosis. Do not use these rows
   as height-anchored supply checkpoints.
2. **Range boundary.** Data stops at block 617 698. The date 2020-02-16 labels the
   final row; completeness of that entire UTC day is not established. A future
   release should identify daily boundary heights and hashes explicitly.
3. **Partial audit coverage.** The successful 617 698 report is `GREEN`, but its
   `source_catalog` phase is `NOT_EVALUATED` and several heavy phases reuse prior
   evidence. Both successful reports record
   `historical_execution_provenance_complete=false`. A later report's `GREEN`
   does not erase those stated limits. See the evidence notes below.
4. **Aggregates are not a full-set proof.** Count, sum and block hash checks are
   useful but cannot replace a compatible project MuHash or a complete output
   comparison. The supplied reports and RPC responses are project/operator
   evidence, not an external audit.
5. **Historical calculator is not supplied.** The run manifest records r4 with
   SHA-256 `1bbed0fcbbd0872a127e3ad99c1a5a326340d071f08d8eda632557317dc04dc1`.
   The separately reviewed current file is r5 with a different hash. An exact
   r4 file and a pinned code revision have not been recovered. Consequently,
   byte-identical code reproduction is not established. See
   `evidence/CODE_IDENTITY.md`; do not replace the historical hash with r5's.

## Evidence notes

- `audit_v51_5_3_617698_…`: recorded status `GREEN`, certification label
  `V50_CANONICAL_CERTIFIED_R12_PROVENANCE`. Its state fingerprint matches the
  Stage-expected fingerprint. `source_catalog` is `NOT_EVALUATED`, an optional
  legacy phase is disabled, and historical execution provenance is incomplete.
  The label is quoted from the report; it is not reinterpreted as complete audit
  coverage or an external certification.
- `audit_v51_5_4_663917_…`: recorded status `GREEN` at a later height, with matching
  state and Stage fingerprints and `source_catalog=OK`. Historical execution
  provenance is still incomplete. Its Core-to-Stage phase imports previous
  ledger evidence; that underlying progress ledger is not bundled here.
- `audit_v51_5_4_core_chain_617698_OK_…`: reports comparisons at every height
  0…617 698 between the node's active chain and the Stage source, with zero
  mismatches. This is a chain-anchor comparison, not a Core UTXO MuHash comparison.
- `audit_v51_5_2_FATAL_…`: unsuccessful historical run. Heavy phases passed, but
  the V40 comparison reference stopped at 456 028, below target 617 698. The
  subsequent run verified that prefix and explicitly reused pinned heavy-phase
  results. The unsuccessful report remains under `evidence/context/` to preserve
  that evidence chain; its overall status is not changed to `GREEN`.
- The old manifest's `independent_state_audit_evidence` and historical
  `independent-auditor` names mean a separate implementation inside BitcoinVero.
  They do not identify an independent outside auditor. Original evidence names,
  contents and hashes have been preserved.
- Absolute paths in original reports describe the source host only. They are
  not portable download locations. The evidence package is not a complete copy
  of all state, Stage, source catalogue and progress-ledger inputs.
- `core_617698.json` and `core_663917.json` preserve all fields of the responses
  shown by the operator, including `block_info`. JSON formatting was transcribed
  for packaging; these are not direct byte captures from the node. The checksums
  identify the packaged files, not a cryptographic signature of the RPC server.

## Coin Metrics and excluded price-derived data

The private run manifest pins a file named `btc_usd_coinmetrics_v1.csv`. Its exact
input hash is recorded in `price/PRICE_SOURCE.json`; the download URL, acquisition
date, API metric and preprocessing provenance have not been recovered. The
filename alone does not establish that it was obtained under Community terms.

Official Coin Metrics Community documentation and its public data repository
identify CC BY-NC 4.0:

- https://docs.coinmetrics.io/packages/coin-metrics-community-data
- https://github.com/coinmetrics/data
- https://creativecommons.org/licenses/by-nc/4.0/

These terms permit noncommercial sharing and adaptation subject to their
conditions; they are not a blanket prohibition on publishing price data. They
also do not supply unconditional commercial reuse rights. This public package
does not assign a licence to, or distribute, the historical price series or the
11 related metric series. No conclusion is asserted about whether every
individual computed statistic is legally an adaptation. Recovering the input
provenance and applicable terms is required before deciding on a separate
price-derived release.

Excluding the raw price CSV alone would not resolve the question: in the reviewed
private data, `market_cap / supply` reconstructs all 3 501 daily price observations
within floating-point rounding. Accordingly, the market-cap series and all other
price-derived series have been withheld here. Metadata retained for audit
provenance does not grant rights in those unbundled inputs or outputs.

## Verify package integrity

From the extracted directory on GNU/Linux:

```sh
sha256sum --check SHA256SUMS
```

`MANIFEST.json` lists every payload file except itself and `SHA256SUMS`, to avoid
self-referential hashes. `SHA256SUMS` covers all files including `MANIFEST.json`
except itself. These checks detect changed bytes; they do not validate the
methodology or establish an author's identity.

## Кратко по-русски

Выпуск содержит 16 дневных рядов без долларовой цены: количество и сумму UTXO,
создания и закрытия выходов, траты, CDD, dormancy и возрастные доли. Период — от
генезиса до блока 617 698; последний день не заявлен как полностью закрытый.
Данные и собственные материалы в указанной области опубликованы под CC BY 4.0;
лицензия кода BitcoinVero остаётся отдельной.

На двух высотах количество UTXO и сумма совпадают с предоставленными ответами
Bitcoin Core до сатоши. Полное совпадение набора через MuHash и внешний аудит не
заявляются. Дневной supply — календарное накопление потоков, а не снимок на
последнем блоке дня. Аномалия 6–7 ноября 2014 года раскрыта; её точная причина ещё
не доказана. Исторический калькулятор r4 отсутствует, поэтому воспроизводимость
по точным байтам кода не подтверждена. Ценовые метрики исключены до выяснения
происхождения входного ряда и условий Coin Metrics.
