# BV-R002 — additional public evidence (v1.2)

The files daily_diff.csv and candidate_blocks.csv are byte-for-byte copies of the operator run outputs (SHA-256 in additional-SHA256SUMS). The former contains all 43 changed dates; the latter contains the 72 candidate spending-block heights and number of matched inputs, including zero-match candidates.

For a CSV-only reproduction, download the two original wide CSVs from their immutable release tags and run compare_releases.py from this directory:

    curl -fL -o v1.csv https://gitlab.com/bitcoinvero/bitcoinvero-data/-/raw/v1.0.0/data/onchain_daily.csv
    curl -fL -o v2.csv https://gitlab.com/bitcoinvero/bitcoinvero-data/-/raw/v2.0.0/data/onchain_daily.csv
    python3 compare_releases.py v1.csv v2.csv --out reproduced
    cmp daily_diff.csv reproduced/daily_diff.csv
    cmp episodes.csv reproduced/episodes.csv

The original CSV files are hash-pinned in the script. Python 3.9+; standard library only. This checks aggregates, not outpoint identities.

For an independent raw-block check, use a non-pruned Bitcoin mainnet node anchored at heights 617698 and 968206 (hashes in result.json). Enumerate all earlier heights with a UTC date later than each spending block's UTC date, not just adjacent heights. Fetch raw blocks, compute TXIDs and Merkle roots, join input prevouts to candidate creation outputs, and add value in integer satoshis and one input to the raw spending date while subtracting both from the creation date. Compare all 4061 dates, including zeros. The candidate list is a cross-check, not a complete replacement for scanning the headers.

Publication status: compact evidence and CSV comparator are public in this directory. The raw header/block archive, full outpoint registry and original causal/offline parsers are not yet available here. The producer source files remain non-public. Do not interpret the receipts as a full independent UTXO audit or third-party attestation.
