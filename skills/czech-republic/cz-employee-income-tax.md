---
name: cz-employee-income-tax
description: "Czech personal income tax for employees and other non-business income, tax year 2026. Covers the 15% and 23% rates and the 2026 threshold of CZK 1,762,812 (36 times the average wage), the employment income base (gross pay, no super-gross), monthly advances withheld by the employer, the signed tax declaration, tax credits (taxpayer, spouse, disability, ZTP/P), the child tax benefit and bonus, deductions (pension and life insurance products, mortgage interest, donations), the employer's annual reconciliation versus filing a return, and rental and capital income at a high level. Trigger on: zaměstnanec, mzda, záloha na daň, prohlášení poplatníka, roční zúčtování, sleva na poplatníka, daňové zvýhodnění, daňový bonus, Czech salary tax, employee tax return Czech Republic. Out of scope: self-employed (OSVČ) income tax (cz-income-tax), social and health insurance (cz-social-health), residence and non-residents (cz-cross-border), corporate tax (cz-corporate-income-tax)."
version: 0.2
jurisdiction: CZ
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Czech Republic: income tax for employees and other non-business income (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure comes from the Income Taxes Act as published in e-Sbírka (version in force 1 August to 31 December 2026), the Tax Code, government regulations, MPSV and the Financial Administration, all read on 23 October 2026. It prepares working papers. It is not authority to file or pay.

This skill covers individuals whose income is employment income under § 6 of Act No. 586/1992 Coll. on Income Taxes ("ITA"), plus rental, capital and other income that does not come from a business. It links to the other skills in the pack rather than repeating them:

- Self-employed (OSVČ) income tax, expense lump sums and the flat-rate regime: [cz-income-tax](cz-income-tax.md).
- Social and health insurance: [cz-social-health](cz-social-health.md) (self-employed only today).
- Residence, non-residents, treaties and withholding on payments abroad: [cz-cross-border](cz-cross-border.md).
- Overview: [cz-tax-overview](cz-tax-overview.md).

Tax year: the calendar year. Currency: Czech koruna (CZK). Authority: the Financial Administration (Finanční správa).

## Who this applies to

- **Employees.** Anyone with income from dependent activity under ITA § 6(1). That covers an employment contract, the two agreements outside employment (dohoda o provedení práce, "DPP", and dohoda o pracovní činnosti, "DPČ"), pay for work by a partner in an s.r.o. or a cooperative member, and fees of board members and liquidators (§ 6(1)(a) to (c)). Income connected with that work counts even if a third party pays it (§ 6(1)(d)).
- **Residents** are taxed on worldwide income. **Non-residents** are taxed on Czech-source income only (ITA § 2). The residence tests (domicile or 183 days) are in [cz-cross-border](cz-cross-border.md).
- **Other non-business income.** Capital income (§ 8), rental income (§ 9) and other income (§ 10) of a person who is not running a business. This skill gives the main rules and points to the detail.
- **Out of scope.** Business and professional income under § 7, the expense lump sums for it and the flat-rate tax (paušální daň) are in [cz-income-tax](cz-income-tax.md).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Rate on the tax base up to 36 times the average wage | 15% | 2026 | [ITA § 16(1)(a)](https://e-sbirka.gov.cz/sb/1992/586/2026-08-01) |
| Rate on the tax base above 36 times the average wage | 23% | 2026 | ITA § 16(1)(b) |
| Average wage for tax purposes (the social insurance figure, ITA § 21g(2)) | CZK 48,967: general assessment base for 2024 of CZK 46,278 times coefficient 1.0581, rounded up | 2026 | [Act 589/1992 § 23b(4)](https://e-sbirka.gov.cz/sb/1992/589/2026-07-01); [Government Regulation 365/2025 § 1](https://e-sbirka.gov.cz/sb/2025/365) |
| 23% threshold, annual (36 × 48,967) | CZK 1,762,812 | 2026 | computed from the two rows above |
| 23% threshold for monthly advances (3 × 48,967) | CZK 146,901 a month | 2026 | ITA § 38h(2); computed |
| Basic taxpayer credit (sleva na poplatníka) | CZK 30,840 a year (CZK 2,570 a month in payroll) | 2026 | ITA § 35ba(1)(a), § 35d(2) |
| Spouse credit (sleva na manžela) | CZK 24,840; double if the spouse holds a ZTP/P card. Only if the couple lives with the taxpayer's child under 3 and the spouse's own income is at most CZK 68,000 | 2026 | ITA § 35bb(1), (2) |
| Basic disability credit (disability pension, grade 1 or 2) | CZK 2,520 | 2026 | ITA § 35ba(1)(c) |
| Extended disability credit (grade 3) | CZK 5,040 | 2026 | ITA § 35ba(1)(d) |
| ZTP/P card holder credit | CZK 16,140 | 2026 | ITA § 35ba(1)(e) |
| Student credit | None for 2026: § 35ba(1) lists no student credit. Act 180/2026 restores it at CZK 4,020 from tax year 2027 (its transitional provision keeps the old text for 2026) | 2026 | ITA § 35ba(1); [Act 180/2026 Part Two, § 31(1), § 36](https://e-sbirka.gov.cz/sb/2026/180) |
| Child tax benefit (daňové zvýhodnění), first child | CZK 15,204 a year | 2026 | ITA § 35c(1) |
| Child tax benefit, second child | CZK 22,320 a year | 2026 | ITA § 35c(1) |
| Child tax benefit, third and each further child | CZK 27,840 a year; doubled for a child with a ZTP/P card | 2026 | ITA § 35c(1), (7) |
| Minimum annual tax bonus | CZK 100 (monthly bonus: CZK 50) | 2026 | ITA § 35c(3), § 35d(4) |
| Income needed for a tax bonus | Employment or business income of at least 6 times the minimum wage: CZK 134,400. Monthly bonus in payroll: at least half the minimum wage, CZK 11,200, in the month | 2026 | ITA § 35c(4), § 35d(4), § 21g(1); [MPSV, minimum wage 2026](https://www.mpsv.cz/minimalni-mzda) (CZK 22,400 a month) |
| Pension products, private life insurance, long-term investment product and long-term care insurance | Deduction of up to CZK 48,000 a year in total | 2026 | ITA § 15(6), (7) |
| Employer contributions to those products | Exempt for the employee up to CZK 50,000 a year | 2026 | ITA § 6(9)(m) |
| Mortgage and building-savings loan interest for own housing | Deduction of up to CZK 150,000 a year per household; CZK 300,000 where the housing was acquired before 1 January 2021; one twelfth of the cap per month if interest is paid for part of the year | 2026 | ITA § 15(3), (4); [Finanční správa, interest cap note](https://financnisprava.gov.cz/assets/cs/prilohy/d-seznam-dani/Informace-ke-zmene-vyse-limitu-uhrnne-castky-uroku.pdf) |
| Donations to qualifying recipients | Deductible if the total is more than 2% of the tax base or at least CZK 1,000; capped at 15% of the tax base | 2026 | ITA § 15(1) |
| Filing threshold | Return required if income subject to tax (not counting exempt income or income taxed by final withholding) exceeds CZK 50,000, or if there is a tax loss | 2026 | ITA § 38g(1) |
| Other income an employee may have without filing | Up to CZK 20,000 of income under §§ 7 to 10 | 2026 | ITA § 38g(2) |
| Small payments taxed by 15% final withholding when no declaration is signed | DPP pay below CZK 12,000 a month with that payer; other employment pay below CZK 4,500 a month with that payer | 2026 | ITA § 6(4), § 36(2); Act 187/2006 § 6(2) and § 7a(1); [MPSV Communication 396/2025](https://e-sbirka.gov.cz/sb/2025/396) (DPP CZK 12,000 from 1 January 2026); [ČSSZ, key figures for 2026](https://www.cssz.gov.cz/-/prehled-nejdulezitejsich-udaju-pro-socialni-zabezpeceni-v-roce-2026) (CZK 4,500 unchanged) |
| Final withholding on dividends and on interest from deposits paid to individuals | 15% | 2026 | ITA § 36(2) |
| Rental income: expense lump sum | 30% of rent, at most CZK 600,000 | 2026 | ITA § 9(4) |
| Late payment interest | CNB repo rate on the first day of the half-year plus 8 points: 11.50% for 1 January to 30 June 2026, 11.75% for 1 July to 31 December 2026 | 2026 | [Tax Code § 252(4), § 251a(5)](https://e-sbirka.gov.cz/sb/2009/280/2026-01-01); [Government Regulation 351/2013 § 2](https://e-sbirka.gov.cz/sb/2013/351); [CNB repo history](https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt) |

The annual tax is worked out on the base after deductions, rounded down to whole hundreds of CZK. It is the sum of each slice times its rate (ITA § 16(2)). The tax is then rounded up to whole CZK (Tax Code § 146(1)), in one step (§ 146(3)).

## The taxable base

**Employment income: gross pay.** The tax base from employment is the employment income itself (ITA § 6(12)). There is no super-gross base: the employer's social and health insurance is not added, and the employee's own contributions are not deducted. Income includes cash and benefits in kind, regular or one-off, whether paid to the employee or to someone else for them (§ 6(3)).

- **Company car for private use.** The employee is taxed on 1% of the car's purchase price (including VAT) for each month or part month. The rate is 0.5% for a low-emission car and 0.25% for a zero-emission car, with a minimum of CZK 1,000 a month (§ 6(6)).
- **Exempt benefits.** § 6(9) lists exempt benefits. Examples: health products up to the average wage in total, and recreation, sport, culture and books up to half the average wage in total (§ 6(9)(d)). Employer contributions to pension and life insurance products are exempt up to CZK 50,000 a year (§ 6(9)(m)). Read the list before treating a benefit as exempt.
- **Timing.** Pay for a year that is paid by 31 January of the next year counts in the earlier year (§ 5(4)).

**Small payments taxed by final withholding.** If the employee has not signed a tax declaration with the payer, these are taxed at 15% as a separate base with no credits (§ 6(4)). The thresholds:

- DPP pay below the amount that brings DPP workers into sickness insurance. That is 25% of the average wage rounded down to whole CZK 500 (Act 187/2006 § 7a(1)): CZK 12,000 from 1 January 2026 (MPSV Communication 396/2025).
- Any other employment pay below the sickness-insurance "decisive income" (Act 187/2006 § 6(2)): CZK 4,500 for 2026, unchanged from 2025 (ČSSZ key figures for 2026).

A resident can put this income into a return instead and credit the tax withheld (ITA § 36(6)). From tax year 2027 this final withholding ends: the version of § 6(4) in force from 1 January 2027 makes this pay a separate base for advances instead (ITA as in force from 1 January 2027).

**Deductions from the base (nezdanitelné části základu daně, ITA § 15).** They come off the total base, before rounding and before the rates:

- **Pension and life insurance products** (§ 15(6), (7)). Up to CZK 48,000 a year in total across supplementary pension savings, pension insurance, private life insurance, the long-term investment product (DIP) and long-term care insurance. For state-supported pension savings (supplementary pension savings and the older pension insurance with state contribution), only the part of each monthly contribution above CZK 1,700 counts, because CZK 1,700 is the contribution that earns the maximum state contribution of CZK 340 (§ 15(7); Act 427/2011 § 14(2), which Act 42/1994 applies to the older product). A single premium for life insurance is spread over the policy term by days.
- **Housing loan interest** (§ 15(3), (4)). Interest on a mortgage or building-savings loan used for the taxpayer's own housing. The cap is CZK 150,000 a year per household, or CZK 300,000 for housing acquired before 2021. Co-borrowers claim it once, or in equal shares. The deduction is pro-rated if part of the home is let or used in a business.
- **Donations** (§ 15(1)). Gifts to Czech municipalities, regions and qualifying Czech and EU or EEA bodies for listed purposes, and to political parties. The total must be over 2% of the base or at least CZK 1,000. The cap is 15% of the base.
- **Non-residents** get these deductions only if they live in the EU or EEA and at least 90% of their world income is Czech-source (§ 15(8)).

**Credits and the child benefit.** They come off the tax, in this order:

1. The credits in ITA § 35ba (basic, spouse, disability, ZTP/P).
2. The child tax benefit (§ 35c), for a child who lives with the taxpayer in a shared household in the EU or EEA (§ 35c(1)). It reduces the tax left after credits. Any excess is paid out as a tax bonus, if the bonus is at least CZK 100 and the taxpayer had employment or business income of at least CZK 134,400 in 2026 (§ 35c(3), (4)).

The basic credit is a full annual amount even for part of a year. The spouse, disability and ZTP/P credits and the child benefit are one twelfth for each month in which the conditions were met at the start of the month (§ 35ba(3), § 35c(10)). The child benefit can be claimed from the month of birth. Only one person in a household may claim it for the same child in the same month (§ 35c(9), (10)). A child counts up to age 18, or up to 26 while in full-time study or training (§ 35c(6)).

**Capital income (§ 8).** Dividends from Czech companies and interest on deposits paid to individuals are taxed by 15% final withholding at source. They do not go into the return (§ 36(2)). Foreign dividends and interest go into a resident's return as § 8 income. Gains on securities are other income under § 10. They are exempt if total proceeds in the year are at most CZK 100,000 (§ 4(1)(t)), or if the security was held for more than 3 years (§ 4(1)(u)). The detail is on the [Financial Administration capital income page](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/kapitalove-prijmy).

**Rental income (§ 9).** Rent from property not held in a business. The landlord deducts actual costs (including tax depreciation) or 30% of the rent, at most CZK 600,000 (§ 9(4)). The choice cannot be changed later for that year. See the [Financial Administration landlord page](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/pronajimatel).

**Other income (§ 10).** Occasional income, sales of property and securities, and similar items. Each type is exempt while its total in the year is at most CZK 50,000 (§ 10(3)(a)). Sales of a home and long-held property have their own exemptions in § 4(1)(a) and (b).

## Deadlines and filing

**Through the employer: monthly advances (ITA § 38h).**

- The employer works out the advance on each month's taxable pay. The base for the advance is rounded up to whole CZK if it is up to CZK 100, and up to whole hundreds if it is above (§ 38h(1)).
- The rate is 15% on the part up to CZK 146,901 and 23% on the rest. The advance is rounded up to whole CZK (§ 38h(2), (3)).
- If the employee has signed the tax declaration (prohlášení poplatníka) with that employer, the advance is reduced by one twelfth of the basic, disability and ZTP/P credits. It is then reduced by one twelfth of the child benefit, and any excess is paid as a monthly bonus (§ 38h(4), § 35d). The spouse credit and the § 15 deductions wait for the annual reconciliation (§ 38h(6)).
- Only one employer at a time may apply the credits (§ 38k(3)). Without a declaration, no credits are given in payroll (§ 38h(5)).
- The employee signs the declaration within 30 days of starting work, and then each year by 15 February (§ 38k(4)).
- The employer pays the advances to its tax office by the 20th of the month in which it withheld them (§ 38h(10)). It files the annual statement of employment tax within two months of the year end, or by 20 March if it files electronically (§ 38j(5)). 20 March 2027 is a Saturday, so the electronic date for 2026 is 22 March 2027 (Tax Code § 33(4)).
- If the employee does not ask for a reconciliation and need not file, the advances are the final tax (§ 38h(9)).

**Annual reconciliation by the employer (roční zúčtování, ITA § 38ch).**

- The employee qualifies if, in 2026, they had employment income only from one employer, or from several one after another, signed the declaration with each, and need not file a return.
- They ask the last employer by **15 February 2027**, with pay certificates from the earlier employers (§ 38ch(1), (3)). Proof for deductions and the spouse credit is due by the same date (§ 38k(5)).
- The employer computes the tax by **31 March 2027** (§ 38ch(4)). It pays any overpayment over CZK 50 with the pay for March 2027 at the latest (§ 38ch(5), § 35d(8)). An underpayment from the reconciliation is not deducted from the employee's pay (§ 38ch(5)).
- If the employer has ceased to exist with no successor, the employee asks the tax office instead, by the same 15 February date (§ 38ch(2)).

**Filing a return (ITA § 38g).** An employee must file if any of these applies:

- they had two employers at the same time (a declaration can be signed with only one of them, § 38k(3)), or worked for an employer without signing a declaration, other than income taxed by final withholding;
- they had more than CZK 20,000 of other income under §§ 7 to 10, such as rent or foreign dividends (§ 38g(2));
- they are a non-resident claiming the spouse or disability credits, the child benefit or deductions (§ 38g(2));
- they are in the other cases in § 38g(4) to (7).

Anyone whose income subject to tax is above CZK 50,000, not counting exempt income and income taxed by final withholding, must file unless the employee exception applies. A tax loss also means a return (§ 38g(1)).

**Return deadlines for tax year 2026.** The return is due within 3 months of the year end, 4 months if filed electronically after that, or 6 months if a tax adviser or advocate files it after that or an audit is compulsory (Tax Code § 136(1), (2)). A deadline that falls on a weekend or public holiday moves to the next working day (Tax Code § 33(4)). The Financial Administration counted the 2025 deadlines as 1 April, 4 May and 1 July 2026 ([Finanční správa](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace)). Counting the same way for 2026:

- paper or electronic: **1 April 2027** (Thursday);
- electronic, after 1 April: **3 May 2027**, because 1 May 2027 is a Saturday and a public holiday;
- tax adviser or advocate: **1 July 2027**.

Tax shown on the return is due on the last day for filing ([Finanční správa](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace)). The return goes to the tax office for the person's place of residence. A person with a data box set up by law must file electronically (Tax Code § 72(6)).

## Penalties and interest

- **Late return.** If the return is more than 5 working days late, the penalty is 0.05% of the tax for each further day, capped at 5% of the tax (Tax Code § 250(1)(a)). Other rules:
  - A penalty under CZK 1,000 is not charged (§ 250(3)).
  - A return never filed is charged the full cap, and at least CZK 500 (§ 250(4)).
  - The maximum is CZK 300,000 (§ 250(5)).
  - The penalty is halved if the return is filed within 30 days of the deadline and there was no other late filing that year (§ 250(7)).
- **Employer as withholding agent.** For a late annual statement, the penalty is 0.05% of the tax a day, capped at 0.5% (Tax Code § 250(2)).
- **Tax assessed by the tax office.** A 20% penalty (penále) on extra tax it assesses (§ 251(1)(a)). There is none on tax the taxpayer reports in a supplementary return (§ 251(4)).
- **Late payment interest.** It runs from the fourth day after the due date (Tax Code § 252(2)). The rate is the CNB repo rate on the first day of the half-year plus 8 points: 11.50% a year for January to June 2026 and 11.75% for July to December 2026 (§ 252(4), § 251a(5); Government Regulation 351/2013 § 2; CNB repo 3.50% from 9 May 2025 and 3.75% from 19 June 2026). Interest of CZK 1,000 or less is not charged (§ 251a(2)).
- **Employer errors.** If the employer withheld too little through its own fault, it may recover the shortfall from the employee's pay within 2 years of the deadline for its annual statement for that year (ITA § 38i(4)). If the employee caused the shortfall, the employer recovers it with the employee's agreement or reports it to the tax office, and the employee must then file a return (§ 38i(5), § 38g(4)).

## Cross-border points

- **Non-resident employees** working in Czechia are taxed through payroll like residents, but no spouse, disability or ZTP/P credit and no child benefit is given in payroll (ITA § 38h(13)). The basic credit is given. The other credits, the child benefit and the deductions need a return, an EU or EEA residence, and at least 90% of world income from Czech sources (§ 35ba(2), § 35c(5), § 15(8), § 38g(2)). See [cz-cross-border](cz-cross-border.md).
- **Residents working abroad.** Foreign employment income is part of the base, with relief under the treaty (ITA § 38f). Where there is no treaty, the base is the foreign income less foreign tax paid (§ 6(13)). An employee whose only income is foreign employment income exempted under § 38f need not file (§ 38g(2)).
- **Foreign employer, work in Czechia.** If a Czech business directs the work but pay goes through a foreign entity (international hiring-out of labour), the Czech business is treated as the employer and withholds the advances (§ 6(2), § 38h(10)).
- **Foreign capital and rental income** of a resident is reported on the return. Foreign tax is credited or the income exempted under the treaty. Method and examples are in [cz-cross-border](cz-cross-border.md).

## Worked examples

### Example 1: employee with one child and life insurance, annual reconciliation

She earns CZK 60,000 a month for all of 2026 from one employer. She signed the tax declaration in January and claims her only child. She pays CZK 24,000 a year into private life insurance. She has no other income, so she asks her employer for the annual reconciliation by 15 February 2027.

1. Monthly advance: the base is CZK 60,000, below the CZK 146,901 monthly threshold, so 15%: CZK 9,000.
2. Monthly credits: basic credit 30,840 / 12 = CZK 2,570. Child benefit 15,204 / 12 = CZK 1,267. Advance after credits: CZK 5,163. Over 12 months: CZK 61,956 withheld.
3. Annual base: CZK 720,000 less the life insurance deduction of CZK 24,000 (under the CZK 48,000 cap) = CZK 696,000, already a whole hundred.
4. Tax at 15%: CZK 104,400. Less the basic credit of CZK 30,840: CZK 73,560. Less the child benefit of CZK 15,204: CZK 58,356.
5. Withheld CZK 61,956 against tax of CZK 58,356 gives an overpayment of CZK 3,600. That is 15% of the life insurance deduction. The employer pays it with the March 2027 pay at the latest.

```oa-check
name: Employee CZK 60,000 a month, one child, CZK 24,000 life insurance (2026)
inputs:
  monthly_pay: 60000
  basic_credit: 30840
  child_benefit: 15204
  life_insurance: 24000
steps:
  - monthly_advance: monthly_pay * 0.15
  - monthly_after_credits: monthly_advance - basic_credit / 12 - child_benefit / 12
  - withheld: monthly_after_credits * 12
  - base: monthly_pay * 12 - min(life_insurance, 48000)
  - tax: base * 0.15 - basic_credit - child_benefit
  - overpayment: withheld - tax
expected:
  monthly_advance: 9000
  monthly_after_credits: 5163
  withheld: 61956
  base: 696000
  tax: 58356
  overpayment: 3600
```

### Example 2: high earner above the 23% threshold with a flat to let and a donation

He earns CZK 150,000 a month for all of 2026 from one employer and signed the declaration there. He also lets a flat for CZK 20,000 a month (CZK 240,000 for the year) and uses the 30% expense lump sum. He gave CZK 50,000 to a registered Czech charity. His rental income is above CZK 20,000, so he cannot use the annual reconciliation and must file a return.

1. Monthly advance: 15% of CZK 146,901 is CZK 22,035.15. Add 23% of the excess of CZK 3,099, which is CZK 712.77. Total CZK 22,747.92, rounded up to CZK 22,748. Less the monthly basic credit of CZK 2,570: CZK 20,178. Over 12 months: CZK 242,136.
2. Employment base: CZK 1,800,000.
3. Rental base: CZK 240,000 less 30% (CZK 72,000, under the CZK 600,000 cap) = CZK 168,000.
4. Total base: CZK 1,968,000. The donation of CZK 50,000 is over 2% of the base (CZK 39,360) and under the 15% cap (CZK 295,200), so all of it is deducted: CZK 1,918,000.
5. Tax: 15% of CZK 1,762,812 is CZK 264,421.80. Add 23% of the excess of CZK 155,188, which is CZK 35,693.24. Total CZK 300,115.04, rounded up to CZK 300,116 (Tax Code § 146(1)). Less the basic credit: CZK 269,276.
6. Less advances withheld of CZK 242,136: CZK 27,140 to pay. It is due by 1 April 2027, or by 3 May 2027 if he files electronically after 1 April.

The monthly payroll applies 23% only to pay above CZK 146,901 in each month. The rental income and the annual threshold are not visible to the employer, so the return produces a balance to pay.

```oa-check
name: Employee CZK 150,000 a month plus rent CZK 240,000 and donation CZK 50,000 (2026)
inputs:
  monthly_pay: 150000
  monthly_threshold: 146901
  annual_threshold: 1762812
  basic_credit: 30840
  rent: 240000
  donation: 50000
steps:
  - monthly_advance: ceil(monthly_threshold * 0.15 + (monthly_pay - monthly_threshold) * 0.23)
  - withheld: (monthly_advance - basic_credit / 12) * 12
  - rental_base: rent - min(rent * 0.30, 600000)
  - total_base: monthly_pay * 12 + rental_base
  - donation_allowed: min(donation, total_base * 0.15)
  - base: floor((total_base - donation_allowed) / 100) * 100
  - tax_15: min(base, annual_threshold) * 0.15
  - tax_23: max(base - annual_threshold, 0) * 0.23
  - tax: ceil(tax_15 + tax_23) - basic_credit
  - balance_due: tax - withheld
expected:
  monthly_advance: 22748
  withheld: 242136
  rental_base: 168000
  total_base: 1968000
  base: 1918000
  tax_15: 264421.80
  tax_23: 35693.24
  tax: 269276
  balance_due: 27140
```

## Ask the client first

1. How many employers paid them in 2026, at the same time or one after another, and with which one they signed the tax declaration. This decides whether a reconciliation is allowed or a return is required.
2. Any other income: rent, foreign employment, foreign dividends or interest, sales of securities, crypto or property, occasional income. Above CZK 20,000 under §§ 7 to 10, a return is required.
3. Children in the household, their ages and whether they study. Whether another person in the household claims them. A spouse with a child under 3 and the spouse's own income.
4. Payments that give deductions: pension and life insurance products, mortgage interest (and when the home was acquired), donations.
5. Residence: whether they lived in Czechia all year, and for a non-resident, the country of residence and the share of world income from Czech sources.
6. Benefits from the employer: company car, contributions to pension or life insurance products, shares or options.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 586/1992 Coll., Income Taxes Act, version in force 1 August to 31 December 2026: §§ 2, 4, 5, 6, 8, 9, 10, 15, 16, 21g, 35ba, 35bb, 35c, 35d, 36, 38f, 38g, 38h, 38ch, 38i, 38j, 38k | https://e-sbirka.gov.cz/sb/1992/586/2026-08-01 | 2026-10-23 |
| Act No. 280/2009 Coll., Tax Code, version in force from 1 January 2026: §§ 33, 72, 136, 146, 250, 251, 251a, 252 | https://e-sbirka.gov.cz/sb/2009/280/2026-01-01 | 2026-10-23 |
| Act No. 589/1992 Coll., social security premiums, § 23b(4) (average wage) | https://e-sbirka.gov.cz/sb/1992/589/2026-07-01 | 2026-10-23 |
| Act No. 187/2006 Coll., sickness insurance, § 6(2) and § 7a(1) (decisive income, DPP threshold) | https://e-sbirka.gov.cz/sb/2006/187/2026-07-01 | 2026-10-23 |
| Act No. 586/1992 Coll., Income Taxes Act, future version in force from 1 January 2027: §§ 6(4), 35ba, 35bc | https://e-sbirka.gov.cz/sb/1992/586/2027-01-01 | 2026-10-23 |
| Act No. 180/2026 Coll. (restores the student credit from 1 January 2027), Part Two §§ 31 and 36 | https://e-sbirka.gov.cz/sb/2026/180 | 2026-10-23 |
| MPSV Communication No. 396/2025 Coll. (DPP threshold CZK 12,000 from 1 January 2026) | https://e-sbirka.gov.cz/sb/2025/396 | 2026-10-23 |
| ČSSZ, Přehled nejdůležitějších údajů pro sociální zabezpečení v roce 2026 (decisive income CZK 4,500) | https://www.cssz.gov.cz/-/prehled-nejdulezitejsich-udaju-pro-socialni-zabezpeceni-v-roce-2026 | 2026-10-23 |
| Act No. 427/2011 Coll., supplementary pension savings, § 14(2) (CZK 1,700 for the maximum state contribution) | https://e-sbirka.gov.cz/sb/2011/427/2026-08-01 | 2026-10-23 |
| Government Regulation No. 365/2025 Coll., § 1 (general assessment base 2024 and coefficient) | https://e-sbirka.gov.cz/sb/2025/365 | 2026-10-23 |
| Government Regulation No. 351/2013 Coll., § 2 (late payment interest: repo plus 8 points) | https://e-sbirka.gov.cz/sb/2013/351 | 2026-10-23 |
| MPSV, Minimální mzda (CZK 22,400 a month for 2026) | https://www.mpsv.cz/minimalni-mzda | 2026-10-23 |
| Finanční správa, Fyzické osoby: obecné informace (filing duty, deadlines, credits, child benefit) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace | 2026-10-23 |
| Finanční správa, information on the change in the interest cap (CZK 300,000 to CZK 150,000) | https://financnisprava.gov.cz/assets/cs/prilohy/d-seznam-dani/Informace-ke-zmene-vyse-limitu-uhrnne-castky-uroku.pdf | 2026-10-23 |
| Finanční správa, Kapitálové příjmy | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/kapitalove-prijmy | 2026-10-23 |
| Finanční správa, Pronajímatel | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/pronajimatel | 2026-10-23 |
| Czech National Bank, two-week repo rate history | https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt | 2026-10-23 |

Not yet confirmed:
- The Financial Administration had not published the filing dates for the 2026 return. The 1 April, 3 May and 1 July 2027 dates come from Tax Code §§ 33 and 136 and the way the Financial Administration counted the 2025 dates.
- Employee social and health insurance rates. These belong to the SC domain, which has no employee skill yet.

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
