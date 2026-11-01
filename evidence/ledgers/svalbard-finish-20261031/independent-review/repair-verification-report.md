# Independent repair verification, 31 October 2026

Verdict: **pass for the staged additions, with the published scope limits**. Both findings from the initial review are closed at commit `d89d6877bea2fdf0dd9d8cbe11dd942bae425dc6`. The country remains partial and the full-country goal remains unachieved. This is independent AI review, not accountant attestation or filing-ready approval.

| Initial finding | Repair checked | Result |
|---|---|---|
| F1, omitted shipment security | Coal Guide now states that security can be required at shipment as a percentage of estimated cargo value, with further rules prescribed by the King. It requires the actual requirement, percentage, valuation and security evidence, and does not substitute the annual duty rate. Checked against the already independently read Act section 2 fourth paragraph and unchanged ledger R005. | Closed |
| F2, descriptions shorter than specification | Environmental description now has 112 words; coal has 116. Both fall within 80 to 150 words. Added material accurately describes existing reconciliation, claimant, assessment, evidence and explicit-limit content. | Closed |

Coal statutory source: https://lovdata.no/dokument/NL/lov/1925-07-17-2. No new tax figure, exemption, operational interface or interest rate is introduced by the repairs.

Exact reviewed Guide SHA256 values:

| Guide | SHA256 |
|---|---|
| sj-svalbard-visitor-environmental-levy | `5557dc93766583516b1f7b86aef349a9e36d172dff2750f1d3a43b3730d2c8a6` |
| sj-svalbard-coal-export-duty | `abb4372e13d8d4ede15d4896efce5cfdefc5553f8ad6a3d6fbdac7da873f16e4` |

The 47 legal ledger rows retain exactly the same quotations, read dates and source identifiers as the initial candidate. All four derived-control records and executable examples are unchanged. Refreshed ledger Guide hashes match, every nonblank new Guide line is mapped, and every mapped line hash matches. Every refreshed writer candidate-manifest entry matches the current file.

All six older Guides, README, original 24 October review, seven supplied HTML/text source pairs, source receipts, original form observation and original preservation table remain unchanged from the initial reviewed candidate. The initial review records and browser captures are preserved separately; this repair record does not rewrite their original findings. Exact preservation and current-file hashes are in `repair-verification-checks.json` and `repair-manifest.json`.

Re-ran the standard example checker: **two files, four blocks, zero failures, zero missing**. Re-ran both Guide shape checks: **all ten checks pass for each Guide**. Output is preserved in `repair-test-results.json`. Repository-wide tests and PR CI were not independently rerun for this prose-only repair; this verdict does not assert their status.

The initial substantive review continues to apply to the unchanged legal content. The declared aviation exceptions, carrier settlement/remittance, post-access refund fields/receipt, coal filing format/evidence/channel, coal annual interest rate and beyond-final-band treatment remain unresolved. The README continues to keep the country issue open and disclaims an exhaustive applicability audit. No new source research or authority contact was needed for this bounded repair verification.
