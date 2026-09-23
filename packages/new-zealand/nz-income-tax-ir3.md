---
name: nz-income-tax-ir3
description: Use this skill whenever asked about New Zealand income tax for self-employed individuals filing an IR3 return. Trigger on phrases like "how much tax do I pay in NZ", "IR3", "income tax return New Zealand", "allowable deductions NZ", "provisional tax NZ", "schedular payments", "independent earner tax credit", "IETC", "ACC levies", "Working for Families", "residual income tax", "self-employed tax NZ", "schedular withholding NZ", or any question about filing or computing income tax for a self-employed individual in New Zealand. This skill covers NZ tax brackets (10.5%-39%), IR3 return structure, allowable deductions, ACC levies, provisional tax, IETC, penalties, and interaction with GST. ALWAYS read this skill before touching any NZ income tax work.
version: 2.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand individual income tax return (IR3) for the self-employed

The IR3 return for self-employed people and others who must file: who files, tax bands, tax credits, deductions, ACC levies, due dates, terminal tax and penalties. Figures are for tax year 2026. In New Zealand that is the income year from 1 April 2026 to 31 March 2027, which Inland Revenue calls the 2027 income year. The IR3 for the 2027 income year is filed after 31 March 2027. The tax band table is headed "From 1 April 2025"; no later table is published, so it applies to the whole 2027 income year. IETC amounts are IRD's rules "From July 2024". Form IR330C is the 2024 edition. Penalty and interest rates have no tax year: they are those on IRD's pages on 22 September 2026.

## Section 1: Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | New Zealand (Aotearoa) |
| Tax | Income tax, progressive from 10.5% to 39% (band table below). ACC levies are invoiced separately by ACC |
| Currency | NZD only |
| Tax year | 1 April to 31 March, named by the year it ends. 1 April 2026 to 31 March 2027 is the 2027 income year |
| Primary legislation | Income Tax Act 2007 |
| Supporting legislation | Tax Administration Act 1994; Goods and Services Tax Act 1985 |
| Tax authority | Inland Revenue (Te Tari Taake) |
| Filing portal | myIR |
| Filing deadline | 7 July after the year ends, unless you have a tax agent or an extension of time (Section 5.9) |
| Non-residents | File an IR3NR, not an IR3 |
| Status | Drafted from IRD pages. No accountant has reviewed it yet |

### Income Tax Brackets for the 2027 income year (1 April 2026 to 31 March 2027) [T1]

**Income Tax Brackets, 2027 income year**

| Taxable income (NZD) | Rate on each dollar in the band | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals |
| Up to NZD 15,600 | 10.5% | Table headed "From 1 April 2025" |
| Above NZD 15,600 up to NZD 53,500 | 17.5% | "For each dollar of income" |
| Above NZD 53,500 up to NZD 78,100 | 30% | |
| Above NZD 78,100 up to NZD 180,000 | 33% | |
| NZD 180,001 and over | 39% | Top rate |

- **How the bands work.** Each rate applies only to the dollars inside its band ("for each dollar of income"). It is not a cliff: crossing a threshold does not change the tax on the lower dollars.
- **Tax calculation formula.** Sum, band by band, the income in the band times its rate.
- **Do not use** IRD's table "From 1 April 2024 to 31 March 2025": its composite rates are history.

### ACC Levies for the 2026-27 levy year [T1]

**ACC earners' levy, 1 April 2026 to 31 March 2027**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |
| Earners' levy rate | 1.75% | "These amounts include GST." |
| Maximum liable earnings | NZD 156,641 | No earners' levy above this |
| Maximum levy payable | NZD 2,741.22 | Per person |

- **Read the right row.** The IRD table also prints the 2027-28 levy year. Do not use it for 2026-27.
- **Who collects it.** Employees pay through PAYE. A self-employed person is invoiced by ACC, not IRD, for the Work, Earners' and Working Safer levies, after filing the IR3 (usually September on CoverPlus). ACC takes the income from IRD ([business.govt.nz ACC levies](https://www.business.govt.nz/tax-and-money/guide-to-business-tax/acc-levies)).
- **Work levy rates** by classification unit are only on acc.co.nz, which this Guide cannot cite. Use the ACC invoice; see `nz-acc-levies`.

### Provisional Tax [T1]

**Provisional Tax methods**

| Method | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option |
| Standard method | Previous year's RIT plus 5% | Or RIT from 2 years ago plus 10% if last year's return is not filed yet |
| Estimation method | Estimate this year's RIT | |
| Ratio method (GST registered) | Share of GST taxable supplies | Conditions apply |

- **Provisional tax requirement.** Residual income tax (RIT) on the last return of more than NZD 5,000 ([IRD provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax)).
- **Dates (standard option, March balance date).** 28 August, 15 January and 7 May ([IRD standard option](https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option)).
- **RIT** is income tax less tax credits (PAYE, schedular withholding, IETC). A self-employed person's ACC levies are not in it. Detail: `nz-provisional-tax`.

### Independent Earner Tax Credit (IETC) [T1]

**IETC table**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc |
| Income range for the credit | NZD 24,000 to NZD 70,000 | NZ tax residents only |
| Full credit, income up to | NZD 66,000 | "From July 2024" rules |
| Credit rate | NZD 10 per week | |
| Reduction above NZD 66,000 | 13 cents per dollar | "your entitlement reduces by 13 cents for every dollar" |
| Maximum per year | NZD 520 | "The most you can receive" |

- **IETC conditions.** NZ tax residents only. Not available if you or your partner are entitled to and receive Working for Families, or you receive an income-tested benefit, New Zealand Superannuation, a Veteran's Pension or an overseas equivalent.
- **Whole months.** Any of those payments in a month removes the IETC for that whole month.
- **Income counted.** Before-tax income, without losses brought forward. Self-employed people claim it in the IR3.

### Conservative Defaults [T1]

**Conservative Defaults**

| Situation | Default Assumption |
| --- | --- |
| GST-exclusive vs GST-inclusive unclear | Flag. Income tax uses GST-exclusive amounts for a GST-registered person |
| Mixed personal/business expense | Non-deductible until apportioned; flag for reviewer |
| Home office deduction claimed | Only the business proportion of home costs; document the basis |
| Motor vehicle: business use unclear | Use logbook records; with no logbook the claim is limited (Section 5.5) |
| Schedular payment withholding rate unknown | Ask for the IR330C. Do not assume a rate (Section 5.6) |
| ACC levy amount uncertain | Use the ACC invoice. Do not estimate a Work levy |
| Provisional tax method not specified | Standard method |

### Red Flag Thresholds [T1]

**Red Flag Thresholds**

| Flag | Threshold |
| --- | --- |
| RIT above the provisional tax threshold (Section 1) | Provisional tax required: check if paid |
| Turnover at or near the GST registration threshold (Section 5.1) | GST registration may be compulsory: verify |
| Motor vehicle claims are a large share of expenses | Logbook scrutiny: flag |
| Cash income with no trail | Document carefully; Inland Revenue audit risk |
| Single contractor relationship (regular, directed work) | Possible employment: flag |

## Section 2: Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full tax year (1 April to 31 March) in CSV, PDF, or pasted text. Confirmation of GST registration status.

**Recommended:** All client invoices, the IR330C given to each payer and the schedular payment details, motor vehicle logbook, ACC levy invoice, provisional tax payment receipts, prior year IR3.

**Ideal:** Complete accounting records (Xero or MYOB export), GST return summary, depreciation schedule, prior year notice of assessment.

### Refusal Catalogue

- **R-NZ-1.** Stop. Strip GST from all income and expense figures before computing. Mixed amounts distort the computation. (Income figures include GST but taxpayer is GST-registered.)
- **R-NZ-2.** Company income is not personal income. Only salary, shareholder salary or dividends from the company appear in the IR3. Escalate. (Company (Ltd) income mixed with personal IR3.)
- **R-NZ-3.** A non-resident files an IR3NR, not an IR3, and different rules apply. Escalate. (Non-resident with NZ-source income.)
- **R-NZ-4.** Reject an undocumented vehicle claim above the no-logbook limit (Section 5.5). (No motor vehicle logbook but large vehicle claim.)
- **R-NZ-5.** The employee versus contractor test may apply. Do not treat as self-employment without review. (Client relationship appears to be employment.)

## Section 3: Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to the Tier 1 rules in Section 5. The patterns and merchant names are this Guide's own working method; no official page lists them.

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| PAYMENT FROM [client] / TFR FROM [client] | Self-employment income | Gross revenue | |
| INTERNET TFR / ONLINE PAYMENT [client] | Self-employment income | Revenue | |
| STRIPE PAYOUT / STRIPE PAYMENTS | Self-employment income, gross-up | Revenue | Net of fees; fee deductible |
| PAYPAL TRANSFER / PAYPAL NZ | Self-employment income, gross-up | Revenue | Net of fees; fee deductible |
| WINDCAVE SETTLEMENT / EFTPOS NZ SETTLEMENT | Self-employment income, gross-up | Revenue | Card settlements |
| SQUARESPACE PAYMENTS / SQUARE NZ | Self-employment income, gross-up | Revenue | |
| SCHEDULAR PAYMENT (line annotation) | Schedular income, gross-up | Revenue | Section 5.6 |
| SALARY CREDIT [employer] | Employment income | NOT self-employment income | Taxed through PAYE |
| INTEREST PAID / BANK INTEREST | Interest income | Reportable income | Usually RWT deducted |
| DIVIDEND [company] | Dividend income | Include imputation credits | |
| IRD REFUND / INLAND REVENUE REFUND | EXCLUDE | Not income | Tax refund |
| GST REFUND IRD | EXCLUDE | Not income | GST refund, separate tax |
| RENTAL INCOME [property] | Rental income | NOT self-employment income | Rental schedule (IR3R) |

### 3.2 Expense Patterns (Debits)

**Expense Patterns (Debits)**

| Pattern | Tax Category | Treatment | Notes |
| --- | --- | --- | --- |
| RENT [office/workspace] / COMMERCIAL RENT | Office rent | Fully deductible | Home office: business share only |
| GENESIS ENERGY / MERIDIAN ENERGY / CONTACT ENERGY / MERCURY | Utilities, business proportion | Deductible | Business share |
| SPARK NZ / ONE NZ / 2DEGREES | Phone/internet, business proportion | Deductible | |
| ADOBE / MICROSOFT 365 / GOOGLE WORKSPACE / XERO / MYOB | Software subscriptions | Fully deductible | |
| CHARTERED ACCOUNTANTS / ACCOUNTANT / TAX AGENT | Accounting/tax fees | Fully deductible | |
| INTERISLANDER / BLUEBRIDGE / AIR NZ / JETSTAR | Travel (business purpose) | Deductible | Business purpose note |
| HILTON / IBIS / NOVOTEL / AIRBNB | Accommodation (business travel) | Deductible | Business purpose note |
| Z ENERGY / BP NZ / MOBIL NZ / GULL | Fuel, business proportion | Business portion | Section 5.5 |
| AA NZ / VEHICLE REGISTRATION / NZTA | Vehicle costs, business proportion | Business portion | Section 5.5 |
| ACC LEVY / ACC INVOICE | ACC levy invoice | See Section 5.2 | |
| INLAND REVENUE PROV TAX / IRD PROVISIONAL TAX | Provisional tax, NOT deductible | EXCLUDE | |
| GST PAYMENT IRD | GST payment, NOT deductible | EXCLUDE | |
| PROFESSIONAL INDEMNITY INS / PUBLIC LIABILITY INS | Business insurance | Fully deductible | |
| LINKEDIN PREMIUM / SEEK ADVERTISE / TRADEME JOBS | Business platform subscriptions | Fully deductible | |
| COURIER POST / NZ POST / DHL NZ | Postage/courier | Fully deductible | |
| BANK FEE / ACCOUNT FEE / ANZ MONTHLY FEE | Bank charges | Fully deductible | |
| XERO SUBSCRIPTION / MYOB SUBSCRIPTION | Accounting software | Fully deductible | |
| TRAINING / COURSE / CONFERENCE | Professional development | Deductible | Existing skills only |
| SUBCONTRACTOR PAYMENT / CONTRACTOR INVOICE | Subcontract expenses | Fully deductible | Schedular rules may apply |
| STRIPE FEES / PAYPAL FEES / SQUARE FEES | Payment processing fees | Fully deductible | |
| ENTERTAINMENT / MEALS CLIENT | Entertainment | Often half deductible | Section 5.3 |

## Section 4: Worked Examples

Method only; no tax amounts.

### Example 1: ANZ NZ (Auckland, IT Consultant)

**Input line (ANZ Business One CSV):**
`03/01/2027,,PAYMENT FROM ACME LTD,,11500.00,`

**Reasoning:**
If James is GST-registered and the receipt is GST-inclusive, income is the receipt less 3/23 of it. If not registered, use the receipt.

**Classification:** Self-employment income, ex-GST if registered.

### Example 2: Westpac NZ (Auckland, Photographer: Vehicle Claim)

**Input line (Westpac Business Online CSV):**
`10/08/2026,SHELL SELECT QUEENSTOWN,120.00,,`

**Reasoning:**
Petrol for client shoots. Apply Emma's logbook business share to the cost; with no logbook, the limit in Section 5.5.

**Classification:** Motor vehicle expense at the logbook share, or the no-logbook limit.

### Example 3: ASB Bank (Christchurch, Plumber: Schedular Payment)

**Input line (ASB Business Edge CSV):**
`15/03/2027,SCHEDULAR PAYMENT BUILDCO LTD,-,4000.00,`

**Reasoning:**
The payer withheld tax at the plumber's IR330C rate. Gross = amount received / (1 minus that rate); the tax withheld is a credit. Confirm in myIR.

**Classification:** Self-employment income at the gross amount. Withholding tax as a credit.

### Example 4: BNZ (Wellington, Marketing Consultant)

**Input line (BNZ Business CSV):**
`28/02/2027,TT,STRIPE PAYOUT,CODE,REF,2185.00,`

**Reasoning:**
Payout is net of fees. Take the gross from the Stripe report (ex-GST if registered); fees are deductible.

**Classification:** Gross revenue per the Stripe report. Stripe fees deductible.

### Example 5: Kiwibank (Dunedin, Freelance Writer: Foreign Income)

**Input line (Kiwibank CSV):**
`20/05/2026,PAYPAL TRANSFER USD,,,1850.00,`

**Reasoning:**
PayPal payout from USD clients. Return the NZD value (method: Section 5.7).

**Classification:** Self-employment income in NZD.

### Example 6: ANZ (Hamilton, E-commerce Seller: GST Check)

**Input line (ANZ FastNet Business CSV):**
`01/09/2026,,WINDCAVE SETTLEMENT,,8500.00,`

**Reasoning:**
Rachel's turnover is above the GST threshold in Section 5.1, so she must register. Strip 3/23 from GST-inclusive amounts.

**Classification:** Revenue, ex-GST. RED FLAG: verify GST registration.

## Section 5: Tier 1 Rules (When Data Is Clear)

### 5.1 GST-Registered: Always Use Ex-GST Amounts

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/gst/registering-for-gst |
| Compulsory GST registration: turnover in the last or next 12 months | NZD 60,000 | Web page: "at least"; guide IR375: "over" |

- **GST-registered ex-GST rule.** Report income and expenses ex-GST. Take 3/23 out of a GST-inclusive amount; the GST rate is 15% ([IRD IR295](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf)). Detail: `new-zealand-gst`, `nz-gst-return`.

### 5.2 ACC Earners' Levy Is Not Part of the IR3 Tax Payment

- **Old rule corrected.** A self-employed person does NOT pay the earners' levy with the IR3. ACC invoices it with the Work and Working Safer levies after the return is filed (Section 1).
- **Deductibility.** The legacy Guide treats the Work levy as deductible. No allowed page read states the income tax treatment of ACC levies for the self-employed. Confirm before claiming.

### 5.3 Entertainment: 50% Limitation

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/entertainment-expenses |
| Not completely business related (significant private element) | 50% | "even if you think the private element was more or less" |
| Completely business related | 100% | E.g. meals an employee buys while travelling on business (not with a business contact), entertainment enjoyed outside New Zealand |

- **Entertainment limitation rule.** Half-deductible examples: sports or cultural events, holiday home, boat hire, parties, food and drink gifts, and meals with a business contact. Purely personal entertainment is not deductible. See IRD guide IR268.

### 5.4 Provisional Tax Is Not Deductible

- **Provisional tax not deductible rule.** Provisional tax instalments are advance payments of income tax, not business expenses. Always exclude them from expenses. Credit them against the year's tax.

### 5.5 Motor Vehicle Logbook Required for > 25% Business Use

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses |
| No logbook: claim limited to this share of running costs | 25% | IRD may still ask you to back it up |

- **Motor vehicle logbook rule.** Keep a logbook for at least 90 consecutive days (odometer at start and end; date, distance and reason of each business trip). Apply the business share of distance to all vehicle costs. It lasts up to 3 years unless business use changes by more than 20% ([IRD use a logbook](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses/use-a-logbook)).
- Home to work is a personal trip. If you use kilometre rates or actual costs, IRD says: "You need to continue to use 1 method for as long as you own the vehicle." Detail: `nz-motor-vehicle-expenses-logbook-business-use`.

### 5.6 Schedular Payments: Always Gross Up

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir330c/ir330c-2024.pdf |
| No IR330C given: no-notification rate | 45% | Non-resident contractor companies: 20% |

- **Schedular payment gross-up rule.** Gross income = amount received / (1 minus the withholding rate). The withheld tax is a credit.
- **No flat default rate.** The contractor uses the standard rate for the activity (IR330C flow chart), a tailored rate, or their own rate of at least 10%, or at least 15% on a temporary visa ([IRD declare my tax rate](https://www.ird.govt.nz/income-tax/withholding-taxes/schedular-payments/getting-schedular-payments/work-out-and-declare-my-tax-rate-for-schedular-payments)). Read the actual rate from the payer or myIR.

### 5.7 Foreign Currency Income: Use NZD at Date of Receipt

- **Foreign currency income rule.** Income received in a foreign currency is returned in NZD. The legacy rule converts at the exchange rate on the date of receipt, or an annual average rate by agreement, and never at the year-end rate. No IRD page was read to confirm this; treat the method as unconfirmed and ask the accountant.

### 5.8 Tax Computation Flow

- **Tax Computation Flow.** Gross self-employment receipts (ex-GST if registered), plus other income (interest, dividends with imputation credits, schedular income grossed up), less allowable business expenses, equals taxable income. Apply the bands in Section 1. Less: IETC if eligible (Section 1). Less: PAYE, schedular withholding, RWT and imputation credits. Less: provisional tax paid. Equals residual income tax payable or a refund. The ACC levies are billed separately by ACC (Section 5.2).

### 5.9 Filing Deadlines

**Filing Deadlines**

| Item | Deadline | Source |
| --- | --- | --- |
| IR3 due (no tax agent, no extension) | 7 July; for the 2027 income year, 7 July 2027 | [IRD IR3](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3) |
| IR3 due (tax agent's client with an extension of time) | "up to 31 March the following year"; for the 2027 income year, 31 March 2028 | [IRD extension of time](https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements) |
| Terminal tax | 7 February of the year after the bill; for the 2027 income year, 7 February 2028 | [IRD timelines](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/timelines-at-the-end-of-the-tax-year) |
| Terminal tax with a tax agent's extension | 7 April; for the 2027 income year, 7 April 2028 | [IRD interest on provisional tax](https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax) |
| Provisional tax | Section 1 | |

- The agent extension is one the Commissioner "can give"; IRD may withdraw it for the next year if a return is not filed by 31 March.
- Wait until June to file if employers, banks or PIE providers still have to report income to IRD.

### 5.10 Penalties

**Late filing penalty (income tax return)**

| Net income | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties |
| Less than NZD 100,000 | NZD 50 | Initially charged at this amount |
| NZD 100,000 to NZD 1 million | NZD 250 | Adjusted after you file to the actual net income shown |
| More than NZD 1 million | NZD 500 | |

**Late payment penalties**

| Stage | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties |
| Day after the due date | 1% | |
| 7th day after, on tax and penalties still unpaid | 4% | |
| Monthly penalty | Not for income tax | Excepted: "GST, income tax including provisional tax" |

**Use-of-money interest**

| Item | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments |
| Underpaid tax, from 16 January 2026 | 8.97% | Check for a newer row |
| Overpaid tax, from 16 January 2026 | 2.25% | Interest IRD pays you |

**Shortfall penalties**

| Behaviour | Share of the shortfall | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/shortfall-penalties |
| Not taking reasonable care | 20% | |
| Unacceptable tax position | 20% | Only if the income tax shortfall is more than both NZD 50,000 and 1% of the total tax figure |
| Gross carelessness | 40% | |
| Abusive tax position | 100% | |
| Evasion | 150% | |

- A first late payment in 2 years may get a grace period. Voluntary disclosure can lower a shortfall penalty.

## Section 6: Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Mixed Company/Personal Income

Company income is not reportable in the IR3; only salary, shareholder salary or dividends from the company appear. Clarify the business structure before proceeding.

### 6.2 Rental Property Income

Reported on the rental income schedule (IR3R). From 1 April 2025 residential rental interest is again fully deductible ([IRD interest limitation rules](https://www.ird.govt.nz/property-interest-rules): "From 1 April 2025 you can claim 100% of the interest you incur."), if the general deductibility rules are met. Ring-fenced residential rental losses may apply. Refer anything beyond a simple single rental.

### 6.3 Brightline Property Sale

The legacy "10-year" test is out of date. For property sold on or after 1 July 2024, the [bright-line test](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test) looks at whether the end date is "within 2 years" of the start date: the start is usually title transfer (settlement), the end is the binding sale agreement. A property that has been your main home is generally excluded when your use meets certain criteria; business premises and farmland are also excluded. Older periods apply to sales before 1 July 2024. Confirm both dates. See `nz-capital-gains`.

### 6.4 Working for Families Tax Credits

The IETC cannot be claimed for any month in which the person or their partner is entitled to and receives Working for Families (Section 1). Working for Families has its own abatement. Confirm eligibility before applying either.

### 6.5 Non-Resident NZ-Source Income

A non-resident files an IR3NR, not an IR3, and non-resident withholding rules apply. Do not apply this Guide. Residence tests are in `nz-tax-residency`.

### 6.6 Imputation Credits on Dividends

Dividends are returned with the imputation credits attached; the imputation credit is a tax credit. Require the dividend statement from the company.

### 6.7 Losses in Prior Years

A business loss can be carried forward to reduce later taxable income if the criteria are met. Confirm with the prior year return. Losses brought forward do not count in the income test for the IETC.

## Section 7: Excel Working Paper Template

~~~
NEW ZEALAND INCOME TAX WORKING PAPER (IR3, SELF-EMPLOYED)
Taxpayer: _________  IRD number: _________
Income year: 2027 income year (1 April 2026 to 31 March 2027)

SECTION A: SELF-EMPLOYMENT INCOME (ex-GST)
                                        NZD
Gross self-employment receipts         _____
Less: GST component (if incl.)         (_____)
Net ex-GST income                      _____
Schedular income (grossed up)          _____
Other business income                  _____
TOTAL INCOME                           _____

SECTION B: DEDUCTIBLE EXPENSES
Rent / workspace (business portion)    _____
Utilities (business proportion)        _____
Phone / internet (business share)      _____
Software subscriptions                 _____
Accounting / tax agent fees            _____
Legal fees                             _____
Travel (business trips)                _____
Accommodation (business travel)        _____
Meals and entertainment (Section 5.3)  _____
Business insurance                     _____
Bank charges (business account)        _____
Motor vehicle (logbook share)          _____
ACC Work levy (confirm, Section 5.2)   _____
Depreciation                           _____
Subcontractor costs                    _____
Payment processor fees                 _____
Other business expenses                _____
TOTAL DEDUCTIBLE EXPENSES              _____

SECTION C: NET TAXABLE INCOME
Total income less total expenses       _____

SECTION D: INCOME TAX
Tax at band rates (Section 1 table)    _____
Less: IETC (if eligible, Section 1)    (_____)
NET INCOME TAX                         _____

SECTION E: ACC LEVIES
Invoiced by ACC after the return is filed; not part of this bill.
Record the invoice for the year's expenses and cash planning.

SECTION F: RIT AND PROVISIONAL TAX
Income tax less withholding credits    _____
Less: provisional tax paid             (_____)
BALANCE DUE / (REFUND)                 _____
Next year provisional (standard option, Section 1): _____

SECTION G: REVIEWER FLAGS
[ ] GST stripped from income/expenses (if GST-registered)?
[ ] Schedular payments grossed up and withholding credit recorded?
[ ] Motor vehicle logbook reviewed, business share substantiated?
[ ] Entertainment split between the full and half-deductible groups?
[ ] Home office: business proportion documented?
[ ] ACC levy treatment confirmed?
[ ] Provisional tax instalments reconciled against the IRD account?
[ ] Foreign income converted to NZD?
~~~

## Section 8: Bank Statement Reading Guide

### New Zealand Bank Statement Formats

**NZ Bank Statement Formats**

These layouts are this Guide's own working assumptions, carried from the legacy version; no bank or IRD page confirms them. Check the client's file.

| Bank | Format | Key Fields |
| --- | --- | --- |
| ANZ NZ | CSV | Date,Description,Debit,Credit,Balance |
| BNZ (Bank of New Zealand) | CSV | Date,Tran Type,Particulars,Code,Reference,Amount,Balance |
| ASB Bank | CSV | Date,Unique Id,Tran Type,Cheque Number,Payee,Memo,Amount |
| Westpac NZ | CSV | Date,Narrative,Debit Amount,Credit Amount,Balance |
| Kiwibank | CSV | Date,Description,Debit,Credit,Balance |

### Key NZ Banking Narrations

**Key NZ Banking Narrations**

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| PAYMENT FROM [name] / TFR FROM [name] | Bank transfer in | Potential business income |
| INTERNET TFR | Online transfer | Income or expense |
| D/C (Direct Credit) | Direct credit | Potential income |
| D/D (Direct Debit) | Direct debit | Recurring expense |
| ATM WITHDRAWAL | Cash withdrawal | Personal: investigate |
| IRD PROV TAX / INLAND REVENUE | Tax payment | Tax prepayment: exclude |
| GST PAYMENT | GST remittance | Separate tax: exclude |
| INTEREST | Bank interest | Other income |
| ACC LEVY | ACC invoice payment | Levy invoice: see Section 5.2 |

### NZ Three-Part Narration (Particulars/Code/Reference)

NZ bank-to-bank transfers allow three fields the sender fills in:
- **Particulars:** Usually the payer's name or invoice reference
- **Code:** Account code or project reference
- **Reference:** Invoice number, date, or other identifier

Combine all three to identify the transaction source.

### Amount Format Notes

- Date format: DD/MM/YYYY
- Amount format: no thousands separator, period decimal (e.g., 11500.00)
- ANZ/Westpac: separate Debit/Credit columns
- BNZ/ASB: single Amount column (positive = credit, negative = debit)

## Section 9: Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all PAYMENT FROM / TFR FROM credits from non-personal sources as potential self-employment income.
2. Apply conservative defaults: not GST-registered (use face value), the no-logbook vehicle limit, no IETC.
3. Exclude all IRD PROV TAX and GST PAYMENT debits from expenses.
4. Mark all Stripe/PayPal/Windcave receipts for gross-up.
5. Treat all entertainment as half-deductible pending confirmation (Section 5.3).
6. Generate the working paper with PENDING flags.

Present these questions:

~~~
ONBOARDING QUESTIONS: NEW ZEALAND INCOME TAX (IR3)
1. Are you GST-registered? If so, are your bank amounts GST-inclusive or exclusive?
2. Tax year: are we preparing the 2027 income year (1 April 2026 to 31 March 2027)?
3. Do you use a vehicle for work? Do you have a logbook of at least 90 consecutive days?
4. Do you work from a dedicated home office? What share of the home does it use?
5. Did any clients deduct schedular withholding tax before paying you? At what rate?
6. Did you pay provisional tax this year? How much, and on which dates?
7. Do you or your partner receive Working for Families tax credits?
8. Any income from rental properties?
9. Did you receive dividends from NZ companies (imputation credits)?
10. Any foreign currency income? From which countries?
~~~

## Section 10: Reference Material

### Key Legislation

**Key Legislation table**

| Topic | Reference |
| --- | --- |
| Income tax (general) | Income Tax Act 2007 |
| Filing and penalties | Tax Administration Act 1994 |
| GST (separate) | Goods and Services Tax Act 1985 |
| Schedular payments | Income Tax Act 2007 (schedular payment rules) |
| Entertainment limitation | Income Tax Act 2007 subpart DD |
| Depreciation | Income Tax Act 2007 subpart EE |
| ACC levies | Accident Compensation Act 2001 |

Subpart references are from the legacy Guide and unchecked (legislation.govt.nz cannot be cited).

### Known Gaps / Out of Scope

- Company (Ltd) income tax
- Non-resident NZ-source income (IR3NR)
- Bright-line property gains (see `nz-capital-gains`)
- Working for Families calculations
- GST return computation (see `nz-gst-return`)
- KiwiSaver employer contribution calculations
- ACC Work levy rates by classification unit (see `nz-acc-levies`)

### Changelog

**Changelog table**

| Version | Date | Change |
| --- | --- | --- |
| 2.1 | September 2026 | Refreshed for the 2027 income year from IRD pages |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; NZ bank formats; transaction pattern library; worked examples; prohibitions and disclaimer added |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] GST stripped from all amounts for GST-registered taxpayers?
- [ ] Schedular payments grossed up (not the net bank receipt)?
- [ ] Motor vehicle claim supported by a logbook, or within the no-logbook limit?
- [ ] Entertainment split correctly (Section 5.3)?
- [ ] ACC levies left out of the IR3 tax bill (they are invoiced by ACC)?
- [ ] ACC levy deduction treatment confirmed?
- [ ] Provisional tax excluded from expenses?
- [ ] Foreign currency converted to NZD?
- [ ] RIT correctly computed (income tax less credits)?
- [ ] Bands from the "From 1 April 2025" table, not the 2024-25 composite table?

## PROHIBITIONS

- NEVER include GST-inclusive amounts in income or expenses for GST-registered taxpayers. Always strip GST first
- NEVER claim motor vehicle business use above the no-logbook limit without a qualifying logbook (90+ consecutive days)
- NEVER deduct more than half of entertainment that has a significant private element
- NEVER include provisional tax or GST payments as deductible business expenses
- NEVER apply the IETC for a month in which the taxpayer or partner receives Working for Families, or the taxpayer receives NZ Super, an income-tested benefit or a Veteran's Pension
- NEVER add the ACC earners' levy of a self-employed person to the IR3 tax bill; ACC invoices it
- NEVER assume a flat schedular withholding rate; read the IR330C or the payer's records
- NEVER treat schedular payment net receipts as gross income. Always gross up
- NEVER apply resident rules to non-residents. Escalate
- NEVER present tax calculations as definitive. Always label them as estimates and direct the client to their accountant for confirmation

## The method, step by step

1. **Must they file?** Yes if they had more than NZD 200 (before tax) of income IRD was not told about, such as self-employment income ([IRD IR3](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3)). Non-residents file an IR3NR.
2. **Business income and expenses** under the Income Tax Act 2007: ex-GST if registered, schedular income grossed up, vehicle and entertainment rules (Section 5, [IRD vehicle expenses](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses)).
3. **Apply the bands** from the table "From 1 April 2025" ([IRD tax rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals)).
4. **Take off credits:** IETC if eligible ([IRD IETC](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc)), PAYE, schedular tax, RWT, imputation credits, provisional tax paid.
5. **File the IR3 and pay** by the dates in Section 5.9 ([IRD extension of time](https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements)).
6. **Next year:** provisional tax if RIT was over the threshold in Section 1; the ACC invoice follows the return ([business.govt.nz ACC levies](https://www.business.govt.nz/tax-and-money/guide-to-business-tax/acc-levies)).

## Ask the client first

- Are you a New Zealand tax resident for the whole year? (A non-resident files an IR3NR; see `nz-tax-residency`.)
- Are you GST-registered, and are your figures GST-inclusive?
- Did any payer withhold schedular tax, and what IR330C rate did you give them?
- Do you or your partner receive Working for Families, or do you receive NZ Super, an income-tested benefit or a Veteran's Pension, in any month? (This removes the IETC for that month.)
- Do you have a tax agent with an extension of time? (It moves the filing and payment dates.)
- Do you keep a vehicle logbook of at least 90 consecutive days?

## When to refuse or refer

- The income belongs to a company, partnership, look-through company or trust: this Guide covers one individual's IR3 only.
- The person is not a New Zealand tax resident, or became or stopped being resident during the year, or may be a transitional resident.
- Sale of residential property that may fall under the bright-line test, or rental with ring-fenced losses.
- Foreign income with foreign tax credits, foreign investment funds, or cryptoassets (see `new-zealand-crypto-tax`).
- A shortfall penalty, a dispute with IRD, a voluntary disclosure, or years of unfiled returns.
- Employee versus contractor doubt, or ACC Work levy classification questions (see `nz-acc-levies`).

## Sources

- https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals
- https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc
- https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates
- https://www.business.govt.nz/tax-and-money/guide-to-business-tax/acc-levies
- https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3
- https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/timelines-at-the-end-of-the-tax-year
- https://www.ird.govt.nz/topics/intermediaries/extension-of-time-arrangements
- https://www.ird.govt.nz/income-tax/provisional-tax
- https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option
- https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option
- https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax
- https://www.ird.govt.nz/gst/registering-for-gst
- https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf
- https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/entertainment-expenses
- https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses
- https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses/use-a-logbook
- https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir330c/ir330c-2024.pdf
- https://www.ird.govt.nz/income-tax/withholding-taxes/schedular-payments/getting-schedular-payments/work-out-and-declare-my-tax-rate-for-schedular-payments
- https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties
- https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties
- https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments
- https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/shortfall-penalties
- https://www.ird.govt.nz/property-interest-rules
- https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant CA ANZ, or equivalent licensed practitioner in New Zealand) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by OpenAccountants.

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
