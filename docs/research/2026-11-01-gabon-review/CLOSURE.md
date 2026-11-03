# Gabon focused independent closure, 1 November 2026

**F1-F4 are closed for the exact frozen file hashes below.** The minor six-children clarification is also closed. No further correction was found in this focused review. The source review passes for an explicitly partial research draft only. It does not certify operative 2026 law, accountant attestation, filing readiness, country completion or merge.

This closure supplements, and does not rewrite, the original `REVIEW.md` and its immutable-candidate evidence. The original review remains the record of the defects in commit `d90a78e28adb1804d0e1fd904886dc16c00cd2bb`, against base `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`. This repair candidate was reviewed as working-tree content, so acceptance is by content hash rather than an invented new commit id.

## Accepted candidate hashes

| File | Accepted SHA-256 |
|---|---|
| `skills/gabon/ga-vat-gst.md` | `c6965cd791352aba24e4034ab1c3c8019aa7396c5a7c05bff32e550fb06fc32a` |
| `skills/gabon/ga-payroll-social.md` | `ff22da19b9ee0c79b0e38b49ed21fac45c68986f871b61e6838ec6143494d7b4` |
| `docs/research/2026-11-01-gabon-pack/rules.json` | `841defae1def3659bd0f74f325514672782b956816dc0ab8da1b7ca3e70f8b7a` |
| `docs/research/2026-11-01-gabon-pack/ledgers/ga-vat-gst.md` | `b8a2c7d49b246ce61938ded81c81c616866a5de9a5cbda53f8cf28d15ad10ed7` |
| `docs/research/2026-11-01-gabon-pack/ledgers/ga-payroll-social.md` | `c5f0f9a64f400fd8dca65c32d3412d9b686f94c9894ba9940eeb6965fc8c13a7` |
| `docs/research/2026-11-01-gabon-pack/ledgers/ga-income-tax.md` | `ec607d842061d7d2bb12c27b02f03b0367b600697fb1fc4f43d903feac32afd8` |

The writer correction receipt itself hashes to `eb14d7d5ca49ca8f482919d6661149a63b6252c176764d56e466475904a632e3`. Its six recorded candidate hashes all match the actual bytes. `CLOSURE.json` also records the corresponding Git blob identifiers and the unchanged hashes of the other six Guides.

## Source and correction checks

Independently re-extracted and read actual CGI PDF pages 39-41, 72-74 and 83-85 from the original hashed PDF, including neighbouring provisions. Its SHA-256 remains `69fdb3d87ede508e412fed7561a256ced70401778ca25489ec90454b1fefdca9`, the source independently obtained through validated HTTPS in the initial review. The new supporting-source objects carry the matching official URL, read date, source hash, article, page and exact quote, and both matching writer ledger blocks carry the same evidence.

| Finding | Closure evidence |
|---|---|
| F1 | VAT Guide and `V-PRORATA` now apply article 226 direct attribution first and the ratio only to shared inputs. Article 226 on PDF page 84 says « seule la fraction de la taxe qui les a grevées est déductible par application d’un prorata ». The taxable-only/non-deductible-only branches were read in full. The July article 227 percentage wording and exact 90% hold remain unchanged. |
| F2 | Payroll Guide and `P-CAR` now state the adjacent baseline non-cumulation condition, cite CGI article 91 bis and retain currentness/commencement holds. PDF page 40 says « L’indemnité de voiture ou d’entretien de véhicule et l’indemnité de déplacement ne sont pas cumulables. » The existing July source and cap are retained separately. |
| F3 | `P-CNSS` and its payroll ledger now expressly leave aggregate employer allocation unresolved and certify no total. The Guide continues to show only the supported pension split, separate branch rates and cap. The original Gazette/date and allocation holds remain. |
| F4 | Both `V-DOMCAP` and `V-FORESTCAP`, in rules and ledger, now point to actual article 208 on PDF page 73. The 60,000,000 ordinary threshold, 500,000,000 forestry threshold, two-year continuation and article 208 bis option conditions were read with neighbouring pages. |
| Minor `I-SHARES` | The rule and income ledger now say “up to six children”, matching the existing article 170 exact quote. No share table, rate, example or Guide body was changed for this clarification. |

Exactly six of the 93 rule records changed: `I-SHARES`, `P-CNSS`, `P-CAR`, `V-PRORATA`, `V-DOMCAP`, `V-FORESTCAP`. The other 87 records are structurally identical to the original candidate. The original review's full 93-rule/127-placement coverage remains the baseline; this closure checks the six deltas and both additional source objects rather than falsely representing a second full fresh review.

## Preservation and validation

- All six other Guides are byte-identical to the reviewed commit. The two edited Guides contain only the requested paragraph correction and matching frontmatter/H1 version advance from `0.1` to `0.2`.
- All 16 `oa-check` blocks are byte-identical to the independently recomputed originals. They pass `check-examples.py --require` again: eight files, 16 blocks, zero failures or missing blocks.
- Descriptions are unchanged at 103-110 parsed words. Every H1 and numeric frontmatter version matches. Platform and author/trust fields are unchanged; all inherited CTAs are byte-identical. The three new Guides remain free of platform/author/trust fields and CTAs.
- All currency-hold paragraphs and `Not yet confirmed:` lines are unchanged. The country README is unchanged and retains all seven partial domains.
- The original source manifest, Guide inventory, writer README, old-file records, 77-topic records and old-topic map are byte-identical to the initial candidate. They remain historical receipts; none was silently replaced. The original old-topic preservation result and `Lost content restored: 0` remain valid.
- `validate-guides.py --changed-only --no-index-check` passes again with eight Guides and zero warning groups.
- `check-sync-integrity.py --base 59c23acba2ad66dd2bb29ffc81ffbb9289769ef8 --worktree --mode audit --strict-metadata` passes: eight source Guides, zero errors, warnings or notices.

`CLOSURE.json`, `closure-checks.py` and the three `closure-*-validation.txt` logs record these checks separately from the original review receipts. Fresh targeted PDF extracts are retained alongside the closure.

## Limits that remain open

All previously stated current-law and workflow limits remain: the intervening amendment chain; July first taxable periods/commencement; complete VAT item reconciliation and exact 90% case; CNSS original publication/date and branch allocation; CNAMGS underlying decree/version; current monthly salary tables and annual forms; complete personal-income categories; filing routes, boxes, payment references and accepted receipts; national formation derogations, dossier and fees; treaty/exchange evidence and the remaining seven-domain gaps. This closure does not close issue 458 or convert the pack into current-law or accountant-approved coverage.

Only this review directory was written during closure. No Guide, writer evidence or generated content was edited by the reviewer. No commit, push, public comment, merge or production action was performed. Any later content change outside these accepted bytes needs its own bounded recheck.
