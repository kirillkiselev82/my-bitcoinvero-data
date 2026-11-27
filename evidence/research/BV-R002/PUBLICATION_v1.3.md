# BV-R002 — published evidence pack v1.3

The operator reports successful upload (HTTP 201 for both files), unauthenticated download, byte identity and complete offline replay (PASS). See the machine-readable [publication receipt](publication_receipt_v1.3.json). This new receipt supersedes the preparation status in the earlier manifest; no historical files have been removed or rewritten.

- [Full evidence ZIP](https://gitlab.com/api/v4/projects/87308878/packages/generic/bv-r002-evidence/1.3.0/BV-R002_evidence_pack_v1.3.zip)
- [Detached SHA-256](https://gitlab.com/api/v4/projects/87308878/packages/generic/bv-r002-evidence/1.3.0/BV-R002_evidence_pack_v1.3.zip.sha256)

Run in an empty directory with Python 3.9+ and unzip:

```sh
curl -fL -O 'https://gitlab.com/api/v4/projects/87308878/packages/generic/bv-r002-evidence/1.3.0/BV-R002_evidence_pack_v1.3.zip'
curl -fL -O 'https://gitlab.com/api/v4/projects/87308878/packages/generic/bv-r002-evidence/1.3.0/BV-R002_evidence_pack_v1.3.zip.sha256'
sha256sum -c BV-R002_evidence_pack_v1.3.zip.sha256
unzip -q BV-R002_evidence_pack_v1.3.zip
cd BV-R002-evidence-v1.3
python3 -B verify_pack.py ../BV-R002_evidence_pack_v1.3.zip
```

No credentials or RPC are needed for this offline path. Expected PASS: 4,061 daily comparisons, zero mismatching dates, 1,169 / 1,331 matched outpoints. The historical Metrics source files are not distributed. A full producer or consensus audit is not claimed. The README inside the immutable ZIP describes its pre-publication state; this receipt records the subsequent upload.
