---
name: estonia-income-tax
description: Use this skill whenever asked about Estonia personal income tax for self-employed individuals (FIE) and resident individuals. Trigger on phrases like "how much tax do I pay in Estonia", "Estonian income tax return", "Form A", "Form E", "tuludeklaratsioon", "TSD", "FIE", "ettevõtluskonto", "entrepreneur account", "basic exemption", "maksuvaba tulu", "tax hump", "social tax", "sotsiaalmaks", "funded pension", "II pillar", "unemployment insurance", "töötuskindlustus", "flat 22% tax", "self-employed tax Estonia", or any question about filing or computing personal income tax for a resident or self-employed (FIE) client in Estonia. Also trigger when preparing or reviewing a Form A / Form E return, computing FIE business deductions, running payroll withholding via TSD, advising on FIE social-tax advance payments, or comparing the entrepreneur-account simplified regime. This skill covers the flat 22% income tax rate, the income-dependent basic exemption and its 2026 reform, social tax, unemployment-insurance premiums, funded (II) pension, the entrepreneur-account regime, payroll (TSD) declarations, filing deadlines, penalties, and interaction with VAT. ALWAYS read this skill before touching any Estonian income tax work.
version: 0.1
jurisdiction: EE
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia personal income tax: residents and sole proprietors (FIE)

## Scope

This Guide covers Estonian personal income tax for a **resident natural person** for tax year 2026 (the calendar year), with a dated section for the tax year 2025 return that was due by 30 April 2026. It covers:

- the flat income tax rate and the basic exemption, including the end of the 2025 "tax hump";
- income of employees (withholding through the employer), and other income declared on the annual return (form A);
- business income of a sole proprietor registered in the commercial register (FIE, füüsilisest isikust ettevõtja) on form E, with social tax, the mandatory funded pension (II pillar) and advance payments;
- the entrepreneur account (ettevõtluskonto) as an alternative to FIE status;
- tax residency, filing, payment, refunds and late-payment interest.

It does not cover companies (OÜ, AS) and their tax on distributions, non-residents and treaty relief, the investment-account system and securities or crypto-asset gains in detail, fringe benefits, or VAT returns. For VAT use the Estonia VAT return Guide; the points where VAT touches form E are below.

The law is the Income Tax Act (tulumaksuseadus), the Social Tax Act (sotsiaalmaksuseadus), the Funded Pensions Act, the Unemployment Insurance Act and the Simplified Business Income Taxation Act (for the entrepreneur account). The tax authority is the Estonian Tax and Customs Board (Maksu- ja Tolliamet, ETCB), with the e-services environment e-MTA.

## Ask the client first

- **Which tax year?** 2026 and 2025 use different basic-exemption rules. Taxation is cash-based: a December 2025 wage paid in January 2026 is taxed with 2026 rates.
- **Are you an Estonian tax resident?** You are resident if your place of residence is in Estonia, or you stay in Estonia at least 183 days in any 12 consecutive calendar months, or you are an Estonian diplomat in foreign service. If you might also be resident elsewhere, stop and refer (treaty tie-breaker).
- **Date of birth, and do you receive a pension?** In 2026 people born in or before 1961 are of pensionable age and get the higher fixed exemption for the whole year.
- **How do you earn?** Employment, FIE registered in the commercial register, entrepreneur account at LHV Pank, rental income, interest, dividends, sale of property, income from abroad. A mix is common.
- **Did you give an employer a written basic-exemption application, and to how many employers?** From 2026 only one employer may apply it.
- **Have you joined the II pillar, and at what rate (2%, 4% or 6%)?**
- **For an FIE:** registration date (and any suspension or deletion), total receipts including VAT, business expenses with documents, VAT registration, social-tax and income-tax advances paid, any employer or state paying social tax for you, whether you are a student, under 19, receiving a state pension or have partial or no work ability, losses carried forward, and whether you keep a special account.
- **Deductions:** training fees, donations to listed organisations, III-pillar contributions, and whether a spouse will share unused training expenses.

## The method, step by step

1. **Fix residency and the year.** Resident: all worldwide income is taxable in Estonia. Non-resident: only Estonian-source income, and this Guide does not apply.
2. **Pick the rate.** Income tax is a flat **22%** for 2026 and for 2025 (it was 20% for 2024). There are no brackets and no local income tax.
3. **Pick the basic exemption for the year** (see the figures table). For 2026: 700 euros a month or 8,400 euros a year for everyone below pensionable age, whatever their income. At pensionable age: 776 euros a month or 9,312 euros a year. For 2025, use the tax hump formula in the dated section.
4. **Employment income.** The employer withholds 22% monthly on the wage minus the employee's unemployment insurance premium (1.6%), minus the II-pillar contribution withheld, minus the monthly basic exemption if the employee gave that employer a written application. With no application, tax is withheld from the first euro. The employer pays social tax (33%) and its own unemployment premium (0.8%) on top and declares everything on form TSD by the 10th of the next month.
5. **FIE business income (form E).** Receipts in the year (cash basis, including VAT) minus documented business expenses paid in the year (including VAT paid and fixed-asset purchases), minus any loss carried forward. Then:
   - **Social tax** = that amount ÷ 1.33 × 33%, but never less than the annual minimum (12 × the monthly rate × 33%) unless exempt, and never more than the annual maximum.
   - **Income for income tax** = that amount ÷ 1.33. If the minimum or maximum social tax applies instead, income for income tax = amount after expenses minus that minimum or maximum social tax.
   - **II pillar** (if joined) = income adjusted by social tax × chosen rate, capped.
6. **Add other income on form A** (rental income with no tax withheld, interest, income from abroad, gains on property), apply deductions (basic exemption; training expenses and donations up to 1,200 euros together; III-pillar contributions up to 15% of taxable income and 6,000 euros), and compute 22% on the remainder.
7. **Credit tax already withheld and advances paid**; the ETCB computes the balance. Pay any additional tax, FIE social tax and II-pillar contribution by 1 October of the following year; refunds are paid by the same date at the latest.
8. **Entrepreneur account instead of FIE:** the bank withholds 20% (22%, 24% or 26% with the II pillar) of every receipt. No expenses, no deductions, no return figures to compute.

## Figures with years

All amounts in euros. "2026" is the year in force now; the 2025 column is for the return filed in 2026.

### Income tax and basic exemption

| Item | 2026 | 2025 | Source |
| --- | --- | --- | --- |
| Income tax rate (resident natural person) | 22% | 22% (20% in 2024) | [ETCB tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Basic exemption, below pensionable age | 700 a month, 8,400 a year, not income-dependent | Up to 654 a month, up to 7,848 a year, reduced by the tax hump | [Calculation of basic exemption](https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption) |
| Basic exemption at pensionable age | 776 a month, 9,312 a year | 776 a month, 9,312 a year | [Basic exemption at pensionable age](https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/basic-exemption-pensionable-age) |
| Who is of pensionable age for the year | Born in or before 1961 | Born in or before 1960 (reached pensionable age in 2025 or earlier) | Basic exemption at pensionable age |
| Training expenses plus gifts and donations | Up to 1,200 a year together, not more than taxable income | Same | [Income tax returns for 2025](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/income-tax-returns-2025) |
| III-pillar (supplementary funded pension) contributions | Up to 15% of taxable income, maximum 6,000 a year, outside the 1,200 limit | Same | [III-pillar contributions](https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/contributions-supplementary-funded-pension) |
| Renting out a dwelling | 20% of the rent deducted automatically; not for short-term accommodation or sub-letting | Same | Income tax returns for 2025 |
| Dividends taxed at 14/86 before 2025 and passed on to an individual | 7% withheld | 7% withheld | [ETCB tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |

The 2026 rate stayed at 22%. Earlier commentary had announced a 24% rate and a separate security tax from 2026; the ETCB 2026 rates list only the 22% rate, so do not use 24% for personal income tax. The 24% figure that does apply is the standard **VAT** rate.

### Payroll and social contributions

| Item | 2026 | 2025 | Source |
| --- | --- | --- | --- |
| Social tax (employer, or FIE on own income) | 33% | 33% | [ETCB tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Monthly rate for the minimum social tax | 886, so at least 292.38 a month | 820, so at least 270.60 a month | [ETCB tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Unemployment insurance premium | Employee 1.6%, employer 0.8% | Same | [ETCB tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Mandatory funded pension (II pillar), employee | 2% default; 4% or 6% on application (by 30 November, from 1 January) | Same | [ETCB tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Health promotion costs exempt per employee | 400 a year | 400 a year | [ETCB tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Minimum wage (full-time month / hour) | 946 / 5.67 from 1 April 2026 (886 / 5.31 in January to March) | 886 / 5.31 | [ETCB tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |

The minimum wage and the social-tax monthly rate are different figures. In 2026 the monthly rate is 886 while the minimum wage rose to 946 from 1 April; the FIE maximum below uses both.

The employee's unemployment premium stops at the end of the month in which the employee reaches pensionable age or is granted an early retirement or flexible old-age pension. The employer's 0.8% continues.

### FIE (sole proprietor) figures

| Item | 2026 | 2025 | Source |
| --- | --- | --- | --- |
| Quarterly social-tax advance | 877.14 (886 × 3 × 33%) | 811.80 (820 × 3 × 33%) | [Social-tax advances](https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/payment-advance-payments-social-tax) |
| Annual minimum social tax (unless exempt) | 3,508.56 (886 × 12 × 33%) | 3,247.20 (820 × 12 × 33%) | Social Tax Act § 2(5) with the monthly rate |
| Annual maximum social tax | 36,867.60 | 35,085.60 | [FIE social tax](https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/social-tax) |
| Maximum II-pillar contribution | 2,234.40 at 2%; 4,468.80 at 4%; 6,703.20 at 6% | Not quoted here | [FIE funded pension](https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/contribution-mandatory-funded-pension) |
| Income-tax advance not payable if one quarterly amount is | 300 or less | 300 or less | [FIE income tax](https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/income-tax) |
| Entertaining guests and partners | Up to 2% of business income after other deductions, plus up to 32 a month | Same | [Deduction limits](https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/deduction-expenses-and-limitations-thereon) |
| Advertising gifts | Deductible if each is worth up to 10 without VAT | Same | Deduction limits |
| Loss (expenses over income) carried forward | Up to ten following years | Same | [Expenses carried forward](https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/expenses-carried-forward) |

### Entrepreneur account (LHV Pank only)

| Item | 2026 | Source |
| --- | --- | --- |
| Business income tax on every receipt | 20%; 22%, 24% or 26% if in the II pillar at 2%, 4% or 6% | [Entrepreneur account](https://www.emta.ee/en/private-client/taxes-and-payment/taxable-income/entrepreneur-account) |
| Split of the 20% | Income tax 22/55, social tax 33/55 | Entrepreneur account |
| Receipts that force registration as FIE or company and for VAT | Over 40,000 in a calendar year | Entrepreneur account |
| Monthly receipts needed for health insurance (no II pillar) | At least 2,436.50 | Entrepreneur account |
| Higher 40% rate | Abolished from 1 January 2025 | Entrepreneur account |

### 2025 return (filed by 30 April 2026): the tax hump

For **2025 income only**, the basic exemption for a person below pensionable age depended on annual income:

| Annual income in 2025 | Basic exemption |
| --- | --- |
| Up to 14,400 | 7,848 |
| Over 14,400 up to 25,200 | 7,848 − 7,848 ÷ 10,800 × (income − 14,400) |
| Over 25,200 | 0 |

Source: [Calculation of basic exemption](https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption), section "Calculation of basic exemption until the end of 2025", and Income Tax Act § 23.

"Annual income" for this test is wide. It includes taxable income (including foreign income), income from abroad not taxed in Estonia, dividends taxed at company level at 22/78 or with 7% withheld, business income, gains, rent, royalties, interest, taxable state pension, and III-pillar payments taxed at the 22% rate before pensionable age. It excludes tax-exempt benefits and tax-exempt or 10%-taxed II- and III-pillar payments. An employer could apply up to 654 a month during 2025; the return then recomputed the exemption for the year, which is why many 2025 returns show additional tax.

2025 return dates: filing opened on 16 February 2026 and closed on 30 April 2026; refunds started on 5 March 2026 (e-MTA) and 18 March 2026 (paper); additional tax and refunds are due by 1 October 2026. A 2025 return can still be corrected in e-MTA; in 2026 the 2023, 2024 and 2025 returns can be corrected.

## FIE rules in detail

**Registration matters.** Only a person registered as an FIE may deduct business expenses. An FIE must file form E with form A every year, even with no business income or no activity. Business income is taxed in the year it is received, including during suspension or after the business ends.

**Income (form E).** Money from selling goods and services, business grants and benefits, rent or licence fees from business property, the market price of business property taken into personal use, and VAT refunded by the ETCB. Receipts are entered **including VAT**. An employment wage, a loan received, and receipts on an entrepreneur account are not FIE business income. Tax accounting is cash-based even if the books are kept on the accrual basis.

**Expenses.** Deduct documented expenses paid in the year that relate to the business: goods, services, rent of business premises, fixed assets when bought, repairs, staff wages with their social tax and employer unemployment premium, business interest, business insurance, licences, business-related training, and state taxes connected with the business including VAT paid. Expenses are entered **together with VAT paid**. Only the business part of a mixed-use cost is deductible. Costs of registering as an FIE are deductible even if paid before registration.

**Not deductible:** income tax on business income (including its advances), the FIE's own social tax and its advances, the FIE's own II-pillar contribution (it goes on form A, table 9.1), fines, penalty payments and interest under the Taxation Act (except interest under an approved instalment schedule), amounts paid for a service to a person taxed on it through an entrepreneur account (Income Tax Act § 34 clause 13), and private living costs.

**Health costs and trip meals.** The FIE's own health costs may be deducted up to 400 a year (2025 and 2026), on the same conditions as for employees (Income Tax Act § 33(4) with § 48(5⁵)). The FIE's own meals on a temporary business trip abroad are deductible up to 50 a day for the first 15 days and 32 a day from the 16th day, if the business is mainly carried on in Estonia. Other own meals are private.

**Social tax adjustment (Income Tax Act § 14(5³) to (5⁵)).** After expenses, the result is divided by 1.33; the ETCB computes income tax on that adjusted income and social tax of 33% on it. Two limits apply:

- If 33% of the adjusted income is **below** the annual minimum, the FIE owes the minimum (unless exempt), and income tax is computed on income after expenses **minus the minimum social tax**. If the minimum is larger than that income, the excess is carried forward as a loss.
- If 33% of the adjusted income is **above** the annual maximum, the FIE owes only the maximum, and income tax is computed on income after expenses **minus the maximum social tax**.

Social tax that an employer or the state paid for the FIE in the year counts toward the minimum (Social Tax Act § 2(7)). An employed FIE whose business income is small pays only the part of the minimum not already covered, not the full 3,508.56 on top. It never pays less than 33% of its adjusted business income. The minimum does not apply for a whole year in which the FIE received a state pension, had partial or no work ability, or was treated as insured as a student. It is reduced day by day for part-year registration and similar changes.

**Social-tax advances.** Paid each quarter by 16 March, 15 June, 15 September and 15 December 2026 (877.14 a quarter). Not payable by an FIE who receives a state pension (including a flexible pension), has partial or no work ability, is a student as defined in the Health Insurance Act, or is under 19. If an employer or the state pays social tax for the FIE of at least 877.14 in the quarter, no advance is due; if it pays less, the FIE pays the difference. Part-quarter liability is computed by days (for example 877.14 ÷ 91 × 50 = 487.50). Advances are credited against the annual social tax; overpayments are refunded.

**Income-tax advances (Income Tax Act § 47).** An FIE who had business income in the previous year pays advances by 15 September and 15 December. Each advance = the previous year's taxable business income adjusted by social tax (the form E figure after dividing by 1.33) × that year's income tax rate ÷ 4. The basic exemption and other form A deductions are not subtracted (the ETCB's own example multiplies 5,455 of adjusted business income by 0.22 and divides by 4). None are due in the first year of business, if one quarterly amount is 300 or less, if the previous year had no taxable business income, or while the business is registered as temporary or seasonal or is suspended. The ETCB may reduce or waive future advances on a reasoned application showing that this year's income will be considerably lower.

**II pillar.** An FIE who has joined pays the contribution once a year, computed by the ETCB on income adjusted by social tax, due by 1 October, within the maximums in the figures table. No contribution is due for a year with no taxable income.

**VAT.** An FIE must register for VAT once its taxable supplies in Estonia exceed 40,000 from the start of a calendar year ([registration as a VAT payer](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer)); see the Estonia VAT return Guide.

**Special account.** An FIE may keep one special account for business receipts, moved there within ten working days of receipt. The year's increase in its balance is deducted from business income (not beyond business income after expenses), and a decrease is added back. Tax is deferred, not removed. Interest on the account is business income unless the bank withheld tax.

**Unemployment insurance.** An FIE pays none for itself; as an employer it pays and withholds it on staff wages.

## Boundaries and exceptions

| Situation | Treatment | Watch for |
| --- | --- | --- |
| Income of exactly 14,400 in 2025 | Full 7,848 exemption (the taper starts only above 14,400) | 2025 only; there is no taper in 2026 |
| Income of exactly 25,200 in 2025 | Exemption 0 (7,848 − 7,848 ÷ 10,800 × 10,800) | Above 25,200 it stays 0 |
| Two employers in 2026 | Only one may apply the basic exemption | If two did, the return collects the extra tax |
| Employee gave no application | Tax withheld from the first euro; the unused exemption comes back through the return | Refund by 1 October at the latest |
| Monthly wage below 700 | Exemption used only up to the wage; unused months are not carried to later months during the year | The return gives the full 8,400 for the year |
| Person with only rent or interest income | Exemption given only through the return | No employer to apply it |
| Reaches pensionable age during 2026 | 9,312 for the whole year from 1 January; the general exemption no longer applies | Pension and wage do not each get an exemption |
| Flexible or favourable-condition pension before pensionable age | General exemption (700 a month in 2026) until the year of pensionable age | Apply to the Social Insurance Board to have it used on the pension |
| Employed pensioner whose pension is below 776 | May ask the employer to apply the difference (for example 776 − 676 = 100) | Only after the pension uses its share |
| FIE start or end mid-quarter | Social-tax advance by days | Quarter lengths: 90, 91, 92, 92 days in 2026 |
| FIE also employed with employer social tax of at least 877.14 a quarter | No social-tax advance | Employer social tax counts toward the annual minimum, so the FIE owes the larger of 33% of its adjusted business income and the minimum minus the social tax the employer or state paid (Social Tax Act § 2(7)) |
| FIE income-tax advance of exactly 300 a quarter | Not payable ("does not exceed 300") | 300.01 or more is payable |
| FIE result below zero | Loss carried forward up to ten years | Minimum social tax above income also becomes a loss carried forward |
| Entrepreneur-account receipts reach over 40,000 in the year | Must register as FIE or company and for VAT | No deductions on entrepreneur-account income, and its income-tax part is not a credit on form A |
| Entrepreneur account used for a service to a resident company, non-profit association, foundation or religious association | The payer owes 22/78 income tax on the payment | Not for goods, and not where the payer is the state, a local authority, a legal person in public law or a non-resident company |
| Sale of goods by an individual | Income from selling goods or handicrafts is taxable (form A line 6.3); property that was in personal use is not taxed; regular, profit-seeking selling is business income on form E and requires registration | Treat platform income the same way |
| Short-term letting (Airbnb, Booking.com) | Declared as other rental income without the 20% deduction | 20% applies only to renting out a dwelling |

## Worked cases

These are estimates built from ETCB rules. The ETCB computes the final amounts from the return.

**Case 1: employee, monthly wage, 2026.** Gross wage 2,000 in a month of 2026. II pillar at 2%. The employee gave this employer (and no other) an application for 700.
- Unemployment premium withheld: 2,000 × 1.6% = 32.00
- II-pillar contribution withheld: 2,000 × 2% = 40.00
- Income tax: (2,000 − 32 − 40 − 700) × 22% = 1,228 × 22% = 270.16
- Net pay: 2,000 − 32 − 40 − 270.16 = 1,657.84
- Employer on top: social tax 2,000 × 33% = 660.00 and unemployment premium 2,000 × 0.8% = 16.00, so total cost 2,000 + 660 + 16 = 2,676.00. Declared on form TSD and paid by the 10th of the next month.
Without an application, income tax would be (2,000 − 32 − 40) × 22% = 1,928 × 22% = 424.16 each month, and the unused exemption would come back on the 2026 return.

**Case 2: FIE, ordinary profit, 2026.** Registered all year, born in 1985, not in the II pillar, no other income. Receipts 50,000 and business expenses 20,000 (both including VAT; the FIE is not VAT-registered).
- Income after expenses: 50,000 − 20,000 = 30,000
- Adjusted for social tax: 30,000 ÷ 1.33 = 22,556.39
- Social tax: 22,556.39 × 33% = 7,443.61. This is between the minimum 3,508.56 and the maximum 36,867.60, so it stands.
- Income tax: (22,556.39 − 8,400) × 22% = 14,156.39 × 22% = 3,114.41
- Social-tax advances paid in 2026: 4 × 877.14 = 3,508.56, so the social-tax balance is 7,443.61 − 3,508.56 = 3,935.05, payable by 1 October 2027 with any income-tax balance.
- Income-tax advances in 2027: 22,556.39 × 22% ÷ 4 = 1,240.60 on each date. The formula does not subtract the basic exemption. That is over 300, so this FIE pays 1,240.60 by 15 September and 1,240.60 by 15 December 2027.

**Case 3: FIE, small profit, 2026 (minimum social tax).** Same person, income after expenses 5,000.
- 5,000 ÷ 1.33 = 3,759.40, and 3,759.40 × 33% = 1,240.60, which is below the minimum 3,508.56.
- Social tax is the minimum: 3,508.56 (already covered by the four advances).
- Income for income tax: 5,000 − 3,508.56 = 1,491.44, which is below the 8,400 exemption, so income tax is 0.

**Case 4: FIE, high profit, 2026 (maximum social tax).** Income after expenses 150,000, not in the II pillar, no other income.
- 150,000 ÷ 1.33 = 112,781.95, and 112,781.95 × 33% = 37,218.05, which is above the maximum 36,867.60.
- Social tax is the maximum: 36,867.60.
- Income for income tax: 150,000 − 36,867.60 = 113,132.40
- Income tax: (113,132.40 − 8,400) × 22% = 104,732.40 × 22% = 23,041.13

**Case 5: 2025 return with the tax hump.** Below pensionable age in 2025. Annual income for the exemption test and taxable income before the exemption are both 18,000 (for example only interest income, with no other deductions).
- Exemption: 7,848 − 7,848 ÷ 10,800 × (18,000 − 14,400) = 7,848 − 2,616 = 5,232
- Income tax: (18,000 − 5,232) × 22% = 12,768 × 22% = 2,808.96
- Compare 2026: the same income gets the full 8,400, so (18,000 − 8,400) × 22% = 2,112.00.

**Case 6: pensionable age, 2026.** Born in 1960, old-age pension 9,000 and interest 3,000 in 2026.
- Exemption 9,312 for the whole year.
- Income tax: (12,000 − 9,312) × 22% = 2,688 × 22% = 591.36. The Social Insurance Board uses the exemption against the pension first; the return settles the rest.

**Case 7: entrepreneur account, 2026.** Receipts 30,000 for babysitting and tutoring, not in the II pillar.
- Business income tax withheld by the bank: 30,000 × 20% = 6,000, of which income tax 6,000 × 22/55 = 2,400 and social tax 6,000 × 33/55 = 3,600.
- Receipts are under 40,000, so no FIE or VAT registration is required. With the II pillar at 2% the rate would be 22%: 30,000 × 22% = 6,600.

## Quick classification of bank lines (FIE)

| Line on the statement | Treatment |
| --- | --- |
| Customer payment (ARVE, MAKSE, ÜLEKANNE), Stripe, PayPal, Wise, platform payouts | Business income on form E, gross including VAT; match payouts to invoices |
| VAT refund from the ETCB | Business income |
| VAT paid to the ETCB (KÄIBEMAKS, KMD) | Business expense (VAT paid) |
| Rent of premises, software, hosting, bank and card fees, accountant, insurance, business training | Business expense if documented |
| Laptop, equipment, furniture, vehicle bought for the business | Expense when paid; business share only if also used privately |
| Phone, internet, fuel, home utilities | Business share only; no records means no deduction |
| Meals, accommodation, transport or entertainment for guests and business partners | Within the limit of 2% of business income plus 32 a month |
| Gifts to customers or partners | Deductible only as advertising items worth up to 10 each without VAT |
| The FIE's own meals (restaurant, café) | Private, not deductible, except meals on a temporary business trip abroad within the daily limits |
| Payment for a service into someone's entrepreneur account | Not deductible |
| Groceries, personal shopping, drawings, own-account transfers | Not income, not an expense |
| Loan received or principal repaid | Not income, not an expense; business loan interest is deductible |
| Social-tax advance (SOTSIAALMAKS), income-tax advance, income tax (TULUMAKS), fines, tax interest | Not an expense; advances are credits against the annual tax |
| Wage (PALK) from an employer | Employment income, already taxed through form TSD; form A |

## When to refuse or refer

Refer to an Estonian tax adviser, or decline, when:

- residency is unclear, the person arrived or left during the year, or may be resident in two countries (form R, treaty tie-breaker);
- the person is non-resident, or has foreign income needing a credit or exemption method, or an FIE has a permanent establishment abroad;
- the question is about a company (OÜ, AS), distributions, or whether to incorporate;
- securities, investment accounts, crypto-assets or sale of immovable property need a gain computed;
- fringe benefits, share options, or employer compensation schemes arise;
- the FIE is also an employer with payroll errors, uses a special account, carries forward old losses, is on sick leave that should reduce the social-tax base, or is transferring or closing the business;
- tax arrears, instalment plans or an ETCB audit are involved, or the client wants to challenge a decision;
- the figures you need are not published yet. State the last published figure with its year instead of guessing.

## Filing and payment

| Obligation | Deadline | Source |
| --- | --- | --- |
| Annual return, form A (and form E for every FIE), for 2026 | 30 April 2027; e-MTA opens from 15 February (next working day if a holiday) | [FIE income tax](https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/income-tax) |
| Additional income tax, FIE social tax and FIE II pillar for 2025 | 1 October 2026 | [Refund and additional payment](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/refund-and-additional-payment-income-tax) |
| Refund of overpaid 2025 income tax | From 5 March 2026 if e-filed without further checks; by 1 October 2026 at the latest | Refund and additional payment |
| FIE social-tax advances 2026 | 16 March, 15 June, 15 September, 15 December | [FIE tax calendar](https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/self-employed-persons-tax-calendar) |
| FIE income-tax advances 2026 | 15 September and 15 December | FIE tax calendar |
| Employer form TSD and payment | 10th of the month after payment | FIE tax calendar |
| VAT return (KMD, KMD INF) if registered | 20th of every month | FIE tax calendar |
| Correction of a return | Up to three years back (in 2026: 2023 to 2025) | Income tax returns for 2025 |

If a due date falls on a public holiday or rest day, the next working day counts.

**Who must file.** Everyone with an FIE registration; anyone with income on which no tax was withheld (platform fees, rent, foreign income, gains, crypto-assets), anyone who used more basic exemption than allowed, used an investment account, or wants a refund for training costs, donations, III-pillar contributions or unused exemption. No return is needed if all tax was correctly withheld (or for 2025 income, income did not exceed 7,848, or 9,312 at pensionable age).

**How.** In e-MTA (ID card, Mobile-ID, Smart-ID or EU eID); the return is pre-filled with wages, pensions, benefits, withheld rent, Nasdaq Baltic trades, dividends, entrepreneur-account amounts, unemployment and II-pillar contributions, III-pillar contributions, training fees and donations. Fields are filled in Estonian. Paper returns go to a service bureau or by post. The ETCB does not issue paper tax notices to e-filers; the amount due is on the return's information page.

**Late payment.** Interest runs from the day after the due date at 0.06% a day (21.9% a year) until payment ([payment of interest](https://www.emta.ee/en/private-client/taxes-and-payment/payment-arrears/payment-interests)). The ETCB does not issue an interest claim under 10 euros, and interest is rounded to whole euros. Instalment plans are applied for in e-MTA. Arrears are taken from any refund first. Penalties for late or wrong returns are not covered here; refer.

## Completion checklist

- [ ] Residency confirmed for the whole year (and form R filed on arrival or departure).
- [ ] Year confirmed; 2026 uses 8,400 flat, 2025 uses the tax hump.
- [ ] Pensionable age checked from the year of birth (2026: born in or before 1961).
- [ ] Only one employer applied the monthly exemption in 2026.
- [ ] Pre-filled income and deductions checked against payslips and certificates.
- [ ] FIE: receipts and expenses entered including VAT, private shares removed, fixed assets expensed when paid.
- [ ] FIE: guest and partner hospitality within 2% plus 32 a month; gifts only as advertising items of at most 10 each; own meals private except trip meals abroad.
- [ ] FIE: employer or state social tax counted toward the annual minimum.
- [ ] FIE: social tax adjusted by 1.33, then tested against the minimum (unless exempt) and the maximum.
- [ ] FIE: social-tax and income-tax advances reconciled; exemptions from advances checked.
- [ ] FIE: II-pillar status and rate confirmed; contribution within the cap.
- [ ] Training plus donations within 1,200; III pillar within 15% and 6,000.
- [ ] Entrepreneur-account receipts not repeated on form E, and not used for deductions.
- [ ] Filing by 30 April; balance paid or refund expected by 1 October.
- [ ] Anything on the refer list escalated.

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
