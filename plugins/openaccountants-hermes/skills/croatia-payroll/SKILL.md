---
name: croatia-payroll
description: "Croatian payroll for employees in tax year 2026: monthly withholding of income tax (predujam poreza na dohodak) and the contributions run with each salary. Covers the EUR 600 basic personal allowance and the dependants' allowances, the two rates set by each local unit within the legal ranges (default 20% and 30% where no decision was taken, band EUR 5,000 a month and EUR 60,000 a year), pension Pillar I 15% and Pillar II 5% (20% for Pillar I only), the 16.5% employer health contribution, the 2026 minimum and maximum bases, the low-wage pension relief, the young-worker income tax relief, the EUR 1,050 minimum wage, the JOPPD report and its deadlines, and fines. Trigger on: Croatia payroll, plaća, bruto neto, JOPPD, predujam poreza, osobni odbitak, gross to net Croatia, employer cost Croatia. Out of scope: contribution rules in depth and the self-employed (croatia-social-contributions), annual income tax (croatia-income-tax), non-residents and treaties (hr-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/croatia-payroll"
  jurisdiction: "HR"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Croatia payroll (tax year 2026) v0.2

> **Source-cited draft.** No accountant has reviewed this skill yet. Figures come from the consolidated texts in the Tax Administration (Porezna uprava) register and from Narodne novine, read on 23 and 24 October 2026. It prepares working papers; it is not authority to file or pay.

This is the payroll (PR) skill for the Croatian pack. It links rather than repeats:

- Contribution rules in depth, the self-employed (obrt) and the bases for other insured persons: [croatia-social-contributions](croatia-social-contributions.md).
- The annual income tax assessment and other income: [croatia-income-tax](croatia-income-tax.md).
- Residence, non-residents and treaties: [hr-cross-border](hr-cross-border.md).

Laws used: the Personal Income Tax Act (Zakon o porezu na dohodak, "ZPDoh", NN 115/16 as amended to NN 152/24, in force from 1 January 2025), the Personal Income Tax Rulebook (Pravilnik o porezu na dohodak, "Rulebook", as amended to NN 157/25), the Contributions Act (Zakon o doprinosima, "ZoD", NN 84/08 as amended to NN 152/24) and the Order on contribution bases for 2026 (NN 150/25). Currency: euro (EUR).

## Who this applies to

**Every employer that pays salary (plaća) in Croatia.** The employer computes, withholds and pays the income tax advance on each payment, under the rules in force on the day of payment (ZPDoh art. 24(1)). The employer also computes and pays all contributions: the employee's pension contributions out of gross pay and the employer's health contribution on top (ZoD art. 19).

**A foreign employer without a Croatian branch.** An employer seated in another EU member state whose employee falls under Croatian social security law computes and pays the contributions in the same way (ZoD art. 19.a). Its contributions fall due within 30 days of the salary payment (ZoD art. 24.a(1)).

**Who is out.** The self-employed pay their own contributions (see [croatia-social-contributions](croatia-social-contributions.md)). Other income (drugi dohodak), pensions and board members paid without an employment contract follow other rules and are not covered here.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Pension Pillar I for a Pillar II member (employee, from gross) | 15% | 2026 | ZoD art. 13(1) point 1.2, https://porezna-uprava.gov.hr/Propisi |
| Pension Pillar I, Pillar I only | 20% | 2026 | ZoD art. 13(1) point 1.1 |
| Pension Pillar II (employee, from gross) | 5% | 2026 | ZoD art. 17(1) point 1 |
| Health (employer, on gross) | 16.5% | 2026 | ZoD art. 14(1) point 1 |
| Average wage used for the bases | EUR 1,993.00 | 2026 | Order NN 150/25 art. 2, https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html |
| Minimum monthly contribution base (0.38 x average wage), full time | EUR 757.34 | 2026 | Order NN 150/25 art. 3; ZoD art. 200 |
| Maximum monthly base for pension contributions (6.0 x average wage) | EUR 11,958.00 | 2026 | Order NN 150/25 art. 4; ZoD art. 204 and 205 |
| Maximum annual base for Pillar I | EUR 143,496.00 | 2026 | Order NN 150/25 art. 5; ZoD art. 206 and 208 |
| Low-wage pension relief, gross up to EUR 700 | Pillar I base cut by EUR 300 | 2026 | ZoD art. 21.a(1), https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1611.html |
| Low-wage pension relief, gross EUR 700.01 to 1,300 | Pillar I base cut by 0.5 x (1,300 - gross) | 2026 | ZoD art. 21.a(2) |
| Basic personal allowance | EUR 600 a month | 2026 | ZPDoh art. 14(1), https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html |
| First, second, third child | EUR 300 / 420 / 600 a month | 2026 | ZPDoh art. 14(3) |
| Dependent family member | EUR 300 a month | 2026 | ZPDoh art. 14(3) |
| Invalidity / 100% invalidity | EUR 180 / 600 a month | 2026 | ZPDoh art. 14(3) |
| Monthly band for withholding | lower rate up to EUR 5,000 of monthly base, higher rate above | 2026 | ZPDoh art. 24(3) |
| Annual band | lower rate up to EUR 60,000, higher rate above | 2026 | ZPDoh art. 19 |
| Rates where the local unit took no decision | 20% and 30% | 2026 | ZPDoh art. 19.a(5) |
| Municipality (općina) range | lower 15% to 20%, higher 25% to 30% | 2026 | ZPDoh art. 19.a(2) |
| Town (grad) range | lower 15% to 21%, higher 25% to 31% | 2026 | ZPDoh art. 19.a(2) |
| Large town or county seat range | lower 15% to 22%, higher 25% to 32% | 2026 | ZPDoh art. 19.a(2) |
| City of Zagreb range / rates decided | 15% to 23% and 25% to 33% / 23% and 33% | 2026 | ZPDoh art. 19.a(2); Zagreb decision NN 28/25, https://narodne-novine.nn.hr/clanci/sluzbeni/2025_02_28_291.html |
| Young-worker relief, born 2001 or later | 100% of lower-rate tax on salary, in the annual assessment | 2026 | ZPDoh art. 46(2); Rulebook art. 58(6) |
| Young-worker relief, born 1996 to 2000 | 50% of lower-rate tax on salary, in the annual assessment | 2026 | ZPDoh art. 46(2); Rulebook art. 58(6) |
| Minimum wage, full time | EUR 1,050.00 gross a month | 2026 | Uredba NN 132/25, https://narodne-novine.nn.hr/clanci/sluzbeni/2025_10_132_1931.html |

The rates follow the local unit where the employee lives, not the employer's seat. A local decision is published in Narodne novine by the end of November and applies from 1 January of the next year until replaced (ZPDoh art. 19.a(3)). The Tax Administration posts every local decision in its register of regulations.

## The taxable base

**Step 1, contributions from gross.** Pillar I is 15% and Pillar II 5% of gross salary for a Pillar II member; a person in Pillar I only pays 20% to Pillar I (ZoD art. 13 and 17). Pension contributions stop at the maximum monthly base of EUR 11,958 (ZoD art. 204). Pillar I also stops once the year's pay from the same employer reaches EUR 143,496 (ZoD art. 206 and 207). Health has no cap.

**Low-wage relief.** Where total monthly gross pay is up to EUR 700, the Pillar I base is cut by EUR 300. From EUR 700.01 to 1,300 it is cut by 0.5 x (1,300 - gross) (ZoD art. 21.a(1) and (2)). It applies whatever the hours or days worked (art. 21.a(3)). The Government's presentation of the measure says it cuts the Pillar I base only; Pillar II stays on full gross ([Vlada, 2023 tax changes](https://vlada.gov.hr/UserDocsImages/2016/Sjednice/2023/Svibanj/220%20sjednica%20VRH/Izmjene%20poreznih%20propisa.pdf)). Pension rights are still counted on the full base (art. 21.a(7)). With two or more employers, each takes a share of the relief from the worker's statement or from Tax Administration data (art. 21.a(5); Contributions Rulebook art. 16.b). Worked figures: [croatia-social-contributions](croatia-social-contributions.md).

**Minimum base.** For full-time work the contribution base cannot be below EUR 757.34; for part-time it is pro rata to hours (ZoD art. 200).

**Step 2, income.** Income from employment is gross pay less the employee's contributions paid (ZPDoh art. 20 and 23).

**Step 3, personal allowance.** Deduct the monthly allowance on the employee's tax card: EUR 600 plus any dependants (ZPDoh art. 14 and 24(2)). A non-resident gets the basic EUR 600 for months with Croatian income (ZPDoh art. 16(1)).

**Step 4, tax.** Apply the local unit's lower rate to the monthly base up to EUR 5,000 and the higher rate above it (ZPDoh art. 24(3)). The advance is cut by 50% for residents of assisted areas in group I and of the City of Vukovar (ZPDoh art. 24(5)).

**Young workers.** The 100% and 50% reductions for those up to 25 and from 26 to 30 apply in the annual assessment, to the lower-rate tax on salary (ZPDoh art. 46(2)). For 2026: born 2001 or later, 100%; born 1996 to 2000, 50% (Rulebook art. 58(6) table). Article 24 does not apply them to the monthly advance, so payroll withholds in full and the refund comes with the annual assessment.

**Net pay** is gross less pension contributions less income tax. **Employer cost** is gross plus 16.5% health.

**First-time trainees.** For a first-time employee under a vocational training contract (ugovor o stručnom osposobljavanju), only the pension contributions are due, for up to one year; no health contribution (ZoD art. 7 point 31, art. 20(2) and (3)). The older health exemption for first permanent contracts and young persons was repealed from 1 January 2025. An employer that started using it before then keeps it (NN 152/24 art. 2 and 5, https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2506.html).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Income tax advance | Withheld and paid on each salary payment | ZPDoh art. 24(1) |
| Contributions on salary | Due with the salary payment | ZoD art. 24(1) |
| Contributions where salary is not paid | By the last day of the month for the previous month | ZoD art. 24(2) |
| Contributions on pay in kind | By the 15th of the following month | ZoD art. 24(3) |
| JOPPD report | On the day of payment, or at latest the next working day | Rulebook art. 79(1) |
| JOPPD for pay in kind | By the 15th of the following month | Rulebook art. 79(5) |
| JOPPD for non-taxable receipts reported in bulk | By the 15th of the following month | Rulebook art. 79(6) |

JOPPD (Izvješće o primicima, porezu na dohodak te doprinosima za obvezna osiguranja) is filed through ePorezna and shows, per employee, the receipt, the contributions and the tax (Rulebook art. 77). An employer that has not paid the contributions must hand the bank the contribution payment orders together with the salary payment orders; otherwise the bank refuses the salary payment, except for a contribution that is not due (ZoD art. 248.b(2) to (4)). The employer also runs the annual income tax recalculation for its employees where the law requires it (ZPDoh art. 47).

## Penalties and interest

| Breach | Fine | Source |
|---|---|---|
| Employer fails to compute, pay on time or report contributions | EUR 660 to 13,270; responsible person EUR 660 to 2,650 | ZoD art. 249 |
| Employer (legal person) does not pay or underpays the income tax advance, or does not file JOPPD on time | EUR 1,320 to 6,630; responsible person EUR 260 to 1,320 | ZPDoh art. 91(1) points 1 and 5, 91(4) |
| Same, by a sole trader or other self-employed employer | EUR 660 to 3,980 | ZPDoh art. 91(2) |

Late payment interest runs on tax and contributions from the due date (General Tax Act art. 130(3)). The General Tax Act leaves the interest rate to a special regulation (art. 130(1)). The Obligations Act sets the default interest rate in relationships other than commercial contracts at the ECB reference rate plus three percentage points, fixed each half year (Zakon o obveznim odnosima art. 29(2) and (8)). The Croatian National Bank published a reference rate of 2.40% in force on 1 July 2026 (NN 68/26, https://narodne-novine.nn.hr/clanci/sluzbeni/2026_06_68_826.html), which gives 5.40% a year from 1 July to 31 December 2026. Whether that rate is the one charged on tax and contribution debts is not yet confirmed in an official text: the Interest Act provision that brought taxes and contributions under the general default rate (Zakon o kamatama art. 1(2)) ceased to apply from 2008 (Obligations Act art. 1164(2)).

## Cross-border points

- **Which country's contributions.** Within the EU, social security follows Regulation 883/2004; an A1 certificate keeps a posted worker in the home system. A foreign EU employer of someone insured in Croatia pays Croatian contributions under ZoD art. 19.a, due 30 days after payment (art. 24.a).
- **Non-resident employees.** Croatian-source salary is taxed by withholding. The non-resident gets the basic allowance for months with Croatian income. An EU/EEA resident who earns at least 90% of world income in Croatia can claim the family allowances in the annual assessment (ZPDoh art. 16).
- **Residence, treaties and the 183-day rules:** [hr-cross-border](hr-cross-border.md).

## Worked examples

### Example 1: employee in a municipality with no rate decision, gross EUR 2,000

A resident employee, Pillar II member, no dependants, gross EUR 2,000 for a month in 2026. The municipality took no rate decision, so 20% and 30% apply. Gross is above EUR 1,300, so no low-wage relief. Pillar I is 15% (EUR 300) and Pillar II 5% (EUR 100). Income is EUR 1,600. Less the EUR 600 allowance, the tax base is EUR 1,000, inside the EUR 5,000 band, so tax is 20%: EUR 200. Net pay is EUR 1,400. The employer adds 16.5% health, EUR 330, for a total cost of EUR 2,330.

```oa-check
name: Croatia 2026, gross EUR 2,000, default 20% rate, no dependants
inputs:
  gross: 2000
  allowance: 600
  lower_rate: 20
steps:
  - pillar1: gross * 15 / 100
  - pillar2: gross * 5 / 100
  - income: gross - pillar1 - pillar2
  - tax_base: max(income - allowance, 0)
  - tax: round(min(tax_base, 5000) * lower_rate / 100, 2)
  - net: income - tax
  - health: gross * 16.5 / 100
  - employer_cost: gross + health
expected:
  pillar1: 300
  pillar2: 100
  income: 1600
  tax_base: 1000
  tax: 200
  net: 1400
  health: 330
  employer_cost: 2330
```

### Example 2: Zagreb employee above the pension cap and the monthly band, one child

A resident employee in Zagreb (23% and 33%), Pillar II member, one dependent child, gross EUR 13,000 for a month in 2026. Pension contributions stop at the EUR 11,958 maximum monthly base: Pillar I EUR 1,793.70 and Pillar II EUR 597.90. Income is EUR 10,608.40. The allowance is EUR 600 plus EUR 300 for the first child, EUR 900, so the tax base is EUR 9,708.40. Tax is 23% on EUR 5,000 (EUR 1,150) plus 33% on EUR 4,708.40 (EUR 1,553.77), so EUR 2,703.77. Net pay is EUR 7,904.63. Health has no cap: 16.5% of EUR 13,000 is EUR 2,145, so the employer cost is EUR 15,145.

```oa-check
name: Croatia 2026, Zagreb, gross EUR 13,000, pension cap and higher band, one child
inputs:
  gross: 13000
  max_base: 11958
  allowance: 900
  lower_rate: 23
  higher_rate: 33
steps:
  - pension_base: min(gross, max_base)
  - pillar1: round(pension_base * 15 / 100, 2)
  - pillar2: round(pension_base * 5 / 100, 2)
  - income: gross - pillar1 - pillar2
  - tax_base: max(income - allowance, 0)
  - tax_lower: round(min(tax_base, 5000) * lower_rate / 100, 2)
  - tax_higher: round(max(tax_base - 5000, 0) * higher_rate / 100, 2)
  - tax: tax_lower + tax_higher
  - net: income - tax
  - health: gross * 16.5 / 100
  - employer_cost: gross + health
expected:
  pillar1: 1793.70
  pillar2: 597.90
  income: 10608.40
  tax_base: 9708.40
  tax: 2703.77
  net: 7904.63
  health: 2145
  employer_cost: 15145
```

## Ask the client first

1. Where does each employee live (town or municipality)? That sets the two rates.
2. Is the employee a Pillar II member, or in Pillar I only?
3. Which dependants are on the tax card (children, family members, invalidity)?
4. Year of birth, for the young-worker relief in the annual assessment.
5. Does the employee have another employer this month (for the low-wage relief split)?
6. Is anyone posted from abroad, a non-resident, on a training contract, or on a pre-2025 first-job exemption?

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o porezu na dohodak, consolidated text (NN 115/16 to 152/24), Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Zakon o izmjenama i dopunama Zakona o porezu na dohodak, NN 152/24 | https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html | 2026-10-23 |
| Pravilnik o porezu na dohodak, consolidated text (to NN 157/25), Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Zakon o doprinosima, consolidated text (NN 84/08 to 152/24), Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Zakon o izmjenama i dopunama Zakona o doprinosima, NN 114/23 (art. 21.a) | https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1611.html | 2026-10-24 |
| Zakon o izmjenama Zakona o doprinosima, NN 152/24 | https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2506.html | 2026-10-23 |
| Naredba o iznosima osnovica za obračun doprinosa za 2026., NN 150/25 | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html | 2026-10-23 |
| Uredba o visini minimalne plaće za 2026., NN 132/25 | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_10_132_1931.html | 2026-10-24 |
| Odluka o visini poreznih stopa godišnjeg poreza na dohodak Grada Zagreba, NN 28/25 (applies from 1 March 2025) | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_02_28_291.html | 2026-10-24 |
| Vlada RH, Izmjene poreznih propisa (2023): low-wage relief on the Pillar I base | https://vlada.gov.hr/UserDocsImages/2016/Sjednice/2023/Svibanj/220%20sjednica%20VRH/Izmjene%20poreznih%20propisa.pdf | 2026-10-24 |
| HNB, ECB main refinancing rate in force on 1 July 2026, NN 68/26 | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_06_68_826.html | 2026-10-24 |
| Zakon o obveznim odnosima, art. 29 and 1164 (NN 35/05 as amended to NN 155/23), consolidated text on zakon.hr (secondary consolidation; art. 29(9) is cited in NN 68/26) | https://www.zakon.hr/z/75/Zakon-o-obveznim-odnosima | 2026-10-24 |
| Zakon o kamatama, NN 94/04, Tax Administration register | https://porezna-uprava.gov.hr/Propisi | 2026-10-24 |

Not yet confirmed: that no amendment to the Personal Income Tax Act or the Contributions Act after NN 152/24 applies in 2026 (the Tax Administration register lists none); that the City of Zagreb has not replaced its NN 28/25 decision for 2026; that the Obligations Act art. 29(2) rate for non-commercial relationships (5.40% from 1 July 2026) is the rate the Tax Administration charges on late tax and contributions, since no official text found ties them together (General Tax Act art. 130(1) points to a special regulation only); who must be a Pillar II member (Mandatory Pension Funds Act) was not read.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `croatia-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/croatia-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
