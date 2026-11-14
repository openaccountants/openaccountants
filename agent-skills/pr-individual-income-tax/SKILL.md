---
name: pr-individual-income-tax
description: "Compute Puerto Rico individual income tax for tax year 2026 under the Puerto Rico Internal Revenue Code of 2011, as revised 28 May 2026. Covers who must file the individual return (planilla de individuos, Formulario 482 for the 2025 informative copy), the regular brackets after the personal and dependent exemptions, the 95 percent and 92 percent reductions, the gradual adjustment above USD 500,000, the optional tax on self-employment gross income, filing and payment on 15 April with a six-month filing extension, estimated tax, and the nonresident-alien withholding rates. Does not compute the alternate basic tax base, Act 60 decree income, corporate tax, or federal self-employment tax. Trigger on \"Puerto Rico income tax\", \"planilla de individuos\", \"Form 482\", \"contribucion sobre ingresos individuo\", \"Hacienda individual tax\", \"optional tax Puerto Rico\", \"gradual adjustment\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pr-individual-income-tax"
  jurisdiction: "PR"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Puerto Rico individual income tax, tax year 2026

> **Source-cited draft.** Built from the Puerto Rico Internal Revenue Code of 2011, legislative-library revision of 28 May 2026, and the Hacienda page for the 2025 informative Formulario 482, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For a tax year beginning after 31 December 2019, regular tax is the section 1021.01(a)(3) table (0 percent through USD 9,000, then 7, 14, 25 and 33 percent) applied to net income after the section 1033.18 exemptions, plus the gradual adjustment, then multiplied by **92 percent** when gross income is not over **USD 100,000**, or by **95 percent** when gross income is over that amount. A person whose only income is wages on a withholding statement or a pension described in section 1021.02(a)(2)(F) is not subject to the alternate basic tax. The calendar-year return and the tax are due **15 April** of the following year. A filing extension does not extend payment.

## Scope and who this is for

In scope: the Puerto Rico income tax of an individual for a tax year beginning in 2026. That is a resident individual, a United States citizen who is not a resident for all or part of the year, and a nonresident alien, on the income the Code taxes in each case. The result is the regular tax under section 1021.01, or the optional tax under section 1021.06 when the client qualifies and chooses it.

A resident individual is a person domiciled in Puerto Rico. Presence in Puerto Rico for 183 days in the calendar year raises a presumption of residence. The Secretary sets the other domicile factors by regulation. [Section 1010.01(a)(30)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Regular corporate income tax | `pr-company-income-tax` |
| Federal bona fide residence, the section 933 exclusion, and which federal return is required | `pr-federal-residence-and-filing` |
| Federal self-employment tax | `pr-self-employment-tax` |
| Act 60 resident-investor and export-services decrees | outside this skill |
| The alternate basic tax computation in section 1021.02 | not computed here; see When to refuse or refer |

## Ask the client first

1. **Residence for the year:** domiciled in Puerto Rico, a United States citizen who was not a resident for all or part of the year, or a nonresident alien. Days present in Puerto Rico, and whether the person was engaged in a trade or business in Puerto Rico.
2. **Filing status:** single, or married and living together. If married, joint or separate, and whether they want the optional split in section 1021.03.
3. **Income by type:** wages on a Comprobante de Retencion, pensions, and self-employment or business income. Any amount covered by an exemption decree.
4. **Exemptions:** veteran status, and each dependent's age, relationship, support, student status, and the dependent's own gross income.
5. **Self-employment, if any:** whether at least 80 percent of gross income is from services subject to withholding under section 1062.03, whether that withholding or estimated tax was satisfied, and the ordinary expenses.
6. **Payments already made:** withholding and estimated-tax payments. Estimated tax is required when the estimated tax is over USD 1,000 and the wage-only exceptions in section 1061.20 do not apply.

## The method, step by step

### Rates, bands and thresholds

The table in section 1021.01(a)(3) is the regular tax for every tax year beginning after 31 December 2012, including 2026. It applies to net income after the exemptions in section 1033.18. Those exemptions are deductions in arriving at net income, so they are subtracted once. [Sections 1021.01 and 1033.18](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

| Item | Amount, tax year 2026 | Who it applies to | Source |
| --- | --- | --- | --- |
| Regular tax, net income not over USD 9,000 | 0 percent | Tax years beginning after 31 December 2012, before the 95 or 92 percent factor | [Section 1021.01(a)(3)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Regular tax, over USD 9,000 and not over USD 25,000 | 7 percent of the excess over USD 9,000 | Same years, before the 95 or 92 percent factor | [Section 1021.01(a)(3)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Regular tax, over USD 25,000 and not over USD 41,500 | USD 1,120 plus 14 percent of the excess over USD 25,000 | Same years, before the 95 or 92 percent factor | [Section 1021.01(a)(3)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Regular tax, over USD 41,500 and not over USD 61,500 | USD 3,430 plus 25 percent of the excess over USD 41,500 | Same years, before the 95 or 92 percent factor | [Section 1021.01(a)(3)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Regular tax, over USD 61,500 | USD 8,430 plus 33 percent of the excess over USD 61,500 | Same years, before the 95 or 92 percent factor | [Section 1021.01(a)(3)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Gradual adjustment | 5 percent of net income subject to tax over USD 500,000 | Tax years beginning after 31 December 2013. Added to the table tax before the 95 or 92 percent factor | [Section 1021.01(b)(4)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Cap on the gradual adjustment | USD 8,895 plus 33 percent of the allowable personal and dependent exemptions | Tax years beginning after 31 December 2014 | [Section 1021.01(b)(5)(E)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Reduction of the section 1021.01 tax | 95 percent of the table tax plus the gradual adjustment | Tax years beginning after 31 December 2018, when gross income is over USD 100,000 | [Section 1021.01(c)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Further reduction of the section 1021.01 tax | 92 percent of the table tax plus the gradual adjustment | Tax years beginning after 31 December 2019, and only when gross income is not over USD 100,000 | [Section 1021.01(c)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Personal exemption, individual | USD 3,500 | One individual. A deduction in computing net income | [Section 1033.18(a)(1)(A)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Personal exemption, married filing jointly | USD 7,000 | Married, living together, joint return | [Section 1033.18(a)(1)(B)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Additional personal exemption, veteran | USD 1,500 (USD 3,000 if both spouses are veterans on a joint return) | On income other than the military pension. Military pension of a qualifying veteran resident is fully exempt | [Section 1033.18(a)(2) and (a)(3)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Dependent exemption | USD 2,500 each | A dependent who received more than half of their support. Gross income must be under USD 2,500, except a child who is a regular student, whose income may be up to USD 7,500 | [Section 1033.18(b)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Optional tax on self-employment gross income, not over USD 100,000 | 6 percent of gross income | In place of sections 1021.01 and 1021.02, only if section 1021.06(b) is met. No expenses or deductions | [Section 1021.06(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Optional tax, gross over USD 100,000 and not over USD 200,000 | 10 percent | Same conditions | [Section 1021.06(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Optional tax, gross over USD 200,000 and not over USD 300,000 | 13 percent | Same conditions | [Section 1021.06(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Optional tax, gross over USD 300,000 and not over USD 400,000 | 15 percent | Same conditions | [Section 1021.06(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Optional tax, gross over USD 400,000 and not over USD 500,000 | 17 percent | Same conditions | [Section 1021.06(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Optional tax, gross over USD 500,000 | 20 percent | Same conditions | [Section 1021.06(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Nonresident alien, not engaged in a Puerto Rico trade or business, most fixed or determinable Puerto Rico-source income | 29 percent | In place of sections 1021.01 and 1021.02. Includes interest from a related person, rents, royalties, salaries, annuities and net capital gain. Not insurance premiums | [Section 1091.01(a)(1)(A)(i)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Nonresident alien, dividends from Puerto Rico sources | 15 percent | Same class of taxpayer | [Section 1091.01(a)(1)(A)(ii)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Nonresident alien, share of an individual corporation (corporacion de individuos) | 33 percent | Same class of taxpayer | [Section 1091.01(a)(1)(A)(iii)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Estimated-tax threshold | Over USD 1,000 of estimated tax | Not wages-only, federal-wage-only, or agricultural-labor-only individuals, and not those whose other income is under USD 5,000 | [Section 1061.20(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Calendar-year return and payment date | 15 April following the close of the year | Moves to the next business day if that date is a Saturday, Sunday or holiday | [Sections 1061.16(a)(1) and 1061.17(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Automatic filing extension | 6 months from the original due date | Tax years beginning after 31 December 2016. Request by the original due date. Does not extend the time to pay | [Section 1061.16(a)(2)(A)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |

The alternate basic tax in section 1021.02 is a separate computation. For tax years beginning after 31 December 2018 the statute states 1 percent when alternate net income is over USD 25,000 and not over USD 50,000, 3 percent over USD 50,000 and not over USD 75,000, 5 percent over USD 75,000 and not over USD 150,000, 10 percent over USD 150,000 and not over USD 250,000, and 24 percent over USD 250,000. It is imposed instead of any other tax in that part when it is greater than the regular tax. It does not apply when the only income is wages reported on a withholding statement, or a pension covered by section 1031.02(a)(13)(A), (a)(13)(B) or (a)(14). [Section 1021.02(a)(1)(D) and (a)(2)(F)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf). Do not compute it from the regular-tax net income. The alternate base is gross income minus only the deductions the section lists, unless a Puerto Rico CPA agreed-upon-procedures or compliance report is attached, or, when business volume is under USD 1,000,000, a sworn due-diligence checklist from an authorized return specialist. [Section 1021.02(a)(2)(B) and (D)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

### Order of the regular computation

1. Start from gross income. Subtract the deductions the Code allows for that person. Subtract the section 1033.18 exemptions once. The result is the net income the section 1021.01(a)(3) table uses.
2. Compute the table tax. Add the gradual adjustment: 5 percent of the excess of that net income over USD 500,000, and stop at the cap.
3. Multiply the sum by 0.92 if the year begins after 31 December 2019 and gross income is not over USD 100,000. Otherwise multiply by 0.95 for a year beginning after 31 December 2018.
4. If the person has income other than wages on a withholding statement or the exempt pensions in section 1021.02(a)(2)(F), the alternate basic tax may replace this result when it is greater. This skill does not compute that base.
5. On a joint return, married spouses who live together may instead elect the section 1021.03 split: each spouse takes the individual personal exemption, half of the dependent exemptions, their own earned income, half of the unearned income, and half of the deductions in section 1033.15(a)(1) through (a)(4) and (a)(10). Each then computes sections 1021.01 and 1021.02 as an individual. The gradual-adjustment threshold is also applied to each spouse separately. [Section 1021.03](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

### Optional tax, when it is available

Section 1021.06 applies to tax years beginning after 31 December 2018. The person must carry on a trade or business for their own account, and that business must be substantially their source of income. All of the following are required:

- At least 80 percent of gross income for the year is from services subject to withholding under section 1062.03.
- That gross income was subject to the section 1062.03 withholding, or the section 1061.20 estimated-tax rules were met.
- For a year beginning after 31 December 2021, a balance due on the return is allowed only if it is paid in full by the filing deadline, ignoring any extension.

The tax is the section 1021.06(a) rate applied to gross income, ignoring exempt income. No expenses and no deductions are allowed, and the reports in section 1061.15 are not required if that section's conditions are met. The optional tax replaces both section 1021.01 and section 1021.02. [Section 1021.06](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

The statute states one rate for each gross-income band. It does not use the "plus the excess" formula of section 1021.01(a)(3). A gross income that sits entirely inside the first band (not over USD 100,000) is taxed at 6 percent either way. Do not apply a stacked marginal reading to a gross income that crosses USD 100,000 until Hacienda's computation for that year is in hand. That point is listed under Sources.

### Who must file

For a tax year beginning after 31 December 2018, a return is required when:

- A resident individual's gross income, reduced by the exclusions in section 1031.02, is greater than zero, unless the tax on that income was entirely withheld at source.
- A United States citizen who was not a Puerto Rico resident for all or part of the year has Puerto Rico-source gross income, reduced by those exclusions, greater than zero, unless the tax was paid entirely at source.
- A nonresident alien has taxable Puerto Rico-source gross income, unless the tax was paid entirely at source.
- Alternate basic tax net income under section 1021.02 is USD 25,000 or more.

Married spouses who live together file one joint return on their combined income, unless they elect separate returns. On separate returns each spouse uses the section 1021.03 split. [Section 1061.01](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

### Nonresidents

A nonresident alien who is not engaged in a Puerto Rico trade or business pays 29 percent, 15 percent or 33 percent, as the rates table states, on the Puerto Rico-source amounts received, instead of sections 1021.01 and 1021.02. A nonresident alien who is engaged in a Puerto Rico trade or business pays tax on the net income effectively connected with that business under the individual rules. An election can treat Puerto Rico real-property income as effectively connected. [Section 1091.01](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

Federal residence, the section 933 exclusion and which federal form is required are in `pr-federal-residence-and-filing`. Federal self-employment tax is in `pr-self-employment-tax`. Neither figure is restated here. A Puerto Rico decree does not, by itself, answer the federal tests.

## Boundary and exception table

| Situation | What changes |
| --- | --- |
| Gross income over USD 100,000 | Use 95 percent, not 92 percent |
| Net income subject to tax over USD 500,000 | Add the gradual adjustment, then apply the cap, then the 95 or 92 percent factor |
| Only wages on a withholding statement, or only a pension described in section 1021.02(a)(2)(F) | Alternate basic tax does not apply |
| Other income, and no CPA report or sworn checklist | Do not treat regular tax as the final liability. Alternate basic tax may be higher |
| Married, living together, electing the section 1021.03 split | Compute each spouse as an individual. Do not put the combined income through one table |
| Self-employment and section 1021.06(b) is met | Compare the optional tax with the regular tax. The optional tax allows no expenses |
| Dependent is a regular student and the taxpayer's child | The USD 2,500 exemption survives income up to USD 7,500, with the school's certification |
| Dependent is 1 year or older | The return must include that dependent's identification number |
| Act 60 or other exemption decree | These brackets do not measure the decree income |
| Nonresident alien not engaged in a Puerto Rico business | Use section 1091.01(a), not the resident table |

## Worked cases

**Case 1. Single wage earner.** A single resident has 2026 wages of USD 40,000 reported on a withholding statement, no other income, no other deductions and no dependents. The personal exemption is USD 3,500, so net income subject to the table is USD 36,500. That falls in the band over USD 25,000 and not over USD 41,500: USD 1,120 plus 14 percent of USD 11,500, which is USD 2,730. The gradual adjustment is zero. Gross income is not over USD 100,000 and the year begins after 31 December 2019, so the tax is 92 percent of USD 2,730, which is USD 2,511.60. Alternate basic tax does not apply because the only income is wages on a withholding statement.

```oa-check
name: Single wage earner, net income 36500 (2026)
inputs:
  net_income: 36500
steps:
  - excess: net_income - 25000
  - table_tax: 1120 + excess * 0.14
  - tax: table_tax * 0.92
expected:
  table_tax: 2730.00
  tax: 2511.60
```

**Case 2, a decision: optional tax or the regular table.** A single resident's only 2026 income is USD 80,000 of gross receipts from services. At least 80 percent of gross income is from services subject to section 1062.03 withholding, that withholding or the estimated-tax rule was met, and any balance will be paid by the return due date without an extension. Ordinary expenses are USD 20,000. There are no other deductions and no dependents.

Optional tax: 6 percent of USD 80,000 is USD 4,800. No expenses are allowed. Regular tax: net income after the USD 20,000 of expenses and the USD 3,500 exemption is USD 56,500. The table gives USD 3,430 plus 25 percent of USD 15,000, which is USD 7,180, then 92 percent, which is USD 6,605.60. The optional tax is USD 1,805.60 lower than this regular tax. Choose the optional tax on these facts. If the 80 percent or withholding condition fails, the optional tax is not available and this comparison does not apply. Alternate basic tax is not computed in this case. If the client does not elect the optional tax, a reviewer still has to run section 1021.02 before treating USD 6,605.60 as the amount due.

```oa-check
name: Optional tax against the regular table, gross 80000 (2026)
inputs:
  gross: 80000
  expenses: 20000
  exemption: 3500
steps:
  - optional_tax: gross * 0.06
  - regular_base: gross - expenses - exemption
  - excess: regular_base - 41500
  - table_tax: 3430 + excess * 0.25
  - regular_tax: table_tax * 0.92
  - saving: regular_tax - optional_tax
expected:
  optional_tax: 4800.00
  regular_base: 56500.00
  table_tax: 7180.00
  regular_tax: 6605.60
  saving: 1805.60
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-PR-ABT | Income other than wages or the pensions in section 1021.02(a)(2)(F), and the alternate-base deductions or the CPA report are not in the file | Stop. Do not quote the regular tax as the liability |
| R-PR-DECREE | Any income is under an Act 60 or other exemption decree | Stop. These brackets do not measure that income |
| R-PR-OPTIONAL-STACK | Gross income for the optional tax is over USD 100,000 | Stop until the band is confirmed as a flat rate or a slice. The first band, not over USD 100,000, is safe |
| R-PR-NRA | Nonresident alien and the file does not show whether a Puerto Rico trade or business exists | Do not choose between section 1091.01(a) and the resident table |
| R-PR-ENTITY | The person is a corporation, partnership, estate or trust | Use `pr-company-income-tax` for a regular corporation. Estates and trusts are outside this skill |
| R-PR-FED | The question is the federal return, section 933, or self-employment tax | Use `pr-federal-residence-and-filing` or `pr-self-employment-tax` |

## Filing and payment

The return is the planilla de contribucion sobre ingresos de individuos. Hacienda's informative copy for tax year 2025 is Formulario 482 (Form 482.0). That page says the 2025 return must be filed electronically and points to Carta Circular de Rentas Internas Num. 26-02 of 5 February 2026. [Hacienda, 2025 Formulario 482 informative copy](https://hacienda.pr.gov/documentos/2025-planilla-de-contribucion-sobre-ingresos-de-individuos-para-propositos-informativos-no-utilice-para-rendir-individual-income-tax-return-information-purposes). For years beginning after 31 December 2014 the Code requires the individual return on the electronic means the Secretary sets, and the Secretary may reject a paper return that is not within an exception. A rejected paper return is treated as not filed. [Section 1061.16(b)(1)(A)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

A calendar-year return is due on or before 15 April after the close of the year. For tax year 2026 that date is 15 April 2027. A fiscal year is due on the 15th day of the fourth month after year-end. If the date falls on a Saturday, Sunday or holiday, the next business day is the due date. For a year beginning after 31 December 2016, an automatic extension of six months is available if it is requested no later than the original due date. For a 2026 calendar year that extended date is 15 October 2027. The extension does not extend the time to pay. The tax is due on 15 April 2027 for a calendar year, or on the fiscal-year payment date in section 1061.17(a). The Secretary may extend the time to pay for up to six months on application. Payment may be required electronically. [Sections 1061.16 and 1061.17](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

Estimated tax, when section 1061.20 requires it, is paid in four equal instalments for a full year: the 15th day of the fourth, sixth and ninth months of the year, and the 15th day of the first month of the next year. For calendar year 2026 those dates are 15 April 2026, 15 June 2026, 15 September 2026 and 15 January 2027. Later first-time liability uses fewer instalments. [Section 1061.21(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

Interest on unpaid tax is 10 percent a year from the due date until payment. If the delay is 30 days or less there is no surcharge. A delay of more than 30 days and not more than 60 days adds 5 percent of the unpaid amount. A delay of more than 60 days adds 10 percent. A filing extension that is honoured is not subject to that surcharge. [Section 6030.02](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf). Failure to file, unless due to reasonable cause and not willful neglect, adds 5 percent if the failure is not more than 30 days, plus 10 percent for each further 30 days or fraction, and not more than 25 percent in total. The addition is computed on the net tax still unpaid at the original due date. [Section 6030.11](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

An individual who holds an Act 60 decree still files on the individual due date. The later corporate decree date in section 1061.16(e) does not apply to an individual. [Section 1061.16(e)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

## Completion checklist

- Residence class is identified before a table is chosen.
- Exemptions are subtracted once, and each dependent's support, age and income tests are recorded.
- Gross income is tested against USD 100,000 before choosing 92 or 95 percent.
- The gradual adjustment is zero, or it is computed and capped, before the percentage factor.
- Wage-only and pension-only cases are marked as outside the alternate basic tax. Every other case is flagged for section 1021.02.
- If the optional tax is used, the 80 percent test, the withholding or estimated-tax test, and the no-deduction rule are recorded.
- The payment date is the original due date unless a payment extension was granted. The filing extension is not treated as a payment extension.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Internal Revenue Code of 2011, revision of 28 May 2026. Read for sections 1010.01(a)(30), 1021.01(a)(3), (b)(4), (b)(5)(E) and (c), 1021.02(a)(1)(D) and (a)(2), 1021.03 and 1021.06. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Same code, same revision. Read for section 1033.18(a) and (b): USD 3,500, USD 7,000, USD 1,500, USD 2,500 and the USD 7,500 student rule. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Same code, same revision. Read for sections 1061.01, 1061.16, 1061.17, 1061.20 and 1061.21: who files, 15 April, the six-month extension, and the four estimated-tax dates. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Same code, same revision. Read for section 1091.01(a) and (b): 29 percent, 15 percent, 33 percent, and the effectively-connected rule. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Same code, same revision. Read for sections 6030.02 and 6030.11: 10 percent interest, the 5 and 10 percent surcharges, and the filing addition capped at 25 percent. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Hacienda page for the 2025 informative Formulario 482 (Form 482.0). Read for the form name and the statement that the 2025 individual return is filed electronically, referring to CC RI 26-02 of 5 February 2026. | https://hacienda.pr.gov/documentos/2025-planilla-de-contribucion-sobre-ingresos-de-individuos-para-propositos-informativos-no-utilice-para-rendir-individual-income-tax-return-information-purposes | 2026-11-13 |

Not yet confirmed: the 2026 Formulario 482 and any circular that restates the electronic-filing rule for the 2026 return were not on the Hacienda page read on 2026-11-13. Whether each optional-tax rate above USD 100,000, and each alternate-basic-tax rate, applies to the whole amount or only to the slice inside the band. The catalogue of section 1031.02 exclusions that reduce gross income for the filing test. The domicile factors the Secretary's regulation adds to the 183-day presumption. Weekend and holiday moves for 15 April 2027 and 15 October 2027 were not checked against the official holiday calendar.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pr-individual-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pr-individual-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
