---
name: ag-abst
description: >
  Antigua and Barbuda Sales Tax (ABST) for 2026. Covers the 17% standard rate set by the
  Revenue (Miscellaneous Provisions) Act 2023, the tour operator change to the passenger
  transport exemption, the return due 15 calendar days after each tax period under the
  ABST (Amendment) Act 2024, the registration test and penalties in the IRD FAQ, how to
  take the tax out of an inclusive price, and the working papers for a return. Trigger
  phrases include ABST, Antigua sales tax, Antigua VAT, ABST return deadline, ABST 17%.
version: 1.0
jurisdiction: AG
tax_year: 2026
last_updated: 2026-11-14
category: international
type: situation-rules
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Antigua and Barbuda Sales Tax (ABST)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

The Antigua and Barbuda Sales Tax (ABST) under the Antigua and Barbuda Sales Tax Act 2006 (No. 5 of 2006) as amended, for tax periods in 2026. Covers the ordinary rate, the return deadline, registration, the tax fraction for inclusive prices, penalties as published by the Inland Revenue Department (IRD), and the return working papers. Amounts are Eastern Caribbean dollars (EC$). Social security and Medical Benefits payroll contributions are in [ag-social-security](ag-social-security.md) and [ag-medical-benefits](ag-medical-benefits.md). This skill does not cover zero-rated and exempt classifications in detail, imports, refunds or temporary reduced-rate days.

## Ask the client first

1. Is the business registered for ABST, and from what date? Does it hold the certificate of registration?
2. Taxable supplies in the last 12 months and expected in the next 12 months.
3. Is the business one of the professions the IRD says must register whatever its turnover (for example lawyers, accountants, architects, land surveyors, engineers)?
4. What does it supply: ordinary goods and services, accommodation, passenger transport (and is it a tour operator), exports, or supplies listed as exempt?
5. Are prices quoted inclusive or exclusive of ABST?
6. Tax period end date, and the input ABST invoices held for the period.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Standard rate, section 8(3)(b) | 17% (the figure 14 replaced by 17) | [Act 13 of 2023, s.2(a)](https://laws.gov.ag/wp-content/uploads/2024/02/No.-13-of-2023-Revenue-Miscellaneous-Provision-Act-2023.pdf) |
| Rate in section 8(3)(d) | 17% (the figure 15 replaced by 17) | same |
| Effective date of 17% | 1 January 2024, applied to old and new stock alike | [Consumer Affairs, question of 15 January 2024](https://consumeraffairs.gov.ag/question_of_the_week_2024.php) |
| Passenger transport exemption, Schedule 4 item 9 | Transport of passengers by land, sea or air within Antigua and Barbuda is exempt, except transportation by tour operators | same |
| Return deadline, section 39(1) | No later than 15 calendar days after the end of each tax period, from the period ending 31 March 2024 | [Act 1 of 2024, ss.1 and 3](https://laws.gov.ag/wp-content/uploads/2025/01/No.-1-of-2024-Antigua-and-Barbuda-Sales-Tax-Amendment-Act-2024.pdf) |
| Compulsory registration | Taxable supplies of EC$300,000 or more (IRD FAQ, 2020 edition) | [IRD ABST FAQ](https://ird.gov.ag/wp-content/uploads/2020/06/Frequently_asked_questions_ABST.pdf) |
| Late filing penalty | EC$500 or 5% of the amount owing, whichever is greater (IRD FAQ, 2020 edition) | same |
| Late payment penalty | 10% of the amount owing, plus interest (IRD FAQ, 2020 edition) | same |

### Steps

1. **Registration.** A person with EC$300,000 or more of taxable supplies, or who expects turnover to rise above that, registers; the listed professions register whatever their turnover. Only registered businesses may charge ABST.
2. **Classify each supply:** taxable at 17%, zero-rated, or exempt (Schedule 4). Passenger transport within the country is exempt unless supplied by a tour operator.
3. **Output tax.** On an exclusive price, multiply the net value by 17%. On an inclusive price, the tax is price x 17/117. Never multiply the inclusive price by 17%.
4. **Input tax.** Deduct only input ABST on invoices that support a taxable business purchase.
5. **Return.** File the return for each tax period by the 15th calendar day after the period ends. For a period ending 30 September 2026 the return is due 15 October 2026.
6. **Reconcile** the transaction register (supply date, net value, ABST, invoice reference, treatment) to the sales ledger, the ABST control account and the return.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Old IRD FAQ shows 15% standard and 14% accommodation | Obsolete: both figures were replaced by 17% from 1 January 2024 | [Act 13 of 2023](https://laws.gov.ag/wp-content/uploads/2024/02/No.-13-of-2023-Revenue-Miscellaneous-Provision-Act-2023.pdf) |
| Old IRD FAQ says the return is due one calendar month after the period | Obsolete: 15 calendar days from the period ending 31 March 2024 | [Act 1 of 2024](https://laws.gov.ag/wp-content/uploads/2025/01/No.-1-of-2024-Antigua-and-Barbuda-Sales-Tax-Amendment-Act-2024.pdf) |
| Tour operator carrying passengers within the country | Not exempt under the new item 9; charge 17% if registered | Act 13 of 2023, s.2(b) |
| Payment timing | Act 1 of 2024 amends only the return date in section 39(1); confirm the payment rule separately before advising on late payment | Act 1 of 2024 |
| Deadline falls on a weekend or public holiday | Not confirmed here; file earlier | not confirmed |
| Unregistered seller adds ABST to an invoice | Not allowed: only registered businesses can charge ABST | [IRD ABST FAQ](https://ird.gov.ag/wp-content/uploads/2020/06/Frequently_asked_questions_ABST.pdf) |

## Worked cases

### Case 1: ordinary monthly return

A registered retailer has net taxable sales of EC$100,000 and EC$7,000 of supported input ABST. Output ABST is 17,000; gross invoices 117,000; net ABST payable 10,000.

```oa-check
name: ABST monthly return, net sales 100,000 at 17%
inputs:
  net_sales: 100000
  input_tax: 7000
  rate: 0.17
steps:
  - output_tax: net_sales * rate
  - gross_invoices: net_sales + output_tax
  - payable: output_tax - input_tax
expected:
  output_tax: 17000
  gross_invoices: 117000
  payable: 10000
```

### Case 2 (decision): is the quoted price inclusive or exclusive?

A customer is quoted EC$11,700. If the quote is ABST-inclusive, the tax inside it is 11,700 x 17/117 = 1,700 and the net price is 10,000. If it is exclusive, ABST of 1,989 is added and the customer pays 13,689. Multiplying the inclusive price by 17% would give 1,989, overstating the tax by 289. Decide the basis from the contract before issuing the invoice.

```oa-check
name: ABST tax fraction on an 11,700 quote, inclusive against exclusive
inputs:
  quote: 11700
  rate: 0.17
steps:
  - tax_if_inclusive: quote * rate / (1 + rate)
  - net_if_inclusive: quote - tax_if_inclusive
  - tax_if_exclusive: quote * rate
  - total_if_exclusive: quote + tax_if_exclusive
  - overstatement: tax_if_exclusive - tax_if_inclusive
expected:
  tax_if_inclusive: 1700
  net_if_inclusive: 10000
  tax_if_exclusive: 1989
  total_if_exclusive: 13689
  overstatement: 289
```

## When to refuse or refer

- Temporary reduced-rate days, concessions, and the transition date for tour operators: not checked here.
- Zero-rated and exempt classifications beyond item 9, imports, refunds, input-credit restrictions, invoices and records rules: refer to the Act and the IRD.
- Disputes, assessments and objections: refer to a local practitioner.
- Any figure from the 2020 FAQ (registration threshold, penalties) that the client will rely on: confirm with the IRD first, as later amendments have not been checked.

## Filing and payment

1. Register with the IRD first; then apply for ABST registration and display the certificate.
2. File the ABST return for each tax period by the 15th calendar day after it ends (Act 1 of 2024).
3. Keep the transaction register, invoices, the calculation and the IRD receipt; reconcile the ABST control account each period.

## Completion checklist

- Registration status and date confirmed.
- Every supply classified; tour operator transport not treated as exempt.
- 17% applied; inclusive prices use 17/117.
- Return filed within 15 calendar days of period end.
- Register reconciled to the ledger and return.

## Sources

| Source | URL | Read on |
|---|---|---|
| Revenue (Miscellaneous Provisions) Act 2023 (No. 13 of 2023): read for section 2, the 17% rates in section 8(3)(b) and (d) and the new Schedule 4 item 9 | https://laws.gov.ag/wp-content/uploads/2024/02/No.-13-of-2023-Revenue-Miscellaneous-Provision-Act-2023.pdf | 2026-11-14 |
| Antigua and Barbuda Sales Tax (Amendment) Act 2024 (No. 1 of 2024): read for commencement (1 March 2024, periods ending 31 March 2024 on) and the new section 39(1) 15-day return rule | https://laws.gov.ag/wp-content/uploads/2025/01/No.-1-of-2024-Antigua-and-Barbuda-Sales-Tax-Amendment-Act-2024.pdf | 2026-11-14 |
| Consumer Affairs Division question of the week, 15 January 2024: read for the 15% to 17% increase effective 1 January 2024 | https://consumeraffairs.gov.ag/question_of_the_week_2024.php | 2026-11-14 |
| IRD ABST frequently asked questions (2020): read for the EC$300,000 registration test, the professions that must register, and the late filing and late payment penalties; its rates and deadline are obsolete | https://ird.gov.ag/wp-content/uploads/2020/06/Frequently_asked_questions_ABST.pdf | 2026-11-14 |

Not yet confirmed: whether the EC$300,000 registration threshold and the FAQ penalties (EC$500 or 5%, 10% late payment) have been amended since 2020; the payment deadline after Act 1 of 2024; the weekend and holiday rule; temporary reduced-rate days and the tour operator transition.
