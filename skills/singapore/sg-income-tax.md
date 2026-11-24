---
name: sg-income-tax
description: Use this skill whenever asked about Singapore income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay in Singapore", "Form B", "Form B1", "IRAS income tax", "trade income", "capital allowances Singapore", "personal reliefs", "tax residence 183 days", "Section 10(1)(a)", "CPF self-employed", "self-employed tax Singapore", "myTax Portal", "DBS Bank statement", "OCBC income", "PayNow transfer", "Stripe Singapore", or any question about filing or computing income tax for a Singapore sole proprietor or freelancer. This skill covers progressive rates (0--24%), trade income computation, capital allowances (Section 19/19A), approved deductions, personal reliefs, CPF MediSave, tax residence rules, filing deadlines, and penalties. ALWAYS read this skill before touching any Singapore income tax work.
version: 3.1
jurisdiction: SG
tax_year: 2026
last_updated: 2026-11-22
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
tax_year_notes: "2026 income, ordinarily YA 2027; historical YA 2026 filing expressly separated"
---

# Singapore self-employed income tax, 2026 income / YA 2027 v3.1

2026 income, ordinarily YA 2027, for resident sole proprietors and freelancers. Confirm the accounting basis period. The [IRAS calendar](https://www.iras.gov.sg/due-dates?dueYear=2027) gives 18 April 2027 as the filing deadline. The resident rate table applies from YA 2024. Section 5 covers the YA 2027 changes to deemed expenses and CPF cash top-up relief.

## Scope and who this is for


| Field | Value |
| --- | --- |
| Country | Singapore |
| Tax | Individual income tax, progressive resident rates (table below) |
| Currency | SGD only |
| Tax year basis | YA 2027 uses the preceding year for individuals. Confirm the 2026 accounting period used for business income. |
| Primary legislation | Income Tax Act 1947 |
| Tax authority | Inland Revenue Authority of Singapore (IRAS) |
| Filing portal | myTax Portal, with Singpass or a Singpass Foreign User Account |
| Return | Form B/B1 (self-employed) |
| Filing deadline | 18 April 2027, subject to any specific IRAS notice |

### Tax residence for YA 2027

Check the following residence tests for YA 2027. [IRAS tax residency](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency)

- a Singapore Citizen or Singapore Permanent Resident who normally resides in Singapore except for temporary absences; OR
- a foreigner who stayed or worked in Singapore for at least 183 days in calendar year 2026; OR
- a foreigner who stayed or worked in Singapore continuously for 3 consecutive years (an administrative concession that applies even if the first and third years are under 183 days); OR
- a foreign employee whose employment straddles 2 calendar years with a continuous stay of at least 183 days. This last test is for employees only and excludes directors, public entertainers and professionals, so it does not help a self-employed person.

A foreign employee with a work pass valid for at least 1 year can be treated as resident initially. IRAS reviews the status at tax clearance using the actual stay. Apply the appropriate residence tests before calculating a sole proprietor’s tax. Refer unresolved residence or treaty questions.

### Conservative Defaults

| Ambiguity | Default |
| --- | --- |
| Tax residence unknown | STOP. Do not compute. |
| GST status unknown | Hold GST/revenue split pending registration date and invoices; ask |
| Vehicle type unknown | Private car (S-plate): no capital allowances and no running costs |
| Business vs capital expenditure unclear | Capital: no deduction until confirmed as revenue |
| Home office apportionment unknown | No deduction until a basis is confirmed |
| Personal relief facts unknown | Apply only reliefs whose 2026 conditions are confirmed |
| Accounting year end unknown | Ask. Do not assume 31 Dec |


## Ask the client first


- Where were you resident in 2026: citizen, PR, or a foreigner with how many days in Singapore (and in the years either side)? This decides whether any of this skill applies.
- When does your accounting year end? A non-December year end changes which accounts feed YA 2027.
- Are you GST-registered, and from what date? Which invoices include output GST?
- Are you a commission agent, private hire car or taxi driver, or delivery worker? FEDR may replace actual expenses.
- What vehicle do you use: private car (S, Q or E plate) or a van, lorry or motorcycle? This decides whether any motor cost or allowance is allowed.
- What are the gross income and actual expenses of every nature of business, including separate businesses within the same NOB, for FEDR eligibility? Which of these did you have in 2026: compulsory MediSave, voluntary CPF, SRS contributions, children born or adopted (and their dates), parents you supported? Each relief turns on 2026 facts.


### Section 2. Required inputs and refusal catalogue


### Required Inputs

**Minimum viable:** bank statements for the whole accounting period (usually 1 Jan to 31 Dec 2026) in CSV, PDF or pasted text; confirmation of tax residence; whether GST-registered; the accounting year end.

**Recommended:** client invoices; CPF statements showing compulsory MediSave and any voluntary contributions paid in 2026; SRS statements; life insurance premium notices; details of children and parents for relief claims.

**Ideal:** fixed asset register; the prior year Notice of Assessment; Form IR8A if also employed; GST returns if GST-registered.

### Refusal Catalogue

- **R-SG-1. Non-residents.** Non-resident income is taxed differently and non-residents get no personal reliefs. Out of scope. Route residence questions to `sg-tax-residency`.
- **R-SG-2. Companies (Pte Ltd, Ltd).** Corporate income tax and Form C-S or Form C are out of scope. This skill covers individuals only.
- **R-SG-3. Partnerships.** Allocating partnership income (Form P) is out of scope. Escalate.
- **R-SG-4. Capital gains and property disposals.** Whether a gain is trading income needs specialist review. See `sg-zero-cgt`.
- **R-SG-5. GST computation.** GST registration, returns and input tax are out of scope. See `sg-gst-return`.
- **R-SG-6. Not Ordinarily Resident (NOR) scheme.** The scheme has ceased. Do not apply it to YA 2027 (Section 10).


## Rates, bands and thresholds
### Resident rate table, YA 2027 (income earned in 2026)

These are the resident rates "From YA 2024 onwards", so they apply to YA 2027. The third column is IRAS's cumulative gross tax on all chargeable income below the slice. The last two rows are non-resident rates, shown here because IRAS prints them on the same page.

| Chargeable income slice | Rate | Gross tax on income below this slice |
| --- | --- | --- |
| First SGD 20,000 | 0% | nil  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 20,000 to SGD 30,000 | 2% | nil  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 30,000 to SGD 40,000 | 3.5% | SGD 200  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 40,000 to SGD 80,000 | 7% | SGD 550  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 80,000 to SGD 120,000 | 11.5% | SGD 3,350  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 120,000 to SGD 160,000 | 15% | SGD 7,950  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 160,000 to SGD 200,000 | 18% | SGD 13,950  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 200,000 to SGD 240,000 | 19% | SGD 21,150  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 240,000 to SGD 280,000 | 19.5% | SGD 28,750  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 280,000 to SGD 320,000 | 20% | SGD 36,550  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 320,000 to SGD 500,000 | 22% | SGD 44,550  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| SGD 500,000 to SGD 1,000,000 | 23% | SGD 84,150  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Above SGD 1,000,000 | 24% | SGD 199,150  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Non-resident: taxable employment income | 15% | Compare with the progressive resident rates and use the higher tax amount. Check the exemption for employment of 60 days or less and its exclusions for directors, public entertainers and professionals. [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Non-resident: director's fees, consultation fees, rental and all other income | 24% | Except employment income and income taxed at reduced withholding rates  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |

Table 3 applies to YA 2024 and later. The Second Schedule also shows the historical rate tables for YA 2012 to 2016 and YA 2017 to 2023. [Income Tax Act 1947, Second Schedule](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=Sc2-)

| Item | Rate | Note |
| --- | --- | --- |
| Table 3, every dollar of chargeable income above SGD 1,000,000 | 24% | Table 3 only; the YA 2017 to 2023 table stops at a lower top rate  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |

No Personal Income Tax Rebate is printed for YA 2027. The IRAS rebate page covers "Years of Assessment (YAs) 2024 and 2025" only and says the rebate "cannot be carried forward". Do not deduct a rebate in a YA 2027 computation unless IRAS publishes one.


## The method, step by step


1. Confirm the year and the person. YA 2027 taxes 2026 income ([IRAS tax residency page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency)). Confirm the person is self-employed: a sole proprietor or partner registered with ACRA is generally self-employed and reports business income, not salary ([IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)).
2. Confirm tax residence for YA 2027 using the tests under Scope. A non-resident is out of scope (refusal R-SG-1). See the [IRAS tax residency page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency).
3. Confirm the accounting period. Most businesses end on 31 Dec, so the 2026 accounts feed YA 2027; a different year end feeds the YA after the year in which it ends ([IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)).
4. Reconcile invoices, settlement reports and receipts (Sections 3 and 8). Exclude output GST shown on the supply records. Check the effective registration date and the GST treatment of each supply. [IRAS GST rates](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates)
5. Deduct the actual allowable expenses or the applicable deemed expenses. Check the industry-specific and YA 2027 broad-based FEDR conditions in Section 5.3. [IRAS business expenses and deductions](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions) · [IRAS FEDR](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/fixed-expense-deduction-ratio-for-self-employed-persons-and-platform-workers)
6. Claim capital allowances on qualifying plant and machinery under Section 19 or 19A of the Income Tax Act 1947 (Section 5.2; [IRAS capital allowances page](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances)). Never on an S-plated private car.
7. Report revenue and adjusted profit on Form B/B1 using the 2-line or 4-line statement for the revenue level (Section 5.5). [IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)
8. Deduct qualifying donations made in 2026 from statutory income to reach assessable income ([IRAS donations page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations)).
9. Deduct personal reliefs, each tested on 2026 facts, within the overall relief cap (Section 5.4; [IRAS tax reliefs page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs)). The result is chargeable income.
10. Apply the resident Rates, bands and thresholds table ([IRAS individual income tax rates](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates)). IRAS prints a Personal Income Tax Rebate for YA 2024 and YA 2025 only, so apply none for YA 2027 unless IRAS publishes one ([IRAS Personal Income Tax Rebate page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/personal-income-tax-rebate)).
11. File by 18 April 2027 and pay within 1 month of the Notice of Assessment, subject to a specific notice or approved payment plan (Sections 5.5 and 5.6). [IRAS calendar](https://www.iras.gov.sg/due-dates?dueYear=2027)


### Section 3. Transaction pattern library


This is the deterministic pre-classifier. When a bank statement line matches a pattern, treat it as a reconciliation prompt; substantiate the underlying transaction before applying a final treatment. If no pattern matches, fall through to the rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| FAST [client name] / FAST CREDIT | Potential business income | Verify invoice/purpose | Local fast payment from a business client |
| PayNow [sender name] / PAYNOW CREDIT | Potential business income | Verify invoice/purpose | PayNow linked to NRIC or UEN |
| GIRO CREDIT [client] | Business income | Revenue | GIRO standing instruction payment from a client |
| TT FROM [client] / TELEGRAPHIC TRANSFER | Business income | Revenue | Overseas client wire transfer |
| STRIPE PAYOUT SG / STRIPE TRANSFER | Business income | Revenue, grossed up | Payout is net of Stripe fees: record gross revenue and the fee separately |
| WISE TRANSFER IN / WISE CREDIT | Business income | Revenue | Wise international payout |
| PAYPAL SG TRANSFER / PAYPAL CREDIT | Business income | Revenue, grossed up | PayPal payout, net of fees |
| SHOPEE PAY SETTLEMENT / SHOPEE PAYOUT | Business income | Revenue, grossed up | Shopee seller settlement |
| CAROUSELL PAYOUT / CAROUSELL SETTLEMENT | Business income | Revenue | Carousell business seller payout |
| GRAB FOR BUSINESS / GRABPAY SETTLEMENT | Business income | Revenue | GrabPay business payout; check whether FEDR applies (Section 5.3) |
| CHEQUE DEPOSIT / CHQ DEP [ref] | Business income | Revenue | Client cheque |
| SALARY CREDIT [employer] | Employment income | NOT business income | Separate source; Form IR8A |
| INTEREST CREDIT / INT EARNED [bank] | Interest | NOT business income | IRAS treats bank interest as generally tax-exempt for individuals |
| DIVIDEND FROM [company] | Dividends | NOT business income | IRAS treats dividends as generally tax-exempt for individuals |
| INCOME TAX REFUND / IRAS REFUND | EXCLUDE | Not income | Tax refund |
| LOAN DRAWDOWN / LOAN DISBURSEMENT | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT [landlord] / COMMERCIAL LEASE | Rent | Allowable | Rent for the business |
| SERVICED OFFICE [WeWork/JustCo/The Work Project] | Rent | Allowable | Co-working used for the business |
| SP SERVICES / SP GROUP UTILITIES | Utilities | Business portion only | Home use: apportion, Section 6.1 |
| SINGTEL BROADBAND / STARHUB HOME / M1 FIBRE | Telephone and internet | Business portion only | Mixed use: apportion |
| SINGTEL MOBILE / STARHUB MOBILE / M1 MOBILE | Telephone | Business portion only | Mixed use: apportion |
| GRAB [ride] / GOJEK / COMFORT TAXI | Travel | Check the trip purpose and keep the receipt | See the distinction between buying transport and hiring a private car in Section 6.2 |
| SINGAPORE AIRLINES / SCOOT / JETSTAR | Travel | Allowable only for a business trip | Travelling expenses for personal trips are private |
| MRT / SBS TRANSIT / EZ-LINK | Travel | Allowable only in the course of business | Travel to and from home is private |
| GOOGLE ADS / META / LINKEDIN | Advertising | Allowable | IRAS lists advertising costs as allowable |
| AMAZON.SG [supplies] / CHALLENGER [office] | Stationery, supplies or equipment | Allowable if a running cost | Equipment is capital: Section 5.2 |
| ADOBE / MICROSOFT 365 / NOTION / SLACK | Software subscription | Allowable | Owned software or a computer is capital: Section 5.2 |
| CPFB [CPF BOARD] MEDISAVE | Own CPF | NOT a business expense | IRAS lists your own MediSave and CPF contributions as disallowable; claim CPF relief instead (Section 5.4) |
| AIA / PRUDENTIAL / GREAT EASTERN / INCOME INSURANCE | Own life insurance | NOT a business expense | Private; Life Insurance Relief may apply (Section 5.4) |
| IRAS INCOME TAX / IRAS NOA | EXCLUDE | Tax payment | Personal income tax is disallowable |
| IRAS GST PAYMENT | EXCLUDE | GST payment | Not income tax |
| BANK CHARGES / ADMIN FEE [DBS/OCBC/UOB] | Bank charges | Allowable if business account | Personal account: private |
| STRIPE FEE / PAYPAL FEE / WISE FEE | Transaction fees | Allowable | Payment processing |
| HIRE PURCHASE / VEHICLE LOAN [bank] | Capital repayment | Principal NOT deductible | Hire purchase interest is allowable; the asset itself goes to capital allowances if it qualifies |
| SHELL / ESSO / SPC / CALTEX [fuel] | Motor | Check the vehicle and use | Qualifying business vehicles and eligible driving businesses have their own rules (Section 6.2) |
| PERSONAL WITHDRAWAL / OWN TRANSFER | EXCLUDE | Drawings | Not a business expense |

### 3.3 Capital Allowance Qualifying Assets

| Asset Purchased | Treatment | Notes |
| --- | --- | --- |
| Computer / laptop / printer [Apple/Lenovo/Dell/HP] | 1-year write-off, Section 19A(2) | Computers and prescribed automation equipment |
| Office phone / tablet | 1-year write-off if a low-value asset, Section 19A(10A); otherwise 3 years or working life | Low-value limit and yearly cap in Section 5.2 |
| Office furniture / desk [IKEA/Harvey Norman/Gain City] | Low-value 1-year write-off, or 3 years, or working life | Furniture and fixtures qualify as plant |
| Camera / video equipment (business) | Low-value 1-year write-off, or 3 years, or working life | If used in the business |
| Private car (S-plate) | NO capital allowances | Running costs are also disallowable |
| Commercial van / lorry / motorcycle | Section 19 or 19A | Capital allowances claimable; COE paid is part of cost |


### Section 5. Rules and reliefs


### 5.1 Business Income Computation

~~~
Gross revenue from the trade, business, profession or vocation
Less: cost of goods sold, where applicable (service-only revenue equals gross profit)
Less: allowable business expenses (Section 5.3)
Less: capital allowances (Section 5.2); add any balancing charge on disposal
= Adjusted profit (the figure on the 2-line or 4-line statement)
Add: other income (employment, rental, etc.) = statutory income
Less: qualifying donations made in 2026 (Section 5.4, donations table)
= Assessable income
Less: personal reliefs, tested on 2026 facts, within the overall relief cap
= Chargeable income
Apply the resident rate table above
Less: Parenthood Tax Rebate if claimable; no Personal Income Tax Rebate is printed for YA 2027
= Tax payable (estimate until IRAS issues the Notice of Assessment)
~~~

IRAS sets the order: "Total statutory income Less: Donations =Assessable income Less: Personal reliefs =Chargeable income" ([IRAS donations page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations)).

### 5.2 Capital Allowances

Capital allowances replace depreciation, which is not deductible. They apply to plant and machinery used in the business. The IRAS page below is written for companies; the IRAS page for self-employed persons sends them to it: "depreciation of fixed assets may be claimed as capital allowances" ([IRAS business expenses and deductions](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions)).

| Method or limit | Value | Note |
| --- | --- | --- |
| 1-year write-off, Section 19A(2) and 19A(10A): computers, prescribed automation equipment, low-value assets | 100% | Of cost in one YA. Only these assets, not every asset  [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| Low-value asset, Section 19A(10A): cost per asset | SGD 5,000 | "A low-value asset is one that does not cost more than" this amount  [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| Low-value assets: total 1-year claim per YA | SGD 30,000 | "must not exceed" this per YA. Assets above the cap go to 3 years or working life  [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| 3-year write-off, Section 19A(1) | 1/3 of cost a year | Any qualifying asset  [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| Working life, Section 19: initial allowance in the first YA | 20% | Of cost  [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |
| Working life, Section 19: annual allowance each YA | 80% after the initial allowance | Divide by the working life. If the initial allowance is not claimed, use 100% divided by the working life. Elect 6 or 12 years if the Sixth Schedule life is 12 years or less, or 6, 12 or 16 years if it is 16 years. The election is irrevocable. [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |

- **Private cars.** The general capital-allowance bar covers private, RU-plated and company cars. Check the exception for registered vehicles hired out or used for driving instruction in the business. A foreign-registered car can qualify if used exclusively outside Singapore for business. Private hire and taxi drivers can separately claim eligible running costs under Section 5.3. Business vans, lorries and motorcycles can qualify under Section 19 or 19A, including the COE cost. [IRAS capital allowances](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances)
- **Hire purchase.** Allowances follow the principal (and deposit) actually paid in each period, not the full price.
- **Government grants.** Capital allowances are not given on expenditure funded by government capital grants approved on or after 1 Jan 2021.
- **Not plant.** Fixed partitions, flooring, false ceilings, lighting fittings and similar items are part of the premises; consider the Section 14N renovation deduction in Section 6.3 instead.

### 5.3 Allowable Business Expenses

IRAS's general rules: the expense must be incurred (the legal liability to pay has arisen), related to the business, not personal or private, and not capital. Records must be kept for at least five years ([IRAS business expenses and deductions](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions)).

- **Allowable (IRAS examples):** accountancy fees; hire purchase interest; interest on money borrowed for the business; legal fees to recover trade debts; advertising; business licence renewal; public transport in the course of business; rent, utility and telephone charges for the business; repairs and upkeep of business assets and premises; stationery and postage; bad trade debts; upkeep of motorcycles, pick-ups, vans, buses and lorries; car-related expenses of private hire car and taxi drivers earning driving income.
- **Disallowable (IRAS examples):** your own salary, drawings, CPF and MediSave contributions, income tax, insurance and donations (donations are claimed separately); purchase of fixed assets and depreciation (claim capital allowances); start-up licence, registration and signboard fees; club fees for the proprietor; travel to and from home; food, household and entertainment for yourself, family and friends; the proprietor's own life insurance and medical expenses; personal trips; the proprietor's own training costs; fines and penalties; interest on private loans; loan repayments; any expense on private cars or private hire cars (E, Q or S-plate), "even if the private cars were used for business purposes".
- **Related-party pay.** Pay to the proprietor's parents, spouse, children or siblings who do not work in the business is disallowable, as is pay above an arm's length rate.
- **FEDR.** Qualifying commission agents, private hire car and taxi drivers and delivery workers may claim a deemed expense equal to a prescribed share of gross income instead of actual expenses ([IRAS FEDR page](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/fixed-expense-deduction-ratio-for-self-employed-persons-and-platform-workers)). Check the conditions on that page before using it.


### 5.3A New broad-based FEDR, YA 2027 onwards

From YA 2027, eligible self-employed individuals may use a 20% deemed expense if they incurred deductible expenses and gross income per nature of business (NOB) for the basis period is at most S$50,000. Exclude partnership income and income covered by the industry-specific commission, PHC, taxi or delivery FEDRs. Aggregate businesses under the same NOB and use one method consistently across that NOB. Different NOBs can use different methods. The deemed amount replaces actual deductions. Qualifying e-filers receive FEDR automatically unless they elect to use actual deductions. [IRAS FEDR](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/fixed-expense-deduction-ratio-for-self-employed-persons-and-platform-workers) · [Finance (Income Taxes) Act 2026, section 13(2)](https://sso.agc.gov.sg/Acts-Supp/23-2026/Published/20261104?DocDate=20261104&ViewType=Pdf)

Keep the pre-existing industry routes: commission eligibility is based on the total relevant gross income and its own conditions, not the new per-NOB test; PHC/taxi actual driving losses are ring-fenced to future driving income. Do not use the broad-based rate to evade an industry exclusion.

### 5.4 Personal Reliefs

This current working method applies the ongoing relief rules to YA 2027, tested on 2026 facts, except the explicit earlier-year dependency in cash-top-up relief. Some authority pages still illustrate YA 2026/2025 facts. The full YA 2027 form/announcement must be checked before filing; it is not certified by changing the guide date. All reliefs together are capped: total reliefs allowed are limited to the cap below.

| Item | Value | Note |
| --- | --- | --- |
| Overall cap on the total of all reliefs, per YA | SGD 80,000 | "applies to the total amount of all tax reliefs claimed for each Year of Assessment"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs) |

**Earned Income Relief.** Granted on taxable earned income (less allowable expenses) in 2026, by age at 31 Dec 2026. If earned income is lower than the maximum, the relief is limited to the earned income.

| Age at 31 Dec 2026 | Maximum | Note |
| --- | --- | --- |
| Below 55 | SGD 1,000 | Disability version: SGD 4,000  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/earned-income-relief) |
| 55 to 59 | SGD 6,000 | Disability version: SGD 10,000  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/earned-income-relief) |
| 60 and above | SGD 8,000 | Disability version: SGD 12,000  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/earned-income-relief) |

**Spouse Relief.** For a spouse who lived with or was supported by the taxpayer in 2026 and whose 2026 annual income was not more than the limit below. Annual income here includes taxable income, tax-exempt income such as bank interest and dividends (but not CPF payouts) and foreign-sourced income whether or not remitted. The income condition does not apply to Spouse Relief (Disability) for a disabled spouse. A legally separated taxpayer may claim if paying maintenance under a Court Order or Deed of Separation; the relief is then the lower of the maintenance paid in 2026 and the amount in the table. Divorced taxpayers paying alimony cannot claim.

| Item | Value | Note |
| --- | --- | --- |
| Spouse's 2026 annual income must not exceed | SGD 8,000 | Raised with effect from YA 2025; the lower YA 2024 limit is stale  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/spouse-relief-spouse-relief-%28disability%29) |
| Spouse Relief | SGD 2,000 | Spouse Relief (Disability): SGD 5,500  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/spouse-relief-spouse-relief-%28disability%29) |

**Qualifying Child Relief (QCR).** All conditions in 2026: the child is unmarried; born to the taxpayer and spouse or ex-spouse, a step-child or legally adopted; below 16, or studying full-time at any university, college or other educational institution; the child's 2026 annual income was not more than SGD 8,000 (the same limit as the spouse table); and the taxpayer maintained the child. The age, study and income conditions do not apply to Child Relief (Disability) for a disabled child.

| Item | Value | Note |
| --- | --- | --- |
| QCR, per child | SGD 4,000 | Child Relief (Disability): SGD 7,500 per child  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/qualifying-child-relief-%28qcr%29-child-relief-%28disability%29) |
| QCR (or Child Relief (Disability)) plus WMCR on the same child | SGD 50,000 | Cap per child  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/qualifying-child-relief-%28qcr%29-child-relief-%28disability%29) |

**Working Mother's Child Relief (WMCR).** Only for a working mother who is married, divorced or widowed and has taxable earned income in 2026, for a child who is a Singapore Citizen at 31 Dec 2026 and meets every QCR condition. Single and male taxpayers cannot claim. Two regimes, by the date the child was born, adopted or became a citizen:

| Child order | Child born or adopted on or after 1 Jan 2024 (fixed amount) | Child born or adopted before 1 Jan 2024 (share of mother's earned income) |
| --- | --- | --- |
| 1st | SGD 8,000 | 15%  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/working-mother%27s-child-relief-%28wmcr%29) |
| 2nd | SGD 10,000 | 20%  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/working-mother%27s-child-relief-%28wmcr%29) |
| 3rd and beyond | SGD 12,000 | 25%  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/working-mother%27s-child-relief-%28wmcr%29) |
| Total WMCR over all children | capped at 100% of her earned income | "the total claim is capped at 100% of her earned income"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/working-mother%27s-child-relief-%28wmcr%29) |

A child born or adopted before 1 Jan 2024 who became a Singapore Citizen only after 1 Jan 2024 takes the fixed amount, not the percentage. The overall relief cap still applies.

IRAS allows relief for an otherwise qualifying child who died during the year. Check the separate counting rules for a deceased child or a stillborn child when determining child order. [IRAS Working Mother’s Child Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/working-mother%27s-child-relief-%28wmcr%29)

**Parent Relief.** All conditions in 2026: the taxpayer supported the dependant (parent, parent-in-law, grandparent, grandparent-in-law, step-parent, step-grandparent, adoptive parent or grandparent); the dependant was 55 or above; the dependant's 2026 annual income was not more than SGD 8,000 (the limit in the spouse table); neither the age nor the income condition applies to Parent Relief (Disability); and the dependant either lived with the taxpayer in Singapore, or lived in a separate household in Singapore and the taxpayer spent at least the support amount below.

| Item | Value | Note |
| --- | --- | --- |
| Staying with the dependant, per dependant | SGD 9,000 | Disability version: SGD 14,000  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29) |
| Not staying with the dependant, per dependant | SGD 5,500 | Disability version: SGD 10,000  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29) |
| Minimum support for a dependant in a separate household | SGD 2,000 | Spent "or more in supporting him/her" in 2026  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29) |

Living in Singapore means residing there with only temporary absences. IRAS generally applies this test to foreign dependants who stay at least 8 months. [IRAS Parent Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29)

**CPF relief for the self-employed.** The person must have made compulsory MediSave or voluntary CPF contributions in 2026. From YA 2026 the rule changed:

- Compulsory MediSave contributions made in 2026 get relief in full, with no cap, even if there is no assessable net trade income for that YA.
- Voluntary CPF contributions: no relief if compulsory MediSave is more than the share of net trade income below. Otherwise relief is the lowest of (a) that share of net trade income assessed, less the relief on compulsory contributions; (b) the CPF annual limit, less the applicable compulsory contributions (including employer and employee CPF for a concurrent employee); (c) the voluntary amount actually paid.
- A person who is also an employee: if compulsory employer and employee CPF plus compulsory MediSave already exhaust the CPF annual limit, no relief is given on voluntary contributions.
- Apply IRAS’s platform-worker exclusion when reducing the voluntary relief limits for compulsory contributions of a worker mandated or opted in to increased CPF contributions.
- MediSave contribution rates are set by the CPF Board by age and net trade income. See `sg-cpf-medisave`.

| Item | Value | Note |
| --- | --- | --- |
| Share of net trade income used in the voluntary-contribution cap | 37% | "37% of your net trade income assessed"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |
| CPF annual limit for self-employed persons | SGD 37,740 | "The CPF annual limit will also remain at" this figure  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |
| CPF annual salary ceiling | SGD 102,000 | Unchanged by the monthly ceiling increases  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |
| CPF monthly salary ceiling, 1 Jan 2025 to 31 Dec 2025 | SGD 7,400 | Historical 2025 wages, YA 2026  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |
| CPF monthly salary ceiling, on or after 1 Jan 2026 | SGD 8,000 | 2026 wages, YA 2027; do not backdate to YA 2026  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |

**CPF Cash Top-up Relief.** A Singapore Citizen or Permanent Resident can claim eligible 2026 cash top-ups to their own or qualifying family members’ Special, Retirement or MediSave Accounts. Apply the remaining Full Retirement Sum or Basic Healthcare Sum limit for that account before the relief caps below. Top-ups that attract Matched Retirement Savings Scheme (MRSS) grants get no relief from YA 2026 (top-ups received from 1 Jan 2025). Cash top-ups attracting Matched MediSave Scheme (MMSS) grants get no cash top-up relief from YA 2027 (cash top-ups made from 1 Jan 2026). A spouse or sibling without a disability must have had annual income of at most SGD 8,000 in 2025, the year before the top-up. This income test excludes qualifying parents, grandparents and a spouse or sibling with a disability. A self-employed person topping up a MediSave Account must be up to date with MediSave payable.

| Item | Value | Note |
| --- | --- | --- |
| Total relief per YA | SGD 16,000 | Self and family members together  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-cash-top-up-relief) |
| Own account, maximum (same maximum again for family members) | SGD 8,000 | Separate limits; one cannot use the other  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-cash-top-up-relief) |

**Supplementary Retirement Scheme (SRS) Relief.** Contributions must be made by 31 Dec 2026 or the SRS operator’s earlier cut-off for YA 2027 relief. Confirm YA residence, any status change/prorated limit, suspension and same-year withdrawal. Cash only; one account, and no refund merely because the overall relief cap is exhausted.

| Item | Value | Note |
| --- | --- | --- |
| Yearly maximum, Singapore Citizens and Permanent Residents | SGD 15,300 | Subject to the overall relief cap  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/supplementary-retirement-scheme-%28srs%29-relief) |
| Yearly maximum, foreigners | SGD 35,700 | Subject to the overall relief cap  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/supplementary-retirement-scheme-%28srs%29-relief) |

**Life Insurance Relief.** Only if the total of compulsory employee CPF and compulsory MediSave or voluntary CPF as a self-employed person in 2026 was LESS than the amount below. Premiums must be on the taxpayer's own or spouse's life; from YA 2026 this includes a wife's premiums on her husband's policy. The insurer needs an office or branch in Singapore for policies taken on or after 10 Aug 1973. IRAS: "You may claim the lower of: a. the difference between" the CPF limit below "and your CPF contribution; or b. up to" the share of insured value below "or the amount of insurance premiums paid." Accident, hospitalisation, health, disability, critical illness, endowment and riders do not qualify, nor investment-linked policies where investment is a fundamental consideration.

| Item | Value | Note |
| --- | --- | --- |
| 2026 CPF contributions must be less than | SGD 5,000 | "The total CPF contribution for the following was less than" this; at or above it, no relief  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/life-insurance-relief) |
| Premium limit, share of the insured value | 7% | "up to 7% of the insured value of your own/your spouse's life"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/life-insurance-relief) |

**Course Fees Relief: discontinued.** IRAS: "Course Fees Relief has been discontinued with effect from Year of Assessment (YA) 2026. The final year in which Course Fees Relief may be claimed is in YA 2025." Do not claim it for YA 2026 or later ([IRAS Course Fees Relief page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/course-fees-relief)).

**Donations.** Deduct qualifying cash donations made in 2026 to an approved Institution of a Public Character (IPC) or the Community Chest from statutory income before applying capped personal reliefs. Give the IPC the taxpayer’s NRIC, FIN or UEN so IRAS can use its records. Check that the charity is an approved IPC. The Finance (Income Taxes) Act 2026 extends the 250% deduction for qualifying donations through 31 December 2029. [IRAS donations](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations) · [Finance (Income Taxes) Act 2026, section 17(d)](https://sso.agc.gov.sg/Acts-Supp/23-2026/Published/20261104?DocDate=20261104&ViewType=Pdf)

| Item | Value | Note |
| --- | --- | --- |
| Deduction for qualifying donations | 250% | "the 250% tax deductions for qualifying donations"; IRAS also writes "up to 2.5 times the qualifying donation amount"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations) |

### 5.7 GST Touchpoints (detail in `sg-gst-return`)

| Item | Value | Note |
| --- | --- | --- |
| Compulsory GST registration: taxable turnover | more than SGD 1 million | Test taxable turnover at calendar year-end or on a reasonably supported forecast for the next 12 months. Check statutory exceptions and the effective date. [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |

| Item | Value | Note |
| --- | --- | --- |
| GST standard rate | 9% | Current standard rate from 1 January 2024; historical rate boundary read on the authority page  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates) |

For a GST-registered person, GST collected is not revenue and GST paid that is claimable as input tax is not an expense.


Additional relief coordination: Parent Relief is for no more than two dependants, with agreed sharing; conflicting spouse/sibling relief claims on the same dependant must be resolved. QCR may be shared only within its total per-child amount, and is allowed before WMCR. The child’s income definition includes relevant NS/internship/part-time income but not scholarships/bursaries of the described kind. Keep the actual disability evidence; do not replace a statutory condition with a label.

### Section 8. Statement reading


### Singapore Bank Statement Formats

| Bank | Format | Key Fields |
| --- | --- | --- |
| DBS / POSB | CSV / PDF | Date, Reference, Debit, Credit, Balance |
| OCBC | CSV | Transaction Date, Description, Withdrawals (SGD), Deposits (SGD), Balance (SGD) |
| UOB | CSV / PDF | Trans. Date, Description, Debit, Credit, Available Balance |
| Standard Chartered SG | CSV | Date, Description, Debit, Credit, Running Balance |
| Citibank SG | CSV | Date, Description, Debit Amount, Credit Amount |
| Wise SG | CSV | Date, Description, Amount, Currency, Running Balance |

### Key Singapore Banking Narrations

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| FAST / FAST CREDIT [name] | Funds transfer via FAST | Potential income from a client |
| PayNow Credit [name/UEN] | PayNow receipt | Potential business income; verify purpose |
| GIRO Credit / GIRO Debit | Standing instruction | Regular income or recurring expense |
| IBG / INTERBANK GIRO | Interbank GIRO | Income or expense transfer |
| TT FROM [bank/name] | Telegraphic transfer in | Overseas client income |
| PAYNOW QR | PayNow QR code payment | Business income |
| ATM WITHDRAWAL | Cash withdrawal | Personal: investigate |
| INTEREST CREDIT | Bank interest | Generally tax-exempt for individuals |
| IRAS GIRO | IRAS tax payment | Tax payment: exclude |
| CPFB | CPF Board payment | MediSave: CPF relief, not an expense |


### Section 9. Onboarding fallback


If the client provides a bank statement but cannot answer the onboarding questions yet:

1. Classify FAST, PayNow and GIRO credits from non-personal sources as potential business income.
2. Flag CPFB debits for reconciliation to contribution notices/statements; do not infer mandatory/voluntary/top-up or relief eligibility from the narration alone.
3. Apply the conservative defaults under Scope: GST split PENDING, no unproved private-car deductions, no unsupported home-office share.
4. Flag every purchase that looks like equipment as potential capital expenditure for Section 5.2.
5. Produce the working paper with PENDING flags. Do not compute tax until residence is confirmed.

Present these questions:

~~~
ONBOARDING QUESTIONS: SINGAPORE INCOME TAX (YA 2027)
1. Are you a Singapore citizen, PR or foreigner? If a foreigner, how many days were you in Singapore in 2026, and in 2025 and 2027?
2. Are you GST-registered?
3. Are you a sole proprietor, also an employee, or a partner? Which return did IRAS issue?
4. What is your business, and when does your accounting year end?
5. Are you a commission agent, private hire car or taxi driver, or delivery worker (FEDR)?
6. Do you work from home or from separate premises?
7. Do you use a vehicle for work? What plate: S, Q, E, or a van, lorry or motorcycle?
8. CPF: what compulsory MediSave and voluntary CPF did you pay in 2026?
9. SRS: did you contribute by 31 Dec 2026?
10. Children (ages, citizenship, birth dates) and parents (ages, 2026 income, living with you)?
11. Donations to approved IPCs in 2026?
~~~


## Boundary and exception table


### 6.1 Home Office Deduction

No saved IRAS page sets a home office method. IRAS allows "Rent, utility, and telephone charges for the business" and disallows household expenses. A business share of home utilities, internet or rent may be arguable where part of the home is used for the business. **Flag for reviewer:** the apportionment basis (floor area or time), the evidence, and whether the person rents or owns.

### 6.2 Motor Vehicles and Ride-hailing

IRAS generally disallows the costs of operating or hiring a private car, including when used on business. Private hire car and taxi drivers can claim eligible running costs incurred to earn driving income if they use actual expenses. Check their FEDR option separately. Vans, lorries, pick-ups and motorcycles can qualify for business upkeep and capital allowances. A taxi fare for a business journey can qualify as public transport. Check the trip purpose and keep the receipt. Refer uncertain ride-hailing arrangements and foreign vehicle cases. [IRAS self-employed business expenses](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions) · [IRAS guide for self-employed tuition operators, section 3.4](https://www.iras.gov.sg/media/docs/default-source/e-tax/starter-guide-for-self-employed-tuition-centre-or-agency-operators.pdf) · [IRAS distinction between transport services and car hire](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses/tax-treatment-of-business-expenses-%28m-r%29)

### 6.3 Capital vs Revenue Expenditure; Renovation (Section 14N)

For capital expenditure, check capital allowances and any specific statutory deduction. Qualifying renovation or refurbishment that does not affect the structure of the premises may be deducted under Section 14N. For a sole proprietor the cap applies across all their sole proprietorships. The first fixed three-YA period is YA 2025 to YA 2027. Claim in equal instalments over 3 years or elect irrevocably to claim qualifying expenditure in one year. Start in the YA for the basis period in which the expenditure is incurred. Include the deduction when calculating adjusted profit and in allowable deductions if filing a 4-line statement. Claim each cost once. Keep an itemised list, confirmation that no Building Control approval is needed and invoices for 5 years.

| Item | Value | Note |
| --- | --- | --- |
| Section 14N renovation deduction cap | SGD 300,000 | Per fixed three-YA period, first YA 2025 to YA 2027. Check the cessation rule before claiming any remaining instalment. [Official source](https://www.iras.gov.sg/media/docs/default-source/e-tax/etaxguide_it_deduction_r_r_costs.pdf) |

### 6.4 CPF MediSave Contributions

The amount of compulsory MediSave depends on age and net trade income and is set by the CPF Board (2026 CPFB Tables 1 and 2 have now been read; see `sg-cpf-medisave`). The from-YA-2026 rule gives full compulsory relief; amounts paid in 2026 are considered in YA 2027 (Section 5.4). **Flag for reviewer:** confirm the amount actually paid in 2026 from the CPF statement, and split compulsory from voluntary.

### 6.5 Working Mother's Child Relief (WMCR)

WMCR has two regimes (Section 5.4): a fixed amount for a Singapore Citizen child born or adopted on or after 1 Jan 2024 (or who became a citizen after that date), and a share of the mother's earned income for an earlier child. The mother must be married, divorced or widowed; the child, not the mother, must be a Singapore Citizen. QCR plus WMCR on one child is capped per child, and all reliefs sit inside the overall cap. **Flag for reviewer:** child order (by birth, marriage or adoption date), each child's citizenship date, and how QCR is shared between parents.

### 6.6 Entertainment

Client entertainment can qualify if wholly and exclusively incurred to earn business income. Keep invoices or receipts and record the business purpose and attendees. Exclude private entertainment and refer unresolved mixed expenses. [IRAS guide for self-employed tuition operators, section 3.4](https://www.iras.gov.sg/media/docs/default-source/e-tax/starter-guide-for-self-employed-tuition-centre-or-agency-operators.pdf) · [IRAS self-employed business expenses](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions)


## Worked cases


All amounts in these examples are hypothetical bank lines, shown as plain numbers in SGD.

### Example 1. PayNow Business Receipt

**Input line (DBS Bank statement):**
~~~
15 Mar 2026 | PayNow Credit ALPHA DESIGN PTE LTD | +8,500.00 | Balance 24,310.50
~~~

**Reasoning:** confirm the design invoice and when the revenue was earned. If the agreed SGD 8,500 is GST-inclusive for a standard-rated supply after GST registration, output GST is SGD 701.83 (8,500 × 9/109, rounded to cents) and revenue is SGD 7,798.17. If the business is unregistered or the supply is zero-rated, the example has no output GST and revenue is SGD 8,500. Use the tax invoice to identify the actual treatment. [IRAS GST-inclusive pricing](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/invoicing-price-display-and-record-keeping/displaying-and-quoting-prices)

**Classification:** business revenue, excluding any output GST.

### Example 2. Stripe Payout (Net of Stripe Fees)

**Input line (OCBC Bank statement):**
~~~
22 Apr 2026 | STRIPE PAYOUT SG | +4,850.00 | Available Balance 31,200.00
~~~

**Reasoning:** Stripe pays out net of its fees. Hypothetically, if Stripe collected 5,000.00 from clients and kept 150.00 in fees, revenue is 5,000.00 and the fee of 150.00 is an allowable expense. Match the payout to the Stripe dashboard for the exact gross and fee.

**Classification:** gross revenue per Stripe report; Stripe fees allowable.

### Example 3. CPF MediSave Payment

**Input line (UOB Bank statement):**
~~~
01 May 2026 | CPFB MEDISAVE CONTRIBUTION | -3,600.00 | Balance 15,400.00
~~~

**Reasoning:** a self-employed person's compulsory MediSave contribution is not a business expense; IRAS lists "Your own ... MediSave/CPF contributions" as disallowable. It is claimed as CPF relief. From YA 2026, compulsory MediSave paid in 2026 gets relief in full, without the old cap, even if the person has no net trade income for YA 2027 ([IRAS CPF relief for self-employed](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed)). Voluntary contributions remain capped (Section 5.4). The relief counts toward the overall relief cap.

**Classification:** exclude from business expenses. If the CPF record confirms SGD 3,600 of compulsory MediSave paid in 2026, record SGD 3,600 of CPF relief before the overall relief cap.

### Example 4. WeWork Office Subscription

**Input line (DBS Bank statement):**
~~~
01 Jun 2026 | WEWORK SINGAPORE PTE LTD | -1,200.00 | Balance 28,750.00
~~~

**Reasoning:** a monthly co-working fee for the business is rent for the business, which IRAS lists as allowable. No apportionment is needed where the space is used only for the business.

**Classification:** rent, allowable.

### Example 5. Laptop Purchase

**Input line (OCBC Bank statement):**
~~~
15 Jul 2026 | APPLE SINGAPORE PTE LTD | -2,899.00 | Balance 19,200.00
~~~

**Reasoning:** assume the laptop is bought and used wholly in the business during the basis period and SGD 2,899 is the qualifying cost after excluding any recoverable GST and government-funded cost. Elect the 100% computer write-off under Section 19A(2) for YA 2027. A business camera or desk at this price may qualify for the low-value write-off under Section 19A(10A), subject to the annual cap and the taxpayer’s choice of method.

**Classification:** capital allowance for the full cost in YA 2027, Section 19A(2).

### Example 6. Private Car Expense

**Input line (UOB Bank statement):**
~~~
10 Aug 2026 | SHELL SELECT QUEENSTOWN | -120.00 | Balance 22,100.00
~~~

**Reasoning:** SGD 120 of fuel for an ordinary Singapore-registered private car gives a deduction of SGD 0. A private hire car or taxi driver using the actual-expense method can deduct eligible fuel incurred to earn driving income. Business use of a van, lorry or motorcycle can qualify for an upkeep deduction.

**Classification:** private car: NOT deductible. Ask whether the person is a private hire car or taxi driver, or whether the vehicle is a van, lorry or motorcycle.


### Section 7. Excel working paper


~~~
SINGAPORE INCOME TAX WORKING PAPER
Taxpayer: _______________  NRIC/FIN: ___________
Year of Assessment: YA 2027 (income earned 1 Jan 2026 to 31 Dec 2026)
Accounting period: ____________ to ____________
GST registered: Yes / No [circle one]

A. GROSS REVENUE AND COST OF SALES
  A1. Total receipts from clients (grossed up for platform fees)   ___________
  A2. Less: output GST on relevant invoices                         ___________
  A3. Net revenue                                                   ___________
  A4. Less: cost of goods sold                                      ___________
  A5. Gross profit (A3 - A4)                                        ___________

B. ALLOWABLE BUSINESS EXPENSES (or FEDR deemed expense, if eligible)
  B1. Rent / co-working space                 ___________
  B2. Utilities (business share)              ___________
  B3. Telephone and internet (business share) ___________
  B4. Travel in the course of business        ___________
  B5. Advertising                             ___________
  B6. Accountancy and legal fees              ___________
  B7. Software subscriptions                  ___________
  B8. Stationery and postage                  ___________
  B9. Section 14N renovation (within cap)     ___________
  B10. Bank and transaction fees              ___________
  B11. Other allowable expenses               ___________
  B12. Total business expenses                ___________

C. CAPITAL ALLOWANCES
  C1. Section 19A(2) computers / automation   ___________
  C2. Section 19A(10A) low-value assets       ___________
  C3. Section 19A(1) three-year write-off     ___________
  C4. Section 19 working life (IA + AA)       ___________
  C5. Total capital allowances                ___________

D. TAX-ADJUSTED PROFIT (A5 - B12 - C5)            ___________

E. OTHER INCOME (employment, rental)          ___________

F. STATUTORY INCOME (D + E)                   ___________

G. QUALIFYING DONATIONS MADE IN 2026 (deduction per donations table)  ___________

H. ASSESSABLE INCOME (F - G)                  ___________

I. PERSONAL RELIEFS (2026 facts)
  I1. Earned Income Relief                    ___________
  I2. CPF relief: compulsory MediSave (full)  ___________
  I3. CPF relief: voluntary (capped)          ___________
  I4. SRS relief                              ___________
  I5. Spouse relief                           ___________
  I6. QCR / WMCR                              ___________
  I7. Parent relief                           ___________
  I8. CPF cash top-up relief                  ___________
  I9. Life insurance relief                   ___________
  I10. Course fees relief                     NOT AVAILABLE FROM YA 2026
  I11. Total reliefs (cap: SGD 80,000)        ___________

J. CHARGEABLE INCOME (H - I11)                ___________

K. GROSS TAX (resident rate table)            ___________

L. LESS: PARENTHOOD TAX REBATE (if any)       ___________
   (no Personal Income Tax Rebate printed for YA 2027)

M. ESTIMATED TAX PAYABLE (K - L)              ___________

REVIEWER FLAGS:
  [ ] Tax residence for YA 2027 confirmed?
  [ ] Accounting year end confirmed?
  [ ] GST status confirmed?
  [ ] Capital vs revenue reviewed?
  [ ] Private car: no capital allowances and no running costs?
  [ ] Relief conditions tested on 2026 facts?
  [ ] Relief cap SGD 80,000 checked?
  [ ] Donations deducted before reliefs, outside the cap?
  [ ] Course Fees Relief NOT claimed?
~~~


```oa-check
name: Revenue reconciliation then resident income tax
inputs:
  gross_client_receipts: 100000
  ordinary_allowable_expenses: 20000
  computer_cost_qualifying_s19a2: 2899
  compulsory_medisave_paid: 4000
  earned_income_relief: 1000
steps:
  - adjusted_profit: gross_client_receipts - ordinary_allowable_expenses - computer_cost_qualifying_s19a2
  - qualifying_reliefs: compulsory_medisave_paid + earned_income_relief
  - chargeable_income: max(0, adjusted_profit - min(qualifying_reliefs, 80000))
  - gross_tax: 550 + max(0, chargeable_income - 40000) * 0.07
expected:
  adjusted_profit: 77101
  qualifying_reliefs: 5000
  chargeable_income: 72101
  gross_tax: 2797.07
```

This hypothetical resident is below 55, has only the stated trade income and eligible payments, no GST, no donations/rebates or other reliefs. It is a method check, not an assessed tax bill; retain the actual return's rounding outcome.

```oa-check
name: YA2027 broad based FEDR same nature business aggregation
inputs:
  firm_a_revenue: 19000
  firm_b_revenue: 30000
steps:
  - same_nob_total: firm_a_revenue + firm_b_revenue
  - deemed_expense_a: firm_a_revenue * 0.20
  - deemed_expense_b: firm_b_revenue * 0.20
  - adjusted_profit_a: firm_a_revenue - deemed_expense_a
  - adjusted_profit_b: firm_b_revenue - deemed_expense_b
expected:
  same_nob_total: 49000
  deemed_expense_a: 3800
  deemed_expense_b: 6000
  adjusted_profit_a: 15200
  adjusted_profit_b: 24000
```

These are two qualifying businesses in the same NOB, each with allowable expenses, combined below the 50,000 ceiling, neither subject to an industry-specific FEDR. Use the same choice for both and do not also deduct their actual expenses. [IRAS worked example1](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/fixed-expense-deduction-ratio-for-self-employed-persons-and-platform-workers).

## When to refuse or refer


- Non-resident for YA 2027, or residence unclear: refuse the computation; refer to `sg-tax-residency` and an accountant.
- A company, LLP or partnership: refuse; this skill is for individuals.
- Disposals of property, shares or crypto where the gain may be trading income: refer.
- Prior years with unfiled returns, an estimated assessment, a composition offer or a summons: refer to an accountant now.
- Any suspected wilful omission of income: refer; do not prepare a return around it.
- Someone claiming NOR concessions or Course Fees Relief for YA 2027: explain both have ended and refer if they insist.
- Always present the tax as an estimate until IRAS issues the Notice of Assessment.


### Prohibitions


- NEVER apply resident rates without confirming tax residence for YA 2027.
- NEVER treat YA 2027 as income earned in 2027. YA 2027 is 2026 income.
- NEVER include GST collected as revenue for a GST-registered person.
- Check the private-car restrictions and the exceptions for hired-out, instructional and exclusively overseas business vehicles in Sections 5.2 and 6.2.
- NEVER give the 1-year write-off to an asset that is not a computer, prescribed automation equipment or a low-value asset.
- NEVER allow income tax, drawings, own CPF or own insurance as business expenses.
- NEVER allow personal or domestic expenses as business deductions.
- NEVER let total personal reliefs exceed the cap (donations are not inside it).
- NEVER claim Course Fees Relief for YA 2027, or apply NOR concessions.
- NEVER apply a YA 2027 Personal Income Tax Rebate without a new official publication for that YA; none is established by the scoped sources here.
- NEVER describe non-resident employment income as taxed at a flat rate alone: it is the flat rate or resident rates, whichever gives more tax.
- NEVER present tax calculations as final. Label them estimates and direct the client to an Accredited Tax Adviser for confirmation.


## Filing and payment
### 5.5 Filing and Payment

The IRAS calendar gives 18 April 2027 for individual income tax returns. IRAS publishes a general 1 March to 18 April filing window. Check the actual YA 2027 portal opening and any specific notification. Anyone instructed to file by letter, form or SMS must file regardless of their income. Check the IRAS filing checker and any No-Filing Service or Direct Notice of Assessment notification. [IRAS calendar](https://www.iras.gov.sg/due-dates?dueYear=2027) · [IRAS filing responsibilities](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/filing-responsibilities-of-self-employed-persons-%28including-individual-partners%29) · [IRAS late filing](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m)

| Item | Value | Note |
| --- | --- | --- |
| Preceding-year total income exceeds | SGD 22,000 | General filing trigger, subject to IRAS notification. [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/filing-responsibilities-of-self-employed-persons-%28including-individual-partners%29) |
| Preceding-year self-employment net profit exceeds | SGD 6,000 | Alternative trigger. A non-resident who derives Singapore income is also covered by the filing guidance. [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/filing-responsibilities-of-self-employed-persons-%28including-individual-partners%29) |

Form B/B1 carries a 2-line or 4-line statement taken from the accounts. Prepare a profit and loss account and a balance sheet at the end of every accounting period.

| Item | Value | Note |
| --- | --- | --- |
| 2-line statement (revenue, adjusted profit or loss) when revenue is this or less | SGD 200,000 | "when your revenue is $200,000 or less from YA 2021"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons) |
| 4-line statement (revenue, gross profit, allowable business expenses, adjusted profit) | more than SGD 200,000 | Applies from YA 2021  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons) |

Tax is payable within 1 month from the date of the Notice of Assessment, even if the person objects ([IRAS late payment page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax)). A person on an approved instalment plan is not charged the late payment penalty. A person who cannot pay in full may apply for up to 12 interest-free monthly instalments via GIRO; the GIRO application must be approved before the payment due date to avoid the late payment penalty.

### 5.6 Penalties

**Late filing or non-filing** ([IRAS late filing page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m)). Failing to file by the due date is an offence. IRAS may issue an estimated Notice of Assessment (payable within 1 month, and it may assume higher income), offer to compound the offence, or issue a summons.

| Item | Value | Note |
| --- | --- | --- |
| Composition amount, per offence | up to SGD 5,000 | "depending on your past compliance records"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m) |
| Fine on conviction in court, per offence | up to SGD 5,000 | Return must still be filed  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m) |
| Failing to file for 2 or more years, on conviction | penalty of twice the tax assessed, plus a fine of up to SGD 5,000 | Imprisonment up to 6 months if unpaid  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m) |

**Late payment** ([IRAS late payment page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax)).

| Item | Value | Note |
| --- | --- | --- |
| Late payment penalty on unpaid tax after the due date | 5% | Not imposed if on an approved instalment plan  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax) |
| Additional penalty per completed month unpaid, starting 60 days after the 5% penalty | 1% | 60 days, not 30  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax) |
| Maximum additional penalty | 12% | "up to a maximum of 12% of the unpaid tax"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax) |

IRAS may also appoint agents (bank, employer, tenant) to collect, and may issue a Travel Restriction Order.

**Incorrect returns and tax evasion.** The table shows the statutory penalty on conviction using the tax undercharged. The evasion provisions also contain rules for repeat offences. [Income Tax Act 1947, sections 95 to 96A](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr95-%2Cpr96-%2Cpr96A-)

| Item | Value | Note |
| --- | --- | --- |
| Incorrect return under Section 95(1) | 100% | Subject to Part 18 of the Act |
| Incorrect return without reasonable excuse or through negligence, Section 95(2) | 200% | Also liable to a fine up to SGD 5,000, imprisonment up to 3 years or both |
| Wilful tax evasion, Section 96 | 300% | Also liable to a fine up to SGD 10,000, imprisonment up to 3 years or both |
| Serious fraudulent tax evasion, Section 96A | 400% | Applies to specified fraudulent conduct. Also liable to a fine up to SGD 50,000, imprisonment up to 5 years or both |

A voluntary disclosure within one year of the statutory filing date can get the penalty waived if IRAS's qualifying conditions are met.


For the current published workflow, log in at myTax Portal with Singpass/SFA, choose Individuals → File Income Tax Return, and report under 2. Trade, Business, Profession or Vocation → Sole-Proprietorship/Self Employment Income. Revenue at most 200,000 uses Revenue/Adjusted Profit or Loss; higher revenue uses Revenue/Gross Profit or Loss/Allowable Deductions/Adjusted Profit or Loss. Cost of goods sold is deducted before gross profit; service-only gross profit equals revenue. At annual revenue 500,000 or more, upload signed certified accounts under Consolidated Statement. Review other income and reliefs, submit through the authorised workflow and retain the acknowledgement. Reconcile the actual YA form’s capital-allowance presentation to the tax workpaper without double deduction. [IRAS filing](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/filing-responsibilities-of-self-employed-persons-%28including-individual-partners%29); [IRAS business computation](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/calculating-my-business-income/calculating-business-income). Payment follows the actual notice/approved plan, with receipt retained.

## Completion checklist


### Key Legislation

| Topic | Provision |
| --- | --- |
| Resident rates | [Income Tax Act 1947, Second Schedule, Table 3](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=Sc2-) (YA 2024 and later) |
| Capital allowances, working life | Income Tax Act 1947, Section 19 and Sixth Schedule |
| Capital allowances, 3-year write-off | Section 19A(1) |
| Computers and prescribed automation equipment | Section 19A(2) |
| Low-value assets | Section 19A(10A) |
| Renovation or refurbishment | Section 14N |
| GST rate | Goods and Services Tax Act 1993, section 16 |

### Not Ordinarily Resident (NOR) scheme

IRAS: "The NOR scheme has ceased. The last NOR status granted will run / be valid from YA 2020 to YA 2024." No NOR concession applies to YA 2027 ([IRAS NOR page](https://www.iras.gov.sg/schemes/individual-income-tax/not-ordinarily-resident-%28nor%29-scheme)).

### Known Gaps / Out of Scope

- Non-resident income tax (see `sg-tax-residency`)
- GST computation and returns (see `sg-gst-return`)
- Corporate income tax (Pte Ltd and other companies)
- Partnership income allocation
- Property gains and capital gains (see `sg-zero-cgt`)
- MediSave contribution rates (see `sg-cpf-medisave`)
- Planning and entity choice (see `singapore-tax-optimization`)
- Crypto and digital tokens (see `singapore-crypto-tax`)

### Self-Check

- [ ] YA 2027 = income earned in 2026, and every relief tested on 2026 facts?
- [ ] Tax residence confirmed before applying resident rates?
- [ ] GST excluded from revenue for a GST-registered person?
- [ ] Private car: no capital allowances, no running costs (running costs only for a private hire car or taxi driver)?
- [ ] 1-year write-off used only for computers, automation equipment and low-value assets?
- [ ] Compulsory MediSave relief given in full; voluntary CPF relief capped?
- [ ] Relief cap applied; donations deducted before reliefs?
- [ ] Course Fees Relief not claimed; no YA 2027 Personal Income Tax Rebate applied?
- [ ] 18 April 2027 deadline, any specific notice and portal details checked?


## Sources

| Source and scope read | Official URL | Read on |
|---|---|---|
| Read for current from-YA2024 resident bands and non-resident employment/director/professional distinction. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates | 2026-11-14 |
| Read for preceding-year basis and resident/three-year/two-year employee-only tests, non-resident relief boundary. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency | 2026-11-14 |
| Read for historical YA2024/2025 personal rebates and no carry-forward. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/personal-income-tax-rebate | 2026-11-14 |
| Read for accounting period, accounts, two/four-line statement, annual filing/no-filing notifications. | https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons | 2026-11-14 |
| Read for incurred-expense definition, allowable/disallowable lists, cars/COE, related-party pay, section14N and records. | https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions | 2026-11-14 |
| Read for industry eligibility, all-SEI 20% fromYA2027, 50,000 per-NOB aggregation/consistent choice and automatic claim/opt-out. | https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/fixed-expense-deduction-ratio-for-self-employed-persons-and-platform-workers | 2026-11-14 |
| Read for qualifying assets/cars, one-year/specific and low-value limits, working-life formulas, historic two-year option, deferral and hire-purchase examples; no new statutory read. | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances | 2026-11-14 |
| Read for overall 80,000 relief cap and coordinated relief sharing. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs | 2026-11-14 |
| Read for age/earned-income limits, disability maxima and evidence. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/earned-income-relief | 2026-11-14 |
| Read for spouse annual-income definition, separation/divorce, disability and competing-claim limits. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/spouse-relief-spouse-relief-%28disability%29 | 2026-11-14 |
| Read for child qualifying conditions, income definition, amounts and shared total/QCR-before-WMCR. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/qualifying-child-relief-%28qcr%29-child-relief-%28disability%29 | 2026-11-14 |
| Read for citizenship/order, fixed/percentage WMCR, combined cap and ongoing rules. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/working-mother%27s-child-relief-%28wmcr%29 | 2026-11-14 |
| Read for parent age/income/residence/support, disability amounts, two dependants and sharing. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29 | 2026-11-14 |
| Read for full compulsory relief fromYA2026, voluntary/concurrent CPF limits and paid-year examples1-5. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed | 2026-11-14 |
| Read for cash-only top-up, self/family and account limits, dependant prior-year income, MRSS and new MMSS exclusion fromYA2027. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-cash-top-up-relief | 2026-11-14 |
| Read for cash SRS caps/operator deadline, residence, status prorating and no-refund condition. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/supplementary-retirement-scheme-%28srs%29-relief | 2026-11-14 |
| Read for life-policy/CPF conditions, spouse expansion, excluded policies and lower-of limits. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/life-insurance-relief | 2026-11-14 |
| Read for course-fees relief discontinuance fromYA2026; historical claims not current. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/course-fees-relief | 2026-11-14 |
| Read for IPC conditions, statutory-income-before-relief ordering, explicit 2026 donation/YA2027 example and no automatic ordinary-charity deduction. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations | 2026-11-14 |
| Read for historical YA2026 window and NFS/D-NOA notification workflow only. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/tax-season-2026---all-you-need-to-know | 2026-11-14 |
| Read for historical YA2026 paper forms and 18April date, acknowledgement. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/filing-a-paper-income-tax-return | 2026-11-14 |
| Read for notification duty, estimated assessment, composition/court penalties and outstanding returns. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m | 2026-11-14 |
| Read for payment within one month, five-percent penalty, 60-day additional-penalty clock, GIRO, agents and travel. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax | 2026-11-14 |
| Read for negligent/wilful error maxima and conditional voluntary-disclosure treatment. | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/consequences-of-non-compliance/errors-in-tax-returns | 2026-11-14 |
| Read for NOR cessation and finalYA2020-2024 period. | https://www.iras.gov.sg/schemes/individual-income-tax/not-ordinarily-resident-%28nor%29-scheme | 2026-11-14 |
| Read for current nine-percent GST standard rate. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates | 2026-11-14 |
| Read for taxable-turnover retrospective/prospective GST boundary. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst | 2026-11-14 |
| Read for transportation-service versus hired/private-car rule only. | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses/tax-treatment-of-business-expenses-%28m-r%29 | 2026-11-14 |
| Read for Form B/B1 published portal path, two/four-line fields, prior-year filing triggers, five-year retention and certified-account attachment threshold. | https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/filing-responsibilities-of-self-employed-persons-%28including-individual-partners%29 | 2026-11-14 |
| Read for revenue, cost of goods, gross profit, allowable-expense sequence and sole-proprietor reporting fields; partnership allocation remains out of scope. | https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/calculating-my-business-income/calculating-business-income | 2026-11-14 |
| Read for paragraphs2.3-2.6,4-6: Section14N one-year option, fixed three-YA cap, sole-proprietor aggregation and no double deduction. | https://www.iras.gov.sg/media/docs/default-source/e-tax/etaxguide_it_deduction_r_r_costs.pdf | 2026-11-14 |
| Calendar entry for the YA 2027 individual filing deadline. | https://www.iras.gov.sg/due-dates?dueYear=2027 | 2026-11-22 |
| Enacted YA 2027 FEDR and extension of the qualifying donation deduction. | https://sso.agc.gov.sg/Acts-Supp/23-2026/Published/20261104?DocDate=20261104&ViewType=Pdf | 2026-11-22 |
| Distinct penalties on conviction for incorrect returns, evasion and serious fraudulent evasion. | https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr95-%2Cpr96-%2Cpr96A- | 2026-11-22 |
| GST-inclusive price and tax fraction. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/invoicing-price-display-and-record-keeping/displaying-and-quoting-prices | 2026-11-22 |
| Self-employed guidance on taxi fares, client entertainment and the records to retain. | https://www.iras.gov.sg/media/docs/default-source/e-tax/starter-guide-for-self-employed-tuition-centre-or-agency-operators.pdf | 2026-11-22 |

Check the final YA 2027 portal opening, field and attachment details, and rounding before filing. Some relief pages illustrate YA 2026 facts, so apply their continuing rules to the relevant 2026 inputs. Refer unproved home-office apportionment, mixed client entertainment and uncertain ride-hailing arrangements.

Not yet confirmed: the allowable home-office allocation without evidence of business use and the exact YA 2027 individual portal opening date. The IRAS calendar gives the closing date.
