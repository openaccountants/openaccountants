---
name: sg-income-tax
description: Use this skill whenever asked about Singapore income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay in Singapore", "Form B", "Form B1", "IRAS income tax", "trade income", "capital allowances Singapore", "personal reliefs", "tax residence 183 days", "Section 10(1)(a)", "CPF self-employed", "self-employed tax Singapore", "myTax Portal", "DBS Bank statement", "OCBC income", "PayNow transfer", "Stripe Singapore", or any question about filing or computing income tax for a Singapore sole proprietor or freelancer. This skill covers progressive rates (0--24%), trade income computation, capital allowances (Section 19/19A), approved deductions, personal reliefs, CPF MediSave, tax residence rules, filing deadlines, and penalties. ALWAYS read this skill before touching any Singapore income tax work.
version: 2.0
jurisdiction: SG
tax_year: 2026
last_updated: 2026-10-16
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Singapore income tax for self-employed individuals (Form B)

Figures are for tax year 2026. In Singapore this means Year of Assessment (YA) 2026, which taxes income earned in calendar year 2025 (1 Jan 2025 to 31 Dec 2025), filed between 1 Mar and 18 Apr 2026. Every relief condition below is tested in 2025: the taxpayer's age at 31 Dec 2025, a dependant's 2025 income, contributions paid in 2025. Income earned in 2026 belongs to YA 2027 and is not covered here. This skill covers a resident sole proprietor or freelancer filing Form B. Official sources were read on 5 Oct 2026. It is a working method for review, not a filed return.

## The method, step by step

1. Confirm the year and the person. YA 2026 taxes 2025 income ([IRAS tax residency page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency)). Confirm the person is self-employed: a sole proprietor or partner registered with ACRA is generally self-employed and reports business income, not salary ([IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)).
2. Confirm tax residence for YA 2026 using the tests in Section 1. A non-resident is out of scope (refusal R-SG-1). See the [IRAS tax residency page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency).
3. Confirm the accounting period. Most businesses end on 31 Dec, so the 2025 accounts feed YA 2026; a different year end feeds the YA after the year in which it ends ([IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)).
4. Build revenue from the bank statement and invoices (Sections 3 and 8). Strip GST out of receipts if the person is GST-registered; see the [GST Act section 16](https://sso.agc.gov.sg/Act/GSTA1993?ProvIds=pr16-) and the `sg-gst-return` skill.
5. Deduct allowable business expenses and remove disallowable ones, using the IRAS lists summarised in Section 5.3 ([IRAS business expenses and deductions](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions)). Qualifying commission agents, private hire car and taxi drivers and delivery workers may instead claim a deemed expense under the Fixed Expense Deduction Ratio ([IRAS FEDR page](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/fixed-expense-deduction-ratio-for-self-employed-persons-and-platform-workers)).
6. Claim capital allowances on qualifying plant and machinery under Section 19 or 19A of the Income Tax Act 1947 (Section 5.2; [IRAS capital allowances page](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances)). Never on an S-plated private car.
7. Report revenue and adjusted profit on Form B as a 2-line or 4-line statement, depending on revenue (Section 5.5; [IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)).
8. Deduct qualifying donations made in 2025 from statutory income to reach assessable income ([IRAS donations page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations)).
9. Deduct personal reliefs, each tested on 2025 facts, within the overall relief cap (Section 5.4; [IRAS tax reliefs page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs)). The result is chargeable income.
10. Apply the resident rate table in Section 1 ([IRAS individual income tax rates](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates)). IRAS prints a Personal Income Tax Rebate for YA 2024 and YA 2025 only, so apply none for YA 2026 unless IRAS publishes one ([IRAS Personal Income Tax Rebate page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/personal-income-tax-rebate)).
11. File by 18 Apr 2026 on myTax Portal, then pay within 1 month of the Notice of Assessment (Sections 5.5 and 5.6; [IRAS Tax Season 2026 page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/tax-season-2026---all-you-need-to-know)).

## Section 1. Quick Reference

| Field | Value |
| --- | --- |
| Country | Singapore |
| Tax | Individual income tax, progressive resident rates (table below) |
| Currency | SGD only |
| Tax year basis | Preceding year basis: YA 2026 taxes income earned 1 Jan 2025 to 31 Dec 2025 |
| Primary legislation | Income Tax Act 1947 |
| Tax authority | Inland Revenue Authority of Singapore (IRAS) |
| Filing portal | myTax Portal, with Singpass |
| Return | Form B (self-employed) |
| Filing deadline | 18 Apr 2026 for YA 2026, e-filing and paper alike |

### Resident rate table, YA 2026 (income earned in 2025)

These are the resident rates "From YA 2024 onwards", so they apply to YA 2026. The third column is IRAS's cumulative gross tax on all chargeable income below the slice. The last two rows are non-resident rates, shown here because IRAS prints them on the same page.

| Chargeable income slice | Rate | Gross tax on income below this slice |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates |
| First SGD 20,000 | 0% | nil |
| SGD 20,000 to SGD 30,000 | 2% | nil |
| SGD 30,000 to SGD 40,000 | 3.5% | SGD 200 |
| SGD 40,000 to SGD 80,000 | 7% | SGD 550 |
| SGD 80,000 to SGD 120,000 | 11.5% | SGD 3,350 |
| SGD 120,000 to SGD 160,000 | 15% | SGD 7,950 |
| SGD 160,000 to SGD 200,000 | 18% | SGD 13,950 |
| SGD 200,000 to SGD 240,000 | 19% | SGD 21,150 |
| SGD 240,000 to SGD 280,000 | 19.5% | SGD 28,750 |
| SGD 280,000 to SGD 320,000 | 20% | SGD 36,550 |
| SGD 320,000 to SGD 500,000 | 22% | SGD 44,550 |
| SGD 500,000 to SGD 1,000,000 | 23% | SGD 84,150 |
| Above SGD 1,000,000 | 24% | SGD 199,150 |
| Non-resident: employment income | 15% | "or the progressive resident tax rates (see table above), whichever is the higher tax amount" |
| Non-resident: director's fees, consultation fees, rental and all other income | 24% | Except employment income and income taxed at reduced withholding rates |

The statute agrees. The Second Schedule to the Income Tax Act 1947 keeps old tables for YA 2012 to 2016 and YA 2017 to 2023 next to the current one; use only Table 3, "YEAR OF ASSESSMENT 2024 AND SUBSEQUENT YEARS".

| Item | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://sso.agc.gov.sg/Act/ITA1947?ProvIds=Sc2- |
| Table 3, every dollar of chargeable income above SGD 1,000,000 | 24% | Table 3 only; the YA 2017 to 2023 table stops at a lower top rate |

No Personal Income Tax Rebate is printed for YA 2026. The IRAS rebate page covers "Years of Assessment (YAs) 2024 and 2025" only and says the rebate "cannot be carried forward". Do not deduct a rebate in a YA 2026 computation unless IRAS publishes one.

### Tax residence for YA 2026

A person is a tax resident for YA 2026 if, per the [IRAS tax residency page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency), any ONE of these holds:

- a Singapore Citizen or Singapore Permanent Resident who normally resides in Singapore except for temporary absences; OR
- a foreigner who stayed or worked in Singapore for at least 183 days in calendar year 2025; OR
- a foreigner who stayed or worked in Singapore continuously for 3 consecutive years (an administrative concession that applies even if the first and third years are under 183 days); OR
- a foreign employee whose employment straddles 2 calendar years with a continuous stay of at least 183 days. This last test is for employees only and excludes directors, public entertainers and professionals, so it does not help a self-employed person.

A stay under 183 days with none of the other tests met means non-resident.

### Conservative Defaults

| Ambiguity | Default |
| --- | --- |
| Tax residence unknown | STOP. Do not compute. |
| GST status unknown | Not GST-registered: treat the full receipt as revenue, and ask |
| Vehicle type unknown | Private car (S-plate): no capital allowances and no running costs |
| Business vs capital expenditure unclear | Capital: no deduction until confirmed as revenue |
| Home office apportionment unknown | No deduction until a basis is confirmed |
| Personal relief facts unknown | Apply only reliefs whose 2025 conditions are confirmed |
| Accounting year end unknown | Ask. Do not assume 31 Dec |

## Section 2. Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** bank statements for the whole accounting period (usually 1 Jan to 31 Dec 2025) in CSV, PDF or pasted text; confirmation of tax residence; whether GST-registered; the accounting year end.

**Recommended:** client invoices; CPF statements showing compulsory MediSave and any voluntary contributions paid in 2025; SRS statements; life insurance premium notices; details of children and parents for relief claims.

**Ideal:** fixed asset register; the prior year Notice of Assessment; Form IR8A if also employed; GST returns if GST-registered.

### Refusal Catalogue

- **R-SG-1. Non-residents.** Non-resident income is taxed differently and non-residents get no personal reliefs. Out of scope. Route residence questions to `sg-tax-residency`.
- **R-SG-2. Companies (Pte Ltd, Ltd).** Corporate income tax and Form C-S or Form C are out of scope. This skill covers individuals only.
- **R-SG-3. Partnerships.** Allocating partnership income (Form P) is out of scope. Escalate.
- **R-SG-4. Capital gains and property disposals.** Whether a gain is trading income needs specialist review. See `sg-zero-cgt`.
- **R-SG-5. GST computation.** GST registration, returns and input tax are out of scope. See `sg-gst-return`.
- **R-SG-6. Not Ordinarily Resident (NOR) scheme.** The scheme has ceased. Do not apply it to YA 2026 (Section 10).

## Section 3. Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to the rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| FAST [client name] / FAST CREDIT | Business income | Revenue | Local fast payment from a business client |
| PayNow [sender name] / PAYNOW CREDIT | Business income | Revenue | PayNow linked to NRIC or UEN |
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

## Section 4. Worked Examples

All amounts in these examples are hypothetical bank lines, shown as plain numbers in SGD.

### Example 1. PayNow Business Receipt

**Input line (DBS Bank statement):**
~~~
15 Mar 2025 | PayNow Credit ALPHA DESIGN PTE LTD | +8,500.00 | Balance 24,310.50
~~~

**Reasoning:** a PayNow receipt from a business client for design services is business income. If the person is not GST-registered, the whole receipt is revenue. If the person is GST-registered, the receipt includes GST at the standard rate in the GST table (Section 5.7); the GST portion is not revenue. Take the split from the tax invoice, not from a calculation on the bank line.

**Classification:** business revenue; GST split only if GST-registered.

### Example 2. Stripe Payout (Net of Stripe Fees)

**Input line (OCBC Bank statement):**
~~~
22 Apr 2025 | STRIPE PAYOUT SG | +4,850.00 | Available Balance 31,200.00
~~~

**Reasoning:** Stripe pays out net of its fees. Hypothetically, if Stripe collected 5,000.00 from clients and kept 150.00 in fees, revenue is 5,000.00 and the fee of 150.00 is an allowable expense. Match the payout to the Stripe dashboard for the exact gross and fee.

**Classification:** gross revenue per Stripe report; Stripe fees allowable.

### Example 3. CPF MediSave Payment

**Input line (UOB Bank statement):**
~~~
01 May 2025 | CPFB MEDISAVE CONTRIBUTION | -3,600.00 | Balance 15,400.00
~~~

**Reasoning:** a self-employed person's compulsory MediSave contribution is not a business expense; IRAS lists "Your own ... MediSave/CPF contributions" as disallowable. It is claimed as CPF relief. From YA 2026, compulsory MediSave paid in 2025 gets relief in full, without the old cap, even if the person has no net trade income for YA 2026 ([IRAS CPF relief for self-employed](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed)). Voluntary contributions remain capped (Section 5.4). The relief counts toward the overall relief cap.

**Classification:** EXCLUDE from business expenses. Record as CPF relief.

### Example 4. WeWork Office Subscription

**Input line (DBS Bank statement):**
~~~
01 Jun 2025 | WEWORK SINGAPORE PTE LTD | -1,200.00 | Balance 28,750.00
~~~

**Reasoning:** a monthly co-working fee for the business is rent for the business, which IRAS lists as allowable. No apportionment is needed where the space is used only for the business.

**Classification:** rent, allowable.

### Example 5. Laptop Purchase

**Input line (OCBC Bank statement):**
~~~
15 Jul 2025 | APPLE SINGAPORE PTE LTD | -2,899.00 | Balance 19,200.00
~~~

**Reasoning:** a laptop is a fixed asset, so its cost is not an expense. Computers qualify for a 100% write-off in one year under Section 19A(2), so the laptop is written off in YA 2026 without using the low-value cap. A different item at this price (a camera, a desk) would use the low-value write-off under Section 19A(10A), which counts toward the yearly cap in Section 5.2.

**Classification:** capital allowance for the full cost in YA 2026, Section 19A(2).

### Example 6. Private Car Expense

**Input line (UOB Bank statement):**
~~~
10 Aug 2025 | SHELL SELECT QUEENSTOWN | -120.00 | Balance 22,100.00
~~~

**Reasoning:** fuel for a private car (E, Q or S-plate) is disallowable. IRAS says such expenses "are not deductible even if the private cars were used for business purposes". The exception is a private hire car or taxi driver, who claims car-related expenses, usually through FEDR. A van, lorry or motorcycle used in the business is different: its upkeep is allowable.

**Classification:** private car: NOT deductible. Ask whether the person is a private hire car or taxi driver, or whether the vehicle is a van, lorry or motorcycle.

## Section 5. Tier 1 Rules (When Data Is Clear)

### 5.1 Business Income Computation

~~~
Gross revenue from the trade, business, profession or vocation
Less: allowable business expenses (Section 5.3)
Less: capital allowances (Section 5.2); add any balancing charge on disposal
= Adjusted profit (the figure on the 2-line or 4-line statement)
Add: other income (employment, rental, etc.) = statutory income
Less: qualifying donations made in 2025 (Section 5.4, donations table)
= Assessable income
Less: personal reliefs, tested on 2025 facts, within the overall relief cap
= Chargeable income
Apply the resident rate table (Section 1)
Less: Parenthood Tax Rebate if claimable; no Personal Income Tax Rebate is printed for YA 2026
= Tax payable (estimate until IRAS issues the Notice of Assessment)
~~~

IRAS sets the order: "Total statutory income Less: Donations =Assessable income Less: Personal reliefs =Chargeable income" ([IRAS donations page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations)).

### 5.2 Capital Allowances

Capital allowances replace depreciation, which is not deductible. They apply to plant and machinery used in the business. The IRAS page below is written for companies; the IRAS page for self-employed persons sends them to it: "depreciation of fixed assets may be claimed as capital allowances" ([IRAS business expenses and deductions](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions)).

| Method or limit | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances |
| 1-year write-off, Section 19A(2) and 19A(10A): computers, prescribed automation equipment, low-value assets | 100% | Of cost in one YA. Only these assets, not every asset |
| Low-value asset, Section 19A(10A): cost per asset | SGD 5,000 | "A low-value asset is one that does not cost more than" this amount |
| Low-value assets: total 1-year claim per YA | SGD 30,000 | "must not exceed" this per YA. Assets above the cap go to 3 years or working life |
| 3-year write-off, Section 19A(1) | 1/3 of cost a year | Any qualifying asset |
| Working life, Section 19: initial allowance in the first YA | 20% | Of cost |
| Working life, Section 19: annual allowance each YA | 80% | Of cost, divided by the working life. By irrevocable election: 6 or 12 years if the Sixth Schedule life is 12 years or less; 6, 12 or 16 years if it is 16 years |

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

### 5.4 Personal Reliefs

Every relief is for YA 2026 and is tested on 2025 facts. All reliefs together are capped: total reliefs allowed are limited to the cap below.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs |
| Overall cap on the total of all reliefs, per YA | SGD 80,000 | "applies to the total amount of all tax reliefs claimed for each Year of Assessment" |

**Earned Income Relief.** Granted on taxable earned income (less allowable expenses) in 2025, by age at 31 Dec 2025. If earned income is lower than the maximum, the relief is limited to the earned income.

| Age at 31 Dec 2025 | Maximum | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/earned-income-relief |
| Below 55 | SGD 1,000 | Disability version: SGD 4,000 |
| 55 to 59 | SGD 6,000 | Disability version: SGD 10,000 |
| 60 and above | SGD 8,000 | Disability version: SGD 12,000 |

**Spouse Relief.** For a spouse who lived with or was supported by the taxpayer in 2025 and whose 2025 annual income was not more than the limit below. Annual income here includes taxable income, tax-exempt income such as bank interest and dividends (but not CPF payouts) and foreign-sourced income whether or not remitted. The income condition does not apply to Spouse Relief (Disability) for a disabled spouse. A legally separated taxpayer may claim if paying maintenance under a Court Order or Deed of Separation; the relief is then the lower of the maintenance paid in 2025 and the amount in the table. Divorced taxpayers paying alimony cannot claim.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/spouse-relief-spouse-relief-%28disability%29 |
| Spouse's 2025 annual income must not exceed | SGD 8,000 | Raised with effect from YA 2025; the lower YA 2024 limit is stale |
| Spouse Relief | SGD 2,000 | Spouse Relief (Disability): SGD 5,500 |

**Qualifying Child Relief (QCR).** All conditions in 2025: the child is unmarried; born to the taxpayer and spouse or ex-spouse, a step-child or legally adopted; below 16, or studying full-time at any university, college or other educational institution; the child's 2025 annual income was not more than SGD 8,000 (the same limit as the spouse table); and the taxpayer maintained the child. The age, study and income conditions do not apply to Child Relief (Disability) for a disabled child.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/qualifying-child-relief-%28qcr%29-child-relief-%28disability%29 |
| QCR, per child | SGD 4,000 | Child Relief (Disability): SGD 7,500 per child |
| QCR (or Child Relief (Disability)) plus WMCR on the same child | SGD 50,000 | Cap per child |

**Working Mother's Child Relief (WMCR).** Only for a working mother who is married, divorced or widowed and has taxable earned income in 2025, for a child who is a Singapore Citizen at 31 Dec 2025 and meets every QCR condition. Single and male taxpayers cannot claim. Two regimes, by the date the child was born, adopted or became a citizen:

| Child order | Child born or adopted on or after 1 Jan 2024 (fixed amount) | Child born or adopted before 1 Jan 2024 (share of mother's earned income) |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/working-mother%27s-child-relief-%28wmcr%29 |
| 1st | SGD 8,000 | 15% |
| 2nd | SGD 10,000 | 20% |
| 3rd and beyond | SGD 12,000 | 25% |
| Total WMCR over all children | capped at 100% of her earned income | "the total claim is capped at 100% of her earned income" |

A child born or adopted before 1 Jan 2024 who became a Singapore Citizen only after 1 Jan 2024 takes the fixed amount, not the percentage. The overall relief cap still applies.

**Parent Relief.** All conditions in 2025: the taxpayer supported the dependant (parent, parent-in-law, grandparent, grandparent-in-law, step-parent, step-grandparent, adoptive parent or grandparent); the dependant was 55 or above; the dependant's 2025 annual income was not more than SGD 8,000 (the limit in the spouse table); neither the age nor the income condition applies to Parent Relief (Disability); and the dependant either lived with the taxpayer in Singapore, or lived in a separate household in Singapore and the taxpayer spent at least the support amount below.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29 |
| Staying with the dependant, per dependant | SGD 9,000 | Disability version: SGD 14,000 |
| Not staying with the dependant, per dependant | SGD 5,500 | Disability version: SGD 10,000 |
| Minimum support for a dependant in a separate household | SGD 2,000 | Spent "or more in supporting him/her" in 2025 |

**CPF relief for the self-employed.** The person must have made compulsory MediSave or voluntary CPF contributions in 2025. From YA 2026 the rule changed:

- Compulsory MediSave contributions made in 2025 get relief in full, with no cap, even if there is no assessable net trade income for YA 2026.
- Voluntary CPF contributions: no relief if compulsory MediSave is more than the share of net trade income below. Otherwise relief is the lowest of (a) that share of net trade income assessed, less the relief on compulsory contributions; (b) the CPF annual limit, less the relief on compulsory contributions; (c) the voluntary amount actually paid.
- A person who is also an employee: if compulsory employee CPF plus compulsory MediSave already exceed the CPF annual limit, no relief is given on voluntary contributions.
- MediSave contribution rates are set by the CPF Board by age and net trade income. See `sg-cpf-medisave`.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed |
| Share of net trade income used in the voluntary-contribution cap | 37% | "37% of your net trade income assessed" |
| CPF annual limit for self-employed persons | SGD 37,740 | "The CPF annual limit will also remain at" this figure |
| CPF annual salary ceiling | SGD 102,000 | Unchanged by the monthly ceiling increases |
| CPF monthly salary ceiling, 1 Jan 2025 to 31 Dec 2025 | SGD 7,400 | Applies to 2025 wages, so to YA 2026 |
| CPF monthly salary ceiling, on or after 1 Jan 2026 | SGD 8,000 | Applies to 2026 wages, so to YA 2027, NOT YA 2026 |

**CPF Cash Top-up Relief.** Only for a Singapore Citizen or Permanent Resident who made cash top-ups in 2025 under the CPF Retirement Sum Topping-Up Scheme to own or family members' accounts. Top-ups that attract Matched Retirement Savings Scheme (MRSS) grants get no relief from YA 2026 (top-ups received from 1 Jan 2025). For a top-up to a spouse or sibling (not one with disability), that person must not have had annual income of more than SGD 8,000 in 2024, the year before the top-up. There is no income condition for parents, grandparents, or a spouse or sibling with disability. A self-employed person topping up a MediSave Account must be up to date with MediSave payable.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-cash-top-up-relief |
| Total relief per YA | SGD 16,000 | Self and family members together |
| Own account, maximum (same maximum again for family members) | SGD 8,000 | Separate limits; one cannot use the other |

**Supplementary Retirement Scheme (SRS) Relief.** Contributions must be made by 31 Dec 2025 for YA 2026. One SRS account only.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/supplementary-retirement-scheme-%28srs%29-relief |
| Yearly maximum, Singapore Citizens and Permanent Residents | SGD 15,300 | Subject to the overall relief cap |
| Yearly maximum, foreigners | SGD 35,700 | Subject to the overall relief cap |

**Life Insurance Relief.** Only if the total of compulsory employee CPF and compulsory MediSave or voluntary CPF as a self-employed person in 2025 was LESS than the amount below. Premiums must be on the taxpayer's own or spouse's life; from YA 2026 this includes a wife's premiums on her husband's policy. The insurer needs an office or branch in Singapore for policies taken on or after 10 Aug 1973. IRAS: "You may claim the lower of: a. the difference between" the CPF limit below "and your CPF contribution; or b. up to" the share of insured value below "or the amount of insurance premiums paid." Accident, hospitalisation, health, disability, critical illness, endowment and riders do not qualify, nor investment-linked policies where investment is a fundamental consideration.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/life-insurance-relief |
| 2025 CPF contributions must be less than | SGD 5,000 | "The total CPF contribution for the following was less than" this; at or above it, no relief |
| Premium limit, share of the insured value | 7% | "up to 7% of the insured value of your own/your spouse's life" |

**Course Fees Relief: discontinued.** IRAS: "Course Fees Relief has been discontinued with effect from Year of Assessment (YA) 2026. The final year in which Course Fees Relief may be claimed is in YA 2025." Do not claim it for YA 2026 ([IRAS Course Fees Relief page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/course-fees-relief)).

**Donations (a deduction, not a relief).** Qualifying cash donations made in 2025 to an approved Institution of a Public Character (IPC) or the Community Chest are deducted from statutory income before reliefs, so they sit outside the relief cap. IRAS computes them automatically from the IPC's records; the donor must give an NRIC, FIN or UEN to the IPC. Not every registered charity is an approved IPC. The 2.5 times deduction covers donations made "from 1 January 2016 to 31 December 2026 (both dates inclusive)" ([Income Tax Act 1947, section 37](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr37-)).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations |
| Deduction for qualifying donations | 250% | "the 250% tax deductions for qualifying donations"; IRAS also writes "up to 2.5 times the qualifying donation amount" |

### 5.5 Filing and Payment

For YA 2026, file between 1 Mar and 18 Apr 2026 on myTax Portal. Anyone who receives a letter, form or SMS from IRAS telling them to file must file, regardless of the previous year's earnings ([IRAS late filing page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m)). Anyone not notified must still file if, in 2025, any ONE of the conditions below holds. The paper return deadline is also 18 Apr, no longer earlier than e-filing ([IRAS paper filing page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/filing-a-paper-income-tax-return)).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/tax-season-2026---all-you-need-to-know |
| Must file if 2025 total income was more than | SGD 22,000 | "Your total income is more than" this; OR |
| Must file if 2025 self-employment net profit was more than | SGD 6,000 | OR a non-resident who derived income from Singapore |

Form B carries a 2-line or 4-line statement taken from the accounts. At the end of every accounting period the person must prepare a Profit and Loss Account and a Balance Sheet.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons |
| 2-line statement (revenue, adjusted profit or loss) when revenue is this or less | SGD 200,000 | "when your revenue is $200,000 or less from YA 2021" |
| 4-line statement (revenue, gross profit, allowable business expenses, adjusted profit) | more than SGD 200,000 | Applies from YA 2021 |

Tax is payable within 1 month from the date of the Notice of Assessment, even if the person objects ([IRAS late payment page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax)). A person on an approved instalment plan is not charged the late payment penalty. A person who cannot pay in full may apply for up to 12 interest-free monthly instalments via GIRO; the GIRO application must be approved before the payment due date to avoid the late payment penalty.

### 5.6 Penalties

**Late filing or non-filing** ([IRAS late filing page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m)). Failing to file by the due date is an offence. IRAS may issue an estimated Notice of Assessment (payable within 1 month, and it may assume higher income), offer to compound the offence, or issue a summons.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m |
| Composition amount, per offence | up to SGD 5,000 | "depending on your past compliance records" |
| Fine on conviction in court, per offence | up to SGD 5,000 | Return must still be filed |
| Failing to file for 2 or more years, on conviction | penalty of twice the tax assessed, plus a fine of up to SGD 5,000 | Imprisonment up to 6 months if unpaid |

**Late payment** ([IRAS late payment page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax)).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax |
| Late payment penalty on unpaid tax after the due date | 5% | Not imposed if on an approved instalment plan |
| Additional penalty per completed month unpaid, starting 60 days after the 5% penalty | 1% | 60 days, not 30 |
| Maximum additional penalty | 12% | "up to a maximum of 12% of the unpaid tax" |

IRAS may also appoint agents (bank, employer, tenant) to collect, and may issue a Travel Restriction Order.

**Incorrect returns** ([IRAS errors in tax returns page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/consequences-of-non-compliance/errors-in-tax-returns)).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/consequences-of-non-compliance/errors-in-tax-returns |
| Without reasonable excuse or through negligence: penalty, share of tax undercharged | up to 200% | Plus a fine up to SGD 5,000 and/or imprisonment up to three years |
| With wilful intention to evade: penalty, share of tax undercharged | up to 400% | Plus a fine up to SGD 50,000 and/or imprisonment up to five years |

A voluntary disclosure within one year of the statutory filing date can get the penalty waived if IRAS's qualifying conditions are met.

### 5.7 GST Touchpoints (detail in `sg-gst-return`)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst |
| Compulsory GST registration: taxable turnover | more than SGD 1 million | At the end of the calendar year (retrospective view), OR expected in the next 12 months (prospective view) |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sso.agc.gov.sg/Act/GSTA1993?ProvIds=pr16- |
| GST standard rate | 9% | "( cb ) 9% from and including 1 January 2024" |

For a GST-registered person, GST collected is not revenue and GST paid that is claimable as input tax is not an expense.

## Section 6. Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

No saved IRAS page sets a home office method. IRAS allows "Rent, utility, and telephone charges for the business" and disallows household expenses. A business share of home utilities, internet or rent may be arguable where part of the home is used for the business. **Flag for reviewer:** the apportionment basis (floor area or time), the evidence, and whether the person rents or owns.

### 6.2 Motor Vehicles and Ride-hailing

IRAS disallows expenses "on using private hire cars or private cars (E, Q or S-plate cars) such as repair, maintenance, parking fees, petrol costs", "even if the private cars were used for business purposes". The exception is a private hire car or taxi driver claiming car-related expenses in earning driving income. Vans, lorries, pick-ups and motorcycles used in the business qualify for capital allowances and upkeep. **Flag for reviewer:** vehicle type and plate; whether the person is a driver eligible for FEDR; whether IRAS's company rule applies to a sole proprietor: "Payments for transportation services for business purposes qualify for tax deduction. In contrast, expenses incurred on hiring a private car and the operation or maintenance of a hired private car are not tax-deductible" ([IRAS tax treatment of business expenses (M-R)](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses/tax-treatment-of-business-expenses-%28m-r%29)).

### 6.3 Capital vs Revenue Expenditure; Renovation (Section 14N)

Capital expenditure is not an expense; it goes through capital allowances if the asset qualifies. Qualifying renovation or refurbishment that does not affect the structure of the premises may be deducted under Section 14N. For a sole proprietor the cap applies to the individual, however many sole proprietorships he or she owns. Claim it under allowable business expenses on the 4-line statement, starting from the YA of the basis period in which the cost is first incurred. Keep an itemised list, confirmation that no Building Control approval is needed, and invoices for 5 years.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions |
| Section 14N renovation deduction cap | SGD 300,000 | "for every relevant 3-year period" |

### 6.4 CPF MediSave Contributions

The amount of compulsory MediSave depends on age and net trade income and is set by the CPF Board (its rate page could not be read; see `sg-cpf-medisave`). For tax, from YA 2026 compulsory MediSave paid in 2025 gets relief in full (Section 5.4). **Flag for reviewer:** confirm the amount actually paid in 2025 from the CPF statement, and split compulsory from voluntary.

### 6.5 Working Mother's Child Relief (WMCR)

WMCR has two regimes (Section 5.4): a fixed amount for a Singapore Citizen child born or adopted on or after 1 Jan 2024 (or who became a citizen after that date), and a share of the mother's earned income for an earlier child. The mother must be married, divorced or widowed; the child, not the mother, must be a Singapore Citizen. QCR plus WMCR on one child is capped per child, and all reliefs sit inside the overall cap. **Flag for reviewer:** child order (by birth, marriage or adoption date), each child's citizenship date, and how QCR is shared between parents.

### 6.6 Entertainment

The live version allowed "business entertainment (with documentation)". The saved IRAS page lists only "Food, household and entertainment expenses for yourself, family members, and friends" as private and does not address client entertainment. **Flag for reviewer:** treat client entertainment as PENDING until an accountant confirms.

## Section 7. Excel Working Paper Template

~~~
SINGAPORE INCOME TAX WORKING PAPER
Taxpayer: _______________  NRIC/FIN: ___________
Year of Assessment: YA 2026 (income earned 1 Jan 2025 to 31 Dec 2025)
Accounting period: ____________ to ____________
GST registered: Yes / No [circle one]

A. GROSS REVENUE
  A1. Total receipts from clients (grossed up for platform fees)   ___________
  A2. Less: GST collected (if GST-registered)                      ___________
  A3. Net revenue                                                   ___________

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

D. ADJUSTED PROFIT (A3 - B12 - C5)            ___________

E. OTHER INCOME (employment, rental)          ___________

F. STATUTORY INCOME (D + E)                   ___________

G. QUALIFYING DONATIONS MADE IN 2025 (deduction per donations table)  ___________

H. ASSESSABLE INCOME (F - G)                  ___________

I. PERSONAL RELIEFS (2025 facts)
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
   (no Personal Income Tax Rebate printed for YA 2026)

M. ESTIMATED TAX PAYABLE (K - L)              ___________

REVIEWER FLAGS:
  [ ] Tax residence for YA 2026 confirmed?
  [ ] Accounting year end confirmed?
  [ ] GST status confirmed?
  [ ] Capital vs revenue reviewed?
  [ ] Private car: no capital allowances and no running costs?
  [ ] Relief conditions tested on 2025 facts?
  [ ] Relief cap SGD 80,000 checked?
  [ ] Donations deducted before reliefs, outside the cap?
  [ ] Course Fees Relief NOT claimed?
~~~

## Section 8. Bank Statement Reading Guide

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
| PayNow Credit [name/UEN] | PayNow receipt | Business income |
| GIRO Credit / GIRO Debit | Standing instruction | Regular income or recurring expense |
| IBG / INTERBANK GIRO | Interbank GIRO | Income or expense transfer |
| TT FROM [bank/name] | Telegraphic transfer in | Overseas client income |
| PAYNOW QR | PayNow QR code payment | Business income |
| ATM WITHDRAWAL | Cash withdrawal | Personal: investigate |
| INTEREST CREDIT | Bank interest | Generally tax-exempt for individuals |
| IRAS GIRO | IRAS tax payment | Tax payment: exclude |
| CPFB | CPF Board payment | MediSave: CPF relief, not an expense |

## Section 9. Onboarding Fallback

If the client provides a bank statement but cannot answer the onboarding questions yet:

1. Classify FAST, PayNow and GIRO credits from non-personal sources as potential business income.
2. Classify CPFB debits as MediSave (CPF relief, not a business expense).
3. Apply the conservative defaults in Section 1: not GST-registered, no private car costs or allowances, no home office share.
4. Flag every purchase that looks like equipment as potential capital expenditure for Section 5.2.
5. Produce the working paper with PENDING flags. Do not compute tax until residence is confirmed.

Present these questions:

~~~
ONBOARDING QUESTIONS: SINGAPORE INCOME TAX (YA 2026)
1. Are you a Singapore citizen, PR or foreigner? If a foreigner, how many days were you in Singapore in 2025, and in 2024 and 2026?
2. Are you GST-registered?
3. Are you a sole proprietor (Form B), also an employee, or a partner?
4. What is your business, and when does your accounting year end?
5. Are you a commission agent, private hire car or taxi driver, or delivery worker (FEDR)?
6. Do you work from home or from separate premises?
7. Do you use a vehicle for work? What plate: S, Q, E, or a van, lorry or motorcycle?
8. CPF: what compulsory MediSave and voluntary CPF did you pay in 2025?
9. SRS: did you contribute by 31 Dec 2025?
10. Children (ages, citizenship, birth dates) and parents (ages, 2025 income, living with you)?
11. Donations to approved IPCs in 2025?
~~~

## Section 10. Reference Material

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

IRAS: "The NOR scheme has ceased. The last NOR status granted will run / be valid from YA 2020 to YA 2024." No NOR concession applies to YA 2026 ([IRAS NOR page](https://www.iras.gov.sg/schemes/individual-income-tax/not-ordinarily-resident-%28nor%29-scheme)).

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

- [ ] YA 2026 = income earned in 2025, and every relief tested on 2025 facts?
- [ ] Tax residence confirmed before applying resident rates?
- [ ] GST excluded from revenue for a GST-registered person?
- [ ] Private car: no capital allowances, no running costs (running costs only for a private hire car or taxi driver)?
- [ ] 1-year write-off used only for computers, automation equipment and low-value assets?
- [ ] Compulsory MediSave relief given in full; voluntary CPF relief capped?
- [ ] Relief cap applied; donations deducted before reliefs?
- [ ] Course Fees Relief not claimed; no YA 2026 Personal Income Tax Rebate applied?
- [ ] Filing deadline 18 Apr 2026 for e-filing and paper?

## Ask the client first

- Where were you resident in 2025: citizen, PR, or a foreigner with how many days in Singapore (and in the years either side)? This decides whether any of this skill applies.
- When does your accounting year end? A non-December year end changes which accounts feed YA 2026.
- Are you GST-registered, and from what date? This changes revenue on every receipt.
- Are you a commission agent, private hire car or taxi driver, or delivery worker? FEDR may replace actual expenses.
- What vehicle do you use: private car (S, Q or E plate) or a van, lorry or motorcycle? This decides whether any motor cost or allowance is allowed.
- Which of these did you have in 2025: compulsory MediSave, voluntary CPF, SRS contributions, children born or adopted (and their dates), parents you supported? Each relief turns on 2025 facts.

## When to refuse or refer

- Non-resident for YA 2026, or residence unclear: refuse the computation; refer to `sg-tax-residency` and an accountant.
- A company, LLP or partnership: refuse; this skill is for individuals.
- Disposals of property, shares or crypto where the gain may be trading income: refer.
- Prior years with unfiled returns, an estimated assessment, a composition offer or a summons: refer to an accountant now.
- Any suspected wilful omission of income: refer; do not prepare a return around it.
- Someone claiming NOR concessions or Course Fees Relief for YA 2026: explain both have ended and refer if they insist.
- Always present the tax as an estimate until IRAS issues the Notice of Assessment.

## PROHIBITIONS

- NEVER apply resident rates without confirming tax residence for YA 2026.
- NEVER treat YA 2026 as income earned in 2026. YA 2026 is 2025 income.
- NEVER include GST collected as revenue for a GST-registered person.
- NEVER allow capital allowances on a private, RU-plated or company car unless it is registered as a private hire or instructional car and hired out or used for driving instruction in the business. NEVER allow private car running costs, except a private hire car or taxi driver's car-related expenses.
- NEVER give the 1-year write-off to an asset that is not a computer, prescribed automation equipment or a low-value asset.
- NEVER allow income tax, drawings, own CPF or own insurance as business expenses.
- NEVER allow personal or domestic expenses as business deductions.
- NEVER let total personal reliefs exceed the cap (donations are not inside it).
- NEVER claim Course Fees Relief for YA 2026, or apply NOR concessions.
- NEVER apply a YA 2026 Personal Income Tax Rebate; IRAS prints none.
- NEVER describe non-resident employment income as taxed at a flat rate alone: it is the flat rate or resident rates, whichever gives more tax.
- NEVER present tax calculations as final. Label them estimates and direct the client to an Accredited Tax Adviser for confirmation.

## Sources

- [IRAS individual income tax rates](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates)
- [Income Tax Act 1947, Second Schedule](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=Sc2-)
- [IRAS working out my tax residency](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/working-out-my-tax-residency)
- [IRAS Personal Income Tax Rebate](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/personal-income-tax-rebate)
- [IRAS basic guide for self-employed persons](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/tax-obligations-of-self-employed-persons/basic-guide-for-self-employed-persons)
- [IRAS business expenses and deductions](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions)
- [IRAS Fixed Expense Deduction Ratio](https://www.iras.gov.sg/taxes/individual-income-tax/self-employed-and-partnerships/business-expenses-and-deductions/fixed-expense-deduction-ratio-for-self-employed-persons-and-platform-workers)
- [IRAS capital allowances](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/claiming-allowances/capital-allowances)
- [IRAS tax reliefs](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs)
- [IRAS Earned Income Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/earned-income-relief)
- [IRAS Spouse Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/spouse-relief-spouse-relief-%28disability%29)
- [IRAS Qualifying Child Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/qualifying-child-relief-%28qcr%29-child-relief-%28disability%29)
- [IRAS Working Mother's Child Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/working-mother%27s-child-relief-%28wmcr%29)
- [IRAS Parent Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-%28disability%29)
- [IRAS CPF relief for self-employed](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-relief-for-self-employed-employee-who-is-also-self-employed)
- [IRAS CPF Cash Top-up Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-%28cpf%29-cash-top-up-relief)
- [IRAS SRS Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/supplementary-retirement-scheme-%28srs%29-relief)
- [IRAS Life Insurance Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/life-insurance-relief)
- [IRAS Course Fees Relief](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/course-fees-relief)
- [IRAS donations](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/donations)
- [Income Tax Act 1947, section 37](https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr37-)
- [IRAS tax treatment of business expenses (M-R)](https://www.iras.gov.sg/taxes/corporate-income-tax/income-deductions-for-companies/business-expenses/tax-treatment-of-business-expenses-%28m-r%29)
- [IRAS Tax Season 2026](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/tax-season-2026---all-you-need-to-know)
- [IRAS paper filing](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/filing-a-paper-income-tax-return)
- [IRAS late filing or non-filing](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/understanding-my-income-tax-filing/late-filing-or-non-filing-of-individual-income-tax-returns-form-b1-b-p-m)
- [IRAS late payment or non-payment](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/late-payment-or-non-payment-of-individual-income-tax)
- [IRAS errors in tax returns](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/consequences-of-non-compliance/errors-in-tax-returns)
- [IRAS NOR scheme](https://www.iras.gov.sg/schemes/individual-income-tax/not-ordinarily-resident-%28nor%29-scheme)
- [IRAS GST registration](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst)
- [Goods and Services Tax Act 1993, section 16](https://sso.agc.gov.sg/Act/GSTA1993?ProvIds=pr16-)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an Accredited Tax Adviser, Chartered Accountant, or equivalent licensed practitioner in Singapore) before filing or acting upon.

The most up-to-date version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
