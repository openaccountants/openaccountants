---
name: sz-payroll-social
description: "Eswatini Payroll and Social Contributions for tax year 2026: rates, deadlines, how to file and worked examples, from official Eswatini sources. Use for questions about payroll and social contributions in Eswatini, ERS, TaxEase, emalangeni or SZL. Covers who it applies to, conditions and penalties. Items that official sources could not settle are listed as not yet confirmed."
jurisdiction: SZ
category: payroll
tax_year: 2026
tax_year_notes: "Year of assessment to 30 June 2026"
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eswatini Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers in Eswatini and their employees. PAYE runs on the year 1 July to 30 June. ENPF runs on the calendar year. Non-citizens are not eligible for ENPF, and employers of domestic workers are exempt from registering.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| ENPF wage level 2026 | E4,300 a month, from 1 January 2026, Legal Notice 5 of 2025 | 2026 | https://enpf.co.sz/ |
| ENPF maximum 2026 | E430 a month: E215 employee, E215 employer | 2026 | https://enpf.co.sz/ |
| ENPF rate | 5% each, derived from E215 on E4,300. The rate wording itself was not seen | 2026 | https://enpf.co.sz/ |
| ENPF other years | E4,000 in 2025 (maximum E400 a month), E4,600 in 2027, E4,900 in 2028, E5,200 in 2029 | 2026 | https://enpf.co.sz/ |
| ENPF payment | Within 21 days after the end of the month (s 14(3)) | 2026 | http://enpf.co.sz/wp-content/uploads/2021/03/The-SNPF-Order-of-1974-1.pdf |
| PAYE bands | Annual table in [Income tax](sz-income-tax.md); rebate E683.33 a month | 2026 | https://www.ers.org.sz/IncomeTax/Paye |
| PAYE return and payment | Within 7 days after month-end (Fourth Schedule para 14(2) as amended). The ERS guide says the 14th; the Act wins | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Late PAYE | 20% penalty plus 18% interest a year | 2026 | https://www.ers.org.sz/IncomeTax/Paye |
| Failure to file the monthly return | E200 a day | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| PAYE reconciliation | By 30 September. Late: E30 a day | 2026 | https://www.ers.org.sz/documents/Step-ByStepGuideforNewBusinesses.pdf |

## The base

PAYE base: gross salary, benefits and commission, less statutory deductions (ENPF) and pension contributions. Annualise, apply the bands, take the rebate, divide by 12. Employers must use the Employees' Tax Deduction Tables and may not deduct less. An ENPF-eligible citizen stays eligible when sent abroad if ordinarily resident. Exempt groups include government pension members, full-time students in vacation work and domestic servants.

## Deadlines and filing

### How to run a month
1. Register as an employer with ERS and with ENPF.
2. Compute PAYE and ENPF, and pay the net wage.
3. File Form PAYE 04 on e-Tax with proof of payment by the 7th, and reference the payment separately.
4. Pay ENPF within 21 days of month-end.
5. By 30 September, file the PAYE reconciliation and issue tax certificates.

ERS allocates payments to penalty, then interest, then tax.

## Penalties and interest

See the table. Employers are personally liable for employees' tax. An employer and employee cannot agree to skip it. ERS may estimate tax on non-filing.

## Cross-border points

Non-citizens stay in PAYE but outside ENPF. The Eswatini National Pension Fund Bill, 2025 was gazetted on 10 July 2025 as a Bill. It would change the scheme and a 7-day payment rule; no enactment was found, so this skill does not apply it.

## Two worked examples that recompute

Wage E10,000 a month.

```oa-check
name: Monthly wage E10,000
inputs:
  wage: 10000
steps:
  - enpf: min(wage, 4300) * 0.05
  - annual: (wage - enpf) * 12
  - tax: 20000 + (annual - 100000) * 0.25 - 8200
  - paye: tax / 12
expected:
  enpf: 215
  annual: 117420
  paye: 1346.25
```

Low wage E3,000: the rebate clears the tax, so only ENPF applies. Decision: tax is nil while annual taxable income stays at or below E41,000.

```oa-check
name: Monthly wage E3,000
inputs:
  wage: 3000
steps:
  - enpf: min(wage, 4300) * 0.05
  - annual: (wage - enpf) * 12
  - gross: annual * 0.20
  - tax: max(gross - 8200, 0)
expected:
  enpf: 150
  annual: 34200
  tax: 0
```

## Ask the client first

1. Is the employee a citizen, and in an exempt group?
2. What are gross pay and benefits?
3. Is there a pension fund?
4. Is the worker on a part-year?
5. Does the person have a second employer?

## Sources

| Source | URL | Read on |
|---|---|---|
| ENPF home page, public notice reproducing Legal Notice 5 of 2025; whole page read | https://enpf.co.sz/ | 2026-11-01 |
| ENPF, Employers; whole page read | https://enpf.co.sz/employers/ | 2026-11-01 |
| National Provident Fund Order 1974, ss 14 to 17; cited sections read | http://enpf.co.sz/wp-content/uploads/2021/03/The-SNPF-Order-of-1974-1.pdf | 2026-11-01 |
| ERS, PAYE Quick Guide; whole page read | https://www.ers.org.sz/IncomeTax/Paye | 2026-11-01 |
| Income Tax (Amendment) Act 2023 (Act 20 of 2023); scanned, read by OCR, Third Schedule pages checked by eye; cited sections read | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf | 2026-11-01 |
| ERS, Step-by-Step Guide for New Businesses; whole page read | https://www.ers.org.sz/documents/Step-ByStepGuideforNewBusinesses.pdf | 2026-11-01 |

Not yet confirmed: The ENPF percentage wording, employee share order and late-payment charge. Whether the National Pension Fund Bill has been enacted. Graded tax from the old pack: no official source found for its current status or amount. Commencement of the 2023 Act rests on the ERS Presumptive Tax page.

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
