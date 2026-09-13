# v1.3 Freeze-Manifest Canonicalization

**Status: PASS**

Freeze-manifest hashes are canonicalized to the SHA-256 of the immutable Git blob bytes
for each tracked manifest target. This makes the freeze contract independent of Windows
checkout EOL/filter representation.

- Volumes: 8
- Manifest rows: 2117
- Rows changed: 254

| Volume | Rows | Changed |
|---|---:|---:|
| I | 36 | 25 |
| II | 40 | 13 |
| III | 45 | 43 |
| IV | 56 | 25 |
| V | 45 | 16 |
| VI | 1668 | 47 |
| VII | 96 | 27 |
| VIII | 131 | 58 |
