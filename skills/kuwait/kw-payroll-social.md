---
name: kw-payroll-social
description: "Payroll intake and social contribution verification in Kuwait for tax year 2026. Covers the income-tax exemption for a natural person's own work, the exception for income representing a corporate body's share, and the evidence needed before payroll can be calculated. Use for Kuwait salary tax, PIFSS contributions, insured salary, employer cost, GCC insurance extension and end-of-service indemnity questions. Contribution rates, ceilings, remittance dates, nationality coverage and indemnity formulas are held as unverified source gaps. Worked cases separate the verified income-tax component from contribution amounts supplied in an employer's records. This Guide does not authorise a payroll run without those missing checks."
version: 0.3
jurisdiction: KW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Payroll and Social Contributions v0.3

Tax year 2026.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers checking Kuwait payroll. The confirmed income-tax rule covers a natural person's income from trade or work in Kuwait, unless it represents a corporate body's share (Executive Regulations of Law 2 of 2008, art. 8). It does not establish social-insurance or indemnity exemptions by nationality.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Income tax on a person's own salary | Exempt under art. 8(2), unless the income represents a corporate body's share | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| PIFSS rates, insured salary and due dates | unverified: NON-OPERATIVE HOLD. Do not use the historical rates or ceiling in Sources | 2026 | unverified |
| Nationality coverage and indemnity | unverified: NON-OPERATIVE HOLD. No zero contribution or gratuity conclusion is authorised | 2026 | unverified |

## The base

Identify the legal recipient of each payment before applying art. 8. Keep gross pay, any confirmed employee deductions, employer contributions and indemnity accrual separate. No contribution base is established here.

## Deadlines and filing

PIFSS service entry point: https://www.pifss.gov.kw. The current remittance form, procedure and deadline have not been verified. Obtain the employee's coverage confirmation and current assessment, reconcile them to payroll, and retain the evidence. Do not submit or release payroll using the held figures.

## Penalties and interest

Unverified: PIFSS and labour-law penalties. No penalty calculation is authorised.

## Cross-border points

The natural-person income-tax exemption does not decide foreign tax, GCC insurance extension, non-GCC coverage or employer indemnity. Refer each of those questions for the current source and the employee's facts.

## Two worked examples that recompute

**Example 1.** An employee receives KWD 2,000 as their own salary, not a corporate body's share. Art. 8(2) exempts that salary from Kuwait income tax. The income-tax component is zero. KWD 2,000 remains before social deductions; this is not approved net pay.

```oa-check
name: Own salary, income-tax component only
inputs:
  salary: 2000
steps:
  - income_tax: salary * 0
  - before_social_deductions: salary - income_tax
expected:
  income_tax: 0.00
  before_social_deductions: 2000.00
```

**Example 2 (decision).** A payroll record specifies gross salary KWD 3,000, an employee deduction of KWD 200 and employer contribution of KWD 250 for that month. Reconcile the supplied amounts: net cash KWD 2,800 and employer cash cost KWD 3,250. The KWD 200 and KWD 250 are example document inputs, not legal rates. Release only after their current legal basis and coverage are checked. If the supporting assessment is missing, hold the payroll rather than assume expatriate contributions are zero or apply historical percentages.

```oa-check
name: Reconcile documented payroll amounts before release decision
inputs:
  gross_salary: 3000
  documented_employee_deduction: 200
  documented_employer_contribution: 250
steps:
  - net_cash: gross_salary - documented_employee_deduction
  - employer_cash_cost: gross_salary + documented_employer_contribution
expected:
  net_cash: 2800.00
  employer_cash_cost: 3250.00
```

## Ask the client first

- Employee nationality and current insurance coverage confirmation?
- Gross pay, allowances and the current insured-salary assessment?
- Private or public sector and the employment contract?
- Length of service, termination reason and current indemnity assessment?

## Sources

| Source | URL | Read on |
|---|---|---|
| Executive Regulations of Law 2 of 2008, art. 8(2), with arts. 1 to 3 and 9 to 14; Arabic OCR read and PDF page 8 visually checked | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf | 2026-11-01 |

Not yet confirmed: NON-OPERATIVE HOLDS. Social Security Law 61 of 1976 and amendments; historical employer 11.5%, employee basic 8% plus additional 2.5% (10.5% total), KWD 2,750 monthly ceiling, claimed remittance by the following month's 15th; no current statutory text read supports using these. Historical claims that non-GCC expatriates are outside PIFSS, GCC nationals use home-state schemes, and social insurance applies only to Kuwaiti nationals are not operational conclusions. Labour Law 6 of 2010: historical 15 days per year for the first five years, then one month per year, all calculation caps and entitlement conditions, not verified. Current PIFSS penalties and any unemployment contribution. Prior writer reports only PIFSS homepage opened and manpower.gov.kw failed on 2026-11-01; those are access reports, not law readings. Historical calculation examples KWD 2,000 yielding employer 230/employee 210 and KWD 3,000 yielding employer 316.25, and the Kuwaiti-versus-expatriate hiring comparison, are withdrawn from operative use pending those checks.

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
