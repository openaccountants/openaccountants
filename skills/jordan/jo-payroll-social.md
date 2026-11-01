---
name: jo-payroll-social
description: "Payroll and social security contributions in Jordan for tax year 2026: employers, employees and voluntary insureds with the Social Security Corporation (SSC). Covers the 14.25% employer and 7.5% employee rates built from Social Security Law No. 1 of 2014 articles 24, 42, 48 and 59, the JOD 3,733 wage ceiling for 2026, the 1% hazardous occupation addition, monthly payment within 15 days, default interest and fines, the small firm reduction for young workers, and income tax withholding on salaries. Use when asked what an employer pays in Jordan, the SSC ceiling, or payroll deadlines. Trigger phrases: Jordan payroll, Jordan social security rate, SSC contributions, Jordan employer cost, Jordan wage ceiling."
version: 1.0
jurisdiction: JO
category: payroll
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Jordan Payroll and Social Contributions

## Who this applies to

Firms employing insured workers and those workers, under the Social Security Law. Employers register employees with SSC. Employers also withhold income tax on employment income under executive instructions (Income Tax Law art. 12(a)). Income tax bands are in [jo-income-tax](jo-income-tax.md).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Old age, disability, death, employer | 11% | Art. 59(a)(1), reached by the yearly steps | https://www.ssc.gov.jo/wp-content/uploads/2025/02/law-26.1.2025-compressed.pdf |
| Old age, disability, death, employee | 6.5% | Art. 59(a)(2), reached by the yearly steps | same |
| Work injury, employer | 2% | Art. 24(a) | same |
| Maternity, employer | 0.75% | Art. 42(a)(1) | same |
| Unemployment, employer | 0.5% | Art. 48(a) | same |
| Unemployment, employee | 1% | Art. 48(b) | same |
| Employer total | 14.25% | Sum of the above | same |
| Employee total | 7.5% | Sum of the above | same |
| Total | 21.75% | Sum of the above | same |
| Hazardous occupation addition | 1% of wage, employer | On top of other contributions, early retirement article | same |
| Voluntary insured | 17.5% | Art. 59(a)(3), reached by the yearly steps | same |
| Wage ceiling 2026 | JOD 3,733 | Set from 1.77% inflation; JOD 3,668 in 2025 | https://petra.gov.jo/en/news/ssc-says-jd3733-maximum-wage-for-social-security-deductions |
| Older insured ceiling | JOD 5,000 base | Insured above that wage before 15 Oct 2009; read art. 20 for the case | https://www.ssc.gov.jo/wp-content/uploads/2025/02/law-26.1.2025-compressed.pdf |
| Maximum net unemployment benefit 2026 | JOD 623 | JOD 612 in 2025 | https://petra.gov.jo/en/news/ssc-says-jd3733-maximum-wage-for-social-security-deductions |
| Minimum wage | unverified | No Ministry of Labour text read | unverified |

## The base

Contributions run on the insured wage up to the ceiling, adjusted each January for inflation (art. 20).

Regulation No. 45 of 2024 lets private firms of up to 25 workers (small) and 26 to 50 workers (medium) apply to reduce the old age contribution for Jordanian insureds under 30 with no prior mandatory coverage, not owners or working partners. A firm that grows to large keeps it for those already covered (https://www.ssc.gov.jo/wp-content/uploads/2024/12/%D9%86%D8%B8%D8%A7%D9%85-%D8%AA%D8%AE%D9%81%D9%8A%D8%B6-%D8%A7%D8%B4%D8%AA%D8%B1%D8%A7%D9%83%D8%A7%D8%AA-%D8%AA%D8%A3%D9%85%D9%8A%D9%86-%D8%A7%D9%84%D8%B4%D9%8A%D8%AE%D9%88%D8%AE%D8%A9-%D9%88%D8%A7%D9%84%D8%B9%D8%AC%D8%B2-%D9%88%D8%A7%D9%84%D9%88%D9%81%D8%A7%D8%A9-%D9%84%D9%84%D8%B9%D8%A7%D9%85%D9%84%D9%8A%D9%86-%D9%81%D9%8A-%D9%85%D9%86%D8%B4%D8%A2%D8%AA-%D8%A7%D9%84%D9%82%D8%B7%D8%A7%D8%B9-%D8%A7%D9%84%D8%AE%D8%A7%D8%B5.pdf). The percentages were not readable.

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Pay SSC | Within the first 15 days of the following month, art. 22(a) | https://www.ssc.gov.jo/wp-content/uploads/2025/02/law-26.1.2025-compressed.pdf |
| Remit withheld income tax | Within 30 days of payment, Income Tax Law art. 12(e) | https://www.istd.gov.jo/EBV4.0/Root_Storage/AR/EB_Tenders/%D9%82%D8%A7%D9%86%D9%88%D9%86_%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%AF%D8%AE%D9%84_34_%D9%84%D8%B3%D9%86%D8%A9_2014_%D9%88%D8%AA%D8%B9%D8%AF%D9%8A%D9%84%D8%A7%D8%AA%D9%87.docx |

SSC e-services screens were not read, so no portal steps are given.

## Penalties and interest

Default interest 1% a month on overdue contributions (art. 22(a)). Fine of 1% of due contributions per month for missing art. 21 data (art. 22(b)). Fine of 30% where contributions are not deducted or not paid on real wages (art. 22(c)). The Board may relieve up to 70% of those fines where no ill intent exists (art. 22(d)).

## Cross-border points

Coverage of foreign or posted workers is not covered here; check SSC coverage rules first.

## Two worked examples that recompute

Simple: wage JOD 1,000.

```oa-check
name: Wage JOD 1,000
inputs:
  wage: 1000
steps:
  - employer: wage * 0.1425
  - employee: wage * 0.075
  - total: employer + employee
expected:
  employer: 142.50
  employee: 75.00
  total: 217.50
```

Edge: wage JOD 5,000, capped at JOD 3,733.

```oa-check
name: Wage above the 2026 ceiling
inputs:
  wage: 5000
steps:
  - base: min(wage, 3733)
  - employer: base * 0.1425
  - employee: base * 0.075
expected:
  employer: 531.95
  employee: 279.98
```

## Ask the client first

- Wage and start date.
- Headcount of the firm.
- Age, nationality and prior coverage of the worker.
- Hazardous occupation or not.
- Wage history above JOD 5,000 before 15 Oct 2009.

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Security Law No. 1 of 2014, SSC English text (amendments to 16 Apr 2023): arts. 20, 22, 24, 42, 48, 59 read | https://www.ssc.gov.jo/wp-content/uploads/2025/02/law-26.1.2025-compressed.pdf | 2026-11-01 |
| Petra, SSC announcement of the 2026 wage ceiling, 14 May 2026 | https://petra.gov.jo/en/news/ssc-says-jd3733-maximum-wage-for-social-security-deductions | 2026-11-01 |
| SSC, Regulation No. 45 of 2024, read by OCR; the rate table in art. 3 did not OCR | https://www.ssc.gov.jo/wp-content/uploads/2024/12/%D9%86%D8%B8%D8%A7%D9%85-%D8%AA%D8%AE%D9%81%D9%8A%D8%B6-%D8%A7%D8%B4%D8%AA%D8%B1%D8%A7%D9%83%D8%A7%D8%AA-%D8%AA%D8%A3%D9%85%D9%8A%D9%86-%D8%A7%D9%84%D8%B4%D9%8A%D8%AE%D9%88%D8%AE%D8%A9-%D9%88%D8%A7%D9%84%D8%B9%D8%AC%D8%B2-%D9%88%D8%A7%D9%84%D9%88%D9%81%D8%A7%D8%A9-%D9%84%D9%84%D8%B9%D8%A7%D9%85%D9%84%D9%8A%D9%86-%D9%81%D9%8A-%D9%85%D9%86%D8%B4%D8%A2%D8%AA-%D8%A7%D9%84%D9%82%D8%B7%D8%A7%D8%B9-%D8%A7%D9%84%D8%AE%D8%A7%D8%B5.pdf | 2026-11-01 |
| Income Tax Law No. 34 of 2014 as amended, ISTD consolidated text: arts. 2, 3, 4 (part), 9 to 12, 17 to 19, 36 read | https://www.istd.gov.jo/EBV4.0/Root_Storage/AR/EB_Tenders/%D9%82%D8%A7%D9%86%D9%88%D9%86_%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%AF%D8%AE%D9%84_34_%D9%84%D8%B3%D9%86%D8%A9_2014_%D9%88%D8%AA%D8%B9%D8%AF%D9%8A%D9%84%D8%A7%D8%AA%D9%87.docx | 2026-11-01 |

Not yet confirmed: minimum wage (the old JOD 260 is out of date; press reports say JOD 290 from 2025 to end 2027 with garments excluded, no official text read); any SSC law amendment after 16 Apr 2023; PAYE instructions; the old "joined on or after 1 May 2010" wording on the ceiling; Regulation 45 art. 3 rates.

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
