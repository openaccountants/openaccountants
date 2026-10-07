---
name: us-1120-corporation-return-schedule-ordinary-business
description: Explains how an S corporation reports a Schedule K-1 ordinary business loss (box 1) and how the individual shareholder applies the basis, at-risk and passive activity limits before deducting it, for tax preparers and S corporation shareholders in the United States.
jurisdiction: US
tax_year: 2026
last_updated: 2026-10-03
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# S corporation ordinary business loss on Schedule K-1 (Form 1120-S)

This Guide is for an S corporation shareholder who receives a Schedule K-1 (Form 1120-S) with a loss in box 1, and for the preparer of that shareholder's federal return. It sets out the four loss limits in the order the IRS applies them: stock and debt basis, then at-risk, then passive activity, then the excess business loss limit. It ends with a full worked example and the carryforwards each limit leaves behind. Figures are for tax year 2026. Federal rules only; state treatment is not covered.

The IRS editions read for this Guide on 3 October 2026 were: Instructions for Form 7203 (revised 12/2022), Shareholder's Instructions for Schedule K-1 (Form 1120-S) (2025), Instructions for Form 6198 (11/2025), Instructions for Form 8582 (2025) and Instructions for Form 461 (2025). Check irs.gov for a 2026 edition before filing.

Out of scope here: how much salary the owner must take (reasonable compensation) is covered in `us-s-corp-election-decision`. The qualified business income deduction is covered in `us-qbi-deduction`. Partnership K-1 losses are covered in `us-form-1065-partnership`.

## The four limits and their order

The IRS page on S corporation basis lists "four shareholder loss limitations: Stock and debt basis limitations At risk limitations Passive activity loss limitations Excess business loss limitation" and says "Each limitation is addressed in the order shown above and must be met before a shareholder is allowed to claim a pass-through loss." ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

The Form 7203 instructions give the same order with the form for each step: "the basis limitations (Form 7203), the at-risk limitations (Form 6198), the passive activity loss limitations (Form 8582), and the excess business loss limitations (Form 461)." ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

A loss that fails one limit does not move on to the next limit that year. It is carried forward under the rule of the limit that stopped it. The K-1 shows the corporation's figures "without reference to limitations on losses"; the shareholder adjusts them before reporting. ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk))

## Who must attach Form 7203

The Form 7203 instructions say: "Form 7203 is filed by S corporation shareholders who: Are claiming a deduction for their share of an aggregate loss from an S corporation (including an aggregate loss not allowed last year because of basis limitations), Received a non-dividend distribution from an S corporation, Disposed of stock in an S corporation (whether or not gain is recognized), or Received a loan repayment from an S corporation." ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

These four triggers are OR: any one of them requires the form. A shareholder who claims no loss this year but deducts a loss suspended last year still files. On a joint return where both spouses hold stock, "complete a separate Form 7203 for each spouse." The instructions also say it "may be beneficial" to complete and keep the form in years it is not required, so basis stays consistent. ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

The corporation does not track basis for the shareholder: "It is not the corporation's responsibility to track a shareholder's stock and debt basis but rather it is the shareholder's responsibility." ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

## Limit 1: stock basis

### Starting point

Stock basis starts with the shareholder's initial capital contribution or the cost of the stock bought. Stock received in a section 351 transfer generally takes the carryover basis of the assets transferred, less liabilities the corporation assumed. Inherited stock generally takes fair market value at the date of death or the alternate valuation date. Stock received as a gift generally takes the donor's basis, with special rules when value is below that basis. Loans to the corporation are NOT stock basis; they go to debt basis. ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203), [IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

### Increases and decreases

Under section 1367(a)(1) of the Internal Revenue Code (LII mirror of the U.S. Code), stock basis increases by the shareholder's share of income items (separately stated and nonseparately computed, including tax-exempt income) and by excess depletion. Under section 1367(a)(2), it decreases, "but not below zero", by non-dividend distributions, items of loss and deduction, nondeductible expenses not chargeable to capital, and certain oil and gas depletion. ([26 U.S.C. 1367, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/1367))

An amount that must be included in gross income increases basis only to the extent it is actually included in gross income on the shareholder's return (section 1367(b)(1)). Tax-exempt income is not subject to that rule; it is an item of income under section 1366(a)(1)(A) and increases basis. ([26 U.S.C. 1367, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/1367), [26 U.S.C. 1366, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/1366)) Only non-dividend distributions (K-1 box 16, code D) reduce stock basis; dividends reported on Form 1099-DIV do not. ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

### The order of adjustments

Treasury Regulation 1.1367-1(f) sets the order for corporate tax years beginning on or after August 18, 1998:

1. Increase for income items and excess depletion.
2. Decrease for non-dividend distributions.
3. Decrease for noncapital, nondeductible expenses and oil and gas depletion.
4. Decrease for items of loss and deduction.

([26 CFR 1.1367-1 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-1))

Because distributions come before losses, a distribution can use up basis that would otherwise have let a loss through. Section 1366(d)(1)(A) builds this into the loss limit: stock basis for the loss limit is "determined with regard to paragraphs (1) and (2)(A) of section 1367(a)", that is, after income and after distributions. ([26 U.S.C. 1366, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/1366))

Basis is adjusted as of the last day of the corporation's tax year. If the shareholder disposes of stock during the year, the adjustments for that stock take effect immediately before the disposition. ([26 CFR 1.1367-1 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-1))

### The elective order

Under Reg. 1.1367-1(g) a shareholder may elect to take losses and deductions (step 4) BEFORE nondeductible expenses (step 3). If elected, nondeductible expenses that exceed stock and debt basis carry to the next year. ([26 CFR 1.1367-1 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-1)) The election is made by a statement attached to a timely filed original or amended return. "Once made, the election applies to the year for which it is made and all future tax years for that S corporation, unless the IRS agrees to revoke your election." ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk)) Form 7203 has a check box (item E) for it. ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

Without the election, nondeductible expenses that exceed basis "are not suspended and carried forward." ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

### Distributions in excess of stock basis

A non-dividend distribution is tax-free up to stock basis. Debt basis does not count for distributions. "A non-dividend distribution in excess of stock basis is taxed as a capital gain on the shareholder's personal return. It is a long-term capital gain (LTCG) if the S corporation stock has been held for longer than one year." ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis)) Report the excess on Form 8949 and Schedule D, and do not increase stock basis for the gain reported. ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

## Limit 1 continued: debt basis

### Only direct loans count

Debt basis is the shareholder's adjusted basis in bona fide indebtedness "of the S corporation that runs directly to the shareholder." Whether a loan is bona fide is a facts and circumstances question under general federal tax principles. A loan made through an entity disregarded as separate from the shareholder can count. A back-to-back loan through another corporation can count only if it is bona fide indebtedness running to the shareholder. ([26 CFR 1.1366-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1366-2))

A guarantee gives no debt basis: "A shareholder does not obtain basis of indebtedness in the S corporation merely by guaranteeing a loan or acting as a surety, accommodation party, or in any similar capacity relating to a loan." Basis arises only when, and to the extent that, the shareholder actually makes a payment on the guaranteed debt. ([26 CFR 1.1366-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1366-2)) The Form 7203 instructions say the same, and add that "Distributions don't reduce loan basis". ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

### Reduction of debt basis

When losses, deductions and nondeductible expenses for the year exceed stock basis, the excess reduces (but not below zero) the basis of loans the shareholder holds at the close of the corporation's year. A loan repaid, disposed of or forgiven during the year is not held at year end and is not reduced. With several loans, the reduction is spread in proportion to each loan's basis. ([26 CFR 1.1367-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-2))

### Restoration of debt basis

Under section 1367(b)(2)(B), a later year's "net increase" first restores reduced debt basis "before any of it may be used to increase the shareholder's basis in the stock". ([26 U.S.C. 1367, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/1367)) Net increase means the shareholder's income items exceed ALL the section 1367(a)(2) decrease items for the year, distributions included. Restoration applies only to debt held at the start of that year, and never above the debt's adjusted basis at the start of that year with the earlier S corporation reductions left out (in practice, not above the loan's basis before those reductions). With several loans, net increase restores first any loan repaid that year (to the extent needed to offset gain on the repayment), then the others in proportion to their unrestored reductions. ([26 CFR 1.1367-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-2))

### The repayment trap

If the corporation repays a loan whose basis was reduced and not fully restored, the repayment "is a recognition event". ([26 CFR 1.1367-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-2)) Each repayment is split between a return of basis and income. ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk)) In the year of a repayment, restoration takes effect immediately before the first repayment, so that year's net increase can cut the gain. ([26 CFR 1.1367-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-2))

The character of the gain depends on the paperwork. The Form 7203 instructions say: "Debt evidenced by a formal note will result in capital gain, and should be reported on Form 8949 and Schedule D. Any open account debt (including debt referenced in Regulations section 1.1367-2(a)(2)(ii)) will result in ordinary gain and should be reported on Form 4797". Gain on repayment does not increase basis. ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.ecfr.gov/current/title-26/section-1.1367-2 |
| Open account debt ceiling at the close of the corporation's year | USD 25,000 | "the aggregate outstanding principal of which does not exceed $25,000 of indebtedness of the S corporation to the shareholder at the close of the S corporation's taxable year" |

Open account debt means shareholder advances not evidenced by separate written instruments, with all advances and repayments in the year netted at year end. If the net unwritten advances are more than the amount in the table above at the close of a year, then for every LATER year Reg. 1.1367-2(a)(2)(ii) treats that debt like debt under a written instrument for the basis rules, and it is no longer open account debt. ([26 CFR 1.1367-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-2)) For the character of gain, the Form 7203 instructions still group that debt with open account debt: ordinary gain on Form 4797. ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

## Limit 1 result: the section 1366(d) loss limit and suspended losses

Section 1366(d)(1): the aggregate losses and deductions a shareholder takes into account for the year "shall not exceed the sum of" (A) adjusted stock basis, after income and distributions, AND (B) adjusted basis of any indebtedness of the corporation to the shareholder, before this year's debt basis reduction. ([26 U.S.C. 1366, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/1366))

When several kinds of loss and deduction exceed the limit, the limit is shared among them in proportion to their size. Losses carried in from earlier years are added to this year's losses for that proration. ([26 CFR 1.1366-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1366-2))

Section 1366(d)(2): a loss disallowed for lack of basis "shall be treated as incurred by the corporation in the succeeding taxable year with respect to that shareholder". ([26 U.S.C. 1366, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/1366)) It keeps its character and carries forward with no time limit. A suspended loss is not netted with next year's ordinary income in the basis ordering; it is listed on its own line on Schedule E (Form 1040). ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

### Losses on disposal of stock

A suspended basis loss is personal to the shareholder. If the shareholder transfers SOME stock, the suspended loss is not reduced and the buyer gets none of it. If the shareholder transfers ALL of the stock, "any disallowed loss or deduction is permanently disallowed." The exception is a transfer to a spouse or former spouse under section 1041(a) after December 31, 2004: the loss on the transferred stock moves to the transferee. ([26 CFR 1.1366-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1366-2)) So a shareholder with a suspended loss who is about to sell all the stock should look at restoring basis first (for example a real capital contribution) and should not expect the loss to survive the sale. ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

When the S election ends, losses suspended in the last S year are treated as incurred on the last day of the post-termination transition period, limited to stock basis (not debt basis) at that day. ([26 U.S.C. 1366, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/1366))

## Limit 2: at-risk (section 465, Form 6198)

Section 465(a)(1): for an individual, a loss from an activity "shall be allowed only to the extent of the aggregate amount with respect to which the taxpayer is at risk ... for such activity at the close of the taxable year." Amounts at risk include money and the adjusted basis of property contributed, and amounts borrowed for which the taxpayer is personally liable or has pledged property not used in the activity. ([26 U.S.C. 465, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/465))

For an S corporation shareholder, stock or loan basis is NOT at risk if the money used came from nonrecourse borrowing (other than qualified nonrecourse financing), was protected by a guarantee or stop-loss arrangement, or was borrowed from a person with an interest in the activity or a related person, other than a creditor. ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk))

Form 6198 is needed when the shareholder had a loss from an at-risk activity AND had amounts not at risk invested in it. ([Instructions for Form 6198](https://www.irs.gov/instructions/i6198)) At-risk applies activity by activity, so get the corporation's separate statement for each activity. ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk))

A loss not allowed under section 465 "shall be treated as a deduction allocable to such activity in the first succeeding taxable year." If the amount at risk falls below zero at a year end, section 465(e) brings the shortfall back into income, capped at the earlier losses that reduced the amount at risk, less amounts already brought back. ([26 U.S.C. 465, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/465))

## Limit 3: passive activity (section 469, Form 8582)

A trade or business in which the shareholder does not materially participate is a passive activity. Its losses offset only passive income, and the excess carries to the next year under section 469(b). ([26 U.S.C. 469, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/469)) Carried passive losses are freed against passive income, or "when you sell or exchange your entire interest in the activity in a fully taxable transaction to an unrelated party." ([Instructions for Form 8582](https://www.irs.gov/instructions/i8582))

### Material participation: the seven tests in Reg. 1.469-5T(a)

An individual materially participates for the year if ANY ONE of these is met:

1. More than 500 hours in the activity during the year.
2. Participation is substantially all of the participation of all individuals, non-owners included.
3. More than 100 hours AND not less than any other individual, non-owners included.
4. The activity is a significant participation activity AND total participation in all such activities exceeds 500 hours.
5. Material participation in any five of the ten immediately preceding years, consecutive or not.
6. A personal service activity with material participation in any three preceding years, consecutive or not.
7. Regular, continuous and substantial participation on all the facts and circumstances.

([26 CFR 1.469-5T on eCFR](https://www.ecfr.gov/current/title-26/section-1.469-5T))

Test 7 is not available to someone who participates for 100 hours or less in the year. ([26 CFR 1.469-5T on eCFR](https://www.ecfr.gov/current/title-26/section-1.469-5T)) Work done as an investor, such as reviewing financial statements in a non-managerial role, does not count. Work the shareholder or the shareholder's spouse does in the activity generally counts, "where you own your stock at the time the work is done". Material participation is judged on participation during the corporation's tax year. ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk))

A shareholder who materially participates reports box 1 on Schedule E (Form 1040), line 28, column (i) or (k). ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk))

## Limit 4: excess business loss (section 461(l), Form 461)

Section 461(l) applies at the shareholder level. It compares the shareholder's total trade or business deductions with total trade or business income plus a threshold. The excess "shall not be allowed" this year and "shall be treated as a net operating loss" carried to later years. Wages, and anything else from performing services as an employee, are left out of the computation. ([26 U.S.C. 461, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/461)) So the W-2 salary the owner draws from the S corporation does not absorb the loss under this limit.

Two items stay out of the comparison. "Deductions for losses from sales or exchanges of capital assets shall not be taken into account", and gains from sales or exchanges of capital assets count only up to "the lesser of (I) the capital gain net income determined by taking into account only gains and losses attributable to a trade or business, or (II) the capital gain net income". The deductions side is figured "without regard to any deduction allowable under section 172 or 199A". ([26 U.S.C. 461, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/461))

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf |
| Excess business loss threshold, tax years beginning in 2026, all filers except joint | USD 256,000 | "is $256,000 ($512,000 for joint returns)" |
| Excess business loss threshold, tax years beginning in 2026, joint returns | USD 512,000 | "is $256,000 ($512,000 for joint returns)" |

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.irs.gov/instructions/i461 |
| 2025 threshold, all filers except joint (NOT the 2026 figure) | USD 313,000 | "For 2025, the threshold amount is $313,000 ($626,000 for taxpayers filing a joint return)." |
| 2025 threshold, joint returns (NOT the 2026 figure) | USD 626,000 | "For 2025, the threshold amount is $313,000 ($626,000 for taxpayers filing a joint return)." |

The 2026 threshold is LOWER than 2025. Public Law 119-21 (4 July 2025), section 70601, reset the inflation base year to 2024 for taxable years beginning after December 31, 2025, and removed the end date "and before January 1, 2029," for taxable years beginning after December 31, 2026. ([Public Law 119-21 on govinfo](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)) The reason is the base year of the inflation adjustment. The statutory amount in the table below is indexed each year; for 2025 the index ran from 2017, and for 2026 Public Law 119-21 restarts it from 2024, so the 2026 figure sits only a little above the statutory amount. Section 461(l)(3)(C) now applies "In the case of any taxable year beginning after December 31, 2025" and indexes the amount "by substituting '2024' for '2016'" in the cost-of-living formula. ([26 U.S.C. 461, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/461))

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.law.cornell.edu/uscode/text/26/461 |
| Statutory excess business loss amount before inflation adjustment, section 461(l)(3)(A)(ii)(II), filers other than joint (joint is 200 percent of it) | USD 250,000 | "(II) $250,000 (200 percent of such amount in the case of a joint return)" |

The Form 461 instructions (2025) say the Act "permanently extended the disallowance of a deduction for excess business losses." ([Instructions for Form 461](https://www.irs.gov/instructions/i461)) The disallowed excess goes to Form 172 as a net operating loss carryover. ([Instructions for Form 461](https://www.irs.gov/instructions/i461))

## The method, step by step

1. Collect the K-1 (Form 1120-S) and any attached statements, the prior year's Form 7203, and the loan papers between shareholder and corporation. Basis is the shareholder's job. ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))
2. Decide whether Form 7203 is required using the four triggers above. ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))
3. Stock basis, Form 7203 Part I: start with beginning basis, add income items, subtract non-dividend distributions (excess over basis is capital gain on Form 8949), subtract nondeductible expenses, in the Reg. 1.1367-1(f) order unless the (g) election is in effect. ([26 CFR 1.1367-1 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-1))
4. Debt basis, Form 7203 Part II: list each direct loan at its start-of-year basis, add new formal notes and net open account advances, apply any restoration from a net increase, and work out gain on any repayment. Ignore guarantees unless the shareholder paid. ([26 CFR 1.1367-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1367-2))
5. Basis limit, Form 7203 Part III: add this year's losses to losses suspended in earlier years, compare with stock basis plus debt basis, prorate if more than one type, and carry the excess forward under section 1366(d)(2). ([26 U.S.C. 1366, LII mirror of the U.S. Code](https://www.law.cornell.edu/uscode/text/26/1366))
6. At-risk, Form 6198: if any of the basis came from amounts not at risk, limit the loss that passed step 5 to the amount at risk at year end; carry the rest under section 465(a)(2). ([Instructions for Form 6198](https://www.irs.gov/instructions/i6198))
7. Passive, Form 8582: test material participation under the seven tests. If passive, allow the loss that passed step 6 only against passive income; carry the rest under section 469(b). ([26 CFR 1.469-5T on eCFR](https://www.ecfr.gov/current/title-26/section-1.469-5T), [Instructions for Form 8582](https://www.irs.gov/instructions/i8582))
8. Excess business loss, Form 461: combine every business result of the shareholder, leave out wages, capital losses and any section 172 or 199A deduction, compare the net business loss with the 2026 threshold in the table above, and send any excess to Form 172 as a net operating loss. ([Instructions for Form 461](https://www.irs.gov/instructions/i461), [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf))
9. Report what survives on Schedule E (Form 1040), line 28, with each suspended loss allowed this year on its own line. Keep a carryforward schedule that names the limit behind each carried amount. ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk), [IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

## Worked example (hypothetical)

All amounts in this example are hypothetical US dollars. They are written without a currency code because they are invented inputs and arithmetic, not official figures. The only official figure used is the 2026 excess business loss threshold for a single filer, from the Rev. Proc. 2025-32 table above.

Facts, tax year 2026. Ana is the sole shareholder of a calendar-year S corporation and files as single.
- Stock basis on 1 January 2026: 30,000. Of the cash she paid for the stock, 10,000 came from a nonrecourse loan secured only by the stock.
- On 1 March 2026 she lent the corporation 40,000 of her own money under a signed note.
- She also guaranteed a 100,000 bank loan to the corporation. She has paid nothing on it.
- No losses are suspended from earlier years. No Reg. 1.1367-1(g) election.
- 2026 K-1: box 1 ordinary business loss (90,000); box 4 interest income 1,000; box 16C nondeductible expenses 2,000; box 16D non-dividend distributions 8,000.
- She worked 1,200 hours in the business. The corporation paid her W-2 wages.
- She also runs a separate sole proprietorship with a Schedule C net loss of (240,000).

Step 1, stock basis in the Reg. 1.1367-1(f) order:

| Step | Amount | Running stock basis |
|---|---|---|
| Stock basis 1 January 2026 | | 30,000 |
| Add interest income (box 4) | 1,000 | 31,000 |
| Less non-dividend distributions (box 16D) | (8,000) | 23,000 |
| Less nondeductible expenses (box 16C) | (2,000) | 21,000 |

The distribution of 8,000 is below the 31,000 of basis before distributions, so it is tax-free.

Step 2, debt basis: 40,000, from the direct loan. The guarantee adds nothing because she has paid nothing.

Step 3, section 1366(d) limit: 21,000 + 40,000 = 61,000. The box 1 loss of 90,000 exceeds it. Allowed past basis: 61,000. Suspended under section 1366(d)(2): 90,000 - 61,000 = 29,000. Stock basis falls to 0 (21,000 used). Debt basis falls by 61,000 - 21,000 = 40,000, to 0.

Step 4, at-risk: the 10,000 of stock cost paid with nonrecourse borrowing is not at risk. Assume Form 6198 shows 61,000 - 10,000 = 51,000 at risk at year end. Allowed past at-risk: 51,000. Carried under section 465(a)(2): 61,000 - 51,000 = 10,000.

Step 5, passive: 1,200 hours is more than 500 hours, so test 1 is met and the loss is nonpassive. All 51,000 passes. (If she had worked 80 hours, met no other test and had no passive income, all 51,000 would be suspended under section 469(b), and test 7 would not be available because she worked 100 hours or less.)

Step 6, excess business loss: her W-2 wages are left out. Business deductions over business income: 51,000 + 240,000 = 291,000. Threshold for a single filer for 2026: 256,000. Excess business loss: 291,000 - 256,000 = 35,000, disallowed for 2026 and carried as a net operating loss on Form 172. Business loss deducted in 2026: 291,000 - 35,000 = 256,000.

Check: the 90,000 K-1 loss splits into 29,000 suspended by basis + 10,000 suspended by at-risk + 51,000 that reached the excess business loss step. 29,000 + 10,000 + 51,000 = 90,000.

Carryforwards into 2027:

| Carried amount | Limit that stopped it | What frees it |
|---|---|---|
| 29,000 | Section 1366(d), basis | New stock or debt basis in a later year (Form 7203 Part III); lost if she disposes of all her stock, except a section 1041 transfer |
| 10,000 | Section 465, at-risk | An increase in her amount at risk in the activity (Form 6198) |
| 35,000 | Section 461(l), excess business loss | Used as a net operating loss under section 172 (Form 172) |

Boundary variant: if the 2026 distribution had been 35,000 instead of 8,000, the first 31,000 would be tax-free and the other 4,000 would be capital gain on Form 8949. Her 40,000 debt basis would not cover any of the distribution.

Repayment trap, the next year (hypothetical): if in 2027 the corporation repays 10,000 of the note and 2027 has no net increase to restore debt basis, her basis in the note is still 0. The whole 10,000 is gain. It is capital gain on Form 8949 and Schedule D because the debt is a formal note. She must file Form 7203 for 2027 because she received a loan repayment.

## Ask the client first

- What was your stock basis at the start of the year, and do you have every Form 7203 (or basis worksheet) since you first held the stock? Without a beginning basis no loss can be proven.
- Did you lend money to the corporation yourself, from your own funds, and is it under a signed note or just advances on account? Or did you only guarantee or co-sign a bank loan?
- Did the corporation repay any shareholder loan this year, or pay you any distribution (K-1 box 16, codes D and E)?
- Did any of the money you put in come from borrowing that you are not personally liable for, or from someone with an interest in the business?
- How many hours did you (and your spouse) work in the business this year, and in which earlier years did you materially participate?
- Do you have other business income or losses this year (Schedule C, Schedule F, other K-1s)? Did you sell or give away any stock, or did the S election end?

## When to refuse or refer

- No reliable beginning basis and no records to rebuild it: refer. Claiming a loss without proven basis invites disallowance.
- Back-to-back loans, loans through another entity, or disputed bona fide debt status: refer, since the regulation turns on all the facts and circumstances. ([26 CFR 1.1366-2 on eCFR](https://www.ecfr.gov/current/title-26/section-1.1366-2))
- Payments made under a guarantee, debt restructurings, or shareholder debt forgiven by or to the corporation: refer.
- Inherited stock (income in respect of a decedent rules under section 1367(b)(4)), stock acquired in a section 351 transfer with liabilities over basis, or several blocks of stock with different bases bought or sold during the year: refer.
- A terminated S election and losses in the post-termination transition period: refer.
- A grouping of activities for the passive rules, rental activities inside the corporation (K-1 boxes 2 and 3), or real estate professional claims: outside this Guide.
- Partnership K-1 losses: use `us-form-1065-partnership`. Reasonable compensation: use `us-s-corp-election-decision`. QBI deduction: use `us-qbi-deduction`.
- The corporation's own Form 1120-S return (due date, extensions, Schedule K-1 penalties) and whether the S election on Form 2553 is valid or has ended: outside this Guide, which covers only the shareholder's loss. No live Guide covers the Form 1120-S return itself; refer.
- State conformity, state basis and state net operating losses: outside this Guide, which is federal only.

## Sources

- IRS, S corporation stock and debt basis: https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis
- IRS, Instructions for Form 7203: https://www.irs.gov/instructions/i7203
- IRS, Shareholder's Instructions for Schedule K-1 (Form 1120-S): https://www.irs.gov/instructions/i1120ssk
- IRS, Instructions for Form 6198: https://www.irs.gov/instructions/i6198
- IRS, Instructions for Form 8582: https://www.irs.gov/instructions/i8582
- IRS, Instructions for Form 461: https://www.irs.gov/instructions/i461
- IRS, Rev. Proc. 2025-32: https://www.irs.gov/pub/irs-drop/rp-25-32.pdf
- 26 U.S.C. 1366, LII mirror of the U.S. Code: https://www.law.cornell.edu/uscode/text/26/1366
- 26 U.S.C. 1367, LII mirror of the U.S. Code: https://www.law.cornell.edu/uscode/text/26/1367
- 26 U.S.C. 465, LII mirror of the U.S. Code: https://www.law.cornell.edu/uscode/text/26/465
- 26 U.S.C. 469, LII mirror of the U.S. Code: https://www.law.cornell.edu/uscode/text/26/469
- 26 U.S.C. 461, LII mirror of the U.S. Code: https://www.law.cornell.edu/uscode/text/26/461
- 26 CFR 1.1366-2 on eCFR: https://www.ecfr.gov/current/title-26/section-1.1366-2
- 26 CFR 1.1367-1 on eCFR: https://www.ecfr.gov/current/title-26/section-1.1367-1
- 26 CFR 1.1367-2 on eCFR: https://www.ecfr.gov/current/title-26/section-1.1367-2
- 26 CFR 1.469-5T on eCFR: https://www.ecfr.gov/current/title-26/section-1.469-5T
- Public Law 119-21 on govinfo: https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
