---
name: croatia-social-contributions
description: "Croatian mandatory social contributions (doprinosi) for tax year 2026, for employees and the self-employed. Covers pension Pillar I 15% and Pillar II 5% (20% for Pillar I only), the 16.5% health contribution, the 2026 average wage of EUR 1,993 and the bases built on it (minimum EUR 757.34, maximum EUR 11,958 a month and EUR 143,496 a year for pension), the low-wage pension relief (EUR 300 cut up to EUR 700 gross, tapering to EUR 1,300), the first-time trainee and grandfathered first-job reliefs, the fixed monthly bases for sole traders (obrt), freelancers and flat-rate taxpayers, payment deadlines, JOPPD reporting, and fines. Trigger on: doprinosi, Croatia social security, mirovinsko I. stup II. stup, zdravstveno 16.5%, obrt doprinosi 2026, paušalist doprinosi, najviša osnovica 2026, olakšica 700 1300. Out of scope: income tax withholding and gross to net (croatia-payroll), annual income tax (croatia-income-tax), posted workers and treaties (hr-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/croatia-social-contributions"
  jurisdiction: "HR"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Croatia social contributions (tax year 2026) v0.2

> **Source-cited draft.** No accountant has reviewed this skill yet. Figures come from the consolidated Contributions Act in the Tax Administration (Porezna uprava) register and from Narodne novine, read on 23 and 24 October 2026. It prepares working papers; it is not authority to file or pay.

This is the social contributions (SC) skill for the Croatian pack. It links rather than repeats:

- Income tax withholding, gross to net and the JOPPD timetable for salaries: [croatia-payroll](croatia-payroll.md).
- Annual income tax and income from self-employment: [croatia-income-tax](croatia-income-tax.md).
- Posted workers, non-residents and treaties: [hr-cross-border](hr-cross-border.md).

Laws used: the Contributions Act (Zakon o doprinosima, "ZoD", NN 84/08 as amended to NN 152/24, in force from 1 January 2025), the Contributions Rulebook (Pravilnik o doprinosima, as amended to NN 16/25) and the Order on contribution bases for 2026 (Naredba, NN 150/25, applying from 1 January 2026). The Tax Administration collects contributions (ZoD art. 6(2)). Currency: euro (EUR).

## Who this applies to

**Employees.** The employee bears the pension contributions out of gross pay ("iz osnovice"); the employer bears health on top ("na osnovicu"). The employer computes and pays both (ZoD art. 19 and 20).

**The self-employed.** Sole traders (obrt), freelancers (slobodno zanimanje), sportspeople, farmers and other registered self-employed people are their own contribution payers and compute and pay for themselves (ZoD art. 64 and 68). Their base is a fixed monthly amount tied to the average wage, not their actual profit (ZoD art. 66 and 70).

**Others.** Board members and directors without an employment contract, people working in Croatia for a foreign employer with no branch, and people with no other cover pay on bases fixed by Tax Administration decision (Order NN 150/25 art. 7 and 8).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Pension Pillar I, member of Pillar II too | 15% | 2026 | ZoD art. 13(1) point 1.2, https://porezna-uprava.gov.hr/Propisi |
| Pension Pillar I, Pillar I only | 20% | 2026 | ZoD art. 13(1) point 1.1 |
| Pension Pillar II | 5% | 2026 | ZoD art. 17(1) point 1 |
| Health | 16.5% | 2026 | ZoD art. 14(1) point 1 |
| Work injury health contribution (certain insured, e.g. trainees outside employment) | 0.5% | 2026 | ZoD art. 14(1) point 4 |
| Average wage (Jan to Aug 2025) | EUR 1,993.00 | 2026 | Naredba NN 150/25 art. 2, https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html |
| Minimum monthly base, full time (x 0.38) | EUR 757.34 | 2026 | Naredba art. 3; ZoD art. 200 |
| Maximum monthly base, pension (x 6.0) | EUR 11,958.00 | 2026 | Naredba art. 4; ZoD art. 204 and 205 |
| Maximum annual base, Pillar I (x 6.0 x 12) | EUR 143,496.00 | 2026 | Naredba art. 5; ZoD art. 206 and 208 |
| Low-wage relief, gross up to EUR 700 | Pillar I base cut by EUR 300 | 2026 | ZoD art. 21.a(1), https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1611.html |
| Low-wage relief, gross EUR 700.01 to 1,300 | Pillar I base cut by 0.5 x (1,300 - gross) | 2026 | ZoD art. 21.a(2) |
| Obrt paying income tax on actual income (x 0.65) | EUR 1,295.45 a month | 2026 | Naredba art. 6 row 1; ZoD art. 66(1) point 1 |
| Freelancer paying income tax (x 1.1) | EUR 2,192.30 a month | 2026 | Naredba art. 6 row 3; ZoD art. 66(1) point 2 |
| Nurse, dental technician, physiotherapist, journalist, film worker (x 0.65) | EUR 1,295.45 a month | 2026 | Naredba art. 6; ZoD art. 66(2) |
| Self-employed paying profit tax instead (x 1.1) | EUR 2,192.30 a month | 2026 | Naredba art. 6 rows 2, 4; ZoD art. 82(2) |
| Flat-rate (paušal) obrt (x 0.4) | EUR 797.20 a month | 2026 | Naredba art. 7 row 1; ZoD art. 70 |
| Board member or executive director without employment (x 1.0) | EUR 1,993.00 a month | 2026 | Naredba art. 7 row 6; ZoD art. 92 |
| Employed in Croatia by a foreign employer with no Croatian branch (x 1.0) | EUR 1,993.00 a month | 2026 | Naredba art. 7 row 9; ZoD art. 109 |
| Voluntary higher base for the self-employed | coefficients 0.5 to 6.0 | 2026 | ZoD art. 203(2) |

## The taxable base

**Employees.** The monthly base is salary taxable as employment income, including pay in kind, and never less than what the contract or collective agreement requires (ZoD art. 21(1) and (2)). For full-time work it cannot fall below EUR 757.34; part-time is pro rata to hours (ZoD art. 200). Pension contributions (Pillar I and II) stop at EUR 11,958 a month (ZoD art. 204). Pillar I also stops once pay from the same employer for the year reaches EUR 143,496 (ZoD art. 206(3) and 207). Health has no cap.

**Low-wage pension relief.** The Pillar I base is cut by EUR 300 where total monthly gross pay is up to EUR 700, and by 0.5 x (1,300 - gross) from EUR 700.01 to 1,300 (ZoD art. 21.a(1) and (2)). Points to apply:

- It applies whatever the days or hours in the month (art. 21.a(3)); below EUR 300 gross the cut stops at the gross pay (Contributions Rulebook art. 16.b(1)).
- Salary for a month paid in parts: the cut goes against the first payment (art. 21.a(4)).
- Two or more employers: each applies its share of the cut in proportion to its gross pay, from the worker's statement or from Tax Administration data (art. 21.a(5); Rulebook art. 16.b(3)). A new employment starting mid-month needs the statement to all employers, or no cut (art. 21.a(6)).
- Pension rights are counted on the full base (art. 21.a(7)).
- It cuts the Pillar I base only. Pillar II stays on full gross ([Vlada, 2023 tax changes](https://vlada.gov.hr/UserDocsImages/2016/Sjednice/2023/Svibanj/220%20sjednica%20VRH/Izmjene%20poreznih%20propisa.pdf)).

**Young and first-time workers.** A first-time employee under a vocational training contract (ugovor o stručnom osposobljavanju) pays only the pension contributions for up to one year; the employer pays no health contribution (ZoD art. 7 point 31, art. 20(2) and (3)). The broader health exemption for first permanent contracts and for young persons was repealed from 1 January 2025. An employer that started using it before then keeps it until it ends (NN 152/24 art. 2 and 5, https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2506.html). The young-worker relief that applies to new hires in 2026 is an income tax relief, not a contribution relief: see [croatia-payroll](croatia-payroll.md).

**Self-employed.** Contributions are pension (Pillar I and II) and health on the fixed monthly base for the activity (ZoD art. 65 and 69), whatever the actual profit. The self-employed person can choose a higher base by coefficient from 0.5 to 6.0 (ZoD art. 203). Where the base is a monthly amount and insurance covers part of a month, the base is pro rata to the days (ZoD art. 202).

**Second activity.** A person already insured on another basis (for example an employee) who also runs a second activity pays on an annual base: pension 10% (or 7.5% Pillar I plus 2.5% Pillar II) and health 7.5% (ZoD art. 13(3), 14(2) and 17(2)). The annual base is the activity's income or profit (Contributions Rulebook, "druga djelatnost").

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Contributions on salary | With the salary payment | ZoD art. 24(1) |
| Contributions where salary is not paid | By the last day of the month for the previous month | ZoD art. 24(2) |
| Contributions on pay in kind | By the 15th of the following month | ZoD art. 24(3) |
| Foreign EU employer without a branch | Within 30 days of the salary payment | ZoD art. 24.a(1) |
| Self-employed (obrt, freelancer) on actual income | Computed and due by the 15th of the month for the previous month | ZoD art. 67 |
| Flat-rate (paušal) obrt | Due by the 15th of the month for the previous month | ZoD art. 71 |
| JOPPD report | On the day of payment, or at latest the next working day; pay in kind by the 15th of the following month | Pravilnik o porezu na dohodak art. 79(1) and (5) |

Contributions are reported on JOPPD through ePorezna (Pravilnik o porezu na dohodak art. 77). A flat-rate obrt's obligation is fixed by Tax Administration decision (ZoD art. 68(2)).

## Penalties and interest

| Breach | Fine | Source |
|---|---|---|
| Employer fails to compute, set the base, pay on time or report | EUR 660 to 13,270; responsible person EUR 660 to 2,650 | ZoD art. 249(1) point 1, (2) |
| Self-employed on actual income or profit fails to compute, pay or report | EUR 660 to 6,630; responsible person in a legal person EUR 390 to 2,650 | ZoD art. 250 |
| Self-employed (incl. paušal) does not pay a due contribution on time | EUR 660 to 3,980 | ZoD art. 252 |

Late payment interest runs from the due date (General Tax Act art. 130(3)). The General Tax Act leaves the interest rate to a special regulation (art. 130(1)). The Obligations Act sets the default interest rate in relationships other than commercial contracts at the ECB reference rate plus three percentage points, fixed each half year (Zakon o obveznim odnosima art. 29(2) and (8)). The Croatian National Bank published a reference rate of 2.40% in force on 1 July 2026 (NN 68/26, https://narodne-novine.nn.hr/clanci/sluzbeni/2026_06_68_826.html), which gives 5.40% a year from 1 July to 31 December 2026. Whether that rate is the one charged on tax and contribution debts is not yet confirmed in an official text: the Interest Act provision that brought taxes and contributions under the general default rate (Zakon o kamatama art. 1(2)) ceased to apply from 2008 (Obligations Act art. 1164(2)). Interest on Pillar II contributions found due in an audit cannot be reduced in a tax settlement (General Tax Act art. 104(6)).

## Cross-border points

- **Which system applies.** Within the EU, EEA and Switzerland, Regulation 883/2004 decides; an A1 certificate keeps a posted worker in the home system. A foreign EU employer of a person insured in Croatia pays Croatian contributions itself (ZoD art. 19.a), due within 30 days (art. 24.a). A self-employed person working in another member state but covered by Croatian law pays as a Croatian self-employed person (ZoD art. 67.b).
- **Working in Croatia for a foreign employer with no branch.** Base EUR 1,993.00 a month, fixed by Tax Administration decision (Naredba art. 7 row 9; ZoD art. 109).
- **Treaties and residence:** [hr-cross-border](hr-cross-border.md).

## Worked examples

### Example 1: low-wage employee, gross EUR 1,000

An employee in Pillar I and II earns EUR 1,000 gross in a month of 2026, one employer, full time. The base is above the EUR 757.34 minimum. The relief is 0.5 x (1,300 - 1,000) = EUR 150, so the Pillar I base is EUR 850 and Pillar I is 15% of that, EUR 127.50. Pillar II is 5% of the full EUR 1,000, EUR 50. Health is 16.5% of EUR 1,000, EUR 165. The employee's contributions are EUR 177.50 against EUR 200 without the relief.

```oa-check
name: Croatia 2026, gross EUR 1,000, low-wage Pillar I relief
inputs:
  gross: 1000
steps:
  - relief: max(min(0.5 * (1300 - gross), 300), 0)
  - pillar1_base: gross - relief
  - pillar1: pillar1_base * 15 / 100
  - pillar2: gross * 5 / 100
  - employee_total: pillar1 + pillar2
  - health: gross * 16.5 / 100
expected:
  relief: 150
  pillar1_base: 850
  pillar1: 127.50
  pillar2: 50
  employee_total: 177.50
  health: 165
```

(For gross up to EUR 700 the relief is the flat EUR 300; the min() cap gives that result.)

### Example 2: sole trader (obrt) paying income tax, full year 2026

A sole trader who pays income tax on actual income, Pillar II member, no higher base chosen. The 2026 monthly base is EUR 1,295.45 (0.65 x EUR 1,993). Each month: Pillar I 15% is EUR 194.32, Pillar II 5% is EUR 64.77, health 16.5% is EUR 213.75, total EUR 472.84, paid by the 15th of the next month. Over twelve months that is EUR 5,674.08, whatever the actual profit.

```oa-check
name: Croatia 2026, obrt on actual income, monthly and annual contributions
inputs:
  average_wage: 1993
  coefficient: 0.65
  months: 12
steps:
  - base: round(average_wage * coefficient, 2)
  - pillar1: round(base * 15 / 100, 2)
  - pillar2: round(base * 5 / 100, 2)
  - health: round(base * 16.5 / 100, 2)
  - monthly_total: pillar1 + pillar2 + health
  - annual_total: monthly_total * months
expected:
  base: 1295.45
  pillar1: 194.32
  pillar2: 64.77
  health: 213.75
  monthly_total: 472.84
  annual_total: 5674.08
```

## Ask the client first

1. Is the person employed, self-employed (which activity, and income tax, profit tax or flat-rate), or both?
2. Pillar II member, or Pillar I only?
3. Monthly gross pay and the number of employers (for the low-wage relief and its split).
4. Is the worker on a vocational training contract, or did the employer start a first-job or young-person exemption before 2025?
5. Has a self-employed person chosen a higher base?
6. Is anyone posted to or from another EU state (A1 certificate)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o doprinosima, consolidated text (NN 84/08 to 152/24), Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Zakon o izmjenama i dopunama Zakona o doprinosima, NN 114/23 (art. 21.a) | https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1611.html | 2026-10-24 |
| Zakon o izmjenama Zakona o doprinosima, NN 152/24 | https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2506.html | 2026-10-23 |
| Pravilnik o doprinosima, consolidated text (to NN 16/25), Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Naredba o iznosima osnovica za obračun doprinosa za obvezna osiguranja za 2026., NN 150/25 | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html | 2026-10-23 |
| Pravilnik o porezu na dohodak, consolidated text (JOPPD, art. 77 and 79), Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Opći porezni zakon, consolidated text (to NN 151/25), Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Vlada RH, Izmjene poreznih propisa (2023): relief cuts the Pillar I base | https://vlada.gov.hr/UserDocsImages/2016/Sjednice/2023/Svibanj/220%20sjednica%20VRH/Izmjene%20poreznih%20propisa.pdf | 2026-10-24 |
| HNB, ECB main refinancing rate in force on 1 July 2026, NN 68/26 | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_06_68_826.html | 2026-10-24 |
| Zakon o obveznim odnosima, art. 29 and 1164 (NN 35/05 as amended to NN 155/23), consolidated text on zakon.hr (secondary consolidation; art. 29(9) is cited in NN 68/26) | https://www.zakon.hr/z/75/Zakon-o-obveznim-odnosima | 2026-10-24 |
| Zakon o kamatama, NN 94/04, Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-24 |

Not yet confirmed: that no amendment to the Contributions Act after NN 152/24, or to the 2026 Order after NN 150/25, applies in 2026 (the Tax Administration register lists none, and the fiskai.hr database lists no amendment to the Order; its 28 March 2026 date is a review date, not a new version); that the Obligations Act art. 29(2) rate for non-commercial relationships (5.40% from 1 July 2026) is the rate the Tax Administration charges on late tax and contributions, since no official text found ties them together (General Tax Act art. 130(1) points to a special regulation only); who must be a Pillar II member (Mandatory Pension Funds Act) was not read.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `croatia-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/croatia-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
