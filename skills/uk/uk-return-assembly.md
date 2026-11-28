---
name: uk-return-assembly
description: "Assemble a UK individual's Self Assessment reviewer package: choose SA100 supplementary pages, reconcile the component computations, apply the statutory income-tax order, and set the 2025-26 and 2026-27 filing and payment calendar. Includes the original six cases, with explicit holds where facts or year-specific instructions are missing."
version: "2.1"
type: filing-howto
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# UK Self Assessment return assembly

Assemble the SA100, its supplementary pages, the computation, reconciliations and payment calendar into one reviewer package.

## Scope

This Guide covers full-year UK-resident individuals whose England, Wales or Northern Ireland taxpayer status and allowance entitlement have been established. It includes sole traders with employment, UK property, gains, savings, dividends and pensions. Residence, Scottish taxpayer status and specialist positions have specific holds below; do not infer status solely from a present address.

Keep the years separate: **2025-26** is 6 April 2025 to 5 April 2026, filed on the “2026” forms; **2026-27** is 6 April 2026 to 5 April 2027. The ordinary online deadlines are respectively **31 January 2027** and **31 January 2028**, subject to the late-notice rules below ([HMRC forms](https://www.gov.uk/government/publications/self-assessment-tax-return-sa100); [TMA 1970 s.8](https://www.legislation.gov.uk/ukpga/1970/9/section/8)).

## Ask the client first

Read the intake, documents and previous working papers before asking for missing facts. Confirm:

- Return year; UTR; actual notice-to-file date; registration and filing history; residence/taxpayer-status decision; any HMRC Making Tax Digital letter.
- Every trade, accounting period and basis; turnover, expenses, assets and closing pools; VAT scheme and periods; CIS statements, deductions and refunds.
- P60/P45 for each job; payrolled benefits, P11D or equivalent, expenses, tips, bonuses and termination payments.
- UK property, disposals including crypto, foreign income/gains/remittances; interest and dividends outside ISAs; pensions, Gift Aid and pension relief method.
- Each partner's adjusted net income, Child Benefit entitlement and relationship weeks; Marriage Allowance; Winter Fuel Payment or Pension Age Winter Heating Payment.
- Student/postgraduate loan plan, repayment status and payroll deductions; prior SA302, HMRC statement, actual payments on account, credits and reduction claims.

Missing amounts are gaps, never zeroes. Continue unaffected work, identify each incomplete computation, and withhold filing until the reviewer resolves it. Do not omit an out-of-scope income source from a supposedly complete return.

## The method, step by step

### 1. Choose the pages

Use the return year's forms and notes. The following is a page-selection map, not a finding that every item creates a filing obligation ([HMRC supplementary pages](https://www.gov.uk/government/publications/self-assessment-tax-return-sa100)).

| Page | Subject and route |
| --- | --- |
| SA100 | Main return: `uk-income-tax-sa100` |
| SA101 | Additional information: less common income, deductions, reliefs and pension charges; specialist hold below |
| SA102 | Employment or directorship, where required; one page for each employment/directorship |
| SA103S / SA103F | Self-employment: `uk-self-employment-sa103` with `uk-bookkeeping` |
| SA104S / SA104F | Partnership income; specialist hold |
| SA105 | UK property: `uk-rental-sa105` |
| SA106 | Foreign income/gains; specialist hold, `uk-non-dom` |
| SA107 | Trust, settlement or deceased estate income; specialist hold |
| SA108 | Capital gains/losses: `uk-capital-gains-sa108`; crypto also `uk-crypto-tax` |
| SA109 | Residence/foreign-income-and-gains matters; specialist hold, `uk-statutory-residence-test` |
| SA110 | Results of a tax calculation on the supplementary tax-calculation pages |

For **2025-26**, short self-employment pages require turnover **less than £90,000**, including the full-year equivalent for a short trading period. Exactly £90,000 requires full pages. Full pages are also needed for the notes' accounting-period profit/loss adjustments (ended before 31 March 2026, not 12 months, or not ending in the tax year), adjustment income from changing accounting basis, Class 4 profit adjustments, or Managing Serious Defaulters participation. The short notes additionally direct a more complicated business to full pages. Establish the actual accounts and any cessation before choosing ([short notes, pp.1–3](https://assets.publishing.service.gov.uk/media/69ce15395cf899414a0bc69f/SA103S_Notes_2026.pdf); [full notes, p.1](https://assets.publishing.service.gov.uk/media/69c26565cfa346b9d4704b35/SA103F_Notes_2026.pdf)).

**2025-26 box map only.** These identify fields, not eligibility for allowances, loss relief or NIC exemptions. Keep the source form beside the worksheet; do not use this map to file 2026-27 ([SA103S form](https://assets.publishing.service.gov.uk/media/69c12ae013101e9908704a53/SA103S-2026.pdf); [SA103F form](https://assets.publishing.service.gov.uk/media/69c2635b13101e9908704b36/SA103F_2026.pdf)).

| Item | SA103S | SA103F | Official form |
| --- | --- | --- | --- |
| Turnover; other business income; trading income allowance | 9; 10; 10.1 | 15; 16; 16.1 | https://assets.publishing.service.gov.uk/media/69c12ae013101e9908704a53/SA103S-2026.pdf https://assets.publishing.service.gov.uk/media/69c2635b13101e9908704b36/SA103F_2026.pdf |
| Expense entries and total | 11–19, total 20 | 17–30, total 31; disallowable amounts separately 32–45, total 46 | same |
| Accounting net profit / loss | 21 / 22 | 47 / 48 | same |
| Annual Investment Allowance and capital-allowance fields | AIA 23; fields 23–25.2 | AIA 49; fields 49–56, total 57 | same |
| Balancing charges; goods/services for own use | 26; 27 | 59; 60 | same |
| Net business profit / loss for tax purposes | 28 / 32 | 64 / 65 | same |
| Total taxable profit / loss | 31 / 32 | 76 / 77; transition profit separate in 73.3, excluded from 76 | same |
| Traditional-accounting election | 8 | 10 | same |
| Voluntary Class 2; Class 4 exemption; Class 4 profit adjustment | 36; 37; no adjustment field | 100; 101; 102 | same |
| CIS deductions | 38 | 81 | same |

For **2025-26 employment**, use SA102 box 1 for that employment's P45/P60 pay and box 2 for UK tax taken off. Avoid counting previous jobs twice. Benefits use the P11D **or equivalent information**; do not assume employment expenses appear on a P11D. Benefits, payrolled-benefit adjustments, expenses and termination payments are held for specialist checking ([SA102 form](https://assets.publishing.service.gov.uk/media/69bd6a7a7e02b81c0d1c75ae/SA102-2026.pdf)).

### 2. Run the component Guides

1. Run `uk-vat-return` first where relevant and prepare a bridge to the income-tax records. Registration alone does not force every trader's income-tax figures to be VAT-exclusive: a VAT-registered **cash-basis** business may record receipts/payments inclusive or exclusive; if inclusive, net VAT payments to HMRC are expenses and net repayments are receipts. Keep one consistent method. Flat Rate Scheme income-tax treatment, partial exemption, irrecoverable VAT, VAT-invoice requirements and actual VAT filing dates are held below ([HMRC BIM72005](https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim72005)).
2. For an unregistered business, test both taxable turnover over £90,000 in the year ending at each month end and reasonable grounds to expect over £90,000 in the next 30 days alone. Overseas/non-established businesses and exceptions require the VAT Guide and specialist checking; no universal £90,000 safe harbour ([VATA 1994 Sch.1 para.1](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1)).
3. Run `uk-self-employment-sa103` and `uk-bookkeeping`: reconcile accounting profit to the tax-year profit, reliefs and adjustments; retain the asset/pool schedule. Cash basis is standard for eligible sole traders; traditional accounting is optional. Cash basis records receipts/payments, traditional accounting invoices/bills; basis changes and transitional adjustments need separate checking, not a blanket “no adjustments” assumption ([cash basis](https://www.gov.uk/simpler-income-tax-cash-basis)).
4. Prepare employment worksheets where applicable. **Property and gains. Run `uk-rental-sa105` and `uk-capital-gains-sa108` if they apply.** Carry validated outputs with their assumptions and credits; do not treat another Guide's unverified answer as established. Run `uk-income-tax-sa100`, `uk-national-insurance`, any applicable `uk-student-loan-repayment`, then `uk-payments-on-account`.

### 3. Assemble the computation

[ITA 2007 s.23](https://www.legislation.gov.uk/ukpga/2007/3/section/23) requires: **total income → eligible Step 2 reliefs → eligible Step 3 allowances → tax on each component → sum of that tax → eligible tax reductions → additional charges**. The result is Income Tax liability. Keep entitlement and claims for each relief separate; a pension contribution is not automatically a Step 2 deduction.

For **2025-26 and 2026-27**, [s.25](https://www.legislation.gov.uk/ukpga/2007/3/section/25) allocates reliefs/allowances to obtain the greatest tax reduction, subject to the statutory restrictions and sufficient income, with no double deduction. **Do not mandate non-savings-first allowance allocation.** The new priority restriction in Finance Act 2026 s.6(6) applies from 2027-28, not these years. Mixed-income optimisation outside the explicit examples is held below.

Keep ordinary non-savings income, savings and dividends separate. Under [s.16](https://www.legislation.gov.uk/ukpga/2007/3/section/16), savings/dividends occupy the highest slice, with dividends above savings. Special highest-slice income is held below.

**Take off tax already paid: PAYE from the SA102, tax taken off at source, Construction Industry Scheme deductions, and the payments on account already made for the year.** Use the actual credit classifications and adjustments below.

Then reconcile Class 4, any valid voluntary Class 2, student/postgraduate loan, CGT and other charges; subtract correctly classified source deductions and actual credited payments on account. Keep refunds already received, PAYE coding adjustments and CGT payments visible; do not deduct a credit twice. Reconcile the result to the HMRC statement rather than promising a cash refund from an arithmetic credit.

### 4. Record six reconciliations

| Check | Required working paper |
| --- | --- |
| Profit carried across | Trace each trade's tax-year profit to the computation. Separate losses, transition profits and specialist adjustments from ordinary taxable profit. |
| National Insurance | Reconcile the actual liable Class 4 profit, exemptions/adjustments and any Class 1 annual-maximum issue; do not copy accounting profit automatically. |
| Payments on account | Compare statutory charges, reductions/amendments, cash paid and allocations with the prior SA302 **and** current HMRC statement. A first filing alone is not an exemption. |
| VAT | Bridge turnover by tax period, timing, VAT accounting method, scheme and non-turnover supplies. A small difference still needs an explanation. |
| Student loan | Confirm the correct loan computation, repayment base/status/year, payroll credit and rounding; no automatic total-income fallback if a Guide is unavailable. |
| Accounting basis | Match the election, actual receipt/invoice timing and any basis-change adjustments to the SA103 fields. |

Record pass/fail/not applicable, the pound difference and the resolution. Compare the assembled computation line by line with HMRC's online calculation or the commercial software before submission. Disagreement may reflect an exclusion, adjustment or software limitation; resolve it rather than presuming a box is wrong. Filing and payment remain human actions.

After filing, retain the submission receipt, calculation and tax year overview. HMRC says documents cannot be printed until **72 hours** after submission; with commercial software, print the computation from that software, and the overview from HMRC ([SA302](https://www.gov.uk/sa302-tax-calculation)). For paper filing, SA110 records the calculation results; held or late-paper cases need a confirmed HMRC calculation/notification route, not an assumed promise of a bill before payment falls due.

## Rates, bands and thresholds

These are checks on established ordinary facts, not complete relief/eligibility decisions. Source sentences and read dates are recorded below. Do not carry a 2026-27 figure into 2025-26.

### Income Tax

These are the ordinary reference income ranges; allowance taper, actual entitlement and any valid band extensions must still be applied. The basic band is measured **after** allowances; the higher-rate taxable limit is not an extra full allowance. Read the conditions with each row.

| Item | 2025-26 (return due 31 January 2027) | 2026-27 (year in force) | Conditions and official source |
| --- | --- | --- | --- |
| Personal Allowance | £12,570 | £12,570 | Entitlement/claim required: https://www.legislation.gov.uk/ukpga/2007/3/section/35 |
| Taper | £1 for every £2 of adjusted net income above £100,000 | Same | Round the **remaining allowance** up to a whole pound: https://www.legislation.gov.uk/ukpga/2007/3/section/35 |
| Allowance nil at | £125,140 or more | £125,140 or more | Computed from the taper: https://www.gov.uk/income-tax-rates |
| Basic rate 20% | £12,571 to £50,270 | £12,571 to £50,270 | Reference ranges subject to the allowance/band conditions above: https://www.gov.uk/income-tax-rates/previous-tax-years https://www.gov.uk/income-tax-rates |
| Higher rate 40% | £50,271 to £125,140 | £50,271 to £125,140 | Same conditions: https://www.gov.uk/income-tax-rates/previous-tax-years https://www.gov.uk/income-tax-rates |
| Additional rate 45% | Over £125,140 | Over £125,140 | Same conditions: https://www.gov.uk/income-tax-rates/previous-tax-years https://www.gov.uk/income-tax-rates |
| Basic rate limit (band above the allowance) | £37,700 | £37,700 | Subject to valid extensions: https://www.legislation.gov.uk/ukpga/2007/3/section/10 |

### Savings and dividends

Nil-rated savings and dividends still occupy bands. The PSA test includes all income, including the nil-rated amounts; these are not deductions from total income.

| Item | 2025-26 | 2026-27 | Conditions and official source |
| --- | --- | --- | --- |
| Starting rate for savings band | Up to £5,000; only if other income is less than £17,570 | Same | The cutoff assumes the standard Personal Allowance; “other” excludes savings/dividends. Reduce the band £1 per £1 of other income above the allowance: https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free https://www.legislation.gov.uk/ukpga/2007/3/section/12 |
| Personal Savings Allowance | £1,000 basic rate, £500 higher rate, £0 additional rate | Same | Test total income including nil-rated interest/dividends: https://www.legislation.gov.uk/ukpga/2007/3/section/12B |
| Savings rates | 20%, 40%, 45% | 20%, 40%, 45% | After available nil bands: https://www.legislation.gov.uk/ukpga/2026/11/section/3 https://www.gov.uk/government/publications/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income |
| Dividend allowance | £500 | £500 | Nil-rate band after unused Personal Allowance: https://www.legislation.gov.uk/ukpga/2007/3/section/13A https://www.gov.uk/tax-on-dividends |
| Dividend ordinary rate | 8.75% | 10.75% | After allowance, to extent in ordinary-rate band: https://www.legislation.gov.uk/ukpga/2026/11/section/4 https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past |
| Dividend upper rate | 33.75% | 35.75% | Higher-band dividend income after allowance: https://www.legislation.gov.uk/ukpga/2026/11/section/4 https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past |
| Dividend additional rate | 39.35% | 39.35% | Additional-band dividend income after allowance: https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past |

### Self-employed National Insurance

| Item | 2025-26 | 2026-27 | Conditions and official source |
| --- | --- | --- | --- |
| Class 4 main rate, profits over £12,570 up to £50,270 | 6% | 6% | Established liable profits after adjustments/exemptions/any Class 1 maximum: https://www.legislation.gov.uk/ukpga/1992/4/section/15 https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions |
| Class 4 rate on profits over £50,270 | 2% | 2% | Same conditions: https://www.legislation.gov.uk/ukpga/1992/4/section/15 https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions |
| Small profits threshold: at or above it, Class 2 is treated as paid | £6,845 | £7,105 | Ordinary eligible self-employment weeks only, not a whole qualifying-year certificate: https://www.legislation.gov.uk/ukpga/1992/4/section/11 https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions |
| Voluntary Class 2, only below the threshold and only if the client chooses | £3.50 a week | £3.65 a week | Eligibility/weeks/payment timing must be established; specialist cases held below: https://www.legislation.gov.uk/ukpga/1992/4/section/11 https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions |

**Adjusted net income:** start with net income before Personal Allowances; deduct eligible gross Gift Aid and relief-at-source pensions, then add back any deducted trade-union/police-organisation relief as required by [ITA s.58](https://www.legislation.gov.uk/ukpga/2007/3/section/58). Do not deduct net-pay payroll pensions twice. For eligible relief-at-source contributions, net ÷ 0.8 = gross; qualifying Gift Aid likewise gross-ups by 1.25. Gross eligible contributions/gifts extend rate-band limits where the relevant conditions and claims apply ([FA 2004 s.192](https://www.legislation.gov.uk/ukpga/2004/12/section/192); [ITA s.414](https://www.legislation.gov.uk/ukpga/2007/3/section/414); [HMRC ANI](https://www.gov.uk/guidance/adjusted-net-income)).

**Child Benefit charge:** for both years, adjusted net income must exceed £60,000. Apply [ITEPA ss.681B–681C](https://www.legislation.gov.uk/ukpga/2003/1/section/681B) to the relevant entitlement/partner weeks; the higher-income partner is charged, or the recipient if incomes are equal. Percentage = (ANI − £60,000) ÷ £200, rounded down, capped at 100%; round the relevant benefit total and resulting charge down to whole pounds. The cap is reached at £80,000, not only above it ([s.681C](https://www.legislation.gov.uk/ukpga/2003/1/section/681C)). Changed relationships, third-party claims for a child living with the client and unknown partner facts are held below.

## Filing and payment

For a return that is required, a first-time filer or a previously registered person who did not need a 2024-25 return must tell HMRC by **5 October 2026** for 2025-26 ([HMRC deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)). Do not ignore an existing notice to file.

| Ordinary event, subject to exceptions below | 2025-26 return | 2026-27 return | Official source |
| --- | --- | --- | --- |
| Paper return received | 31 October 2026 | 31 October 2027 | https://www.legislation.gov.uk/ukpga/1970/9/section/8 |
| Electronic return | 31 January 2027 | 31 January 2028 | same |
| Balancing payment, after actual source deductions/credits and payments on account | 31 January 2027 | 31 January 2028 | https://www.legislation.gov.uk/ukpga/1970/9/section/59B |
| Balancing payment for 2025-26 and first payment on account for 2026-27 | 11:59pm on 31 January 2027 | Not applicable to this year | https://www.legislation.gov.uk/ukpga/1970/9/section/59A https://www.legislation.gov.uk/ukpga/1970/9/section/59B |
| Second payment on account for 2026-27 | 31 July 2027 | Not applicable to this year | https://www.legislation.gov.uk/ukpga/1970/9/section/59A |
| 2026-27 balance and first 2027-28 advance; second 2027-28 advance | Not applicable to this year | 31 January 2028; 31 July 2028 | https://www.legislation.gov.uk/ukpga/1970/9/section/59A https://www.legislation.gov.uk/ukpga/1970/9/section/59B |
| Ordinary amendment deadline | 31 January 2028 | 31 January 2029 | https://www.legislation.gov.uk/ukpga/1970/9/section/9ZA |

**Late notice to file:** under [TMA s.8](https://www.legislation.gov.uk/ukpga/1970/9/section/8), a notice after 31 July but by 31 October following the tax year gives three months for paper, while the electronic deadline stays 31 January. A notice after 31 October gives three months for either method. Under [s.59B](https://www.legislation.gov.uk/ukpga/1970/9/section/59B), the balance also gets three months only if the taxpayer gave the required s.7 notification within six months after the year and HMRC's notice came after 31 October; otherwise the ordinary balance date remains. Under [s.9ZA](https://www.legislation.gov.uk/ukpga/1970/9/section/9ZA), a post-31-October notice also changes the filing-date basis for the twelve-month amendment window. Obtain the actual notices; “registered late” alone does not settle these dates.

**Tax-code collection:** the bill must be strictly below £3,000, the client must already pay through PAYE, and the return must meet the paper 31 October or online 30 December cutoff. For 2025-26 the online cutoff is 30 December 2026; for 2026-27 it is 30 December 2027. A part payment cannot bring a bill originally at or above £3,000 within the limit. HMRC cannot collect if earnings/coding capacity fails its limits. Current Class 2 contributions cannot be collected this way. A no-PAYE sole trader cannot use this route; an eligible date alone is insufficient ([HMRC coding conditions and capacity](https://www.gov.uk/pay-self-assessment-tax-bill/through-your-tax-code)).

**Payments on account:** use `uk-payments-on-account`. The ordinary base is the previous year's relevant Income Tax/Class 4 liability after the correct source deductions/coding adjustments, excluding CGT, Class 2 and student/postgraduate loans. Each instalment is half that base (an odd penny goes on the second). None are due if the relevant amount is below £1,000 **or** more than 80% was paid outside Self Assessment; exactly £1,000 and exactly 80% do not pass those exclusions. For a relevant amount at least £1,000 with no other statutory exception: **At exactly 80% paid outside Self Assessment, they are still due.** Reductions, subsequent assessments and interest need the statutory calculation, not half of a cash balancing payment. A first filing can require both the entire balance and the next year's first advance ([TMA s.59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A); [HMRC SAM1100](https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam1100); [HMRC payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).

**MTD:** the entry tests use qualifying income, generally combined gross trade/property income, not profit or one trade alone: over £50,000 in 2024-25 → 6 April 2026; over £30,000 in 2025-26 → 6 April 2027; over £20,000 in 2026-27 → 6 April 2028. Eligibility, exemptions, annualisation, continuing obligations and software/update filing are held below; do not infer exemption from no HMRC letter ([HMRC entry tests](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax); [qualifying income](https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax)). The new penalty regime for a 6 April 2026 entrant applies to the 2026-27 return deadline of 31 January 2028; the 2025-26 deadline of 31 January 2027 stays under the current regime ([HMRC MTD penalties](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax)).

**Corrections:** a return may ordinarily be amended within twelve months of its statutory filing date. HMRC's online service requires a 72-hour wait; MTD amendments use compatible software. Late-notice dates, out-of-window changes, separate claims and resulting bills/refunds require checking ([TMA s.9ZA](https://www.legislation.gov.uk/ukpga/1970/9/section/9ZA); [HMRC corrections](https://www.gov.uk/self-assessment-tax-returns/corrections)).

**Interest and records:** ordinary late-payment interest is 8% from 24 November 2026; the earlier 7.75% applies from 9 January through 23 November 2026. The formula is Bank Rate plus 4% from 6 April 2025, but use HMRC's effective dates for the actual period, never predict a future charge from today's rate ([HMRC interest](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates)). A self-employed client ordinarily keeps records at least five years after the relevant January submission deadline, longer where the statutory enquiry window/enquiry requires; late-return and specialist retention cases need checking ([TMA s.12B](https://www.legislation.gov.uk/ukpga/1970/9/section/12B); [HMRC records](https://www.gov.uk/self-employed-records/how-long-to-keep-your-records)). Actual penalties/interest, failure-to-notify, repayment interest, defences, appeals and Time to Pay are held below, except the explicitly conditional Case E.

## Worked cases

All original inputs and years are retained. These are conditional illustrations for England, with established allowance entitlement, ordinary taxable income and no unstated reliefs, source deductions or charges. Calculations retain pence for reconciliation; actual return rounding must be checked. Class 2 treatment assumes ordinary eligible self-employment weeks; Class 4 assumes liability and no adjustment unless stated.

### Case A: employee and sole trader, 2026-27

Salary **£30,000**, P60 PAYE **£3,486**, sole-trade taxable profit **£25,000**, no other income. Use the return year's fields; the old “SA103S box 31” reference is a 2025-26 field, not certified for 2026-27.

Income £55,000 less allowance £12,570 = taxable £42,430. Income Tax = £37,700 × 20% + £4,730 × 40% = **£9,432**. Standalone Class 4 = (£25,000 − £12,570) × 6% = **£745.80**. Assuming the employment/Class 1 annual-maximum check leaves that amount unchanged, balance = £9,432 − £3,486 + £745.80 = **£6,691.80**; each next-year advance **£3,345.90**, subject to the statutory tests and no reduction. The profit exceeds the £7,105 Class 2 threshold; eligible weeks are treated as paid ([rates](https://www.gov.uk/income-tax-rates); [NIC](https://www.legislation.gov.uk/ukpga/1992/4/section/15); [advances](https://www.legislation.gov.uk/ukpga/1970/9/section/59A)).

The original Plan 2 calculation **9% × (£55,000 − £29,385) = £2,305.35** is retained as **unrounded arithmetic only**, not an amount certified for the return. The plan threshold is not a complete repayment computation. Payroll credit, repayment status, relevant income and whole-pound rounding must be established. **Student-loan filing result on hold. Check this point with one of our partner accountants.**

```oa-check
name: Case A 2026-27 conditional assembly before student loan
inputs:
  salary: 30000
  paye: 3486
  profit: 25000
  personal_allowance: 12570
  basic_band: 37700
steps:
  - taxable: salary + profit - personal_allowance
  - income_tax: pct(basic_band, 20) + pct(taxable - basic_band, 40)
  - class4: pct(profit - personal_allowance, 6)
  - balance: income_tax - paye + class4
  - each_poa: balance / 2
expected:
  income_tax: 9432
  class4: 745.80
  balance: 6691.80
  each_poa: 3345.90
```

### Case B: allowance taper and pension, 2026-27

Sole-trade profit **£110,000**, nothing else. ANI £110,000 gives allowance **£7,570**; taxable £102,430; tax £7,540 + £64,730 × 40% = **£33,432**. With an **eligible £8,000 net / £10,000 gross** relief-at-source contribution, valid relief claim and no other ANI adjustments, ANI becomes £100,000, allowance £12,570 and basic band £47,700. Tax = £47,700 × 20% + £49,730 × 40% = **£29,432**, a **£4,000** reduction, separate from the provider's £2,000 basic relief. The personal contribution does not reduce the trade's Class 4 profit. Contribution eligibility/annual allowance is not established by this arithmetic ([ITA s.35](https://www.legislation.gov.uk/ukpga/2007/3/section/35); [FA s.192](https://www.legislation.gov.uk/ukpga/2004/12/section/192)).

### Case C: savings and dividends, both years

Pension **£40,000**, interest **£2,000**, dividends **£6,000**; total **£48,000**. Assuming no other income/reliefs, allowance to pension gives £27,430 × 20% = **£5,486**. No savings starting band; £1,000 PSA, then £1,000 × 20% = **£200**. Savings occupy £2,000 of the basic band, leaving **£8,270** for dividends, correcting the old £7,770 figure. Of £6,000 dividends, £500 is nil-rated and £5,500 taxed: **£591.25** at 10.75% for 2026-27, total **£6,277.25**; **£481.25** at 8.75% for 2025-26, total **£6,167.25**. Difference **£110** ([savings](https://www.legislation.gov.uk/ukpga/2007/3/section/12B); [dividends](https://www.legislation.gov.uk/ukpga/2026/11/section/4)).

### Case D: first return, 2025-26

New sole trader: taxable profit **£30,000**, no other income, registered by **5 October 2026**, no prior payments on account, ordinary timely notice. Tax **£3,486**; Class 4 **£1,045.80**; balance **£4,531.80**. Profit exceeds £6,845; eligible Class 2 weeks treated as paid. Each 2026-27 advance **£2,265.90**. Pay **£6,797.70** on **31 January 2027**, and **£2,265.90** on **31 July 2027**. With no PAYE income there is no coding-out route, even if a balance were under £3,000 ([prior-year rates](https://www.gov.uk/income-tax-rates/previous-tax-years); [NIC](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions); [advances](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).

### Case E: Case D filed and paid late

Keep the original facts: online return filed **15 August 2027**, **£4,531.80** balancing tax paid that day. A conditional ordinary-regime illustration additionally assumes a valid HMRC daily-penalty decision/notice covering **90 days**, no reasonable excuse/special reduction, and the full balance unpaid at both late-payment triggers. Filing: **£100 + £900 + max(5% × £4,531.80, £300) = £1,300**; 5% is **£226.59**. Payment: **two × £226.59 = £453.18**, plus period-specific interest. This does **not** quantify unpaid 2026-27 advances, allocation effects or their interest. Original facts do not establish those assumptions or the total actual bill. **Actual Case E charge on hold. Check this point with one of our partner accountants.** ([FA 2009 Sch.55 paras.3–5](https://www.legislation.gov.uk/ukpga/2009/10/schedule/55); [HMRC payment penalties](https://www.gov.uk/self-assessment-tax-returns/penalties)).

```oa-check
name: Cases D and E conditional 2025-26 illustration, not the actual late bill
inputs:
  profit: 30000
  personal_allowance: 12570
  noticed_daily_days: 90
steps:
  - income_tax: pct(profit - personal_allowance, 20)
  - class4: pct(profit - personal_allowance, 6)
  - balance: income_tax + class4
  - each_poa: balance / 2
  - due_31_jan_2027: balance + each_poa
  - daily_penalty: min(noticed_daily_days * 10, 900)
  - six_month_penalty: max(pct(balance, 5), 300)
  - filing_penalties: 100 + daily_penalty + six_month_penalty
  - payment_penalties: round(pct(balance, 5), 2) * 2
expected:
  income_tax: 3486
  class4: 1045.80
  balance: 4531.80
  each_poa: 2265.90
  due_31_jan_2027: 6797.70
  filing_penalties: 1300
  payment_penalties: 453.18
```

### Case F: Child Benefit charge, 2026-27

ANI **£70,000**, Child Benefit **£2,000**, partner's ANI lower. Assuming the entire £2,000 relates to qualifying entitlement/partner weeks under s.681B, percentage = (£70,000 − £60,000) ÷ £200 = **50%**; charge **£1,000**, added at Step 7. A household cash receipt alone does not establish the qualifying amount ([ITEPA s.681B](https://www.legislation.gov.uk/ukpga/2003/1/section/681B); [s.681C](https://www.legislation.gov.uk/ukpga/2003/1/section/681C)).

## When to refuse or refer

These are **non-usable holds**, not completed tax answers. Retain the relevant inputs and missing conditions in the brief:

- **Residence/status and specialist income:** Scotland or uncertain UK/Welsh status, non-residence, split years, dual residence, foreign income/gains, the four-year FIG regime, old remittances, partnerships, trusts, estates and companies. Use the original routing Guides; **Check this point with one of our partner accountants.**
- **Reliefs and assets:** Marriage Allowance, trading/property allowances, loss claims/caps, transition profits, non-standard accounting periods, mixed-income allowance optimisation, capital allowances/AIA/pools/private use and missing opening balances. The old £1,800 MacBook AIA example has no established asset/basis/eligibility facts; preserve £1,800 without asserting a deduction. Missing pools do not justify relieving only this year's purchases. **Check this point with one of our partner accountants.**
- **Employment, NIC and benefits:** noncash/payrolled benefits, employment expenses, termination payments, pension annual allowance, combined Class 1/Class 4 limits, special occupations/ages, voluntary NIC eligibility and payment timing. **Check this point with one of our partner accountants.**
- **Student loans:** all plans and postgraduate loans, start/stop status, relevant-income exclusions, unearned-income boundary, payroll deductions, multiple plans, rounding and SLC refunds. Original Case A and the older Plan 1/2/4/5/Postgraduate threshold topics remain here; there is no fallback calculation from generic total income. **Check this point with one of our partner accountants.**
- **Family charges:** third-party Child Benefit, changing partners/weeks or unknown partner ANI; Winter Fuel Payment/Pension Age Winter Heating Payment and the old £35,000 test. No liability inferred from the threshold alone. **Check this point with one of our partner accountants.**
- **VAT, MTD and submission:** Flat Rate Scheme income-tax bridge, VAT invoice/return/payment timing and exceptions, MTD qualifying income/exemptions/continuing obligations, quarterly updates and software, 2026-27 form boxes, late paper HMRC calculation, provisional figures and amendments, payment method/reference/capacity, penalties, interest, failure-to-notify, repayments, enquiries and appeals. Preserve records and actual notices; no filing from unconfirmed boxes or an incomplete penalty regime. **Check this point with one of our partner accountants.**
- **Other years:** the earliest 2024-25 applicability statement and all 2027-28 savings/property rate and allocation questions require their own year-specific proof. **Check this point with one of our partner accountants.**

Two older expense illustrations can still be reconciled conditionally: an eligible 2025-26 car/goods vehicle with **8,000 business miles × 45p = £3,600**, no prior allowance/cost claim and the continuing mileage choice established; and eligible home working of **101+ hours in a month = £26**. These are not proof of the client's eligibility. The wider mileage/home methods remain in `uk-self-employment-sa103` and `uk-bookkeeping`; do not reuse the old £150,000 cash-basis limit or compulsory £179.40 Class 2 example as current instructions ([HMRC simplified expenses and conditions](https://www.gov.uk/simpler-income-tax-simplified-expenses/print)).

## Completion checklist

Give the qualified reviewer the complete package, identifying every hold:

1. **Master workbook** (`[client_slug]_[tax-year]_uk_master.xlsx`) named for the actual client and year: Cover; VAT if relevant; SA103; SA102/SA105/SA108 as applicable; SA100 computation; Capital Allowances and Expense Detail; NIC; Student Loan if relevant; Payments on Account; Cross-Check Summary. Link cells, check formulas and rounding, and reconcile every figure with the approved computation. Never invent a zero to complete a sheet.
2. **Reviewer brief** (`reviewer_brief.md`): year and pages, income components, each tax/charge, source deductions and actual payments, balance/credit, next advances, all component workings, six reconciliations, software/HMRC comparison, each tax position with official source and operative conditions, missing evidence and specific holds.
3. **Client action list** (`client_action_list.md`): human review/approval, actual submission method, receipt, payment dates/amounts/references, VAT and MTD obligations where established, record retention, carry-forward pools and next-year planning. Filing, declarations and payment are not performed by this Guide.

Continue all authorised preparation without repeated pacing questions. Deliver complete parts and label missing/partial parts; no claim that an unresolved package is ready to file. Save in the user's authorised output location and link the actual files; do not presume a particular operating system or a `present_files` tool.

## Sources

Completed exact official reads from the existing UK SA100, SA103, NIC, VAT, bookkeeping and payments-on-account proofs were checked for the same operative periods and conditions on **27 November 2026**. They are reused below rather than represented as fresh reads. Fresh reads cover the page/form map, s.23, s.25 and commencement, s.9ZA, SA302 and correction workflow. A download or live URL alone was not treated as proof.

| Official source and part used | URL | Read date / reuse |
| --- | --- | --- |
| Read for self assessment tax return sa100 | https://www.gov.uk/government/publications/self-assessment-tax-return-sa100 | 2026-11-27 fresh read |
| Read for Ordinary and late-notice filing deadlines | https://www.legislation.gov.uk/ukpga/1970/9/section/8 | 2026-11-26 completed read reused |
| Read for 2025-26 official field map/notes: SA103S_Notes_2026.pdf | https://assets.publishing.service.gov.uk/media/69ce15395cf899414a0bc69f/SA103S_Notes_2026.pdf | 2026-11-27 fresh read |
| Read for 2025-26 official field map/notes: SA103F_Notes_2026.pdf | https://assets.publishing.service.gov.uk/media/69c26565cfa346b9d4704b35/SA103F_Notes_2026.pdf | 2026-11-27 fresh read |
| Read for 2025-26 official field map/notes: SA103S-2026.pdf | https://assets.publishing.service.gov.uk/media/69c12ae013101e9908704a53/SA103S-2026.pdf | 2026-11-27 fresh read |
| Read for 2025-26 official field map/notes: SA103F_2026.pdf | https://assets.publishing.service.gov.uk/media/69c2635b13101e9908704b36/SA103F_2026.pdf | 2026-11-27 fresh read |
| Read for 2025-26 official field map/notes: SA102-2026.pdf | https://assets.publishing.service.gov.uk/media/69bd6a7a7e02b81c0d1c75ae/SA102-2026.pdf | 2026-11-27 fresh read |
| Read for bim72005 | https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim72005 | 2026-11-26 completed read reused |
| Read for VAT rolling-month and forward-30-day registration tests | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1 | 2026-11-22 completed read reused |
| Read for simpler income tax cash basis | https://www.gov.uk/simpler-income-tax-cash-basis | 2026-11-26 completed read reused |
| Read for Seven-step Income Tax computation | https://www.legislation.gov.uk/ukpga/2007/3/section/23 | 2026-11-27 fresh read |
| Read for Allowance allocation, restrictions and sufficient income | https://www.legislation.gov.uk/ukpga/2007/3/section/25 | 2026-11-27 fresh read |
| Read for Savings/dividend ordering | https://www.legislation.gov.uk/ukpga/2007/3/section/16 | 2026-11-26 completed read reused |
| Read for sa302 tax calculation | https://www.gov.uk/sa302-tax-calculation | 2026-11-27 fresh read |
| Read for Personal Allowance entitlement/taper/rounding | https://www.legislation.gov.uk/ukpga/2007/3/section/35 | 2026-11-26 completed read reused |
| Read for previous tax years | https://www.gov.uk/income-tax-rates/previous-tax-years | 2026-11-26 completed read reused |
| Read for income tax rates | https://www.gov.uk/income-tax-rates | 2026-11-26 completed read reused |
| Read for Basic and higher taxable rate limits | https://www.legislation.gov.uk/ukpga/2007/3/section/10 | 2026-11-26 completed read reused |
| Read for how much is tax free | https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free | 2026-11-26 completed read reused |
| Read for Savings starting band | https://www.legislation.gov.uk/ukpga/2007/3/section/12 | 2026-11-26 completed read reused |
| Read for Personal Savings Allowance and rate-band test | https://www.legislation.gov.uk/ukpga/2007/3/section/12B | 2026-11-26 completed read reused |
| Read for 2026-27 savings rates | https://www.legislation.gov.uk/ukpga/2026/11/section/3 | 2026-11-26 completed read reused |
| Read for income tax changes to tax rates for property savings and dividend income | https://www.gov.uk/government/publications/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income | 2026-11-26 completed read reused |
| Read for Dividend nil-rate band | https://www.legislation.gov.uk/ukpga/2007/3/section/13A | 2026-11-26 completed read reused |
| Read for tax on dividends | https://www.gov.uk/tax-on-dividends | 2026-11-26 completed read reused |
| Read for 2026-27 dividend rate change and commencement | https://www.legislation.gov.uk/ukpga/2026/11/section/4 | 2026-11-26 completed read reused |
| Read for income tax rates and allowances current and past | https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past | 2026-11-26 completed read reused |
| Read for Class 4 liable profits and rates | https://www.legislation.gov.uk/ukpga/1992/4/section/15 | 2026-11-26 completed read reused |
| Read for rates and allowances national insurance contributions | https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions | 2026-11-26 completed read reused |
| Read for Class 2 ordinary eligible weeks | https://www.legislation.gov.uk/ukpga/1992/4/section/11 | 2026-11-26 completed read reused |
| Read for ANI adjustments and add-back | https://www.legislation.gov.uk/ukpga/2007/3/section/58 | 2026-11-26 completed read reused |
| Read for Relief-at-source gross-up and band extension | https://www.legislation.gov.uk/ukpga/2004/12/section/192 | 2026-11-26 completed read reused |
| Read for Gift Aid band extension | https://www.legislation.gov.uk/ukpga/2007/3/section/414 | 2026-11-26 completed read reused |
| Read for adjusted net income | https://www.gov.uk/guidance/adjusted-net-income | 2026-11-26 completed read reused |
| Read for Child Benefit relevant entitlement/partner weeks | https://www.legislation.gov.uk/ukpga/2003/1/section/681B | 2026-11-26 completed read reused |
| Read for Child Benefit percentage/cap/rounding | https://www.legislation.gov.uk/ukpga/2003/1/section/681C | 2026-11-26 completed read reused |
| Read for deadlines | https://www.gov.uk/self-assessment-tax-returns/deadlines | 2026-11-26 completed read reused |
| Read for Balance and late-notice payment conditions | https://www.legislation.gov.uk/ukpga/1970/9/section/59B | 2026-11-26 completed read reused |
| Read for Relevant advance base, dates, source deductions and thresholds | https://www.legislation.gov.uk/ukpga/1970/9/section/59A | 2026-11-26 completed read reused |
| Read for Amendment window and late-notice filing date | https://www.legislation.gov.uk/ukpga/1970/9/section/9ZA | 2026-11-27 fresh read |
| Read for through your tax code | https://www.gov.uk/pay-self-assessment-tax-bill/through-your-tax-code | 2026-11-27 fresh read |
| Read for sam1100 | https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam1100 | 2026-11-26 completed read reused |
| Read for payments on account | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-11-26 completed read reused |
| Read for find out if and when you need to use making tax digital for income tax | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax | 2026-11-26 completed read reused |
| Read for work out your qualifying income for making tax digital for income tax | https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax | 2026-11-26 completed read reused |
| Read for penalties for making tax digital for income tax | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax | 2026-11-26 completed read reused |
| Read for corrections | https://www.gov.uk/self-assessment-tax-returns/corrections | 2026-11-27 fresh read |
| Read for rates and allowances hmrc interest rates | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-11-22 ordinary-rate read; 2026-11-26 basis read; reused |
| Read for Records and extended enquiry retention | https://www.legislation.gov.uk/ukpga/1970/9/section/12B | 2026-11-26 completed read reused |
| Read for how long to keep your records | https://www.gov.uk/self-employed-records/how-long-to-keep-your-records | 2026-11-26 completed read reused |
| Read for penalties | https://www.gov.uk/self-assessment-tax-returns/penalties | 2026-11-26 completed read reused |
| Read for print | https://www.gov.uk/simpler-income-tax-simplified-expenses/print | 2026-11-26 completed read reused |

| Read for Case E ordinary filing penalty illustration, paras.3–5 only | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 | 2026-11-26 completed exact paragraphs read reused |

Not yet confirmed: the specifically enumerated specialist, form, student-loan and actual-charge outcomes under “When to refuse or refer” are non-usable holds. No unconfirmed outcome may be used to file, pay, amend or claim relief.
