---
name: sg-income-tax
description: Use this skill whenever asked about Singapore income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay in Singapore", "Form B", "Form B1", "IRAS income tax", "trade income", "capital allowances Singapore", "personal reliefs", "tax residence 183 days", "Section 10(1)(a)", "CPF self-employed", "self-employed tax Singapore", "myTax Portal", "DBS Bank statement", "OCBC income", "PayNow transfer", "Stripe Singapore", or any question about filing or computing income tax for a Singapore sole proprietor or freelancer. This skill covers progressive rates (0--24%), trade income computation, capital allowances (Section 19/19A), approved deductions, personal reliefs, CPF MediSave, tax residence rules, filing deadlines, and penalties. ALWAYS read this skill before touching any Singapore income tax work.
version: 3.0
jurisdiction: SG
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
tax_year_notes: "2026 income, ordinarily YA 2027; historical YA 2026 filing expressly separated"
---

# Singapore self-employed income tax, 2026 income / YA 2027 v3.0

2026 income, ordinarily YA 2027, for resident sole proprietors/freelancers. Confirm the actual accounting basis period. The ongoing rate table applies from YA 2024; this version adds the expressly announced YA 2027 FEDR and MMSS changes. Historical YA 2026 filing covered 2025 income and ran 1 March to 18 April 2026; those dates are not a newly verified YA 2027 announcement. Source read scopes and remaining gaps are below. It is a working method, not a filed return.

## Scope and who this is for


| Field | Value |
| --- | --- |
| Country | Singapore |
| Tax | Individual income tax, progressive resident rates (table below) |
| Currency | SGD only |
| Tax year basis | Preceding year basis: YA 2027 taxes income earned 1 Jan 2026 to 31 Dec 2026 |
| Primary legislation | Income Tax Act 1947 |
| Tax authority | Inland Revenue Authority of Singapore (IRAS) |
| Filing portal | myTax Portal, with Singpass |
| Return | Form B (self-employed) |
| Filing deadline | Historical YA 2026: 18 Apr 2026 for both; confirm the actual YA 2027 notice/window |

### Tax residence for YA 2027

A person is a tax resident for YA 2027 if, per the [IRAS tax residency page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency), any ONE of these holds:

- a Singapore Citizen or Singapore Permanent Resident who normally resides in Singapore except for temporary absences; OR
- a foreigner who stayed or worked in Singapore for at least 183 days in calendar year 2026; OR
- a foreigner who stayed or worked in Singapore continuously for 3 consecutive years (an administrative concession that applies even if the first and third years are under 183 days); OR
- a foreign employee whose employment straddles 2 calendar years with a continuous stay of at least 183 days. This last test is for employees only and excludes directors, public entertainers and professionals, so it does not help a self-employed person.

A stay under 183 days with none of the other tests met means non-resident.

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
- Are you GST-registered, and from what date? This changes revenue on every receipt.
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
| Non-resident: employment income | 15% | "or the progressive resident tax rates (see table above), whichever is the higher tax amount"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |
| Non-resident: director's fees, consultation fees, rental and all other income | 24% | Except employment income and income taxed at reduced withholding rates  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |

The legacy statutory reference is the Second Schedule to the Income Tax Act 1947, which keeps old tables for YA 2012 to 2016 and YA 2017 to 2023 next to the current one; the IRAS rate page independently confirms the ongoing rates. The statute could not be reopened in this pass. Legacy Table 3 is titled "YEAR OF ASSESSMENT 2024 AND SUBSEQUENT YEARS".

| Item | Rate | Note |
| --- | --- | --- |
| Table 3, every dollar of chargeable income above SGD 1,000,000 | 24% | Table 3 only; the YA 2017 to 2023 table stops at a lower top rate  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates) |

No Personal Income Tax Rebate is printed for YA 2027. The IRAS rebate page covers "Years of Assessment (YAs) 2024 and 2025" only and says the rebate "cannot be carried forward". Do not deduct a rebate in a YA 2027 computation unless IRAS publishes one.


## The method, step by step


1. Confirm the year and the person. YA 2027 taxes 2026 income ([IRAS tax residency page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency)). Confirm the person is self-employed: a sole proprietor or partner registered with ACRA is generally self-employed and reports business income, not salary ([IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)).
2. Confirm tax residence for YA 2027 using the tests under Scope. A non-resident is out of scope (refusal R-SG-1). See the [IRAS tax residency page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency).
3. Confirm the accounting period. Most businesses end on 31 Dec, so the 2026 accounts feed YA 2027; a different year end feeds the YA after the year in which it ends ([IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)).
4. Build revenue from the bank statement and invoices (Sections 3 and 8). Strip GST out of receipts if the person is GST-registered; see the [IRAS current GST rate](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates) and the `sg-gst-return` skill.
5. Deduct allowable business expenses and remove disallowable ones, using the IRAS lists summarised in Section 5.3 ([IRAS business expenses and deductions](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions)). Qualifying commission agents, private hire car and taxi drivers and delivery workers may instead claim a deemed expense under the Fixed Expense Deduction Ratio ([IRAS FEDR page](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/fixed-expense-deduction-ratio-for-self-employed-persons-and-platform-workers)).
6. Claim capital allowances on qualifying plant and machinery under Section 19 or 19A of the Income Tax Act 1947 (Section 5.2; [IRAS capital allowances page](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances)). Never on an S-plated private car.
7. Report revenue and adjusted profit on Form B as a 2-line or 4-line statement, depending on revenue (Section 5.5; [IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)).
8. Deduct qualifying donations made in 2026 from statutory income to reach assessable income ([IRAS donations page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations)).
9. Deduct personal reliefs, each tested on 2026 facts, within the overall relief cap (Section 5.4; [IRAS tax reliefs page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs)). The result is chargeable income.
10. Apply the resident Rates, bands and thresholds table ([IRAS individual income tax rates](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates)). IRAS prints a Personal Income Tax Rebate for YA 2024 and YA 2025 only, so apply none for YA 2027 unless IRAS publishes one ([IRAS Personal Income Tax Rebate page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/personal-income-tax-rebate)).
11. File within the actual YA 2027 window on myTax Portal, then pay within 1 month of the Notice of Assessment (Sections 5.5 and 5.6; [IRAS historical Tax Season 2026 page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/tax-season-2026---all-you-need-to-know)).


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
| GRAB [ride] / GOJEK / COMFORT TAXI | Travel | Allowable only for a business trip; flag for review | A ride is a transportation service. IRAS lets companies deduct business rides but not hiring or running a private car; the self-employed page does not address fares (Section 6.2) |
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
| SHELL / ESSO / SPC / CALTEX [fuel] | Motor | NOT deductible for a private car | Allowable only for a qualifying vehicle (van, lorry, motorcycle) or under FEDR for drivers |
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
| Working life, Section 19: annual allowance each YA | 80% | Of cost, divided by the working life. By irrevocable election: 6 or 12 years if the Sixth Schedule life is 12 years or less; 6, 12 or 16 years if it is 16 years  [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances) |

- **Private cars.** No capital allowance is given on private cars (S-plated), RU-plated cars or company cars (Q-plated or S-plated), except where the cars are registered as private hire cars or cars for instructional purpose and are hired out or used for providing driving instruction in the course of the business. A private hire car or taxi driver's car-related running costs are allowable expenses (Section 5.3), not capital allowances. Vans, lorries and motorcycles qualify under Section 19 or 19A; the COE paid is part of their cost ([IRAS business expenses and deductions](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions)).
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

For income earned in 2026 onwards, eligible self-employed individuals may use a 20% deemed expense where they incurred allowable expenses, annual gross income per nature of business (NOB) does not exceed S$50,000, and the income is not covered by the industry-specific commission/PHC/taxi/delivery FEDRs. Aggregate businesses under the same NOB and use one method consistently across that NOB; different NOBs can use different methods. The deemed amount replaces actual allowable expenses, not an extra deduction on top. Qualifying e-filers receive FEDR automatically unless they opt out for actual allowable expenses. [IRAS FEDR](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/fixed-expense-deduction-ratio-for-self-employed-persons-and-platform-workers).

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

**Parent Relief.** All conditions in 2026: the taxpayer supported the dependant (parent, parent-in-law, grandparent, grandparent-in-law, step-parent, step-grandparent, adoptive parent or grandparent); the dependant was 55 or above; the dependant's 2026 annual income was not more than SGD 8,000 (the limit in the spouse table); neither the age nor the income condition applies to Parent Relief (Disability); and the dependant either lived with the taxpayer in Singapore, or lived in a separate household in Singapore and the taxpayer spent at least the support amount below.

| Item | Value | Note |
| --- | --- | --- |
| Staying with the dependant, per dependant | SGD 9,000 | Disability version: SGD 14,000  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29) |
| Not staying with the dependant, per dependant | SGD 5,500 | Disability version: SGD 10,000  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29) |
| Minimum support for a dependant in a separate household | SGD 2,000 | Spent "or more in supporting him/her" in 2026  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29) |

**CPF relief for the self-employed.** The person must have made compulsory MediSave or voluntary CPF contributions in 2026. From YA 2026 the rule changed:

- Compulsory MediSave contributions made in 2026 get relief in full, with no cap, even if there is no assessable net trade income for that YA.
- Voluntary CPF contributions: no relief if compulsory MediSave is more than the share of net trade income below. Otherwise relief is the lowest of (a) that share of net trade income assessed, less the relief on compulsory contributions; (b) the CPF annual limit, less the applicable compulsory contributions (including employer and employee CPF for a concurrent employee); (c) the voluntary amount actually paid.
- A person who is also an employee: if compulsory employer and employee CPF plus compulsory MediSave already exhaust the CPF annual limit, no relief is given on voluntary contributions.
- MediSave contribution rates are set by the CPF Board by age and net trade income. See `sg-cpf-medisave`.

| Item | Value | Note |
| --- | --- | --- |
| Share of net trade income used in the voluntary-contribution cap | 37% | "37% of your net trade income assessed"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |
| CPF annual limit for self-employed persons | SGD 37,740 | "The CPF annual limit will also remain at" this figure  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |
| CPF annual salary ceiling | SGD 102,000 | Unchanged by the monthly ceiling increases  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |
| CPF monthly salary ceiling, 1 Jan 2025 to 31 Dec 2025 | SGD 7,400 | Historical 2025 wages, YA 2026  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |
| CPF monthly salary ceiling, on or after 1 Jan 2026 | SGD 8,000 | 2026 wages, YA 2027; do not backdate to YA 2026  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed) |

**CPF Cash Top-up Relief.** Only for a Singapore Citizen or Permanent Resident who made cash top-ups in 2026 under the CPF Retirement Sum Topping-Up Scheme to own or family members' accounts. Top-ups that attract Matched Retirement Savings Scheme (MRSS) grants get no relief from YA 2026 (top-ups received from 1 Jan 2025). Cash top-ups attracting Matched MediSave Scheme (MMSS) grants get no cash-top-up relief from YA 2027 (cash top-ups made from 1 Jan 2026). For a top-up to a spouse or sibling (not one with disability), that person must not have had annual income of more than SGD 8,000 in 2025, the year before the top-up. There is no income condition for parents, grandparents, or a spouse or sibling with disability. A self-employed person topping up a MediSave Account must be up to date with MediSave payable.

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

**Donations (a deduction, not a relief).** Qualifying cash donations made in 2026 to an approved Institution of a Public Character (IPC) or the Community Chest are deducted from statutory income before reliefs, so they sit outside the relief cap. IRAS computes them automatically from the IPC's records; the donor must give an NRIC, FIN or UEN to the IPC. Not every registered charity is an approved IPC. The current IRAS donations page expressly illustrates a 2026 qualifying IPC donation deducted in YA 2027. The old statutory expiry quotation was not newly read; no claim is made here about donations after 2026. [IRAS donations](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations).

| Item | Value | Note |
| --- | --- | --- |
| Deduction for qualifying donations | 250% | "the 250% tax deductions for qualifying donations"; IRAS also writes "up to 2.5 times the qualifying donation amount"  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations) |

### 5.7 GST Touchpoints (detail in `sg-gst-return`)

| Item | Value | Note |
| --- | --- | --- |
| Compulsory GST registration: taxable turnover | more than SGD 1 million | At the end of the calendar year (retrospective view), OR expected in the next 12 months (prospective view)  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |

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
3. Are you a sole proprietor (Form B), also an employee, or a partner?
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

IRAS disallows expenses "on using private hire cars or private cars (E, Q or S-plate cars) such as repair, maintenance, parking fees, petrol costs", "even if the private cars were used for business purposes". The exception is a private hire car or taxi driver claiming car-related expenses in earning driving income. Vans, lorries, pick-ups and motorcycles used in the business qualify for capital allowances and upkeep. **Flag for reviewer:** vehicle type and plate; whether the person is a driver eligible for FEDR; whether IRAS's company rule applies to a sole proprietor: "Payments for transportation services for business purposes qualify for tax deduction. In contrast, expenses incurred on hiring a private car and the operation or maintenance of a hired private car are not tax-deductible" ([IRAS tax treatment of business expenses (M-R)](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses/tax-treatment-of-business-expenses-%28m-r%29)).

### 6.3 Capital vs Revenue Expenditure; Renovation (Section 14N)

Capital expenditure is not an expense; it goes through capital allowances if the asset qualifies. Qualifying renovation or refurbishment that does not affect the structure of the premises may be deducted under Section 14N. For a sole proprietor the cap applies to the individual, however many sole proprietorships he or she owns. From YA 2025 the expenditure cap uses fixed three-YA periods, first YA 2025 to YA 2027, rather than a rolling project-specific period. Three-year straight-line treatment exists, with an irrevocable option to claim qualifying expenditure in one year permanently available from YA 2025. Do not also claim the same expenditure as repairs or capital allowances. Claim it under allowable business expenses on the 4-line statement, starting from the YA of the basis period in which the cost is first incurred. Keep an itemised list, confirmation that no Building Control approval is needed, and invoices for 5 years.

| Item | Value | Note |
| --- | --- | --- |
| Section 14N renovation deduction cap | SGD 300,000 | Per fixed three-YA period, first YA2025-YA2027; qualifying-cost and no-double-deduction conditions, not a fresh cap per project. [Official source](https://www.iras.gov.sg/media/docs/default-source/e-tax/etaxguide_it_deduction_r_r_costs.pdf) |

### 6.4 CPF MediSave Contributions

The amount of compulsory MediSave depends on age and net trade income and is set by the CPF Board (2026 CPFB Tables 1 and 2 have now been read; see `sg-cpf-medisave`). The from-YA-2026 rule gives full compulsory relief; amounts paid in 2026 are considered in YA 2027 (Section 5.4). **Flag for reviewer:** confirm the amount actually paid in 2026 from the CPF statement, and split compulsory from voluntary.

### 6.5 Working Mother's Child Relief (WMCR)

WMCR has two regimes (Section 5.4): a fixed amount for a Singapore Citizen child born or adopted on or after 1 Jan 2024 (or who became a citizen after that date), and a share of the mother's earned income for an earlier child. The mother must be married, divorced or widowed; the child, not the mother, must be a Singapore Citizen. QCR plus WMCR on one child is capped per child, and all reliefs sit inside the overall cap. **Flag for reviewer:** child order (by birth, marriage or adoption date), each child's citizenship date, and how QCR is shared between parents.

### 6.6 Entertainment

The live version allowed "business entertainment (with documentation)". The saved IRAS page lists only "Food, household and entertainment expenses for yourself, family members, and friends" as private and does not address client entertainment. **Flag for reviewer:** treat client entertainment as PENDING until an accountant confirms.


## Worked cases


All amounts in these examples are hypothetical bank lines, shown as plain numbers in SGD.

### Example 1. PayNow Business Receipt

**Input line (DBS Bank statement):**
~~~
15 Mar 2026 | PayNow Credit ALPHA DESIGN PTE LTD | +8,500.00 | Balance 24,310.50
~~~

**Reasoning:** a PayNow receipt from a business client for design services is business income. If the person is not GST-registered, the whole receipt is revenue. If the person is GST-registered, the receipt includes GST at the standard rate in the GST table (Section 5.7); the GST portion is not revenue. Take the split from the tax invoice, not from a calculation on the bank line.

**Classification:** business revenue; GST split only if GST-registered.

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

**Classification:** EXCLUDE from business expenses. Record as CPF relief.

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

**Reasoning:** a laptop is a fixed asset, so its cost is not an expense. Computers qualify for a 100% write-off in one year under Section 19A(2), so the laptop is written off in YA 2027 without using the low-value cap. A different item at this price (a camera, a desk) would use the low-value write-off under Section 19A(10A), which counts toward the yearly cap in Section 5.2.

**Classification:** capital allowance for the full cost in YA 2027, Section 19A(2).

### Example 6. Private Car Expense

**Input line (UOB Bank statement):**
~~~
10 Aug 2026 | SHELL SELECT QUEENSTOWN | -120.00 | Balance 22,100.00
~~~

**Reasoning:** fuel for a private car (E, Q or S-plate) is disallowable. IRAS says such expenses "are not deductible even if the private cars were used for business purposes". The exception is a private hire car or taxi driver, who claims car-related expenses, usually through FEDR. A van, lorry or motorcycle used in the business is different: its upkeep is allowable.

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
  A2. Less: GST collected (if GST-registered)                      ___________
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
- NEVER allow capital allowances on a private, RU-plated or company car unless it is registered as a private hire or instructional car and hired out or used for driving instruction in the business. NEVER allow private car running costs, except a private hire car or taxi driver's car-related expenses.
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

Historical YA 2026 filing ran 1 Mar to 18 Apr 2026. The general IRAS self-employed guide states a 1 Mar to 18 Apr annual window, but this pass has not established a YA 2027-specific announcement. Use the actual YA 2027 notice/window; do not silently reuse a historical form. Anyone who receives a letter, form or SMS from IRAS telling them to file must file, regardless of the previous year's earnings ([IRAS late filing page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m)). For the retained historical YA 2026 cycle, the thresholds below test 2025 income. For YA 2027 use the current filing checker and actual notification; these historical rows do not certify a new-year filing exemption. The historical paper return deadline was also 18 Apr, the same as e-filing ([IRAS paper filing page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/filing-a-paper-income-tax-return)).

| Item | Value | Note |
| --- | --- | --- |
| Historical YA 2026: must file if 2025 total income was more than | SGD 22,000 | "Your total income is more than" this; OR  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/tax-season-2026---all-you-need-to-know) |
| Historical YA 2026: must file if 2025 self-employment net profit was more than | SGD 6,000 | OR a non-resident who derived income from Singapore  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/tax-season-2026---all-you-need-to-know) |

Form B carries a 2-line or 4-line statement taken from the accounts. At the end of every accounting period the person must prepare a Profit and Loss Account and a Balance Sheet.

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

**Incorrect returns** ([IRAS errors in tax returns page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/consequences-of-non-compliance/errors-in-tax-returns)).

| Item | Value | Note |
| --- | --- | --- |
| Without reasonable excuse or through negligence: penalty, share of tax undercharged | up to 200% | Plus a fine up to SGD 5,000 and/or imprisonment up to three years  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/consequences-of-non-compliance/errors-in-tax-returns) |
| With wilful intention to evade: penalty, share of tax undercharged | up to 400% | Plus a fine up to SGD 50,000 and/or imprisonment up to five years  [Official source](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/consequences-of-non-compliance/errors-in-tax-returns) |

A voluntary disclosure within one year of the statutory filing date can get the penalty waived if IRAS's qualifying conditions are met.


For the current published workflow, log in at myTax Portal with Singpass/SFA, choose Individuals → File Income Tax Return, and report under 2. Trade, Business, Profession or Vocation → Sole-Proprietorship/Self Employment Income. Revenue at most 200,000 uses Revenue/Adjusted Profit or Loss; higher revenue uses Revenue/Gross Profit or Loss/Allowable Deductions/Adjusted Profit or Loss. Cost of goods sold is deducted before gross profit; service-only gross profit equals revenue. At annual revenue 500,000 or more, upload signed certified accounts under Consolidated Statement. Review other income and reliefs, submit through the authorised workflow and retain the acknowledgement. Reconcile the actual YA form’s capital-allowance presentation to the tax workpaper without double deduction. [IRAS filing](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/filing-responsibilities-of-self-employed-persons-%28including-individual-partners%29); [IRAS business computation](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/calculating-my-business-income/calculating-business-income). Payment follows the actual notice/approved plan, with receipt retained.

## Completion checklist


### Key Legislation

| Topic | Provision |
| --- | --- |
| Resident rates | Income Tax Act 1947, Second Schedule, Table 3 (YA 2024 and later) |
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
- [ ] Actual YA 2027 filing notice/window confirmed; historical YA 2026 deadline not reused?


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

Not yet confirmed: the exact YA 2027 announced filing window, final Form B field/attachment/rounding requirements and any new personal rebate; do not reuse a YA 2026 form by changing its date. Some relief pages still illustrate YA 2026 facts; ongoing conditions and expressly announced YA 2027 changes above are the planning basis, to be reconciled with the final YA 2027 form before filing. The old statutory donation expiry and Income Tax Act/GST Act article text could not be newly opened. Home-office apportionment, client entertainment, sole-proprietor ride-hailing application, non-residence, partnerships, property/crypto character and refund/disputes remain the stated referral questions.
