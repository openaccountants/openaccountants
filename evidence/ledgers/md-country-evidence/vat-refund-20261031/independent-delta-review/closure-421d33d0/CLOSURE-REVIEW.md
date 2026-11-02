# Independent bounded closure of Moldova VAT-refund repairs

Verdict: ACCEPT the repaired delta for partial tier-2 publication. All four initial findings are resolved; no remaining blocking finding in this reviewed delta. This is not country completion, domain completion, accountant attestation, approval to file, or proof of a green PR.

Exact reviewed HEAD: `421d33d0b4bdcedfcd09ea861dbf48b341a247e1`.
Writer repair manifest SHA-256: `f63d432c02e5bd0a7f3b1f87b87e39ba185cc43e241afdffa5483312362b99ae`.
Independent closure manifest SHA-256: `c2bac8bba6a407b3a97d2c8fcea98bfd5bd445c4bae3112d7786a745a83e8275`. It pins 715 current input/evidence files, including 669 historical evidence files, the initial review and original input snapshots. All 715 hashes matched at closure. The initial 31-input manifest and four-finding review remain immutable; this record supplements them.

## Findings closed

| Finding | Exact repair and verification | Result |
|---|---|---|
| MD-DR-01 | Ordinary cap row now tests payment at initiation of the audit; the base method first establishes deductible input paid at that time before unpaid-first output allocation. This matches HG93 point 35¹(2) and preserves point 38¹ ordering and the approved 2¹ control. | CLOSED |
| MD-DR-02 | e-Factura row says Registered VAT payer; the route-specific base method first confirms registration. This matches Code 101⁶(1); the nonregistered vehicle route remains distinct. | CLOSED |
| MD-DR-03 | MD-VATR-185 explicitly binds the current Code 101⁴ repeal, exact original-language text, official URL, article, read date, preserved source observation and context SHA. Original 184 rows are unchanged. | CLOSED |
| MD-DR-04 | Full repository General reference notice now follows H1, with This Guide terminology. No platform CTA was added or altered. | CLOSED |

Sources are the same [current HG93/2013](https://www.legis.md/cautare/getResults?doc_id=152472&lang=ro) and [current Fiscal Code](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro) independently read during the initial review. No new unsupported tax rule was introduced. Current 185 source bindings all pass independently rerun quote/context checks; semantic review of the original 184 rows is inherited unchanged from the initial review, plus this direct check of the added repeal row. This does not claim a second full re-reading of unchanged law or the sealed 3,913-row predecessor pack.

The additional intake change combines original questions 5 and 7 into one question, yielding six. Every original fact remains: prior refunds/offsets/assignment/dispute/other application, previous audits, scheme exclusions, December 2022 credit and criminal-proceeding suspension. The other five questions are unchanged. No eligibility fact was lost.

## Preservation and checks

- New Guide SHA-256: `33cad03c0ed10d7046cef011d1b6f4faf2d62ad6ded725fdbd62685c8b13e5c1`.
- 185-row ledger JSON SHA-256: `f81d5859d33c2c2f92c8f3f95e72d7102e39d4d82c772a41fdc37ae3db60c9f4`.
- Ledger Markdown SHA-256: `5714c5e8d25e684612580f0abcdb0f3713a7ac187a3b055479ab0068d1b003cf`.

The original 184 row objects and 242 VAT destination units are identical. All ten other Guides are byte-exact against 6637d0dbf, as are the initial seven review files, original five preserved input snapshots and the primary source captures. All 669 historical evidence hashes still match. The only active README change is 184→185 in its ledger count; all seven partial flags and remaining-job statements are unchanged. Lost content restored: 0; nothing was removed.

The two new examples are byte-exact against the initial reviewed version. Re-running the pack checker yields 22 oa-check blocks, 0 failures, 0 missing. Re-running the new Guide's ten skill checks yields 10 passes. The writer's strict metadata audit was inspected; GitHub CI, platform ingestion and authenticated filing remain untested by this reviewer.

All seven core domains remain partial. Excise, property, wealth, local, resources, road and tax-administration jobs and the already recorded ordinary/specialist gaps remain unfinished. This closure accepts the repaired refund-method delta only. Its pending-review prose may now receive a narrow dated pointer to this closure; a substantive change must receive a new bounded check.

Review files were written only inside this new closure directory. No Guide, README, initial review or Faroe accepted review was edited.
