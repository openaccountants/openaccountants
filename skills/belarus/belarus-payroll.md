---
name: belarus-payroll
description: Prepare 2026 Belarus payroll working papers for ordinary employees and covered civil-contract recipients, including resident and nonresident income-tax-agent duties. Trigger on Belarus salary, gross to net, podokhodny nalog, PIT withholding, child and standard deductions, FSZN employee pension, employer contributions, quarterly tax-agent declarations and income information reports. The skill distinguishes resident annual high-income assessment from the specific foreign-person withholding rule, and prevents subtracting the employee pension contribution twice or deducting it from the PIT base without authority. It provides filing and payment procedures, statutory penalties and two recomputing examples. Read the social-contributions skill for contribution classes and ceilings and the individual-income skill for annual assessment; tier 2, checked against the law, with the director historical-insurance gap retained.
version: 0.2
jurisdiction: BY
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belarus payroll withholding and gross-to-net, 2026 v0.2

## Who this applies to

Ordinary 2026 payroll for Belarus tax agents under Special Code art. 216, including Belarus organisations/entrepreneurs and covered foreign PEs. Determine employee versus covered civil contractor, main employment place, residence and any special regime before calculating. The individual taxpayer's annual high-income declaration is separate from the employer's quarterly tax-agent declaration. [Code arts. 195-199, 207, 214-216-1](https://pravo.by/document/?guid=3871&p0=hk0900071).

FSZN covers employees, covered civil contractors and founder-managers under Law 118-Z; Belgosstrakh civil-contract coverage depends on the specified workplace conditions. HTP, special presidential concessions, severance/benefit schemes and cross-border coverage exemptions require their own treatment. [Law arts. 1-5](https://pravo.by/document/?guid=3871&p0=H12100118); [Decree 108 Regulation para. 193](https://pravo.by/document/?guid=3871&p0=P32500108).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official act/article |
|---|---|---|---|
| Ordinary income-tax withholding | 13% | 2026 | [Code art. 214(1.1)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Specified nonpermanently resident foreign citizens/stateless recipients | Tax-agent higher-rate calculation on specified income above BYN 350,000 and 600,000, at 25%/30%; dividends separate | 2026 | [Art. 214(1.2)-(1.3)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Basic monthly deduction | BYN 216 if taxable income no more than BYN 1,308 | 2026 | [Art. 209(1.1)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Child/dependant monthly deduction | BYN 63; qualifying enhanced cases BYN 120 each | 2026 | [Art. 209(1.2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Protected category / qualifying young specialist | BYN 306 / 860 monthly, subject to documented statutory conditions | 2026 | [Art. 209(1.3)-(1.4)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Ordinary employee pension | 1% of covered FSZN base | 2026 | [Law 118-Z art. 5(1)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Ordinary employer FSZN | 28% pension plus 6% social = 34% | 2026 | [Law art. 5](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Ordinary FSZN maximum base | 5 times preceding month's national average wage | Monthly, 2026 | [Law art. 4(1)](https://pravo.by/document/?guid=3871&p0=H12100118) |
| Monthly minimum wage | BYN 858 from 1 January 2026; use any later indexed amount the law requires for the month | 2026 | [Council Resolution 612 of 6 November 2025, paras. 1, 4](https://pravo.by/document/?guid=12551&p0=C22500612) |
| Accident insurance baseline | 0.6% nonbudget employer, before insurer adjustments | 2026 | [Decree 108 Regulation para. 194](https://pravo.by/document/?guid=3871&p0=P32500108) |
| Main-job non-work gifts/material assistance exemption | BYN 3,910 per source/year; other-source qualifying gifts BYN 259 | 2026 | [Code art. 208(23)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Qualifying main-job insurance benefits exemption | BYN 6,695 per source/year | 2026 | [Art. 208(24)](https://pravo.by/document/?guid=3871&p0=hk0900071) |

## The base

1. Assemble each worker's month: salary, bonuses, leave pay, taxable in-kind benefits, civil-contract remuneration and qualifying exemptions. Date and value receipts under arts. 200, 213/216. Maintain monthly and annual source-level totals and all exemption certificates. A gift connected with work is not automatically covered by the non-work gift exemption. [Arts. 196, 200, 208, 213, 216](https://pravo.by/document/?guid=3871&p0=hk0900071).
2. Determine the main job and deduction documents. Apply the basic deduction only when monthly taxable income is within its limit, plus proved child/dependant or protected-category deductions and qualifying young-specialist relief. For the latter, use the placement/service, duration and continued-employment conditions in art. 209(1.4), not age alone. Apply qualifying social/housing deductions under arts. 210-211 using payment and entitlement records, reconcile any other agent's usage, and floor the ordinary PIT base at zero. [Arts. 199(3), 209-211](https://pravo.by/document/?guid=3871&p0=hk0900071).
3. Compute ordinary PIT from taxable remuneration less lawful PIT deductions. The employee's 1% pension contribution is separately withheld from net pay; it is not automatically subtracted from the PIT base. For ordinary employees outside art. 214's special foreign-person rule, withhold at 13% during the year and supply the information needed for annual high-income assessment. Do not mechanically make every employer aggregate all employers' annual wage income at progressive rates. [Arts. 199, 214-216](https://pravo.by/document/?guid=3871&p0=hk0900071).
4. For an agent accruing specified high income to foreign citizens/stateless persons not permanently residing in Belarus, implement art. 214(1.2)-(1.3): apply the higher rates to the statutory annual excess as it arises, withhold on actual payment, and keep dividends in their separate base. This wording is not identical to all nonresident individuals; a Belarus citizen who is tax-nonresident is not automatically in this special foreign-person category. The annual declaration remains mandatory for high-income cases. [Arts. 199(8-2)-(8-3), 214, 219(1.9)](https://pravo.by/document/?guid=3871&p0=hk0900071).
5. Compute FSZN from covered remuneration and the actual monthly minimum/maximum, separately from the PIT base. Use the appropriate employer class and exemptions; withhold the employee pension component once. Calculate Belgosstrakh on its separate covered base and actual notified tariff, without importing the FSZN ceiling. From March, covered directors require the national-average-wage minimum test. Route the unresolved January-February director base and exact floor proration to the named gap. [Law arts. 4-5, 9, 12](https://pravo.by/document/?guid=3871&p0=H12100118); [Resolution 1462 payment Regulation para. 2](https://pravo.by/document/?guid=3871&p0=C20601462).
6. `Net pay = gross cash entitlement - employee PIT - employee pension - other lawful employee deductions`. `Employer cost = gross entitlement + employer FSZN + accident premium + any applicable professional occupational pension`. Employer charges are not employee deductions. Reconcile the payroll register, bank payment, tax ledger and individual social accounts. [Code art. 216](https://pravo.by/document/?guid=3871&p0=hk0900071); [Law arts. 4-6, 11](https://pravo.by/document/?guid=3871&p0=H12100118).

## Deadlines and filing

| Obligation | Deadline/rule | Official source |
|---|---|---|
| PIT withheld on bank-paid cash income | Remit no later than bank cash withdrawal or transfer of income to recipient/third party | [Code art. 216(6)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| PIT on cash paid from agent's till / in-kind income | No later than day after cash payment / actual withholding, respectively | [Art. 216(6)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Quarterly agent PIT declaration | By 20th of month after quarter, subject to object and statutory annual-final-return rules | [Arts. 207, 216-1](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Individual income information, distinct from agent return | Cumulative first six months by 20 July 2026; twelve months by 20 January 2027; use respective old/new forms | [General Code art. 85(6); MNS 2026 instructions](https://nalog.gov.by/individuals_income_2024/) |
| Ordinary FSZN payment | Actual/contractual payday for previous month, capped at 20th following month; eligible quarterly exception in Law art. 8 | [Law art. 8](https://pravo.by/document/?guid=3871&p0=H12100118) |
| 4-Fund | Electronic quarterly, by 20th after period | [Ministry Resolution 143, Form 4-Fund](https://pravo.by/document/?guid=12551&p0=W22544374p) |
| PU-2 | Hire within 5 calendar days; new employer within 15 days of state registration; dismissal generally by next day | [Resolution 742 Rules para. 16](https://pravo.by/document/?guid=12551&p0=C22500742) |
| PU-3 | Quarterly within following month; initial covered civil-contract submission within 5 calendar days, 15 for new payer | [Rules para. 17](https://pravo.by/document/?guid=12551&p0=C22500742) |
| Belgosstrakh premium | By 25th following quarter | [Resolution 1462 payment Regulation para. 4](https://pravo.by/document/?guid=3871&p0=C20601462) |
| Belgosstrakh annual report | Registered policyholders file calendar-year report by 25 January following year; nonworking deadline moves to next working day | [Resolution 1462 reporting Regulation paras. 2-3, 33-35](https://pravo.by/document/?guid=3871&p0=C20601462) |

Use the MNS portal/inspectorate for the agent declaration and income information. Do not replace the two 2026 individual-income information submissions with a single March report. Under Law art. 8(5), employer FSZN payments due on nonworking days move to the preceding working day; tax deadlines use General Code art. 4. The ordinary PU/report process above follows Resolution 742 effective 8 January 2026; do not retroactively apply its new engagement-notification rules to 1-7 January without checking the predecessor rules. [General Code arts. 4, 40, 85](https://pravo.by/document/?guid=3871&p0=hk0200166); [Law art. 8](https://pravo.by/document/?guid=3871&p0=H12100118); [Resolution 742 para. 5](https://pravo.by/document/?guid=12551&p0=C22500742).

From 8 January, Resolution 742 Rules 15-17 also require: PU-1 registration within two calendar days of hiring a person without a social-insurance certificate, except a person whose identity document contains an identification number; PU-1 personal-data change within five working days after the supporting document is presented (identification-number holders use population-register data); PU-2 section 2 job/occupation-only changes quarterly by the 10th after the quarter. For sickness/maternity entitlement, submit the preceding quarter's PU-3 within three working days after the certificate is presented or the Fund's portal notice is received. PU-2 is also due within three working days after the sickness certificate if the post-1-July-2019 concurrent-job code was not supplied. The pension-assignment PU-3 is due within five working days after the person's pension/recalculation application. These event-driven filings do not wait for the ordinary quarter-end batch. [Resolution 742 Rules 15-17, official PDF pp. 32-33](https://pravo.by/document/?guid=12551&p0=C22500742).

From 8 January, covered professional-occupational-pension policyholders also file PU-6 after PU-3 within the month following each quarter. Pension assignment/recalculation for the listed special-work/service/professional pensions triggers PU-6 within five working days after the relevant application; ordinary pension-age attainment or qualifying dismissal triggers it by the following month. Continued employment after a pension-event PU-6 still requires the ordinary quarterly PU-6. On Fund deregistration for liquidation/cessation, PU-2/PU-3/PU-6 are due within thirty working days after the liquidation-start documents are filed; payers outside state registration use the decision/deregistration trigger. PU-2/PU-3/PU-6 reporting deadlines falling on a nonworking day move to the next working day. [Resolution 742 Rules 19-21, official PDF pp. 34-35](https://pravo.by/document/?guid=12551&p0=C22500742).

The 2026 Belgosstrakh annual report is due 25 January 2027. Use the insurer's prescribed electronic-document/electronic software delivery and keep its receipt; the reporting deadline moves to the following working day, while quarterly premium payment moves to the preceding working day. Reorganisation/liquidation reports use the separate 15-working-day triggers in reporting Regulation para. 33 and can be filed on paper under para. 35. [Resolution 1462 reporting Regulation paras. 33-38](https://pravo.by/document/?guid=3871&p0=C20601462); [Resolution 660 commencement para. 3](https://pravo.by/document/?guid=12551&p0=C22500660).

## Penalties and interest

Agent PIT interest follows General Code art. 55, including the special start at the first day of the following month for ordinary agent PIT remittance delay and the stated audit/transaction exceptions. The generic day-after-due-date rule must not be applied indiscriminately to this withholding liability. [General Code art. 55(2),(4)](https://pravo.by/document/?guid=3871&p0=hk0200166).

Administrative Code art. 14.5 sets a lower fixed-range fine where both the amount and relative-size tests are satisfied (no more than 4 basic units for an entrepreneur or 10 for a company, and no more than 5% of withheld/remitted tax). Exceeding either invokes 40% of the amount due, minimum 2 basic units for an entrepreneur or 10 for a company. Apply the article's correction and nonpayment exclusions; intentional/responsible-person cases have separate rules. Late agent returns use art. 14.2. [Administrative Code arts. 14.2, 14.5](https://pravo.by/document/?guid=3871&p0=hk2100091). The basic unit is BYN 45 from 1 January 2026 ([Council Resolution 651 of 20 November 2025](https://pravo.by/document/?guid=12551&p0=C22500651)).

FSZN interest uses 1/360 of the refinancing rate at payment under Law art. 10; accident penalties use Decree 108 paras. 196-197. An official finding of unlawful PIT non-withholding/non-remittance triggers the separate 26% PIT treatment in art. 214(7.2), as well as the applicable procedural/penalty analysis. [Law art. 10](https://pravo.by/document/?guid=3871&p0=H12100118); [Decree 108](https://pravo.by/document/?guid=3871&p0=P32500108); [Tax Code art. 214(7.2)](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Cross-border points

Determine Belarus-source employment income and actual work location under art. 197 before withholding. Treaty employment relief requires the actual operative treaty, sufficient residence evidence under art. 224 and confirmation that relevant provisions are not suspended. Nonresident status alone does not imply exemption. A foreign PE's retrospective payroll-agent duties and specific initial remittance deadline are in art. 216(6). Foreign social coverage requires a separate agreement/certificate analysis, not a PIT treaty conclusion. [Arts. 197, 216(6), 224](https://pravo.by/document/?guid=3871&p0=hk0900071); [Law art. 2](https://pravo.by/document/?guid=3871&p0=H12100118).

## Two worked examples that recompute

### 1. Ordinary employee, no deductions

Gross cash salary is BYN 3,000. Statutory social limits do not alter the covered base, no PIT deductions apply, and the insurer confirms an unadjusted tariff. PIT is 390, employee pension 30 and net pay 2,580. Employer FSZN and accident premium are 1,020 and 18; total employer cost is 4,038.

```oa-check
name: BY 2026 payroll standard employee
inputs:
  gross: 3000
steps:
  pit: gross * 0.13
  employee: gross * 0.01
  net: gross - pit - employee
  employer: gross * 0.34
  accident: gross * 0.006
  cost: gross + employer + accident
expected:
  net: 2580
  cost: 4038
```

### 2. Main-job employee with two qualifying children

Gross and taxable monthly remuneration are BYN 1,200, within the basic-deduction limit. Two qualifying children attract 120 each. The PIT base is 1,200 - 216 - 240 = 744; PIT is 96.72. Employee pension is 12 on the social base, not on the PIT base. Net pay is 1,091.28. The statutory social limits do not change the 1,200 covered base.

```oa-check
name: BY 2026 payroll standard and enhanced child deductions
inputs:
  gross: 1200
  children: 2
steps:
  deductions: 216 + children * 120
  pit_base: max(0, gross - deductions)
  pit: pit_base * 0.13
  employee: gross * 0.01
  net: gross - pit - employee
expected:
  pit_base: 744
  pit: 96.72
  net: 1091.28
```

## Ask the client first

- Which employment/civil contracts, main job, work locations and remuneration periods apply?
- What nationality, permanent residence and tax residence documents exist?
- Which deductions, benefits and annual per-source exemption balances are documented?
- What gross, in-kind and cash amounts, payroll corrections and previous deductions were recorded?
- Which contribution class, disability status, wage limits and insurer tariff are applicable?
- What bank/cash paydays, agent returns, information reports and social submissions were actually filed?

## Sources

| Source and read scope | Official URL | Read on |
|---|---|---|
| Tax Code Special Part, arts. 195-216-1, 219, 224 | https://pravo.by/document/?guid=3871&p0=hk0900071 | 2026-10-24 |
| Tax Code General Part, arts. 4, 40, 55, 85(6) | https://pravo.by/document/?guid=3871&p0=hk0200166 | 2026-10-24 |
| MNS 2026 individual-income information instructions | https://nalog.gov.by/individuals_income_2024/ | 2026-10-24 |
| FSZN Law 118-Z, arts. 1-12 | https://pravo.by/document/?guid=3871&p0=H12100118 | 2026-10-24 |
| Decree 108, approved Regulation paras. 192-197 | https://pravo.by/document/?guid=3871&p0=P32500108 | 2026-10-24 |
| Council Resolution 1462, contribution-payment Regulation | https://pravo.by/document/?guid=3871&p0=C20601462 | 2026-10-24 |
| Ministry Resolution 143, Form 4-Fund official PDF p. 1 | https://pravo.by/document/?guid=12551&p0=W22544374p | 2026-10-24 |
| Council Resolution 742, official PDF pp. 27-35 | https://pravo.by/document/?guid=12551&p0=C22500742 | 2026-10-24 |
| Administrative Code, arts. 14.2, 14.5 | https://pravo.by/document/?guid=3871&p0=hk2100091 | 2026-10-24 |
| Council Resolution 612 of 6 November 2025, paras. 1, 4, official PDF, monthly minimum wage BYN 858 from 1 January 2026 | https://pravo.by/document/?guid=12551&p0=C22500612 | 2026-10-31 |
| Council Resolution 651 of 20 November 2025, paras. 1, 3, official PDF, basic unit BYN 45 from 1 January 2026 | https://pravo.by/document/?guid=12551&p0=C22500651 | 2026-10-31 |

Pravo consolidated HTML was read in a normal browser after scripted access returned HTTP 403. Published PDFs were read in the official browser PDF viewer. Checked against the law (tier 2); no licensed Belarusian accountant has signed it off.

Not yet confirmed: The migration-law minimum salary for foreign employees carried in the old payroll file (five minimum wages from 1 November 2025) is a labour/migration condition, not a tax computation, and was not checked against its act. The January-February director accident-insurance base, exact March director-floor proration, and predecessor engagement-notification rules for 1-7 January 2026 remain unverified. PR is partial for those ordinary cases; do not substitute the later rules for earlier dates.

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
