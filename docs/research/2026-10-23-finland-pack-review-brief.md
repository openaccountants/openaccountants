# Finland independent full-pack review brief

Status: **historical writer-prepared handoff** for checkpoint `b7b4a75f`. The subsequent independent report and correction closure are recorded in [2026-10-23-finland-pack-review.md](2026-10-23-finland-pack-review.md). The preparation evidence below describes the original checkpoint, not final publication evidence or accountant approval.

Source checkpoint: `b7b4a75f53c5a0aba3cb5ff994ece7cae6f20bf4` on local branch `codex/finland-country-completion` in `/private/tmp/oa-world-support`. Compare the country batch with published shared baseline `915c5118`. Reuse consolidated draft PR #514 after review; country issue #392 remains open. The primary chat is currently writing Bosnia and Herzegovina. Norway and Iceland remain parked. No Finland content has been pushed.

## Scope and identity checks

Review the entire Finland pack below, including unchanged-looking source passages and cross-file interactions. There are 12 source Guides plus README. All source Guides have `tax_year: 2026`, `tier: 2`; the overview is a router. The seven core tax domains remain partial in README. The named Finnish accountant review is separate from this independent source/arithmetic review.

Use this exact commit, or verify each Git blob before reviewing a working copy. Do not review a later mutable branch and attribute the result to this checkpoint.

| File | Version | Executable controls | Git blob at source checkpoint |
|---|---:|---:|---|
| `README.md` | 0.8 | 0 | `aeb574ad6cab913d3d7ec84143487d49d9679a27` |
| `fi-company-formation.md` | 0.1 | 2 | `c1085275a205c97e401071a31f87894ef23c506d` |
| `fi-corporate-income-tax.md` | 1.1 | 3 | `81e683462c429d75c8d767790e9d85ada92bf740` |
| `fi-country-by-country-reporting.md` | 0.3 | 2 | `5c8f2da6a6aa51b7465a99f764b23543f5422310` |
| `fi-employer-payroll.md` | 0.5 | 6 | `4727ca37f0e1226875ee55b9547e4c9c5fd5b948` |
| `fi-income-tax.md` | 1.2 | 3 | `6e925c7e367e6d62e49be71b73ee553ee86f7738` |
| `fi-individual-cross-border-residence.md` | 0.3 | 3 | `8792b6c359837cf8f4efec0a0d47f90b6a571e6d` |
| `fi-prepayments.md` | 1.1 | 2 | `b13b83dffef33a1d6ada777747296f78ea9d911e` |
| `fi-property-transfer-tax.md` | 0.2 | 3 | `53ae8c25e21f04d0fd96a245c6b1e42d31f5df99` |
| `fi-tax-overview.md` | 0.2 | 0 | `c1f3305489f40d0fdc459a51d4e8965aacd28028` |
| `fi-transfer-pricing.md` | 0.4 | 3 | `782ccd9ab3056ecb5c93974c4c7e1b2c9262919f` |
| `fi-yel-social.md` | 1.2 | 3 | `5c06ddccc04a8a485d6088ce8e2d9a3bedb2be77` |
| `finland-vat-return.md` | 2.3 | 3 | `b0ea89e766deaddf7c3cb74dbbc0e1b2d68a8194` |

## Review method

1. Read GOAL.md, OWNERS.md's country-batch rule, the country README and the existing research. Preserve original author/source provenance. A source-cited draft can be partial; review must assess whether its stated scope and remaining limits are accurate.
2. Independently inspect the cited primary authority text and operative dates. Link reachability is not legal verification. Finlex browser-reader output sometimes omits the statute body; direct official HTML statutory content and local `/private/tmp/oa-finlex-*` snapshots are available, with scope/hashes in the retrieval record. Do not treat the writer's extraction or interpretation as independent proof.
3. Recompute all 33 controls and check that their assumptions and arithmetic correspond to the narrative. The checker validates arithmetic, not whether inputs qualify, the law applies or a threshold flag is correctly classified.
4. Check every Guide for internally conflicting or cross-file rules, inaccurate current-year labels, unsupported figures/forms/deadlines, legal exceptions hidden by absolute wording, invented filing outcomes and professional-review claims. Examine the complete pack rather than only added paragraphs.
5. Return a review record naming the exact checkpoint, files/sources examined, results, severity and concrete correction for each finding. Explicitly distinguish a full-pack source review from any narrower source audit or professional approval. Do not invent credentials or set tier 1. Do not push, merge, file returns, transmit payments or change another country's files.

## High-priority checks

- Individual: mainland versus Åland scope; 2026 state table and capital bands; entrepreneur deduction/loss ordering; startup net worth, gain minimum and election timing; YEL deduction route/no duplication; individual sanctions and interest categories; 2027 filing calendar remains unconfirmed.
- Corporate: current rate and loss period versus proposals; source/ownership/permit limits; listed-company condition; book-to-tax assumptions; separate accounting-period returns and deadlines; nonresident payment identification/treaty/PE limits; displayed 2027 amendments must not be used as 2026 rules.
- Payroll/social: current tax-card and income-ceiling logic, cash cap, coverage/age/base differences, reporting versus payment, TyEL/unemployment contributions and exceptions; verify what remains unquantified.
- YEL: review-cap history/consent and pre-2029 transition, disability exception to ordinary prospective changes, indexed versus base-year amounts, compulsory insurance/neglect fee, annual decree/provider/benefit limits, spouse/payment deduction routes.
- VAT: current and preceding-year registration test, crossing sale, rate transition, transaction classifications, input/vehicle/entertainment limits, domestic/EU/non-EU/import return entries, correction alternatives and original/replacement penalties. Existing operational paragraphs require review too.
- TP/CbCR: SME/group and simplification boundaries, actual transaction/control test, gross versus net method bases and reliability preference, request deadlines, scoped penalties, notification versus report deadline, secondary/surrogate/refusal conditions, current exchange/schema evidence.
- Property: debt-free base, signing/ownership triggers, nonresident distinction and contingent-consideration contract transition. Calendar and supplemental filing specifics remain open.
- Formation: PRH route/fee eligibility and electronic filing; ordinary/deputy EEA tests; registration and share-payment conditions; the precise positive audit-omission test in each of two periods; adoption-to-filing clock versus the PRH outer timetable. Other entities/special sectors remain open.

## Evidence already available; independently assess its scope

- All 33 arithmetic controls pass across eleven computation/preparation Guides.
- The repository suite passes 129 tests with `TMPDIR=/private/tmp`.
- Contributor validation passes with the inherited Gibraltar 2024 freshness warning; generated trees were not changed.
- Source reachability contains 98 current non-CTA URLs with HTTP 200 evidence and timestamps; earlier results are retained rather than represented as newly fetched.
- Direct statutory retrieval records ten statutes with selected provisions, structural section IDs and source hashes; a separate official PDF supports the 2026 transfer-tax transition. Retrieval of an entire page does not prove every provision was read.

Country research entry points: `2026-10-23-finland-core-reconciliation.md`, `2026-10-23-finland-statutory-reconciliation.md`, `2026-10-23-finland-formation-sources.md`, the original topic-source notes, `2026-10-23-finland-direct-statute-retrieval.json` and `2026-10-23-finland-source-reachability.json` in docs/research.

## Publication gate

The writer fixes review findings, advances substantive versions, obtains closure for changed material, fetches/reconciles only the published shared branch and runs the required checks before one country content push to the active consolidated PR. Preserve other writers' work and all unchecked maintainer/CLA decisions. Exact-head CI after publication and a named Finnish accountant review remain separate gates. This brief proves neither review completion nor country completeness.
