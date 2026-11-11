---
name: bc-individual-return
description: "British Columbia provincial personal income tax for an individual resident in BC on 31 December, computed on Form BC428 with the federal T1 return. Written for tax year 2026, with a dated section of full 2025 figures for returns being filed now. Covers the seven BC brackets and rates (lowest rate back to 5.6% for 2026), the basic personal amount and main non-refundable credits, the BC tax reduction for low incomes, dividend, political contribution and minimum tax lines, the BC479 refundable credits and the end of the climate action tax credit. Trigger on \"BC tax\", \"BC428\", \"British Columbia income tax\", \"BC tax brackets\", \"BC basic personal amount\", \"BC tax reduction\", \"BC renter's tax credit\". Out of scope: the federal return (ca-fed-t1-return), business income (ca-fed-t2125), CPP and EI (ca-fed-cpp-ei), instalments (ca-fed-instalments), residence (ca-tax-residency), BC PST (bc-pst), Employer Health Tax (bc-eht)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bc-individual-return"
  jurisdiction: "CA"
  tax_year: "2026"
  last_updated: "2026-11-08"
---

# British Columbia individual income tax (Form BC428), 2026 and 2025

## Who this applies to

This skill computes British Columbia (BC) tax for an individual who was resident in BC on 31 December of the tax year. CRA's BC tax information tells you to complete Form BC428 if "You were a resident of British Columbia at the end of the year." The province of residence on 31 December decides which provincial form applies for the whole year. A person who moved into BC during 2026 and lived there on 31 December 2026 pays BC tax on the whole year's taxable income; a person who left BC for another province before 31 December uses the form of the province they lived in on that date.

BC tax is collected by the Canada Revenue Agency (CRA) on the federal T1 return. Form BC428 is filed with the T1 and its result goes on line 42800 of the return. The law is the Income Tax Act of British Columbia, RSBC 1996, chapter 215 (the BC Act), Part 1, Division 2, read with the federal Income Tax Act. BC uses federal taxable income (line 26000) and federal net income (line 23600) as its starting points.

Year covered: **2026** is the main year (calendar 2026, return filed in 2027). CRA has not yet published the 2026 Form BC428, so the 2026 amounts below come from BC's own pages, CRA's 2026 rate page and the BC Act, laid out on the 2025 form's lines. A dated section gives the **2025** figures exactly as printed on the 2025 Form BC428.

Who is out, and where to go:

- Not resident in BC on 31 December: this skill does not apply. Use the skill for the province of residence on that date.
- A BC resident with business income allocated to a permanent establishment outside BC: CRA says to use Form T2203 instead of BC428 (see Cross-border points).
- Trusts, estates and corporations: out of scope. The BC Act taxes most trusts at the top rate (BC Act s. 4.1(3)); corporations are not covered here.
- Income that may be exempt under section 87 of the Indian Act: refer to a specialist. This skill does not apply the exemption.
- The federal return, federal credits, CPP and EI, instalments and self-employment income are in their own skills: `ca-fed-t1-return`, `ca-fed-cpp-ei`, `ca-fed-instalments`, `ca-fed-t2125`. Residence questions go to `ca-tax-residency`.

## Rates, bands and thresholds

### What changed for 2026

- The lowest BC rate went from 5.06% (2025) to **5.6%** (2026). The BC Act, s. 4.1(1)(a), now reads "5.6% of the taxable income". Because BC's non-refundable credits are valued at the lowest rate (the "appropriate percentage", BC Act s. 1), every basic credit is now worth 5.6% of its base amount, not 5.06%.
- Brackets and credit amounts were indexed by BC CPI of 2.2% for 2026. BC's Budget 2026 paused indexation of brackets and basic credits for 2027 to 2030 (BC Act s. 4.52(4.25)); the renter's tax credit amounts are the only ones still indexed in those years.
- The BC tax reduction rose from $562 (2025) to **$690** for 2026 to 2030 (BC Act s. 4.301).
- BC minimum tax is 40% of federal minimum tax for 2026; the 2025 form used 34.9%.
- The climate action tax credit has ended. Its April 2025 payment was the last.

### 2026 brackets and rates

Rates apply on a cumulative basis to taxable income (T1 line 26000). The "tax on first" amount in brackets is what goes on line 7 or line 14 of the form layout, worked out the way CRA prints it on the 2025 form (bracket width times rate, to the cent).

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Taxable income $0 to $50,363 | 5.6% | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates |
| $50,363.01 to $100,728 (tax on first $50,363: $2,820.33) | 7.7% | 2026 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| $100,728.01 to $115,648 (tax on first $100,728: $6,698.43) | 10.5% | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates |
| $115,648.01 to $140,430 (tax on first $115,648: $8,265.03) | 12.29% | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates |
| $140,430.01 to $190,405 (tax on first $140,430: $11,310.74) | 14.7% | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates |
| $190,405.01 to $265,545 (tax on first $190,405: $18,657.07) | 16.8% | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates |
| Over $265,545 (tax on first $265,545: $31,280.59) | 20.5% | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates |
| Credit rate for non-refundable credits (lowest rate) | 5.6% | 2026 | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_01 |
| Brackets and basic credits indexed | 2.2% (BC CPI) | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates |
| Indexation of brackets and basic credits | paused | 2027 to 2030 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |

### 2026 basic non-refundable credits (base amounts; credit = base amount x 5.6%)

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Basic personal amount (BC428 line 16) | $13,216 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Spouse or common-law partner amount | $11,317, reduced by the partner's net income above $1,132 (form base amount $12,449) | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Eligible dependant amount | $11,317, reduced by the dependant's net income above $1,132 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| BC caregiver amount | $5,784, reduced when the dependant's income exceeds $19,572 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Age amount (65 or older at year end) | $5,927, reduced by 15% of net income above $44,119 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Pension income amount | up to $1,000 (not indexed) | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Adoption expenses | actual, up to $19,972 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Volunteer firefighters and search and rescue volunteers | $6,000 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Disability amount | $9,913 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Disability supplement for a child under 18 | $5,783, reduced by care expenses above $3,358 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Medical expenses | actual, less the lesser of 3% of net income and $2,748 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| CPP base contributions | up to $3,519.45 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| EI premiums | up to $1,123.07 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Tuition, student loan interest | actual (BC education credit ended in 2019; old unused amounts carry forward) | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Charitable gifts | 5.6% on first $200; 20.5% on the part above $200 that matches taxable income above $265,545; 16.8% on the rest | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |

### 2026 BC tax reduction and other credits

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| BC tax reduction, basic amount | $690 | 2026 to 2030 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| BC tax reduction, net income threshold where it starts to fall | $25,570 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| BC tax reduction, rate of reduction | 3.56% of net income above the threshold | 2026 | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_01 |
| BC tax reduction, net income where it reaches zero | $44,952 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Dividend tax credit, eligible dividends | 12% of the taxable (grossed-up) amount | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Dividend tax credit, other than eligible dividends | 1.96% of the taxable amount | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| BC minimum tax | 40% of federal minimum tax | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates |
| BC minimum tax credit | 40% of the federal minimum tax credit | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Political contribution credit | 75% of first $100; $75 + 50% of $100 to $550; $300 + 33 1/3% above $550; maximum $500 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/political-contribution |
| Renter's tax credit (refundable, BC479) | up to $400; reduced by 2% of adjusted income above $66,189; zero at $86,189 | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/renters-tax-credit |
| Home renovation credit for seniors and persons with disabilities (refundable, BC479) | 10% of up to $10,000 of qualifying expenses, maximum $1,000 a year | 2026 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/seniors-renovation |

### 2025 figures (for 2025 returns), as printed on Form BC428 2025

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Taxable income $0 to $49,279 | 5.06% | 2025 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html |
| $49,279.01 to $98,560 (tax on first $49,279: $2,493.52) | 7.7% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| $98,560.01 to $113,158 (tax on first $98,560: $6,288.15) | 10.5% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| $113,158.01 to $137,407 (tax on first $113,158: $7,820.94) | 12.29% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| $137,407.01 to $186,306 (tax on first $137,407: $10,801.15) | 14.7% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| $186,306.01 to $259,829 (tax on first $186,306: $17,989.30) | 16.8% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| Over $259,829 (tax on first $259,829: $30,341.16) | 20.5% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| Credit rate (line 55) | 5.06% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| Basic personal amount (line 16) | $12,932 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| Spouse or eligible dependant: base amount (lines 18, 21) and maximum | base $12,181 less the person's net income; maximum $11,073 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| Age amount (born 1960 or earlier) | maximum $5,799, reduced when income exceeds $43,169 | 2025 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| BC caregiver amount | $5,659, reduced when the dependant's income exceeds $19,151 | 2025 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Disability amount (line 38) | $9,699 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| Disability supplement for a child under 18 | $5,659, reduced by care expenses above $3,285 | 2025 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Pension income amount (line 36) | maximum $1,000 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| Adoption expenses | actual, up to $19,580 | 2025 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Volunteer firefighters and search and rescue volunteers | $3,000 | 2025 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Medical expenses threshold (line 50) | lesser of 3% of net income and $2,689 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| CPP base contributions / EI premiums | up to $3,356.10 / up to $1,077.48 | 2025 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Charitable gifts | 5.06% on first $200; 20.5% on the part above $200 that matches taxable income above $259,829; 16.8% on the rest | 2025 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| Farmers' food donation credit (line 59) | 25% of qualifying gifts also claimed on line 57 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| BC tax reduction: basic reduction (line 73) | $562 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| BC tax reduction: base amount (line 75), where it starts to fall | $25,020 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| BC tax reduction: rate (line 77) | 3.56% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| BC tax reduction: zero at net income of | $40,807 | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| BC minimum tax carryover and additional tax (lines 66, 69) | 34.9% | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| Dividend tax credit, eligible / other than eligible | 12% / 1.96% of the taxable amount | 2025 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic |
| ESOP and EVCC credits (line 88) | maximum $2,000 combined | 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf |
| Renter's tax credit | up to $400; reduced by 2% of adjusted income above $64,764; zero at $84,764 | 2025 | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/renters-tax-credit |

### The climate action tax credit (ended)

The BC climate action tax credit "has ended", and the April 2025 payment was the final one. It was a quarterly payment paid with the GST/HST credit. For the last benefit year (July 2024 to June 2025, based on 2023 income) the maximums were $504 for the individual, $252 for a spouse or common-law partner (or the first child of a single parent) and $126 for each other child, reduced by 2% of adjusted family net income above $41,071 (individuals) or $57,288 (families). Someone who has not filed a 2023 or earlier return may still get the credit for those years when they file. Do not compute it for 2025 or 2026. Source: https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/climate-action

## The base

BC tax is a tax on the federal taxable income from T1 line 26000. Nothing is added or deducted for BC: income, deductions, the capital gains inclusion and losses are all federal (see `ca-fed-t1-return` and `ca-capital-gains`).

The order on Form BC428 is:

1. **Part A, lines 1 to 15.** Pick the column for the taxable income, subtract the column's threshold, multiply by the rate and add the tax on lower brackets. The result is BC tax on taxable income (line 61).
2. **Part B, lines 16 to 60.** Add the credit base amounts (basic personal, age, spouse or eligible dependant, caregiver, CPP and EI, volunteer amounts, adoption, pension, disability, student loan interest, tuition, transfers, medical) to line 54. Multiply by the credit rate on line 55 (5.06% for 2025, 5.6% for 2026). Add donations (line 57) and the farmers' food donation credit (line 59). The total is BC non-refundable credits (line 60, line 61500).
3. **Part C, lines 61 to 91.** Add BC tax on split income from Form T1206 (line 62). Subtract non-refundable credits, the BC dividend tax credit (line 65) and the minimum tax carryover (line 66); the result cannot go below zero (line 68). Add BC additional tax for minimum tax (line 69). Subtract the provincial foreign tax credit from Form T2036 (line 71). Then subtract the BC tax reduction (line 79), the logging tax credit (line 81), the political contribution credit (line 84, maximum $500), ESOP and EVCC credits (line 88, maximum $2,000) and the mining flow-through share credit (line 90). Line 91 goes on line 42800 of the return.

**The BC tax reduction.** BC Act s. 4.301 gives the formula A minus B, where A is $690 (for 2026) and B is 3.56% of net income above the indexed threshold ($19,400 in the Act, indexed to $25,570 for 2026). On the 2025 form it is line 73 ($562) minus 3.56% of net income (line 23600) above $25,020 (lines 74 to 78), not below zero. If net income is $40,807 or more for 2025 ($44,952 or more for 2026), the reduction is zero. It uses the individual's own net income only; the formula has no add-on for a spouse or dependants. It is non-refundable: it reduces BC tax to zero but does not create a refund.

**Credits use net income, the brackets use taxable income.** The tax reduction, the age amount, the medical expense threshold and the spouse and dependant amounts are tested against net income (line 23600 of the person concerned). The brackets apply to taxable income (line 26000).

**Refundable BC credits are on Form BC479**, not BC428: the renter's tax credit, the home renovation credit for seniors and persons with disabilities, and others (training, clean buildings, sales tax, venture capital, mining exploration). They reduce tax and the excess is refunded.

- Renter's tax credit: the individual rented and lived in an eligible rental unit in BC for at least six one-month periods, paid rent, and on 31 December was a BC resident aged 19 or older, a parent, or living with a spouse or common-law partner. Only one person of a cohabiting couple claims. Rent to a non-arm's length landlord, rent-to-own payments, and campsite, moorage or pad rent do not count. The credit depends on adjusted family income, not on the rent paid.
- Home renovation credit: for a resident who on the last day of the year is 65 or older, a person with a disability, or a family member living with either. The renovation must be to the principal residence and improve access or mobility or reduce the risk of harm; its main purpose cannot be to add value. The credit can be shared between eligible residents of the home up to the maximum.

## Deadlines and filing

BC tax is filed and paid with the federal T1. There is no separate BC return.

| Item | 2025 return | 2026 return |
|---|---|---|
| Filing deadline, most individuals | 30 April 2026 | 30 April 2027 (same rule) |
| Filing deadline, self-employed and their spouses or common-law partners | 15 June 2026 | 15 June 2027 (same rule) |
| Payment deadline, everyone | 30 April 2026 | 30 April 2027 (same rule) |

The 2025 dates are CRA's published dates. The 2026 dates apply the same rule; CRA had not yet published its 2027 calendar when this skill was written. Instalments are federal and include BC tax: see `ca-fed-instalments`.

What to file:

- Form BC428, attached to the T1 (paper) or produced by the certified software for NETFILE or EFILE. The result goes on T1 line 42800.
- Form BC479 for the refundable BC credits. For the renter's credit, enter the rental address, total rent paid, months of tenancy and the landlord's name.
- Schedule BC(S2) for amounts transferred from a spouse, Schedule BC(S11) for tuition, Form T1206 for split income, Form T2036 for the provincial foreign tax credit, Form T691 for minimum tax.
- The Provincial Worksheet (Worksheet BC428) is for your records (age, caregiver, donations, dividends, political contributions); it does not need to be attached.
- Form T2203 instead of BC428 when business income is allocated to a permanent establishment outside BC.

## Penalties and interest

BC tax is part of the T1 balance owing, so the federal penalty and interest rules apply to it.

- Late filing: 5% of the balance owing, plus 1% of the balance owing for each full month late, up to 12 months.
- Repeated late filing: 10% of the balance owing, plus 2% for each full month late, up to 20 months. For a 2025 return this applies if you were penalized in 2022, 2023 or 2024 and received a demand to file.
- Interest: CRA charges compound daily interest on unpaid tax starting the day after the due date. The rate follows the prescribed rate and can change every three months.

Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html. Other penalties are federal and sit in `ca-fed-t1-return`.

## Cross-border points

- **Moving into or out of BC within Canada.** The province of residence on 31 December decides the provincial tax for the whole year (CRA 2026 rate page: "The rate is determined by your province or territory of residence on December 31"). There is no split between provinces for a mover. Check residence with `ca-tax-residency`.
- **BC resident with business income earned outside BC.** BC Act s. 4.1(5) scales BC tax by the share of income earned in BC: tax x (income minus income earned outside BC) / income. CRA's form package says to use Form T2203 instead of BC428 when a BC resident has business income allocated to a permanent establishment outside BC.
- **Not resident in BC on 31 December but with income earned in BC.** BC Act s. 4.1(6) charges BC tax on the share of income earned in BC: tax x income earned in BC / income. This is computed on Form T2203.
- **Foreign tax.** Where the federal foreign tax credit on non-business income is less than the foreign tax paid, a provincial foreign tax credit may be claimed on Form T2036 and entered on BC428 line 71.
- **Emigrants and immigrants.** CRA's package refers to residence in BC "on December 31, 2025 (or your departure date)": a person who leaves Canada uses the province of residence on the departure date. Departure tax and part-year rules are in `ca-tax-residency` and `leaving-canada-departure-tax`.

## Two worked examples that recompute

### Example 1: 2026, single BC resident, taxable income $42,000

A single BC resident has net income and taxable income of $42,000 for 2026. No spouse, no dependants, and for this example no claim other than the basic personal amount (CPP and EI credits are left out to keep the lines clear; in practice add them on lines 27 to 30).

- Part A, first column (taxable income is $50,363 or less): $42,000 x 5.6% = $2,352.00 (line 61).
- Part B: basic personal amount $13,216 x 5.6% = $740.10 (line 60).
- Line 68: $2,352.00 minus $740.10 = $1,611.90.
- BC tax reduction: net income is below $44,952, so compute it. $42,000 minus $25,570 = $16,430. $16,430 x 3.56% = $584.91. $690 minus $584.91 = $105.09 (line 79).
- BC tax, line 91: $1,611.90 minus $105.09 = **$1,506.81**.

The 2026 Form BC428 is not yet published; this uses the 2025 form's line numbers with the 2026 amounts.

```oa-check
name: BC 2026, single, taxable and net income 42000
inputs:
  taxable_income: 42000
  net_income: 42000
  bpa: 13216
  reduction_basic: 690
  reduction_threshold: 25570
steps:
  - tax_on_income: round(taxable_income * 0.056, 2)
  - credits: round(bpa * 0.056, 2)
  - line_68: max(tax_on_income - credits, 0)
  - reduction_clawback: round(max(net_income - reduction_threshold, 0) * 0.0356, 2)
  - reduction: max(reduction_basic - reduction_clawback, 0)
  - bc_tax: max(line_68 - reduction, 0)
expected:
  tax_on_income: 2352.00
  credits: 740.10
  reduction: 105.09
  bc_tax: 1506.81
```

### Example 2: 2025 return, employee with a low-income spouse and donations

A BC resident employee has 2025 net income and taxable income of $120,000. Their spouse's net income is $5,000. CPP base contributions on T1 line 30800 are $3,356.10, EI premiums on line 31200 are $1,077.48, and charitable donations are $1,000. Taxable income is below $259,829, so donations above $200 get 16.8%.

- Part A, fourth column (more than $113,158, not more than $137,407): line 4 is $120,000 minus $113,158 = $6,842. Line 6: $6,842 x 12.29% = $840.88. Line 8: $840.88 plus $7,820.94 = $8,661.82.
- Part B: line 16 $12,932. Line 20: $12,181 minus $5,000 = $7,181 (within the $11,073 maximum). Line 25: $20,113. Line 33: $3,356.10 plus $1,077.48 = $4,433.58. Line 54: $24,546.58. Line 56: $24,546.58 x 5.06% = $1,242.06.
- Donations (line 57): $200 x 5.06% = $10.12, plus $800 x 16.8% = $134.40, total $144.52. Line 60: $1,242.06 plus $144.52 = $1,386.58.
- Part C, line 68: $8,661.82 minus $1,386.58 = $7,275.24.
- BC tax reduction: net income is $40,807 or more, so line 79 is zero.
- BC tax, line 91: **$7,275.24**.

The edge in this case is that the BC tax reduction gives nothing at this income, while the spouse amount still does: the spouse amount is tested against the spouse's net income, not the claimant's.

```oa-check
name: BC 2025, taxable income 120000, spouse income 5000, donations 1000
inputs:
  taxable_income: 120000
  net_income: 120000
  spouse_income: 5000
  cpp_base: 3356.10
  ei: 1077.48
  donations: 1000
steps:
  - line_8: round((taxable_income - 113158) * 0.1229, 2) + 7820.94
  - line_20: min(max(12181 - spouse_income, 0), 11073)
  - line_54: 12932 + line_20 + cpp_base + ei
  - line_56: round(line_54 * 0.0506, 2)
  - line_57: round(min(donations, 200) * 0.0506, 2) + round(max(donations - 200, 0) * 0.168, 2)
  - line_60: line_56 + line_57
  - line_68: max(line_8 - line_60, 0)
  - line_79: max(562 - round(max(net_income - 25020, 0) * 0.0356, 2), 0)
  - bc_tax: max(line_68 - line_79, 0)
expected:
  line_8: 8661.82
  line_56: 1242.06
  line_60: 1386.58
  line_79: 0
  bc_tax: 7275.24
```

## Ask the client first

1. Where did you live on 31 December of the tax year? If not BC, this skill does not apply. If you moved in or out of Canada during the year, give the date.
2. Which year is the return for, 2025 or 2026? The lowest rate, the credit rate and the tax reduction changed between them.
3. Your net income (T1 line 23600) and taxable income (line 26000), and your spouse's or common-law partner's net income.
4. Did you earn business income through a fixed place of business outside BC, or in BC while living elsewhere? That moves the computation to Form T2203.
5. Dependants, age 65 or over, disability certificate (T2201), pension income, medical expenses, donations, political contributions to BC parties or candidates, and dividends.
6. Did you rent your home in BC for at least six months, or make accessibility renovations to your home if 65 or over or living with a person with a disability? Those are BC479 refundable credits.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act (BC), RSBC 1996, c. 215, ss. 1, 4.1, 4.3, 4.301, 4.31, 4.4, 4.52, 4.69, 4.722 (current to 3 November 2026) | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_01 | 2026-11-08 |
| Government of BC, Personal income tax rates (updated 17 April 2026), read for 2026 and 2025 brackets, indexation, minimum tax | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates | 2026-11-08 |
| Government of BC, B.C. basic personal income tax credits (updated 20 April 2026), read for 2026 and 2025 credit amounts, tax reduction, dividend credit | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic | 2026-11-08 |
| Government of BC, Political contribution personal income tax credit, read for the credit bands and $500 cap | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/political-contribution | 2026-11-08 |
| Government of BC, B.C. renter's tax credit, read for eligibility and 2025 and 2026 thresholds | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/renters-tax-credit | 2026-11-08 |
| Government of BC, Home renovation tax credit for seniors and persons with disabilities, read for eligibility, 10% rate and $10,000 cap | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/seniors-renovation | 2026-11-08 |
| Government of BC, Climate action tax credit, read for the end of the program and last-year amounts | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/climate-action | 2026-11-08 |
| CRA, Form BC428 British Columbia Tax 2025 (5010-C), Part A, Part B and Part C, lines 1 to 91 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf | 2026-11-08 |
| CRA, British Columbia Tax Information 2025 (5010-PC), read for who completes BC428 and the BC479 credits | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/british-columbia/5010-pc.html | 2026-11-08 |
| CRA, British Columbia 2025 income tax package, read for the T2203 rule | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/british-columbia.html | 2026-11-08 |
| CRA, Current year tax rates and income brackets (2026), read for the BC 2026 brackets and residence rule | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-08 |
| CRA, Last year tax rates and income brackets (2025), read for the BC 2025 brackets | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html | 2026-11-08 |
| CRA, Important dates for individuals, read for 2025 filing and payment dates | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-08 |
| CRA, Interest and penalties on late taxes, read for late-filing penalties and interest | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html | 2026-11-08 |

Not yet confirmed: the 2026 Form BC428 and its exact printed line amounts (not yet published by CRA; the 2026 bracket base amounts here are computed the way the 2025 form prints them); the 2027 filing dates as published by CRA; the 2026 BC479 figures other than the renter's credit (training, clean buildings, sales tax, venture capital, mining exploration credit rates); the BC logging tax credit and mining flow-through share credit rates; how the section 87 Indian Act exemption is applied on BC428; whether the renter's tax credit interacts with a home office claim for the same space (the old skill said both cannot be claimed for the same space; no official source found).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-08. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bc-individual-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bc-individual-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
