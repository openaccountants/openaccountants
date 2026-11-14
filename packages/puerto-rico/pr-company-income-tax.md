---
name: pr-company-income-tax
description: >
  Compute the Puerto Rico income tax of a regular corporation for a tax year beginning in 2026 under the Internal Revenue Code of 2011 as revised 28 May 2026. Covers which entities are regular corporations, the 18.5 percent normal tax on net income less the dividends deduction, the graduated surtax (5 to 19 percent) after the USD 25,000 surtax deduction and its split in a controlled group, the alternative minimum tax (greater of USD 500 or 18.5 percent, 23 percent for USD 10 million businesses, USD 50,000 exempt amount), the net operating loss carryforward (10 years, 90 percent of net income), the optional gross income tax for service corporations, the 20 percent alternative tax on long-term capital gains, the financial statement tiers (USD 1, 3 and 10 million), quarterly estimated tax over USD 1,000, and filing Form 480.20 electronically by 15 April with a 6-month extension (Form AS 2644) that requires full payment. Trigger on "Puerto Rico corporate tax", "Form 480.20", "contribucion adicional", "surtax Puerto Rico", "corporacion regular", "Schedule X optional tax", "Puerto Rico estimated tax corporation".
version: "1.0"
jurisdiction: PR
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Puerto Rico regular corporation income tax, tax year 2026

> **Source-cited draft.** Built from the Puerto Rico Internal Revenue Code of 2011 (Ley 1-2011), legislative-library revision of 28 May 2026 (amendments to Ley 93 of 26 May 2026), and Hacienda's 2025 instructions for Form 480.20 with the Form 480.20 document page, read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A regular corporation pays a **normal tax of 18.5 percent** on net income less the dividends deduction, plus a **surtax** on that same base less a **USD 25,000** deduction: 5 percent up to USD 75,000, rising by bands to 19 percent above USD 275,000 (top combined marginal rate 37.5 percent). If tentative minimum tax (the greater of **USD 500** or **18.5 percent** of alternative minimum net income above the exempt amount, **23 percent** for businesses with USD 10 million or more of volume) is higher, the excess is added. A controlled group shares one USD 25,000 deduction. A service corporation with at least 80 percent of gross income from services subject to withholding can instead pay an optional tax on gross income (6 percent up to USD 100,000). For a calendar 2026 year, Form 480.20 is filed electronically and the tax paid by **15 April 2027**; the automatic 6-month extension (Form AS 2644 through SURI) requires the full tax with the request. Estimated tax is due in four instalments in 2026 when it is over USD 1,000.

## Scope and who this is for

In scope: a "regular corporation" (corporación regular) for a tax year beginning after 31 December 2025: a domestic corporation, or a foreign corporation engaged in a trade or business in Puerto Rico on its effectively connected income. Regular corporation excludes (section 1022.01(c)): corporations taxed under Subchapter A of Chapter 11, special employee-owned corporations, special partnerships, corporations of individuals, foreign corporations not engaged in a Puerto Rico trade or business (taxed under section 1092.01), and limited liability companies under Chapter 7. Establish the entity's classification and any election (Form AS 6045) before using these rates. [Section 1022.01(c)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Act 60 decree corporations (export services, manufacturing) | `pr-act-60-incentives` |
| Individuals, including the individual optional tax | `pr-individual-income-tax` |
| Sales and use tax (IVU) | `pr-ivu-sales-and-use-tax` |
| Federal tax of the shareholders | `pr-federal-residence-and-filing` |
| Municipal licence tax, property tax (CRIM), payroll | not covered in this pack yet |

## Ask the client first

1. **Entity and classification:** corporation, LLC or partnership; any classification election; domestic or foreign; decree under Act 60 or an earlier incentives law.
2. **Tax year:** calendar or fiscal; first year or short year.
3. **Group:** other corporations or entities under common control on 31 December 2026 (controlled group under section 1010.04, related group under section 1010.05), and any agreed plan for the surtax deduction.
4. **Volume of business** for 2026 (this entity and the related group), for the financial statement tier.
5. **Income mix:** share of gross income from services subject to withholding under section 1062.03; long-term capital gains; dividends received.
6. **Losses and payments:** net operating losses carried forward by year; 2026 estimated payments made.

## The method, step by step

### Rates, bands and thresholds

All rows: Ley 1-2011 as revised 28 May 2026, unless the row names Hacienda.

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Normal tax | 18.5% of net income subject to normal tax | Years beginning after 31 Dec 2018 | [Section 1022.01(b)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Surtax deduction | USD 25,000 | Years beginning after 31 Dec 2012; shared in a controlled group | [Section 1022.02(d)(2), (e)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Surtax, base not over USD 75,000 | 5% | Base is normal-tax net income less the surtax deduction | [Section 1022.02(b)(2)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Surtax, over USD 75,000 to USD 125,000 | USD 3,750 plus 15% of the excess over USD 75,000 | same | same |
| Surtax, over USD 125,000 to USD 175,000 | USD 11,250 plus 16% of the excess over USD 125,000 | same | same |
| Surtax, over USD 175,000 to USD 225,000 | USD 19,250 plus 17% of the excess over USD 175,000 | same | same |
| Surtax, over USD 225,000 to USD 275,000 | USD 27,750 plus 18% of the excess over USD 225,000 | same | same |
| Surtax, over USD 275,000 | USD 36,750 plus 19% of the excess over USD 275,000 | same | same |
| Tentative minimum tax | Greater of USD 500 or 18.5% of alternative minimum net income over the exempt amount, less the alternative minimum foreign tax credit | Years beginning after 31 Dec 2018 | [Section 1022.03(g)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Tentative minimum tax rate, large businesses | 23% instead of 18.5% | Corporations within section 1061.15(a)(4) (volume of USD 10 million or more) | [Section 1022.03(g)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Alternative minimum tax exempt amount | USD 50,000, reduced by 25% of alternative minimum net income over USD 500,000 (not below zero) | | [Section 1022.03(c)(3)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Net operating loss carryforward | 10 years | Losses of years beginning after 31 Dec 2012 | [Section 1033.14(b)(1)(C)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Net operating loss deduction cap | 90% of net income | Years beginning after 31 Dec 2018 | [Section 1033.14(b)(1)(D)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Alternative tax on long-term capital gain | 20% of the excess of net long-term gain over net short-term loss, plus regular tax on the rest | Transactions after 30 Jun 2014; only if lower than the regular computation | [Section 1023.03(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Optional tax for service corporations, gross income not over USD 100,000 | 6% of gross income | At least 80% of gross income from services subject to section 1062.03 withholding; all gross income withheld on or estimated tax paid; balance paid by the original due date; no deductions | [Section 1022.07](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Optional tax, over USD 100,000 to USD 200,000 | 10% | same | same |
| Optional tax, over USD 200,000 to USD 300,000 | 13% | same | same |
| Optional tax, over USD 300,000 to USD 400,000 | 15% | same | same |
| Optional tax, over USD 400,000 to USD 500,000 | 17% | same | same |
| Optional tax, over USD 500,000 | 20% | same | same |
| Estimated tax required | Estimated tax over USD 1,000, including alternative minimum tax | Corporations engaged in business in Puerto Rico | [Section 1061.23(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Financial statements not required | Volume under USD 1,000,000 | A voluntary agreed-upon procedures report lifts the section 1022.04 deduction limits | [Section 1061.15(a)(1)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Audited statements optional | Volume USD 1,000,000 to under USD 3,000,000 | Audited statements, or an agreed-upon procedures or compliance attestation report, by a CPA licensed in Puerto Rico | [Section 1061.15(a)(2)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Audited statements, or a report in their place | Volume USD 3,000,000 to under USD 10,000,000 | Agreed-upon procedures or compliance attestation report allowed instead of audited statements | [Section 1061.15(a)(3)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Audited statements required | Volume USD 10,000,000 or more | Audit report by a CPA licensed in Puerto Rico under US GAAS; related groups counted in aggregate | [Section 1061.15(a)(4), (5)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Interest on unpaid tax | 10% a year | From the due date | [Hacienda, 2025 Form 480.20 instructions, Interests](https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf) |
| Surcharge | 5% if more than 30 and not more than 60 days late; 10% if more than 60 days | When interest applies | [Hacienda, 2025 Form 480.20 instructions, Surcharges](https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf) |
| Late filing penalty | 5% to 25% of the tax | Unless reasonable cause | [Hacienda, 2025 Form 480.20 instructions, Penalties](https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf) |
| Estimated tax penalty | 10% of each instalment due and not paid | Schedule T Corporation; not for the optional tax | [Hacienda, 2025 Form 480.20 instructions, Schedule T](https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf) |

Quick check of the regular tax, for a standalone corporation with the full USD 25,000 deduction, no special-rate income and no alternative minimum tax:

| Normal-tax base (USD) | Normal tax | Surtax base | Surtax | Regular tax |
| ---: | ---: | ---: | ---: | ---: |
| 25,000 | 4,625 | 0 | 0 | 4,625 |
| 100,000 | 18,500 | 75,000 | 3,750 | 22,250 |
| 200,000 | 37,000 | 175,000 | 19,250 | 56,250 |
| 400,000 | 74,000 | 375,000 | 55,750 | 129,750 |

The Code prints an older surtax table (section 1022.02(b)(1), years 2011 to 2013, 5 and 10 percent with a USD 750,000 deduction) above the current one. Do not use it.

### Step 1: net income

Start from gross income less allowable deductions (Form 480.20 Part III). Deduct a net operating loss carried forward: losses of years beginning after 2012 carry forward 10 years, and for a year beginning after 2018 the loss used cannot exceed 90 percent of net income (Schedule G Corporation). An ownership change of 50 percent or more limits carried losses under section 1033.14(b)(3). [Section 1033.14](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

### Step 2: normal tax

Net income subject to normal tax is net income less the dividends deduction of section 1033.19(a); for a foreign corporation engaged in business in Puerto Rico, it is the net income effectively connected with that business. Multiply by 18.5 percent. It is a tax on net income, not gross sales. [Section 1022.01](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

### Step 3: surtax

Surtax base = normal-tax base less the surtax deduction. Apply the table. The USD 25,000 does not reduce the normal-tax base. A member of a controlled group on 31 December gets USD 25,000 divided by the number of members, unless all members agree a plan allocating it (Form AS 2652.1); the total for the group cannot exceed USD 25,000. A short year not including 31 December uses the member count on its last day. [Section 1022.02(d) to (f)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

### Step 4: alternative minimum tax

Alternative minimum net income is the normal-tax base with the section 1022.04 adjustments; it cannot be replaced by book profit. Subtract the exempt amount, apply 18.5 percent (or 23 percent), take the greater of that and USD 500, less the alternative minimum foreign tax credit. Regular tax is the normal tax plus surtax less the section 1051.01 credit. The alternative minimum tax is only the **excess** of tentative minimum tax over regular tax (Schedule A Corporation). Example: regular tax USD 22,250 and a separately computed tentative minimum tax of USD 24,000 add USD 1,750, for USD 24,000 in total, not USD 46,250; a lower tentative tax adds nothing. Corporations that submit an agreed-upon procedures report or audited statements are not subject to the section 1022.04 deduction limits. [Sections 1022.03 to 1022.05](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf); [Hacienda, 2025 Form 480.20 instructions, Financial Statements Requirement](https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf).

### Step 5: the alternatives that replace the regular computation

- **Long-term capital gain:** if net long-term gain exceeds net short-term loss, compute regular tax on income without that gain plus 20 percent of the gain, and use it only if lower (Schedule D1 Corporation, return line 4). [Section 1023.03](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).
- **Optional tax for service corporations (Schedule X Corporation):** in place of the normal tax, surtax and alternative minimum tax, the rate for the gross income band times gross income (exempt income excluded), with no deductions and without the section 1061.15 financial statements. Hacienda's 2025 instructions say to multiply taxable gross income by the applicable rate. Eligibility: at least 80 percent of gross income from services subject to section 1062.03 withholding, all gross income subject to that withholding or estimated tax paid under section 1061.23, and any balance paid in full by the original due date (no extension). A corporation that chose it in SURI with the 6 percent partial withholding waiver (CC RI 19-16) must use Schedule X if it meets the 80 percent test. [Section 1022.07](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf); [Hacienda, 2025 Form 480.20 instructions, Schedule X](https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf).

### Step 6: financial statements

Use the volume tiers in the table. A related group under section 1010.05 adds its members' volume; when the aggregate is USD 10 million or more, members with USD 3 million or more file consolidated or combined statements (or individual audited statements listing all related entities), and members under USD 1 million need no audit but do need an agreed-upon procedures or compliance report unless they file audited statements. Audited statements carry the supplementary information of section 1061.15(b) only for certain construction businesses, hospitals and financial institutions for years after 2022, due by the last day of the month after the return due date including extensions (30 November for a calendar-year corporation, even without an extension). [Section 1061.15](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf); [Hacienda, 2025 Form 480.20 instructions](https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf).

The Code reads the USD 3 million to USD 10 million tier as audited statements with a report allowed in their place; Hacienda's instructions describe it as a choice that lifts the section 1022.04 limits. Treat it as a requirement and flag it.

### Step 7: estimated tax for 2026

If estimated tax (including alternative minimum tax) is over USD 1,000, pay 25 percent by the 15th day of the 4th, 6th, 9th and 12th months of the tax year: for calendar 2026, 15 April, 15 June, 15 September and 15 December 2026. If the duty first arises later in the year, pay a third each in months 6, 9 and 12, half each in months 9 and 12, or all in month 12. Payments are made electronically through SURI. A decree corporation may pay the first instalment with the second, by the 15th day of the 6th month. [Section 1061.23](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf); [Hacienda, 2025 Form 480.20 instructions, Estimated Tax Payment](https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| LLC, partnership, corporation of individuals or special partnership | Not a regular corporation; check classification and pass-through rules first |
| Foreign corporation with no Puerto Rico trade or business | Section 1092.01, not these rates |
| Foreign corporation operating as a branch | Also a 10% branch profits tax on the dividend equivalent amount, unless 80% of gross income was Puerto Rico source or effectively connected over the 3 years (Form AS 2879) |
| Controlled group | One USD 25,000 surtax deduction shared; allocate by plan to the member with the highest marginal surtax rate |
| Act 60 decree corporation | Return and tax due the 15th day of the 6th month (15 June 2027 for calendar 2026); decree rates in `pr-act-60-incentives` |
| Large taxpayer | Return filed where or how the Secretary specifies; otherwise treated as not filed |
| Weekend or holiday due date | Next working day |
| Emergency declared by the Governor or the President | The Secretary may move filing and payment dates by up to 6 months by administrative determination |
| Service corporation with gross income over USD 500,000 | Optional tax at 20% of gross; compare with the regular computation before choosing |
| Balance not paid by the original due date | Optional tax lost; regular rates apply |
| Net operating loss larger than 90% of net income | Only 90% used; the rest carries forward within the 10 years |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Group membership | Assume a group exists until ruled out; do not give a full USD 25,000 |
| Volume of business | Ask; the tier decides the alternative minimum tax rate and the statements |
| Alternative minimum net income | Do not compute alternative minimum tax from book profit; flag it |
| Share of services income | Optional tax not available until the 80% test is shown |

### Red flags

| Flag | Why it matters |
| --- | --- |
| Group members each claiming USD 25,000 | Surtax understated |
| Volume near USD 10 million | 23% tentative minimum rate and audited statements |
| No estimated payments with tax over USD 1,000 | 10% addition per instalment |
| Extension requested without paying the tax | Interest, surcharge, and the optional tax is lost |

## Worked cases

**Case 1, net operating loss and the 90 percent cap.** A standalone calendar-year regular corporation has 2026 net income of USD 240,000 before a USD 300,000 loss carried forward from 2022, no dividends deduction and no special-rate income. The loss used is capped at 90 percent, USD 216,000, leaving net income of USD 24,000 and USD 84,000 of loss to carry forward to 2027 (the 2022 loss expires after 2032). Normal tax: 18.5 percent of USD 24,000, USD 4,440. Surtax base: zero after the USD 25,000 deduction. Regular tax USD 4,440, before checking the alternative minimum tax on the alternative base.

```oa-check
name: Net operating loss capped at 90 percent, regular tax (2026)
inputs:
  net_income: 240000
  nol_available: 300000
steps:
  - nol_used: min(nol_available, net_income * 0.9)
  - base: net_income - nol_used
  - nol_left: nol_available - nol_used
  - normal_tax: base * 0.185
  - surtax_base: max(base - 25000, 0)
  - surtax: 0.05 * min(surtax_base, 75000) + 0.15 * clamp(surtax_base - 75000, 0, 50000) + 0.16 * clamp(surtax_base - 125000, 0, 50000) + 0.17 * clamp(surtax_base - 175000, 0, 50000) + 0.18 * clamp(surtax_base - 225000, 0, 50000) + 0.19 * max(surtax_base - 275000, 0)
  - regular_tax: normal_tax + surtax
expected:
  nol_used: 216000
  base: 24000
  nol_left: 84000
  normal_tax: 4440
  regular_tax: 4440
```

**Case 2, a decision: how should a two-company group allocate the surtax deduction?** Two regular corporations are a controlled group on 31 December 2026. A has a normal-tax base of USD 300,000; B has USD 60,000. With the default equal split (USD 12,500 each), A's surtax base is USD 287,500 (surtax USD 39,125) and B's is USD 47,500 (USD 2,375): total surtax USD 41,500. With a plan giving all USD 25,000 to A, A's surtax is USD 36,750 and B's USD 3,000: total USD 39,750. Giving it all to B would cost USD 43,250. Choose the plan allocating the deduction to A, which saves USD 1,750 against the equal split, because each dollar of deduction at A saves 19 percent while at B it saves only 5 percent. The normal tax is the same in every option.

```oa-check
name: Controlled group surtax deduction allocation (2026)
inputs:
  base_a: 300000
  base_b: 60000
steps:
  - a_equal: 36750 + 0.19 * (base_a - 12500 - 275000)
  - b_equal: 0.05 * (base_b - 12500)
  - equal_total: a_equal + b_equal
  - a_plan: 36750 + 0.19 * max(base_a - 25000 - 275000, 0)
  - b_plan: 0.05 * min(base_b, 75000)
  - plan_total: a_plan + b_plan
  - a_to_b: 36750 + 0.19 * (base_a - 275000)
  - b_to_b: 0.05 * (base_b - 25000)
  - to_b_total: a_to_b + b_to_b
  - saving_vs_equal: equal_total - plan_total
expected:
  a_equal: 39125
  b_equal: 2375
  equal_total: 41500
  plan_total: 39750
  to_b_total: 43250
  saving_vs_equal: 1750
```

**Case 3, a decision: optional tax or regular tax for a small service company.** A consulting corporation has 2026 gross income of USD 90,000, all from services subject to section 1062.03 withholding, and will pay any balance by 15 April 2027. With expenses of USD 50,000, the regular tax on USD 40,000 is USD 7,400 normal tax plus USD 750 surtax, USD 8,150; the optional tax is 6 percent of USD 90,000, USD 5,400. Choose the optional tax, saving USD 2,750. With expenses of USD 75,000, net income is USD 15,000 and the regular tax is USD 2,775: the regular computation wins by USD 2,625 (check the alternative minimum tax first). The figure that decides is the expense ratio.

```oa-check
name: Service corporation optional tax against regular tax (2026)
inputs:
  gross: 90000
  expenses_low: 50000
  expenses_high: 75000
steps:
  - optional_tax: gross * 0.06
  - net_low: gross - expenses_low
  - regular_low: net_low * 0.185 + 0.05 * max(net_low - 25000, 0)
  - saving_low: regular_low - optional_tax
  - net_high: gross - expenses_high
  - regular_high: net_high * 0.185 + 0.05 * max(net_high - 25000, 0)
  - saving_high: optional_tax - regular_high
expected:
  optional_tax: 5400
  regular_low: 8150
  saving_low: 2750
  regular_high: 2775
  saving_high: 2625
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-PRC-DECREE | Act 60 or earlier incentives decree | Use `pr-act-60-incentives`; the regular rates may not apply |
| R-PRC-AMT | Alternative minimum net income needed | Refer: section 1022.04 adjustments are not computed here |
| R-PRC-CREDITS | Tax credits, foreign tax credit or the section 1051.01 credit | Refer |
| R-PRC-ACCUM | Improper accumulation of surplus | Refer: section 1022.05 additional tax |
| R-PRC-FINANCIAL | Bank, insurer or financial business | Refer: special rules and section 1023.10 |
| R-PRC-REORG | Reorganization or ownership change with losses | Refer: section 1033.14(b)(2) and (3) limits |
| R-PRC-GROSS | Optional tax with gross income above USD 100,000 where Hacienda's later guidance may differ | Confirm the year's Schedule X before relying on the flat-rate reading |

## Filing and payment

1. **Return:** Form 480.20 (Planilla de Contribución sobre Ingresos de Corporaciones) for calendar 2026, filed electronically with a program certified by Hacienda, by **15 April 2027** (fiscal year: 15th day of the 4th month after year end). A foreign corporation with no office or place of business in Puerto Rico files by the 15th day of the 6th month. Decree corporations file by **15 June 2027**. For 2025 Hacienda required electronic filing under Circular Letter CC RI 26-06; expect the same for 2026.
2. **Evidence:** upload the supporting evidence to SURI (suri.hacienda.pr.gov) after filing and no later than the 4th business day after the due date including extensions (or after filing, if late).
3. **Extension:** automatic 6 months (to 15 October 2027) if Form AS 2644 is filed electronically through SURI by the due date. The corporation must pay the whole tax with the request; the extension does not extend payment. A separate extension to pay of up to 6 months may be granted by the Secretary on request (section 1061.17(c)). Corporations cannot pay in two instalments.
4. **Payment:** by 15 April 2027 (15 June 2027 for decree corporations), electronically through SURI or by electronic debit with the certified program.
5. **Signature:** one officer (president, vice president, treasurer, assistant treasurer or principal or finance officer), by digital signature.
6. **After filing:** keep the copy with Hacienda's electronic filing seal; it serves when a government contract needs the filing certification (Form SC 6088).

Sources: [Sections 1061.16 and 1061.17](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf); [Hacienda, 2025 Form 480.20 instructions](https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf); [Hacienda, Form 480.20 (2025) document page](https://hacienda.pr.gov/documentos/2025-planilla-de-contribucion-sobre-ingresos-de-corporaciones-para-propositos-informativos-no-utilice-para-rendir-corporation-income-tax-return-information).

## Completion checklist

- Regular corporation status confirmed; no decree.
- Group membership on 31 December checked; surtax deduction allocation recorded (Form AS 2652.1).
- Net operating loss used within the 90% cap and the 10-year window.
- Normal tax and surtax on the right bases; alternative minimum tax run (Schedule A Corporation).
- Capital gain alternative and Schedule X compared where they apply.
- Financial statement tier set from this entity's and the group's volume.
- 2026 estimated instalments reconciled; Schedule T run.
- Return, evidence and payment through SURI by the due date.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Código de Rentas Internas de Puerto Rico de 2011 (Ley 1-2011), revision of 28 May 2026, Oficina de Gerencia y Presupuesto legislative library. Read for sections 1022.01, 1022.02 (pages 47 to 49), 1022.03(a), (c)(3) and (g), 1022.07, 1023.03, 1033.14(b), 1061.15(a), 1061.16, 1061.17 and 1061.23. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-14 |
| Hacienda, Instructions for Form 480.20, Corporation Income Tax Return, 2025. Read for electronic filing and SURI evidence, financial statements requirement, estimated tax, when and where to file, the AS 2644 extension, interest, surcharges and penalties, Schedule T and Schedule X. | https://hacienda.pr.gov/sites/default/files/inst_corporations_2025.pdf | 2026-11-14 |
| Hacienda, Form 480.20 (2025) document page. Read for the notice that the 2025 return must be filed electronically under CC RI 26-06 of 13 March 2026. | https://hacienda.pr.gov/documentos/2025-planilla-de-contribucion-sobre-ingresos-de-corporaciones-para-propositos-informativos-no-utilice-para-rendir-corporation-income-tax-return-information | 2026-11-14 |

Not yet confirmed: Hacienda's 2026 Form 480.20 and its instructions were not published on the read date, so the filing mechanics, schedules, interest, surcharge and penalty figures are from the 2025 instructions; the penalty, interest and surcharge figures were not read in Subtitle F of the Code; whether any amendment after 28 May 2026 changes these sections was not checked; CC RI 26-06 itself was not read; the dividends deduction of section 1033.19(a), the section 1022.04 adjustments and the section 1051.01 credit were not read.
