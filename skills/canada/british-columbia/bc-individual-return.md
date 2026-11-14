---
name: bc-individual-return
description: "British Columbia individual income tax: execute the BC428 calculation and BC479 renter and accessibility-renovation workpapers for 2026 estimates or actual 2025 returns. Covers all seven bands, conditional personal credits, caregiver overlap, medical baskets, tuition, donations, dividends, tax reduction, minimum tax, foreign credit and the final split-income comparison. Establish BC residence, departure/death dates and actual non-resident or multiple-jurisdiction form routes first. Trigger on BC tax, BC428, British Columbia income tax, brackets, basic personal amount, tax reduction or renter tax credit. Federal T1, T2125, CPP/EI, instalments, residence, BC PST and Employer Health Tax remain in their named companion skills."
version: 2.2
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: computation
domain: income-tax
---

# British Columbia individual income tax (Form BC428), 2026 and 2025

## Who this applies to

This method computes British Columbia (BC) provincial income tax for an individual. The ordinary case is a Canadian resident whose province of residence was BC on 31 December of the tax year. A move between Canadian provinces ordinarily uses the province of residence on that date for the whole year, rather than splitting employment income between provinces. A person moving to BC during 2026 who remains resident there on 31 December ordinarily uses BC tax; a person moving to another province before that date ordinarily uses that province. First resolve actual residence, departure from Canada, death, non-resident income and business permanent-establishment facts. CRA also instructs a non-resident of Canada with employment only in BC, or a business permanent establishment only in BC, to complete BC428. See the specific routes below; absence of BC residence on 31 December is not itself a universal exclusion.

BC tax is collected by the Canada Revenue Agency (CRA) on the federal T1 return. Form BC428 is filed with the T1 and its result goes on line 42800 of the return. The law is the Income Tax Act of British Columbia, RSBC 1996, chapter 215 (the BC Act), Part 1, Division 2, read with the federal Income Tax Act. BC uses federal taxable income (line 26000) and federal net income (line 23600) as its starting points.

Year covered: **2026** is the main income year, filed in 2027. The current CRA BC428 catalogue read on 14 November 2026 offers the **2025** annual edition; no final 2026 BC428 or BC479 annual form was obtained in this audit. Published 2026 BC amounts and enacted law support estimates; all numbered fields below are from the actual 2025 forms unless expressly stated otherwise. Keep an estimate separate from a completed 2026 filing and obtain the actual-year forms/software before finalizing it. The dated 2025 table preserves that filing year without rolling its rates into 2026.

Who is out, and where to go:

- Resident in another Canadian province at year end, with no BC business allocation or applicable special route: use that province's method. A Canada-non-resident with BC-only employment or a BC-only business permanent establishment can still use ordinary BC428; test credit restrictions separately. Departure from Canada uses the relevant departure-date rule; a deceased person needs the actual final/optional-return rules.
- A BC resident with business income allocated to a permanent establishment outside BC: CRA says to use Form T2203 instead of BC428 (see Cross-border points).
- Trusts, estates and corporations: out of scope. The BC Act taxes most trusts at the top rate (BC Act s. 4.1(3)); corporations are not covered here.
- Income that may be exempt under section 87 of the Indian Act: refer to a specialist. This skill does not apply the exemption.
- The federal return, federal credits, CPP and EI, instalments and self-employment income are in their own skills: `ca-fed-t1-return`, `ca-fed-cpp-ei`, `ca-fed-instalments`, `ca-fed-t2125`. Residence questions go to `ca-tax-residency`.

## Rates, bands and thresholds

### What changed for 2026

- The lowest BC rate went from 5.06% (2025) to **5.6%** (2026), enacted in BC Act s. 4.1(1)(a). The ordinary credit rate is the "appropriate percentage" defined in **s. 4(1)**. It is 5.6% for 2026 and 5.06% for 2025. This values eligible basic credit bases; donations, dividend credits, political credits and refundables have their own calculations, not a blanket 5.6% multiplier.
- Brackets and credit amounts were indexed by BC CPI of 2.2% for 2026. BC's Budget 2026 paused indexation of brackets and basic credits for 2027 to 2030 (BC Act s. 4.52(4.25)); the renter's tax credit amounts are the only ones still indexed in those years.
- The BC tax reduction rose from $562 (2025) to **$690** for 2026 to 2030 (BC Act s. 4.301).
- BC minimum tax is 40% of federal minimum tax for 2026; the 2025 form used 34.9%.
- The climate action tax credit has ended. Its April 2025 payment was the last.

### 2026 brackets and rates

Rates apply cumulatively to federal taxable income (T1 line 26000) for the ordinary resident case. The six 2026 "tax on first" constants below are **derived estimates** using the cumulative-cent convention shown on the actual 2025 form, not amounts read from a final 2026 annual form. There is an unresolved source-edition difference: BC Act s. 4.1(2) specifies nearest-whole-dollar rounding for the highest tax in a lower band, while actual 2025 BC428 prints cent constants. Preserve the actual 2025 printed constants for that edition and reconcile the final 2026 form/certified-software instructions before filing. Do not represent the estimated cent constants as a resolution of that difference.

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

### 2026 basic non-refundable credits (ordinary eligible bases x 5.6%; donations separate)

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

The BC climate action tax credit "has ended", and the April 2025 payment was the final one. It was a quarterly payment paid with the GST/HST credit. For the last benefit year (July 2024 to June 2025, based on 2023 income) the maximums were $504 for the individual, $252 for a spouse or common-law partner (or the first child of a single parent) and $126 for each other child, reduced by 2% of adjusted family net income above $41,071 (individuals) or $57,288 (families). Someone who has not filed a 2023 or earlier return may still get the credit for those years when they file. Do not create a new entitlement based on income tax years 2025 or 2026. That does not deny the historical January/April 2025 payments or later recovery for an eligible older income year. Source: https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/climate-action

## The base

In the ordinary full-year resident case, start with federal taxable income from T1 line 26000 and net income from line 23600. Federal income, deductions, capital-gains inclusion and losses are settled in `ca-fed-t1-return`, `ca-fed-t2125` and `ca-capital-gains`; do not invent a separate BC deduction for the same expense. Non-residents use the applicable Canadian taxable-income base under BC Act s. 4.1(7). Multiple-jurisdiction allocation, part-year credits and TOSI adjustments are separate required operations, not permission to assume worldwide full-year income or use unadjusted credit inputs.

The order on Form BC428 is:

1. **Part A, lines 1 to 15.** Pick the column for the taxable income, subtract the column's threshold, multiply by the rate and add the tax on lower brackets. The result is BC tax on taxable income (line 61).
2. **Part B, lines 16 to 60.** Add the credit base amounts (basic personal, age, spouse or eligible dependant, caregiver, CPP and EI, volunteer amounts, adoption, pension, disability, student loan interest, tuition, transfers, medical) to line 54. Multiply by the credit rate on line 55 (5.06% for 2025, 5.6% for 2026). Add donations (line 57) and the farmers' food donation credit (line 59). The total is BC non-refundable credits (line 60, line 61500).
3. **Part C, lines 61 to 91.** Add completed T1206 provincial split-income tax at line 62. Deduct the non-refundable credits (64), dividend credit (65) and minimum-tax carryover (66); floor the result at zero (68). Add the correctly sourced additional minimum tax (69), then subtract the permitted provincial foreign credit (71), flooring at 72. Deduct the tax reduction (79), floor at 80; logging credit (81), floor at 82; political credit (84, maximum $500), floor at 85; ESOP/EVCC (88, combined maximum $2,000), floor at 89; and eligible mining flow-through share credit (90), floor at 91. Without TOSI, 91 goes to T1 line 42800. **With TOSI this is not the final result:** complete T1206's greater-of comparison below. Do not deduct BC479 refundables in this chain.

**The BC tax reduction.** BC Act s. 4.301 gives the formula A minus B, where A is $690 (for 2026) and B is 3.56% of net income above the indexed threshold ($19,400 in the Act, indexed to $25,570 for 2026). On the 2025 form it is line 73 ($562) minus 3.56% of net income (line 23600) above $25,020 (lines 74 to 78), not below zero. If net income is $40,807 or more for 2025 ($44,952 or more for 2026), the reduction is zero. It uses the individual's own net income only; the formula has no add-on for a spouse or dependants. It is non-refundable: it reduces BC tax to zero but does not create a refund.

**Credits use net income, the brackets use taxable income.** The tax reduction, the age amount, the medical expense threshold and the spouse and dependant amounts are tested against net income (line 23600 of the person concerned). The brackets apply to taxable income (line 26000).

**Refundable BC credits are on Form BC479**, not BC428: the renter's tax credit, the home renovation credit for seniors and persons with disabilities, and others (training, clean buildings, sales tax, venture capital, mining exploration). They reduce tax and the excess is refunded.

- Renter's tax credit: establish at least six one-month periods of eligible BC occupancy, rent paid by or on behalf of the individual, year-end BC residence and age 19/parent/spouse eligibility. Apply the actual exclusions, adjusted family income and one-credit-per-cohabiting-couple rules in the detailed workpaper below. Non-arm's-length rent, rent-to-own, campsites, moorage and manufactured-home pad rent do not count. The amount is income-based, not a percentage of the rent.
- Home renovation credit: establish an eligible senior, qualifying person with a disability or qualifying relation, BC principal-residence facts and an enduring access/mobility/safety improvement. Apply the actual expense exclusions, assistance and shared limits in the detailed workpaper below. Merely being aged 65 or buying a renovation does not make the whole bill eligible.

### Credit eligibility and workpapers

Use the actual year's provincial worksheet with the federal eligibility evidence. A table maximum is not an automatic claim. Ordinary 2025 field references below identify the workpaper; they do not establish final 2026 field numbers. Primary sources: [BC Act ss. 4.3–4.67](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_01), [actual 2025 Worksheet BC428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-d/5010-d-25e.pdf), and [CRA BC information](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/british-columbia/5010-pc.html).

1. **Basic personal, spouse and eligible dependant.** The ordinary BPA is $13,216 for 2026 or $12,932 for 2025, subject to special-return restrictions. For an otherwise eligible supported spouse or eligible dependant, the 2026 base is `min(11317, max(12449 - person's net income, 0))`; for 2025 use `min(11073, max(12181 - person's net income, 0))`. Obtain the actual net income and relationship/support/household facts. Follow the federal spouse/eligible-dependant eligibility and multiple-claim/support-payment restrictions; do not claim both for the same person or assume every relative qualifies. The claimant's high income does not itself eliminate an otherwise valid spouse amount.
2. **Age.** Age 65 or over at year end: 2026 base `max(5927 - 15% * max(own net income - 44119, 0), 0)`; 2025 `max(5799 - 15% * max(own net income - 43169, 0), 0)`. Use the actual worksheet's rounding. Death-year eligibility needs the final-return instructions, not a fictional December birthday. Only unused eligible amounts can transfer.
3. **Caregiver.** Confirm an adult dependant with the required infirmity, actual dependence for support, qualifying relationship and applicable Canadian residence; age alone does not qualify a parent. For 2026 compute `preliminary = min(5784, max(25356 - dependant's net income, 0))`; for 2025 use maximum $5,659 and base $24,810. Then deduct the **same person's amount actually claimed on 58120 OR 58160**, floor at zero. This overlap applies to a spouse claim as well as an eligible-dependant claim. Use the actual worksheet for each dependant and coordinate eligible claimants so their total does not exceed the permitted amount; do not give everyone the full maximum. For a 2026 qualifying spouse with net income $10,000, the spouse base is $2,449, preliminary caregiver $5,784, remaining caregiver $3,335. At zero spouse income the spouse base $11,317 eliminates the caregiver amount.
4. **CPP, QPP and EI.** Transfer the eligible actual base-contribution credit from federal lines 30800/31000 and EI from 31200/31217. The table's CPP maximum is the base component, not total employee CPP including enhanced contributions. Enhanced CPP deducted in net income is not credited a second time. Self-employment uses the permitted credit component after the federal CPP calculation, not every dollar paid. Obtain slips, overpayment adjustments and completed `ca-fed-cpp-ei`; do not infer the maximum from a salary alone.
5. **Pension, adoption and volunteers.** Pension is the lesser of $1,000 and the eligible federal pension amount; CPP/OAS income is not automatically eligible pension income. Adoption uses eligible federal adoption expenses, with the BC cap $19,972 for 2026/$19,580 for 2025, shared/period restrictions and no duplicated expenses between claimants. The volunteer amount is $6,000 for 2026/$3,000 for 2025 only for the corresponding qualifying federal firefighter or search-and-rescue claim. Do not claim both categories or combine it with an incompatible exempt volunteer allowance under federal s. 81(4). BC Act ss. 4.32/.33/.37 require BC residence on the relevant last day, so do not grant these automatically to a full-year Canada-non-resident.
6. **Disability.** Require the relevant federal disability entitlement/T2201 evidence. The 2026 personal base is $9,913; the under-18 supplement is `max(5783 - max(qualifying care/supervision expenses - 3358, 0), 0)`. For 2025 the base/supplement/expense floor are $9,699/$5,659/$3,285. Use expenses claimed by any person under the applicable child-care, disability-support and medical provisions. Check attendant-care/nursing-home interactions before combining claims. A dependant's transfer is only the eligible unused amount after the dependant's tax and specified own credits, including the supplementary rules, not the whole personal maximum. Obtain the actual provincial worksheet and tax calculation even if their income is low.
7. **Medical: two baskets.** Use eligible unreimbursed federal expenses, qualifying patients and the same federal claim period: normally a 12-month period ending in the year; where the federal death rule permits it, a 24-month period including the patient's death date. No reuse of an expense claimed in an earlier year or by another person. For the self/spouse/minor-child basket, subtract the lesser of 3% of the claimant's net income and $2,748 (2026)/$2,689 (2025), floor at zero. For each other eligible dependant use that dependant's own net income and the same annual threshold separately, then sum the positive results. **BC has no Ontario-style dollar cap on each other dependant's allowed basket in this worksheet.** Add the baskets and value the result at the year's ordinary BC credit rate. Do not copy Ontario's separate medical limits into BC. Special expense ceilings still need the applicable federal/BC rule and actual-year evidence.
8. **Student interest, tuition and transfers.** Use eligible government student-loan interest and the federal qualifying-year/carryforward rules; ordinary bank refinancing is not automatically eligible. BC still has current eligible tuition. Only the education-credit accrual ended in 2019. Use [BC(S11)](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-s11/5010-s11-25e.pdf): verify the assessment balance, current tuition from federal Schedule 11 after its Canada training credit adjustment, own-use calculation, designated current-year transfer and closing carryforward. The actual 2025 form uses prior unused amounts first, then current tuition; transferable current tuition is at most $5,000 less required current-year own use, floored at zero. Prior carried-forward amounts cannot transfer. The student signs the designation on the tuition certificate. A spouse's relevant claim can preclude a parent/grandparent transfer. For a prior-year non-BC resident use the applicable federal unused balance under the actual form/BC Act s. 4.62(3); s. 4.62(4) also converts credit-value balances when the appropriate rate changes. Distinguish a dollar credit value from a tuition base: do not both revalue a base and multiply it again. Use [BC(S2)](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-s2/5010-s2-25e.pdf) for unused age, pension, disability and designated tuition from a spouse, using their actual tax/own credits and provincial-residence conditions. Never copy all their available bases directly to the claimant.
9. **Donations and dividends.** Reconcile eligible gifts with federal Schedule 9 and prior claims. Split donations into the first $200 at the year's lowest rate, the amount above $200 matching taxable income above the year's top threshold at 20.5%, and the remaining excess at 16.8%, using the actual worksheet. Do not multiply all gifts by 5.6%. The farmers' additional credit is 25% of an otherwise qualifying agricultural-product gift by an eligible farmer/spouse to an eligible recipient, also claimed as a donation; obtain the actual recipient/product, farming-year and carryforward evidence (BC Act s. 20.1). Dividends use the **taxable grossed-up** eligible/other-than-eligible amounts, respectively 12%/1.96% in the published 2025/2026 guidance; do not apply the rates to the cash received or treat the federal dividend credit as the provincial input.

### Minimum tax, foreign credit and final split-income check

**AMT and carryover are separate.** Complete the federal T691/actual federal return first. Under BC Act ss. 4.68 and 4.8 the factor is BC's appropriate percentage divided by the federal **appropriate percentage**, rounded to the nearest .001. For 2025, 5.06/14.5 rounds to .349; actual BC428 line 66 uses federal line 40427 x 34.9%, and line 69 uses **T691 Part 7 line 14 x 34.9%**. For 2026, 5.6/14 = .400, matching the published 40%. Do not divide by the federal 20.5% AMT rate, copy Ontario's different bridge, or apply 40% to ordinary federal income tax. A carryover is limited by available BC tax in the prescribed order; it cannot make line 68 negative. Use actual-year federal outputs, special retroactive CPP/QPP or lump-sum adjustments where applicable, and T2203 allocation for multiple jurisdictions. If the required federal calculation is missing, keep the affected result unresolved rather than entering zero. The 2026 ratio is confirmed; final 2026 printed field references are not.

**Foreign non-business credit.** Complete federal T2209 first, then [T2036](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2036/t2036-25e.pdf). Broadly the BC credit is the lesser of eligible foreign non-business tax remaining after the federal credit and the BC net-foreign-income/net-income share of BC tax otherwise payable; it cannot exceed that BC tax. Use separate country calculations where required (the actual 2025 form requires them when total foreign non-business tax exceeds $200), the actual net-income adjustments, treaty/source qualifications and part-year or allocation notes. For BC, otherwise-payable tax **excludes the BC additional tax for minimum-tax purposes** as well as the provincial foreign credit itself. Under actual 2025 T2036's BC AMT note, line 2 still uses T2209 line 3; do not substitute Ontario's special-credit apportionment or its lines 70/72 recipe. Foreign excess alone is not an entitlement. In a T2203 case the provincial foreign credit belongs only to the province of residence under the form's conditions. Sources: BC Act s. 4.71 and both actual T2036 pages.

**Mandatory final TOSI comparison.** [Actual 2025 T1206](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1206/t1206-25e.pdf), Part 3 and Chart C, uses BC's 20.5% high rate, 5.06% low rate, 12%/1.96% dividend rates, BC428 line 71 foreign credit, and **BC428 line 91** as the ordinary-tax comparison. Establish actual split-income classification and exclusions; use the TOSI-adjusted net/taxable income and credit-transfer inputs instructed by that form. Put the computed provincial split-income amount on BC428 line 62, complete BC428, then compare T1206 line 50 with ordinary BC428 line 91 at line 51. **The greater goes to T1206 line 52 and T1 line 42800.** For BC, unlike Ontario, it is not an intermediate line before a health premium. Multiple-jurisdiction cases use T1206 Part 4 instead of Part 3. For 2026 obtain the correct-year T1206/instructions and use enacted rates; do not reuse 2025's low rate or pretend this paragraph is a complete TOSI classification engine. Missing T1206 evidence prevents a final TOSI result.

### Political, logging and investment credits

**Political contributions:** obtain eligible cash/payment receipts for registered BC parties, constituency associations or candidates, not federal political contributions or a generic donation. BC Act s. 4.722 gives 75% of the first $100; $75 plus 50% of excess over $100 up to $550; then $300 plus exactly 33 1/3% of excess over $550, capped at $500. The credit is non-refundable with no unused-credit carryforward. Preserve an edition difference: the actual 2025 worksheet prints **33.33%** and says enter $500 above $1,150. At exactly $1,150 the printed decimal yields $499.98 whereas the statutory fraction yields $500.00. Identify the source/form/software used and resolve that cents difference for an actual filing; do not claim the two instructions are mathematically identical or silently certify an unavailable 2026 worksheet.

**Logging:** BC Act **s. 19.1**, not the old supplementary-credit s. 4.72, allows one-third of BC logging tax payable **and paid**. Use the actual FIN 542S or FIN 542P evidence and the applicable-year credit on BC428 line 81, bounded by the tax at that point. An unpaid assessment or logging revenue is not itself the credit base. This establishes the rate, not an independent logging-tax assessment engine.

**Employee investments:** use ESOP 20 and EVCC 30 certificates, actual eligible purchase dates, amounts previously claimed and any valid first-60-days election. Actual 2025 BC428 caps their combined deduction at $2,000 on line 88 and requires the certificate numbers/amounts. CRA permits first-60-days 2026 certificates to be allocated to 2025/2026 under its instructions; record the split so it is not claimed twice. Do not substitute the different refundable venture-capital program on BC479.

**Mining flow-through:** current BC Act s. 4.721 and [BC's current guidance](https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/mining-flow-through) support 20% of qualifying BC flow-through mining expenditures actually renounced to an eligible individual (not a corporation, trust or estate), subject to actual T101/T5013 amounts, qualifying exploration, reductions and available tax. Use [T1231](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1231/t1231-25e.pdf), track unused credit, 10-year carryforward/3-year carryback and the application deadline within one year after the relevant filing-due date, even if carrying forward. The actual 2025 form's expenditure wording includes a before-1-January-2026 boundary; do not convert that old-edition wording into an expiry of the current statute, which does not contain that upper date. Current BC guidance addresses Budget 2026's renunciation reductions effective 4 August 2023. Obtain the applicable-year form and corrected renunciation data before finalizing a 2026 claim. Refundable mining exploration on BC479 is a separate program.

### Renter's refundable-credit workpaper

Sources: BC Act ss. 8/8.3, [current BC renter guidance](https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/renters-tax-credit), [actual 2025 BC479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-tc/5010-tc-25e.pdf) and CRA BC information. Apply all steps:

1. Confirm BC residence on 31 December and age 19 or older, a spouse/common-law partner or parent of a child. Establish at least **six one-month periods** of eligible BC rental occupancy in the year. They need not be consecutive or at the same address. Rent may have been paid on the tenant's behalf. Record actual rental address, rent for the unit, months and landlord/payee for every eligible unit; do not inflate the months with excluded accommodation.
2. Test actual eligible-unit/tenant conditions. Exclude non-arm's-length payments, capital leases/rent-to-own, campsite/moorage/manufactured-home pad rent, and employer-paid accommodation not included in taxable income. Check ownership/homeowner-grant and owner-occupied housing-co-op restrictions under the guidance. Do not claim for a deceased person, an exempt foreign-government employee within the statutory exclusion, or a person confined at year end whose confinement total exceeds six months. A non-resident or bankruptcy case needs the statutory/CRA special rules; the actual 2025 guidance excludes pre-bankruptcy/in-bankruptcy returns and tests occupancy across the calendar year.
3. Establish spouse/common-law status and collect both incomes even if the other person is not an eligible tenant. Only one credit for a cohabiting couple, including spouses living separately for work or medical care where the relationship remains intact. Independent unrelated roommates may each qualify; do not divide $400 between all occupants as if they were a couple. Resolve an actual relationship breakdown using the applicable spouse definition.
4. Prepare each person's adjusted income separately. Actual 2025 BC479 starts with line 23600 **including a negative amount**, adds line 21300 UCCB repayment and RDSP repayment included in 23200, subtracts UCCB 11700 and RDSP income 12500, then floors each person's result at zero before adding the two. BC Act s. 8.3(1) also excludes specified deemed gains under federal ss. 40(3.21)/79; test those special facts rather than using the ordinary workpaper unchanged. If T1206 applies, follow its BC479 adjusted-net-income notes. Gross salary or ordinary taxable income is not a substitute for this family workpaper.
5. For an eligible 2026 tenant compute `max(400 - 2% * max(adjusted family income - 66189, 0), 0)`; 2025 uses $64,764. The full amount applies through the threshold and it is nil at $86,189 for 2026/$84,764 for 2025. It is not limited to the amount of income tax or computed as a percentage of rent. On actual 2025 BC479, eligible months go to 60575 and the credit to 60576; line 45's total goes to **T1 line 47900**, separate from BC428's 42800.

### Accessibility-renovation refundable-credit workpaper

Sources: [current BC Act Part 11, ss. 141–148](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_11), [actual BC(S12)](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-s12/5010-s12-25e.pdf) and CRA BC information. The credit is 10% of up to $10,000 qualifying net expenses, maximum $1,000, without an income phaseout. Apply eligibility before the formula:

- The claimant must be an eligible BC resident: a senior age 65 or older, a person meeting the federal disability entitlement (including the relevant exception where care claims prevent the actual disability deduction), or a qualifying relation. Establish a BC qualifying principal residence and shared occupancy where required. The statute allows a residence reasonably expected to become the qualifying principal residence within **24 months after the end of the taxation year**; this is not a general credit for any property the family owns.
- Each improvement must be enduring and integral to the residence/land, or an eligible modular/removable equivalent, and improve access, mobility, function or safety for the qualifying individual. Obtain the purpose and itemized work, not just a hardware-store description. Examples include eligible ramps, grab bars, accessible doors/counters and bath/shower adaptations. Exclude routine repairs/maintenance, ordinary aesthetic/value improvements, independently usable property/appliances, entertainment equipment, financing, business/property-income expenditures and non-arm's-length work unless the supplier meets the GST-registration exception. Materials, permits and equipment hire may qualify; the owner's unpaid labour does not create an expense.
- Record the actual contract/sales-slip date, supplier/contractor, GST/HST number where applicable, description, amount including tax and residence address on BC(S12). Establish timing under the paid/payable and instalment rules; the work must start within a reasonable time. Subtract related government assistance received/receivable, qualifying forgivable loans and amounts claimed by other eligible people. Do not multiply the gross project bill by 10%.
- Apply the $10,000 shared expenditure ceiling per qualifying residence and the combined spouse ceiling, including multiple residences occupied in the year. The spouse limit has actual medical-separation and 90-day relationship-breakdown exceptions; it is not a separate $10,000 automatically for every family member. Coordinate claims and retain a written allocation. On actual 2025 BC(S12) subtract assistance, cap line 3, subtract other claimants at line 4, and transfer line 5 to BC479 **60480**; its 10% result is BC479 line 14.
- Part-year residence, bankruptcy and death need ss. 143–145: attribute expenses to the relevant resident period/return, keep the calendar-year cap across bankruptcy returns, and apply the specific senior/would-have-turned-65 death rules for the claimant or qualifying relation. Do not duplicate the annual cap or automatically reject every death-year claim. **Section 146(2) expressly permits an otherwise eligible expense in both the BC medical and BC renovation credits.** This exception does not authorize two people to claim the same expense twice within a single program or ignore assistance.
- Attach BC(S12) to a paper return and retain receipts; do not send the receipts with the schedule unless requested. Complete the other BC479 credits and transfer its total to T1 47900. The actual 2025 BC(S12)/BC479 fields are an edition-specific bridge, not a claim to have verified final 2026 field numbering.

### Other refundable BC479 jobs

Preserve these screens when preparing BC479. The actual 2025 form's line 45 total goes to T1 47900 even where credits exceed tax. For 2026 obtain the applicable form/certificates and current program conditions, rather than assume every 2025 amount or closing date remains unchanged.

|Program|Actual 2025 execution and evidence, separate from a full specialized engine|
|---|---|
|Sales tax credit|Test BC year-end residence, age 19/parent/spouse and death/exemption/confinement/bankruptcy exclusions. Use the BC479 family-income workpaper, $75 own amount plus $75 for an eligible BC spouse, and 2% reduction over $15,000 if single/$18,000 if partnered under the form. Obtain the spouse's residence/status even when not claiming their extra amount. Actual published zero thresholds differ for eligible-BC-spouse, ineligible-spouse and single cases; do not grant $150 to every couple.|
|Venture capital|Use SBVC 10 certificates, investment dates, unused credits and prior claims. The actual 2025 annual maximum is $300,000 aggregate, with a $120,000 sublimit on pre-4-March-2025 investments; follow BC479 lines 17–24 and the first-60-days election. Do not apply the ESOP/EVCC $2,000 cap to this distinct refundable program.|
|Mining exploration|Obtain eligible expenditures/residence and actual T88; a partnership allocation uses T1249. CRA's 2025 information states 20%, or up to 30% for prescribed mountain-pine-beetle areas. Distinguish this from non-refundable T1231 flow-through. Use the actual form for qualifying geography/expenditures rather than labeling every mining payment eligible.|
|Clean buildings|Require the ministry's retrofit certification and completed T1356, not the certificate's estimated amount alone. Actual 2025 guidance gives 5% of qualifying expenditures after assistance, the year-following-completion claim, expenditure/payment, completion, certification and 18-month filing deadlines. Obtain those exact dates and actual-year authority before a claim; a general home renovation is not automatically this program. BC479 has separate own and partnership fields.|
|Training and ship repair/building|Screen for the eligible apprentice, program, completion dates, enhanced-credit status and, for an employer, actual eligible BC wages/business/residence. Use actual T1014 (individual), T1014-1 (employer) or T1014-2 (shipbuilding/repair); 2025 BC479 lines 31–34 combine the form outputs. CRA's 2025 guidance notes the March 2025 federal grant end and continued qualifying enhanced credit; do not substitute a generic course fee or invent 2026 rates from the credit name.|

## Deadlines and filing

BC tax is filed and paid with the federal T1. There is no separate BC return.

| Item | 2025 return | 2026 return |
|---|---|---|
| Filing deadline, most individuals | 30 April 2026 | 30 April 2027 |
| Filing deadline, qualifying self-employed people and spouses/common-law partners | 15 June 2026 | 15 June 2027 |
| Ordinary balance payment deadline (including self-employed) | 30 April 2026 | 30 April 2027 |

Both columns now have published CRA support. The current [CRA business-deadline fact sheet](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html) actually states the 2027 filing/payment dates despite its older URL slug. The June extension is not universal: apply the actual tax-shelter-business restriction and death/spouse/special-return rules under [federal ITA s. 150(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html). Do not tell a business owner to pay in June. Instalments are federal and include BC tax: see `ca-fed-instalments`.

What to file:

- Form BC428, attached to the T1 (paper) or produced by the certified software for NETFILE or EFILE. The result goes on T1 line 42800.
- Form BC479 for the refundable BC credits. For the renter's credit, enter the rental address, total rent paid, months of tenancy and the landlord's name.
- Schedule BC(S2) for amounts transferred from a spouse, Schedule BC(S11) for tuition, Form T1206 for split income, Form T2036 for the provincial foreign tax credit, Form T691 for minimum tax.
- The Provincial Worksheet (Worksheet BC428) is for your records (age, caregiver, donations, dividends, political contributions); it does not need to be attached.
- Form T2203 instead of ordinary BC428 for actual multiple-jurisdiction business-income cases; complete its provincial/territorial summary. A Canada-non-resident with employment only in BC or a business permanent establishment only in BC is not automatically a T2203 case.

## Penalties and interest

BC tax is part of the T1 balance owing, so the federal penalty and interest rules apply to it.

- Late filing: 5% of the balance owing, plus 1% of the balance owing for each full month late, up to 12 months.
- Repeated late filing: 10% of the unpaid balance, plus 2% for each full month late, up to 20 months, only where the actual demand and prior-penalty conditions apply. For a 2025 return the relevant prior years are 2022, 2023 or 2024; for 2026 they are 2023, 2024 or 2025. Check the demand and assessment record under federal ITA s. 162(2); a second late return alone is not enough.
- Interest: CRA charges compound daily interest on unpaid tax starting the day after the due date. The rate follows the prescribed rate and can change every three months.

Source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html. Other penalties are federal and sit in `ca-fed-t1-return`.

## Cross-border points

- **Moving into or out of BC within Canada.** The province of residence on 31 December decides the provincial tax for the whole year (CRA 2026 rate page: "The rate is determined by your province or territory of residence on December 31"). There is no split between provinces for a mover. Check residence with `ca-tax-residency`.
- **BC resident with business income earned outside BC.** BC Act s. 4.1(5) contains the BC-share formula, with related credit/allocation restrictions in ss. 4.75 and 4.85. Use actual T2203 for business income allocated to a permanent establishment outside BC. The actual 2025 BC428MJ applies rates to the full relevant taxable base, calculates resident-only/allocated credits, additional tax and reduction, and transfers the correct provincial summary. It is **not** ordinary final BC428 multiplied by a guessed BC share. Employment performed in another province alone does not establish a second business permanent establishment.
- **Not resident in BC on 31 December but with BC income.** BC Act s. 4.1(6) taxes the applicable BC income share, and s. 4.1(7) modifies the base for Canada-non-residents. Establish the source and actual permanent establishments. A Canada-non-resident with employment only in BC or a business permanent establishment only in BC uses ordinary BC428 under CRA's instructions; multiple jurisdictions require the applicable T2203 route. Do not simply select the current country's tax form or grant every BC resident credit. See the non-resident restrictions below.
- **Foreign tax.** A provincial foreign non-business credit may remain after federal T2209, but only within the country/income-ratio/BC-tax limits on T2036 and BC Act s. 4.71. Enter the properly computed ordinary-form credit at BC428 line 71. The detailed AMT/foreign-credit workpaper above controls; no automatic credit equal to all foreign tax left over.
- **Emigrants and immigrants.** CRA's package uses residence on 31 December or the departure date; BC Act s. 1(2) deems the relevant last day for a person ceasing Canadian residence. Apply actual resident/non-resident income periods and the corresponding provincial reductions when federal basic/age/spouse/dependant claims are reduced. BC Act s. 4.76 limits applicable credits; do not multiply every income item or every credit by days/365. Departure tax and residence evidence stay in `ca-tax-residency` and `leaving-canada-departure-tax`. Death, optional returns and bankruptcy likewise need the actual statutory/CRA branch and annual limits, not a fictional full-year residence.

### Non-resident and special-return credit restrictions

BC Act ss. 4.73–4.77 distinguish trusts, bankruptcy, allocated income, part-year residents and full-year Canada-non-residents. For a full-year non-resident, s. 4.77 restricts listed personal, reduction, age, medical, impairment-transfer and family-transfer credits unless all or substantially all income is included in Canadian taxable income. Obtain the actual Canadian/world income and the applicable federal/CRA eligibility calculation. Separately test resident-only pension/adoption/volunteer/dividend provisions; an ordinary BC428 route does not erase those requirements. Bankruptcy credits must be attributable to the relevant return and cannot exceed their calendar-year maximum across returns. T2203 and T1206 have their own adjusted inputs/allocations. If those facts or forms are absent, report an incomplete conditional workpaper, not an ordinary resident maximum as a final answer.

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

## Additional synthetic checks of the missing branches

These are fictional, otherwise eligible component workpapers. They do not assert that TOSI, a disability transfer, a renovation or another credit applies without its legal eligibility evidence. All 2026 numbered-form examples remain estimates pending the final annual forms.

### Caregiver overlap, including a spouse

For an otherwise qualifying impaired adult spouse in 2026, net income $10,000 leaves a $2,449 spouse base and $3,335 caregiver base, worth $186.76 as a caregiver credit. With spouse income zero, the spouse base is $11,317 and the caregiver base is zero. A caregiver maximum cannot simply be stacked on either spouse amount.

```oa-check
name: BC 2026 caregiver subtracts same-person spouse base
inputs:
  dependant_income: 10000
  second_income: 0
steps:
  - spouse_base: min(max(12449 - dependant_income, 0), 11317)
  - preliminary: min(max(25356 - dependant_income, 0), 5784)
  - caregiver_base: max(preliminary - spouse_base, 0)
  - caregiver_credit: round(caregiver_base * 0.056, 2)
  - second_spouse: min(max(12449 - second_income, 0), 11317)
  - second_caregiver: max(min(max(25356 - second_income, 0), 5784) - second_spouse, 0)
expected:
  spouse_base: 2449
  preliminary: 5784
  caregiver_base: 3335
  caregiver_credit: 186.76
  second_spouse: 11317
  second_caregiver: 0
```

### Medical baskets and a child's disability supplement

Assume all expenses/relationships/periods qualify and none were reimbursed or reused. With claimant net income $100,000 and self-family medical expenses $5,000, the allowed first basket is $2,252. Another eligible adult dependant has net income $30,000 and medical expenses $20,000, giving $19,100 without an Ontario per-person cap. Their combined base is $21,352 and the 2026 credit $1,195.71. Separately, an eligible disabled child with $5,000 of relevant care claims has supplement $4,141 and total personal disability base $14,054; this is not an automatic transferable amount.

```oa-check
name: BC 2026 separate medical baskets and child supplement
inputs:
  own_income: 100000
  own_medical: 5000
  adult_income: 30000
  adult_medical: 20000
  care_claims: 5000
steps:
  - own_threshold: min(own_income * 0.03, 2748)
  - own_allowed: max(own_medical - own_threshold, 0)
  - adult_threshold: min(adult_income * 0.03, 2748)
  - adult_allowed: max(adult_medical - adult_threshold, 0)
  - total_medical: own_allowed + adult_allowed
  - medical_credit: round(total_medical * 0.056, 2)
  - supplement: max(5783 - max(care_claims - 3358, 0), 0)
  - child_disability_base: 9913 + supplement
expected:
  own_threshold: 2748
  own_allowed: 2252
  adult_threshold: 900
  adult_allowed: 19100
  total_medical: 21352
  medical_credit: 1195.71
  supplement: 4141
  child_disability_base: 14054
```

### Top-band donation split

For 2026 taxable income $270,000 and eligible gifts $10,000 actually claimed federally, $200 attracts 5.6%; $4,455 attracts 20.5%; the remaining $5,345 attracts 16.8%. Using rounded worksheet components gives $1,822.44. This is a donation credit alone, not a complete tax return.

```oa-check
name: BC 2026 donations span all three credit rates
inputs:
  taxable_income: 270000
  gifts: 10000
steps:
  - first_base: min(gifts, 200)
  - top_base: min(max(gifts - 200, 0), max(taxable_income - 265545, 0))
  - middle_base: max(gifts - first_base - top_base, 0)
  - first_credit: round(first_base * 0.056, 2)
  - top_credit: round(top_base * 0.205, 2)
  - middle_credit: round(middle_base * 0.168, 2)
  - gift_credit: first_credit + top_credit + middle_credit
expected:
  first_base: 200
  top_base: 4455
  middle_base: 5345
  first_credit: 11.20
  top_credit: 913.28
  middle_credit: 897.96
  gift_credit: 1822.44
```

### Renter family adjustment and renovation assistance

Assume an otherwise eligible couple and ordinary BC479 adjustments: one person's net income is minus $1,000 plus a $3,000 RDSP repayment, giving $2,000; the other has $76,189 net income less $2,000 RDSP income, giving $74,189. Family adjusted income $76,189 yields a 2026 renter credit $200. At the full and zero boundaries the credit is $400 and $0. Separately, qualifying renovation expenses $12,000 less $3,000 assistance leave $9,000; if another eligible resident claims $4,000 of that amount, this claimant's $5,000 base yields $500 and the other's $400, $900 total. Assume the shared cap and actual schedules permit that allocation; it is not a duplicated $900 each.

```oa-check
name: BC 2026 family rent adjustments and shared renovation
inputs:
  first_net: -1000
  first_rdsp_repayment: 3000
  second_net: 76189
  second_rdsp_income: 2000
  renovation: 12000
  assistance: 3000
  other_claim: 4000
steps:
  - first_adjusted: max(first_net + first_rdsp_repayment, 0)
  - second_adjusted: max(second_net - second_rdsp_income, 0)
  - family_adjusted: first_adjusted + second_adjusted
  - renter_credit: max(400 - round(max(family_adjusted - 66189, 0) * 0.02, 2), 0)
  - rent_at_threshold: max(400 - max(66189 - 66189, 0) * 0.02, 0)
  - rent_at_zero_boundary: max(400 - max(86189 - 66189, 0) * 0.02, 0)
  - net_renovation: min(max(renovation - assistance, 0), 10000)
  - own_base: max(net_renovation - other_claim, 0)
  - own_renovation_credit: round(own_base * 0.10, 2)
  - other_renovation_credit: round(other_claim * 0.10, 2)
expected:
  first_adjusted: 2000
  second_adjusted: 74189
  family_adjusted: 76189
  renter_credit: 200
  rent_at_threshold: 400
  rent_at_zero_boundary: 0
  net_renovation: 9000
  own_base: 5000
  own_renovation_credit: 500
  other_renovation_credit: 400
```

### 2025 AMT bridge, foreign limit and final TOSI floor

These are supplied, already completed form components, not a determination that the taxpayer is subject to AMT/TOSI or entitled to a carryover. Suppose actual 2025 BC tax before these credits is $6,000 and the valid federal 40427 amount is $1,000: the BC carryover component is $349. A separate valid T691 Part 7 line 14 amount $2,000 creates $698 additional BC tax. Suppose T2036's remaining eligible foreign tax is $700, but its properly determined BC otherwise-payable income-ratio limit is $500: only $500 is deductible. Finally, if the completed ordinary BC428 line 91 is $1,200 and T1206 line 50 is $1,600, T1 42800 is $1,600, not $1,200. A second case with line 50 $900 retains $1,200. The same 2026 AMT component on $2,000 would use the confirmed .400 ratio, subject to actual-year federal output and filing fields.

```oa-check
name: BC dated AMT interfaces foreign cap and TOSI final comparison
inputs:
  ordinary_before_credits: 6000
  federal_40427: 1000
  federal_t691_part7_line14: 2000
  eligible_foreign_remainder: 700
  supplied_provincial_ratio_limit: 500
  supplied_bc428_line91: 1200
  supplied_t1206_line50: 1600
  second_t1206_line50: 900
steps:
  - carryover_2025: round(federal_40427 * 0.349, 2)
  - after_carryover: max(ordinary_before_credits - carryover_2025, 0)
  - additional_2025: round(federal_t691_part7_line14 * 0.349, 2)
  - provincial_foreign: min(eligible_foreign_remainder, supplied_provincial_ratio_limit)
  - final_42800: max(supplied_bc428_line91, supplied_t1206_line50)
  - second_final_42800: max(supplied_bc428_line91, second_t1206_line50)
  - additional_2026_component: round(federal_t691_part7_line14 * 0.400, 2)
expected:
  carryover_2025: 349
  after_carryover: 5651
  additional_2025: 698
  provincial_foreign: 500
  final_42800: 1600
  second_final_42800: 1200
  additional_2026_component: 800
```

## Ask the client first

1. Where did you live on 31 December, and did you enter or leave Canada, die or become bankrupt during the year? Obtain dates and the actual residence/source record. A Canada-non-resident with BC-only employment/business may still use BC428; another Canadian province or multi-jurisdiction business may require another route.
2. Which year is the return for, 2025 or 2026? The lowest rate, the credit rate and the tax reduction changed between them.
3. Your net income (T1 line 23600) and taxable income (line 26000), and your spouse's or common-law partner's net income.
4. Did you earn business income through a permanent establishment outside BC, or have BC business/employment income while living elsewhere? Identify actual establishments and jurisdictions before selecting BC428 or T2203. Do not infer a business permanent establishment merely from travel or employment in another province.
5. Obtain dependant relationships, age, infirmity/support/residence and incomes; same-person spouse/dependant claims; T2201 and actual disability/care amounts; eligible pension and adoption/volunteer evidence; medical dates/reimbursements; tuition assessment/certificates and unused-transfer calculations; eligible donation/political receipts and taxable dividend amounts. Are T691, T1206 or T2036 required, and are their actual-year results available?
6. Did you rent/occupy eligible BC units for six one-month periods, or incur qualifying accessibility-renovation expenses? Obtain addresses, rent/months/payee, spouse's adjusted-income workpaper, owner/related-party exclusions, invoices, disability/senior/occupancy evidence, assistance and shared claims. Screen separately for the other BC479 programs and their forms/certificates.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act (BC), RSBC 1996, c. 215, operative ss. 1–4.8x, 8.3, 19.1 and 20.1 (consolidation current to 10 November 2026; bounded personal-tax provisions) | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_01 | 2026-11-14 |
| Government of BC, Personal income tax rates (updated 17 April 2026), read for 2026 and 2025 brackets, indexation, minimum tax; actual indexed official body read after normal direct connection failure | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates | 2026-11-14 |
| Government of BC, B.C. basic personal income tax credits (updated 20 April 2026), read for 2026 and 2025 credit amounts, tax reduction, dividend credit; actual indexed official body read after normal direct connection failure | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic | 2026-11-14 |
| Government of BC, Political contribution personal income tax credit, read for the credit bands and $500 cap; actual indexed official body read after normal direct connection failure | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/political-contribution | 2026-11-14 |
| Government of BC, B.C. renter's tax credit, read for eligibility and 2025 and 2026 thresholds; actual indexed official body read after normal direct connection failure | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/renters-tax-credit | 2026-11-14 |
| Government of BC, Home renovation tax credit for seniors and persons with disabilities, historical guidance read for eligibility, 10% rate and $10,000 cap; current check uses Act Part 11 and federal forms below | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/seniors-renovation | 2026-11-08 |
| Government of BC, Climate action tax credit, read for the end of the program and last-year amounts; actual indexed official body read after normal direct connection failure | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/climate-action | 2026-11-14 |
| CRA, Form BC428 British Columbia Tax 2025 (5010-C), Part A, Part B and Part C, lines 1 to 91 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-c/5010-c-25e.pdf | 2026-11-14 |
| CRA, British Columbia Tax Information 2025 (5010-PC), read for who completes BC428 and the BC479 credits | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/british-columbia/5010-pc.html | 2026-11-14 |
| CRA, British Columbia 2025 income tax package, read for the T2203 rule | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/british-columbia.html | 2026-11-14 |
| CRA, Current year tax rates and income brackets (2026), read for the BC 2026 brackets and residence rule | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-14 |
| CRA, Last year tax rates and income brackets (2025), read for the BC 2025 brackets | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html | 2026-11-14 |
| CRA, Important dates for individuals, read for 2025 filing and payment dates | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-14 |
| CRA, Interest and penalties on late taxes, read for late-filing penalties and interest | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html | 2026-11-14 |
| BC Act Part 11, ss. 141–148: eligibility, expenses, assistance, shared limits, part-year, bankruptcy, death and medical exception | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_11 | 2026-11-14 |
| CRA actual 2025 Worksheet BC428, all three pages: age, caregiver, disability, medical, donations, dividends, political | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-d/5010-d-25e.pdf | 2026-11-14 |
| CRA actual 2025 BC479, all three pages: family income, refundables, rent declaration and 47900 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-tc/5010-tc-25e.pdf | 2026-11-14 |
| CRA actual 2025 BC(S12), complete renovation expense/assistance/sharing workpaper | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-s12/5010-s12-25e.pdf | 2026-11-14 |
| CRA actual 2025 BC(S2), unused spouse transfer/own-use calculation | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-s2/5010-s2-25e.pdf | 2026-11-14 |
| CRA actual 2025 BC(S11), both pages: tuition, own use, transfer and carryforward | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-s11/5010-s11-25e.pdf | 2026-11-14 |
| CRA actual 2025 T1206, BC adjusted-income notes, Chart C and Part 3 final greater-of; Part 4 route | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1206/t1206-25e.pdf | 2026-11-14 |
| CRA actual 2025 T2036, both pages including BC AMT/otherwise-payable notes | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2036/t2036-25e.pdf | 2026-11-14 |
| CRA actual 2025 T2203, opening instructions and BC428MJ/summary interface only | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2203/t2203-25e.pdf | 2026-11-14 |
| CRA BC428 catalogue, actual offered annual edition 2025; no final 2026 edition obtained | https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5010-c.html | 2026-11-14 |
| BC current flow-through guidance, 20%, renunciation, application and carry periods | https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/mining-flow-through | 2026-11-14 |
| CRA actual 2025 T1231, complete two-page dated flow-through form | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1231/t1231-25e.pdf | 2026-11-14 |
| CRA current business deadline fact sheet: actual 2027 body despite older URL slug | https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html | 2026-11-14 |
| Federal ITA s. 150(1), ordinary, self-employed/spouse, tax-shelter and death filing branches | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Federal ITA s. 162(1)–(2), unpaid balance/full-month/demand/prior-penalty conditions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html | 2026-11-14 |
| Federal ITA s. 118.2(1) B(d)/E(d), ordinary 12-month and eligible death 24-month medical period, including death day and no prior/other claim reuse | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.2.html | 2026-11-14 |

Not yet confirmed: final 2026 BC428/BC479 and related worksheets or their printed field numbers; reconciliation of the statutory whole-dollar/actual-form cent bracket constants and the political fraction/printed-decimal difference for a real filing; all client-specific 2026 specialized BC479/logging/mining form entitlements and certificates beyond the bounded rates/interfaces above; special medical expense ceilings not established here; application of the section 87 Indian Act exemption on a particular BC428; any alleged blanket renter/home-office prohibition (no supporting official rule was found). Confirm actual eligible-unit and federal business-use facts separately. These are specific limits, not permission to replace the substantive ordinary calculation or assume missing inputs. The published 2027 ordinary dates, statutory logging one-third and current mining flow-through 20% are now established and are no longer listed as wholly unknown.
