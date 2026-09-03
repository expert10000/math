# Volume VIII - Algebraic Topology Release

This release freezes the complete 35-chapter canonical Volume VIII after:

1. full one-to-one legacy corpus reconciliation;
2. canonical Problem/Exercise pairing audit;
3. duplicate-label and active-include audit;
4. reconciliation-manifest drift verification;
5. clean `latexmk` PDF build;
6. undefined-reference/citation regression check;
7. visual inventory preservation;
8. chapter-status transition to `FROZEN / COMPLETE`;
9. SHA-256 freeze manifest generation.

The release commit is source-authoritative.  The generated PDF is built and
hashed during freeze; it need not be committed if repository ignore policy
excludes build products.
