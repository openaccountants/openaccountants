---
name: jo-payroll-social
description: "Conditional Jordan payroll and social security extracts for a 2026 refresh. Covers ordinary full-coverage employment, employer and employee contributions, insured wage limits, legacy wage protection, hazardous-work additions, payment timing and the distinction between source-text penalties and a current assessment. Reads Social Security Law No. 1 of 2014 through its stated 2023 consolidation and the SSC 2026 ceiling announcement. Later amendment currentness, PAYE instructions, reduction rates and portal procedures remain on hold. Use for Jordan payroll research, SSC contribution calculations, employer cost and wage ceilings. Examples require their stated coverage assumptions and do not clear payroll implementation."
version: 1.1
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

**Source currentness hold.** This is a source-cited research draft for the 2026 refresh, not a cleared filing instruction. The clause extracts below are conditional reference material. Before using them for a 2026 position, close the amendment and procedure gaps named in Sources. A read date records the stated read scope, not verification of every later amendment.

Ordinary employment covered by all four insurances under the Social Security Law. The totals below are not universal: establish coverage before calculating, especially for agricultural holdings, partial coverage, government workers, voluntary insureds, hazardous work and approved reductions (arts. 3, 4, 43, 49, 59). Employers register employees with SSC. Employers also withhold income tax on employment income under executive instructions (Income Tax Law art. 12(a)). Income tax bands are in [jo-income-tax](jo-income-tax.md).

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
| Hazardous occupation addition | 1% of wage, employer | On top of other contributions for a profession prescribed as hazardous, art. 64(c)(3)-(4) | same |
| Voluntary insured | 17.5% | Art. 59(a)(3), reached by the yearly steps | same |
| Wage ceiling 2026 | JOD 3,733 | Set from 1.77% inflation; JOD 3,668 in 2025 | https://petra.gov.jo/en/news/ssc-says-jd3733-maximum-wage-for-social-security-deductions |
| Older insured ceiling | JOD 5,000 base | Insured covered before 15 Oct 2009, art. 20(c)(1); qualifying higher pre-date wages stay frozen under art. 20(c)(2), subject to the inflation catch-up in art. 20(c)(3) | https://www.ssc.gov.jo/wp-content/uploads/2025/02/law-26.1.2025-compressed.pdf |
| Maximum net unemployment benefit 2026 | JOD 623 | JOD 612 in 2025 | https://petra.gov.jo/en/news/ssc-says-jd3733-maximum-wage-for-social-security-deductions |
| Minimum wage | unverified | No Ministry of Labour text read | unverified |

## The base

Contributions run on the insured wage up to the ceiling, adjusted each January for inflation (art. 20).

Do not apply a small/medium-firm reduction from this draft: the complete Regulation No. 45 of 2024 rate table and continued eligibility need verification (hold JO-SSC-REDUCTION).

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Pay SSC | Within the first 15 days of the following month, art. 22(a) | https://www.ssc.gov.jo/wp-content/uploads/2025/02/law-26.1.2025-compressed.pdf |
| Remit withheld income tax | Within 30 days of payment, Income Tax Law art. 12(e) | https://www.istd.gov.jo/EBV4.0/Root_Storage/AR/EB_Tenders/%D9%82%D8%A7%D9%86%D9%88%D9%86_%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%AF%D8%AE%D9%84_34_%D9%84%D8%B3%D9%86%D8%A9_2014_%D9%88%D8%AA%D8%B9%D8%AF%D9%8A%D9%84%D8%A7%D8%AA%D9%87.docx |

SSC e-services screens were not read, so no portal steps are given.

## Penalties and interest

The 2023 consolidation states default interest of 1% a month on overdue contributions (art. 22(a)); art. 19(a)(2) starts interest after 60 days from employment. These are source extracts, not a determination of a current penalty assessment. Fine of 1% of due contributions per month for missing art. 21 data (art. 22(b)). The same consolidation states a 30% fine where contributions are not deducted or not paid on real wages (art. 22(c)); currentness is on hold because a 2026 amending bill was found, without a verified enacted text or commencement date. The Board may relieve up to 70% of those fines of art. 22(b)/(c) fines if non-payment or late end-of-service notice arose from circumstances without ill intent, under Board rules published in the Gazette (art. 22(d)).

## Cross-border points

Coverage of foreign or posted workers is not covered here; check SSC coverage rules first.

## Two worked examples that recompute

Simple: ordinary full-coverage worker, wage JOD 1,000; no hazardous surcharge or approved reduction. Employer JOD 142.50 plus employee JOD 75 gives total JOD 217.50.

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

Edge: ordinary full-coverage worker subject to the ordinary 2026 ceiling, wage JOD 5,000. This worker has no protected pre-15 October 2009 wage, hazardous surcharge or approved reduction. Capping at JOD 3,733 gives employer JOD 531.9525 and employee JOD 279.975 before currency rounding. A protected legacy case requires the separate art. 20(c) test.

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
- Whether the worker was insured before 15 Oct 2009, and any wage above JOD 5,000 before that date.

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Security Law No. 1 of 2014, SSC official translation through 16 Apr 2023: arts. 3-7, 19-24, 42-49, 59, 64 read; original Arabic source/pages recorded in closeout ledger | https://www.ssc.gov.jo/wp-content/uploads/2025/02/law-26.1.2025-compressed.pdf | 2026-11-01 |
| Petra, SSC announcement of the 2026 wage ceiling, 14 May 2026 | https://petra.gov.jo/en/news/ssc-says-jd3733-maximum-wage-for-social-security-deductions | 2026-11-01 |
| SSC, Regulation No. 45 of 2024, read by OCR; the rate table in art. 3 did not OCR | https://www.ssc.gov.jo/wp-content/uploads/2024/12/%D9%86%D8%B8%D8%A7%D9%85-%D8%AA%D8%AE%D9%81%D9%8A%D8%B6-%D8%A7%D8%B4%D8%AA%D8%B1%D8%A7%D9%83%D8%A7%D8%AA-%D8%AA%D8%A3%D9%85%D9%8A%D9%86-%D8%A7%D9%84%D8%B4%D9%8A%D8%AE%D9%88%D8%AE%D8%A9-%D9%88%D8%A7%D9%84%D8%B9%D8%AC%D8%B2-%D9%88%D8%A7%D9%84%D9%88%D9%81%D8%A7%D8%A9-%D9%84%D9%84%D8%B9%D8%A7%D9%85%D9%84%D9%8A%D9%86-%D9%81%D9%8A-%D9%85%D9%86%D8%B4%D8%A2%D8%AA-%D8%A7%D9%84%D9%82%D8%B7%D8%A7%D8%B9-%D8%A7%D9%84%D8%AE%D8%A7%D8%B5.pdf | 2026-11-01 |
| Income Tax Law No. 34 of 2014 as amended, ISTD consolidated text: inherited original-author reading of arts. 2, 3, 4 (part), 9 to 12, 17 to 19, 36; closeout reread cached clause output; normal refetch blocked | https://www.istd.gov.jo/EBV4.0/Root_Storage/AR/EB_Tenders/%D9%82%D8%A7%D9%86%D9%88%D9%86_%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%AF%D8%AE%D9%84_34_%D9%84%D8%B3%D9%86%D8%A9_2014_%D9%88%D8%AA%D8%B9%D8%AF%D9%8A%D9%84%D8%A7%D8%AA%D9%87.docx | 2026-11-01 |

Not yet confirmed: minimum wage (the old JOD 260 is out of date; press reports say JOD 290 from 2025 to end 2027 with garments excluded, no official text read); any SSC law amendment after 16 Apr 2023; PAYE instructions; the old "joined on or after 1 May 2010" wording on the ceiling; Regulation 45 art. 3 rates, 25-worker small and 26-50-worker medium definitions, nationality/under-30/no-previous-coverage and owner/partner exclusions and transition conditions (JO-SSC-REDUCTION); original Arabic reading and Gazette commencement of any 2026 amendment (JO-SSC-CURRENT). Do not implement the contribution or penalty extracts until JO-SSC-CURRENT is closed. The Petra ceiling announcement alone does not verify the rest of the law.

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
