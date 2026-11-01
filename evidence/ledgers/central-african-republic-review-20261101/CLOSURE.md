# Independent review closure: corrected Central African Republic pack

Read and checked on 2026-11-01 by the original independent review agent. This supplement preserves `REVIEW.md`, its original receipts and the historical draft manifest. It closes only the four requested corrections against the exact corrected content identified below.

**Decision: accepted as a partial source-based research draft within the stated baseline/amendment scope. No remaining correction from this review.** This is not accountant attestation, a complete operative 2026 consolidation, complete seven-domain coverage or permission to file, pay or register.

## Exact accepted content

The corrected worktree is a delta from prior candidate commit `2460f6898fd1eb9bc7ddbf211377c617cc7ce7e9`; no new commit ID exists at closure. `closure-invariants.json` binds all nine accepted Guide files, writer repair files and supporting records by SHA-256. The three changed Guides are:

| Guide | Version | Accepted SHA-256 |
|---|---|---|
| `cf-transfer-pricing.md` | 0.2 | `aaa980fe2738f846f247ec4f70f5418617ccd173cd3830a0790e78c425ecd504` |
| `cf-payroll-social.md` | 0.2 | `1ac588e65081ec4dfc3c5c3e7e2a4236d5b1f2c5b7ef614edd6b75a5e710fdf5` |
| `cf-tax-overview.md` | 0.2 | `2c16ae0fcf56d3c2299d6c4134b9cff9708f35c8855427c7ec08b2c122428972` |

The other six Guides are byte-identical to the originally reviewed candidate and retain their original accepted-scope hashes in `invariants.json`; closure recomputed and recorded those hashes again. All eight candidate-file hashes in `writer-corrections.json` match the actual corrected bytes.

## Closure findings

| Original correction | Result |
|---|---|
| R1: intermediary ownership | Closed. T01 now states majority capital held directly or through an intermediary, consistent with CGI art.131(2)(a), PDF p.51. Guide, `rules.json` and writer ledger agree. Actual decision power, common control and privileged/non-cooperative exceptions remain intact. |
| R2: tax retained or due | Closed. W04 now states tax retained or tax due within ten days of cession/cessation, consistent with CGI art.112, PDF p.35. Guide, `rules.json` and writer ledger agree; foreign-paid resident salary obligation is unchanged. |
| R3: source the 2024 LPF creation | Closed. Overview links signed Finance Act art.11 and adds an honest selective Sources row. New O08 records that creation and opening scope, without claiming the complete LPF was read. The reviewer independently rendered and visually read PDF p.35, printed p.34, and read neighbours p.34/p.36. The scan confirms “Il est crée un Livre des Procédures Fiscales annéxé au Code Général des Impôts”. The original signed PDF hash remains `738aafbbc084ace0a25989f0b02fb7a7751bc08128090873026bcf0a2f16f223`. |
| R4: historical VAT opener | Closed. Old-topic table item 68 expressly records removal of the unsupported “in force since 2006” assertion for lack of authenticated primary support. The immutable old-topic JSON is unchanged. No unverified historical rule was reinstated. |

The rule set now contains 82 grouped records: original 81 reviewed in full, with T01/W04 repaired, plus independently checked O08. The other 79 original records are unchanged. The old topic inventory remains 68 items. Lost content restored: 0; the unsupported historical commencement claim now has an explicit removal disposition.

## Preserved checks and limits

All nine Guides were compared with the prior candidate. Only the three named Guides changed. All 18 worked-example blocks and their surrounding example prose are byte-identical, remain within the source conditions previously reviewed, and recompute successfully. Parsed descriptions are unchanged at 96-100 words. Three H1/frontmatter versions both advance to 0.2; the others remain 0.1. Platform-owned fields and existing CTAs remain unchanged, and new Guides have no newly added platform metadata or CTA.

Every Not yet confirmed line and source-status hold is unchanged. The country README, all seven `partial` domains, immutable old-topics JSON and historical original draft manifest are unchanged. CNSS rates, complete current consolidation, operative treaty tables, live forms/boxes/portals, implementing orders and special/general penalty priority remain unresolved. Issue 449 stays open.

`closure-validation.json` records independent shape, 18-example, changed-guide, strict-metadata worktree audit and whitespace checks, all exit 0. The only warning is the pre-existing unmapped property-tax slug. The worktree audit is content/metadata audit, not production-exporter compare-and-swap. The earlier GitHub fetch DNS limitation is not treated as resolved by these local checks.

The reviewer wrote only review-directory evidence. No Guide, writer ledger, country README, source cache, historical receipt, generated artifact, Git index or Git history was changed by the reviewer. No push, PR comment, merge or production write was performed. A later commit may be associated with this acceptance only if these exact Guide and repair-file bytes are preserved.
