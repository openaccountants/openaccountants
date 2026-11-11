---
name: ab-individual-return
description: "Alberta provincial personal income tax for an individual resident in Alberta on 31 December, worked through Form AB428 (Alberta Tax and Credits) on the T1 return. Primary tax year 2026, with a dated section carrying the full 2025 figures. Covers the six brackets (8%, 10%, 12%, 13%, 14%, 15%) including the 8% bracket added from 2025, the Alberta basic personal amount and the main non-refundable credits, the 8% credit rate, the Alberta supplemental tax credit, donations, medical expenses, the dividend tax credit, political contributions, minimum tax and indexing. Trigger on 'Alberta tax', 'AB428', 'Alberta tax brackets', 'Alberta 8% bracket', 'Alberta basic personal amount', 'Alberta supplemental tax credit', 'line 42800 Alberta'. Out of scope: federal tax (ca-fed-t1-return), CPP and EI (ca-fed-cpp-ei), instalments (ca-fed-instalments), self-employed expenses (ca-ab-deductions-for-self-employed-independent-contractor), emigrating (ca-ab-departure-tax-t1244-security-election-defer), compa"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ab-individual-return"
  jurisdiction: "CA-AB"
  tax_year: "2026"
  last_updated: "2026-11-08"
---

# Alberta personal income tax (Form AB428), tax year 2026, with 2025 figures

> **Built from the law.** Drafted from the Alberta Personal Income Tax Act (RSA 2000 c A-30, consolidation current as of 11 December 2025), the CRA's 2025 Form AB428 and Worksheet AB428, the CRA's 2026 and 2025 tax rate pages, the CRA's 2026 TD1AB, the CRA's July 2026 payroll formulas (T4127), Alberta's Budget 2026 Fiscal Plan and the Fiscal Measures Statutes Amendment Act, 2026, all read on 2026-11-08. Not yet approved by an accountant. Do not file from it without review by a qualified Canadian professional.

Built by Michael Cutajar and the OpenAccountants team.

Tax year: the calendar year. Currency: Canadian dollars. Alberta sets the law. The Canada Revenue Agency (CRA) runs it on the federal T1 return. The result goes on line 42800 of the return (2025 Form AB428, line 75).

Old figures to drop: Alberta no longer has a single flat 10% rate. From the 2025 tax year the first band is taxed at 8%, and credits are worked out at 8% (Act s.4).

See also: `ca-fed-t1-return` (federal tax and the federal credits), `ca-fed-cpp-ei`, `ca-fed-instalments`, `ca-capital-gains`, `ca-tax-residency`, `ca-ab-deductions-for-self-employed-independent-contractor`, `ca-ab-departure-tax-t1244-security-election-defer`, `ab-corporate-tax`.

## Who this applies to

**Residents on 31 December.** An individual who was resident in Alberta on the last day of the calendar year must pay Alberta tax (Act s.3(1)(a)). The tax is worked out on the whole year's taxable income (s.6.1(1)). So the province you live in on 31 December decides the provincial tax for the year, even if you moved in during the year. Use `ca-tax-residency` for the residential ties test.

**Alberta residents with business income outside Alberta.** The Alberta tax is reduced to T x (C - D) / C, where T is the normal Alberta tax, C is income for the year and D is the business income earned outside Alberta (s.6.1(3)).

**Residents of another province with Alberta business income.** An individual resident in another province or territory on 31 December who had business income in Alberta must also pay Alberta tax (s.3(1)(b)). The tax is the full Alberta tax multiplied by the Alberta share: T x C / D, where C is the Alberta business income and D is income for the year (s.6.1(4)).

**Part-year residents who leave Canada.** An individual resident in Alberta for part of the year, who did not live in another province after leaving Alberta, and who was resident outside Canada on the last day of the year, is taxed under s.6.1(5). Part-year credit limits are in s.36.1 and the emigrant proration in s.40. Use `ca-ab-departure-tax-t1244-security-election-defer` for departure tax.

**Non-residents of Canada with Canadian income** are caught by s.3(1)(c). This skill does not work that case through.

**Not here:** the federal calculation (`ca-fed-t1-return`), companies (`ab-corporate-tax`), and trusts. A trust taxed under s.122 of the federal Act pays the top Alberta rate on all its taxable income (s.6.1(1)(b)).

## Rates, bands and thresholds

Alberta taxable income is the same as federal taxable income (s.5(1)), line 26000 of the return.

**Tax year 2026.** Bands from the CRA's 2026 rate page. Credit amounts from the CRA's 2026 TD1AB. Alberta says: "In 2026, thresholds and credit amounts will rise by 2%."

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Taxable income up to $61,200 | 8% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| $61,200.01 to $154,259 | 10% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| $154,259.01 to $185,111 | 12% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| $185,111.01 to $246,813 | 13% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| $246,813.01 to $370,220 | 14% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Over $370,220 | 15% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Rate used for non-refundable credits ("specified percentage") | 8% | 2025 and later | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.4) |
| Alberta indexing factor | 2.0% | 2026 | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html (Table 8.2, index rate) |
| Basic personal amount | $22,769 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Spouse or common-law partner amount, and eligible dependant amount | $22,769 minus the spouse's or dependant's net income | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Age amount (65 or older on 31 December) | $6,345, reduced when net income is over $47,234, nil at $89,534 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Pension income amount | Up to $1,753 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Disability amount | $17,563 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Caregiver amount | Up to $13,180; full if the dependant's net income is $20,956 or less, nil at $34,136 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Amount for infirm dependants 18 or older | Up to $13,180; full if the dependant's net income is $8,707 or less, nil at $21,887 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf |
| Disability supplement for a person under 18 | Up to $13,180 | 2026 | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf (Tax Plan, Non-Refundable Tax Credits table, printed page 130) |
| Adoption expenses | Up to $19,741 | 2026 | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf (Tax Plan, Non-Refundable Tax Credits table, printed page 130) |
| Donations: first $200, then the rest | 60%, then 21% (not indexed) | 2025 and 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.11(1)) |
| Political contributions credit | 75% of the first $200, 50% of the next $900, 33.33% of the rest, at most $1,000 (fixed in the Act, not indexed) | 2025 and 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.24(2.1)) |
| Minimum tax carryover | 35% of the federal minimum tax carryover | 2025 and 2026 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.27(1)) |

Alberta's Budget 2026 Fiscal Plan says "Credit amounts have increased by 2% from 2025 due to the Alberta escalator." Three 2026 amounts are not printed by the CRA or Alberta yet, because the 2026 Form AB428 comes out with the 2026 tax package. The Act sets each one as the 2025 figure plus the Alberta escalator, rounded to the nearest dollar (s.44.2(1) and (4)). At 2% they work out as below. Check them against the 2026 AB428 when it is out:

- medical expense threshold: the lesser of $2,942 (2025: $2,884) and 3% of net income;
- supplemental tax credit base: $4,896 (2025: $4,800);
- child care and attendant care threshold for the under-18 disability supplement: $3,594 (2025: $3,524).

The method is backed up by the TD1AB: its 2026 basic personal amount ($22,769), age amount ($6,345 and $47,234) and pension amount ($1,753) are each the 2025 figure times 1.02, rounded.

**Tax year 2025.** From the CRA's 2025 rate page, 2025 Form AB428 and 2025 Worksheet AB428.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Taxable income up to $60,000 | 8% | 2025 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html |
| $60,000.01 to $151,234 | 10% (AB428 adds $4,800 for the first band) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| $151,234.01 to $181,481 | 12% (plus $13,923.40) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| $181,481.01 to $241,974 | 13% (plus $17,553.04) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| $241,974.01 to $362,961 | 14% (plus $25,417.13) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Over $362,961 | 15% (plus $42,355.31) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Non-refundable credit rate | 8% (AB428 line 53) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Basic personal amount | $22,323 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Spouse or common-law partner amount, and eligible dependant amount | $22,323 minus that person's net income | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Age amount (born in 1960 or earlier) | $6,221, reduced by 15% of net income over $46,308, nil at $87,782 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Pension income amount | Up to $1,719 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Disability amount for self | $17,219; under 18, a supplement of up to $12,922 less child and attendant care over $3,524, total at most $30,141 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Caregiver amount | $33,467 minus the dependant's net income, at most $12,922 per dependant | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Amount for infirm dependants 18 or older | $21,458 minus the dependant's net income, at most $12,922 per dependant | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Medical expenses | Expenses over the lesser of $2,884 and 3% of net income | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |
| Adoption expenses | Up to $19,354 | 2025 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf (s.13.1(2)) |
| Supplemental tax credit | 25% of (credits at 8%, leaving out unused tuition, minus $4,800) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Dividend tax credit | 8.12% of the taxable amount of eligible dividends; 2.18% of the taxable amount of other dividends | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt |
| Minimum tax: carryover and additional tax | 35% of the federal amount (AB428 lines 64 and 67) | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt |

**The supplemental tax credit.** Credits are worked out at 8%, but the 8% band only covers the first $60,000 of income (2025). The Act gives back a quarter of the credit value above $4,800: (A - $4,800) x 0.25, where A is the credits under ss.8 to 10, 12 to 13.1, 18, 19 and 20.1 (s.20.2). Donations (s.11) and unused tuition (s.17) are not in A. The AB428 worksheet takes line 58800 less line 58560, times 8%, less $4,800, times 25%. The effect is an extra 2% on credit amounts above $60,000 (2025) or $61,200 (2026). So a large credit claim is worth 10% on the part above that level, as it was before 2025.

**The dividend credit in 2026.** The Act sets the Alberta credit as a fraction of the federal gross-up, 149/890 and 227/770, "for the 2021 and subsequent taxation years" (s.21). The 2025 worksheet turns these into 2.18% and 8.12% of the taxable amount. Those percentages hold for 2026 only if the federal gross-up rates are unchanged: see `ca-fed-t1-return`.

**Political contributions in 2026.** The dollar amounts are written into s.24(2.1) of the Act ($200, $1,100, $600, $1,000) and s.24 is not in the list of indexed provisions (s.44.2(1)), so the 2025 limits apply unchanged in 2026.

**Caregiver credits from 2027.** The Fiscal Measures Statutes Amendment Act, 2026 (SA 2026 c3, s.2) replaces the caregiver amount and the amount for infirm dependants 18 or older with one Alberta caregiver credit of $13,180 less the dependant's income over $20,956, which can also be claimed for an infirm spouse. It "comes into force on January 1, 2027", so it does not change 2026 returns; the 2027 amounts are indexed (new s.44.2(1.01)).

## The taxable base

1. **Start from line 26000.** Alberta uses federal taxable income (s.5(1)). Every federal deduction (RRSP, child care, business losses, the capital gains inclusion, the capital gains deduction) flows through. Federal rules live in `ca-fed-t1-return` and `ca-capital-gains`. Self-employed CPP is in `ca-fed-cpp-ei`. AB428 has no deductions of its own at this step.
2. **Part A: tax on taxable income.** Pick the band and apply the AB428 column: (taxable income - band floor) x band rate, plus the fixed amount for the bands below. For 2026 the fixed amounts are $4,896 at $61,200 (8% x $61,200), $14,201.90 at $154,259, $17,904.14 at $185,111, $25,925.40 at $246,813 and $43,202.38 at $370,220. These are worked from the CRA's 2026 bands. They agree with the CRA payroll constants (KP 0, 1,224, 4,309, 6,160, 8,628, 12,331).
3. **Tax on split income.** Add Alberta tax on split income from Form T1206 (2025 AB428 line 60).
4. **Part B: non-refundable credits.** Add up the credit amounts: basic personal amount, age, spouse or eligible dependant, infirm dependants, CPP and EI (lines 30800, 31000, 31200 and 31217 of the return), adoption, pension, caregiver, disability for self and transferred from a dependant, student loan interest, unused tuition carried forward, transfers from a spouse, and medical expenses. Multiply the total by 8%. Then add donations: 60% of the first $200 and 21% of the rest. AB428 has no line for the Canada employment amount. Alberta's tuition line is only for unused amounts carried forward (line 58560, Schedule AB(S11)).
5. **Part C: reduce the tax.** From the Part A tax plus split-income tax, subtract the non-refundable credits, the dividend tax credit and the minimum tax carryover (35% of federal line 40427). The result cannot go below zero. Add Alberta additional tax for minimum tax purposes (35% of the federal amount from Form T691). Subtract the provincial foreign tax credit (Form T2036), the political contributions credit and the supplemental tax credit, each step not going below zero. The result is Alberta tax on line 42800.
6. **Other items.** An unused Alberta stock savings plan credit is claimed on Form T89. The Alberta child and family benefit (Act s.30.2) is a separate payment, not claimed on AB428. Alberta says it "is distributed quarterly with payments in August, November, February and May." The Fiscal Plan gives these yearly maximums (base component, then working component; the working component phases in on family working income, and both phase out on family net income above the threshold):

| Benefit year | 1 child | 2 children | 3 children | 4 or more | Phase-out threshold | Source URL |
|---|---|---|---|---|---|---|
| July 2025 to June 2026 | $1,499 / $767 | $2,248 / $1,465 | $2,997 / $1,883 | $3,746 / $2,021 | $27,565 / $46,191 | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf (printed page 130) |
| July 2026 to June 2027 | $1,529 / $782 | $2,293 / $1,494 | $3,057 / $1,920 | $3,821 / $2,061 | $28,116 / $47,115 | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf (printed page 130) |

   Alberta has no provincial sales tax and no payroll tax in 2026: the Fiscal Plan's Major Provincial Tax Rates, 2026 table shows "-" for Alberta on both rows (https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf, printed page 132). GST is federal: see `canada-gst-hst`.

## Deadlines and filing

AB428 is filed with the federal T1 return. There is no separate Alberta return and no separate Alberta deadline. The CRA dates for the 2025 return:

- **30 April 2026**: deadline to file and to pay.
- **15 June 2026**: deadline to file if you or your spouse or common-law partner are self-employed. Payment is still due 30 April 2026.

For the 2026 return the same rule gives 30 April 2027 and 15 June 2027, but the CRA has not yet published those dates. Instalments are federal rules covering federal and Alberta tax together: see `ca-fed-instalments`.

## Penalties and interest

Alberta tax is assessed and collected with federal tax, so the federal penalties apply to the combined balance (CRA, 2025 return):

- **Late filing:** 5% of the balance owing, plus 1% for each full month late, up to 12 months.
- **Repeated late filing:** if you were penalized in 2022, 2023 or 2024 and received a demand to file, 10% of the balance owing plus 2% for each full month late, up to 20 months.
- **Interest:** "the CRA charges compound daily interest starting the day after the due date." The rate can change every three months, so take it from the CRA's prescribed interest rate page.

## Cross-border points

- **Moving between provinces:** only the province of residence on 31 December taxes the year, apart from the business income split in s.6.1(3) and (4). Ask where the client lived on 31 December, not where the money was earned.
- **Foreign income of an Alberta resident:** taxed as part of taxable income. Foreign tax not used against federal tax can be claimed against Alberta tax as the provincial foreign tax credit on Form T2036 (s.23, 2025 AB428 line 69).
- **Overseas employment tax credit:** Alberta allows 35% of the federal s.122.3 deduction (s.22).
- **Leaving Canada:** Alberta tax still applies for the part of the year before departure (s.3(1), s.6.1(5)), with credits prorated for emigrants (s.40). The departure return and the T1244 deferral are in `ca-ab-departure-tax-t1244-security-election-defer`.
- **Arriving in Canada:** credits are restricted for part-year residents (s.36.1). Use `ca-tax-residency` for the arrival date.

## Worked examples

**Example 1. Employee, single, 2026.** Priya lives in Calgary all year. Her taxable income (line 26000) is $75,000. Her return shows CPP of $3,400 on line 30800 and EI of $1,000 on line 31200. She claims no other credits. Part A: $75,000 is in the second band, so ($75,000 - $61,200) x 10% = $1,380, plus $4,896 for the first band, gives $6,276.00. Part B: $22,769 + $3,400 + $1,000 = $27,169, times 8% = $2,173.52. The supplemental credit is nil, because $2,173.52 is below the $4,896 base. Alberta tax on line 42800 is $6,276.00 - $2,173.52 = $4,102.48.

```oa-check
name: Alberta 2026, employee, taxable income 75,000
inputs:
  taxable_income: 75000
  cpp_30800: 3400
  ei_31200: 1000
  bpa: 22769
steps:
  - part_a_tax: (taxable_income - 61200) * 0.10 + 4896
  - credit_amounts: bpa + cpp_30800 + ei_31200
  - credits: round(credit_amounts * 0.08, 2)
  - supplemental: max((credits - 4896) * 0.25, 0)
  - alberta_tax: max(max(part_a_tax - credits, 0) - supplemental, 0)
expected:
  part_a_tax: 6276.00
  credit_amounts: 27169
  credits: 2173.52
  supplemental: 0
  alberta_tax: 4102.48
```

**Example 2. One earner with a spouse and a disability, 2025 (the supplemental credit applies).** Marc lived in Edmonton on 31 December 2025. His taxable income is $120,000. His spouse's net income (line 23600) is $3,000. Marc has an approved disability tax credit certificate. His return shows CPP of $3,100 on line 30800 and EI of $1,000 on line 31200. Part A: ($120,000 - $60,000) x 10% + $4,800 = $10,800.00. Part B: basic personal amount $22,323, spouse amount $22,323 - $3,000 = $19,323, CPP $3,100, EI $1,000, disability $17,219. The total on line 58800 is $62,965, times 8% = $5,037.20. Supplemental credit: ($5,037.20 - $4,800) x 25% = $59.30. That is 2% of the $2,965 by which his credit amounts exceed $60,000. Alberta tax: $10,800.00 - $5,037.20 - $59.30 = $5,703.50.

```oa-check
name: Alberta 2025, one earner, spouse amount, disability, supplemental credit
inputs:
  taxable_income: 120000
  spouse_net_income: 3000
  cpp_30800: 3100
  ei_31200: 1000
  bpa: 22323
  disability: 17219
steps:
  - part_a_tax: (taxable_income - 60000) * 0.10 + 4800
  - spouse_amount: max(bpa - spouse_net_income, 0)
  - line_58800: bpa + spouse_amount + cpp_30800 + ei_31200 + disability
  - credits: round(line_58800 * 0.08, 2)
  - supplemental: max((credits - 4800) * 0.25, 0)
  - check_two_percent: (line_58800 - 60000) * 0.02
  - alberta_tax: max(max(part_a_tax - credits, 0) - supplemental, 0)
expected:
  part_a_tax: 10800.00
  spouse_amount: 19323
  line_58800: 62965
  credits: 5037.20
  supplemental: 59.30
  check_two_percent: 59.30
  alberta_tax: 5703.50
```

## Ask the client first

1. Where did you live on 31 December of the year? If you moved during the year, when and from where? If unknown, do not work out provincial tax.
2. Did you have business income earned outside Alberta (or, if you live in another province, inside Alberta)?
3. Your taxable income (line 26000) and net income (line 23600), and your spouse's or dependant's net income. If marital status is unknown, assume single and claim no spouse amount.
4. Your age on 31 December, any pension income, and whether a T2201 disability certificate is approved for you or a dependant.
5. Medical expenses, donations, Alberta political contributions, and any unused Alberta tuition carried forward (Schedule AB(S11)).
6. Did you leave or enter Canada in the year, and did you pay foreign tax?

## Sources

| Source | URL | Read on |
|---|---|---|
| Alberta Personal Income Tax Act, RSA 2000 c A-30, consolidation current as of 11 December 2025 (Alberta King's Printer): ss.3, 4, 5, 6.1, 11, 12, 13.1, 20.2, 21, 22, 23, 24, 27, 30.2, 36.1, 40, 44.2 | https://kings-printer.alberta.ca/documents/Acts/A30.pdf | 2026-11-08 |
| CRA, 2025 Form AB428 Alberta Tax and Credits (5009-C), e-text, Parts A, B and C read for bands, credit lines and the 8% rate | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-c/5009-c-25e.txt | 2026-11-08 |
| CRA, 2025 Worksheet AB428 (5009-D), e-text, read for age, caregiver, infirm dependant, disability, dividend, political contribution and supplemental credit lines | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-25e.txt | 2026-11-08 |
| CRA, Current year tax rates and income brackets (2026), read for the Alberta rate table | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-08 |
| CRA, Last year tax rates and income brackets (2025), read for the Alberta rate table and footnote 2 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html | 2026-11-08 |
| CRA, TD1AB 2026 Alberta Personal Tax Credits Return, lines 1 to 8 read for 2026 credit amounts | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-26e.pdf | 2026-11-08 |
| CRA, T4127 Payroll Deductions Formulas, 123rd edition, effective 1 July 2026, read for Tables 8.1 and 8.2 (Alberta) | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html | 2026-11-08 |
| Government of Alberta, Personal income tax, read for the overview, Table 1 and the child and family benefit | https://www.alberta.ca/personal-income-tax | 2026-11-08 |
| CRA, Due dates and payment dates (individuals), read for the 2025 filing and payment dates | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-08 |
| CRA, Interest and penalties on late taxes, read for the late-filing penalty and interest | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html | 2026-11-08 |
| Government of Alberta, Budget 2026 Fiscal Plan 2026-29, Tax Plan, read for the Non-Refundable Tax Credits and Alberta Child and Family Benefit tables (printed page 130), the Major Provincial Tax Rates, 2026 table (page 132) and the new Alberta caregiver credit (page 123) | https://open.alberta.ca/dataset/3393a7b5-07bf-4b9f-8aaf-a6d89273297b/resource/58a8d024-398f-482e-b1c2-81a754a97253/download/budget-2026-fiscal-plan-2026-29.pdf | 2026-11-08 |
| Fiscal Measures Statutes Amendment Act, 2026, SA 2026 c3, s.2 (not in force provisions, current as of 30 June 2026) | https://kings-printer.alberta.ca/documents/Acts/2026ch03_unpr.pdf | 2026-11-08 |

Not yet confirmed: the 2026 Form AB428 and Worksheet AB428 are not published yet, so these 2026 figures are worked out from the Act's indexing at 2% and not read from a CRA or Alberta form: the medical threshold of $2,942, the supplemental credit base of $4,896, the $3,594 care threshold for the under-18 disability supplement, and the band fixed amounts in Part A (arithmetic on the CRA's 2026 bands); the 2026 dividend credit percentages (they depend on unchanged federal gross-ups); the 2026 return due dates (30 April and 15 June 2027) until the CRA publishes them; the CRA's prescribed interest rate; the Alberta child and family benefit phase-out rates (not set out here); whether the federal Canada Carbon Rebate still applies (a federal matter, not checked); the old skill's Alberta royalty tax credit, small farm tax credit and Alberta SR&ED top-up (no AB428 line for individuals found; business items belong in `ab-corporate-tax`); the Alberta Climate Leadership Adjustment Rebate (the Act keeps only a transitional s.35.4, not checked further); and combined federal and Alberta marginal rates, including on dividends (they depend on federal figures; see `ca-fed-t1-return`).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-08. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ab-individual-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ab-individual-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
