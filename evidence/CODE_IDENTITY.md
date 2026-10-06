# Historical metrics calculator identity

The original run manifest records:

- Version: `utxo_metrics_v4-r4-v50-r12.9-prod`.
- Expected script SHA-256:
  `1bbed0fcbbd0872a127e3ad99c1a5a326340d071f08d8eda632557317dc04dc1`.
- Canonical operator filename: `/root/mybot/utxo_metrics_v4`.

The script separately supplied in the private review archive has:

- Version: `utxo_metrics_v4-r5-v50-r12.9-lineage-prod`.
- Observed script SHA-256:
  `c26a1c1ae699060441484b3ecd2d7698227915fc68291fab60b61288d9745c7e`.

Both the recorded version and the bytes differ. The current r5 file is not the
historical file pinned by the manifest. This does not by itself prove a numerical
error, but it prevents asserting byte-identical code reproduction. The exact
historical r4 file and a corresponding immutable repository revision have not
been recovered in the supplied materials. The hash of a GitLab copy has not been
independently verified in this review.

Status: **HISTORICAL_CODE_NOT_AVAILABLE; BYTE_EXACT_REPRODUCTION_NOT_ESTABLISHED**.

The public package includes neither script. Do not edit the original manifest to
substitute r5's hash, and do not label r5 as the script used for this historical
run. Recovery should locate the original bytes in backups or repository history,
verify the complete expected SHA-256, publish that version under the existing
code licence and provide an immutable revision link. A new calculation with r5
would be a separate run with a new manifest, not a repair to old provenance.

Recovering a script alone would not complete end-to-end reproduction: exact state,
Stage inputs, source/ledger evidence and applicable input permissions must also
be identified. The canonical production filename need not be changed to recover
or publish a historical version.
