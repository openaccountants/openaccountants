---
name: eg-social-insurance
description: Use this skill for Egypt social insurance contributions in tax year 2026 for an employee, employer, or self-employed business owner, professional, craftsman, merchant, farmer, freelancer, company director, Egyptian abroad or irregular worker. Trigger on "Egypt social insurance", "التأمينات الاجتماعية", "social insurance contributions Egypt", "self-employed social insurance Egypt", "Law 148 2019", "NOSI", "insurance wage Egypt", "comprehensive social insurance scheme" or "تأمين أصحاب الأعمال". It covers rates by branch, the 2026 wage band, payment, forms, late charges and fines. Read this skill before any Egypt social insurance work. Salary tax sits in eg-payroll.
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt Social Insurance v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar 2026. Amounts are EGP. Governed by the Social Insurance and Pensions Law 148 of 2019, administered by the National Organization for Social Insurance (NOSI, الهيئة القومية للتأمين الاجتماعي). Reply in the user's language.

## Who this applies to

Art. 2 of [Law 148/2019](https://www.nosi.gov.eg/ar/Lists/NOSILibrary/2-12-2019%20%D9%83%D8%AA%D8%A7%D8%A8%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF.pdf) sets four groups:

- **First, employees (العاملون لدى الغير):** government and public bodies; public and business sector units; private sector workers under the Labour Law with a regular work relationship (contract, shipping, transport, fishing workers are excepted from that test); household service work, except those working inside homes; family of the employer who work for and are supported by the employer. Age 18 or over for items 3, 4, 5. With two employers, only the period with one counts.
- **Second, employers and similar (أصحاب الأعمال ومن في حكمهم):** sole traders, industrial and farming owners, craftsmen; general partners; managing partners and elected board members in private joint stock companies; managers in limited liability companies; single-member company owners; liberal professions and syndicate members from the date NOSI's head sets; transport vehicle owners; commercial agents; authors and artists; tour guides; others listed. Age 21 or over and not in group first.
- **Third, Egyptians working abroad** under personal contracts, for themselves, as emigrants who keep nationality, or as seafarers on foreign flag ships, age 18 or over and not in groups first or second.
- **Fourth, irregular workers (العمالة غير المنتظمة).**

Unemployment cover excludes casual and temporary work, contract, seasonal, shipping, transport, farm and fishing workers, and applies only under the retirement age (arts. 85, 86).

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Minimum insurance wage | EGP 2,700 a month | 2026 | From 1 January 2026; was 2,300 | https://www.nosi.gov.eg/ar/news/Pages/2025-11-30.aspx |
| Maximum insurance wage | EGP 16,700 a month | 2026 | From 1 January 2026; was 14,500 | same |
| Old age, disability, death, employer | 12% | 2026 | Group first; art. 19(1)(a) | https://www.nosi.gov.eg/ar/Lists/NOSILibrary/2-12-2019%20%D9%83%D8%AA%D8%A7%D8%A8%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF.pdf |
| Old age, disability, death, employee | 9% | 2026 | Group first; art. 19(1)(b) | same |
| Reward system, employer | 1% | 2026 | Group first; art. 36 | same |
| Reward system, employee | 1% | 2026 | Group first; art. 36, paid into a personal account | same |
| Work injury, medical | 1% employer | 2026 | Not under comprehensive health insurance; art. 46(1) | same |
| Work injury, cash rights | 0.5% employer | 2026 | Can rise to 1% by activity risk; art. 46(2) | same |
| Sickness, employer | 3.25% | 2026 | Private sector items 3, 4, 5; art. 70. Government and public sector: 3% | same |
| Sickness, employee | 1% | 2026 | Art. 70 | same |
| Unemployment, employer | 1% | 2026 | Arts. 85 and 86 scope | same |
| Total employee, private sector | 11% | 2026 | 9 + 1 + 1, computed from the rows above | same |
| Total employer, private sector | 18.75% | 2026 | 12 + 1 + 1.5 + 3.25 + 1, at the 0.5% injury rate and not under comprehensive health insurance | same |
| Employers, self-employed, Egyptians abroad | 21% of chosen contribution income | 2026 | Groups second and third; art. 19(2). NOSI table, between the minimum and maximum (art. 1(9)) | same |
| Irregular workers | 9% of the minimum by the worker, 12% of the minimum by the Treasury | 2026 | Group fourth; art. 19(3). At 2,700: 243 and 324 | same |
| Scheduled rise | 1% every seven years from commencement, split equally, cap 26% | Next: see Not yet confirmed | Art. 19, last paragraph | same |
| Minimum pension for 2026 retirees | EGP 1,755 | 2026 | From January 2026 | https://www.nosi.gov.eg/ar/news/Pages/2025-11-30.aspx |
| Maximum pension | EGP 13,360 | 2026 | From January 2026 | same |

Law 148 obliges employers to insure the **actual wage**; the minimum exists to set a wage for groups whose pay is hard to fix, such as irregular, contracting and farm workers ([NOSI](https://www.nosi.gov.eg/ar/news/Pages/2025-11-30.aspx)).

## The base

- **Insurance wage = actual wage, clamped to the band:** min(max(wage, 2,700), 16,700). Pay above the maximum carries no contribution.
- **Fixed for the year:** for private sector employees, contributions run for the calendar year on the January wage. Someone who joins later uses the joining month's wage until the next January (art. 115). A daily wage is multiplied by 30 where pay is not monthly.
- **Start and end months:** no contribution for the start month unless it is a full month; a full contribution for the month service ends (art. 115).
- **Suspended contract or too little pay:** the private employer still pays in full; sums paid for the worker count as a loan (art. 122).
- **Compulsory military service:** both sides are exempt (art. 115).
- **Comprehensive wage (الأجر الشامل):** the figure on insurance form 2; non-insurable allowances are the difference between it and the insurance wage ([ETA FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) insurance q.1, q.2).
- **Tax:** contributions are deductible for salary tax ([eg-payroll](eg-payroll.md)).
- **Changing self-employed income class:** one class up or down at a time on request; effective the month after; up again after no more than three years (art. 117).

## Deadlines and filing

**Due date (art. 121):** contributions fall due on the **first of the month after** the month they relate to. The late charge is waived if paid within 15 days of that date, so payment by the 15th costs nothing extra.

**Employer steps:**

1. Register the establishment with the NOSI office for its area. Ask for a single account for branches on form 10 if wanted ([NOSI FAQ](https://www.nosi.gov.eg/ar/About/Pages/FAQ.aspx)).
2. Report each employee and wage on NOSI forms (art. 120). The joining date comes from form 1 or form 2 ([ETA FAQ](https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf) q.65). Report end of service on form 6.
3. Each January, private sector employers file form 2 with wages; also on any law or decree changing wages. Electronic filing is allowed by NOSI rules ([NOSI FAQ](https://www.nosi.gov.eg/ar/About/Pages/FAQ.aspx)). Over 100 insured: wage change forms may be delivered on a flash drive or CD to the office ([NOSI](https://www.nosi.gov.eg/ar/news/Pages/2025-11-30.aspx)).
4. Withhold the 11%, add the 18.75%, and pay. Ask balances on hotline 16217; pay at a bank through NOSI's payment system quoting the establishment number ([NOSI FAQ](https://www.nosi.gov.eg/ar/About/Pages/FAQ.aspx)). Art. 123 lets NOSI use electronic channels.
5. Post the certificate of payment at the workplace (art. 122).
6. Enter the same insurance data on the ETA monthly form ([eg-payroll](eg-payroll.md)). ETA does not collect insurance.

**What happens next.** Contributions are computed on the forms. If forms are missing, NOSI uses the last filing or its own inquiries and notifies the amount. The employer has 30 days to object at the office, with an EGP 100 fee; NOSI replies within 30 days; refusal goes to the disputes committee within 30 days, then to court within 30 days. With no challenge, the amount becomes final (art. 120).

**Self-employed steps:** register at the competent NOSI office, choose the income class, and pay the 21% by the 15th. Class change: as in The base.

## Penalties and interest

| Item | Amount | Source |
|---|---|---|
| Late payment | Monthly extra charge: average Treasury bill and bond yield in the month before payment, plus 2%, from due date to end of payment month. Nil if paid within 15 days | [art. 121](https://www.nosi.gov.eg/ar/Lists/NOSILibrary/2-12-2019%20%D9%83%D8%AA%D8%A7%D8%A8%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF.pdf) |
| Blocking inspectors, false or missing data | EGP 30,000 to 100,000; doubled on repeat | art. 165 |
| Evading sums owed through false or hidden data | EGP 20,000 to 50,000 | art. 166 |
| Not filing names, wages, contributions | EGP 20,000 to 50,000; doubled on repeat | art. 167 |
| Injury: not moving the injured worker to treatment (art. 50), or not telling police without good excuse (art. 61) | Prison up to one year and EGP 50,000 to 100,000, or either; up to three years if death or over 50% disability follows | art. 167 |
| Not insuring a worker, or not on the true period or wage; charging workers insurance costs | EGP 20,000 to 100,000; doubled on repeat; court orders repayment | art. 168 |

Fines are reviewed every ten years from commencement (art. 170).

## Cross-border points

- Egyptians abroad pay 21% in group third. NOSI's FAQ says this fell from 22.5% ([NOSI FAQ](https://www.nosi.gov.eg/ar/About/Pages/FAQ.aspx)). Contributions on unpaid foreign leave are paid by the worker with both shares in foreign currency (art. 119).
- Foreign nationals and totalization agreements: refer to a qualified reviewer.

## Two worked examples that recompute

### Example 1: EGP 25,000 a month, private sector

The wage is above the maximum, so the insurance wage is 16,700. Employee 1,837. Employer 3,131.25. Total paid to NOSI 4,968.25. Nothing on the other 8,300.

```oa-check
name: Employee above the maximum, 2026
inputs:
  wage: 25000
steps:
  - ins_wage: clamp(wage, 2700, 16700)
  - employee: ins_wage * 0.11
  - employer: ins_wage * (0.12 + 0.01 + 0.015 + 0.0325 + 0.01)
  - total: employee + employer
expected:
  ins_wage: 16700
  employee: 1837.00
  employer: 3131.25
  total: 4968.25
```

### Example 2: decision, which contribution income should a self-employed designer pick?

Choosing the minimum costs 567 a month; EGP 8,000 costs 1,680; the maximum 3,507. Going from minimum to maximum costs 35,280 a year more. Pension rises with income paid on, so the decision is the cash now against the pension later: if cash is short, start low and step up (one class at a time). The NOSI table sets the actual class.

```oa-check
name: Lowest or highest class, 2026
inputs:
  low: 2700
  high: 16700
steps:
  - low_month: low * 0.21
  - high_month: high * 0.21
  - extra_year: (high_month - low_month) * 12
expected:
  low_month: 567.00
  high_month: 3507.00
  extra_year: 35280.00
```

### Band table and further cases

| Insurance wage | Employee 11% | Employer 18.75% | Combined 29.75% | Self-employed 21% |
|---|---|---|---|---|
| 2,700 | 297.00 | 506.25 | 803.25 | 567.00 |
| 8,000 | 880.00 | 1,500.00 | 2,380.00 | 1,680.00 |
| 16,700 | 1,837.00 | 3,131.25 | 4,968.25 | 3,507.00 |

- Employee on 12,000: 1,320 and 2,250, total 3,570.
- Employee on 10,000: 1,100 and 1,875.
- Wage reported below 2,700: use 2,700: 297 and 506.25. A true wage must be declared; the private minimum wage is in eg-payroll.
- Managing partner in an LLC: employer group at 21% of chosen income, not 11% plus 18.75%.

## Ask the client first

1. Which group: employee, business owner or manager, Egyptian abroad, irregular? If a name is on the commercial register, start from group second.
2. Actual January wage, or joining month wage?
3. Private or public sector, and under comprehensive health insurance?
4. Activity risk (injury rate 0.5% to 1%)?
5. For the self-employed: chosen class and age (21 or over)?
6. Any second job or capacity?

**Defaults:** unknown employee wage: gross fixed wage clamped to the band. Self-employed with no class chosen: show the minimum and say it is an assumption. Rates older than this January: recheck against NOSI.

**Do not:** apply 11% and 18.75% to the self-employed; compute on uncapped pay; treat a registered owner-manager as salaried without checking; advise on irregular-worker eligibility, totalization or settlements without a qualified reviewer; file, register or pay for the client. Output needs a qualified Egyptian accountant's review. Salary tax and the martyrs fund are in eg-payroll.

## Sources

| Source | URL | Read on |
|---|---|---|
| NOSI, 2026 minimum and maximum, 30 Nov 2025, whole | https://www.nosi.gov.eg/ar/news/Pages/2025-11-30.aspx | 2026-11-01 |
| Law 148/2019, NOSI consolidated PDF, arts. 1, 2, 19, 36, 45, 46, 70, 85, 86, 115 to 123, 164 to 170 | https://www.nosi.gov.eg/ar/Lists/NOSILibrary/2-12-2019%20%D9%83%D8%AA%D8%A7%D8%A8%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF.pdf | 2026-11-01 |
| NOSI FAQ, employer questions | https://www.nosi.gov.eg/ar/About/Pages/FAQ.aspx | 2026-11-01 |
| ETA payroll FAQ, 4th edition, insurance section | https://eta.gov.eg/sites/default/files/2026-05/faqs-payroll-system-v4.pdf | 2026-11-01 |

Not yet confirmed: the 15% yearly rise of the band to 2028 (the law leaves the band to the executive regulations, which were not opened; the actual 2026 rises were 17.4% and 15.2%); 2027 band; the date of the first 1% rate rise (seven years from commencement; old text gives commencement as 1 January 2020); rates after the Law 148 amendments since 2019 (the PDF is the 2019 text; the 2026 NOSI notice confirms the band only); the old rule that board members and register managers pay on the maximum wage (art. 19(2) reads as chosen income); the sickness 4% in art. 70 for groups second and fourth and who it binds; rates under comprehensive health insurance, Law 2/2018; the contribution income table; the NOSI form to open an employer file; the Martyrs Fund treatment (eg-payroll); board members' position under art. 2 second for unlisted companies.

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
