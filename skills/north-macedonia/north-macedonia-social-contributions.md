---
name: north-macedonia-social-contributions
description: "Use this skill for North Macedonia mandatory insurance contributions for calendar year 2026. Trigger on social security, pension insurance, health contributions, MPIN, minimum contribution base, maximum contribution base, self-employed insurance or director contributions. It separates ordinary employees, uninsured directors, self-employed business people, professional service providers and individual farmers; identifies who bears and remits each contribution; and gives the January-to-June and July-to-December wage-period rates. It covers contribution floors and ceilings, employer extended-service contributions, monthly reporting and payment, record reconciliation and international insurance routing. Salary PIT is calculated in the payroll skill. This tier 2 skill, checked against the law, is for reviewable calculations and awaits licensed professional sign-off."
jurisdiction: MK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.3
---

# North Macedonia mandatory social contributions v0.3

**Tax year: 2026. Checked against the law, tier 2.** Amounts are MKD unless stated otherwise. Professional review remains outstanding.

## Who this applies to

[Contributions Law arts. 7, 10-13][social] define each insured group and the person responsible for calculation/remittance. Ordinary employees bear the employee contributions and the employer calculates, withholds and remits them. A self-employed person calculates/pays their own contributions. **Lump-sum self-employed administration changes with the July 2026
contribution period:** under amended art. 13 and [UJP's 22 September 2026
implementation notice][lump-implementation], UJP generates the proprietor's own
MPIN; the proprietor still pays. Before July the proprietor calculates their own
contributions. July/August calculations already filed and paid by the person do
not require a second payment against UJP's duplicate calculation. Retrieve the
UJP calculation from the taxpayer's e-services profile, registered email or UJP
office, reconcile the period/payment and retain evidence. The proprietor still
files MPIN for their employees. UJP withdrew automatic nonfiling reminders for
the proprietor's calculation duty it had taken over. Uninsured executive directors/board members/managers fall into the separate arts. 7(1)(1-a), 10(1)(1-a) class if not already insured by employment/self-employment. Do not apply employee rates to every payment called a fee.

Individual farmers and registered market-stall traders have their own base; the pension/health funds and Chamber have the calculation responsibilities specified in art. 13. Employer-funded extended-service pension contributions are separate from deductions from employee gross salary (art. 7(3)).

## Rates, bands and thresholds

| Item | Amount | Period | Official provision |
|---|---|---|---|
| Pension/disability | 18.8% | Wages January-June 2026 | [UJP dated rate table][rates], Contributions Law prior art. 25 |
| Pension/disability | 19.9% | Wages July-December 2026 | [Contributions Law art. 25(1)(1)][social]; [UJP amendment notice][july] |
| Ordinary health | 7.5% | All 2026 | [Art. 25(1)(3)][social]; [dated rate table][rates] |
| Additional injury/occupational-disease health | 0.5% for art. 11 insured groups | All 2026 | [Arts. 11, 25(1)(7)][social] |
| Unemployment | 1.2% / 0.1% for art. 12 groups | January-June / July-December wages 2026 | [Art. 25(1)(8)][social]; [dated rate table][rates] |
| Derived ordinary employee total | 28% in both periods | 2026 | Sum of applicable [art. 25][social] / [dated rates][rates] |
| Derived ordinary self-employed total | 26.8% / 27.9% | January-June / July-December 2026 | [Arts. 7(1)(5), 10(1)(3), 11-12, 25][social]; [dated rates][rates] |
| Derived uninsured director total | 26.3% / 27.4% | January-June / July-December 2026 | [Arts. 7(1)(1-a), 10(1)(1-a), 11-12, 25][social]; [dated rates][rates] |
| January-published average gross wage reference | 69,141 | January-December 2026 calculations | [UJP 22 January announcement][bases] |
| General minimum monthly base | 34,570, UJP published amount | 2026 | [Art. 15(1)][social]; [UJP announcement][bases] |
| Established professional/intellectual self-employed minimum | 69,141, one reference wage; starter exception below | 2026 | [Art. 15(2)][social]; [reference wage][bases] |
| Employee/director maximum monthly base | 1,106,256, 16 reference wages | 2026 | [Art. 16(1)-(2),(5)-(6)][social]; [UJP announcement][bases] |
| Self-employed maximum monthly base | 829,692, 12 reference wages | 2026 | [Art. 16(3),(5)-(6)][social]; [UJP announcement][bases] |
| First-calendar-year self-employed base, including professionals | 50% of 69,141 = 34,570.50 before accepted MPIN denomination | 2026 | [Art. 14(1)(14), final starter indent][social]; [UJP starter code 060][mpin-manual]; [current July 2026 MPIN package][mpin-2026] |
| Individual farmer/covered market trader base | 20% of January-published average, arithmetic 13,828.20 before operational rounding | 2026 | [Art. 14(1)(12), art. 15 exception][social]; [reference wage][bases] |

The **wage month**, not the day a bank transfer happens, determines the July split: art. 25 expressly starts with the July wage and ends with the December wage. Use the published 34,570 floor; do not silently replace it with a different rounding of half the reference wage. These parameters are not a statutory minimum-wage amount.

## The base

**Employees:** art. 14 includes salary, statutory employment additions and performance pay. Compute each fund on the appropriate base, subject to arts. 15-16. For ordinary full-month employee salary, `base = min(max(contributory gross, 34570), 1106256)`. Aggregate salary components paid by the same remitter for the same month before applying the cap; the employee cap is expressly per remitter. A cap limits contributions, not salary PIT. **Ordinary reduced hours or joining/leaving month:** [UJP's hours method, pp. 12, 22-24, 37][mpin-manual], applies both bounds in proportion to effective/paid salary hours plus overtime `h`, divided by full-time month hours `H`. With current [arts. 14(1)(2), 15-16][social] and 2026 parameters: `floor = 34570 × h/H`; `ceiling = 1106256 × h/H`; `base = min(max(contributory salary, floor), ceiling)`. Declare floor top-ups separately. Use employment dates and insured hours, not calendar-day fractions. The manual's historical rates/caps are superseded. Protected shortened hours credited as full-time, unpaid suspension and replacement benefits require their own status rules.

For mixed work/sickness, [UJP guidance step 4][hours] separately computes effective-work gross = monthly gross / full month hours × effective hours, effective-hours minimum = published minimum / full month hours × effective hours, and top-up base = max(0, effective-hours minimum - effective-work gross). Keep sickness compensation and the legally responsible payer separate.

**Self-employed:** art. 14(1)(4) starts from monthly advance net business income, or UJP-assessed lump-sum net income. After the starting calendar year, the general business floor is 34,570, established professional/intellectual services use at least 69,141, and the self-employed cap is 829,692. **Until 31 December of the calendar year activity starts**, art. 14(1)(14)'s specific half-reference base applies to self-employed entrants, including professionals: analytical base 34,570.50 in 2026. The [UJP manual p. 36][mpin-manual] assigns intellectual entrants code **060**. The [July 2026 package published by UJP][mpin-2026], linked by [current MPIN form 81][mpin-form], retains that code's 50%-of-average-gross-wage instruction for pension, health and injury health. Its legacy description says “commencing activity 2009”; the current-year application comes from the statute and manual, not that historical label. This specific starter route takes precedence over the ordinary established-professional minimum for that calendar year. Document registration/start date, use the correct insured code and reconcile UJP-accepted denomination rather than silently turning 34,570.50 into the published general minimum of 34,570. A higher elected base is permitted on personal request under art. 14(2). Business losses do not remove a contribution floor.

The ordinary self-employed group pays pension, ordinary health and 0.5% additional health because art. 11 explicitly includes art. 10(1)(3). It is not an ordinary art. 12 unemployment-insured group. Thus its derived totals differ from an employee's. A separate continued-insurance status must be tested separately under art. 12(2).

**Uninsured directors/managers:** base is their monetary remuneration (art. 14(1)(1-a)), subject to the general floor and director ceiling. They pay pension and ordinary health; art. 11 does not list the 1-a health group and art. 12 does not list this standalone director group. If the director is an employee, use employee rules for that employment instead. Do not deduct the salary personal allowance from standalone director fees without the PIT basis.

**Individual farmers/covered market traders:** use art. 14(1)(12)'s 20% base, exempt from the general floor. Pension and ordinary health follow their group in arts. 7 and 10; art. 11 does not add the 0.5% employee/self-employed charge to those groups, nor art. 12 ordinary unemployment. Follow the designated fund/Chamber calculation rather than inventing a payroll salary.

**Foreign currency:** For foreign-currency salary, **art. 14(3)** converts the contribution base at the National Bank official middle exchange rate on the **last day of the month for which contributions are calculated/paid**. Keep this distinct from PIT art. 93(2)'s receipt-date conversion for foreign income.

**Employer-funded extended-service pension:** for jobs whose 12 worked months count as 18, 17, 16, 15, 14 or 13 insured months, the additional rates are respectively **9.4%, 7.83%, 6.27%, 4.7%, 3.13%, 1.57%** through June, and **9.95%, 8.29%, 6.63%, 4.98%, 3.32%, 1.66%** for July-December ([art. 25(2)][social]; [dated table][rates]). Confirm the legally designated job and duration first. Apply the relevant extra to its applicable contributory base and add it to employer cost, not the ordinary employee deduction. Ordinary employment does not itself trigger this extra.

**Lump-sum assessed self-employment:** [the same current UJP notice][lump-implementation]
confirms that registered part-time hours do not reduce this group's assessed
net-income contribution base. Do not apply an employee's hourly salary formula.
Report sick leave with evidence to the competent UJP unit for its calculation.

Sick-pay/maternity replacement payments, domestic pensioners, non-working health-insured people, trainees and the new seasonal-engagement class have separate arts. 7-14 and 25 categories. Do not apply the ordinary employee bundle to them; their specialist computations are outside this skill's ordinary scope. No deduction, business expense or tax-loss offset reduces the insurance base beyond its own statutory definition. Salary PIT is computed after insurance in the payroll skill.

## Deadlines and filing

Establish the appropriate insurance admission/status with the competent employment/insurance body before calculating; retain employment/self-employment registration and any foreign coverage certificate. The [MPIN rulebook arts. 4-7][contrib-rules] requires electronic monthly integrated calculations with insured identifiers, gross pay, bases and separate funds. Funds submit calculations for the groups they administer under rulebook art. 5. Keep a status change/cessation aligned with the insurance register; a final contribution debt survives cessation.

[Contributions Law art. 18][social]: ordinary monthly MPIN by the **10th of the following month**, per insured person. Standalone directors' calculations are submitted **before paying remuneration** under art. 18(3), not automatically the employee monthly timetable. UJP checks/confirms the calculation before bank payment. Correct a rejected/incorrect calculation using the rulebook process; reconcile fund-by-fund and retain acceptance/payment references.

Art. 24: payment on salary/remuneration payment day. Unpaid ordinary wages still produce contribution maturity on the **15th of the following month**; the standalone director exception in art. 24(3) must be kept distinct. People paying for themselves pay by the **15th of the following month**. Under art. 22 employees receive the certified contribution calculation no later than **15 days after payment**, and the annual summary by **15 February next year**. No separate annual contribution settlement replaces these monthly obligations. Obligation during approved employment suspension follows art. 26, with any special-law exception.

## Penalties and interest

[Arts. 28, 28-a and 28-b][social] distinguish failure to issue records, incorrect/late calculation and paying remuneration without timely contributions. Legal-person fine ranges are micro **EUR 300-1,000**, small **600-2,000**, medium **1,800-6,000**, large **3,000-10,000**, in MKD equivalent. Sole trader/self-employed **EUR 100-250** and ordinary physical remitter **EUR 50-250** apply to the specified offences. Art. 28-b has separate responsible-person fines and potential activity/profession restrictions of **3-30 days**. UJP can assess missing contributions officially under art. 23; failing to file does not stop accrual. Art. 23 imports Tax Procedure Law collection; [art. 123][procedure] interest is **0.03% daily** from the day after maturity.

## Cross-border points

Contributions residence is not decided by the PIT 183-day test. Arts. 7, 10 and 12 define foreign-worker, foreign-employer and outbound-worker cover subject to ratified social-insurance agreements. Outbound assignments use the specific wage-history/reference rules in art. 14(1)(5)-(6). Check the actual agreement and competent body's certificate before removing local insurance. A tax treaty is not itself a social-insurance certificate, and EU coordination is not assumed.

## Two worked examples that recompute

**Simple: existing nonprofessional self-employed business, June 2026.** Assessed monthly business-income base 50,000 is between the floor and self-employed cap. Pension 9,400, health 3,750 and additional health 250 total 13,400. There is no ordinary unemployment contribution for this group (arts. 7, 10-12, 14-16; dated rates).

```oa-check
name: MK June 2026 self-employed fund split
inputs:
  declared_base: 50000
steps:
  - base: min(max(declared_base, 34570), 829692)
  - pension: base * 0.188
  - health: base * 0.075
  - injury_health: base * 0.005
  - total: pension + health + injury_health
expected:
  base: 50000
  pension: 9400
  health: 3750
  injury_health: 250
  total: 13400
```

**Edge: ordinary half-time employee below the hourly floor, July 2026.** The payroll has 184 full-time hours and 92 insured effective hours, with contributory salary 10,000. The hourly floor is 17,285 and ceiling 553,128. MPIN separates the 7,285 floor top-up. Apply July's employee fund rates to 17,285; analytical two-decimal amounts total 4,839.82. This is an insurance calculation, not a statement that this contractual pay satisfies labour-law minimum pay. The statutory salary and accepted MPIN rounding must be checked separately ([arts. 14-16, 25][social]; [UJP hours method, pp. 12, 37][mpin-manual]).

```oa-check
name: MK July 2026 half-time employee floor
inputs:
  full_time_hours: 184
  insured_hours: 92
  salary: 10000
steps:
  - hourly_floor: 34570 * insured_hours / full_time_hours
  - hourly_ceiling: 1106256 * insured_hours / full_time_hours
  - top_up: max(0, hourly_floor - salary)
  - base: min(max(salary, hourly_floor), hourly_ceiling)
  - pension: round(base * 0.199, 2)
  - health: round(base * 0.075, 2)
  - injury_health: round(base * 0.005, 2)
  - unemployment: round(base * 0.001, 2)
  - total: pension + health + injury_health + unemployment
expected:
  hourly_floor: 17285
  hourly_ceiling: 553128
  top_up: 7285
  base: 17285
  pension: 3439.72
  health: 1296.38
  injury_health: 86.43
  unemployment: 17.29
  total: 4839.82
```

## Ask the client first

- What is each person's actual insured status, including employment, other cover and standalone directorship?
- Which wage month, start/stop dates, hours and paid/unpaid absences does the payment cover?
- Is self-employment professional, first-calendar-year or lump-sum assessed, and what base was accepted?
- Are there multiple remitters, bonuses or prior corrections for the month?
- Is the job designated for extended-service insurance, or is foreign coverage documented?

## Sources

| Official source | URL | Read on |
|---|---|---|
| UJP current MPIN form and July 2026 client archive; static strukturaN.xml, starter code 060 | https://www.ujp.gov.mk/mk/obrasci/opis/81 ; https://www.ujp.gov.mk/files/attachment/0000/0393/klientski_13.07.2026.zip | 2026-10-24 |
| UJP MPIN manual, 2016 procedural hours method pp. 12, 22-24, 37; historical figures superseded by 2026 law/table | https://www.ujp.gov.mk/files/attachment/0000/0526/ISBN_978-608-4592-70-9_Mesecna_presmetka_za_integrirana_naplata_11.03.2016.pdf | 2026-10-24 |
| UJP 22 September 2026 implementation, July/August proprietor calculations, duplicate payments, employee returns and part-time/sickness treatment | https://ujp.gov.mk/mk/javnost/soopstenija/pogledni/1284?print=1 | 2026-10-24 |
| UJP, gross salary calculation guidance, steps 2-4 | https://www.ujp.gov.mk/file/pravni_lica/category/643?print=1 | 2026-10-24 |
| Mandatory Social Insurance Contributions Law, through Gazette 148/2026 | https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf | 2026-10-24 |
| UJP, dated contribution-rate tables | https://www.ujp.gov.mk/en/vodic/category/641?print=1 | 2026-10-24 |
| UJP, 22 January 2026 contribution-base announcement | https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1187 | 2026-10-24 |
| State Statistical Office, average gross wage November 2025 (69,141), published 21 January 2026 | https://www.stat.mk/en/stat/population-and-living-conditions/labour-market/average-monthly-gross-wage-paid-per-employee/average-monthly-gross-wage-paid-per-employee-november-2025/ | 2026-10-30 |
| UJP, 13 July 2026 contributions amendment notice | https://ujp.gov.mk/en/javnost/soopstenija/pogledni/1266?print=1 | 2026-10-24 |
| Contribution calculation/payment rulebook, MPIN structure | https://www.ujp.gov.mk/files/attachment/0000/0198/Pravilnik_za_nacinot_na_presmetka_i_uplata_na_pridonesite_od_zadolzitelno_socijalno_osiguruvanje_od_09.12.2008_godina.pdf | 2026-10-24 |
| Tax Procedure Law, through Gazette 3/2025 | https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |

[lump-implementation]: https://ujp.gov.mk/mk/javnost/soopstenija/pogledni/1284?print=1
[mpin-form]: https://www.ujp.gov.mk/mk/obrasci/opis/81
[mpin-2026]: https://www.ujp.gov.mk/files/attachment/0000/0393/klientski_13.07.2026.zip
[mpin-manual]: https://www.ujp.gov.mk/files/attachment/0000/0526/ISBN_978-608-4592-70-9_Mesecna_presmetka_za_integrirana_naplata_11.03.2016.pdf
[hours]: https://www.ujp.gov.mk/file/pravni_lica/category/643?print=1
[social]: https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf
[rates]: https://www.ujp.gov.mk/en/vodic/category/641?print=1
[bases]: https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1187
[july]: https://ujp.gov.mk/en/javnost/soopstenija/pogledni/1266?print=1
[contrib-rules]: https://www.ujp.gov.mk/files/attachment/0000/0198/Pravilnik_za_nacinot_na_presmetka_i_uplata_na_pridonesite_od_zadolzitelno_socijalno_osiguruvanje_od_09.12.2008_godina.pdf
[procedure]: https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf

Not yet confirmed: A universal operational MPIN rounding convention; reconcile analytical decimals to UJP's accepted calculation. Specialist protected-hours and replacement-benefit computations are outside the ordinary employee scope. No ordinary insured group is omitted on that account.

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
