---
name: na-income-tax
description: >
  Namibia personal income tax for individuals, year of assessment ending 28 February 2027: seven bands, the N$150,000 retirement cap, provisional tax, returns on ITAS and penalties. Figures come from Namibian law and official pages opened on 2026-11-01. Items that could not be opened are named as not yet confirmed. Not reviewed by a licensed accountant.
version: 0.2
jurisdiction: NA
category: international
tax_year: 2026
tax_year_notes: "Individuals: year of assessment 1 March 2026 to 28 February 2027. Companies: financial year."
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Namibia Personal Income Tax v0.2

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. Do not rely on it to file, pay or take a position without review by a qualified professional in Namibia.

Year of assessment: 1 March 2026 to 28 February 2027. The annotated Income Tax Act read runs to Income Tax Amendment Act 4 of 2024. The 2025 and 2026 gazette indexes list no Income Tax or VAT amendment act.

## Who this applies to

Individuals, deceased estates and trusts ([NamRA](https://www.namra.org.na/tax-types/page/income-tax/)). Namibia taxes income from a source within or deemed within Namibia (s.15, [Act](https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf)), and the bands apply whether or not the person is resident. An employee with salary above N$100,000 a year registers and gives proof to the employer ([NamRA](https://www.namra.org.na/individual-tax/page/i-earn-a-monthly-salary/)). Anyone with over N$50,000 a year of non-remuneration taxable income, farmers, and directors of private companies and members of close corporations register as provisional taxpayers ([NamRA](https://www.namra.org.na/individual-tax/page/i-am-a-provisional-taxpayer/)).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Taxable amount to N$100,000 | No tax | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (Schedule 4 para 1) |
| N$100,001 to N$150,000 | 18% above N$100,000 | 2026 | same |
| N$150,001 to N$350,000 | N$9,000 + 25% above N$150,000 | 2026 | same |
| N$350,001 to N$550,000 | N$59,000 + 28% above N$350,000 | 2026 | same |
| N$550,001 to N$850,000 | N$115,000 + 30% above N$550,000 | 2026 | same |
| N$850,001 to N$1,550,000 | N$205,000 + 32% above N$850,000 | 2026 | same |
| Above N$1,550,000 | N$429,000 + 37% above N$1,550,000 | 2026 | same |
| Retirement, provident, annuity and education policy deductions together | N$150,000 cap, from years starting 1 March 2022 | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.17(2)) |
| Lump sum exemption | N$300,000 lifetime, conditions in s.16(1)(o) | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf |
| Company car fringe benefit | 1.5% if employer pays all costs; 1.4% if employee pays fuel | Page undated | https://www.namra.org.na/individual-tax/page/i-earn-a-monthly-salary/ |
| Housing allowance | Taxable; one third exempt under an approved scheme | Page undated | same |

NamRA's salary page still shows a N$40,000 cap. Its own brochure and s.17(2) say N$150,000. The statute wins.

## The base

Gross income less exemptions and deductions. Income from several sources is combined for the rate. A withdrawal from a pension or provident fund is fully taxed; transfer to a preservation fund defers tax to withdrawal ([NamRA](https://www.namra.org.na/individual-tax/page/i-earn-a-monthly-salary/)). Farmers state animals held on 1 March and 28 February in the return. Assessed losses: see the [company skill](na-corporate-income-tax.md); s.21A ring-fences repeated trade losses where income before the rule is N$200,000 or more. Married persons: excess income from a spouse's trade is deemed the other spouse's (Schedule 4 para 2).

## Deadlines and filing

| Who | Return and payment | Law |
|---|---|---|
| No business, profession or farming income | Last day of June after year end: 30 June 2027 | s.56(1A)(a) |
| Business, profession or farming income | Last day of 7th month: 30 September 2027 | s.56(1A)(b) |
| Provisional, first | Within 6 months of 1 March: half of estimated tax less PAYE | Sch 2 para 22(1)(a) |
| Provisional, second | By 28 February: full estimate less PAYE and first payment | Sch 2 para 22(1)(b) |
| Farmers under a Minister's direction | One payment by the last day of the year | Sch 2 para 23 |

Six months from 1 March ends on 31 August. NamRA's page says 30 August, so pay by 30 August to be safe under both.

How to file: ITAS registration ([NamRA brochure](https://www.namra.org.na/documents/cms/uploaded/information-brochure--how-to-register-on-itas-ce02d8af03.pdf)): 1. Go to https://itas.namra.org.na and choose to register. 2. Create a username and password and give a valid email. 3. Activate through the emailed link. 4. Log in and link your taxpayer account. 5. Complete the mandatory fields and submit. Then file the self-assessment return with a computation of tax (s.56(1)). Payment ([NamRA](https://www.namra.org.na/documents/cms/uploaded/information-brochure--tax-payments-325a997127.pdf)): EFT, direct deposit, cash or point of sale. The reference is payment type, registration office, taxpayer number, tax type and tax period. Tax type 11 is income tax; its period is the year plus a 2-digit value, "00" for final income tax. NamRA's pages opened do not give the step-by-step return screens, and individual return boxes are not on them.

## Penalties and interest

Late payment: interest 20% a year from the day after the due date (s.79(2), https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf). Failure to render a return: additional tax up to twice the tax chargeable, less amounts paid (s.66(1)(a)). Omission or incorrect statement: twice the shortfall (s.66(1)(b), (c)). The Minister may remit (s.66(2)), but not where there was intent to evade unless circumstances were extenuating. Late provisional tax: penalty 10% per month or part, capped at the unpaid tax (Sch 2 para 28) plus interest 20% (s.80(2), interest capped at the original tax by s.80(5)). Missing provisional estimate: N$100 per day (Sch 2 para 21). Under-estimate below 80% of final taxable income: additional tax up to 100% of the shortfall (Sch 2 para 20). The tax amnesty extension ran to 31 October 2026 (https://www.namra.org.na/tax-amnesty); it is over unless NamRA extends it again.

## Cross-border points

Non-residents pay the same bands on Namibian-source income. Withholding on payments to non-residents is in the [cross-border skill](na-cross-border.md).

## Two worked examples that recompute

Example 1. Taxable amount N$400,000: N$59,000 + 28% of N$50,000 = N$73,000.

```oa-check
name: Salaried N$400,000
inputs:
  t: 400000
steps:
  - tax: 59000 + (t - 350000) * 0.28
expected:
  tax: 73000.00
```

Example 2. A decision: contribute N$180,000 or N$150,000 to retirement funds on income of N$900,000? The cap stops at N$150,000, so the extra N$30,000 saves nothing. Taxable N$750,000: N$115,000 + 30% of N$200,000 = N$175,000.

```oa-check
name: Retirement cap
inputs:
  i: 900000
  c: 180000
steps:
  - d: min(c, 150000)
  - t: i - d
  - tax: 115000 + (t - 550000) * 0.30
expected:
  tax: 175000.00
```

## Ask the client first

1. Salary only, or business, profession or farming income?
2. Director of a private company or member of a CC?
3. Source of each income stream?
4. Retirement, annuity and education policy contributions?
5. Fringe benefits?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 24 of 1981, annotated to Act 4 of 2024 (read: Schedule 4, ss.6, 15, 16, 17, 21, 21A, 56, 66, 79, 80, Schedule 2 Part III) | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf | 2026-11-01 |
| NamRA salary page (read: whole page) | https://www.namra.org.na/individual-tax/page/i-earn-a-monthly-salary/ | 2026-11-01 |
| NamRA provisional page (read: whole page) | https://www.namra.org.na/individual-tax/page/i-am-a-provisional-taxpayer/ | 2026-11-01 |
| NamRA income tax page (read: whole page) | https://www.namra.org.na/tax-types/page/income-tax/ | 2026-11-01 |
| NamRA ITAS brochure (read: whole) | https://www.namra.org.na/documents/cms/uploaded/information-brochure--how-to-register-on-itas-ce02d8af03.pdf | 2026-11-01 |
| NamRA tax payments brochure (read: whole) | https://www.namra.org.na/documents/cms/uploaded/information-brochure--tax-payments-325a997127.pdf | 2026-11-01 |
| NamRA tax amnesty (read: whole page) | https://www.namra.org.na/tax-amnesty | 2026-11-01 |

Not yet confirmed: Budget 2026/27 proposals (mof.gov.na refused plain fetch and the browser read failed); any Income Tax Amendment Act passed after the LAC index was last updated; ITAS return screens and box numbers.

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
