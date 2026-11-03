# Bounded independent Faroese repair review

Candidate: `99ddd1c3c1e7075528aa014977e9931dec90f831`. Verdict: **do not accept yet**. Four original findings are fixed, but the version repair leaves both body headings inconsistent with their frontmatter. This report preserves the initial review and does not reopen the supported64 claims.

## Pins

Current81-input writer manifest SHA256: `4051b7cb6a083afe736ec383743f5a63a566713e844bd7c3eac1f6778200f023`. Every input hash matches. Inheritance Guide SHA256: `016885210094b6a657f989951b253eca653407b01794f27f550439f05ee006c0`. Estate Guide SHA256: `71bf0d38603d94ce671380538c13f7e98986cb0353d24c3cf8c3aacdcf7e87bb`.

## Dispositions checked

- FO-EST-001: closed. All four repaired court/D03/closing reference definitions exactly match the clean publisher URLs independently opened in the initial review; corresponding Sources cells match, with no whitespace/concatenation. The operational text and form details are unchanged.
- FO-EST-002: closed. NewET-029 matches the current Guide and the full original Tax Act§103(1),(3) paragraphs in the retained reader, originally independently fetched. The duty explicitly covers estates and requires income statement plus opening/closing balances. Omission invalidates the return with assessment/appeal consequences; authority-set deadline and discretionary100DKK/day from expiry until receipt are retained. It is correctly distinct from §14's unspecified opening-statement fine and §104 late-return sanctions. The source read/provenance is explicit; no new rate or automatic blanket penalty was inferred.
- FO-EST-003: closed. Only the two newly added trust_label keys were removed. Nine predecessor Guides/attribution remain unchanged.
- FO-EST-004: category defect closed. Both categories now international, preserving distinct names/job. Versions advanced to0.2 in frontmatter, but the associated body-heading correction is incomplete as below.

## Residual finding

**FO-EST-005, P2:** inheritance line25 and estate line26 still read `v 0.1` while frontmatter says0.2. `docs/skill-template.md` requires agreement; repair disposition incorrectly says headings were advanced. Change only those two H1s to `v 0.2`, refresh current hashes/manifest and corresponding evidence, then request final closure. No new legal research or re-review of the accepted64 claims is needed for that narrow change.

## Preservation and controls

Initial16 independent-review files remain unchanged against805268ba7. Every retained source/review and initial-snapshot hash in repair preservation matches. The two original row files remain byte-exact againstaa3de1064; every one of their64 complete claims still appears in the current Guide after whitespace normalization. The separate65th row isET-029. Neither original review nor writer input was changed by this reviewer.

Reran20 shape checks and4 examples for the two repaired Guides, all pass. Inspected pinned full-pack110shape/22examples, changed-only11Guide validator with5distinct-job/domain warnings and strict-sync11zero-error evidence. Prior152unit tests remain prior evidence and were not rerun. The mechanical shape checker misses the spaced `v 0.1` H1 mismatch; the manual standard check found it.

All seven partials and additional tax jobs remain open; no country-complete claim, professional attestation or publication-rights clearance is supplied. No Guide/README/old evidence edits, contacts, submissions, commits or pushes. A dated pending-review README pointer is not approved until the two-H1 residual is closed. Detailed machine checks are in verification.json and residual-findings.json.
