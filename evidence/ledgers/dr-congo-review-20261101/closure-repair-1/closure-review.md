# Independent closure: DR Congo repair 1

Decision: **ACCEPT the two source-cited 2026 drafts for their explicitly partial scope.** Bound to frozen Git HEAD `ddde60a16e113f9056297e6d6ae09d0294bec075` on `codex/dr-congo-tax-2026`, reviewed 2026-11-01. This closes F1 and F2 from the preserved initial rejection. It is not accountant attestation, comprehensive country-pack completion, verification of six retained 2025 Guides, approval of a tax return or proof of an accepted filing. No push, PR, comment, merge or publication was performed by this reviewer.

## Candidate identity

The repair manifest SHA256 is `0e4d8c0495edf354764dcf4b927a240ff9e892cd17a32efbe2c06e085df4cfd9`. All five hashes it specifies match the actual frozen candidate. Exact checked inputs:

| File | SHA256 |
|---|---|
| skills/dr-congo/cd-transfer-pricing.md | eaf229a8e5b8d73421245a15842c4b38b5ba9459d91980def7ea5154eccf144e |
| skills/dr-congo/cd-cross-border.md | 56f4aa2e49baef36617c51a8ed749d663a76ba1a68b9e5468b94d4afd75ac805 |
| evidence/ledgers/cd-transfer-pricing.md | cba6f33709282bde196fbb623371aabf6d9fb4447d9b26b7bcddd90dd9c2f4b0 |
| evidence/ledgers/cd-cross-border.md | 316036fe631be133b6406a2dd2694a8814d3aefa5ce30ef22bb8bc9b22a2f006 |
| evidence/ledgers/dr-congo-draft-20261101/source-record-repair-1.json | 684ac141b7d7b2d58f6a47f3d31ec1aa15c5cf56c189ebb380ae3b8868907b75 |

The initial source-record.json and candidate-manifest.json remain byte-exact against initial HEAD `aab7ad45549b4926e8619cd280ca52401a90a56b`. The initial review report remains SHA256 `572dba48310ccf69b622cb86c79e7888e8502ca6b20c7120d076fefccbeeda09`. The initial review evidence remains alongside this separate closure directory; none was overwritten. README and all six old Guide hashes are unchanged. The original source PDF identities remain those checked in the initial review; no replacement source was introduced.

## Closed findings and source checks

| Finding | Repair verified | Citation and result |
|---|---|---|
| F1 | TP Cross-border points and ledger row 014 now include both privileged-tax alternatives: not taxable in the foreign state, or a foreign profit/income-tax amount more than half lower than ordinary hypothetical Congolese IS. The amount comparison and hypothetical domestic operation are retained. | Law 23/053 art. 47, combined PDF page 23, original French scan read in the initial review: “si elle n'est pas imposable dans cet État ou”. The repaired wording and two short excerpts match both branches. https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf |
| F2, original Finance Act | Both Guides now cite art. 88, and TP038/XB033 record the 1 January 2026 commencement, article, original French quote and PDF page 53. | Finance Act 25/060 art. 88: “à la date du 1er janvier 2026”. Original page 53 was visually checked in the initial review. https://www.budget.gouv.cd/wp-content/uploads/budget2026/lf_2026_recettes.pdf |
| F2, procedure reform | Both Guides cite the separate Law 23/052 art. 6; TP039/XB034 record its 24-month commencement from 31 December of promulgation year, with the correct combined PDF page 8. | Law 23/052 art. 6, signed 30 November 2023: “après vingt-quatre mois à compter du 31 décembre”. The original page 8 was also visually checked after the initial report. This supports application in 2026 and does not borrow Law 23/053's commencement without checking. https://dgi.gouv.cd/wp-content/uploads/2025/09/loi-is-et-Irpp.pdf |
| Provenance clarification | A distinct source-record-repair-1.json preserves the initial source-record hash, adds the actual new/repeated repair reads, and explicitly says they are not retrospectively attributed to the initial candidate. It resolves the earlier scan-pending note. | Source records distinguish full captures from pages actually read. Original records remain intact. No authenticated form inspection or new professional review is claimed. |

Checked the complete initial-to-repair diff, not only the snippets describing the fixes. The only changed original ledger row is TP014. Four commencement rows were added. All other 68 original rows are unchanged. The original review covered 69 rows; closure covers the one changed row and four added rows. The candidate therefore contains **73 reviewed ledger rows: TP 39 and XB 34**, comprising 71 PDF rows and two HTML-link rows. This is a row count, not a claim of 73 unique numerical figures. No unresolved rejection finding remains within these drafts' declared scope.

## Examples, metadata and preservation

Both Guides advance from v0.1 to v0.2, with matching body titles. All four worked examples, their prose assumptions, arithmetic blocks and results are byte-exact against the initial candidate. The initial manual results therefore remain applicable: TP adjustment CDF 200,000 and adjusted profit CDF 5,200,000; conditional TP penalty CDF 160 million; service withholding/net CDF 1.4 million/CDF 8.6 million; passive withholding/net CDF 1.6 million/CDF 6.4 million and classification difference CDF 480,000. Four blocks were recomputed again successfully at closure.

Closure validation passed: changed-only validate-guides with --no-index-check; all 15 skill checks for both Guides; all four oa-check blocks; strict metadata/sync-integrity audit from the initial candidate to the repaired HEAD. Exact commands and complete outputs are in closure-validation.json. The dependency path and generated-index exclusion are the same as the initial review. Exact file and preservation assertions are in closure-input-hashes.json.

All six old Guide hashes match the initial retention evidence and base bytes; the 86-topic destination map is unchanged. Lost content restored: **0**. Retention is not legal validation of their old claims.

## Scope that stays unresolved

Acceptance preserves the initial review's explicit gaps: current TP file specifications/forms, authenticated submission and receipts, CbC lists/notifications/conversion instructions, non-cooperative list, treaty/corresponding-adjustment procedures, complete general penalties/interest/dispute treatment, technical-service/passive-income overlap, mixed contracts, earlier royalty treatment, sector privileges and the wider residence/credit/exit jobs. The country README remains partial in every domain. Pending-review phrasing in the frozen local drafts is conservative status text; this closure report records the independent source-review completion for exactly the bytes above and confers no accountant attestation.

A later edit to tax content or source conditions requires review of that changed candidate. A later commit that only adds this closure evidence can reference these same file hashes without claiming a new substantive review.
