---
name: slovenia-payroll
description: "Slovenian payroll for employees for tax year 2026. Covers the monthly gross-to-net: employee contributions of 22.1% plus 1% long-term care, employer contributions of 16.1% plus 1% long-term care, the flat compulsory health contribution (EUR 39.36 a month from 1 March 2026), the minimum contribution base (60% of the average wage, EUR 1,521.62) against the 2026 minimum wage of EUR 1,481.88, withholding on the monthly scale with the 2026 general allowance (EUR 462.66 a month plus the low-income taper), the REK-O return filed on the pay date, and fines and late interest. Trigger phrases: Slovenia payroll, gross to net Slovenia, bruto neto plača, akontacija dohodnine, REK-O, REK-1, minimalna plača 2026, najnižja osnova za prispevke, OZP, prispevek za dolgotrajno oskrbo. Out of scope: the self-employed (s.p.) and contribution bases in depth (slovenia-social-contributions), the annual return (slovenia-income-tax), residence and treaties (si-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/slovenia-payroll"
  jurisdiction: "SI"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Slovenia payroll (2026)

> **Source-cited draft.** Drafted from the Social Security Contributions Act (ZPSV), the Pension and Disability Insurance Act (ZPIZ-2), the Health Care and Health Insurance Act (ZZVZZ), the Long-Term Care Act (ZDOsk-1), the Personal Income Tax Act (ZDoh-2) and the Tax Procedure Act (ZDavP-2), as consolidated on pisrs.si, with figures from the Financial Administration (FURS), the Health Insurance Institute (ZZZS) and gov.si, read on 2026-10-24. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Slovenian professional.

Tax year: the calendar year. Authority: the Financial Administration (Finančna uprava, FURS) collects withholding tax and contributions through eDavki. The ZZZS runs health and long-term care insurance; the ZPIZ runs pensions. Currency: euro. For the self-employed and the contribution bases in depth, see `slovenia-social-contributions`. For the annual assessment and all allowances, see `slovenia-income-tax`.

## Who this applies to

- **Employers** that pay wages to anyone in an employment relationship in Slovenia: companies, sole proprietors (s.p.) with staff, branches of foreign companies. They calculate, withhold and pay the employee's contributions and tax, and pay their own contributions (ZDavP-2 art. 352(2) and (3); ZPSV art. 6).
- **Employees** insured under ZPIZ-2 art. 14 and ZZVZZ art. 15(1)(1), whatever their nationality.
- **Main employer and secondary employer.** The employer from whom the employee earns most of their employment income is the main employer and withholds on the monthly scale with allowances. Any other employer withholds a flat 25% with no allowances (ZDoh-2 art. 127(2), (3) and (6)).
- **Not covered here:** contract work (podjemna pogodba, 25% withholding under ZDoh-2 art. 127(10)), student work, directors who are also shareholders (insured on a 90% minimum base, see `slovenia-social-contributions`), pensioners who work, and the special rules for companies employing disabled staff.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Pension and disability, employee / employer | 15.50% / 8.85% | 2026 | ZPSV art. 8, [pisrs.si](https://pisrs.si/pregledPredpisa?id=ZAKO984) |
| Health (illness and injury outside work), employee / employer | 6.36% / 6.56% | 2026 | ZPSV art. 11(1) |
| Injury at work and occupational disease, employer | 0.53% | 2026 | ZPSV art. 12(1) |
| Parental care, employee / employer | 0.10% / 0.10% | 2026 | ZPSV art. 13 |
| Employment (unemployment), employee / employer | 0.14% / 0.06% | 2026 | ZPSV art. 14 |
| Total ZPSV contributions, employee / employer | 22.10% / 16.10% | 2026 | ZPSV arts. 8, 11 to 14 |
| Long-term care (dolgotrajna oskrba), employee / employer | 1% / 1%, for pay for periods from 1 July 2025 | 2026 | ZDOsk-1 arts. 55, 56(1) and 137, [pisrs.si](https://pisrs.si/pregledPredpisa?id=ZAKO8819); ZZZS table, [zzzs.si](https://zavezanec.zzzs.si/fileadmin/user_upload/dokumenti/zavezanec/do/preglednica_zavarovanci__do_furs__v2.pdf) |
| All percentage contributions, employee / employer | 23.10% / 17.10% | 2026 | sum of the rows above |
| Compulsory health contribution (obvezni zdravstveni prispevek, OZP), employee | EUR 39.36 a month from 1 March 2026 (EUR 37.17 in January and February 2026) | 2026 | ZZVZZ art. 48; Uradni list RS 16/26 as cited by FURS, [fu.gov.si](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Prispevki_za_socialno_varnost/Samozaposleni/SZ_10_2026.xlsx) |
| Average monthly gross wage for 2025 | EUR 2,536.03 | 2026 | FURS contribution tables, [fu.gov.si](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/prispevki_za_socialno_varnost/osnove_za_placilo_ter_zneski_prispevkov_za_socialno_varnost/) |
| Minimum monthly contribution base (60% of the last known average wage) | EUR 1,521.62 (EUR 1,436.95 while the 2024 average was the last known) | 2026 | ZPIZ-2 art. 144(4), [pisrs.si](https://pisrs.si/pregledPredpisa?id=ZAKO6280); FURS tables |
| Maximum contribution base for employees | none | 2026 | ZPIZ-2 art. 144(1); ZPSV art. 3 |
| Minimum wage (gross, full time) | EUR 1,481.88 a month for work from 1 January 2026 | 2026 | Ministry of Labour, [gov.si](https://www.gov.si/novice/2026-01-28-dolocen-znesek-minimalne-place-za-2026/) |
| Monthly withholding scale (main employer) | 16% to EUR 810.12; EUR 129.62 + 26% to 2,382.70; EUR 538.49 + 33% to 4,765.41; EUR 1,324.78 + 39% to 6,862.19; EUR 2,142.53 + 50% above | 2026 | ZDoh-2 arts. 122 and 127(2); FURS 2026 scale, [fu.gov.si](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Dohodnina/Letna_odmera_dohodnine/Opis/Lestvica_za_leto_2026.docx) |
| General allowance in monthly withholding | EUR 462.66; if monthly gross is up to EUR 1,480.51, add 1,736.03 minus 1.17259 times monthly gross | 2026 | ZDoh-2 arts. 111 and 127(3); FURS 2026 scale |
| Annual general allowance (for the year-end assessment) | EUR 5,551.93; extra taper if total income is up to EUR 17,766.18 | 2026 | ZDoh-2 art. 111; FURS 2026 scale |
| Monthly dependant allowance, first / second / third child | EUR 249.65 / 271.40 / 452.67 | 2026 | ZDoh-2 art. 114; FURS 2026 scale |
| Secondary employer withholding | 25%, no allowances | 2026 | ZDoh-2 art. 127(6) |
| Late payment interest | 10.15% a year from 1 January 2026; 10.40% from 1 July 2026 | 2026 | ZDavP-2 art. 96; ZPOMZO-1 art. 2; [Uradni list RS 2/2026](https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2026-01-0011); [Uradni list RS 1124/2026](https://pisrs.si/api/uradni-list/objava/u20261124.pdf) |

## The taxable base

**Contribution base.** Contributions are due on gross pay, wage compensation and all other pay from employment, including benefits in kind and work-related reimbursements, except where the law exempts them (ZPSV art. 3(1) and (3); ZPIZ-2 art. 144(1)). Reimbursements, jubilee awards, severance on retirement and similar items bear contributions only on the part that is taxed. Holiday pay (regres) bears contributions only on the part above 100% of the last known average monthly wage (ZPIZ-2 art. 144(2)). There is no upper limit for employees.

**The minimum base.** If a month's pay is below 60% of the last known average annual wage (EUR 1,521.62), contributions are still due on EUR 1,521.62 (ZPIZ-2 art. 144(4)). The employee pays their share only on the pay actually earned. The employer pays the employee's share on the difference, as well as its own share on the whole minimum base (ZPIZ-2 art. 152(2); ZZVZZ art. 50). FURS says all contributions are due on the difference, reported as base type P02 on the REK-O (FURS note on REK corrections, 21 December 2023). The long-term care contribution follows the same base and is also due on the difference (ZDOsk-1 art. 56(4); ZZZS table). A full-time employee on the 2026 minimum wage (EUR 1,481.88) is below the minimum base, so the employer pays on the EUR 39.74 difference.

**Long-term care.** Since pay for July 2025, the employee and the employer each pay 1% on the health contribution base (ZDOsk-1 arts. 56(1), (4) and 137). An employee whose employer does not pay Slovenian health contributions pays 2% alone (art. 56(2)).

**Compulsory health contribution (OZP).** A flat amount per calendar month, whatever the number of insured days. The main employer withholds it from the first payment for the month (ZZVZZ art. 48). It does not depend on pay.

**Tax base for withholding.** Gross employment income less the contributions the employee must pay (ZDoh-2 art. 41(1)), less one twelfth of the allowances the employee is entitled to (art. 127(3)). Deduct the employee's 22.1%, the 1% long-term care contribution and the OZP. All three are compulsory social security contributions the employee must pay: ZPSV art. 1 defines contributions for compulsory health insurance as social security contributions, ZZVZZ art. 48 levies the OZP as a health insurance contribution paid by the insured person, and ZDOsk-1 arts. 51(2) and 56.a(1) treat long-term care insurance as social insurance and its contribution as a compulsory social security contribution. The REK-O lists the OZP (field A072a) among the employee's social security contributions, whose total (A075) is taken into account in computing the withholding (Pravilnik, Uradni list RS 4/2025, Annex 1; FURS REK-O instructions, 10th edition, October 2026, point 5.4). Then apply the monthly scale.

**General allowance.** EUR 462.66 a month, which is one twelfth of the EUR 5,551.93 annual allowance. If the month's gross employment income is up to EUR 1,480.51, the allowance rises by 1,736.03 minus 1.17259 times that gross. At EUR 1,480.51 and above the extra is nil. The employee can ask the employer to apply only the EUR 462.66 (FURS 2026 scale). Dependant allowances apply only if the employee tells the main employer in writing (ZDavP-2 art. 287). The allowance for employees under 29 and the other personal allowances are in `slovenia-income-tax`.

**Annual assessment.** Monthly withholding is an advance. FURS issues the informative calculation for the year and squares it up. See `slovenia-income-tax`.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| File the withholding return REK-O (obračun davčnega odtegljaja), with the contributions calculated in it | no later than the day the pay is paid | ZDavP-2 arts. 284(1), 352(2) and (3), 353(2) |
| Pay the withheld tax and the contributions | no later than 5 days after the pay is paid | ZDavP-2 arts. 283(1) and 353(2) |
| Give the employee the data from the REK-O (pay slip data) | the same deadline as the REK-O | ZDavP-2 arts. 284(2) and 353(2) |
| Register the employee for health insurance; the same registration covers long-term care | under the health insurance rules | ZDOsk-1 art. 54(6) |

The REK-O has applied to payments from 1 January 2023. It replaced the REK-1, which is now used only to correct payments made up to 31 December 2022 (FURS note of 21 December 2023). The form's content is set by the Pravilnik o obračunu davčnih odtegljajev (Uradni list RS 4/2025). Contributions are calculated at the rates in force on the day the obligation arises (ZDavP-2 art. 352(6)).

## Penalties and interest

- **REK-O not filed, filed late or filed wrongly.** Fine EUR 1,200 to 15,000 for a company, EUR 3,200 to 30,000 for a medium or large company, EUR 800 to 10,000 for an s.p. employer (ZDavP-2 art. 397(1) point 2). The responsible person of a company is fined EUR 600 to 4,000, or EUR 800 to 4,000 in a medium or large company (art. 397(3)).
- **No fine on a proper correction.** An employer that files or corrects the return under the self-report and correction rules (ZDavP-2 arts. 53, 54, 54.a, 55 or 57) is not fined under art. 397(1) point 2 (art. 399).
- **Late payment.** Tax and contributions paid late carry late interest at the statutory rate: 10.15% a year from 1 January 2026 and 10.40% from 1 July 2026 (ZDavP-2 art. 96(1); ZPOMZO-1 art. 2; Uradni list RS 2/2026 and 1124/2026). ZPSV art. 15 applies ZDavP-2 to contributions.
- **OZP and long-term care.** Neither can be written off, deferred or paid in instalments on request (ZZVZZ art. 48; ZDOsk-1 art. 56(8)).

## Cross-border points

- **Which country's contributions.** In the EU, EEA and Switzerland, Regulation (EC) 883/2004 decides which country insures the worker. A worker posted from Slovenia keeps paying Slovenian contributions on the pay for equal work in Slovenia, unless a treaty says otherwise (ZPSV art. 3(2)). ZZZS issues the A1 certificate.
- **Workers coming to Slovenia.** Compulsory contributions paid to a comparable foreign scheme reduce the Slovenian tax base, if the worker was not resident in Slovenia just before starting the job and already paid into that scheme (ZDoh-2 art. 41(2)).
- **Non-resident employees.** The allowances are for residents. An EU or EEA resident with at least 90% of taxable income from Slovenia can claim them in a return (ZDoh-2 art. 116). Residence rules and treaty relief are in `si-cross-border`.
- **Second job.** Only the main employer applies the scale and allowances. A secondary employer withholds 25% (ZDoh-2 art. 127(6)).

## Worked examples

### Example 1: standard employee, October 2026

A company pays a resident employee EUR 2,500 gross for October 2026. It is the main employer. The employee claims no dependants.

Employee contributions at 22.1%: EUR 552.50. Long-term care at 1%: EUR 25.00. OZP: EUR 39.36. Gross is above EUR 1,480.51, so the allowance is EUR 462.66. Tax base: 2,500 - 552.50 - 25.00 - 39.36 - 462.66 = EUR 1,420.48. Tax: 129.62 + 26% of (1,420.48 - 810.12) = EUR 288.31. Net pay: EUR 1,594.83. Employer contributions: 16.1% = EUR 402.50, plus long-term care 1% = EUR 25.00. Cost to the employer: EUR 2,927.50. The REK-O is due on the pay date and the payment within 5 days of it.

```oa-check
name: Slovenia employee, EUR 2,500 gross, October 2026, main employer
inputs:
  gross: 2500
  ozp: 39.36
  allowance: 462.66
steps:
  - ee_contrib: round(gross * 0.221, 2)
  - ee_ltc: round(gross * 0.01, 2)
  - tax_base: gross - ee_contrib - ee_ltc - ozp - allowance
  - tax: round(129.62 + (tax_base - 810.12) * 0.26, 2)
  - net: gross - ee_contrib - ee_ltc - ozp - tax
  - er_contrib: round(gross * 0.161, 2)
  - er_ltc: round(gross * 0.01, 2)
  - employer_cost: gross + er_contrib + er_ltc
expected:
  ee_contrib: 552.50
  tax_base: 1420.48
  tax: 288.31
  net: 1594.83
  er_contrib: 402.50
  employer_cost: 2927.50
```

### Example 2: minimum wage, below the minimum contribution base

A company pays a full-time resident employee the 2026 minimum wage of EUR 1,481.88 for October 2026. The minimum contribution base is EUR 1,521.62, so the gap is EUR 39.74.

The employee pays 22.1% and 1% only on the wage: EUR 327.50 and EUR 14.82, plus the OZP of EUR 39.36. The monthly allowance taper gives 1,736.03 - 1.17259 x 1,481.88, which is below zero, so the allowance is the flat EUR 462.66. Tax base: 1,481.88 - 327.50 - 14.82 - 39.36 - 462.66 = EUR 637.54. Tax at 16%: EUR 102.01. Net pay: EUR 998.19.

The employer pays its 16.1% and 1% on the whole minimum base: EUR 244.98 and EUR 15.22. It also pays the employee's 23.1% on the EUR 39.74 gap: EUR 9.18. Cost to the employer: EUR 1,751.26.

```oa-check
name: Slovenia minimum wage EUR 1,481.88, October 2026, minimum base EUR 1,521.62
inputs:
  gross: 1481.88
  min_base: 1521.62
  ozp: 39.36
steps:
  - allowance: 462.66 + max(1736.03 - 1.17259 * gross, 0)
  - ee_contrib: round(gross * 0.221, 2)
  - ee_ltc: round(gross * 0.01, 2)
  - tax_base: gross - ee_contrib - ee_ltc - ozp - allowance
  - tax: round(tax_base * 0.16, 2)
  - net: gross - ee_contrib - ee_ltc - ozp - tax
  - gap: max(min_base - gross, 0)
  - er_on_gap: round(gap * 0.231, 2)
  - er_contrib: round(min_base * 0.161, 2)
  - er_ltc: round(min_base * 0.01, 2)
  - employer_cost: gross + er_contrib + er_ltc + er_on_gap
expected:
  allowance: 462.66
  ee_contrib: 327.50
  tax_base: 637.54
  tax: 102.01
  net: 998.19
  er_on_gap: 9.18
  er_contrib: 244.98
  employer_cost: 1751.26
```

## Ask the client first

1. Is this the employee's main employer? If not, withholding is 25% with no allowances.
2. Is the job full time, and which month does each payment relate to? The minimum base and the OZP work by month, and the OZP changed on 1 March 2026.
3. Has the employee given written notice of dependants, or asked for only the flat EUR 462.66 allowance?
4. Is the employee resident in Slovenia, and are they insured here or abroad (A1 certificate)?
5. What else is paid with the wage: holiday pay, bonuses, benefits in kind, reimbursements above the tax-free limits?
6. Is the employee under 29, over 70, or disabled? Each changes the allowances (see `slovenia-income-tax`).

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Security Contributions Act (ZPSV), consolidated NPB 14: arts. 1, 3, 6, 8, 11 to 16 | https://pisrs.si/pregledPredpisa?id=ZAKO984 | 2026-10-24 |
| Pension and Disability Insurance Act (ZPIZ-2), consolidated NPB 27 to Uradni list RS 90/25: arts. 14, 144, 152 | https://pisrs.si/pregledPredpisa?id=ZAKO6280 | 2026-10-24 |
| Health Care and Health Insurance Act (ZZVZZ), consolidated NPB 42: arts. 48, 50 | https://pisrs.si/pregledPredpisa?id=ZAKO213 | 2026-10-24 |
| Long-Term Care Act (ZDOsk-1), consolidated NPB 2: arts. 51, 54, 55, 56, 56.a, 137 | https://pisrs.si/pregledPredpisa?id=ZAKO8819 | 2026-10-24 |
| Personal Income Tax Act (ZDoh-2): arts. 41, 111, 114, 116, 122, 127 | https://pisrs.si/pregledPredpisa?id=ZAKO4697 | 2026-10-24 |
| Tax Procedure Act (ZDavP-2), consolidated to Uradni list RS 100/25: arts. 96, 283, 284, 287, 352, 353, 397, 399 | https://pisrs.si/pregledPredpisa?id=ZAKO4703 | 2026-10-24 |
| Act on the Prescribed Default Interest Rate (ZPOMZO-1): art. 2 | https://pisrs.si/pregledPredpisa?id=ZAKO3695 | 2026-10-24 |
| Minister of Finance, default interest rate from 1 January 2026, Uradni list RS 2/2026 | https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2026-01-0011 | 2026-10-24 |
| Minister of Finance, default interest rate from 1 July 2026, Uradni list RS 1124/2026 | https://pisrs.si/api/uradni-list/objava/u20261124.pdf | 2026-10-24 |
| FURS, REK-O form and filing instructions, 10th edition, October 2026: points 5.3 to 5.5 | https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/rek_obrazci/ | 2026-10-24 |
| Pravilnik o obračunu davčnih odtegljajev, Uradni list RS 4/2025, Annex 1 (REK-O fields) | https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2025-01-0139 | 2026-10-24 |
| FURS, 2026 tax scale and allowances (notice of 15 December 2025) | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Dohodnina/Letna_odmera_dohodnine/Opis/Lestvica_za_leto_2026.docx | 2026-10-24 |
| FURS, contribution bases and amounts 2026 (self-employed tables for January, February, March and October 2026: average wage, 60% base, OZP) | https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/prispevki_za_socialno_varnost/osnove_za_placilo_ter_zneski_prispevkov_za_socialno_varnost/ | 2026-10-24 |
| FURS, REK forms page and the note on correcting REK forms for the difference to the minimum base (21 December 2023) | https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/rek_obrazci/ | 2026-10-24 |
| ZZZS, long-term care contribution table for insured persons supervised by FURS | https://zavezanec.zzzs.si/fileadmin/user_upload/dokumenti/zavezanec/do/preglednica_zavarovanci__do_furs__v2.pdf | 2026-10-24 |
| Ministry of Labour, minimum wage for 2026 (28 January 2026) | https://www.gov.si/novice/2026-01-28-dolocen-znesek-minimalne-place-za-2026/ | 2026-10-24 |

Not yet confirmed: the Uradni list RS 16/26 order setting the OZP at EUR 39.36 was not read (the figure is from the FURS 2026 tables, which cite it); the minimum wage decision in the Uradni list was not read (the figure is from the ministry's notice); the exact payment date from which employers moved from EUR 1,436.95 to EUR 1,521.62 as the minimum base (FURS applies the 2025 average from the February 2026 self-employed contributions); who bears the employee's 0.24% parental care and employment share on the gap to the minimum base (ZPIZ-2 and ZZVZZ put the pension and health shares on the employer; the employment and parental care acts were not read); the deadline for registering a new employee for insurance; the 2026 version of the REK-O field list with the long-term care fields.

> Contributed by Michael Cutajar.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `slovenia-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/slovenia-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
