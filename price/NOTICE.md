# Historical price input — withheld

This directory contains input identity metadata only. It contains no prices,
and no price-derived metric series are included anywhere in this public package.

The private run used a pinned file named `btc_usd_coinmetrics_v1.csv`. Its download
channel, acquisition date, API metric and transformation history are not known
from the supplied evidence. Coin Metrics Community documentation identifies
CC BY-NC 4.0, but applicability to this exact file has not been established:

- https://docs.coinmetrics.io/packages/coin-metrics-community-data
- https://github.com/coinmetrics/data
- https://creativecommons.org/licenses/by-nc/4.0/legalcode.en

CC BY-NC 4.0 permits noncommercial sharing and adaptation subject to attribution
and its other conditions; it does not automatically grant commercial reuse.
The existence of a mathematical transformation alone does not settle which
copyright or database rights apply. The project does not assert that publishing
all derived metrics is prohibited, or that all such metrics are unconditionally
free of third-party rights.

The withheld market-cap series, together with published supply, could reconstruct
all 3 501 historical input prices to within numerical rounding. Not bundling the
raw CSV would therefore not by itself resolve redistribution concerns.

Before a separate price-derived release, establish the actual acquisition
provenance and applicable terms, identify the input metric and date convention,
and prepare suitable attribution, source/licence links and transformation notes.
If commercial rights are required, Community availability alone does not supply
them. No licence to unbundled Coin Metrics data is granted by this package.
