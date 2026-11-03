# Liberia independent source review, initial freeze

Reviewed candidate: `ae03c48733c558b6c8df9945a9810c5ebbe30bf8`.
Baseline: `aa8fb52e20d1f4083020d7724dabe8c9e5ccfce8`.
Read date: 2026-11-01. Reviewer: fresh independent Codex agent `/root/liberia_independent_review`, with no role in drafting these Guides.

**Result: three focused corrections requested before acceptance as a source-cited partial draft.** The review does not approve operative 2026 advice, resolve VAT commencement, establish full currentness or confer accountant attestation. All seven core domains remain partial. No Guide or writer evidence was edited during this review.

## Findings

| ID | Location | Problem and exact source | Required correction |
|---|---|---|---|
| F1 | `skills/liberia/lr-payroll-social.md` lines 50,52; S05 ledger/rules; README payroll-calendar finding | Regulation18(A)(1) says the employer shall **record** employee earnings/contributions on an approved e-Payroll form no later than the end of the following month. The Guide labels this as e-Payroll being due and a reporting calendar, which can be read as an established transmission deadline. Regulation17 separately requires payment with the Payroll Submission Form. The actual transmission workflow is already acknowledged as unverified. | Say explicitly that the following-month date governs recording employee detail; preserve the contribution payment and accompanying-form duties; leave any separate transmission deadline unconfirmed. Update corresponding ledger/rules and README summary. |
| F2 | `skills/liberia/lr-corporate-income-tax.md` The base; old-topic map Resident company tax base and related narrative | The old Guide explicitly stated worldwide taxation of residents. Its map points to corporate scope/base/filing, but the rewritten corporate Guide does not state that base or give an exact route to the owning statement. The rule survives in the personal Guide as I06, which is narrower than a clear corporate-base instruction. Revenue Code201(c) explicitly distinguishes resident worldwide economic benefits from nonresident Liberia-source benefits; 801(d) gives the PE attribution condition. | Restore a short sourced resident/nonresident base statement in Corporate, with the applicable PE qualification and an I06 ledger placement or a dedicated rule; correct the destination map to that exact statement. This is preservation of an old topic, not a request to broaden the pack. |
| F3 | `skills/liberia/lr-corporate-income-tax.md` line39; C05 ledger/rules | The blanket phrase “tax interest” is broader than Code206(d), which disallows interest relating to **any Liberian tax**. It does not state the same categorical disallowance for all foreign-tax interest. | Qualify the phrase as interest on Liberian tax; keep the distinct Liberian/foreign income-tax disallowance. |

Primary sources for F1: <https://www.nasscorp.org.lr/wp-content/uploads/2024/06/GenReg-2023.pdf>, regs17 and18(A).
Primary source for F2/F3: <https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf>, ss201(c),206(d),801(d).

## Scope and affirmative checks

- Read all eight Guides and README. Checked all84 unique rule records and all97 Guide-ledger placements, not only the numerical table cells. `row-checks.json` gives an individual source/condition check for every ID. Each placement exists in its ledger and its ID is present beside the Guide statement.
- Compared all75 old-topic map entries against the exact six baseline blobs: **68 named bullets plus7 substantive introductory/bridging paragraphs**. All old source prose/blob IDs match. F2 is the one direct base statement needing restoration or exact routing. The remaining topics are carried, corrected, routed or expressly withheld in Sources. No old Guide shrank; length ratios are2.68–4.49. Unsupported agent prices, timeline, minimum capital and pension deduction were not silently carried as verified law.
- Metadata: every description102–113 words, all eight H1 versions exactly `v0.1` matching numeric YAML `0.1`, current2026 tax-year fields and required opening notice. Old baseline had no numeric version, so this is an initial explicit version, not a decrement. All six old complete CTA suffixes and platform fields are unchanged. Both new Guides have no copied CTA, author or platform trust attribution. Tier2 is not accountant attestation.
- Independently recomputed all16 examples and checked their legal assumptions against the cited provisions. All arithmetic passes. GST and TP range examples are expressly conditional; assumed prices, fees, profits and rates are labelled assumptions. Formation examples do not claim statutory registration fees. The first overview example expressly excludes simultaneous payment and additional failure-to-file liability, so its three-month filing result is not represented as a total penalty computation.
- Checked all17 cached source hashes against the writer manifest, with all matches. Captured-but-unread sources are not counted as evidence of a verified rule. Reviewer read scopes are limited to the provisions identified in `row-checks.json`, not the entire Code or every NASSCORP benefit provision.
- Inspected the critical scanned pages visually: VAT amendment physical4 (15%,18months/1July2026 subject1066(b)); general2024 amendment physical8 (20%EBITDA and recharacterisation), physical11 (905(l) repeal); April2026 amendment physical7 (defective74(d)),8 (30-day PE),9 (software15%,GST13%,telecom additional5%); TP actual range page (5.1(b)/(c) conflict, median); pension entry-age page. OCR is not sole support for those numerals/paragraph identities.

## Significant source conclusions

The December2024 repeal is **905(l)** under the resident-withholding heading. It does not repeal nonresident806(i), whose election runs for the elected period plus four succeeding periods. The amended203(d) limit genuinely uses interest received plus20%EBITDA excluding interest income, with the resident-bank exception. The Act approved24March2026/printed1April2026 genuinely changes GST to13% with an additional telecom5%, software withholding and PE thresholds.

The VAT conflict is real in the source set reviewed: the published2024 amendment states15% and18months after handbill publication or1July2026, whichever is sooner, subject1066(b); the LRA announcement dated29September2026 describes implementation1January2027. The full coreVATAct,1066(b), and any binding legal deferral remain unreconciled. This review accepts the **hold**, not either operative date. The ordinary assessment-period omission is visible in the actual April2026 amended74(d); no missing seven-year period was silently supplied. Literal TP range/allocation defects and the Act/regulation retrospective employee-deduction conflict remain explicit holds.

Authenticated live official pages in addition to cached reading: LRA Tax Laws and Amendments catalogue (all four amendment links), LRA September2026VAT announcement, LRA Business Tax Kinds, NIC Starting a Business and NASSCORP Act. Direct web rendering of ANACTT1 failed; the official catalogue link and cached PDF/cover/pages were used, not an invented successful page read. No CAPTCHA, authentication barrier or access control was bypassed.

## Checks and limits

All checks passed at the candidate: skill checks,16 recomputations, changed-only Guide validator, public-repository sync-integrity audit with strict metadata, and baseline-to-candidate whitespace. Outputs and `snapshot.json` are in this review directory. This is not a production exporter/CAS check, live filing simulation, full amendment/inflation-chain audit or licence-holder attestation. Do not mark Liberia comprehensive or close issue466 from this review.

Await focused writer repairs and closure review of F1–F3. The initial reviewed Guide hashes are fixed in `snapshot.json`; subsequent edits need their own delta-bound closure evidence.
