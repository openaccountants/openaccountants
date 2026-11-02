---
name: gq-payroll-social
description: >
  Payroll in Equatorial Guinea for tax year 2026. Covers employer withholding of Impuesto sobre Sueldos y Salarios under Ley 1/2024 General Tributaria, the monthly return and form, the annual pay statement, benefits in kind, exceptional pay, non-resident staff, and INSESO and Work Protection Fund contributions. Use for questions such as how do I run payroll in Equatorial Guinea, when is salary tax due, what form do I use, what are INSESO rates, how are expatriates taxed, and how are benefits valued. Applies to employers, public bodies, international organisations and diplomatic missions paying staff. Social contribution rates could not be read from an official source and are marked unverified.
jurisdiction: GQ
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Equatorial Guinea Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone paying taxable pay, including State bodies, local bodies, companies, individuals, international organisations and missions (art 132.1). Scale, residence and benefits are owned by [Income tax](gq-income-tax.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Salary tax | Scale in the income tax skill (art 130) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Non-resident pay | 15% of gross (art 130.3) | 2026 | same |
| Employer INSESO | unverified: 21.5% of gross salary, carried from the old skill | 2026 | unverified |
| Employer Work Protection Fund | unverified: 1% of gross salary | 2026 | unverified |
| Employee INSESO | unverified: 4.5% of net salary; deductible for salary tax (art 129.2) | 2026 | unverified |
| Employee Work Protection Fund | unverified: 0.5% of net salary; deductible for salary tax (art 129.3) | 2026 | unverified |
| Totals | unverified: 22.5% employer, 5% employee | 2026 | unverified |
| Contribution ceiling | unverified: none found | 2026 | unverified |

## The base

Net pay plus cash and in-kind benefits (art 128). Deductions are in art 129. Employer mutual fund premiums are taxable unless they benefit all staff (art 128.3). No other exemption can be given as a hiring incentive (art 125.3).

## Deadlines and filing

Steps each month:

1. Work out pay, benefits and deductions per person; apply the scale on an annual basis.
2. Complete form code [0720](https://minhacienda-gob.com/uploads/2025/10/IMP.SUELDOS-Y-SALARIOS_SEC.COMUN_.pdf) (common sector) or 0820 (oil and mining): tax withheld in the month, surcharge, interest, total.
3. Pay at a Treasury bank by day 15 of the following month (art 132.1).
4. Lodge the form, bank proof and the payee file at the Ministry: name, address, contact, type and amount of pay, benefits, tax withheld and number of dependent children, up to 10 under 25 (art 132.2).

Annually, attach the pay statement to the DEF: each employee's details, taxable pay, benefits, allowances and tax (art 32).

The old note that contributions go to the tax authority within 15 days is unverified for INSESO.

## Penalties and interest

Surcharges under art 410 and interest under art 412, shown on form 0720. Oil and mining form 0820 uses art 315: 35% late, 100% for failure to withhold, 150% for not paying over, with 5% monthly interest.

## Cross-border points

Resident staff working abroad are taxed here; non-residents are taxed on work done here or paid from here (art 126). Expatriate pension withholdings are deductible up to 50% of the employee's social security contribution (art 129.1).

## Two worked examples that recompute

**Employee, annual pay 10,000,000 XAF, employee contributions 500,000.** Taxable 9,500,000. Tax 360,000 plus 15% of 4,500,000 is 1,035,000, or 86,250 a month.

```oa-check
name: Monthly withholding
inputs:
  pay: 10000000
  contrib: 500000
steps:
  - net: pay - contrib
  - tax: 360000 + (net - 5000000) * 0.15
  - month: tax / 12
expected:
  net: 9500000
  tax: 1035000
  month: 86250
```

**Decision: resident or non-resident, gross 10,000,000 XAF, no contributions.** Resident: 1,110,000. Non-resident at 15%: 1,500,000. Passing 183 days or taking a permanent home lowers the tax at this pay by 390,000.

```oa-check
name: Resident against non-resident
inputs:
  pay: 10000000
steps:
  - resident: 360000 + (pay - 5000000) * 0.15
  - non_resident: pay * 0.15
  - gap: non_resident - resident
expected:
  resident: 1110000
  non_resident: 1500000
  gap: 390000
```

## Ask the client first

1. Common sector, or oil and mining?
2. Staff residence and days in the country?
3. Pay and benefits per person?
4. Directors on the payroll?
5. INSESO registration in place?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 1/2024 General Tributaria, Boletin Oficial del Estado scan, read by OCR; arts 32, 124 to 133, 315, 410, 412 read | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf | 2026-11-01 |
| Ministry of Finance, tax return forms page, list read | https://minhacienda-gob.com/formularios-de-declaraciones-fiscales | 2026-11-01 |
| Government press office, 13 Jan 2025 presentation, read in full (filing route) | https://www.guineaecuatorialpress.com/noticias/presentacion_oficial_de_la_nueva_ley_general_tributaria_de_guinea_ecuatorial | 2026-11-01 |
| Salary tax form, common sector, read | https://minhacienda-gob.com/uploads/2025/10/IMP.SUELDOS-Y-SALARIOS_SEC.COMUN_.pdf | 2026-11-01 |

The law is a scan with no text layer: figures were read from machine OCR, and the salary scale from the page image. It applies to tax year 2026; the 2026 Budget Law (Ley 9/2025) changes it only where stated.

Not yet confirmed: all INSESO and Work Protection Fund rates, ceilings and deadlines (carried from the old skill, no official text found; boe.gob.gq searches returned none; the INSESO site did not open); minimum wage; employee base of net against gross.

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
