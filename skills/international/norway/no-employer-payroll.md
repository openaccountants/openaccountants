---
name: no-employer-payroll
description: >
  Prepare Norway employer payroll for 2026: retrieve tax-card instructions,
  reconcile deductions, distinguish payday withholding remittance from monthly
  a-melding and employer contribution payments. Special cases, statutes and
  independent review remain outstanding.
jurisdiction: "NO"
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.2
---

# Norway employer payroll preparation v0.2

## Who this applies to

This draft covers the ordinary business-employer payroll workflow. Establish the actual employment, wage base, tax-card instruction and insurance position before calculating. It does not determine employee classification or the tax treatment of every benefit, allowance, foreign assignment or special scheme.

## 2026 withholding: pay after each payday

The authority states that the tax-deduction account scheme ends from 2026. Employers must pay withholding directly to the Tax Administration no later than the **first working day after salary payment**. A monthly report does not defer that payment. [Employer withholding obligations][obligations]

Retrieve the employee's tax-card data electronically, update it for each payroll run, apply it to the correct base and document the deduction to the employee. The obligation page describes a limited cross-border deferral application; it requires the specified circumstances and an authority decision, not merely the employer's preference. [Employer withholding obligations][obligations]

## Tax-card decision branches

The deduction guidance directs the main employer to use the table and secondary employers to use the card's percentage; clarify the employer role. If the role is unknown, it directs percentage deduction. PAYE cards use their fixed percentage, including holiday and pre-Christmas pay. [Deduction guidance][deductions]

For ordinary salary without an available tax card, it states **50% withholding**; pensions and specified benefits have a different 30% rule. January use of a prior-year card has separate correction rules. Do not extend the salary rule to every payment or treat an old card as indefinitely valid. [Deduction guidance][deductions]

The employer card-information page requires retrieval of an amended card before payroll. For exemption cards, use the amount allocated to this employer. Salary above that allocation is subject to 50% withholding; a zero allocation means 50% on the whole salary. An employee with several employers must allocate the exemption amount. [Employer card information][cards]

Store card source, version, type, employer role, allocated amount and cumulative use with the pay-run record. No general 2026 exemption ceiling is asserted here: use the actual valid card. The guidance's displayed 2025 amount must not be silently presented as a verified 2026 threshold.

## Reporting is a separate clock

The a-melding is ordinarily due on the fifth of the following month, with the next working day used when that deadline is a weekend/holiday. Report salary for the payment month and employment information monthly through the employee's leaving month. Simplified reporting and specified foreign-employer cases have separate rules. [Reporting deadlines][deadlines]

The general deadlines page still contains legacy advance-tax payment wording. Use the explicit 2026 changes and dedicated payment guidance to avoid applying the old withholding schedule. This draft does not resolve every special-case deadline. [Reporting deadlines][deadlines]; [Payment guidance][payments]

## Employer contribution payments

The dedicated payment page keeps employer national-insurance contributions on a two-month cycle, with ordinary deadlines of 15 January, March, May, July, September and November. Confirm the actual period and business-day treatment. [Payment guidance][payments]

Reconcile both monthly feedbacks to the payment for the period. Payment references differ between taxes/contributions; use the correct KID and account information. A submission confirmation and bank payment evidence are separate records. The page also discusses financial activity tax, which needs its own applicability review. [Payment guidance][payments]

See the existing [social-contribution Guide](no-social-contributions.md) for employer-rate material. Determine coverage, zone, activity and exceptions before selecting a rate. This payroll draft does not independently reverify that Guide or supply an all-in employer cost rate.

## Wage calculation controls

The deduction guidance requires withholding from cash salary and explains that benefits in kind require deductions to the extent cash permits. If cash is insufficient, notify the tax office. It requires deduction documentation for each payment and an annual employee summary in January. [Correct deduction guidance][deductions]

A practical pay-run workpaper should record:

- Worker identity, employment dates and the applicable tax-card version.
- Cash remuneration, benefits, reimbursements and the basis for each treatment.
- Calculated withholding, any attachment order and other authorised deductions.
- Employee net cash and employer contribution liabilities separately.
- Payday, next-working-day remittance, monthly reporting and contribution-period deadlines.
- Accepted report feedback, corrections, payment references and bank confirmations.

This is preparation practice, not the complete statutory payroll specification. Resolve any unexplained difference before treating a pay run as complete.

## Worked example

Assume ordinary cash salary of NOK 50,000, a valid percentage card requiring 30% withholding, and no other deductions. Employee cash is NOK 35,000 and tax withheld is NOK 15,000. The example excludes holiday pay, benefits, pension deductions, attachments and employer contributions. It does not establish the card rate or final annual tax.

```oa-check
name: Norway assumed percentage card payroll split
inputs:
  cash_salary: 50000
  assumed_card_rate: 0.30
steps:
  withholding: cash_salary * assumed_card_rate
  employee_cash: cash_salary - withholding
  reconciled_salary: withholding + employee_cash
expected:
  withholding: 15000
  employee_cash: 35000
  reconciled_salary: 50000
```

Do not use this percentage example to replace a table-based tax card. A payday calendar must be checked separately against Norwegian working days before scheduling remittance.

### 2. Ordinary salary without a card

Assume an ordinary NOK 10,000 salary payment to which the missing-card rule applies, no January exception and no other deductions. At 50%, withholding is NOK 5,000. This is not a final annual tax assessment.

```oa-check
name: Norway assumed missing salary tax card
inputs:
  ordinary_salary: 10000
  missing_card_rate: 0.50
steps:
  withholding: ordinary_salary * missing_card_rate
  cash_before_other_deductions: ordinary_salary - withholding
expected:
  withholding: 5000
  cash_before_other_deductions: 5000
```

### 3. Employer allocation on an exemption card

Assume a valid employer allocation with NOK 1,000 remaining and a NOK 4,000 ordinary salary payment. The NOK 3,000 excess gives NOK 1,500 withholding at 50%. Other deductions remain separate. The example assumes correct allocation and cumulative records.

```oa-check
name: Norway assumed exemption allocation excess
inputs:
  current_salary: 4000
  remaining_allocated_exemption: 1000
  excess_rate: 0.50
steps:
  exempt_part: min(current_salary, remaining_allocated_exemption)
  excess_part: current_salary - exempt_part
  withholding: excess_part * excess_rate
  cash_before_other_deductions: current_salary - withholding
expected:
  exempt_part: 1000
  excess_part: 3000
  withholding: 1500
  cash_before_other_deductions: 2500
```

## Ask the client first

- What employment, work-location, insurance and tax-card facts apply?
- What cash, benefits and reimbursements comprise the payroll base?
- Which payday, report period and employer contribution period are involved?
- Are there attachments, cross-border relief decisions or special schemes?
- Which reports, corrections and payments already exist?

## Sources and review limits

Official authority text retrieved through the search index on 23 October 2026:

- [Employer withholding obligations][obligations].
- [A-melding deadlines][deadlines].
- [Dedicated payment guidance][payments].
- [Correct deduction guidance][deductions]; [employer card information][cards], retrieved in indexed official text on 23 October 2026.

Not yet confirmed: full statutory/amendment chain, complete missing-card/January application, table calculations, benefit valuation, holiday pay, pension and insurance conditions, zone exceptions, attachments, special foreign-employer schemes, sanctions and live filing/payment. Independent review and professional attestation remain outstanding. Payroll and country coverage remain partial.

[obligations]: https://www.skatteetaten.no/en/business-and-organisation/employer/tax-deduction-cards-and-tax-deductions/as-an-employer-you-are-obliged-to-make-withholding-tax-deductions/
[deadlines]: https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/deadlines-and-payment/
[payments]: https://www.skatteetaten.no/en/business-and-organisation/employer/employers-national-insurance-contributions/payment-of-withholding-tax-and-employers-national-insurance-contributions/
[deductions]: https://www.skatteetaten.no/en/business-and-organisation/employer/tax-deduction-cards-and-tax-deductions/how-to-deduct-the-correct-amount-of-tax/

[cards]: https://www.skatteetaten.no/en/business-and-organisation/employer/tax-deduction-cards-and-tax-deductions/tax-deduction-cards/about-tax-deduction-cards-for-you-as-an-employer/
