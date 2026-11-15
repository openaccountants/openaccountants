---
name: bt-payroll-social
description: "Compute Bhutan monthly salary withholding and distinguish civil NPPF from private provident-fund coverage, bases, remittance and annual reconciliation in 2026."
jurisdiction: BT
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
version: "2.0"
type: situation-rules
---

# Bhutan Payroll and Social Contributions (2026) | v2.0

For 2026 payroll, compute salary TDS under Rule 153 and AnnexureI, then apply the employee’s actual pension/provident scheme separately. Civil NPPF and private PF rates are not interchangeable, and PF is not a second annual employment-tax deduction. [r.153;AnnexureI,42401-42500 row](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf); [ss.21-24,44](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [contribution table and remittance paragraphs](https://www.nppf.org.bt/remittance-of-contribution/); [clauses 1.1-1.2](https://www.nppf.org.bt/downloads/?attachment_id=442)

## Who this applies to

Rule 153 applies to a resident employer making a taxable employment payment. Pension/PF coverage depends on the member and scheme: the civil/Government contribution table is not a universal minimum for every worker. The Private PF Guidelines exclude members already covered by the civil, armed-forces or specified alternative schemes and require an agreement and member accounts. Establish employee status, coverage and the signed agreement before deducting contributions. [r.153;AnnexureI,42401-42500 row](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf); [contribution table and remittance paragraphs](https://www.nppf.org.bt/remittance-of-contribution/); [ss.1-10](https://www.nppf.org.bt/wp-content/uploads/2024/08/Private PFSchemeGuidelines.pdf)

## Rates, bands and thresholds

| Item | Rule for 2026 | Official source |
|---|---|---|
| Monthly salary withholding | Reduce gross monthly employment income by 15% (in words on the page), then use the actual AnnexureI band. Do not replace its rounded band amount by annual tax divided by 12. | [r.153;AnnexureI,42401-42500 row](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf) |
| Civil/Government NPPF table | Employee 11%, employer 15%; combined 26% is derived. Apply the scheme’s confirmed salary base, not an assumed all-allowances gross-pay base. Armed-forces rates differ. | [contribution table and remittance paragraphs](https://www.nppf.org.bt/remittance-of-contribution/) |
| Private agency PF agreement | Minimum 5% employee and 5% employer of monthly basic pay, with matching and the actual agreement; 10% combined is derived. This is not the civil 11% table. | [ss.1-10](https://www.nppf.org.bt/wp-content/uploads/2024/08/Private PFSchemeGuidelines.pdf); [clauses 1.1-1.2](https://www.nppf.org.bt/downloads/?attachment_id=442) |
| Private-member minimum notice | NPPF’s 7 April 2025 notice requests members contributing below Nu.1,000 per month to increase to at least Nu.1,000 immediately. The notice does not allocate that figure between employee and combined contributions; reconcile the member’s agreement before applying a below-floor result. | [whole operative notice](https://www.nppf.org.bt/important-notice-minimum-contribution-update-for-private-pf-members/); [clauses 1.1-1.2](https://www.nppf.org.bt/downloads/?attachment_id=442) |
| Salary TDS statement and deposit | Within 10 days after each calendar month. The employer’s duty to pay tax it should have withheld remains even if the deduction was missed. | [ss.273-279](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [whole notice](https://www.drc.gov.bt/wp-content/uploads/2026/02/TDS-return-and-deposit.pdf) |
| Pension/PF remittance | Civil combined contributions by the 10 th of the following month. Private agreement: both shares by the 10 th of the following month for the agreed contribution period; do not assume every enrolled arrangement uses the same period. | [contribution table and remittance paragraphs](https://www.nppf.org.bt/remittance-of-contribution/); [clauses 1.1-1.2](https://www.nppf.org.bt/downloads/?attachment_id=442) |

## The base

Identify taxable employment income, including salary, bonuses, allowances and benefits, and apply s.24’s specific exclusions before using the statutory method. Employer pension/PF contributions are excluded only within the applicable recognized-fund limits, not without limit. Annual resident employment deduction is separately capped under s.44; do not subtract employee PF/GIS again under the old regime. [ss.21-24,44](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [r.153;AnnexureI,42401-42500 row](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf)

For monthly withholding, Rule 153 specifies the reduction from gross monthly employment income and AnnexureI supplies the band amount. For annual resident tax, s.44 instead uses the lower of the percentage and annual cap. Rounding and the monthly/annual limits can produce a difference even for regular salary. Reconcile through the applicable annual return and credits; do not promise an automatic refund or use an annual effective rate as the payroll table. [r.153;AnnexureI,42401-42500 row](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf); [ss.21-24,44](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.263,290-295](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

The private scheme defines salary as basic pay. Its current standard agreement separately lists private-agency, self-employed and contract-employee contribution options; the signed membership category and period control. A Government/civil membership record does not establish that all allowances belong in its contribution base. Obtain the operative plan/pay record before computing that branch. Do not extend the old “at least 11% for covered members” statement to every NPPF or private member. [ss.1-10](https://www.nppf.org.bt/wp-content/uploads/2024/08/Private PFSchemeGuidelines.pdf); [clauses 1.1-1.2](https://www.nppf.org.bt/downloads/?attachment_id=442); [contribution table and remittance paragraphs](https://www.nppf.org.bt/remittance-of-contribution/)

## Deadlines and filing

Check the employee’s TPN; the employer must apply within 30 days of joining unless one has already been issued. Keep the taxpayer’s existing/new TPN correspondence during the announced BITS transition. [ss.296-300](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [both image pages](https://www.drc.gov.bt/transition-to-the-bhutan-integrated-taxation-system-income-tax-module/)

DRC’s February notice requires the monthly TDS return in RAMIS. Prepare AnnexureII with payer name/TPN/address, each payee’s identity/TPN, payment nature and gross amount, rate, tax, dates/mode and remittance summary. Submit electronically through the DRC-specified platform; hard copy requires prior written permission under Rule 162. Deposit the tax, preserve the submission and payment references, and reconcile both to payroll. The final live button/field names and later BITS replacement screens are not certified here. [whole notice](https://www.drc.gov.bt/wp-content/uploads/2026/02/TDS-return-and-deposit.pdf); [r.162;AnnexureII](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf); [ss.273-279](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

For private PF, complete the agreement and enrollment process to obtain the member/agency code and PF number. Use the issued deposit invoice and recovery schedule with the correct member numbers, remit both shares for the agreed period, and forward the deposit invoice plus schedule as required by the agreement. The civil remittance page likewise requires the recovery schedule and deposit slip. Retain payroll-to-schedule and bank reconciliation. [clauses 1.1-1.2](https://www.nppf.org.bt/downloads/?attachment_id=442); [contribution table and remittance paragraphs](https://www.nppf.org.bt/remittance-of-contribution/)

An employee’s annual filing duty depends on the statutory exception, total income and other sources, not simply whether tax was deducted monthly. Use [the personal-tax skill](bt-income-tax.md) for the annual deadline and reconciliation. The old March PIT deadline is not the 2025 PIT deadline and does not become the 2026 one. [ss.263,290-295](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [paragraphs 1-2](https://www.drc.gov.bt/wp-content/uploads/2025/12/Tax-Filing-Notification_IY-2025_final.pdf)

## Penalties and interest

For late TDS statements, s.664 charges Nu.300 per day for a company and Nu.100 per day for another person, subject to permitted filing extensions and no duplicate penalty for the same s.600 notice failure. Tax not deposited bears 15% per annum simple late interest (in words on the page), capped at the tax liability; the withholding agent bears that interest personally. The NPPF remittance page separately states 2% per month or 24% per annum late interest on delayed contributions. Do not confuse the two liabilities. [ss.442-450,664-666](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [whole notice](https://www.drc.gov.bt/wp-content/uploads/2026/02/TDS-return-and-deposit.pdf); [contribution table and remittance paragraphs](https://www.nppf.org.bt/remittance-of-contribution/)

## Cross-border points

Separate employment source and tax residence from nationality and PF membership. Foreign or contract status does not by itself establish the civil pension rate or a tax exemption. Confirm the actual member category/agreement and any treaty entitlement before adjusting salary withholding. Use the personal skill’s source/residence rules and refer unresolved foreign-employer or treaty questions before a rate is certified. [ss.16-20](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.226-232](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [clauses 1.1-1.2](https://www.nppf.org.bt/downloads/?attachment_id=442)

## Two worked examples that recompute

A resident employee receives taxable monthly gross Nu.50,000. After the Rule 153 reduction the AnnexureI base is Nu.42,500, which falls in its Nu.42,401-42,500 row and gives actual monthly TDS Nu.917. Over 12 identical months withholding is Nu.11,004. Annual income Nu.600,000 less the resident annual deduction gives tax Nu.11,000, a derived Nu.4 difference before other reliefs or credits. Nu.917 is a table lookup, not a rounded annual-rate substitute. [r.153;AnnexureI,42401-42500 row](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf); [ss.21-24,44](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

```oa-check
name: Actual monthly table versus annual reconciliation
inputs:
  monthly_gross: 50000
  months: 12
  table_tds: 917
steps:
  monthly_table_base: monthly_gross * (1 - 0.15)
  withheld: table_tds * months
  annual_gross: monthly_gross * months
  annual_deduction: min(annual_gross * 0.15, 150000)
  annual_taxable: annual_gross - annual_deduction
  annual_tax: 10000 + (annual_taxable - 500000) * 0.10
  difference: withheld - annual_tax
expected:
  monthly_table_base: 42500
  withheld: 11004
  annual_tax: 11000
  difference: 4
```

An enrolled private-agency employee has monthly basic pay Nu.30,000 and taxable gross Nu.40,000. The signed agreement uses 5% employee plus matching 5% employer on basic pay. Each share is Nu.1,500 and combined remittance Nu.3,000, all derived and above the private-member minimum notice figure. Using gross would produce Nu.4,000 combined, an excess Nu.1,000. Choose the supported basic-pay base; this case does not determine the civil-plan base or allocate a below-floor adjustment. [ss.1-10](https://www.nppf.org.bt/wp-content/uploads/2024/08/Private PFSchemeGuidelines.pdf); [clauses 1.1-1.2](https://www.nppf.org.bt/downloads/?attachment_id=442); [whole operative notice](https://www.nppf.org.bt/important-notice-minimum-contribution-update-for-private-pf-members/)

```oa-check
name: Private PF basic pay rather than total gross
inputs:
  basic_pay: 30000
  gross_pay: 40000
steps:
  employee: basic_pay * 0.05
  employer: basic_pay * 0.05
  combined: employee + employer
  gross_based_combined: gross_pay * 0.10
  excess: gross_based_combined - combined
expected:
  employee: 1500
  employer: 1500
  combined: 3000
  gross_based_combined: 4000
  excess: 1000
```

## Ask the client first

- Employer residence, employee status, source and income year?
- Monthly gross components, exclusions, bonuses and annual totals?
- Civil/armed/private/contract membership, signed agreement and scheme salary base?
- Basic pay, unpaid leave, contribution period and minimum-notice treatment?
- Employee TPN, PF number, payroll table, prior deductions and tax paid?
- Return acknowledgements, remittance schedules and any default notice?

## Sources

| Source | Read for | Read date |
|---|---|---|
| [Income Tax Act of Bhutan 2025](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) | Read for ss.1-64,204-207,226-240,262-300,324-326,442-450,664-674,706(40); Schedules 1-3 and 6. | 2026-11-15 |
| [Rules on the Income Tax Act 2025](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf) | Read for rr.47-58,151-164; Annexures I-II and IV, relevant individual and company computation fields. | 2026-11-15 |
| [DRC income-year 2025 filing notice,29 December 2025](https://www.drc.gov.bt/wp-content/uploads/2025/12/Tax-Filing-Notification_IY-2025_final.pdf) | Read for both pages: filing windows, inactive entities, RAMIS/BETA, completion status and payment voucher. | 2026-11-15 |
| [DRC withholding notice,4 February 2026](https://www.drc.gov.bt/wp-content/uploads/2026/02/TDS-return-and-deposit.pdf) | Read for both pages: monthly statement/payment, RAMIS and statutory penalties. | 2026-11-15 |
| [DRC income-module transition notice,10 November 2026](https://www.drc.gov.bt/transition-to-the-bhutan-integrated-taxation-system-income-tax-module/) | Read for both image pages: January transition, TPN notices and December application timing. | 2026-11-15 |
| [NPPF remittance of contribution](https://www.nppf.org.bt/remittance-of-contribution/) | Read for complete contribution table,remittance instructions and late-interest paragraph. | 2026-11-15 |
| [NPPF Private PF Scheme Guidelines 2021](https://www.nppf.org.bt/wp-content/uploads/2024/08/PrivatePFSchemeGuidelines.pdf) | Read for pp.1-6,ss.1-10: coverage,basic-pay definition,agreement and contributions. | 2026-11-15 |
| [NPPF current Private PF agreement](https://www.nppf.org.bt/downloads/?attachment_id=442) | Read for all 4 pages,especially clauses 1.1-1.2: member numbers,rate,base,deposit and recovery schedule. | 2026-11-15 |
| [NPPF minimum-contribution notice,7 April 2025](https://www.nppf.org.bt/important-notice-minimum-contribution-update-for-private-pf-members/) | Read for whole operative notice: request to increase private-member monthly contributions. | 2026-11-15 |

Not yet confirmed: the civil-plan contribution base for allowances not supported by an operative plan record; allocation of the private Nu.1,000 notice between employee and combined shares; any universal minimum across all NPPF categories; final live RAMIS/BITS buttons and 2027 screens; employee-specific treaty relief.
