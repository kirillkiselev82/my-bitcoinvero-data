# BV-R002 — BitcoinVero Research

## Public evidence index (v1.2)

Scope: historical calendar attribution of normal Bitcoin UTXO spends in releases v1.0.0 and v2.0.0. Comparison interval: 2009-01-03 through 2020-02-15 inclusive. The last UTC day of v1 is excluded as a boundary day.

The operator's read-only Bitcoin Core run and a separate offline implementation on data from the same node returned PASS: 968207 headers, 72 candidate spending blocks, 111 raw blocks, 30468 transactions, 1169 affected outpoints in v1 and 1331 in v2. All 4061 daily deltas in spent value and input count match, with zero residual. Gross nominal value in v1: 24084.21374030 BTC; sum of positive daily net changes: 24077.02250364 BTC. March 29–31, 2014 explains the 7.19123666 BTC and five-input netting difference.

## Published here

- result.json — operator RPC verification receipt.
- offline_receipt.json — independent implementation replay receipt (same node data).
- episodes.csv — 21 contiguous episodes, 43 dates. Values are integer satoshis.
- Original datasets: [v1.0.0](https://gitlab.com/bitcoinvero/bitcoinvero-data/-/raw/v1.0.0/data/onchain_daily.csv), [v2.0.0](https://gitlab.com/bitcoinvero/bitcoinvero-data/-/raw/v2.0.0/data/onchain_daily.csv).

CSV SHA-256:
- v1: e8dae3aa663bec46f8848a8bc09c7ded1d2e35bb8a8cf649d653a0ff91882ee9
- v2: 3ad5f40c86988e525f06b3e7db67a5494c9e911f0bcba9abc31c6dda9be54d0b

## Publication boundary

This is a compact evidence index, not yet the complete raw evidence archive. The original operator archive BV-R002-research.zip (SHA-256 25b472325271032e76fa8e8b44bf56f6767aa2689a4ca14a9075af2739e9063e) and both verification implementations are retained for publication separately. Producer sources r4 and v4.4 are not included. The recorded hashes identify the inspected versions, but external readers cannot verify those source bytes without obtaining them. No full UTXO or consensus audit is claimed. Existing historical release tags are unchanged.
