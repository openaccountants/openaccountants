---
name: gr-income-tax
description: "Greek personal income tax for tax year 2026 (calendar year, return filed in 2027) for all individuals: employees, pensioners, the self-employed and landlords. Covers the 2026 scale of ν. 5246/2025 (9% to 44%), the lower rates for parents and for under-30s, the tax reduction for salaries and pensions (EUR 777 upwards, by number of children), the minimum deemed income of the self-employed (arts. 28A to 28Γ, from ν. 5073/2023), the 2026 rental scale (15% to 45%), dividends 5%, interest 15%, royalties 20%, the 30% card-spending requirement, the abolished solidarity contribution, the E1 return in myAADE, eight instalments, the early-filing discount and the 55% prepayment. Trigger phrases: Greek income tax, φορολογική δήλωση, E1, how much tax in Greece, salary tax Greece, freelancer tax Greece, τεκμήρια, rental income Greece. Out of scope: moving in or out and non-residents (gr-cross-border), EFKA contributions (gr-efka for the self-employed, gr-employee-contributions for employees), company tax (gr-corporate-income-tax), VAT (gr-vat-return)."
jurisdiction: GR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 2.4
verified_by: pending
---

# Greece: personal income tax, tax year 2026

Source-cited draft. Built by Michael Cutajar and the OpenAccountants team.

This skill covers Greek income tax for individuals for tax year 2026: employees, pensioners, the self-employed, landlords and people with dividends, interest or royalties. It links to the pack's other skills instead of repeating them:

- Moving to or from Greece, non-residents, the 5A, 5B and 5C regimes, withholding on payments abroad: `gr-cross-border`
- EFKA social contributions for the self-employed: `gr-efka`
- EFKA contributions on employees' pay: `gr-employee-contributions`
- Company income tax: `gr-corporate-income-tax`
- VAT: `gr-vat-return`
- Overview of the system: `gr-tax-overview`

The law is the Income Tax Code (Κώδικας Φορολογίας Εισοδήματος, ΚΦΕ, ν. 4172/2013). We read the Ministry of Finance codification, which includes amendments up to ν. 5264/2025 (Α' 239/19.12.2025). Its footnotes give the start date of each change. The 2026 scale, the child and youth rates, the rental scale and the new art. 15(1A) come from ν. 5246/2025 (Α' 198/11.11.2025) and apply to income earned from tax year 2026 (ν. 5246/2025 art. 47(3)). The changes to the minimum deemed income of the self-employed in the same law apply from tax year 2025 (art. 47(2)). Procedure, fines and interest are in the Tax Procedure Code (Κώδικας Φορολογικής Διαδικασίας, ΚΦΔ, ν. 5104/2024), read in AADE codification Ε.2109/2025. The tax authority is AADE. The tax year is the calendar year (art. 8 ΚΦΕ).

## Who this applies to

Every individual who has income taxable in Greece for 2026:

1. **Greek tax residents** are taxed on worldwide income. **Non-residents** are taxed only on Greek-source income (art. 3 ΚΦΕ). The residence tests (home, centre of vital interests, more than 183 days in any 12 months) are in `gr-cross-border`.
2. **Employees and pensioners.** Employment income includes salary, bonuses, allowances, benefits in kind and pensions from compulsory and occupational funds (art. 12(1) and (3)). A worker paid under written service contracts by no more than 3 clients, or with 75% or more of gross business income from one client, is treated as an employee for tax, if they have no commercial status and no business premises other than their home (art. 12(2)(στ)).
3. **The self-employed** (sole traders and freelancers, ατομική επιχείρηση) are taxed on business profit (arts. 21 to 29) and are subject to the minimum deemed income of arts. 28A to 28Δ.
4. **Landlords and investors** with rent, dividends, interest or royalties (arts. 35 to 40).

Every person aged 18 or over must declare all income, taxed or exempt, electronically (art. 67(1)). Married couples and registered partners file one joint return, with tax assessed separately for each spouse, unless one of them elects separate returns by 28 February of the filing year (art. 67(4)).

Out of scope here: capital gains on property and securities (arts. 41 to 42, see `gr-capital-gains`), the inbound regimes 5A, 5B and 5C (see `gr-cross-border`), farmers' special rules, and seafarers and other groups taxed at flat rates under art. 15(2).

## Rates, bands and thresholds

"Codification" is the Ministry of Finance codification of ν. 4172/2013 up to ν. 5264/2025, linked under the table and in Sources.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Scale for employment, pension and business income: EUR 0 to 10,000 | 9% | 2026 | ΚΦΕ art. 15(1)(a), as replaced by ν. 5246/2025 art. 3(1); Codification |
| EUR 10,000.01 to 20,000 | 20% | 2026 | same |
| EUR 20,000.01 to 30,000 | 26% | 2026 | same |
| EUR 30,000.01 to 40,000 | 34% | 2026 | same |
| EUR 40,000.01 to 60,000 | 39% | 2026 | same |
| Over EUR 60,000 | 44% | 2026 | same |
| 2nd band (10,000.01 to 20,000) with 1, 2 or 3 dependent children | 18%, 16%, 9% | 2026 | ΚΦΕ art. 15(1)(b); Codification |
| 3rd band (20,000.01 to 30,000) with 1, 2, 3 or 4 dependent children | 24%, 22%, 20%, 18%; 2 points lower for each child over 4 | 2026 | ΚΦΕ art. 15(1)(δ); Codification |
| First two bands with 4 or more dependent children | 0% | 2026 | ΚΦΕ art. 15(1)(γ); Codification |
| Young taxpayers, first two bands (income up to EUR 20,000) | 0% up to age 25; 9% aged 26 to 30 (0% if 4 or more children) | 2026 | ΚΦΕ art. 15(1)(ε); Codification |
| Tax reduction on employment and pension income, by dependent children: 0, 1, 2, 3, 4, 5 | EUR 777, 900, 1,120, 1,340, 1,580, 1,780; EUR 220 more for each further child | 2024 onwards, so 2026 | ΚΦΕ art. 16(1), as amended by ν. 5045/2023 art. 43; Codification |
| Phase-out of the art. 16 reduction | EUR 20 less per EUR 1,000 of taxable employment and pension income over EUR 12,000; not applied with 5 or more children | 2026 | ΚΦΕ art. 16(2); Codification |
| Extra tax reduction for disability of 67% or more (and the other groups in art. 17) | EUR 200 | 2026 | ΚΦΕ art. 17; Codification |
| Donations to approved bodies (over EUR 100 a year) | 20% of the donation off the tax, donations capped at 5% of taxable income; 40% for donations to charitable foundations and registered civil society organisations paid into dedicated bank accounts, capped at 40% of taxable income | 2026 | ΚΦΕ art. 19(1); Codification |
| Electronic payment spending requirement | 30% of real employment, pension and business income, spending capped at EUR 20,000; 20% if tax, ENFIA, loan and rent payments exceed 60% of real income; EUR 5,000 cap if bank accounts are seized | 2026 | ΚΦΕ art. 15(6)(b) and (στ); Codification |
| Tax on any shortfall in electronic spending | 22% of the shortfall | 2026 | ΚΦΕ art. 15(6)(b); Codification |
| Deduction for certain services paid electronically | 30% of the spending, up to EUR 5,000 off taxable income | 2022 to 2026 | ΚΦΕ art. 15(7)(a), as amended by ν. 5246/2025 art. 4(2); Codification |
| New business, first 3 years (first registration from 2013), gross business income up to EUR 10,000 | 1st-band rate cut by 50% | 2026 | ΚΦΕ art. 29(2); Codification |
| Minimum deemed income of the self-employed: cap | EUR 50,000 | 2025 onwards, so 2026 | ΚΦΕ art. 28A(2), as amended by ν. 5259/2025 art. 187; Codification |
| Minimum deemed income: base | Annual gross minimum wage at 31 December of the tax year, raised by 10% for years 7 to 9 of activity, by a further 10% of that amount for years 10 to 12 and by a further 10% for later years; plus 10% of staff costs (up to EUR 15,000); plus 5% of turnover above the average for the main activity code (KAD) | 2026 | ΚΦΕ art. 28A(2); Codification |
| Statutory minimum wage, white-collar workers | EUR 920.00 a month from 1 April 2026 (Ministerial Decision 8934/27.3.2026, Β' 1759) | 2026 | [Ministry of Labour, minimum wage](https://ypergasias.gov.gr/en/labour-relations/collective-employment-relations/minimum-wage/) |
| Prepayment of tax on business income | 55% of the tax on business income; half that in the first year with business income; not charged if EUR 30 or less | 2026 | ΚΦΕ art. 69(1) and (2); Codification |
| Dividends | 5% | 2026 | ΚΦΕ art. 40(1); Codification |
| Interest | 15%; 5% on qualifying listed corporate bonds held by residents; Greek government bonds and T-bills exempt | 2026 | ΚΦΕ art. 40(2) and art. 37(2) and (5); Codification |
| Royalties | 20% | 2026 | ΚΦΕ art. 40(3); Codification |
| Rental income: EUR 0 to 12,000 | 15% | 2026 | ΚΦΕ art. 40(4), as amended by ν. 5246/2025 art. 8; Codification |
| Rental income: EUR 12,000.01 to 24,000 | 25% | 2026 | same |
| Rental income: EUR 24,000.01 to 36,000 | 35% | 2026 | same |
| Rental income: over EUR 36,000 | 45% | 2026 | same |
| Deduction from gross rent, individual landlord | 5% | 2026 | ΚΦΕ art. 39(3)(a); Codification |
| Special solidarity contribution (art. 43A) | Abolished for all income from 1.1.2023 | 2023 onwards | ΚΦΕ art. 72(74); Codification |
| Benefits in kind tax-free allowance | First EUR 300 a year | 2026 | ΚΦΕ art. 13(1); Codification |
| Early-payment discount (tax paid in full by the first-instalment date) | 4% if the return is filed by 30 April, 3% by 15 June, 2% by 15 July | 2026 return | ΚΦΕ art. 67(6); Codification |

Codification: [Income Tax Code, Ministry of Finance codification up to ν. 5264/2025](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf)

## The taxable base

**Four categories.** Gross income is split into employment and pensions, business activity, capital (dividends, interest, royalties, rent) and capital gains (art. 7(2)). Employment, pension and business income are added together and taxed on the art. 15 scale (art. 29(1)). Capital income is taxed separately at its own rates (art. 40).

**Employees and pensioners.** Taxable income is gross pay minus the employee's compulsory social insurance contributions (art. 14(1)(δ)). Also excluded: business travel and subsistence refunds, meal vouchers up to EUR 6 a working day, gifts up to EUR 27 a year, health and life cover paid by the employer up to EUR 1,500 a year, and public transport passes (art. 14(1)). Benefits in kind above EUR 300 a year are taxed at market value; a company car is valued on a scale of its pre-tax retail price (art. 13). The employer withholds tax each month on the annualised salary, using the art. 15 scale and the art. 16 reduction (art. 60(1)). The return reconciles that withholding.

**The art. 16 tax reduction** applies only to tax on employment and pension income. It does not apply to business profit (art. 29(1)), or to rent, dividends or interest. If tax is lower than the reduction, the reduction is limited to the tax (art. 16(1)).

**Dependent children** (art. 11) are unmarried children up to 18, or up to 25 if studying, registered unemployed or doing military service, and children with a disability of 67% or more. A child with taxable income over EUR 3,000 (EUR 6,000 for a disabled child) is not a dependant.

**Low incomes with no business (art. 15(1A), new from 2026).** Where real income is EUR 6,000 or less, deemed living-expense income is EUR 9,500 or less, and the person runs no registered business or farm, that income and any added deemed-income difference are taxed on the scale with the art. 16 reduction. The part of real income above EUR 6,000 is taxed under art. 29(1), without the art. 16 reduction.

**Self-employed: profit.** Profit is business income minus deductible expenses (arts. 21 and 22). An expense is deductible if it is in the business's interest, is a real transaction at market value, and is recorded and documented. Not deductible (art. 23), among others: any purchase over EUR 500 not paid by bank means; unpaid social contributions; fines; income tax itself; personal consumption; entertainment; rent and staff costs not paid electronically. EFKA contributions of the self-employed are fixed monthly amounts by insurance category, not a percentage of profit. The 2026 amounts are in e-EFKA circular 6/2026 ([circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026)), and the category for a year is chosen in the e-EFKA online service open in December and January, applying from 1 January ([e-EFKA general document 1811441/13.07.2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/geniko-eggrafo-181144113-07-2026), section 7). Contributions actually paid are a business expense, so they reduce business profit (art. 22). They are not deducted from total taxable income. Unpaid contributions are not deductible (art. 23(γ)), and nor are late-payment surcharges (art. 23(ε)). The amounts, categories and deadlines are in `gr-efka`. Fees for technical work, management, consulting and similar services paid by a business are subject to 20% withholding (art. 64(1)(δ)). That tax is credited on the return (art. 67(6)) and is also deducted from the prepayment (art. 69(1)). A business loss is carried forward against business profit for 5 years (art. 27(1)). Losses of one spouse cannot be set against the other's income (art. 67(4)(ε)).

**Self-employed: minimum deemed income (arts. 28A to 28Γ, from ν. 5073/2023).** A sole trader's annual business income is presumed to be at least the art. 28A amount, capped at EUR 50,000:

1. the annual gross minimum wage in force on 31 December of the tax year, raised by 10% for years 7 to 9 of activity, by a further 10% of that raised amount for years 10 to 12, and by a further 10% of the years 10 to 12 amount after that (so 1.10, 1.21 and 1.331 times the base); plus
2. 10% of the year's staff costs, up to EUR 15,000; plus
3. 5% of the amount by which turnover exceeds the average turnover of the main activity code (KAD), as AADE publishes it by 30 September each year. This part does not apply if that average is EUR 10,000 or less, or the code has 30 or fewer businesses.

If the total is under EUR 30,000 and the best-paid employee earns more, that salary is the presumed income, up to EUR 30,000. The amount is reduced by any salary, pension or farm income the person has (art. 28B). It does not apply in the first 3 years of activity; it is cut by two thirds in year 4 and by one third in year 5 (art. 28Γ(1)). It is halved for parents of large families, people with a 67% disability, single parents of minors, some taxi owners and school canteen operators (art. 28Γ(2)), and for businesses based in small villages and islands (art. 28Γ(3): under 500 inhabitants; 500 to 1,500 outside Attica, 1,700 in some border areas; islands under 3,100). It does not apply at all to farm profit, to people treated as employees under art. 12(2)(στ) with up to 3 clients, to people with an 80% disability, to mothers in the year of birth or adoption and the next 2 years, and to the other cases of art. 28A(6). The amount is cut by 30% for street-market traders with KAD 47.81.10.02 or 47.89.10.02, from tax year 2025: ν. 5301/2026 art. 41 amended art. 28Γ (AADE circular Ε.2035/2026).

The presumption can be rebutted for objective reasons (military service, prison, hospital, pregnancy, natural disaster, licence withdrawal, closure by public order, force majeure) with evidence, or by asking for a tax audit under ΚΦΔ art. 23 for other reasons (art. 28A(3) and (4)).

**Deemed living-expense income (arts. 30 to 34).** Separately, if a person's deemed living expenses (homes, cars, boats, staff, school fees, asset purchases) exceed declared income, the difference is added and taxed. `gr-living-expense-presumptions` computes them.

**Electronic spending (art. 15(6)).** A resident must spend 30% of real employment, pension and business income (capped at EUR 20,000 of spending) by card, e-wallet or other electronic payment, on goods and services in Greece or the EU/EEA. Rent, car purchases and road tax do not count. The shortfall is taxed at 22%. Business income for this test is never less than the art. 28A minimum (art. 28A(5)). The requirement does not apply to people aged 70 or more, people with an 80% disability, non-residents, residents living or working abroad, minors, conscripts, people in villages up to 500 inhabitants or islands under 3,100 (except tourist areas), and the other groups in art. 15(6)(γ). Each spouse declares their own spending; a surplus can be moved to the other spouse on a joint return (art. 15(6)(ε)).

**Capital income.** Dividends: the 5% withheld at source is final for individuals (art. 36(2)). Interest: the withheld tax is final (art. 37(4)). Rent: gross rent minus 5% for property costs (art. 39(3)(a)), taxed on the separate art. 40(4) scale. Rent must be paid into the landlord's bank account notified to AADE, or the 5% deduction is lost (art. 39(5)). Unpaid rent is not taxed if legal action has started by the filing deadline (art. 39(4)). Short-term rental of up to 2 properties with no services other than linen is rental income; 3 or more properties, or extra services, make it business income (art. 39A(1)).

## Deadlines and filing

| Event | Deadline | Source |
|---|---|---|
| Election for separate returns by spouses | By 28 February of the filing year (28 February 2027 for 2026) | ΚΦΕ art. 67(4)(β) |
| Income tax return (form E1, with E2 for rent and E3 for business) via myAADE / TAXISnet | 15 March to 15 July 2027 for 2026 income. If the start date falls on a holiday or weekend, it moves to the next working day | ΚΦΕ art. 67(3) and (8); [AADE E1 instructions](https://www.aade.gr/sites/default/files/2026-03/Odigies_E1_2026_0.pdf) |
| Members of companies keeping single-entry books | By the last working day of July 2027 | ΚΦΕ art. 67(3) |
| Payment of the tax | 8 equal monthly instalments: the first by the last working day of July 2027, the rest by the last working day of each of the next 7 months (to February 2028) | ΚΦΕ art. 67(6) |
| Early-payment discount | Pay the whole tax by the first-instalment date: 4% off if filed by 30 April 2027, 3% by 15 June 2027, 2% by 15 July 2027 | ΚΦΕ art. 67(6) |
| Prepayment for 2027 | Assessed with the 2026 return at 55% of the tax on business income, paid with the same instalments | ΚΦΕ art. 69(1) |
| Request to cut the prepayment (income down by more than 25%) | By the end of September of the year of assessment | ΚΦΕ art. 70(1) |
| Person who dies or moves abroad | The return may be filed at any time during the year | ΚΦΕ art. 67(3) |

The tax due on the return is the tax on all income minus tax withheld, tax prepaid and foreign tax credited under art. 9. Any excess is refunded (art. 67(6)). The 2026 E1 form and its instructions are published by AADE in early 2027; the linked instructions are for 2025 income.

## Penalties and interest

From the Tax Procedure Code (ν. 5104/2024), AADE codification Ε.2109/2025:

| Breach | Penalty | Source |
|---|---|---|
| Late or missing return with no tax due | EUR 100 per breach | ΚΦΔ art. 53(1) |
| Late or missing tax return (with or without tax due), taxpayer keeping single-entry books | EUR 250 per breach | ΚΦΔ art. 53(2) |
| Same, taxpayer keeping double-entry books | EUR 500 per breach | ΚΦΔ art. 53(2) |
| No return filed where tax would be due | 50% of the tax on the missing return | ΚΦΔ art. 53(6) |
| Late original income tax return showing tax of EUR 100 or less; late amended return adding EUR 100 or less | No fine under art. 53(1) or (2) | ΚΦΔ art. 53(7)(β) and (γ) |
| Inaccurate return: tax difference 5% to 20% of the tax declared | 10% of the difference | ΚΦΔ art. 54(1)(a) |
| Difference over 20% and up to 50% | 25% of the difference | ΚΦΔ art. 54(1)(b) |
| Difference over 50% | 50% of the difference | ΚΦΔ art. 54(1)(c) |
| Late payment | Interest from the day after the payment deadline. For a late or amended return, interest runs from the original payment deadline | ΚΦΔ art. 52(1) |
| Missed electronic spending | 22% of the shortfall, added to the tax | ΚΦΕ art. 15(6)(b) |

The late-payment interest rate is set by ministerial decision, not in art. 52; we did not read the percentage on an official page (see Sources).

## Cross-border points

- **Non-residents** are taxed only on Greek-source income (salary for work in Greece, Greek pensions, rent from Greek property). They do not get the art. 16 to 19 reductions unless they live in another EU or EEA state and either earn at least 90% of their worldwide income in Greece or show their income is low enough to get the reduction at home (art. 20). The electronic spending rule does not apply to them (art. 15(6)(γ)(iv)). A non-resident with only Greek government bond interest does not have to file (art. 67(1)). Full rules: `gr-cross-border`.
- **Foreign income of residents** is taxed in Greece with a credit for foreign tax, capped at the Greek tax on that income (art. 9). Treaties decide which state taxes; a residence certificate is needed for treaty rates.
- **Moving to Greece**: the 5A lump sum, 5B 7% pensioner regime and 5C 50% exemption for workers are in `gr-cross-border`.
- **Withholding** on dividends, interest and royalties paid to non-residents, and the EU directive exemptions, are in `gr-cross-border`.
- **Sole trader who becomes a one-person company.** After an audit, AADE may tax the individual on the art. 28A minimum if they closed a sole business and carry on the same activity (same 2-digit KAD) through a one-person company, and the company tax plus dividend tax is lower than that minimum tax (art. 28E). This rule applies to income up to tax year 2026 (art. 28E(7)).

## Worked examples

### Example 1: employee with two children

Maria is a Greek-resident employee, aged 40, married, with 2 dependent children. Her 2026 salary after employee social contributions is EUR 30,000. She paid EUR 7,000 by card during 2026 on qualifying spending. She has no other income.

With 2 children the scale is 9% on the first 10,000 (900), 16% on the second band (1,600) and 22% on the third band (2,200): EUR 4,700. The art. 16 reduction for 2 children is EUR 1,120, minus EUR 20 for each EUR 1,000 over EUR 12,000. She is EUR 18,000 over, so the reduction falls by EUR 360 to EUR 760. Tax after the reduction is EUR 3,940.

She had to spend 30% of EUR 30,000, so EUR 9,000, electronically. She is EUR 2,000 short, which adds 22%, EUR 440. Total tax is EUR 4,380. Her employer withheld tax monthly under art. 60, so the return shows a balance due or a refund depending on what was withheld. If any balance is paid in full by the end of July 2027 and she filed by 30 April 2027, she gets 4% off it.

```oa-check
name: GR employee, salary EUR 30,000, 2 children, 2026 scale and art. 16 reduction
inputs:
  salary: 30000
  card_spend: 7000
steps:
  - b1: min(salary, 10000) * 0.09
  - b2: max(min(salary, 20000) - 10000, 0) * 0.16
  - b3: max(min(salary, 30000) - 20000, 0) * 0.22
  - b4: max(min(salary, 40000) - 30000, 0) * 0.34
  - b5: max(min(salary, 60000) - 40000, 0) * 0.39
  - b6: max(salary - 60000, 0) * 0.44
  - scale_tax: b1 + b2 + b3 + b4 + b5 + b6
  - reduction: max(1120 - max(salary - 12000, 0) / 1000 * 20, 0)
  - tax_after_reduction: max(scale_tax - reduction, 0)
  - required_spend: min(salary * 0.30, 20000)
  - shortfall_tax: max(required_spend - card_spend, 0) * 0.22
  - total_tax: tax_after_reduction + shortfall_tax
expected:
  scale_tax: 4700.00
  reduction: 760.00
  tax_after_reduction: 3940.00
  required_spend: 9000.00
  shortfall_tax: 440.00
  total_tax: 4380.00
```

### Example 2: freelancer with rent, prepayment due

Nikos is a Greek-resident freelance physiotherapist, aged 45, no children, in his 10th year of activity, with no staff. His clients are private individuals, so no tax was withheld at source. His turnover is below the average for his KAD. His 2026 business profit after expenses and EFKA is EUR 40,000. He also lets a flat for EUR 6,000 a year, paid into his bank account. He has filed business income before, so the full 55% prepayment applies. He met the 30% card-spending requirement.

With no staff and no turnover excess, his art. 28A minimum is 1.21 times the annual gross minimum wage (10% for years 7 to 9, then a further 10% of that for years 10 to 12). On EUR 920 a month that is under EUR 16,000 whether the year counts 12 or 14 monthly payments, well below EUR 40,000, so the minimum does not change his base (see "Not yet confirmed" for the exact annual figure). Business profit is taxed on the scale with no art. 16 reduction: 900 + 2,000 + 2,600 + 3,400 = EUR 8,900. The rent, after the 5% deduction, is EUR 5,700, taxed separately at 15%: EUR 855.

With the 2026 return he is also assessed a prepayment for 2027 of 55% of the tax on business income: EUR 4,895. Any prepayment assessed on his 2025 return is credited against the 2026 tax. Before that credit, the total assessed with the return is EUR 14,650, payable in 8 instalments from July 2027.

```oa-check
name: GR freelancer, profit EUR 40,000 plus rent EUR 6,000, 2026, with 55% prepayment
inputs:
  profit: 40000
  gross_rent: 6000
  prepay_rate: 0.55
steps:
  - b1: min(profit, 10000) * 0.09
  - b2: max(min(profit, 20000) - 10000, 0) * 0.20
  - b3: max(min(profit, 30000) - 20000, 0) * 0.26
  - b4: max(min(profit, 40000) - 30000, 0) * 0.34
  - b5: max(min(profit, 60000) - 40000, 0) * 0.39
  - b6: max(profit - 60000, 0) * 0.44
  - business_tax: b1 + b2 + b3 + b4 + b5 + b6
  - net_rent: gross_rent * (1 - 0.05)
  - r1: min(net_rent, 12000) * 0.15
  - r2: max(min(net_rent, 24000) - 12000, 0) * 0.25
  - r3: max(min(net_rent, 36000) - 24000, 0) * 0.35
  - r4: max(net_rent - 36000, 0) * 0.45
  - rent_tax: r1 + r2 + r3 + r4
  - prepayment: business_tax * prepay_rate
  - total_assessed: business_tax + rent_tax + prepayment
expected:
  business_tax: 8900.00
  net_rent: 5700.00
  rent_tax: 855.00
  prepayment: 4895.00
  total_assessed: 14650.00
```

## Ask the client first

1. Were you Greek tax resident for all of 2026, and is any income from abroad? This decides worldwide or Greek-only taxation and the art. 20 test.
2. What kinds of income did you have in 2026 (salary, pension, business, rent, dividends, interest) and how much of each? Salary and business share one scale; rent and capital income are taxed apart; the art. 16 reduction applies only to salary and pension.
3. How old are you, and how many dependent children do you have? Age under 31 and each child change the rates and the art. 16 reduction.
4. If self-employed: when did you first register the activity, do you have staff, which KAD is your main one, where is your business based, and do you fall in any art. 28A(6) or 28Γ exception? These decide the minimum deemed income and the prepayment rate.
5. How much did you spend by card or other electronic means in 2026? A shortfall below 30% costs 22%.
6. Are you married or in a registered partnership, and did either of you elect separate returns? This decides joint or separate filing.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Code (ν. 4172/2013), Ministry of Finance codification up to ν. 5264/2025: arts. 3, 7, 8, 11 to 17, 19 to 23, 27 to 30, 35 to 40, 60, 67, 69, 70, 72(74), with footnotes on ν. 5246/2025 and ν. 5259/2025 | https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf | 2026-10-23 |
| e-EFKA circular 6/2026 (2026 monthly contributions of the self-employed; detail in `gr-efka`) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026 | 2026-10-23 |
| e-EFKA general document 1811441/13.07.2026, section 7 (category change open December to January) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/geniko-eggrafo-181144113-07-2026 | 2026-10-23 |
| Ministry of Finance, notice of the codification | https://minfin.gov.gr/koinopoiisi-kodikopoiisis-tou-kodika-forologias-eisodimatos-symfona-me-to-arthro-83-par-55-tou-n-5104-2024/ | 2026-10-23 |
| Tax Procedure Code (ν. 5104/2024), AADE codification Ε.2109/2025: arts. 52, 53, 54 | https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf | 2026-10-23 |
| AADE, E1 return instructions (2025 income, filed 2026) | https://www.aade.gr/sites/default/files/2026-03/Odigies_E1_2026_0.pdf | 2026-10-23 |
| AADE circular Ε.2035/02-07-2026, 30% reduction of the art. 28A minimum for street-market KADs (ν. 5301/2026 art. 41, from tax year 2025) | https://www.aade.gr/egkyklioi-kai-apofaseis/e-2035-02-07-2026 | 2026-10-23 |
| Ministry of Labour, minimum wage (EUR 920 from 1 April 2026, decision 8934/27.3.2026, Β' 1759) | https://ypergasias.gov.gr/en/labour-relations/collective-employment-relations/minimum-wage/ | 2026-10-23 |
| Ministry of Labour, announcement of the new minimum wage in force from 1 April 2026 | https://ypergasias.gov.gr/se-ischy-apo-simera-o-neos-katotatos-misthos-ofelei-15-ekatommyrio-polites/ | 2026-10-23 |

Not yet confirmed: how AADE annualises the EUR 920 monthly minimum wage for the 2026 art. 28A minimum (the law says "annual amount of the gross minimum wage"; if 14 monthly payments are used, the base is EUR 12,880, but we did not read that figure or the multiplier on an official page); any amendment to the Income Tax Code made during 2026 after ν. 5264/2025, other than the ν. 5301/2026 change to art. 28Γ that AADE circular Ε.2035/2026 describes; the full text of ν. 5301/2026 (only its art. 41, as AADE circular Ε.2035/2026 describes it, was read); the percentage of the late-payment interest rate under ΚΦΔ art. 52 (set by ministerial decision); how the "analogous application" of the art. 15(6) electronic spending rule in art. 40(4) works for rental income; the 2026 E1 form and instructions, which AADE has not yet published.
