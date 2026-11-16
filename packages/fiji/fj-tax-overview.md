---
name: fj-tax-overview
description: "Choose the Fiji tax skill for a 2026 question, with current headline taxes, date-sensitive changes and a source-first handoff."
jurisdiction: FJ
tax_year: 2026
last_updated: 2026-11-16
version: 0.1
type: router
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Fiji Tax Overview v0.1

## Scope

Route a Fiji tax or company question to the right skill and official source for 2026. The national authority is the Fiji Revenue and Customs Service (FRCS). Use Fijian dollars, FJD, for local tax figures. This overview is an entry point, not a substitute for the detailed tax base, return, exemption or registration conditions in the destination skill. [FRCS tax rates and codes](https://frcs.org.fj/tax-rates-and-codes/).

### Quick reference

| Question | Headline with its conditions | Official source |
|---|---|---|
| Tax year | Calendar year unless a company has an approved substituted year; do not assume every company ends in December. | [Income Tax Act, section 36 and definition of tax year](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| Residence/source | Residents' gross income includes Fiji and foreign sources; non-residents include Fiji-source income. Exempt and separately taxed final-income categories are excluded as the Act provides. | [Income Tax Act, section 14](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| Resident personal tax | First FJD 30,000 of annual chargeable income is nil-rated. The top marginal rate is 39% above FJD 1,000,000; 20% is only an intermediate band. Non-residents do not receive the resident nil band. | [LN 55/2023, regulation 3(a), effective 1 January 2024](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Ordinary company tax | 25% of chargeable income. A qualifying SPSE-listed company is at 15% through its seventh tax year from listing, then 25%. | [LN 55/2023, regulations 2 and 3(b)](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| VAT | Standard rate 12.5% from 1 August 2025; zero-rating and exemption depend on the statutory supply and conditions, not the headline rate. | [VAT Act, section 15 and Schedules 1-2](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf); [FRCS VAT guide](https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/vat-guide/) |
| Annual income-tax return | Generally within three months after year-end if required to file; for calendar-year 2026 that normally means 31 March 2027, subject to an evidenced extension. Not every employee has an annual filing obligation. | [Income Tax Act, sections 104-105 and 125](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| Social Responsibility Tax | Do not add the former SRT table to current personal tax. Its definition and separate charge were removed from 1 January 2024. | [Act 5/2023, sections 1-3](https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-5-Income-Tax-Budget-Amendment.pdf) |
| Tourism Services Tax | From 1 September 2026, 5% for the Act's listed tourism services where annual gross turnover is over FJD 2 million. Show it separately; TST itself is not subject to VAT. It is not a tax on every business or every tourist payment. | [Tourism Services Tax Act 2026, sections 1-4 and Schedule](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-20-Tourism-Services-Tax-Act-2026.pdf?ver=1794354122) |

## Ask the client first

Ask what work must be done, the transaction/pay date and tax year, individual/company/other structure, residence, where income/supply/work arises, gross and taxable amounts, registration status, employees, listing/incentive claims and relevant foreign country. For a deadline, ask for the actual year-end, tax type and any approved extension. Establish these before selecting a rate.

## The method, step by step

1. **Place the question and date.** Confirm Fiji and the relevant year/transaction period. A proposed budget measure is not an enacted amendment. Apply the commencement section of the final Act, especially for the mid-year changes below.
2. **Load the destination.** Read the complete relevant skill before answering or computing.

| Job | Load | Handoff |
|---|---|---|
| Personal income, non-resident individual or self-employment | [Fiji income tax](fj-income-tax.md) | Establish residence, chargeable income, source, filing obligation and credits. This unchanged sibling has its own source limits; check later 2026 enactments before relying on a held budget item. |
| Company profits, listing, losses, advances and non-resident payments | [Fiji corporate income tax](fj-corporate-income-tax.md) | Supply tax year, residence/source, adjusted base, listing date, loss vintages and payment/treaty facts. |
| Supply, registration, invoice, input credit or VAT return | [Fiji VAT](fiji-vat.md) | Supply date/type, turnover, registration, value, invoices, imports and taxable/exempt use. Do not infer zero-rating from the country alone. |
| Employer payroll, PAYE or FNPF | [Fiji payroll and social contributions](fj-payroll-social.md) | Pay period/date, tax-code/residence facts, taxable remuneration, contribution wages and prior pay/withholding. |
| Entity choice, company registration and ownership records | [Fiji company formation](fj-company-formation.md) | Members, ultimate controllers, resident officers, business activity, foreign investment and documents. |
| Detailed transfer pricing or a cross-border structure | Country pack gap | There is no complete dedicated local skill in this pack. Retrieve the applicable law and effective treaty; do not substitute another country's thresholds or turn domestic WHT rates into treaty advice. |

3. **Check date-sensitive changes.** The enacted 2026 Income Tax amendment takes effect from August and includes targeted deductions, losses and reporting changes. The 2026 Tax Administration amendment introduces beneficial ownership obligations from August, while its CRS division commences in January 2027. These are different systems and start dates. Follow the actual provisions in the relevant destination rather than treating every 2026 budget announcement as applying for the entire calendar year. [Act 14/2026, section 1](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-14-Income-Tax-Budget-Amendment-No.-2-Act-2026.pdf?ver=1794354122); [Act 13/2026, sections 1, 6-7](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-13-Tax-Administration-Budget-Amendment-Act-2026.pdf?ver=1794354122).
4. **Identify other levies by the activity.** The old overview's general ECAL-on-services and high-income SRT instructions are obsolete. FRCS's VAT guide marks the old service ECAL as removed; do not restore it as a general 2026 surcharge. Tourism Services Tax is a separate enacted regime with a service schedule, turnover condition, accountable person and return/payment duty. Other activity-specific levies require their own law. [FRCS VAT guide, tax labels](https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/vat-guide/); [Act 5/2023](https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-5-Income-Tax-Budget-Amendment.pdf); [Tourism Services Tax Act, sections 2-4 and Schedule](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-20-Tourism-Services-Tax-Act-2026.pdf?ver=1794354122).
5. **Return a usable answer with its boundaries.** State the period, facts relied on, method, applicable official provision and next filing/payment step. If an affected input or rule is held in the destination, explain the exact missing point and stop that result; never silently supply the old figure.

## Worked cases

**Tax-inclusive invoice routing.** A registered business makes an ordinary standard-rated supply for FJD 1,125 including VAT in 2026, with no special supply or TST. The VAT skill must extract FJD 125, leaving FJD 1,000 net. It must not calculate VAT at 12.5% of the inclusive price or apply the old 9% rate. This arithmetic does not establish registration, deductibility or input-credit entitlement. [VAT Act, sections 2 and 15](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf); [FRCS VAT guide](https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/vat-guide/).

```oa-check
name: Fiji overview routes a standard tax-inclusive invoice
inputs:
  invoice_total: 1125
steps:
  net_value: invoice_total / 1.125
  vat: invoice_total - net_value
expected:
  net_value: 1000
  vat: 125
```

## When to refuse or refer

Refuse to turn headline figures into a return, payroll result, investment approval, audit exemption or treaty conclusion without the destination's required facts. Refer a dedicated transfer-pricing/cross-border request when the missing local method or treaty cannot be read. Do not infer professional approval from the folder, committer or maintenance assignment.

## Sources

| Source | What was read | Read on |
|---|---|---|
| [FRCS tax rates and codes](https://frcs.org.fj/tax-rates-and-codes/) | Read for current individual/company/VAT headings and tables to identify the tax authority, local currency convention and headline routing checks. | 2026-11-16 |
| [Income Tax Act, FRCS revision](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) | Sections 14, 36, 104-105 and 125: residence/source, substituted year, return duty and employment final-tax exception. | 2026-11-16 |
| [LN 55/2023](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) | Entire rate amendment: individual bands, company listing transition, replacement company rates and separate commencement dates. | 2026-11-16 |
| [Income Tax amendment, Act 5/2023](https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-5-Income-Tax-Budget-Amendment.pdf) | Sections 1-3 remove the separate SRT definition/charge from 1 January 2024. | 2026-11-16 |
| [VAT Act, FRCS revision](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) | Sections 2 and 15 and the supply classification structure, for the standard rate and inclusive-value example. | 2026-11-16 |
| [FRCS VAT guide](https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/vat-guide/) | Standard VAT and historical/current tax labels; service ECAL marked removed, distinct tourism tax introduced. | 2026-11-16 |
| [Income Tax amendment, Act 14/2026](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-14-Income-Tax-Budget-Amendment-No.-2-Act-2026.pdf?ver=1794354122) | Final enacted three-page text and August commencement, rather than relying on the budget bill. | 2026-11-16 |
| [Tax Administration amendment, Act 13/2026](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-13-Tax-Administration-Budget-Amendment-Act-2026.pdf?ver=1794354122) | Section 1 commencement distinction and inserted CRS/beneficial ownership divisions, for separate routing. | 2026-11-16 |
| [Tourism Services Tax Act 2026](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-20-Tourism-Services-Tax-Act-2026.pdf?ver=1794354122) | Entire five-page Act, including commencement, turnover threshold, tax base, VAT exclusion, monthly duty, registration and service Schedule. | 2026-11-16 |

Not yet confirmed: a complete local transfer-pricing method and dedicated cross-border/treaty pack; all activity-specific levies outside the taxes above; the exact service-ECAL repeal instrument for historical periods; later-law resolution of every held item in the unchanged income-tax sibling. Missing methods and held items remain gaps, not comprehensive coverage.
