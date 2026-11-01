---
name: lb-payroll-social
description: "Use this Guide for Lebanon payroll, NSSF, CNSS, family-branch earnings ceilings and family-benefit questions in 2026. It distinguishes ordinary employees from special worker categories and confirms the May family-branch changes against the official Arabic memo. It also identifies the later legal-time suspension and social-security debt-relief documents. The examples recompute a capped family base and the spouse and child benefit cap. They do not apply an unconfirmed contribution percentage or establish full payroll net pay. Current contribution rates, medical and end-of-service parameters, operational filing dates and foreign-worker coverage remain named non-operative holds requiring further primary-source evidence."
version: 1.2
jurisdiction: LB
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
---

# Lebanon Payroll and Social Contributions

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Lebanon.

## Who this applies to

Payroll working papers for ordinary NSSF-covered employees in Lebanon. NSSF memo 831 distinguishes ordinary family-benefit parameters from special public-driver and newspaper-vendor arrangements. Apply the ordinary rows only after establishing the category. Salary income tax is in [Personal income tax](lb-income-tax.md); a family benefit paid by NSSF is not a salary-tax personal allowance.

## Rates, bands and thresholds

| Item and period, ordinary family branch | Amount | Official source |
|---|---|---|
| Monthly earnings ceiling from 1 May 2026 | LBP 28,000,000 | [NSSF memo 831, paragraph I; Social Security Law art. 68(2), Decree 2923/2026](https://drive.google.com/file/d/1LXzz54n5z6hZ7fajiek3aZr6EadZqShk/view?usp=sharing) |
| Monthly spouse benefit from 1 May 2026, eligibility required | LBP 2,100,000 | [Memo 831 II, arts. 46-48](https://drive.google.com/file/d/1LXzz54n5z6hZ7fajiek3aZr6EadZqShk/view?usp=sharing) |
| Monthly benefit per eligible child, at most five | LBP 1,155,000 | same |
| Monthly ordinary family-benefit maximum | LBP 7,875,000 | same |
| Contribution rates and other branch ceilings | Unverified: PAY-H1; do not calculate an employer or employee contribution from this table | [NSSF official publications index](https://www.cnss.gov.lb/%D8%A7%D9%84%D9%85%D8%B0%D9%83%D8%B1%D8%A7%D8%AA-%D8%A7%D9%84%D8%A5%D8%B9%D9%84%D8%A7%D9%85%D9%8A%D8%A9-2026/) |

## The base

For the ordinary family branch, take evidenced contributory earnings and cap them at the monthly ceiling for the applicable period. The memo changes the ceiling and benefit amounts from 1 May 2026; it does not itself establish all ordinary employer contribution percentages, contributory pay exclusions or sickness/end-of-service rules. Those are PAY-H1. Keep gross pay, reimbursements and benefits separate until the contributory basis is established. The old medical ceiling and minimum-wage figures remain PAY-H2 pending their decree and later-amendment chain; do not derive them from a multiple in a press note.

## Deadlines and filing

NSSF memo 843 applies Law 46/2026 and suspends the specifically listed legal periods from 1 March through 31 July 2026, including those under Social Security Law art. 80, while excluding discretionary administrative time limits. This is not a blanket instruction that every payment is deferred by the same number of days. Match the obligation and original due date. The current account route, monthly/quarterly schedule, annual declaration, memos 828/830 and any further extensions remain PAY-H3. Stop before submission/payment until the actual applicable date and reference are established.

## Penalties and interest

Memo 846 is later than the budget summary: it implements Law 47/2026 with conditions for debt relief, instalments and a new penalty table. The published route concerns debts due through 31 December 2025, a 30 July 2027 application/payment limit, exclusions and consequences for default. Do not substitute the budget's temporary general penalty reduction. An individual employer's entitlement, instalments and exact new penalty row remain PAY-H4; the entire three-page memo is in the source ledger.

## Cross-border points

Foreign-worker coverage, reciprocity, offshore staff and non-resident payroll are PAY-H5. Do not infer social-security exemption from foreign nationality or a company label. Use a Lebanese professional for those coverage decisions.

## Two worked examples that recompute

For a fully eligible ordinary employee after 1 May, monthly contributory earnings LBP 40 million exceed the family ceiling. The family base is LBP 28 million, LBP 12 million below uncapped pay. This is a base computation only; no unconfirmed contribution rate is applied.

```oa-check
name: Family branch capped base
inputs:
  earnings: 40000000
  ceiling: 28000000
steps:
  - family_base: min(earnings, ceiling)
  - excess: earnings - family_base
expected:
  family_base: 28000000
  excess: 12000000
```


Eligibility decision: the documents establish an eligible spouse and six eligible children. Count at most five children: monthly family benefit LBP 7,875,000. Without an eligible spouse, five eligible children produce LBP 5,775,000. A sixth child does not raise the child cap. This is a benefit calculation, not employer contribution or salary tax.

```oa-check
name: Five-child cap and spouse eligibility
inputs:
  children: 6
  child_amount: 1155000
  spouse_amount: 2100000
steps:
  - children_benefit: min(children, 5) * child_amount
  - with_spouse: children_benefit + spouse_amount
  - without_spouse: children_benefit
expected:
  with_spouse: 7875000
  without_spouse: 5775000
```


## Ask the client first

- What is the worker category and NSSF coverage evidence?
- Which pay month, contributory earnings and currency apply?
- What spouse and child eligibility documents are available?
- Which branch, due date, employer category and prior declaration are involved?
- Are there arrears, settlements, foreign workers or special-regime staff?

## Sources

| Source and read scope | URL | Read on |
|---|---|---|
| NSSF 2026 memo index, rows 822-852 screened; linked official documents | https://www.cnss.gov.lb/%D8%A7%D9%84%D9%85%D8%B0%D9%83%D8%B1%D8%A7%D8%AA-%D8%A7%D9%84%D8%A5%D8%B9%D9%84%D8%A7%D9%85%D9%8A%D8%A9-2026/ | 2026-11-01 |
| NSSF memo 831, 4 May 2026, whole one-page Arabic scan read; Decree 2923, Social Security Law art. 68(2) | https://drive.google.com/file/d/1LXzz54n5z6hZ7fajiek3aZr6EadZqShk/view?usp=sharing | 2026-11-01 |
| NSSF memo 843, 3 August 2026, both pages including Law 46/2026 arts. 1-2 read | https://drive.google.com/file/d/1r3zBw08rayUiNKRVbQwWnFVqHRwUcsD6/view?usp=sharing | 2026-11-01 |
| NSSF memo 846, 11 September 2026, all three pages read including amended penalty table and conditions | https://drive.google.com/file/d/1TgzCAn9WhaCLEAn0rC7MBwig3cXm6oXj/view?usp=sharing | 2026-11-01 |

Not yet confirmed: PAY-H1: ordinary employer/employee percentages, sickness/maternity and end-of-service calculation, pay exclusions. PAY-H2: pre-May family ceiling, current sickness ceiling and minimum wage after the full decree/amendment chain. PAY-H3: portal/payment steps, remittance dates, annual return and memos 828/830 plus further extensions. PAY-H4: taxpayer-specific Law 47/2026 relief and instalment eligibility, exact current penalty calculation. PAY-H5: foreign-worker, reciprocity, offshore and special driver/vendor rules. All prior values remain non-operative in the lineage ledger; no payroll amount is certified for filing.

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
