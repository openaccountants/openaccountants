# Burkina Faso IRCM independent source review

Reviewed frozen commit `cad488c270c42ad731ff3b975d6afe2e6c4208d5` on 2026-11-01. This is a fresh independent review of the new investment-income job and the two migrated corporate rate rows. It is conditional source-fidelity review of the identified cached official texts, not a later-law search, whole-country completion claim or accountant attestation. The writer's records and pending statuses were not substituted or edited.

## Result

**One repair required before acceptance: F01, article 610(2) coupon-owner reporting.** The other 59 ledger rows have conditional source fidelity. All 60 rows were read against their complete CGI provisions and neighbouring conditions; the exact source clauses and individual findings are preserved in `every-row-review.json`, with one reviewer note per row in `row-notes.json`.

F01 concerns `skills/burkina-faso/bf-investment-income.md`, filing step 7 (line 72 in this frozen version), and writer ledger C49. The draft says to annex the true-owner list where coupons are presented for third parties, and C49 says third-party owners are identified and their list annexed. CGI article 610(2), physical/printed pages 260-261, instead provides a presumption and a faculty:

> Les coupons présentés sont, sauf preuve contraire, réputés propriété du requérant.

> Dans le cas où celui-ci présente des coupons pour le compte de tiers, il a la faculté de remettre à l’établissement payeur une liste

The list gives the presenter's names and real domicile, the true owners' names and real domiciles, and the coupons belonging to each. The next sentence imposes annexation of **that supplied list**:

> L’établissement payeur annexe cette liste au relevé en exécution du deuxième alinéa du paragraphe 1 du présent article.

Required repair: retain article 610(1)'s identity and net-payment reporting obligations; state the article 610(2) ownership presumption, the presenter's ability to supply the third-party owner list and the paying institution's duty to annex it if supplied. Amend C49's rule and decisive quotes in an append-only writer correction record or revised ledger with preserved original evidence. Do not describe provision of the list as unconditional. A precise replacement for the affected clause is: "Coupons are presumed to belong to the presenter unless there is contrary proof. A presenter acting for third parties can supply a list giving the presenter and true owners' names and real domiciles and each owner's coupon amount. If supplied, the paying institution annexes that list to its payment statement."

This is a source-fidelity defect in the legal condition, not an arithmetic or rate defect. F01 remains open in this record; the writer must fix it and request a separate closure against the resulting hashes. No other Guide or README wording was changed by the reviewer.

## Classification, timing and examples

The article 132(6) company/public-body borrowing category is preserved, including borrowings without securities or negotiable obligations. The 25% example correctly uses a private individual debtor. Qualifying bank deposits at 12.5%, non-exempt Burkina-issued obligations at 6%, other securities at 12.5% and exempt State instruments remain distinct. Article 141's 6.25% branch concerns equity products and is bounded by both the first three social periods and 42 months; the separate 3% community-company branch is conditional on unverified status evidence.

The calendars were checked separately: bank quarterly bordereau by the following 20th, article 147 before 30 April, article 148 no later than 30 April, article 152 meeting documents within one month, article 153 dividend remittance within thirty days of mise en paiement, article 155's board-quarter and capital-repayment-month branches, and articles 610-611 information duties. Unresolved general-administrator/non-dividend borrowing calendars remain held rather than inferred from the dividend rule. Article 134(6)'s printed subsequent loss-motivated reduction wording is faithfully preserved; interpretation remains held.

All four examples in the two changed Guides were recomputed independently using exact integer/Decimal calculations and by the committed example checker. Results and legal gates are in `case-review.json`; no failures. The advance example correctly applies the attributable fraction and strict less-than-five-years rule, without calling a computed entitlement an executed refund.

## Preservation and complete old-topic destinations

The immutable predecessor is `5bd11581ceea39807036d3aa4875fb4348c8b31f`. Every one of the 142 baseline blobs was independently compared with that commit and the frozen target. The ten other Guide files and all 130 earlier evidence files are exact. The README is an exact append. Reversing only the authorised two-row migration, version and H1 increment recovers every byte of the corporate Guide. The existing arts. 93-94 corporate IRCM-credit paragraph is exact.

The complete 36 non-empty corporate predecessor blocks, their hashes, exact content and destination/disposition are in `complete-old-topic-review.json`. M01's ordinary securities 12.5% and Burkina bond 6% rules land in C13-C14; M02's new-company half rate, three periods, 42 months and separate community-company 3% land in C15-C16. Both destinations were checked against articles 140-141. No other old topic was removed. Lost content restored: 0. Preservation is not a new legal review of the ten unchanged Guides.

## Sources and checks

Source identities, reading scope, finance-law amendment targets and commencement are in `source-reading.json`. CGI PDF SHA256: `a8acc390c74bc605540ad493c09e6f9381b5a20148b8804810a164256f7f8c5c`. Signed finance-law PDF SHA256: `24242939052ac8dc40b6b59e9dd5e89b5e72e5f29aaeed6362cefa97a02f7d6a`. Full relevant CGI clauses, full article 130/134 exemptions, and neighbours were read. CGI pages 73-80 and 260-261 were also visually inspected. The signed finance-law identity/promulgation and amendment clauses 14-36 were read, with visual checks of pages 2, 6 and 16-19. Those clauses amend no selected IRCM provision; the actual commencement wording is 1 January 2026. The writer's limited-overlay scope is accurately described and does not claim a complete amendment chain. Fresh web fetches of both official URLs timed out, so no new live-access/currentness assertion is made.

`validation.json` records all commands, exit codes and output at the frozen commit, using actual merge base `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`. Both changed Guides passed all 15 shape checks. The committed changed-Guide validator passed with two disclosed warnings: the property and investment-income slugs have no recognised tax domain, so the country-cell check did not run for those names. Strict metadata integrity passed with zero warnings/notices; whole-merge-base whitespace check passed; four example blocks passed; source identities/anchors and preservation checks passed. Mechanical passes do not close F01.

The new Guide's hashes, corporate/README hashes and every writer-evidence target hash are frozen in `frozen-targets.json`. The new Guide SHA256 is `530f1a6eb5c3a3ef37536edf262f026f2d0b9998019686bd1f30f2baa26ecaab`; corporate Guide SHA256 is `55a386eae02d92195cce7d04e3fd2dce82f18edbdb6f1c41a396da1dd3a8e7eb`.

All seven country domains remain partial. Forms, live filing, residence, treaty entitlement, specialist exemptions, PE distributions and the other stated gaps remain open. No commit, push, GitHub mutation, Guide edit, README edit or writer-record edit was performed by the reviewer.
