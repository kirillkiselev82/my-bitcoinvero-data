# BitcoinVero — 2014-11-06/07 UTC calendar inversion validation

**Result:** `PASS` — the investigated BitcoinVero v2 daily supply anomaly is explained exactly by the UTC calendar-close causality rule applied to nine outputs. **Mismatch: 0 satoshis.** This is an explanation of the metrics' calendar accounting, not a full historical certification of the dataset.

## Context and observed blocks

The operator used a Bitcoin Core RPC node (`getblockhash`, `getblockheader`, and `getblock ... 2`) to export an adjacent block pair on Bitcoin mainnet:

| Height | UTC time | Block hash |
|---:|---|---|
| 328875 | 2014-11-07 00:03:02 | `00000000000000001866fcc86548d0ce02980c5cafbebef31de3601c0ea043df` |
| 328876 | 2014-11-06 23:57:14 | `000000000000000014957e9e22643209571d7e0519f0491d85614f3644c6eff6` |

Although block height increases, the next block's timestamp moves backwards by **348 seconds** (5 minutes 48 seconds) and crosses the UTC date boundary. The archive includes **501 contiguous headers** (328650–329150); the offline check found exactly one backwards *UTC date transition* in that range. A backwards timestamp within the same UTC date is not counted as a backwards date transition.

The operator's two-block RPC analysis identified **nine distinct eligible outpoints**, created at height 328875 and spent at height 328876, with a total of **1,089,538,263,160 sats = 10895.38263160 BTC**. Every outpoint has a unique `(txid, vout)` pair; the spend references involve six distinct transactions.

## Exact cross-check against v2 CSV

The following values are taken directly from the four original v2 metric CSVs, parsed as decimals:

| UTC date | created_btc | closed_btc | spent_btc | closed − spent (BTC) | Δ supply_btc (BTC) |
|---|---:|---:|---:|---:|---:|
| 2014-11-05 | 958586.36540753 | 955136.36540753 | 955136.36540753 | 0E-8 | 3450.00000000 |
| 2014-11-06 | 755795.97081008 | 741050.58817849 | 751945.97081009 | -10895.38263160 | 14745.38263159 |
| 2014-11-07 | 859523.14999217 | 866668.53262377 | 855773.14999217 | 10895.38263160 | -7145.38263160 |
| 2014-11-08 | 566350.1301227 | 562525.1301227 | 562525.1301227 | 0E-7 | 3825.00000000 |

At 2014-11-06, `closed − spent = −10895.38263160 BTC`; at 2014-11-07, the difference is `+10895.38263160 BTC`. The entire two-day offset matches the nine outpoints **exactly**; there is no remaining aggregate difference for these dates in these two CSV series. Note that `created_btc`, `closed_btc`, and `spent_btc` are independently serialized decimal values, so one-satoshi presentation differences can exist in a comparison against rounded round-number issuance.

## Verified producer rule

The supplied Metrics v4.4 source file SHA-256 is:

`65810f7a3521e22dceff7185b7726134dc268bd7d4e615ff7eaaa8a18c5cf249`

This **matches** the `metrics_code_sha256` field in the original H968206 Metrics manifest, tying the inspected code to the published v2 calculation. In `metrics_close_prepare`, the production policy is:

```python
cd = height_day[ch]
sd_raw = height_day[sh]
sd = np.maximum(sd_raw, cd)
```

The close path increments `closed_sats` by `sd`, the later of the UTXO creation UTC day and the spending block UTC day. Normal spends increment `spent_sats` by `sd_raw`, the original spending block UTC day. Thus the spending block at height 328876 is assigned to **Nov 6** in `spent_btc` and to **Nov 7** in `closed_btc` and calendar inventory accounting for the nine affected outpoints. The shift changes the per-day shape, but cancels over the two days.

This is a documented calendar-accounting choice, **not evidence of an incorrect UTXO set, excess issuance, missing bitcoins, or a need to rewrite the calculator**.

## Outpoints from the operator's Bitcoin Core RPC comparison

| Created outpoint | Spending transaction | Value, satoshis |
|---|---|---:|
| `1b149381259a2e6941b869066ee7621a9f5f53ff2cef8363444d0de054a19b89:0` | `7eacfe642b6a78c6902dd5e5cd0cad529360fdf554243c89401ba9fb94827d18` | 920,400,000,100 |
| `8cbc9bc2e8aae28e8a960f818db365ef522b39c874ac69b24bd5edc1a7bd4c39:1` | `d06b1cbd3dd9632d9d64ddcbb3242ce8aaa2912656f6c82e1b2a87955ad236f2` | 10,226,660 |
| `77ec0fa58aa3383f700a6d4715fed2b82281ce8717a5759c4f130ae2649b5d0c:0` | `d06b1cbd3dd9632d9d64ddcbb3242ce8aaa2912656f6c82e1b2a87955ad236f2` | 4,099,960,000 |
| `2a82a34dcfd511f468a632677224a479ec2431cbf43e331608e4c10a04b9b872:3` | `d06b1cbd3dd9632d9d64ddcbb3242ce8aaa2912656f6c82e1b2a87955ad236f2` | 160,189,246,000 |
| `c77addaed62c6148da82f968ab66c963214c27ccfe3841c35ab23c61a26cfce1:1` | `d06b1cbd3dd9632d9d64ddcbb3242ce8aaa2912656f6c82e1b2a87955ad236f2` | 32,319,110 |
| `6034e49e618604537eb7d05799b737dc44b0f10e0cc867d3d1a331755bf4c559:0` | `81d148d3dda87dd4cb7a40aebeda540b55e5d058ee53569aae5bf586a9467d12` | 1,665,000 |
| `4a2735fb0871955f6eaccf6eb3bb0f1b3b4b1a58b4be54e2f4cf76b84fc0ab5c:1` | `5bb6a11acfdf2385f8cd980111f0abf7df32d2a5658ab41d8fac752ff910e97e` | 361,170,000 |
| `9cc847680fc76637176b4f0ee2155733c9cdfa35fd4e2725b049a82d36c1ff2a:1` | `2c4a8a2d61cd46b3e2a3af209110bea1c1acb830c9bfd9467e772011580e0f0d` | 4,207,676,290 |
| `60e7a3afaab22480f3cf6eb90b2f5b81071521fe58a62a338d726bd1274e0b91:0` | `6225754e8edcdd752708bde870b0568f8d30d54da62b3f8228b839db8dd99952` | 236,000,000 |

**Total: 1,089,538,263,160 satoshis.** All nine entries are marked eligible in the original RPC-derived CSV; the eligibility decision was made by the collection script. The archive does not include the full raw blocks/scripts to independently recompute eligibility from Bitcoin Core, although the individual outpoint identifiers are supplied for reproduction.

## Evidence and verification boundary

- Four byte-preserved operator-generated files are in `original/`: header CSV, date inversion report, outpoint CSV, and spending report.
- `validation_summary.json` records source archive SHA-256, full inspected Metrics v4.4 file SHA-256, v2 CSV content hashes, block IDs, and validation assertions.
- The review **independently recomputed** header timestamp/date consistency, contiguous height coverage, exact outpoint sum, uniqueness and v2 CSV decimal identities from the supplied exported files, and confirmed the code/manifest identity.
- It **did not re-query the Bitcoin Core node or perform a raw block / transaction-script verification**. For a stronger independent proof, re-fetch blocks 328875 and 328876 and verify all nine `(txid, vout, value)` links and scripts from their raw transaction data.
- This finding does not amend the producer manifest's `COMPUTED_WITH_LIMITED_VALIDATION` classification and does not extend the auditor's `STATE_CONSISTENCY` certificate to historical daily metrics.

## Publication note

In the user-facing README, it is sufficient to describe the UTC block-timestamp grouping and the creation-date clamp. Preserve this targeted case study under `evidence/validation/` to avoid implying that every calendar-day data point corresponds to an independently certified height-anchored UTXO snapshot.

## Source identification

- Original investigation archive SHA-256: `6fbe707451f245c1499e93e289f2d78f1c3a96cf63a2a6529fd8a5b88da616d9`
- `bv_2014_headers.csv` SHA-256: `28c0dd6d4e8d679292644dde2e2a5efdab3934954a80f1596837d9b7f7913871`
- `bv_2014_cross_date_outpoints.csv` SHA-256: `ae97a6f40fd7f665f4ef388e347dc62ddf105d0e39329c5fda20dfff4c09dd91`
- v2 `utxo_supply_btc.csv` SHA-256: `88c49d24ece549a7b248b2aa5ba6a6f596783a12a39f1d679baa73f5f9f6e581`
- v2 `utxo_closed_btc.csv` SHA-256: `591f5f32bcc4d136d421e3b0698ccda76eadbecc4fabd16f496c40b665685af7`
- v2 `utxo_spent_btc.csv` SHA-256: `b90b1cee64bec74ca2ba9b991e5864ef77d44d39e75f521e82216448128af10c`
- v2 `utxo_created_btc.csv` SHA-256: `ed9fbe245351000b1cd2c26a9b96b2f4037a21d182d8d9fc33d5319dbe55bc5c`

All times are UTC. All comparisons against the outpoint values use integer satoshis.
