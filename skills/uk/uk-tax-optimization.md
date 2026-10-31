---
name: uk-tax-optimization
description: "Use this skill whenever asked about reducing tax in the UK, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for self-employed individuals in the UK, for tax year 2026/27 (6 April 2026 to 5 April 2027). Trigger on phrases like 'reduce tax', 'tax planning', 'save tax', 'optimize', 'allowances', 'deductions I'm missing', 'pay less tax', 'tax-efficient', 'tax minimization', 'how to lower my tax bill', 'sole trader or limited company 2026'. Covers 2026/27 bands, incorporation, salary and dividends, simplified expenses, capital allowances (14% main pool, 40% first-year allowance), loss relief, pensions, ISAs, EIS, SEIS and VCT (20% from April 2026), VAT schemes and anti-avoidance red lines. Out of scope, see siblings: uk-self-employment-sa103, uk-dividends, uk-national-insurance, uk-vat-return. ALWAYS read this skill before advising on any UK tax optimization strategy."
version: 1.2
jurisdiction: GB
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
verified_by: pending
source_checked: 2026-10-23
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Tax Optimization

## UK Tax Optimization -- Self-Employed Skill v1.1

> Source-cited draft: not reviewed by an accountant.

Tax year in force: 2026/27 (6 April 2026 to 5 April 2027). Changelog v1.1 (2026-10-23): every figure moved to 2026/27 with the year named; dividend rates 10.75% / 35.75% / 39.35%; employer NIC 15% above GBP 5,000; 55p mileage; 14% main pool and 40% first-year allowance (Finance Act 2026 ss.28 and 29); VCT relief 20% (FA 2026 s.15); voluntary Class 2 abroad withdrawn; Example 2 (incorporation) recomputed, it previously applied corporation tax to the dividend instead of the profit; accountant attribution removed; Sources table added. Review fixes (2026-10-23): Capital Goods Scheme values taken from VAT Regulations 1995 reg 113; simplified expenses no longer tied to the cash basis; the List 3 condition for traders removed; the zero-emission car allowance dated; em dashes removed.

## Rates and thresholds, 2026/27

| Item | Rate or amount | Year | Source |
| --- | --- | --- | --- |
| Personal Allowance | GBP 12,570, reduced by GBP 1 for every GBP 2 of adjusted net income over GBP 100,000 | 2026/27 | https://www.gov.uk/income-tax-rates |
| Basic, higher, additional rates | 20% to GBP 50,270; 40% to GBP 125,140; 45% above | 2026/27 | https://www.gov.uk/income-tax-rates |
| Dividend allowance and rates | GBP 500; 10.75%, 35.75%, 39.35% | 2026/27 | https://www.gov.uk/tax-on-dividends |
| Class 4 NIC | 6% on profits GBP 12,570 to 50,270; 2% above | 2026/27 | https://www.gov.uk/self-employed-national-insurance-rates |
| Class 2 NIC | Treated as paid if profits GBP 7,105 or more; voluntary GBP 3.65 a week below | 2026/27 | https://www.gov.uk/self-employed-national-insurance-rates |
| Employer NIC | 15% above the Secondary Threshold of GBP 5,000; Lower Earnings Limit GBP 6,708; Primary Threshold GBP 12,570 | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Corporation tax | 19% up to GBP 50,000; 25% over GBP 250,000; marginal relief between | FY 2026 | https://www.gov.uk/corporation-tax-rates |
| Simplified mileage | 55p a mile for the first 10,000 miles, 25p after | 2026/27 | https://www.gov.uk/simpler-income-tax-simplified-expenses/print |
| Annual Investment Allowance | GBP 1,000,000 | 2026/27 | https://www.gov.uk/capital-allowances/annual-investment-allowance |
| Main pool writing down allowance | 14% (18% before April 2026) | From April 2026 | https://www.legislation.gov.uk/ukpga/2026/11/section/28 |
| 40% first-year allowance | New, unused main-rate plant, not cars | From 1 January 2026 | https://www.legislation.gov.uk/ukpga/2026/11/section/29 |
| Sideways loss relief cap | Greater of GBP 50,000 or 25% of adjusted total income | 2026/27 | https://www.legislation.gov.uk/ukpga/2007/3/section/24A |
| Pension annual allowance | GBP 60,000; tapered over GBP 260,000 adjusted income (threshold income GBP 200,000) to a minimum of GBP 10,000; MPAA GBP 10,000 | 2026/27 | https://www.gov.uk/government/publications/rates-and-allowances-pension-schemes/pension-schemes-rates |
| ISA allowance | GBP 20,000 | 2026/27 | https://www.gov.uk/individual-savings-accounts |
| EIS / SEIS / VCT income tax relief | 30% on up to GBP 1m (GBP 2m with knowledge-intensive) / 50% on up to GBP 200,000 / 20% on up to GBP 200,000 | 2026/27 | https://www.gov.uk/guidance/venture-capital-schemes-tax-relief-for-investors |
| VAT registration / deregistration | GBP 90,000 / GBP 88,000 | 2026/27 | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1 |

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Key optimization legislation | Income Tax Act 2007 (ITA 2007); Income Tax (Trading and Other Income) Act 2005 (ITTOIA 2005); Income Tax (Earnings and Pensions) Act 2003 (ITEPA 2003); Capital Allowances Act 2001 (CAA 2001); Finance Act 2026 |
| Tax authority attitude to planning | HMRC accepts legitimate tax planning but actively pursues avoidance. The General Anti-Abuse Rule (GAAR) under Finance Act 2013 s.206-215 applies to arrangements that are "abusive" -- i.e. not a reasonable course of action. Promoters of Tax Avoidance Schemes (POTAS) regime and Disclosure of Tax Avoidance Schemes (DOTAS) requirements apply. |
| Currency | GBP |
| Tax year | 6 April -- 5 April (this skill: 2026/27) |
| Filing deadline | 31 January following the tax year (online Self Assessment) |

### Income Tax Rates 2026/27

**Income Tax Rates 2026/27**  _(https://www.gov.uk/income-tax-rates)_

| Band | Taxable income | Rate |
| --- | --- | --- |
| Personal Allowance | £0 -- £12,570 | 0% Source: https://www.gov.uk/income-tax-rates (tax year 2026) (read 2026-10-31) |
| Basic rate | £12,571 -- £50,270 | 20% Source: https://www.gov.uk/income-tax-rates (tax year 2026) (read 2026-10-31) |
| Higher rate | £50,271 -- £125,140 | 40% Source: https://www.gov.uk/income-tax-rates (tax year 2026) (read 2026-10-31) |
| Additional rate | Over £125,140 | 45% Source: https://www.gov.uk/income-tax-rates (tax year 2026) (read 2026-10-31) |

- **Personal Allowance taper**: Personal Allowance tapers: reduced by £1 for every £2 of adjusted net income above £100,000. Fully withdrawn at £125,140.

## Section 2 -- Income Splitting & Structuring

### Sole Trader vs Limited Company

**Sole Trader vs Limited Company**

| Factor | Sole trader | Ltd company |
| --- | --- | --- |
| Profits up to £50,270 | Income tax 20% + Class 4 NIC 6% | Corporation tax 19-25% + extraction costs |
| Profits over £50,270 | Income tax 40% + NIC Class 4 (2%) | Corporation tax 25% + salary/dividend mix |
| When to incorporate | Run both routes for the client (Example 2). At 2026/27 rates, with all profit extracted, the cost at £60,000 is about the same; profit retained in the company is what tips the result | Requires Companies House filing, accounts, employer PAYE |

- **Legislation**: Companies Act 2006; Corporation Tax Act 2009; ITEPA 2003 (dividend taxation)  _(Companies Act 2006; Corporation Tax Act 2009; ITEPA 2003)_

### Salary vs Dividends (for Ltd companies)

**Salary vs Dividends (for Ltd companies)**

| Strategy | Detail |
| --- | --- |
| Optimal salary level | A salary at the Primary Threshold (£12,570 for 2026/27) builds State Pension entitlement without employee NIC. Employer NIC at 15% applies above the Secondary Threshold (£5,000). Where the Employment Allowance is not available (for example a company whose only employee is a director), compare a salary at the Secondary Threshold. |
| Dividend allowance | First £500 of dividend income is taxed at 0% (2026/27). |
| Dividend tax rates | 10.75% (basic), 35.75% (higher), 39.35% (additional) for 2026/27. See `uk-dividends`. Source: https://www.gov.uk/tax-on-dividends (tax year 2026) (read 2026-10-31) |

### Family Employment

- **Family employment strategy**: Employ a spouse or family member for genuine work at market rate. Their salary is a deductible business expense and taxed in their hands. Must be genuine employment with documented duties.
- **Legislation**: ITEPA 2003 s.7; ITTOIA 2005 s.34 (wholly and exclusively test)  _(ITEPA 2003 s.7; ITTOIA 2005 s.34)_

## Section 3 -- Deductions Most People Miss

**Deductions Most People Miss**  _(https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles)_

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Use of home as office | ITTOIA 2005 s.34 | Proportion of home costs (rent, mortgage interest, council tax, electricity, heating, internet, insurance) based on rooms used and time spent. Alternatively, use HMRC simplified expenses: £10/month (25-50 hrs), £18/month (51-100 hrs), £26/month (101+ hrs). |
| Business mileage | ITTOIA 2005 ss.94B-94D | Simplified mileage for cars and goods vehicles in 2026/27: 55p a mile for the first 10,000 business miles, 25p a mile after that (45p for the first 10,000 before 6 April 2026). Covers fuel, insurance, repairs, depreciation. |
| Professional subscriptions | ITTOIA 2005 s.34 | ICAEW, ACCA, CIMA, CII, Law Society, etc. Deductible where paid wholly and exclusively for the trade. |
| Training & CPD | ITTOIA 2005 s.34 | Training to maintain or update existing skills is deductible. Training for a new trade is not. |
| Pre-trading expenses | ITTOIA 2005 s.57 | Expenses incurred up to 7 years before trading begins, which would have been deductible if incurred during trading. |
| Bad debts | ITTOIA 2005 s.35 | Specific bad debts written off are deductible. General provisions are not. |
| Telephone & broadband | ITTOIA 2005 s.34 | Business-use proportion of personal phone/broadband. A separate business phone line is fully deductible. |
| Bank charges | ITTOIA 2005 s.34 | Business account fees, payment processing fees (Stripe, PayPal, GoCardless). |
| Protective clothing & tools | ITTOIA 2005 s.34 | Work-specific clothing (not everyday wear), tools of the trade. |
| Flat rate expenses (simplified) | ITTOIA 2005 s.94B-D | Available to sole traders and to partnerships with no company partner, whether or not they use the cash basis: vehicles (mileage rates), use of home, business premises lived in. |

## Section 4 -- Capital Allowances Optimization

- **Legislation**: Capital Allowances Act 2001 (CAA 2001)  _(CAA 2001)_

### Annual Investment Allowance (AIA)

**Annual Investment Allowance (AIA)**

| Feature | Detail |
| --- | --- |
| Rate | 100% first-year deduction |
| Limit | £1,000,000 per year |
| Qualifying expenditure | Plant and machinery (not cars, not buildings) |
| Strategy | Claim AIA on all qualifying expenditure up to £1m for full write-off in year of purchase |

### Writing Down Allowances (WDA)

**Writing Down Allowances (WDA)**

| Pool | Rate (before April 2026) | Rate (from April 2026: 1 April for companies, 6 April for income tax) | Assets |
| --- | --- | --- | --- |
| Main pool | 18% (reducing balance) | 14% | General plant & machinery Source: https://www.gov.uk/capital-allowances/business-cars (tax year 2026) (read 2026-10-31) |
| Special rate pool | 6% | 6% | Long-life assets, integral features, thermal insulation, cars with CO2 > 50g/km Source: https://www.gov.uk/capital-allowances/business-cars (tax year 2026) (read 2026-10-31) |

### New 40% First-Year Allowance (from 1 January 2026)

- **New 40% First-Year Allowance**: Available for main-rate expenditure where AIA or full expensing does not apply. The plant or machinery must be new and unused and must not be a car. Particularly relevant for unincorporated businesses (sole traders/partnerships) and leased assets.  _([Finance Act 2026 s.29, inserting CAA 2001 s.45U](https://www.legislation.gov.uk/ukpga/2026/11/section/29))_

### Cars

**Cars**  _(https://www.gov.uk/capital-allowances/business-cars)_

| CO2 emissions | Allowance |
| --- | --- |
| 0 g/km (electric), new and unused, bought before April 2027 (second hand electric car: main pool) | 100% FYA |
| 1-50 g/km | Main pool (14% from April 2026) |
| Over 50 g/km | Special rate pool (6%) |

### Timing Strategy

- **Timing strategy**: Buy qualifying plant and machinery before the end of your accounting period to claim AIA in the current year. Defer purchases to the next period only if you expect higher profits next year.

## Section 5 -- Loss Utilization

- **Legislation**: ITA 2007 s.64-83  _(ITA 2007 s.64-83)_

**Loss Utilization**

| Relief | Detail | Cap |
| --- | --- | --- |
| Sideways relief (s.64) | Set current-year trading loss against total income of the same year or prior year | Greater of £50,000 or 25% of adjusted total income |
| Carry-forward (s.83) | Carry forward trading losses against future profits of the same trade | Unlimited, no time limit |
| Carry-back (s.64) | Set loss against total income of the prior year | Same cap as sideways relief |
| Early trade losses (s.72) | Losses in the first 4 years of a new trade can be carried back 3 years (FIFO) | Same cap applies |
| Terminal loss relief (s.89) | Losses in the final 12 months of a trade can be carried back against profits of the same trade in the prior 3 years (LIFO) | No cap |
| Capital allowances and losses | Excess capital allowances can create or increase a trading loss | N/A |

### Strategy

- **Loss utilization strategy**: In a loss-making year, accelerate expenditure (training, equipment, marketing) to maximize the loss. Use sideways relief to set it against employment income or other income, capped at the greater of £50,000 or 25% of adjusted total income.

## Section 6 -- Timing Strategies

**Timing Strategies**

| Strategy | Detail |
| --- | --- |
| Defer income | If using the cash basis (the default for the self-employed since 2024/25), delay invoicing to after 5 April to push income into the next tax year. Useful if expecting lower income next year or approaching a rate threshold. |
| Accelerate expenses | Prepay annual subscriptions, make planned purchases, and pay outstanding invoices before 5 April. |
| Personal Allowance recovery | If adjusted net income is between £100,000 and £125,140, the effective marginal rate is 60%. Make pension contributions or Gift Aid donations to bring income below £100,000 and recover the full Personal Allowance. |
| Payment on account management | Payments on account (31 January and 31 July) are based on prior year's liability. If current-year income will be lower, apply to reduce payments on account (SA303). Source: https://www.gov.uk/understand-self-assessment-bill/payments-on-account (tax year 2026) (read 2026-10-31) |
| Spouse transfers | Transfer savings income or rental property ownership to a lower-earning spouse to use their Personal Allowance, savings allowance, or basic rate band. |

## Section 7 -- VAT Optimization

- **Legislation**: Value Added Tax Act 1994 (VATA 1994)  _(VATA 1994)_

**VAT Optimization**  _(https://www.gov.uk/guidance/capital-goods-scheme-notice-7062)_

| Strategy | Detail |
| --- | --- |
| VAT registration threshold | £90,000 (2026/27). Below this, registration is voluntary. Source: https://www.gov.uk/vat-registration/when-to-register (tax year 2026) (read 2026-10-31) |
| Flat Rate Scheme (FRS) | Fixed percentage of gross turnover as VAT. Can be simpler and may result in lower VAT if input VAT is low. 1% discount in first year of VAT registration. Source: https://www.gov.uk/simpler-income-tax-simplified-expenses/print (tax year 2026) (read 2026-10-31) |
| Cash accounting scheme | Pay VAT only when paid by customers (not when invoiced). Helps cash flow and avoids paying VAT on bad debts. |
| Annual accounting scheme | One VAT return per year instead of quarterly. Nine monthly instalments based on estimate, balancing payment with annual return. |
| Partial exemption | If making both taxable and exempt supplies, optimize the allocation method to maximize input VAT recovery. Standard method vs special method. |
| Capital Goods Scheme | For land and buildings (and civil engineering works) of £600,000 or more (exclusive of VAT) and aircraft, ships, boats and other vessels of £50,000 or more, input VAT is adjusted over later intervals (VAT Regulations 1995 reg 113). Computers are no longer capital items: reg 113(2)(d) is repealed, and HMRC notice 706/2 was updated on 29 July 2026 to match. |
| De-registration | If turnover falls below £88,000 (de-registration threshold), consider voluntary de-registration if clients are VAT-exempt consumers. Source: https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1 (tax year 2026) (read 2026-10-31) |

## Section 8 -- Social Security Optimization

- **Legislation**: Social Security Contributions and Benefits Act 1992; National Insurance Contributions Act 2014  _(Social Security Contributions and Benefits Act 1992; National Insurance Contributions Act 2014)_

### National Insurance Contributions (NIC) 2026/27

**National Insurance Contributions (NIC) 2026/27**

| Class | Who pays | Rate | Threshold |
| --- | --- | --- | --- |
| Class 2 | Self-employed | Treated as paid (no charge) if profits ≥ £7,105 | Voluntary (£3.65 a week) if below Source: https://www.gov.uk/self-employed-national-insurance-rates (tax year 2026) (read 2026-10-31) |
| Class 4 | Self-employed | 6% on profits £12,570-£50,270; 2% above £50,270 | Lower Profits Limit £12,570 Source: https://www.gov.uk/self-employed-national-insurance-rates (tax year 2026) (read 2026-10-31) |

### Optimization Strategies

**Optimization Strategies**  _(https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)_

| Strategy | Detail |
| --- | --- |
| Voluntary Class 2 | If profits are below £7,105, voluntary Class 2 (£3.65 a week for 2026/27) protects State Pension entitlement. From 2026/27, voluntary Class 2 is no longer available for periods abroad for most people. Source: https://www.gov.uk/self-employed-national-insurance-rates (tax year 2026) (read 2026-10-31) |
| NIC holiday (incorporation) | Directors of Ltd companies can set salary below the Primary Threshold (£12,570), but at or above the Lower Earnings Limit (£6,708 for 2026/27), to avoid employee NIC while still earning a qualifying year. |
| Maximize pension contributions | Pension contributions reduce income for the Personal Allowance taper calculation but do not reduce NIC-liable profits. |

## Section 9 -- Investment & Retirement

### Pension Contributions

**Pension Contributions (2026/27)**  _(https://www.gov.uk/government/publications/rates-and-allowances-pension-schemes/pension-schemes-rates)_

| Feature | Detail | Legislation |
| --- | --- | --- |
| Annual allowance | £60,000 (or 100% of earnings, whichever is lower) | Finance Act 2004 s.228 |
| Carry forward | Unused allowance from previous 3 tax years can be carried forward | FA 2004 s.228A |
| Tax relief | Basic rate (20%) added at source; higher/additional rate claimed via Self Assessment | FA 2004 s.188-195 |
| Tapered allowance | Reduces by £1 for every £2 of adjusted income above £260,000, minimum £10,000 (not reduced if threshold income is £200,000 or less) | FA 2004 s.228ZA |
| Money Purchase Annual Allowance | £10,000 if flexibly accessed pension benefits | FA 2004 s.227ZA |

- **Strategy**: A higher-rate taxpayer contributing £40,000 to a pension receives 40% tax relief = £16,000 saving. If this brings adjusted net income below £100,000, the Personal Allowance is restored = additional saving of up to £5,028 (£12,570 × 40%).

### ISA (Individual Savings Account)

**ISA (Individual Savings Account)**

| Feature | Detail |
| --- | --- |
| Annual allowance | £20,000 (2026/27) |
| Tax treatment | No income tax or CGT on returns. Does not reduce taxable income. |
| Strategy | Shelter investment returns from tax. Use after maximizing pension contributions. |

### Venture Capital Schemes

**Venture Capital Schemes (2026/27)**  _(https://www.gov.uk/guidance/venture-capital-schemes-tax-relief-for-investors)_

| Scheme | Income tax relief | CGT exemption | Legislation |
| --- | --- | --- | --- |
| EIS (Enterprise Investment Scheme) | 30% on up to £1m invested (£2m if at least £1m goes to knowledge-intensive companies) | Yes, if held 3+ years | ITA 2007 s.156-257 |
| SEIS (Seed EIS) | 50% on up to £200,000 invested | Yes, if held 3+ years | ITA 2007 s.257SA-SG |
| VCT (Venture Capital Trust) | 20% from 6 April 2026 (30% before; FA 2026 s.15) on up to £200,000 invested, shares held 5 years | Yes | ITA 2007 s.258-332 |

## Section 10 -- Red Lines

**Red Lines**

| Risk | Detail |
| --- | --- |
| GAAR | Finance Act 2013 s.206-215. Any arrangement that is not a "reasonable course of action" in relation to the relevant tax provisions may be counteracted. |
| DOTAS | Disclosure of Tax Avoidance Schemes. Promoters must notify HMRC of schemes. Users must disclose scheme reference numbers on tax returns. |
| Accelerated Payment Notices | HMRC can demand upfront payment of disputed tax from users of avoidance schemes. |
| IR35 | Off-payroll working rules (ITEPA 2003 Chapter 8). If HMRC determines that a self-employed contractor would be an employee "but for" the intermediary (PSC), income is taxed as employment income with full PAYE/NIC. |
| Disguised remuneration | Loans to self/employees via trusts or third parties (ITEPA 2003 Part 7A) are treated as taxable income. |
| Personal Allowance manipulation | Artificial arrangements solely to stay below £100,000 for Personal Allowance purposes may be challenged. |
| Non-commercial loss claims | Sideways loss relief requires the trade to be run on a commercial basis with a view to profit (ITA 2007 s.66). |
| Capital allowances on non-qualifying items | Only "plant and machinery" qualifies. Buildings, structures, and land do not (except via Structures and Buildings Allowance at 3%). |

## Section 11 -- Annual Tax Planning Calendar

**Annual Tax Planning Calendar**

| Month | Action |
| --- | --- |
| April | New tax year starts 6 April. Review prior year's income and plan current year. Use ISA allowance (£20,000) before 5 April if not yet done. |
| May | Register for Self Assessment if newly self-employed (by 5 October deadline, but earlier is better). |
| June | Mid-year review: estimate profits and tax liability. Plan pension contributions. |
| July | **31 July** -- 2nd payment on account for prior year. Apply to reduce if overpaying (SA303). |
| August | Review capital expenditure plans. Consider AIA timing. |
| September | Review NIC position: voluntary Class 2 if profits low. |
| October | **5 October** -- deadline to register for Self Assessment if newly self-employed. |
| November | Consider income deferral if approaching higher rate threshold. Accelerate deductible expenses. |
| December | Buy capital equipment before 31 December (if accounting period is calendar year) for AIA. |
| January | **31 January** -- Self Assessment filing deadline + 1st payment on account + balancing payment. Make pension contributions before 5 April to claim relief in current year. |
| February | Final push for pension contributions and Gift Aid donations before 5 April. |
| March | **5 April** -- tax year ends. Complete any income deferral / expense acceleration. Maximize ISA contributions. |

## Section 12 -- Cash Impact Examples (2026/27)

### Example 1 -- Personal Allowance Recovery via Pension (Income £110,000)

| Item | Without pension | With £10,000 gross pension contribution |
| --- | --- | --- |
| Adjusted net income | £110,000 | £100,000 |
| Personal Allowance | £7,570 (tapered) | £12,570 (full) |
| Tax saving from pension relief | -- | £4,000 (40% × £10,000) |
| Tax saving from PA recovery | -- | £2,000 (40% × £5,000 PA restored) |
| **Total annual saving** |  | **£6,000** |

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

### Example 2 -- Incorporation (Profits £60,000, Single, No Other Income, All Profit Extracted)

A sole trader with £60,000 profit pays income tax of £11,432 and Class 4 NIC of £2,456.60: £13,888.60. Through a company with no associated companies and no Employment Allowance, a £12,570 salary costs £1,135.50 of employer NIC, corporation tax at 19% on the remaining £46,294.50 is £8,795.96, and paying out the £37,498.54 left as dividends costs £3,977.34 of dividend tax (£500 at 0%, the rest at 10.75%, all inside the basic rate band). Total: £13,908.80. At £60,000 with everything extracted the two routes cost about the same; the company only wins when profit is retained in it or other facts change (for example the Employment Allowance is available).

| Item | Sole trader | Ltd (£12,570 salary + £37,498.54 dividends) |
| --- | --- | --- |
| Income tax | £11,432.00 | £3,977.34 (dividend tax) |
| NIC | £2,456.60 (Class 4) | £1,135.50 (employer, 15% over £5,000) |
| Corporation tax | -- | £8,795.96 (19% of £46,294.50) |
| **Total tax + NIC** | **£13,888.60** | **£13,908.80** |

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
```

### Example 3 -- AIA on Equipment Purchase (£20,000)

| Item | Without AIA | With AIA |
| --- | --- | --- |
| Deduction in Year 1 | £2,800 (14% WDA) | £20,000 (100%) |
| Tax saving at 40% | £1,120 | **£8,000 in Year 1** |

### Example 4 -- Simplified Home Office (101+ hours a month)

| Simplified expense claim | £26/month × 12 = **£312/year** |
| --- | --- |
| Tax saving at 20% | **£62.40/year** |
| Tax saving at 40% | **£124.80/year** |

### Example 5 -- EIS Investment (£50,000)

| Income tax relief (30%) | **£15,000** |
| --- | --- |
| CGT exemption on gains (if held 3+ years) | Full exemption |
| Loss relief if investment fails | Loss, net of relief, can be set against income |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Sources

| Source | URL | Read on |
|---|---|---|
| GOV.UK, Income Tax rates 2026/27 | https://www.gov.uk/income-tax-rates | 2026-10-31 |
| GOV.UK, Tax on dividends | https://www.gov.uk/tax-on-dividends | 2026-10-31 |
| Finance Act 2026 s.4 (dividend rates) | https://www.legislation.gov.uk/ukpga/2026/11/section/4 | 2026-10-23 |
| GOV.UK, Self-employed National Insurance rates | https://www.gov.uk/self-employed-national-insurance-rates | 2026-10-31 |
| GOV.UK, Rates and thresholds for employers 2026 to 2027 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 | 2026-10-23 |
| GOV.UK, Corporation Tax rates | https://www.gov.uk/corporation-tax-rates | 2026-10-23 |
| GOV.UK, Simplified expenses (mileage, use of home) | https://www.gov.uk/simpler-income-tax-simplified-expenses/print | 2026-10-31 |
| GOV.UK, Annual Investment Allowance | https://www.gov.uk/capital-allowances/annual-investment-allowance | 2026-10-23 |
| Finance Act 2026 s.28 (main pool 14%) | https://www.legislation.gov.uk/ukpga/2026/11/section/28 | 2026-10-23 |
| Finance Act 2026 s.29 (40% first-year allowance) | https://www.legislation.gov.uk/ukpga/2026/11/section/29 | 2026-10-23 |
| ITA 2007 s.24A (cap on income tax reliefs) | https://www.legislation.gov.uk/ukpga/2007/3/section/24A | 2026-10-23 |
| HMRC, Pension schemes rates 2026/27 | https://www.gov.uk/government/publications/rates-and-allowances-pension-schemes/pension-schemes-rates | 2026-10-23 |
| GOV.UK, Tapered annual allowance | https://www.gov.uk/guidance/pension-schemes-work-out-your-tapered-annual-allowance | 2026-10-23 |
| GOV.UK, Individual Savings Accounts | https://www.gov.uk/individual-savings-accounts | 2026-10-23 |
| GOV.UK, Venture capital schemes: tax relief for investors | https://www.gov.uk/guidance/venture-capital-schemes-tax-relief-for-investors | 2026-10-23 |
| Finance Act 2026 s.15 (VCT relief 20%) | https://www.legislation.gov.uk/ukpga/2026/11/section/15 | 2026-10-23 |
| VATA 1994 Sch 1 para 1 (registration threshold) | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1 | 2026-10-31 |
| HMRC, Capital Goods Scheme (VAT Notice 706/2) | https://www.gov.uk/guidance/capital-goods-scheme-notice-7062 | 2026-10-23 |
| VAT Regulations 1995 reg 113 (capital items and values) | https://www.legislation.gov.uk/uksi/1995/2518/regulation/113 | 2026-10-23 |
| GOV.UK, Business cars (40% FYA, 100% FYA before April 2027) | https://www.gov.uk/capital-allowances/business-cars | 2026-10-31 |
| GOV.UK, Voluntary National Insurance abroad from 6 April 2026 | https://www.gov.uk/government/publications/voluntary-national-insurance-contributions-for-periods-abroad-from-6-april-2026/voluntary-national-insurance-contributions-abroad-from-6-april-2026 | 2026-10-23 |
| Official page | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-10-31 |
| Official page | https://www.gov.uk/vat-registration/when-to-register | 2026-10-31 |

Not yet confirmed: nothing in this skill depends on a figure not read from the sources above.

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
