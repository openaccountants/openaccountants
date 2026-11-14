---
name: us-1120-corporation-return-schedule-ordinary-business
description: "How an S corporation shareholder takes a 2026 Schedule K-1 (Form 1120-S) box 1 ordinary business loss on the individual return, applying the four loss limits in the IRS order (stock and debt basis on Form 7203, at-risk on Form 6198, passive activity on Form 8582, excess business loss on Form 461) and tracking what each limit carries forward. Covers the basis ordering rules, the elective order, debt basis from direct loans only (guarantees give none), restoration and the repayment trap, the USD 25,000 open account debt rule, the seven material participation tests, and the 2026 excess business loss threshold of USD 256,000 (USD 512,000 joint). For tax preparers and S corporation shareholders. Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-1120-corporation-return-schedule-ordinary-business"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# S corporation ordinary business loss on Schedule K-1 (Form 1120-S), tax year 2026

> **Source-cited draft.** Built from the IRS S corporation stock and debt basis page, the Instructions for Form 7203, the Shareholder's Instructions for Schedule K-1 (Form 1120-S) (2025), the Instructions for Forms 6198, 8582 and 461, Rev. Proc. 2025-32, Public Law 119-21 section 70601, 26 U.S.C. 461, 465, 469, 1366 and 1367 and Treas. Reg. 1.1366-2, 1.1367-1, 1.1367-2 and 1.469-5T (govinfo), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A box 1 loss from an S corporation reaches the shareholder's return only after four limits, in this order: stock and debt basis (Form 7203), at-risk (Form 6198), passive activity (Form 8582), excess business loss (Form 461). Basis is stock basis after the year's income and distributions, plus the basis of loans the shareholder made directly to the corporation; a guarantee adds nothing until the shareholder pays. For 2026, business losses above business income plus **USD 256,000** (**USD 512,000** joint) are disallowed and carried as a net operating loss. Each limit keeps its own carryforward.

## Scope and who this is for

In scope: an S corporation shareholder who receives a Schedule K-1 (Form 1120-S) for tax year 2026 with a loss in box 1, and the preparer of that shareholder's federal return. The skill sets out the four loss limits in the order the IRS applies them, a full worked example, and the carryforwards each limit leaves behind.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The C corporation return (Form 1120) | `us-form-1120-c-corp` |
| The S corporation's own Form 1120-S return, the election and reasonable compensation | `us-s-corp-election-decision` |
| Partnership K-1 losses | `us-form-1065-partnership` |
| The qualified business income deduction | `us-qbi-deduction` |
| Capital gain on a distribution over basis or a note repayment | `us-capital-gains-and-losses` |
| The individual return itself | `us-form-1040-individual-return` |
| State conformity, state basis and state net operating losses | the state's income tax skill |

## Ask the client first

- What was your stock basis at the start of the year, and do you have every Form 7203 (or basis worksheet) since you first held the stock? Without a beginning basis no loss can be proven.
- Did you lend money to the corporation yourself, from your own funds, and is it under a signed note or just advances on account? Or did you only guarantee or co-sign a bank loan?
- Did the corporation repay any shareholder loan this year, or pay you any distribution (K-1 box 16, codes D and E)?
- Did any of the money you put in come from borrowing that you are not personally liable for, or from someone with an interest in the business?
- How many hours did you (and your spouse) work in the business this year, and in which earlier years did you materially participate?
- Do you have other business income or losses this year (Schedule C, Schedule F, other K-1s)? What is your filing status? Did you sell or give away any stock, or did the S election end?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Excess business loss threshold, tax years beginning in 2026, all filers except joint | USD 256,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Excess business loss threshold, tax years beginning in 2026, joint returns | USD 512,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Statutory excess business loss amount before inflation adjustment (joint is 200 percent of it) | USD 250,000 | [26 U.S.C. 461(l)(3)(A)(ii)(II)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm) |
| 2025 threshold, all filers except joint (not the 2026 figure) | USD 313,000 | [Instructions for Form 461 (2025)](https://www.irs.gov/pub/irs-pdf/i461.pdf) |
| 2025 threshold, joint returns (not the 2026 figure) | USD 626,000 | [Instructions for Form 461 (2025)](https://www.irs.gov/pub/irs-pdf/i461.pdf) |
| Open account debt ceiling at the close of the corporation's year | USD 25,000 | [Treas. Reg. 1.1367-2(a)(2)(ii)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-2.pdf) |
| Material participation, test 1 | more than 500 hours | [Treas. Reg. 1.469-5T(a)(1)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf) |
| Material participation, test 3, and the floor for test 7 | more than 100 hours | [Treas. Reg. 1.469-5T(a)(3) and (b)(2)(iii)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf) |

**Why 2026 is lower than 2025.** Public Law 119-21, section 70601, made the limit permanent (striking "and before January 1, 2029," for taxable years beginning after 31 December 2026) and, for taxable years beginning after 31 December 2025, changed the inflation adjustment in section 461(l)(3)(C) so that "December 31, 2018" becomes "December 31, 2025" and the base year "2017" becomes "2024". The 2025 figure was indexed from 2017; the 2026 figure is indexed only from 2024, so it sits just above the USD 250,000 statutory amount. Source: [Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm). The Form 461 instructions (2025) say the Act "permanently extended the disallowance of a deduction for excess business losses." The disallowed excess goes to Form 172 as a net operating loss carryover.

### The four limits and their order

The IRS page on S corporation basis lists "four shareholder loss limitations: Stock and debt basis limitations At risk limitations Passive activity loss limitations Excess business loss limitation" and says "Each limitation is addressed in the order shown above and must be met before a shareholder is allowed to claim a pass-through loss." ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

The Form 7203 instructions give the same order with the form for each step: "the basis limitations (Form 7203), the at-risk limitations (Form 6198), the passive activity loss limitations (Form 8582), and the excess business loss limitations (Form 461)." ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

A loss that fails one limit does not move on to the next limit that year. It is carried forward under the rule of the limit that stopped it. The K-1 shows the corporation's figures "without reference to limitations on losses"; the shareholder adjusts them before reporting. ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk))

### Who must attach Form 7203

The Form 7203 instructions say: "Form 7203 is filed by S corporation shareholders who: Are claiming a deduction for their share of an aggregate loss from an S corporation (including an aggregate loss not allowed last year because of basis limitations), Received a non-dividend distribution from an S corporation, Disposed of stock in an S corporation (whether or not gain is recognized), or Received a loan repayment from an S corporation." ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

These four triggers are OR: any one of them requires the form. A shareholder who claims no loss this year but deducts a loss suspended last year still files. On a joint return where both spouses hold stock, "complete a separate Form 7203 for each spouse." The instructions also say it "may be beneficial" to complete and keep the form in years it is not required, so basis stays consistent.

The corporation does not track basis for the shareholder: "It is not the corporation's responsibility to track a shareholder's stock and debt basis but rather it is the shareholder's responsibility." ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

### Limit 1: stock basis

**Starting point.** Stock basis starts with the shareholder's initial capital contribution or the cost of the stock bought. Stock received in a section 351 transfer generally takes the carryover basis of the assets transferred, less liabilities the corporation assumed. Inherited stock generally takes fair market value at the date of death or the alternate valuation date. Stock received as a gift generally takes the donor's basis, with special rules when value is below that basis. Loans to the corporation are NOT stock basis; they go to debt basis. ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

**Increases and decreases.** Under section 1367(a)(1), stock basis increases by the shareholder's share of income items (separately stated and nonseparately computed, including tax-exempt income) and by excess depletion. Under section 1367(a)(2), it decreases, "but not below zero", by non-dividend distributions, items of loss and deduction, nondeductible expenses not chargeable to capital, and certain oil and gas depletion. ([26 U.S.C. 1367](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1367.htm))

An amount that must be included in gross income increases basis only to the extent it is actually included in gross income on the shareholder's return (section 1367(b)(1)). Tax-exempt income is not subject to that rule; it is an item of income under section 1366(a)(1)(A) and increases basis. Only non-dividend distributions (K-1 box 16, code D) reduce stock basis; dividends reported on Form 1099-DIV do not. ([26 U.S.C. 1366](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1366.htm))

**The order of adjustments.** Treas. Reg. 1.1367-1(f) sets the order for corporate tax years beginning on or after 18 August 1998 ([Treas. Reg. 1.1367-1](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-1.pdf)):

1. Increase for income items and excess depletion.
2. Decrease for non-dividend distributions.
3. Decrease for noncapital, nondeductible expenses and oil and gas depletion.
4. Decrease for items of loss and deduction.

Because distributions come before losses, a distribution can use up basis that would otherwise have let a loss through. Section 1366(d)(1)(A) builds this into the loss limit: stock basis for the loss limit is "determined with regard to paragraphs (1) and (2)(A) of section 1367(a)", that is, after income and after distributions.

Basis is adjusted as of the last day of the corporation's tax year. If the shareholder disposes of stock during the year, the adjustments for that stock take effect immediately before the disposition.

**The elective order.** Under Reg. 1.1367-1(g) a shareholder may elect to take losses and deductions (step 4) BEFORE nondeductible expenses (step 3). If elected, nondeductible expenses that exceed stock and debt basis carry to the next year. The election is made by a statement attached to a timely filed original or amended return. "Once made, the election applies to the year for which it is made and all future tax years for that S corporation, unless the IRS agrees to revoke your election." ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk)) Form 7203 has a check box (item E) for it. Without the election, nondeductible expenses that exceed basis "are not suspended and carried forward." ([IRS: S corporation stock and debt basis](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis))

**Distributions in excess of stock basis.** A non-dividend distribution is tax-free up to stock basis. Debt basis does not count for distributions. "A non-dividend distribution in excess of stock basis is taxed as a capital gain on the shareholder's personal return. It is a long-term capital gain (LTCG) if the S corporation stock has been held for longer than one year." Report the excess on Form 8949 and Schedule D, and do not increase stock basis for the gain reported. ([Instructions for Form 7203](https://www.irs.gov/instructions/i7203))

### Limit 1 continued: debt basis

**Only direct loans count.** Debt basis is the shareholder's adjusted basis in bona fide indebtedness "of the S corporation that runs directly to the shareholder." Whether a loan is bona fide is a facts and circumstances question under general federal tax principles. A loan made through an entity disregarded as separate from the shareholder can count. A back-to-back loan through another corporation can count only if it is bona fide indebtedness running to the shareholder. ([Treas. Reg. 1.1366-2](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1366-2.pdf))

A guarantee gives no debt basis: "A shareholder does not obtain basis of indebtedness in the S corporation merely by guaranteeing a loan or acting as a surety, accommodation party, or in any similar capacity relating to a loan." Basis arises only when, and to the extent that, the shareholder actually makes a payment on the guaranteed debt. The Form 7203 instructions say the same, and add that "Distributions don't reduce loan basis".

**Reduction of debt basis.** When losses, deductions and nondeductible expenses for the year exceed stock basis, the excess reduces (but not below zero) the basis of loans the shareholder holds at the close of the corporation's year. A loan repaid, disposed of or forgiven during the year is not held at year end and is not reduced. With several loans, the reduction is spread in proportion to each loan's basis. ([Treas. Reg. 1.1367-2](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-2.pdf))

**Restoration of debt basis.** Under section 1367(b)(2)(B), a later year's "net increase" first restores reduced debt basis "before any of it may be used to increase the shareholder's basis in the stock". Net increase means the shareholder's income items exceed ALL the section 1367(a)(2) decrease items for the year, distributions included. Restoration applies only to debt held at the start of that year, and never above the debt's adjusted basis at the start of that year with the earlier S corporation reductions left out (in practice, not above the loan's basis before those reductions). With several loans, net increase restores first any loan repaid that year (to the extent needed to offset gain on the repayment), then the others in proportion to their unrestored reductions.

**The repayment trap.** If the corporation repays a loan whose basis was reduced and not fully restored, the repayment "is a recognition event". Each repayment is split between a return of basis and income. In the year of a repayment, restoration takes effect immediately before the first repayment, so that year's net increase can cut the gain. The character of the gain depends on the paperwork. The Form 7203 instructions say: "Debt evidenced by a formal note will result in capital gain, and should be reported on Form 8949 and Schedule D. Any open account debt (including debt referenced in Regulations section 1.1367-2(a)(2)(ii)) will result in ordinary gain and should be reported on Form 4797". Gain on repayment does not increase basis.

**Open account debt.** Shareholder advances not evidenced by separate written instruments, with all advances and repayments in the year netted at year end. If the net unwritten advances are more than USD 25,000 at the close of a year, then for every LATER year Reg. 1.1367-2(a)(2)(ii) treats that debt like debt under a written instrument for the basis rules, and it is no longer open account debt. For the character of gain, the Form 7203 instructions still group that debt with open account debt: ordinary gain on Form 4797.

### Limit 1 result: the section 1366(d) loss limit and suspended losses

Section 1366(d)(1): the aggregate losses and deductions a shareholder takes into account for the year "shall not exceed the sum of" (A) adjusted stock basis, after income and distributions, AND (B) adjusted basis of any indebtedness of the corporation to the shareholder, before this year's debt basis reduction. ([26 U.S.C. 1366](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1366.htm))

When several kinds of loss and deduction exceed the limit, the limit is shared among them in proportion to their size. Losses carried in from earlier years are added to this year's losses for that proration. ([Treas. Reg. 1.1366-2](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1366-2.pdf))

Section 1366(d)(2): a loss disallowed for lack of basis "shall be treated as incurred by the corporation in the succeeding taxable year with respect to that shareholder". It keeps its character and carries forward with no time limit. A suspended loss is not netted with next year's ordinary income in the basis ordering; it is listed on its own line on Schedule E (Form 1040).

**Losses on disposal of stock.** A suspended basis loss is personal to the shareholder. If the shareholder transfers SOME stock, the suspended loss is not reduced and the buyer gets none of it. If the shareholder transfers ALL of the stock, "any disallowed loss or deduction is permanently disallowed." The exception is a transfer to a spouse or former spouse under section 1041(a) after 31 December 2004: the loss on the transferred stock moves to the transferee. So a shareholder with a suspended loss who is about to sell all the stock should look at restoring basis first (for example a real capital contribution) and should not expect the loss to survive the sale.

When the S election ends, losses suspended in the last S year are treated as incurred on the last day of the post-termination transition period, limited to stock basis (not debt basis) at that day.

### Limit 2: at-risk (section 465, Form 6198)

Section 465(a)(1): for an individual, a loss from an activity "shall be allowed only to the extent of the aggregate amount with respect to which the taxpayer is at risk ... for such activity at the close of the taxable year." Amounts at risk include money and the adjusted basis of property contributed, and amounts borrowed for which the taxpayer is personally liable or has pledged property not used in the activity. ([26 U.S.C. 465](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec465.htm))

For an S corporation shareholder, stock or loan basis is NOT at risk if the money used came from nonrecourse borrowing (other than qualified nonrecourse financing), was protected by a guarantee or stop-loss arrangement, or was borrowed from a person with an interest in the activity or a related person, other than a creditor. ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk))

Form 6198 is needed when the shareholder had a loss from an at-risk activity AND had amounts not at risk invested in it. ([Instructions for Form 6198](https://www.irs.gov/instructions/i6198)) At-risk applies activity by activity, so get the corporation's separate statement for each activity.

A loss not allowed under section 465 "shall be treated as a deduction allocable to such activity in the first succeeding taxable year." If the amount at risk falls below zero at a year end, section 465(e) brings the shortfall back into income, capped at the earlier losses that reduced the amount at risk, less amounts already brought back.

### Limit 3: passive activity (section 469, Form 8582)

A trade or business in which the shareholder does not materially participate is a passive activity. Its losses offset only passive income, and the excess carries to the next year under section 469(b). ([26 U.S.C. 469](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm)) Carried passive losses are freed against passive income, or "when you sell or exchange your entire interest in the activity in a fully taxable transaction to an unrelated party." ([Instructions for Form 8582](https://www.irs.gov/instructions/i8582))

**Material participation: the seven tests in Reg. 1.469-5T(a).** An individual materially participates for the year if ANY ONE of these is met ([Treas. Reg. 1.469-5T](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf)):

1. More than 500 hours in the activity during the year.
2. Participation is substantially all of the participation of all individuals, non-owners included.
3. More than 100 hours AND not less than any other individual, non-owners included.
4. The activity is a significant participation activity AND total participation in all such activities exceeds 500 hours.
5. Material participation in any five of the ten immediately preceding years, consecutive or not.
6. A personal service activity with material participation in any three preceding years, consecutive or not.
7. Regular, continuous and substantial participation on all the facts and circumstances.

Test 7 is not available to someone who participates for 100 hours or less in the year. Work done as an investor, such as reviewing financial statements in a non-managerial role, does not count. Work the shareholder or the shareholder's spouse does in the activity generally counts, "where you own your stock at the time the work is done". Material participation is judged on participation during the corporation's tax year. A shareholder who materially participates reports box 1 on Schedule E (Form 1040), line 28, column (i) or (k). ([Shareholder's Instructions for Schedule K-1 (Form 1120-S)](https://www.irs.gov/instructions/i1120ssk))

### Limit 4: excess business loss (section 461(l), Form 461)

Section 461(l) applies at the shareholder level. It compares the shareholder's total trade or business deductions with total trade or business income plus the threshold. The excess "shall not be allowed" this year and "shall be treated as a net operating loss" carried to later years. Wages, and anything else from performing services as an employee, are left out of the computation. So the W-2 salary the owner draws from the S corporation does not absorb the loss under this limit. ([26 U.S.C. 461](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm))

Two items stay out of the comparison. "Deductions for losses from sales or exchanges of capital assets shall not be taken into account", and gains from sales or exchanges of capital assets count only up to "the lesser of (I) the capital gain net income determined by taking into account only gains and losses attributable to a trade or business, or (II) the capital gain net income". The deductions side is figured "without regard to any deduction allowable under section 172 or 199A".

### Steps

1. Collect the K-1 (Form 1120-S) and any attached statements, the prior year's Form 7203, and the loan papers between shareholder and corporation. Basis is the shareholder's job.
2. Decide whether Form 7203 is required using the four triggers above.
3. Stock basis, Form 7203 Part I: start with beginning basis, add income items, subtract non-dividend distributions (excess over basis is capital gain on Form 8949), subtract nondeductible expenses, in the Reg. 1.1367-1(f) order unless the (g) election is in effect.
4. Debt basis, Form 7203 Part II: list each direct loan at its start-of-year basis, add new formal notes and net open account advances, apply any restoration from a net increase, and work out gain on any repayment. Ignore guarantees unless the shareholder paid.
5. Basis limit, Form 7203 Part III: add this year's losses to losses suspended in earlier years, compare with stock basis plus debt basis, prorate if more than one type, and carry the excess forward under section 1366(d)(2).
6. At-risk, Form 6198: if any of the basis came from amounts not at risk, limit the loss that passed step 5 to the amount at risk at year end; carry the rest under section 465(a)(2).
7. Passive, Form 8582: test material participation under the seven tests. If passive, allow the loss that passed step 6 only against passive income; carry the rest under section 469(b).
8. Excess business loss, Form 461: combine every business result of the shareholder, leave out wages, capital losses and any section 172 or 199A deduction, compare the net business loss with the 2026 threshold (USD 256,000, or USD 512,000 joint), and send any excess to Form 172 as a net operating loss.
9. Report what survives on Schedule E (Form 1040), line 28, with each suspended loss allowed this year on its own line. Keep a carryforward schedule that names the limit behind each carried amount.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Guarantee of a corporate bank loan, nothing paid | No debt basis; basis only for amounts actually paid under the guarantee |
| Loan from the shareholder through another corporation (back-to-back) | Debt basis only if bona fide indebtedness running directly to the shareholder; refer if disputed |
| Distribution larger than stock basis | Excess is capital gain (long-term if held over one year); debt basis does not cover distributions |
| Nondeductible expenses larger than basis, no (g) election | Not suspended and not carried forward |
| Elective order under Reg. 1.1367-1(g) | Losses before nondeductible expenses; binding for later years unless the IRS agrees to revoke |
| Repayment of a reduced-basis loan | Gain: capital if a formal note, ordinary (Form 4797) if open account debt |
| Net unwritten advances over USD 25,000 at a year end | Treated as written-instrument debt for basis in later years; still ordinary gain on repayment |
| Sale of ALL the stock with a suspended basis loss | Suspended loss is lost, except a section 1041 transfer to a spouse or former spouse |
| Shareholder worked 100 hours or less | Test 7 is not available |
| W-2 wages from the S corporation | Left out of the excess business loss computation |
| 2025 tax year | Threshold USD 313,000 (USD 626,000 joint), not the 2026 figures |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Beginning stock basis | No loss allowed until basis is rebuilt from records; refer if it cannot be |
| Whether a loan is a formal note or open account | Treat as open account (ordinary gain on repayment) until a signed note is produced |
| Source of the money for the stock (recourse or nonrecourse) | Ask; do not assume it is at risk |
| Hours worked | Treat as passive until hours are documented |
| Other business income and losses of the shareholder | Ask for every Schedule C, Schedule F and K-1 before applying the excess business loss limit |
| Filing status | Ask; the threshold doubles for a joint return |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| No Form 7203 or basis schedule for earlier years | Loss not provable on audit |
| Shareholder relies on a guarantee for basis | No debt basis until payment |
| Repayment of a shareholder loan in a year after losses | Gain on repayment, often missed |
| Large distributions in a loss year | Distributions reduce basis before the loss |
| Planned sale of all the stock with suspended losses | The losses disappear on the sale |
| Combined business losses over USD 256,000 (USD 512,000 joint) | Form 461 and a net operating loss carryover |

## Worked cases

All amounts are invented US dollars for illustration. The only official figure used is the 2026 excess business loss threshold for a single filer (USD 256,000).

**Case 1, the four limits in order.** Ana is the sole shareholder of a calendar-year S corporation and files as single. Stock basis on 1 January 2026: 30,000. Of the cash she paid for the stock, 10,000 came from a nonrecourse loan secured only by the stock. On 1 March 2026 she lent the corporation 40,000 of her own money under a signed note. She also guaranteed a 100,000 bank loan to the corporation and has paid nothing on it. No losses are suspended from earlier years and no Reg. 1.1367-1(g) election. 2026 K-1: box 1 ordinary business loss (90,000); box 4 interest income 1,000; box 16C nondeductible expenses 2,000; box 16D non-dividend distributions 8,000. She worked 1,200 hours in the business; the corporation paid her W-2 wages. She also runs a separate sole proprietorship with a Schedule C net loss of (240,000).

| Step | USD | Running stock basis |
| --- | --- | --- |
| Stock basis 1 January 2026 | | 30,000 |
| Add interest income (box 4) | 1,000 | 31,000 |
| Less non-dividend distributions (box 16D) | (8,000) | 23,000 |
| Less nondeductible expenses (box 16C) | (2,000) | 21,000 |

The distribution of 8,000 is below the 31,000 of basis before distributions, so it is tax-free. Debt basis: 40,000 from the direct loan; the guarantee adds nothing. Section 1366(d) limit: 21,000 + 40,000 = 61,000; suspended for basis: 29,000. At-risk: the 10,000 of stock cost paid with nonrecourse borrowing is not at risk, so 51,000 passes and 10,000 is carried under section 465. Passive: 1,200 hours is more than 500 hours (test 1), so the 51,000 is nonpassive. (If she had worked 80 hours, met no other test and had no passive income, all 51,000 would be suspended under section 469(b), and test 7 would not be available.) Excess business loss: 51,000 + 240,000 = 291,000 of net business loss, wages left out; over the 256,000 threshold by 35,000, which becomes a net operating loss on Form 172. Business loss deducted in 2026: 256,000. Check: 29,000 + 10,000 + 51,000 = 90,000.

```oa-check
name: S corporation K-1 loss through the four limits, single (2026)
inputs:
  beginning_stock_basis: 30000
  interest_income: 1000
  distributions: 8000
  nondeductible: 2000
  debt_basis: 40000
  k1_loss: 90000
  not_at_risk: 10000
  schedule_c_loss: 240000
  ebl_threshold: 256000
steps:
  - stock_basis_before_loss: beginning_stock_basis + interest_income - distributions - nondeductible
  - basis_limit: stock_basis_before_loss + debt_basis
  - allowed_after_basis: min(k1_loss, basis_limit)
  - suspended_basis: k1_loss - allowed_after_basis
  - allowed_after_at_risk: allowed_after_basis - not_at_risk
  - suspended_at_risk: allowed_after_basis - allowed_after_at_risk
  - net_business_loss: allowed_after_at_risk + schedule_c_loss
  - excess_business_loss: max(net_business_loss - ebl_threshold, 0)
  - deducted_2026: net_business_loss - excess_business_loss
expected:
  stock_basis_before_loss: 21000.00
  basis_limit: 61000.00
  suspended_basis: 29000.00
  allowed_after_at_risk: 51000.00
  suspended_at_risk: 10000.00
  net_business_loss: 291000.00
  excess_business_loss: 35000.00
  deducted_2026: 256000.00
```

Carryforwards into 2027:

| Carried (USD) | Limit that stopped it | What frees it |
| --- | --- | --- |
| 29,000 | Section 1366(d), basis | New stock or debt basis in a later year (Form 7203 Part III); lost if she disposes of all her stock, except a section 1041 transfer |
| 10,000 | Section 465, at-risk | An increase in her amount at risk in the activity (Form 6198) |
| 35,000 | Section 461(l), excess business loss | Used as a net operating loss under section 172 (Form 172) |

**Case 2, a distribution over basis and the repayment trap.** Same facts, but the 2026 distribution is 35,000 instead of 8,000. Basis before distributions is 31,000, so 31,000 is tax-free and 4,000 is capital gain on Form 8949; her 40,000 of debt basis does not cover any of the distribution, and stock basis is then 0. The 2,000 of nondeductible expenses comes next in the Reg. 1.1367-1(f) order and, with no stock basis left, reduces debt basis to 38,000 (Reg. 1.1367-2). That 38,000 is all the basis left for the loss, so 52,000 of the 90,000 loss is suspended. Then in 2027 the corporation repays 10,000 of the note and 2027 has no net increase to restore debt basis: her basis in the note is 0 and the whole 10,000 is gain, capital gain on Form 8949 and Schedule D because the debt is a formal note. She files Form 7203 for 2027 because she received a loan repayment.

```oa-check
name: Distribution over stock basis, then repayment of a zero-basis note
inputs:
  basis_before_distribution: 31000
  distribution: 35000
  debt_basis: 40000
  nondeductible: 2000
  k1_loss: 90000
  repayment_2027: 10000
  note_basis_2027: 0
steps:
  - tax_free: min(distribution, basis_before_distribution)
  - capital_gain_distribution: distribution - tax_free
  - stock_basis_after: max(basis_before_distribution - distribution, 0)
  - basis_limit: stock_basis_after + debt_basis - nondeductible
  - suspended_basis: k1_loss - min(k1_loss, basis_limit)
  - repayment_gain: repayment_2027 - min(repayment_2027, note_basis_2027)
expected:
  tax_free: 31000.00
  capital_gain_distribution: 4000.00
  basis_limit: 38000.00
  suspended_basis: 52000.00
  repayment_gain: 10000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-K1-NOBASIS | No reliable beginning basis and no records to rebuild it | Refer: claiming a loss without proven basis invites disallowance |
| R-K1-DEBT | Back-to-back loans, loans through another entity, or disputed bona fide debt status | Refer: the regulation turns on all the facts and circumstances |
| R-K1-GUAR | Payments made under a guarantee, debt restructurings, or shareholder debt forgiven by or to the corporation | Refer |
| R-K1-BASISCASES | Inherited stock (income in respect of a decedent rules under section 1367(b)(4)), stock from a section 351 transfer with liabilities over basis, or several blocks of stock with different bases bought or sold during the year | Refer |
| R-K1-TERM | A terminated S election and losses in the post-termination transition period | Refer |
| R-K1-PASSIVE | Grouping of activities, rental activities inside the corporation (K-1 boxes 2 and 3), real estate professional claims | Outside this skill; refer |
| R-K1-OTHER | Partnership K-1 losses, reasonable compensation, QBI | Use `us-form-1065-partnership`, `us-s-corp-election-decision`, `us-qbi-deduction` |
| R-K1-ENTITY | The corporation's own Form 1120-S return, or whether the S election is valid or has ended | Refer: this skill covers only the shareholder's loss |
| R-K1-STATE | State conformity, state basis and state net operating losses | Outside this skill |

## Filing and payment

The shareholder attaches Form 7203 (when any trigger applies), Form 6198 (when amounts not at risk are invested), Form 8582 (passive losses) and Form 461 (excess business loss) to the 2026 Form 1040, due 15 April 2027; an extension to 15 October 2027 extends filing, not payment. Allowed losses go on Schedule E (Form 1040), Part II, line 28; the excess business loss goes to Form 172 as a net operating loss carryover. The S corporation's own Form 1120-S for calendar 2026 is due 15 March 2027 (see `us-corporate-extension-form-7004-and-the` for its extension).

## Completion checklist

- Form 7203 need tested against all four triggers; one form per spouse holding stock.
- Stock basis adjusted in the Reg. 1.1367-1(f) order, or the (g) election documented.
- Debt basis from direct loans only; guarantees excluded unless paid; open account debt netted at year end against USD 25,000.
- Basis limit applied with proration across loss types and prior suspended losses.
- At-risk, passive and excess business loss limits applied in that order, each with its form.
- 2026 threshold used (USD 256,000 or USD 512,000), not the 2025 figures.
- Carryforward schedule names the limit behind each carried amount.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS, S corporation stock and debt basis. Read for the four limits in order, the shareholder's responsibility, and distributions in excess of basis. | https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis | 2026-11-13 |
| Instructions for Form 7203 (Rev. December 2022). Read for the filing triggers, the order of limits, guarantees, and character of repayment gain. | https://www.irs.gov/pub/irs-pdf/i7203.pdf | 2026-11-13 |
| Shareholder's Instructions for Schedule K-1 (Form 1120-S) (2025). Read for "without reference to limitations on losses", the (g) election, at-risk exclusions and material participation. | https://www.irs.gov/pub/irs-pdf/i1120ssk.pdf | 2026-11-13 |
| Instructions for Form 6198 (2025). Read for who must file. | https://www.irs.gov/pub/irs-pdf/i6198.pdf | 2026-11-13 |
| Instructions for Form 8582 (2025). Read for freeing suspended losses on a full taxable disposition. | https://www.irs.gov/pub/irs-pdf/i8582.pdf | 2026-11-13 |
| Instructions for Form 461 (2025). Read for the 2025 threshold (USD 313,000 and USD 626,000) and the permanent extension. | https://www.irs.gov/pub/irs-pdf/i461.pdf | 2026-11-13 |
| Rev. Proc. 2025-32. Read for the 2026 excess business loss threshold (USD 256,000 and USD 512,000). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Public Law 119-21, section 70601. Read for the permanent rule and the change of the base year from 2017 to 2024. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 461 (govinfo, 2024 edition). Read for (l) and the USD 250,000 statutory amount. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec461.htm | 2026-11-13 |
| 26 U.S.C. 465 and 469 (govinfo). Read for the at-risk limit and passive activity carryover. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm | 2026-11-13 |
| 26 U.S.C. 1366 and 1367 (govinfo). Read for the (d) loss limit and the basis adjustments. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1366.htm | 2026-11-13 |
| Treas. Reg. 1.1366-2, 1.1367-1, 1.1367-2 (govinfo, CFR 2025). Read for direct debt, guarantees, the ordering rule and the USD 25,000 open account rule. | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/pdf/CFR-2025-title26-vol13-sec1-1367-2.pdf | 2026-11-13 |
| Treas. Reg. 1.469-5T (govinfo, CFR 2025). Read for the seven tests (500 and 100 hours). | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol8/pdf/CFR-2025-title26-vol8-sec1-469-5T.pdf | 2026-11-13 |

Not yet confirmed: the 2026 editions of the Shareholder's Instructions for Schedule K-1 (Form 1120-S) and of the Form 6198, 8582 and 461 instructions were not yet published when read; the 2025 editions are relied on for procedure, and the 2026 excess business loss threshold comes from Rev. Proc. 2025-32.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-1120-corporation-return-schedule-ordinary-business` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-1120-corporation-return-schedule-ordinary-business. If neither is available, confirm every figure against the official source pages cited above before relying on it.
