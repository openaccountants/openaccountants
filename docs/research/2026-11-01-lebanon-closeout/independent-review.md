# Independent Lebanon pack review, 1 November 2026

**Repairs required at frozen head `17b9399bd2fb6144e46ce804d6ecc3b48308c0ea`.** Every one of the 52 operative ledger rows was compared with its actual cached primary-source text or page image and with the six Guide bodies. The source-baseline figures match; four rows need a Guide condition, wording or preservation repair. This report does not approve a different head.

- PR: https://github.com/openaccountants/openaccountants/pull/1199
- Actual full merge-base: `46c01152da0fdd1b722f61190c88413d0a195d02`.
- Original PR head: `581bde2b4b59ae820f17c46e13b570c2e73edb05`.
- Reviewer: independent Codex second reader, separate from the writer. No Guide edits, commits, pushes, merging or accountant attestation performed.
- Six Guides; 52 source-baseline rows: 48 pass within stated scope, 4 require repair. Full per-row findings and frozen Guide/source hashes: [row-verdicts.json](row-verdicts.json).
- Twelve worked examples independently recomputed and read for the legal assumptions. All arithmetic passes. Hypothetical inputs are distinguished from legal figures.
- 692 predecessor nonblank body lines inventoried: 88 income, 109 corporate, 295 VAT, 81 payroll, 61 formation and 58 overview, counting both baselines. Exact line text, old hashes and coverage independently match Git. Semantic destination spot checks found repairs below.

## Required repairs

| ID | Finding and necessary change | Primary source actually read |
|---|---|---|
| PIT-15 | The business deduction amounts match, but the Guide only says child/spouse conditions are on pp. 48-49. Put the conditions beside the rule, or explicitly hold applying that deduction. Preserve the dependent-child distinctions: male child up to 18, or up to 25 for university study; disabled male child without paid work subject to the specified Ministry certificate; female child before marriage or widowed/divorced; at most five children. Preserve both working spouses' single deductions and equal child allocation, the legally separated spouse paying maintenance, and the special non-working father/working mother allocation. A generic qualifying label does not communicate these switches. | Budget 324/2024 art. 49, pp. 48-49, rendered official PDF. |
| CIT-06 | The Guide collapses art. 11's employee limbs into more than four permanent employees. Industrial establishments (excluding craft establishments), publishers/printers and specified mills have the permanent-worker wording; the retail-trader limb 6 says more than four persons without that permanence condition. State the relevant classes separately or limit the permanent-worker sentence expressly to the industrial limb. | Income Tax Law art. 11, official PDF p. 9, including neighbouring classes and arts. 12-14. |
| VAT-06 | Restore the source-backed rule that excess deductible input is carried to the following period. It is in the operative ledger but absent from the Guide body. The old carryforward lines are assigned a generic VAT-H1..H7 destination even though no named hold specifically preserves this rule. Give it an actual Guide home and map both old lines there. | Budget 40/2026 art. 31, p. 41 first sentence; p. 42 refund-decision, extension and interest conditions also read. |
| VAT-09 | Change the Guide's public-entity penalty settlement wording. Article 43 concerns specified fines payable **to** state, municipalities and other public entities, not a taxpayer class limited to public entities. Suggested wording: specified fines payable to public bodies under art. 43 remain held pending publication, suspension and extension checks. | Budget 40/2026 art. 43, p. 66, title and complete operative paragraph. |

No published band boundary, rate, capital baseline or ordinary NSSF memo 831 amount needs a numeric correction on the read sources. That is not a statement that every 2026 tax parameter or later amendment is confirmed.

## Predecessor preservation

The inventory is mechanically complete, but individual mapping is not proof of a correct destination. Spot checks included every Guide, both baselines, substantive old rates/thresholds, household relief, exemptions, corporate special regimes, import advances, filing dates/forms, payroll branches, salary remittance, supplier classifications, blocked inputs, carryforward/refunds, company audit/lawyer requirements and old numerical examples.

Required destination corrections, in addition to carryforward:

- `lb-income-tax`, merge-base line 37: annual employer payroll declaration/form claim is currently mapped to PIT-01/PIT-H4 non-resident collection. Point it to PIT-19 and PIT-H2. The original-PR equivalent line 41 is correctly routed.
- `lb-corporate-income-tax`, original-PR line 61: the line contains both holding/offshore relief and art. 40 revaluation. Add CIT-H6 alongside CIT-H4. The current Guide has CIT-H6, but the item-level map does not identify it.
- `lb-company-formation`, original-PR line 24: the holding/offshore vehicle row is currently assigned FORM-02/FORM-03 (SAL capital/lawyer). Point the entity distinction to FORM-05 and special-tax conditions to CIT-H4/FORM-H4 as appropriate.
- `lb-payroll-social`, both baselines' payroll-tax remittance rows (base line 24, original line 37): point salary withholding/remittance to the linked Personal income tax Guide, PIT-18/PIT-H2. PAY-04 is the NSSF statutory suspension, not the source of the employer income-tax remittance rule.

Old numerical examples can be superseded by the new domain-owned examples. Obsolete source references and boilerplate need not become operative law. The existing holds correctly retain unresolved supplier labels, salary allowances/pensions, foreign withholding, special regimes, filing implementation and other NSSF branches. The carryforward omission is the identified source-backed substantive rule requiring restoration.

**Lost content restored: 0 at this frozen head; 1 rule still requires restoration (VAT carryforward).** This reviewer did not edit the Guides. A later repair receipt must record the actual restored count and bind its follow-up review to the new frozen head.

## What was read, and what was not

Read `docs/skill-template.md`, all six Guides, country README, writer evidence/ledgers, and machine-readable claim/source/predecessor records. Verified every source manifest SHA-256 and each ledger's current Guide SHA-256 against local bytes. The 14 source identifiers reference 12 distinct cached documents/tool-text files. IDAL and Ministry HTML captures were read as authority-page tool text, not misrepresented as origin HTML.

Independent source reading for the operative rows:

- 2024 official budget images pp. 45-49: complete business and employment bands, 17% capital-company rate and household business deduction conditions.
- 2025 official budget PDF p. 28 / Gazette p. 26: complete art. 17 replacing Income Tax Law art. 63, including neighbouring foreign-currency and end-of-service qualifications.
- 2026 official budget: cover; pp. 26-30 (arts. 16-18), 38-43 (arts. 27-33 and neighbours), 45 (art. 35), 65-66 (arts. 40-43), 79 (art. 51), and closing p. 82. Pages 28-30 and 42 were independently rendered from the cached authenticated PDF for this review. Only relevant clauses were accepted; unrelated refund industries and other adjacent categories were read as context, not added to operative claims.
- Income Tax Law older consolidation: arts. 1-3 and neighbouring scope, arts. 6-14 and surrounding expense/real-profit classes, arts. 46-50 and salary neighbours, arts. 57-59. Later figures came from the budget replacements, not the stale numeric consolidation.
- Whole one-page corporate/dividend notices 4859 and 4676 in images.
- IDAL SAL/SARL tax and complete entity-choice sections, holding/offshore distinctions and E-services paragraphs; Ministry salary index form labels; VAT declaration periods, deduction/apportionment paragraphs and obsolete postal/deadline context.
- Whole memo 831, both memo 843/attached Law 46 pages, and all three memo 846 pages, including category distinctions, discretionary-limit exception, relief/default exclusions and new penalty table. Official memo-index provenance is present in the cached authority capture.

This is **not** an exhaustive currentness search across all non-budget legal instruments, the full 2025 amendment chapter, the 927-page 2026 budget, or its fiscal/fee annexes. The writer's wider screening receipt is not substituted for my own reading. No CAPTCHA, authentication or TLS block was bypassed. No new external-source search was necessary: the failed checks are resolved by neighbouring conditions in the already-cited primary sources.

The partial scope is candid and acceptable in principle. Salary gross-to-net and pensions, current VAT rate/registration, full contribution rates, special regimes, filing boxes/dates/extensions/suspensions, relief entitlement and company-law currentness remain non-operative holds. This review does not close them. The undated IDAL pages remain guidance baselines rather than proof of the entire 2026 statute chain. No accountant sign-off is claimed.

## Integrity and mechanical validation

Independently rerun at the frozen head:

- `validate-guides.py --changed-only --no-index-check`: six Guides pass, zero warning groups.
- `skill_checks.py` on the six actual Guide paths: all 15 checks per Guide pass, 90 passes.
- `check-examples.py --changed-only --require`: 12 blocks, zero failures, zero missing; its broader file count includes research Markdown.
- `check-sync-integrity.py --base 46c01152da0fdd1b722f61190c88413d0a195d02 --head HEAD --strict-metadata`: six Guides, zero errors/warnings/notices.
- `git diff --check 46c01152da0fdd1b722f61190c88413d0a195d02...HEAD`: no output.
- Full stamped CTA suffixes compared byte for byte with original PR head: all six unchanged. Protected platform/contributor metadata passes strict comparison with the actual merge-base. No existing author/history/licence replaced.
- Frozen commit author/committer: Michael Cutajar with the linked GitHub noreply address; no attribution trailer.

These passes do not override the four source/content repairs or the explicit open holds. Recheck repaired rows, semantic destinations, Guide hashes and validation on the actual new head before treating this review as closed.
