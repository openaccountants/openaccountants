---
name: bosnia-payroll
description: "Bosnia and Herzegovina payroll for employers, tax year 2026, worked separately for the Federation of BiH (FBiH), Republika Srpska (RS) and Brčko District. Covers the monthly gross-to-net: FBiH employee contributions 31% and employer contributions 5% on gross, 10% income tax after contributions and the 300 KM tax-card allowance, the 2026 FBiH minimum wage (1,027 KM net) and the minimum contribution base; RS 31% contributions withheld from gross, 8% tax on gross less the 1,000 KM allowance, the 2026 50 KM tax-free part and seasonal-work daily amounts; Brčko 10% tax with a 1,200 KM allowance. Also tax-free allowances, forms (MIP-1023, Form 1002), payment days and fines. Trigger on: obračun plaće, bruto u neto, porezna kartica, MIP-1023, Obrazac 1002, najniža plaća, doprinosi iz plaće, Bosnia payroll. Out of scope: contributions for the self-employed (bosnia-social-contributions), annual income tax (bosnia-income-tax)."
version: 0.2
jurisdiction: BA
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bosnia and Herzegovina: payroll (2026)

> **Not reviewed by an accountant.** Figures come from the FBiH, RS and Brčko income tax and contribution laws and their 2026 implementing texts, read on the official sites of the FBiH Tax Administration (pufbih.ba), the FBiH Ministry of Finance and Government, the RS Tax Administration (poreskaupravars.org) and the Brčko District Assembly (skupstinabd.ba) on 30 October 2026. It prepares working papers; it is not authority to file or pay.

This skill covers what an employer does each time it pays a salary in 2026: work out contributions and income tax, report, and pay. Payroll is run under the law of the place where the employer has its seat (or its business unit). There is no state-level payroll system; VAT is the only state tax and has nothing to do with payroll.

Related skills: annual personal income tax and the rules on residence and other income in [bosnia-income-tax](bosnia-income-tax.md); contribution rates and bases for everyone, including the self-employed, in [bosnia-social-contributions](bosnia-social-contributions.md); [ba-tax-overview](ba-tax-overview.md).

## Who this applies to

- **FBiH employers.** A legal or natural person resident in the Federation pays salary and is the payer of contributions on the salary and the withholder of contributions from it and of income tax (Contributions Law arts. 5 and 11; Income Tax Law art. 28). The employee is the taxpayer (Income Tax Law art. 27(2)). A person domiciled in RS or Brčko who works for an FBiH employer is taxed in the Federation on that salary (Income Tax Law art. 2(4)).
- **RS employers.** The payer withholds tax at the moment of payment (Income Tax Law art. 61(1)) and contributions are paid by deduction from the base at each payment (Contributions Law art. 24(1) and (3)).
- **Brčko District employers.** The employer withholds the tax advance at each payment (Income Tax Law art. 28). An employee domiciled in an entity who works for a District employer is a District resident for that salary (art. 3(1)(e)).
- **Foreign employers.** An FBiH resident working in the Federation for a non-resident employer pays contributions himself by the 10th of the next month, or the foreign employer can do it (Contributions Law art. 11(1)(b) and (c)); an employee paid directly from abroad self-assesses the tax advance within five days (Income Tax Law art. 27(10)).

Out of scope: labour-law rules on pay rates, overtime and leave beyond the 2026 FBiH minimum wage.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| FBiH employee contributions (withheld) | pension 17% + health 12.5% + unemployment 1.5% = 31% of gross | 2026 | [FBiH Contributions Law art. 10(1)](https://www.pufbih.ba/v1/public/upload/zakoni/2dcc6-zakon-o-doprinosima-precisceni-tekst-25.pdf) |
| FBiH employer contributions (on top) | pension 2.5% + health 2% + unemployment 0.5% = 5% of gross | salaries for July 2025 onward | [FBiH Contributions Law art. 10(2) as amended by 33/25](https://www.fmf.gov.ba/Content/Open/102560?n=Zakona_o_izmjenama_i_dopunama_Zakona_o_doprinosima.doc); [Rulebook art. 40b](https://www.pufbih.ba/v1/public/upload/zakoni/7cfcb-pravilnik-o-nacinu-obracunavanja-i-uplate-doprinosa-precisceni-48-25.pdf) |
| FBiH additional pension contribution, jobs with extended service credit | 2%, 3% or 6% of gross | 2026 | FBiH Contributions Law art. 10(3) |
| FBiH income tax | 10% | 2026 | [FBiH Income Tax Law art. 9](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf) |
| FBiH monthly allowance by tax card | 300 KM basic; +150 spouse, +150 first child, +210 second child, +270 each further child, +90 other dependant, +90 disability | 2026 | [FBiH Rulebook art. 21(6)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| FBiH minimum wage | 1,027 KM net a month | 1 Jan to 31 Dec 2026 | [FBiH Government decision 1094, 30 Dec 2025](https://fbihvlada.gov.ba/bs/1094-odluka-o-iznosu-najnize-place-za-2026-godinu) |
| FBiH minimum contribution base | the minimum wage converted to gross with the employee's own allowance; 50% of it for part-time of 4 hours a day or less | 2026 | FBiH Contributions Law art. 7(1) and (2); Rulebook art. 20 |
| FBiH meal allowance not taxed | up to 1% of the latest average net salary in the Federation | 2026 | FBiH Rulebook art. 20(7) |
| FBiH holiday pay (regres) not taxed | up to 50% of the average net salary in the Federation for the last three months | 2026 | FBiH Rulebook art. 20(12) |
| FBiH gifts not taxed | up to 30% of the average monthly salary, total for the year | 2026 | FBiH Income Tax Law art. 10(4)(5); Rulebook art. 20(20) |
| FBiH dismissal severance not taxed | up to 70% of the employee's average monthly salary for the last three months, per year of service | 2026 | FBiH Rulebook art. 20(14) |
| FBiH retirement severance not taxed | six net salaries of the employee, or six average net salaries in the Federation if higher | 2026 | FBiH Rulebook art. 20(13) |
| FBiH own car for commuting | 15% of the price of a litre of petrol per km (0.30 KM per km for electric and hybrid cars), capped at 1.5 monthly public transport tickets | 2026 | FBiH Rulebook art. 20(6) |
| RS contributions (all withheld from gross) | pension 18.5% + health 10.2% + unemployment 0.6% + child protection 1.7% = 31% | 2026 | [RS Contributions Law art. 22(1)](https://www.poreskaupravars.org/dokumenti/zakoni/Zakon-o-doprinosima-SLGL-114_17.pdf) as amended by [112/19](https://www.poreskaupravars.org/dokumenti/zakoni/Zakon-o-izmjenama-Zakona-o-doprinosima-SLGL-112_19.pdf) and [119/21](https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20doprinosima.pdf) |
| RS income tax on salary | 8% of gross less allowances (contributions not deducted) | 2026 | [RS Tax Administration notice, February 2026](https://poreskaupravars.org/izmjene-u-podnosenju-obrasca-1002-od-01-01-2026-godine-3/); RS Income Tax Law art. 13 |
| RS monthly allowance by tax card | 1,000 KM (1/12 of 12,000); +150 KM a month per dependant (1/12 of 1,800) | 2026 | RS Income Tax Law arts. 10(3) and 58(2) |
| RS tax-free part of salary, jobs needing no qualification or at most 3-year secondary school | 50 KM a month, out of both the tax base and the contribution base | from 1 Jan 2026 | [RS Income Tax Law art. 8(2)(13), by 114/25](https://poreskaupravars.org/wp-content/uploads/2025/12/Dohodak.pdf); Contributions Law art. 21(1) |
| RS minimum contribution base | the minimum gross wage in force in the month | 2026 | [RS Contributions Law art. 10a, by 49/21](https://poreskaupravars.org/wp-content/uploads/2021/06/Zakon-o-doprinosima-2.pdf) |
| RS canteen or catered meals not taxed | up to 0.75% of the previous year's average net salary a day (2025 average net: 1,528 KM) | 2026 | RS Income Tax Law art. 8(2)(11) as amended by 56/22; [RS Statistics Institute](https://www.rzs.rs.ba/) |
| RS employer payments into the European voluntary pension fund (EDPF) | not taxed up to 100 KM, reported as payment type 113 on the monthly Form 1002 | 2026 | [RS Tax Administration notice, March 2026](https://poreskaupravars.org/prijavljivanje-uplata-u-dobrovoljni-penzijski-fond-i-neoporezivog-dijela-plate-u-okviru-obrasca-1002/) |
| RS seasonal and temporary work | tax 9 KM and contributions 16 KM for each day of engagement, paid by the 20th of the next month | from 1 Jan 2026 | RS Income Tax Law art. 52a and Contributions Law arts. 16b and 24(5), by 114/25 |
| Brčko income tax | 10% after employee contributions and the allowance | 2026 | [BD Income Tax Law arts. 10, 12, 28](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf) |
| Brčko monthly allowance | 1,200 KM | from 1 Aug 2022 | BD Income Tax Law art. 25(1) as amended by 21/22 |
| Brčko meal allowance not taxed | up to 10 KM per working day | from 1 Jan 2023 | BD Income Tax Law art. 11(2)(c)(6) as amended by 45/22 |
| Late payment interest | FBiH 0.04% a day; RS 0.03% a day; Brčko 0.03% a day | 2026 | [FBiH interest law art. 2](https://pufbih.ba/v1/public/upload/zakoni/1%20Zakon%20o%20visini%20stope%20zatezne%20kamate%20na%20javne%20prihode%20-%20PRECISCEN%20TEKST.pdf); [RS ZPP art. 60](https://poreskaupravars.org/wp-content/uploads/2026/05/Zakon-o-poreskom-postupku-78-20.pdf); BD ZPU art. 68 |

## The taxable base

### FBiH gross to net

1. **Contribution base** = gross salary (all pay in cash or kind that is taxable as salary). It is not less than the minimum gross wage (Contributions Law art. 7(1)). To find the minimum gross for an employee, the employer grosses up the 1,027 KM net minimum using that employee's own tax-card allowance (Contributions Rulebook art. 20). For a part-time employee working 4 hours a day or less, the base is the pro-rata salary but not less than 50% of the minimum wage (art. 7(2)).
2. **Employee contributions** = base × 31%, withheld.
3. **Tax base** = gross − employee contributions − monthly allowance from the tax card (Income Tax Law arts. 11 and 27(3)). Without a tax card, no allowance (art. 27(4)). At most 12 monthly allowances a year (Rulebook art. 21(4)).
4. **Income tax** = tax base × 10%, not below zero.
5. **Net pay** = gross − employee contributions − income tax.
6. **Employer contributions** = base × 5%, on top (from salaries for July 2025).

Benefits within the rulebook limits (travel and field allowances under the government travel decree, commuting, meals, holiday pay, gifts, severance, aid for serious illness or disability up to three average salaries, funeral costs up to four average salaries) are neither taxed nor subject to contributions (Income Tax Law art. 10(4); Rulebook art. 20; Contributions Law art. 9(2)). Amounts above the limit are salary (Rulebook art. 20(21)).

### RS gross to net

1. **Contribution base** = gross personal income less the 50 KM tax-free part where it applies, not less than the minimum gross wage (Contributions Law arts. 10, 10a, 21(1)).
2. **Contributions** = base × 31%, deducted from gross. There is no further charge on top of gross.
3. **Tax base** = gross − tax-free part − 1,000 KM allowance − 150 KM per dependant on the tax card. Contributions are not deducted (Income Tax Law art. 13 as amended by 119/21).
4. **Income tax** = tax base × 8%.
5. **Net pay** = gross − contributions − income tax.

The RS Tax Administration's own 2026 example: gross 1,800 KM, tax-free part 50 KM, base 1,750 KM, contributions 542.50 KM, tax base 750 KM, tax 60 KM, net 1,197.50 KM (Example 2 below). The 50 KM part applies only to workers registered for jobs needing no qualification or a qualification up to a 3-year secondary school (NK, PK, KV and lower), whatever their pay. For posted workers (insurance code 56) and low-qualified workers in textiles, clothing and leather, contributions are paid on the minimum wage (art. 16a) or on 25% of the previous year's average gross salary (art. 16), so the 50 KM changes only the tax base.

### Brčko gross to net

Tax base = gross − employee contributions − 1,200 KM allowance (more for dependants and disability, see bosnia-income-tax), at 10% (Income Tax Law arts. 12, 25, 28). The contribution rates for Brčko employees are not covered here (see Not yet confirmed).

## Deadlines and filing

| What | FBiH | RS | Brčko |
|---|---|---|---|
| Contributions paid | with the salary (Contributions Law art. 11(4)) | at each payment, by deduction (Contributions Law art. 24(1) and (3)) | |
| Income tax paid | same day as the salary or the first day after (Income Tax Law art. 27(1)) | at the moment of payment (Income Tax Law art. 61(1)) | same day or the first day after (art. 28(2)) |
| Report with each payment | specification of contributions, tax and pay, same day or the next day (Contributions Law art. 11a) | | |
| Monthly report | MIP-1023, with PMIP-1024 per employee, by the 15th for the previous month (Income Tax Law art. 28(2); Rulebook) | Form 1002 (monthly withholding return) by the 10th for the previous month (Income Tax Law art. 61(4)); contributions reported on the same form by the end of the month for the previous month (Contributions Law art. 23(1)) | monthly return (Income Tax Law art. 38a) |
| Salary not paid on time | contributions calculated on the unpaid salary by the last day of the month it fell due, and paid by that day (Contributions Law art. 11(5) and (6)) | contribution liability arises two months after the end of the month (Contributions Law art. 24(2)) | |
| Annual data | to each employee and the Tax Administration by the end of January (Contributions Law art. 11); employee certificate by the end of February (Income Tax Law art. 28(3)) | certificate at each payment and after year-end (Income Tax Law art. 61(2)) | |

Each employee hands the employer a tax card (FBiH PK-1002, RS poreska kartica) when they start; only the employer holding the card gives the allowance (FBiH Income Tax Law art. 28(1); RS art. 62).

## Penalties and interest

**FBiH.**

- Employer does not calculate contributions with the salary, or by the last day of the month the salary fell due, or calculates them on a base below the minimum: 2,000 to 10,000 KM; responsible person 500 to 2,000 KM (Contributions Law art. 15).
- Employer does not pay contributions with the salary, or does not file the payment specification on time: 1,000 to 5,000 KM (Contributions Law art. 16). A repeat offence can also bring a ban on the activity for up to a year (art. 17a).
- Withholding return not filed: 200 KM per failure, up to 50,000 KM (Tax Administration Law art. 87).
- Late payment interest 0.04% a day (interest law art. 2; Contributions Law art. 13).

**RS.**

- Payer does not withhold and pay tax: fine equal to the tax not withheld; responsible person 1,000 to 3,000 KM (Income Tax Law art. 70b). Payer does not pass on the allowance benefit to the employee: 3,000 to 9,000 KM for a legal person, 1,500 to 4,500 KM for a natural person (art. 70a).
- Return not filed or late: legal person 2,000 to 6,000 KM; entrepreneur 1,000 to 3,000 KM (Tax Procedure Law art. 112).
- Employee not registered in the single contributions system: legal person 10,000 to 30,000 KM; natural person and responsible person 3,000 to 9,000 KM (Tax Procedure Law art. 114).
- Late payment interest 0.03% a day (Tax Procedure Law art. 60).

**Brčko.** Return not filed: legal person 1,000 to 5,000 KM, entrepreneur 200 to 1,000 KM (Tax Administration Law art. 76). Interest 0.03% a day, capped at the debt (art. 68).

## Cross-border points

- **Between entities.** The FBiH and Brčko laws tax an employee by the employer's seat (FBiH art. 2(4); BD art. 3(1)(e)). An RS employer pays contributions according to its seat in RS; an employer from the other entity or Brčko pays through its RS business unit (RS Contributions Law art. 26).
- **Posted abroad (FBiH).** For an employee sent abroad by an FBiH employer, or employed abroad by a foreign employer, the contribution base is the pay for the same job in the Federation and not less than the average monthly salary in the Federation (Contributions Law art. 7(3)). The FBiH average for setting 2026 bases is 2,464 KM (January to September 2025).
- **Non-resident employees** working in the Federation for a resident employer pay FBiH contributions (Contributions Law art. 5). Social security agreements can change this; check the agreement before excluding anyone.
- **Payments to foreign individuals for occasional services** are not payroll; see bosnia-income-tax (FBiH art. 30; RS art. 61a, 10% final).

## Worked examples

### Example 1: FBiH employee, gross 2,000 KM, basic tax card (2026)

An employee in Mostar earns gross 2,000 KM a month and has a tax card with factor 1.0.

- Employee contributions: 2,000 × 31% = 620 KM.
- Tax base: 2,000 − 620 − 300 = 1,080 KM. Tax at 10%: 108 KM.
- Net pay: 2,000 − 620 − 108 = 1,272 KM.
- Employer contributions: 2,000 × 5% = 100 KM. Employer cost: 2,100 KM.

The employer pays the 620 KM, 100 KM and 108 KM with the salary, files the payment specification the same or next day and includes the employee on MIP-1023 by the 15th of the next month.

```oa-check
name: FBiH gross 2000 KM, factor 1.0 (2026)
inputs:
  gross: 2000
  employee_rate: 0.31
  employer_rate: 0.05
  allowance: 300
steps:
  - employee_contributions: gross * employee_rate
  - tax_base: max(gross - employee_contributions - allowance, 0)
  - tax: tax_base * 0.10
  - net: gross - employee_contributions - tax
  - employer_contributions: gross * employer_rate
  - employer_cost: gross + employer_contributions
expected:
  employee_contributions: 620.00
  tax: 108.00
  net: 1272.00
  employer_cost: 2100.00
```

### Example 2: RS worker with the 50 KM tax-free part, gross 1,800 KM (2026)

This is the RS Tax Administration's own example. A worker in a job requiring 3-year secondary school earns gross 1,800 KM a month; the tax card gives the basic allowance only.

- Contribution base: 1,800 − 50 = 1,750 KM. Contributions at 31%: 542.50 KM.
- Tax base: 1,750 − 1,000 = 750 KM. Tax at 8%: 60 KM.
- Net pay: 1,800 − 542.50 − 60 = 1,197.50 KM.

On Form 1002 the 1,800 KM goes in DL1 column 6 and the 50 KM in DL6 with payment type 60.

```oa-check
name: RS gross 1800 KM with 50 KM tax-free part (2026)
inputs:
  gross: 1800
  tax_free: 50
  contribution_rate: 0.31
  allowance: 1000
steps:
  - base: gross - tax_free
  - contributions: base * contribution_rate
  - tax_base: max(base - allowance, 0)
  - tax: tax_base * 0.08
  - net: gross - contributions - tax
expected:
  contributions: 542.50
  tax_base: 750.00
  tax: 60.00
  net: 1197.50
```

## Ask the client first

1. Where is the employer's seat or business unit, and where does the employee work and live (FBiH, RS or Brčko)?
2. Is the gross salary agreed, or a net figure that has to be grossed up?
3. Has the employee given you a tax card, and with which dependants?
4. Full-time or part-time, and what job qualification is the employee registered with (RS 50 KM part)?
5. Which allowances do you pay (meals, travel, commuting, holiday pay, gifts, severance), and how much?
6. Any employee sent abroad, working for you from abroad, or paid by a foreign employer?

## Sources

| Source | URL | Read on |
|---|---|---|
| FBiH Zakon o doprinosima (consolidated to 33/25), arts. 5 to 17a | https://www.pufbih.ba/v1/public/upload/zakoni/2dcc6-zakon-o-doprinosima-precisceni-tekst-25.pdf | 2026-10-30 |
| FBiH Zakon o izmjenama i dopunama Zakona o doprinosima 33/25 (applies from 1 July 2025) | https://www.fmf.gov.ba/Content/Open/102560?n=Zakona_o_izmjenama_i_dopunama_Zakona_o_doprinosima.doc | 2026-10-30 |
| FBiH Pravilnik o načinu obračunavanja i uplate doprinosa (consolidated to 48/25), arts. 2, 20, 40b | https://www.pufbih.ba/v1/public/upload/zakoni/7cfcb-pravilnik-o-nacinu-obracunavanja-i-uplate-doprinosa-precisceni-48-25.pdf | 2026-10-30 |
| FBiH Zakon o porezu na dohodak (consolidated to 65/13), arts. 2, 9 to 11, 27, 28 | https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf | 2026-10-30 |
| FBiH Pravilnik o primjeni Zakona o porezu na dohodak (consolidated to 12/26), arts. 20 and 21 | https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf | 2026-10-30 |
| FBiH Government, Odluka o iznosu najniže plaće za 2026. godinu | https://fbihvlada.gov.ba/bs/1094-odluka-o-iznosu-najnize-place-za-2026-godinu | 2026-10-30 |
| FBiH Ministry of Finance, Osnovice za obračun doprinosa 2026 (Sl. novine 100/25) | https://www.fmf.gov.ba/Content/Open/102838?n=Osnovice_za_obra%C4%8Dun_doprinosa_odre%C4%91enih_obveznika_za_2026._godinu.docx | 2026-10-30 |
| FBiH Zakon o Poreznoj upravi (consolidated to 44/22), art. 87; interest law art. 2 | https://www.pufbih.ba/v1/public/upload/zakoni/a0e37-zakon-o-poreznoj-upravi-fbih-preciscen-tekst-novi-22.pdf | 2026-10-30 |
| RS Zakon o doprinosima 114/17, arts. 10, 21 to 26 | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon-o-doprinosima-SLGL-114_17.pdf | 2026-10-30 |
| RS amendments to the Contributions Law 112/19, 49/21, 119/21, 114/25 | https://poreskaupravars.org/pravna-lica/propisi-o-doprinosima/ | 2026-10-30 |
| RS Zakon o porezu na dohodak 60/15 and amendments 66/18, 119/21, 56/22, 114/25 | https://poreskaupravars.org/pravna-lica/propisi-o-porezu-na-dohodak/ | 2026-10-30 |
| RS Tax Administration, Form 1002 from 1 January 2026 (worked example) | https://poreskaupravars.org/izmjene-u-podnosenju-obrasca-1002-od-01-01-2026-godine-3/ | 2026-10-30 |
| RS Tax Administration, voluntary pension and the 50 KM part on Form 1002 | https://poreskaupravars.org/prijavljivanje-uplata-u-dobrovoljni-penzijski-fond-i-neoporezivog-dijela-plate-u-okviru-obrasca-1002/ | 2026-10-30 |
| RS Zakon o poreskom postupku 78/20, arts. 60, 112, 114 | https://poreskaupravars.org/wp-content/uploads/2026/05/Zakon-o-poreskom-postupku-78-20.pdf | 2026-10-30 |
| RS Statistics Institute, average salaries 2025 | https://www.rzs.rs.ba/ | 2026-10-30 |
| Brčko Zakon o porezu na dohodak (consolidated) and amendments 21/22, 45/22 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf | 2026-10-30 |
| Brčko Zakon o Poreznoj upravi 11/20, arts. 68 and 76 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20Poreznoj%20upravi%20Brc--ko%20Distrikta%20BiH/011B11-20%20Zakon%20%20o%20poreznoj%20upravi%20Brcko%20distrikta%20BiH.pdf | 2026-10-30 |

Not yet confirmed: the RS minimum wage for 2026 (the RS Government decision was not reached); the Brčko contribution rates and base limits (set partly by the District Assembly and the entity pension funds the employee belongs to); the FBiH employer levies charged on net pay under other laws (fees for protection from natural disasters and water fees, shown as 0.5% each in the old version); whether the 0.75% RS meal limit uses the 2025 average net of 1,528 KM as published in the RS gazette; the RS 2026 rulebook on seasonal-work returns; any FBiH Income Tax Law amendment after 65/13 (none on the Tax Administration's list of 12 October 2026).

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
