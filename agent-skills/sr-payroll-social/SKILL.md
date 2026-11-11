---
name: sr-payroll-social
description: "Suriname employer payroll and social contributions for tax year 2026: what an employer withholds, pays and reports each month. Covers wage tax (loonbelasting) withholding mechanics with the rates linked to sr-income-tax, the AOV old-age premium of 4% of zuiver loon under the Wet AOV (residents under 60, employee premium withheld by the employer, no ceiling), the general pension under the Wet Algemeen Pensioen 2014 (APF premium split at least half employer, 8% published for 2025, minimum and maximum contribution base, payment by the 15th), the basic health insurance under the Wet Nationale Basiszorgverzekering (employer must insure every employee and pay at least half the premium), the monthly LB/AOV return in the Tax Administration portal, the annual verzamelloonstaat, and penalties. Trigger on: Suriname payroll, premie AOV 4%, loonbelasting werkgever, aangifte LB/AOV, verzamelloonstaat, Algemeen Pensioenfonds premie, APF 8%, basiszorgverzekering werkgever 50%, BZV premie, Suriname emp"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sr-payroll-social"
  jurisdiction: "SR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Suriname payroll and social contributions (2026) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill tells an employer in Suriname what to withhold from each pay, what to pay itself, and where and when to report, for the 2026 calendar year. Four laws reach a payroll, and each has its own collector:

| Charge | Law | Who bears it | Paid to |
|---|---|---|---|
| Wage tax (loonbelasting) | Wet Loonbelasting | Employee, withheld | Tax Administration (Belastingdienst Suriname), LB/AOV return |
| AOV old-age premium | Wet Algemeen Oudedagsvoorzieningsfonds (Wet AOV) | Employee, withheld | Tax Administration, same LB/AOV return |
| General pension premium | Wet Algemeen Pensioen 2014 | Employer at least half, employee at most half | Algemeen Pensioenfonds (APF) |
| Basic health insurance premium | Wet Nationale Basiszorgverzekering | Employer at least half, employee at most half | The employee's health insurer |

**One figure, one home.** The wage tax rates, the SRD 108,000 tax-free amount, the 4% professional-expense deduction capped at SRD 4,800, and the exclusions for vacation allowance, bonus and child allowance are in [sr-income-tax](sr-income-tax.md). This skill uses them but does not restate them. Companies are in [sr-corporate-income-tax](sr-corporate-income-tax.md); non-resident employees and treaties in [sr-cross-border](sr-cross-border.md).

**Which text of the law.** The Wet AOV (S.B. 1981 no. 30, as last amended by S.B. 2002 no. 96) and the Wet Loonbelasting (as last amended by S.B. 2024 no. 2) with its Uitvoeringsbeschikking (S.B. 1981 no. 186, as last amended by S.B. 2016 no. 99), as published by the Tax Administration; the Wet Algemeen Pensioen 2014 (S.B. 2014 no. 113) and the Wet Nationale Basiszorgverzekering (S.B. 2014 no. 114), as published in the Staatsblad scans on the APF site. Read on 11 November 2026.

## Who this applies to

- **Employer (inhoudingsplichtige).** Anyone who pays wages to one or more employees must withhold wage tax (LB art. 6, art. 19(1)). Each employer registers once in the Tax Administration portal and gets one FIN; it may register only its own employees, and the fiscal unity rules of the VAT do not apply to wage tax (Tax Administration, Loonbelasting page). For the pension and health laws an employer is any natural or legal person with at least one employee (Wet Algemeen Pensioen art. 1(m); Wet Basiszorgverzekering art. 1).
- **AOV premium payers.** A resident of Suriname, of any nationality, who has wages from employment or profit from a business or profession and is under 60 (Wet AOV art. 19(1)). Not liable: foreign nationals who are heads or members of an international mission, diplomatic or consular staff, staff of a recognised international organisation covered by its own social security, members of a foreign armed force, and (other than as household staff) staff of an international organisation of which Suriname is a member (art. 19(2)). Non-residents and people aged 60 or over pay no AOV premium.
- **Pension.** Every employer must provide its employees with a pension scheme that gives at least the rights of the Wet Algemeen Pensioen 2014 (art. 10(1)). An employer whose own existing scheme already gives at least those rights is exempt from that duty (art. 10(2)). Where the act is silent, the Wet Pensioenfondsen en Voorzieningsfondsen (S.B. 2005 no. 75) applies to the employer's obligations (art. 10(12)). The self-employed must take out a scheme themselves and report it to the APF (art. 12).
- **Health insurance.** Every resident, including foreigners who live in Suriname, must have at least a basic health insurance (Wet Basiszorgverzekering art. 3(2); gov.sr). Every employer must take one out for each employee (art. 8(1)). It is forbidden to let a resident work for pay without one (art. 18(1)).
- **Out of scope:** civil servants (Ambtenarenpensioenwet); the minimum wage amount (set by the Minister by beschikking under the Wet Minimumloon, S.B. 2019 no. 101, art. 3(1) as amended by S.B. 2024 no. 31; the current amount was not found in a primary text); the AOV surcharge (opcenten) on companies' income tax (Wet AOV art. 18(b); see sr-corporate-income-tax); employment law (leave, notice, severance).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Wage tax: tax-free amount, bands, 4% deduction, exclusions | See [sr-income-tax](sr-income-tax.md) | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Loonbelasting.pdf |
| AOV premium (Wet AOV art. 20(2)); base is zuiver loon in the sense of the Wet Loonbelasting where wage tax is due, otherwise zuiver inkomen (art. 20(1)); residents under 60 only (art. 19) | 4% of the base | 2026 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-AOV.pdf |
| AOV premium: minimum or maximum base | None in the act | 2026 | same |
| AOV premium as computed in the 2026 income tax return portal ("Berekening Premie AOV" screen, manual of May 2026, page 25) | "4% over het zuiver inkomen" | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/05/Handleiding_1-IB-Nat.-Pers._mei-2026_compressed.pdf |
| General pension premium, statutory schedule (Wet Algemeen Pensioen art. 8(1), (2)) | 3% of the contribution base at entry into force; raised by half a percentage point each year from 1 January 2016, to at most 28% | 2026 | https://www.pensioen.sr/wp-content/uploads/2025/09/sb_2014__no_113_wet_algemeen_pensioen_2014-1.pdf |
| General pension premium published by the APF for 2025 "conform art 8 lid 2" (no 2026 notice found) | 8% of gross wage | 2025 | https://www.pensioen.sr/ |
| Pension premium split for an employee (art. 8(7), (8)); another split may be agreed only if the employee's share is not higher than the employer's | Employee 50%, employer 50% | 2026 | https://www.pensioen.sr/wp-content/uploads/2025/09/sb_2014__no_113_wet_algemeen_pensioen_2014-1.pdf |
| Pension contribution base at entry into force (art. 8(3)); changed by staatsbesluit (art. 8(6)); premium on at least the minimum base whatever the wage (art. 8(4)); nothing above the maximum base (art. 8(5)) | Minimum SRD 500, maximum SRD 5,000 a month (2014 amounts) | 2014 | same |
| Pension accrual (art. 7(1)) | 2% of the average wage of the last 60 months for each year of premium | 2026 | same |
| Pension right arises after (art. 3(1)); pension age (art. 1(i)) | 5 years of premium; age 60 | 2026 | same |
| Basic health insurance premium split for an employee (Wet Basiszorgverzekering art. 7(6), (7)); another split only if the employee's share is not higher than the employer's | Employee 50%, employer 50% | 2026 | https://www.pensioen.sr/wp-content/uploads/2025/09/S.B.-2014-no.-114-Wet-Nationale-Basiszorgverzekering_compressed-1.pdf |
| Maximum monthly basic health premium an insurer may charge, at entry into force (art. 7(1)); may be changed by staatsbesluit (art. 7(2)) | Age 0 to 16: SRD 55; 17 to 20: SRD 75; 21 to 59: SRD 165; 60 and over: SRD 240 | 2014 | same |
| Government pays the basic health premium (Council of Ministers decision under art. 7(3)) | Surinamese nationals aged 0 to 16 and 60 and over | 2026 | https://gov.sr/thema/basiszorgverzekering/ |
| Employee stays insured after premiums stop (art. 7(8)) | 3 months | 2026 | https://www.pensioen.sr/wp-content/uploads/2025/09/S.B.-2014-no.-114-Wet-Nationale-Basiszorgverzekering_compressed-1.pdf |

The figure that decides most payrolls is the AOV premium. The old version of this skill gave 8% with an SRD 2,250 to SRD 22,500 monthly base. Neither appears in the Wet AOV: the act says 4% with no base limits, and the Tax Administration's own 2026 return manual computes "4% over het zuiver inkomen". The 8% matches the APF pension premium published for 2025, a different charge paid to a different body.

## The base

Work each employee's month in this order.

1. **Gross pay for the month** (loon), leaving out what the Wet Loonbelasting keeps out of wages (vacation allowance, bonus and child allowance within their caps, LB art. 10; see sr-income-tax).
2. **Zuiver loon.** Gross wages less the 4% professional-expense deduction, at most SRD 400 a month (1/12 of SRD 4,800) (LB arts. 12(2), 13(3); figures in sr-income-tax).
3. **Wage tax.** Deduct the period's tax-free amount from zuiver loon (residents only), apply the monthly bands, and withhold when the wage is paid or made available (LB arts. 13, 14, 19(2)). Method and figures: sr-income-tax.
4. **AOV premium.** 4% of zuiver loon, for a resident under 60 (Wet AOV arts. 19, 20). There is no tax-free amount and no ceiling: the premium runs from the first SRD. It is withheld from the wage (art. 20(3)); the wage tax rules on withholding, collection and set-off apply as far as possible (art. 20(4)). The act has no employer AOV premium.
5. **Pension premium.** Pension "loon" is every money payment for work except overtime pay, pay for temporary extra work, vacation allowances, profit shares, conditional payments, reimbursed necessary costs, allowances to heads of household and year-end payments (Wet Algemeen Pensioen art. 6(1)). Clamp it between the minimum and maximum contribution base in force (art. 8(3) to (6)), apply the year's premium percentage (art. 8(1), (2)), withhold the employee share (at most half) and add the employer share (at least half) (arts. 8(7), (8), 10(4)).
6. **Basic health premium.** The premium is the one on the employee's policy, not a percentage of pay (art. 7(5); explanatory note to art. 7: "De hoogte van de premie is niet inkomen gerelateerd"). Withhold the employee share (at most half) and pay the whole premium to the insurer (arts. 7(6), (7), 8(1), (2)). Where the employee also insures a partner and children through the employer, they agree the premium for them (art. 9(2)).
7. **Net pay** is gross pay less wage tax, AOV premium, the employee's pension share and the employee's health share.

**Where pay passes a threshold in the month.** Overtime and one-off payments can be taxed at special rates on the employee's request (LB arts. 17a, 17c; sr-income-tax). Overtime and year-end payments do not count as pension loon (Wet Algemeen Pensioen art. 6(1)(a), (h)); they do count in zuiver loon for the AOV premium unless the Wet Loonbelasting keeps them out of wages.

## Deadlines and filing

| Step | When | Law |
|---|---|---|
| Register as an employer in the portal (portaal.belastingdienst.sr/OPO), one FIN per employer | Before the first pay; anyone without an electronic form must ask for portal access before the end of the month in which the pay period ends | Tax Administration, Loonbelasting page; LB art. 20(4) |
| Get a signed employee statement (werknemersverklaring) | Before the first pay, and again before a pay affected by a change | Uitvoeringsbeschikking LB arts. 7, 8 |
| Monthly LB/AOV return (aangifte loonbelasting en premie AOV), electronic, with an electronic signature; also when nothing is due | By the 7th working day after the end of the month in which the pay period ended | LB art. 20(1)(1°) to (3°), 20(3) |
| Pay the wage tax withheld | The statute says in the month in which the period ended (LB art. 20(1)(4°)); the Tax Administration page says return and payment from the 26th to the 10th of the next month, with the payment reference shown in the portal after filing | LB art. 20(1)(4°); Tax Administration, Loonbelasting page |
| Annual verzamelloonstaat: all wages and pensions paid and the wage tax and AOV premium withheld, per employee; online by CSV upload or by hand, from tax year 2024 | Within one month after the end of the calendar year (by 31 January 2027 for 2026) | Uitvoeringsbeschikking LB art. 21; Tax Administration, Loonbelasting page and online instructions |
| Statement of the year's wages, wage tax and AOV premium to the employee | On request | Uitvoeringsbeschikking LB art. 22 |
| Tell the inspector you have stopped being an employer | Within one month | Uitvoeringsbeschikking LB art. 23 |
| Pay the pension premium to the APF with a specification (employer code, month, participant code, premium per participant, wage and period) | By the 15th of the month after the month the premium is for | Wet Algemeen Pensioen art. 10(5) |
| Report to the APF a new employee (and the date withholding starts) or a leaver (and the date it stops), and that you stopped being an employer | Within one month | Wet Algemeen Pensioen art. 10(8), (9) |
| Give each employee proof that their pension share was withheld and the premium paid for the past year | By the end of February, or earlier on written request; at once on reaching pension age or becoming disabled | Wet Algemeen Pensioen art. 10(6), (7) |
| Pay the health premium to the insurer and give the employee proof of withholding and payment | On time under the policy terms | Wet Basiszorgverzekering art. 8(2) |
| Tell the insurer that employment ended and from when you stop paying; tell it in writing that you stopped being an employer | Within one month | Wet Basiszorgverzekering art. 8(3), (4) |

**Portal steps for the verzamelloonstaat (Tax Administration manual, December 2025).** Log in to the online portal; in the green bar click LB/AOV, then Verzamelloonstaat; click "Nieuwe Verzamelloonstaat registreren"; under Taken choose "Opvoeren dienstverbanden" to enter employees by hand or "CSV bestand dienstverbanden importeren" to upload; correct any rows the system flags (a file with more than 30% wrong rows is refused); submit when no incorrect rows remain. Amounts are whole SRD; withheld wage tax plus withheld AOV premium may not exceed the wages and pensions paid. A filed verzamelloonstaat can be corrected online until the deadline.

## Penalties and interest

- **Late or missing LB/AOV return or payment.** A default means the return or the payment was not made on time. The first default in the last seven pay periods carries no increase; the second, 5% of the tax with a minimum of SRD 5 and a maximum of SRD 250; the third and later, 10% with a minimum of SRD 5 (Uitvoeringsbeschikking LB art. 24(A)). Late payment before a top-up assessment can carry up to 10% (LB art. 26).
- **Top-up assessment (naheffing)** of tax not withheld or not paid, within five years after the end of the calendar year (LB art. 24). The increase is up to 100% (LB art. 25): 100% for serious fraud or a repeat; 25% for intent or serious gross negligence; 10% for ordinary gross negligence; none without intent or gross negligence; 5% after a voluntary correction (Uitvoeringsbeschikking LB art. 24(B)). The assessment is payable 15 days after its date (LB art. 27(2)). An employee is jointly liable for wage tax wrongly not withheld unless they told the inspector (LB art. 29(1)(e)).
- **Pension.** The Pensioenraad may impose an order subject to a penalty of SRD 500 to SRD 100,000, and an administrative fine of 10 to 1,000 times the premium due, doubled for a repeat within three years (Wet Algemeen Pensioen art. 19). An employer in breach commits an offence punishable by a fine of the sixth category of the Algemene Geldboetewet or up to one month's detention (art. 20).
- **Health insurance.** The Zorgraad may impose an order subject to a penalty of SRD 500 to SRD 100,000, and an administrative fine of 10 to 1,000 times the premium due, doubled for a repeat within three years (Wet Basiszorgverzekering art. 17). An employer in breach is punishable by a fine of the sixth category of the Algemene Geldboetewet or up to one month's detention (art. 18(3)).

## Cross-border points

- **Non-resident employees** get no wage tax tax-free amount (LB art. 13(1)(a)(2); see sr-income-tax) and pay no AOV premium, which falls only on residents (Wet AOV art. 19(1)). Treaty relief from wage tax may be applied only on a statement from the inspector (LB art. 19(3)). Detail: [sr-cross-border](sr-cross-border.md).
- **Foreign employer.** A non-resident employer's wage tax and fines are also owed by the head of its Surinamese permanent establishment, its resident permanent representative, or whoever runs the work in Suriname (LB art. 29(1)(a)).
- **Diplomats and international organisations.** Foreign nationals in the groups of Wet AOV art. 19(2) pay no AOV premium.
- **Foreigners living in Suriname** fall under the basic health insurance duty like Surinamese residents (gov.sr).

## Two worked examples that recompute

**Example 1: resident employee aged 35, monthly wage SRD 20,000.** The 4% deduction is SRD 800, capped at SRD 400 a month, so zuiver loon is SRD 19,600. Wage tax for the month is SRD 1,928 (computed in sr-income-tax, Example 1: SRD 23,136 a year divided by 12). AOV premium: 4% of SRD 19,600 = SRD 784, with no ceiling. Withheld for the Tax Administration: SRD 2,712, on the LB/AOV return by the 7th working day of the next month. The pension and health premiums come on top: the employee's pension share is half of the 2026 APF percentage times the wage clamped to the contribution base in force, paid to the APF by the 15th; the health share is half of the policy premium. Both depend on figures the employer must get from the APF and the insurer (see "Ask the client first"), so they are not computed here.

```oa-check
name: Suriname resident employee, SRD 20,000 a month, LB and AOV (2026)
inputs:
  wage: 20000
  wage_tax_month: 1928
steps:
  - deduction: min(wage * 0.04, 400)
  - zuiver_loon: wage - deduction
  - aov: zuiver_loon * 0.04
  - to_tax_admin: wage_tax_month + aov
  - net_before_pension_health: wage - to_tax_admin
expected:
  zuiver_loon: 19600
  aov: 784.00
  to_tax_admin: 2712.00
  net_before_pension_health: 17288.00
```

**Example 2 (decision): is AOV premium due? Three employees each paid SRD 8,000 a month.** The answer turns on residence and age (Wet AOV art. 19).

- **A, resident, aged 45.** Zuiver loon SRD 7,680 (deduction 4% = SRD 320, under the SRD 400 cap). Wage tax: zuiver loon is below the monthly tax-free amount of SRD 9,000 (sr-income-tax), so nil. AOV premium: 4% of 7,680 = SRD 307.20. AOV is due even though wage tax is not.
- **B, resident, aged 61.** Wage tax nil as for A. AOV premium nil: only residents under 60 are liable (art. 19(1)).
- **C, non-resident.** No tax-free amount (LB art. 13(1)(a)(2)), so belastbaar loon is SRD 7,680, and wage tax at the monthly bands of sr-income-tax (8% to SRD 3,500, 18% to SRD 7,000, 28% to SRD 10,500) is SRD 1,100.40. AOV premium nil: a non-resident is not liable.

For C the employer withholds no AOV but must withhold wage tax that A and B do not pay. Ask both facts (residence, date of birth) before the first pay.

```oa-check
name: Suriname AOV due or not, three employees at SRD 8,000 a month (2026)
inputs:
  wage: 8000
  taxfree_month: 9000
steps:
  - zuiver: wage - min(wage * 0.04, 400)
  - a_wage_tax: max(zuiver - taxfree_month, 0) * 0.08
  - a_aov: zuiver * 0.04
  - b_aov: 0
  - c_wage_tax: min(zuiver, 3500) * 0.08 + clamp(zuiver - 3500, 0, 3500) * 0.18 + clamp(zuiver - 7000, 0, 3500) * 0.28
  - c_aov: 0
  - a_withheld: a_wage_tax + a_aov
  - c_withheld: c_wage_tax + c_aov
expected:
  zuiver: 7680
  a_wage_tax: 0.00
  a_aov: 307.20
  b_aov: 0
  c_wage_tax: 1100.40
  a_withheld: 307.20
  c_withheld: 1100.40
```

## Ask the client first

1. For each employee: do they live in Suriname, and what is their date of birth? Residence decides the tax-free amount and the AOV premium; age 60 ends the AOV premium.
2. Is the employer registered with the Tax Administration (FIN) and with the APF, and which health insurer insures each employee?
3. What pension premium percentage and minimum and maximum contribution base has the APF set for 2026 (it published 8% for 2025; the 2014 base limits of SRD 500 and SRD 5,000 can be changed by staatsbesluit)? Or does the employer have its own pension scheme that gives at least the statutory rights?
4. What is each employee's monthly basic health premium on the policy, and has the employer agreed to pay more than half of it or of the pension premium?
5. What did each employee receive this month besides basic pay: overtime, vacation allowance, bonus or year-end payment, child allowance, expense reimbursements? These change wage tax, the AOV base and the pension base in different ways.
6. Does any employee hold a statement from the inspector under a tax treaty (LB art. 19(3)), or belong to a diplomatic or international-organisation group exempt from AOV?

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet Algemeen Oudedagsvoorzieningsfonds (S.B. 1981 no. 30, as last amended by S.B. 2002 no. 96), text published by the Tax Administration: read in full (arts. 1 to 23; premium arts. 18 to 20) | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-AOV.pdf | 2026-11-11 |
| Wet Loonbelasting with the Uitvoeringsbeschikking Loonbelasting (S.B. 1981 no. 186, as last amended by S.B. 2016 no. 99), text published by the Tax Administration: read LB arts. 6, 12, 13, 19 to 30 and Uitvoeringsbeschikking arts. 5 to 9 and 21 to 26 | https://belastingdienst.sr/wp-content/uploads/2024/10/Wet-Loonbelasting.pdf | 2026-11-11 |
| Tax Administration, manual Definitieve Aangifte Inkomstenbelasting natuurlijke personen (May 2026): read step 22, the "Berekening Premie AOV" screen on page 25, and the payment-reference step | https://belastingdienst.sr/wp-content/uploads/2026/05/Handleiding_1-IB-Nat.-Pers._mei-2026_compressed.pdf | 2026-11-11 |
| Tax Administration, Loonbelasting page: read in full (registration, one FIN, LB/AOV return and payment window, verzamelloonstaat) | https://belastingdienst.sr/belastingen/loonbelasting/ | 2026-11-11 |
| Tax Administration, Handleiding online verzamelloonstaat (December 2025): read in full (portal steps 1 to 16) | https://belastingdienst.sr/wp-content/uploads/2025/12/Handleiding_Verzamelloonstaat_051225.pdf | 2026-11-11 |
| Tax Administration, requirements for the online verzamelloonstaat file: read in full (fields, whole SRD, 30% rule, correction until the deadline) | https://belastingdienst.sr/wp-content/uploads/2026/01/Instructies-online-VZLS-05112025-002.pdf | 2026-11-11 |
| Wet Algemeen Pensioen 2014 (S.B. 2014 no. 113), Staatsblad scan published by the APF, read by OCR with the art. 8 page checked visually: read arts. 1 to 22 and the explanatory note | https://www.pensioen.sr/wp-content/uploads/2025/09/sb_2014__no_113_wet_algemeen_pensioen_2014-1.pdf | 2026-11-11 |
| Algemeen Pensioenfonds, home page: read the employer duties, the 50/50 split and "Pensioen premie voor het jaar 2025 ... 8% van het brutoloon" | https://www.pensioen.sr/ | 2026-11-11 |
| Algemeen Pensioenfonds, Verplichtingen page: read in full (employer and employee duties) | https://www.pensioen.sr/verplichtingen/ | 2026-11-11 |
| Algemeen Pensioenfonds, Bekendmakingen page: read the list of notices (no 2026 premium notice) | https://www.pensioen.sr/bekendmakingen/ | 2026-11-11 |
| Wet Nationale Basiszorgverzekering (S.B. 2014 no. 114), Staatsblad scan published on the APF site, read by OCR: read arts. 1 to 10, 17, 18 and the explanatory note to arts. 5 to 8 | https://www.pensioen.sr/wp-content/uploads/2025/09/S.B.-2014-no.-114-Wet-Nationale-Basiszorgverzekering_compressed-1.pdf | 2026-11-11 |
| Government of Suriname (gov.sr), Basiszorgverzekering: read in full (who is covered, entry into force 9 October 2014, premium categories, government-paid groups, employer at least 50%) | https://gov.sr/thema/basiszorgverzekering/ | 2026-11-11 |
| Uitvoeringsorgaan Basiszorg, employer duties page: read in full | https://www.basiszorg.sr/index.php/basiszorgwerkgevers/ | 2026-11-11 |
| Wet van 19 maart 2024 (S.B. 2024 no. 31) amending the Wet Minimumloon, Staatsblad text published on the APF site: read in full (minimum wage set by ministerial beschikking) | https://www.pensioen.sr/wp-content/uploads/2025/09/s-b-_2024_no-_31__wet_van_19_maart_2024__houdende_wijziging_van_de_wet_minimumloon__s-b-_2019_no-_101_.pdf | 2026-11-11 |

Not yet confirmed: the APF pension premium percentage for 2026 (the APF published 8% for 2025 under art. 8(2); the act's half-point yearly rise would continue unless changed, but no 2026 notice or staatsbesluit was found, so ask the APF) and the minimum and maximum pension contribution base in force in 2026 (only the 2014 amounts of SRD 500 and SRD 5,000 were found); whether a staatsbesluit has changed the 2014 maximum basic health premiums of art. 7(1) (gov.sr still lists them); the amount of a sixth-category fine under the Algemene Geldboetewet (S.B. 2002 no. 73, not read); the text of the Wet Pensioenfondsen en Voorzieningsfondsen (S.B. 2005 no. 75), which the Central Bank site would not serve to a script; the current statutory minimum wage (the old version's SRD 49.12 an hour from 1 April 2024 was not found in a primary text and is left out); the wage tax payment date, where the statute (LB art. 20(1)(4°), within the month in which the period ends) and the Tax Administration page (26th to the 10th of the next month) differ; whether any law after S.B. 2002 no. 96 changed the 4% AOV premium (none is on the Tax Administration law pages, and its May 2026 manual computes 4%); whether the Staatsziekenfonds (SZF) contributions named in the old version still apply to any group of employees (not found; for employees the basic health insurance law now governs).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sr-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sr-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
