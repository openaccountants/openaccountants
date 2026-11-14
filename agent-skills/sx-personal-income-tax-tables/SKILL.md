---
name: sx-personal-income-tax-tables
description: "Sint Maarten personal income tax for calendar year 2026 under AB 2026 no. 11 and its Annex I. Covers the nil-tax rule for taxable income up to Cg 27,281.28, the six marginal bands from 12.5% to 47.5%, the lookup-table method with the basic credit already deducted, the 2026 supplements (sole earner, child categories I to IV, elderly), worked examples from the annex, who must file, the two-month deadline after the invitation, the 36-month rule, postponement and the escalating late-filing fines. Applies to Dutch Sint Maarten, not French Saint-Martin. Trigger phrases include Sint Maarten income tax, inkomstenbelasting Sint Maarten, St. Maarten tax table 2026, basisaftrek, Inspectorate of Taxes Sint Maarten."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sx-personal-income-tax-tables"
  jurisdiction: "SX"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Sint Maarten: 2026 personal income tax tables v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar year 2026. Authority: the Inspectorate of Taxes, Sint Maarten Tax Administration (tax.sx). Amounts are Caribbean guilders (Cg or XCG). Dutch Sint Maarten (SX) and French Saint-Martin (MF) are separate jurisdictions.

## Who this applies to

- Every natural person who receives worldwide income must file an income tax return with the Inspectorate of Taxes ([Sint Maarten Tax Administration, FAQ](https://www.tax.sx/)).
- This skill computes tax on an **already determined taxable income**. It does not determine residence, income source, deductions or special treatment.
- [AB 2026 no. 11](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Regeling%20vaststelling%20inkomsten-%20en%20loonbelastingtabellen%202026.pdf), dated 16 March and published 18 March 2026, sets the 2026 income and wage tax tables: article 1 adopts Annex I for income tax, article 3 repeals the 2025 table regulation, article 4 gives retrospective effect to 1 January 2026, subject to the constitutional-review provisions it states.
- Wage tax withholding is in `sx-wage-tax-tables`; turnover tax in `sx-turnover-tax`.

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Nil-tax rule | no income tax if taxable income is Cg 27,281.28 or less | From 1 January 2026; otherwise the normal table applies | 2026 | [Annex I, AB 2026 no. 11](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20I%20TABEL%20INKOMSTENBELASTING%202026.pdf) |
| Band 1: 0 to 36,576 | 12.5% | Tax at the upper limit 4,571.95 (before credits) | 2026 | same |
| Band 2: over 36,576 to 54,864 | 20% | Tax at the lower limit 4,571.95 | 2026 | same |
| Band 3: over 54,864 to 76,200 | 26.25% | Tax at the lower limit 8,229.49 | 2026 | same |
| Band 4: over 76,200 to 114,297 | 33.75% | Tax at the lower limit 13,830.02 | 2026 | same |
| Band 5: over 114,297 to 161,540 | 40% | Tax at the lower limit 26,688.11 | 2026 | same |
| Band 6: over 161,540 | 47.5% | Tax at the lower limit 45,585.20 | 2026 | same |
| Basic credit (basisaftrek) | 2,381 | Already deducted in the lookup table | 2026 | same |
| Sole-earner supplement | 1,590 | Eligibility not set out in the annex | 2026 | same |
| Child supplement I, II, III, IV | 847, 420, 107, 86 | Category conditions not set out in the annex | 2026 | same |
| Elderly supplement; transferred | 1,199; 603 | Eligibility not set out in the annex | 2026 | same |
| Late-filing fines after a reminder | XCG 250, 500, 1,000, 1,500, 2,500 | First to fifth default | 2026 | [Sint Maarten Tax Administration, FAQ](https://www.tax.sx/) |

## The base

1. **Low-income rule first.** If taxable income is Cg 27,281.28 or less, tax is nil. Do not deduct 27,281.28 from everyone's income, and do not ignore the rule because the lookup table shows positive amounts below it: the row at Cg 27,248 shows Cg 1,025, but tax is nil there ([Annex I](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20I%20TABEL%20INKOMSTENBELASTING%202026.pdf)).
2. **Lookup method.** Take the tax printed in the table at the table income just below the taxable income and add the remainder times the listed percentage (same annex).
3. **Basic credit is already in the table.** The table is headed "Inclusief basiskorting" and starts at 19,048 with nil tax (2,381 / 12.5%). Do not deduct 2,381 again. Other supplements are still deducted, but tax never goes below nil (same annex).
4. **Do not rebuild the table from the bands.** The printed cumulative amounts carry cent differences that a formula on rounded thresholds would miss; for a return use the printed table (same annex).
5. **Supplements need eligibility evidence.** The annex lists amounts only; who qualifies and which child or elderly category applies come from the ordinance and the facts.

## Deadlines and filing

- File within two months of the invitation date, on the paper return form. If you cannot, request a postponement from the Inspector before the deadline, preferably by email to taxinfo@sintmaartengov.org with your name, CRIB number, the period and the reason ([Sint Maarten Tax Administration, FAQ](https://www.tax.sx/)).
- No invitation received: you must still file within 36 months from the return's due date (same page).
- CRIB number for individuals: the Personal CRIB Number Registration Form with a valid ID or passport and proof of address (census form under 6 months old or a recent utility bill) (same page).
- Payment by bank transfer to the Receiver's accounts at Windward Island Bank or RBC Royal Bank, in USD or XCG; refunds by the Tax Refund Form to Receivers.Admin@sintmaartengov.org (same page).

## Penalties and interest

After the deadline (including any approved extension) the Inspector sends a reminder. Not filing after the reminder brings a fine that rises with repeated defaults: XCG 250, 500, 1,000, 1,500 and 2,500 for the first to fifth default ([Sint Maarten Tax Administration, FAQ](https://www.tax.sx/)). Interest is not on the pages read.

## Cross-border points

- The table applies to Dutch Sint Maarten only; French Saint-Martin has its own tax code (see `skills/saint-martin/`).
- Non-resident taxation, treaties and the tax arrangement for the Kingdom are not covered: refer.

## Two worked examples that recompute

**Case 1: taxable income Cg 42,360 (Annex I example I).** Table tax at 42,348 is 3,345.40; remainder 12 at 20% = 2.40; total 3,347.80, with the basic credit already deducted. A check against the bands: 4,571.95 + 20% of (42,360 less 36,576) = 5,728.75, less the basic credit 2,381 = 3,347.75, five cents off the printed table, which is why the table is used.

```oa-check
name: Sint Maarten 2026 income tax, taxable income 42360
inputs:
  taxable_income: 42360
  table_row: 42348
  table_tax: 3345.40
steps:
  - remainder_tax: (taxable_income - table_row) * 0.20
  - total_tax: table_tax + remainder_tax
  - band_formula: 4571.95 + (taxable_income - 36576) * 0.20 - 2381
  - difference: total_tax - band_formula
expected:
  remainder_tax: 2.40
  total_tax: 3347.80
  band_formula: 3347.75
  difference: 0.05
```

**Case 2: taxable income Cg 169,958 (Annex I example II), and the nil-rule edge.** Table tax at 169,948 is 47,197.96; remainder 10 at 47.5% = 4.75; total 47,202.71. By contrast, someone with taxable income of 27,248 pays nil, not the 1,025 printed on that row, because 27,248 is not more than 27,281.28.

```oa-check
name: Sint Maarten 2026 income tax, taxable income 169958
inputs:
  taxable_income: 169958
  table_row: 169948
  table_tax: 47197.96
  nil_limit: 27281.28
  low_income: 27248
steps:
  - remainder_tax: (taxable_income - table_row) * 0.475
  - total_tax: table_tax + remainder_tax
  - low_income_headroom: nil_limit - low_income
expected:
  remainder_tax: 4.75
  total_tax: 47202.71
  low_income_headroom: 33.28
```

## Ask the client first

1. Do you live in Sint Maarten (Dutch side), and did you all year?
2. Taxable income for 2026, after the deductions you claim.
3. Married, and does your spouse earn income (sole-earner supplement)?
4. Children: ages and schooling (child categories).
5. Your age and your spouse's (elderly supplement).
6. Did you receive the invitation to file, and when?

## Sources

| Source | URL | Read on |
|---|---|---|
| AB 2026 no. 11, Regeling vaststelling inkomsten- en loonbelastingtabellen 2026: read for articles 1 to 4 (adoption of Annex I and II, repeal of the 2025 tables, retrospective entry into force) | https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Regeling%20vaststelling%20inkomsten-%20en%20loonbelastingtabellen%202026.pdf | 2026-11-14 |
| AB 2026 no. 11, Annex I (income tax table 2026): read for the instructions, both examples, the nil-tax rule, the band table, the supplements and the lookup rows at 19,048 and 27,248 | https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20I%20TABEL%20INKOMSTENBELASTING%202026.pdf | 2026-11-14 |
| Sint Maarten Tax Administration, home page FAQ: read for who must file, the two-month and 36-month rules, postponement, the escalating fines, CRIB registration, payment accounts and refunds | https://www.tax.sx/ | 2026-11-14 |

Not yet confirmed: the conditions for the sole-earner, child and elderly supplements; deductions and residence rules in the Landsverordening inkomstenbelasting; interest on late tax; whether the constitutional-review condition in article 4 was met.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sx-personal-income-tax-tables` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sx-personal-income-tax-tables. If neither is available, confirm every figure against the official source pages cited above before relying on it.
