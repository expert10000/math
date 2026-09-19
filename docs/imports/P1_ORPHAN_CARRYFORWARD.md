# P1 orphan carry-forward

This pass restores only previously established P1 editorial decisions:

- prior `NOT_A_PROBLEM` terminal dispositions are restored;
- prior accepted links are restored only when the exact prior target problem ID
  is still active in the current ledger;
- inactive prior targets are left for explicit remapping.

It does not link anything based solely on refreshed similarity scores.

The same bundle also generates a review-only P2/P3 packet.
