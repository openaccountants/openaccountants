---
name: kosovo-social-contributions
description: >
  Compute Kosovo employee and self-employed pension contributions for 2026 using the Pension Funds Law, its amendments, and current tax-authority filing guidance. Covers the employee and employer shares, voluntary limits, full-time wage floor, the real-income owner's quarterly cap, presumptive-business contributions, payment and reporting, and foreign employees with temporary stay. Separates pension deductions from wage income tax and identifies the new compulsory healthcare law and its unresolved implementation instruments. Use for Trusti, KPST, social security, pension payroll, owner contributions, IS or IL calculations, and minimum-wage questions. Health-inclusive social contributions remain partial until the applicable phase and collection rules are confirmed.
version: 0.2
jurisdiction: XK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants skill License v1.0 (content)
---

# Kosovo social contributions v0.2

Tax year **2026**. Checked against the law on **30 October 2026** (tier 2); no
licensed accountant has signed it off.

## Who this applies to

This skill computes ordinary Kosovo Pension Savings Trust contributions for
covered employees and self-employed people. Law 04/L-101 art. 1 defines an
employee by work under the employer's control and supervision, including
part-time work, regardless of the contract's title. Article 6(1), (13) requires
resident employee contributions from the first employment day until pension
age, defined as 65. Article 6(14) prohibits contributions by foreign employees
with temporary stay. Establish residence, stay and age before choosing the
pension treatment ([Pension Funds Law arts. 1 and 6](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en)).

Self-employed business income is covered by art. 6(12), including a business
owner who allocates part of business income as wages. Do not substitute the
company's corporate tax threshold for the individual's pension base. Pension
benefit calculations and supplementary-fund investment arrangements are outside
this contribution skill. The new health-law implementation gap below keeps SC
partial for a complete 2026 social-contribution calculation.

## Rates, bands and thresholds

All money amounts are EUR. The minimum-wage figures change during 2026.

| Item | Amount or rule | Period | Official authority |
|---|---|---|---|
| Employee mandatory pension | 5% of total wages | 2026 | [04/L-101 art. 6(2)(b)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en) |
| Employer mandatory pension | 5% of total wages, additional employer cost | 2026 | [04/L-101 art. 6(2)(a)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en) |
| Voluntary additional contribution | Up to 10 percentage points per side, making a maximum 15% per side; employer monthly / employee annual wage wording | 2026 | [04/L-101 art. 6(2)(c)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en) |
| Pension age | 65 | 2026 | [04/L-101 art. 1, Pension Age](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en) |
| Full-time minimum wage | EUR 425 monthly / EUR 2.50 per regular work hour | 1 January–30 June 2026 | [Decision 10/273 para. 1.1](https://kryeministri.rks-gov.net/wp-content/uploads/2025/10/Vendimet-e-mbledhjes-se-273-te-te-Qeverise.pdf) |
| Full-time minimum wage | EUR 500 monthly / EUR 3 per regular work hour | From 1 July 2026 | [Decision 10/273 para. 1.2](https://kryeministri.rks-gov.net/wp-content/uploads/2025/10/Vendimet-e-mbledhjes-se-273-te-te-Qeverise.pdf) |
| Self-employed, real-income mandatory pension | 10% of net income before pension deduction; maximum EUR 600 per quarter, subject to the minimum below | 2026 | [04/L-101 art. 6(12)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en); [04/L-168 art. 3](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=8655) |
| Self-employed, real-income voluntary upper limit | 30% of that net income | 2026 | [04/L-101 art. 6(12)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en) |
| Self-employed, presumptive basis | Minimum one-third of presumptive tax; voluntary maximum three times that tax, subject to the statutory minimum | 2026 | [04/L-101 art. 6(12)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en) |
| All self-employed, quarterly minimum | 30% of minimum wage: EUR 127.50 in Q1/Q2; EUR 150 in Q3/Q4 | 2026 | [04/L-101 art. 6(12)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en); [Decision 10/273 para. 1](https://kryeministri.rks-gov.net/wp-content/uploads/2025/10/Vendimet-e-mbledhjes-se-273-te-te-Qeverise.pdf) |
| Health, standard statutory employee/employer split | 3.5% / 3.5%; current phase and collection application remain unconfirmed | New 2026 law, subject to transition | [10/L-028 arts. 22(1), 35(2)](https://gzk.rks-gov.net/ActDetail.aspx?ActID=119938&langid=1) |

The EUR 600 cap belongs to mandatory **real-income self-employment** contributions.
It is not a ceiling on an employee's pensionable wage and not a EUR 24,000 annual
employee income exemption: Law 04/L-101, as amended by 04/L-115, 04/L-168 and
05/L-116 (the full amendment list in the Official Gazette record), sets no
maximum wage base for employee or employer contributions.

## The base

For an ordinary covered employee use total wages for each employer separately.
Employee pension is withheld from pay; employer pension is paid on top. Article
6(5) expressly charges each side on the market value where wages are paid
substantially in kind. Apply that pension provision separately from PIT's
benefit-in-kind threshold. If full-time wages are below the minimum wage,
art. 6(6) charges the employer on the minimum wage and the employee on actual
full-time wages. That rule does not authorise a below-minimum employment wage.
It does not impose a full-time monthly floor on every part-time contract
([04/L-101 art. 6(2)–(6)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en)).

For actual-income self-employment, calculate quarterly gross income less
allowable business deductions **before** pension contributions. Mandatory
pension is the greater of the quarterly floor and the lesser of 10% of that
net amount and EUR 600. TAK's current IL calculator expressly shows the 10%
net-income base, EUR 600 maximum and 30%-of-minimum-wage floor
([04/L-101 art. 6(12)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en); [04/L-168 art. 3](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=8655);
[TAK IL calculator, pension section](https://crmm.atk-ks.org/en/Public/CalculatorDetail?id=4)).

For presumptive businesses, start with the applicable quarterly presumptive
income tax and take one-third, then apply the quarterly floor. Do not use the
real-income EUR 600 cap for this category. The floor applies to all categories
of self-employed persons. Business-income PIT is calculated in
[kosovo-income-tax](kosovo-income-tax.md), not as a blanket flat rate on net
profit. Where an owner treats some business income as wages, art. 6(12)
requires employer and employee contributions on that wage part and contribution
reporting on the additional non-wage part; reconcile the two bases.

Employer pension under art. 6 is a deductible operating expense; employee
contributions under that article are outside PIT. For wage tax deduct only the
employee's pension from their wage, not the employer's contribution
([04/L-101 art. 37, replaced by 05/L-116 art. 10](https://bqk-kos.org/wp-content/uploads/2024/11/Law-05-L116-on-Amending-and-Supplementing-The-Law-on-Pension-Funds-Of-Ko.pdf);
[PIT AI 01/2016 art. 37(4)](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233)).

**2026 health-law change.** Law 10/L-028 was published on 15 May 2026;
art. 37 provides entry into force fifteen days after publication. Article 36
repeals Law 04/L-249, its amendment and derived by-laws. The old description of
04/L-249 as the current dormant law is therefore obsolete.

Article 22(1) sets a standard wage contribution of 7%, split 3.5% employee and
3.5% employer. Article 35(2) allows different rates during the first five years
of operation, with phase contributions approved through the government and
Assembly process. Article 22(2), (13) and (21) requires collection procedures.
A statutory standard rate alone does not establish the operative collection
period, phased rate or filing process. Obtain those instruments before adding
a health deduction. This skill supplies pension and wage-tax components and
leaves final health-inclusive payroll open; it does not certify either a zero
health liability or automatic collection at the standard rate
([10/L-028 arts. 21–22, 35–37](https://gzk.rks-gov.net/ActDetail.aspx?ActID=119938&langid=1)).


The health law also supplies distinct standard bases for actual-income and
presumptive self-employment, pension receipts and other mandatory insured
persons in art. 22(10)–(19). They cannot be replaced by the employee split or
included in an operative calculation until the applicable phase is established.

## Deadlines and filing

Report the employee's identity and each side's pension amount to TAK **before
payment**; self-employed persons report their own information (04/L-101 art.
6(10)). TAK's current timetable uses WM/CM for monthly wage withholding and
pension contributions, filed and paid by the 15th of the following month.
It uses IS for small individual businesses and IL for actual-income businesses,
by the 15th following each quarter. The current IL calculator includes the
owner's pension section. Keep the income-tax and pension payments separately
identifiable ([04/L-101 art. 6(3), (10), (12)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en);
[TAK current forms/deadlines](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/); [TAK IL form](https://crmm.atk-ks.org/en/Public/CalculatorDetail?id=4)).

Before employment starts, notify TAK of the contract one day in advance
([08/L-257 art. 43(5)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf)). Obtain the tax registration and EDI
access needed for the employer's filing. Reconcile declared personal IDs,
pension payments and Trust account allocations; the bank's transfer and Trust's
allocation deadlines in art. 6(8)–(11) are not extra time for the employer.
Do not invent a health return or use CM as evidence of a health payment.

## Penalties and interest

Use Law 08/L-257, not the repealed Law 03/L-222's penalty schedule.

| Failure | Current statutory consequence | Official authority |
|---|---|---|
| Missing mandatory return that results in a tax liability | EUR 50 per return for a business natural person; EUR 150 for a legal entity; EUR 20 for a non-business natural person | [08/L-257 art. 99](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Understatement or excess refund/credit | 15% of the difference if it is at most 10% of correct tax; 25% if it exceeds 10% | [08/L-257 art. 100(1)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Failure to withhold and pay over wage tax | 25% of the unpaid difference | [08/L-257 art. 103(1)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Failure to withhold or pay pension contributions | 25% of the unpaid contribution difference | [08/L-257 art. 103(2)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Failure to notify TAK of an employee as required | EUR 500 per undeclared worker | [08/L-257 art. 102(3)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |

Late-payment interest runs for each month or part-month, for at most ten years.
The Minister sets the rate at least annually and TAK publishes it. Under a
compliant instalment agreement interest stops from the following month; default
reinstates it. The rate must be higher than commercial bank lending rates in
Kosovo (art. 24(3)). Apply the published rate for the liability period, not an old
presentation or the rate for commercial debts ([08/L-257 art. 24](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf)).
These fines
have distinct statutory triggers; do not automatically add every row to every
correction.

## Cross-border points

The resident/temporary-foreign-employee distinction in Pension Funds Law art.
6(13)–(14) must be tested independently of wage-tax residence. A wage-tax treaty
relief does not itself establish exemption from pension contributions. Obtain
the applicable social-security agreement, coverage certificate and relevant
period before applying a cross-border exception. This skill supplies no
universal expatriate exclusion or automatic foreign-contribution credit.
Foreign employees with temporary stay are subject to the express prohibition
in art. 6(14); other foreign-worker cases require the actual legal status.

The health law has its own insured-person categories and non-resident rules
in arts. 9–11. Do not copy the pension rule into health insurance
([04/L-101 art. 6](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en); [10/L-028 arts. 9–11](https://gzk.rks-gov.net/ActDetail.aspx?ActID=119938&langid=1)).

## Two worked examples that recompute

### 1. Covered employee, mandatory pension only

Assume a resident employee below pension age, EUR 1,000 total cash wages, no
benefits and no voluntary contribution. Employee pension is EUR 50; employer
pension is EUR 50; pension remittance is EUR 100. The employer's wage-plus-
pension cost is EUR 1,050. These are pension components, not final pay after
PIT and health obligations.

```oa-check
name: Kosovo mandatory employee pension components 2026
inputs:
  gross_wage: 1000
steps:
  - employee_pension: gross_wage * 0.05
  - employer_pension: gross_wage * 0.05
  - pension_remittance: employee_pension + employer_pension
  - wage_plus_pension_cost: gross_wage + employer_pension
expected:
  employee_pension: 50
  employer_pension: 50
  pension_remittance: 100
  wage_plus_pension_cost: 1050
```

### 2. Actual-income owner, cap and zero-profit floor

Assume a covered actual-income owner with Q3 net business income before pension
of EUR 25,000 and Q4 net income zero, no wages and no voluntary top-up. Both
quarters use the EUR 500 minimum wage. Q3 mandatory pension is capped at EUR
600, rather than EUR 2,500. Q4 still has the EUR 150 floor. Total pension for
these two quarters is EUR 750; health is a separate unresolved component.

```oa-check
name: Kosovo self-employed real-income cap and quarterly floor 2026
inputs:
  q3_net_before_pension: 25000
  q4_net_before_pension: 0
  minimum_wage: 500
steps:
  - quarterly_floor: minimum_wage * 0.30
  - q3_mandatory: max(quarterly_floor, min(q3_net_before_pension * 0.10, 600))
  - q4_mandatory: max(quarterly_floor, min(q4_net_before_pension * 0.10, 600))
  - two_quarter_pension: q3_mandatory + q4_mandatory
expected:
  quarterly_floor: 150
  q3_mandatory: 600
  q4_mandatory: 150
  two_quarter_pension: 750
```

## Ask the client first

1. What are the worker's age, residence and immigration/stay status, and are they already receiving Trust benefits?
2. Is the person controlled as an employee, independently self-employed, or receiving both owner wages and business income?
3. Which period, hours, cash wages, benefits and voluntary pension election apply?
4. For an owner, what are the tax method, quarterly net income before pension and presumptive tax?
5. What health phase/collection instruments and cross-border coverage certificate apply to that period?
6. Which TAK returns, payment receipts and Trust allocations are outstanding or inconsistent?


## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Pension Funds Law 04/L-101 arts. 1, 6 and 37 | https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en | 2026-10-30 |
| 04/L-168 art. 3, quarterly mandatory cap | https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=8655 | 2026-10-30 |
| Gazette record of 04/L-101 and its amending acts | https://gzk.rks-gov.net/ActDetail.aspx?ActID=2815&langid=2 | 2026-10-30 |
| 05/L-116 art. 10, replacement tax-treatment art. 37 | https://bqk-kos.org/wp-content/uploads/2024/11/Law-05-L116-on-Amending-and-Supplementing-The-Law-on-Pension-Funds-Of-Ko.pdf | 2026-10-30 |
| PIT AI 01/2016 art. 37, pension deduction and voluntary limits | https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233 | 2026-10-30 |
| Decision 10/273 of 31 October 2025 para. 1, 2026 minimum wages | https://kryeministri.rks-gov.net/wp-content/uploads/2025/10/Vendimet-e-mbledhjes-se-273-te-te-Qeverise.pdf | 2026-10-30 |
| Tax-procedure Law 08/L-257 arts. 24, 43(5), 99–103 | https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf | 2026-10-30 |
| Current TAK forms and deadlines; read in ordinary browser | https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/ | 2026-10-30 |
| Current TAK IL calculator, owner-pension fields | https://crmm.atk-ks.org/en/Public/CalculatorDetail?id=4 | 2026-10-30 |
| Compulsory Healthcare Insurance Law 10/L-028 arts. 9–11, 21–22, 35–37; actual Gazette PDF downloaded through its public form | https://gzk.rks-gov.net/ActDetail.aspx?ActID=119938&langid=1 | 2026-10-30 |
| Official health fund copy of 10/L-028; full normalised text matches the Gazette download | https://fssh.rks-gov.net/wp-content/uploads/2026/05/LIGJI-PER-SIGURIMIN-E-DETYRUESHEM-TE-KUJDESIT-SHENDETESOR-2.pdf | 2026-10-30 |

Not yet confirmed: operative 2026 health-insurance phase, contribution rates, collection commencement and filing instruments; numeric 2026 tax late-interest rate; foreign-worker/social-security agreement outcomes for a specified case. SC remains partial pending the health implementation evidence.

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
