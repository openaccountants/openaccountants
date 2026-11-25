---
name: pg-income-tax
description: >
  Compute 2026 PNG individual income tax using the enacted Income Tax Act 2025 and budget amendment. Separate final salary withholding, annual ordinary tax and eligible small business tax; reconcile bank evidence, deductions, GST, dependant credits, superannuation, provisional payments and filing dates. Produce a supported working paper and retain unresolved facts for a PNG practitioner.
jurisdiction: PG
category: international
tax_year: 2026
last_updated: 2026-11-22
version: 1.1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Papua New Guinea employee and sole-trader income tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Compute PNG individual income tax for the calendar tax year 2026, reconcile employment withholding and sole-trader income, and produce a working paper for a PNG practitioner. This skill covers the new Income Tax Act 2025 as enacted and amended for 2026. The Finance Department's current fiscal-year instruction designates the calendar year. [FMM 03.7](https://www.finance.gov.pg/wp-content/uploads/2026/04/FMM-03-07-Financial-Fiscal-Year.pdf). It does not recertify a 2025 return under the repealed Act. The new Act's transition provisions preserve specified earlier liabilities and project arrangements; an old-year return needs its own period's law. [Income Tax Act ss. 163-165](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Employees and sole traders are different tax jobs. A salary-only person may have final SWT and no compulsory annual income-tax return. A professional sole trader may fall under ordinary annual income tax, while another sole trader may qualify for small business tax instead. Never compute ordinary tax on every bank receipt without identifying the regime first.

### Quick reference

| Item | 2026 rule and conditions | Official source |
|---|---|---|
| Resident first annual band | PGK 20,000 at 0%; no former resident 22% first band | [Sch. 1 Part I clause (1)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Non-resident first annual band | PGK 20,000 at 22%, if ordinary income tax applies | [Sch. 1 Part I clause (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Top annual marginal band | 42% on the part above PGK 250,000 | [Sch. 1 Part I clauses (1), (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Resident day-count test | 183 days or more in aggregate, subject to usual-abode and intention exception and other residence tests | [s. 10](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Ordinary individual return | Within 3 months of tax-year end; no automatic individual tax-agent extension in this provision | [s. 135(1)(c)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Calendar-year 2026 return | Derived: 31 March 2027, unless an applicable lawful extension changes it | [s. 135](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| SWT employer remittance | By 7th of the month following the payment month | [s. 158](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Provisional income tax | 3 instalments, last day of the month after the third, sixth and ninth tax-year months | [s. 138](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| GST and income tax | Output GST is excluded from registered business assessable income; recoverable input GST is excluded from deductions and asset cost | [s. 46](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |

## Ask the client first

Read the complete case record and existing records before asking for more facts. Obtain the tax year, residence facts and travel dates, income sources, legal entity and business activities, full bank records and reconciliations, gross payroll and withholding certificates, invoices, contracts, GST registration and returns, expenses and evidence of business use, asset register, fund statements, dependants, prior assessments and provisional payments. A tax-agent deadline must be grounded in the correct taxpayer category; the company deadline is not an individual extension.

Minimum records for an actual annual calculation are residence and regime facts plus enough source documents to reconstruct gross assessable income, deductions and credits. A bank statement alone supports a provisional transaction schedule, not a final gross salary, final-tax conclusion or tax return. No bank statement or other income evidence at all is a hard stop. Existing payslips or an income ledger can substitute for a bank document where they supply the necessary facts; do not demand the same evidence twice.

| Missing fact | Action rather than a guessed default |
|---|---|
| Residence | Stop selection of annual or fortnightly bands; retain alternative scenarios |
| SWT already withheld | Obtain payslips and certificate; do not assume final tax from a salary narrative |
| Business purpose or mixed-use percentage | Mark the expense pending with its full amount and evidence request; an excluded draft amount is not a legal finding of no deduction |
| GST status | Obtain the registration record and effective dates; do not assume not registered |
| Fund coverage or pay base | Use `pg-payroll-social`; do not invent a citizenship exemption or exclude commissions automatically |
| Capital asset or depreciation life | Preserve in the asset schedule and obtain the applicable statutory allowance; do not expense the whole bank payment |
| Sole-trader small business tax eligibility | Test the statutory conditions before applying ordinary bands |

## The method, step by step

### 1. Identify residence, source and the applicable regime

A resident individual is one who resides in PNG; has PNG domicile without a permanent abode outside PNG; meets the statutory aggregate day-count test without its usual-abode/intention exception; or is a PNG citizen government employee posted abroad. Temporary absences specified by the Act count towards presence and part of a day counts as a whole day. Arrival and departure years have statutory part-year residence rules. Citizenship alone does not decide annual tax residence. Refer part-year allocation and treaty dual residence rather than granting or denying a whole-year threshold automatically. [s. 10](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Residents generally bring worldwide assessable income into ordinary income tax, subject to exemptions and foreign-income rules. Non-residents bring PNG-source assessable income into it. Foreign employment, treaty relief, expatriate packages, foreign losses and foreign credits require the actual statutory conditions, not the place where a bank account is held. Mixed expatriate or foreign-source cases remain outside the ordinary computation here. [ss. 7-10, 18(4)-(5), 23-25 and 66-70, Sch. 3](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Check small business tax before ordinary sole-trader tax. Under the Act it applies to a qualifying individual carrying on business solely in PNG, not registered for GST, whose prior-year business income was not subject to ordinary income tax and whose prior-year turnover did not exceed the GST registration threshold in the GST Act. The Commissioner may consider associates' turnover. Professional services, including accounting, consulting, managerial, financial, legal, medical, dental, engineering and architectural services, are excluded from this small-business definition. Obtain the current GST threshold before certifying eligibility. [s. 12(1)-(3)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

| Small business tax item | Statutory figure and condition | Official source |
|---|---|---|
| Annual mode | If current-year turnover is below PGK 60,000, annual tax PGK 250 | [s. 12(4), Sch. 1 Part I clause (7) and Part II clause (1)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Quarterly mode | If current-year turnover is PGK 60,000 or more, PGK 62.50 plus 2% of that quarter's turnover above PGK 15,000 | [s. 12(5), Sch. 1 Part I clause (8) and Part II clause (1)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Election into ordinary income tax | Approved-form election by return due date or permitted later date; remains in force indefinitely unless permission is granted | [s. 12(6)-(8)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Return to small business tax | Prior ordinary-income-tax payer needs permission; after an election, application cannot be made until at least 3 years after the first ordinary-tax year | [s. 12(9)-(12)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |

Small business tax is final on the business income to which it applies. It is not a second tax added to the same income under the ordinary annual bands. An election-year credit prevents small-business payments being lost when ordinary income tax applies. Do not infer the small-business calendar from ordinary provisional tax. Under section 141 keep cash and credit sales records, employment-income records where staff are employed, quarterly inventories and evidence supporting exempt income. Retain these for 3 years after the relevant quarter ends. Maintain a bank account solely for business unless the Commissioner General exempts the taxpayer. The annual mode under section 12(4) requires a return within 28 days after tax-year end; the quarterly mode under section 12(5) requires one within 28 days after quarter-end. Tax is due on the corresponding return due date. The live form and GST threshold remain held; these statutory dates do not. [ss. 12, 141-143](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Companies use `pg-corporate-income-tax`. Partnerships file an information return but their partners are taxed under the partnership rules; do not label a partnership itself an ordinary individual. Trust distributions and fund returns need their own rules. [ss. 55-65 and 135](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

### 2. Use the correct rate table

Annual ordinary income tax uses the following marginal bands. Rates apply only to the part in each band, not all income at the highest reached rate. Amounts and return working papers are in Papua New Guinea kina, PGK.

| Annual taxable income, PGK | Resident marginal rate | Non-resident marginal rate | Official source |
|---|---|---|---|
| Up to 20,000 | 0% | 22% | [Income Tax Act Sch. 1 Part I clauses (1), (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Above 20,000 up to 33,000 | 30% | 30% | [Sch. 1 Part I clauses (1), (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Above 33,000 up to 70,000 | 35% | 35% | [Sch. 1 Part I clauses (1), (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Above 70,000 up to 250,000 | 40% | 40% | [Sch. 1 Part I clauses (1), (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Above 250,000 | 42% | 42% | [Sch. 1 Part I clauses (1), (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |


Derived resident cumulative annual tax is nil at the first threshold, PGK 3,900 at the second, PGK 16,850 at the third and PGK 88,850 at the fourth. For an otherwise identical non-resident annual ordinary-tax calculation, add the first-band tax of PGK 4,400. These are computations from the linked annual schedule, not separate statutory flat taxes. [Sch. 1 Part I clauses (1), (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Employment SWT uses different statutory fortnightly boundaries, not annual income tax divided by the number of pay periods. `pg-payroll-social` supplies the declaration rule, fortnightly bands, multiple-payment aggregation and remittance process. This individual skill's annual examples cannot replace those withholding calculations. [s. 13 and Sch. 6](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

### 3. Decide whether SWT is final and whether an annual return is needed

An employee with only assessable employment income from which the required tax has been withheld may be exempt from the compulsory annual return. SWT is final only where the statutory no-return conditions apply and the person does not choose to file the permitted return. Other assessable income can bring employment income into annual tax with a credit for SWT already paid. A salary bank deposit alone proves neither gross income nor proper withholding. [ss. 13(5)-(7) and 136](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

IRC can assess a salary-only shortfall even where no ordinary return was required. Fraud or wilful neglect is not protected by an ordinary time limit. A person who is eligible for the salary-only exemption may choose an annual return for excess withholding or the specified donation/election-expense deductions, within the special statutory period or permitted extension. Do not tell a client that a refund claim is prohibited because salary was taxed at source. [s. 136](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

| Filing situation | Timing and conditions | Official source |
|---|---|---|
| Ordinary individual annual return | Within 3 months of tax-year end | [s. 135](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Optional salary-only return under the special provision | Within 1 year after tax-year end or further time allowed in writing | [s. 136(5)-(6)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Salary-only non-fraud shortfall assessment | Normally within 2 years after tax-year end; fraud or wilful neglect can be assessed at any time | [s. 136(2)-(4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Self-assessed annual income-tax payment | Return due date | [s. 137(1)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Non-self-assessed annual tax | Date specified on the IRC notice, not an assumed period after service | [s. 137(3)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |

Do not automatically require an annual return merely because a bank credit says dividend: specified resident dividend withholding is final under the Act. Check the recipient, distribution and final-withholding provision. Ordinary interest, rent and business income require their own source, exemption and credit analysis. A gross final-tax receipt must not be taxed again merely because it appears in the bank reconciliation. [ss. 151, 160-161](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

### 4. Reconcile transaction evidence before tax classification

Descriptions below are prompts to obtain the underlying document, not deterministic legal classifications. Match the actual debit or credit, owner, purpose, tax period and supporting evidence. Remove internal transfers and financing principal from turnover without removing genuine fees or interest. Record unresolved lines in a suspense schedule so no tax item disappears.

| Bank narrative or counterparty cue | Provisional category and evidence required |
|---|---|
| Client name, transfer, deposit, payment received | Possible business receipt; inspect invoice and distinguish loan, capital, reimbursement and own-account transfer |
| Fees, professional fees, consultancy, services | Possible ordinary professional-business income; professional small-business-tax exclusion must be checked |
| Salary, wages, pay, employer name, fortnight/FN | Possible employment net pay; obtain gross pay, benefits, SWT and employee deductions |
| Rent received, rental | Rental/property income, ownership and deductible costs need separate reconciliation |
| Interest, INTERESSI | Investment receipt; obtain gross amount and withholding certificate, identify any final-tax rule |
| Dividend | Identify company, recipient, gross dividend and whether withholding is final |
| IRC refund, tax refund | Reconcile to the tax ledger; an income-tax refund is not sales turnover; registered-business GST refunds are excluded by the GST income-tax rule |
| Government grant, capital grant | Obtain the grant terms and specific tax rule; never exclude an amount solely because the narrative says capital |
| Super withdrawal, Nambawan, Nasfund credit | Obtain the fund's taxable/exempt component and membership record; do not add the entire amount to ordinary wages |
| Internal transfer, own account, between accounts | Match the other owned account; exclude confirmed transfer, not an unidentified third-party receipt |
| Loan receipt or loan principal repayment | Separate principal from interest and fees; principal is financing, not a business expense |
| GST payment, IRC GST | Reconcile the GST liability, not an ordinary deduction for recoverable tax |
| Provisional tax, PT instalment | Reconcile to income-tax credit, never deduct from assessable income |
| Super contribution debit | Identify employee, employer or sole-trader character and approved fund; do not call every fund debit a deductible business expense |

BSP, Kina Bank, Westpac PNG and ANZ PNG are legacy statement labels in the old guide, not verified current account-product descriptions. Read the actual statement layout. Preserve transaction date and value date, narrative, counterparty/reference, debit/credit sign, currency and running balance. Reconcile opening balance plus credits minus debits to closing balance and identify duplicated pages or imports. EFT/TRF means a transfer; DD direct debit; SO standing order; EFTPOS a card transaction; PMV a transport reference. None proves deductibility. Do not assume an exported date format or merchant name contains complete tax evidence.

### 5. Establish assessable income and allowable expenses

Employment is accounted for on the cash basis. Companies, partnerships and individuals registered for GST who account on an invoice basis use accrual accounting; other persons may fall under the permitted cash/accrual provisions. A bank-only schedule is insufficient where accruals are required. Maintain consistent timing and adjustment records rather than reporting only cash movements. [ss. 43-47](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

The ordinary deduction rule requires expenditure incurred in deriving assessable income, subject to specific prohibitions and limitations. Apply that test to every expense and use the statutory capital-allowance rules for assets. No general safe percentage for home, vehicle, phone or internet is stated here. [ss. 29-41](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

| Expense cues retained from the old guide | Required treatment and evidence |
|---|---|
| Office rent, commercial rent | Lease, business premises and period; private/home portion requires supported apportionment |
| Professional indemnity or business insurance | Policy and connection to assessable income; segregate personal cover |
| Accountant, auditor, bookkeeper, CPA or tax agent | Invoice and purpose; tax-agent-fee deduction also requires the registered-provider conditions |
| Lawyer, legal, notary | Distinguish current revenue work from acquisition, title, entity or other capital matters |
| Stationery and office supplies | Business invoice and actual business use, with capital items separately identified |
| Marketing, advertising, Google/Facebook ads | Business campaign and invoice; do not approve a personal charge from its merchant alone |
| Training, course, seminar or conference | Connection to the existing income activity and any private/capital component; entertainment elements require their own test |
| Bank fee, service fee, BSP or Kina charge | Reconcile to the business facility and purpose, separate financing principal |
| Internet, Digicel data, Telikom, hosting or domain | Deduct supported business use only; keep private and capital components separate |
| PNG Power, Water PNG, Eda Ranu, electricity, water | Business-premises cost or evidenced home-business allocation, not a blanket private bill deduction |
| Digicel, bmobile, Vodafone or telephone | Usage evidence and reasonable allocation; unknown use remains pending |
| Air Niugini, PNG Air, flights | Itinerary and business purpose; split a mixed trip rather than claiming all fares |
| Hotel, lodge, guesthouse, booking service | Business travel dates and invoice, excluding private extension |
| Taxi, PMV, hire car | Business journey evidence; ordinary private travel is not converted by a merchant label |
| Fuel, petrol, diesel, Puma or Mobil | Vehicle log and business share; preserve running costs and asset allowance separately |
| Groceries, supermarket, Stop N Shop, RH or personal | Usually private living cost; require actual evidence before treating any part as business stock or allowable staff cost |
| Restaurant, dinner, client meal, entertainment | Statutory restriction with specified exceptions, not an unconditional full business deduction |
| Fine, penalty or infringement | Statutory fines/penalties are disallowed; preserve the underlying event and tax notice |
| IRC income-tax payment or provisional payment | Tax ledger/credit, not a deduction from taxable income |
| Drawings, personal withdrawal or private ATM | Owner movement, not business expense; obtain evidence if the label is ambiguous |

These categories apply the source-connected general deduction and disallowance provisions; they are not a list of automatic merchant-name concessions. [ss. 29-32, 38-41 and 134](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

For a home workspace, keep the actual area/use and basis for allocating rent and utilities. A dedicated room may support an allocation, but no statutory requirement that every mixed room be denied in full is established here. Vehicle running costs need supported business use, with actual log evidence. Phone and internet allocation needs a record of business versus private use. Unknown facts remain pending, not a legal zero-percent default. Capital purchases remain in the asset register until the allowance and eligible basis are established; a second-hand asset is not automatically a full expense.

Entertainment is restricted, but the Act preserves specified exceptions for business/employment travel, ordinary arm's-length hospitality businesses, industrial-award overtime food, prescribed public promotion and qualifying incidental daytime seminar activity, as well as certain employee benefits. Obtain facts and the cited condition before allowing an exception. [s. 31](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf). Registered tax-agent fees need the provider condition in the separate fee provision. [s. 32](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Distinguish employee SWT remitted from the employer's gross wage expense. Income tax itself is not deductible, but gross otherwise-deductible wages are not reduced merely because part was withheld for tax. The Act delays the specified deduction until withheld tax has been paid where required. Do not use the old blanket “never deduct any SWT payment” line to deny the tax component of a legitimate gross wage expense twice. [s. 30(3)-(4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

### 6. Keep GST out of the wrong income-tax line

For a GST-registered person, exclude output tax and refunded GST from assessable income. Do not deduct input GST, or include it in asset cost, to the extent it is recoverable under GST law. Irrecoverable GST forms part of the relevant cost but does not make a capital or private item deductible as a current expense. Apply the underlying revenue/capital and business-purpose tests. [s. 46](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Use `png-gst` for standard-rate classification, temporary household-goods relief, registration and filing-status evidence and the actual G1 return mapping. Unknown registration status must not become “turnover below threshold” by default. GST is a separate return and does not replace the annual income-tax reconciliation.

### 7. Apply dependant credits honestly

The old guide's statement that dependant credits were repealed is incorrect for this Act. A resident maintaining a qualifying dependant may claim the credit subject to relationship, age, income and maintenance conditions. The dependant can be a spouse, an unmarried child under the stated age, a qualifying full-time student child, a medically certified permanently incapacitated child or sibling, or a resident parent of the taxpayer or spouse. Part-year and shared support require reasonable apportionment as determined by IRC. [s. 56](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

| Dependant-credit condition | Amount or rule | Official source |
|---|---|---|
| Child or student | Unmarried child under 16; student child at least 16 but under 25 in full-time education | [s. 56(1)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Invalid relative | At least 16; statutory relationship and Public Service medical-officer certificate of permanent incapacity | [s. 56(1)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Income condition | Dependant taxable income not above PGK 1,040; where subject only to SWT, fortnightly employment income not above PGK 40 | [s. 56(1), Sch. 1 Part II clauses (11), (12)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| One dependant | Lesser of 15% of assessed tax before credits and PGK 450 | [s. 56(2)(a), Sch. 1 Part II clause (8)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Each other dependant | Lesser of 10% of assessed tax before credits and PGK 300 | [s. 56(2)(b), Sch. 1 Part II clause (9)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Aggregate ceiling | Greater of 35% of tax before credits and PGK 1,050; cannot reduce tax below zero and no refund or carry-forward | [s. 56(4), Sch. 1 Part II clause (10)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |

The aggregate wording is “greater”, not “lesser”. Do not restore old minimum-credit amounts or a fixed dependant-count limit absent a current provision. Apply this non-refundable credit before foreign and refundable credits in the statutory order. [ss. 11(5) and 56](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf). Withholding uses its own declaration and annual-credit allocation, not a new independent annual credit for every fortnight.

### 8. Reconcile superannuation and payout components

Use `pg-payroll-social` for standard contribution rates, coverage, the unresolved amended pay-component definition and the conflicting remittance clocks. Do not use the former citizenship-only coverage assumption, exclusion of all commission, or an unverified no-ceiling claim. Employee contributions are not a deduction from the employee's taxable salary or an automatic sole-trader expense. Employer approved-fund contributions have their own deduction conditions and limit. [Income Tax Act s. 117](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Under the payout provision, the part representing previously taxed contributions is exempt. A transfer of an approved-fund lump sum into a retirement savings account with the same or another approved fund is not taxed; prescribed retirement-account withdrawals need their own limit. The remaining payout component has the applicable special rate. A non-approved-fund payout has a separate statutory treatment, so first establish fund status. [s. 119](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

| Approved-fund taxable payout component | Rate and condition | Official source |
|---|---|---|
| Permanent disability or dependant of deceased member | 2% under the specific payout branch | [Sch. 1 Part I clause (12)(a)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Member contributed at least 7 years and is at least 50 or subject to enforced early retirement | 2% under the separate qualifying branch | [Sch. 1 Part I clause (12)(b)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Other payout, contributions at least 15 years | 0% from the 2026 amendment, replacing the principal Act's 2% in clause (12)(c) | [2026 budget amendment s. 4](https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050) |
| Other payout, contribution period at least 9 but below 15 years | Lesser of 8% or the applicable individual rate; exact boundary overlap needs resolution below | [Sch. 1 Part I clause (12)(c)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Other payout, contribution period at least 5 and not greater than 9 years | Lesser of 15% or the applicable individual rate; exact boundary overlap needs resolution below | [Sch. 1 Part I clause (12)(c)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Other payout, contribution period below 5 years | Applicable resident or non-resident individual rates | [Sch. 1 Part I clause (12)(c)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |

The printed table overlaps at exactly nine years. Do not silently choose one branch for that boundary; hold the payout calculation for current statutory/IRC resolution. The budget amendment changes the ordinary long-contribution branch only; it does not replace the separate disability/death and age/early-retirement branches with zero. Ordinary salary, qualifying long-service leave and a superannuation payout are three different bases.

### 9. Compute provisional tax, final credits and the return

The old non-salary-income trigger and single September payment rule must not be used for 2026. Under the new provision, ordinary income taxpayers generally pay instalments; an individual reasonably expecting taxable income below the statutory tax-free threshold is excluded. For calendar-year 2026, the instalments are due on 30 April, 31 July and 2 November. Section 68 moves a tax filing, payment or other due date that falls on a Saturday, Sunday or PNG public holiday to the next business day. The ordinary date of 31 October 2026 fell on a Saturday. [Income Tax Act s. 138](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf); [Tax Administration Act s. 68](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d#page=48).

Each ordinary instalment is **(A - B) / 3**. A is the most recent assessed income-tax liability, including self-assessment, reduced by the foreign tax credit allowed for that year and multiplied by the prescribed regulatory uplift factor. B is the portion of A paid by amounts withheld under Part X. Subtract B before dividing by three, not the whole withholding amount from each third. The current uplift factor has not been confirmed from the Regulation; do not assume it equals unity. A new income taxpayer or one whose most recent return showed a net loss instead uses 2% of the instalment-period assessable income not subject to withholding. A lower/nil estimate requires reasonable grounds, approved-form election by the first instalment date or permitted later date, and the appropriate estimate. An underestimation penalty can apply; it is not an unconditional safe harbour. [s. 138](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf); [TAA s. 98](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d).

Reconcile provisional payments and creditable withholding to actual IRC payments/certificates. Apply non-refundable credits in order, then refundable credits, keeping final withholding outside duplicate annual assessment. Pay self-assessed tax by the return due date. Filing early leaves that payment deadline in place. A taxpayer-specific filing extension leaves the payment deadline and interest rules in place. For a non-self-assessment, read the due date on the assessment notice. Prepare the current authorised IRC return with the supporting schedules and save its acknowledgement and payment reference. No live 2026 form fields or filing extension have been verified here, so the working paper does not pretend to be a completed submitted return. [Income Tax Act s. 137](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf#page=97); [Tax Administration Act s. 14](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d#page=18).

### Working paper retained and corrected

```text
PAPUA NEW GUINEA INDIVIDUAL INCOME TAX, 2026
Client / TIN / period / residence evidence / applicable regime
A Employment: gross cash + taxable benefits; SWT withheld; employee deductions; net-pay reconciliation
B Other income: business sales net of output GST; rent; interest; distributions; exemption/final-tax analysis
C Deductions: premises, insurance, professional and legal, supplies, marketing, training, bank,
  telecom, travel, home and vehicle allocations; capital allowances separately; supported total
D Ordinary taxable income: assessable income less allowable deductions, with losses and timing adjustments
E Annual tax: resident/non-resident marginal computation; dependant credit; foreign credit;
  provisional and creditable withholding; balance or excess credit; payment/return due date
F Super: fund/coverage; verified base; employee deduction; employer cost; actual remittances;
  payout taxable/exempt components and applicable special branch
G Open items: residence, missing gross income, business purpose, GST, fund components, capital allowances,
  small-business eligibility/election, dependants, uplift, source conflicts and actual filing-channel requirements
Evidence references, preparer estimate, unresolved amounts and practitioner sign-off
```

Do not compute net employment income as gross minus SWT alone when employee superannuation or other deductions also affect the bank credit. Do not deduct provisional tax in taxable income and again as a credit. Do not infer all exemptions, GST status or no-return treatment from a matching transaction pattern.

### Income-tax administration

The Income Tax Act's administration clause incorporates the Tax Administration Act 2017, with the cross-reference corrections in the enacted budget amendment. Keep a penalty separate from interest and from the underlying tax. A penalty requires an IRC assessment and notice; remission may be requested. Do not turn these statutory exposures into an automatic debit in a working paper. [Income Tax Act s. 133 and amendment s. 3](https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050); [TAA ss. 39, 93-101](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d).

| Default | Statutory amount and conditions | Official source |
|---|---|---|
| Late filing | Higher of 20% of tax due, or PGK 200 per month or part month for a company and PGK 100 for another person | [TAA s. 93](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Late payment penalty | 20% of unpaid tax, in addition to interest; tax for this purpose excludes penalty and interest | [TAA s. 94](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Late payment interest | Central Bank rediscount rate at the start of the relevant period plus 5 percentage points; simple interest calculated daily, not a fixed annual penalty rate | [TAA s. 39](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Tax shortfall | 100% for deliberate or reckless statements; otherwise 25%, subject to repeat-default increases, timely-disclosure reductions and statutory defences | [TAA s. 95](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Retention | 7 years after the tax period, extended for unexpired amendment periods, unused losses, audits and proceedings | [TAA s. 11](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Objection and review | Objection within 60 days of service; Tribunal review normally within 28 days of service of the reviewable decision; National Court appeal on law within 28 days of notification, with extension powers | [TAA ss. 24-27, 79](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |

Preserve the notice, service date, grounds, return, undisputed-tax payment and disputed-tax payment arrangements. An objection does not itself suspend collection. Obtain current legislation and the actual IRC decision before advising on a dispute, transition or enforcement case. The current rediscount rate and day-count denominator are not supplied here, so no numerical interest estimate is authorised.


### Refusal and referral catalogue

Keep the original refusal topics as explicit controls. Residence unknown means no final rate selection. Companies, trusts and partnerships require their own regimes. Extractive/resource taxable-asset disposals and indirect ownership changes need the capital-gains provisions, statutory asset definition and actual project documents, not a blanket tax on all investments or an unverified beneficial-ownership percentage. Mixed expatriate and foreign-source income needs specialised analysis. Arrears, audit and enforcement require the actual notice and dispute deadlines. GST return work goes to `png-gst`. For 2026 work, apply the new enacted Act rather than asking a reviewer to bless an old-year table. Current minimum wage, levy and unverified depreciation inputs remain held topics, not omitted obligations.

## Worked cases

All figures below are illustrative client inputs in PGK. The annual ordinary-tax cases assume a full-year resident or non-resident, no small-business-tax regime, no part-year adjustment, and no unmentioned exemption or credit. A consulting professional does not enter the small-business regime merely because turnover is modest. Arithmetic should be recomputed by a deterministic engine or checked working paper; do not claim that a live calculator supports this country without testing it.

### Original example 1: salary bank credit

A bank credit of PGK 2,450 described as fortnightly pay is a net-pay reconciliation item. It cannot establish gross pay, SWT or final liability. If payslips and all-income checks establish the statutory salary-only final-tax conditions, keep it outside business turnover. If not, retain a pending item rather than declaring no further tax. This corrects the old unconditional final-tax inference. [ss. 13, 136](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

### Original example 2: GST-inclusive sole-trader receipt

A confirmed registered business receives PGK 1,100 for an ordinary standard-rated invoice, not an exempt or zero-rated supply. Revenue is PGK 1,000 and output GST PGK 100. This calculation does not establish registration from the receipt alone. [s. 46](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf); [IRC GST factsheet](https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf).

```oa-check
name: PNG registered business receipt split
inputs:
  gross_receipt: 1100
steps:
  - net_revenue: gross_receipt / 1.10
  - gst: gross_receipt - net_revenue
expected:
  net_revenue: 1000
  gst: 100
```


### Original example 3: ordinary contributions

A covered employee's independently confirmed base salary is PGK 2,450, not inferred from a net bank deposit. Standard employee and employer contributions are PGK 147 and PGK 205.80. Disputed commissions, exemptions and limits remain for the payroll skill's source-resolution process. [BPNG current contribution notice](https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions).

```oa-check
name: PNG uncontested salary contribution example
inputs:
  base_salary: 2450
steps:
  - employee: base_salary * 0.06
  - employer: base_salary * 0.084
  - combined: employee + employer
expected:
  employee: 147
  employer: 205.8
  combined: 352.8
```


### Original example 4: mixed-use fuel

A fuel payment of PGK 180 has documented business use of sixty percent and qualifies as a revenue running cost. Deductible cost is PGK 108, private cost PGK 72 before any separately established GST adjustment. Without that usage evidence the amount is pending, not a final statutory zero. [ss. 29-30](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG documented mixed-use fuel
inputs:
  fuel_cost: 180
  business_fraction: 0.6
steps:
  - business_cost: fuel_cost * business_fraction
  - private_cost: fuel_cost - business_cost
expected:
  business_cost: 108
  private_cost: 72
```


### Original examples 5 and 6: annual ordinary tax and payment credit

A resident consulting sole trader has assessable business income PGK 120,000, supported allowable deductions PGK 35,000 and no dependant or foreign credit. Ordinary taxable income is PGK 85,000. Tax is PGK 22,850; verified provisional payments of PGK 3,000 leave PGK 19,850. The provisional payment date must come from the actual instalment schedule, not the old September-only rule. [ss. 11-12, 138, Sch. 1 annual bands](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG resident ordinary professional business and provisional credit
inputs:
  assessable_income: 120000
  deductions: 35000
  provisional_paid: 3000
steps:
  - taxable_income: assessable_income - deductions
  - band_two: max(min(taxable_income,33000)-20000,0)*0.30
  - band_three: max(min(taxable_income,70000)-33000,0)*0.35
  - band_four: max(min(taxable_income,250000)-70000,0)*0.40
  - band_five: max(taxable_income-250000,0)*0.42
  - tax: band_two + band_three + band_four + band_five
  - balance: tax - provisional_paid
expected:
  taxable_income: 85000
  tax: 22850
  balance: 19850
```


### Original example 7: internal transfer

A debit of PGK 2,000 is matched to the same owner's other account. Record it as a transfer with the matching reference, not a deduction or a taxable receipt. If the other account or ownership cannot be established, retain it for reconciliation.

### Resident and non-resident annual band regression cases

The old boundary and top-band tests remain, recomputed from the annual statute. These are not fortnightly SWT calculations. [Sch. 1 Part I clauses (1), (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG annual band boundaries and top band
inputs:
  income_at_second: 33000
  income_at_third: 70000
  high_income: 300000
  nonresident_income: 85000
steps:
  - resident_second: (income_at_second - 20000) * 0.30
  - resident_third: 13000 * 0.30 + (income_at_third - 33000) * 0.35
  - resident_high: 13000 * 0.30 + 37000 * 0.35 + 180000 * 0.40 + (high_income - 250000) * 0.42
  - nonresident_tax: 20000 * 0.22 + 13000 * 0.30 + 37000 * 0.35 + (nonresident_income - 70000) * 0.40
expected:
  resident_second: 3900
  resident_third: 16850
  resident_high: 109850
  nonresident_tax: 27250
```


### Dependant credit, three verified eligible dependants

A full-year resident has pre-credit assessed tax of PGK 3,900 and maintains three dependants who meet every statutory relationship, income and maintenance condition, with no shared/part-year adjustment. Credits are PGK 450, PGK 300 and PGK 300. The greater-of aggregate ceiling is PGK 1,365, so the PGK 1,050 sum is allowed and tax after this credit is PGK 2,850. No refundable payment credit is included in this case. [s. 56, Sch. 1 Part II](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG annual dependant credit not repealed
inputs:
  tax_before_credits: 3900
steps:
  - first: min(tax_before_credits * 0.15,450)
  - second: min(tax_before_credits * 0.10,300)
  - third: min(tax_before_credits * 0.10,300)
  - ceiling: max(tax_before_credits * 0.35,1050)
  - credit: min(first + second + third,ceiling,tax_before_credits)
  - tax_after_credit: tax_before_credits - credit
expected:
  ceiling: 1365
  credit: 1050
  tax_after_credit: 2850
```


### Other approved-fund payout after the required contribution period

An ordinary clause (12)(c) payout is confirmed, the member has at least the statutory long contribution period, and the taxable component after exempt taxed contributions is PGK 40,000. The amended rate gives nil tax on that component. This is not the separate disability/death or early-retirement branch and does not resolve the exact-nine-year overlap. [2026 Budget amendment s. 4](https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050).

```oa-check
name: PNG amended ordinary long-contribution payout
inputs:
  taxable_component: 40000
steps:
  - payout_tax: taxable_component * 0
expected:
  payout_tax: 0
```


### Ordinary provisional instalment order

Assume A, already calculated after the allowed foreign credit and the actual prescribed uplift, is PGK 9,000. B, the portion of A paid by Part X withholding, is PGK 3,000. Each ordinary instalment is PGK 2,000. These are supplied illustrative A/B inputs; the example does not assume the unread current uplift factor. [s. 138(4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG provisional withholding subtracted before division
inputs:
  assessed_after_credit_and_uplift: 9000
  amount_of_A_paid_by_withholding: 3000
steps:
  - instalment: (assessed_after_credit_and_uplift - amount_of_A_paid_by_withholding) / 3
expected:
  instalment: 2000
```

## When to refuse or refer

Stop finalisation on any missing input or held legal rule that changes the outcome. Preserve all unknown amounts and documents in the open-items schedule. Refer resource gains, capital allowances not established, foreign/treaty cases, the exact-nine-year payout overlap, disputed fund coverage and any audit/arrears position. Do not use a confident model answer, a historical bank pattern or an accountant's name in an old credit line as professional approval.

## Sources

Read on the dates below. A scoped read does not certify every provision in a long Act.

| Official source and scope read | URL | Read on |
|---|---|---|
| Read for Finance Department FMM 03.7, current fiscal-year designation, whole one-page instruction | https://www.finance.gov.pg/wp-content/uploads/2026/04/FMM-03-07-Financial-Fiscal-Year.pdf | 2026-11-16 |
| Read for Income Tax Act 2025: ss. 7-14, 18-25, 29-56, 66-71, 117-119, 132-160, 163-165 and schedules; scoped to the rules above, rate tables visually inspected | https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf | 2026-11-23 |
| Read for Certified Income Tax 2026 Budget amendment: commencement, administration cross-references and payout-rate replacement | https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050 | 2026-11-16 |
| Read for Tax Administration Act 2017: extension, business-day, record, amendment, dispute, interest and administrative-penalty provisions, as incorporated for income tax | https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d | 2026-11-23 |
| Read for BPNG contribution notice: standard rates and coverage read through official web text; amended component rules not certified | https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions | 2026-11-16 |
| Read for IRC GST factsheet: standard-rate arithmetic and GST accounting mechanism | https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf | 2026-11-16 |

Not yet confirmed: Current GST registration threshold text needed for small-business eligibility; provisional-tax uplift Regulation; live small-business return form; live 2026 annual return fields and any extensions; current minimum-wage determination, levy status, capital-allowance rates for a particular asset; exact-nine-year fund-table overlap; amended superannuation base/ceilings and deduction-remittance clock; current interest input. The 2025 tax regime and every benefit valuation are not certified by this 2026 scoped read.
