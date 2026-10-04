---
name: uk-income-tax-sa100
description: Use this skill whenever asked about UK income tax for individuals filing SA100 Self Assessment. Trigger on phrases like "income tax UK", "SA100", "personal allowance", "tax bands", "tax computation", "marriage allowance", "savings allowance", "dividend allowance", "Scottish tax rates", "payments on account", "tax reducers", "tax relief", "April 2026", "2026-27", "Autumn Budget 2025", "income tax bands frozen 2027-28", or any question about computing a UK individual's income tax liability. Covers personal allowance (including taper), income tax bands for rUK and Scotland, marriage allowance, savings and dividend allowances, tax reducers, the final tax computation, payments on account, and the Autumn Budget 2025 changes from April 2026. ALWAYS read this skill before touching any UK income tax return work.
version: 2.1
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-26
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Income Tax for individuals: the SA100 Self Assessment return

Tax year 2026/27 (6 April 2026 to 5 April 2027) is the year in force. The returns being filed now are for tax year 2025/26, on the SA100 form HMRC calls "Tax Return 2026", which is due online by 31 January 2027. Where a rule differs between those years, both are shown. Changes already enacted for 2027/28 are flagged so that nobody applies them early.

## Scope and who this is for

This guide covers individuals resident in England, Wales or Northern Ireland who work out Income Tax on the SA100 return. It covers who must register and file, rates and bands, the Personal Allowance taper, the savings and dividend allowances, the Finance Act 2026 rate changes, the High Income Child Benefit Charge, Marriage Allowance, pension and Gift Aid relief claimed through the return, payments on account, deadlines, penalties and interest.

Out of scope: Scottish taxpayers (the rates are different, so refer them); non-residents and split years (SA109); the foreign income and gains regime; trusts (SA107); Capital Gains Tax (SA108); the detail of self-employment (SA103) and UK property (SA105); National Insurance. Making Tax Digital for Income Tax (MTD) gets a cross-reference only ([MTD: who needs it](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax)).

## Ask the client first

- Which tax year is this: the 2025/26 return being filed now, or planning for 2026/27?
- Where was your main home during the year? If it was in Scotland, stop and refer. If you were outside the UK for part of the year, also refer.
- Have you registered for Self Assessment before? Did you get a return for 2024/25? (This decides the 5 October registration duty.)
- Employment: P60, P11D, P45, any tips or payments not on the P60, any termination or redundancy payment?
- Self-employment or property: gross income before expenses? (This decides the trading and property allowances and MTD.)
- Bank and building society interest, including taxed and untaxed interest, but not ISA interest.
- Dividends from UK companies and funds, and any non-ISA share holdings.
- Pensions received: State Pension, workplace or private pensions, annuities.
- Personal pension contributions: relief at source or net pay? Contributions paid gross? Have you taken flexible pension income before?
- Gift Aid donations, and any made since 6 April of the current year that you want carried back.
- Married or in a civil partnership? What are both partners' incomes? Is Marriage Allowance already in place?
- Does anyone in the household get Child Benefit? What is each partner's adjusted net income?
- Did you get a Winter Fuel Payment in 2025/26?
- What did your last SA302 say, and which payments on account did you make on 31 January and 31 July?
- Has HMRC written to you about MTD?

## The method, step by step

1. **Pick the tax year and confirm the person is in scope.** For a Scottish taxpayer, a non-resident or a split year, stop and refer.
2. **Decide whether a return is needed** and whether the 5 October registration deadline has been missed ([who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return); [register](https://www.gov.uk/register-for-self-assessment)).
3. **Collect total income** by source, gross. Non-savings income is employment, self-employment, pensions and property. Savings income is interest. Dividend income comes last.
4. **Take off reliefs deductible from income**, such as trading losses and pension contributions paid gross. Then work out adjusted net income by also deducting grossed-up Gift Aid and grossed-up relief-at-source pension contributions ([adjusted net income](https://www.gov.uk/guidance/adjusted-net-income)).
5. **Set the Personal Allowance.** Start at £12,570 and taper it by £1 for every £2 of adjusted net income above £100,000 ([Income Tax rates](https://www.gov.uk/income-tax-rates)). Adjust for Marriage Allowance if the client is the transferor.
6. **Extend the basic rate band** by grossed-up relief-at-source pension contributions and grossed-up Gift Aid.
7. **Tax the income in statutory order**: non-savings first, then savings (starting rate, then Personal Savings Allowance), then dividends (dividend allowance). Use the rates for the chosen year.
8. **Take off tax reducers**, such as the Marriage Allowance reduction for the recipient.
9. **Add charges**: High Income Child Benefit Charge, any Winter Fuel Payment charge for 2025/26, and the pension annual allowance charge.
10. **Take off tax already paid**: PAYE, tax taken off interest, and payments on account made.
11. **Work out payments on account** for the next year, then set the 31 January and 31 July dates ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).
12. **File and pay on time.** A late return or late payment triggers the penalties and interest below.

## Rates, allowances and thresholds by year

### Main rates and bands: England, Wales and Northern Ireland ([Finance Act 2026 s.2](https://www.legislation.gov.uk/ukpga/2026/11/section/2); [Income Tax rates](https://www.gov.uk/income-tax-rates); [previous tax years](https://www.gov.uk/income-tax-rates/previous-tax-years))

| Band (standard Personal Allowance) | 2025/26 | 2026/27 (current year) |
| --- | --- | --- |
| Personal Allowance | Up to £12,570 at 0% | Up to £12,570 at 0% |
| Basic rate 20% | £12,571 to £50,270 | £12,571 to £50,270 |
| Higher rate 40% | £50,271 to £125,140 | £50,271 to £125,140 |
| Additional rate 45% | Over £125,140 | Over £125,140 |

- For 2026/27, Finance Act 2026 s.2 sets "the basic rate is 20%", "the higher rate is 40%" and "the additional rate is 45%".
- "You do not get a Personal Allowance on taxable income over £125,140" ([Income Tax rates](https://www.gov.uk/income-tax-rates)).
- Scotland: "Income tax bands are different if you live in Scotland". Scottish rates apply to non-savings income only; savings and dividends use UK rates ([Income Tax in Scotland](https://www.gov.uk/scottish-income-tax)). This guide refers Scottish taxpayers; see "When to refuse or refer".

### Frozen thresholds ([Finance Act 2026 s.10](https://www.legislation.gov.uk/ukpga/2026/11/section/10); [s.9](https://www.legislation.gov.uk/ukpga/2026/11/section/9))

- The Personal Allowance is £12,570 and the basic rate limit is £37,700 for every tax year up to and including 2030/31. FA 2026 s.10 extended the freeze in FA 2021 s.5 from 2027/28 to 2030/31. With a standard allowance, higher rate therefore starts above £50,270 until then.
- The starting rate limit for savings is £5,000 for 2026/27 to 2030/31 (s.9), and indexation is switched off.

### Savings income ([Finance Act 2026 s.3](https://www.legislation.gov.uk/ukpga/2026/11/section/3); [s.5](https://www.legislation.gov.uk/ukpga/2026/11/section/5); [HMRC policy paper](https://www.gov.uk/government/publications/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income); [savings allowances](https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free))

| Item | 2025/26 | 2026/27 (current year) | 2027/28 (enacted, not yet in force) |
| --- | --- | --- | --- |
| Savings basic rate | 20% | 20% | 22% |
| Savings higher rate | 40% | 40% | 42% |
| Savings additional rate | 45% | 45% | 47% |
| Starting rate for savings band | £5,000 | £5,000 | £5,000 |
| Personal Savings Allowance: basic rate taxpayer | £1,000 | £1,000 | Not yet published |
| Personal Savings Allowance: higher rate taxpayer | £500 | £500 | Not yet published |
| Personal Savings Allowance: additional rate taxpayer | £0 | £0 | Not yet published |

- For 2025/26 the policy paper says "Since April 2017 the rates have been 20% for basic rate taxpayers, 40% for higher rate taxpayers, and 45% for additional rate taxpayers". FA 2026 s.3(2) keeps them for 2026/27.
- **The savings increase is for 2027/28, not 2026/27.** FA 2026 s.5: "For the tax year 2027-28 ... the savings basic rate is 22% ... higher rate is 42% ... additional rate is 47%." These rates apply UK-wide.
- Personal Savings Allowance amounts are from HMRC's current guidance. HMRC has not published 2027/28 amounts.

### Dividend income ([Finance Act 2026 s.4](https://www.legislation.gov.uk/ukpga/2026/11/section/4); [tax on dividends](https://www.gov.uk/tax-on-dividends); [HMRC policy paper](https://www.gov.uk/government/publications/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income))

| Item | 2025/26 | 2026/27 onwards |
| --- | --- | --- |
| Dividend allowance | £500 | £500 |
| Dividend ordinary rate (basic rate band) | 8.75% | 10.75% |
| Dividend upper rate (higher rate band) | 33.75% | 35.75% |
| Dividend additional rate | 39.35% | 39.35% |

- FA 2026 s.4 substitutes "10.75%" for "8.75%" and "35.75%" for "33.75%", with "effect for the tax year 2026-27 and subsequent tax years". The policy paper confirms "the dividend additional rate will remain at 39.35%". The rates apply UK-wide, including to Scottish taxpayers.
- The rise applies to distributions made on or after 6 April 2026. A 2025/26 return uses 8.75% and 33.75%.

### Property income and allowance order from 2027/28 ([Finance Act 2026 s.7](https://www.legislation.gov.uk/ukpga/2026/11/section/7); [HMRC policy paper](https://www.gov.uk/government/publications/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income))

- 2025/26 and 2026/27: property profit is taxed at the main rates (20%, 40%, 45%).
- 2027/28: separate property rates of 22%, 42% and 47% apply in England, Wales and Northern Ireland (s.7). See the UK property (SA105) guide.
- From 2027/28, general reliefs and allowances, including the Personal Allowance, are set against property, savings and dividend income only after other income. Do not apply this ordering to 2025/26 or 2026/27.

### Other allowances and thresholds ([trading and property allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income); [Marriage Allowance](https://www.gov.uk/marriage-allowance); [Child Benefit charge](https://www.gov.uk/child-benefit-tax-charge); [annual allowance](https://www.gov.uk/tax-on-your-private-pension/annual-allowance); [tapered annual allowance](https://www.gov.uk/guidance/pension-schemes-work-out-your-tapered-annual-allowance); [ITEPA 2003 s.403](https://www.legislation.gov.uk/ukpga/2003/1/section/403))

| Item | Figure | Years |
| --- | --- | --- |
| Trading allowance | Up to £1,000 of gross trading income | Each year since 6 April 2017 |
| Property allowance | Up to £1,000 of gross property income | Each year since 6 April 2017 |
| Marriage Allowance | Transfer £1,260 of Personal Allowance; reduces partner's tax by up to £252 | 2025/26 and 2026/27 |
| High Income Child Benefit Charge | Adjusted net income over £60,000; full charge at £80,000 or more; 1% per £200 | 2024/25 onwards |
| Pension annual allowance | £60,000 | Current tax year |
| Tapered annual allowance | Threshold income over £200,000 and adjusted income over £260,000; minimum £10,000 | Current tax year |
| Termination payments | Taxable above the £30,000 threshold only for a payment to which s.403 applies. Post-employment notice pay (ss.402A-402E), contractual PILON, holiday pay and bonuses are taxed in full as earnings ([s.401](https://www.legislation.gov.uk/ukpga/2003/1/section/401); [s.402B](https://www.legislation.gov.uk/ukpga/2003/1/section/402B)) | Standing law |

## The rules in detail

### Who must register and file ([who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return); [register](https://www.gov.uk/register-for-self-assessment); [trading and property allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income))

- **A return is required if**, in the last tax year, the person "were self-employed as a 'sole trader' and earned more than £1,000 (before taking off anything you can claim tax relief on)", was a partner in a partnership, had Capital Gains Tax to pay, "had to pay the High Income Child Benefit Charge and do not pay it through PAYE", or is an off-payroll worker repaying a student or postgraduate loan.
- **A return may be needed** for untaxed income: rent, tips and commission, savings interest, dividends, foreign income, or any taxable UK income of a non-resident. It may also be needed to claim some reliefs. A person HMRC has written to "must" send a return by the deadline on the letter.
- **Trading and property thresholds.** Gross trading income of £1,000 or less, and gross property income of £1,000 or less, is covered by the allowances ("full relief"). HMRC must be told about "gross trading income over £1,000 — register for Self Assessment". Above £1,000 the person may deduct the £1,000 allowance instead of actual expenses ("partial relief"), but not both. The trading allowance does not apply to partnership income.
- **Property notification tiers**: "gross property income over £1,000 up to £2,500 — contact HMRC"; "property income over £2,500 — register for Self Assessment".
- **Allowances cannot be used** in a year with any trade or property income from "a company you or someone connected to you owns or controls", a partnership where you or someone connected to you are partners, or "your employer or the employer of your spouse or civil partner". The property allowance also cannot be used if you "claim the tax reducer for finance costs", or if you deduct expenses from letting a room in your own home instead of using Rent a Room.
- **Other income under the trading allowance** (miscellaneous income such as casual services, for example babysitting or gardening, or hiring out personal equipment): HMRC says to contact it for "other gross income over £1,000 up to £2,500" and to register for Self Assessment for "other income over £2,500".
- **Register by 5 October.** "You must tell HMRC by 5 October 2026 if you need to complete a tax return for the previous tax year" (2025/26) and you have not sent a return before, or did not need to send one for 2024/25. Registering late can lead to a failure-to-notify penalty if the tax is not paid by 31 January.

### Personal Allowance and the taper ([Income Tax rates](https://www.gov.uk/income-tax-rates); [adjusted net income](https://www.gov.uk/guidance/adjusted-net-income))

- The standard Personal Allowance is £12,570. It "goes down by £1 for every £2 that your adjusted net income is above £100,000", so it is zero at £125,140 or above. This applies "regardless of your date of birth".
- Adjusted net income is total taxable income, less trading losses and pension contributions paid gross, less grossed-up Gift Aid ("for every £1 of Gift Aid donations you made, take £1.25"), and less grossed-up relief-at-source pension contributions (also £1.25 per £1). Add back any trade union or police organisation relief (up to £100) taken at step 1.
- Pension contributions and Gift Aid can bring adjusted net income back under £100,000 and restore the allowance. Check the contribution fits the annual allowance.

### Savings income ([savings allowances](https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free); [Finance Act 2026 s.9](https://www.legislation.gov.uk/ukpga/2026/11/section/9))

- Order: any unused Personal Allowance first, then the starting rate for savings, then the Personal Savings Allowance, then the savings rates.
- **Starting rate for savings**: available if other taxable income (not savings or dividends) "is less than £17,570". It gives up to £5,000 of interest tax-free, reduced £1 for every £1 of other income above the Personal Allowance.
- **Personal Savings Allowance**: £1,000 for basic rate, £500 for higher rate, £0 for additional rate. "To work out your tax band, add all the interest you've earned to your other income." Interest above the allowance is taxed at the savings rates.
- ISA interest is not taxable. Joint account interest is split equally unless shown otherwise.

### Dividend income ([tax on dividends](https://www.gov.uk/tax-on-dividends); [Finance Act 2026 s.4](https://www.legislation.gov.uk/ukpga/2026/11/section/4))

- Dividends sit on top of all other income. First, dividends within any unused Personal Allowance are tax-free. Then the £500 dividend allowance applies. Then 10.75% (ordinary), 35.75% (upper) or 39.35% (additional) for 2026/27.
- The allowance is a band taxed at nothing, not a deduction. Dividends inside it still count toward the basic and higher rate bands. The SA150 notes say to include all dividend income "even if it's less than £500".
- ISA dividends are not taxable. Dividends above both the unused Personal Allowance and the dividend allowance must be reported.

### High Income Child Benefit Charge ([Child Benefit charge](https://www.gov.uk/child-benefit-tax-charge))

- The charge applies if you or your partner gets Child Benefit and an adjusted net income is "over £60,000 for tax years starting from 2024 to 2025". It is "1% of your Child Benefit for every £200" above £60,000, and all of it at "£80,000 or more".
- If both partners are over the threshold, "whoever has the higher income is responsible". 'Partner' includes an unmarried partner living with you. The charge may also apply "if someone else gets Child Benefit for a child living with you and they contribute at least an equal amount towards the child's upkeep". "It does not matter if the child living with you is not your own child."
- You can pay through PAYE, but you **must** use Self Assessment if you need a return for another reason, or if it is later than 31 January after the tax year. For example, a 2025/26 charge not settled by 31 January 2027 must go through Self Assessment.
- Opting out of Child Benefit payments avoids the charge but keeps National Insurance credits.

### Marriage Allowance ([Marriage Allowance](https://www.gov.uk/marriage-allowance))

- The lower earner transfers £1,260 of Personal Allowance to a spouse or civil partner, which "reduces their tax by up to £252".
- All of these conditions must be met: married or in a civil partnership (not just living together); the transferor pays no Income Tax or has income below the Personal Allowance; the recipient pays basic rate, "which usually means their income is between £12,571 and £50,270". A Scottish recipient may pay starter, basic or intermediate rate.
- Claims can be backdated "to 6 April 2022 (the 2022 to 2023 tax year)". The transfer renews automatically until cancelled. It cannot be combined with Married Couple's Allowance.
- In the 2025/26 SA150 notes, the Marriage Allowance section is for a transferor whose "earnings from 6 April 2025 to 5 April 2026 were less than £12,570 (plus up to £6,000 in savings interest)". A claim under the foreign income and gains regime for 2025/26 loses the entitlement ([SA150 notes 2026](https://assets.publishing.service.gov.uk/media/6a9ea8a5df4246cf45e469e0/SA150_Notes_2026.pdf)).

### Pension contributions through the return ([pension tax relief](https://www.gov.uk/tax-on-your-private-pension/pension-tax-relief); [annual allowance](https://www.gov.uk/tax-on-your-private-pension/annual-allowance))

- **Net pay schemes**: relief is given through payroll, so there is nothing to claim.
- **Relief at source** (personal and stakeholder pensions, some workplace schemes): the provider adds 20% basic rate relief. On the return, enter the gross amount (the net paid multiplied by 100/80). The gross amount extends the basic rate band and reduces adjusted net income. A higher or additional rate taxpayer in England, Wales or Northern Ireland claims "20% up to the amount of any income you have paid 40% tax on" and "25% up to the amount of any income you have paid 45% tax on".
- Relief is limited to contributions up to 100% of annual earnings. A non-taxpayer gets relief at source up to £2,880 of net contributions if they have no earnings.
- **Annual allowance** of £60,000. It is lower after flexible access (the money purchase annual allowance) or with high income (the taper). Unused allowance from the previous 3 tax years can be carried forward. Any charge is reported in the 'Pension savings tax charges' section (SA101 on paper).

### Gift Aid through the return ([Gift Aid](https://www.gov.uk/donating-to-charity/gift-aid))

- The charity claims 25p per £1. A higher rate taxpayer claims the difference on the return. HMRC's example: "You donate £100 ... make your donation £125. You pay 40% tax so you can personally claim back £25.00 (£125 x 20%)."
- Donations must not exceed "4 times what you have paid in tax in that tax year". Otherwise HMRC may recover the shortfall.
- Donations made in the current year, up to the filing date, can be treated as made in the previous year. This is lost if you "miss the deadline for your Self Assessment tax return (31 January if you file online, or 31 October if you file by post)".
- Payroll Giving is not entered as Gift Aid.

### Payments on account and the balancing payment ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account); [Taxes Management Act 1970 s.59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A))

- Two payments, each normally half of last year's Self Assessment liability, are due "by midnight on 31 January and 31 July". The liability used is the net amount after tax deducted at source; it includes Class 4 National Insurance.
- They are not required if either: "the amount of tax you owed last year was less than £1,000", or "last year you paid more than 80% of the tax you owed outside of Self Assessment" (PAYE, tax taken off interest).
- The balancing payment (total tax for the year less the payments on account made) is due "by midnight on 31 January the following year", together with the first payment on account for the next year.
- To reduce payments on account, apply online or on form SA303. If the bill turns out higher, "you'll be charged interest on the difference".
- The 2026/27 payments on account are based on 2025/26 liability. The 2026/27 dividend rate rise can leave a larger balancing payment on 31 January 2028.

## Boundary and exception table ([Income Tax rates](https://www.gov.uk/income-tax-rates); [Child Benefit charge](https://www.gov.uk/child-benefit-tax-charge); [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account); [deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines))

| Situation | Rule |
| --- | --- |
| Adjusted net income exactly £100,000 | No taper. The allowance falls only for income "above £100,000" |
| Adjusted net income £125,140 or more | Personal Allowance is zero |
| Adjusted net income exactly £60,000 | No Child Benefit charge. It applies "over £60,000" |
| Adjusted net income £80,000 or more | Child Benefit charge equals all Child Benefit received |
| Both partners over £60,000 | The partner with the higher adjusted net income pays |
| Other income £17,570 or more | No starting rate for savings. It needs other income "less than £17,570" |
| Last year's tax owed under £1,000 | No payments on account. At £1,000 or more they are due, unless the 80% test is met |
| More than 80% of last year's tax paid at source | No payments on account. At exactly 80% they are still due (s.59A uses "not less than") |
| Gross trading income £1,000 or less | Full relief. Registration not needed unless another reason applies |
| Marriage Allowance recipient pays higher or additional rate (England, Wales, NI) | Not eligible |
| Dividends or interest inside an ISA | Not taxable and not entered |
| Paper return misses 31 October | File online by 31 January instead to avoid a penalty |
| Registered after 5 October 2026 for 2025/26 | Return due 3 months from the date of HMRC's notice, but tax still due by 31 January 2027 |
| Wants a 2025/26 balance collected through the tax code | Online return by 30 December 2026 |
| Scottish taxpayer | Refer. Non-savings bands differ; savings and dividends use UK rates |

## Worked cases

### Case A: basic rate employee, England, 2026/27 ([Income Tax rates](https://www.gov.uk/income-tax-rates); [previous tax years](https://www.gov.uk/income-tax-rates/previous-tax-years))

Salary £35,000, PAYE £4,486, no other income. Taxable income is £35,000 − £12,570 = £22,430. Tax at 20% is £4,486. After PAYE, nothing is due. The result is the same for 2025/26: HMRC's own example taxes "£22,430 (£35,000 minus £12,570)" at 20%. No return is needed for this income alone.

### Case B: employment, self-employment and dividends, 2025/26 against 2026/27 ([Finance Act 2026 s.4](https://www.legislation.gov.uk/ukpga/2026/11/section/4); [Income Tax rates](https://www.gov.uk/income-tax-rates); [tax on dividends](https://www.gov.uk/tax-on-dividends))

Employment £40,000 (PAYE £5,486), self-employment profit £20,000, UK dividends £5,000. Total income is £65,000 and adjusted net income is under £100,000, so the full £12,570 allowance applies.

- Non-savings income: £60,000 − £12,570 = £47,430 taxable. £37,700 at 20% = £7,540. £9,730 at 40% = £3,892. Non-savings tax is £11,432.
- Dividends sit wholly in the higher rate band. The first £500 is taxed at nothing; the remaining £4,500 is taxed at the upper rate.
- **2025/26 return:** £4,500 × 33.75% = £1,518.75. Total Income Tax is £12,950.75. Less PAYE £5,486 leaves £7,464.75 through Self Assessment.
- **2026/27:** £4,500 × 35.75% = £1,608.75. Total Income Tax is £13,040.75. Less PAYE £5,486 leaves £7,554.75, which is £90 more.
- Class 4 National Insurance on the profit is extra (see the SA103 guide), and it also feeds payments on account.

### Case C: Personal Allowance taper, 2026/27 ([Income Tax rates](https://www.gov.uk/income-tax-rates); [adjusted net income](https://www.gov.uk/guidance/adjusted-net-income))

Total income £115,000, all non-savings. Relief-at-source pension contributions are £8,000 paid, which is £10,000 gross. Adjusted net income is £115,000 − £10,000 = £105,000. The allowance falls by (£105,000 − £100,000) / 2 = £2,500, to £10,070. The basic rate band is extended by the gross contribution: £37,700 + £10,000 = £47,700. Higher rate therefore starts above £10,070 + £47,700 = £57,770 of income. Without the contribution, adjusted net income would be £115,000 and the allowance would be £12,570 − £7,500 = £5,070.

### Case D: High Income Child Benefit Charge, 2026/27 ([Child Benefit charge](https://www.gov.uk/child-benefit-tax-charge))

The higher-earning partner has adjusted net income of £70,000; the other partner's is lower. Assume Child Benefit received in the year was £1,800 (the actual figure comes from the family's award). £70,000 − £60,000 = £10,000 over the threshold. £10,000 / £200 = 50, so the charge is 50% × £1,800 = £900, payable by the higher earner. HMRC's own example: adjusted net income of £67,600 gives "38%".

### Case E: Marriage Allowance ([Marriage Allowance](https://www.gov.uk/marriage-allowance))

HMRC's example: the lower earner has £11,500 of income and the partner has £20,000. Before the transfer the couple pays tax on £7,430. After transferring £1,260, the lower earner's allowance is £11,310, so they pay tax on £190. The partner is taxed on £6,170. "As a couple you benefit, as you are only paying Income Tax on £6,360 rather than £7,430, which saves you £214 in tax."

### Case F: savings interest ([savings allowances](https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free))

- Starting rate: wages £16,000 and interest £200. £16,000 − £12,570 = £3,430 reduces the starting rate band to £5,000 − £3,430 = £1,570, so the £200 is tax-free.
- Personal Savings Allowance: a basic rate taxpayer with £1,300 of interest. The first £1,000 is tax-free; £300 × 20% = £60. The rate is still 20% in 2026/27; 22% applies only from 2027/28.

### Case G: first-year payments on account, 2025/26 return ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account))

Employee with rental profit, filing for the first time. 2025/26 Income Tax is £13,000 and PAYE is £5,000, so £8,000 is owed through Self Assessment. That is at least £1,000, and far less than 80% was paid at source, so payments on account apply. By 31 January 2027 the client pays the £8,000 plus a first 2026/27 payment on account of £4,000, a total of £12,000. A second £4,000 is due by 31 July 2027. Any 2026/27 balance is due by 31 January 2028.

### Case H: late online return for 2025/26 ([penalties](https://www.gov.uk/self-assessment-tax-returns/penalties))

The return is filed on 20 August 2027 with £4,000 of tax due, which was paid on 31 January 2027. Late filing penalties: £100, plus £10 a day for 90 days (£900, the maximum), plus the 6-month penalty of the greater of 5% × £4,000 = £200 and £300, so £300. The total is £1,300. Had the tax also been paid late, 5% penalties at 30 days, 6 months and 12 months would be added, plus interest.

## When to refuse or refer

- **Scottish taxpayers** (main home in Scotland, or unclear between homes): refer. The 2026/27 Scottish bands are 19%, 20%, 21%, 42%, 45% and 48% at different thresholds. Pension relief and Marriage Allowance limits also differ ([Income Tax in Scotland](https://www.gov.uk/scottish-income-tax)).
- **Non-residents, split years, dual residents and the foreign income and gains regime** (which replaced the remittance basis from 6 April 2025): refer to a specialist and the SA109 pages.
- **Trust or estate income** (SA107), **capital gains** (SA108) and **partnership returns**: out of scope.
- **Pensions**: the tapered or money purchase annual allowance, carry-forward near the limit, annual allowance charges, lump sums and drawdown. Refer ([annual allowance](https://www.gov.uk/tax-on-your-private-pension/annual-allowance)).
- **Termination and redundancy payments**: refer, whatever the size, if the payment includes notice pay or PILON, if its make-up is unclear, if it is over the £30,000 threshold, or if it has non-cash elements ([ITEPA 2003 s.403](https://www.legislation.gov.uk/ukpga/2003/1/section/403); [s.401](https://www.legislation.gov.uk/ukpga/2003/1/section/401)).
- **Anyone asking to apply 2027/28 savings or property rates, or the new allowance order, to 2025/26 or 2026/27**: refuse. Those rules are not in force until 6 April 2027.
- **MTD for Income Tax clients**: the quarterly updates and digital records are outside this guide. See the Making Tax Digital guide.
- **Disputes, enquiries, penalty appeals and reasonable excuse**: refer.
- Never present a computation as final. It is an estimate until checked against the SA302 or HMRC's calculation.

## Filing and payment

### Deadlines for the 2025/26 return ([deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines); [register](https://www.gov.uk/register-for-self-assessment))

| Event | Date |
| --- | --- |
| Register if new to Self Assessment | 5 October 2026 |
| Paper return received by HMRC | 11:59pm on 31 October 2026 |
| Online return, if the balance is to be collected through the tax code | 11:59pm on 30 December 2026 |
| Online return | 11:59pm on 31 January 2027 |
| Balancing payment for 2025/26 and first 2026/27 payment on account | 11:59pm on 31 January 2027 |
| Second 2026/27 payment on account | 31 July 2027 |
| 2026/27 return (online) and balancing payment | 31 January 2028 |

HMRC must receive the return and any money owed by the deadline. A return is still required even if the profit for the whole year is not yet known.

### Penalties ([penalties](https://www.gov.uk/self-assessment-tax-returns/penalties))

- **Late filing**: "an initial £100 penalty". After 3 months, "additional daily penalties of £10 per day, up to a maximum of £900". After 6 months, "a further penalty of 5% of the tax due or £300, whichever is greater". After 12 months, "another 5% or £300 charge, whichever is greater". All partners are charged if a partnership return is late.
- **Late payment**: "penalties of 5% of the tax unpaid at: 30 days 6 months 12 months", plus interest.
- **Late registration**: a failure-to-notify penalty can apply if you register after 5 October and do not pay all the tax by 31 January.
- A penalty is payable within 30 days of the notice. Appeals need a reasonable excuse.

### Late payment interest ([HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates))

- Late payment interest is "set at base rate plus 4% from 6 April 2025 (was plus 2.5% on or before 5 April 2025)" and is charged on tax paid late.
- The current rate on HMRC's page is "7.75% from 9 January 2026". Repayment interest is "2.75% from 9 January 2026". The rate moves with Bank of England base rate, so check the page on the day.

### Making Tax Digital for Income Tax: cross-reference only ([MTD: who needs it](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax); [MTD penalties](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax))

- Sole traders and landlords with qualifying income over £50,000 for 2024/25 "should've started using Making Tax Digital for Income Tax from 6 April 2026". The threshold is over £30,000 (2025/26 income) from 6 April 2027 and over £20,000 (2026/27 income) from 6 April 2028. Partnerships come later.
- A 2025/26 SA100 is still filed as normal. HMRC: "if you use Making Tax Digital for Income Tax from 6 April 2026, current penalties will apply to your 2025 to 2026 tax return deadline of 31 January 2027".
- From the year a person joins, new points-based late submission and late payment penalties replace the ones above. There are no penalties for missed quarterly updates in 2026/27. See the Making Tax Digital guide for details.

### The 2025/26 SA100 ("Tax Return 2026"): where things go ([SA150 notes 2026](https://assets.publishing.service.gov.uk/media/6a9ea8a5df4246cf45e469e0/SA150_Notes_2026.pdf); [supplementary pages](https://www.gov.uk/government/publications/self-assessment-tax-return-sa100))

| Item | Where |
| --- | --- |
| Employment income, benefits, PAYE | SA102 Employment pages |
| Self-employment | SA103S or SA103F |
| UK property | SA105 |
| Foreign income; residence | SA106; SA109 |
| Taxed and untaxed UK interest | Income section: box 1 (taxed, net) and box 2 (untaxed, gross) |
| Dividends from UK companies | Income section: box 4, even if under £500 |
| UK pensions, annuities and State Pension | Income section: UK pensions, annuities and other state benefits |
| Pension contributions (relief at source, gross, employer scheme, overseas scheme) | Tax reliefs section: boxes 1 to 4 |
| Gift Aid paid in the year, one-off gifts, carry-back | Tax reliefs section: box 5 onwards |
| High Income Child Benefit Charge | "Fill in this section if during the 2025 to 2026 tax year: your adjusted net income was over £60,000" and higher than your partner's |
| Winter Fuel Payment or Pension Age Winter Heating Payment charge | WFP and PAWHP charge section: "If your total income was over £35,000" and you got none of the qualifying benefits (new for 2025/26) |
| Marriage Allowance | Marriage Allowance section, with the partner's details |
| Annual allowance charge, other reliefs | SA101 Additional information |

## Completion checklist ([Income Tax rates](https://www.gov.uk/income-tax-rates); [Finance Act 2026 s.4](https://www.legislation.gov.uk/ukpga/2026/11/section/4); [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account))

- [ ] Tax year confirmed. The 2025/26 return uses dividend rates of 8.75%, 33.75% and 39.35%; 2026/27 uses 10.75%, 35.75% and 39.35%.
- [ ] Residence confirmed; Scottish, non-resident and split-year cases referred.
- [ ] Registration by 5 October checked for first-time filers.
- [ ] Income split into non-savings, savings and dividends, and taxed in that order.
- [ ] Adjusted net income worked out; Personal Allowance taper applied above £100,000.
- [ ] Basic rate band extended for relief-at-source pensions and Gift Aid; higher rate relief claimed.
- [ ] Starting rate for savings and Personal Savings Allowance applied by band; savings at 20%, 40% or 45%, not the 2027/28 rates.
- [ ] £500 dividend allowance treated as a band, not a deduction.
- [ ] Marriage Allowance conditions checked on both partners.
- [ ] Child Benefit charge worked out for the higher-income partner if over £60,000.
- [ ] Winter Fuel Payment charge considered on the 2025/26 return.
- [ ] PAYE and tax deducted at source taken off; payments on account made taken off.
- [ ] Next year's payments on account worked out (the £1,000 and 80% tests); SA303 considered only with evidence.
- [ ] Filed by 31 January 2027 online, or by 31 October 2026 on paper; payment dates given to the client.
- [ ] MTD status checked for 2026/27 onwards.

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
