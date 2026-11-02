---
name: sc-personal-income-tax
description: "Seychelles personal income tax for tax year 2026: the Income and Non-Monetary Benefits Tax on employment emoluments, for citizens and non-citizens, with sole trader business tax linked to its own skill. Covers monthly bands, the DTAA citizen-rate rule and 183-day test, flat rates, exempt emoluments, bonus and 13th month pay, and refunds. Use for questions such as how much income tax on a Seychelles salary, non-citizen tax rate Seychelles, or GOP holder tax. Source-based; no accountant has signed it."
jurisdiction: SC
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Seychelles Income Tax (employment income) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employed persons paid emoluments in Seychelles, taxed each month on each source of employment. There is no annual personal return for employees in this skill: the employer withholds. Sole traders and partnerships pay business tax, see [Corporate income tax](sc-corporate-income-tax.md). Employer steps are in [Payroll social](sc-payroll-social.md).

Seychelles historically taxes on a territorial basis. The old pack said residents are taxed on worldwide income; no official text read supports that, so it is on the Not yet confirmed line.

## Rates, bands and thresholds

| Item | Amount or rule | Tax year | Official URL |
|---|---|---|---|
| Citizen, up to SCR 8,555.50 a month | 0% | 2026 | https://src.gov.sc/income-and-non-monetary-benefits-tax/ |
| Citizen, SCR 8,555.51 to 10,000 | 15% of the excess over SCR 8,555.50 | 2026 | same |
| Citizen, SCR 10,000.01 to 83,333 | SCR 216.68 plus 20% of the excess over SCR 10,000 (the SRC page prints SCR 216; its brochure and the arithmetic give 216.68) | 2026 | https://src.gov.sc/wp-content/uploads/2022/12/Progressive-Income-Tax-Brochure.pdf |
| Citizen, above SCR 83,333 | SCR 14,883.28 plus 30% of the excess over SCR 83,333 | 2026 | https://src.gov.sc/income-and-non-monetary-benefits-tax/ |
| Non-citizen, up to SCR 10,000 a month | 15% from the first rupee, so no tax-free band | 2026 | https://src.gov.sc/income-and-non-monetary-benefits-tax/ |
| Non-citizen, SCR 10,000.01 to 83,333 | SCR 1,500 plus 20% of the excess over SCR 10,000 | 2026 | same |
| Non-citizen, above SCR 83,333 | SCR 16,166.60 plus 30% of the excess over SCR 83,333 | 2026 | same |
| Non-citizen from a DTAA country present 183 days or more in any 12 months that start or end in the tax year | Citizen rates apply | 2026 | https://src.gov.sc/wp-content/uploads/2022/12/Income-Tax-for-Non-Citizen-Brochure.pdf |
| Specific programme financed by an overseas grant | 3% of the emolument | 2026 | https://src.gov.sc/income-and-non-monetary-benefits-tax/ |
| Stevedore on dock work | Flat 10% of total emoluments | 2026 | same |
| Bonus under a scheme, monthly basic above SCR 8,555.50 | Nil up to 1/12 of annual basic; then 15% up to 15% of annual basic; then 20% | 2026 | https://src.gov.sc/wp-content/uploads/2026/02/SI-26-2024-Income-and-Non-Monetary-Benefits-Tax-Amendment-of-Seychelles-Regulations-2024_0.pdf |
| Bonus under a scheme, monthly basic SCR 8,555.50 or less | Nil up to SCR 8,555.50; then 15% up to 15% of annual basic; then 20% | 2026 | same |
| Thirteenth month pay | Nil up to the amount in Employment Act s 46C(8)(c); 15% on the excess | 2026 | same |

The SRC FAQ prints 0% for non-citizens in the first band. The Income page table and the brochure example (SR 1,500 on the first SR 10,000) both give 15%, and that is used here. The non-citizen brochure prints SR 83,000 for the top band; every other source says 83,333. No 2026 amendment to this rate was found on the SRC legislation list read on 1 Nov 2026, so 2026 rests on the instruments below staying in force.

## The base

The monthly figure is gross emoluments from each employment. Exempt emoluments in the Second Schedule are left out: reimbursement for a company vehicle or own vehicle used for the employer, per diem, shoe allowance, compensation, service charge, retirement pension, gratuity, overtime, end of contract payment, all subject to conditions in the Act. Back pay from 1 January 2023 is spread to the months it belongs to, each taxed at that month's bands. ([SRC](https://src.gov.sc/income-and-non-monetary-benefits-tax/))

## Deadlines and filing

The employer withholds and files, see [Payroll social](sc-payroll-social.md). A DTAA non-citizen overtaxed at non-citizen rates claims through the employer: a formal letter to the Commissioner General, the PIT refund request spreadsheet, the payroll copy if not already given, and each employee's passport, NIN and GOP. The refund goes to the employer's bank account, who passes it on. ([brochure](https://src.gov.sc/wp-content/uploads/2022/12/Income-Tax-for-Non-Citizen-Brochure.pdf))

## Penalties and interest

An employer that fails to withhold or pay is personally liable for the tax and penalties ([SRC](https://src.gov.sc/income-and-non-monetary-benefits-tax/)). Amounts are in [Corporate income tax](sc-corporate-income-tax.md).

## Cross-border points

The citizen-rate rule needs a treaty in force: the list is on the [SRC Agreements page](https://src.gov.sc/agreements/). The 2017 brochure list is shorter than the current page, so use the page. Check the treaty's own employment article as well; those articles were not read for this skill.

## Two worked examples that recompute

Citizen on SCR 12,000 a month: SCR 216.68 in band 2 plus SCR 400 in band 3, SCR 616.68 (the SRC brochure's own scenario).

```oa-check
name: Citizen, SCR 12,000 a month
inputs:
  pay: 12000
steps:
  - band2: (10000 - 8555.5) * 0.15
  - band3: (pay - 10000) * 0.20
  - tax: band2 + band3
expected:
  tax: 616.68
```

Decision: a non-citizen on SCR 12,000 asks whether the 183-day treaty rule is worth claiming. Non-citizen rates give SCR 1,900; citizen rates SCR 616.68. The claim saves SCR 1,283.32 a month, so check country and days.

```oa-check
name: Non-citizen SCR 12,000, treaty claim against none
inputs:
  pay: 12000
steps:
  - noncitizen: 10000 * 0.15 + (pay - 10000) * 0.20
  - citizen: (10000 - 8555.5) * 0.15 + (pay - 10000) * 0.20
  - saving: noncitizen - citizen
expected:
  saving: 1283.32
```

## Ask the client first

- Citizen or non-citizen, and which nationality or residence for treaty purposes?
- Days in Seychelles in the 12-month window?
- Gross monthly emoluments, split by employer?
- Any bonus, 13th month pay or allowance, and under what scheme?
- Grant-funded project or stevedore work?

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for the figures cited: SRC Income and Non-Monetary Benefits Tax page, whole page | https://src.gov.sc/income-and-non-monetary-benefits-tax/ | 2026-11-01 |
| Read for the figures cited: SRC Progressive Income Tax brochure, worked scenarios | https://src.gov.sc/wp-content/uploads/2022/12/Progressive-Income-Tax-Brochure.pdf | 2026-11-01 |
| Read for the figures cited: SRC brochure, Income Tax for non-citizen | https://src.gov.sc/wp-content/uploads/2022/12/Income-Tax-for-Non-Citizen-Brochure.pdf | 2026-11-01 |
| Read for the figures cited: S.I. 26 of 2024, First and Second Schedule changes | https://src.gov.sc/wp-content/uploads/2026/02/SI-26-2024-Income-and-Non-Monetary-Benefits-Tax-Amendment-of-Seychelles-Regulations-2024_0.pdf | 2026-11-01 |
| Read for the figures cited: SRC FAQ, domestic section | https://src.gov.sc/faq/ | 2026-11-01 |
| Read for the figures cited: SRC Agreements page, treaty lists | https://src.gov.sc/agreements/ | 2026-11-01 |

Not yet confirmed: worldwide taxation of residents (old pack claim; the Income and Non-Monetary Benefits Tax Act itself and any residence definition were not read closely enough to state it); whether Seychelles Pension Fund contributions reduce the taxable figure; the current Employment Act s 46C(8)(c) amount; the conditions and caps on each exempt emolument.

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
