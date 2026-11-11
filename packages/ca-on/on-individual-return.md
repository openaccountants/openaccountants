---
name: on-individual-return
description: 'Ontario personal income tax on Form ON428 for an individual resident in Ontario on 31 December, for tax year 2026, with the full 2025 figures kept for 2025 returns still being filed or amended. Covers the five Ontario brackets, the basic personal amount and the main non-refundable credits at 5.05%, the Ontario surtax, the Ontario tax reduction, the LIFT credit for low earners, the dividend tax credit, and the Ontario Health Premium chart step by step. Applies to employees, the self-employed and retirees. Trigger on "Ontario tax", "ON428", "Ontario income tax", "Ontario surtax", "Ontario Health Premium", "OHP", "Ontario tax reduction", "LIFT credit", "Ontario basic personal amount", "Ontario tax brackets 2026". Out of scope: Ontario refundable credits and the Trillium Benefit (on-tax-credits), Employer Health Tax (on-eht), the federal T1 (ca-fed-t1-return), CPP and EI (ca-fed-cpp-ei), residency (ca-tax-residency), corporations and trusts.'
version: 2.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-08
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Ontario personal income tax (Form ON428), 2026 and 2025

## Who this applies to

- An individual who is resident in Ontario on the last day of the tax year (31 December, or the date of death, or the date they left Canada). Ontario taxes their taxable income from line 26000 of the federal return. Taxation Act, 2007, s. 4(1), paragraphs 1 and 2.
- A non-resident of Canada for the year completes ON428 if they earned employment income only in Ontario, or business income from a permanent establishment only in Ontario (CRA, Ontario tax information 2025, "Who should complete Form ON428").
- The tax is on the same T1 return as the federal tax, and CRA administers it. The result on ON428 line 90 goes on line 42800 of the return.
- It covers employees, the self-employed and retirees alike. The income type changes only the inputs: business income comes from ca-fed-t2125, CPP and EI amounts from ca-fed-cpp-ei.
- Not covered here:
  - Someone resident in another province on 31 December. Use that province's skill. The province on 31 December decides, even if the person lived in Ontario for most of the year.
  - Corporations and trusts. A trust pays no Ontario Health Premium (s. 24(3)) and has its own rates.
  - Ontario refundable credits on ON479, the Ontario Trillium Benefit (OEPTC, OSTC, NOEC) and the CARE credit. See on-tax-credits.
  - Employer Health Tax. See on-eht.
- Status Indians: Ontario says a person with a Certificate of Indian Status pays the health premium if their taxable income for the year was earned off-reserve and is more than $20,000. Refer any mix of on-reserve and off-reserve income to an accountant.

## Rates, bands and thresholds

Ontario tax on taxable income (ON428 Part A). Each rate applies only to the slice inside the band.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Band 1: taxable income up to $53,891 | 5.05% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 2: $53,891.01 to $107,785 | 9.15% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 3: $107,785.01 to $150,000 | 11.16% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 4: $150,000.01 to $220,000 | 12.16% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 5: over $220,000 | 13.16% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Band 1: taxable income up to $52,886 | 5.05% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Band 2: $52,886.01 to $105,775 (tax on lower bands $2,670.74) | 9.15% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Band 3: $105,775.01 to $150,000 (tax on lower bands $7,510.09) | 11.16% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Band 4: $150,000.01 to $220,000 (tax on lower bands $12,445.60) | 12.16% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Band 5: over $220,000 (tax on lower bands $20,957.60) | 13.16% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Indexation rate for Ontario amounts | 1.9% (2026), 2.8% (2025) | 2026, 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jan/t4127-01-26e.pdf |
| Non-refundable credit rate (all Part B amounts, CPP and EI included) | 5.05% | 2026, 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Basic personal amount | $12,989 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on/td1on-26e.pdf |
| Basic personal amount | $12,747 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Spouse or common-law partner amount, and eligible dependant amount | base $12,132 less the other person's net income, maximum $11,029 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on-ws/td1on-ws-26e.pdf |
| Spouse or common-law partner amount, and eligible dependant amount | base $11,905 less the other person's net income, maximum $10,823 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Age amount (65 or older on 31 December) | maximum $6,342, reduced by 15% of net income over $47,210, nil from $89,490 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on-ws/td1on-ws-26e.pdf |
| Age amount (born in 1960 or earlier) | maximum $6,223, reduced by 15% of net income over $46,330, nil from $87,817 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf |
| Pension income amount | maximum $1,796 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on/td1on-26e.pdf |
| Pension income amount | maximum $1,762 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Disability amount for self | $10,494 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on/td1on-26e.pdf |
| Disability amount for self | $10,298 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Ontario caregiver amount, per dependant | base $27,066 less the dependant's net income, maximum $6,122 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on-ws/td1on-ws-26e.pdf |
| Ontario caregiver amount, per dependant | base $26,562 less the dependant's net income, maximum $6,008 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf |
| Medical expenses: part not claimable | lesser of 3% of net income and $2,885 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Donations and gifts credit | 5.05% on the first $200, 11.16% on the rest | 2026, 2025 | https://www.ontario.ca/laws/statute/07t11 |
| Dividend tax credit (share of the taxable amount of dividends) | eligible 10%, other than eligible 2.9863% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf |
| Dividend tax credit (share of the federal gross-up) | eligible 36.3158%; other than eligible 22.895% to 2026, 15.2283% from 2027 | 2026 | https://www.ontario.ca/laws/statute/07t11 |
| Ontario surtax | 20% of basic Ontario tax over $5,818, plus 36% of basic Ontario tax over $7,446 | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jan/t4127-01-26e.pdf |
| Ontario surtax | 20% of basic Ontario tax over $5,710, plus 36% of basic Ontario tax over $7,307 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Ontario tax reduction | basic $300, plus $554 for each dependent child born in 2008 or later (under 18 at any time in 2026, s. 20(3)) and each dependant with an impairment; reduction is twice that total minus Ontario tax | 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jan/t4127-01-26e.pdf |
| Ontario tax reduction | basic $294, plus $544 for each dependent child born in 2007 or later and each dependant with an impairment | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| LIFT credit | lesser of $875 and 5.05% of employment income, less 5% of the greater of adjusted net income over $32,500 and adjusted family net income over $65,000 | 2026, 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-a/5006-a-25e.pdf |
| LIFT credit: income at which it reaches nil | individual adjusted net income $50,000, family $82,500 | 2026, 2025 | https://www.ontario.ca/page/low-income-individuals-and-families-tax-credit |
| Community food program donation credit for farmers | 25% of qualifying donations | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| Ontario Health Premium | chart below; not indexed, same for 2025 and 2026 | 2026, 2025 | https://www.ontario.ca/laws/statute/07t11 |

What is indexed and what is not. Taxation Act s. 23(1) indexes the first two bracket limits, the third bracket limit except the $150,000, the credit amounts in s. 9, the surtax thresholds in s. 16 and the tax reduction amounts in s. 20(4) and (5). So $150,000 and $220,000 stay fixed and the surtax thresholds move every year. The LIFT figures (s. 21.1) and the Health Premium (s. 24) are not on the list and stay fixed.

Tax on the lower bands for 2026, computed from the CRA brackets the way ON428 line 7 shows it: $2,721.50 at $53,891, $7,652.80 at $107,785, $12,363.99 at $150,000, $20,875.99 at $220,000. The 2026 ON428 is not published yet, so check these against it when it comes out.

### Ontario Health Premium chart (ON428, line 89)

Based on taxable income from line 26000. The 2025 ON428 prints these steps. Taxation Act s. 24(2) sets the same steps in law with no indexing, so they apply to 2026 too.

| Taxable income | Ontario Health Premium | Source URL |
|---|---|---|
| $20,000 or less | $0 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $20,000, not more than $25,000 | 6% of the amount over $20,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $25,000, not more than $36,000 | $300 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $36,000, not more than $38,500 | $300 plus 6% of the amount over $36,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $38,500, not more than $48,000 | $450 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $48,000, not more than $48,600 | $450 plus 25% of the amount over $48,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $48,600, not more than $72,000 | $600 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $72,000, not more than $72,600 | $600 plus 25% of the amount over $72,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $72,600, not more than $200,000 | $750 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $200,000, not more than $200,600 | $750 plus 25% of the amount over $200,000 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |
| more than $200,600 | $900 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf |

The same steps are in the law: https://www.ontario.ca/laws/statute/07t11 (s. 24(2)).

## The taxable base

Ontario starts from the finished federal return: complete steps 1 to 5 of the T1 first, then ON428 (CRA, Ontario tax information 2025). The order of ON428 is the method.

1. **Part A, tax on taxable income (line 8).** Take line 26000. Find the band, take the amount over the band floor, multiply by the band rate, round to the cent, add the tax on the lower bands.
2. **Part B, non-refundable credits (line 50).** Add the Ontario amounts that apply: basic personal amount, age, spouse or eligible dependant, caregiver, CPP or QPP contributions (lines 30800 and 31000), EI premiums (lines 31200 and 31217), adoption, pension, disability, interest on student loans, unused tuition and education amounts carried forward (Schedule ON(S11)), amounts transferred from a spouse (Schedule ON(S2)), and medical expenses over the threshold. Multiply the total by 5.05%. Add the donations credit: 5.05% on the first $200 and 11.16% on the rest.
   - Ontario amounts differ from the federal ones. Never copy a federal amount across. The eligibility rules are mostly the same as federal; the amounts are Ontario's (CRA, Ontario tax information 2025).
   - If a federal claim was reduced, for example for a newcomer or an emigrant, reduce the matching Ontario claim the same way.
3. **Basic Ontario tax (lines 53 to 61).** Line 8 minus line 50, not below zero. Add Ontario tax on split income from Form T1206 (line 54). Deduct any Ontario minimum tax carryover (line 60).
4. **Surtax (lines 63 to 68).** Take line 62 minus the tax on split income. If that is more than the first threshold, the surtax is 20% of the excess over the first threshold plus 36% of the excess over the second. Surtax is worked on Ontario tax after the non-refundable credits, but before the dividend tax credit, the tax reduction and LIFT.
5. **Dividend tax credit (line 70).** Deduct it after the surtax.
6. **Ontario tax reduction (lines 74 to 80).** Personal amount = basic reduction plus the per-dependant amount for each dependent child who was under 18 at any time in the year (born in 2008 or later for 2026, in 2007 or later for 2025; s. 20(3)) and each dependant with an impairment. Reduction = twice the personal amount minus line 73, not below zero. It is nil if the person was not resident in Canada at the start of the year, not resident in Ontario on 31 December, had Ontario additional tax for minimum tax purposes, or was bankrupt in the year. With a spouse or common-law partner on 31 December, only the one with the higher net income claims the dependant amounts (ON428 lines 75 and 76; s. 20(2)).
7. **Provincial foreign tax credit (line 82)** from Form T2036, for foreign non-business income tax not fully used federally (s. 21).
8. **LIFT credit (line 85)** from Schedule ON428-A. Start with the lesser of $875 and 5.05% of employment income (lines 10100 and 10400). Reduce it by 5% of the greater of (a) adjusted net income over $32,500 and (b) adjusted family net income over $65,000. Single people use only (a). It reduces Ontario tax but never the Health Premium, and it is non-refundable, so any part not used is lost.
9. **Community food program donation credit for farmers (line 87)**: 25% of qualifying donations that were also claimed as charitable gifts.
10. **Ontario Health Premium (line 89)** from the chart, on taxable income. Since 2024 the law adds split income taxed under s. 12.1 to taxable income for this test (s. 24(0.1)). No credit, reduction or LIFT reduces the premium.
11. **Line 90** = line 88 plus line 89. Enter it on line 42800 of the return.

Rounding: work each ON428 line to the cent. The surtax is worked on basic Ontario tax, not on taxable income. The premium is worked on taxable income, not on tax.

## Deadlines and filing

- Ontario tax is filed on the federal T1 return to CRA, with Form ON428 (and Schedule ON428-A for LIFT). There is no separate Ontario return. Ontario's own page tells the self-employed to pay the health premium as part of the return by completing ON428.
- 2025 return: file by April 30, 2026, or by June 15, 2026 if the person or their spouse or common-law partner is self-employed. Any balance owing was due April 30, 2026 in both cases.
- 2026 return: the same rule applies, April 30 for most people and June 15 for the self-employed, with payment due April 30.
- Employers deduct Ontario tax and the Health Premium from pay (T4127, Form TD1ON). For self-employed instalments see ca-fed-instalments. For filing channels and the federal return itself see ca-fed-t1-return.

## Penalties and interest

These are federal rules. CRA applies them to the whole balance owing on the T1, Ontario tax included.

- Late filing with a balance owing: 5% of the balance owing, plus 1% of the balance for each full month late, up to 12 months.
- Repeat late filing: 10% of the balance owing, plus 2% for each full month late, up to 20 months, if a late-filing penalty was charged in any of the three previous years and CRA sent a demand to file.
- Interest: compound daily interest on any unpaid amount from the day after the due date, reassessed amounts included, at CRA's prescribed rate, which can change every three months.

## Cross-border points

- **Residence on 31 December decides.** Someone who moved into Ontario during the year pays Ontario tax for the whole year. Someone who moved out pays the new province's tax. For how residence is decided see ca-tax-residency.
- **Newcomers and emigrants.** A person who arrived in or left Canada during the year may have to reduce some Ontario credits, the same way as the federal claims. A newcomer arriving on January 1, or an emigrant leaving on December 31, may still claim the tax reduction and LIFT if resident in Ontario on December 31 and the other conditions are met (CRA, Ontario tax information 2025). Departure tax: see leaving-canada-departure-tax.
- **Business in more than one province.** An Ontario resident with business income from a permanent establishment outside Ontario pays Ontario tax only on the Ontario share, using the Ontario allocation factor from Form T2203 (Taxation Act s. 6(2)). The surtax and the basic tax reduction are scaled by the same factor (s. 16(4), s. 20(4)). Flag for an accountant.
- **Non-residents with Ontario income.** A non-resident of Canada with employment income only in Ontario, or business income from a permanent establishment only in Ontario, uses ON428 (s. 4(1) para. 3). The Health Premium applies only to Ontario residents: s. 24(1) charges it on the people in paragraphs 1 and 2 of s. 4(1), not paragraph 3.
- **Foreign tax.** Foreign non-business income tax not fully credited against federal tax may give a provincial foreign tax credit on Form T2036 (s. 21).

## Worked examples

### Example 1: 2026, single employee on a low income (tax reduction, LIFT and the Health Premium)

Amira is 30, single, with no dependants, and lives in Toronto all of 2026. Her only income is employment income of $34,000. Her T4 shows base CPP contributions of $1,509.75 (line 30800) and EI premiums of $554.20 (line 31200). After the enhanced CPP deduction of $305 on line 22215, her net income (line 23600) and taxable income (line 26000) are both $33,695.

- Part A: $33,695 is in band 1. $33,695 x 5.05% = $1,701.60 (line 8).
- Part B: $12,989 + $1,509.75 + $554.20 = $15,052.95. Times 5.05% = $760.17 (line 50).
- Basic Ontario tax: $1,701.60 - $760.17 = $941.43. That is below $5,818, so no surtax. Line 73 is $941.43.
- Tax reduction: 2 x $300 = $600, minus $941.43, is negative, so the reduction is nil.
- LIFT: the lesser of $875 and 5.05% x $34,000 ($1,717.00) is $875. Her adjusted net income of $33,695 is $1,195 over $32,500, and 5% of that is $59.75. LIFT = $875 - $59.75 = $815.25. Ontario tax after LIFT: $941.43 - $815.25 = $126.18.
- Health Premium: taxable income of $33,695 is in the $25,000 to $36,000 step, so $300.
- Ontario tax, line 90 (to line 42800): $126.18 + $300 = $426.18. Most of what she pays is the premium, which LIFT cannot reduce.

```oa-check
name: Ontario 2026, single employee, taxable income 33,695
inputs:
  taxable_income: 33695
  employment_income: 34000
  adjusted_net_income: 33695
  cpp_30800: 1509.75
  ei_31200: 554.20
  bpa: 12989
  reduction_basic: 300
steps:
  - line8: round(taxable_income * 0.0505, 2)
  - line50: round((bpa + cpp_30800 + ei_31200) * 0.0505, 2)
  - line53: max(line8 - line50, 0)
  - surtax: round(max(line53 - 5818, 0) * 0.20, 2) + round(max(line53 - 7446, 0) * 0.36, 2)
  - line73: line53 + surtax
  - reduction: max(2 * reduction_basic - line73, 0)
  - line83: max(line73 - reduction, 0)
  - lift_max: min(875, round(employment_income * 0.0505, 2))
  - lift: max(lift_max - round(max(adjusted_net_income - 32500, 0) * 0.05, 2), 0)
  - line86: max(line83 - lift, 0)
  - ohp: 300
  - ontario_tax: line86 + ohp
expected:
  line8: 1701.60
  line50: 760.17
  line53: 941.43
  reduction: 0
  lift: 815.25
  ontario_tax: 426.18
```

### Example 2: 2025, married high earner with surtax and donations

Daniel lives in Ottawa all of 2025. He is 45 and married, and his spouse had no income in 2025. His taxable income (line 26000) is $180,000, all from employment. He paid base CPP of $3,356.10 (line 30800) and EI of $1,077.48 (line 31200), and gave $1,000 to registered charities. He has no children.

- Part A: $180,000 is in band 4. ($180,000 - $150,000) x 12.16% = $3,648.00, plus $12,445.60 = $16,093.60 (line 8).
- Part B: $12,747 basic, plus the spouse amount ($11,905 - $0 = $11,905, capped at $10,823), plus $3,356.10 and $1,077.48, makes $28,003.58. Times 5.05% = $1,414.18. Donations: $200 x 5.05% = $10.10, plus $800 x 11.16% = $89.28, total $99.38. Line 50 = $1,513.56.
- Basic Ontario tax: $16,093.60 - $1,513.56 = $14,580.04.
- Surtax: ($14,580.04 - $5,710) x 20% = $1,774.01, plus ($14,580.04 - $7,307) x 36% = $2,618.29. Surtax $4,392.30. Line 69 = $18,972.34.
- Tax reduction: 2 x $294 = $588 is far below his tax, so nil. LIFT is nil at his income.
- Health Premium: $180,000 is in the $72,600 to $200,000 step, so $750.
- Ontario tax, line 90: $18,972.34 + $750 = $19,722.34. The surtax adds about 30% to his basic Ontario tax.

```oa-check
name: Ontario 2025, married, taxable income 180,000, donations 1,000
inputs:
  taxable_income: 180000
  bpa: 12747
  spouse_base: 11905
  spouse_net_income: 0
  spouse_max: 10823
  cpp_30800: 3356.10
  ei_31200: 1077.48
  donations: 1000
  reduction_basic: 294
steps:
  - line8: round((taxable_income - 150000) * 0.1216, 2) + 12445.60
  - spouse_amount: min(max(spouse_base - spouse_net_income, 0), spouse_max)
  - line46: round((bpa + spouse_amount + cpp_30800 + ei_31200) * 0.0505, 2)
  - line49: round(min(donations, 200) * 0.0505, 2) + round(max(donations - 200, 0) * 0.1116, 2)
  - line50: line46 + line49
  - line53: max(line8 - line50, 0)
  - surtax: round(max(line53 - 5710, 0) * 0.20, 2) + round(max(line53 - 7307, 0) * 0.36, 2)
  - line69: line53 + surtax
  - reduction: max(2 * reduction_basic - line69, 0)
  - ohp: 750
  - ontario_tax: line69 - reduction + ohp
expected:
  line8: 16093.60
  line50: 1513.56
  line53: 14580.04
  surtax: 4392.30
  line69: 18972.34
  ontario_tax: 19722.34
```

## Ask the client first

1. Which province did you live in on 31 December (or on the date you left Canada)? Were you resident in Canada on 1 January?
2. Your federal figures once the T1 is done: taxable income (line 26000), net income (line 23600), employment income (lines 10100 and 10400), CPP and EI amounts (lines 30800, 31000, 31200, 31217), dividends (lines 12000 and 12010), and any split income on Form T1206.
3. Did you have a spouse or common-law partner on 31 December, and what was their net income? This decides the spouse amount, the LIFT family test and who claims the tax reduction for dependants.
4. How many children born in 2008 or later (2007 or later for a 2025 return), or dependants with an impairment, did you support, and what is each one's net income?
5. Your age on 31 December, pension income, disability tax credit certificate, medical expenses, donations, and unused tuition carried forward.
6. Any business with a place of business outside Ontario, foreign tax paid, bankruptcy in the year, or minimum tax (Form T691)? Each changes the method; refer these to an accountant.

## Sources

| Source | URL | Read on |
|---|---|---|
| CRA, Form ON428 Ontario Tax 2025 (5006-C), read for Parts A, B and C and the line 89 chart | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-c/5006-c-25e.pdf | 2026-11-08 |
| CRA, Worksheet ON428 2025 (5006-D), read for the age amount, caregiver amount and dividend tax credit lines | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf | 2026-11-08 |
| CRA, Schedule ON428-A, LIFT credit 2025 (5006-A), read for Parts A and B | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-a/5006-a-25e.pdf | 2026-11-08 |
| CRA, Ontario tax information 2025 (5006-PC), read for who completes ON428, newcomers and emigrants, tax reduction, line 89 | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html | 2026-11-08 |
| CRA, Tax rates and brackets, current year (2026), read for the Ontario rate table | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-08 |
| CRA, Tax rates and brackets, last year (2025), read for the Ontario rate table | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html | 2026-11-08 |
| CRA, T4127 Payroll Deductions Formulas, 122nd edition, effective January 1, 2026, read for the Ontario factors V1, V2, S and Tables 8.2 and 8.23 | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jan/t4127-01-26e.pdf | 2026-11-08 |
| CRA, Form TD1ON 2026, Ontario Personal Tax Credits Return, read for lines 1 to 6 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on/td1on-26e.pdf | 2026-11-08 |
| CRA, Worksheet TD1ON-WS 2026, read for the age, spouse, eligible dependant and caregiver parts | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1on-ws/td1on-ws-26e.pdf | 2026-11-08 |
| CRA, Due dates and payment dates, personal income tax, read for the filing and payment due dates | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-08 |
| CRA, Interest and penalties on late taxes, read for the late-filing penalty and interest | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html | 2026-11-08 |
| CRA, CPP contribution rates, maximums and exemptions, read for the 2025 row (example 2 input) | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html | 2026-11-08 |
| CRA, EI premium rates and maximums, read for the 2025 row (example 2 input) | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html | 2026-11-08 |
| Ontario, Taxation Act, 2007, S.O. 2007, c. 11, Sch. A consolidation from July 1, 2026, read for ss. 3, 4, 6, 9, 16, 19.1, 20, 21, 21.1, 23 and 24 | https://www.ontario.ca/laws/statute/07t11 | 2026-11-08 |
| Ontario, Low-income Individuals and Families Tax (LIFT) Credit, read for eligibility and the 2022 onward calculation | https://www.ontario.ca/page/low-income-individuals-and-families-tax-credit | 2026-11-08 |
| Ontario, Ontario Tax Reduction, read for eligibility and the spouse rule | https://www.ontario.ca/page/ontario-tax-reduction | 2026-11-08 |
| Ontario, Health premium, read for who pays and Status card holders | https://www.ontario.ca/page/health-premium | 2026-11-08 |

Not yet confirmed: the 2026 Form ON428 is not published yet, so the 2026 tax on lower bands ($2,721.50, $7,652.80, $12,363.99, $20,875.99) is computed from the CRA brackets rather than read from the form; the 2026 medical expense cap (2025: $2,885), the 2026 Ontario attendant care maximums and the 2026 under-18 disability supplement were not found on a 2026 CRA or Ontario page; the 2026 dividend tax credit as a percentage of the taxable amount is not printed anywhere yet (the law states it as a share of the federal gross-up); filing channels (NETFILE, EFILE, My Account) are left to ca-fed-t1-return; Ontario minimum tax (Worksheet ON428, Form T691) and tax on split income (Form T1206) are named but not worked here.
