# Niger: independent review and finite corrections

17 November 2026. PR #2156 was merged before its independent source review.
This record binds the completed first review and its three corrections. No
accountant approval or complete filing clearance is granted.

The separate first reader checked all 60 writer ledger rows, 68 original
nonblank-line destinations and six cases. All numerical case outputs recomputed.
Two VAT cases nevertheless asserted deduction entitlement that the skill's
unread entitlement, timing and pro-rata rules could not establish. The corporate
accounting paragraph also omitted a statutory sector exception, and one source
locator ended a page before the rule it supported.

| Finding | Correction and operative source |
|---|---|
| N1: VAT entitlement | Description, scope and both cases now stop at the amounts surviving the specified exclusion screens. The original facts and numerical results remain. The advertising lot is XOF 2,000,000 before VAT, with no supplied payment method; the bank-payment question remains unresolved. Neither case establishes a deductible total. [CGI 339(c), (g), finance ordinance PDF pages 14-15](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44). |
| N2: accounting scope | Entities outside the OHADA accounting system's scope must use the prescribed sector or status-specific system, expressly including banks, financial establishments and insurers. Place, language, separate accounts and translation rules remain. [CGI 799(5), PDF page 29](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44). |
| N3: locator | The corroborated bank loan-income and own-funds exception remains unchanged; the corporate paragraph and source-read scope now include PDF page 9. [CGI 180(h)](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44). |

The writer's finite correction is commit
`e68885f2f899686047dbf94b88df5aee539b3137`. The separate first reader then checked
all three changes and dependencies, returning PASS with existing limits. The
two source files bind to:

| File under skills/niger/ | SHA256 |
|---|---|
| ne-corporate-income-tax.md | `3a13327531c164b621dfcf5a293454cfd029f89ce99945637e4e45838a5ff3eb` |
| ne-vat-gst.md | `bd350b715577d59582ad3216fd9fb45308215e5404fa28c54539a1861e9311a3` |

Original case input blocks and all numerical expected values are unchanged.
VAT output names now describe potential amounts, rather than a legally
established deduction. Both versions advance from 0.1 to 0.2; the actual edit
date remains 17 November. Payroll, names, approval fields, licence, CTA,
calculator quotations and the existing non-usable holds remain unchanged.

The first reader corroborated all 38 scanner MISS occurrences against the
actual retained ordinance and CNSS sources. The earlier figures job still
failed mechanically; its result is not relabelled green. Current-head hosted
checks and any occurrence-specific explanations remain separate merge gates.
Completed source, old-topic and unchanged arithmetic work is reused after its
applicability check, rather than represented as a new whole-pack review.

The external canonical records are `niger-publication-review/RECEIPT.json`,
`ROW-RESULTS.json`, `OLD-TOPIC-AUDIT.json`, `CASE-RECOMPUTATIONS.json`,
`FIGURE-DISPOSITIONS.json`, `SOURCE-MANIFEST.json` and
`delta-e68885f2/RECEIPT.json` under the 17 November nine-chat evidence directory.
The actual finance ordinance has SHA256
`a841c4fa47e4db2b174ea2085050b92ffd84f183039c5cfd5d4bec9a2281f42e`.
These records distinguish actual source reads from failed access attempts.

Root alone controls merge and delivery. No merge occurs during active or
queued ingestion. Publication remains a separate normal admin action.

Written by Codex. Not reviewed by an accountant.
