# Companion Part II solution-quality audit

This is the first full 570-pair editorial triage against
`COMPANION_SOLUTION_EDITORIAL_STANDARD.md`.

The audit is deliberately separate from solution coverage. It does not modify
the Part II mathematics.

## Coverage

- audited problem/solution pairs: **570**
- source-backed provenance rows: **165**
- canonical-authored provenance rows: **405**

## Quality result

- `A_STRONG`: **310**
- `B_POLISH`: **260**
- `C_REWRITE`: **0**
- `D_BLOCKING`: **0**

## Priority queues

- `P0`: **0**
- `P1`: **0**
- `P2`: **260**
- `P3`: **310**

## Interpretation

This audit is a deterministic editorial triage. `D_BLOCKING` includes exact
pairing failures and selected known mathematical regression gates from the
Part II completion pass. `C_REWRITE` captures large overmerges, fragments,
and solutions that are too short for the task. `B_POLISH` captures pairs
that are basically usable but do not yet meet the Part III editorial
convention.

The rewrite/polish passes should still read the exact current problem and
solution before changing mathematics; the audit is a queue, not a substitute
for mathematical review.

## D_BLOCKING queue

None.

## C_REWRITE queue

None.

## B_POLISH queue

`CP-II-0008`, `CP-II-0021`, `CP-II-0030`, `CP-II-0035`, `CP-II-0069`, `CP-II-0072`, `CP-II-0082`, `CP-II-0166`, `CP-II-0223`, `CP-II-0269`
`CP-II-0297`, `CP-II-0299`, `CP-II-0301`, `CP-II-0367`, `CP-II-0426`, `CP-II-0443`, `CP-II-0479`, `CP-II-0492`, `CP-II-0010`, `CP-II-0012`
`CP-II-0077`, `CP-II-0096`, `CP-II-0139`, `CP-II-0172`, `CP-II-0225`, `CP-II-0252`, `CP-II-0279`, `CP-II-0280`, `CP-II-0328`, `CP-II-0429`
`CP-II-0438`, `CP-II-0459`, `CP-II-0499`, `CP-II-0528`, `CP-II-0535`, `CP-II-0552`, `CP-II-0001`, `CP-II-0002`, `CP-II-0003`, `CP-II-0004`
`CP-II-0007`, `CP-II-0011`, `CP-II-0016`, `CP-II-0019`, `CP-II-0020`, `CP-II-0024`, `CP-II-0025`, `CP-II-0027`, `CP-II-0033`, `CP-II-0034`
`CP-II-0036`, `CP-II-0039`, `CP-II-0042`, `CP-II-0043`, `CP-II-0044`, `CP-II-0045`, `CP-II-0046`, `CP-II-0049`, `CP-II-0050`, `CP-II-0053`
`CP-II-0056`, `CP-II-0058`, `CP-II-0063`, `CP-II-0071`, `CP-II-0074`, `CP-II-0078`, `CP-II-0079`, `CP-II-0080`, `CP-II-0084`, `CP-II-0087`
`CP-II-0095`, `CP-II-0097`, `CP-II-0101`, `CP-II-0102`, `CP-II-0103`, `CP-II-0104`, `CP-II-0105`, `CP-II-0106`, `CP-II-0107`, `CP-II-0118`
`CP-II-0120`, `CP-II-0121`, `CP-II-0123`, `CP-II-0124`, `CP-II-0125`, `CP-II-0126`, `CP-II-0128`, `CP-II-0140`, `CP-II-0141`, `CP-II-0144`
`CP-II-0147`, `CP-II-0148`, `CP-II-0150`, `CP-II-0156`, `CP-II-0157`, `CP-II-0160`, `CP-II-0164`, `CP-II-0165`, `CP-II-0169`, `CP-II-0176`
`CP-II-0177`, `CP-II-0178`, `CP-II-0186`, `CP-II-0187`, `CP-II-0188`, `CP-II-0192`, `CP-II-0193`, `CP-II-0195`, `CP-II-0196`, `CP-II-0200`
`CP-II-0201`, `CP-II-0204`, `CP-II-0205`, `CP-II-0207`, `CP-II-0208`, `CP-II-0209`, `CP-II-0210`, `CP-II-0213`, `CP-II-0214`, `CP-II-0219`
`CP-II-0220`, `CP-II-0221`, `CP-II-0222`, `CP-II-0224`, `CP-II-0226`, `CP-II-0227`, `CP-II-0228`, `CP-II-0233`, `CP-II-0234`, `CP-II-0235`
`CP-II-0236`, `CP-II-0239`, `CP-II-0240`, `CP-II-0243`, `CP-II-0244`, `CP-II-0245`, `CP-II-0246`, `CP-II-0247`, `CP-II-0254`, `CP-II-0255`
`CP-II-0256`, `CP-II-0258`, `CP-II-0259`, `CP-II-0263`, `CP-II-0264`, `CP-II-0270`, `CP-II-0272`, `CP-II-0275`, `CP-II-0284`, `CP-II-0287`
`CP-II-0288`, `CP-II-0290`, `CP-II-0292`, `CP-II-0295`, `CP-II-0302`, `CP-II-0306`, `CP-II-0307`, `CP-II-0313`, `CP-II-0314`, `CP-II-0318`
`CP-II-0335`, `CP-II-0337`, `CP-II-0342`, `CP-II-0343`, `CP-II-0356`, `CP-II-0361`, `CP-II-0362`, `CP-II-0364`, `CP-II-0368`, `CP-II-0369`
`CP-II-0370`, `CP-II-0374`, `CP-II-0376`, `CP-II-0378`, `CP-II-0379`, `CP-II-0381`, `CP-II-0382`, `CP-II-0384`, `CP-II-0386`, `CP-II-0387`
`CP-II-0390`, `CP-II-0392`, `CP-II-0394`, `CP-II-0397`, `CP-II-0398`, `CP-II-0399`, `CP-II-0400`, `CP-II-0401`, `CP-II-0402`, `CP-II-0409`
`CP-II-0412`, `CP-II-0416`, `CP-II-0418`, `CP-II-0419`, `CP-II-0421`, `CP-II-0423`, `CP-II-0425`, `CP-II-0430`, `CP-II-0431`, `CP-II-0437`
`CP-II-0442`, `CP-II-0448`, `CP-II-0449`, `CP-II-0456`, `CP-II-0463`, `CP-II-0465`, `CP-II-0472`, `CP-II-0474`, `CP-II-0481`, `CP-II-0482`
`CP-II-0483`, `CP-II-0486`, `CP-II-0489`, `CP-II-0493`, `CP-II-0503`, `CP-II-0505`, `CP-II-0509`, `CP-II-0512`, `CP-II-0513`, `CP-II-0515`
`CP-II-0521`, `CP-II-0522`, `CP-II-0524`, `CP-II-0525`, `CP-II-0526`, `CP-II-0527`, `CP-II-0529`, `CP-II-0531`, `CP-II-0537`, `CP-II-0541`
`CP-II-0542`, `CP-II-0546`, `CP-II-0553`, `CP-II-0555`, `CP-II-0557`, `CP-II-0558`, `CP-II-0562`, `CP-II-0566`, `CP-II-0570`, `CP-II-0018`
`CP-II-0112`, `CP-II-0119`, `CP-II-0159`, `CP-II-0174`, `CP-II-0182`, `CP-II-0197`, `CP-II-0377`, `CP-II-0461`, `CP-II-0462`, `CP-II-0567`
`CP-II-0076`, `CP-II-0111`, `CP-II-0143`, `CP-II-0198`, `CP-II-0363`, `CP-II-0373`, `CP-II-0410`, `CP-II-0466`, `CP-II-0496`, `CP-II-0510`
