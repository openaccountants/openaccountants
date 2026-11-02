# Independent bounded closure: Gibraltar legacy repair 1

**Accepted within the two-finding repair scope.** LSR-1 and LSR-2 are closed on exact commit `6e75f698f89321470fa55245b8993d28f2bafb0b`. No new bounded issue was found. The initial review and its verdict remain intact at `721fda0ac7d98ce5e2eedbea23020968e5fb174b`; this closure records the later fixes without rewriting that evidence.

## Findings closed

**LSR-1:** LEG-17 now identifies the principal-purpose paragraph as **Article 28(1), Entitlement to benefits**, consistently in the revised JSON ledger, Markdown ledger, builder and source-read scope. The native context lines 1588–1600 contain that heading and operative paragraph. The only difference across the 29 original ledger rows is this one locator field; all 46 exact quotations and every other row field are unchanged. The original erroneous Article 25 locator remains in the historical evidence rather than being silently overwritten. No tax-rule substance changed.

**LSR-2:** The stamp-duty Guide's new Penalties and interest paragraph now points accurately to its retained section 16 method and existing base-penalty controls. It explicitly preserves the exclusions for interest, further penalties, court fines and other charges and the later-notice/day-count/settlement limits. The internal anchor resolves to the existing Stamping, responsibility and late instruments heading. The Guide no longer denies the penalty amounts it actually computes. Exact reconstruction confirms only three replacements: frontmatter version 0.5→0.6, H1 v0.6 and that one paragraph. All original methods, figures, controls, caveats and CTA remain exact. No new statutory amount or interest-rate assertion was introduced.

The relevant primary text had already been read in the initial review. The two repair excerpts were checked again against their unchanged native source ranges; no source refresh, capture or research beyond this bounded repair was necessary. The 29-row review is preserved without repeating already completed checks. [closure-checks.json](closure-checks.json) records the bindings and [input-hashes.json](input-hashes.json) freezes the current inputs.

## Preservation and validation

Independent checks confirm 86 of 87 original review inputs remain unchanged; the sole change is the stamp Guide, now SHA256 `0dedd5f962df8896a647cc8f5d41cdbf49843aef915ee3741723198a65ca7860`. Every initial independent-review artifact matches its committed bytes. The original 552 content lines, 77 topic mappings, 14 old controls and five added controls remain preserved, as do descriptions, attribution/platform metadata and CTA presence/suffix apart from the disclosed version/H1 change. Lost content restored: 0. Prior minimum-tax and six-Guide mechanical acceptance remains untouched.

The changed stamp Guide independently passes 10/10 mechanical checks. An independent **audit-mode strict-metadata comparison** against the reviewed candidate `b0c501e5` reports one source Guide and zero errors, warnings or notices. This is not a test of private platform CAS ingestion or a live export. Existing writer rerun logs remain bound by hash and report 150/150 tax checks, 19 country files/34 executable blocks with no failures/missing, and changed-PR validation with 0 errors/31 warning groups. Arithmetic was not repeated because all example bytes and their already passing results are unchanged.

The three unchanged general/accounting Guides retain their 15 tax-style shape failures. All seven country partials and the remaining tax-job/method gaps remain open. The broader recorded comparison against newer origin/main `3de6616a827b5f4b3ea9707ede381a6735e5299a` has 57 errors on 20 paths outside Gibraltar. A normal main merge and rerun are still required before any push; this bounded metadata pass does not waive that failure or establish remote green checks.

## Strict scope of acceptance

A narrow dated README link/status pointer may record this exact bounded closure and its limits. It must not clear partial entries, assert country completion, green remote checks, professional attestation, publication reuse clearance or untested export/CAS. No new Guide/tax copy is covered by that allowance.

Source publication-reuse clearance remains pending the parent's separate check. No licence, commercial redistribution or professional-attestation clearance is given here. No Guide/README edit, commit, push, merge, filing, payment, source capture or authority contact was made by the reviewer. The input hashes remained stable through closure.
