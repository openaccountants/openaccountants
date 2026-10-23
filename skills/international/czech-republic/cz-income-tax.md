---
name: cz-income-tax
description: "Czech personal income tax for the self-employed (OSVČ), tax year 2026. Covers business and professional income under § 7 of the Income Taxes Act, the expense lump sums (80%, 60%, 40% and 30% of income, capped at CZK 1,600,000, 1,200,000, 800,000 and 600,000), actual expenses and tax records, the 15% and 23% rates with the 2026 threshold of CZK 1,762,812, credits and the child tax benefit, losses, tax advances (zálohy), the flat-rate regime (paušální daň) with its three bands and 2026 monthly payments, and the return deadlines for 2026. Trigger on: OSVČ, živnostník, DPFO, daňové přiznání, výdajové paušály, výdaje procentem z příjmů, paušální daň, paušální režim, zálohy na daň, Czech freelancer tax, self-employed tax Czech Republic. Out of scope: employees and non-business income (cz-employee-income-tax), social and health insurance (cz-social-health), non-residents and treaties (cz-cross-border), companies (cz-corporate-income-tax), VAT (cz-vat-return)."
jurisdiction: CZ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Czech Republic: income tax for the self-employed (OSVČ) (2026) v0.1

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team. No accountant has reviewed this skill yet. Every figure comes from the Income Taxes Act as published in e-Sbírka (version in force 1 August to 31 December 2026), the Tax Code, government regulations, MPSV and the Financial Administration, all read on 23 October 2026. It prepares working papers. It is not authority to file or pay.

This skill covers individuals with income from self-employment under § 7 of Act No. 586/1992 Coll. on Income Taxes ("ITA"): trades, farming, licensed professions, independent professions, royalties and letting of business property. It links to the other skills in the pack rather than repeating them:

- Employees, rental, capital and other non-business income, and the full rules on credits and § 15 deductions: [cz-employee-income-tax](cz-employee-income-tax.md).
- Social and health insurance of the self-employed, including the annual overviews (přehledy): [cz-social-health](cz-social-health.md).
- Residence, non-residents, treaties and withholding: [cz-cross-border](cz-cross-border.md).
- VAT registration (which ends the flat-rate regime): [cz-vat-return](cz-vat-return.md).
- Overview: [cz-tax-overview](cz-tax-overview.md).

Tax year: the calendar year. Currency: Czech koruna (CZK). Authority: the Financial Administration (Finanční správa).

## Who this applies to

- **Self-employed individuals (OSVČ)** with income from self-employment under ITA § 7(1) and (2):
  - farming, forestry and water management (§ 7(1)(a));
  - trades under a trade licence (živnost) (§ 7(1)(b));
  - other business that needs a business authorisation, such as licensed professions (§ 7(1)(c));
  - a partner's share of profit in a v.o.s. or a general partner's share in a k.s. (§ 7(1)(d));
  - royalties and use of industrial property and copyright (§ 7(2)(a)), letting of property held in the business (§ 7(2)(b)), and independent professions (§ 7(2)(c)).
- **Residents** are taxed on worldwide income; **non-residents** on Czech-source income only (ITA § 2). The residence tests are in [cz-cross-border](cz-cross-border.md).
- **Flat-rate regime (paušální režim).** A self-employed person who joins it pays one monthly amount covering income tax, pension insurance and health insurance, and files no return while the conditions hold (ITA § 2a, § 7a, § 38lh, § 38lk). The rules are below.
- **Out of scope.** Employment income (§ 6) and rental, capital and other income outside a business (§§ 8 to 10): [cz-employee-income-tax](cz-employee-income-tax.md). A person with both kinds of income files one return with a partial base for each.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Rate on the tax base up to 36 times the average wage | 15% | 2026 | [ITA § 16(1)(a)](https://e-sbirka.gov.cz/sb/1992/586/2026-08-01) |
| Rate on the tax base above 36 times the average wage | 23% | 2026 | ITA § 16(1)(b) |
| Average wage for tax purposes (ITA § 21g(2)) | CZK 48,967: general assessment base for 2024 of CZK 46,278 times coefficient 1.0581, rounded up | 2026 | [Government Regulation 365/2025 § 1](https://e-sbirka.gov.cz/sb/2025/365); Act 589/1992 § 23b(4) |
| 23% threshold (36 × 48,967) | CZK 1,762,812 | 2026 | computed from the row above |
| Expense lump sum: farming, forestry, water management and craft trades (řemeslné živnosti) | 80% of income, at most CZK 1,600,000 | 2026 | ITA § 7(7)(a) |
| Expense lump sum: other trades | 60% of income, at most CZK 1,200,000 | 2026 | ITA § 7(7)(b) |
| Expense lump sum: letting of property held in the business | 30% of income, at most CZK 600,000 | 2026 | ITA § 7(7)(c) |
| Expense lump sum: other self-employment income (licensed and independent professions, royalties) | 40% of income, at most CZK 800,000 | 2026 | ITA § 7(7)(d) |
| Basic taxpayer credit | CZK 30,840 a year | 2026 | ITA § 35ba(1)(a) |
| Spouse credit | CZK 24,840, only with a child under 3 in the household and the spouse's own income at most CZK 68,000 | 2026 | ITA § 35bb |
| Child tax benefit, first, second, third and further child | CZK 15,204; CZK 22,320; CZK 27,840 a year | 2026 | ITA § 35c(1) |
| Income needed for a tax bonus | § 6 or § 7 income of at least 6 times the minimum wage: CZK 134,400 | 2026 | ITA § 35c(4), § 21g(1); [MPSV, minimum wage](https://www.mpsv.cz/minimalni-mzda) (CZK 22,400 a month) |
| Student credit | None: § 35ba(1) lists no student credit for 2026 | 2026 | ITA § 35ba(1) |
| Advances: none due | Last known tax liability up to CZK 30,000 | 2026 | ITA § 38a(2)(a) |
| Advances: two a year | 40% of the last known tax each, if it was over CZK 30,000 and up to CZK 150,000 | 2026 | ITA § 38a(3) |
| Advances: four a year | 25% of the last known tax each, if it was over CZK 150,000 | 2026 | ITA § 38a(4) |
| Flat-rate regime, band I: income limit in the previous year | CZK 1,000,000 from any activity; CZK 1,500,000 if at least 75% is 80% or 60% lump-sum income; CZK 2,000,000 if at least 75% is 80% lump-sum income | 2026 | ITA § 2a(5)(a) |
| Flat-rate regime, band II: income limit | CZK 1,500,000 from any activity; CZK 2,000,000 if at least 75% is 80% or 60% lump-sum income | 2026 | ITA § 2a(5)(b) |
| Flat-rate regime, band III: income limit | CZK 2,000,000 from any activity | 2026 | ITA § 2a(5)(c) |
| Band I monthly payment | CZK 9,162: tax CZK 100; pension insurance CZK 5,756 (29.2% of the minimum base of 35% of the average wage, raised by 15%); health insurance CZK 3,306 (13.5% of 50% of the average wage). Each is rounded up to whole CZK. Act 90/2026 cut the minimum pension base for 2026 from 40% to 35% of the average wage from 1 July 2026, and for people in the flat-rate regime it applies from 1 January 2026, so the payment fell from CZK 9,984 | 2026 | ITA § 38lk(7)(a); [Act 589/1992 § 14(3)(a), (5)](https://e-sbirka.gov.cz/sb/1992/589/2026-07-01); [Act 90/2026 Art. II(4)](https://e-sbirka.gov.cz/sb/2026/90); [Act 592/1992 § 3a(2), (5), § 8a](https://e-sbirka.gov.cz/sb/1992/592); [Finanční správa, paušální daň 2025 and 2026](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pausalni-dan/informace-k-institutu-pausalni-dane-pro-rok-2025) |
| Band II monthly payment | CZK 16,745: tax CZK 4,963, pension insurance CZK 8,191 (29.2% of CZK 28,050), health insurance CZK 3,591 (13.5% of CZK 319,200 / 12) | 2026 | ITA § 38lk(7)(b); Act 589/1992 § 14(3)(b); Act 592/1992 § 3a(5)(b); Finanční správa, same page |
| Band III monthly payment | CZK 27,139: tax CZK 9,320, pension insurance CZK 12,527 (29.2% of CZK 42,900), health insurance CZK 5,292 (13.5% of CZK 470,400 / 12) | 2026 | ITA § 38lk(7)(c); Act 589/1992 § 14(3)(c); Act 592/1992 § 3a(5)(c); Finanční správa, same page |
| Late payment interest | CNB repo rate on the first day of the calendar half-year in which each day of interest falls, plus 8 points: 11.50% a year for days from 1 January to 30 June 2026, 11.75% for days from 1 July to 31 December 2026 | 2026 | [Tax Code § 251a(5), § 252(4)](https://e-sbirka.gov.cz/sb/2009/280/2026-01-01); [Government Regulation 351/2013 § 2(1)](https://e-sbirka.gov.cz/sb/2013/351); [CNB repo history](https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt) |

The tax is worked out on the base after deductions, rounded down to whole hundreds of CZK, as the sum of each slice times its rate (ITA § 16(2)). The tax is then rounded up to whole CZK, and each advance up to whole hundreds of CZK (Tax Code § 146(1), (2)).

## The taxable base

**Partial base from self-employment (ITA § 7(3)).** Income under § 7(1) and (2) less the expenses spent to earn, secure and keep it. A partner's share of profit in a v.o.s. or k.s. is not reduced by expenses (§ 7(3)). The partner instead takes their share of the partnership's base or loss (§ 7(4), (5)). The base is worked out under §§ 23 to 33.

**Method 1: expense lump sum (výdaje procentem z příjmů, § 7(7)).** Instead of proving expenses, the taxpayer deducts a fixed share of income:

- 80% of income from farming, forestry, water management and craft trades, at most CZK 1,600,000;
- 60% of income from other trades, at most CZK 1,200,000;
- 30% of income from letting property held in the business, at most CZK 600,000;
- 40% of other self-employment income (licensed and independent professions, royalties), at most CZK 800,000.

Rules that follow from it:

- The lump sum covers every expense of the self-employment (§ 7(8)). Nothing is deducted on top. Social and health insurance the self-employed person pays for themselves is not deductible under either method (§ 25(1)(g)).
- The choice cannot be changed back for that year once made (§ 7(7)).
- The taxpayer must keep records of income and of receivables (§ 7(8)).
- Income means the income the person would have if they did not keep accounts, so cash received (§ 7(8)).
- A person with activities in different lump-sum groups applies each percentage and cap to the income of that activity.
- The lump sum cannot exceed income, so it cannot create a tax loss.

**Method 2: actual expenses.** The taxpayer deducts expenses actually incurred (§ 24) and keeps tax records (daňová evidence) of income, expenses, assets and debts (§ 7b), or full accounts. Tax depreciation of business assets is in §§ 26 to 33. Expenses listed in § 25 are never deductible.

**Switching methods.** Moving from actual expenses to the lump sum, or into the flat-rate regime, means adjusting the base of the last year on actual expenses. Unpaid receivables are added and unpaid debts deducted (§ 23(8)). The adjustment is made by a supplementary return by the deadline for the year in which the method changed.

**Losses (§ 34(1)).** A tax loss from actual expenses can be deducted from the base of the 5 following years, or from the 2 preceding years (carry back up to CZK 30,000,000 in total). For an individual, a loss can only be set against the partial bases under §§ 7 to 10, not against employment income. A person with a tax loss must file even below the CZK 50,000 income threshold (§ 38g(1)).

**Deductions from the base (§ 15).** Contributions to tax-supported retirement savings products and long-term care insurance (up to CZK 48,000 a year in total, § 15(6)), housing loan interest (up to CZK 150,000 a household, or CZK 300,000 for housing acquired before 1 January 2021 under Act 386/2020 Art. IV(3)) and donations (over 2% of the base or at least CZK 1,000, at most 15%). They come off the total base after the partial bases are added. Detail: [cz-employee-income-tax](cz-employee-income-tax.md).

**Credits and the child tax benefit (§§ 35ba to 35c).** They come off the tax. Credits come first, then the child benefit. Any child benefit above the tax is paid as a tax bonus of at least CZK 100. The bonus needs § 6 or § 7 income (gross income, not base) of at least CZK 134,400 in 2026 (§ 35c(3), (4)). The full rules are in [cz-employee-income-tax](cz-employee-income-tax.md). They apply in the same way to the self-employed, whatever expense method they use.

**Flat-rate regime (paušální daň).** A person in the regime pays a fixed monthly amount. No base is computed while the conditions below hold.

- **Who can join (§ 2a(1)).** On 1 January of the year, the person must meet all of these:
  - be self-employed for pension and health insurance, and not exempt from health insurance for a long stay abroad;
  - not be a VAT payer or required to register for VAT (registration as an identified person is allowed);
  - not be a partner in a v.o.s. or a general partner in a k.s.;
  - not be in insolvency proceedings;
  - have no employment at that date, other than income taxed by final withholding.

  They must also have stayed within the band's income limit in the previous year, and notify the tax office.
- **Bands (§ 2a(5)).** The person picks a band. A person may always pick a higher band than the lowest one they qualify for. The income limits are in the table above. The 75% tests use the lump-sum percentage that would apply to the activity, whether or not the person used the lump sum.
- **Tax equal to the flat tax (§ 7a(1)).** At the year end, the tax equals the flat tax if all of these hold:
  - the person stayed within the band's limit, or exceeded it but stayed within a higher band's limit and notified the higher amount;
  - besides self-employment income, they had only exempt income, income outside the scope of tax, income taxed by final withholding, and up to CZK 50,000 of capital, rental and other income;
  - they were not a VAT payer and not a partner in a v.o.s. or k.s.;
  - as a resident, they do not claim relief from double tax on foreign income (§ 7a(5)).

  The flat tax is the number of months in the regime times the monthly tax part (§ 7a(6)).
- **Leaving.** The regime ends after a year in which the person exceeded the band limit (unless they notify a higher band that fits), registered for VAT or joined a v.o.s. or k.s. (§ 2a(8)). It can also be left voluntarily. If the tax for a year is not equal to the flat tax, the person files a normal return for that year (§ 38g(7)). The monthly payments made count towards the tax and the insurance.

## Deadlines and filing

**Return for tax year 2026 (Tax Code § 136, § 33(4)).** The return is due within 3 months of the year end. That becomes 4 months if it is filed electronically after the 3 months, and 6 months if a tax adviser or advocate files it after the 3 months, or if an audit is compulsory. A deadline on a weekend or public holiday moves to the next working day. The Financial Administration gave the 2025 dates as 1 April, 4 May and 1 July 2026 ([Finanční správa](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace)). Counting the same way for 2026:

- paper or electronic: **1 April 2027** (Thursday);
- electronic, after 1 April: **3 May 2027**, because 1 May 2027 is a Saturday and a public holiday;
- tax adviser or advocate: **1 July 2027**.

The tax is due on the last day for filing. Anyone whose taxable income is over CZK 50,000, or who has a tax loss, must file (ITA § 38g(1)). A person with a data box set up by law files electronically (Tax Code § 72). The self-employed also file annual overviews with ČSSZ and their health insurer: see [cz-social-health](cz-social-health.md).

**Tax advances (ITA § 38a).** They depend on the last known tax liability (the tax on the last return):

- up to CZK 30,000: no advances;
- over CZK 30,000 and up to CZK 150,000: two advances of 40% each, due 15 June and 15 December;
- over CZK 150,000: four advances of 25% each, due 15 March, 15 June, 15 September and 15 December.

The advance period runs from the day after the return deadline to the next return deadline (§ 38a(1)). Each advance is rounded up to whole hundreds of CZK (Tax Code § 146(2)). Advances are reduced or dropped where employment income with payroll withholding is part of the base: none if it is 50% or more of the total base, half if it is 15% to 50% (§ 38a(5)). Advances paid late count towards the tax only if paid by the return deadline (§ 38a(1)).

**Flat-rate regime.**

- Notice to join: by 10 January of the year (§ 38lc(1)). For 2027 that is **11 January 2027**, because 10 January 2027 is a Sunday. A person starting a business later in the year notifies by the day the business starts (§ 38lc(2)). A late notice has no effect and the deadline cannot be restored (§ 38lc(6)).
- Notice to change band, notice of a different flat tax amount, and notice to leave voluntarily: each by 10 January of the relevant year (§§ 38lda, 38ldb, 38le).
- From 2027, a person in band I whose self-employment income in the previous year was at most CZK 1,000,000 can sign up for a surcharge of CZK 1,400 a month on the flat payment. It frees them from the new sales-registration duty. The sign-up is by 10 January or in the notice to join or change band (ITA §§ 2b, 7a(7) and 38lk(7)(a), (8), as amended by Act 180/2026 from 1 January 2027). Act 180/2026 does not change the rules for tax year 2026 (its § 31(1)).
- Notice that the regime has ended (for example on VAT registration): within 15 days (§ 38lg).
- Monthly payment: by the 20th of each month to the shared personal tax account. In the month a business starts, the first payment is due by the 20th of the next month (§ 38lk(5), (6)).
- No return: the person is treated as having filed a return showing the flat tax on the last filing day (§ 38lh(1)). The tax and the flat insurance are assessed and due on that day (§ 38li, § 38lj).

## Penalties and interest

- **Late return** (Tax Code § 250). If the return is more than 5 working days late, the penalty is 0.05% of the tax for each further day, capped at 5% of the tax. For a late return showing a loss, it is 0.01% of the loss a day, capped at 5%. Other rules:
  - A penalty under CZK 1,000 is not charged (§ 250(3)).
  - A return never filed is charged the full cap, and at least CZK 500 (§ 250(4)).
  - The maximum is CZK 300,000 (§ 250(5)).
  - The penalty is halved if the return is filed within 30 days of the deadline and there was no other late filing that year (§ 250(7)).
- **Tax assessed by the tax office.** 20% penalty (penále) on extra tax over the last known tax, and 1% on a reduction of a loss (Tax Code § 251(1)).
- **Late payment interest** on unpaid tax and advances. It runs from the fourth day after the original due date until payment (Tax Code § 252(2)). Interest arises for each day separately. The rate for each day is the CNB repo rate on the first day of the calendar half-year in which that day falls, plus 8 points (Tax Code § 251a(1), (5) and § 252(4); Government Regulation 351/2013 § 2(1)). Days from 1 January to 30 June 2026 bear 11.50% a year; days from 1 July to 31 December 2026 bear 11.75% (CNB repo 3.50% from 9 May 2025 and 3.75% from 19 June 2026). A daily amount uses a 365-day year (Tax Code § 146(4)). Interest of CZK 1,000 or less in total for one tax and period is not charged (§ 251a(2)).
- **Flat-rate regime.** Failing a condition must be reported within 15 days of finding it (ITA § 38lf). The person then files a normal return and pays tax and insurance under the normal rules.

## Cross-border points

- **Non-residents** with a Czech permanent establishment or Czech-source business income file a return on that income (ITA § 22). The basic credit applies. The other credits, the child benefit and the § 15 deductions need EU or EEA residence and at least 90% of world income from Czech sources (§ 35ba(2), § 35c(5), § 15(8)). See [cz-cross-border](cz-cross-border.md).
- **Flat-rate regime.** It ends in the month a person becomes non-resident and stops working in Czechia (§ 2a(8)(e)). It also ends the month before a health insurance exemption for a long stay abroad starts (§ 2a(8)(d)). A resident who claims treaty relief on foreign income in a return loses the flat tax for that year (§ 7a(5)).
- **Foreign business income of a resident** goes into the base, with relief under the treaty (§ 38f). Withholding on payments to non-residents (15%, 35% to non-cooperative states) and the tax security are in [cz-cross-border](cz-cross-border.md).
- **Social insurance** for people working in more than one EU state follows the EU coordination rules: see [cz-social-health](cz-social-health.md).

## Worked examples

### Example 1: trader on the 60% lump sum, single, two advances the next year

She runs a free trade (not a craft trade) and has income of CZK 1,200,000 in 2026. She uses the 60% lump sum. She has no other income, no children and no deductions.

1. Lump sum: 60% of CZK 1,200,000 is CZK 720,000, under the CZK 1,200,000 cap.
2. Partial base: CZK 1,200,000 less CZK 720,000 = CZK 480,000, already a whole hundred.
3. Tax at 15%: CZK 72,000. Less the basic credit of CZK 30,840: CZK 41,160.
4. The tax is due by 1 April 2027 (or 3 May 2027 if filed electronically after 1 April).
5. CZK 41,160 is over CZK 30,000 and under CZK 150,000, so in the next advance period she pays two advances of 40%. 40% of 41,160 is 16,464, rounded up to CZK 16,500, due 15 June and 15 December 2027.

Her 2026 income was under CZK 1,500,000, and all of it is 60% lump-sum income. So for 2027 she could also join band I of the flat-rate regime (CZK 9,162 a month at 2026 rates, covering tax and insurance). That needs a notice by 11 January 2027. Compare the two only after working out her social and health insurance in [cz-social-health](cz-social-health.md).

```oa-check
name: OSVČ free trade, income CZK 1,200,000, 60% lump sum (2026)
inputs:
  income: 1200000
  basic_credit: 30840
steps:
  - lump_sum: min(income * 0.60, 1200000)
  - base: floor((income - lump_sum) / 100) * 100
  - tax: ceil(base * 0.15 - basic_credit)
  - advance: ceil(tax * 0.40 / 100) * 100
expected:
  lump_sum: 720000
  base: 480000
  tax: 41160
  advance: 16500
```

### Example 2: professional above the lump-sum cap and the 23% threshold

He is an independent professional (40% lump-sum group) with income of CZK 3,000,000 in 2026. His documented business expenses are CZK 1,000,000. He has no other income, no children and no deductions. He compares the two methods.

1. Lump sum: 40% of CZK 3,000,000 is CZK 1,200,000, capped at CZK 800,000. Base: CZK 2,200,000.
2. Actual expenses: base CZK 3,000,000 less CZK 1,000,000 = CZK 2,000,000.
3. Tax on the lump-sum base: 15% of CZK 1,762,812 is CZK 264,421.80. 23% of the excess of CZK 437,188 is CZK 100,553.24. Total CZK 364,975.04. Less the basic credit: CZK 334,135.04, rounded up to CZK 334,136.
4. Tax on the actual-expenses base: CZK 264,421.80 plus 23% of CZK 237,188 (CZK 54,553.24) = CZK 318,975.04. Less the basic credit: CZK 288,135.04, rounded up to CZK 288,136.
5. Actual expenses save CZK 46,000 of income tax: the extra CZK 200,000 of expenses, all taxed at 23%. They also lower the base for social and health insurance (see [cz-social-health](cz-social-health.md)). Under actual expenses he must keep tax records (§ 7b).
6. Either way, his tax is over CZK 150,000, so he pays four quarterly advances in the next period. Each is 25% of CZK 288,136 = 72,034, rounded up to CZK 72,100.

His income is over CZK 2,000,000, so the flat-rate regime is not open to him for 2027.

```oa-check
name: OSVČ professional, income CZK 3,000,000, lump sum vs actual expenses CZK 1,000,000 (2026)
inputs:
  income: 3000000
  actual_expenses: 1000000
  threshold: 1762812
  basic_credit: 30840
steps:
  - lump_sum: min(income * 0.40, 800000)
  - base_lump: floor((income - lump_sum) / 100) * 100
  - base_actual: floor((income - actual_expenses) / 100) * 100
  - tax_lump: ceil(min(base_lump, threshold) * 0.15 + max(base_lump - threshold, 0) * 0.23 - basic_credit)
  - tax_actual: ceil(min(base_actual, threshold) * 0.15 + max(base_actual - threshold, 0) * 0.23 - basic_credit)
  - saving: tax_lump - tax_actual
  - quarterly_advance: ceil(tax_actual * 0.25 / 100) * 100
expected:
  lump_sum: 800000
  base_lump: 2200000
  base_actual: 2000000
  tax_lump: 334136
  tax_actual: 288136
  saving: 46000
  quarterly_advance: 72100
```

## Ask the client first

1. What the activity is, and under which licence: craft trade, other trade, licensed or independent profession, royalties, or letting of business property. This sets the lump-sum percentage, its cap and the flat-rate bands.
2. Income for the year, and documented business expenses if any. This decides lump sum or actual expenses, and whether the 23% rate applies.
3. Whether they are a VAT payer or must register, are a partner in a v.o.s. or k.s., or had employment on 1 January. Each rules out the flat-rate regime.
4. Whether they are in the flat-rate regime now, in which band, and whether income stayed within that band's limit.
5. Other income: employment, rent, capital, foreign income, sales of property or securities. This affects filing, advances and the flat-rate test.
6. Children in the household, a spouse with a child under 3, and payments that give deductions (pension and life insurance products, mortgage interest, donations).

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 586/1992 Coll., Income Taxes Act, version in force 1 August to 31 December 2026: §§ 2, 2a, 7, 7a, 7b, 15, 16, 21g, 23, 25, 34, 35ba, 35bb, 35c, 38a, 38g, 38lc to 38lk | https://e-sbirka.gov.cz/sb/1992/586/2026-08-01 | 2026-10-23 |
| Act No. 280/2009 Coll., Tax Code, version in force from 1 January 2026: §§ 33, 136, 146, 250, 251, 251a, 252 | https://e-sbirka.gov.cz/sb/2009/280/2026-01-01 | 2026-10-23 |
| Government Regulation No. 365/2025 Coll., § 1 (general assessment base 2024 and coefficient) | https://e-sbirka.gov.cz/sb/2025/365 | 2026-10-23 |
| Government Regulation No. 351/2013 Coll., § 2 (late payment interest: repo plus 8 points) | https://e-sbirka.gov.cz/sb/2013/351 | 2026-10-23 |
| Finanční správa, Informace k institutu paušální daně pro rok 2025 a 2026 (bands, 2026 monthly payments, band I change from 1 July 2026) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pausalni-dan/informace-k-institutu-pausalni-dane-pro-rok-2025 | 2026-10-23 |
| Finanční správa, Fyzické osoby: obecné informace (2025 filing dates) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace | 2026-10-23 |
| MPSV, Minimální mzda (CZK 22,400 a month for 2026) | https://www.mpsv.cz/minimalni-mzda | 2026-10-23 |
| Act No. 589/1992 Coll., social security premiums, version in force from 1 July 2026: § 14(3), (5) (flat-rate pension bases) | https://e-sbirka.gov.cz/sb/1992/589/2026-07-01 | 2026-10-23 |
| Act No. 90/2026 Coll., amending Act 589/1992 (minimum base 35% for 2026; Art. II(4) flat-rate regime from 1 January 2026; in force 1 July 2026) | https://e-sbirka.gov.cz/sb/2026/90 | 2026-10-23 |
| Act No. 592/1992 Coll., public health insurance premiums: §§ 2, 3a(2), (5), 8a (flat-rate health bases) | https://e-sbirka.gov.cz/sb/1992/592 | 2026-10-23 |
| Act No. 180/2026 Coll., sales registration and amendments (ITA changes from 1 January 2027; § 31(1) transitional rule) | https://e-sbirka.gov.cz/sb/2026/180 | 2026-10-23 |
| Finanční správa, change of the interest cap (Act 386/2020 Art. IV(3): CZK 300,000 for housing acquired before 2021) | https://financnisprava.gov.cz/assets/cs/prilohy/d-seznam-dani/Informace-ke-zmene-vyse-limitu-uhrnne-castky-uroku.pdf | 2026-10-23 |
| Czech National Bank, two-week repo rate history | https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt | 2026-10-23 |

Not yet confirmed:
- The Financial Administration had not published the filing dates for the 2026 return. The 1 April, 3 May and 1 July 2027 dates come from Tax Code §§ 33 and 136 and the way it counted the 2025 dates.
- Applying each lump-sum percentage and cap per activity, for a person with activities in more than one group, follows the wording of § 7(7); no Financial Administration instruction on it was read.
- 2026 social and health insurance of the self-employed (minimum advances, assessment bases) is not covered here. cz-social-health still carries 2025 figures.
