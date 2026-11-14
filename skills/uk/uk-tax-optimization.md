---
name: uk-tax-optimization
description: "Use this skill whenever asked about reducing tax in the UK, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for self-employed individuals in the UK, for tax year 2026/27 (6 April 2026 to 5 April 2027). Trigger on phrases like 'reduce tax', 'tax planning', 'save tax', 'optimize', 'allowances', 'deductions I'm missing', 'pay less tax', 'tax-efficient', 'tax minimization', 'how to lower my tax bill', 'sole trader or limited company 2026'. Covers 2026/27 bands, incorporation, salary and dividends, simplified expenses, capital allowances (14% main pool, 40% first-year allowance), loss relief, pensions, ISAs, EIS, SEIS and VCT (20% from April 2026), VAT schemes and anti-avoidance red lines. Out of scope (see siblings uk-self-employment-sa103, uk-dividends, uk-national-insurance, uk-vat-return). ALWAYS read this skill before advising on any UK tax optimization strategy."
version: "2.0"
type: decision
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-14
source_checked: 2026-11-14
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
---

# UK Tax Optimization

Tax year in force: 2026/27 (6 April 2026 to 5 April 2027). Every figure below was read on the official page on 14 November 2026.

Changelog v2.0 (2026-11-14): rebuilt on the standard method headings; every rate row carries its official URL; the Flat Rate Scheme 1% first-year discount now cites the Flat Rate Scheme page (it cited the simplified expenses page); the zero-emission car 100% allowance end date moved to "Not yet confirmed"; the incorporation case now shows the deciding figure. Earlier, v1.1 (2026-10-23): every figure moved to 2026/27 with the year named; dividend rates 10.75% / 35.75% / 39.35%; employer NIC 15% above GBP 5,000; 55p mileage; 14% main pool and 40% first-year allowance (Finance Act 2026 ss.28 and 29); VCT relief 20% (FA 2026 s.15); voluntary Class 2 abroad withdrawn; Example 2 (incorporation) recomputed, it previously applied corporation tax to the dividend instead of the profit; accountant attribution removed; Capital Goods Scheme values taken from VAT Regulations 1995 reg 113; simplified expenses no longer tied to the cash basis; the List 3 condition for traders removed; the zero-emission car allowance dated; em dashes removed.

## Scope

This skill sets out the legal options a UK self-employed person (or the owner of a small company) has to lower tax in 2026/27, side by side with the figure that decides each one, and the anti-avoidance lines that must not be crossed. It is for England, Wales and Northern Ireland income tax rates; Scottish rates differ.

Out of scope: the SA103 computation itself (`uk-self-employment-sa103`), dividend tax in detail (`uk-dividends`), National Insurance in detail (`uk-national-insurance`), and the VAT return (`uk-vat-return`).

### Quick reference

- **Country:** United Kingdom
- **Key optimization legislation:** Income Tax Act 2007 (ITA 2007); Income Tax (Trading and Other Income) Act 2005 (ITTOIA 2005); Income Tax (Earnings and Pensions) Act 2003 (ITEPA 2003); Capital Allowances Act 2001 (CAA 2001); Finance Act 2026
- **Tax authority attitude to planning:** HMRC accepts legitimate tax planning but actively pursues avoidance. The General Anti-Abuse Rule (GAAR) under Finance Act 2013 s.206-215 applies to arrangements that are "abusive", that is not a reasonable course of action. The Promoters of Tax Avoidance Schemes (POTAS) regime and Disclosure of Tax Avoidance Schemes (DOTAS) requirements apply.
- **Currency:** GBP
- **Tax year:** 6 April to 5 April (this skill: 2026/27)
- **Filing deadline:** 31 January following the tax year (online Self Assessment)

## Ask the client first

- What is your expected profit for 2026/27, and your other income (employment, savings, dividends, rent)?
- Are you a sole trader, a partner, or do you own a limited company? Are you thinking of incorporating?
- Is your adjusted net income near GBP 100,000 (the Personal Allowance taper) or GBP 50,270 (higher rate)?
- What pension contributions have you made this year and in the last 3 years (carry forward)? Have you flexibly accessed a pension?
- Do you plan to buy equipment, vans or cars? New or second hand? What CO2 emissions?
- Do you have trading losses, or expect any?
- Is your turnover near the VAT threshold? What share of your customers can recover VAT?
- Does a spouse or family member do genuine work in the business?
- Are you in Scotland? (Scottish income tax rates are not in this skill.)

## The method, step by step

1. **Set the client's position**: profit, total income, marginal rate (with the 60% band between GBP 100,000 and GBP 125,140) and NIC position, using the rates table.
2. **Check the deductions first** (deductions most people miss, simplified expenses): they are risk-free.
3. **Time capital expenditure**: AIA, the 40% first-year allowance and the main pool.
4. **Test pension contributions** against the marginal rate and the Personal Allowance taper, within the annual allowance and carry forward.
5. **Compare structures both ways** where profits justify it: sole trader against company (salary at the Primary Threshold plus dividends), and decide on the total cost figure (Worked cases, Case 2).
6. **Use losses** in the best year within the cap.
7. **Review VAT schemes** (threshold, Flat Rate Scheme, cash and annual accounting).
8. **Check every step against the red lines** (GAAR, DOTAS, IR35, disguised remuneration, commerciality) before recommending it.

### Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
| --- | --- | --- | --- |
| Personal Allowance | GBP 12,570, reduced by GBP 1 for every GBP 2 of adjusted net income over GBP 100,000; zero at GBP 125,140 | 2026/27 | https://www.gov.uk/income-tax-rates |
| Basic, higher, additional rates | 20% to GBP 50,270; 40% to GBP 125,140; 45% above | 2026/27 | same |
| Dividend allowance and rates | GBP 500; 10.75%, 35.75%, 39.35% | 2026/27 | https://www.gov.uk/tax-on-dividends |
| Class 4 NIC | 6% on profits GBP 12,570 to 50,270; 2% above | 2026/27 | https://www.gov.uk/self-employed-national-insurance-rates |
| Class 2 NIC | Treated as paid if profits GBP 7,105 or more; voluntary GBP 3.65 a week below | 2026/27 | same |
| Employer NIC | 15% above the Secondary Threshold of GBP 5,000; Lower Earnings Limit GBP 6,708; Primary Threshold GBP 12,570 | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Corporation tax | 19% up to GBP 50,000; 25% over GBP 250,000; marginal relief between | FY 2026 | https://www.gov.uk/corporation-tax-rates |
| Simplified mileage | 55p a mile for the first 10,000 miles, 25p after (45p for the first 10,000 before 6 April 2026) | 2026/27 | https://www.gov.uk/simpler-income-tax-simplified-expenses/print |
| Simplified use of home | GBP 10 a month (25 to 50 hours), GBP 18 (51 to 100), GBP 26 (101 and more) | 2026/27 | same |
| Annual Investment Allowance | GBP 1,000,000 | 2026/27 | https://www.gov.uk/capital-allowances/annual-investment-allowance |
| Main pool writing down allowance | 14% (18% before April 2026) | From April 2026 | https://www.legislation.gov.uk/ukpga/2026/11/section/28 |
| 40% first-year allowance | New, unused, not second-hand main-rate plant, not cars | From 1 January 2026 | https://www.legislation.gov.uk/ukpga/2026/11/section/29 |
| Special rate pool and cars | 6% special rate; cars 50g/km or less main rate (14%); new and unused 0g/km or electric 100% first-year allowance | 2026/27 | https://www.gov.uk/capital-allowances/business-cars |
| Structures and Buildings Allowance | 3% a year (10% on special tax site expenditure) | 2026/27 | https://www.legislation.gov.uk/ukpga/2001/2/section/270AA |
| Sideways loss relief cap | Greater of GBP 50,000 or 25% of adjusted total income | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/24A |
| Early trade losses | Losses in the first 4 tax years carried back against the 3 earlier tax years | ITA 2007 s.72 | https://www.legislation.gov.uk/ukpga/2007/3/section/72 |
| Terminal loss relief | Final tax year and the 3 previous tax years | ITA 2007 s.89 | https://www.legislation.gov.uk/ukpga/2007/3/section/89 |
| Pre-trading expenses | Up to 7 years before trading starts | ITTOIA 2005 s.57 | https://www.legislation.gov.uk/ukpga/2005/5/section/57 |
| Pension annual allowance | GBP 60,000; tapered over GBP 260,000 adjusted income (threshold income GBP 200,000) to a minimum of GBP 10,000; MPAA GBP 10,000 | 2026/27 | https://www.gov.uk/government/publications/rates-and-allowances-pension-schemes/pension-schemes-rates |
| Pension carry forward | Unused allowance of the 3 previous tax years | FA 2004 s.228A | https://www.legislation.gov.uk/ukpga/2004/12/section/228A |
| ISA allowance | GBP 20,000 | 2026/27 | https://www.gov.uk/individual-savings-accounts |
| EIS / SEIS / VCT income tax relief | 30% on up to GBP 1 million (GBP 2 million with knowledge-intensive) / 50% on up to GBP 200,000 / 20% on up to GBP 200,000; VCT held 5 years | 2026/27 | https://www.gov.uk/guidance/venture-capital-schemes-tax-relief-for-investors |
| VCT relief rate change | 30% replaced by 20% | From 6 April 2026 | https://www.legislation.gov.uk/ukpga/2026/11/section/15 |
| VAT registration / deregistration | GBP 90,000 / GBP 88,000 | 2026/27 | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1 |
| Flat Rate Scheme first-year discount | 1% off the flat rate in the first year of VAT registration | 2026/27 | https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay |
| Capital Goods Scheme values | Land and buildings GBP 600,000 or more; aircraft, ships, boats and other vessels GBP 50,000 or more | VAT Regulations 1995 reg 113 | https://www.legislation.gov.uk/uksi/1995/2518/regulation/113 |

### Income tax rates 2026/27

| Band | Taxable income | Rate | Source |
| --- | --- | --- | --- |
| Personal Allowance | GBP 0 to GBP 12,570 | 0% | https://www.gov.uk/income-tax-rates |
| Basic rate | GBP 12,571 to GBP 50,270 | 20% | same |
| Higher rate | GBP 50,271 to GBP 125,140 | 40% | same |
| Additional rate | Over GBP 125,140 | 45% | same |

- **Personal Allowance taper**: reduced by GBP 1 for every GBP 2 of adjusted net income above GBP 100,000. Fully withdrawn at GBP 125,140.

### Income splitting and structuring

#### Sole trader vs limited company

| Factor | Sole trader | Ltd company |
| --- | --- | --- |
| Profits up to GBP 50,270 | Income tax 20% + Class 4 NIC 6% | Corporation tax 19-25% + extraction costs |
| Profits over GBP 50,270 | Income tax 40% + NIC Class 4 (2%) | Corporation tax 25% + salary/dividend mix |
| When to incorporate | Run both routes for the client (Case 2). At 2026/27 rates, with all profit extracted, the cost at GBP 60,000 is about the same; profit retained in the company is what tips the result | Requires Companies House filing, accounts, employer PAYE |

- **Legislation**: Companies Act 2006; Corporation Tax Act 2009; ITEPA 2003 (dividend taxation).

#### Salary vs dividends (for Ltd companies)

| Option | Detail |
| --- | --- |
| Optimal salary level | A salary at the Primary Threshold (GBP 12,570 for 2026/27) builds State Pension entitlement without employee NIC. Employer NIC at 15% applies above the Secondary Threshold (GBP 5,000). Where the Employment Allowance is not available (for example a company whose only employee is a director), compare a salary at the Secondary Threshold. |
| Dividend allowance | First GBP 500 of dividend income is taxed at 0% (2026/27). |
| Dividend tax rates | 10.75% (basic), 35.75% (higher), 39.35% (additional) for 2026/27. See `uk-dividends`. |

#### Family employment

- **Family employment strategy**: employ a spouse or family member for genuine work at market rate. Their salary is a deductible business expense and taxed in their hands. Must be genuine employment with documented duties.
- **Legislation**: ITEPA 2003 s.7; ITTOIA 2005 s.34 (wholly and exclusively test).

### Deductions most people miss

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Use of home as office | ITTOIA 2005 s.34 | Proportion of home costs (rent, mortgage interest, council tax, electricity, heating, internet, insurance) based on rooms used and time spent. Alternatively, use HMRC simplified expenses: GBP 10/month (25-50 hrs), GBP 18/month (51-100 hrs), GBP 26/month (101+ hrs). |
| Business mileage | ITTOIA 2005 ss.94B-94D | Simplified mileage for cars and goods vehicles in 2026/27: 55p a mile for the first 10,000 business miles, 25p a mile after that (45p for the first 10,000 before 6 April 2026). Covers fuel, insurance, repairs, depreciation. |
| Professional subscriptions | ITTOIA 2005 s.34 | ICAEW, ACCA, CIMA, CII, Law Society, etc. Deductible where paid wholly and exclusively for the trade. |
| Training & CPD | ITTOIA 2005 s.34 | Training to maintain or update existing skills is deductible. Training for a new trade is not. |
| Pre-trading expenses | ITTOIA 2005 s.57 | Expenses incurred up to 7 years before trading begins, which would have been deductible if incurred during trading. |
| Bad debts | ITTOIA 2005 s.35 | Specific bad debts written off are deductible. General provisions are not. |
| Telephone & broadband | ITTOIA 2005 s.34 | Business-use proportion of personal phone/broadband. A separate business phone line is fully deductible. |
| Bank charges | ITTOIA 2005 s.34 | Business account fees, payment processing fees (Stripe, PayPal, GoCardless). |
| Protective clothing & tools | ITTOIA 2005 s.34 | Work-specific clothing (not everyday wear), tools of the trade. |
| Flat rate expenses (simplified) | ITTOIA 2005 s.94B-D | Available to sole traders and to partnerships with no company partner, whether or not they use the cash basis: vehicles (mileage rates), use of home, business premises lived in. |

### Capital allowances

- **Legislation**: Capital Allowances Act 2001 (CAA 2001).

#### Annual Investment Allowance (AIA)

| Feature | Detail |
| --- | --- |
| Rate | 100% first-year deduction |
| Limit | GBP 1,000,000 per year |
| Qualifying expenditure | Plant and machinery (not cars, not buildings) |
| Strategy | Claim AIA on all qualifying expenditure up to GBP 1m for full write-off in year of purchase |

#### Writing down allowances (WDA)

| Pool | Rate (before April 2026) | Rate (from April 2026: 1 April for companies, 6 April for income tax) | Assets | Source |
| --- | --- | --- | --- | --- |
| Main pool | 18% (reducing balance) | 14% | General plant & machinery | https://www.gov.uk/capital-allowances/business-cars |
| Special rate pool | 6% | 6% | Long-life assets, integral features, thermal insulation, cars with CO2 over 50g/km | same |

#### The 40% first-year allowance (from 1 January 2026)

Available for main-rate expenditure where AIA or full expensing does not apply. The plant or machinery must be new and unused and must not be a car. Particularly relevant for unincorporated businesses (sole traders/partnerships) and leased assets (Finance Act 2026 s.29, inserting CAA 2001 s.45U).

#### Cars

| CO2 emissions | Allowance |
| --- | --- |
| 0 g/km (electric), new and unused (second hand electric car: main pool) | 100% FYA |
| 1-50 g/km | Main pool (14% from April 2026) |
| Over 50 g/km | Special rate pool (6%) |

#### Timing strategy

Buy qualifying plant and machinery before the end of your accounting period to claim AIA in the current year. Defer purchases to the next period only if you expect higher profits next year.

### Loss utilisation

- **Legislation**: ITA 2007 s.64-83.

| Relief | Detail | Cap |
| --- | --- | --- |
| Sideways relief (s.64) | Set current-year trading loss against total income of the same year or prior year | Greater of GBP 50,000 or 25% of adjusted total income |
| Carry-forward (s.83) | Carry forward trading losses against future profits of the same trade | Unlimited, no time limit |
| Carry-back (s.64) | Set loss against total income of the prior year | Same cap as sideways relief |
| Early trade losses (s.72) | Losses in the first 4 years of a new trade can be carried back 3 years (FIFO) | Same cap applies |
| Terminal loss relief (s.89) | Losses in the final 12 months of a trade can be carried back against profits of the same trade in the prior 3 years (LIFO) | No cap |
| Capital allowances and losses | Excess capital allowances can create or increase a trading loss | N/A |

**Loss utilisation strategy**: in a loss-making year, accelerate expenditure (training, equipment, marketing) to maximise the loss. Use sideways relief to set it against employment income or other income, capped at the greater of GBP 50,000 or 25% of adjusted total income.

### Timing strategies

| Option | Detail |
| --- | --- |
| Defer income | If using the cash basis (the default for the self-employed since 2024/25), delay invoicing to after 5 April to push income into the next tax year. Useful if expecting lower income next year or approaching a rate threshold. |
| Accelerate expenses | Prepay annual subscriptions, make planned purchases, and pay outstanding invoices before 5 April. |
| Personal Allowance recovery | If adjusted net income is between GBP 100,000 and GBP 125,140, the effective marginal rate is 60%. Make pension contributions or Gift Aid donations to bring income below GBP 100,000 and recover the full Personal Allowance. |
| Payment on account management | Payments on account (31 January and 31 July) are based on prior year's liability. If current-year income will be lower, apply to reduce payments on account (online or form SA303). |
| Spouse transfers | Transfer savings income or rental property ownership to a lower-earning spouse to use their Personal Allowance, savings allowance, or basic rate band. |

### VAT optimisation

- **Legislation**: Value Added Tax Act 1994 (VATA 1994).

| Option | Detail |
| --- | --- |
| VAT registration threshold | GBP 90,000 (2026/27). Below this, registration is voluntary. |
| Flat Rate Scheme (FRS) | Fixed percentage of gross turnover as VAT. Can be simpler and may result in lower VAT if input VAT is low. 1% discount in first year of VAT registration. |
| Cash accounting scheme | Pay VAT only when paid by customers (not when invoiced). Helps cash flow and avoids paying VAT on bad debts. |
| Annual accounting scheme | One VAT return per year instead of quarterly. Nine monthly instalments based on estimate, balancing payment with annual return. |
| Partial exemption | If making both taxable and exempt supplies, optimise the allocation method to maximise input VAT recovery. Standard method vs special method. |
| Capital Goods Scheme | For land and buildings (and civil engineering works) of GBP 600,000 or more (exclusive of VAT) and aircraft, ships, boats and other vessels of GBP 50,000 or more, input VAT is adjusted over later intervals (VAT Regulations 1995 reg 113). Computers are no longer capital items: reg 113(2)(d) is repealed, and HMRC notice 706/2 was updated on 29 July 2026 to match. |
| De-registration | If turnover falls below GBP 88,000 (de-registration threshold), consider voluntary de-registration if clients are VAT-exempt consumers. |

### Social security optimisation

- **Legislation**: Social Security Contributions and Benefits Act 1992; National Insurance Contributions Act 2014.

| Class | Who pays | Rate | Threshold | Source |
| --- | --- | --- | --- | --- |
| Class 2 | Self-employed | Treated as paid (no charge) if profits GBP 7,105 or more | Voluntary (GBP 3.65 a week) if below | https://www.gov.uk/self-employed-national-insurance-rates |
| Class 4 | Self-employed | 6% on profits GBP 12,570-GBP 50,270; 2% above GBP 50,270 | Lower Profits Limit GBP 12,570 | same |

| Option | Detail |
| --- | --- |
| Voluntary Class 2 | If profits are below GBP 7,105, voluntary Class 2 (GBP 3.65 a week for 2026/27) protects State Pension entitlement. From 2026/27, voluntary Class 2 is no longer available for periods abroad for most people. |
| NIC holiday (incorporation) | Directors of Ltd companies can set salary below the Primary Threshold (GBP 12,570), but at or above the Lower Earnings Limit (GBP 6,708 for 2026/27), to avoid employee NIC while still earning a qualifying year. |
| Maximise pension contributions | Pension contributions reduce income for the Personal Allowance taper calculation but do not reduce NIC-liable profits. |

### Investment and retirement

#### Pension contributions (2026/27)

| Feature | Detail | Legislation |
| --- | --- | --- |
| Annual allowance | GBP 60,000 (or 100% of earnings, whichever is lower) | Finance Act 2004 s.228 |
| Carry forward | Unused allowance from previous 3 tax years can be carried forward | FA 2004 s.228A |
| Tax relief | Basic rate (20%) added at source; higher/additional rate claimed via Self Assessment | FA 2004 s.188-195 |
| Tapered allowance | Reduces by GBP 1 for every GBP 2 of adjusted income above GBP 260,000, minimum GBP 10,000 (not reduced if threshold income is GBP 200,000 or less) | FA 2004 s.228ZA |
| Money Purchase Annual Allowance | GBP 10,000 if flexibly accessed pension benefits | FA 2004 s.227ZA |

- **Strategy**: a higher-rate taxpayer contributing GBP 40,000 to a pension receives 40% tax relief = GBP 16,000 saving. If this brings adjusted net income below GBP 100,000, the Personal Allowance is restored = additional saving of up to GBP 5,028 (GBP 12,570 x 40%).

#### ISA (Individual Savings Account)

| Feature | Detail |
| --- | --- |
| Annual allowance | GBP 20,000 (2026/27) |
| Tax treatment | No income tax or CGT on returns. Does not reduce taxable income. |
| Strategy | Shelter investment returns from tax. Use after maximising pension contributions. |

#### Venture capital schemes (2026/27)

| Scheme | Income tax relief | CGT exemption | Legislation |
| --- | --- | --- | --- |
| EIS (Enterprise Investment Scheme) | 30% on up to GBP 1m invested (GBP 2m if at least GBP 1m goes to knowledge-intensive companies) | Yes, if held 3+ years | ITA 2007 s.156-257 |
| SEIS (Seed EIS) | 50% on up to GBP 200,000 invested | Yes, if held 3+ years | ITA 2007 s.257SA-SG |
| VCT (Venture Capital Trust) | 20% from 6 April 2026 (30% before; FA 2026 s.15) on up to GBP 200,000 invested, shares held 5 years | Yes | ITA 2007 s.258-332 |

## Boundary and exception table

### Red lines

| Risk | Detail |
| --- | --- |
| GAAR | Finance Act 2013 s.206-215. Any arrangement that is not a "reasonable course of action" in relation to the relevant tax provisions may be counteracted. |
| DOTAS | Disclosure of Tax Avoidance Schemes. Promoters must notify HMRC of schemes. Users must disclose scheme reference numbers on tax returns. |
| Accelerated Payment Notices | HMRC can demand upfront payment of disputed tax from users of avoidance schemes. |
| IR35 | Off-payroll working rules (ITEPA 2003 Chapter 8). If HMRC determines that a self-employed contractor would be an employee "but for" the intermediary (PSC), income is taxed as employment income with full PAYE/NIC. |
| Disguised remuneration | Loans to self/employees via trusts or third parties (ITEPA 2003 Part 7A) are treated as taxable income. |
| Personal Allowance manipulation | Artificial arrangements solely to stay below GBP 100,000 for Personal Allowance purposes may be challenged. |
| Non-commercial loss claims | Sideways loss relief requires the trade to be run on a commercial basis with a view to profit (ITA 2007 s.66). |
| Capital allowances on non-qualifying items | Only "plant and machinery" qualifies. Buildings, structures, and land do not (except via Structures and Buildings Allowance at 3%). |

### Where the options do not apply

| Situation | Treatment |
| --- | --- |
| Car purchase | No AIA and no 40% first-year allowance; only the car rules (100% FYA for new zero-emission, else main or special rate pool) |
| Second-hand plant | No 40% first-year allowance (new and unused only); AIA still available |
| Flexibly accessed pension | Money purchase contributions limited by the GBP 10,000 MPAA |
| Company with a director as the only employee | No Employment Allowance; compare a salary at the Secondary Threshold |
| Scottish taxpayer | Scottish income tax bands apply; this skill's income tax figures do not |

## Worked cases

All amounts are illustrations, not client data.

### Case 1: Personal Allowance recovery via pension (income GBP 110,000)

| Item | Without pension | With GBP 10,000 gross pension contribution |
| --- | --- | --- |
| Adjusted net income | GBP 110,000 | GBP 100,000 |
| Personal Allowance | GBP 7,570 (tapered) | GBP 12,570 (full) |
| Tax saving from pension relief | none | GBP 4,000 (40% x GBP 10,000) |
| Tax saving from PA recovery | none | GBP 2,000 (40% x GBP 5,000 PA restored) |
| **Total annual saving** |  | **GBP 6,000** |

```oa-check
name: Personal Allowance recovered by a GBP 10,000 pension contribution (2026/27)
inputs:
  income: 110000
  contribution: 10000
  personal_allowance: 12570
  taper_start: 100000
steps:
  - pa_before: max(personal_allowance - (income - taper_start) / 2, 0)
  - pa_after: max(personal_allowance - max(income - contribution - taper_start, 0) / 2, 0)
  - pa_restored: pa_after - pa_before
  - saving: contribution * 0.40 + pa_restored * 0.40
expected:
  pa_before: 7570.00
  pa_restored: 5000.00
  saving: 6000.00
```

### Case 2 (decision, both ways): incorporation at GBP 60,000 profit, single, no other income, all profit extracted

A sole trader with GBP 60,000 profit pays income tax of GBP 11,432 and Class 4 NIC of GBP 2,456.60: GBP 13,888.60. Through a company with no associated companies and no Employment Allowance, a GBP 12,570 salary costs GBP 1,135.50 of employer NIC, corporation tax at 19% on the remaining GBP 46,294.50 is GBP 8,795.96, and paying out the GBP 37,498.54 left as dividends costs GBP 3,977.34 of dividend tax (GBP 500 at 0%, the rest at 10.75%, all inside the basic rate band). Total: GBP 13,908.80.

**The deciding figure** is the difference: the company route costs GBP 20.20 more. So at GBP 60,000 with everything extracted, stay a sole trader (the company also adds Companies House filing, accounts and payroll costs). The company only wins when profit is retained in it (the retained part bears corporation tax but no dividend tax yet) or other facts change (for example the Employment Allowance is available).

| Item | Sole trader | Ltd (GBP 12,570 salary + GBP 37,498.54 dividends) |
| --- | --- | --- |
| Income tax | GBP 11,432.00 | GBP 3,977.34 (dividend tax) |
| NIC | GBP 2,456.60 (Class 4) | GBP 1,135.50 (employer, 15% over GBP 5,000) |
| Corporation tax | none | GBP 8,795.96 (19% of GBP 46,294.50) |
| **Total tax + NIC** | **GBP 13,888.60** | **GBP 13,908.80** |

```oa-check
name: Sole trader versus company at GBP 60,000 profit, all extracted (2026/27)
inputs:
  profit: 60000
  personal_allowance: 12570
  basic_limit: 50270
  salary: 12570
  secondary_threshold: 5000
  dividend_allowance: 500
steps:
  - st_income_tax: (basic_limit - personal_allowance) * 0.20 + (profit - basic_limit) * 0.40
  - st_class4: (basic_limit - personal_allowance) * 0.06 + (profit - basic_limit) * 0.02
  - st_total: st_income_tax + st_class4
  - er_nic: (salary - secondary_threshold) * 0.15
  - company_profit: profit - salary - er_nic
  - corp_tax: round(company_profit * 0.19, 2)
  - dividends: company_profit - corp_tax
  - dividend_tax: round((dividends - dividend_allowance) * 0.1075, 2)
  - ltd_total: er_nic + corp_tax + dividend_tax
  - company_costs_more_by: ltd_total - st_total
expected:
  st_income_tax: 11432.00
  st_class4: 2456.60
  st_total: 13888.60
  er_nic: 1135.50
  company_profit: 46294.50
  corp_tax: 8795.96
  dividends: 37498.54
  dividend_tax: 3977.34
  ltd_total: 13908.80
  company_costs_more_by: 20.20
```

### Case 3: AIA on an equipment purchase (GBP 20,000)

| Item | Without AIA | With AIA |
| --- | --- | --- |
| Deduction in Year 1 | GBP 2,800 (14% WDA) | GBP 20,000 (100%) |
| Tax saving at 40% | GBP 1,120 | **GBP 8,000 in Year 1** |

### Case 4: simplified home office (101+ hours a month)

| Simplified expense claim | GBP 26/month x 12 = **GBP 312/year** |
| --- | --- |
| Tax saving at 20% | **GBP 62.40/year** |
| Tax saving at 40% | **GBP 124.80/year** |

### Case 5: EIS investment (GBP 50,000)

| Income tax relief (30%) | **GBP 15,000** |
| --- | --- |
| CGT exemption on gains (if held 3+ years) | Full exemption |
| Loss relief if investment fails | Loss, net of relief, can be set against income |

## When to refuse or refer

- Refuse any arrangement that fails the red lines (GAAR, DOTAS-notifiable schemes, disguised remuneration, artificial Personal Allowance arrangements). Do not design or endorse a marketed avoidance scheme.
- Refer IR35 status questions on a specific contract to an employment status review.
- Refer incorporation of a business with property, goodwill above a nominal value, or existing losses to a specialist: incorporation relief, stamp duty land tax and loss transfer are outside this skill.
- Refer Scottish taxpayers for the Scottish rate bands.
- Refer EIS, SEIS and VCT investment choices to a regulated financial adviser: the tax relief is in scope, the investment is not.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Filing and payment

- Self Assessment online return by **31 January** after the tax year, with the balancing payment and the first payment on account; the second payment on account by **31 July**.
- Reduce payments on account online or on form SA303 if this year's income will be lower.
- Pension contributions must be paid by **5 April** to count for 2026/27; higher and additional rate relief is claimed on the return.

### Annual tax planning calendar

| Month | Action |
| --- | --- |
| April | New tax year starts 6 April. Review prior year's income and plan current year. Use ISA allowance (GBP 20,000) before 5 April if not yet done. |
| May | Register for Self Assessment if newly self-employed (by 5 October deadline, but earlier is better). |
| June | Mid-year review: estimate profits and tax liability. Plan pension contributions. |
| July | **31 July**: 2nd payment on account for prior year. Apply to reduce if overpaying (SA303). |
| August | Review capital expenditure plans. Consider AIA timing. |
| September | Review NIC position: voluntary Class 2 if profits low. |
| October | **5 October**: deadline to register for Self Assessment if newly self-employed. |
| November | Consider income deferral if approaching higher rate threshold. Accelerate deductible expenses. |
| December | Buy capital equipment before 31 December (if accounting period is calendar year) for AIA. |
| January | **31 January**: Self Assessment filing deadline + 1st payment on account + balancing payment. Make pension contributions before 5 April to claim relief in current year. |
| February | Final push for pension contributions and Gift Aid donations before 5 April. |
| March | **5 April**: tax year ends. Complete any income deferral / expense acceleration. Maximise ISA contributions. |

## Completion checklist

- [ ] Marginal rate set, including the 60% band and the Class 4 position.
- [ ] Missed deductions and simplified expenses checked.
- [ ] Capital purchases timed; AIA, 40% FYA and car rules applied correctly.
- [ ] Pension contribution tested against the taper, annual allowance, carry forward and MPAA.
- [ ] Sole trader and company routes both computed where relevant; the deciding figure stated.
- [ ] Losses placed in the best year within the cap and the commerciality test.
- [ ] VAT position and schemes reviewed.
- [ ] Every recommendation checked against the red lines.

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| GOV.UK, Income Tax rates and Personal Allowances | Read for GBP 12,570, the taper above GBP 100,000 to GBP 125,140, the 20%, 40% and 45% bands | https://www.gov.uk/income-tax-rates | 2026-11-14 |
| GOV.UK, Tax on dividends | Read for the GBP 500 allowance and 10.75%, 35.75%, 39.35% | https://www.gov.uk/tax-on-dividends | 2026-11-14 |
| Finance Act 2026 s.4 | Read for the dividend ordinary rate 10.75% and upper rate 35.75% | https://www.legislation.gov.uk/ukpga/2026/11/section/4 | 2026-11-14 |
| GOV.UK, Self-employed National Insurance rates | Read for Class 4 at 6% and 2%, Class 2 treated as paid at GBP 7,105 and GBP 3.65 a week | https://www.gov.uk/self-employed-national-insurance-rates | 2026-11-14 |
| GOV.UK, Rates and thresholds for employers 2026 to 2027 | Read for 15% employer NIC, GBP 5,000 Secondary Threshold, GBP 6,708 LEL, GBP 12,570 Primary Threshold | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 | 2026-11-14 |
| GOV.UK, Corporation Tax rates | Read for 19% up to GBP 50,000, 25% over GBP 250,000 and marginal relief | https://www.gov.uk/corporation-tax-rates | 2026-11-14 |
| GOV.UK, Simplified expenses (print version) | Read for 55p and 25p mileage (45p before 6 April 2026) and the GBP 10, 18 and 26 home rates | https://www.gov.uk/simpler-income-tax-simplified-expenses/print | 2026-11-14 |
| GOV.UK, Simplified expenses: vehicles | Read for the vehicle mileage method | https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles | 2026-11-14 |
| GOV.UK, Annual Investment Allowance | Read for the GBP 1 million AIA | https://www.gov.uk/capital-allowances/annual-investment-allowance | 2026-11-14 |
| Finance Act 2026 s.28 | Read for the main rate changed from 18% to 14% | https://www.legislation.gov.uk/ukpga/2026/11/section/28 | 2026-11-14 |
| Finance Act 2026 s.29 | Read for the 40% first-year allowance from 1 January 2026, unused and not second-hand | https://www.legislation.gov.uk/ukpga/2026/11/section/29 | 2026-11-14 |
| GOV.UK, Business cars | Read for the 100% FYA on new and unused 0g/km cars, 14% main rate, 6% special rate, 50g/km | https://www.gov.uk/capital-allowances/business-cars | 2026-11-14 |
| CAA 2001 s.270AA | Read for the Structures and Buildings Allowance at 3% (10% special tax site) | https://www.legislation.gov.uk/ukpga/2001/2/section/270AA | 2026-11-14 |
| ITA 2007 s.24A | Read for the cap of GBP 50,000 or 25% of adjusted total income | https://www.legislation.gov.uk/ukpga/2007/3/section/24A | 2026-11-14 |
| ITA 2007 s.72 | Read for losses in the first 4 years and the 3 earlier tax years | https://www.legislation.gov.uk/ukpga/2007/3/section/72 | 2026-11-14 |
| ITA 2007 s.89 | Read for terminal loss relief against the final tax year and the 3 previous tax years | https://www.legislation.gov.uk/ukpga/2007/3/section/89 | 2026-11-14 |
| ITTOIA 2005 s.57 | Read for pre-trading expenses up to 7 years before trading | https://www.legislation.gov.uk/ukpga/2005/5/section/57 | 2026-11-14 |
| HMRC, Pension schemes rates | Read for GBP 60,000, the GBP 200,000 and GBP 260,000 limits, the GBP 10,000 minimum and MPAA for 2026/27 | https://www.gov.uk/government/publications/rates-and-allowances-pension-schemes/pension-schemes-rates | 2026-11-14 |
| GOV.UK, Tapered annual allowance | Read for the GBP 10,000 minimum reduced allowance | https://www.gov.uk/guidance/pension-schemes-work-out-your-tapered-annual-allowance | 2026-11-14 |
| FA 2004 s.228A | Read for carry forward from the 3 previous tax years | https://www.legislation.gov.uk/ukpga/2004/12/section/228A | 2026-11-14 |
| GOV.UK, Individual Savings Accounts | Read for the GBP 20,000 allowance for 2026/27 | https://www.gov.uk/individual-savings-accounts | 2026-11-14 |
| GOV.UK, Venture capital schemes: tax relief for investors | Read for EIS 30%, SEIS 50%, VCT 20%, the limits and the 3 and 5 year holding periods | https://www.gov.uk/guidance/venture-capital-schemes-tax-relief-for-investors | 2026-11-14 |
| Finance Act 2026 s.15 | Read for VCT relief changed from 30% to 20% | https://www.legislation.gov.uk/ukpga/2026/11/section/15 | 2026-11-14 |
| VATA 1994 Sch 1 para 1 | Read for the GBP 90,000 registration and GBP 88,000 deregistration thresholds | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1 | 2026-11-14 |
| GOV.UK, VAT registration: when to register | Read for the GBP 90,000 threshold | https://www.gov.uk/vat-registration/when-to-register | 2026-11-14 |
| GOV.UK, VAT Flat Rate Scheme: how much you pay | Read for the 1% first-year discount | https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay | 2026-11-14 |
| HMRC, Capital Goods Scheme (VAT Notice 706/2) | Read for the 29 July 2026 update and computers | https://www.gov.uk/guidance/capital-goods-scheme-notice-7062 | 2026-11-14 |
| VAT Regulations 1995 reg 113 | Read for the GBP 600,000 and GBP 50,000 capital item values | https://www.legislation.gov.uk/uksi/1995/2518/regulation/113 | 2026-11-14 |
| GOV.UK, Voluntary National Insurance abroad from 6 April 2026 | Read for the end of voluntary Class 2 for periods abroad | https://www.gov.uk/government/publications/voluntary-national-insurance-contributions-for-periods-abroad-from-6-april-2026/voluntary-national-insurance-contributions-abroad-from-6-april-2026 | 2026-11-14 |
| GOV.UK, Payments on account | Read for the 31 January and 31 July dates and form SA303 | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-11-14 |

Not yet confirmed: the end date of the 100% first-year allowance for new zero-emission cars (the old file said "bought before April 2027"; the business cars page read today does not state a date).
