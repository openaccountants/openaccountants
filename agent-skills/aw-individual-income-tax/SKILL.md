---
name: aw-individual-income-tax
description: "Aruba individual income tax (inkomstenbelasting) and the annual wage tax table for tax year 2026. Covers resident and non-resident taxpayers, table income (taxable income or net full-year wage less the tax-free amount of at most Afl. 30,000), the 2026 four-band table at 0%, 21%, 42% and 52%, rounding down to whole florins, the 3% employment-cost deduction capped at Afl. 1,500, separate taxation of the SVB AOV pension, tips, the two-month return deadline, the automatic four-month extension, late-filing penalties and collection costs. Trigger phrases include Aruba income tax, inkomstenbelasting Aruba, loonbelasting Aruba, tabelinkomen, belastingvrije som, DIMP, impuesto.aw."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/aw-individual-income-tax"
  jurisdiction: "AW"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Aruba individual income tax: 2026 table and method v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar year 2026. Authority: Departamento di Impuesto (DIMP), impuesto.aw. Amounts are Aruban florins (Afl.). DIMP converts USD at Afl. 1.79 ([DIMP, Hoeveel BBO en BAVP moet u betalen](https://www.impuesto.aw/hoeveel-bbo-en-bavp-moet-u-betalen)).

## Who this applies to

- **Residents** file income tax on their income; employees have wage tax withheld through payroll, using the same table ([DIMP, Tarief inkomstenbelasting en loonbelasting](https://www.impuesto.aw/tarief-inkomstenbelasting-en-loonbelasting)).
- **Non-residents** (buitenlandse belastingplichtigen) are those who did not live in Aruba all year but had Aruban sources of income, or lived there part of the year and had Aruban income in the period they did not. Sources include Aruban real estate, business and professional income earned in Aruba, and pensions and periodic payments paid by Aruba or APFA. They file if they receive a return or should reasonably know tax is due ([DIMP, Aangifte buitenlandse belastingplichtigen](https://www.impuesto.aw/aangifte-buitenlandse-belastingplichtigen)).
- **Not covered:** profit tax, dividend tax, the wage tax monthly withholding mechanics beyond the annual table, social premiums (`aw-social-contributions`), turnover taxes (`aw-turnover-taxes`).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Band 1: table income 0 to 34,930 | 0% | Tax 0 | 2026 | [DIMP, Tarief inkomstenbelasting en loonbelasting](https://www.impuesto.aw/tarief-inkomstenbelasting-en-loonbelasting) |
| Band 2: over 34,930 to 63,904 | 21% of the excess over 34,930 | Base tax 0 | 2026 | same |
| Band 3: over 63,904 to 135,527 | 42% of the excess over 63,904 | Base tax 6,084.54 | 2026 | same |
| Band 4: over 135,527 | 52% of the excess over 135,527 | Base tax 36,166.20 | 2026 | same |
| Tax-free amount (belastingvrije som) | at most Afl. 30,000 a year | Deducted to reach table income; reduced pro rata if liable for only part of the year | 2026 | same |
| Rounding | down to whole florins | On the tax from the table | 2026 | same |
| Employment costs (verwervingskosten) in wage tax | 3%, at most Afl. 1,500 | Deducted from the full-year wage | 2026 | [DIMP, Premies volksverzekering](https://www.impuesto.aw/premies-volksverzekering) |
| Late return after a reminder | 5% of the tax due, minimum Afl. 250, up to Afl. 10,000 | Return received after the reminder's new deadline | 2026 | [DIMP, U doet geen of niet op tijd aangifte](https://www.impuesto.aw/u-doet-geen-of-niet-op-tijd-aangifte) |
| Reminder (aanmaning) cost | Afl. 10 | Unpaid assessment | 2026 | [DIMP, U betaalt deels niet of niet op tijd](https://www.impuesto.aw/u-betaalt-deels-niet-of-niet-op-tijd) |
| Writ (dwangschrift) cost | at least Afl. 25 | | 2026 | same |
| Attachment costs | at least Afl. 107.15 (movables), 146.50 (real estate), 132.15 (third parties) | | 2026 | same |

The 2025 table on the same page is identical to the 2026 table. The 2023 table had a 10% first band (Belastingplan 2023, AB 2022 no. 161); do not use it for 2026 ([DIMP, Belastingplan 2023](https://www.impuesto.aw/belastingplan_2023)).

## The base

1. **Income tax:** table income = taxable income less the tax-free amount ([DIMP, Tarief inkomstenbelasting en loonbelasting](https://www.impuesto.aw/tarief-inkomstenbelasting-en-loonbelasting)).
2. **Wage tax:** table income = net full-year wage (zuiver voljaarsloon) less the tax-free amount (same page). DIMP's method: annualise the gross wage; deduct the 3% costs (max Afl. 1,500) and the employee's AOV/AWW and AZV premiums to reach the net full-year wage; deduct the tax-free amount; apply the table ([DIMP, Hoeveel loonbelasting houdt u in en draagt u af](https://www.impuesto.aw/hoeveel-loonbelasting-houdt-u-in-en-draagt-u-af)). That page's example uses 2019 figures; use the 2026 amounts above.
3. **Wage includes** money (salary, holiday pay, overtime, bonus, 13th month), benefits in kind at market value, entitlements (pension entitlements are exempt) and expense allowances. Private use of a company car adds 15% of its catalogue value ([DIMP, Waarover houdt u loonbelasting en premies in](https://www.impuesto.aw/waarover-houdt-u-loonbelasting-en-premies-in)).
4. **Tips** stay exempt from wage and income tax ([DIMP, Belastingplan 2023](https://www.impuesto.aw/belastingplan_2023)).
5. **The SVB AOV pension** is taxed separately for each spouse, not added to the higher earner's income (same page).
6. **Not covered here:** other deductions, personal charges, credits and special rates. Check the 2026 return instructions.

## Deadlines and filing

- File within the legal period of 2 months after the return is issued. Where the return's part 2 allows it, an automatic, one-time extension moves the deadline to 4 months after the official issue date on the label; no further extension ([DIMP, U kunt niet op tijd aangifte doen](https://www.impuesto.aw/u-kunt-niet-op-tijd-aangifte-doen)).
- Returns are filed in the BOi portal. DIMP announced that the 2025 income tax return is available in BOi from 16 November 2026 ([DIMP, Tarief inkomstenbelasting en loonbelasting](https://www.impuesto.aw/tarief-inkomstenbelasting-en-loonbelasting)), so with the 2-month rule it is due about mid-January 2027 unless the label says otherwise.
- Not registered yet: file the form "Opgaaf persoonsgegevens particulieren"; returns then arrive by post. Registered taxpayers can request a duplicate online ([DIMP, Aangiftebiljet inkomstenbelasting aanvragen](https://www.impuesto.aw/aangiftebiljet-inkomstenbelasting-aanvragen)).

## Penalties and interest

- Return not filed by the deadline: a reminder giving 10 working days. Filed after that: penalty of 5% of the tax due, minimum Afl. 250, up to Afl. 10,000. Not filed at all: the Inspector estimates income and imposes an ex officio assessment ([DIMP, U doet geen of niet op tijd aangifte](https://www.impuesto.aw/u-doet-geen-of-niet-op-tijd-aangifte)).
- Assessment not paid by the due date: a reminder (pay within 3 weeks, cost Afl. 10), then a wage garnishment for employees (up to one third of net pay) or a writ (pay within 2 days), then attachment. Collection interest runs from the day after the due date to the day before payment ([DIMP, U betaalt deels niet of niet op tijd](https://www.impuesto.aw/u-betaalt-deels-niet-of-niet-op-tijd)). The interest rate is not on the page.

## Cross-border points

- Non-residents are taxed on Aruban sources only, see "Who this applies to".
- Part-year liability: the tax-free amount is reduced pro rata ([DIMP, Hoeveel loonbelasting houdt u in en draagt u af](https://www.impuesto.aw/hoeveel-loonbelasting-houdt-u-in-en-draagt-u-af)).
- Treaties and the tax arrangement for the Kingdom: refer.

## Two worked examples that recompute

**Case 1: employee on Afl. 8,000 a month, 2026.** Full-year wage 96,000. Less costs 1,500 (3% would be 2,880, capped), employee AOV/AWW 5% of the Afl. 85,000 ceiling = 4,250 and AZV 1.6% of 85,000 = 1,360: net full-year wage 88,890. Less the tax-free amount 30,000: table income 58,890. Tax: 21% of (58,890 less 34,930) = 5,031.60, rounded down to Afl. 5,031.

```oa-check
name: Aruba 2026 employee, Afl. 8000 a month
inputs:
  monthly_wage: 8000
  premium_ceiling: 85000
  tax_free: 30000
steps:
  - full_year: monthly_wage * 12
  - costs: min(full_year * 0.03, 1500)
  - aov_aww: min(full_year, premium_ceiling) * 0.05
  - azv: min(full_year, premium_ceiling) * 0.016
  - net_full_year: full_year - costs - aov_aww - azv
  - table_income: net_full_year - tax_free
  - tax_exact: (table_income - 34930) * 0.21
  - tax: floor(tax_exact)
expected:
  net_full_year: 88890.00
  table_income: 58890.00
  tax_exact: 5031.60
  tax: 5031
```

**Case 2: table income of Afl. 150,000, and the band continuity check.** Band 4: 36,166.20 + 52% of (150,000 less 135,527) = 43,692.16, rounded down to 43,692. The base tax of band 4 equals 42% of the whole band 3 width plus the band 3 base: 6,084.54 + 42% of 71,623 = 36,166.20, so the table is continuous.

```oa-check
name: Aruba 2026 table income 150000
inputs:
  table_income: 150000
steps:
  - band3_full: 6084.54 + (135527 - 63904) * 0.42
  - tax_exact: 36166.20 + (table_income - 135527) * 0.52
  - tax: floor(tax_exact)
expected:
  band3_full: 36166.20
  tax_exact: 43692.16
  tax: 43692
```

## Ask the client first

1. Did you live in Aruba all of 2026? If not, the dates and your Aruban sources of income.
2. Employee, self-employed, pensioner, or a mix? Annual statements from each payer.
3. Married? Does either spouse receive the SVB AOV pension?
4. Benefits in kind (company car, housing, meals) and pension contributions.
5. When was your return issued (the label date), and does it allow the automatic extension?

## Sources

| Source | URL | Read on |
|---|---|---|
| DIMP, Tarief inkomstenbelasting en loonbelasting: read for the 2026 and 2025 tables, table income, the Afl. 30,000 tax-free amount, rounding and the 2025 return in BOi from 16 November 2026 | https://www.impuesto.aw/tarief-inkomstenbelasting-en-loonbelasting | 2026-11-14 |
| DIMP, Belastingplan 2023: read for the 2023 table, the tax-free amount rise, tips and separate taxation of the AOV pension | https://www.impuesto.aw/belastingplan_2023 | 2026-11-14 |
| DIMP, Hoeveel loonbelasting houdt u in en draagt u af: read for the wage tax steps and pro rata tax-free amount | https://www.impuesto.aw/hoeveel-loonbelasting-houdt-u-in-en-draagt-u-af | 2026-11-14 |
| DIMP, Premies volksverzekering: read for the 3% costs capped at Afl. 1,500 | https://www.impuesto.aw/premies-volksverzekering | 2026-11-14 |
| DIMP, Waarover houdt u loonbelasting en premies in: read for the wage concept and the 15% car addition | https://www.impuesto.aw/waarover-houdt-u-loonbelasting-en-premies-in | 2026-11-14 |
| DIMP, Aangifte buitenlandse belastingplichtigen: read for who is a non-resident taxpayer | https://www.impuesto.aw/aangifte-buitenlandse-belastingplichtigen | 2026-11-14 |
| DIMP, U kunt niet op tijd aangifte doen: read for the 2-month period and the 4-month automatic extension | https://www.impuesto.aw/u-kunt-niet-op-tijd-aangifte-doen | 2026-11-14 |
| DIMP, U doet geen of niet op tijd aangifte: read for the reminder and the 5% penalty | https://www.impuesto.aw/u-doet-geen-of-niet-op-tijd-aangifte | 2026-11-14 |
| DIMP, U betaalt deels niet of niet op tijd: read for collection steps, costs and collection interest | https://www.impuesto.aw/u-betaalt-deels-niet-of-niet-op-tijd | 2026-11-14 |
| DIMP, Aangiftebiljet inkomstenbelasting aanvragen: read for registration and duplicate returns | https://www.impuesto.aw/aangiftebiljet-inkomstenbelasting-aanvragen | 2026-11-14 |
| DIMP, Hoeveel BBO en BAVP moet u betalen: read for the USD rate of Afl. 1.79 | https://www.impuesto.aw/hoeveel-bbo-en-bavp-moet-u-betalen | 2026-11-14 |

Not yet confirmed: deductions, personal charges and credits on the 2026 return; the collection interest rate; spousal allocation rules other than the AOV pension; the 2026 monthly wage tax tables (the annual table is shown; DIMP's calculator file was not opened).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `aw-individual-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/aw-individual-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
