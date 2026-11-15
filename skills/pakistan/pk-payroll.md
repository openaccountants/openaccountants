---
name: pk-payroll
description: Use for pakistan employer salary withholding. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
version: 1.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - social-contributions-workflow-base
tier: 2
domain: payroll
type: computation
---

# Pakistan employer salary withholding v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers preparing Pakistan salary-withholding working papers for 2026. Use the salary owner's actual tax-year table: normal tax year 2026 is 1 July 2025 to 30 June 2026; a payment in the following tax year needs the later year's law. Load `pk-income-tax` for the applicable table, `pk-payroll-eobi` for integrated payroll and `pk-social-contributions` for coverage. A solo freelancer without employees has no employer salary run, but employment/insurance elsewhere is a separate question.

Quick answer: s.149 uses an estimated annual salary tax average rate at payment, with documented allowed adjustments. A flat annual-tax/12 shortcut only fits an unchanged full-year, equal-pay case. The 2025 consolidation incorrectly attaches the s.4AB addition to denominator B: enacted Finance Act 2024 amendment 22(b) puts it in numerator A, as current 2026 s.149(2) correctly prints. Use that enacted formula; this does not adopt a later tax year's salary bands. [Amendment 22(b)](https://download1.fbr.gov.pk/Docs/2024630146346801FinanceAct-2024.pdf); [current s.149(2)](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf). [ITO s.149](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Rates, bands and thresholds

| Item and conditions | Published tax-year 2026 rule | Source |
|---|---|---|
| Annual individual-return table gate, not an employer s.149 switch | Salary exceeds 75% of taxable income (in words on the page); exactly 75% does not qualify for this table | [First Schedule Part I Division I(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Salary-table lower boundary | Taxable income up to 600,000 is 0%; over 600,000 to 1,200,000 is 1% of excess over 600,000 | [Division I(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Top salary-table band | Over 4,100,000:616,000+35% of excess; separate s.4AB high-income surcharge must be tested | [Division I(2); s.4AB](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Withholding average rate | A/B: A is tax computed on B plus applicable s.4AB; B is estimated income under Salary only. Other-head income is not B; make documented permitted adjustments | [s.149(1)-(2)](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf); [Finance Act 2024 amendment 22(b)](https://download1.fbr.gov.pk/Docs/2024630146346801FinanceAct-2024.pdf) |

## The base

1. Obtain employee identity, taxable pay/benefits, salary from earlier/concurrent employers, bonuses, arrears, join/leave dates, tax already withheld and documented eligible tax credits/other withholding. Value perquisites under the applicable law; special cases below require review.
2. Estimate full-year chargeable salary, using the correct period and actual prior pay rather than merely multiplying remaining-month pay. Use the period's salary table on the salary estimate for s.149, including applicable s.4AB and documented allowable s.61/63 adjustments. The >75% test belongs to the individual's combined annual return; an employer must not switch to business slabs merely because an employee also has other-head income. The omitted s.62 shares credit is not revived.
3. Apply s.149's average-rate method at payment and adjust excess/deficiency or earlier failure to deduct as permitted by s.149(1). Maintain the annual forecast, year-to-date deductions and remaining payments so adjustments are transparent; never tax every bonus at an invented standalone rate.
4. Run employee contributions separately after identifying scheme coverage/base. Employer social costs are employer costs, not employee tax credits or a reason to reduce chargeable salary without a legal deduction. Unknown EOBI/ESSI coverage is an unresolved item rather than assumed cash deduction. [ITO s.149](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf); [EOB Act s.9(3)](https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf).

## Deadlines and filing

Report s.149 deductions in the applicable quarterly s.165 statement, not a blanket monthly statement. The 2025 ordinance and current 2026 text require quarters ending March/June/September/December by 20 April/20 July/20 October/20 January. [s.165(1)-(2)](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf). Reconcile employee identifiers, pay, deduction, section and actual CPR. Use the sourced deposit/statement/certificate distinctions below; the old flat 15th-of-next-month deposit rule is wrong.

Generate the correct FBR payment instruction, remit and retain the CPR; reconcile with quarterly reporting and employee deduction certificates. EOBI/provincial contributions have their own institutions and calendars. This skill produces the reviewed working paper, not a filed statement.


### Deposit, salary statement and certificate rules now sourced

Income Tax Rules 43 requires federal/provincial government deposit on the day of collection/deduction; other persons deposit within 7 days from each week ending Sunday, with nonresident overseas remittances paid before remitting abroad. There is no separate other-agent fortnight rule. Rule 44(5) requires the s.149 deductor's **annual salary statement by 31 July** after financial-year end, Part IX Second Schedule, separately from quarterly s.165 reporting. Rule 44(4) requires reconciliation when the Commissioner requires it, not a universal annual reconciliation automatically replacing that salary statement. [Rules 43/44](https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf).

Rule 42's non-salary collection/deduction certificate uses Part VII Second Schedule within 15 days after financial-year end or business discontinuation; an earlier in-year request is answered within 7 days. Duplicate/lost-certificate and serial-number rules apply. This non-salary rule is not an employer salary-certificate deadline. Verify actual salary certificate entitlement/form under the operative law rather than revive omitted rule 41. [r 42](https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf).

## Penalties and interest

Failure to deduct/pay may expose the payer under s.161; late/default consequences under ss.182/205 depend on the law/date/default. Do not present an unsupported daily penalty or a monthly contribution due date as a withholding-tax rule. Refer default/notices for separate assessment.

## Cross-border points

Non-resident/split-pay employees, expatriate packages, foreign currency and treaty relief need specific source/credit analysis; s.71 governs evidenced currency conversion, not a contractual override. Refer share awards/RSUs,s.14 valuation, termination/golden handshake/gratuity, provident-fund recognition, directors' fees outside payroll, casual/piece-rate coverage and arrears spanning tax years. Do not choose business slabs for employment merely to raise tax.

## Two worked examples that recompute

Cases assume only documented salary, no other charge/credit and the tax-year 2026 table. Results are derived, not rates for the following year.

```oa-check
name: Earlier1200000annual salary case now computed
inputs:
  annual_taxable_salary: 1200000
  equal_payments: 12
steps:
  - annual_tax: (annual_taxable_salary - 600000) * 0.01
  - monthly_tax: annual_tax / equal_payments
  - monthly_gross: annual_taxable_salary / equal_payments
  - net_before_other_deductions: monthly_gross - monthly_tax
expected:
  annual_tax: 6000
  monthly_tax: 500
  monthly_gross: 100000
  net_before_other_deductions: 99500
```

```oa-check
name: Remaining payment adjustment after annual forecast changes
inputs:
  supported_revised_annual_tax: 300000
  tax_already_deducted: 180000
  remaining_equal_payments: 4
steps:
  - remaining_tax: supported_revised_annual_tax - tax_already_deducted
  - remaining_payment_deduction: remaining_tax / remaining_equal_payments
expected:
  remaining_tax: 120000
  remaining_payment_deduction: 30000
```

The second case is an equal-pay reconciliation illustration: the annual forecast and permitted adjustment must first be established under s.149. Do not treat a mid-year joiner as having no earlier salary without records.

## Ask the client first

Obtain contracts/payroll records, employee identifiers, current/previous employment pay, benefits/bonuses, tax period, actual prior deductions/credits, joining/leaving/arrears facts, scheme registrations/base notices and current payment/reporting requirements. Refuse final payroll where the period/table or necessary pay records are missing. Never skip quarterly reporting, use business slabs for ordinary employee salary, assume an EOBI base or invent a credit/certificate.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Income Tax Rules 42-44 operative payment, non-salary certificate, annual salary statement and requested reconciliation branches on 2026-11-14 | https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf. | 2026-11-14 |
| Read for enacted Finance Act 2024 amendment 22(b) and current s.149(2), reconciling the 2025 consolidation's incorrect denominator annotation | https://download1.fbr.gov.pk/Docs/2024630146346801FinanceAct-2024.pdf; https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf | 2026-11-15 |
| Read for ITO ss.71,74,149 and First Schedule salary table/classification, with s.4AB surcharge context | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |
| Read for current 2026 ITO s.165 quarterly statement and schedule, confirming cadence separate from deposit | https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf | 2026-11-14 |
| Read for EOB Act ss.9/9 B employer/employee contribution distinction and employer-share recovery prohibition | https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf | 2026-11-14 |

Not yet confirmed: salary-certificate form, current IRIS screen identifiers, individual credits/benefits and non-resident packages, current EOBI/provincial coverage/base/deadlines, later-period salary tables and any default-date penalty assessment. The old monthly-withholding-statement instruction is replaced by the sourced quarterly rule.
