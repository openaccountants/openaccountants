---
name: kh-income-tax
description: >
  Compute Cambodia monthly Tax on Salary for residents and non-residents and
  basic annual Tax on Income for physical persons in 2026. Covers residence,
  salary-base adjustments, dependent relief, fringe benefits, annual bands,
  prepayments, filing and review boundaries. Use for Cambodia salary tax, TOS,
  personal income tax, sole-proprietor TOI and payroll withholding. NSSF current
  wage-table and full special-regime calculations require separate confirmation.
jurisdiction: KH
category: international
type: computation
tax_year: 2026
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 0.3
---

# Cambodia Income Tax: Salary and Physical-Person Business Income v0.3

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

The tax authority is the General Department of Taxation (GDT), Ministry of Economy and Finance. Prepare a KHR working paper distinguishing monthly employment Tax on Salary(TOS), separate fringe-benefit tax and annual business/professional Tax on Income(TOI) for a physical person, sole proprietorship or relevant partnership share. Do not combine these different bases merely because their progressive rates match. A bank/payroll descriptor is an intake clue. Legal-person company tax routes to [corporate income tax](kh-corporate-income-tax.md); VAT routes to [Cambodia VAT](cambodia-vat.md); social-security assessment routes to [payroll/social](kh-payroll-social.md). The Khmer legislation prevails.

The current instrument is **Sub-Decree 48 of 11 March 2024**, read with the 2023 Law and **Prakas 575 of 19 September 2024**. The GDT register lists old Sub-Decree 196 of 28 September 2022 as abrogated; do not call it the current 2026 instrument. The band amounts below are confirmed by the replacement, rather than guessed from the old citation.

| Quick reference | Amount / rule and complete population | Source |
|---|---|---|
| Resident salary | Monthly worldwide salary; progressive 0%to 20% after lawful base adjustments | [Law 41-47](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [SD48 arts 1-3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35); [Prakas575,12-14](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |
| Non-resident salary | 20% final salary tax on Cambodian-source taxable salary, with the technical-assistance source rule; fringe benefits separate; no resident dependent relief | [Law 42(6),46(3),49](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575,3,5,14](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |
| Fringe benefits | 20% of fair-market value inclusive of all taxes, employer withholding/payment obligation; test exemptions and value before applying | [Law 48](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575,15-18](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |
| Dependent relief | KHR 150,000 per qualifying child and KHR 150,000 for the qualifying non-working spouse per month; resident salary only, evidence required; where both spouses work, child relief is granted to only one spouse | [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35); [Prakas575,12-13](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |
| Child age / transition | Age no more than 14; or no more than 25 and full-time study at a recognized institution, with required evidence. Retain relief in the specified month of reaching 15, finishing studies or reaching 26 | [Prakas575,13](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |
| Monthly filing | Statutory 20th of following month; actual electronic calendar may differ | [Law 53](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575,22](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |
| Annual business year / filing | Calendar year baseline; annual return/payment within 3 months after year-end, including loss return; approved alternative-year rules separate | [Law 8,29-30,39](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| Monthly TOI prepayment | 1% of previous-month turnover including all taxes except VAT, within self-assessment liability; credit, not expense; check actual incentives/suspensions | [Law 28,32,38-39](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### Resident monthly salary bands

Each rate applies only to its tranche of the confirmed resident monthly taxable base. Cumulative amounts are **derived**, not an official quick-deduction column. Source: [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) and [Prakas575,14](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70).

| Taxable monthly base KHR | Rate | Derived cumulative tax at upper limit KHR | Official source |
|---|---|---|---|
| 0 to 1,500,000 | 0% | 0 | [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| 1,500,001 to 2,000,000 | 5% | 25,000 | [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| 2,000,001 to 8,500,000 | 10% | 675,000 | [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| 8,500,001 to 12,500,000 | 15% | 1,275,000 | [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| Above 12,500,000 | 20% | No upper limit | [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |

### Annual physical-person business-income bands

Apply to annual taxable income of the physical-person/sole-proprietor or distributive partnership-share population specified in SD48; not the ordinary legal-person corporate rate. Cumulative figures are derived.

| Annual taxable base KHR | Rate | Derived cumulative tax at upper limit KHR | Official source |
|---|---|---|---|
| 0 to 18,000,000 | 0% | 0 | [SD48 art 4](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| 18,000,001 to 24,000,000 | 5% | 300,000 | [SD48 art 4](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| 24,000,001 to 102,000,000 | 10% | 8,100,000 | [SD48 art 4](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| 102,000,001 to 150,000,000 | 15% | 15,300,000 | [SD48 art 4](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| Above 150,000,000 | 20% | No upper limit | [SD48 art 4](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |

## Ask the client first

Obtain actual employment/business facts, legal form, residence evidence, domicile/principal abode and arrival/departure day records; actual month/year, payment dates and all payers; gross pay, cash allowances/bonus/overtime, advances/loans and repayments; foreign salary/tax certificates; documented exempt reimbursements; fringe-benefit register and valuation; family, birth/study and spouse-income evidence; mandatory withholding required by labour/social-security law; actual NSSF assessment, registration and employee headcount as an intake fact; currency/rate instruction; payroll register, prior returns/acknowledgments and payment receipts.

For TOI obtain complete income/expense books and invoices, taxpayer classification, turnover, deductible-expense reconciliation, related-party/private/capital items, losses, proper-accounting/minimum-tax status and prepayment receipts. A full-year bank statement starts reconciliation; it does not establish taxable profit or expense deductions. Missing salary or residence means stop TOS; missing business income/base or classification means stop TOI. Identify mixed TOS/TOI facts instead of guessing.

## The method, step by step

### Establish residence, employment and source

[Law 41-42](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) and [Prakas575,3-5](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) use residence/domicile, principal place of abode or presence **more than 182 days in a 12-month period ending in the current tax year**; review all independent residence limbs, not day count alone. Non-residents are outside the resident definition and receive Cambodian-source salary. Cambodian source generally follows employment activities in Cambodia, but a non-resident's technical-assistance salary follows payer residence. Prakas575 art 5(3) separately excepts specified technical-assistance/other-services salary where the payer has no Cambodian PE or fixed base and the salary is not borne by a Cambodian PE or fixed base. Establish both conditions and refer the actual technical/service arrangement; a foreign payer alone does not resolve taxation. Count any part of a day as 1 full day and aggregate one or multiple stays under Prakas575 art 5(1)(c). If domicile and principal abode cannot be determined, apply the presence test under [Prakas 575 art 5(1)](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70). Apply the factual residence provisions; border cases, dual residence and treaties require referral.

Prakas 575 art 4 treats a person as an employee subject to salary tax where 2 of its conditions are met: no risk of non-payment after attending the specified workplace and performing the agreed work; inability to set their own work time and place; no need to invest capital to buy work equipment; and not working for multiple persons simultaneously. Apply those actual facts rather than the word “consultant.” The employee definition excludes National Assembly and Senate members; refer that special population. Salary includes direct/indirect cash and in-kind remuneration, indemnity, bonus and overtime. Classify benefits separately under arts 15-18 and genuine salary exemptions under arts 8-11; do not tax every unexplained payment as a benefit automatically.

### Build resident salary base before the bands

[Law 44-46](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) controls the base: exclude separately taxed fringe benefits, deduct mandatory withholding required by labour and social-security law, and apply confirmed exempt payments. Then apply evidenced resident dependent relief. Prakas 575 art 12 details family relief and the treatment of employer advances/loans/installments and repayments; it does not erase the statutory deduction in Law 45. Do not subtract an assumed current NSSF maximum. Use the actual legally required withholding amount and retain its separate assessment evidence.

Law 44/Prakas 575 art 8 exempt genuine business-expense reimbursement only under employer instructions, for the direct/exclusive employer interest, with a reasonable amount and already-paid detailed invoices in the reimbursement recipient's name; termination indemnities, pension/social-welfare remuneration and specific professional uniform/equipment/travel allowances have their own labour-law and implementing conditions. Uniforms must be necessary for work and supplied uniformly to employees in the same role; uniforms/equipment must be returned when employment ends (art 8(4)). Mission/travel lump sums replace actual reimbursement, cannot duplicate it and cannot exceed the government allowance for equivalent work (art 8(5)). Diplomatic/consular exemptions require art 9 official-function, passport and reciprocity conditions; art 10 international-organization relief has its headquarters-hired staff scope. These special applications are held for a complete document-specific review here. For art 11 technical-cooperation relief, the MEF-approved project documents must identify the technical-assistance staff. Resident administrative/helper staff remain taxable. A contractor must keep clear staff/work records separating the approved project from non-project work and other staff. Not every foreign employee qualifies.

Under Law 46/Prakas 575 art 12, employer advances, loans or installments enter taxable salary when paid; repayment reduces that month's taxable salary within the prescribed limits, with loan principal distinguished from interest. Retain separate schedules; do not net an entire loan balance against annual pay.

Dependent relief needs the actual family situation. Prakas 575 art 13 requires birth/supporting documents and recognized full-time study proof for the older child population; GDT can reject false study certificates. The old “under 14/under 25” wording excludes the ages the current rule includes. Claim qualifying children through the specified birthday/completion transition month, and grant child relief to only one spouse where both spouses work, without splitting different children between them. Relief does not apply to non-resident salary, fringe-benefit tax or annual TOI.

Apply the monthly marginal bands mechanically without intermediate hand-rounding; record the final rounding instruction used. An official quick-deduction column is not confirmed here: do not present derived cumulative figures as that column. For foreign-currency salary use the National Bank of Cambodia rate on the 15th of the month. If there is no rate on that day, use the closest preceding published rate. Record the rate and publication date. [GDT Instruction 26118, point 2](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/07e6ee8b-8a9d-49ab-8c4e-d092b061613f), [GDT exchange rates](https://www.tax.gov.kh/en/exchange-rate).

### Non-resident salary and benefits

Apply [Law 49](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e)/Prakas 575 art 14 to confirmed Cambodian-source taxable salary:20%final salary tax, no resident bands/dependents. Do not automatically deduct a resident-only base adjustment for a non-resident. Keep NSSF/other payroll liabilities separate and establish actual coverage.

[Law 48](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) and [Prakas575,15-18](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) impose 20%on fringe-benefit value inclusive of taxes with employer withholding/payment. Benefits can include private vehicles, food, housing, utilities, domestic help, below-market loans, discounts, personal education/children's school fees, non-uniform insurance, unreasonable or unnecessary employer costs, social-welfare contributions above the legal limit and pension-fund contributions above 10% of monthly salary excluding fringe benefits under [Prakas 575 art 15(2)](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70), and other listed benefits. Unconfirmed cash-benefit thresholds and special valuation rules are held for separate confirmation; the list and exceptions govern. Necessary work transport/accommodation/meals supplied to all employees regardless of role are excluded under art 16. Uniform benefit-insurance and employment-training/business-need exceptions must be tested before applying tax. Art 18 requires market value and taxes the benefit in the month provided, regardless of when it becomes an employer expense; below-market loan interest needs the prescribed market rate. Unknown valuation or exemption means hold and refer, not automatic 20%classification.

For resident foreign salary, [Law 50](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e)/Prakas 575 arts 19-20 determine the foreign credit annually, excluding separately taxed benefits, and require all-source salary in the computation, certified foreign tax and a per-country credit equal to the lower of actual foreign salary tax paid in that country and same-period all-source Cambodian salary tax multiplied by that country's salary divided by all-source salary, plus procedural/employer/tax-authority documents and certified translations of documents not in Khmer or English. This skill does not complete a treaty or foreign-credit application; route R-KH-3 rather than omit foreign salary silently.

### Annual physical-person TOI and credits

[Law 4-11,19-20,28-39](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) and [SD48 art 4](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) govern the ordinary outline. A sole proprietorship is owned by a physical person; husband, wife and dependent children form the specified physical-person unit for this tax definition. Determine the actual taxable business base from books, recognizing taxable receipts and deducting only substantiated business costs under the law. Owner drawings/private living costs, income tax and unsupported costs do not become deductions because they left a business bank account. Capital/depreciation, interest limits, related-party sale/exchange losses, loss eligibility and specific penalty deductibility need their actual detailed rules; do not assume every pattern is deductible.

Apply the annual bands to the established base, then reconcile verified prepayments/withholding and any minimum-tax exposure in the statutory order. Proper-accounting and classification conditions matter; a taxpayer's ordinary annual burden can be higher than progressive TOI if minimum tax applies. Minimum tax is not an unrestricted extra credit against TOI. The simple annual example below assumes minimum tax does not apply and no special credit/incentive/loss. A negative balance goes to the lawful refund/carryforward process, not a guaranteed cash refund. Current Prakas 578 details/classification thresholds and special small-taxpayer calculations are not computed here. The 2023 Law has 3 self-assessment classes; do not revive an estimated regime as current merely from the old text.

### Filing and the review working paper

Withhold at payment and retain employee identity, salary and benefit detail, family and adjustment evidence and accounting records. Report amounts withheld to the employee and GDT. Apply the foreign-employer representative and joint responsibility rules in [Law arts 51-53](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e). Monthly tax is due by the 20th under the statute. October 2026 manual returns were due 20 November. [GDT Notice 40235](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/7219e6f1-3fc4-4f90-811c-ef6f995a735f) extended online filing and payment to **27 November 2026**. Use the published notice for each later period and channel. Annual calendar-year 2026 TOI has a 31 March 2027 baseline, subject to later notices. Track NSSF deadlines separately.

Working-paper cover: tax year, month, employee, residence and contract currency with conversion rate/source. Working paper: A 1 base salary+A 2 taxable cash allowances/bonus=A 3 gross; separate advances/repayments and exemptions; B 1 mandatory statutory withholding; B 2 qualifying spouse relief+B 3 child relief; Cconfirmed resident taxable base; Dresident marginal or non-resident final salary tax; Eseparate fringe-benefit value/tax; Factual employee contribution/other deductions; Gnet cash pay=A 3 less employee deductions and salary tax, avoiding a second cash deduction for an amount already withheld. Annual schedule records turnover, tax-adjusted expenses/base, annual band tax, minimum-tax status, receipts-backed credits and balance. Preserve separate NSSF employer/employee records. Explicit reviewer checklist: residence; documented currency conversion; dependent proof; benefit scope/value and tax; NSSF registration and scheme phase; sole-proprietor taxpayer classification; and prepayment credits matched to receipts.

### Payment patterns and statement reading

These are preserved search prompts, not a deterministic classifier or proof of deductibility/residence/registration. Inspect actual documents, underlying invoices and currency. A refund, transfer or wallet descriptor can conceal a different transaction.

### 1 Income / Salary Patterns (Credits)

**Income/salary patterns table**

| Pattern | Regime / Line | Treatment | Notes | Source / condition |
| --- | --- | --- | --- | --- |
| SALARY, PAYROLL, BROAS (ប្រាក់ខែ), WAGE, EMPLOYER [name] | TOS tax base | Employment income | Apply resident brackets or non-resident 20% per status  | [Law arts 7,11,19,40-54](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| ALLOWANCE (cash, taxable), OVERTIME, BONUS (cash) | TOS tax base | Add to monthly taxable salary | Cash allowances/bonuses are part of the TOS base  | [Law arts 7,11,19,40-54](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| FRINGE BENEFIT, HOUSING PROVIDED, CAR PROVIDED, SCHOOL FEES PAID | Fringe benefit | Test fringe-benefit scope/valuation/exemption | Separate eligible fringe benefits from salary; Prakas575 exclusions and value rules apply  | [Law arts 7,11,19,40-54](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| CLIENT PAYMENT, INVOICE, PROFESSIONAL FEES, CONSULTANCY (sole proprietor) | TOI turnover | Business income | Feeds annual TOI + 1% monthly prepayment base  | [Law arts 7,11,19,28,38-39](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| STRIPE / PAYPAL / WISE PAYOUT (sole proprietor) | TOI turnover | Business income | Match to underlying invoices  | [Law arts 7,11,19,28,38-39](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| TAX REFUND, GDT REFUND | Tax recovery | Hold/reconcile tax nature | A profit-tax refund is not sales income; establish the actual tax/recovery | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| INTEREST RECEIVED, DIVIDEND | OUT OF SCOPE | Flag | Investment income ; separate withholding rules; escalate  | [Law arts 7,11,19,40-54](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |

### 2 Expense Patterns (Sole-Proprietor Debits) / Potential business expense; substantiate against TOI

**Expense patterns table**

| Pattern | Category | Treatment | Notes | Source / condition |
| --- | --- | --- | --- | --- |
| OFFICE RENT, KIRI (ការជួល), SHOP RENT | Premises rent | Potential business expense; substantiate | Business premises only  | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| ACCOUNTANT, AUDITOR, BOOKKEEP, LEGAL (business) | Professional fees | Potential business expense; substantiate | Business-related  | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| SUPPLIES, STATIONERY, INVENTORY, STOCK PURCHASE | Cost of goods / supplies | Potential business expense; substantiate | Trading inputs  | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| MARKETING, FACEBOOK ADS, GOOGLE ADS | Advertising | Potential business expense; substantiate |   | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| UTILITIES (business premises), EDC ELECTRICITY, WATER | Utilities | Potential business expense; substantiate | Business premises; apportion if mixed  | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| BANK FEE, ABA CHARGE, ACLEDA CHARGE, WING FEE | Bank/transfer charges | Potential business expense; substantiate | Business account  | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| SOFTWARE SUBSCRIPTION, SAAS | Software | Potential business expense; substantiate | Recurring operating expense  | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |

### 3 Statutory Withholdings / Contributions (Debits)

**Statutory withholdings table**

| Pattern | Category | Treatment | Notes | Source / condition |
| --- | --- | --- | --- | --- |
| NSSF, SOCIAL SECURITY FUND | NSSF contribution | See NSSF boundary below | Obtain actual period-specific NSSF assessment; no current ceiling confirmed  | NSSF boundary; no current rate/base confirmed here |
| TOS PAYMENT, SALARY TAX, GDT TOS | TOS remittance | Liability payment | Statutory 20th; check actual period/channel calendar  | [Law arts 7,11,19,40-54](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| TOI PREPAYMENT, 1% TURNOVER TAX | TOI monthly prepayment | Credit vs annual TOI | Not an expense ; creditable  | [Law arts 7,11,19,28,38-39](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| VAT PAYMENT, GDT VAT | EXCLUDE | Out of scope | Separate regime  | [Law arts 7,11,19,40-54](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |

### 4 Excluded or unresolved deductions

**Excluded or unresolved deduction patterns**

| Pattern | Treatment | Notes | Source / condition |
| --- | --- | --- | --- |
| OWNER DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | EXCLUDE | Not a business expense  | [Law arts 7,11,19,40-54](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| FINE, PENALTY, GDT PENALTY | Hold deduction pending confirmation | Establish actual tax deductibility; current specific rule not confirmed here  | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| INCOME TAX, TOI PAYMENT (final) | Not deductible | Tax on income  | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Own-account movement  | [Law arts 7,11,19,40-54](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |
| PERSONAL GROCERIES, RESTAURANT (personal) | Not deductible | Private living cost  | [Law arts 7,11,19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); actual transaction controls |

### 5 Cambodian Banks / Wallets / Statement Format Reference

**Banks/wallets statement format reference table**

| Provider | Common patterns | Notes | Source / condition |
| --- | --- | --- | --- |
| ABA Bank | TRANSFER, PAYWAY, QR PAYMENT, CHARGE | App/CSV export; USD and KHR accounts common  | Illustrative original workflow; inspect actual bank export |
| ACLEDA Bank | TRANSFER, ACLEDA UNITY, FEE | PDF/CSV; dual-currency  | Illustrative original workflow; inspect actual bank export |
| Wing (WingMoney) | CASH IN, CASH OUT, TRANSFER | Mobile wallet; many micro-payments  | Illustrative original workflow; inspect actual bank export |
| Canadia / Vattanac | TRANSFER, STANDING ORDER, CHARGE | PDF statements  | Illustrative original workflow; inspect actual bank export |
| Bakong / KHQR | QR PAYMENT, BAKONG TRANSFER | National QR rail; counterparty in reference  | Illustrative original workflow; inspect actual bank export |


### Khmer terms and bank-format clues



**Key Khmer terms table**

| Term (Khmer / translit) | English | Classification hint |
| --- | --- | --- |
| ប្រាក់ខែ / BROAS KHE | Monthly salary | TOS tax base |
| ការជួល / KIRI | Rent | Business expense (premises) or personal |
| ពន្ធ / PUNH | Tax | TOS/TOI remittance ; not an expense |
| ផ្ទេរ / PHTOR / TRANSFER | Transfer | Check direction for income/expense |
| សោហ៊ុយ / SOHUY / CHARGE | Fee / charge | Bank charge; verify business/tax conditions |
| NSSF / បេឡាជាតិ | Social security | NSSF contribution (NSSF boundary) |
| ប្រាក់រង្វាន់ / BONUS | Bonus | Cash bonus → TOS base |



Actual bank exports control: ABA Bank app/CSV/PDF may show date, description, amount,currency,balance and PayWay/KHQR references; ACLEDA Bank exports may show particulars/debit/credit and bilingual currency data; Wing(WingMoney)cash-in/out and micro-payments need underlying facts; Canadia/Vattanac standing orders and Bakong/KHQRreferences need tracing. These are illustrative old format clues, not current bank-interface guarantees.

| Original provider | Illustrative format | Illustrative exported fields, subject to actual file |
|---|---|---|
| ABA Bank | App / CSV / PDF | Date, Description, Amount, Currency, Balance |
| ACLEDA Bank | PDF / CSV | Date, Particulars, Debit, Credit, Balance |
| Wing (WingMoney) | App / CSV | Date, Type (Cash In/Out), Amount |
| Canadia / Vattanac | PDF | Date, Description, Withdrawal, Deposit |
| Bakong / KHQR | App | Date, Counterparty, Amount, Reference |

## Boundary and exception table

| Situation | Action |
|---|---|
| Residence/regime/base missing | Stop affected calculation; obtain facts, not a default residence or band. |
| Unproved dependent | No relief claimed until proof; retain the pending claim for review. |
| Unexplained personal benefit | Hold nature/value/exemption; do not automatically assess fringe tax. |
| NSSF coverage/contributory wage/phase unknown | Obtain registration and actual period assessment. Do not infer registration from employee count or apply the old ceiling. |
| Mixed/private business cost | Withhold the deduction pending documented lawful apportionment. |
| Current small-taxpayer regime/classification | Confirm current GDT classification and detailed method; R-KH-4. |
| USD contract | Obtain official conversion basis and actual monthly rate. |
| Arrears/assessment/penalties | R-KH-5; no penalty calculation from the old percentage table. |

### NSSF and minimum-wage boundary

NSSF assessment and sector wage compliance remain part of payroll intake, but the current contribution-wage table and transition instruments have not been recovered. **No usable current ceiling/floor or automatic NSSF calculation is supplied here.** Do not charge employer-only health/risk contributions to the employee or turn a historical ceiling into a 2026 default. Confirm the actual registration, worker coverage, scheme/phase, base, employer/employee shares, contributions and reporting/payment dates in the separate payroll working paper. The old 8 employees/45 days assumption is not a current instruction. The pension schedule is a scheme-phase question, not automatically each worker's individual tenure.

For covered textile, garment, footwear, travel-goods and bag production, [Prakas 214/25 arts 1–4](https://mlvt.gov.kh/index.php/en/official-docs/prakas/51-%E1%9E%9F%E1%9F%81%E1%9E%85%E1%9E%80%E1%9F%92%E1%9E%8A%E1%9E%B8%E1%9E%87%E1%9E%BC%E1%9E%93%E1%9E%8A%E1%9F%86%E1%9E%8E%E1%9E%B9%E1%9E%84-%E1%9E%9F%E1%9F%81%E1%9E%85%E1%9E%80%E1%9F%92%E1%9E%8A%E1%9E%B8%E1%9E%8E%E1%9F%82%E1%9E%93%E1%9E%B6%E1%9F%86/download/1699_c948ae737b36d7f517973537b499d4ae.html) sets the 2026 minimum at USD 208 per month on probation and USD 210 after probation, effective 1 January 2026. Employers must top up piece-rate wages below the applicable minimum. Check other sector-specific benefits and employee eligibility separately.

## Worked cases

All amounts are hypothetical KHR inputs or derived. Original employer/supplier identities and historical transaction strings are retained; the old March-June 2025 dates are scenario provenance, not newly validated current filing periods. The original 31 April/31 June are invalid calendar dates and must be corrected from source documents before posting. Current examples below apply the confirmed 2026 salary/annual rules to those amounts; any mandatory contribution 24,000 is an **assumed documented input**, never a computed current maximum.

| Original scenario / identity | Inputs | Derived result under stated assumptions | Source |
|---|---|---|---|
| 31/03/2025; ABA PAYROLL; EMPLOYER SOKHA TRADING CO; SALARY MAR | Gross 6,000,000; resident; no dependents; documented mandatory withholding 24,000 | Base 5,976,000; TOS 422,600; cash 5,553,400 | [Law 45-47](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| 31/04/2025; ACLEDA PAYROLL; GARMENT FACTORY KH; WAGE APR | Gross 1,200,000; resident; assumed required withholding 24,000 | Base 1,176,000; TOS 0; cash 1,176,000; invalid date held | [Law 45-47](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| 31/05/2025; ABA PAYROLL; MEKONG LOGISTICS; SALARY MAY | Gross 10,000,000; qualifying spouse+2 children; documented withholding 24,000 | Relief 450,000; base 9,526,000; TOS 828,900; cash 9,147,100 | [Law 45-47](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| 31/06/2025; CANADIA PAYROLL; INTL CONSULTING SARL; SALARY(NON-RESIDENT) | Cambodian-source taxable salary 8,000,000; no fringe benefit | TOS 1,600,000 final; cash 6,400,000 before separately determined contributions; invalid date held | [Law 49](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| 30/06/2025; ABA TRANSFER; LANDLORD / STAFF HOUSING; HOUSING PROVIDED TO MANAGER | Confirmed taxable private housing, fair-market value inclusive of taxes 2,000,000; no exemption | Fringe-benefit tax 400,000 paid and borne by employer as a scenario assumption, separate from employee TOS | [Law 48](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575,16-18](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |
| FY 2025; sole proprietor(real regime) | Scenario taxable business income 60,000,000; eligible prepayments 1,500,000; assume no minimum-tax/special-credit exposure | Annual tax 3,900,000; balance 2,400,000; verify actual period/classification before filing | [SD48 art 4](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35); [Law 28,38-39](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

```oa-check
name: Resident salary after documented mandatory withholding
inputs:
  gross: 6000000
  statutory_withholding: 24000
steps:
  base: gross - statutory_withholding
  tax: 500000 * 0.05 + (base - 2000000) * 0.10
  cash: gross - statutory_withholding - tax
expected:
  base: 5976000
  tax: 422600
  cash: 5553400
```

```oa-check
name: Family relief plus required withholding
inputs:
  gross: 10000000
  statutory_withholding: 24000
  children: 2
steps:
  relief: (children + 1) * 150000
  base: gross - statutory_withholding - relief
  tax: 675000 + (base - 8500000) * 0.15
  cash: gross - statutory_withholding - tax
expected:
  relief: 450000
  base: 9526000
  tax: 828900
  cash: 9147100
```

```oa-check
name: Physical-person annual bands and prepayment credit
inputs:
  taxable_income: 60000000
  prepayments: 1500000
steps:
  first_taxed_band: (24000000 - 18000000) * 0.05
  next_band: (taxable_income - 24000000) * 0.10
  tax: first_taxed_band + next_band
  balance: tax - prepayments
expected:
  first_taxed_band: 300000
  tax: 3900000
  balance: 2400000
```

```oa-check
name: Non-resident final salary and separate employer benefit
inputs:
  nonresident_taxable_salary: 8000000
  taxable_benefit_value: 2000000
steps:
  final_salary_tax: nonresident_taxable_salary * 0.20
  cash_before_other_deductions: nonresident_taxable_salary - final_salary_tax
  employer_benefit_tax: taxable_benefit_value * 0.20
expected:
  final_salary_tax: 1600000
  cash_before_other_deductions: 6400000
  employer_benefit_tax: 400000
```

## When to refuse or refer

- **R-KH-1:** Residence unknown or marginal; obtain domicile/abode/day-count evidence before choosing resident/non-resident treatment.
- **R-KH-2:** Corporate/legal-person TOI, QIP or company minimum-tax special application: route corporate skill and qualified review.
- **R-KH-3:** Cross-border treaty/non-resident payments/PE/foreign-credit application: specialist analysis; preserve all-source salary facts.
- **R-KH-4:** Unconfirmed current small-taxpayer classification or special method: confirm GDT regime; obsolete estimated-regime wording is not current law.
- **R-KH-5:** Arrears, reassessment or enforcement: refer with actual notices. Do not reuse the old penalty category assignments.
- **R-KH-6:** VAT: separate skill. NSSF and labour minimum-wage questions need their own confirmed instruments/period.

On incomplete onboarding, produce a visibly pending working paper, not a completed tax bill. Questions cover each employee's residence, currency/conversion, spouse/children/study proof, benefit type/value, NSSF registration/assessment, sole-proprietor turnover/classification, prepayment receipts and any enforcement notices. Do not allow missing documentation to become a legal assumption.

## Sources

| Source | URL | Read for; actual date |
|---|---|---|
| Law 2023,original Khmer pages 3-24 and 77-78; corresponding English reference operative income/salary provisions and enforcement passages read separately | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e | Residence/base/business outline, salary 41-54, base 45, nonresident 49, benefits 48, foreigncredit 50, payment/records; original salary 20-24 read 2026-11-15; original corporate 3-19 and 77-78 read 2026-11-14 |
| SD48,11 March 2024 | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35 | Original Khmer pages 2-3, salary bands/relief and annual bands/abrogation;2026-11-14 |
| Prakas575,19 September 2024 | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70 | All 10 original Khmer pages visually read, salary definitions/employee tests/residence/exemptions/base/child/benefits/credits/filing; OCRassisted clauses 12-14 compared to images;2026-11-15 |
| GDT registers | https://www.tax.gov.kh/en/sub-decree | SD48 valid/196 abrogated;2026-11-14. Prakas 575 valid at https://www.tax.gov.kh/en/prakas read 2026-11-15 |
| GDT calendar | https://www.tax.gov.kh/en/ | October 2026 manual date, 2026-11-22 |
| GDT Notice 40235 | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/7219e6f1-3fc4-4f90-811c-ef6f995a735f | October 2026 e-filing and payment extension, 2026-11-22 |
| GDT Instruction 26118 | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/07e6ee8b-8a9d-49ab-8c4e-d092b061613f | Point 2, salary conversion rate, 2026-11-22 |
| MLVT Prakas 214/25 | https://mlvt.gov.kh/index.php/en/official-docs/prakas/51-%E1%9E%9F%E1%9F%81%E1%9E%85%E1%9E%80%E1%9F%92%E1%9E%8A%E1%9E%B8%E1%9E%87%E1%9E%BC%E1%9E%93%E1%9E%8A%E1%9F%86%E1%9E%8E%E1%9E%B9%E1%9E%84-%E1%9E%9F%E1%9F%81%E1%9E%85%E1%9E%80%E1%9F%92%E1%9E%8A%E1%9E%B8%E1%9E%8E%E1%9F%82%E1%9E%93%E1%9E%B6%E1%9F%86/download/1699_c948ae737b36d7f517973537b499d4ae.html | Arts 1–4, 2026 covered-sector minimum wages, 2026-11-22 |

The [English reference translation](https://embindpp.gov.in/pdf/menu/Tax-Law-Cambodia-2023.pdf) was read 2026-11-14 for the specified law passages; it is an unofficial reference hosted by the Embassy of India in Phnom Penh. Original Khmer controls and exact original-language ledger quotations are separate. Downloading Prakas 578 is not claimed as reading its 48 pages.

Not yet confirmed: current NSSF contributory-wage table/transition instruments and a current complete scheme computation; exact final rounding instruction; official quick-deduction column; the specific amounts and eligibility rules for additional garment-sector benefits; current GDT box identifiers; cash-benefit scope thresholds and special fringe-benefit valuations; detailed Prakas 578 physical-person/small-taxpayer classification, deductions, losses and special credits; individual treaty/foreign-credit procedure and future deadline extensions. These are not usable calculations here; README retains partial coverage.

Historical claims preserved, excluded from current instructions: old healthcare presentation of a statutory 1.3%/1.3% employer/worker split with the employer bearing all 2.6% from 1 January 2018 (unconfirmed historical claim); old NSSF 400,000 floor/1,200,000 ceiling (health old 200,000 floor),0.8%risk/2.6%health/4%first-phase pension split 2%+2%, derived employer 5.4%/employee 2%/total 7.4%, old maximum employee 24,000/employer 64,800,8 employees/45-dayregistration, first 5 years 4%then next 5 years 8%and later 2.75 percentage-pointdecade steps. Earlier official English NSSF sources were opened, but these do not establish the current wage table/transition. The actual 24,000 example is a hypothetical documented withholding input, not a revived ceiling.

Historical labour claims still to check include the separate 2025 wage schedule and the exact eligibility and amounts of transport, accommodation, attendance, seniority and overtime-meal benefits. The 2026 minimum rates above come from Prakas 214/25. The specific deductibility of fines and penalties requires its current implementing rule. For enforcement, apply the triggers and bases in [Law arts 223–225 and 233](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) to the actual assessment or reminder.

Historical arithmetic retained for reconciliation: the old 6,000,000 salary example omitted the Law 45 mandatory withholding deduction and gave 425,000 tax/net 5,551,000 using 24,000 contribution; applying that documented deduction gives 422,600/net 5,553,400. The old 10,000,000 family example gave base 9,550,000/tax 832,500/net 9,143,500; with the same documented deduction it is 9,526,000/828,900/9,147,100. The old 1,200,000 example remains tax 0/net 1,176,000 on its assumed 24,000 input. The former 5,000,000 salary “NSSF ceiling test” and its 24,000/64,800 outputs are not a current assessment. All 7 old tests remain mapped in the evidence ledger; unsupported claims are not silently deleted.

Prohibitions retained: confirm residence before bands; no resident allowances/bands for non-residents; no double inclusion of separately taxed benefits; no employee charge for employer-only contributions; no stale NSSF ceiling; no invented official quick-deduction figures; prepayment is a credit, not expense; no unsupported private/owner/income-tax deductions; no USD-to-KHR guess; all results pending qualified review.



## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
